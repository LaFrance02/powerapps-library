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
  real paste. Don't assume it's required or safe to omit until tested.
- `Screens:` can appear as the top-level key of a captured example (a full screen definition:
  `Screens: / <ScreenName>: / Properties: / Children:`) rather than the usual flat `- control:`
  children list meant to paste into an existing screen. These are structurally different pastes —
  a full `Screens:` block creates/replaces an entire screen (and its `OnVisible`), while a flat
  children list only adds controls to whatever screen is already open in Tree View. Check which
  shape an example file has before pasting it, they are not interchangeable.

## Workflow rule (not syntax, but load-bearing)

Always deliver the **complete corrected file**, never an isolated snippet to "insert." Matt works
by deleting the whole screen/component in Studio's Tree View and pasting the replacement over it.
