# Vine Robot Body Fabrication

<style>
  .center-img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 50%; /* Optional: controls the width of the image */
  }
</style>

## Overview

This document provides fabrication instructions for the vine robot body used in SPROUT: The Open-Source Soft Robot for Search and Rescue.

---

## Fabrication Overview

The general fabrication workflow is:

1. Prepare materials, equipment and workspace
2. Cut fabric
3. Mark fabric with stencil
4. Form and seal the robot body
5. Install pneumatic fittings
7. Inspect and test the completed body

Detailed instructions for each stage are provided below.

---

## Materials, Equipment, and Tools

### Materials

| Item | Qty | Manufacturer/Source | Part Number / Specification | Notes |
|---|---:|---|---|---|
| Heat-Sealable TPU Coated Nylon Fabric | AxY (w by L) | Manufacturer | Model | --- |
| Painter's Tape (1 in) | 1 roll | [Scotch Blue](amazon.com/ScotchBlue-Original-Multi-Surface-Painters-2090-24NC/dp/B00004Z4CP/) | --- | --- |
| Magic Tape (1 in) | 1 roll | [Scotch](https://www.amazon.com/Scotch-Magic-Tape-Inch-Count/dp/B01C5IHGJW/) | --- | --- |
| Double-Sided Red Tape (Heat Resistan) | 1 roll | [Amazon](https://www.amazon.com/BAOFALI-Resistant-AdhesivesPerfect-Microbeads-Scrapbooking/dp/B0CHP8RTSV/) | --- | --- | 
| Permanent Marker Fine Point | 1 | [Sharpie](https://www.amazon.com/Sharpie-37161PP-Permanent-Markers-Resists/dp/B00144862U/) | --- | --- |
| PP/PVC Sheet | 1 | [Amazon](https://www.amazon.com/Plastic-Colored-Folders-Letter-Straight/dp/B09J1KNW1M/) | --- | Used a plastic folder but could be anything that can be perforated or laser cut |  
| Push-to-Connect, Through-Wall Connectors | 3 |[McMaster]() | --- | --- |

### Fabrication Equipment and Tools

| Item | Notes |
|---|---|
| [Precision Pick](https://www.amazon.com/ROTATION-4-Piece-Precision-Automotive-Aluminum/dp/B0CHGJHV77/) | --- |
| [6" x 24" Sewing & Quilting Ruler with Gridlines](https://www.amazon.com/gp/aw/d/B0C8BMVL93/) | --- |
| Yard Stick / Straight Edge | --- |
| X-Acto Knife | --- |
| Scissors | --- |
| [Foot-Operated Impulse Sealer](https://www.uline.com/Product/Detail/H-89/Poly-Bag-Sealers/Foot-Operated-Impulse-Sealer-18) | ULINE H-89 | 



NOTE: The foot-operated heat sealer H-89 has limited space in the back between the sealing edge and the stand post. This makes it difficult to handle fabric while sealing, especially when making a long vine robot (10ft+). For an enhanced model that facilitates the process with a roll-to-roll manufacturing style, please see the [H-1256 model](https://www.uline.com/Product/Detail/H-1256/Poly-Bag-Sealers/Foot-Operated-Impulse-Sealer-with-Cutter-18).

The repository includes the files required to reproduce the SPROUT vine robot body.

| File / Folder | Description |
|---|---|
| `TODO` | Robot body cutting pattern / template |
| `TODO` | Reference drawings and dimensions |

---

## Workspace and Equipment Preparation

Before beginning fabrication:

1. Clean the work surface and remove debris that could damage the fabric.
2. Gather the required materials, tools, and fixtures.
3. Verify that all fabrication equipment is operating correctly, especially the impulse sealer. Overheating of the heating element can ruin hours of work in a couple of seconds (and it is hard to fix these overheating errors!). Similarly, underheating could result in a robot that bursts at lower actuation pressures. 
4. Adjust the impulse sealer to the adequate time using the knob. This adjustment is critical to have a good seal (as discussed above). The timer adjustment will highly depend on the fabric. Some fabric TPU coating needs more heat to be sealed than others.
5. Practice the sealing a few times with a remnant piece of fabric to get used to the process.


---

# Fabrication Procedure

## Step 1: Fabric Preparation

### Stencil preparation
Here we show how to make a stencil so the marking process is less teadious and prone to human error. The stencil shown in these steps is very basic (a piece of plastic with holes on it!), but a more-precise version could be made by laser cutting a stencil on thin pvc or acrylic sheets. 

1. Grab a plastic folder and unfold it a couple of times so it can stay flat. Mark xxx mm from one edge, and cut it to have a rectangle x mm wide.
<img src="Images/Vine/folder_1.jpg" width="300" class="center-img"/>

2. Use the permanent marker to mark down the stencil according to the provided template (see XXX).
<img src="Images/Vine/folder_2.jpg" width="300" class="center-img"/>

3. Make holes in the edges of each mark line using the precision pick.
<img src="Images/Vine/folder_3.jpg" width="300" class="center-img"/>
<img src="Images/Vine/folder_4.jpg" width="300" class="center-img"/>

### Material Cutting and Marking

1. Cut a piece of fabric around 27in wide (and as long as the desired robot lenght).
<img src="Images/Vine/fabric_marking_1.jpg" width="300" class="center-img"/>

2. Lay the fabric flat on a surface with the TPU side down and place the stencil in one corner. Use the marker to mark each of the holes in the stencil, including the outer edges and the ending of each of the lines in the stencil.
<img src="Images/Vine/fabric_marking_2.jpg" width="300" class="center-img"/>

3. Move the stencil forward down the lenght and align it with the previously made markings.
<img src="Images/Vine/fabric_marking_4.jpg" width="300" class="center-img"/>

4. Continue until the whole lenght of the fabric is marked. 
<img src="Images/Vine/fabric_marking.jpg" width="300" class="center-img"/>

5. Fold the fabric in half (width-wise) with the TPU side inside. Keep the marked side facing up.
<img src="Images/Vine/fabric_marking_5.jpg" width="300" class="center-img"/>

6. (Optional) Use the yard stick or straight edge to mark the lines shown in the stencil. The end product should look as below.
<img src="Images/Vine/fabric_marking_6.jpg" width="300" class="center-img"/>
<img src="Images/Vine/fabric_marking_8.jpg" width="300" class="center-img"/>

---

## Step 2: Heat sealing fabric

### Lengthwise Heat Seals
1. With the fabric folded, grab the edges carefully to maintain them aligned. Then, place the fabric in the impulse sealer holding it aligned with the lengthwise mark closer to the edge. Press on the sealer.
<img src="Images/Vine/sealing_long_edge_1.jpg" width="300" class="center-img"/>

2. Repeat the process for the lenghtwise marks (4 total).
<img src="Images/Vine/sealing_long_edge_2.jpg" width="300" class="center-img"/>

3. One edge of the fabric (widthwise) should be closed due to the fold. Open this end with scissors so it has two flaps like the other end.

### Pouch Motor Line Heat Seals

1. Stick a piece of heat-resistant red tape along the length of the impulse sealer. Use the stencil to mark down the width of the pouch motor lines. 

2. Use the X-Acto knife to cut the tape at the marked locations. This way, the spots where a heat seal is desired should be tape-free. 
<img src="Images/Vine/pouches_tape.jpg" width="300" class="center-img"/>
<img src="Images/Vine/pouches_tape_2.jpg" width="300" class="center-img"/>

3. Grab the fabric width-wise and hold it tight in both edges. Line up the fabric so the pouch motor line markings are lined up with the tape in the sealer. Press on the sealer. *Note:* Placing a piece of painter's tape in the top edge of the selaer clamp and marking it with the stencil can help with alignment during the pocuh motor sealing. 
<img src="Images/Vine/sealing_pouches_lines.jpg" width="300" class="center-img"/>  
<img src="Images/Vine/sealing_pouches_lines_2.jpg" width="300" class="center-img"/>  

4. Continue to seal the pouch motor lines in the whole length of the robot. *IMPORTANT:* Leave on end of the robot with approximately 6in of fabric without pouch motor seals. This end will have the push-to-connect adapters to actuate each of the pouch motor lines.
<img src="Images/Vine/sealing_pouches_lines_3.jpg" width="300" class="center-img"/>  

5. Once done, remove the tape markings from the sealer.

6. At this stage, inspect the pouch-motor seals for weak seams or unintended bonding in regions protected by heat-resistant tape. Some residual bonding may occur due to heat spreading beyond the intended seal area; these bonds are typically weak and can be separated by gently pinching and pulling the fabric apart

### Join the Longitudinal Seam

1. Lay the fabric flat. On each side, fold the top flap completely inwards, lay it flat, and tape it with the magic tape.
<img src="Images/Vine/tape_edges.jpg" width="300" class="center-img"/>  
<img src="Images/Vine/tape_edges_2.jpg" width="300" class="center-img"/> 

2. The exposed TPU on each edge will be joined with the sealer. To do so, on one end of the robot fabric, grab the edges, fold the fabric, and line the edges up. This way, the exposed TPU sides should be facing each other.
<img src="Images/Vine/seal_edge.jpg" width="300" class="center-img"/> 

3. Carefully line up the fabric in the sealer lengthwise, just above the outermost marking. Press on the sealer. 
<img src="Images/Vine/seal_edge_2.jpg" width="300" class="center-img"/> 
<img src="Images/Vine/seal_edge_3.jpg" width="300" class="center-img"/> 

4. Repeating this process a couple more times above the previous sealed line can reinforce the body by providing more sealed surface area lenghtwise. 

5. Turn the robot inside out. This way, the taped flaps are on the outside. Remove the tape. The two exposed TPU flaps should now be facing each other.
<img src="Images/Vine/seal_edge_5.jpg" width="300" class="center-img"/> 

6. Seal these flaps together along the whole lenght. Now the robot has two sealed edges (for extra reinforcement): one inside and one outside.
<img src="Images/Vine/seal_edge_6.jpg" width="300" class="center-img"/> 

7. At this point, it is a good idea to inspect the seams and reinforce them if needed. 

---

## Step 3: Pneumatic Fittings

1. We will add a push-to-connect fitting on each of the pouch motor lines.
<img src="Images/Vine/pneum_1.jpg" width="300" class="center-img"/> 

2. Make a horizontal line 6-7cm away from the edge in one of the pouch lines.
<img src="Images/Vine/pneum_2.jpg" width="300" class="center-img"/> 

3. Grab a connector and use it to mark a circle right in the middle of the line.
<img src="Images/Vine/pneum_3.jpg" width="300" class="center-img"/> 
<img src="Images/Vine/pneum_4.jpg" width="300" class="center-img"/> 

4. Repeat steps 2 and 3 on each pouch motor line.

5. Insert a piece of rubber, wood, or a slender thick material inside a pouch motor line. Use the X-Acto knife to cut an opening in the marked circle. The slender piece of wood prevents from cutting the inner fabric layers.
<img src="Images/Vine/pneum_5.jpg" width="300" class="center-img"/> 
<img src="Images/Vine/pneum_6.jpg" width="300" class="center-img"/> 

6. Repeat step 5 for the three pouch motor lines. 

7. To install the pneumatic adapters, slide them inside each of the pouch motor lines, push them through the cut holes, and secure them with the provided nut. 
<img src="Images/Vine/pneum_7.jpg" width="300" class="center-img"/> 
<img src="Images/Vine/pneum_8.jpg" width="300" class="center-img"/> 
<img src="Images/Vine/pneum_9.jpg" width="300" class="center-img"/> 

## Step 7: Inspection and Validation

### Visual Inspection

Verify:
- seam continuity,
- fabric integrity,
- penumatic adapter attachment

### Leak / Pressure Test

To test the robot, use a compressed air line at a low pressure (~2 psi) and verify the main robot body holds pressure. Connect the pressurized air to each pouch motor line to verify these are in working order as well. 

<img src="Images/Vine/test_1.jpg" width="300" class="center-img"/> 



