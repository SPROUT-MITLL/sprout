# Enclosure Preparation and Mounting Layout

This document describes the preparation and mounting layout of the compute box enclosure used in the SPROUT robotic platform. The enclosure integrates compute hardware, power electronics, communication interfaces, and electropneumatic control hardware while maintaining portability and environmental protection.

The mounting architecture was designed to:
- preserve enclosure waterproofing,
- minimize permanent enclosure modification,
- support modular servicing,
- and allow repeatable assembly.

<style>
  .center-img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 50%; /* Optional: controls the width of the image */
  }
</style>

---

# Primary Components

| Component | Manufacturer/Source | Link |
|---|---|---|
| NANUK 930 Empty Case | NANUK | [Link](https://nanukcases.ca/products/nanuk-930-empty) |
| ABS Mounting Plate for Junction Box | Amazon | [Link](https://www.amazon.com/LeMotech-Junction-Mounting-Installation-Electrical/dp/B0CGCS2C4B) |

The ABS mounting plate serves as the primary internal mounting surface for compute hardware, power electronics, and electropneumatics.

---

# Provided CAD Files

The repository includes STL files and CAD assemblies for all mounting components.

---

# General Enclosure Preparation

Prior to any mounting or adhesive bonding operations, the enclosure interior should be cleaned thoroughly.

Recommended procedure:

1. Remove all foam inserts and debris from the enclosure.
2. Wipe internal surfaces using isopropyl alcohol (IPA).
3. Allow all surfaces to dry completely before proceeding.

Before adhesive bonding, all bonding regions should be lightly roughened using sandpaper and cleaned again using IPA.

---

# Internal Mounting System

## Mounting Plate Design

Custom corner brackets were designed to secure the ABS mounting plate to the enclosure interior. These brackets are custom 3D printed and conform directly to the interior geometry of the NANUK 930 enclosure.

To ensure accurate fitment, the enclosure interior surface CAD model was obtained from the manufacturer and imported into SolidWorks. The mounting brackets were designed directly against the enclosure geometry to maximize bonding area, maintain mounting plate alignment, and minimize internal stress during assembly.

Each corner bracket contains M5 heat-set threaded inserts that interface directly with the ABS mounting plate hardware. STL files for all mounting components are provided in the repository (see XXXXXXX). Install the heat-set inserts to the brackets before adhering them to the case.

<img src="Images/Enclosure/mounting_plate.jpg" alt="Corner Mount Overview" width="500" class="center-img"/>

*Figure 1. Internal corner mounting brackets used to secure the mounting plate.*

---

## Bonding Procedure

The corner mounting brackets are permanently attached to the enclosure using two-part clear epoxy.

Recommended procedure:

1. Prepare epoxy according to manufacturer instructions.
2. Apply epoxy evenly to the bonding surfaces of each corner bracket.
3. Position the bracket within the enclosure corners.
4. Verify mounting plate alignment before curing.
5. Allow full adhesive cure prior to mechanical loading.

<img src="Images/Enclosure/corner_mounts.jpg" alt="Bonded Corner Mounts" width="500" class="center-img"/>

*Figure 2. Epoxied internal mounting brackets with integrated heat-set inserts.*

---

## Top Interface Plate Mounts

Additional custom 3D printed brackets are used to support the top acrylic interface plate. These mounting brackets were designed using the same enclosure interior CAD geometry and use the same epoxy bonding procedure described previously. There are 4 of these brackets, one for each corner.

The brackets contain M5 heat-set threaded inserts and support the acrylic interface plate used for external connectors, display hardware, user interface peripherals, and power switches (see XXXXXXX).

<img src="Images/Enclosure/top_plate_mounts.jpg" alt="Top interface plate mounting system" width="500" class="center-img"/>

*Figure 3. Top interface plate mounting system.*

<img src="Images/Enclosure/top_plate_mounts_2.jpg" alt="Top interface plate mounting system" width="500" class="center-img"/>

*Figure 4. Top interface plate and mounting plate brackets.*

---

# External Robot Mounting System

Additional external mounting hardware was designed to allow the compute box to interface mechanically with the robot body. The mounting system is attached to the underside of the enclosure and allows the compute box to remain securely seated on the cylindrical body structure of the robot.

<img src="Images/Enclosure/robot_mount.jpg" alt="External robot mounting assembly attached to the underside of the enclosure." width="500" class="center-img"/>

*Figure 5. External robot mounting assembly attached to the underside of the enclosure.*

Unlike the enclosure interior geometry, the exterior shell CAD for the NANUK 930 enclosure was not available from the manufacturer. As a result, the external mounting system was developed through manual measurements and iterative CAD refinement. The geometry was adjusted through repeated test fitting to achieve stable seating, proper enclosure fitment, and sufficient clearance for enclosure hardware and interfaces.

---

## Mounting Assembly

The robot mounting assembly consists of:
- a primary mounting bracket bonded directly to the enclosure,
- an adjustment bracket with slotted mounting hole,
- and a curved support foot assembly.

The primary mounting brackets are custom 3D printed and bonded to the enclosure underside using two-part epoxy. These brackets contain heat-set threaded inserts that provide the structural interface for the remaining mounting hardware.

The adjustment plates allow lateral positioning and alignment tuning relative to the robot body. The curved support feet were designed to match the cylindrical profile of the robot and improve seating stability during operation.

<img src="Images/Enclosure/robot_mount_assembly.png" alt="External robot mounting brackets and support feet assembly." width="500" class="center-img"/>

*Figure 6. External robot mounting brackets and support feet assembly.*

First, 3D-print the primary bracket mounts (4), install M5 heat-inserts, and epoxy them to the bottom of the case.

<img src="Images/Enclosure/robot_mount_part_1.jpg" alt="Primary brackets epoxied to the bottom of the case." width="500" class="center-img"/>

*Figure 7. Primary brackets epoxied to the bottom of the case.*

Then, 3D-print and assemble the curved foot assembly (2 sets). It is composed of two parts that slide and attach together. A few drops of SuperGlue around the inner edges of the parts will make sure the parts are bonded strongly. 

Next, 3D-print the adjusment brackets (4) and install M5 het-set inserts. Then, use M5 fasteners to attach these to the foot assembly.

<img src="Images/Enclosure/robot_mount_part_2.jpg" alt="Curved foot assembly attached to the adjustment brackets." width="500" class="center-img"/>

*Figure 8. Curved foot assembly attached to the adjustment brackets.*

Lastly, use M5 fasteners to attach the aasembly to the primary mounting brackets. 

<img src="Images/Enclosure/robot_mount_assembly_full.jpg" alt="Installed external robot mounting assembly." width="500" class="center-img"/>

*Figure 9. Installed external robot mounting assembly.*


---

## Screen Mounting Assembly
The last step in preparing the enclosure is to attach mounting structure for installing a screen. This screen is to be placed inside the lid of the case, so that when the case is opened, the user can see the peripherals panel in the bottom and the screen in the lid, like a laptop.

<img src="Images/Enclosure/end_product.jpg" alt="Peripheral panel and screen." width="500" class="center-img"/>

First, 3D print the screen mounting brackets, provided in the CAD. These were designed using the inner shell of the case so that they perfectly rest on the feautres of the inner wall of the lid. Depending on your 3D-printer bed size, you may need to cut these into two section so it fits in the build plates, as shown below. 

<img src="Images/Enclosure/screen_mounting_1.jpg" alt="3D-printed screen mounting brackets." width="500" class="center-img"/>

Install M5 heat-set inserts in the holes (two on each bracket). Adhere the brackets to the case using epoxy, lining the printed parts with the wall features, and resting in the bottom of the lid. The end product should look as below. 

<img src="Images/Enclosure/screen_mounting_2.jpg" alt="Installed screen brackets." width="500" class="center-img"/>

<!-- Following enclosure preparation, the next assembly stages include:

1. Mounting plate installation
2. Power subsystem installation
3. Compute hardware installation
4. Wiring and connector routing
5. Peripheral integration
6. Final enclosure validation -->