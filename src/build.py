# -*- coding: utf-8 -*-
import io, re

def rd(p):
    with io.open(p, encoding="utf-8") as fh:
        return fh.read()

head = rd("_head.html")         # page shell: <!doctype> ... <div class="wrap">
mock = rd("_mock.css")
body = rd("body.html")

# fold the mock stylesheet into the existing <style> block
assert "</style>" in head
head = head.replace("</style>", "\n/* ==== mock screens ==== */\n" + mock + "\n</style>", 1)

for key, frag in [
    ("__STOCK_LIST__",  "frag_stock_list.html"),
    ("__STOCK_SUM__",   "frag_stock_sum.html"),
    ("__UNFOLD_LIST__", "frag_unfold_list.html"),
    ("__UNFOLD_SUM__",  "frag_unfold_sum.html"),
    ("__JAZZ_LIST__",   "frag_jazz_list.html"),
    ("__JAZZ_SUM__",    "frag_jazz_sum.html"),
    ("__AI_LIST__",     "frag_ai_list.html"),
    ("__AI_SUM__",      "frag_ai_sum.html"),
]:
    assert key in body, key
    body = body.replace(key, rd(frag))

out = head + body
left = re.findall(r"__[A-Z_]+__", out)
assert not left, left
with io.open("site.html", "w", encoding="utf-8") as fh:
    fh.write(out)
print("built site.html: %d bytes, %d lines" % (len(out.encode("utf-8")), out.count("\n")))
