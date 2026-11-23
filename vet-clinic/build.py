"""Rebuild vet-clinic/vet-clinic.html from the game starter, the game's code (vet-clinic/game-parts.txt) and its pictures.
python3 vet-clinic/build.py   (run from the My Game folder). The parts file has @@CSS@@, @@HEADER@@, @@HTML@@ and @@JS@@ sections."""
import base64, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
T = "tools/"
page = open(T + "game-starter.html").read()
toolbar = open(T + "toolbar.html").read().replace('data-root="ROOT_HERE"', 'data-root="../"')
loading = open(T + "loading.html").read().replace('Getting ready...', 'Getting the pets ready...')
for k, v in {'TITLE': 'Vet Clinic', 'BUILDING': 'vet', 'BUILDING_NAME': 'Vet Clinic', 'COLOR': '#3bb273', 'SAVEKEY': 'vetClinic',
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
ART = {"room": ("images/vet-room.jpg", "image/jpeg"), "dachshundSit": (A + "dachshund-sit.webp", "image/webp"),
       "ralphieEat": (A + "ralphie-eat.webp", "image/webp"), "ralphieBath": (A + "ralphie-bath.webp", "image/webp"),
       "ralphieDone": (A + "ralphie-done.webp", "image/webp"), "cup": (A + "cup.webp", "image/webp"),
       "bowlFood": (A + "bowl-food.webp", "image/webp"), "bowlWater": (A + "bowl-water.webp", "image/webp"),
       "soap": (A + "soap.webp", "image/webp"), "towel": (A + "towel.webp", "image/webp"), "brush": (A + "brush.webp", "image/webp")}
page = page.replace("const ART = {};", "const ART = {\n" + "".join("  %s: '%s',\n" % (k, d(*v)) for k, v in ART.items()) + "};", 1)
page = page.replace("// ---------- The game ----------\n", "// ---------- The game ----------\n" + js, 1)
open("vet-clinic/vet-clinic.html", "w").write(page); print("vet-clinic.html", len(page) // 1024, "KB")
