# -*- coding: utf-8 -*-
"""Assemble index.html from the page shell and the body.

The mock-screen generator (gen.py / _mock.css) is gone: every figure on the
page is now a real screenshot in ../images/, captured against a locally
installed theme on a seeded throwaway database.
"""
import io
import re


def rd(p):
    with io.open(p, encoding="utf-8") as fh:
        return fh.read()


head = rd("_head.html")
body = rd("body.html")

out = head + body
left = re.findall(r"__[A-Z_]+__", out)
assert not left, left

# Fold the dark-mode block into its conventional form (nested @media inside a
# rule is CSS nesting; this keeps it working in older engines too).
old = ':root:not([data-theme="light"]){ @media (prefers-color-scheme: dark){'
if old in out:
    i = out.index(old)
    j = out.index(':root[data-theme="dark"]{', i)
    inner = out[i:j][len(old):].rstrip()[:-2].strip()
    out = (out[:i]
           + '@media (prefers-color-scheme: dark){\n:root:not([data-theme="light"]){\n'
           + inner + '\n}}\n'
           + out[j:])

with io.open("../index.html", "w", encoding="utf-8") as fh:
    fh.write(out)
print("built ../index.html: %d bytes" % len(out.encode("utf-8")))
