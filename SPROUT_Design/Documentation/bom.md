# Bill of Materials (BOM)

This document lists the primary hardware components required to assemble the compute box for the SPROUT platform.

The BOM is organized by subsystem to simplify assembly, troubleshooting, and future hardware revisions.

---

# Overview

## Major Subsystems

The compute box consists of the following subsystems:

- Compute hardware
- Power distribution
- Embedded control electronics
- Communication interfaces
- Enclosure hardware
- Wiring 

---

# Compute Hardware

| Item | Qty | Manufacturer/Source | Part Number | Description | Notes |
|---|---|---|---|---|---|
| NVIDIA Jetson Nano | 1 | NVIDIA | -- | Main onboard computer | 4GB RAM 16G eMMC |
| Arduino Uno Rev3 | 1 | [Amazon](https://www.amazon.com/Arduino-A000066-ARDUINO-UNO-R3/dp/B008GRTSV6/) | -- | Low-level embedded controller | -- |
| 128 GB microSD Card | 1 | [Amazon](https://www.amazon.com/PNY-Premier-X-microSDXC-Memory-2-Pack/dp/B09WBT52KN/) | -- | -- | For Jetson Nano image |
| Dual-Mode Wireless NIC Module with Antennas | 1 | [Amazon](https://www.amazon.com/Wireless-AC8265-Wireless-Developer-Support-Bluetooth/dp/B07SM4SPLV) | -- | -- | -- |

---

# Power Distribution

| Item | Qty | Manufacturer/Source | Part Number | Description | Notes |
|---|---|---|---|---|---|
| DC-DC Buck Converter | 5 | [Amazon](https://a.co/d/7YLiOVz) | -- | -- | -- |
| Inline Fuse Holder | 5 | [Amazon](amazon.com/Nilight-NI-FH01-Automotive-Holder-10-Warranty/dp/B07426WCLM/) | -- | -- | -- |
| Blade Fuse Kit | 1 | [Amazon](https://www.amazon.com/gp/aw/d/B0B18W5WGB/) | -- | -- | -- |
| M18  Battery | 1 | [Amazon](https://www.amazon.com/dp/B0C9TL93P4) | B0C9TL93P4 | -- | -- |
| Battery Adapter | 1 | [Amazon](https://www.amazon.com/Upgrade-Adapter-Milwaukee-Connector-Robotics/dp/B097JPSFKG?th=1) | -- | -- | -- |
| DC Barrel Plug to Bare Wire Cable | 2 | [Amazon](https://www.amazon.com/Fancasee-Replacement-Degree-Pigtail-Supply/dp/B081TXY6ML) | -- | For Power Adapter use instead of batteries | -- |
| Emergency Stop Switch | 1 | [Mouser](https://mou.sr/42U3Vo7) | 123-84-5220.0020 |---|---|
| Push Button Switch | 1 | [Amazon](https://www.amazon.sg/DMWD-Latching-Waterproof-Terminals-Aluminium/dp/B0BJ637Z3H) | B0BJ637Z3H | -- |--|
|Push Button Cover| 1 | [Amazon](https://www.amazon.sg/Transparent-Switches-Protector-Mounting-Double-Sided/dp/B0CM5W3PBS) | B0CM5W3PBS |---|---|
|Plastic Submersible Cord Grip/Gland|1|[McMaster-Carr](https://www.mcmaster.com/69915K54/) |69915K54|---|---|
---

# Embedded Control Electronics

| Item | Qty | Manufacturer/Source | Part Number | Description | Notes |
|---|---|---|---|---|---|
| DC Motor Driver | 1 | [Cytron](https://www.cytron.io/p-10amp-5v-30v-dc-motor-driver-2-channels?srsltid=AfmBOoqLlEKV7RdCk8bj8ulY_xR6eksgS2bsN1FIhOsCGok0lpGYtu23) | MDD10A | -- | -- |
| Custom Arduino Shield PCB | 1 | Custom | -- | Interface breakout board | Mounted on Arduino |
| QB3 Pressure Regulators | 4 | [ProportionAir](https://proportionair.com/product/qb3/?srsltid=AfmBOopWVfBzKiqhEIHj34tvOh7SmVpA9b6pAgFK551bGtBSLAs6F036) | -- | Pneumatic pressure regulation | -- |
| Solenoid Valve 3/2 NC | 1 | [U.S. Solid](https://ussolid.com/products/u-s-solid-1-4-3-way-2-position-pneumatic-electric-solenoid-valve-dc-12-v-html) | -- | -- | -- |

---

# Pneumatics

| Item | Qty | Manufacturer/Source | Part Number | Description | Notes |
|---|---|---|---|---|---|
| 1/2" Polyurethane Tubing | 2 ft | McMaster-Carr | 5648K78 |--|--|
| 1/4" Polyurethane Tubing | 5 ft | McMaster-Carr | 5648K25 |--|--|
| 1/4" Pipe Nipples, 3" Long | 5 | McMaster-Carr | 46755K42 |--|--|
| 1/2" Push-to-Connect Fitting Plug | 1 | [Amazon](https://www.amazon.com/dp/B08D6LFY9S) | B08D6LFY9S | --- | Plugs for testing/troubleshooting pneumatics |
| 1/4" Push-to-Connect Fitting Plug | 1 | [Amazon](https://www.amazon.com/HJGarden-Connect-Fitting-Pneumatic-Connector/dp/B09FLG61BX/) | B09FLG61BX | --- | Plugs for testing/troubleshooting pneumatics |
|1/4" Push-to-Connect OD x 1/4" NPT Thread Tee | 1 (Pack of 10) | [Amazon](https://www.amazon.com/dp/B07RY31QH5) | B07RY31QH5 |---|---|
|1/4" Push-to-Connect OD Elbow | 1 (Pack of 10) | [Amazon](https://www.amazon.com/dp/B0B3X2CY13) | B0B3X2CY13 |---|---|
|1/4" Push-to-Connect OD x 1/4" NPT Thread Elbow | 1 (Pack of 10) | [Amazon](https://www.amazon.com/dp/B07GLH22HV) | B07GLH22HV |---|---|
|1/4" Push-to-Connect OD x 1/4" NPT Female|3|[McMaster-Carr](https://www.mcmaster.com/5779K131/)|5779K131|---|---|
|1/2" Push-to-Connect OD x 1/4" NPT Female|1|[McMaster-Carr](https://www.mcmaster.com/5779K445/)|5779K445|---|---|
| 1/4" NPT Female, Quick Connect Air Coupler | 1 (pack of 10) | [Amazon](https://www.amazon.com/dp/B0C6K1CYN7?th=1) |---|---|
| 1/4" NPT Female, Quick Connect Air Plug | 1 (pack of 10) | [Amazon](https://www.amazon.com/dp/B08M3VLL4D) | B08M3VLL4D |---|---|
|Through-Wall Adapter, for 1/4" Tube OD Push-to-connect x 1/4 NPT Female|1|[McMaster-Carr](https://www.mcmaster.com/5779K272/)|5779K272|---|---|
|Check Valve, 1/4 NPT Female x NPT Male|1|[McMaster-Carr](https://www.mcmaster.com/7768K22/)|7768K22|---|---|
|Straight Adapter, for 1/4" Tube OD push-to-connect x 1/4 NPT Male|2|[McMaster-Carr](https://www.mcmaster.com/5779K109/)|5779K109|---|---|



---

# Communication Interfaces and Peripherals

| Item | Qty | Manufacturer/Source | Part Number | Description | Notes |
|---|---|---|---|---|---|
| USB Connector Panel-Mount | 2 | [Amazon](https://a.co/d/8kQKNGa) | --- | External USB access | --- |
| USB 3.0 Cable 1ft Long, A-to-A, Male-to-Male | 2 | [Amazon](https://www.amazon.com/SUNGUY-USB-Cable-Type-Male/dp/B0FB3WJSN5/) | -- | -- | -- |
| DisplayPort to HDMI Cable, 3ft Long | 1 | [Amazon](https://www.amazon.com/Amazon-Basics-Uni-Directional-DisplayPort-Display/dp/B015OW3GJK?th=1) | B015OW3GJK |---|---|
| HDMI Connector Panel-Mount | 1 | [Amazon](https://a.co/d/hMF2q71) | B0CM386VJ3 |---|---|
| RJ45 Connector Panel-Mount | 1 | [Amazon](https://www.amazon.com/dp/B0C6PPZCV3) | B0C6PPZCV3 |---|---|
| Ethernet Extension Cable 1ft Female-to-Male | 1 | [Amazon](https://www.amazon.com/XANHAM-Ethernet-Extension-Extender-Connector/dp/B0CQ8F4CZX/) | B0CQ8F4CZX |---|---|
| 6-pole Receptacle Connector|1|[McMaster-Carr](https://www.mcmaster.com/8903T45/)|8903T45|---|---|
| 6-pole Plug Connector|1|[McMaster-Carr](https://www.mcmaster.com/8903T15/)|8903T15|---|---|
|15" LCD Display|1|[Amazon](https://www.amazon.com/VSDISPLAY-1024X768-G150XGE-1000-Brightness-Controller/dp/B0BFRF126F)|B0BFRF126F|---|---|
| LCD1602 Display Module | 1 | [Amazon](https://www.amazon.com/SunFounder-Serial-Module-Display-Arduino/dp/B019K5X53O?th=1)| B019K5X53O | --- | --- | 
| Right Angle USB A to USB B male connector | 1 | [Amazon](https://www.amazon.com/YCS-Basics-Black-Printer-Scanner/dp/B00B5HS7TI/) | B00B5HS7TI | 1 | 1 |

---

# Enclosure Hardware

| Item | Qty | Manufacturer/Source | Part Number | Description | Notes |
|---|---|---|---|---|---|
| NANUK 930 Empty Case | 1 | [Nanuk Cases](https://nanukcases.ca/products/nanuk-930-empty) | 930S-000BK-0A0 | Main compute box enclosure | -- |
| ABS Mounting Plate for Junction Box | 1 | [Amazon](https://www.amazon.com/LeMotech-Junction-Mounting-Installation-Electrical/dp/B0CGCS2C4B?th=1) | B0CGCS2C4B | -- | -- |
| 3D Printed Attachments | TBD | TBD | TBD | -- | -- |
|Pull Handle|2|[McMaster-Carr](https://www.mcmaster.com/1568A64/)|1568A64|---|---|
|M5 Plastic-Head Thumb Screws | 1 (pack of 10)|[McMaster-Carr](https://www.mcmaster.com/96016A566-96016A237/)|96016A566-96016A237|---|---|


---

# Wiring

| Item | Qty | Manufacturer/Source | Part Number | Description | Notes |
|---|---|---|---|---|---|
| 16 AWG Wire | 1 roll | [Amazon](https://www.amazon.sg/NAOEVO-Conductors-Electrical-Extension-Automotive/dp/B0CP1SGHK7?th=1) | -- | Main power wiring | Red/black |
| 22 AWG Wire | 1 kit | [Amazon](https://www.amazon.com/Electric-Flexible-Silicone-different-Electronic/dp/B07G2JWYDW?th=1) | B07G2JWYDW | Signal wiring | -- |
| Heat Shrink Tubing | 1 kit | [Amazon](https://www.amazon.com/Eventronic-Shrink-Adhesive-Industrial-Heat-Shrink/dp/B0DK34NL18/) | B0DK34NL18 | --- | Multiple diameters |
| Expandable Braided Cable Sleeve Kit | 1 kit | [Amazon](https://www.amazon.com/Expandable-Sleeving-Automotive-Sheathing-Management/dp/B0F6YLMR18?th=1) | B0F6YLMR18 | Cable insulation | Multiple diameters |
| Lever Wire Electrical Connector Kit | 1 kit | [Amazon](https://www.amazon.com/dp/B07SFCCPZ6) | B07SFCCPZ6 |---|---|
| JST-HX Connectors | 1 kit | [Amazon](https://www.amazon.com/Taiss-560PCS-Connector-Adapter-Housing/dp/B09ZTWCZ3K/) | B09ZTWCZ3K | --- | --- |
| XT60 Connector | TBD | TBD | TBD | Battery connector | Optional |



---

# Fasteners

| Item | Qty | Manufacturer/Source | Part Number | Description | Notes |
|---|---|---|---|---|---|
| Metric Screw Assortment | 1 | [Amazon](https://www.amazon.com/dp/B0CBMMPPKF) | B0CBMMPPKF | -- | -- |
| Heat-set Insert (Metric) Assortment | 1 | [Amazon](https://www.amazon.com/FFVRVSS-M2-M3-Threaded-Inserts/dp/B0FWCF14RN) | B0FWCF14RN | -- | -- |
| M3 Standoff Spacers Kit | 1 kit | [Amazon](https://www.amazon.com/Csdtylh-Male-Female-Standoff-Stainless-Assortment/dp/B06Y5TJXY1/) | B06Y5TJXY1 | ---| --- |

---

# Miscellaneous 

| Item | Qty | Manufacturer/Source | Part Number | Description | Notes |
|---|---|---|---|---|---|
| Two-Part Clear Epoxy | 1 | [Gorilla (Amazon)](https://www.amazon.com/Gorilla-Epoxy-Minute-Ounce-Syringe/dp/B001Z3C3AG?th=1) | B01M7VD07W |---|---|
| Loctite Super Glue Pro | 1 | [Loctite (Amazon)](https://www.amazon.com/Loctite-Liquid-Professional-Super-Glue/dp/B07VL6MP94?th=1) | B07VL6MP94 |---|---|
| Velcro 1in Straps | 1 | [Amazon](https://www.amazon.com/dp/B09QH2NVM1) | B09QH2NVM1 |---|---|
| Zip Ties | 1 | [Amazon](https://www.amazon.com/HAVE-ME-TD-Cable-Ties/dp/B08TVLYB3Q)| B08TVLYB3Q|---|---|
| Adhesive Zip Tie Mount | 1 | [Amazon](https://www.amazon.com/dp/B07M69LK65)| B07M69LK65 |---|---|

# Recommended Spare Components

The following spare components are recommended for field deployment:
- Extra buck converters
- Spare fuses
- Spare connectors
- Extra robot bodies
- Tape

---

# Notes

Where possible:
- use locking connectors,
- use waterproof feedthroughs for external connections,
- maintain consistent connector labeling.

---

# Revision History

| Revision | Date | Notes |
|---|---|---|
| A | 2026-05-20 | Initial BOM draft |