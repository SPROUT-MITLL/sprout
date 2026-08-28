---
layout: default
title: Wiring
parent: Documentation
nav_order: 4
---

# Wiring
{: .no_toc }

Source: [`SPROUT_Design/Documentation/wiring.md`]({{ site.github_blob }}/SPROUT_Design/Documentation/wiring.md)
{: .label .label-green }

<style>
  .center-img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 50%;
  }
</style>

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

{: .warning }
> Disconnect all power sources before making or changing any connections described below.

---

## Section 1: Mounting plate electrical connections

1. Cut 2-22 AWG stranded wire segments (about 8" long each). On one end, install a 2-pin JST-HX male connector. Leave the other end bare. Cover wire with sleeve mesh and heat-shrink tubing.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Wiring/electrical_wire_1.png" width="500" class="center-img"/>
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Wiring/connector_bw.png" width="300" class="center-img"/>

2. Connect the **JST-HX male** port to **M_DRV_PWR** in the arduino shield. Connect the bare **white wire** to **B+** in motor driver board, and bare **black wire** to **B-**.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Wiring/motor_driver_1.png" width="500" class="center-img"/>

3. Cut 2-22 AWG stranded wire segments (about 6" long each). On one end, install a 2-pin JST-HX male connector. On the other end, install a 2-pin female Dupont connector.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Wiring/electrical_wire_2.png" width="500" class="center-img"/>
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Wiring/connector_bg.png" width="300" class="center-img"/>

4. Connect the **JST-HX male** port to **M_DRV_ARD** in the arduino shield. Connect the Dupont wires to the motor driver (**green** wire to **DIR1**, **blue** wire to **PWM1**).
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Wiring/motor_driver_2.png" width="500" class="center-img"/>

5. Cut 1-22 AWG stranded wire segment (about 5"). On one end, install a 2-pin JST-HX male connector. On the other end, install a 1-pin female Dupont connector.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Wiring/electrical_wire_3.png" width="500" class="center-img"/>
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Wiring/connector_b_only.png" width="300" class="center-img"/>

6. Connect the **JST-HX male** port to **M_5V** in the arduino shield. Connect the Dupont wire to the motor driver (**GND**).
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Wiring/motor_driver_3.png" width="500" class="center-img"/>

7. Connect the **JST-HX male** port from the buck converter **INPUT** to **Solenoid** in the arduino shield.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Wiring/motor_driver_4.png" width="500" class="center-img"/>

8. Connect the **solenoid** wiring to the buck converter **OUTPUT**.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Wiring/solenoid.png" width="500" class="center-img"/>

9. Connect one of the JST-HX terminated power cables from the 15V buck converters to M_15V in the arduino shield.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Wiring/power_1.png" width="500" class="center-img"/>

10. Connect the other 15V JST-HX terminated buck converter to R_15V in the arduino shield.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Wiring/power_2.png" width="500" class="center-img"/>

11. Connect the QB3 JST connectors to the Actuator 1, Actuator 2, Actuator 3, and Chamber ports in the arduino shield. In this case, Chamber is the leftmost QB3, followed by Actuator 3, Actuator 2, and Actuator 1.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Wiring/qb3_connectors.png" width="500" class="center-img"/>
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Wiring/qb3_connectors_2.png" width="500" class="center-img"/>

12. Make a connector with 4-22 AWG stranded wires, with 4-pin female Dupont connectors on one end. Make sure to follow the wire order shown in the picture below for this connector. Install individual 1-pin Dupont female connectors on the other end.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Wiring/display_1.png" width="500" class="center-img"/>
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Wiring/display_3.png" width="500" class="center-img"/>

13. Connect the individual wires as shown. **White** is **SCL**, **Blue** is **SCA**, **Red** is **5.0V**, **Black** is **GND**.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Wiring/display_2.png" width="500" class="center-img"/>

---

Return to [Assembly → Step 5]({{ site.baseurl }}/documentation/assembly.html#step-5-install-external-elements) to continue the build.
