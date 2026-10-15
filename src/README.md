# Sources

`index.html` at the repo root is generated. To change it:

1. edit `_head.html` (page shell + CSS), `body.html` (prose) or `_mock.css` / `gen.py` (the mock screens)
2. `python3 gen.py` — writes the `frag_*.html` mock fragments
3. `python3 build.py` — assembles `site.html`, then move it to `../index.html`

The mock screens are drawn at a fixed 1440px design width and scaled to fit by a
small script at the end of the page, so the layout never reflows.
