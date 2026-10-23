# NFRP World: animations

The animations wiki for the RimWorld mod NFRP World: recorded in-game clips of every hand-made technique animation.
`index.html` is the site (a plain static page for GitHub Pages: Settings > Pages > Deploy from a branch > main / root).
The main wiki is https://cassiegiang.github.io/NFRP-World-Wiki/

## Folders

- `hero-showcase/`: the full hand-crafted hero showcase recorded 23 October 2026 after update 175 (226 techniques in 29 batches, slow motion, zoomed 1280x720 cuts from the 4K recording, plus each batch as recorded). Page: `showcase.html`, built by `tools/showcase.py <cut-folder> <mod Defs folder> <date>`.
- `clans-and-styles/`: 162 clips (the nine major clans, ANBU, Red Leg, Busosen and Kenseijin), recorded
  22 October 2026. Each technique has a looping silent `.mp4` (960 px wide, 24 fps) and a `.jpg` poster frame.
  `index.json` lists them in play order with their group, technique tree and file names.

The Kazeraikou clan was created by Marii from NFRP and is used with her permission.

## Updating
`tools/animations.py` and `tools/animations.json` are the page generator and the clip list (moved here from the main wiki).

