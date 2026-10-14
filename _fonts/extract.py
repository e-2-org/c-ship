"""Cut the letters out of the c-ship lettering images and trace them.

Writes glyphs.json: {char: {"contours": [...], "source": ...}} in font units
(advance 600, baseline 0), and a preview of each source's segmentation.
"""
import json, sys
import numpy as np
from PIL import Image
import potrace

REPO = sys.argv[1]
OUT = sys.argv[2]
ADV = 600
UP = 8  # upscale before tracing

# (image, text as drawn, first text column) -- master size first
SOURCES = [
    ('namege', 'geraint evans', 0, 250),
    ('namesf', 'simon faithfull', 0, 250),
    ('namesc', 'susan collins', 0, 250),
    ('namedl', 'David lilley', 0, 250),
    ('namego', 'gill ord', 0, 250),
    ('namebl', 'brigHid lowe', 0, 250),
    # fill-ins from smaller lettering
    ('ac404', 'error 404', 0, 999),
    ('accru', "cruisin'", 0, 999),
    ('acnow', 'now here/nowhere', 0, 999),
    ('tback', 'back to artists and index', 28, 999),
    ('tabout', 'about c-ship', 25, 999),
]


def intensity(path):
    im = Image.open(path).convert('RGB')
    a = np.asarray(im).astype(float)
    h, w, _ = a.shape
    bg = a[h - 1, w - 1]
    d = np.abs(a - bg).sum(axis=2)
    # ink colour: the most common colour far from the background
    far = d > d.max() * 0.8
    ink = np.median(a[far], axis=0)
    return np.clip(d / np.abs(ink - bg).sum(), 0, 1)


def segments(I, x0, thr=0.15):
    cols = I[:, x0:].max(axis=0) > thr
    runs, start = [], None
    for x, on in enumerate(list(cols) + [False]):
        if on and start is None:
            start = x
        elif not on and start is not None:
            runs.append((start + x0, x + x0))
            start = None
    return runs


def trace(I, x0, x1, y0, y1):
    crop = Image.fromarray((I[y0:y1, x0:x1] * 255).astype(np.uint8))
    big = crop.resize((crop.width * UP, crop.height * UP), Image.BICUBIC)
    bm = potrace.Bitmap(np.asarray(big) <= 127)
    plist = bm.trace(turdsize=4 * UP, alphamax=0.9, opticurve=True, opttolerance=0.2)
    out = []
    for curve in plist:
        pts = [('M', [curve.start_point])]
        for seg in curve.segments:
            if seg.is_corner:
                pts.append(('L', [seg.c]))
                pts.append(('L', [seg.end_point]))
            else:
                pts.append(('C', [seg.c1, seg.c2, seg.end_point]))
        out.append(pts)
    return out


glyphs = {}
report = []
for name, text, x0, x1 in SOURCES:
    I = intensity(f'{REPO}/images/{name}.gif')
    runs = segments(I[:, :x1], x0)
    chars = [(k, c) for k, c in enumerate(text) if c != ' ']
    if len(runs) != len(chars):
        report.append(f'{name}: {len(runs)} runs for {len(chars)} letters {runs}')
        continue
    # monospaced: fit centre = origin + adv * k
    ks = np.array([k for k, _ in chars], float)
    cs = np.array([(a + b) / 2 for a, b in runs])
    adv, origin = np.polyfit(ks, cs, 1)
    # baseline: the bottom of the x-height letters
    bottoms = []
    for (k, c), (a, b) in zip(chars, runs):
        if c in 'acemnorsuvwxz':
            rows = np.where(I[:, a:b].max(axis=1) > 0.5)[0]
            bottoms.append(rows.max() + 1)
    base = float(np.median(bottoms))
    U = ADV / adv
    report.append(f'{name}: adv {adv:.2f}px baseline {base}')
    h = I.shape[0]
    for (k, c), (a, b) in zip(chars, runs):
        if c in glyphs:
            continue
        cell = origin + adv * k - adv / 2
        ca, cb = max(a - 2, 0), min(b + 2, I.shape[1])
        contours = []
        for path in trace(I, ca, cb, 0, h):
            contours.append([(op, [((p.x / UP + ca - cell) * U, (base - p.y / UP) * U) for p in ps]) for op, ps in path])
        glyphs[c] = {'contours': contours, 'source': name, 'px': round(adv, 2)}

json.dump(glyphs, open(f'{OUT}/glyphs.json', 'w'))
print('\n'.join(report))
print('glyphs:', ''.join(sorted(glyphs)))
