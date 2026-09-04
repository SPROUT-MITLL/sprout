---
layout: default
title: SPROUT ROS
parent: Software
nav_order: 2
---

# SPROUT ROS
{: .no_toc }

Source: [`SPROUT_Design/Code/sprout_ros`]({{ site.github_tree }}/SPROUT_Design/Code/sprout_ros)
{: .label .label-green }

ROS 2 stack for SPROUT. Main installation instructions live in the [Jetson Bootstrap]({{ site.baseurl }}/software/jetson-bootstrap.html) guide; this page summarizes the package layout.

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

## Package layout

The `sprout_ros` package (`ament_cmake`, ROS 2) is organized as follows:

| Path | Contents |
|---|---|
| [`arduino/vine_control`]({{ site.github_tree }}/SPROUT_Design/Code/sprout_ros/arduino/vine_control) | `vine_control_uno_rev3` Arduino sketch that runs on the Uno Rev3 and talks to the shield hardware |
| [`launch/system_bringup.py`]({{ site.github_blob }}/SPROUT_Design/Code/sprout_ros/launch/system_bringup.py) | Top-level launch file that brings up the Fort controller, Arduino interface, and LCD screen nodes |
| [`msg/`]({{ site.github_tree }}/SPROUT_Design/Code/sprout_ros/msg) | `Command.msg` and `State.msg` message definitions |
| [`scripts/`]({{ site.github_tree }}/SPROUT_Design/Code/sprout_ros/scripts) | ROS 2 node implementations (controller drivers, vine interface, display, camera) |
| [`srv/`]({{ site.github_tree }}/SPROUT_Design/Code/sprout_ros/srv) | `PressureSet.srv` service definition |
| [`resource/`]({{ site.github_tree }}/SPROUT_Design/Code/sprout_ros/resource) | systemd service unit for auto-starting the stack on boot |

## Messages and services

**`Command.msg`** — teleop command sent to the vine robot driver:

```
bool toggle_retract
bool grow_speed_inc
bool grow_speed_dec
bool chamber_inc
bool chamber_dec
bool stop_grow
bool estop
float32 steer_ud
float32 steer_lr
```

**`State.msg`** — robot state feedback (pressure sensor and actuator values):

```
float32 cp_s
float32 a1_s
float32 a2_s
float32 a3_s
float32 cp_a
float32 a1_a
float32 a2_a
float32 a3_a
float32 d_s
float32 d_c
float32 c_m
float32 a_m
```

**`PressureSet.srv`** — request/response for setting a chamber/actuator pressure target:

```
float32 chamber_val
float32 actuator_val
---
bool success
string message
```

## Nodes

| Script | Description |
|---|---|
| [`fort_controller.py`]({{ site.github_blob }}/SPROUT_Design/Code/sprout_ros/scripts/fort_controller.py) | Reads the Fort Robotics Wireless Controller (FRWC) HID device directly and publishes `sensor_msgs/Joy` |
| [`fort_scm_controller.py`]({{ site.github_blob }}/SPROUT_Design/Code/sprout_ros/scripts/fort_scm_controller.py) | Publishes `Joy` messages using the `fort_scm` SCM protocol library for the Fort controller |
| [`joy_vine_interface.py`]({{ site.github_blob }}/SPROUT_Design/Code/sprout_ros/scripts/joy_vine_interface.py) | Bridges `Joy` messages to the vine robot's Arduino over serial, publishing `sprout_ros/State` |
| [`fort_vine_interface.py`]({{ site.github_blob }}/SPROUT_Design/Code/sprout_ros/scripts/fort_vine_interface.py) | Variant of the vine interface driver that also exposes the `PressureSet` service |
| [`screen.py`]({{ site.github_blob }}/SPROUT_Design/Code/sprout_ros/scripts/screen.py) | Drives the onboard status LCD from `sprout_ros/State` |

## Bring-up

`launch/system_bringup.py` starts the Fort controller driver, the Arduino/vine interface node, and the LCD screen node together:

```python
Node(package='sprout_ros', executable='fort_scm_controller.py', name='fort_driver', output='screen'),
Node(package='sprout_ros', executable='fort_vine_interface.py', name='jetson_arduino', output='screen'),
Node(package='sprout_ros', executable='screen.py', name='jetson_screen', output='screen'),
```

## Arduino firmware

The `vine_control` sketch (`arduino/vine_control/vine_control/vine_control_uno_rev3`) runs on the Arduino Uno Rev3 mounted on the [custom shield]({{ site.baseurl }}/electronics/) and is flashed following the [Jetson Bootstrap]({{ site.baseurl }}/software/jetson-bootstrap.html#flash-arduino-with-code) guide.
