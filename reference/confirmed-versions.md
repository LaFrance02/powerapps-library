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
| `Gallery` variant | `BrowseLayout_Vertical_TwoTextOneImageVariant_ver5.0` | Confirmed baseline uses `..._pcfCore` for the same `Gallery@2.15.0` version — two different variant strings for one control version. Watch for a variant-mismatch error if this gets pasted. |
| `Classic/Button` | 2.2.0 | Seen identically across the animation batch and the entire button/badge batch — this specific version looks like Power_Libs' standard for any button that needs custom Hover/Pressed states or a hit-target overlay over a custom-drawn shape (see note below). |
| `Classic/Icon` | 2.5.0 | Seen in the animation batch (Success Check, Progress Circle) and once in the button batch (Split Button's chevron). Contradicts the modern-controls rule below — Icon has a modern successor — but Power_Libs hasn't used it once across ~20 examples. Worth testing the modern Icon control directly rather than assuming Power_Libs' choice is representative. |
| `GroupContainer` | 1.3.0 | **Differs from the 1.5.0 cross-project baseline.** Seen in the three avatar components (User Avatar, User Chip, Avatar Group) *and now also* both calendar screens (Calendar, Calendar with Header) — no longer a one-off, this is a recurring second version. Don't mix 1.3.0 and 1.5.0 `GroupContainer` instances in one screen without checking they're actually compatible; re-verify which version Studio actually offers before pasting. |
| `GroupContainer` | 1.4.0 | **A third distinct version**, seen only in the Time Picker component (`conSelectedTime`, `conDropdownHoursSub`/`conDropdownHours` and its Minutes/Seconds twins). So across the library so far: 1.5.0 (baseline + sidebar shell + buttons/badges), 1.3.0 (avatars + calendars), 1.4.0 (time picker) — three different `GroupContainer` versions from what's presumably the same PowerLibs source. Treat the version number as per-example, not global, until proven otherwise — always check what's on the specific line you're about to paste rather than assuming it matches an earlier confirmed version. |
| `Circle` | 2.3.0 | New control, not seen before this batch (Calendar's selected-day/today-dot indicators, Calendar with Header's selected-day/today-ring/event-dot indicators). Shares its version number with the already-confirmed `Rectangle@2.3.0` from Cryo — plausibly the same control family/release wave, unconfirmed. |

**Recurring architectural pattern worth naming:** across the button batch, most custom-shaped buttons (icon+label combos, pill shapes, split buttons) are built as a `GroupContainer` + `Image`/`Text` for the visual, with a fully transparent `Classic/Button@2.2.0` layered on top purely as the tap target (`Fill`/`Color`/`BorderColor` all `RGBA(0,0,0,0)`, real styling lives in the container). Plain single-purpose buttons (Primary, Outline, Action Bar's two buttons, Raised) skip this and use bare modern `Button@0.0.45` directly. So "modern where available" in practice means: modern `Button` for anything a plain button can do, classic `Button` only as an invisible overlay when the visual needs a shape modern `Button` can't produce alone. The four bare `Classic/Button@2.2.0` **badge** components (Simple/Border/Pills/Outlined Pills Badge) are a different case — there the classic button *is* the visible badge, styled entirely through `Self.Color`/`Self.BorderColor` references so one control instance is fully parameterized (set `Color`, `BorderColor`, `Text`, `Width` and the Hover/Pressed states follow automatically). That self-referencing pattern is worth reusing elsewhere.

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
