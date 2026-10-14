"""Build the c-ship lettering font from glyphs.json (and drawn.json) with fontTools."""
import json, sys
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.t2CharStringPen import T2CharStringPen

OUT = sys.argv[1]
glyphs = json.load(open(f'{OUT}/glyphs.json'))
try:
    glyphs.update(json.load(open(f'{OUT}/drawn.json')))
except FileNotFoundError:
    pass

ADV = 600
names = {' ': 'space', "'": 'quotesingle', '-': 'hyphen', '/': 'slash', '.': 'period', ',': 'comma',
         ':': 'colon', ';': 'semicolon', '!': 'exclam', '?': 'question', '&': 'ampersand',
         '(': 'parenleft', ')': 'parenright', '"': 'quotedbl', '@': 'at', '_': 'underscore',
         '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six',
         '7': 'seven', '8': 'eight', '9': 'nine', '’': 'quoteright', '‘': 'quoteleft',
         '–': 'endash', '—': 'emdash', '©': 'copyright'}


def gname(c):
    if c in names:
        return names[c]
    return c if c.islower() else c + '.unicase'


order = ['.notdef', 'space']
charstrings, cmap = {}, {}
pen = T2CharStringPen(ADV, None)
charstrings['.notdef'] = pen.getCharString()
pen = T2CharStringPen(ADV, None)
charstrings['space'] = pen.getCharString()
cmap[ord(' ')] = 'space'
cmap[0xa0] = 'space'

for c, g in sorted(glyphs.items()):
    n = gname(c)
    pen = T2CharStringPen(ADV, None)
    for contour in g['contours']:
        for op, pts in contour:
            pts = [(round(x), round(y)) for x, y in pts]
            if op == 'M':
                pen.moveTo(pts[0])
            elif op == 'L':
                pen.lineTo(pts[0])
            else:
                pen.curveTo(*pts)
        pen.closePath()
    charstrings[n] = pen.getCharString()
    order.append(n)
    cmap[ord(c)] = n

# unicase: each letter answers to both cases, unless it has its own capital
for c in list(glyphs):
    if c.isalpha() and c.islower() and c.upper() not in glyphs:
        cmap[ord(c.upper())] = gname(c)
    if c.isalpha() and c.isupper() and c.lower() not in glyphs:
        cmap[ord(c.lower())] = gname(c)
for a, b in (('’', "'"), ('‘', "'"), ('–', '-')):
    if a not in glyphs and b in glyphs:
        cmap[ord(a)] = gname(b)

fb = FontBuilder(1000, isTTF=False)
fb.setupGlyphOrder(order)
fb.setupCharacterMap(cmap)
fb.setupCFF('CShipLettering-Regular', {'FullName': 'C-Ship Lettering'}, charstrings, {})
fb.setupHorizontalMetrics({n: (ADV, charstrings[n].calcBounds(None)[0] if charstrings[n].calcBounds(None) else 0) for n in order})
fb.setupHorizontalHeader(ascent=850, descent=-250)
fb.setupNameTable({
    'familyName': 'C-Ship Lettering',
    'styleName': 'Regular',
    'copyright': 'Drawn from the container-ship (1998) lettering images, e-2',
})
fb.setupOS2(sTypoAscender=850, sTypoDescender=-250, sTypoLineGap=200, usWinAscent=900, usWinDescent=300,
            sxHeight=600, sCapHeight=830, achVendID='E2  ', fsType=0)
fb.setupPost(isFixedPitch=1)
fb.save(f'{OUT}/c-ship-lettering.otf')
fb.font.flavor = 'woff2'
fb.save(f'{OUT}/c-ship-lettering.woff2')
print(len(order), 'glyphs:', ''.join(sorted(chr(k) for k in cmap)))
