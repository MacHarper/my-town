"""Rebuild vet-clinic/vet-clinic.html from the game starter, the game's code (vet-clinic/game-parts.txt) and its pictures.
python3 vet-clinic/build.py   (run from the My Game folder). The parts file has @@CSS@@, @@HEADER@@, @@HTML@@ and @@JS@@ sections."""
import base64, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
T = "tools/"
page = open(T + "game-starter.html").read()
toolbar = open(T + "toolbar.html").read().replace('data-root="ROOT_HERE"', 'data-root="../"')
loading = open(T + "loading.html").read().replace('Getting ready...', 'Getting the pets ready...')
for k, v in {'TITLE': 'Vet Clinic', 'BUILDING': 'vet', 'BUILDING_NAME': 'Vet Clinic', 'COLOR': '#5fae7a', 'SAVEKEY': 'vetClinic',
             'LOADING': loading, 'TOOLBAR': toolbar}.items():
    page = page.replace('{{%s}}' % k, v)
parts = open("vet-clinic/game-parts.txt").read()
g = lambda a, b: parts.split(a)[1].split(b)[0]
css, hdr, html, js = g("@@CSS@@", "@@HEADER@@"), g("@@HEADER@@", "@@HTML@@"), g("@@HTML@@", "@@JS@@"), parts.split("@@JS@@")[1]
page = page.replace("</style>", css + "</style>", 1)
i = page.index("<h2>Vet Clinic</h2>") + len("<h2>Vet Clinic</h2>"); page = page[:i] + "\n" + hdr.rstrip("\n") + page[i:]
a = page.index('  <div class="play" id="play">'); b = page.index("</div>", a) + 6; page = page[:a] + html.strip("\n") + page[b:]
d = lambda f, m: "data:%s;base64,%s" % (m, base64.b64encode(open(f, "rb").read()).decode())
A = "vet-clinic/art/"
ART = {"room": ("images/vet-room.jpg", "image/jpeg"), "dachshundSit": (A + "pets/ralphie-sit.webp", "image/webp"),
       "ralphieEat": (A + "pets/ralphie-eat.webp", "image/webp"), "ralphieBath": (A + "pets/ralphie-bath.webp", "image/webp"),
       "ralphieDone": (A + "pets/ralphie-done.webp", "image/webp"), "cup": (A + "cup.webp", "image/webp"),
       "bowlFood": (A + "bowl-food.webp", "image/webp"), "bowlWater": (A + "bowl-water.webp", "image/webp"),
       "soap": (A + "soap.webp", "image/webp"), "towel": (A + "towel.webp", "image/webp"), "brush": (A + "brush.webp", "image/webp"),
       "bellaSit": (A + "pets/bella-sit.webp", "image/webp"), "bellaEat": (A + "pets/bella-eat.webp", "image/webp"),
       "bellaBath": (A + "pets/bella-bath.webp", "image/webp"), "bellaDone": (A + "pets/bella-done.webp", "image/webp"),
       "vetLogo": (A + "vet-logo.webp", "image/webp"), "zuzuSit": (A + "pets/zuzu-sit.webp", "image/webp"), "zuzuEat": (A + "pets/zuzu-eat.webp", "image/webp"),
       "zuzuBath": (A + "pets/zuzu-bath.webp", "image/webp"), "zuzuDone": (A + "pets/zuzu-done.webp", "image/webp"),
       "spudSit": (A + "pets/spud-sit.webp", "image/webp"), "spudEat": (A + "pets/spud-eat.webp", "image/webp"),
       "spudBath": (A + "pets/spud-bath.webp", "image/webp"), "spudDone": (A + "pets/spud-done.webp", "image/webp"),
       "millySit": (A + "pets/milly-sit.webp", "image/webp"), "millyEat": (A + "pets/milly-eat.webp", "image/webp"),
       "millyBath": (A + "pets/milly-bath.webp", "image/webp"), "millyDone": (A + "pets/milly-done.webp", "image/webp"),
       "suzySit": (A + "pets/suzy-sit.webp", "image/webp"), "suzyEat": (A + "pets/suzy-eat.webp", "image/webp"),
       "suzyBath": (A + "pets/suzy-bath.webp", "image/webp"), "suzyDone": (A + "pets/suzy-done.webp", "image/webp"),
       "lunaSit": (A + "pets/luna-sit.webp", "image/webp"), "lunaEat": (A + "pets/luna-eat.webp", "image/webp"),
       "lunaGroom": (A + "pets/luna-groom.webp", "image/webp"), "lunaPlay": (A + "pets/luna-play.webp", "image/webp"),
       "lunaDone": (A + "pets/luna-done.webp", "image/webp"), "lunaSleep": (A + "pets/luna-sleep.webp", "image/webp")}
# every pet pose (sit, bath, done) is measured across its paws, so the game can draw each pose the same size as sitting
from PIL import Image
def paws(f):
    a = Image.open(f).convert("RGBA").split()[3]; W, H = a.size
    b = a.crop((0, int(H * .94), W, H)).point(lambda v: 255 if v > 128 else 0).getbbox()
    return [b[2] - b[0], (b[0] + b[2]) / 2] + collar(f)
def collar(f):   # the middle of the collar band: the widest row of a color that is not fur (blue, purple, green, coral...)
    import colorsys
    im = Image.open(f).convert("RGBA"); W, H = im.size; px = im.load(); rows = {}
    for y in range(int(H * .6)):
        n = xs = 0
        for x in range(0, W, 2):
            r, g, bb, a = px[x, y]
            if a < 200: continue
            h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, bb / 255)
            if s > .35 and v > .3 and (90 < h * 360 < 352 or (h * 360 < 15 and s > .55 and v > .8)): n += 1; xs += x   # (red and coral collars too)
        if n: rows[y] = (n, xs / n)
    if not rows: return [W / 2, H * .45]
    m = max(v[0] for v in rows.values()); ys = [y for y, v in rows.items() if v[0] > .5 * m]
    return [round(sum(rows[y][1] for y in ys) / len(ys)), round(sum(ys) / len(ys))]
PAW = {k: paws(f) for k, (f, m) in ART.items() if "/pets/" in f and not f.endswith(("-eat.webp", "-sleep.webp"))}
for k, v in PAW.items(): print("  paws", k, v[0], "collar", v[2], v[3])
page = page.replace("const ART = {};", "const ART = {\n" + "".join("  %s: '%s',\n" % (k, d(*v)) for k, v in ART.items()) + "};", 1)
page = page.replace("// ---------- The game ----------\n", "// ---------- The game ----------\n" + js, 1)
page = page.replace("const PAWS = {};", "const PAWS = " + str(PAW).replace("'", '"') + ";", 1)
open("vet-clinic/vet-clinic.html", "w").write(page); print("vet-clinic.html", len(page) // 1024, "KB")
