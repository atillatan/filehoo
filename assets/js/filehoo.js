/* Filehoo 2026 — vanilla JS: theme toggle, instant search, favorites. No dependencies. */
(function () {
  "use strict";

  /* ---------------- Theme ---------------- */
  var root = document.documentElement;
  function currentTheme() {
    var attr = root.getAttribute("data-theme");
    if (attr) return attr;
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }
  function initTheme() {
    var btn = document.querySelector(".theme-toggle");
    if (!btn) return;
    btn.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("fh-theme", next); } catch (e) {}
    });
  }

  /* ---------------- Instant search ---------------- */
  var index = null, loading = false;
  function loadIndex(cb) {
    if (index) return cb();
    if (loading) return;
    loading = true;
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/search.json", true);
    xhr.onload = function () {
      try { index = JSON.parse(xhr.responseText); } catch (e) { index = []; }
      cb();
    };
    xhr.send();
  }

  function score(item, q) {
    var name = item.n.toLowerCase();
    if (name === q) return 100;
    if (name.indexOf(q) === 0) return 80;
    if (name.indexOf(q) > -1) return 60;
    if (item.c && item.c.toLowerCase().indexOf(q) > -1) return 30;
    if (item.t && item.t.toLowerCase().indexOf(q) > -1) return 20;
    return 0;
  }

  function initSearch() {
    var box = document.querySelector(".search-box");
    if (!box) return;
    var input = box.querySelector("input");
    var panel = box.querySelector(".search-results");
    var sel = -1, items = [];

    function close() { panel.classList.remove("open"); sel = -1; }

    function render(q) {
      var results = [];
      for (var i = 0; i < index.length; i++) {
        var s = score(index[i], q);
        if (s > 0) results.push([s, index[i]]);
      }
      results.sort(function (a, b) { return b[0] - a[0] || a[1].n.localeCompare(b[1].n); });
      results = results.slice(0, 10);
      items = results;
      if (!results.length) {
        panel.innerHTML = '<div class="empty">No results for &ldquo;' +
          q.replace(/&/g, "&amp;").replace(/</g, "&lt;") + '&rdquo;</div>';
      } else {
        var html = "";
        for (var j = 0; j < results.length; j++) {
          var it = results[j][1];
          html += '<a href="' + it.u + '"><span class="r-name">' + esc(it.n) +
            '</span><span class="r-cat">' + esc(it.c || "") + "</span></a>";
        }
        panel.innerHTML = html;
      }
      panel.classList.add("open");
    }

    function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;"); }

    input.addEventListener("focus", function () { loadIndex(function () {}); });
    input.addEventListener("input", function () {
      var q = input.value.trim().toLowerCase();
      if (q.length < 2) { close(); return; }
      loadIndex(function () { render(q); });
    });
    input.addEventListener("keydown", function (e) {
      var links = panel.querySelectorAll("a");
      if (e.key === "Escape") { close(); input.blur(); }
      else if (e.key === "ArrowDown" && links.length) { e.preventDefault(); sel = (sel + 1) % links.length; mark(links); }
      else if (e.key === "ArrowUp" && links.length) { e.preventDefault(); sel = (sel - 1 + links.length) % links.length; mark(links); }
      else if (e.key === "Enter" && links.length) { e.preventDefault(); (links[sel > -1 ? sel : 0]).click(); }
    });
    function mark(links) {
      for (var i = 0; i < links.length; i++) links[i].classList.toggle("sel", i === sel);
    }
    document.addEventListener("click", function (e) { if (!box.contains(e.target)) close(); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "/" && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) {
        e.preventDefault(); input.focus();
      }
    });
  }

  /* ---------------- Favorites (My Apps) ---------------- */
  var FAV_KEY = "fh-favs";
  function getFavs() {
    try { return JSON.parse(localStorage.getItem(FAV_KEY)) || []; } catch (e) { return []; }
  }
  function setFavs(f) { try { localStorage.setItem(FAV_KEY, JSON.stringify(f)); } catch (e) {} }

  function initFavButton() {
    var btn = document.querySelector(".fav-toggle");
    if (!btn) return;
    var url = btn.getAttribute("data-url"), name = btn.getAttribute("data-name");
    function refresh() {
      var on = getFavs().some(function (f) { return f.u === url; });
      btn.classList.toggle("on", on);
      btn.title = on ? "Remove from My Apps" : "Add to My Apps";
      var label = btn.querySelector("span");
      if (label) label.textContent = on ? "Saved to My Apps" : "Add to My Apps";
    }
    btn.addEventListener("click", function () {
      var favs = getFavs();
      var i = favs.findIndex(function (f) { return f.u === url; });
      if (i > -1) favs.splice(i, 1); else favs.push({ u: url, n: name });
      setFavs(favs); refresh();
    });
    refresh();
  }

  function initFavList() {
    var wrap = document.querySelector(".my-apps");
    if (!wrap) return;
    var favs = getFavs();
    if (!favs.length) { wrap.style.display = "none"; return; }
    var html = "";
    favs.forEach(function (f) {
      html += '<a class="app-card" href="' + f.u + '"><span class="name">' +
        String(f.n).replace(/&/g, "&amp;").replace(/</g, "&lt;") + "</span></a>";
    });
    wrap.querySelector(".app-grid").innerHTML = html;
    wrap.style.display = "";
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else { boot(); }
  function boot() { initTheme(); initSearch(); initFavButton(); initFavList(); }
})();
