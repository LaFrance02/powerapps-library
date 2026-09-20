# Confirmed control versions

Paste-tested against real Power Apps Studio errors, not Power_Libs suggestions or documentation
defaults. Each entry is tagged with the project it was confirmed in and when. **Studio's default
control versions drift over time** — treat every entry here as "last known good," and re-verify
against a fresh paste before trusting it in a new environment or after a long gap.

## Classic vs. modern — this is not a binary choice

Corrected 2026-09-19: an earlier version of the paired skill said to default to Power_Libs'
*classic* YAML mode because "every confirmed version on file is classic-style." That was wrong.
Looking at the baseline below, `Button@0.0.45`, `TextInput@0.0.54`, and `ComboBox@0.0.51` are
already **modern** (Fluent) controls — no `Classic/` prefix, `0.0.x` versioning is the tell.
`GroupContainer@1.5.0`, `Gallery@2.15.0`, `Label@2.5.1`, `Rectangle@2.3.0`, and `Timer@2.1.0` are
classic — but not by choice. Per Microsoft's own current guidance (Feb 2026,
[Overview of modern controls](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/overview-modern-controls)),
**Image, Gallery, GroupContainer, Timer, and Rectangle have no modern version at all yet** — classic
is the only option for those, not a preference. Meanwhile Button, Text (the modern successor to
Label), TextInput, ComboBox, Dropdown, Checkbox, Toggle, Slider, Radio, DatePicker, TabList, Icon,
Avatar, Spinner, Link, InfoButton, and Form all have modern versions available, and Microsoft
explicitly recommends modern for new work (better accessibility, performance, and active
investment — classic is legacy, still supported, not going anywhere immediate, but not where
Microsoft is putting effort).

**The actual rule:** use modern for any control family that has one; use classic only for the
handful that don't yet. Transfer Log and Cryo already do this correctly without it being a
deliberate decision at the time — don't "fix" their existing `Label@2.5.1` usage, it's
paste-tested and working, but new text elements in those apps or in any new app going forward
should default to `Text` (modern) instead of `Label`. There is no scenario where deliberately
picking pure classic is the better choice going forward; the only real classic-vs-modern decision
left is per control family, and it's already made by which families have a modern version at all.

When Power_Libs (or anything else) suggests a version or property that conflicts with an entry
here, this file wins. Power_Libs is for coverage and inspiration, not ground truth on versions.

## Cross-project baseline

Confirmed in **Transfer Log** (Frederick site 6433, Dataverse for Teams) as of mid-2026:

| Control | Version | Notes |
|---|---|---|
| `GroupContainer` | 1.5.0 | Must stay consistent within a single component file. |
| `TextInput` | 0.0.54 | Use `Placeholder`, not `HintText` or `Default`. |
| `Button` | 0.0.45 | Use `Appearance: ButtonAppearance.Primary` / `.Outline`. `Fill`/`Color` are invalid → PA2108. |
| `ComboBox` | 0.0.51 | Use `InputTextPlaceholder`, not `HintText`. |
| `Timer` | 2.1.0 | |
| `Gallery` | 2.15.0 | `BrowseLayout_Vertical_TwoTextOneImageVariant_pcfCore` variant confirmed; bare `Variant: Vertical` unverified. |
| `Label` | 2.5.1 | |

Confirmed in **Cryo Dewar Tracking Suite** (Dataverse, full) as of mid-2026:

| Control | Version | Notes |
|---|---|---|
| `Rectangle` | 2.3.0 | No corner-radius support — `BorderRadius`, `RadiusTopLeft`, etc. all → PA2108. |
| `Label` | 2.5.1 | Matches Transfer Log. |

## Seen in examples, not yet paste-tested

Controls that showed up in a PowerLibs example (`examples/powerlibs-collapsible-sidebar-shell.yaml`)
but have never been confirmed against a real Matt Studio paste. Do not treat these as ground truth
— they're here so a future paste attempt has a specific thing to verify, not a surprise:

| Control | Version | Note |
|---|---|---|
| `Text` | 0.0.51 | Not the same control as the confirmed `Label@2.5.1` — unclear if it's a newer replacement or a parallel modern control. Verify both still work if an app mixes them. Now seen consistently across the sidebar shell and the whole button/badge batch — looks like Power_Libs' standard modern text control, not a one-off. |
| `Image` | 2.2.3 | No prior confirmed entry for this control at all. Now seen consistently across the sidebar shell, animation batch, and button/badge batch — looks like Power_Libs' standard classic image control. |
| `Gallery` variant | `BrowseLayout_Vertical_TwoTextOneImageVariant_ver5.0` | Confirmed baseline uses `..._pcfCore` for the same `Gallery@2.15.0` version — two different variant strings for one control version. Now also confirmed (same exact string) across the whole Gallery batch's 5 real-Gallery entries (List Gallery, Card Grid, Card List, Data Table, Sortable Data Table). Watch for a variant-mismatch error if this gets pasted. |
| `Gallery` variant | `BrowseLayout_Flexible_SocialFeed_ver5.0` | A third distinct variant string for `Gallery@2.15.0`, seen in the Data Display batch's Bar Chart entry (`galBarChart`) — a gallery used to lay out chart bars, not a typical list/feed. Not yet seen anywhere else. |
| `Classic/Button` | 2.2.0 | Seen identically across the animation batch and the entire button/badge batch — this specific version looks like Power_Libs' standard for any button that needs custom Hover/Pressed states or a hit-target overlay over a custom-drawn shape (see note below). |
| `Classic/Icon` | 2.5.0 | Seen in the animation batch (Success Check, Progress Circle) and once in the button batch (Split Button's chevron). Contradicts the modern-controls rule below — Icon has a modern successor — but Power_Libs hasn't used it once across ~20 examples. Worth testing the modern Icon control directly rather than assuming Power_Libs' choice is representative. |
| `GroupContainer` | 1.3.0 | **Differs from the 1.5.0 cross-project baseline.** Seen in the three avatar components (User Avatar, User Chip, Avatar Group) *and now also* both calendar screens (Calendar, Calendar with Header) — no longer a one-off, this is a recurring second version. Don't mix 1.3.0 and 1.5.0 `GroupContainer` instances in one screen without checking they're actually compatible; re-verify which version Studio actually offers before pasting. |
| `GroupContainer` | 1.4.0 | **A third distinct version**, seen only in the Time Picker component (`conSelectedTime`, `conDropdownHoursSub`/`conDropdownHours` and its Minutes/Seconds twins). So across the library so far: 1.5.0 (baseline + sidebar shell + buttons/badges), 1.3.0 (avatars + calendars), 1.4.0 (time picker) — three different `GroupContainer` versions from what's presumably the same PowerLibs source. Treat the version number as per-example, not global, until proven otherwise — always check what's on the specific line you're about to paste rather than assuming it matches an earlier confirmed version. |
| `Circle` | 2.3.0 | New control, not seen before this batch (Calendar's selected-day/today-dot indicators, Calendar with Header's selected-day/today-ring/event-dot indicators). Shares its version number with the already-confirmed `Rectangle@2.3.0` from Cryo — plausibly the same control family/release wave, unconfirmed. |
| `DropDown` | 0.0.45 | Modern control, seen in the Drawer and Card batches (Filter Drawer's owner picker, Form Drawer/Modern Form's field pickers). Despite an entire "Dropdown Components" source file existing in the library, **no entry in that file actually uses this control** — every dropdown/menu there is hand-built from Button+GroupContainer instead. |
| `DatePicker` | 0.0.46 | Modern control, seen in the Drawer and Card batches (Filter Drawer's date-range fields, Form Drawer/Modern Form's date fields). |
| `TextInput` | 0.0.52 | **Differs from the confirmed 0.0.54 baseline** — seen in the Dropdown batch (Searchable Lookup, People Picker). Not yet reconciled against 0.0.54; treat as a second, unconfirmed TextInput version until checked. |
| `Classic/TextInput` | 2.3.2 | New — classic-family TextInput, seen once (Advanced Sidebar's `cmpSidebar` search box, `txtNavSearch`). Contradicts the modern-controls rule (TextInput has a modern option) but is Power_Libs' own choice in that component, not something I introduced. |
| `GroupContainer` | 1.4.0 | Now also confirmed as a root container in the Card batch (Dynamic Form Card, Modern Form — both modal-shaped entries, `DropShadow.Regular`) and throughout most of the Sidebars/Navigation batch (Sidebar Wide, Narrow Sidebar, Collapsible Sidebar, Sidebar with Navbar, Dropdown Sidebar, Glass Floating Sidebar, Navigation Bar, Mega Menu Navbar, Minimal Mega Menu Navbar, NavBar with Scrollable Content) — this is now the single most common version across the whole library, not a rare third option. Updated tally across all examples so far: 1.5.0 (baseline + buttons/badges + sidebar shell + most Modal/Gallery/Dropdown/Drawer/8-of-10-Card entries), 1.3.0 (avatars + both calendars + KPI Tile + Bar Chart's bar/track + Empty State), 1.4.0 (Time Picker + most of Sidebars/Navigation + the 2 modal-shaped Card entries). Still no 4th distinct version seen. |

**"Another big example drip" batch (2026-09-19) — new controls/versions:**

| Control | Version | Note |
|---|---|---|
| `Classic/DropDown` | 2.3.1 | New, seen once (Basic Approvals App's Type field, `arqDdType`). First distinct DropDown version other than the already-confirmed modern `DropDown@0.0.45`. |
| `AddMedia` | 2.2.1 | New control, Photo Upload's picker (Upload & Signature batch). |
| `Attachments` | 2.3.0 | New control, all 4 Document Upload variants (Upload & Signature batch) — identical version across all four. |
| `PenInput` | 2.3.0 | New control, Signature Pad (Upload & Signature batch), cleared via `Reset()`. |
| `Rating` | (bare, no version) | New, unversioned control — Input Field batch (Rating, Rating Compact, Rating Feedback Card). No version number to fall back on if a paste fails. |
| `Slider` | (bare, no version) | New, unversioned control — Input Field batch (Slider, Slider with Value Bubble, Slider Minimal). Same caveat as `Rating`. |
| `GroupContainer` | 1.4.0, `Variant: AutoLayout` | New layout variant, seen once ("Toast Notification" entry's `conToast`) with `LayoutAlignItems`/`LayoutDirection`/`LayoutGap`/`PaddingX` properties — every other `GroupContainer` in the library so far uses `Variant: ManualLayout`. |
| `Gallery` variant | `BrowseLayout_Flexible_SocialFeed_ver5.0` | Now confirmed a third time (Input Field batch's Radio Group and Checkbox Group), on top of the two prior sightings (Data Display's Bar Chart) — no longer a one-off pairing with `Gallery@2.15.0`. |

**New architectural patterns from this batch:**

- **Timer-driven X-position slide animation** ("Toast Notification" entry): `conToast.X` computed
  live from a running `Timer@2.1.0`'s `.Value` (e.g. `Max(App.Width, App.MinScreenWidth) -
  conToast.Width * timerAnimation.Value/300 - 20`), interpolating the container between off-screen
  and resting position as the timer runs. Distinct from the SVG-`<animate>`-keyframe approach used
  everywhere else in the library — no SVG involved at all, pure numeric position formula.
- **Live shrinking progress bar keyed off a countdown Timer** ("Notification with Timer"): `Width:
  =If(..., (1 - (AutoClose.Value / AutoClose.Duration)) * Parent.Width, 0)` — a bar that visually
  empties as an auto-close timer counts down.
- **Per-row `Timer` inside a `Gallery`** ("Queue Notifications"): a collection (`colNotifications`)
  rendered through `Gallery@2.15.0`, with each row/template instantiating its own independent
  `Timer@2.1.0` (`AutoStart`, its own `Duration`) whose `OnTimerEnd` does `Remove(colNotifications,
  ThisItem)`. Because the Timer lives inside the gallery template, each row gets its own countdown —
  a genuine multi-instance, independently-timed toast queue, not a single shared timer.

**Project Management / Inventory Dashboard / Layouts batch (2026-09-19) — new controls/versions:**

| Control | Version | Note |
|---|---|---|
| `Classic/DatePicker` | 2.6.0 | New, Basic Project Management App's New Project modal (date fields). Differs from the already-confirmed modern `DatePicker@0.0.46`. |
| `TextInput` | 0.0.54 | Matches the cross-project baseline exactly (Basic Project Management App's nav search box) — first re-confirmation of the 0.0.54 baseline version inside a PowerLibs example rather than just Transfer Log. |
| `ModernText` | 1.0.0 | New control, seen in Dashboard Layout and throughout the Inventory Dashboard app — looks like a newer/alternate modern text control distinct from both `Label@2.5.1` and `Text@0.0.51`. Three different "text" controls now exist across the library (`Label@2.5.1`, `Text@0.0.51`, `ModernText@1.0.0`) — unclear which is current/recommended, worth checking Microsoft's docs before standardizing on one. |
| `ModernButton` | 1.0.0 | New control, Inventory Dashboard's Export button (`Appearance: ButtonAppearance.Outline`, icon support). A second modern button family alongside the already-confirmed `Button@0.0.45`. |
| `HtmlViewer` | 2.1.0 | New control, used once in Inventory Dashboard as a blur/backdrop layer behind the sidebar drawer — not seen anywhere else in the library. |

**A real, complete .msapp reference app** ("DocRouterFree," supplied 2026-09-19, not yet merged into
this repo pending Matt's decision) contains real `ComponentDefinitions:` source for 20 named
components, several of which the Inventory Dashboard example above only *references* by name:
`cmpKPI`, `cmpBarList`, `cmpMyTable`, `cmpBottomNavigation`, `cmpSidebar`, `Badge`,
`cmpFloatingActionButton`, plus 13 more not yet seen anywhere else in this library
(`cmpFileUpload`, `cmpDetFinish`, `cmpDetEditWorkflow`, `cmpSendEmail`, `cmpLoadingSpinner`,
`cmpAccordionList`, `cmpEnhancedDialog`, `cmpStepper`, `cmpProgressRail`, `cmpDetReroute`,
`cmpPieChart`, `cmpBreadcrumbs`, `cmpActivityTimeline`). Its `cmpSidebar.pa.yaml` may be the same
component family as `powerlibs-sidebar-advanced.yaml`'s `cmpSidebar` — worth diffing the two before
deciding whether to replace or supplement the existing one. Data sources are 100% self-contained
sample/static data (`CustomGallerySample`, `ComboBoxSample`, both Lorem-ipsum placeholders) — no
real backend, Dataverse table, or client-specific schema is embedded anywhere in the app, so it's
safe to mine for reference material. Its own Power Apps App Checker run (`AppCheckerResult.sarif`)
flagged 15 issues in the real, complete app: 7× `app-CollectingReadOnlyTable`, 5×
`app-ForAllWithMutation`, 2× `acc-TabIndexShouldBeDefinedForInteractiveControl`, 1×
`app-IndexedAccessViaCopy` — genuine Microsoft-linter-confirmed gotchas from a real app, a
different (and arguably stronger) confirmation source than "pasted cleanly in Studio."

**Recurring architectural pattern worth naming:** across the button batch, most custom-shaped buttons (icon+label combos, pill shapes, split buttons) are built as a `GroupContainer` + `Image`/`Text` for the visual, with a fully transparent `Classic/Button@2.2.0` layered on top purely as the tap target (`Fill`/`Color`/`BorderColor` all `RGBA(0,0,0,0)`, real styling lives in the container). Plain single-purpose buttons (Primary, Outline, Action Bar's two buttons, Raised) skip this and use bare modern `Button@0.0.45` directly. So "modern where available" in practice means: modern `Button` for anything a plain button can do, classic `Button` only as an invisible overlay when the visual needs a shape modern `Button` can't produce alone. The four bare `Classic/Button@2.2.0` **badge** components (Simple/Border/Pills/Outlined Pills Badge) are a different case — there the classic button *is* the visible badge, styled entirely through `Self.Color`/`Self.BorderColor` references so one control instance is fully parameterized (set `Color`, `BorderColor`, `Text`, `Width` and the Hover/Pressed states follow automatically). That self-referencing pattern is worth reusing elsewhere.

**Modal shell pattern (confirmed across all 14 Modal-batch examples, identical every time):** modern `Button@0.0.45` trigger → `Classic/Button@2.2.0` full-bleed transparent scrim (`RGBA(11,18,32,0.45)`, dismisses via `UpdateContext({ varShowX: false })`, unless the modal is meant to be non-dismissible by tap-out, in which case the scrim's `OnSelect` is a deliberate `=false`) → a self-sizing `GroupContainer@1.5.0` panel, always centered (`X: =(Parent.Width - Self.Width)/2`, `Y: =(Parent.Height - Self.Height)/2`), with `Height: =<lastVisibleControl>.Y + <lastVisibleControl>.Height + 24` so the panel never needs a hardcoded height. The same shell (scrim + self-sizing centered panel) also appears, with `Rectangle@2.3.0` instead of `Classic/Button@2.2.0` as the scrim, on the Drawer batch's side-panel/bottom-sheet variants, plus a responsive corner-radius formula on the hinge-side corners of right-anchored drawers: `If(Self.Width >= Parent.Width, 0, 16)` (so the drawer loses its rounding when it goes full-width on a phone). Bottom-anchored sheets skip that responsive-radius formula since they're always full-width by design.

**Shimmer/skeleton loading pattern** (Data Display batch — Skeleton Card/List/Text): a hidden `Timer@2.1.0` (`Visible: false`, `AutoStart`, `Repeat`) whose `.Value`/`.Duration` are fed straight into a `GroupContainer.Fill`'s alpha channel via `Sin(Pi() * Timer.Value / Timer.Duration)` (e.g. `RGBA(55,65,81, 0.35 + 0.45 * Sin(...))`), producing a pulsing-opacity shimmer with no SVG/CSS involved at all — a much simpler mechanism than the SVG-keyframe-replay pattern used elsewhere in the Animation batch.

**`ComponentDefinitions:` — a third top-level YAML shape**, seen in `powerlibs-sidebar-advanced.yaml` (the "Advanced Sidebar" / `cmpSidebar`). Structure: `ComponentDefinitions: → <Name>: → DefinitionType: CanvasComponent, AccessAppScope: true, CustomProperties: {...}, Properties: {...}, Children: [...]`, with `CustomProperties` entries typed `PropertyKind: Input | Output | Event`. This is distinct from both the flat `- control:` children-list shape (everything else in the library except the two full-screen Calendar files) and the full `Screens:` block shape (the two Calendar files) — a real Component definition ready to paste into Studio's Components pane, not a paste-into-existing-screen fragment. `AccessAppScope: true` means the component reads/writes app-scoped variables directly (here: `_cmpNavIsExpanded`, `_cmpNavSelID`, `_cmpNavFooterMenu`, plus collection `colNavExpanded`) rather than only through its own declared custom properties — anything using this component must initialize all of those on the consuming screen's `OnVisible`.

## Patterns with no Power_Libs equivalent

Don't spend a `search_components` call looking for these — confirmed to not exist in the library,
build from scratch:

- **The Scan Pattern** — a `ComboBox` as the live-typing surface (TextInput only updates on blur),
  a repeating debounce timer at 200ms polling `SearchText`, and a baseline-diff extraction
  technique to isolate each new scan from a field that can't be cleared programmatically. Manual
  trigger mode, not continuous scan. See `components/scan-pattern.md` for the full writeup.
- **Pill-style toggles** for binary mode switches (preferred over plain buttons).
- **"Add to a list" pattern** for multi-entity selection (preferred over native multi-select).

## Format for adding a new entry

When a new control version gets confirmed on a new app, add it under a new `## <Project>` heading
with the date, and note here in the baseline section only once it's been confirmed working in a
*second* project — that's what promotes something from "worked once" to "cross-project baseline."
