#!/usr/bin/env python3
"""Usage:  python apply-intro.py index.html
Puts the intro + admin animations into your page (safe to run again; it replaces its own earlier insert)."""
import re, sys, os
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, "intro-animations.html"), encoding="utf-8").read()
def blk(n):
    a = src.index("<!-- ============================ BLOCK %d of 2" % n)
    a = src.index("-->", a) + 3
    b = src.index("<!-- ========================== END BLOCK %d of 2" % n)
    return src[a:b].strip()
page_path = sys.argv[1]
page = open(page_path, encoding="utf-8").read()
page = re.sub(r"<!--ADV-INTRO-1-->.*?<!--/ADV-INTRO-1-->\s*", "", page, flags=re.S)
page = re.sub(r"<!--ADV-INTRO-2-->.*?<!--/ADV-INTRO-2-->\s*", "", page, flags=re.S)
m = re.search(r"<body[^>]*>", page)
if not m: sys.exit("No <body> tag found")
page = page[:m.end()] + "\n<!--ADV-INTRO-1-->\n" + blk(1) + "\n<!--/ADV-INTRO-1-->\n" + page[m.end():]
i = page.rindex("</body>")
page = page[:i] + "<!--ADV-INTRO-2-->\n" + blk(2) + "\n<!--/ADV-INTRO-2-->\n" + page[i:]
open(page_path, "w", encoding="utf-8").write(page)
print("Done. Animations added to", page_path)
