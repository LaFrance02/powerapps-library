# PowerApps Library

Matt's cross-project reference library for building Power Apps canvas apps (Teams-embedded,
Dataverse-backed) with Claude. This repo is the durable half of the `powerapps-canvas-app-builder`
Claude skill — the skill holds behavior (the pipeline, the arbitration rule, the rules that never
change), this repo holds facts (control versions, boilerplate, examples), so nothing has to be
re-pasted into a fresh chat.

Used from two computers with no shared cloud-sync folder, so this is a plain git repo with a
private GitHub remote — clone/pull it on whichever machine a session is linked to before reading,
push after writing.

## Layout

- `reference/confirmed-versions.md` — paste-tested control versions and properties, one section
  per source project, dated. Cross-project baseline for a new app; always re-verify before
  trusting an entry in a new environment.
- `reference/syntax-gotchas.md` — version-independent YAML/Power Fx rules that come from the
  parser/language itself, not a specific control version.
- `reference/data-store-decisions.md` — Dataverse vs. Dataverse for Teams vs. SharePoint/Excel,
  and why, based on what's actually broken or worked so far.
- `reference/schema/` — a cached copy of Microsoft's official `pa.yaml` grammar
  (`microsoft/PowerApps-Tooling`), used to structurally validate generated YAML before handoff.
- `components/` — Matt's own canonical, reusable YAML (sidebar, theme, toast, Scan Pattern, etc.),
  captured verbatim from him once. Never regenerated from a guess.
- `examples/` — real working YAML snippets Matt has pasted in from PowerLibs or elsewhere that he
  likes and wants used as a template.
- `projects/` — one living-architecture handoff doc per active app (mission, architecture,
  constraints, decisions, unresolved issues, next actions — the P-HAND-001 format), plus any
  per-app deltas from the cross-project baseline in `reference/`.

## Maintenance rule

When a real Power Apps Studio paste proves something in `reference/` or `components/` wrong or
incomplete, that's new ground truth — update the file and commit it in the same session, don't
just fix the one screen and let the fix evaporate. This repo should only ever get more reliable,
never stay static while the skill re-learns the same lesson twice.
