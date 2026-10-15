# Sources

`../index.html` is generated. To change it:

1. edit `_head.html` (page shell + CSS) or `body.html` (prose and figures)
2. `python3 build.py` — writes `../index.html`

Every figure is a real screenshot in `../images/`, captured against a locally
installed theme running on a throwaway database seeded with placeholder data
(`admin@example.co.jp` etc.). Nothing real appears in any image — the page is
served from a public repository.
