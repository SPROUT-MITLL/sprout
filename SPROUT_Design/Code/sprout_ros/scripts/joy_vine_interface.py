#!/usr/bin/env python3

import rclpy
import threading
import time
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import String
from sprout_ros.msg import State
import serial
import serial.serialutil


# Vine Robot Driver
# Author: Nathaniel Hanson
# ROS 2 Version

class VineDriver(Node):
    def __init__(self):
        super().__init__('vine_driver')
        self.serial_lock = threading.Lock()
        self.serial_port = '/dev/com/vine_arduino'
        self.baudrate = 115200
        self.ser = None
        self.serial_thread = threading.Thread(target=self._establish_serial_connection)
        self.serial_thread.daemon = True
        self.serial_thread.start()

        self.state_pub = self.create_publisher(State, '/vine_state', 1)
        self.joy_sub = self.create_subscription(Joy, '/joy', self.process_commands, 2)
        self.create_timer(0.01, self.read_serial)

    def _establish_serial_connection(self):
        delay = 1
        while rclpy.ok():
            try:
                self.get_logger().info(f'Trying to connect to {self.serial_port}...')
                self.ser = serial.Serial(
                    self.serial_port,
                    self.baudrate,
                    timeout=0.5,
                )
                self.get_logger().info('Serial connection established')
                return
            except serial.serialutil.SerialException as e:
                self.get_logger().warn(f"Serial connection failed: {e}")
                time.sleep(delay)
                delay = min(delay * 2, 30)  # exponential backoff, max 30 sec

    def process_commands(self, msg: Joy) -> None:
        '''
        Map commands to a compact string and send over serial.
        '''
        if not self.ser or not self.ser.is_open:
            self.get_logger().warn("Serial port not available. Skipping command.")
            return

        to_send = f"SET,{msg.buttons[5]},{msg.buttons[14]},{msg.buttons[13]},{msg.buttons[2]},{msg.buttons[0]},{msg.buttons[3]},{msg.buttons[1]},{msg.axes[1]},{msg.axes[2]}"
        self.get_logger().debug(f"SENDING: {to_send}")
        try:
            with self.serial_lock:
                self.ser.write((to_send + '\n').encode())
        except Exception as e:
            self.get_logger().warn(f"Serial write error: {e}")
            self._restart_serial_connection()

    def read_serial(self):
        if not self.ser or not self.ser.is_open:
            return

        try:
            with self.serial_lock:
                line = self.ser.readline().decode(errors='ignore').strip()

            if not line:
                return  # Skip empty lines

            self.get_logger().debug(f"Received: {line}")

            if line.startswith("STATE"):
                parts = line.split(",")[1:]  # skip 'STATE'
                if len(parts) != 10:
                    self.get_logger().warn(f"Unexpected STATE format: {line}")
                    return

                msg = State()
                msg.cp_a = float(parts[0])
                msg.cp_s = float(parts[1])
                msg.a1_a = float(parts[2])
                msg.a1_s = float(parts[3])
                msg.a2_a = float(parts[4])
                msg.a2_s = float(parts[5])
                msg.a3_a = float(parts[6])
                msg.a3_s = float(parts[7])
                msg.d_s = float(parts[8])
                msg.d_c = float(parts[9])
                self.state_pub.publish(msg)
            else:
                self.get_logger().warn(f"Invalid vine state received: {line}")

        except Exception as e:
            self.get_logger().warn(f"Serial read error: {e}")
            self._restart_serial_connection()

    def _restart_serial_connection(self):
        try:
            if self.ser:
                self.ser.close()
        except Exception:
            pass
        self.ser = None
        self.serial_thread = threading.Thread(target=self._establish_serial_connection)
        self.serial_thread.daemon = True
        self.serial_thread.start()


def main(args=None):
    rclpy.init(args=args)
    node = VineDriver()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.get_logger().info('Shutting down VineDriver node')
        if node.ser and node.ser.is_open:
            node.ser.close()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()