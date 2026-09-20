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
  layout approach.
- Inside AutoLayout containers, set `FillPortions: =0` explicitly on any child that must not
  stretch.
- Inside gallery templates: formula-based X position (e.g. `(Parent.Width - Self.Width) - 20`)
  works; a literal integer X silently resets to 0.
- `Parent.TemplateWidth` and other gallery-computed widths are unreliable inside PCF-based
  gallery templates.
- `Icons` on `cmpSidebar` must never be set to a blank value — doing so overrides the default icon
  table and breaks all icon rendering.

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
  `PressedFill`) — same defect class, same "preserve as-is, don't silently fix" treatment.
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

## Workflow rule (not syntax, but load-bearing)

Always deliver the **complete corrected file**, never an isolated snippet to "insert." Matt works
by deleting the whole screen/component in Studio's Tree View and pasting the replacement over it.
