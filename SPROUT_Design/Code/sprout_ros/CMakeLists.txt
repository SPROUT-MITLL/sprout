cmake_minimum_required(VERSION 3.10)
project(sprout_ros)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)

find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Command.msg"
  "msg/State.msg"
  "srv/PressureSet.srv"
)

# Install Python scripts
install(
  PROGRAMS
    scripts/joy_vine_interface.py
    scripts/screen.py
    scripts/fort_controller.py
    scripts/fort_vine_interface.py
    scripts/fort_scm_controller.py
  DESTINATION lib/${PROJECT_NAME}
)

# Install launch files
install(DIRECTORY
  launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

ament_package()