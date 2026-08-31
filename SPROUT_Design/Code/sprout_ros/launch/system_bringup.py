from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, TimerAction, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os

from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    # Declare launch arguments
    DeclareLaunchArgument('node_start_delay', default_value='20.0'),
    node_start_delay = LaunchConfiguration('node_start_delay')

    return LaunchDescription([

        # PS5 Controller Driver
        # Node(
        #     package='ds5_ros',
        #     executable='ds5ros_node.py',
        #     name='ps5_driver',
        #     output='screen'
        # ),
        Node(
            package='sprout_ros',
            executable='fort_scm_controller.py',
            name='fort_driver',
            output='screen'
        ),

        # Arduino Preprocessor
        # Node(
        #     package='sprout_ros',
        #     executable='joy_vine_interface.py',
        #     name='jetson_arduino',
        #     output='screen'
        # ),
        Node(
            package='sprout_ros',
            executable='fort_vine_interface.py',
            name='jetson_arduino',
            output='screen'
        ),

        # LCD Screen Display
        Node(
            package='sprout_ros',
            executable='screen.py',
            name='jetson_screen',
            output='screen'
        ),
    ])
