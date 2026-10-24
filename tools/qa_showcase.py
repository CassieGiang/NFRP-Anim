#!/usr/bin/env python3
"""Publish one QA showcase round (painted creatures, immersion fixes, combos) on its own tab.

python3 tools/qa_showcase.py <round-folder> <date YYYY-MM-DD> <slug>
<round-folder> holds the cut folders from Showcase/ (*_creatures, *_immersion, *_combos), each with its timeline_*.json,
the clips "NN <label>.mp4" and, for combos, combos_*.txt. Clips go to qa-<slug>/, the page to qa-<slug>.html, and the tab is
added to the nav of every page. Posters are taken from each clip with ffmpeg.
"""
import html, json, re, shutil, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
E = html.escape

SECTIONS = [
    ('creatures', 'Painted creatures', 'The 14 painted creature techniques, each cast to the right and to the left.'),
    ('immersion', 'Immersion fixes', 'The techniques from the immersion review, real casts after the fixes. The caption says what to look for.'),
    ('combos', 'Elemental combos', 'Two allied ninjas cast for real; every pair should set off its combo. Also the jutsu chain, the solo rules and a control.'),
]


def clips_of(folder):
    tl = json.loads(next(folder.glob('timeline_*.json')).read_text(encoding='utf-8'))
    files = {int(p.name.split(' ', 1)[0]): p for p in folder.glob('*.mp4')}
    return tl, files


def poster(src, dst):
    dur = 2.0
    try:
        out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(src)], capture_output=True, text=True).stdout
        dur = float(out.strip())
    except Exception:
        pass
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{dur * 0.55:.2f}', '-i', str(src), '-frames:v', '1', '-vf', 'scale=640:-2', '-q:v', '4', str(dst)], check=True)


def build(rnd, date, slug):
    out_dir = ROOT / f'qa-{slug}'
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir()
    pre = out_dir.name + '/'
    body, toc, total = [], [], 0
    for key, title, lead in SECTIONS:
        folder = next((p for p in sorted(rnd.iterdir()) if p.is_dir() and p.name.endswith('_' + key)), None)
        if folder is None:
            continue
        tl, files = clips_of(folder)
        notes = []
        if key == 'combos':
            txt = next(folder.glob('combos_*.txt'), None)
            if txt:
                notes = [l for l in txt.read_text(encoding='utf-8').splitlines() if l.startswith(('PASS', 'FAIL', 'SKIP'))]
        cards = []
        clips = tl['clips']
        for i, c in enumerate(clips):
            n = c['index']
            if n not in files:
                continue
            if key == 'immersion' and c.get('scene'):
                continue   # the outer scene clip repeats the cast clip; its label becomes the cast's caption
            label, sub, body_txt = c['label'], '', ''
            if key == 'immersion':
                nxt = clips[i + 1] if i + 1 < len(clips) else None
                look = nxt['label'] if nxt and nxt.get('scene') else ''
                sub = 'Look for: ' + re.sub(r'^IM\d+(?: \(still open\))?:\s*', '', look) if look else ''
            elif key == 'combos':
                line = notes[len(cards)] if len(cards) < len(notes) else ''
                body_txt = line.split('->', 1)[1].strip() if '->' in line else ''
                sub = (c.get('verdict') or '') + (' · ' + body_txt if body_txt else '')
                body_txt = ''
            else:
                sub = 'Visual review: ' + ('to the right' if 'right' in label else 'to the left')
            stem = f'{key}-{n:02d}'
            shutil.copy(files[n], out_dir / (stem + '.mp4'))
            poster(out_dir / (stem + '.mp4'), out_dir / (stem + '.jpg'))
            data = (label + ' ' + sub + ' ' + body_txt).lower()
            cards.append(f'<figure class="anim" data-n="{E(data, quote=True)}"><div class="vw"><video src="{pre}{stem}.mp4" muted loop playsinline preload="none" poster="{pre}{stem}.jpg" aria-label="{E(label, quote=True)}"></video>'
                         '<button class="big" type="button" aria-label="Open large">&#x26F6;</button></div>'
                         f'<figcaption><b>{E(label)}</b>' + (f'<small>{E(sub)}</small>' if sub else '') + (f'<p>{E(body_txt)}</p>' if body_txt else '') + '</figcaption></figure>')
        total += len(cards)
        toc.append(f'<a href="#{key}">{E(title)}</a>')
        body.append(f'<h2 id="{key}">{E(title)} <small>{len(cards)}</small></h2><p>{E(lead)}</p><div class="grid anims">' + ''.join(cards) + '</div>')

    tab = f'Showcase QA {date[8:10].lstrip("0")} {["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"][int(date[5:7]) - 1]}'
    page_name = f'qa-{slug}.html'
    main = [f'<h1>{E(tab)}</h1>',
            f'<p class="lead">The showcase runs recorded {E(date)} for QA: {total} clips. The checks behind them only count what played; the look is for review.</p>',
            '<p>Tap a clip to open it large.</p>',
            '<div class="toolbar"><input type="search" placeholder="Filter clips" aria-label="Filter clips" autocomplete="off" id="animq"></div>',
            '<div class="toc">' + ''.join(toc) + '</div>'] + body

    shell = (ROOT / 'index.html').read_text(encoding='utf-8')
    viewer = re.search(r'<script>.*?</script>', shell, re.S).group(0)
    page = re.sub(r'<main>.*?</main>', lambda _: '<main>' + ''.join(main) + viewer + '</main>', shell, count=1, flags=re.S)
    page = re.sub(r'<title>.*?</title>', f'<title>{E(tab)} · NFRP World</title>', page, count=1)
    (ROOT / page_name).write_text(page, encoding='utf-8')

    # the tab on every page (nav links kept in order; the current page marked)
    pages = sorted(p.name for p in ROOT.glob('*.html'))
    for p in pages:
        s = (ROOT / p).read_text(encoding='utf-8')
        m = re.search(r'<nav>(.*?)</nav>', s, re.S)
        if not m:
            continue
        links = re.findall(r'<a href="([^"]+)"[^>]*>(.*?)</a>', m.group(1))
        if page_name not in [h for h, _ in links]:
            links.append((page_name, E(tab)))
        nav = '<nav>' + ''.join(f'<a href="{h}"' + (' class=on' if h == p else '') + f'>{t}</a>' for h, t in links) + '</nav>'
        (ROOT / p).write_text(s.replace(m.group(0), nav, 1), encoding='utf-8')
    print(page_name + ':', total, 'clips')


if __name__ == '__main__':
    build(Path(sys.argv[1]), sys.argv[2], sys.argv[3])
