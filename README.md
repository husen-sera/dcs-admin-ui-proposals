# DCS Admin UI — Three Proposals

Three options for modernizing the DCS Django admin panel, each **installed against the real DCS
admin and photographed on our own screens**. Every figure is a screenshot of a running system.

**👉 [Open the proposal page](https://husen-sera.github.io/dcs-admin-ui-proposals/)**

- **A — [django-unfold](https://unfoldadmin.com/docs/)** 0.67.0 — most polished, and the best base for
  the analytics dashboard planned next. Pinned to an older release to run on our Python.
  ([demo](https://demo.unfoldadmin.com/) · [repo](https://github.com/unfoldadmin/django-unfold))
- **B — [django-daisy](https://hypy13.github.io/django-daisy-docs/)** 2.0.15 — runs its *current*
  release on our Python, and needed no admin code changes.
  ([demo](https://hypy13-django-daisy.hf.space/admin/) · [repo](https://github.com/hypy13/django-daisy))
- **C — [django-jazzmin](https://github.com/farridav/django-jazzmin)** 3.0.1 — AdminLTE 3 / Bootstrap 5,
  the most conventional admin-panel look, configuration only. Pinned to an Oct-2024 release and ships
  no Japanese translation. ([docs](https://django-jazzmin.readthedocs.io/))

**django-jet-reboot was evaluated and dropped**: it is AGPLv3 and its own packaging declares
"free for non-commercial use", which fails the requirement that libraries be free *and* licensed
for commercial use.

> ℹ️ Screenshots were taken against a throwaway database seeded with placeholder data, because this
> page is served from a public repository. Real figures are in the ClickUp ticket. The DCS admin's
> own language is Japanese, which is why the screens are Japanese.
