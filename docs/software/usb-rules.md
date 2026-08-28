---
layout: default
title: USB Device Rules
parent: Compute Setup
grand_parent: Software
nav_order: 2
---

# Device Aliasing Setup
{: .no_toc }

Source: [`.../compute_setup/jetson/usb_rules.md`]({{ site.github_blob }}/SPROUT_Design/Code/compute_setup/jetson/usb_rules.md)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

First, add your user to some groups:

```bash
sudo adduser <<USER>> dialout
sudo adduser <<USER>> video
```

## Setup notes

Do the following to set up access to the Arduino which controls the vine robot base:

```bash
sudo nano /etc/udev/rules.d/99-arduino.rules
```

and then paste in the following:

```
KERNEL=="ttyACM[0-9]*", ACTION=="add", ATTRS{idVendor}=="2341", ATTRS{idProduct}=="0043", SYMLINK+="com/vine_arduino"
```

To put the changes into effect, run

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

and then reboot.

## Connect to PS5 controller

First install the following package to interface with the PS5 controller via python:

```bash
python -m pip install pydualsense pyserial
```

### Via wired cable

Plug the PS5 DualSense controller into one of the Jetson's USB 3.0 ports using a data-cable USB-C cable. Make sure the cable is not just a charging cable!

{: .warning }
> Charge-only USB-C cables are missing the data lines the controller needs and will not work here, even though they charge the controller fine.

Do the following to set up access to the PS5 controller for teleoperation:

```bash
sudo nano /etc/udev/rules.d/70-ps5-controller.rules
```

and then paste in the following:

```
# ref.: https://boilingsteam.com/the-dualsense-is-making-even-more-sense/

# PS5 DualSense controller over USB hidraw
KERNEL=="hidraw*", ATTRS{idVendor}=="054c", ATTRS{idProduct}=="0ce6", MODE="0660", TAG+="uaccess" SYMLINK+="input/ps5"
# PS5 DualSense Edge controller over USB hidraw
KERNEL=="hidraw*", ATTRS{idVendor}=="054c", ATTRS{idProduct}=="0df2", MODE="0660", TAG+="uaccess"  SYMLINK+="input/ps5"
```

To put the changes into effect, run

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

### Via Bluetooth (optional)

Do the following to set up access to the PS5 controller for teleoperation:

```bash
sudo nano /etc/udev/rules.d/70-ps5-controller.rules
```

and then paste in the following:

```
# ref.: https://boilingsteam.com/the-dualsense-is-making-even-more-sense/
# PS5 DualSense controller over bluetooth hidraw
KERNEL=="hidraw*", KERNELS=="*054C:0CE6*", MODE="0660", TAG+="uaccess"  SYMLINK+="input/ps5"
# PS5 DualSense Edge controller over bluetooth hidraw
KERNEL=="hidraw*", KERNELS=="*054C:0DF2*", MODE="0660", TAG+="uaccess"  SYMLINK+="input/ps5"
```

To put the changes into effect, run

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

Pairing can be accomplished in the terminal with the following commands.

Find the computer's Bluetooth device using the command.

```bash
hcitool dev
```

This will return a Bluetooth device name and a MAC address. To find Bluetooth devices in range, run

```bash
hcitool -i <dev_name> scan
```

where `dev_name` is likely `hci0`. The PlayStation 5 DualSense will be called `DualSense Wireless Controller`. Note the MAC address for this device, and then trust and connect to the device using the following commands:

```bash
bluetoothctl  # enters you into some terminal environment
trust <<MAC_address>>
connect <<MAC_address>>
```

## Fort Robotics controller

As an alternative to the PS5 controller, the Fort Robotics Wireless Controller (FRWC) provides a parallel interface.

```bash
sudo nano /etc/udev/rules.d/99-fort-wrc.rules
```

and then paste in the following:

```
KERNEL=="ttyACM[0-9]*", ACTION=="add", ATTRS{idVendor}=="2a99", ATTRS{idProduct}=="c011", MODE="0666", TAG+="uaccess", SYMLINK+="input/fort"
```

To put the changes into effect, run

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

You will also need to install the dedicated package to interface with the Fort Controller.

```bash
cd ~/Downloads
git clone git@github.com:SPROUT-MITLL/fort_scm_py3.git
cd fort_scm_py3
bash build.sh
cd dist
python3 -m pip install <<NAME OF WHL FILE>>
```

## Some useful USB commands

`lsusb` allows you to see connected USB devices. To figure out where a device is connected, run `lsusb` without the device plugged in, and then plug in the device and run again.

`usb-devices` lists all of the USB devices with more information including the vendor ID and product ID which are needed for creating symbolic links to the device.

`dmesg | less` and then hitting `/` and searching for keywords (like the product ID or vendor ID) can also be useful.

`sudo udevadm info --name=<device_name> --attribute-walk` where `<device_name>` is the location of your device on the system (e.g., `/dev/input/js0`). You can also append `| less` to the end of this command to search for the `idVendor` or `idProduct`.
