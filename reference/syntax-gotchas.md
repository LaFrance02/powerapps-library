# Universal YAML / Power Fx syntax rules

These come from the YAML parser and Power Fx language itself, not from a specific control
version — they don't need re-verification per project the way `confirmed-versions.md` does.
Apply all of these on every generation pass, regardless of app.

## YAML structure

- `Screens:` must be the literal first line of the file — no preceding comments or `--`.
- No `#` comments anywhere in the file — they cause parse errors.
- Control names must be globally unique across a multi-screen paste — append the screen name as a
  suffix to guarantee this.
- Component instances use `Control: CanvasComponent` plus `ComponentName: cmpX` — never
  `Control: cmpX`.
- A component instance with a stale hardcoded `Items` override silently shadows component-level
  updates. Use `Properties: {}` to defer to the component's own defaults when that's the intent.
- `ControlTypeId` must match `^([A-Z][a-zA-Z0-9]*/)?[A-Z][a-zA-Z0-9]*(@\d+\.\d+\.\d+)?$` — e.g.
  `Classic/Button@2.2.0` or `Button@0.0.45`.
- Disallowed as a `Control:` value per the official schema: `AppInfo`, `HostControl`, `Screen`,
  `AppTest`, `TestCase`, `TestSuite`.

## Properties and values

- Every property value needs an `=` prefix.
- `RGBA(0,0,0,0)` instead of `Transparent`.
- `Size` instead of `FontSize`.
- `": "` (colon-space) inside an inline formula string → `PA1001 YamlInvalidSyntax`. Use ` - `
  (dash) as a separator in display strings instead, or move the formula to multi-line `|` block
  literal syntax (safe from this issue).

## Power Fx formulas

- `Set()` is disallowed inside `ForAll()`.
- Don't `Patch()` the same Dataverse table a `ForAll` is currently iterating over.
- `Navigate()` cannot take a computed Text value — use a `Switch` mapping to literal, unquoted
  screen names.
- Global Choice comparisons use the choice's own name (`'App.ChoiceName'.Value`), not a
  table-scoped reference.
- Dataverse tables are referenced in **plural** form in Power Fx formulas.

## Layout

- `LayoutOverflowY: Scroll` does not reliably produce visible scrolling — avoid, find another
  layout approach. **Contradiction flagged 2026-09-19**: all 5 files in the Basic Layouts Examples
  batch (Dashboard, Master-Detail, Browse, Form, Mobile-First) use
  `LayoutOverflowY: =LayoutOverflow.Scroll` on their main scrollable `GroupContainer`/`AutoLayout`
  content areas as their primary scrolling mechanism — directly at odds with this documented
  gotcha. Worth a real paste test to see whether AutoLayout containers specifically behave
  differently than whatever context this gotcha was originally confirmed in, before assuming either
  the gotcha or these five examples are correct.
- Inside AutoLayout containers, set `FillPortions: =0` explicitly on any child that must not
  stretch.
- Inside gallery templates: formula-based X position (e.g. `(Parent.Width - Self.Width) - 20`)
  works; a literal integer X silently resets to 0.
- `Parent.TemplateWidth` and other gallery-computed widths are unreliable inside PCF-based
  gallery templates.
- `Icons` on `cmpSidebar` must never be set to a blank value — doing so overrides the default icon
  table and breaks all icon rendering.
- **Repeated inline breakpoint sub-expressions are a real verbosity/maintainability smell, not a
  style choice worth copying.** `powerlibs-app-project-management.yaml` repeats the exact
  sub-expression `If(navRoot.Width < 640, 1, navRoot.Width < 1024, 2, navRoot.Width < 1600, 3, 4)`
  **128 times** inline across `Height`/`Width`/`Size`/`Padding*`/`Visible`/`X`/`Y`/`Switch()`
  formulas, rather than computing the tier once (e.g. into a context variable on `OnVisible` or a
  hidden sensor control's property) and referencing that everywhere. Preserved as-sourced since
  it's still valid Power Fx, but flag this pattern for simplification rather than reproducing it
  verbatim in generated apps.

## Modern control breaking changes (vs. their classic counterparts)

Relevant any time a modern control replaces what used to be classic in a given screen — see
`confirmed-versions.md`'s classic-vs-modern section for which families this applies to.

- Modern controls take **enum values**, not string literals, for properties like alignment or
  appearance — e.g. `Align.Left` instead of `"Start"`. Pasting a classic-style string into a
  modern control's property is a likely source of a new, not-yet-catalogued paste error.
- `FontColor` → `Color`, `FontSize` → `Size` (already reflected above), `BorderRadius` → separate
  `RadiusTopLeft`/`RadiusTopRight`/`RadiusBottomLeft`/`RadiusBottomRight` properties.
- `OnChange` timing shifted on several modern input controls: modern `TextInput` fires on focus-out
  only (not every keystroke like classic); modern `ComboBox` fires on every selection. If a pattern
  depends on continuous typing (the Scan Pattern does, via `SearchText` polling rather than
  `OnChange`), verify it still behaves the same way before assuming a modern swap is safe — the
  Scan Pattern likely isn't affected since it doesn't use `OnChange` at all, but this hasn't been
  re-tested against a modern `ComboBox`.

## New/unverified syntax seen in examples (not yet confirmed)

- A `Group:` property (e.g. `Group: Time Picker`) appears as a sibling of `Control:`/`Properties:`
  on several Time Picker controls — distinct from the `GroupContainer` control type. This looks
  like a Studio Tree View organizational tag (grouping unrelated controls under a label without
  making them a real container/parent), but that's inferred, not confirmed against the schema or a
  real paste. Don't assume it's required or safe to omit until tested. **Update from the Navigation
  batch:** the pattern now looks clearer — `Group:` shows up specifically on a navbar's root
  container plus every dropdown/overlay panel that must sit as a structural *sibling* (not nested
  child) of that navbar so it can render outside the navbar's own clipping bounds, tagging them as
  logically related in Studio's outline despite not being parent/child. Seen with two different
  group-name values (`Group: NavBar`, `Group: MinimalMegaNavBar`) in the Mega Menu Navbar / Minimal
  Mega Menu Navbar examples specifically for this reason — still not confirmed against a real
  paste, but the "just a Tree View label, no runtime effect" theory is looking more solid.
  **Clearest confirmation yet, from the Tooltip batch** ("Another big example drip," 2026-09-19):
  every one of its 5 entries tags its top-level trigger/overlay/bubble siblings with a shared
  `Group:` value (`grpSimpleTooltip`, `grpHelpIconTooltip`, `grpMenuPopover`, `grpDelete`,
  `grpRichPopOver`) — and in every case it's applied only to controls sitting directly on the
  screen root, never to controls nested inside a container's own `Children:` list. This lines up
  exactly with the "ties structural siblings that need to render outside their parent's clip
  bounds" theory. Also seen once in the Toast Notification batch (`Group: grpAnimatedToast`, tying
  together `conToast`/`btnToast`/`timerAnimation`/`timerCloseToast`). Still unconfirmed against a
  real Studio paste, but the pattern (screen-root siblings only, shared label, no nesting) is now
  consistent across four separate source files (Navigation, Tooltip, Toast Notification, plus the
  original Time Picker sighting).
- `Screens:` can appear as the top-level key of a captured example (a full screen definition:
  `Screens: / <ScreenName>: / Properties: / Children:`) rather than the usual flat `- control:`
  children list meant to paste into an existing screen. These are structurally different pastes —
  a full `Screens:` block creates/replaces an entire screen (and its `OnVisible`), while a flat
  children list only adds controls to whatever screen is already open in Tree View. Check which
  shape an example file has before pasting it, they are not interchangeable.
- **A third top-level shape**: `ComponentDefinitions:` (seen in `powerlibs-sidebar-advanced.yaml`,
  the "Advanced Sidebar" `cmpSidebar`) — `ComponentDefinitions: / <ComponentName>: / DefinitionType:
  CanvasComponent, AccessAppScope: true (optional), CustomProperties: {...}, Properties: {...},
  Children: [...]`. This is a real, importable Component definition (Studio's Components → New
  component → Import from code), not a children-list fragment or a screen. `CustomProperties`
  entries are typed via `PropertyKind: Input | Output | Event`. When `AccessAppScope: true` is
  present, the component reads/writes named app-scoped variables directly (bypassing its own
  declared custom properties) — every consuming screen must initialize those variables on
  `OnVisible` or the component starts in an undefined state. None of this is confirmed against a
  real paste yet.
- **Bare `=` (empty formula) as a property value**: seen in `powerlibs-nav-mega-menu.yaml` on four
  controls' `HoverBorderColor`/`PressedBorderColor` (e.g. `HoverBorderColor: =` with nothing
  following). A lone `=` is a reserved YAML 1.1 indicator, so this fails strict `yaml.safe_load`
  (PyYAML) with a constructor error. Unconfirmed whether Power Apps Studio's own (non-standard)
  YAML importer tolerates this or rejects it the same way — don't assume either way without a real
  paste test. If it turns out to be a real defect, the fix is straightforward: fill in the omitted
  value explicitly (e.g. `=RGBA(0,0,0,0)`, matching every other Border/Fill property on the same
  control) rather than leaving the property blank. **A third occurrence** was found in
  `powerlibs-upload-photo.yaml` ("Another big example drip" batch, 2026-09-19): `btnPhotoUploadPicker`
  has four bare-`=` properties (`HoverBorderColor`, `HoverFill`, `PressedBorderColor`,
  `PressedFill`) — same defect class, same "preserve as-is, don't silently fix" treatment. **A
  fourth, and by far the worst, occurrence** was found in `powerlibs-app-inventory-dashboard.yaml`
  (2026-09-19): **10** separate bare-`=` properties across three different referenced components'
  bindings (`IconColor` on the Badge, `OnCardClick`/`CharWidths`/`OnRowSelect`/`OnViewChange` on
  `cmpMyTable`/`cmpKPI`, and `AppNameAccent`/`OnFooterSettings`/`OnHelp`/`OnThemeToggle`/`OnToggle`
  on `cmpSidebar`) — mostly event handlers and a couple of styling properties left genuinely unset
  in the source rather than deliberately blanked. Same treatment: preserved as-is, not fixed.
  **Confidence upgraded to "confirmed genuine Studio export behavior" (2026-09-19):** all four
  occurrences above came from PowerLibs drip text, leaving open the possibility this was an
  authoring/paste-generation quirk specific to PowerLibs rather than something Studio itself does.
  The DocRouterFree `.msapp` — a real Power Apps Studio export, unzipped and extracted directly,
  not drip text — adds **139 more bare-`=` occurrences across 12 of its 29 extracted files**
  (`Home`, `MyTasks`, `AllRequests`, `Details`, `Reports`, `Help`, `cmpKPI`, `cmpBarList`,
  `cmpBottomNavigation`, `cmpBreadcrumbs` [58 alone — worst in the library by far],
  `cmpEnhancedDialog`, `cmpMyTable`). Since this app was never touched by PowerLibs, this confirms
  the bare-`=` pattern is genuine native Power Apps Studio export behavior — Studio itself emits an
  empty formula value for certain unset/default properties on export — not a PowerLibs-specific
  artifact. Continue preserving these as-is when reusing any file that has them; do not "fix" them
  into a filled-in value, since that would no longer match what Studio actually produces.
- **`var`/`gbl` variable-name prefixes do not reliably indicate actual Power Fx scope.** Multiple
  examples across the Navigation, Gallery, and Dropdown batches use a `var`-prefixed name (which,
  by convention elsewhere in this library, signals a screen-local context variable created via
  `UpdateContext()`) for a variable that is actually created via `Set()` — i.e., a real **global**,
  app-wide in scope. Sibling examples solving the identical problem sometimes get this right (a
  `gbl`-prefixed name backing a real `Set()` global) and sometimes don't (a `var`-prefixed name
  backing the same `Set()` call) — see `examples/README.md`'s Navigation/Gallery/Dropdown batch
  notes for the specific file-by-file breakdown. **Do not infer a variable's actual scope from its
  name prefix when generating or reviewing Power Fx — check whether the initializing call is
  `Set()` (global) or `UpdateContext()` (context/local) directly.** **Update from the "Another big
  example drip" batch:** the entire Steppers batch (`varHStep`, `varAnimProg`, `varAnimRunning`,
  `varVStep`, `varCheckCount`, `varTimeStep`) and the entire Speed Dials batch
  (`varHorizontalDialOpen`/`Run`, `varSpeedDialOpen`/`Run`, `varSquareDialOpen`/`Run`,
  `varLabeledDialOpen`/`Run`) are clean, total instances of this mismatch — every single state
  variable in both files is `Set()`-backed with zero `UpdateContext()` calls anywhere. Conversely,
  the **Tabs batch (8 entries) and Basic Approvals App are clean positive counter-examples** — every
  tab-state variable (`varIconTabs`, `varSideTabs`, `varTabBar`, `varCountTabs`, `varChipTabs`,
  `varSegmentedTabs`, `varUnderlineTabs`, `varPillTabs`, each with `*Prev`/`*Run` companions) and
  every Approvals App variable (`varFilter`, `varShowNew`, `varShowDetail`, `varSel`) is genuinely
  `UpdateContext()`-scoped with zero `Set()` calls found — proof this convention CAN be followed
  correctly, it just isn't consistently. Toggles (11 entries) and Tooltips (5 entries) are also
  clean on this front — every state variable in both is `UpdateContext()`-scoped. The Toast
  Notification batch is a third, different variant of the problem: its globals use **no `gbl`
  prefix at all** — `varPowerLibsNotification` is `Set()`-backed despite the `var` name, while
  `ShowHideToast`/`StartTimer` are bare (no prefix) but correctly `UpdateContext()`-scoped.
  **A third variant, from the Inventory Dashboard example (2026-09-19)**: `_cmpNavIsExpanded` and
  `_cmpNavSelID` use an `_cmp`-prefix — which elsewhere signals genuinely component-instance-scoped
  state — for real app-wide `Set()` globals, the same underlying mismatch as `var`/`Set()` just
  with a different prefix family. The same file's `varActiveTab`/`varNavOpen`/`varLoadComplete` are
  the ordinary `var`/`Set()` mismatch. Only `gblRange`/`gblMetric`/`gblAlertFilter`/
  `gblLastRefresh`/`gblNowTick` (all `gbl`-prefixed, all `Set()`-backed) and `locRefreshing` (no
  prefix, `UpdateContext()`-backed) get the naming right in that same file — so a single file can
  mix correct and incorrect scoping conventions freely, don't assume consistency within one file
  either.
  **A distinct, separate naming convention** shows up in the Basic Layouts Examples batch
  (2026-09-19): Master-Detail Layout uses `g`-prefixed names for real `Set()` globals (`gViewMode`,
  `gSelItemID`) and `ctx`-prefixed names for `UpdateContext()` context variables (`ctxSearch`,
  `ctxCategory`, `ctxPanelOpen`) — both used correctly, just a third prefix family (`g`/`ctx`)
  alongside the `gbl`/`var` convention used almost everywhere else in this library. The other four
  Layout files use only `ctx`-prefixed context vars, no globals at all. Bottom line stands
  regardless of which prefix family a given file happens to use: check the actual `Set()` vs.
  `UpdateContext()` call, never infer scope from any prefix.

- **Duplicate/colliding control names across sibling example files, not just within one file.**
  New pattern, distinct from the earlier cross-file `cmpSidebar` duplicate (which was the *same*
  component pasted into two source files by mistake): the three "Favorite Toggle" variants (Heart /
  Star / Bookmark, `powerlibs-toggle-favorite-*.yaml`) are three *intentionally different* examples
  that nonetheless share byte-for-byte identical internal control names (`conFavorite`,
  `imgFavoriteIcon`, `lblFavoriteCount`, `btnFavorite`) and variable names (`varFavorite`,
  `varFavoriteRun`) — they differ only in SVG path/fill color. Pasting more than one variant onto
  the same screen will collide on every one of those names. Preserved as-sourced in all three files
  (no silent renaming) per this library's policy — rename one set of controls before pasting a
  second variant alongside the first on the same screen.

## Accessibility best practice (confirmed from a real shipped app's own version history)

- **Give every interactive control `AccessibleLabel`, `TabIndex: =0`, and
  `FocusedBorderThickness: =0.5`** (not `0`). Confirmed 2026-09-19 by diffing two real revisions of
  the same component: `powerlibs-sidebar-advanced.yaml`'s `cmpSidebar` (earlier) vs.
  `msapp-docrouterfree-component-sidebar.yaml`'s `cmpSidebar` (later, from a real shipped
  `.msapp`) — identical 20 custom properties, but the later version adds `AccessibleLabel="..."`,
  `TabIndex: =0`, and bumps `FocusedBorderThickness` from `=0` to `=0.5` on interactive controls
  throughout. This lines up exactly with a real finding in that app's own
  `AppCheckerResult.sarif` (Microsoft's Power Apps Checker/linter run against the shipped app):
  `acc-TabIndexShouldBeDefinedForInteractiveControl` (2 occurrences remained even in the newer,
  hardened version — so this is a real, still-imperfect fix in production, not a hypothetical).
  When generating new controls or reviewing existing ones for the paired Skill, default to setting
  all three on anything clickable/focusable rather than leaving them at Studio's bare defaults.

## Confirmed by paste test (2026-10-28, Dataverse for Teams scratch app)

- **One version per control type — PA2107 / PA2105.** Pasting a single `GroupContainer@1.3.0` or
  `@1.4.0` alone works: Studio treats it as older than the current `1.5.0` (warning PA2105, "using
  the current version, which may produce errors"). Pasting `1.3.0`, `1.4.0` and `1.5.0` containers
  together in one paste fails with `PA2107: Another instance of control type 'GroupContainer' has
  already been referenced using a different version '1.3.0'. All control instances for the same type
  must currently reference the same version.` Rule for generated YAML: rewrite every
  `GroupContainer@x.y.z` to `@1.5.0` before pasting. The error says "control type", not just
  GroupContainer, so the same likely applies to other controls (e.g. `TextInput` 0.0.52 vs 0.0.54) —
  inferred from the message, not tested. Different controls can mix freely (`Label@2.5.1`,
  `Text@0.0.51`, `ModernText@1.0.0` pasted together cleanly).
- **Bare `=` (empty formula) pastes cleanly.** A `Classic/Button@2.2.0` with `HoverBorderColor: =`,
  `HoverFill: =`, `PressedBorderColor: =`, `PressedFill: =` pasted with no error. This supersedes the
  earlier "unconfirmed whether Studio tolerates this" note: it's only a defect for strict YAML
  parsers (PyYAML), not for Studio. Tested on one control at screen level only — not yet inside a
  `ComponentDefinitions:` paste or on the real msapp files.
- **Named Formulas work.** `nfBrand = RGBA(0, 120, 212, 1);`, `nfIsDesktop = App.Width >= 768;`,
  `nfSpace = If(nfIsDesktop, 16, 8);` entered under App > Formulas were accepted, and `Fill: =nfBrand`
  on a control resolved.

## Workflow rule (not syntax, but load-bearing)

Always deliver the **complete corrected file**, never an isolated snippet to "insert." Matt works
by deleting the whole screen/component in Studio's Tree View and pasting the replacement over it.
