# container-ship

Container-ship (1998) was an e-2 project commissioned by NMP (Network Museum Project, Japan) consisting of new work by contemporary artists made for the Internet. This is a rebuild of the original site which incorporates modern technologies, accessibility enhancements and is built using Jekyll.

The pages are rebuilt from the 1998 originals (in git history, on the `main` branch) with their text and images, and keep their addresses. The drawings are the original images; the lettering is now text, in a font made from the original lettering images; the layout around them is new, so the site works on any screen.

## Content

* `section.html`: the deck. The ship is drawn from its original slices, listed with their positions in `_data/deck.yml`, and scales with the page (`_includes/deck.html`), with the quay beside it on wide screens. Rooms and containers light up and show their pictures on hover, keyboard focus or a first tap (`js/deck.js`), and the pictures link to their room or project. Help and the introduction open in overlays.
* `_rooms/`: the bridge, about c-ship, platform, communications and the engine room.
* `_artists/`: about each artist (`aa*.html`).
* `_works/`: each artist's work (`ac*.html`), with credits. Each launches the work from its own repository on the e-2 site (`/adelaide/`, `/tome/tome.html` and so on); Cruisin' has no link.
* `help.html`, `intro.html`: help and the introduction as pages, sharing their text (`_includes/help.html`, `_includes/intro.html`) with the deck's overlays.
* `index.html`: the front page, with the still the original showed instead of its Flash intro.
`_sessions/` has a summary and transcript of each working session with Claude Code.

Layouts are in `_layouts/` (`room`, `artist`, `work`, `note`). `css/c-ship.css` is plain CSS (with nesting), loading `css/modules/` and `css/partials/` with `@import`.

## The lettering font

`fonts/c-ship-lettering.woff2` was made from the 1998 lettering images, which are kept in `_fonts/sources/`. The scripts that made it, and how to rebuild it, are in `_fonts/` (see `_fonts/README.md`).

## The artworks

`_projects/` holds the artworks as they were hosted on container-ship in 1998. Each is now worked on in its own repository under the e-2 organisation (adelaide, ahouse, bird-island, error404, nowhere, pigstails, tome). Cruisin' was hacked and lost in 2000. These copies are kept for reference and aren't part of the site.

The Flash and FutureSplash intros, the old stylesheets and the gulp setup were removed in October 2026; they are in git history.

## Running it locally

```
bundle install
bundle exec jekyll serve
```

then open http://localhost:4000/c-ship/

## Layout

The original files are at the top of this repository. The current version of the site is in `docs/`, which is what GitHub Pages publishes. To run it locally, use the commands below from inside `docs/`. Summaries and transcripts of the Claude Code sessions are in `_sessions/`.
