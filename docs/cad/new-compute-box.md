---
layout: default
title: New Compute Box
parent: CAD
nav_order: 1
---

# New Compute Box CAD
{: .no_toc }

Source: [`SPROUT_Design/CAD/new_compute_box`]({{ site.github_tree }}/SPROUT_Design/CAD/new_compute_box)
{: .label .label-green }

Full mechanical design for the compute box described in
[Documentation]({{ site.baseurl }}/documentation/): enclosure mounts, electropneumatic hardware,
power electronics, connectors, and the robot-base interface. See
[Assembly]({{ site.baseurl }}/documentation/assembly.html) and
[Enclosure]({{ site.baseurl }}/documentation/enclosure.html) for how these parts go together.

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

## Top-level assemblies

| File | Description |
|---|---|
| [`sprout_computer_subassembly.SLDASM`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/sprout_computer_subassembly.SLDASM) | Top-level compute box subassembly |
| [`jetson_subassembly.SLDASM`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/jetson_subassembly.SLDASM) | Jetson computer + mounting housing subassembly |
| [`feet_assembly.SLDASM`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/feet_assembly.SLDASM) | External robot mounting foot assembly (see [Enclosure]({{ site.baseurl }}/documentation/enclosure.html#external-robot-mounting-system)) |
| [`EMERGENCY STOP SWITCH.SLDASM`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/EMERGENCY%20STOP%20SWITCH.SLDASM) | E-stop switch assembly |
| [`1_8 NPT - 1_4 Inch Push to Connect Elbow Fitting.SLDASM`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/1_8%20NPT%20-%201_4%20Inch%20Push%20to%20Connect%20Elbow%20Fitting.SLDASM) | Pneumatic elbow fitting assembly |
| [`UA-006.SLDASM`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/UA-006.SLDASM) / [`.STEP`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/UA-006.STEP) | Vendor sub-assembly (STEP export included) |

## Compute & electronics mounting

| File | Description |
|---|---|
| [`jetson_base.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/jetson_base.SLDPRT) | 3D-printed Jetson mounting base |
| [`jetson_computer.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/jetson_computer.SLDPRT) | NVIDIA Jetson reference model |
| [`arduino uno.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/arduino%20uno.SLDPRT) | Arduino Uno Rev3 reference model |
| [`vine_robot_arduino_shield.step`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/vine_robot_arduino_shield.step) | Custom Arduino shield (see [Electronics]({{ site.baseurl }}/electronics/)) |
| [`MDDS10.step`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/MDDS10.step) | Cytron MDD10A dual-channel motor driver |
| [`xl6009_DCDC_BoostBuck.step`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/xl6009_DCDC_BoostBuck.step) | DC-DC buck/boost converter module |
| [`QB3-3D.STEP`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/QB3-3D.STEP) | ProportionAir QB3 pressure regulator |
| [`3V210-08NC SOLENOID VALVE.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/3V210-08NC%20SOLENOID%20VALVE.SLDPRT) | 3/2 NC solenoid valve |
| [`M18 Battery 8Ah.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/M18%20Battery%208Ah.SLDPRT) | M18 8Ah battery reference model |
| [`M18 battery mount.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/M18%20battery%20mount.SLDPRT) | Custom M18 battery mounting bracket |

## Enclosure & robot mounting

| File | Description |
|---|---|
| [`7335K231_Polycarbonate Washdown Enclosure.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/7335K231_Polycarbonate%20Washdown%20Enclosure.SLDPRT) / [`.SLDDRW`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/7335K231_Polycarbonate%20Washdown%20Enclosure.SLDDRW) | Enclosure reference model and drawing |
| [`7335K41_10-5-8 x 6-3-4 Steel Panel for Polycarbonate Washdown Enclosure.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/7335K41_10-5-8%20x%206-3-4%20Steel%20Panel%20for%20Polycarbonate%20Washdown%20Enclosure.SLDPRT) | Backer panel for the enclosure |
| [`feet_part_1.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/feet_part_1.SLDPRT), [`feet_part_2.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/feet_part_2.SLDPRT), [`feet_rail_1.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/feet_rail_1.SLDPRT) | Curved support foot components (see [Enclosure]({{ site.baseurl }}/documentation/enclosure.html#external-robot-mounting-system)) |
| [`69915K54_Plastic Submersible Cord Grip.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/69915K54_Plastic%20Submersible%20Cord%20Grip.SLDPRT) | Cable gland for battery wiring pass-through |

## Connectors, switches & fittings

| File | Description |
|---|---|
| [`1860N13_Wet-Location HDMI Connector.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/1860N13_Wet-Location%20HDMI%20Connector.SLDPRT) | Panel-mount HDMI connector |
| [`3216K56_Harsh Environment Mini Signal Power Connector.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/3216K56_Harsh%20Environment%20Mini%20Signal%20Power%20Connector.SLDPRT) | Sealed signal/power connector |
| [`5697T29_Wet-Location Data Connector.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/5697T29_Wet-Location%20Data%20Connector.SLDPRT) | Panel-mount Ethernet/data connector |
| [`CNLINKO YU-USB.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/CNLINKO%20YU-USB.SLDPRT) / [`.step`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/CNLINKO%20YU-USB.step) | Panel-mount USB connector |
| [`EMERGENCY STOP DOME.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/EMERGENCY%20STOP%20DOME.SLDPRT), [`EMERGENCY STOP YELLOW  PLATE.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/EMERGENCY%20STOP%20YELLOW%20%20PLATE.SLDPRT) | E-stop mushroom dome and mounting plate |
| [`Push button 12mm.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/Push%20button%2012mm.SLDPRT) | 12 mm panel push button |
| [`Antenna_assembly v4.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/Antenna_assembly%20v4.SLDPRT) | WiFi/wireless NIC antenna assembly |

## Pneumatic fittings

| File | Description |
|---|---|
| [`5602K14_Industrial Quick-Disconnect Hose Coupling Set for Air.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/5602K14_Industrial%20Quick-Disconnect%20Hose%20Coupling%20Set%20for%20Air.SLDPRT) | Quick-disconnect air coupling |
| [`5779K109_Push-to-Connect Tube Fitting for Air.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/5779K109_Push-to-Connect%20Tube%20Fitting%20for%20Air.SLDPRT) | Push-to-connect fitting |
| [`5779K131_Push-to-Connect Tube Fitting for Air.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/5779K131_Push-to-Connect%20Tube%20Fitting%20for%20Air.SLDPRT) | Push-to-connect fitting |
| [`5779K24_Push-to-Connect Tube Fitting for Air.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/5779K24_Push-to-Connect%20Tube%20Fitting%20for%20Air.SLDPRT) | Push-to-connect fitting |
| [`5779K445_Push-to-Connect Tube Fitting for Air.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/5779K445_Push-to-Connect%20Tube%20Fitting%20for%20Air.SLDPRT) | Push-to-connect fitting |
| [`7699N53_Universal-Thread Push-to-Connect Tube Fittings.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/7699N53_Universal-Thread%20Push-to-Connect%20Tube%20Fittings.SLDPRT) | Universal-thread push-to-connect fitting |
| [`9027N158_Low-Pressure Stainless Steel Threaded Pipe Fitting.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/new_compute_box/9027N158_Low-Pressure%20Stainless%20Steel%20Threaded%20Pipe%20Fitting.SLDPRT) | Low-pressure threaded pipe fitting |

See the [Bill of Materials]({{ site.baseurl }}/documentation/bom.html#pneumatics) for the matching McMaster-Carr/vendor part numbers.
