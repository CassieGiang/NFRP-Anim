#!/usr/bin/env python3
"""NFRP World wiki: the Animations page, built from animations.json (one entry per clip; the clips live in docs/anim/).
Run on its own to (re)write docs/animations.html and add the Animations tab to every page's nav:
    python3 wiki-src/animations.py docs
gen_wiki.py also calls build() so a full regeneration keeps the page."""
import os, sys, json, re, glob, html
E = lambda s: html.escape(s or '', quote=True)
HERE = os.path.dirname(os.path.abspath(__file__))

def body():
    m = json.load(open(os.path.join(HERE, 'animations.json'), encoding='utf-8'))
    groups = []
    for c in m['clips']:
        if not groups or groups[-1][0] != c['group']: groups.append((c['group'], []))
        groups[-1][1].append(c)
    toc = ''.join(f'<a href="#{re.sub(r"[^a-z0-9]+", "-", g.lower()).strip("-")}">{E(g)}</a>' for g, _ in groups)
    out = ['<h1>Animations</h1>',
           f'<p class="lead">{E(m["intro"])}</p>',
           '<div class="toolbar"><input type="search" placeholder="Filter animations" aria-label="Filter animations" autocomplete="off" id="animq"></div>',
           f'<div class="toc">{toc}</div>']
    for g, cs in groups:
        gid = re.sub(r'[^a-z0-9]+', '-', g.lower()).strip('-')
        cards = ''.join(
            f'<figure class="anim" data-n="{E((c["label"] + " " + c.get("tree", "") + " " + c.get("desc", "")).lower())}">'
            f'<div class="vw"><video src="anim/{E(c["file"])}" muted loop playsinline preload="none" poster="anim/{E(c["poster"])}" aria-label="{E(c["label"])}"></video>'
            f'<button class="big" type="button" aria-label="Open large">&#x26F6;</button></div>'
            f'<figcaption><b>{E(c["label"])}</b>{("<small>" + E(c["tree"]) + (" · " + E(c["rank"]) + "-rank" if c.get("rank") else "") + "</small>") if c.get("tree") else ""}'
            f'{("<p>" + E(c["desc"]) + "</p>") if c.get("desc") else ""}</figcaption></figure>'
            for c in cs)
        out.append(f'<h2 id="{gid}">{E(g)} <small>{len(cs)}</small></h2><div class="grid anims">{cards}</div>')
    out.append('''<script>
(function(){var vs=[].slice.call(document.querySelectorAll('figure.anim video'));
var io='IntersectionObserver' in window?new IntersectionObserver(function(es){es.forEach(function(e){var v=e.target;if(e.isIntersecting){v.preload='auto';var p=v.play();if(p&&p.catch)p.catch(function(){});}else v.pause();});},{rootMargin:'200px'}):null;
vs.forEach(function(v,i){if(io)io.observe(v);else{v.preload='auto';v.autoplay=true;}v.addEventListener('click',function(){open(i);});v.parentNode.querySelector('.big').addEventListener('click',function(){open(i);});});
var bx=document.createElement('div');bx.id='viewer';bx.hidden=true;bx.innerHTML='<div class="vbar"><b></b><button type="button" data-a="x" aria-label="Close">&#x2715;</button></div><video loop playsinline muted controls></video><p class="vd"></p><div class="vbtn"><button type="button" data-a="p">&#x2039; Prev</button><button type="button" data-a="s">Speed 1&times;</button><button type="button" data-a="f">Full screen</button><button type="button" data-a="n">Next &#x203A;</button></div>';document.body.appendChild(bx);
var bv=bx.querySelector('video'),cur=-1,sp=[1,0.5,0.25],si=0;
function vis(){return vs.filter(function(v){return v.closest('figure').style.display!=='none';});}
function open(i){var v=vs[i];cur=i;var f=v.closest('figure');bx.querySelector('b').textContent=f.querySelector('figcaption b').textContent;var d=f.querySelector('figcaption p');bx.querySelector('.vd').textContent=d?d.textContent:'';bv.src=v.currentSrc||v.src;bv.poster=v.poster;bv.playbackRate=sp[si];bx.hidden=false;document.documentElement.classList.add('vopen');var p=bv.play();if(p&&p.catch)p.catch(function(){});}
function close(){if(document.fullscreenElement&&document.exitFullscreen)document.exitFullscreen();bv.pause();bv.removeAttribute('src');bv.load();bx.hidden=true;document.documentElement.classList.remove('vopen');}
function step(k){var l=vis(),j=l.indexOf(vs[cur]);if(j<0)return;j=(j+k+l.length)%l.length;open(vs.indexOf(l[j]));}
bx.addEventListener('click',function(e){var a=e.target.closest('[data-a]');if(!a){if(e.target===bx)close();return;}var k=a.dataset.a;
if(k==='x')close();else if(k==='p')step(-1);else if(k==='n')step(1);
else if(k==='s'){si=(si+1)%sp.length;bv.playbackRate=sp[si];a.innerHTML='Speed '+sp[si]+'&times;';}
else if(k==='f'){var r=bv.requestFullscreen||bv.webkitRequestFullscreen||bv.webkitEnterFullscreen;if(r){var q=r.call(bv);if(q&&q.then)q.then(function(){try{screen.orientation.lock('landscape').catch(function(){});}catch(_){}}).catch(function(){});}}});
bv.addEventListener('ratechange',function(){});bv.addEventListener('loadedmetadata',function(){bv.playbackRate=sp[si];});
document.addEventListener('keydown',function(e){if(bx.hidden)return;if(e.key==='Escape')close();else if(e.key==='ArrowRight')step(1);else if(e.key==='ArrowLeft')step(-1);});
var tx=null;bv.addEventListener('touchstart',function(e){tx=e.touches[0].clientX;},{passive:true});bv.addEventListener('touchend',function(e){if(tx===null)return;var dx=e.changedTouches[0].clientX-tx;tx=null;if(Math.abs(dx)>60)step(dx<0?1:-1);},{passive:true});
var q=document.getElementById('animq');if(q)q.addEventListener('input',function(){var s=q.value.trim().toLowerCase();document.querySelectorAll('figure.anim').forEach(function(f){f.style.display=!s||f.dataset.n.indexOf(s)>=0?'':'none';});});})();
</script>''')
    return ''.join(out), m

CSS = ('.grid.anims{grid-template-columns:repeat(auto-fill,minmax(300px,1fr))}'
       'figure.anim{margin:0;background:var(--panel);border:1px solid var(--line);border-radius:8px;overflow:hidden}'
       'figure.anim .vw{position:relative}figure.anim video{display:block;width:100%;aspect-ratio:16/9;background:#111;cursor:zoom-in;object-fit:cover}'
       'figure.anim .big{position:absolute;right:8px;top:8px;width:40px;height:40px;border-radius:8px;border:0;background:rgba(0,0,0,.55);color:#fff;font-size:22px;line-height:40px;padding:0;cursor:pointer}'
       '#viewer{position:fixed;inset:0;z-index:100;background:rgba(8,10,14,.96);display:flex;flex-direction:column;justify-content:center;gap:10px;padding:12px 0}#viewer[hidden]{display:none}html.vopen{overflow:hidden}'
       '#viewer .vbar{display:flex;align-items:center;gap:10px;padding:0 14px;color:#fff}#viewer .vbar b{flex:1;font-family:"Shippori Mincho",Georgia,serif;font-size:1.15rem}'
       '#viewer video{width:100%;max-height:72vh;background:#000;object-fit:contain}#viewer .vd{margin:0;padding:0 14px;color:#d8dbe2;font-size:.95rem;line-height:1.4}'
       '#viewer .vbtn{display:flex;flex-wrap:wrap;gap:8px;padding:0 14px}#viewer button{min-height:44px;padding:0 14px;border-radius:8px;border:1px solid #3a4150;background:#1b2029;color:#fff;font-size:1rem;cursor:pointer}'
       '#viewer .vbtn button{flex:1 1 auto}'
       'figure.anim figcaption{padding:8px 10px}figure.anim figcaption b{display:block;font-family:"Shippori Mincho",Georgia,serif}'
       'figure.anim figcaption small{color:var(--muted)}figure.anim figcaption p{margin:6px 0 0;font-size:.9rem;line-height:1.4;color:var(--ink)}')

def build(page):
    b, m = body()
    page('animations.html', 'Animations', b, desc='Every hand-made technique animation, recorded in game.')
    return m

if __name__ == '__main__':
    out = sys.argv[1]
    b, m = body()
    # reuse an existing page as the shell: swap <main> and the title, mark the tab
    tpl = open(os.path.join(out, 'items.html'), encoding='utf-8').read()
    doc = re.sub(r'<main>.*</main>', lambda _: '<main>' + b + '</main>', tpl, flags=re.S)
    doc = re.sub(r'<title>.*?</title>', '<title>Animations · NFRP World</title>', doc).replace('<a href="items.html" class=on>', '<a href="items.html">')
    open(os.path.join(out, 'animations.html'), 'w', encoding='utf-8').write(doc)
    # the tab on every page (after Factions), marked "on" only on the animations page
    for f in glob.glob(os.path.join(out, '**', '*.html'), recursive=True):
        s = open(f, encoding='utf-8').read()
        if 'animations.html">Animations</a>' in s and not f.endswith('animations.html'): continue
        up = '../' * os.path.relpath(f, out).count(os.sep)
        s = re.sub(r'<a href="[./]*animations\.html"[^>]*>Animations</a>', '', s)
        on = ' class=on' if os.path.relpath(f, out) == 'animations.html' else ''
        s = re.sub(r'(<a href="' + re.escape(up) + r'factions\.html"[^>]*>Factions</a>)', r'\1<a href="' + up + 'animations.html"' + on + '>Animations</a>', s, count=1)
        open(f, 'w', encoding='utf-8').write(s)
    css = os.path.join(out, 'assets', 'style.css'); s = open(css, encoding='utf-8').read()
    if 'figure.anim' not in s: open(css, 'a', encoding='utf-8').write('\n' + CSS + '\n')
    print('animations:', len(m['clips']))
