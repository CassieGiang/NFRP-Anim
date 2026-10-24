/* Native, keyboard-accessible category sections, shared by all clip pages. */
(function () {
  'use strict';
  var categories = Array.from(document.querySelectorAll('details.anim-category'));
  if (!categories.length) return;
  var allDetails = Array.from(document.querySelectorAll('main details'));
  var toolbar = document.querySelector('.toolbar');
  var search = document.getElementById('animq');
  var beforeSearch = null;
  var count = document.createElement('span');
  count.className = 'count';
  count.setAttribute('role', 'status');
  count.setAttribute('aria-live', 'polite');

  function shown(video) {
    if (video.closest('figure').style.display === 'none') return false;
    for (var d = video.closest('details'); d; d = d.parentElement.closest('details')) {
      if (!d.open || d.hidden) return false;
    }
    return true;
  }

  function syncVideos() {
    document.querySelectorAll('figure.anim video').forEach(function (video) {
      if (!shown(video)) video.pause();
      else if (!('IntersectionObserver' in window)) {
        video.preload = 'auto';
        var playing = video.play();
        if (playing && playing.catch) playing.catch(function () {});
      }
    });
  }

  function button(label, open) {
    var b = document.createElement('button');
    b.type = 'button';
    b.textContent = label;
    b.addEventListener('click', function () {
      categories.forEach(function (d) { if (!d.hidden) d.open = open; });
      syncVideos();
    });
    toolbar.appendChild(b);
  }
  if (toolbar) {
    button('Expand all', true);
    button('Collapse all', false);
    toolbar.appendChild(count);
  }

  function filter() {
    var term = search ? search.value.trim().toLowerCase() : '';
    if (term && !beforeSearch) {
      beforeSearch = new Map(allDetails.map(function (d) { return [d, d.open]; }));
    }
    var matches = 0;
    categories.forEach(function (category) {
      var visible = 0;
      category.querySelectorAll('figure.anim').forEach(function (card) {
        var match = !term || (card.dataset.n || '').indexOf(term) !== -1;
        card.style.display = match ? '' : 'none';
        if (match) {
          visible++;
          matches++;
          if (term) {
            for (var d = card.closest('details'); d && d !== category; d = d.parentElement.closest('details')) d.open = true;
          }
        }
      });
      category.hidden = !!term && !visible;
      if (term) category.open = visible > 0;
    });
    if (!term && beforeSearch) {
      beforeSearch.forEach(function (open, d) { d.open = open; });
      beforeSearch = null;
    }
    count.textContent = matches + (matches === 1 ? ' clip' : ' clips') + (term ? ' found' : '');
    syncVideos();
  }

  function revealHash(hash, scroll) {
    if (!hash || hash === '#') return;
    var id;
    try { id = decodeURIComponent(hash.slice(1)); } catch (_) { return; }
    var target = document.getElementById(id);
    if (!target || !target.closest('main')) return;
    // A category link should remain usable even after a search hid its target.
    if (target.hidden && search) { search.value = ''; filter(); }
    for (var d = target.closest('details'); d; d = d.parentElement.closest('details')) d.open = true;
    if (scroll) requestAnimationFrame(function () { target.scrollIntoView({ block: 'start' }); });
  }
  allDetails.forEach(function (d) { d.addEventListener('toggle', syncVideos); });
  if (search) search.addEventListener('input', filter);
  document.addEventListener('click', function (event) {
    var link = event.target.closest('.toc a[href^="#"]');
    if (link) revealHash(link.hash, true);
  });
  window.addEventListener('hashchange', function () { revealHash(location.hash, true); });
  filter();
  revealHash(location.hash, true);
})();
