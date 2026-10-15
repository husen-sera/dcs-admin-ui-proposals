# DCS Admin UI — Three Proposals

A comparison of three options for modernizing the DCS Django admin panel using free,
commercially-licensed (MIT) open-source UI libraries.

**👉 [Open the proposal page](https://husen-sera.github.io/dcs-admin-ui-proposals/)**

- **A — django-unfold** (recommended): Tailwind-based; ships chart components, so it also becomes the
  foundation for the analytics dashboard planned as a follow-up
- **B — django-jazzmin**: AdminLTE / Bootstrap; enabled through configuration alone, lowest migration risk
- **C — django-admin-interface**: keeps Django's structure untouched and changes only the colour scheme

Each option is shown applied to DCS's own screens (the user activity log Detail and Summary pages).

> ⚠️ The images recreate how each library looks — they are not screenshots of a running system.
> Once an option is chosen they will be replaced with real screenshots from a local install.
>
> ℹ️ This page is served from a public repository, so the email addresses, hostname and account
> figures shown are placeholders. The real values are in the ClickUp ticket.
