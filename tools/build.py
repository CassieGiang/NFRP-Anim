#!/usr/bin/env python3
"""Rebuild index.html (the animations site) from tools/animations.json.  usage: python3 tools/build.py"""
import os, sys, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE); import animations
b, m = animations.body()
b = b.replace('src="anim/', 'src="clans-and-styles/').replace('poster="anim/', 'poster="clans-and-styles/')
doc = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Animations · NFRP World</title><meta name="description" content="Every hand-made technique animation in NFRP World, recorded in game.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@600;700&display=swap">
<link rel="stylesheet" href="assets/style.css"><link rel="icon" href="assets/icon.png">
</head><body>
<header><div class="hin"><a class="brand" href="index.html"><img src="assets/icon.png" alt=""><span>NFRP World</span></a>
<nav><a href="index.html" class=on>Animations</a></nav></div></header>
<main>{b}</main>
<footer>NFRP World is a RimWorld mod by Cassie, an add-on for World of Naruto and Taran Magic Framework. The Kazeraikou clan was created by Marii from NFRP and is used with her permission.</footer>
</body></html>'''
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(doc)
css = os.path.join(ROOT, 'assets', 'style.css'); s = open(css, encoding='utf-8').read()
s = re.sub(r'\n\.grid\.anims\{.*?\n', '\n', s, flags=re.S)
open(css, 'w', encoding='utf-8').write(s.rstrip() + '\n' + animations.CSS + '\n')
print('clips:', len(m['clips']))
