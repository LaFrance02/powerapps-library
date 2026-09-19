# The Scan Pattern

Home-grown barcode/serial-number scan handling. Confirmed working across the Transfer Log app's
pickup, delivery, and component scanners. No Power_Libs equivalent exists — don't search the
library for a replacement.

## Why it exists

`TextInput` only updates its bound value on blur, which is too late for a handheld scanner firing
Enter/Tab after each scan. A live-typing surface that updates continuously is needed instead, plus
a way to isolate just the newest scan from a field that keeps accumulating and can't be cleared
programmatically mid-session.

## Mechanism

1. Use a `ComboBox` as the live-typing surface (not `TextInput`), because its `SearchText`
   property updates continuously as the scanner (or a human) types/pastes into it.
2. Run a repeating `Timer` in polling mode at a 200ms interval, checking `SearchText` on every
   tick.
3. Maintain a "baseline" variable capturing the last-processed value of `SearchText`. On each
   tick, diff the current `SearchText` against the baseline — the difference (typically a suffix)
   is the newest scan. Extract it, process it, then update the baseline to the current full value.
   This works around `SearchText` being effectively append-only / not programmatically clearable.
4. Scanner runs in **manual trigger mode**, not continuous scan — a deliberate choice, not a
   limitation to fix.
5. Reset both the ComboBox's underlying value and the baseline variable in every place this
   pattern's popout/control can be opened — Transfer Log had a bug from resetting it in only some
   of the three places the "Look Up SN Info" popout opens from.

## Known open question (as of last session)

A report that "Look Up SN Info" search was broken had a leading hypothesis: the scanner's Enter
keystroke was triggering the lookup button before the full barcode finished being captured. A
200ms debounce conversion may have fixed this — needs confirmation via keyboard-only entry testing
before treating it as resolved.

## TODO

The literal confirmed YAML (ComboBox settings, Timer settings, the exact diff/extraction formula)
was never captured verbatim into this repo — only the procedure above. Next time this pattern is
touched, paste the current working YAML here.
