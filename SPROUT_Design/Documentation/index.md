# Compute Box Documentation

## Overview
This document provides assembly, wiring, software setup, and validation instructions for the compute box used in SPROUT: The Open-Source Soft Robot for Search and Rescue.

The compute box integrates:
- onboard computation,
- power regulation,
- actuator control,
- sensing interfaces,
- networking,
- embedded communication hardware.

The system is designed for:
- field deployment,
- modular servicing,
- battery-powered operation,
- rapid hardware iteration,
- reproducible research integration.

---

## System Architecture

![System Architecture](Images/system_architecture_ssrr_large.jpg)

The compute stack coordinates communication between:
- embedded microcontrollers,
- motor drivers,
- sensing hardware,
- pneumatic regulators,
- operator interfaces,
- power regulation hardware.

Major subsystems include:
- Compute Stack
- Control Peripherals
- Vine Base

---

## Documentation Map

| Section | Description |
|---|---|
| `bom.md` | Bill of materials and sourcing |
| `enclosure.md` | Enclosure preparation and mounting layout |
| `wiring.md` | Wiring harnesses and connector pinouts |
| `compute.md` | Compute hardware installation and interfaces |
| `assembly.md` | Step-by-step assembly procedure |
| `troubleshooting.md` | Hardware diagnostics and common failures |
| `robot.md` | Robot manufacturing instructions | 

---

## Compute Hardware

Current compute hardware includes:

| Component | Function |
|---|---|
| NVIDIA Jetson | Main onboard compute |
| Arduino Uno Rev3 | Low-level actuator/sensor interface |
| DC-DC regulators | Power conversion |
| Motor drivers | Actuator control |

---

## Power Architecture

The compute box operates from an external DC battery source.

Primary voltage rails:
- 18 V actuator rail
- 15 V auxiliary rail
- 5 V compute rail

All rails are fused independently.

---

## Communication Architecture

The system currently uses:
- USB serial communication
- Ethernet 
- WiFi

---

## Assembly Workflow

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

> Disconnect all power before servicing the compute box.

> Verify voltage polarity prior to powering up the system.

> Use strain relief for all external cable interfaces.

---

## Repository Structure

```text
sprout/
├── index.md
├── bom.md
├── enclosure.md
├── assembly.md
├── compute.md
├── wiring.md
├── troubleshooting.md
├── robot.md
├── figures/
│   ├── assembly/
│   ├── enclosure/
│   ├── wiring/
├── schematics/
├── cad/
└── datasheets/