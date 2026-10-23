#!/usr/bin/env python3
"""Publish the cut 23 October hero showcase using the existing animation viewer.

python tools/showcase.py <cut-folder> <ffmpeg-executable>
Keeps the source recording speed; creates 960px/24fps web copies and posters.
"""
import html
import json
from pathlib import Path
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

ROOT = Path(__file__).resolve().parents[1]
E = html.escape


def build(cut, ffmpeg):
    timeline = json.loads((cut / 'timeline-aligned.json').read_text(encoding='utf-8'))
    folder = ROOT / 'hero-showcase-20261023'
    folder.mkdir(exist_ok=True)
    entries = timeline['clips']

    def encode(c):
        if c.get('skipped'):
            return c
        sources = list(cut.glob(f"{c['index']:03d} *.mp4"))
        if len(sources) != 1:
            raise ValueError(f"Expected one source for entry {c['index']}")
        stem = f"{c['index']:03d}"
        dst = folder / (stem + '.mp4')
        poster = folder / (stem + '.jpg')
        if not dst.exists():
            subprocess.run([ffmpeg, '-v', 'error', '-y', '-i', str(sources[0]),
                            '-vf', 'fps=24,scale=960:-2', '-c:v', 'libx264',
                            '-crf', '23', '-preset', 'veryfast', '-threads', '2',
                            '-pix_fmt', 'yuv420p', '-an', '-movflags', '+faststart', str(dst)], check=True)
        if not poster.exists():
            subprocess.run([ffmpeg, '-v', 'error', '-y', '-ss',
                            str(min(1.5, (c['end']-c['start'])/2)), '-i', str(dst),
                            '-frames:v', '1', '-q:v', '3', str(poster)], check=True)
        return dict(c, file=dst.name, poster=poster.name)

    converted = list(ThreadPoolExecutor(max_workers=4).map(encode, entries))
    timeline['clips'] = converted
    timeline['publication'] = {
        'recorded': '2026-10-23', 'partial': True, 'ownerStoppedEarly': True,
        'captureSpeed': 'Hero batches use 0.35 simulation tick rate; visual clocks may differ.',
        'webWidth': 960, 'webFps': 24, 'speedChanged': False,
        'note': 'ok/camera fields are capture diagnostics, not visual acceptance.'}
    (folder / 'index.json').write_text(json.dumps(timeline, ensure_ascii=False, indent=2), encoding='utf-8')

    groups, pending = [], []
    for c in converted:
        if c.get('scene'):
            groups.append((c['label'], pending, c))
            pending = []
        else:
            pending.append(c)
    if pending:
        groups.append(('Masked guard binds — partial batch', pending, None))

    def card(c, summary=False):
        if c.get('skipped'):
            return f'<p><b>{E(c["label"])}</b> — not recorded: {E(c["skipped"])}</p>'
        notes = ['Batch overview'] if summary else []
        notes.append('Recorded in showcase slow motion')
        if c.get('recordingTruncatedStart'):
            notes.append('Recording begins mid-scene; opening is incomplete')
        if c['index'] == 3:
            notes.append('Layer demonstration only: real cast did not start the animation')
        desc = '. '.join(n for n in notes if n) + '.'
        prefix = folder.name + '/'
        return (f'<figure class="anim" data-n="{E((c["label"]+" "+desc).lower(), quote=True)}">'
                f'<div class="vw"><video src="{prefix}{c["file"]}" muted loop playsinline preload="none" '
                f'poster="{prefix}{c["poster"]}" aria-label="{E(c["label"], quote=True)}"></video>'
                '<button class="big" type="button" aria-label="Open large">&#x26F6;</button></div>'
                f'<figcaption><b>{E(c["label"])}</b><small>Entry {c["index"]:03d} · 23 October 2026</small>'
                f'<p>{E(desc)}</p></figcaption></figure>')

    out = ['<h1>Hand-crafted showcase</h1>',
           '<p class="lead">Recorded 23 October 2026: 190 individual technique clips and 24 batch overviews. '
           'This is a partial session, stopped before all animations ran.</p>',
           '<p>These are slow-motion demonstrations. The showcase slows game simulation to 0.35×; '
           'some visual effects use a different clock. Playback preserves the recording speed. '
           'Later, unrecorded animations have not been judged. Two techniques were skipped because their prerequisite was inactive.</p>',
           '<div class="toolbar"><input type="search" placeholder="Filter hand-crafted animations" '
           'aria-label="Filter animations" autocomplete="off" id="animq"></div>',
           '<div class="toc">' + ''.join(f'<a href="#batch-{i}">{E(name)}</a>' for i,(name,_,_) in enumerate(groups)) + '</div>']
    for i, (name, children, overview) in enumerate(groups):
        out.append(f'<h2 id="batch-{i}">{E(name)}</h2><div class="grid anims">')
        out.extend(card(c) for c in children)
        out.append('</div>')
        if overview:
            out.append('<details><summary>Watch batch overview</summary><div class="grid anims">' + card(overview, True) + '</div></details>')

    original = ROOT / 'index.html'
    shell = original.read_text(encoding='utf-8')
    viewer = re.search(r'<script>.*?</script>', shell, re.S).group(0)
    nav = '<nav><a href="index.html">Animations</a><a href="showcase.html" class=on>Hand-crafted showcase</a></nav>'
    page = re.sub(r'<nav>.*?</nav>', lambda _: nav, shell, count=1, flags=re.S)
    page = re.sub(r'<main>.*?</main>', lambda _: '<main>' + ''.join(out) + viewer + '</main>', page, count=1, flags=re.S)
    page = re.sub(r'<title>.*?</title>', '<title>Hand-crafted showcase · NFRP World</title>', page, count=1)
    page = re.sub(r'<meta name="description"[^>]*>', '<meta name="description" content="Partial slow-motion showcase of NFRP World hand-crafted animations, recorded 23 October 2026.">', page, count=1)
    (ROOT / 'showcase.html').write_text(page, encoding='utf-8')
    home_nav = '<nav><a href="index.html" class=on>Animations</a><a href="showcase.html">Hand-crafted showcase</a></nav>'
    original.write_text(re.sub(r'<nav>.*?</nav>', lambda _: home_nav, shell, count=1, flags=re.S), encoding='utf-8')
    print(f'Built showcase.html: {len(converted)} entries, {len(groups)} groups, 214 videos.', flush=True)


if __name__ == '__main__':
    build(Path(sys.argv[1]), sys.argv[2])
