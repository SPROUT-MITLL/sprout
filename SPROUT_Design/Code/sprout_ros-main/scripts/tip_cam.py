#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class MjpegIpCamera(Node):
    def __init__(self):
        super().__init__('mjpeg_ip_camera')
        self.declare_parameter('stream_url', 'http://192.168.4.1')
        stream_url = self.get_parameter('stream_url').get_parameter_value().string_value

        self.cap = cv2.VideoCapture(stream_url)
        if not self.cap.isOpened():
            self.get_logger().error(f'Could not open stream: {stream_url}')
            return

        self.publisher_ = self.create_publisher(Image, 'camera/image_raw', 10)
        self.bridge = CvBridge()
        self.timer = self.create_timer(1.0 / 30.0, self.timer_callback)  # 30 Hz

    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
            msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
            self.publisher_.publish(msg)
        else:
            self.get_logger().warn('Failed to read frame from camera.')

def main(args=None):
    rclpy.init(args=args)
    node = MjpegIpCamera()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()