---
layout: default
title: Documentation
nav_order: 2
has_children: true
permalink: /documentation/
---

# Compute Box Documentation
{: .no_toc }

Source: [`SPROUT_Design/Documentation`]({{ site.github_tree }}/SPROUT_Design/Documentation)
{: .label .label-green }

## Overview

This section provides assembly, wiring, and hardware validation instructions
for the compute box used in SPROUT: The Open-Source Soft Robot for Search and
Rescue.

The compute box integrates:
- onboard computation
- power regulation
- actuator control
- sensing interfaces
- networking
- embedded communication hardware

The system is designed for:
- field deployment
- modular servicing
- battery-powered operation
- rapid hardware iteration
- reproducible research integration

---

## System architecture

![System Architecture]({{ site.github_raw }}/SPROUT_Design/Documentation/Images/system_architecture_ssrr_large.jpg)

The compute stack coordinates communication between:
- embedded microcontrollers
- motor drivers
- sensing hardware
- pneumatic regulators
- operator interfaces
- power regulation hardware

Major subsystems include:
- Compute Stack
- Control Peripherals
- Vine Base

---

## Documentation map

| Page | Description |
|---|---|
| [Bill of Materials]({{ site.baseurl }}/documentation/bom.html) | Bill of materials and sourcing |
| [Enclosure]({{ site.baseurl }}/documentation/enclosure.html) | Enclosure preparation and mounting layout |
| [Assembly]({{ site.baseurl }}/documentation/assembly.html) | Step-by-step assembly procedure |
| [Wiring]({{ site.baseurl }}/documentation/wiring.html) | Wiring harnesses and connector pinouts |
| [Vine Construction]({{ site.baseurl }}/documentation/vine-construction.html) | Building the vine robot body *(work in progress)* |

---

## Compute hardware

| Component | Function |
|---|---|
| NVIDIA Jetson | Main onboard compute |
| Arduino Uno Rev3 | Low-level actuator/sensor interface |
| DC-DC regulators | Power conversion |
| Motor drivers | Actuator control |

---

## Power architecture

The compute box operates from an external DC battery source.

Primary voltage rails:
- 18 V actuator rail
- 15 V auxiliary rail
- 5 V compute rail

All rails are fused independently.

---

## Communication architecture

The system currently uses:
- USB serial communication
- Ethernet
- WiFi

---

## Assembly workflow

Recommended assembly order:

1. Mechanical enclosure preparation
2. Component mounting
3. Power subsystem wiring
4. Compute subsystem installation
5. Peripheral wiring
6. Software flashing/setup
7. Validation testing

---

## Safety

{: .warning }
> Disconnect all power before servicing the compute box.
>
> Verify voltage polarity prior to powering up the system.
>
> Use strain relief for all external cable interfaces.
