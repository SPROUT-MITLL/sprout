---
layout: default
title: CAD
nav_order: 3
has_children: true
permalink: /cad/
---

# CAD
{: .no_toc }

Source: [`SPROUT_Design/CAD`]({{ site.github_tree }}/SPROUT_Design/CAD)
{: .label .label-green }

Mechanical design files for SPROUT, authored in SolidWorks with STEP exports
for interchange with other CAD tools. Files are binary and are not rendered
inline on this site — follow the links below to view file details on GitHub
or clone the repository to open them locally.

| Folder | Description |
|---|---|
| [New Compute Box]({{ site.baseurl }}/cad/new-compute-box.html) | Full compute box design: enclosure mounts, electropneumatic hardware, power electronics, connectors, and robot-base interface |
| [New Base CAD]({{ site.baseurl }}/cad/new-base-cad.html) | Companion CAD set for the robot base revision paired with the compute box |

## Working with these files

- **SolidWorks** (`.SLDPRT`, `.SLDASM`, `.SLDDRW`) — open directly in SolidWorks. Top-level assemblies are the `.SLDASM` files.
- **STEP** (`.STEP`/`.step`) — neutral format importable into any major CAD package (SolidWorks, Fusion 360, OnShape, FreeCAD, etc.).
- Clone the repository to get all files at once:

```bash
git clone https://github.com/SPROUT-MITLL/sprout.git
```
