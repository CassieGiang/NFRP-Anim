"""Generic effects page: every shared (non-hand-made) effect visual, animated on the stone floor, with where it is used and a comment box.
usage: generic_fx.py <FX texture root> <usage.json> <stone_floor.jpg>"""
import sys, os, json, re, html, pathlib
from PIL import Image
ROOT = pathlib.Path(__file__).resolve().parent.parent; E = html.escape
fx, usage, floor = sys.argv[1:4]
OUT = ROOT / 'generic-effects'; OUT.mkdir(exist_ok=True)
LAYER = {'KZFx': 'shared effect engine', 'Kazeraikou': 'element and storm effects', 'NFFxSignature': 'technique look by element and kind',
 'NFSequence': 'cast sequence (wind-up, finishers)', 'NFProjFx': 'projectile launch and impact', 'NFHitFx': 'melee hits', 'NFBeastArts': 'beast and summon attacks',
 'NFBeasts': 'beasts', 'NFBigCombo': 'element combos', 'NFPolishA2': 'movement and status polish', 'NFPolishB': 'polish pass B', 'NFPolishC': 'polish pass C',
 'NFPolishDUI': 'polish (UI)', 'NFKenseijin': 'Kenseijin sword moves', 'NFWeaponArts': 'weapon arts', 'NFTaijutsu': 'taijutsu', 'NFCreatureAnim': 'creatures',
 'NFProcFxMigrate': 'procedural effects', 'NFImprove': 'effect improvements', 'NFCrisp': 'crisp projectiles and bursts', 'NFVisualC': 'signature looks',
 'NFKinds': 'technique kinds', 'NFTeam': 'team moves', 'NFFizzle': 'fizzled casts', 'NFConstruct': 'constructs', 'NFProcImpact': 'impacts', 'NFBajutsu': 'mounted combat',
 'NFMouth': 'mouth techniques', 'NFPolishChecksB': 'polish checks'}
use = {n: [LAYER.get(f[:-3], f[:-3]) for f in g] for n, g, h in json.load(open(usage))}
herouse = {n: len(h) for n, g, h in json.load(open(usage))}
bgc = Image.open(floor).convert('RGBA')
def frames(d):
    fs = sorted([f for f in os.listdir(d) if f.endswith('.png')], key=lambda x: int(re.findall(r'(\d+)\.png$', x)[0]) if re.findall(r'(\d+)\.png$', x) else 0)
    return [Image.open(os.path.join(d, f)).convert('RGBA') for f in fs]
def gif(name, fs, px=200, ms=90):
    out = []
    for i in range(max(len(fs), 1)):
        b = bgc.resize((px, px)).copy(); f = fs[i % len(fs)].resize((px, px), Image.LANCZOS); b.alpha_composite(f); out.append(b.convert('RGB'))
    p = OUT / (name + '.gif'); out[0].save(p, save_all=True, append_images=out[1:], duration=ms, loop=0); return p.name
def still(name, im, px=150):
    b = bgc.resize((px, px)).copy(); w, h = im.size; s = min(px / w, px / h) * 0.95; f = im.resize((max(1, int(w * s)), max(1, int(h * s))), Image.LANCZOS)
    b.alpha_composite(f, ((px - f.size[0]) // 2, (px - f.size[1]) // 2)); p = OUT / (name + '.png'); b.convert('RGB').save(p); return p.name
cards = {}; idx = [0]
def card(key, img, title, sub, small=False):
    idx[0] += 1
    return (f'<figure class="anim"><div class="vw"><img src="generic-effects/{img}" alt="{E(title, quote=True)}" loading="lazy" style="width:100%;height:auto"></div>'
            f'<figcaption><b>{E(title)}</b>' + (f'<small>{E(sub)}</small>' if sub else '') +
            f'<textarea class="cmt" data-k="{E(key, quote=True)}" data-l="{E(title, quote=True)}" data-i="{idx[0]}" placeholder="Keep, replace, or what it should look like"></textarea>'
            '<div class="cmtbar"><button type="button" class="cmtsave">Save comments to a file</button><span class="cmtstate"></span></div></figcaption></figure>')
secs = []
# 1 shared painted flipbooks (the crisp repaint where it exists: that is what the game draws with crisp art on)
lib = sorted(n for n in set(os.listdir(f'{fx}/Anim')) | set(os.listdir(f'{fx}/AnimCrisp')) if not n.startswith('Sig') and not n.startswith('WallRing') and not n.endswith('.png'))
c = []
for n in lib:
    d = f'{fx}/AnimCrisp/{n}' if os.path.isdir(f'{fx}/AnimCrisp/{n}') else f'{fx}/Anim/{n}'
    fs = frames(d)
    if not fs: continue
    u = sorted(set(use.get(n, [])))
    sub = f'{len(fs)} frames · used by: ' + (', '.join(u) if u else 'nothing generic') + (f' · also in {herouse[n]} hand-made animation files' if herouse.get(n) else '')
    c.append(card('lib:' + n, gif('lib_' + n, fs), n, sub))
secs.append(('Shared painted effects', f'{len(c)} flipbooks every technique without its own animation draws from: bursts, splashes, gathers, slashes, rings. Shown as the game draws them (the crisp repaint).', c))
# 2 barrier rings
c = []
for n in sorted(x for x in os.listdir(f'{fx}/Anim') if x.startswith('WallRing')):
    fs = frames(f'{fx}/Anim/{n}')
    if fs: c.append(card('ring:' + n, gif('ring_' + n, fs), n, f'{len(fs)} frames · barrier and wall techniques, by material'))
secs.append(('Barrier rings', 'The ring a barrier or wall technique raises, one per material.', c))
# 3 element sets
c = []
for el in sorted(os.listdir(f'{fx}/Crisp')):
    for f in sorted(os.listdir(f'{fx}/Crisp/{el}')):
        if f.endswith('.png'): c.append(card(f'el:{el}/{f[:-4]}', still(f'el_{el}_{f[:-4]}', Image.open(f'{fx}/Crisp/{el}/{f}').convert('RGBA')), f'{el}: {f[:-4]}',
                                             {'Spear': 'the projectile in flight', 'Burst': 'impact burst', 'Shard': 'impact shards and gathering', 'Wall': 'walls', 'Crescent': 'crescent slashes',
                                              'Scar': 'ground mark left behind', 'BeamBody': 'beam body', 'BeamHead': 'beam front'}.get(f[:-4], '')))
secs.append(('Element sets', 'Eight pieces per element (earth, fire, ice, lightning, sand, water, wind, wood): projectile, impact, shards, wall, crescent, ground mark and beam.', c))
# 4 particles and marks
c = []
for f in sorted(os.listdir(f'{fx}/CrispParts')):
    if f.endswith('.png'): c.append(card('part:' + f[:-4], still('part_' + f[:-4], Image.open(f'{fx}/CrispParts/{f}').convert('RGBA')), f[:-4], 'particle or mark (cast-start seal circle, summon circles, embers, sparks, leaves...)'))
secs.append(('Particles and marks', 'Small pieces scattered by the generic layers, plus the seal and summon circles.', c))
# 5 soft sprites and overlays
c = []
for d, what in (('', 'soft glow sprite'), ('Soft', 'soft sprite'), ('Overlay', 'status overlay on a pawn'), ('Polish', 'polish piece'), ('Bolt', 'lightning bolt frame')):
    p = f'{fx}/{d}' if d else fx
    for f in sorted(os.listdir(p)):
        if f.endswith('.png'): c.append(card(f'soft:{d}/{f[:-4]}', still(f'soft_{d or "root"}_{f[:-4]}', Image.open(f'{p}/{f}').convert('RGBA')), (d + '/' if d else '') + f[:-4], what))
secs.append(('Soft sprites, overlays and bolts', 'The older soft glow sprites (glows, rings, beams), status overlays and bolt frames.', c))
n = sum(len(x[2]) for x in secs)
out = ['<h1>Generic effects</h1>',
       f'<p class="lead">Every shared effect visual a technique without its own hand-made animation can show: {n} pieces in {len(secs)} groups, before we source better ones.</p>',
       '<p>When a technique has no animation of its own, these layers draw it: at the cast start a soft glow, a reversed chakra burst and a seal circle; in the wind-up hand-seal glyphs and a chakra gather; at release a muzzle flash, the element\'s projectile and a ribbon trail; then the element\'s burst, splash or slash, a finisher (pillar, slam, smoke) and a ground mark. Some layers are drawn by code (glows, waves, rings, trails) and have no picture here. Type a comment under anything to keep, replace or describe it; the buttons save all comments to one file.</p>',
       '<div class="toolbar" id="notesrun" data-run="generic-fx"><button type="button" id="notesave">Save comments to a file</button><button type="button" id="notecopy">Copy all comments</button><span id="notecount"></span></div>',
       '<div class="toc">' + ''.join(f'<a href="#g{i}">{E(t)} ({len(c)})</a>' for i, (t, _, c) in enumerate(secs)) + '</div>']
for i, (t, intro, c) in enumerate(secs):
    out.append(f'<details class="sec" id="g{i}"' + (' open' if i == 0 else '') + f'><summary><h2 class="st">{E(t)} <small>{len(c)}</small></h2></summary><div class="body"><p>{E(intro)}</p><div class="grid anims">' + ''.join(c) + '</div></div></details>')
for p in ROOT.glob('*.html'):
    s = p.read_text(encoding='utf-8')
    if 'href="generic-effects.html"' not in s and '<nav>' in s: p.write_text(re.sub(r'(<nav>.*?)(</nav>)', lambda m: m.group(1) + '<a href="generic-effects.html">Generic effects</a>' + m.group(2), s, count=1, flags=re.S), encoding='utf-8')
shell = (ROOT / 'index.html').read_text(encoding='utf-8')
nav = re.search(r'<nav>.*?</nav>', shell, re.S).group(0).replace(' class=on', '').replace('<a href="generic-effects.html">', '<a href="generic-effects.html" class=on>')
page = re.sub(r'<nav>.*?</nav>', lambda _: nav, shell, count=1, flags=re.S)
page = re.sub(r'<main>.*?</main>', lambda _: '<main>' + ''.join(out) + '<script src="assets/notes.js"></script></main>', page, count=1, flags=re.S)
page = re.sub(r'<title>.*?</title>', '<title>Generic effects · NFRP World</title>', page, count=1)
(ROOT / 'generic-effects.html').write_text(page, encoding='utf-8')
print('generic-effects.html:', n, 'pieces in', len(secs), 'groups')
