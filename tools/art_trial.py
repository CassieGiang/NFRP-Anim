"""Art trials page: side-by-side comparisons of trial art batches (GIFs), with a comment box per option."""
import re, html, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
E = html.escape
TRIALS = [
 ('fireball', 'Great Fireball: still core, travel dart, impact flash (batch 124)',
  'After the pixel-art reference video: the round body stays identical in every frame and only the flames and embers move; '
  'a small stretched dart for the flight; a short hard flash at contact before the dome of fire. Each option flies across the '
  'stone floor at game speed (left) and loops in close-up (right). Nothing here is in the game yet.',
  [('A_current', 'A · Today: 4-frame ball (batch 122)', 'What the game draws now. The swirl inside the ball is redrawn every frame.'),
   ('A2_current_lockedcore', 'A2 · Today\'s ball with its core locked', 'Same art, no new batch: frame 1\'s round body is copied into the other three, so only the flames move.'),
   ('B_loop8', 'B · New 8-frame loop, as painted', 'Batch 124: twice the frames, flames curl and embers peel away; the painter kept the core almost the same.'),
   ('C_loop8_lockedcore', 'C · New 8-frame loop, core locked', 'B with the core made exactly identical in all eight frames.'),
   ('D_loop_dart_flash', 'D · Big ball at release, dart in flight, flash at contact', 'C for the first moment, then the small white-hot dart carries it, then the star flash and today\'s dome of fire.'),
   ('E_sequence', 'E · Your pick (installed in u252)', 'Flame gathers in at the mouth while the ball swells, C\'s full fireball for the whole flight with today\'s swirling orange fire set inside its bright centre, D\'s star flash at contact, then the dome of fire.')]),
]
def add_tab():
    for p in ROOT.glob('*.html'):
        t = p.read_text(encoding='utf-8')
        if 'href="art-trials.html"' in t or '<nav>' not in t: continue
        t = re.sub(r'(<nav>.*?)(</nav>)', lambda m: m.group(1) + '<a href="art-trials.html">Art trials</a>' + m.group(2), t, count=1, flags=re.S)
        p.write_text(t, encoding='utf-8')
def build():
    out = ['<h1>Art trials</h1>', '<p class="lead">Trial art next to what the game uses today. Pick what reads best; nothing on this page is installed until you choose.</p>',
           '<div class="toolbar" id="notesrun" data-run="art-trials"><button type="button" id="notesave">Save comments to a file</button><button type="button" id="notecopy">Copy all comments</button><span id="notecount"></span></div>']
    i = 0
    for key, title, intro, opts in TRIALS:
        out.append(f'<details class="sec" open><summary><h2 class="st">{E(title)}</h2></summary><div class="body"><p>{E(intro)}</p><div class="grid anims">')
        for f, label, desc in opts:
            i += 1
            out.append(f'<figure class="anim"><div class="vw" style="display:flex;gap:6px;flex-wrap:wrap"><img src="art-trials/{key}/{f}.gif" alt="{E(label, quote=True)} in flight" style="max-width:100%;height:auto">'
                       f'<img src="art-trials/{key}/{f}_closeup.gif" alt="{E(label, quote=True)} close-up" style="width:130px;height:130px"></div>'
                       f'<figcaption><b>{E(label)}</b><p>{E(desc)}</p>'
                       f'<textarea class="cmt" data-k="{key}:{f}" data-l="{E(label, quote=True)}" data-i="{i}" placeholder="Your comment on this option (saved automatically)"></textarea>'
                       '<div class="cmtbar"><button type="button" class="cmtsave">Save comments to a file</button><span class="cmtstate"></span></div></figcaption></figure>')
        out.append('</div></div></details>')
    add_tab()
    shell = (ROOT / 'index.html').read_text(encoding='utf-8')
    nav = re.search(r'<nav>.*?</nav>', shell, re.S).group(0).replace(' class=on', '').replace('<a href="art-trials.html">', '<a href="art-trials.html" class=on>')
    page = re.sub(r'<nav>.*?</nav>', lambda _: nav, shell, count=1, flags=re.S)
    page = re.sub(r'<main>.*?</main>', lambda _: '<main>' + ''.join(out) + '<script src="assets/notes.js"></script></main>', page, count=1, flags=re.S)
    page = re.sub(r'<title>.*?</title>', '<title>Art trials · NFRP World</title>', page, count=1)
    (ROOT / 'art-trials.html').write_text(page, encoding='utf-8')
    print('art-trials.html:', i, 'options')
if __name__ == '__main__': build()
