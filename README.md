# DCS Admin UI — Two Proposals

Two options for modernizing the DCS Django admin panel, both **installed against the real DCS
admin and photographed on our own screens**. Every figure is a screenshot of a running system.

**👉 [Open the proposal page](https://husen-sera.github.io/dcs-admin-ui-proposals/)**

- **A — [django-unfold](https://unfoldadmin.com/docs/)** 0.67.0 — the more polished option, and the
  better base for the analytics dashboard planned next. Must be pinned to an older release to run
  on our Python. ([demo](https://demo.unfoldadmin.com/) · [repo](https://github.com/unfoldadmin/django-unfold))
- **B — [django-daisy](https://hypy13.github.io/django-daisy-docs/)** 2.0.15 — the only candidate
  that runs its *current* release on our Python, and it needed no admin code changes at all.
  ([demo](https://hypy13-django-daisy.hf.space/admin/) · [repo](https://github.com/hypy13/django-daisy))

**django-jet-reboot was evaluated and dropped**: it is AGPLv3 and its own packaging declares
"free for non-commercial use", which fails the requirement that libraries be free *and* licensed
for commercial use.

> ℹ️ The screenshots were taken against a throwaway database seeded with placeholder data, because
> this page is served from a public repository. Real figures are in the ClickUp ticket.
> The DCS admin's own language is Japanese, which is why the screens are Japanese.
