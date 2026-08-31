---
layout: default
title: Vine Construction
parent: Documentation
nav_order: 5
---

# Vine Robot Body Fabrication
{: .no_toc }

Source: [`SPROUT_Design/Documentation/vine.md`]({{ site.github_blob }}/SPROUT_Design/Documentation/vine.md)
{: .label .label-green }

<style>
  .center-img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 50%;
  }
</style>

This page covers building the vine robot body itself — the soft,
pneumatically-actuated "vine" that everts from the base — as opposed to the
[compute box]({{ site.baseurl }}/documentation/) that drives and powers it.

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

## Overview

The general fabrication workflow is:

1. Prepare materials, equipment, and workspace
2. Cut fabric
3. Mark fabric with stencil
4. Form and seal the robot body
5. Install pneumatic fittings
6. Inspect and test the completed body

Detailed instructions for each stage are provided below.

---

## Materials, equipment, and tools

### Materials

| Item | Qty | Manufacturer/Source | Part Number / Specification | Notes |
|---|---:|---|---|---|
| Heat-Sealable TPU Coated Nylon Fabric | TODO (width by length) | TODO | TODO | --- |
| Painter's Tape (1 in) | 1 roll | [Scotch Blue](https://www.amazon.com/ScotchBlue-Original-Multi-Surface-Painters-2090-24NC/dp/B00004Z4CP/) | --- | --- |
| Magic Tape (1 in) | 1 roll | [Scotch](https://www.amazon.com/Scotch-Magic-Tape-Inch-Count/dp/B01C5IHGJW/) | --- | --- |
| Double-Sided Red Tape (Heat Resistant) | 1 roll | [Amazon](https://www.amazon.com/BAOFALI-Resistant-AdhesivesPerfect-Microbeads-Scrapbooking/dp/B0CHP8RTSV/) | --- | --- |
| Permanent Marker, Fine Point | 1 | [Sharpie](https://www.amazon.com/Sharpie-37161PP-Permanent-Markers-Resists/dp/B00144862U/) | --- | --- |
| PP/PVC Sheet | 1 | [Amazon](https://www.amazon.com/Plastic-Colored-Folders-Letter-Straight/dp/B09J1KNW1M/) | --- | Used a plastic folder, but could be anything that can be perforated or laser cut |
| Push-to-Connect, Through-Wall Connectors | 3 | McMaster-Carr | TODO | --- |

See the [main BOM]({{ site.baseurl }}/documentation/bom.html) for compute box hardware.

### Fabrication equipment and tools

| Item | Notes |
|---|---|
| [Precision Pick](https://www.amazon.com/ROTATION-4-Piece-Precision-Automotive-Aluminum/dp/B0CHGJHV77/) | --- |
| [6" x 24" Sewing & Quilting Ruler with Gridlines](https://www.amazon.com/gp/aw/d/B0C8BMVL93/) | --- |
| Yard Stick / Straight Edge | --- |
| X-Acto Knife | --- |
| Scissors | --- |
| [Foot-Operated Impulse Sealer](https://www.uline.com/Product/Detail/H-89/Poly-Bag-Sealers/Foot-Operated-Impulse-Sealer-18) | ULINE H-89 |

{: .note }
> The foot-operated heat sealer H-89 has limited space in the back between the sealing edge and the stand post. This makes it difficult to handle fabric while sealing, especially when making a long vine robot (10ft+). For an enhanced model that facilitates the process in a roll-to-roll manufacturing style, see the [H-1256 model](https://www.uline.com/Product/Detail/H-1256/Poly-Bag-Sealers/Foot-Operated-Impulse-Sealer-with-Cutter-18).

### Provided files

| File / Folder | Description |
|---|---|
| TODO | Robot body cutting pattern / template |
| TODO | Reference drawings and dimensions |

---

## Workspace and equipment preparation

Before beginning fabrication:

1. Clean the work surface and remove debris that could damage the fabric.
2. Gather the required materials, tools, and fixtures.
3. Verify that all fabrication equipment is operating correctly, especially the impulse sealer.

   {: .warning }
   > Overheating of the heating element can ruin hours of work in a couple of seconds (and overheating errors are hard to fix!). Underheating, on the other hand, can result in a robot that bursts at low actuation pressures.

4. Adjust the impulse sealer to the correct sealing time using the knob. This adjustment is critical to a good seal, and the correct value will depend heavily on the fabric — some TPU coatings need more heat to seal than others.
5. Practice sealing a few times with a remnant piece of fabric to get used to the process.

---

# Fabrication procedure

## Step 1: Fabric preparation

### Stencil preparation

Here we show how to make a stencil so the marking process is less tedious and less prone to human error. The stencil shown in these steps is very basic (a piece of plastic with holes in it!), but a more precise version could be made by laser cutting a stencil out of thin PVC or acrylic sheet.

1. Grab a plastic folder and unfold it a couple of times so it lies flat. Mark the desired distance from one edge, and cut it to the desired stencil width.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/folder_1.jpg" width="300" class="center-img"/>

2. Use the permanent marker to mark the stencil according to the provided template.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/folder_2.jpg" width="300" class="center-img"/>

3. Make holes at the edges of each mark line using the precision pick.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/folder_3.jpg" width="300" class="center-img"/>
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/folder_4.jpg" width="300" class="center-img"/>

### Material cutting and marking

1. Cut a piece of fabric around 27in wide (and as long as the desired robot length).
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/fabric_marking_1.jpg" width="300" class="center-img"/>

2. Lay the fabric flat on a surface with the TPU side down and place the stencil in one corner. Use the marker to mark each of the holes in the stencil, including the outer edges and the ends of each line in the stencil.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/fabric_marking_2.jpg" width="300" class="center-img"/>

3. Move the stencil forward down the length of the fabric and align it with the previously made markings.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/fabric_marking_4.jpg" width="300" class="center-img"/>

4. Continue until the whole length of the fabric is marked.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/fabric_marking.jpg" width="300" class="center-img"/>

5. Fold the fabric in half (width-wise) with the TPU side inside. Keep the marked side facing up.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/fabric_marking_5.jpg" width="300" class="center-img"/>

6. (Optional) Use the yard stick or straight edge to mark the lines shown in the stencil. The end product should look as below.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/fabric_marking_6.jpg" width="300" class="center-img"/>
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/fabric_marking_8.jpg" width="300" class="center-img"/>

---

## Step 2: Heat sealing fabric

### Lengthwise heat seals

1. With the fabric folded, grab the edges carefully to keep them aligned. Place the fabric in the impulse sealer, holding it aligned with the lengthwise mark closest to the edge, and press the sealer.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/sealing_long_edge_1.jpg" width="300" class="center-img"/>

2. Repeat the process for the remaining lengthwise marks (4 total).
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/sealing_long_edge_2.jpg" width="300" class="center-img"/>

3. One edge of the fabric (width-wise) should be closed due to the fold. Open this end with scissors so it has two flaps like the other end.

### Pouch motor line heat seals

1. Stick a piece of heat-resistant red tape along the length of the impulse sealer. Use the stencil to mark the width of the pouch motor lines.

2. Use the X-Acto knife to cut the tape at the marked locations, so the spots where a heat seal is desired are tape-free.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/pouches_tape.jpg" width="300" class="center-img"/>
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/pouches_tape_2.jpg" width="300" class="center-img"/>

3. Grab the fabric width-wise and hold it tight at both edges. Line up the fabric so the pouch motor line markings align with the tape on the sealer, and press the sealer.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/sealing_pouches_lines.jpg" width="300" class="center-img"/>
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/sealing_pouches_lines_2.jpg" width="300" class="center-img"/>

   {: .note }
   > Placing a piece of painter's tape on the top edge of the sealer clamp and marking it with the stencil can help with alignment during pouch motor sealing.

4. Continue sealing the pouch motor lines along the whole length of the robot.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/sealing_pouches_lines_3.jpg" width="300" class="center-img"/>

   {: .important }
   > Leave one end of the robot with approximately 6in of fabric without pouch motor seals. This end will have the push-to-connect adapters used to actuate each pouch motor line.

5. Once done, remove the tape markings from the sealer.

6. Inspect the pouch motor seals for weak seams or unintended bonding in regions protected by heat-resistant tape. Some residual bonding may occur where heat spreads beyond the intended seal area; these bonds are typically weak and can be separated by gently pinching and pulling the fabric apart.

### Join the longitudinal seam

1. Lay the fabric flat. On each side, fold the top flap completely inward, lay it flat, and tape it down with the magic tape.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/tape_edges.jpg" width="300" class="center-img"/>
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/tape_edges_2.jpg" width="300" class="center-img"/>

2. The exposed TPU on each edge will be joined with the sealer. On one end of the robot fabric, grab the edges, fold the fabric, and line the edges up so the exposed TPU sides face each other.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/seal_edge.jpg" width="300" class="center-img"/>

3. Carefully line up the fabric in the sealer lengthwise, just above the outermost marking, and press the sealer.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/seal_edge_2.jpg" width="300" class="center-img"/>
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/seal_edge_3.jpg" width="300" class="center-img"/>

4. Repeating this process a couple more times above the previous sealed line can reinforce the body by adding more sealed surface area lengthwise.

5. Turn the robot inside out so the taped flaps are on the outside, then remove the tape. The two exposed TPU flaps should now be facing each other.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/seal_edge_5.jpg" width="300" class="center-img"/>

6. Seal these flaps together along the whole length. The robot now has two sealed edges for extra reinforcement — one inside and one outside.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/seal_edge_6.jpg" width="300" class="center-img"/>

7. At this point, it is a good idea to inspect the seams and reinforce them if needed.

---

## Step 3: Pneumatic fittings

1. A push-to-connect fitting will be added to each of the pouch motor lines.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/pneum_1.jpg" width="300" class="center-img"/>

2. Make a horizontal line 6-7cm from the edge on one of the pouch lines.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/pneum_2.jpg" width="300" class="center-img"/>

3. Grab a connector and use it to mark a circle right in the middle of the line.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/pneum_3.jpg" width="300" class="center-img"/>
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/pneum_4.jpg" width="300" class="center-img"/>

4. Repeat steps 2 and 3 on each pouch motor line.

5. Insert a piece of rubber, wood, or another slender, thick material inside a pouch motor line, then use the X-Acto knife to cut an opening in the marked circle. The slender insert prevents cutting through the inner fabric layers.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/pneum_5.jpg" width="300" class="center-img"/>
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/pneum_6.jpg" width="300" class="center-img"/>

6. Repeat step 5 for all three pouch motor lines.

7. To install the pneumatic adapters, slide them inside each pouch motor line, push them through the cut holes, and secure them with the provided nut.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/pneum_7.jpg" width="300" class="center-img"/>
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/pneum_8.jpg" width="300" class="center-img"/>
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/pneum_9.jpg" width="300" class="center-img"/>

---

## Step 4: Inspection and validation

### Visual inspection

Verify:
- seam continuity
- fabric integrity
- pneumatic adapter attachment

### Leak / pressure test

To test the robot, use a compressed air line at low pressure (~2 psi) and verify that the main robot body holds pressure. Connect pressurized air to each pouch motor line to verify these are in working order as well.
<img src="{{ site.github_raw }}/SPROUT_Design/Documentation/Images/Vine/test_1.jpg" width="300" class="center-img"/>

---

## Integration with the base

TODO: How the finished vine mounts into the reel and connects to the base —
see [Assembly → Step 8]({{ site.baseurl }}/documentation/assembly.html#step-8-assembly-with-robot-base) for how the base itself goes together.

## Reference

The current base construction follows the steps from
[vinerobots.org](https://www.vinerobots.org/), with modifications noted in
[Assembly → Step 8]({{ site.baseurl }}/documentation/assembly.html#step-8-assembly-with-robot-base).

