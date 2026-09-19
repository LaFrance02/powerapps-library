# Examples

Real, working YAML snippets Matt has pasted in — from PowerLibs or anywhere else he's found a
pattern he likes — kept as templates to reuse rather than regenerate from scratch each time.

**Important distinction from `reference/confirmed-versions.md`:** everything here is PowerLibs- or
third-party-sourced and **not yet paste-tested by Matt in his own Studio environment**. Treat
control versions used in these files as "worth trying," not "confirmed." Once one of these gets
pasted and actually works (or needs a fix) in a real app, promote the relevant facts into
`reference/confirmed-versions.md` and note it here as tested.

| File | Source | What it is | Status |
|---|---|---|---|
| `powerlibs-collapsible-sidebar-shell.yaml` | PowerLibs, "Collapsible Sidebar App Shell" | A responsive nav shell: collapsible 240px/64px sidebar on desktop (chevron toggle, `gblRailShellRail`), a bottom tab bar below 768px, dark/light theme switch (`gblRailShellDark`), and a gallery-driven nav list with header rows. Selection state lives in `gblRailShellNav` / `gblRailShellPage`. | Not yet paste-tested |

## Notes on the sidebar shell (read before using)

This is **not a Component** — there's no `ComponentDefinitions` entry, no `ComponentName`. It's a
flat list of screen-level controls meant to be pasted directly as a screen's `Children:`, and its
own instructions say to paste the same block onto every screen that needs it. That's a real
architectural difference from `components/README.md`'s `cmpSidebar` (a reusable
`CanvasComponent`/`ComponentName: cmpSidebar` instance) — copy-per-screen vs. instantiate-once.
Decide which pattern a given app should use before assuming this replaces the component approach;
don't mix them in one app without a reason.

Control versions used: `GroupContainer@1.5.0`, `Button@0.0.45`, and `Gallery@2.15.0` all match the
cross-project confirmed baseline. `Text@0.0.51` and `Image@2.2.3` are new — not in
`confirmed-versions.md` at all (Matt's confirmed baseline uses `Label@2.5.1`, not `Text`, and has
no confirmed `Image` control). The `Gallery` variant here
(`BrowseLayout_Vertical_TwoTextOneImageVariant_ver5.0`) also **differs** from the confirmed
`..._pcfCore` variant — worth watching for a paste error on that specific line if this gets tried.
