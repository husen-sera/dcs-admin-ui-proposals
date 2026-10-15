# -*- coding: utf-8 -*-
"""Emit the mock admin screens. One data set, four skins."""

ROWS = [
    ("2026/10/14 18:32:10", "admin@example.co.jp",   "Page view", "Project detail",        "/project-detail",        "/project-detail/601"),
    ("2026/10/14 18:31:44", "admin@example.co.jp",   "Action",    "Export project P&L",    "exportProject",          "—"),
    ("2026/10/14 18:28:03", "staff-a@example.co.jp", "Query",     "Contract list",         "allContractInstance",    "—"),
    ("2026/10/14 18:12:55", "staff-a@example.co.jp", "Page view", "Contract management",   "/contract-management",   "/contract-management"),
    ("2026/10/14 09:04:21", "staff-b@example.co.jp", "Login",     "Login",                 "login",                  "—"),
    ("2026/10/13 17:40:09", "admin@example.co.jp",   "Action",    "Export payslip",        "exportPaySlipStatement", "—"),
    ("2026/10/13 16:58:30", "admin@example.co.jp",   "Page view", "Royalty sales",         "/royalty",               "/royalty"),
]
PILL = {"Page view": "", "Action": "b", "Login": "g", "Query": ""}
HEAD = ["Timestamp (JST)", "User", "Type", "Label", "Key", "Path"]

NAV = [("Home", 0), ("Users", 0), ("Activity log — Detail", 1), ("Activity log — Summary", 0),
       ("Master data", 0), ("Royalty companies", 0), ("Guidelines", 0), ("Scheduled tasks", 0)]

CARDS = [("Total events", "18,432"), ("Active users", "19"), ("Sessions", "1,204"), ("Unused features", "47")]
BARS = [("Project list", 3210, 100), ("Contract management", 2884, 90), ("Project detail", 2106, 66),
        ("Royalty sales", 1455, 45), ("Payslips", 980, 31)]


def rows_html(skin, pill=True):
    out = []
    for d, u, t, c, k, p in ROWS:
        badge = ('<span class="m-pill %s">%s</span>' % (PILL[t], t)) if pill else t
        out.append(
            "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
            % (d, u, badge, c, k, p))
    return "".join(out)


def thead():
    return "<thead><tr>%s</tr></thead>" % "".join("<th>%s</th>" % h for h in HEAD)


def nav_html(skin, active="Activity log — Detail"):
    items = []
    for label, _ in NAV:
        items.append('<div class="m-nl%s"><i class="m-ico"></i>%s</div>'
                     % (" on" if label == active else "", label))
    return "".join(items)


def filters(skin):
    """The real sidebar: Type / User / Period (start+end) — our own DateRangeFilter."""
    sel = 'class="on"'
    g1 = ('<div class="g"><b>Type</b><a %s>All</a><a>Login</a><a>Page view</a>'
          '<a>Action</a><a>Query</a></div>' % sel)
    g2 = ('<div class="g"><b>User</b><a %s>All</a><a>admin@example.co.jp</a>'
          '<a>staff-a@example.co.jp</a></div>' % sel)
    btn = "m-btn" if skin in ("stock", "ai") else "m-b1"
    g3 = ('<div class="g"><b>Period (JST)</b>'
          '<span class="m-in">2026-10-01</span><span class="m-in">2026-10-14</span>'
          '<span class="%s">Apply</span></div>' % btn)
    return g1 + g2 + g3


# ----------------------------------------------------------------- list screens
def list_stock(skin="stock"):
    tools = ('<div class="m-tools"><a>View summary</a><a>Download CSV</a></div>')
    return """<div class="m-main">
<div class="m-top">Django administration</div>
<div class="m-crumb"><a>Home</a> › <a>Activity log</a> › Detail</div>
<div class="m-body">
<div class="m-hdrow"><h1 class="m-ttl">User activity log — Detail</h1>%s</div>
<div class="m-flex"><div class="m-grow"><table>%s<tbody>%s</tbody></table></div>
<div class="m-side"><h4>Filter</h4>%s</div></div>
</div></div>""" % (tools, thead(), rows_html("stock", pill=False), filters("stock"))


def list_ai():
    tools = ('<div class="m-tools"><a>View summary</a><a class="alt">Download CSV</a></div>')
    return """<div class="m-main">
<div class="m-top"><span class="lg">D</span><span class="n">DCS Administration</span>
<span class="r">admin@example.co.jp</span></div>
<div class="m-crumb"><a>Home</a> › <a>Activity log</a> › Detail</div>
<div class="m-body">
<div class="m-hdrow"><h1 class="m-ttl">User activity log — Detail</h1>%s</div>
<div class="m-flex"><div class="m-grow"><div class="m-card"><table>%s<tbody>%s</tbody></table></div></div>
<div class="m-side"><h4>Filter</h4>%s</div></div>
</div></div>""" % (tools, thead(), rows_html("ai"), filters("ai"))


def list_unfold():
    return """<div class="m-nav">
<div class="m-brand"><span class="lg">D</span>DCS Admin</div>%s</div>
<div class="m-main">
<div class="m-top"><div class="m-search">Search… ⌘K</div><div class="m-moon"></div><div class="m-av"></div></div>
<div class="m-body">
<div class="m-crumb">Home / Activity log / Detail</div>
<h1 class="m-ttl">User activity log — Detail</h1>
<div class="m-tools"><span class="m-b1">View summary</span><span class="m-b2">Download CSV</span></div>
<div class="m-flex"><div class="m-grow"><div class="m-card"><table>%s<tbody>%s</tbody></table></div></div>
<div class="m-side"><h4>Filter</h4>%s</div></div>
</div></div>""" % (nav_html("unfold"), thead(), rows_html("unfold"), filters("unfold"))


def list_jazz():
    return """<div class="m-nav">
<div class="m-brand"><span class="lg">D</span>DCS Admin</div>
<div class="m-user"><span class="av"></span><div>admin@example.co.jp</div></div>
<div class="m-grp">Menu</div>%s</div>
<div class="m-main">
<div class="m-top"><span class="t">Home</span><span class="t">View site</span><div class="m-av"></div></div>
<div class="m-crumbbar"><h1>User activity log — Detail</h1>
<div class="c"><a>Home</a> / <a>Activity log</a> / Detail</div></div>
<div class="m-body">
<div class="m-flex"><div class="m-grow"><div class="m-card">
<div class="m-ch"><h3>Detail — 18,432 records</h3><div>
<span class="m-b1">View summary</span> <span class="m-b2">Download CSV</span></div></div>
<table>%s<tbody>%s</tbody></table></div></div>
<div class="m-side"><div class="m-card"><h4>Filter</h4>%s</div></div></div>
</div></div>""" % (nav_html("jazz"), thead(), rows_html("jazz"), filters("jazz"))


# -------------------------------------------------------------- summary screens
def cards_html(skin):
    cls = "m-stat" if skin in ("unfold", "jazz", "ai") else "m-stat"
    return '<div class="m-cards">%s</div>' % "".join(
        '<div class="%s"><div class="m-k">%s</div><div class="m-v">%s</div></div>' % (cls, k, v)
        for k, v in CARDS)


def bars_html():
    return '<div class="m-bars">%s</div>' % "".join(
        '<div class="m-bl"><span>%s</span><span class="m-bt">'
        '<span class="m-bf" style="width:%d%%"></span></span><span class="m-bn">%s</span></div>'
        % (n, pct, "{:,}".format(c)) for n, c, pct in BARS)


def sum_unfold():
    return """<div class="m-nav">
<div class="m-brand"><span class="lg">D</span>DCS Admin</div>%s</div>
<div class="m-main">
<div class="m-top"><div class="m-search">Search… ⌘K</div><div class="m-moon"></div><div class="m-av"></div></div>
<div class="m-body">
<div class="m-crumb">Home / Activity log / Summary</div>
<h1 class="m-ttl">User activity log — Summary</h1>
<div class="m-tools"><span class="m-chipr on">Last 30 days</span><span class="m-chipr">Last 7 days</span>
<span class="m-chipr">Custom range</span></div>
%s
<div class="m-card" style="padding:17px 19px">
<div class="m-k" style="margin-bottom:11px">Most-viewed screens</div>%s</div>
</div></div>""" % (nav_html("unfold", "Activity log — Summary"), cards_html("unfold"), bars_html())


def sum_jazz():
    return """<div class="m-nav">
<div class="m-brand"><span class="lg">D</span>DCS Admin</div>
<div class="m-user"><span class="av"></span><div>admin@example.co.jp</div></div>
<div class="m-grp">Menu</div>%s</div>
<div class="m-main">
<div class="m-top"><span class="t">Home</span><span class="t">View site</span><div class="m-av"></div></div>
<div class="m-crumbbar"><h1>User activity log — Summary</h1>
<div class="c"><a>Home</a> / <a>Activity log</a> / Summary</div></div>
<div class="m-body">%s
<div class="m-card"><div class="m-ch"><h3>Most-viewed screens</h3><span class="m-b2">Last 30 days</span></div>
<div style="padding:15px 17px">%s</div></div>
</div></div>""" % (nav_html("jazz", "Activity log — Summary"), cards_html("jazz"), bars_html())


def sum_stock(skin="stock"):
    return """<div class="m-main">
<div class="m-top">Django administration</div>
<div class="m-crumb"><a>Home</a> › <a>Activity log</a> › Summary</div>
<div class="m-body">
<h1 class="m-ttl">User activity log — Summary</h1>
<div style="margin:14px 0 16px;font-size:11.5px;color:#666">
Period <span class="m-in" style="display:inline-block;width:110px">2026-09-15</span>
〜 <span class="m-in" style="display:inline-block;width:110px">2026-10-14</span>
<span class="m-btn">Show</span></div>
%s
<div style="border:1px solid #eee;padding:14px 16px">
<div class="m-k" style="margin-bottom:11px">Most-viewed screens</div>%s</div>
</div></div>""" % (cards_html("stock"), bars_html())


def sum_ai():
    return """<div class="m-main">
<div class="m-top"><span class="lg">D</span><span class="n">DCS Administration</span>
<span class="r">admin@example.co.jp</span></div>
<div class="m-crumb"><a>Home</a> › <a>Activity log</a> › Summary</div>
<div class="m-body">
<h1 class="m-ttl">User activity log — Summary</h1>
<div style="margin:14px 0 16px;font-size:11.5px;color:#5a6276">
Period <span class="m-in" style="display:inline-block;width:110px">2026-09-15</span>
〜 <span class="m-in" style="display:inline-block;width:110px">2026-10-14</span>
<span class="m-btn">Show</span></div>
%s
<div class="m-card" style="padding:14px 16px">
<div class="m-k" style="margin-bottom:11px">Most-viewed screens</div>%s</div>
</div></div>""" % (cards_html("ai"), bars_html())


def shot(skin, inner, url, cap, kind="list"):
    return """<div class="shot"><div class="bar"><i></i><i></i><i></i>
<div class="url">%s</div></div>
<div class="vp h-%s"><div class="inner sk-%s"><div class="m-row">%s</div></div></div></div>
<p class="cap">%s</p>""" % (url, "sum" if kind == "sum" else "list", skin, inner, cap)


LIST_URL = "dcs.example.com/admin/activitylog/activityevent/"
SUM_URL = "dcs.example.com/admin/activitylog/activityevent/summary/"

OUT = {
    "stock_list": shot("stock", list_stock(), LIST_URL,
                       "<b>Today</b> — stock Django 4.2. The filter rail on the right and the two "
                       "links at the top (View summary / Download CSV) are what ships now."),
    "stock_sum": shot("stock", sum_stock(), SUM_URL,
                      "<b>Today</b> — the summary page. The bar chart is pure CSS "
                      "(<code>widthratio</code>); there is not one line of JavaScript on it.", "sum"),
    "unfold_list": shot("unfold", list_unfold(), LIST_URL,
                        "<b>Option A / django-unfold</b> — left sidebar, \u2318K command palette, "
                        "dark-mode toggle. The filter names and behaviour stay exactly as they are."),
    "unfold_sum": shot("unfold", sum_unfold(), SUM_URL,
                       "<b>Option A / django-unfold</b> — the summary page. The stat cards and tables "
                       "can be rebuilt from unfold's own components.", "sum"),
    "jazz_list": shot("jazz", list_jazz(), LIST_URL,
                      "<b>Option B / django-jazzmin</b> — AdminLTE 3 / Bootstrap 5, with a record "
                      "count in the card header and a dark navy sidebar."),
    "jazz_sum": shot("jazz", sum_jazz(), SUM_URL,
                     "<b>Option B / django-jazzmin</b> — the summary page, inside a Bootstrap card.", "sum"),
    "ai_list": shot("ai", list_ai(), LIST_URL,
                    "<b>Option C / django-admin-interface</b> — Django's structure is untouched; only "
                    "the colours and the logo change. The smallest migration of the three."),
    "ai_sum": shot("ai", sum_ai(), SUM_URL,
                   "<b>Option C / django-admin-interface</b> — the summary page. The layout is "
                   "identical to today's.", "sum"),
}

import io
for k, v in OUT.items():
    with io.open("frag_%s.html" % k, "w", encoding="utf-8") as fh:
        fh.write(v)
print("wrote %d fragments" % len(OUT))
