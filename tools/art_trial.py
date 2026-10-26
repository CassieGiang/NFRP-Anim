"""Art trials page: side-by-side comparisons of trial art batches (GIFs), with a comment box per option."""
import re, html, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
E = html.escape
TRIALS = [
 (
 'tabs', 'Pawn tab buttons in the NFRP look (design mockups)',
  'The tab row under a selected pawn. Shinobi is shown selected and Log hovered. The wooden look today comes from the PrettyUI mod. Mockups only, nothing is in the game.',
  [('O_current', 'Today (PrettyUI wood)', 'For comparison.'), ('A_slate', 'A · Dark slate, like the technique trees', 'Dark slate tabs with the thin steel-grey inset line and diamond of the tree backgrounds; the selected tab brightens.'), ('B_scroll', 'B · Paper scroll, like the chakra bar', 'Scroll paper between short wooden rods; the selected tab gets an indigo ink stroke and a vermilion seal.'), ('C_slate_seal', 'C · Slate with a paper selected tab', 'Dark slate tabs with cut corners; the selected tab turns to scroll paper with an ink stroke and a vermilion seal mark.')]),
 (
 'own125', 'Own art for four hand-made groups (batch 125 pilot)',
  'Each technique group gets its own version of the stock effects it used: old on the left, new on the right (close-up of the new one beside it). Not in the game until you say so.',
  [('SigRedLegFireburst', 'BX125-1 · Red Leg: replaces Fireburst', 'Heat of a kick bursting where the heel lands. Note: it came out round, close to the old design, not the lopsided burst asked for.'), ('SigRedLegFlamekick', 'BX125-2 · Red Leg: replaces Flamekick', 'The fire arc a sweeping leg leaves.'), ('SigRedLegFlamepillar', 'BX125-3 · Red Leg: replaces Flamepillar', 'Heat climbing the leg.'), ('SigRedLegSpinkick', 'BX125-4 · Red Leg: replaces Spinkick', 'A spinning wheel of fiery kicks.'), ('SigMindGazespiral', 'BX125-5 · mind arts: replaces Gazespiral', 'Threads and petals wheeling round the head (light art, tinted in game).'), ('SigMindGenripple', 'BX125-6 · mind arts: replaces Genripple', 'Thread ripples spreading out.'), ('SigMindCrystalshatter', 'BX125-7 · mind arts: replaces Crystalshatter', 'A glowing thought cracking apart (Broken Mind).'), ('SigMindSealcircle', 'BX125-8 · mind arts: replaces Sealcircle', 'A binding circle woven from thread.'), ('SigMindSoundwave', 'BX125-9 · mind arts: replaces Soundwave', 'A calm pulse of the mind (Mind Pulse).'), ('SigSharkWatersplash', 'BX125-10 · shark arts: replaces Watersplash', 'A sea splash with fin-tipped spray.'), ('SigSharkShellguard', 'BX125-11 · shark arts: replaces Shellguard', 'Shark-skin scale shell in place of the hexagon shield (Shark Skin).'), ('SigSharkWatercrash', 'BX125-12 · shark arts: replaces Watercrash', 'A heavy charge of deep water landing (Depth Charge, Killing Depths).'), ('SigSharkBitechomp', 'BX125-13 · shark arts: replaces Bitechomp', 'Jaws of water snapping shut.'), ('SigSharkWaterdragon', 'BX125-14 · shark arts: replaces Waterdragon', 'A circling current with two fins (Shark Wall, Shark Frenzy).'), ('SigSwarmBugswarm', 'BX125-15 · bug arts: replaces Bugswarm', 'A swarm made only of beetles, no grey smoke.'), ('SigSwarmDustdebris', 'BX125-16 · bug arts: replaces Dustdebris', 'A beetle mass slamming down and scattering.'), ('SigSwarmGroundslam', 'BX125-17 · bug arts: replaces Groundslam', 'Beetles boiling out of cracks round the feet.'), ('gemini_vs_gpt', 'Sheet 1 made by GPT, Gemini and ComfyUI', "The same brief: GPT (paid, installed), Gemini (free) and FLUX 3 Image Klein in ComfyUI on your PC (free, 17 s); the close-up is ComfyUI's. All three drew a round burst.")]),
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
