# C-Ship Lettering

The font in `fonts/c-ship-lettering.woff2`, made from the 1998 lettering images
so the titles and menus can be text.

- `extract.py` cuts the letters out of the lettering images (the artists' names,
  at 13px a letter, and a few from the smaller titles and menus), smooths them
  and traces them into outlines.
- `drawn.py` has the letters which never appear in the images (j, q, z, the
  figures and punctuation, and p, k and x, which only appear small), drawn on the
  same pixel grid as the names, then traced the same way.
- `build.py` makes the font (OpenType CFF and WOFF2) with fontTools.

It's unicase, as the original was: capitals and small letters share a glyph,
except D and H, which have their own x-height forms. The figures are old-style.

To rebuild (Python 3 with pillow, numpy, potracer, fonttools and brotli):

    python _fonts/extract.py . /tmp/font
    python _fonts/drawn.py /tmp/font
    python _fonts/build.py /tmp/font
    cp /tmp/font/c-ship-lettering.woff2 fonts/
