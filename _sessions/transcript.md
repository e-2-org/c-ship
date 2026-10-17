# container-ship - session transcripts

Transcripts of two Claude Code sessions on the `jekyll` branch, oldest first. Summaries are in [summary.md](summary.md).

## e-2 and c-ship to Jekyll - session transcript

Transcript of a Claude Code session on 2026-10-08, converting e-2.org and container-ship to Jekyll for GitHub Pages. The same transcript is in both repositories (`e-2` and `c-ship`). Tool calls are shown as one-line notes; their output is omitted. Message times weren't recorded, so only the date is given. Claude's longer replies are shortened where they repeat what the summaries record.

---

### User - 2026-10-08

My next project is converting the website of my old organisation (e-2.org) to a jekyll site so I can move it to GitHub Pages. This will form an organisation site, with projects in organisation repos. The current site is flat HTML in ~/repos/e-2. The other port I want to do to jekyll is one of the umbrella projects (~/repos/c-ship) where some of the projects were hosted.

### Claude

I'll start by looking at both sites: their size, structure, and how the pages are built.

> *Bash: Survey the e-2 and c-ship site folders*

> *Bash: List e-2 pages and build files*

> *Bash: Read e-2 home page, a commission page and the JS*

Every e-2 page shares the same skeleton: a two-column layout, the same footer, and analytics, with only the column contents changing.

> *Bash: Read the body of each e-2 page type*

> *Bash: List c-ship pages, folders and build files*

> *Bash: Summarise c-ship's hosted projects*

> *Bash: Read c-ship home and intro pages*

> *Bash: Read c-ship section and a container page*

I have enough to see the shape of both sites, but a few decisions are yours.

- **e-2:** 27 pages, a 2018 two-column design with SCSS. Two lists, projects (9) and commissions (11). Many links point at subdomains, redirected by `.htaccess`, which GitHub Pages can't do. One page is a QuickTime VR panorama.
- **c-ship:** 24 pages from 1998 (image-based table layouts, rollovers, a Flash intro, server-side image maps), plus eight hosted artworks in `projects/`.

> *AskUserQuestion: URLs, c-ship's look, where the artworks live, dead technology*

Answers: paths under e-2.org; c-ship modernised in the same spirit; each artwork in its own repo; dead technology kept and noted for later.

> *Bash: Check repo state, remotes and Jekyll tooling*

### User (sent while Claude was working) - 2026-10-08

The c-ship site contains some of the projects, which I want to move to different repositories (the VRML and Flash are projects) so please ignore these fo0r now

### Claude

Understood. I'll leave everything in `c-ship/projects/` alone; the c-ship work covers only the container-ship pages themselves.

> *Bash: Extract e-2 page contents and style references*

> *Bash: Read navigation and layout styles*

My plan for e-2 on a new `jekyll` branch: each project and commission becomes a document in `_projects/` or `_commissions/`; the home and index pages list from the collections; one layout and footer include replace the copied markup; Jekyll compiles the SCSS; launch links stay as they are for now.

> *Bash: Create branch and move SCSS into Jekyll's places*

### User (sent while Claude was working) - 2026-10-08

I've made a start on some of the projects I'm most familiar with

### Claude

Noted. Before going further, I'll check what you've started, so I don't duplicate it or conflict with it.

> *Bash: Check the project repos you've started*

### User (sent while Claude was working) - 2026-10-08

I'll treat Tome and other projects as separate task. each managed in their own repositories

### Claude

Understood: this job covers only the e-2 site and the c-ship container-ship pages. I can't see your start in `bird-island`, `minus20` or `contact` (their latest commits are from 2018), so I assume it's elsewhere. Nothing here conflicts with it.

> *Bash: Convert project and commission pages to collection docs*

> *Bash: Remove the old flat pages and node build files*

> *Bash: Write config, Gemfile and CNAME; add SCSS front matter*

> *Bash: Write layouts, list and footer includes*

> *Bash: Write home, index, about and contact pages; recreate projects index and build the site*

> *Bash: Screenshot original and Jekyll e-2 side by side*

> *Read: side-by-side screenshots*

> *Bash: Pixel-compare every page at two widths*

> *Bash: Inspect the one page that differs; compare bird island logo markup*

Bird island has a second column block after the first one's end marker, which the converter missed. I'll add its logo to the front matter.

> *Bash: Add bird island logo and recheck*

### User (sent while Claude was working) - 2026-10-08

I'd rather the CSS was plain CSS (with nesting) with the partials and modules loaded using import

### Claude

Understood: plain CSS using native nesting, with the partials pulled in by CSS `@import`, and no Sass.

> *Bash: Find Sass-only features in the styles*

No mixins or functions, just variables, nesting and nested media queries. Colours become custom properties; breakpoints become literal values in the media queries (custom properties can't be used there); the disabled legacy blocks in normalize are dropped; the unused `_navigation_old` partial is left out.

> *Bash: Convert SCSS partials to plain CSS files*

> *Bash: Switch to plain CSS imports and recheck all pages (git rm refused part way)*

> *Bash: Remove Sass sources properly and recheck all pages*

> *Bash: Locate and zoom the logo difference*

Progress update: e-2 now builds with Jekyll and plain CSS, and every page matches the original pixel for pixel at 1200, 800 and 400px wide, except bird island's Arts Council logo, which now sits 16px higher, consistent with the other pages.

> *Bash: Add redirect pages and update .gitignore*

> *Write: README.md (e-2)*

> *Bash: Screenshot every c-ship page; contact sheet*

> *Read: contact sheet*

> *Bash: Screenshot the deck page and read its markup*

The deck is a 1998 table of image slices. I'll measure where every slice sits in the original, then place them in one scalable deck, with the containers as real links named after the artists.

> *Bash: Outline the content of an artist pair and a room; check apgo, indexold and the deck's pop-up functions*

> *Bash: Measure deck slice positions and hover images*

> *Bash: Read hover preview images and create the branch*

> *Bash: Write the deck's data file from the measurements*

> *Bash: Add light hovers and check for BeautifulSoup*

> *Bash: Extract artist pages, room content and work pages*

> *Bash: Generate c-ship's room, artist and work documents (fixes: credit labels, the bridge's content, rows without links, YAML lists)*

> *Bash: Check button images; contact sheet*

> *Read: button images*

The buttons are coloured dots that reveal a label on hover. The deck can do all its hover effects in plain CSS with `:has()`.

> *Bash: Write c-ship config, Gemfile and base layout*

> *Bash: Write room, artist and work layouts*

> *Bash: Write note layout, deck, front page; remove old pages*

> *Bash: Check c-ship's existing CSS (unused style.css and tabs.css left as they are)*

> *Bash: Write c-ship's CSS and build the site*

> *Bash: Screenshot the new c-ship at two widths*

> *Read: screenshots*

The artist and work pages rendered navy: the base layout read `page.theme`, where a layout's own front matter is `layout.theme`. Fixed.

> *Bash: Fix layout theme lookup and re-screenshot*

> *Bash: Test deck hover panels and keyboard focus*

> *Read: hover screenshots*

> *Write: README.md (c-ship)*

> *Bash: Stage both branches; remove the temporary comparison worktree*

Both sites are now Jekyll sites ready for GitHub Pages, each on a new `jekyll` branch, staged but not committed, both with plain CSS (nesting, `@import`).

- **e-2:** collections for projects and commissions; same URLs; pixel-identical to the original except bird island's logo; redirect pages for `/perhect/` and `/projman/`; gulp, npm, `js/e-2.js` and the old Analytics removed; `CNAME` added.
- **c-ship:** the deck from its 29 original slices, scaling with the window and lighting up on hover or keyboard focus; rooms, artist and work pages rebuilt with their original lettering; same URLs; `projects/`, the Flash and FutureSplash intros and `apgo.html` untouched.
- **Noted for later:** the Flash intros, the QuickTime VR panorama, and e-2's launch links, which still point at the current subdomains.

### User - 2026-10-08

Can you make an SVG from images/logos/e2_160.gif and use that instead

### Claude

I'll look at the logo first, and check whether a tracing tool is available.

> *Bash: Inspect the logo GIF and tracing tools*

> *Read: the logo at 8x*

The logo is simple enough to rebuild as clean vectors: a black-outlined pill, white on the left and grey (#999) on the right, "e-2" in a bold sans-serif and "ORG" in white. I'll set the lettering in a Helvetica-like font and convert it to outlines.

> *Bash: Find a Helvetica-like bold font (Nimbus Sans Bold)*

> *Bash: Measure the logo's parts in the GIF*

> *Bash: Build the SVG logo and compare with the GIF*

> *Read: comparison*

Progress update: the lettering lines up; the original's ends are flatter ellipses, so the outline gets elliptical corners.

> *Bash: Use elliptical ends and recompare*

> *Bash: Use the SVG in the footer and screenshot it (the test server lacked the SVG type; fixed)*

> *Read: footer screenshot*

> *Bash: Stage the new logo and footer change*

The footer now uses `images/logos/e2.svg`: a pill rebuilt from the GIF's measurements, with "e-2" and "ORG" as Nimbus Sans Bold outlines fitted to the GIF's letters, 2.4KB at 160×46. The old GIF is unused but left in place.

### User - 2026-10-08

I've made a couple of adjustments

### Claude

> *Bash: Show unstaged changes in e-2 and c-ship*

> *Bash: Render the edited logo beside the GIF and my version*

> *Read: comparison*

Your edits read well: the slanted hyphen, the narrower "r" and the square dot on the colour split are closer to the original. One thing the Inkscape optimisation broke: the `<title>` element's id became `b`, but `aria-labelledby` still says `e2-logo-title`. It doesn't matter while the logo is an `<img>`, but would if the SVG were inlined. `e2-inkscape.svg` is untracked: commit it as the source, or ignore it?

### User - 2026-10-08

OK that's it for today - please create a summary and transcript like before in the e-2 and c-ship repository folders under _sessions

### Claude

> *Write: _sessions/2026-10-08-transcript.md (e-2 and c-ship)*

> *Write: _sessions/2026-10-08-summary.md (e-2)*

> *Write: _sessions/2026-10-08-summary.md (c-ship)*

I've written a summary to each repo's `_sessions` folder, and this transcript to both.

---

## container-ship - session transcript

Transcript of a Claude Code session on 2026-10-14, fixing and extending the Jekyll version of container-ship. Tool calls are shown as one-line notes; their output is omitted. Message times weren't recorded, so only the date is given. Claude's longer replies are shortened where they repeat what the summary records.

---

### User - 2026-10-14

I'm looking at repos/c-ship and have spotted some errors:
- When some of the hotspots on the deck are hovered over, the mages/indexb.gif image remains in place - in the live version this is replaced
- Although the original showed a dock with 4 containers off screen - I'd rather the dock be on screen. The ship could take up 2/3 of the screen width, with the dock right-aligned in the remainder. Smaller screens should not display the dock
- on touchscreen devices, touching one of the containers should show the relevant info box like hovering does with a mouse
- rather than opening new pages, help and info should use overlays

### Claude

> *Bash: Survey the c-ship repo*

> *Bash: Read deck data, templates and CSS*

> *Bash: Read original deck and help page source*

> *Bash: Read rest of original deck and intro*

> *Bash: Check image sizes and available tools*

> *Bash: Check transparency of room previews*

The room pictures (about2.gif and the rest) are transparent GIFs layered over indexb.gif; the original swapped the image's `src`, so nothing showed through.

> *Bash: Read base CSS and find help/intro links*

> *Bash: Move help and intro text into includes*

> *Edit: deck.yml (overlay: help, overlay: intro)*

> *Write: _includes/deck.html*

> *Write: js/deck.js*

> *Bash: Rewrite deck CSS and build the site*

> *Bash: Serve site and take screenshots at several widths*

> *Bash: Test hover, overlay and touch taps in headless Chrome*

All four fixed and tested: the panel's own image is hidden while a room or container is lit; the ship takes two thirds of the width with the quay right-aligned (hidden below 60em, with no sideways scroll); the first tap on a touch screen shows a container's picture and the second opens it; help and the introduction open in `<dialog>` overlays, sharing their text with the pages through includes. The help text still talks of the cursor and Netscape Navigator 3.

### User - 2026-10-14

Can the ship stop shrinking when it reaches the breakpoint? ideally users on small screens would scroll to see the rest of the ship - the detail in the images starts to disappear as the image is scaled down

### Claude

> *Edit: deck.css (clamp the ship's width; scroll the harbour sideways)*

> *Bash: Measure ship width across viewport widths*

Below the breakpoint the ship stays the size it was there (about 624px, 63% of its drawn size) and scrolls sideways, on its own, under the fixed credit line. It could stay at full drawn size instead, if that's still too small.

### User - 2026-10-14

Somethings not quite right - I now have a vertical scrollbar and parts of the ship do not align correctly

### Claude

> *Bash: Measure vertical overflow and slice positions*

> *Bash: Compare deck.yml sizes with real image sizes*

> *Bash: Inspect the overflowing slices' boxes*

### User (sent while Claude was working) - 2026-10-14

Can the credit line be placed at the bottom of the page?

### Claude

> *Bash: Find CSS rules matching room or container*

The misalignment was there from the first conversion: the deck's room links had the class `room`, which the room pages' stylesheet also uses (padding, a grid), so the hotspots were knocked out of place and two slices hung below the ship. Once the ship scrolled sideways, that overflow became a vertical scrollbar.

> *Bash: Prefix deck room and container classes*

> *Edit: deck.css (credit line at the foot of the window; no vertical scrolling)*

> *Bash: Re-measure layout and re-run interaction tests*

> *Edit: deck.css (dark scrollbar)*

The deck's classes are now `deck-room` and `deck-container`; nothing overflows; the credit line sits at the foot of the window; the sideways scrollbar is dark grey on navy.

### User - 2026-10-14

The artists names in bridge.html are images - can these be swapped for text?

### Claude

> *Bash: Read the bridge page, room layout and styles*

> *Bash: Get original alt text and view name images*

> *Bash: Swap name images for artist names in bridge data*

> *Edit: room.html, rooms.css (red bold names with a shadow, like the images)*

> *Bash: Rebuild and screenshot the bridge page*

### User (sent while Claude was working) - 2026-10-14

Ideally the text will be in a standard font and orange like the other links

### Claude

> *Edit: rooms.css, room.html (plain links)*

> *Bash: Rebuild and screenshot the project list*

The names are plain text, orange and underlined like the other links. Anna Best and Janice Kerbel aren't links, as in the original.

### User - 2026-10-14

The links to index pages and about the artist on item pages are invisible until they are hovered over (white text) and they move around when hovered. can these be made into plain text? and the bullets made using CSS rather than images. What is the font used in the titles and these links? is it possible to use a fiont instead?

### Claude

> *Bash: Read work and artist layouts and their CSS*

> *Bash: View button and lettering images*

> *Bash: Find every use of the dot buttons*

> *Bash: Turn dot buttons into text links in layouts*

> *Bash: Add dot CSS, rebuild and screenshot pages*

The links are plain text with CSS dots. The lettering is a monospaced, "unicase" 1990s display face I can't name with confidence. Major Mono Display is the nearest free font; the trade-off is that the titles are the original 1998 lettering.

### User - 2026-10-14

Yes, lets have a look

### Claude

> *Bash: Download Major Mono Display font and licence*

> *Bash: Save licence, take before screenshots, sample colours*

> *Bash: Sample main colour of each work title*

> *Bash: Add font-face and use it for titles and room menu*

> *Edit: rooms.css (CSS arrows for the room menu), artists.css*

> *Bash: Rebuild and make before/after comparison*

### User (sent while Claude was working) - 2026-10-14

Can you make a font from the images?

### Claude

Major Mono Display is all caps-style, thin and wide, and doesn't match. Making a font from the lettering images is a better idea.

> *Bash: Inventory lettering images and font tools*

> *Bash: Contact sheet of all lettering images*

> *Bash: Set up venv and measure lettering sizes*

> *Bash: Zoom in on name and title lettering*

> *Bash: Dump name lettering as ASCII pixels*

> *Bash: Dump the other artist name images*

It's a true unicase design, drawn at three or four sizes. The six artist names (13px a letter, crisp) give 21 letters; p, k, x and a little punctuation appear only in the smaller lettering; j, q, z and most figures appear nowhere.

> *Bash: Install potrace port and check FontForge Python*

> *Write: extract.py (cut out, smooth and trace the letters)*

> *Bash: Extract and trace glyphs*

### User (sent while Claude was working) - 2026-10-14

Can you fill in any missing letters?

### Claude

Yes, once the traced ones are in.

> *Bash: Re-run glyph extraction*

> *Bash: Limit columns per source and re-run*

> *Write: build.py (build the font with fontTools)*

> *Bash: Build font and render a specimen*

> *Bash: Fix inverted tracing and rebuild*

> *Bash: Dump small source glyphs as ASCII*

The figures are old-style (the 4 in "error 404" descends) and p has a descender.

> *Write: drawn.py (the missing letters, drawn on the names' pixel grid)*

> *Bash: Trace drawn glyphs, rebuild, render specimen*

> *Bash: Smooth drawn glyphs and re-render*

> *Bash: Install font and build scripts into repo*

> *Bash: Point the lettering style at the new font*

> *Bash: Rebuild and compare before and after*

The font, "C-Ship Lettering", is in `fonts/`, with the scripts in `_fonts/`, and replaces Major Mono Display on the work titles and room menu. The room menu is a little heavier than the original small lettering. The original was almost certainly a commercial typeface, which matters if the font file itself were distributed.

### User - 2026-10-14

Can the remaining images containing the font be switched to use the font, along with the project titles on bridge.html

### Claude

> *Bash: Find remaining lettering images and their colours*

The room heading images don't say the room's name: they say "programme", "ideas and intentions" and so on.

> *Bash: Measure bracket and room heading text*

> *Bash: Replace room heading images with their wording*

> *Bash: Switch layouts from lettering images to text*

> *Bash: Simplify artist and work front matter*

> *Bash: Style the text headings, back link and name*

> *Bash: Rebuild and screenshot converted pages*

> *Bash: Fix help back link colour and check for leftover lettering images*

Room headings, "back to artists and index", the artist names (with a CSS bracket) and the bridge's project titles are text in the font. No built page uses a lettering image.

### User - 2026-10-14

The original bullets in the menu on pages like bridge.html and engione.html consisted of two triangles, one filled and one outline, with the filled triangleoffset to the left and above the outline triangle. hovering cause the filled triangle to shift over the outline - can this bve replicated?

### Claude

> *Bash: Dump the original menu arrows, normal and hover*

> *Bash: Check text colour in normal and hover images*

> *Edit: rooms.css (two triangles; the filled one slides over the outline)*

> *Bash: Screenshot menu arrows normal and hovered*

> *Bash: Thin the outline triangle and re-render*

Replicated with two pseudo-elements and `clip-path`. In the original images the triangles are level, not offset upwards, so that's what's copied.

### User - 2026-10-14

Can you put a left margin on the link back to artists and index and title on the about.html, bridge.html etc. pages so when it shifts under the image is has the same margin as the text.

### Claude

> *Edit: rooms.css (stack the header under the picture, with a 1em margin, at 640px and below)*

> *Bash: Rebuild and screenshot room header at three widths*

Done; the link, heading, menu and text share the same left edge on small screens.

### User - 2026-10-14

Can you increase the font size ogf the headings

### Claude

> *Bash: Enlarge room headings and screenshot*

The orange room headings are 1.2em, the size of the work titles.

### User - 2026-10-14

can you increase the spacing between nav.room and .room content on larger screens so it lines up underneaththe title

### Claude

> *Bash: List room picture widths*

> *Bash: Widen menu column and measure alignment*

The menu column is 220px, the width of the room pictures; the heading and text both start 236px from the left.

### User - 2026-10-14

can you change the index page and about the artist links on the item pages to use the font. Ideally in the same colour as their bullet, shift8ing to black on hover / active

### Claude

> *Bash: Use the font and dot colours for item page links, then test*

Done. Orange on white is about 2:1 contrast, below what's recommended for text.

### User - 2026-10-14

When a container is clicked on the section.html page, it shows part of an image in the container and the image/artist name in a space above the ship. Can both theseareas be linked to the relevant project rather than just the container

### Claude

> *Bash: Find the preview markup and styles*

> *Bash: Make panel pictures links*

> *Bash: Keep the last hotspot lit and allow tapping pictures*

> *Bash: Test linked panel pictures with mouse and touch*

> *Bash: Add hover delay and re-run tests*

The pictures in the panels link to their project (or room). With a mouse, the last one pointed at stays lit so the picture can be reached; a 150ms delay stops another room taking over on the way across.

### User - 2026-10-14

Can the intro and help links on the home page be converterd to text like the links on the project pages? with the text the same colour as the bullet, changing to white on hover

### Claude

> *Bash: View the help and intro dot images*

> *Bash: Replace help and intro images in deck data*

> *Bash: Render dot links as text and style them*

> *Bash: Screenshot deck dot links and test overlays*

"help" and "intro" are text links with CSS dots, scaled with the ship (at least 11px), white on hover, still opening the overlays.

### User - 2026-10-14

on bridge.html, can the artists names links lose the underline, and the titles be made into links - removing the single quotes. link the artist name to the artist page and the project title to the project page. Should these be titles?

### Claude

> *Bash: Read bridge data, layout and project styles*

> *Bash: Add artist and project links to bridge data*

> *Bash: Render titles as heading links and check*

> *Bash: Rename clashing class and re-render*

Yes: the titles are `h3` headings, under an `h2` "Artists' projects", linking to the project pages; the names link to the artist pages without an underline. Anna Best has no artist page and Janice Kerbel's project was external, so their names are plain text.

### User - 2026-10-14

Can you make a project page for bird island so it behaves like the rest? acjk.html The project will eventually be at /bird-island/ in another repo under the e-2 github org - take the text from the bird-island repo readme (make shorter) Technical Director was Peter Moore. And get rid of all those Viewing requirements!

### Claude

> *Bash: Read bird-island README and an existing work page*

> *Bash: Look for Bird Island images and launch pictures*

> *Bash: List Bird Island images and view launch strips*

> *Bash: Measure the picture window in launch strips*

> *Bash: Check the aerial photo in the bird-island repo*

> *Bash: Make the Bird Island launch strip image*

> *Bash: Read Gill Ord's work page for the credit format*

> *Write: _works/acjk.html*

> *Bash: Leave root and external launch links unchanged*

> *Bash: Drop viewing requirements and link Bird Island page*

> *Bash: Build and check the Bird Island page*

> *Bash: Shorten the Bird Island description*

`acjk.html` is made, with a launch picture made from the island photo in the bird-island repo; the deck and the bridge link to it; Viewing requirements are gone from every project.

### User - 2026-10-14

All the other projects have repos under e-2 (apart from Cruisin') - can you change the links to these as well - adelaide, error404, tome, ahouse, nowhere and pigstails

### Claude

> *Bash: Check each project repo's entry page and remote*

> *Bash: Point launch links at the project repos*

> *Bash: Update artist page launch links and check output*

The project and artist pages launch the works from `/adelaide/`, `/error404/`, `/tome/tome.html`, `/ahouse/`, `/nowhere/` and `/pigstails/`. The local error404 checkout's remote is `bjorsq/error404`. `projects/` and `apgo.html` are no longer linked.

### User - 2026-10-14

Can you update the files in _sessions please

### Claude

> *Bash: Inspect existing session files*

> *Write: 2026-10-14-summary.md*

> *Write: 2026-10-14-transcript.md*

### User - 2026-10-14

Great!

### Claude

Everything is still uncommitted on the `jekyll` branch.

### User - 2026-10-14

I've committed the changes now - what is left in this branch which isn't being used? can it be deleted?

### Claude

> *Bash: Show repo state and tracked files by folder*

> *Bash: List remaining top-level files, projects and config*

> *Bash: Find images not referenced by any source file*

> *Bash: Check project references, font sources, other root files*

> *Bash: Check index.swf, cruisin, htaccess and project repos*

> *Bash: Compare project copies with their own repos*

> *Bash: Check the project repos' history for the missing files*

Unused: 81 images, the old stylesheets, the gulp files, the empty `.htaccess`, `apgo.html` and the FutureSplash intro. The Flash intro is a judgement call. 11 more images are used only by `_fonts/extract.py`, to be moved into `_fonts/sources/`. Claude also suggested deleting the artworks in `_projects/` (except Cruisin', a single Word document with no repository), since each has its own e-2-org repo, after checking those repos had their files or history; error404's original pages are only in c-ship's history.

### User - 2026-10-14

I wanted to keep the projects folder as it was - these are the original projects which we have been working on in their own repos

### Claude

> *Bash: Trace when projects/ became _projects/*

`_projects/` is off the list. It was renamed from `projects/` in commit `2c2631b`, with the files unchanged; with the underscore Jekyll doesn't publish it, and the README still says `projects/`. Rename it back, or keep it as `_projects/`?

### User - 2026-10-14

Keep as _projects, update the README, remo0ve all the unused files, and move the stuff used to generate the font as suggested

### Claude

> *Bash: Move font source images into _fonts/sources*

> *Bash: Point extract.py at sources and test a rebuild*

> *Bash: Compare rebuilt font outlines with the committed font*

> *Bash: Remove unused images and old files*

> *Bash: Read README and front page comment*

> *Bash: Update front page comment and config excludes*

> *Bash: Check for a local node_modules folder*

> *Bash: Remove node_modules from gitignore*

> *Write: README.md*

> *Bash: Build and check all local references in the site*

> *Bash: Find where the built assets folder comes from*

> *Bash: Stage changes and summarise*

Removed: 81 images, the Flash and FutureSplash intros, `apgo.html`, the old stylesheets, the gulp setup and `.htaccess`. The font sources are in `_fonts/sources/`, and a rebuild from there gives identical outlines. The README describes the site as it now is, with `_projects/` kept for reference. All 252 local references in the built site work. `assets/css/style.css` in the built site comes from GitHub Pages' default theme and isn't used.

### User - 2026-10-14

Thanks - love it!

### Claude

The clean-up is staged, and isn't in today's session files yet.

### User - 2026-10-14

Please update the sessions and I'll commit them

### Claude

> *Edit: 2026-10-14-summary.md (clean-up, checks, status)*

> *Edit: 2026-10-14-transcript.md (this conversation since the last update)*
