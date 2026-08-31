#!/usr/bin/env python3

import rclpy
import time
from rclpy.node import Node
from sprout_ros.msg import State
import threading
import random
import queue
import smbus2 as smbus

class I2CLCD:
    def __init__(self, addr=0x27, bus_id=1, backlight=True):
        self.addr = addr
        self.backlight = 1 if backlight else 0
        self.bus = smbus.SMBus(bus_id)
        self._init_display()

    def _i2c_delay(self):
        import time
        time.sleep(0.002)

    def write_word(self, data):
        temp = data
        if self.backlight:
            temp |= 0x08
        else:
            temp &= 0xF7
        self.bus.write_byte(self.addr, temp)

    def send_command(self, comm):
        buf = comm & 0xF0
        buf |= 0x04
        self.write_word(buf)
        self._i2c_delay()
        buf &= 0xFB
        self.write_word(buf)

        buf = (comm & 0x0F) << 4
        buf |= 0x04
        self.write_word(buf)
        self._i2c_delay()
        buf &= 0xFB
        self.write_word(buf)

    def send_data(self, data):
        buf = data & 0xF0
        buf |= 0x05
        self.write_word(buf)
        self._i2c_delay()
        buf &= 0xFB
        self.write_word(buf)

        buf = (data & 0x0F) << 4
        buf |= 0x05
        self.write_word(buf)
        self._i2c_delay()
        buf &= 0xFB
        self.write_word(buf)

    def _init_display(self):
        try:
            self.send_command(0x33)
            self.send_command(0x32)
            self.send_command(0x28)
            self.send_command(0x0C)
            self.send_command(0x01)
            self.bus.write_byte(self.addr, 0x08)
        except Exception as e:
            print(f"LCD init failed: {e}")
            raise

    def clear(self):
        self.send_command(0x01)

    def write(self, x, y, text):
        if x < 0: x = 0
        if x > 19: x = 19
        if y < 0: y = 0
        if y > 3: y = 3

        row_offsets = [0x00, 0x40, 0x14, 0x54]
        addr = 0x80 + row_offsets[y] + x
        self.send_command(addr)

        for ch in text:
            self.send_data(ord(ch))


class VineScreen(Node):
    def __init__(self):
        super().__init__('vine_screen')
        self.lcd = I2CLCD(addr=0x27, bus_id=1, backlight=True)
        self.latest_msg = None
        self.sub = self.create_subscription(State, '/vine_state', self.draw_state, 1)
        self.lcd.write(0, 0, "Waiting for data...")
        self.get_logger().info("VineScreen node initialized")

    def safe_lcd_write(self, x, y, text):
        text = text[:20].ljust(20)  # Ensure exactly 20 characters
        self.lcd.write(x, y, text)
        time.sleep(0.01)  # Allow LCD hardware to settle

    def draw_state(self, msg):
        if msg is None:
            return
        status = 'Okay'  # or derive from msg if needed
        line0 = f"Stat:{status} Main:{msg.cp_s:.2f}"
        line1 = f"Act #1: {msg.a1_s:.2f}"
        line2 = f"Act #2: {msg.a2_s:.2f}"
        line3 = f"Act #3: {msg.a3_s:.2f}"

        self.get_logger().debug(f"LCD Update:\n{line0}\n{line1}\n{line2}\n{line3}")

        self.safe_lcd_write(0, 0, line0)
        self.safe_lcd_write(0, 1, line1)
        self.safe_lcd_write(0, 2, line2)
        self.safe_lcd_write(0, 3, line3)

    def shutdown(self):
        self.lcd.clear()


def main(args=None):
    rclpy.init(args=args)
    node = VineScreen()
    executor = rclpy.executors.SingleThreadedExecutor()
    executor.add_node(node)
    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        node.get_logger().info("Shutting down VineScreen node")
        node.shutdown()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
