# Components

Matt's own canonical, reusable YAML — captured verbatim from a working paste, never regenerated
from memory or a guess. Each file here is meant to be pasted as-is into a new app as the starting
shell, then left alone.

**Status: seeding in progress.** These were described in past sessions but the literal YAML text
was never captured into a durable file — it lived only in chat history. Next time each one comes
up, paste the current canonical version into the matching file below (replacing the placeholder)
and commit it. After that, it should never need to be asked for again.

| File | What it is | Status |
|---|---|---|
| `sidebar.yaml` | `cmpSidebar` from powerappsui.com (MIT-licensed) — visible at `Width >= 600`, replaced by a Label-based bottom nav below that. `Items` schema uses `Title` (not `Label`) plus ~18 properties (`AccentColor`, `AppName`, `AppNameAccent`, `Expanded`, `ShowFooterMenu`, `ShowHeader`, `ShowSearch`, `ShowToggle`, `ShowUser`, `Theme`, etc.). | Needs Matt's current paste |
| `theme.yaml` | Dark theme: `RGBA(10,17,32,1)` background, `RGBA(21,24,31,1)` card fill, plus light-mode equivalents and the light/dark switch mechanism. | Needs Matt's current paste (colors known, full mechanism not) |
| `toast.yaml` | Toast notification system — `varToastVisible`, `varToastType`, `varToastMessage`, auto-dismissed by `ToastTimer` at 3000ms. | Needs Matt's current paste |
| `scan-pattern.md` | The Scan Pattern — home-grown barcode/SN scan handling, no Power_Libs equivalent. Written up procedurally below since it was documented in enough detail to reconstruct, but the literal confirmed YAML hasn't been captured yet. | Procedure documented; literal YAML still needed |

Design defaults to apply across all of these unless told otherwise: dynamic/responsive layout,
outline/lined icons over filled, pill toggles over buttons for binary switches.
