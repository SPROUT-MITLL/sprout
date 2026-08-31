#!/usr/bin/env python3

import rclpy
import threading
import time
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import String
from sprout_ros.msg import State
from sprout_ros.srv import PressureSet
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
        self.last_time = 0.0
        self.throttle_rate = 0.1  # seconds between messages (10 Hz)
        self.chamber_pressure = 2.5
        self.actuator_pressure = 2.5
        self.state_pub = self.create_publisher(State, '/vine_state', 1)
        self.joy_sub = self.create_subscription(Joy, '/joy', self.process_commands, 2)
        self.create_timer(0.01, self.read_serial)
        self.srv = self.create_service(
            PressureSet,
            '/pressure_set',
            self.handle_pressure_request,
        )

    def handle_pressure_request(self, request, response):
            """
            Handle request to update the maximum chamber and actuator pressures. 
            This is triggered by changes to the values on the joystick nodes
            """
            try:
                self.chamber_pressure = request.chamber_val
                self.actuator_pressure = request.actuator_val
                response.success = True

            except Exception as e:
                response.success = False
                response.message = str(e)
                self.get_logger().error(str(e))

            return response

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
        now = time.time()
        if now - self.last_time >= self.throttle_rate:
            self.last_time = now
            to_send = f"SET,{msg.buttons[7]},{msg.buttons[2]},{msg.buttons[0]},{msg.buttons[6]},{msg.buttons[4]},{msg.buttons[1]},{msg.buttons[5]},{msg.axes[4]},{msg.axes[3]},{self.chamber_pressure},{self.actuator_pressure}"
            self.get_logger().info(f"SENDING: {to_send}")
        else:
            return
        # int rb         = (int)values[0]; pouch pressure reset
        # int dpad_down  = (int)values[1]; motor speed decrease
        # int dpad_up    = (int)values[2]; motor speed increase
        # int triangle   = (int)values[3]; increase p
        # int x          = (int)values[4]; decrease p
        # int square     = (int)values[5]; motor stop
        # int circle     = (int)values[6]; empty
        # float y_joy    = values[7] * 5.0;         // Amplify for actuator control
        # float x_joy    = values[8] * 5.0 * -1.0;  // Inverted for consistency
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
                # parts = line.split(",")[1:]  # skip 'STATE'
                parts = [float(z.strip()) for z in line.split(",")[1:]]
                if len(parts) != 12:
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
                msg.c_m = float(parts[10])
                msg.a_m = float(parts[11])
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