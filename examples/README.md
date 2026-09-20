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
| Calendars | `powerlibs-calendar-basic.yaml` | PowerLibs, "Calendar" | Full-screen month-view date picker: nav arrows, weekday header, selected/today indicators, selected-date footer. | Not yet paste-tested — see full-screen caution below |
| Calendars | `powerlibs-calendar-with-header.yaml` | PowerLibs, "Calendar with Header" | Same calendar, styled with a colored header band (year/month), a today ring instead of a dot, and an event-dot placeholder. | Not yet paste-tested — see full-screen caution below |
| Calendars | `powerlibs-time-picker.yaml` | PowerLibs, "Time Picker" | Three dropdown selectors (hours/minutes/seconds), each a button that opens a scrollable gallery of values, with a rotating-arrow icon and an HH:MM:SS display. | Not yet paste-tested |
| Sidebars | `powerlibs-sidebar-wide.yaml` | PowerLibs, "Sidebar Wide" | Full-width labeled sidebar, single container. | Not yet paste-tested |
| Sidebars | `powerlibs-sidebar-narrow.yaml` | PowerLibs, "Narrow Sidebar" | Icon-only narrow sidebar for space-efficient navigation. | Not yet paste-tested |
| Sidebars | `powerlibs-sidebar-collapsible.yaml` | PowerLibs, "Collapsible Sidebar" | Sidebar that toggles between expanded/icon-only. | Not yet paste-tested |
| Sidebars | `powerlibs-sidebar-with-navbar.yaml` | PowerLibs, "Sidebar with Navbar" | Narrow icon sidebar combined with a top navbar — two sibling root containers, not nested. | Not yet paste-tested |
| Sidebars | `powerlibs-sidebar-dropdown.yaml` | PowerLibs, "Dropdown Sidebar" | Sidebar with expand/collapse dropdown sections (MAIN/WORKSPACE), SVG chevron rotation per section. | Not yet paste-tested |
| Sidebars | `powerlibs-sidebar-glass-floating.yaml` | PowerLibs, "Glass Floating Sidebar" | Glassmorphism-styled floating variant of the dropdown sidebar; reuses the same root control name (`conSidebarDropdown`) as the file above — rename before using both on one screen. | Not yet paste-tested |
| Sidebars | `powerlibs-sidebar-animated.yaml` | PowerLibs, "Animated Sidebar" | Sidebar with per-item select animation. | Not yet paste-tested — see caution below, one control's `Image` formula looks corrupted |
| Sidebars | `powerlibs-sidebar-advanced.yaml` | PowerLibs / powerappsui.com, "Advanced Sidebar" | A genuine `ComponentDefinitions:` Canvas Component (`cmpSidebar`) — collapsible nav with theming, parent/child tree, badges, footer menu. Full property/event docs captured — see notes below. **This exact component was pasted verbatim into both the Sidebars and Navigation source files** — only one copy is kept here. | Not yet paste-tested |
| Navigation | `powerlibs-nav-bar.yaml` | PowerLibs, "Navigation Bar" | Clean navbar: logo, title, user profile picture. | Not yet paste-tested |
| Navigation | `powerlibs-nav-bar-tablist.yaml` | PowerLibs, "NavBar with Tablist" | Navbar with centered tabs + underline indicator — **not** a real `TabList` control despite the name; hand-built from Gallery+Classic/Button+Rectangle. | Not yet paste-tested |
| Navigation | `powerlibs-nav-bar-scrollable-content.yaml` | PowerLibs, "NavBar with Scrollable Content" | Navbar + a vertically scrollable content area below it. Source `Description:` was blank. | Not yet paste-tested |
| Navigation | `powerlibs-nav-mega-menu.yaml` | PowerLibs, "Mega Menu Navbar" | Navbar with expandable mega-menu dropdowns, animated rotating arrows, tied together via a `Group: NavBar` tag. | Not yet paste-tested — see YAML bug below |
| Navigation | `powerlibs-nav-mega-menu-minimal.yaml` | PowerLibs, "Minimal Mega Menu Navbar" | Same mega-menu pattern, minimal styling, `Group: MinimalMegaNavBar` tag, `gbl`-prefixed globals (correctly Set()-backed, unlike its sibling above). | Not yet paste-tested |
| Modals | `powerlibs-modal-bulk-action.yaml` | PowerLibs, "Bulk Action Modal" | Delete N selected records confirmation with row preview list. | Not yet paste-tested |
| Modals | `powerlibs-modal-type-to-confirm.yaml` | PowerLibs, "Type to Confirm Modal" | Irreversible delete gated by typing an exact confirmation word. | Not yet paste-tested |
| Modals | `powerlibs-modal-progress.yaml` | PowerLibs, "Progress Modal" | Spinning-ring + percent bar driven by a variable; scrim tap does not dismiss it. | Not yet paste-tested |
| Modals | `powerlibs-modal-access-denied.yaml` | PowerLibs, "Access Denied Modal" | Lock badge, required role + who to ask, Request access / Go back. | Not yet paste-tested |
| Modals | `powerlibs-modal-feedback-rating.yaml` | PowerLibs, "Feedback Rating Modal" | 5-star picker + optional comment. | Not yet paste-tested |
| Modals | `powerlibs-modal-confirm-action.yaml` | PowerLibs, "Confirm Action" | Generic destructive-action confirm. | Not yet paste-tested |
| Modals | `powerlibs-modal-basic.yaml` | PowerLibs, "Modal" | The plain baseline modal — title, text, close X, one button. | Not yet paste-tested |
| Modals | `powerlibs-modal-success.yaml` | PowerLibs, "Success Modal" | Green check badge (uses `Classic/Icon`, the one badge in this batch not built from an inline SVG). | Not yet paste-tested |
| Modals | `powerlibs-modal-info.yaml` | PowerLibs, "Info Modal" | "What's new" checklist + external link (`Launch`); the link uses classic `Label`, not modern `Text`. | Not yet paste-tested |
| Modals | `powerlibs-modal-sign-out.yaml` | PowerLibs, "Sign Out Modal" | Grey badge sign-out confirm. | Not yet paste-tested |
| Modals | `powerlibs-modal-unsaved-changes.yaml` | PowerLibs, "Unsaved Changes Modal" | Warning badge, changed-fields box, 3-way choice (save & leave / discard / stay). | Not yet paste-tested |
| Modals | `powerlibs-modal-approval-request.yaml` | PowerLibs, "Approval Request Modal" | Request summary + approver card, Cancel/Submit. | Not yet paste-tested |
| Modals | `powerlibs-modal-error.yaml` | PowerLibs, "Error Modal" | Optional error-details box (message + code), Try again/Go back. | Not yet paste-tested |
| Modals | `powerlibs-modal-input.yaml` | PowerLibs, "Input Modal" | Multiline text capture into a variable, Cancel/Submit. | Not yet paste-tested |
| Galleries | `powerlibs-gallery-carousel.yaml` | PowerLibs, "Gallery Carousel" | Auto-advancing spotlight carousel via hidden `Timer`; not an actual `Gallery` control despite the file's category. | Not yet paste-tested |
| Galleries | `powerlibs-gallery-announcement-bar-carousel.yaml` | PowerLibs, "Announcement Bar Carousel" | Slim auto-advancing announcement bar, same Timer-driven pattern. | Not yet paste-tested |
| Galleries | `powerlibs-gallery-list.yaml` | PowerLibs, "List Gallery" | Row list: avatar initials, status pill, chevron, search. | Not yet paste-tested |
| Galleries | `powerlibs-gallery-card-grid.yaml` | PowerLibs, "Card Grid" | Responsive tile grid with icon tile + status pill. | Not yet paste-tested |
| Galleries | `powerlibs-gallery-card-list.yaml` | PowerLibs, "Card List" | One-card-per-record list with status/priority pills. | Not yet paste-tested |
| Galleries | `powerlibs-gallery-data-table.yaml` | PowerLibs, "Data Table" | Rows/columns table, search, pagination footer. | Not yet paste-tested |
| Galleries | `powerlibs-gallery-sortable-data-table.yaml` | PowerLibs, "Sortable Data Table" | Data Table plus clickable sortable column headers. | Not yet paste-tested |
| Dropdowns | `powerlibs-dropdown-menu.yaml` | PowerLibs, "Dropdown Menu" | Trigger + chevron + action menu, click-outside-to-close scrim. | Not yet paste-tested |
| Dropdowns | `powerlibs-dropdown-user-profile.yaml` | PowerLibs, "User Profile Dropdown" | Round-avatar trigger, profile menu — near-duplicate of Profile Menu below. | Not yet paste-tested |
| Dropdowns | `powerlibs-dropdown-nested.yaml` | PowerLibs, "Nested Dropdown" | Menu row that opens a second-level submenu; submenu position is hardcoded per row index. | Not yet paste-tested |
| Dropdowns | `powerlibs-dropdown-profile-menu.yaml` | PowerLibs, "Profile Menu" | Name+avatar pill trigger, `User()`-driven header — near-duplicate of User Profile Dropdown above. | Not yet paste-tested |
| Dropdowns | `powerlibs-dropdown-inline.yaml` | PowerLibs, "Inline Dropdown" | Quiet text trigger with icon + chevron, no box — for headers/breadcrumbs. | Not yet paste-tested |
| Dropdowns | `powerlibs-dropdown-navigation.yaml` | PowerLibs, "Navigation Dropdown" | Menu of screens, grid icon per row. | Not yet paste-tested |
| Dropdowns | `powerlibs-dropdown-searchable-lookup.yaml` | PowerLibs, "Searchable Lookup" | Type-ahead filter over a static in-memory `Table()`. | Not yet paste-tested — see TextInput footgun below |
| Dropdowns | `powerlibs-dropdown-people-picker.yaml` | PowerLibs, "People Picker" | Searchable person picker, sample data by default, switchable to `Office365Users.SearchUser`. | Not yet paste-tested |
| Drawers | `powerlibs-drawer-detail.yaml` | PowerLibs, "Detail Drawer" | Right-side record detail panel, Reject/Approve. | Not yet paste-tested |
| Drawers | `powerlibs-drawer-filter.yaml` | PowerLibs, "Filter Drawer" | Right-side filter panel, toggle chips backed by collections, Reset/Apply. | Not yet paste-tested |
| Drawers | `powerlibs-drawer-action-sheet.yaml` | PowerLibs, "Action Sheet" | Bottom sheet action menu, grab handle, 5 rows. | Not yet paste-tested |
| Drawers | `powerlibs-drawer-comments.yaml` | PowerLibs, "Comments Drawer" | Right-side comment thread, gallery + composer that appends to a collection. | Not yet paste-tested |
| Drawers | `powerlibs-drawer-bottom-sheet.yaml` | PowerLibs, "Bottom Sheet" | Bottom-anchored quick-entry sheet, always full width (no responsive-radius formula needed). | Not yet paste-tested |
| Drawers | `powerlibs-drawer-form.yaml` | PowerLibs, "Form Drawer" | Right-side new/edit-record panel, 5 mixed-type fields. | Not yet paste-tested |
| Cards | `powerlibs-card-approval.yaml` | PowerLibs, "Approval Card" | Approver-queue item, Reject/Approve. | Not yet paste-tested |
| Cards | `powerlibs-card-asset.yaml` | PowerLibs, "Asset Card" | IT/inventory asset, Check out/in. | Not yet paste-tested |
| Cards | `powerlibs-card-contact.yaml` | PowerLibs, "Contact Card" | Contact directory item with real `Launch()` Email/Call buttons. | Not yet paste-tested |
| Cards | `powerlibs-card-task.yaml` | PowerLibs, "Task Card" | Kanban task, subtask progress bar, 3 stacked assignee avatars. | Not yet paste-tested |
| Cards | `powerlibs-card-timesheet.yaml` | PowerLibs, "Timesheet Card" | Weekly timesheet rows + total box with progress bar. | Not yet paste-tested |
| Cards | `powerlibs-card-inspection.yaml` | PowerLibs, "Inspection Card" | Pass/fail inspection, score bar, 5-item checklist, photo thumbnails. | Not yet paste-tested |
| Cards | `powerlibs-card-dynamic-form.yaml` | PowerLibs, "Dynamic Form Card" | Deploy-confirmation form driven by an inline `Table()` field-definition list — the one genuinely data-driven-schema entry in the Card batch. | Not yet paste-tested |
| Cards | `powerlibs-card-employee.yaml` | PowerLibs, "Employee Card" | Employee directory item, 3 stat tiles, Assign task/Message. | Not yet paste-tested |
| Cards | `powerlibs-card-project.yaml` | PowerLibs, "Project Card" | Project board card, cover image, progress bar, 2 metric tiles. | Not yet paste-tested |
| Cards | `powerlibs-card-modern-form.yaml` | PowerLibs, "Modern Form" | Generic "New Form" modal — mislabeled "Card" in the source file, actually a form/modal. | Not yet paste-tested |
| Data Display | `powerlibs-data-display-skeleton-card.yaml` | PowerLibs, "Skeleton Card" | Pulsing placeholder card via `Timer` + `Sin()` opacity pulse on `GroupContainer.Fill`. | Not yet paste-tested |
| Data Display | `powerlibs-data-display-skeleton-list.yaml` | PowerLibs, "Skeleton List" | Same shimmer pattern, 3 avatar+text rows. | Not yet paste-tested |
| Data Display | `powerlibs-data-display-skeleton-text.yaml` | PowerLibs, "Skeleton Text" | Same shimmer pattern, 4 paragraph lines. | Not yet paste-tested |
| Data Display | `powerlibs-data-display-kpi-spotlight-carousel.yaml` | PowerLibs, "KPI Spotlight Carousel" | Auto-rotating single-metric spotlight, dots/arrows/pause, `Timer`-driven. | Not yet paste-tested |
| Data Display | `powerlibs-data-display-kpi-tile.yaml` | PowerLibs, "KPI Tile" | Caption + big number + trend delta. Comment stripped, see notes below. | Not yet paste-tested |
| Data Display | `powerlibs-data-display-bar-chart.yaml` | PowerLibs, "Bar Chart" | Real-control horizontal bar chart (`Gallery` + `GroupContainer` bars), theme-following. Comment stripped, see notes below. | Not yet paste-tested |
| Data Display | `powerlibs-data-display-empty-state.yaml` | PowerLibs, "Empty State" | Icon + heading + body + CTA for an empty gallery. Comment stripped, see notes below. | Not yet paste-tested |

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

## Notes on the calendar/time-picker batch (read before using)

**These two calendar files are full screens, not children lists — a different shape than
everything else in this library.** `powerlibs-calendar-basic.yaml` and
`powerlibs-calendar-with-header.yaml` both start with `Screens: / ScreenCalendar:`, meaning they
define (or overwrite) an entire screen including its own `OnVisible`. Every other example so far —
sidebar shell, all buttons, avatars, badges, animations, and this batch's own Time Picker — is a
flat `- control:` children list meant to paste *into* an existing screen's `Children:`. Don't treat
these two the same way; pasting a full `Screens:` block where Studio expects a children list (or
vice versa) will fail or do something unintended. Added the general version of this distinction to
`syntax-gotchas.md`. Pick **one** of the two Calendar variants for a given screen — they reuse the
same control names (`conCalendar`, `galWeekday`, `galMonthDay`, `lblDayLabel`, `icoPrevMonth`,
`icoNextMonth`, `lblSelectedDate`), so they're alternate designs, not composable pieces.

**Dead/unresolved variables in both Calendar files:** `OnSelect` on the prev/next month icons
references `_minDate` and `_maxDate` (`If(_minDate > _firstDayOfMonth, Set(_minDate, ...))`), but
neither variable is ever initialized in `OnVisible` or anywhere else in the captured YAML. This
looks like vestigial logic from a larger PowerLibs component (probably a date-range-restricted
variant) that got left in. Harmless as-is (comparing a date to a blank variable just won't trigger
the `Set`), but don't assume `_minDate`/`_maxDate` do anything until you either initialize them
yourself or strip the dead branches.

**New/unverified syntax:** Time Picker's dropdown buttons carry a `Group: Time Picker` property
alongside `Control:`/`Properties:` — not the same thing as a `GroupContainer` control, looks like a
Studio Tree View organizational label. Not confirmed against a real paste; see the new-syntax
section in `syntax-gotchas.md`.

**Version notes**: this batch adds a brand-new control, `Circle@2.3.0` (used for selected-day/today
indicators in both calendars), and a *third* distinct `GroupContainer` version — `1.4.0` in Time
Picker, joining the already-flagged `1.3.0` (avatars) vs. `1.5.0` (baseline/everything else)
split. Full detail in `confirmed-versions.md` — don't assume any single `GroupContainer` version is
"the" version going forward, check per-file.

**Style note:** Time Picker's hour/minute/second value lists use `Items: |` (literal block,
*keeps* trailing newline) where the rest of the library consistently uses `Items: |-` (strips it).
Probably harmless for a `Table`/array literal, but it's a style inconsistency worth normalizing to
`|-` if this gets edited before pasting, for consistency with everything else confirmed so far.

## Notes on the "Large Drip" batch (Sidebars, Navigation, Modals, Galleries, Dropdowns, Drawers,
## Cards, Data Display — read before using)

This was a 9-file simultaneous upload (8 of the 9 processed here; the 9th, a duplicate re-paste of
the already-processed Calendar Components file, was correctly skipped). Each of the 8 source files
was processed by its own pass so findings below are organized by source file. A cross-cutting theme
worth calling out up front: **several of these files openly claim "modern controls used where
available" in their own intro line, and that claim does not hold uniformly** — see each section
below for specifics. Treat every "modern where available" claim in a file's intro as a hint to
verify, not a guarantee.

### Sidebars batch

Source file promised extra "cmpnav" documentation at the end — what's actually there is full
third-party template documentation (Installation/Usage/Properties/Events/Architecture) for the
**Advanced Sidebar** entry, sourced from `https://www.powerappsui.com/components/sidebar`, not
anything specific to Matt's own Transfer Log / Cryo Dewar apps. "cmpnav" turned out to be informal
shorthand for that component's internal variable names (`_cmpNavIsExpanded`, `_cmpNavSelID`,
`_cmpNavFooterMenu`, `galNavItems`, `cntNavHeader`, etc.) — the component itself is named
`cmpSidebar`, and every internal child control still says "Nav." If Matt's real apps do use a
component under the literal name `cmpNav`, this file doesn't confirm that connection.

`powerlibs-sidebar-advanced.yaml` is a genuine Canvas **Component** (`ComponentDefinitions:` root
key) — a third top-level YAML shape alongside the flat children-list and the full `Screens:` block,
with `AccessAppScope: true` so it reads/writes three app-scoped variables directly
(`_cmpNavIsExpanded`, `_cmpNavSelID`, `_cmpNavFooterMenu`) plus a collection (`colNavExpanded`),
bypassing normal component-property encapsulation — all three (four, really — the component's own
doc undercounts them, see below) must be initialized on every screen's `OnVisible`. It ships 13
Input properties, 2 Output properties, 5 Events, and 15 built-in SVG icons; full property/event
tables and usage snippets (OnNavSelect switch, Items schema, badge wiring, logo fallback, icon
extension) are preserved in the file's originating source — ask if you need them restated here.
The component's own "Implementation Details" section says "App-scoped variables (3)" but its own
architecture diagram lists four (`_cmpNavIsExpanded`, `_cmpNavSelID`, `_cmpNavFooterMenu`,
`colNavExpanded`) — a small inconsistency in the source's own docs, not something to silently
correct without checking against a real paste.

**This exact `cmpSidebar` component was pasted verbatim into both the Sidebars and Navigation
source files** (byte-identical except one trailing blank line) — only `powerlibs-sidebar-advanced.yaml`
is kept; do not recreate a Navigation-prefixed copy.

Version/pattern findings: `GroupContainer` appears in all three already-known versions (1.5.0,
1.3.0, 1.4.0) across this one file's entries — no 4th version. A genuinely new control version,
**`Classic/TextInput@2.3.2`**, shows up once (Advanced Sidebar's search box) — not the confirmed
modern `TextInput@0.0.54`. Every entry in this batch uses **only classic controls** for Button
(`Classic/Button@2.2.0`) and Icon (`Classic/Icon@2.5.0`) despite both families having a modern
option — a total violation of "modern where available" for this whole file, worth noting since the
sidebar shell already in the library (`powerlibs-collapsible-sidebar-shell.yaml`) does use modern
Button/Text. Text choice is also split: the 7 non-componentized sidebars use modern `Text@0.0.51`,
but Advanced Sidebar uses classic `Label@2.5.1` exclusively.

`powerlibs-sidebar-animated.yaml`'s `imgAnimatedSidebar.Image` formula looks corrupted as captured
— it's a `|-` block whose entire body is wrapped in an extra layer of literal double-quotes with
escaped `\n`/`\"` sequences (reads like a JSON-stringified formula rather than a raw one), which
would likely make Power Fx treat the whole thing as inert literal text rather than an executable
`With(...)` expression. Several of that same file's buttons also have empty `PropertyName: =`
values (`HoverBorderColor`, `PressedBorderColor`, `PressedColor`, `Text`) — don't assume this file
pastes cleanly without checking these two things first.

`powerlibs-sidebar-dropdown.yaml` and `powerlibs-sidebar-glass-floating.yaml` share the identical
root control name `conSidebarDropdown` — rename one before using both on the same screen.

### Navigation batch

6 entries total, but one (Advanced Sidebar) is the cross-file duplicate described above and isn't
duplicated here — see Sidebars notes. The remaining 5 (`powerlibs-nav-bar*`,
`powerlibs-nav-mega-menu*`) are **100% classic-control** (`Classic/Button@2.2.0`,
`Classic/Icon@2.5.0`, one `Classic/TextInput@2.3.2`) — zero modern Button/Text/TextInput anywhere,
despite Button/Text/TextInput/Icon all having modern options. "NavBar with Tablist" is misleadingly
named — it's hand-built from `Gallery` + `Classic/Button` + `Rectangle`, not a real `TabList`
control.

**Genuine YAML defect, preserved as-is:** `powerlibs-nav-mega-menu.yaml` has four controls
(`btn<Category>ItemOverlay` ×4) with a bare `HoverBorderColor: =` / `PressedBorderColor: =` — an
empty Power Fx expression with nothing after the `=`. This fails strict `yaml.safe_load` (a lone
`=` is a reserved YAML 1.1 indicator) — unclear whether Power Apps Studio's own importer tolerates
it. Worth a real paste test before trusting this file, or fixing to `=RGBA(0,0,0,0)` for
consistency with every other Border/Fill property in the same block first.

**Variable-naming semantic mismatch, worth flagging to the paired Skill's generation logic:**
`powerlibs-nav-mega-menu.yaml` uses `var`-prefixed names (`varActiveNav`, `varAnimProducts`, etc.)
that are actually created via `Set()` — i.e., real **globals**, not context variables, despite the
`var` prefix normally signaling `UpdateContext`/local scope elsewhere in this library. Its sibling
`powerlibs-nav-mega-menu-minimal.yaml` solves the identical problem (toggle active category + stamp
a timestamp to re-key a CSS animation) with correctly-prefixed `gbl`-names (`gblActiveNav`,
`gblAnimProjects`, etc.) via the same `Set()` mechanism — same mechanism, two conflicting naming
conventions in two sibling files. A `Group:` property (Studio Tree View tag, still unverified
against a real paste) appears on both mega-menu files, tagging the navbar root plus every dropdown
panel that must live outside the navbar's own nesting to render as an overlay.

### Modal batch (14 entries)

All 14 use the identical backdrop-scrim + centered-panel shell already named in
`confirmed-versions.md`: modern `Button@0.0.45` trigger, `Classic/Button@2.2.0` full-bleed
transparent scrim (`RGBA(11,18,32,0.45)` in every entry, dismissing via
`UpdateContext({ varShowX: false })` — except Progress Modal's scrim, whose `OnSelect` is a
deliberate `=false` no-op since that modal isn't meant to be dismissible by tapping out), and a
self-sizing `GroupContainer@1.5.0` panel (`Height: =<lastControl>.Y + <lastControl>.Height + 24`,
centered via `(Parent.Width/Height - Self.Width/Height) / 2`). `GroupContainer` is exclusively
1.5.0 in this batch — no 1.3.0/1.4.0 fragmentation here. Every modal correctly uses
`UpdateContext`-based context variables (`varShowX`), never `Set()`/globals — the cleanest batch so
far on that front.

Two small "modern where available" exceptions worth noting: Success Modal's check badge uses
`Classic/Icon@2.5.0` (`Icon.CheckBadge`) instead of the inline-SVG-`Image` technique every other
badge in this batch uses; Info Modal's clickable "release notes" link uses classic `Label@2.5.1`
instead of modern `Text@0.0.51` (plausibly because modern Text can't fire `OnSelect`/`HoverColor`
the way classic Label can — unverified). Also: despite every description claiming "Light and dark,"
only a dark palette is actually present in the captured YAML for any of the 14 modals — no
`If(varDarkMode, ...)` branching anywhere. Confirm with a real paste whether a light variant exists
separately before assuming these are theme-complete.

### Gallery batch (7 entries)

Two entries (Gallery Carousel, Announcement Bar Carousel) aren't `Gallery` controls at all — they're
`Timer`-driven auto-advance carousels built from `GroupContainer`/`Switch()`, and they're the only
two entries in this file using classic controls (`Classic/Button@2.2.0`, `Classic/Icon@2.5.0`,
`Label@2.5.1`) — the other five (List/Card Grid/Card List/Data Table/Sortable Data Table) correctly
use modern `Button@0.0.45`/`Text@0.0.51`. The five real-Gallery entries all use the variant string
**`BrowseLayout_Vertical_TwoTextOneImageVariant_ver5.0`** — note the extra `Vertical_` segment
versus the shorter `..._TwoTextOneImageVariant_ver5.0` already on file from the sidebar-shell batch;
needs reconciling as either the same variant loosely described before, or a genuinely distinct 4th
Gallery variant string. Data Table / Sortable Data Table duplicate their `Filter(...)` predicate in
two places (a hidden helper label plus the gallery's own `Items`) and hardcode page size (`5`) in
several places each — a maintenance risk if either library gets used as a real generation template.
Naming mismatch again: the two carousels' `Set()`-created state uses misleading `var`-prefixes
(`varCarouselIndex`, `varAnnouncementIndex`), while the five Gallery-based entries correctly use
`gbl`-prefixes for their own `Set()`-created state (`gblTablePage`, `gblSortTableSort`, etc.).

### Dropdown batch (8 entries)

New control version: **`TextInput@0.0.52`** (Searchable Lookup, People Picker) — not the confirmed
`TextInput@0.0.54` baseline. Despite the file being "Dropdown Components," **no entry uses a native
`DropDown` control** — every menu is hand-built from Button+GroupContainer. "Modern where available"
is violated identically to the Sidebars/Navigation batches: `Classic/Icon@2.5.0` for every chevron,
`Classic/Button@2.2.0` for the six menus' full-screen scrim (the two search/picker entries use a
modern `Button@0.0.45` overlay instead, so the classic-scrim choice isn't universal within this
file). The promised SVG-keyframe chevron-rotation pattern is **absent** — chevrons swap between two
static Classic/Icon glyphs, no CSS animation. Dead plumbing found: Searchable Lookup and People
Picker both set a `varXAnimTrigger` timestamp variable that is never read anywhere in either entry —
likely vestigial from a cut animated-control paste. Both of those two entries also use
`var`-prefixed names for `Set()`-created globals (same naming/scope mismatch as elsewhere), while
the six menu entries correctly use `UpdateContext`. Searchable Lookup's search box has a
formula-bound `Value` (`=If(!IsBlank(varLookupSelected), varLookupSelected.Title, "")`) on a
`TextInput` a user is expected to type into — a known Power Apps footgun (typed input can be
overwritten by the formula recalculating); People Picker avoids this by keeping `Value` static and
overlaying a separate selected-chip control instead. "User Profile Dropdown" and "Profile Menu" are
near-duplicate content with different trigger styling — may be redundant for generation purposes.

### Drawer batch (6 entries)

Cleanest batch version-wise: only `GroupContainer@1.5.0` (no fragmentation), and it's the only batch
in this drip that uses **zero** Icon control of either kind — every icon is an inline SVG `Image`.
Confirms the responsive corner-radius pattern (`If(Self.Width >= Parent.Width, 0, 16)` on the
hinge-side corners) on all 4 right-side panels (Detail, Filter, Comments, Form Drawer); the two
bottom-anchored sheets (Action Sheet, Bottom Sheet) skip it since they're always full-width by
design. All 6 correctly use `UpdateContext` context variables, no `gbl`/`Set()` globals. Worth
knowing before using these as a real generation template: most primary/secondary action buttons
(Detail/Filter/Bottom Sheet/Form Drawer's Save/Apply/Reject/Approve) only dismiss the panel — they
don't `Patch`/`SubmitForm`/`Collect` anything. The two exceptions that ARE functionally real: Filter
Drawer's Reset (clears the actual filter collections) and Comments Drawer's Send (appends to
`colDrawerComments`).

### Card batch (10 entries, not 6 — 4 more follow Inspection Card)

Fully modern — zero classic controls anywhere in this batch, the only "Large Drip" file where the
"modern where available" claim holds without exception. `GroupContainer@1.4.0` reappears as the root
container specifically in the two modal-shaped entries (Dynamic Form Card, Modern Form — both use
`DropShadow.Regular` like a floating dialog, vs. `DropShadow.None` on all 8 true "card" entries); no
1.3.0 in this batch, no 4th version. `lblTitle`/`btnCancel` control names are reused verbatim
between Dynamic Form Card and Modern Form (same scaffold, copy-pasted). No `Set()`/`UpdateContext`
state at all in 9 of 10 entries (static mock cards, `OnSelect: =false` placeholders) — Contact Card
is the exception with real `Launch("mailto:...")`/`Launch("tel:...")` calls, and Dynamic Form Card
is the exception with a real `colFormValues` collection driven by a `Gallery` whose `Items` is an
inline `Table()` of field definitions (the one data-driven-schema pattern in this batch). Recurring
visual idioms worth reusing elsewhere: the tinted-pill status/priority badge, the tinted-circle
initials avatar (including a 3-avatar overlap-stack via manual X offsets in Task Card), the
dark-fill metric/stat tile, and a clamped-percentage `GroupContainer`-track progress bar
(`Parent.Width * Min(100, Max(0, pct)) / 100`) reused verbatim across Task/Timesheet/Inspection/
Project. "Modern Form" and "Dynamic Form Card" are really modal/form components mislabeled as
"Card" in the source file — cross-reference if organizing by function rather than by source file.

### Data Display batch (7 entries — fully read, no pagination needed)

New named pattern for `confirmed-versions.md`: **shimmer/skeleton loading placeholders** — a hidden
`Timer@2.1.0` (`AutoStart, Repeat, Visible: false`) whose `.Value`/`.Duration` feed a
`Sin(Pi() * Timer.Value / Timer.Duration)` expression directly into a `GroupContainer.Fill`'s alpha
channel (`RGBA(55,65,81, 0.35 + 0.45 * Sin(...))`), producing a pulsing opacity effect with no SVG
or CSS involved — used identically across Skeleton Card, Skeleton List, and Skeleton Text. KPI
Spotlight Carousel is a third distinct `Timer`-driven auto-rotate implementation in this drip
(alongside the Gallery batch's two) — `Classic/Button@2.2.0` dot indicators and
`Classic/Icon@2.5.0` chevrons here, contradicting "modern where available" the same way the
Gallery batch's two carousels did, while KPI Tile/Bar Chart/Empty State all use classic `Label@2.5.1`
throughout (this whole file predates or simply doesn't follow the modern-controls convention seen
in Modals/Drawers/Cards). `GroupContainer@1.3.0` appears in KPI Tile, Bar Chart's bar/track, and
Empty State — consistent with its already-known avatars/calendars fragmentation, no new version.
Bar Chart's `Gallery@2.15.0` uses the **`BrowseLayout_Flexible_SocialFeed_ver5.0`** variant already
flagged once before elsewhere in this library — now confirmed seen at least twice.

**Comments stripped and preserved** (all three had bare `#` YAML-structural comments that would
break Studio's parser — stripped from the saved files, preserved here):
- **KPI Tile**: `# Bind it to real data by replacing the Text formulas, for example
  Text(Sum(Orders, Total), "[$-en-US]$#,###") on lblKpiValue`
- **Bar Chart**: `# Swap the static Table for your own data, keeping the Label and Value column
  names: Items: =AddColumns(GroupBy(Orders, "Day", "ByDay"), "Label", Day, "Value",
  CountRows(ByDay))` — followed by a second comment explaining that a gallery can't read its own
  `AllItems` from inside its template, so a live bar-width divisor needs the source's max value
  computed outside the gallery (e.g. a hidden label: `lblBarMax.Text: =Max(YourSource,
  YourValueColumn)`, then `conBar.Width: =Min(ThisItem.Value / Value(lblBarMax.Text), 1) * 216`) —
  the saved file keeps the hardcoded `/75` divisor, this is how to make it live.
- **Empty State**: `# Visible is =true so this pastes cleanly and you can see it. Wire it up by
  putting your gallery's name in Settings, or by editing Visible directly, for example
  =IsEmpty(galOrders.AllItems) or =IsEmpty(Filter(Orders, Status = "Open")).`
