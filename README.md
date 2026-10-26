# NFRP World: animations

The animations wiki for the RimWorld mod NFRP World: recorded in-game clips of the hand-made technique animations, art trials and the shared effects.
`index.html` is the site (a plain static page for GitHub Pages: Settings > Pages > Deploy from a branch > main / root).
The main wiki is https://cassiegiang.github.io/NFRP-World-Wiki/

## Tabs and folders

| Tab | Page | Folder | What |
| --- | --- | --- | --- |
| Animations | `index.html` | `clans-and-styles/` | 162 clips (the nine major clans, ANBU, Red Leg, Busosen and Kenseijin), replaced on 26 October 2026 with the matching clips of the 00:23 hero run (update 260). Each technique has a looping silent `.mp4` and a `.jpg` poster. `index.json` lists them in play order |
| Hand-crafted showcase | `showcase.html` | `hero-showcase/` | The full hero showcase recorded 26 October 2026 00:23 on update 260: 226 techniques in 29 batches, with a comment box per technique |
| Art trials | `art-trials.html` | `art-trials/` | Side-by-side options for new art before it goes in (Great Fireball A to E; E is installed) |
| Generic effects | `generic-effects.html` | `generic-effects/` | All 252 shared effect visuals (painted flipbooks, barrier rings, element pieces, particles and marks, soft sprites, overlays and bolts), where each is used, with comment boxes |

Comment boxes are saved in the viewer's browser per page; "Download comments" saves them as a text file to hand to Claude.

The Kazeraikou clan was created by Marii from NFRP and is used with her permission.

## Updating

- `tools/showcase.py <cut-folder> <mod Defs folder> <date>` builds the Hand-crafted showcase page from a cut run.
- `tools/animations.py` and `tools/animations.json` build the Animations tab and its clip list.
- `tools/art_trial.py` builds Art trials; `tools/generic_fx.py` builds Generic effects.
- `tools/hero_review.py` and `tools/qa_showcase.py` built the removed "Showcase: hero animations" and "Showcase QA 24 Oct" tabs. Don't run them unless those tabs should come back.
