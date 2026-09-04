---
layout: default
title: Compute Box
parent: CAD
nav_order: 1
---

# Compute Box CAD
{: .no_toc }

Source: [`SPROUT_Design/CAD/compute_box`]({{ site.github_tree }}/SPROUT_Design/CAD/compute_box)
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

## 3D previews

STEP files can be previewed directly in the browser. SolidWorks-only files (`.SLDPRT`/`.SLDASM`) don't have an open format to preview and must be downloaded.

{% assign step_url = site.github_raw | append: "/SPROUT_Design/CAD/compute_box/vine_robot_arduino_shield.step" %}
{% include step_viewer.html url=step_url name="Arduino shield" %}

{% assign step_url = site.github_raw | append: "/SPROUT_Design/CAD/compute_box/xl6009_DCDC_BoostBuck.step" %}
{% include step_viewer.html url=step_url name="Buck/boost converter" %}

{% assign step_url = site.github_raw | append: "/SPROUT_Design/CAD/compute_box/QB3-3D.STEP" %}
{% include step_viewer.html url=step_url name="QB3 pressure regulator" %}

<script type="module" src="{{ site.baseurl }}/assets/js/step-viewer.js"></script>

---

## Top-level assemblies

| File | Description |
|---|---|
| [`compute_box.SLDASM`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/compute_box.SLDASM) / [`compute_box_assembly.SLDASM`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/compute_box_assembly.SLDASM) | Top-level compute box assembly |
| [`case.SLDASM`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/case.SLDASM) / [`case_assembly.SLDASM`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/case_assembly.SLDASM) | Enclosure case assembly |
| [`jetson_subassembly.SLDASM`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/jetson_subassembly.SLDASM) | Jetson computer + mounting housing subassembly |
| [`feet_assembly.SLDASM`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/feet_assembly.SLDASM) | External robot mounting foot assembly (see [Enclosure]({{ site.baseurl }}/documentation/enclosure.html#external-robot-mounting-system)) |
| [`EMERGENCY STOP SWITCH.SLDASM`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/EMERGENCY%20STOP%20SWITCH.SLDASM) | E-stop switch assembly |
| [`1_8 NPT - 1_4 Inch Push to Connect Elbow Fitting.SLDASM`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/1_8%20NPT%20-%201_4%20Inch%20Push%20to%20Connect%20Elbow%20Fitting.SLDASM) | Pneumatic elbow fitting assembly |
| [`UA-006.SLDASM`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/UA-006.SLDASM) | Vendor sub-assembly |

## Enclosure & case

| File | Description |
|---|---|
| [`case.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/case.SLDPRT) | Enclosure case body |
| [`bottom_panel.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/bottom_panel.SLDPRT) | Enclosure bottom mounting panel |
| [`top_interface.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/top_interface.SLDPRT) | Top interface panel |
| [`acrylic_top.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/acrylic_top.SLDPRT) / [`.SLDDRW`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/acrylic_top.SLDDRW) / [`.DXF`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/acrylic_top.DXF) / [`.pdf`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/acrylic_top.pdf) | Acrylic top panel model, drawing, cut file, and print-ready PDF |
| [`CASE_930_R1_Btm_INNER_SURFACE.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/CASE_930_R1_Btm_INNER_SURFACE.SLDPRT) | NANUK 930 case bottom inner-surface reference (manufacturer geometry) |
| [`CASE_930_R1_Btm_INNER_SURFACE_hole_drawing.SLDDRW`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/CASE_930_R1_Btm_INNER_SURFACE_hole_drawing.SLDDRW) / [`.pdf`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/CASE_930_R1_Btm_INNER_SURFACE_hole_drawing.pdf) | Mounting hole drawing for the case bottom |
| [`CASE_930_R1_Top_INNER_SURFACE.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/CASE_930_R1_Top_INNER_SURFACE.SLDPRT) | NANUK 930 case top inner-surface reference (manufacturer geometry) |
| [`930_R1_INNER_SURFACE_STEP/`]({{ site.github_tree }}/SPROUT_Design/CAD/compute_box/930_R1_INNER_SURFACE_STEP) / [`.zip`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/930_R1_INNER_SURFACE_STEP.zip) | Manufacturer-provided NANUK 930 inner-surface STEP files (top + bottom), used as the reference geometry for the mounting brackets (see [Enclosure]({{ site.baseurl }}/documentation/enclosure.html)) |

## Screen, plate & regulator mounting

| File | Description |
|---|---|
| [`screen.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/screen.SLDPRT) | Display panel reference model |
| [`screen_holder.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/screen_holder.SLDPRT) / [`.STL`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/screen_holder.STL) | Display mounting bracket |
| [`screen_holder_extended.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/screen_holder_extended.SLDPRT) / [`.STL`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/screen_holder_extended.STL) | Extended display mounting bracket |
| [`screen_and_plate_holders.3mf`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/screen_and_plate_holders.3mf) | Sliced 3D-print file for the screen and plate holder brackets |
| [`plate_corner_holder.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/plate_corner_holder.SLDPRT) / [`.STL`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/plate_corner_holder.STL) | Corner mounting bracket for the interior mounting plate |
| [`plate_interface.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/plate_interface.SLDPRT) / [`.STL`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/plate_interface.STL) | Interior mounting plate interface |
| [`regulator_cover.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/regulator_cover.SLDPRT) / [`.STL`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/regulator_cover.STL) / [`.3mf`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/regulator_cover.3mf) | 3D-printed cover for the QB3 pressure regulators |

## Feet & robot mounting

| File | Description |
|---|---|
| [`feet_part_1.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/feet_part_1.SLDPRT), [`feet_part_2.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/feet_part_2.SLDPRT) | Curved support foot components (see [Enclosure]({{ site.baseurl }}/documentation/enclosure.html#external-robot-mounting-system)) |
| [`feet_rail_1.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/feet_rail_1.SLDPRT) | Mounting foot rail |
| [`feet_rail.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/feet_rail.SLDPRT) / [`.STL`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/feet_rail.STL) | Mounting foot rail (current revision) |
| [`feet_rail_simplified.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/feet_rail_simplified.SLDPRT) / [`.STL`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/feet_rail_simplified.STL) / [`_R.STL`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/feet_rail_simplified_R.STL) | Simplified foot rail for 3D printing (left/right) |
| [`base_bottom_insert_left.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/base_bottom_insert_left.SLDPRT) / [`.STL`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/base_bottom_insert_left.STL) | Base bottom insert (left) |
| [`base_bottom_insert_simplified.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/base_bottom_insert_simplified.SLDPRT) / [`.STL`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/base_bottom_insert_simplified.STL) / [`_R.STL`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/base_bottom_insert_simplified_R.STL) | Simplified base bottom insert for 3D printing (left/right) |

## Compute & electronics mounting

| File | Description |
|---|---|
| [`jetson_base.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/jetson_base.SLDPRT) / [`.STL`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/jetson_base.STL) | 3D-printed Jetson mounting base |
| [`jetson_computer.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/jetson_computer.SLDPRT) | NVIDIA Jetson reference model |
| [`arduino uno.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/arduino%20uno.SLDPRT) | Arduino Uno Rev3 reference model |
| [`vine_robot_arduino_shield.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/vine_robot_arduino_shield.SLDPRT) / [`.step`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/vine_robot_arduino_shield.step) | Custom Arduino shield (see [Electronics]({{ site.baseurl }}/electronics/)) |
| [`MDDS10.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/MDDS10.SLDPRT) | Cytron MDD10A dual-channel motor driver |
| [`xl6009_DCDC_BoostBuck.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/xl6009_DCDC_BoostBuck.SLDPRT) / [`.step`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/xl6009_DCDC_BoostBuck.step) | DC-DC buck/boost converter module |
| [`QB3-3D.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/QB3-3D.SLDPRT) / [`.STEP`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/QB3-3D.STEP) | ProportionAir QB3 pressure regulator |
| [`3V210-08NC SOLENOID VALVE.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/3V210-08NC%20SOLENOID%20VALVE.SLDPRT) | 3/2 NC solenoid valve |
| [`M18 Battery 8Ah.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/M18%20Battery%208Ah.SLDPRT) | M18 8Ah battery reference model |
| [`M18 battery mount.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/M18%20battery%20mount.SLDPRT) | Custom M18 battery mounting bracket |
| [`fiber_interface_PCB.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/fiber_interface_PCB.SLDPRT) | Reference model for the fiber/comms interface PCB |
| [`small_emergency_button.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/small_emergency_button.SLDPRT) | Small panel-mount E-stop button variant |

## Connectors, switches & fittings

| File | Description |
|---|---|
| [`1860N13_Wet-Location HDMI Connector.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/1860N13_Wet-Location%20HDMI%20Connector.SLDPRT) | Panel-mount HDMI connector |
| [`3216K56_Harsh Environment Mini Signal Power Connector.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/3216K56_Harsh%20Environment%20Mini%20Signal%20Power%20Connector.SLDPRT) | Sealed signal/power connector |
| [`5697T29_Wet-Location Data Connector.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/5697T29_Wet-Location%20Data%20Connector.SLDPRT) | Panel-mount Ethernet/data connector |
| [`8903T45_Mil. Spec. Signal-Power Connector.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/8903T45_Mil.%20Spec.%20Signal-Power%20Connector.SLDPRT) | Mil-spec signal/power connector |
| [`CNLINKO YU-USB.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/CNLINKO%20YU-USB.SLDPRT) | Panel-mount USB connector |
| [`EMERGENCY STOP DOME.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/EMERGENCY%20STOP%20DOME.SLDPRT), [`EMERGENCY STOP SWITCH.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/EMERGENCY%20STOP%20SWITCH.SLDPRT), [`EMERGENCY STOP YELLOW  PLATE.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/EMERGENCY%20STOP%20YELLOW%20%20PLATE.SLDPRT) | E-stop mushroom dome, switch body, and mounting plate |
| [`Push button 12mm.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/Push%20button%2012mm.SLDPRT) | 12 mm panel push button |
| [`Antenna_assembly v4.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/Antenna_assembly%20v4.SLDPRT) | WiFi/wireless NIC antenna assembly |
| [`1568A64_Threaded-Hole Round Pull Handle.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/1568A64_Threaded-Hole%20Round%20Pull%20Handle.SLDPRT) | Case pull handle |
| [`96016A237_Plastic-Head Thumb Screws.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/96016A237_Plastic-Head%20Thumb%20Screws.SLDPRT) | Thumb screws for tool-less panel access |
| [`92000A318_Passivated 18-8 Stainless Steel Pan Head Phillips Screws.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/92000A318_Passivated%2018-8%20Stainless%20Steel%20Pan%20Head%20Phillips%20Screws.SLDPRT) | Panel-mounting screws |
| [`69915K54_Plastic Submersible Cord Grip.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/69915K54_Plastic%20Submersible%20Cord%20Grip.SLDPRT) | Cable gland for battery wiring pass-through |

## Pneumatic fittings

| File | Description |
|---|---|
| [`5602K14_Industrial Quick-Disconnect Hose Coupling Set for Air.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/5602K14_Industrial%20Quick-Disconnect%20Hose%20Coupling%20Set%20for%20Air.SLDPRT) | Quick-disconnect air coupling |
| [`5779K109_Push-to-Connect Tube Fitting for Air.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/5779K109_Push-to-Connect%20Tube%20Fitting%20for%20Air.SLDPRT) | Push-to-connect fitting |
| [`5779K131_Push-to-Connect Tube Fitting for Air.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/5779K131_Push-to-Connect%20Tube%20Fitting%20for%20Air.SLDPRT) | Push-to-connect fitting |
| [`5779K24_Push-to-Connect Tube Fitting for Air.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/5779K24_Push-to-Connect%20Tube%20Fitting%20for%20Air.SLDPRT) | Push-to-connect fitting |
| [`5779K445_Push-to-Connect Tube Fitting for Air.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/5779K445_Push-to-Connect%20Tube%20Fitting%20for%20Air.SLDPRT) | Push-to-connect fitting |
| [`7699N53_Universal-Thread Push-to-Connect Tube Fittings.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/7699N53_Universal-Thread%20Push-to-Connect%20Tube%20Fittings.SLDPRT) | Universal-thread push-to-connect fitting |
| [`4830K133_Standard-Wall 304-304L Stainless Steel Pipe Nipple.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/compute_box/4830K133_Standard-Wall%20304-304L%20Stainless%20Steel%20Pipe%20Nipple.SLDPRT) | Stainless steel pipe nipple |

See the [Bill of Materials]({{ site.baseurl }}/documentation/bom.html#pneumatics) for the matching McMaster-Carr/vendor part numbers.

