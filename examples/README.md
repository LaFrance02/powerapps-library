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
| Buttons | `powerlibs-button-danger.yaml` | PowerLibs, "Danger Button" | Red icon+label button (delete/remove/cancel), filled. | Not yet paste-tested |
| Buttons | `powerlibs-button-ghost.yaml` | PowerLibs, "Ghost Button" | Text-only tinted-on-hover button for a third/lesser action row. | Not yet paste-tested |
| Buttons | `powerlibs-button-link.yaml` | PowerLibs, "Link Button" | A `Label` styled and wired to act like a hyperlink (e.g. "Forgot your password?"). | Not yet paste-tested |
| Buttons | `powerlibs-button-badge-count.yaml` | PowerLibs, "Badge Button" | Icon+label button with a small numbered count pill (e.g. "Approvals 3"). | Not yet paste-tested |
| Buttons | `powerlibs-button-back.yaml` | PowerLibs, "Back Button" | Chevron + "Back" wired to `Back()`. | Not yet paste-tested |
| Buttons | `powerlibs-button-split.yaml` | PowerLibs, "Split Button" | Primary action + chevron that opens a dropdown of related actions (Save / Save and new / Save as draft). | Not yet paste-tested |
| Buttons | `powerlibs-button-action-bar.yaml` | PowerLibs, "Action Bar" | Bottom-pinned bar with an unsaved-changes hint plus Cancel/Save — meant for the bottom of every edit screen. | Not yet paste-tested |
| Buttons | `powerlibs-button-primary.yaml` | PowerLibs, "Primary Button" | Bare modern filled brand button — the default button most screens need. | Not yet paste-tested |
| Buttons | `powerlibs-button-icon.yaml` | PowerLibs, "Icon Button" | Filled icon+label button (e.g. "Add item"). | Not yet paste-tested |
| Buttons | `powerlibs-button-outline.yaml` | PowerLibs, "Outline Button" | Bare modern outline-appearance button — the default secondary action next to a primary. | Not yet paste-tested |
| Buttons | `powerlibs-button-loading.yaml` | PowerLibs, "Loading Button" | Button that swaps its label for a spinner + "Saving..." while a variable is true; includes a demo `Timer` to reset it. | Not yet paste-tested — see caution below |
| Buttons | `powerlibs-button-gradient.yaml` | PowerLibs, "Gradient Button" | Two-color gradient button drawn as an SVG `Image`, no HTML control needed. | Not yet paste-tested |
| Buttons | `powerlibs-button-raised.yaml` | PowerLibs, "Raised Button" | Primary button with a bold drop shadow for the one action that must stand out. | Not yet paste-tested |
| Buttons | `powerlibs-button-group.yaml` | PowerLibs, "Button Group" | Three-way segmented control (e.g. List/Board/Calendar) in one outlined track, active segment tinted. | Not yet paste-tested |
| Avatars | `powerlibs-avatar-user.yaml` | PowerLibs, "User Avatar" | Signed-in user's M365 photo via `User().Image`, falling back to initials from `User().FullName`; optional presence dot. | Not yet paste-tested |
| Avatars | `powerlibs-avatar-user-chip.yaml` | PowerLibs, "User Chip" | Avatar + live user name in one pill, sized to the name's length. | Not yet paste-tested |
| Avatars | `powerlibs-avatar-group.yaml` | PowerLibs, "Avatar Group" | Overlapping stack of initials circles (signed-in user live, others literal names) with a "+N" overflow circle. | Not yet paste-tested |
| Badges | `powerlibs-badge-simple.yaml` | PowerLibs, "Simple Badge" | Self-contained colored status badge — set `Color`/`Text`/`Width` only, Hover/Pressed follow automatically. | Not yet paste-tested |
| Badges | `powerlibs-badge-border.yaml` | PowerLibs, "Border Badge" | Same self-contained pattern as Simple Badge, plus a border outline. | Not yet paste-tested |
| Badges | `powerlibs-badge-pills.yaml` | PowerLibs, "Pills Badge" | Same pattern, pill-shaped (fully rounded corners). | Not yet paste-tested — see naming caution below |
| Badges | `powerlibs-badge-outlined-pills.yaml` | PowerLibs, "Outlined Pills Badge" | Pill-shaped plus a border outline. | Not yet paste-tested — see naming caution below |

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

## Notes on the button/avatar/badge batch (read before using)

**This batch, unlike the animation batch, genuinely does prefer modern controls where one
exists** — the source file's own header says "pasted using Modern Controls if that option was
available," and that mostly holds up: `Primary Button`, `Outline Button`, and both buttons in
`Action Bar` are bare `Button@0.0.45`. But most of the icon+label and custom-shaped buttons
(Danger, Ghost, Badge Button, Back, Split, Icon, Loading, Gradient, Button Group) are built as a
`GroupContainer@1.5.0` + `Image@2.2.3`/`Text@0.0.51` for the visual, with an invisible
`Classic/Button@2.2.0` layered on top purely as the tap target — see
`reference/confirmed-versions.md` for why that's not a contradiction (classic is used as a hitbox,
not for its styling). Full breakdown of every version seen, including the new `GroupContainer@1.3.0`
mismatch in the avatar components and the one `Classic/Icon@2.5.0` instance in Split Button, is in
that file now — don't duplicate it here.

**Naming caution:** `powerlibs-badge-simple.yaml`, `powerlibs-badge-pills.yaml`, and
`powerlibs-badge-outlined-pills.yaml` all use the **identical** control name `btnBadge1` — this is
copy-paste residue from PowerLibs, not intentional. `powerlibs-badge-border.yaml` got renamed to
`btnBadge1_1` but the other three didn't. Per `syntax-gotchas.md`'s uniqueness rule, rename these
before using more than one badge variant on the same screen — Studio will reject (or silently
misbehave on) a duplicate control name.

**Usage notes worth keeping** (from comments stripped out of the badge/avatar file — the button
file had none):
- **User Avatar**: `imgUserAvatarPhoto` shows the signed-in user's M365 photo via `User().Image`
  with no connector needed; when they have no photo it falls back to initials from
  `User().FullName`. The presence dot is a static color picked at design time — to make it live,
  point `conUserAvatarPresence`'s `Fill` at a real status field (e.g. a SharePoint column).
- **User Chip**: name, initials, and pill width all follow `User().FullName` live, no connector
  needed.
- **Avatar Group**: only the first circle is live (the signed-in user via `User().FullName`); the
  rest are literal names set at design time, with each one's color and initials derived from that
  name so the same person always renders the same color.
- **Loading Button**: the included `Timer` (`tmrLoadingReset`) is a **demo only** — it flips
  `varLoadingButtonBusy` back to `false` after a fixed 3 seconds. In a real screen, delete this
  timer and set `varLoadingButtonBusy` to `false` yourself once the real `Patch`/`SubmitForm`
  finishes.
