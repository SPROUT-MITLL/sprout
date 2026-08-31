---
layout: default
title: Base CAD
parent: CAD
nav_order: 2
---

# Base CAD
{: .no_toc }

Source: [`SPROUT_Design/CAD/sprout_base`]({{ site.github_tree }}/SPROUT_Design/CAD/sprout_base)
{: .label .label-green }

Mechanical design for the robot base — the motorized reel mechanism that
houses, drives, and everts the [vine body]({{ site.baseurl }}/documentation/vine-construction.html)
— following the [vinerobots.org](https://www.vinerobots.org/) base design,
with modifications noted in
[Assembly → Step 8]({{ site.baseurl }}/documentation/assembly.html#step-8-assembly-with-robot-base).
See [Compute Box]({{ site.baseurl }}/cad/new-compute-box.html) for the compute box that mounts
to this base.

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

## 3D previews

STEP files can be previewed directly in the browser. SolidWorks-only files (`.SLDPRT`/`.SLDASM`) must be downloaded.

{% assign step_url = site.github_raw | append: "/SPROUT_Design/CAD/sprout_base/1314-0016-0250 assembly.STEP" %}
{% include step_viewer.html url=step_url name="Gearmotor assembly" %}

<script type="module" src="{{ site.baseurl }}/assets/js/step-viewer.js"></script>

---

## Subassemblies

| File | Description |
|---|---|
| [`Base_assembly.SLDASM`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/Base_assembly.SLDASM) | Top-level base assembly |
| [`mounting_plate_subassembly.SLDASM`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/mounting_plate_subassembly.SLDASM) | Motor/bearing mounting plate subassembly |
| [`spool_subassembly.SLDASM`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/spool_subassembly.SLDASM) | Reel/spool subassembly |
| [`outlet_subassembly.SLDASM`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/outlet_subassembly.SLDASM) | Vine outlet subassembly |

## Reel / spool mechanism

| File | Description |
|---|---|
| [`SpoolBig.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/SpoolBig.SLDPRT) / [`.STL`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/SpoolBig.STL) | Main reel/spool |
| [`SpoolGuideLarge.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/SpoolGuideLarge.SLDPRT) | Spool guide |
| [`HexHolder.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/HexHolder.SLDPRT) | Hex shaft-to-spool holder |
| [`BearingHolder.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/BearingHolder.SLDPRT) | Bearing holder |
| [`BearingPlateLarge.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/BearingPlateLarge.SLDPRT) | Bearing mounting plate |
| [`MotorPlateLarge.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/MotorPlateLarge.SLDPRT) | Motor mounting plate |
| [`Holder Plate Large.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/Holder%20Plate%20Large.SLDPRT) | Reel holder plate |
| [`sprout_feet.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/sprout_feet.SLDPRT) | Base feet |

## Drive train & shaft components

| File | Description |
|---|---|
| [`6409K27_Compact Square-Face DC Gearmotor.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/6409K27_Compact%20Square-Face%20DC%20Gearmotor.SLDPRT) | Drive gearmotor |
| [`1314-0016-0250 assembly.STEP`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/1314-0016-0250%20assembly.STEP) | Vendor gearmotor assembly reference (STEP export) |
| [`6408K111_Flexible Shaft Coupling Iron Hub.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/6408K111_Flexible%20Shaft%20Coupling%20Iron%20Hub.SLDPRT) | Flexible shaft coupling hub |
| [`6408K84_18000 rpm Buna-N Rubber Spider for 1-5-64 OD Flexible Shaft Coupling Iron Hub.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/6408K84_18000%20rpm%20Buna-N%20Rubber%20Spider%20for%201-5-64%20OD%20Flexible%20Shaft%20Coupling%20Iron%20Hub.SLDPRT) | Rubber spider insert for the shaft coupling |
| [`6432K12_Set Screw Shaft Collar.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/6432K12_Set%20Screw%20Shaft%20Collar.SLDPRT) | Set screw shaft collar |
| [`1870K1_Easy-Access Flange-Mounted Shaft Support.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/1870K1_Easy-Access%20Flange-Mounted%20Shaft%20Support.SLDPRT) | Flange-mounted shaft support |
| [`1886K1_Rotary Shaft.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/1886K1_Rotary%20Shaft.SLDPRT) | Rotary shaft |
| [`8632T139_D-Profile Rotary Shaft.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/8632T139_D-Profile%20Rotary%20Shaft.SLDPRT) | D-profile rotary shaft |
| [`57155K336_Stainless Steel Ball Bearing.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/57155K336_Stainless%20Steel%20Ball%20Bearing.SLDPRT) | Stainless steel ball bearing |
| [`60355K151_Ball Bearing.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/60355K151_Ball%20Bearing.SLDPRT) | Ball bearing |

## Tube & housing

| File | Description |
|---|---|
| [`84865K315_Clear Scratch- and UV-Resistant Cast Acrylic Tube.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/84865K315_Clear%20Scratch-%20and%20UV-Resistant%20Cast%20Acrylic%20Tube.SLDPRT) | Clear acrylic housing tube |
| [`8585K391_Impact-Resistant Polycarbonate Round Tube.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/8585K391_Impact-Resistant%20Polycarbonate%20Round%20Tube.SLDPRT) | Polycarbonate housing tube |

## Pneumatic & electrical fittings

| File | Description |
|---|---|
| [`4511K115_Low-Pressure Connector for Drain, Waste and Vent.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/4511K115_Low-Pressure%20Connector%20for%20Drain,%20Waste%20and%20Vent.SLDPRT) | Low-pressure vent connector |
| [`50785K142_High-Pressure Brass Pipe Fitting.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/50785K142_High-Pressure%20Brass%20Pipe%20Fitting.SLDPRT) | High-pressure brass pipe fitting |
| [`5779K119_Push-to-Connect Tube Fitting for Air.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/5779K119_Push-to-Connect%20Tube%20Fitting%20for%20Air.SLDPRT) | Push-to-connect fitting |
| [`69915K54_Plastic Submersible Cord Grip (1).SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/69915K54_Plastic%20Submersible%20Cord%20Grip%20(1).SLDPRT) | Cable gland for wiring pass-through |

## Fasteners & hardware

| File | Description |
|---|---|
| [`90480A195_Low-Strength Steel Hex Nut.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/90480A195_Low-Strength%20Steel%20Hex%20Nut.SLDPRT) | Hex nut |
| [`95462A029_Medium-Strength Steel Hex Nut.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/95462A029_Medium-Strength%20Steel%20Hex%20Nut.SLDPRT) | Hex nut |
| [`91290A121_Alloy Steel Socket Head Screw.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/91290A121_Alloy%20Steel%20Socket%20Head%20Screw.SLDPRT) | Socket head screw |
| [`96006A709_Black Oxide 18-8 Stainless Steel Socket Head Screw.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/96006A709_Black%20Oxide%2018-8%20Stainless%20Steel%20Socket%20Head%20Screw.SLDPRT) | Socket head screw |
| [`94180A331_Tapered Heat-Set Inserts for Plastic.SLDPRT`]({{ site.github_blob }}/SPROUT_Design/CAD/sprout_base/94180A331_Tapered%20Heat-Set%20Inserts%20for%20Plastic.SLDPRT) | Heat-set threaded insert |

See the [Bill of Materials]({{ site.baseurl }}/documentation/bom.html) for the matching McMaster-Carr/vendor part numbers.

