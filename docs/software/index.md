---
layout: default
title: Software
nav_order: 5
has_children: true
permalink: /software/
---

# Software
{: .no_toc }

Source: [`SPROUT_Design/Code`]({{ site.github_tree }}/SPROUT_Design/Code)
{: .label .label-green }

The `Code` directory contains everything needed to bring the compute box's
software stack online: a bootstrap guide for the onboard NVIDIA Jetson, and
`sprout_ros`, the ROS 2 package that drives the vine robot.

| Page | Source folder | Description |
|---|---|---|
| [Compute Setup]({{ site.baseurl }}/software/compute-setup.html) | [`SPROUT_Design/Code/compute_setup`]({{ site.github_tree }}/SPROUT_Design/Code/compute_setup) | Reference system architecture and Jetson bring-up |
| [Jetson Bootstrap]({{ site.baseurl }}/software/jetson-bootstrap.html) | [`.../compute_setup/jetson`]({{ site.github_tree }}/SPROUT_Design/Code/compute_setup/jetson) | Flashing JetPack, installing ROS 2, and first boot configuration |
| [USB Device Rules]({{ site.baseurl }}/software/usb-rules.html) | [`.../jetson/usb_rules.md`]({{ site.github_blob }}/SPROUT_Design/Code/compute_setup/jetson/usb_rules.md) | udev rules for the Arduino, PS5, and Fort Robotics controllers |
| [SPROUT ROS]({{ site.baseurl }}/software/sprout-ros.html) | [`SPROUT_Design/Code/sprout_ros-main`]({{ site.github_tree }}/SPROUT_Design/Code/sprout_ros-main) | ROS 2 nodes, messages, services, and Arduino firmware |

## Reference architecture

![System Architecture]({{ site.github_raw }}/SPROUT_Design/Code/compute_setup/img/system_architecture.png)
