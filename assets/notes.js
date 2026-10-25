// Comment boxes on the "Showcase: hero animations" tab: kept in this browser (localStorage), saved to one text file or copied.
(function () {
  var KEY = 'nfrp-notes:' + location.pathname, notes = {};
  try { notes = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { notes = {}; }
  var boxes = Array.prototype.slice.call(document.querySelectorAll('textarea.cmt'));
  function count() { var n = 0; for (var k in notes) if (notes[k] && notes[k].trim()) n++; var c = document.getElementById('notecount'); if (c) c.textContent = n ? n + ' commented' : ''; }
  function store() { try { localStorage.setItem(KEY, JSON.stringify(notes)); } catch (e) {} count(); }
  boxes.forEach(function (t) {
    t.value = notes[t.dataset.k] || ''; t.classList.toggle('has', !!t.value.trim());
    t.addEventListener('input', function () { notes[t.dataset.k] = t.value; t.classList.toggle('has', !!t.value.trim()); store(); });
    t.addEventListener('click', function (e) { e.stopPropagation(); });
  });
  function text() {
    var out = ['NFRP World - Showcase: hero animations - comments', ''];
    boxes.forEach(function (t) { var v = (notes[t.dataset.k] || '').trim(); if (v) out.push('#' + t.dataset.i + ' ' + t.dataset.l + ' [' + t.dataset.k + ']', '  ' + v.split('\n').join('\n  '), ''); });
    return out.join('\n');
  }
  var s = document.getElementById('notesave'), c = document.getElementById('notecopy');
  function save() { var a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([text()], { type: 'text/plain' })); a.download = 'hero-animations-comments.txt'; document.body.appendChild(a); a.click(); a.remove(); }
  if (s) s.onclick = save;
  // a save button under every technique's box: saves all comments to one file, without scrolling back to the top
  Array.prototype.slice.call(document.querySelectorAll('button.cmtsave')).forEach(function (b) {
    b.addEventListener('click', function (e) { e.stopPropagation(); save(); var st = b.parentNode.querySelector('.cmtstate'); if (st) { st.textContent = 'Saved'; setTimeout(function () { st.textContent = ''; }, 1500); } });
  });
  if (c) c.onclick = function () { navigator.clipboard.writeText(text()).then(function () { c.textContent = 'Copied'; setTimeout(function () { c.textContent = 'Copy all comments'; }, 1200); }); };
  count();
})();
