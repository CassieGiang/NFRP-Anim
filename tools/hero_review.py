#!/usr/bin/env python3
"""Publish a cut "Showcase: hero animations" run on its own tab, with a comment box under every technique.

python3 tools/hero_review.py <cut-folder> <mod-defs-folder> <date YYYY-MM-DD>
<cut-folder> holds NNN.mp4 + NNN.jpg (zoomed web cuts, one per timeline entry) and timeline.json (the showcase timeline).
Clips go to hero-animations/, the page to hero-animations.html; comments autosave in the viewer's browser and save to one text file; each card gets the technique's description and rank from the mod's Defs.
"""
import html, json, re, shutil, sys, glob, os
import xml.etree.ElementTree as ET
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
E = html.escape

def defs_info(defs):
    desc, tree, tierlab = {}, {}, {}
    for f in glob.glob(os.path.join(defs, '**', '*.xml'), recursive=True):
        try: r = ET.parse(f).getroot()
        except ET.ParseError: continue
        for d in r:
            dn = d.findtext('defName')
            if not dn: continue
            t = d.tag.split('.')[-1]
            if t == 'AbilityDef': desc[dn] = (d.findtext('description') or '').strip()
            elif t == 'AbilityTreeDef': tree[dn] = (d.findtext('label') or '').strip()
            elif t == 'AbilityTierDef': tierlab[dn] = (d.findtext('label') or '').strip()
    return desc, tree, tierlab

RANK = re.compile(r'^(?:(?:SS|S|A|B|C|D|E)-rank(?: passive)?[.:,;]?\s*)+', re.I)

def build(cut, defs, date):
    tl = json.loads((cut / 'timeline.json').read_text(encoding='utf-8'))
    desc, trees, tiers = defs_info(defs)
    folder = ROOT / 'hero-animations'
    if folder.exists(): shutil.rmtree(folder)
    folder.mkdir()
    ss = tl.get('skippedScenes', []); ss = ss if isinstance(ss, list) else []
    skipped = {s.split(':')[0][:-2] if s.split(':')[0].endswith('_1') else s.split(':')[0]: s for s in ss}
    clips = []
    for c in tl['clips']:
        stem = f"{c['index']:03d}"
        if not (cut / (stem + '.mp4')).exists(): continue
        shutil.copy(cut / (stem + '.mp4'), folder / (stem + '.mp4')); shutil.copy(cut / (stem + '.jpg'), folder / (stem + '.jpg'))
        d = desc.get(c.get('defName', ''), '')
        d = RANK.sub('', d); d = d[:1].upper() + d[1:]
        m = re.search(r'\(([SABCDE]{1,2})\)\s*$', tiers.get(f"{c.get('defName','')}_{c.get('tier',0)+1}", ''))
        c['label'] = re.sub(r'[Mm]asked guard', 'ANBU', c['label']).replace('ANBU,', 'ANBU:') if c.get('scene') else c['label']
        clips.append(dict(c, file=stem + '.mp4', poster=stem + '.jpg', desc=d, rank=m.group(1) if m else '',
                          treeLabel=trees.get(c.get('tree', ''), ''), note=skipped.get(c.get('defName', ''), '')))
    tl['clips'] = clips
    (folder / 'index.json').write_text(json.dumps(tl, ensure_ascii=False, indent=1), encoding='utf-8')

    groups, pending = [], []
    for c in clips:
        if c.get('scene'): groups.append((c['label'], pending, c)); pending = []
        else: pending.append(c)
    if pending: groups.append(('More', pending, None))

    def card(c, overview=False):
        sub = 'Whole batch, as recorded' if overview else ' · '.join(x for x in (c['treeLabel'], (c['rank'] + '-rank') if c['rank'] else '') if x)
        body = c['desc'] if not overview else ''
        if c.get('skipped'): body += (' ' if body else '') + '(Showcase check: ' + c['skipped'].rstrip('.') + '.)'
        elif c.get('verdict') in ('WARN', 'FAIL') and c.get('why'): body += (' ' if body else '') + '(Showcase check, ' + c['verdict'].lower() + ': ' + c['why'].split('  [')[0].rstrip('.') + '.)'
        pre = folder.name + '/'
        return (f'<figure class="anim" data-n="{E((c["label"]+" "+sub+" "+body).lower(), quote=True)}">'
                f'<div class="vw"><video src="{pre}{c["file"]}" muted loop playsinline preload="none" poster="{pre}{c["poster"]}" aria-label="{E(c["label"], quote=True)}"></video>'
                '<button class="big" type="button" aria-label="Open large">&#x26F6;</button></div>'
                f'<figcaption><b>{E(c["label"])}</b>' + (f'<small>{E(sub)}</small>' if sub else '') + (f'<p>{E(body)}</p>' if body else '')
                + ('' if overview else f'<textarea class="cmt" data-k="{E(c.get("defName","") or c["file"], quote=True)}" data-l="{E(c["label"], quote=True)}" data-i="{c["index"]}" placeholder="Your comment on this technique (saved automatically)"></textarea>'
                                 '<div class="cmtbar"><button type="button" class="cmtsave">Save comments to a file</button><span class="cmtstate"></span></div>')
                + '</figcaption></figure>')

    n = sum(len(g[1]) for g in groups)
    out = ['<h1>Showcase: hero animations</h1>',
           f'<p class="lead">Every technique with a hand-made animation, cast for real in the showcase on {E(date)}: {n} techniques in {len(groups)} batches.</p>',
           '<p>Zoomed on the action. Tap a clip to open it large. Type a comment under any technique: it is kept in this browser, and the buttons save all your comments to one file or copy them.</p>',
           '<div class="toolbar"><input type="search" placeholder="Filter techniques" aria-label="Filter animations" autocomplete="off" id="animq">'
           '<button type="button" id="notesave">Save comments to a file</button><button type="button" id="notecopy">Copy all comments</button><span id="notecount"></span></div>',
           '<div class="toc">' + ''.join(f'<a href="#batch-{i}">{E(name)}</a>' for i, (name, _, _) in enumerate(groups)) + '</div>']
    for i, (name, children, overview) in enumerate(groups):
        out.append(f'<details class="sec anim-category" id="batch-{i}"><summary><h2 class="st">{E(name)} <small>{len(children)}</small></h2></summary><div class="body"><div class="grid anims">')
        out.extend(card(c) for c in children)
        out.append('</div>')
        if overview: out.append('<details><summary>Watch the whole batch</summary><div class="grid anims">' + card(overview, True) + '</div></details>')
        out.append('</div></details>')

    add_tab()
    shell = (ROOT / 'index.html').read_text(encoding='utf-8')
    viewer = re.search(r'<script>.*?</script>', shell, re.S).group(0)
    nav = re.search(r'<nav>.*?</nav>', shell, re.S).group(0).replace(' class=on', '').replace('<a href="hero-animations.html">', '<a href="hero-animations.html" class=on>')   # keeps every tab
    page = re.sub(r'<nav>.*?</nav>', lambda _: nav, shell, count=1, flags=re.S)
    page = re.sub(r'<main>.*?</main>', lambda _: '<main>' + ''.join(out) + viewer + '<script src="assets/animation-categories.js"></script><script src="assets/notes.js"></script></main>', page, count=1, flags=re.S)
    page = re.sub(r'<title>.*?</title>', '<title>Showcase: hero animations · NFRP World</title>', page, count=1)
    (ROOT / 'hero-animations.html').write_text(page, encoding='utf-8')
    print('hero-animations.html:', n, 'clips,', len(groups), 'batches')

def add_tab():
    # the new tab on every page of the site
    for f in ROOT.glob('*.html'):
        t = f.read_text(encoding='utf-8')
        if 'href="hero-animations.html"' in t or '<nav>' not in t: continue
        t = re.sub(r'(<nav>.*?)(</nav>)', lambda m: m.group(1) + '<a href="hero-animations.html">Showcase: hero animations</a>' + m.group(2), t, count=1, flags=re.S)
        f.write_text(t, encoding='utf-8')

if __name__ == '__main__':
    build(Path(sys.argv[1]), sys.argv[2], sys.argv[3])
