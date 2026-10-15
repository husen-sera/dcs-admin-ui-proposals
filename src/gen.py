# -*- coding: utf-8 -*-
"""Emit the mock admin screens. One data set, four skins."""

ROWS = [
    ("2026/10/14 18:32:10", "admin@example.co.jp",   "画面閲覧", "プロジェクト詳細",         "/project-detail",         "/project-detail/601"),
    ("2026/10/14 18:31:44", "admin@example.co.jp",   "操作",     "プロジェクト収支データ出力", "exportProject",           "—"),
    ("2026/10/14 18:28:03", "staff-a@example.co.jp", "参照",     "契約書一覧",               "allContractInstance",     "—"),
    ("2026/10/14 18:12:55", "staff-a@example.co.jp", "画面閲覧", "契約書管理",               "/contract-management",    "/contract-management"),
    ("2026/10/14 09:04:21", "staff-b@example.co.jp",  "ログイン", "ログイン",                 "login",                   "—"),
    ("2026/10/13 17:40:09", "admin@example.co.jp",   "操作",     "支払明細書出力",            "exportPaySlipStatement",  "—"),
    ("2026/10/13 16:58:30", "admin@example.co.jp",   "画面閲覧", "ロイヤリティ売上管理",      "/royalty",                "/royalty"),
]
PILL = {"画面閲覧": "", "操作": "b", "ログイン": "g", "参照": ""}
HEAD = ["日時 (JST)", "ユーザー", "種別", "内容", "キー", "パス"]

NAV = [("ホーム", 0), ("ユーザー", 0), ("活動ログ 明細", 1), ("活動ログ 集計", 0),
       ("マスタデータ", 0), ("ロイヤリティ会社", 0), ("ガイドライン", 0), ("定期実行タスク", 0)]

CARDS = [("総イベント数", "18,432"), ("利用ユーザー", "19"), ("セッション", "1,204"), ("未使用の機能", "47")]
BARS = [("プロジェクト一覧", 3210, 100), ("契約書管理", 2884, 90), ("プロジェクト詳細", 2106, 66),
        ("ロイヤリティ売上管理", 1455, 45), ("支払明細", 980, 31)]


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


def nav_html(skin, active="活動ログ 明細"):
    items = []
    for label, _ in NAV:
        items.append('<div class="m-nl%s"><i class="m-ico"></i>%s</div>'
                     % (" on" if label == active else "", label))
    return "".join(items)


def filters(skin):
    """The real sidebar: 種別 / ユーザー / 期間 (start+end) — our own DateRangeFilter."""
    sel = 'class="on"'
    g1 = ('<div class="g"><b>種別</b><a %s>すべて</a><a>ログイン</a><a>画面閲覧</a>'
          '<a>操作</a><a>参照</a></div>' % sel)
    g2 = ('<div class="g"><b>ユーザー</b><a %s>すべて</a><a>admin@example.co.jp</a>'
          '<a>staff-a@example.co.jp</a></div>' % sel)
    btn = "m-btn" if skin in ("stock", "ai") else "m-b1"
    g3 = ('<div class="g"><b>期間 (JST)</b>'
          '<span class="m-in">2026-10-01</span><span class="m-in">2026-10-14</span>'
          '<span class="%s">絞り込む</span></div>' % btn)
    return g1 + g2 + g3


# ----------------------------------------------------------------- list screens
def list_stock(skin="stock"):
    tools = ('<div class="m-tools"><a>集計を見る</a><a>CSVダウンロード</a></div>')
    return """<div class="m-main">
<div class="m-top">Django 管理サイト</div>
<div class="m-crumb"><a>ホーム</a> › <a>活動ログ</a> › ユーザー活動ログ 明細</div>
<div class="m-body">
<div class="m-hdrow"><h1 class="m-ttl">ユーザー活動ログ 明細</h1>%s</div>
<div class="m-flex"><div class="m-grow"><table>%s<tbody>%s</tbody></table></div>
<div class="m-side"><h4>絞り込み</h4>%s</div></div>
</div></div>""" % (tools, thead(), rows_html("stock", pill=False), filters("stock"))


def list_ai():
    tools = ('<div class="m-tools"><a>集計を見る</a><a class="alt">CSVダウンロード</a></div>')
    return """<div class="m-main">
<div class="m-top"><span class="lg">D</span><span class="n">DCS 管理サイト</span>
<span class="r">admin@example.co.jp</span></div>
<div class="m-crumb"><a>ホーム</a> › <a>活動ログ</a> › ユーザー活動ログ 明細</div>
<div class="m-body">
<div class="m-hdrow"><h1 class="m-ttl">ユーザー活動ログ 明細</h1>%s</div>
<div class="m-flex"><div class="m-grow"><div class="m-card"><table>%s<tbody>%s</tbody></table></div></div>
<div class="m-side"><h4>絞り込み</h4>%s</div></div>
</div></div>""" % (tools, thead(), rows_html("ai"), filters("ai"))


def list_unfold():
    return """<div class="m-nav">
<div class="m-brand"><span class="lg">D</span>DCS 管理</div>%s</div>
<div class="m-main">
<div class="m-top"><div class="m-search">検索… ⌘K</div><div class="m-moon"></div><div class="m-av"></div></div>
<div class="m-body">
<div class="m-crumb">ホーム / 活動ログ / 明細</div>
<h1 class="m-ttl">ユーザー活動ログ 明細</h1>
<div class="m-tools"><span class="m-b1">集計を見る</span><span class="m-b2">CSVダウンロード</span></div>
<div class="m-flex"><div class="m-grow"><div class="m-card"><table>%s<tbody>%s</tbody></table></div></div>
<div class="m-side"><h4>絞り込み</h4>%s</div></div>
</div></div>""" % (nav_html("unfold"), thead(), rows_html("unfold"), filters("unfold"))


def list_jazz():
    return """<div class="m-nav">
<div class="m-brand"><span class="lg">D</span>DCS 管理</div>
<div class="m-user"><span class="av"></span><div>admin@example.co.jp</div></div>
<div class="m-grp">メニュー</div>%s</div>
<div class="m-main">
<div class="m-top"><span class="t">ホーム</span><span class="t">サイトを表示</span><div class="m-av"></div></div>
<div class="m-crumbbar"><h1>ユーザー活動ログ 明細</h1>
<div class="c"><a>ホーム</a> / <a>活動ログ</a> / 明細</div></div>
<div class="m-body">
<div class="m-flex"><div class="m-grow"><div class="m-card">
<div class="m-ch"><h3>明細 — 全 18,432 件</h3><div>
<span class="m-b1">集計を見る</span> <span class="m-b2">CSVダウンロード</span></div></div>
<table>%s<tbody>%s</tbody></table></div></div>
<div class="m-side"><div class="m-card"><h4>絞り込み</h4>%s</div></div></div>
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
<div class="m-brand"><span class="lg">D</span>DCS 管理</div>%s</div>
<div class="m-main">
<div class="m-top"><div class="m-search">検索… ⌘K</div><div class="m-moon"></div><div class="m-av"></div></div>
<div class="m-body">
<div class="m-crumb">ホーム / 活動ログ / 集計</div>
<h1 class="m-ttl">ユーザー活動ログ 集計</h1>
<div class="m-tools"><span class="m-chipr on">過去30日</span><span class="m-chipr">過去7日</span>
<span class="m-chipr">期間を指定</span></div>
%s
<div class="m-card" style="padding:17px 19px">
<div class="m-k" style="margin-bottom:11px">よく見られる画面</div>%s</div>
</div></div>""" % (nav_html("unfold", "活動ログ 集計"), cards_html("unfold"), bars_html())


def sum_jazz():
    return """<div class="m-nav">
<div class="m-brand"><span class="lg">D</span>DCS 管理</div>
<div class="m-user"><span class="av"></span><div>admin@example.co.jp</div></div>
<div class="m-grp">メニュー</div>%s</div>
<div class="m-main">
<div class="m-top"><span class="t">ホーム</span><span class="t">サイトを表示</span><div class="m-av"></div></div>
<div class="m-crumbbar"><h1>ユーザー活動ログ 集計</h1>
<div class="c"><a>ホーム</a> / <a>活動ログ</a> / 集計</div></div>
<div class="m-body">%s
<div class="m-card"><div class="m-ch"><h3>よく見られる画面</h3><span class="m-b2">過去30日</span></div>
<div style="padding:15px 17px">%s</div></div>
</div></div>""" % (nav_html("jazz", "活動ログ 集計"), cards_html("jazz"), bars_html())


def sum_stock(skin="stock"):
    return """<div class="m-main">
<div class="m-top">Django 管理サイト</div>
<div class="m-crumb"><a>ホーム</a> › <a>活動ログ</a> › ユーザー活動ログ 集計</div>
<div class="m-body">
<h1 class="m-ttl">ユーザー活動ログ 集計</h1>
<div style="margin:14px 0 16px;font-size:11.5px;color:#666">
期間 <span class="m-in" style="display:inline-block;width:110px">2026-09-15</span>
〜 <span class="m-in" style="display:inline-block;width:110px">2026-10-14</span>
<span class="m-btn">表示</span></div>
%s
<div style="border:1px solid #eee;padding:14px 16px">
<div class="m-k" style="margin-bottom:11px">よく見られる画面</div>%s</div>
</div></div>""" % (cards_html("stock"), bars_html())


def sum_ai():
    return """<div class="m-main">
<div class="m-top"><span class="lg">D</span><span class="n">DCS 管理サイト</span>
<span class="r">admin@example.co.jp</span></div>
<div class="m-crumb"><a>ホーム</a> › <a>活動ログ</a> › ユーザー活動ログ 集計</div>
<div class="m-body">
<h1 class="m-ttl">ユーザー活動ログ 集計</h1>
<div style="margin:14px 0 16px;font-size:11.5px;color:#5a6276">
期間 <span class="m-in" style="display:inline-block;width:110px">2026-09-15</span>
〜 <span class="m-in" style="display:inline-block;width:110px">2026-10-14</span>
<span class="m-btn">表示</span></div>
%s
<div class="m-card" style="padding:14px 16px">
<div class="m-k" style="margin-bottom:11px">よく見られる画面</div>%s</div>
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
                       "<b>現状</b> — Django 4.2 標準。右サイドバーの絞り込み、"
                       "右上の 2 リンク（集計を見る / CSVダウンロード）はいま動いているものです。"),
    "stock_sum": shot("stock", sum_stock(), SUM_URL,
                      "<b>現状</b> — 集計ページ。棒グラフは CSS の <code>widthratio</code> 製で、"
                      "JavaScript は 1 行もありません。", "sum"),
    "unfold_list": shot("unfold", list_unfold(), LIST_URL,
                        "<b>A 案 / django-unfold</b> — 左サイドバー、⌘K コマンドパレット、"
                        "ダークモード切替。絞り込みの項目名と挙動は現状のまま。"),
    "unfold_sum": shot("unfold", sum_unfold(), SUM_URL,
                       "<b>A 案 / django-unfold</b> — 集計ページ。"
                       "数値カードと表は unfold のコンポーネントで組み直せます。", "sum"),
    "jazz_list": shot("jazz", list_jazz(), LIST_URL,
                      "<b>B 案 / django-jazzmin</b> — AdminLTE 3 / Bootstrap 5。"
                      "カード見出しに件数、濃紺のサイドバー。"),
    "jazz_sum": shot("jazz", sum_jazz(), SUM_URL,
                     "<b>B 案 / django-jazzmin</b> — 集計ページ。"
                     "Bootstrap のカードに収まります。", "sum"),
    "ai_list": shot("ai", list_ai(), LIST_URL,
                    "<b>C 案 / django-admin-interface</b> — Django の構造はそのまま、"
                    "配色とロゴだけを差し替え。移行コストは最小。"),
    "ai_sum": shot("ai", sum_ai(), SUM_URL,
                   "<b>C 案 / django-admin-interface</b> — 集計ページ。"
                   "レイアウトは現状と同一です。", "sum"),
}

import io
for k, v in OUT.items():
    with io.open("frag_%s.html" % k, "w", encoding="utf-8") as fh:
        fh.write(v)
print("wrote %d fragments" % len(OUT))
