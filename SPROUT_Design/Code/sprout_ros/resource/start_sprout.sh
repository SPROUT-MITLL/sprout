#!/bin/bash

# Source ROS 2 base installation
source /opt/ros/humble/setup.bash

# Source your workspace
source /home/jetson/ws/install/setup.bash

# Optional: Set environment variables here if needed
# export RMW_IMPLEMENTATION=rmw_fastrtps_cpp

# Launch your robot
exec ros2 launch sprout_ros system_bringup.py