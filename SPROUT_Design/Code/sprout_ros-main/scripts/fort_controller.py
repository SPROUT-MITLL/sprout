#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import Bool
import hid
import struct
import time

FORT_VID = 0x2A99
FORT_PID = 0xC011
FORT_INTERFACE = 2

RECONNECT_PERIOD_SEC = 1.0

class FortWRCJoyNode(Node):
    def __init__(self):
        super().__init__('fort_wrc_joy')

        self.joy_pub = self.create_publisher(Joy, '/joy', 1)
        self.status_pub = self.create_publisher(Bool, '/joy/status', 1)

        self.dev = None
        self.connected = False
        self.last_connect_attempt = 0.0

        self.timer = self.create_timer(0.005, self.read_hid)

        # Publish initial status
        self.publish_status(False)

    def publish_status(self, state: bool):
        if self.connected == state:
            return
        self.connected = state
        msg = Bool()
        msg.data = state
        self.status_pub.publish(msg)

    def open_wrc(self):
        for d in hid.enumerate(FORT_VID, FORT_PID):
            if d.get("interface_number") == FORT_INTERFACE:
                dev = hid.Device(path=d["path"])
                dev.nonblocking = True
                self.get_logger().info("FORT WRC connected")
                self.publish_status(True)
                return dev
        return None

    def close_wrc(self, reason: str):
        if self.dev is not None:
            try:
                self.dev.close()
            except Exception:
                pass

        if self.connected:
            self.get_logger().warn(f"FORT WRC disconnected: {reason}")

        self.dev = None
        self.publish_status(False)

    def try_reconnect(self):
        now = time.monotonic()
        if now - self.last_connect_attempt < RECONNECT_PERIOD_SEC:
            return

        self.last_connect_attempt = now
        self.dev = self.open_wrc()

    def parse_input_report(self, report):
        if len(report) < 8:
            return None

        lx, ly, lz, rx, ry, rz = struct.unpack("bbbbbb", bytes(report[:6]))

        lx = -lx
        ly = -ly
        rx = -rx
        ry = -ry

        axes = [v / 127.0 for v in (lx, ly, lz, rx, ry, rz)]

        buttons_byte = (report[6] >> 4) & 0x0F
        buttons = [bool(buttons_byte & (1 << i)) for i in range(4)]

        dpad = report[6] & 0x0F
        dpad_buttons = [
            dpad == 0,
            dpad == 2,
            dpad == 4,
            dpad == 6
        ]

        buttons.extend(dpad_buttons)

        msg = Joy()
        msg.axes = axes
        msg.buttons = [int(b) for b in buttons]
        return msg

    def read_hid(self):
        if self.dev is None:
            self.try_reconnect()
            return

        try:
            report = self.dev.read(64)
        except (hid.HIDException, OSError) as e:
            self.close_wrc(str(e))
            return

        if report:
            msg = self.parse_input_report(report)
            if msg:
                self.joy_pub.publish(msg)

    def destroy_node(self):
        self.close_wrc("node shutdown")
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = FortWRCJoyNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()