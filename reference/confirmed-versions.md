# Confirmed control versions

Paste-tested against real Power Apps Studio errors, not Power_Libs suggestions or documentation
defaults. Each entry is tagged with the project it was confirmed in and when. **Studio's default
control versions drift over time** — treat every entry here as "last known good," and re-verify
against a fresh paste before trusting it in a new environment or after a long gap.

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
| `Text` | 0.0.51 | Not the same control as the confirmed `Label@2.5.1` — unclear if it's a newer replacement or a parallel modern control. Verify both still work if an app mixes them. |
| `Image` | 2.2.3 | No prior confirmed entry for this control at all. |
| `Gallery` variant | `BrowseLayout_Vertical_TwoTextOneImageVariant_ver5.0` | Confirmed baseline uses `..._pcfCore` for the same `Gallery@2.15.0` version — two different variant strings for one control version. Watch for a variant-mismatch error if this gets pasted. |

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
