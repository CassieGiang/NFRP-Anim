# NFRP World: animations

The animations wiki for the RimWorld mod NFRP World: recorded in-game clips of every hand-made technique animation.
`index.html` is the site (a plain static page for GitHub Pages: Settings > Pages > Deploy from a branch > main / root).
The main wiki is https://cassiegiang.github.io/NFRP-World-Wiki/

## Folders

- `hero-showcase-20261023/`: the partial hero-animation session recorded 23 October 2026. The **Hand-crafted showcase** tab (`showcase.html`) contains 190 individual clips and 24 overlapping batch overviews, plus explanations for two prerequisite skips. Web copies are 960 px wide at 24 fps and preserve the recording speed. The owner intentionally stopped before all animations ran. Hero batches use 0.35× simulation speed; visual-effect clocks may differ. These clips are diagnostic evidence, not a completed visual acceptance pass.
- `clans-and-styles/`: 162 clips (the nine major clans, ANBU, Red Leg, Busosen and Kenseijin), recorded
  22 October 2026. Each technique has a looping silent `.mp4` (960 px wide, 24 fps) and a `.jpg` poster frame.
  `index.json` lists them in play order with their group, technique tree and file names.

The Kazeraikou clan was created by Marii from NFRP and is used with her permission.

## Updating
`tools/animations.py` and `tools/animations.json` are the page generator and the clip list (moved here from the main wiki).

`tools/showcase.py <cut-folder> <ffmpeg-executable>` builds the new tab and web media from the calibrated local cuts. `hero-showcase-20261023/index.json` retains the timeline entries, skipped-scene warnings and calibration notes. Entry 1 and batch overview 7 have incomplete openings; entry 3 demonstrates the layer without proving real-cast triggering.
