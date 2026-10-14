container-ship
==============

Container-ship (1998), an e-2 project commissioned by NMP (Network Museum Project, Japan): new work by contemporary artists, made for the Internet, around the metaphor of a cargo boat. This is the site as a Jekyll site for GitHub Pages, published from the e-2 organisation at e-2.org/c-ship/.

The pages are rebuilt from the 1998 originals (in git history, on `master`) with their text and images, and keep their addresses. The lettering, buttons and drawings are the original images; the layout around them is new, so the site works on any screen.

Content
-------

* `section.html`: the deck. The ship is drawn from its original slices, listed with their positions in `_data/deck.yml`, and scales with the page (`_includes/deck.html`). Rooms and containers light up and show their pictures on hover or keyboard focus, in CSS; the quay is off to the right, to scroll to.
* `_rooms/`: the bridge, about c-ship, platform, communications and the engine room.
* `_artists/`: about each artist (`aa*.html`).
* `_works/`: each artist's work (`ac*.html`), with credits and viewing requirements.
* `help.html`, `intro.html`: help and the introduction, which the deck used to open in pop-up windows.
* `index.html`: the front page, with the still the original showed instead of its Flash intro.

Layouts are in `_layouts/` (`room`, `artist`, `work`, `note`). `css/c-ship.css` is plain CSS (with nesting), loading `css/modules/` and `css/partials/` with `@import`.

Kept as they were
-----------------

* `projects/`: the artworks, which are to move to their own repositories.
* The Flash intro (`index.swf`, `anim.swf`, `animdark.swf`, `cov2.swf`, `cov3.swf`), the older FutureSplash intro (`indexold.html`, `cov4.spl`), and Pig's Tails' launcher (`apgo.html`), which need Flash.
* `css/style.css`, `css/tabs.css`, which no page uses.

Running it locally
------------------

```
bundle install
bundle exec jekyll serve
```

then open http://localhost:4000/c-ship/
