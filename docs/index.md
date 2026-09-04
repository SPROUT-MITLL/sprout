---
title: Home
layout: home
nav_order: 1
permalink: /
---

{: .fs-9 }

<!-- <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; margin-bottom: 1.5rem;">
  <iframe src="https://www.youtube.com/embed/DaMCTH4qZTE" title="SPROUT overview video" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div> -->

<i>An open-source, open-hardware soft robot platform for search and rescue and confined space operations.</i>
{: .fs-6 .fw-300 }

[Get started with Documentation]({{ site.baseurl }}/documentation/){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[View the repository on GitHub](https://github.com/SPROUT-MITLL/sprout){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## What is SPROUT?

SPROUT is a fully open-source, open-hardware soft robot built for search-and-rescue
applications. It pairs a pneumatically-actuated "vine robot" body with a
field-deployable compute box that handles onboard computation, power
regulation, actuator control, sensing, and networking.

Everything needed to build your own SPROUT — mechanical CAD, PCB designs, bills
of materials, assembly instructions, and the full software/ROS 2 stack — is
released here under the MIT license.

## Site Map

This site mirrors the folder structure of the [`SPROUT_Design`]({{ site.github_tree }}/SPROUT_Design) directory in the repository, so every page here has a matching source folder you can browse, clone, or download.

| Section | What's inside | Source folder |
|---|---|---|
| [Documentation]({{ site.baseurl }}/documentation/) | Bill of materials, enclosure prep, assembly, and wiring guides for the compute box | [`SPROUT_Design/Documentation`]({{ site.github_tree }}/SPROUT_Design/Documentation) (photos and BOM spreadsheet only — guides are authored directly on this site) |
| [CAD]({{ site.baseurl }}/cad/) | SolidWorks/STEP models for the compute box and robot base | [`SPROUT_Design/CAD`]({{ site.github_tree }}/SPROUT_Design/CAD) |
| [Electronics]({{ site.baseurl }}/electronics/) | Custom Arduino shield PCB (KiCad project, gerbers, schematics) | [`SPROUT_Design/Electronics`]({{ site.github_tree }}/SPROUT_Design/Electronics) |
| [Software]({{ site.baseurl }}/software/) | Jetson bootstrap guide and the `sprout_ros` ROS 2 stack | [`SPROUT_Design/Code`]({{ site.github_tree }}/SPROUT_Design/Code) |

## Getting Help

Have a question, run into an issue building your own SPROUT, or spot something
that needs fixing in the docs? [Open an issue on
GitHub](https://github.com/SPROUT-MITLL/sprout/issues) — it's the best way to
reach the team and helps other builders who run into the same thing.

## Citation

A paper describing SPROUT is planned for release on [arXiv](https://arxiv.org/). If you use SPROUT in your research, please cite it using the entry below.

{: .note }
> This citation is a placeholder and will be updated with the final author list and arXiv identifier once the paper is posted.

```bibtex
@misc{sprout2026,
  title         = {SPROUT: An Open-Source, Open-Hardware Soft Robot for Search and Rescue},
{% comment %}
  author        = {Antonio Alvarez Valdivia, Ciera McFarland, Robert Reeve, Ankush Dhawan, Chad Council, Megan Richardson, Margaret McGuinness, and Nathaniel Hanson},
{% endcomment %}
  author        = {Authors withheld for double-blind review},
  year          = {2026},
  eprint        = {TODO: arXiv ID},
  archivePrefix = {arXiv},
  primaryClass  = {cs.RO},
  url           = {https://arxiv.org/abs/TODO}
}
```

## License

SPROUT is released under the [MIT License]({{ site.github_blob }}/LICENSE).

---

## Team

> Team and affiliation information withheld for double-blind review.

{% comment %}
<style>
  .team-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 2rem;
    margin: 1.5rem 0 2rem;
  }
  .team-member {
    width: 140px;
    text-align: center;
  }
  .team-member img {
    width: 120px;
    height: 120px;
    object-fit: cover;
    border-radius: 50%;
    display: block;
    margin: 0 auto 0.6rem;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
    background-color: #eaf5ec;
  }
  .team-member .team-name {
    font-weight: 600;
    font-size: 0.95rem;
  }
  .team-member .team-role {
    font-size: 0.8rem;
    color: #5c5962;
  }
</style>

<!-- Add one .team-member block per collaborator; headshots live in assets/images/team/ -->
<div class="team-grid">
  <div class="team-member">
    <img src="{{ site.baseurl }}/assets/images/team/Nathaniel_Hanson.jpg" alt="Nathaniel Hanson">
    <div class="team-name">Nathaniel Hanson</div>
    <div class="team-role">Principal Investigator, MIT Lincoln Laboratory</div>
  </div>
  <div class="team-member">
    <img src="{{ site.baseurl }}/assets/images/team/Antonio_Alvarez_Valdivia.jpg" alt="Antonio Alvarez Valdivia">
    <div class="team-name">Antonio Alvarez Valdivia</div>
    <div class="team-role">MIT Lincoln Laboratory</div>
  </div>
  <div class="team-member">
    <img src="{{ site.baseurl }}/assets/images/team/Ankush_Dhwan.jpg" alt="Ankush Dhwan">
    <div class="team-name">Ankush Dhwan</div>
    <div class="team-role">MIT Lincoln Laboratory</div>
  </div>
  <div class="team-member">
    <img src="{{ site.baseurl }}/assets/images/team/Chad_Council.png" alt="Chad Council">
    <div class="team-name">Chad Council</div>
    <div class="team-role">MIT Lincoln Laboratory</div>
  </div>
  <div class="team-member">
    <img src="{{ site.baseurl }}/assets/images/team/Ciera_McFarland.jpg" alt="Ciera McFarland">
    <div class="team-name">Ciera McFarland</div>
    <div class="team-role">University of Notre Dame</div>
  </div>
  <div class="team-member">
    <img src="{{ site.baseurl }}/assets/images/team/Margaret_McGuinness.jpg" alt="Margaret McGuinness">
    <div class="team-name">Margaret McGuinness</div>
    <div class="team-role">University of Notre Dame</div>
  </div>
  <div class="team-member">
    <img src="{{ site.baseurl }}/assets/images/team/Megan_Richardson.jpg" alt="Megan Richardson">
    <div class="team-name">Megan Richardson</div>
    <div class="team-role">MIT Lincoln Laboratory</div>
  </div>
  <div class="team-member">
    <img src="{{ site.baseurl }}/assets/images/team/Robert_Reeve.png" alt="Robert Reeve">
    <div class="team-name">Robert Reeve</div>
    <div class="team-role">MIT Lincoln Laboratory</div>
  </div>
</div>

<div style="display: flex; align-items: center; justify-content: center; gap: 3rem; flex-wrap: wrap; margin: 2rem 0 1rem;">
  <a href="https://www.nd.edu" target="_blank" rel="noopener"><img src="{{ site.baseurl }}/assets/images/notre-dame.png" alt="University of Notre Dame" height="60"></a>
  <a href="https://www.ll.mit.edu" target="_blank" rel="noopener"><img src="{{ site.baseurl }}/assets/images/mit-ll.png" alt="MIT Lincoln Laboratory" height="60"></a>
</div>
<p style="text-align: center; font-size: 0.85rem; color: #5c5962; margin-bottom: 2rem;">A joint project of the University of Notre Dame and MIT Lincoln Laboratory.</p>
{% endcomment %}

## Distribution Statement

DISTRIBUTION STATEMENT A. Approved for public release. Distribution is unlimited.
This material is based upon work supported by the Department of the Air Force under Air Force Contract No. FA8702-15-D-0001 or FA8702-25-D-B002. Any opinions, findings, conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the Department of the Air Force.
{% comment %}© 2026 Massachusetts Institute of Technology.{% endcomment %}
© 2026 [Institution redacted for double-blind review].

Subject to FAR52.227-11 Patent Rights - Ownership by the contractor (May 2014)
Delivered to the U.S. Government with Unlimited Rights, as defined in DFARS Part 252.227-7013 or 7014 (Feb 2014). Notwithstanding any copyright notice, U.S. Government rights in this work are defined by DFARS 252.227-7013 or DFARS 252.227-7014 as detailed above. Use of this work other than as specifically authorized by the U.S. Government may violate any copyrights that exist in this work.
