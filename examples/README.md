# Examples

Real, working YAML snippets Matt has pasted in — from PowerLibs or anywhere else he's found a
pattern he likes — kept as templates to reuse rather than regenerate from scratch each time.

**Important distinction from `reference/confirmed-versions.md`:** everything here is PowerLibs- or
third-party-sourced and **not yet paste-tested by Matt in his own Studio environment**. Treat
control versions used in these files as "worth trying," not "confirmed." Once one of these gets
pasted and actually works (or needs a fix) in a real app, promote the relevant facts into
`reference/confirmed-versions.md` and note it here as tested.

**Ingestion format (confirmed working, 2026-09-19):** Matt pastes a `.txt` with
`Title: ... / Description: ... / YAML: ...` blocks, one per component, separated by blank lines.
This splits cleanly and reliably — keep using it. Any `#` comments inside a pasted YAML block are
stripped before saving here (they'd cause a Studio parse error per `syntax-gotchas.md`); anything
load-bearing in a stripped comment (how to wire the pattern to real data, which variable to bind)
is preserved in this file's notes instead, not silently dropped.

| Category | File | Source | What it is | Status |
|---|---|---|---|---|
| App Shells | `powerlibs-collapsible-sidebar-shell.yaml` | PowerLibs, "Collapsible Sidebar App Shell" | Responsive nav shell: collapsible 240px/64px sidebar, bottom tab bar below 768px, dark/light switch, gallery-driven nav list. | Not yet paste-tested |
| Animations | `powerlibs-animation-bar-chart.yaml` | PowerLibs, "Animated Bar Chart" | One SVG `Image` control; bars grow from baseline in sequence, values fade in after landing. | Not yet paste-tested |
| Animations | `powerlibs-animation-line-chart.yaml` | PowerLibs, "Animated Line Chart" | SVG line chart with gradient fill, animated draw-on line, staggered data-point reveals, paired with a separate replay button control. | Not yet paste-tested — see caution below |
| Animations | `powerlibs-animation-success-check.yaml` | PowerLibs, "Success Check" | Ring-sweep + checkmark-draw SVG shown on `varShowSuccess`, plus a demo button. | Not yet paste-tested |
| Animations | `powerlibs-animation-staggered-fade-in.yaml` | PowerLibs, "Staggered Fade-in" | Gallery rows, each row a per-item SVG that fades in and slides up on a staggered delay by row index. | Not yet paste-tested |
| Animations | `powerlibs-animation-loading-spinner-ring.yaml` | PowerLibs, "Loading Spinner - Ring" | Spinning-ring SVG loading indicator with caption label. | Not yet paste-tested |
| Animations | `powerlibs-animation-loading-spinner-dots.yaml` | PowerLibs, "Loading Spinner - Dots" | Pulsing-dots variant of the same loading indicator. | Not yet paste-tested |
| Animations | `powerlibs-animation-loading-spinner-bars.yaml` | PowerLibs, "Loading Spinner" (bars) | Bouncing-bars variant of the same loading indicator. | Not yet paste-tested |
| Animations | `powerlibs-animation-toggle.yaml` | PowerLibs, "Animated Toggle" | Two-option pill switch (e.g. Monthly/Yearly) that slides on select, sets `varToggle`. | Not yet paste-tested |
| Animations | `powerlibs-animation-count-up.yaml` | PowerLibs, "Count-up Number" | KPI number that animates 0 → target on open via a 60-frame SVG sequence; replay icon included. | Not yet paste-tested |
| Animations | `powerlibs-animation-progress-bar.yaml` | PowerLibs, "Progress Bar" | Bar that fills over 3s with an ease-out curve, status text swap, percentage counter, paired `Timer` and Start button. | Not yet paste-tested |
| Animations | `powerlibs-animation-progress-circle.yaml` | PowerLibs, "Progress Circle" | Ring that sweeps to a value (0–100) over 3s, number + caption in the middle, replay icon. | Not yet paste-tested |

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

## Notes on the animation batch (read before using)

**These are classic controls, not modern — flagging since that contradicts the stated intent.**
Every control across all 11 files is either `Label@2.5.1` (classic; modern equivalent is `Text`),
`Classic/Button@2.2.0` and `Classic/Icon@2.5.0` (explicit classic prefix), or a classic-only
control with no modern option at all (`Image`, `GroupContainer`, `Gallery`, `Timer`). Not one bare
modern control (`Button@0.0.x`, `Text@0.0.x`) appears anywhere in this batch — unlike the sidebar
shell above, which does use modern `Button`/`Text`. If these get built into a modern-family app,
the `Classic/Button` and `Classic/Icon` instances specifically should probably be swapped to their
modern equivalents (bare `Button`, and whatever the modern icon control turns out to be) for
consistency — that swap hasn't been attempted or verified.

**Caution — untested syntax style:** `powerlibs-animation-line-chart.yaml`'s `Image` property uses
a bare `Image: =` with the formula continuing on indented following lines, instead of the `Image: |-`
block literal style every other file here (and every one of Matt's confirmed patterns) uses. This
is likely valid YAML (a folded plain scalar), but it's a different, unverified style — worth
converting to `|-` block literal for consistency before pasting, rather than assuming it behaves
identically to the confirmed pattern.

**Usage notes worth keeping** (from comments stripped out of the YAML for paste-safety):
- **Success Check**: the demo button (`btnSuccessDemo`) is a placeholder — in a real screen, delete
  it and call its same two `Set()` calls (`Set(varSuccessCount, ...)`; `Set(varShowSuccess, true)`)
  right after your actual `Patch`/`SubmitForm`.
- **Count-up Number**: the target value (`12480`) is hardcoded in the SVG string — replace it with
  a real formula, e.g. `CountRows(Customers)`, before use.
- **Progress Circle**: the displayed value comes from `lblCircleValue.Text` (hardcoded to `65`) —
  replace with a real formula, e.g.
  `Round(100 * CountRows(Filter(Tasks, Done)) / CountRows(Tasks), 0)`.
- **Loading Spinner (all three variants)**: bind the container's `Visible` to a real loading flag,
  e.g. `=varIsLoading` — it's hardcoded `true` in the saved file.
- **Progress Bar**: the `Timer` only re-enables the Start button after the 3-second run; the fill
  animation itself is driven entirely inside the SVG, not by the Timer.
- Several animations replay by incrementing a counter variable (`varBarChartReplay`,
  `varChartReload`, `varRevealRun`, `varCountRun`, `varCircleRun`, `varToggleCount`) that gets
  embedded into the SVG's `id` attribute, forcing the browser to treat it as a new image and
  replay the animation. If combining several of these in one app, keep each one's counter variable
  name distinct — don't reuse one counter across two different animated components.
