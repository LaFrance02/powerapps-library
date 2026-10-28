# Paste-test runbook — 2026-10-28

Run on the **work computer** (Studio only works there). Get each file via GitHub (private repo
LaFrance02/powerapps-library > examples/<file> > "Copy raw file"). Paste into Tree view's YAML
editor. Record the result in the table at the bottom, then bring it back to a chat so the
findings get promoted into `reference/confirmed-versions.md` / `syntax-gotchas.md`.

Rules for every test: fresh scratch app (same Dataverse for Teams one as before). Paste ONE file,
note the exact error code + line on failure, do not hand-fix before reporting. Delete what you
pasted before the next test unless the step says to keep it.

Already confirmed (do not re-test): single bare `=` on a screen-level Classic/Button; named formulas;
mixed GroupContainer versions in one paste -> PA2107; `LayoutOverflowY: =LayoutOverflow.Scroll`
scrolls on AutoLayout GroupContainer@1.5.0.

## Test A — bare `=` inside real Studio-export ComponentDefinitions

Open question from the last session: does bare `=` survive inside `ComponentDefinitions:`, and as a
custom-property `Default: =` and an event `OnSelect: =`? All three files below are self-contained
(no `nf*` names, no other components), so a failure is attributable to the bare `=` or something
else in the file, not a missing dependency. Run in this order, stop at first failure and report it.

| Step | File | Bare `=` | Why this one |
|---|---|---|---|
| A1 | examples/msapp-docrouterfree-component-bottom-navigation.yaml | 2 | Smallest. Line 53 is a custom-property `Default: =`; line 102 is a control `OnSelect: =`. Isolates both contexts. |
| A2 | examples/msapp-docrouterfree-component-kpi.yaml | 10 | Mid-size; Gallery + ModernText + Classic/Button. |
| A3 | examples/msapp-docrouterfree-component-breadcrumbs.yaml | 58 | Stress case, worst in the library. Only run if A1 and A2 pass. |

Predicted: all pass (the real msapp exported them this way). Also watch for a PA2105 version warning;
all three use GroupContainer@1.5.0, Classic/Button@2.2.0, Image@2.2.3, Gallery@2.15.0, Label@2.5.1,
ModernText@1.0.0 — all already confirmed, so any version error would be new information.
After pasting, open the component and confirm the bare-`=` properties show empty, not an error badge.

Not in this runbook (needs the full app): the 6 screens with bare `=` (Home, MyTasks, AllRequests,
Details, Reports, Help). They reference `nf*` formulas and ~8 components, so they only paste cleanly
after the whole DocRouterFree set. Do that as Test D if A passes.

## Test B — msapp cmpSidebar

File: examples/msapp-docrouterfree-component-sidebar.yaml (1225 lines, 0 bare `=`).

Setup, before pasting the component: App > Formulas, add these two, which the component reads:

```
nfUserEmail = Lower(User().Email);
nfUserName = Proper(User().FullName);
```

Then paste the component file as-is. Do NOT also paste examples/powerlibs-sidebar-advanced.yaml: it
defines the same `cmpSidebar` name (older, un-hardened revision).

Then paste this host screen to see it render. Everything here is derived from how the msapp's Reports
screen calls it; the `Icon` names (Home, Settings) are the ones that screen uses, but the component's
default `Icons` table was not checked for them, so if icons are blank, supply `Icons` (the msapp passes
`nfSidebarIcons`) before calling it a failure.

```
Screens:
  scrSidebarTest:
    Properties:
      OnVisible: |-
        =Set(_cmpNavIsExpanded, true);
        Set(_cmpNavSelID, 1);
        ClearCollect(colNavExpanded, {ID: 1})
    Children:
      - cmpSidebarTest:
          Control: CanvasComponent
          ComponentName: cmpSidebar
          Properties:
            Height: =Parent.Height
            Items: |-
              =Table(
                  { ID: 1, Title: "Home", Icon: "Home", Letter: "", Badge: 0, BadgeColor: RGBA(220, 38, 38, 1), BadgeDot: false, IsSection: false, ParentID: -1, Visible: true },
                  { ID: 2, Title: "Settings", Icon: "Settings", Letter: "", Badge: 3, BadgeColor: RGBA(220, 38, 38, 1), BadgeDot: false, IsSection: false, ParentID: -1, Visible: true }
              )
```

Things to record: any PA error on the component paste; any on the host paste; whether it renders;
whether expand/collapse and selection work in play mode; the `Classic/TextInput@2.3.2` search box
(version confirmed once before in the older copy, now in a second file); and whether the
`AccessibleLabel` / `TabIndex` / `FocusedBorderThickness: =0.5` properties are accepted. A
`Set(gNavExpanded...)`/`Set(gTheme...)` only appears in descriptions, not in formulas — not a dependency.

## Test C — five layout skeletons

Files (each is a standalone `Screens:` block, distinct screen names, no `#` comments, no bare `=`):

| Step | File | Screen | Controls |
|---|---|---|---|
| C1 | examples/powerlibs-layout-mobile.yaml | scrMobile | GroupContainer@1.5.0, Text@0.0.51 |
| C2 | examples/powerlibs-layout-browse.yaml | scrBrowse | + Rectangle@2.3.0 |
| C3 | examples/powerlibs-layout-form.yaml | scrForm | + `LayoutWrap` |
| C4 | examples/powerlibs-layout-master-detail.yaml | scrMasterDetail | + side-by-side 1:2 panels |
| C5 | examples/powerlibs-layout-dashboard.yaml | scrDashboard | **ModernText@1.0.0** (the only one) + `LayoutWrap`, `LayoutMaxHeight` |

Paste each one separately first (this tells you which file fails), then, only if all five pass,
paste C1 and C5 into the same app to re-confirm that Text@0.0.51 and ModernText@1.0.0 coexist.
All five use GroupContainer@1.5.0 only, so PA2107 should not fire.

Properties seen in these files that are NOT yet in confirmed-versions.md, i.e. the likely failure
points if one breaks: `LayoutWrap`, `LayoutMaxHeight`, `LayoutMinWidth`, and on `Text@0.0.51`:
`Wrap`, `VerticalAlign`, `Weight`, `TextAlign`. On ModernText@1.0.0: `AutoHeight`, `FontWeight`, `Color`.
Rectangle@2.3.0 here only gets `BorderStyle`, `Fill`, `Height`, `Width`, `LayoutMinHeight`,
`AlignInContainer`, `BorderColor` — no radius, so the known PA2108 trap is avoided.

After each paste, in play mode, resize the preview width across ~600 / ~900 / ~1200 px; the
breakpoints in these use `App.Width < 640` and similar. Record whether the layout reflows and, for
Browse/Form/Master-Detail/Mobile, whether the scroll region scrolls with the wheel.

## Results (run 2026-10-28, Dataverse for Teams scratch app, Studio paste)

| Test | Pass/fail | Error code + line | Notes |
|---|---|---|---|
| A1 cmpBottomNavigation | Pass after patch | PA2231 at (48,7) on first paste | Custom `Event` property with `Default: =` rejected. Patched to `Default: =false`, then clean and renders. Control-level bare `=` (e.g. Gallery `OnSelect: =`) fine. |
| A2 cmpKPI | Pass after patch | PA2231 (same cause, prevented by pre-patching `OnCardClick`) | Bare `=` on Gallery `LayoutMaxHeight`/`LayoutMaxWidth` and Classic/Button `Text` inside a component all fine. |
| A3 cmpBreadcrumbs | Pass after patch | PA2231 (same cause, prevented by pre-patching `OnBack`/`OnSelect`) | 56 other bare `=` on Image/Label/GroupContainer properties fine. |
| A4 host screen (extra) | Pass after 2 fixes | PA1001 at (39,42), my error | `: ` inside a plain-scalar formula. Fixed with ` - `. Omitted custom props resolved empty, so pass all explicitly. |
| A5 scroll container (extra) | Pass | none | `LayoutOverflowY: =LayoutOverflow.Scroll` on AutoLayout GroupContainer@1.5.0 scrolls component children. |
| B1 named formulas | Pass | none | `nfUserEmail = Lower(User().Email); nfUserName = Proper(User().FullName);` accepted. |
| B component cmpSidebar | Pass | none, no warnings | Verbatim 1225-line msapp component. Undeclared globals did not raise warnings. |
| B host scrSidebarTest | Pass (2nd attempt) | 1st attempt: "Pasting the YAML code for screen isn't supported yet" | Wrong paste location, not a YAML problem. Render, taps and outputs all work. |
| C1 mobile | Pass after 2 fixes | PA2108 x4 `TextAlign` on Text@0.0.51; red formula error `LayoutJustifyContent.SpaceEvenly` | Fixes: `Align: ='TextCanvas.Align'.Center` and `SpaceBetween`. File patched in examples/. |
| C2 browse | Pass | none | `BorderStyle` on Rectangle fine. |
| C3 form | Pass | none | `LayoutWrap: =true` on GroupContainer@1.5.0 works and fields reflow. |
| C4 master-detail | Pass | none | `BorderStyle` on GroupContainer, `If()` on `LayoutDirection`, `Visible` by `App.Width` all fine. |
| C5 dashboard | Pass | none | ModernText@1.0.0 with `AutoHeight`, `FontWeight`, `Color`; GroupContainer `LayoutMaxHeight`. Page scroll works. |
| C1+C5 together | Pass | none | Text@0.0.51 + ModernText@1.0.0 + Label@2.5.1 in one app, no PA2107/PA2105. App checker: only the known cmpKPI Data warning. |

Not answered by the tester: Rating and Slider paste results from the earlier session remain unrecorded.

## Findings

- **PA2231.** A custom `Event` property in `ComponentDefinitions` needs a non-empty `Default`. Bare `Default: =` fails. `=false` works. Six msapp component files carry this (see examples/README.md).
- **Omitted custom properties resolve empty on a pasted instance** (cmpKPI, cmpBottomNavigation). Pass every property explicitly. An instance's `Height` is not inherited from the definition, so set it.
- **Component instances work as AutoLayout children** with `FillPortions: =0`.
- **Text@0.0.51 uses `Align: ='TextCanvas.Align'.Center`.** `TextAlign` is PA2108.
- **`SpaceEvenly` is not a `LayoutJustifyContent` value.** Paste does not validate enum values, so it shows up as a red formula error afterward.
- **Pasting a `Screens:` block** into the wrong place gives "Pasting the YAML code for screen isn't supported yet". Component definitions need the Components tab (error "You cannot paste a component definition here" elsewhere).
- **`: ` inside a plain-scalar formula** gives PA1001. Use ` - ` or a `|-` block.
- **Classic/TextInput@2.3.2 without `Default`** shows "Text input". Set `Default: =""`.
- **Open item:** cmpKPI `Data` shows "Expected a different collection record structure" (harmless, cause unresolved).
- **Skeleton cosmetics** (not paste failures): placeholder `[icon]`/`[action]` wrap in scrMobile; `cntFabSlot` fills leftover space; action containers without `Fill`/`DropShadow` draw a default box; scrDashboard `cntKpiRow` phone height 200 clips the wrapped KPI cards (needs about 204+).
