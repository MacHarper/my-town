"""Embed the Community Cafe rooms (front room, kitchen, packing room; Mac's pictures as they are, colors unchanged) and their outline glows in index.html (between CAFE_ROOMS start/end).
python3 community-cafe/tools/cafe_rooms.py"""
import base64, io, json, re
from PIL import Image, ImageDraw, ImageFilter, ImageChops

def glow(draw_shape, box):
    """the room glow, the same as the salon chair's (style-guide.md Highlights): a thin soft #fff6b0 line about 6 wide,
    just outside the thing's outline, and a faint fill over the thing. Sized like the spot plus 16 on each side."""
    x, y, w, h = box
    m = Image.new('L', (w + 32, h + 32), 0); draw_shape(ImageDraw.Draw(m), 16 - x, 16 - y)
    inner = m.filter(ImageFilter.MaxFilter(11)); outer = m.filter(ImageFilter.MaxFilter(23))
    ring = ImageChops.subtract(outer, inner).filter(ImageFilter.GaussianBlur(1.3)).point(lambda v: round(v * .82))
    fill = inner.point(lambda v: 63 if v > 128 else 0)
    a = ImageChops.lighter(ring, fill)
    im = Image.new('RGBA', m.size, (255, 246, 176, 0)); im.putalpha(a)
    b = io.BytesIO(); im.save(b, 'WEBP', lossless=True); return 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode()

def counter(d, ox, oy):   # cream top slab plus the dark wood base (same table in both rooms)
    d.rounded_rectangle([640 + ox, 622 + oy, 1366 + ox, 734 + oy], 40, fill=255)
    d.rounded_rectangle([660 + ox, 700 + oy, 1326 + ox, 942 + oy], 26, fill=255)
def door(x0, y0, x1, y1):
    def shape(d, ox, oy):   # the door frame, minus the table that stands in front of it
        d.rounded_rectangle([x0 + ox, y0 + oy, x1 + ox, y1 + oy], 10, fill=255)
        d.rounded_rectangle([640 + ox - 14, 622 + oy - 14, 1366 + ox + 14, 734 + oy], 40, fill=0)
        d.rectangle([660 + ox - 14, 700 + oy, 1326 + ox + 14, 942 + oy], fill=0)
    return shape

def jpg(path):
    return 'data:image/jpeg;base64,' + base64.b64encode(open(path, 'rb').read()).decode()

def logo():   # the cafe icon (community-cafe/art/cafe-logo.png: Mac's cup, dark brown softened to the cafe's dark wood)
    im = Image.open('community-cafe/art/cafe-logo.png'); im.thumbnail((240, 240))
    b = io.BytesIO(); im.save(b, 'WEBP', quality=92); return 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode()

TABLE = (630, 610, 746, 344)
out = {
  'frontDoor': glow(lambda d, ox, oy: d.rounded_rectangle([1520 + ox, 208 + oy, 1945 + ox, 900 + oy], 12, fill=255), (1518, 206, 430, 696)),
}
def small(path, w):   # a small picture for the career card buttons
    im = Image.open(path); im.thumbnail((w, w)); b = io.BytesIO(); im.save(b, 'WEBP', quality=90); return 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode()
PICS = {'bake': small('community-cafe/art/items/muffin-tin-baked.png', 240), 'pack': small('community-cafe/art/items/box-closed.png', 220), 'eat': small('community-cafe/art/eat-plate.png', 240)}
block = ('// CAFE_ROOMS start (made by community-cafe/tools/cafe_rooms.py)\n'
         f"const CAFE_GLOW = {json.dumps(out)};\n"
         f"const CAFE_LOGO = '{logo()}';\n"
         f"const CHEF_DOLL = 'data:image/webp;base64,{base64.b64encode(open('community-cafe/art/chef-doll.webp', 'rb').read()).decode()}';\n"
         f"const CAFE_PICS = {json.dumps(PICS)};\n"
         f"const CAFE_FRONT = '{jpg('images/cafe-front-room.jpg')}';\n"
         f"const CAFE_KITCHEN = '{jpg('images/cafe-kitchen-room.jpg')}';\n"
         '// CAFE_ROOMS end\n')
t = open('index.html').read()
if '// CAFE_ROOMS start' in t:
    t = re.sub(r'// CAFE_ROOMS start.*?// CAFE_ROOMS end\n', lambda m: block, t, flags=re.S)
else:
    t = t.replace('const ROOMS = {', block + 'const ROOMS = {', 1)
open('index.html', 'w').write(t); print('cafe rooms embedded,', len(block) // 1024, 'KB')
