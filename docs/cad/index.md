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
for interchange with other CAD tools. Individual part files are binary and
are not rendered inline — follow the links on the pages below to view file
details on GitHub or clone the repository to open them locally.

| Folder | Description |
|---|---|
| [Compute Box]({{ site.baseurl }}/cad/new-compute-box.html) | Full compute box design: enclosure mounts, electropneumatic hardware, power electronics, connectors, and robot-base interface |
| [Base CAD]({{ site.baseurl }}/cad/new-base-cad.html) | Robot base design: the motorized reel mechanism that houses, drives, and everts the vine body |

## 3D preview

The full SPROUT assembly (compute box + robot base) can be previewed directly in the browser.

{% assign step_url = site.github_raw | append: "/SPROUT_Design/CAD/STEP/SPROUT_assembly.STEP" %}
{% include step_viewer.html url=step_url name="SPROUT assembly" %}

<script type="module" src="{{ site.baseurl }}/assets/js/step-viewer.js"></script>

## Working with these files

- **SolidWorks** (`.SLDPRT`, `.SLDASM`, `.SLDDRW`) — open directly in SolidWorks. Top-level assemblies are the `.SLDASM` files.
- **STEP** (`.STEP`/`.step`) — neutral format importable into any major CAD package (SolidWorks, Fusion 360, OnShape, FreeCAD, etc.).
- Clone the repository to get all files at once:

```bash
git clone https://github.com/SPROUT-MITLL/sprout.git
```
