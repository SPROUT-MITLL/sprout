---
layout: default
title: Electronics
nav_order: 4
has_children: true
permalink: /electronics/
---

# Electronics
{: .no_toc }

Source: [`SPROUT_Design/Electronics`]({{ site.github_tree }}/SPROUT_Design/Electronics)
{: .label .label-green }

The `Electronics` directory contains the custom Arduino shield PCB that
interfaces the Arduino Uno Rev3 with the motor driver, QB3 pressure
regulators, solenoid valve, LCD screen, and the compute box's power rails (see
[Wiring]({{ site.baseurl }}/documentation/wiring.html) for the full pinout).

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

## Arduino shield

Source: [`Electronics/Arduino Shield`]({{ site.github_tree }}/SPROUT_Design/Electronics/Arduino%20Shield)
{: .label .label-green }

Designed in KiCad. The project targets an Arduino Uno Rev3 shield footprint
and breaks out the following interfaces referenced throughout the
[wiring guide]({{ site.baseurl }}/documentation/wiring.html):

- Motor driver power and control (`M_DRV_PWR`, `M_DRV_ARD`, `M_5V`)
- Solenoid valve output
- 15 V actuator/regulator rails (`M_15V`, `R_15V`)
- QB3 pressure regulator channels (Chamber, Actuator 1–3)
- I²C breakout for the LCD display

### 3D preview

{% assign step_url = site.github_raw | append: "/SPROUT_Design/Electronics/Arduino Shield/vine_robot_arduino_shield.step" %}
{% include step_viewer.html url=step_url name="Arduino shield" %}

<script type="module" src="{{ site.baseurl }}/assets/js/step-viewer.js"></script>

### Board layout

![Arduino shield PCB layout]({{ site.github_raw }}/SPROUT_Design/Documentation/Images/Electronics/arduino_shield_schematic.jpg)

*Figure 1. PCB layout showing traces and connector pinouts for the actuator, solenoid, motor driver, power, encoder, and joystick headers referenced in the [wiring guide]({{ site.baseurl }}/documentation/wiring.html).*

| File | Description |
|---|---|
| [`vine_robot_arduino_shield.kicad_sch`]({{ site.github_blob }}/SPROUT_Design/Electronics/Arduino%20Shield/vine_robot_arduino_shield.kicad_sch) | KiCad schematic |
| [`vine_robot_arduino_shield.kicad_pcb`]({{ site.github_blob }}/SPROUT_Design/Electronics/Arduino%20Shield/vine_robot_arduino_shield.kicad_pcb) | KiCad PCB layout |
| [`vine_robot_arduino_shield.kicad_pro`]({{ site.github_blob }}/SPROUT_Design/Electronics/Arduino%20Shield/vine_robot_arduino_shield.kicad_pro) | KiCad project file |
| [`vine_robot_arduino_shield.step`]({{ site.github_blob }}/SPROUT_Design/Electronics/Arduino%20Shield/vine_robot_arduino_shield.step) | 3D STEP model of the assembled board |
| [`v2_gerbers_8_23/`]({{ site.github_tree }}/SPROUT_Design/Electronics/Arduino%20Shield/v2_gerbers_8_23) | Fabrication-ready Gerber/drill files (rev. 8/23) |
| [`v2_gerbers_8_23_2/`]({{ site.github_tree }}/SPROUT_Design/Electronics/Arduino%20Shield/v2_gerbers_8_23_2) | Follow-up Gerber/drill export (rev. 8/23, v2) |
| [`Arduino_MountingHole.pretty/`]({{ site.github_tree }}/SPROUT_Design/Electronics/Arduino%20Shield/Arduino_MountingHole.pretty) | Custom KiCad footprint library: standard Arduino mounting holes |
| [`Arduino_MountingHole_3.2mm.pretty/`]({{ site.github_tree }}/SPROUT_Design/Electronics/Arduino%20Shield/Arduino_MountingHole_3.2mm.pretty) | Custom KiCad footprint library: 3.2 mm mounting holes |

To fabricate a board, download the contents of a `v2_gerbers_8_23*` folder (or
the corresponding `.zip`) and submit it directly to your PCB manufacturer of
choice.

To open and edit the design, clone the repository and open
`vine_robot_arduino_shield.kicad_pro` in [KiCad](https://www.kicad.org/) 7 or
later — the custom footprint libraries in this folder are referenced by the
project's local `fp-lib-table` and will resolve automatically.

## Related hardware

The shield is mounted alongside the Arduino Uno Rev3 in the compute box — see
[Assembly → Step 3]({{ site.baseurl }}/documentation/assembly.html#step-3-install-compute-hardware)
for installation and [Wiring]({{ site.baseurl }}/documentation/wiring.html) for the full
connector pinout. CAD for the shield's mechanical footprint and mounting is
included in [CAD → Compute Box]({{ site.baseurl }}/cad/new-compute-box.html).
