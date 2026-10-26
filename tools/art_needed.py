"""Art to source page: every hand-made technique that still draws a shared (stock) flipbook, and which ones.
usage: art_needed.py   (reads tools/art_needed.json, made by the mod repo's tools/heroes/stock_art/scan.py; uses generic-effects/lib_*.gif)"""
import json, re, html, pathlib, collections
ROOT = pathlib.Path(__file__).resolve().parent.parent; E = html.escape
d = json.load(open(ROOT / 'tools' / 'art_needed.json', encoding='utf-8'))
rows, bt, ken = d['rows'], d['batches'], d['kenseijin']
idx = [0]
def box(key, label):
    idx[0] += 1
    return (f'<textarea class="cmt" data-k="{E(key, quote=True)}" data-l="{E(label, quote=True)}" data-i="{idx[0]}" placeholder="What its own art should look like, or keep"></textarea>'
            '<div class="cmtbar"><button type="button" class="cmtsave">Save comments to a file</button><span class="cmtstate"></span></div>')
def chip(n):
    return f'<span class="chip"><img src="generic-effects/lib_{E(n)}.gif" alt="" loading="lazy"><span>{E(n)}</span></span>'
users = collections.defaultdict(list)
for r in rows:
    for n in r['stock']: users[n].append(r['label'])
for n in ken['stock']: users[n].append('Kenseijin (all 11)')
need = [r for r in rows if r['stock']]; clean = [r for r in rows if not r['stock']]
pairs = sum(len(r['stock']) for r in rows) + len(ken['stock'])
out = ['<h1>Art to source</h1>',
       f'<p class="lead">{len(need)} of the {len(rows)} hand-made animations still draw at least one shared flipbook (plus all 11 Kenseijin sword moves): '
       f'{len(users)} different stock pieces, {pairs} uses in all. Only {len(clean)} draw nothing but their own art.</p>',
       '<p>Read from the animation code on 26 Oct 2026 (update 262), counting only what plays with the installed art: fallbacks that only run when a technique\'s own art is missing are left out. '
       'Some shared helpers are counted for every rank of a technique, so a rank may use a little less than listed. The in-game audit ("Audit: hand-made animation art") gives the exact list.</p>',
       '<style>.chip{display:inline-flex;align-items:center;gap:6px;margin:3px 6px 3px 0;padding:2px 8px 2px 2px;border:1px solid #8884;border-radius:6px;font-size:.85em}'
       '.chip img{width:44px;height:44px;border-radius:4px}.tr{padding:10px 0;border-top:1px solid #8883}.tr b{display:block}.tr small{opacity:.7}'
       '.uses{font-size:.85em;opacity:.8}.tr textarea.cmt{display:block;width:100%;max-width:720px;min-height:56px;margin:6px 0 4px;font:inherit;padding:6px;box-sizing:border-box}.pc{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px}.pc figure{margin:0}</style>',
       '<div class="toolbar" id="notesrun" data-run="art-needed"><button type="button" id="notesave">Save comments to a file</button><button type="button" id="notecopy">Copy all comments</button><span id="notecount"></span></div>']
# 1 by stock piece
c = []
for n, us in sorted(users.items(), key=lambda kv: -len(kv[1])):
    c.append(f'<figure class="anim"><div class="vw"><img src="generic-effects/lib_{E(n)}.gif" alt="{E(n)}" loading="lazy" style="width:100%;height:auto"></div>'
             f'<figcaption><b>{E(n)}</b><small>{len(us)} techniques</small><div class="uses">{E(", ".join(us))}</div>' + box('stock:' + n, n) + '</figcaption></figure>')
secs = [('By stock piece', 'Each shared flipbook the hand-made animations still use, most used first. One new piece can replace a stock one across a family of similar techniques.', '<div class="pc">' + ''.join(c) + '</div>', len(c))]
# 2 by technique, per batch
by = collections.defaultdict(list)
for r in need: by[r['batch']].append(r)
for b in sorted(by):
    h = ''.join(f'<div class="tr"><b>{E(r["label"])}</b><small>{E(", ".join(r["tiers"]))}</small><div>' + ''.join(chip(n) for n in r['stock']) + '</div>' + box('tech:' + r['tiers'][0], r['label']) + '</div>' for r in by[b])
    secs.append((bt.get(str(b), f'Batch {b}'), '', h, len(by[b])))
secs.append(('Kenseijin sword moves', ', '.join(ken['techs']) + ': the shared slashes and hits are drawn by all of them.',
             '<div class="tr"><div>' + ''.join(chip(n) for n in ken['stock']) + '</div>' + box('tech:kenseijin', 'Kenseijin') + '</div>', len(ken['techs'])))
secs.append(('Already own art only', 'Nothing to source.', '<p>' + E(', '.join(r['label'] for r in clean)) + '</p>', len(clean)))
out.append('<div class="toc">' + ''.join(f'<a href="#g{i}">{E(t)} ({n})</a>' for i, (t, _, _, n) in enumerate(secs)) + '</div>')
for i, (t, intro, body, n) in enumerate(secs):
    out.append(f'<details class="sec" id="g{i}"' + (' open' if i == 0 else '') + f'><summary><h2 class="st">{E(t)} <small>{n}</small></h2></summary><div class="body">' + (f'<p>{E(intro)}</p>' if intro else '') + body + '</div></details>')
for p in ROOT.glob('*.html'):
    s = p.read_text(encoding='utf-8')
    if 'href="art-needed.html"' not in s and '<nav>' in s: p.write_text(re.sub(r'(<nav>.*?)(</nav>)', lambda m: m.group(1) + '<a href="art-needed.html">Art to source</a>' + m.group(2), s, count=1, flags=re.S), encoding='utf-8')
shell = (ROOT / 'index.html').read_text(encoding='utf-8')
nav = re.search(r'<nav>.*?</nav>', shell, re.S).group(0).replace(' class=on', '').replace('<a href="art-needed.html">', '<a href="art-needed.html" class=on>')
page = re.sub(r'<nav>.*?</nav>', lambda _: nav, shell, count=1, flags=re.S)
page = re.sub(r'<main>.*?</main>', lambda _: '<main>' + ''.join(out) + '<script src="assets/notes.js"></script></main>', page, count=1, flags=re.S)
page = re.sub(r'<title>.*?</title>', '<title>Art to source · NFRP World</title>', page, count=1)
(ROOT / 'art-needed.html').write_text(page, encoding='utf-8')
print('art-needed.html:', len(need), 'techniques,', len(users), 'stock pieces,', pairs, 'uses')
