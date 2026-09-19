# Schema source

`pa.schema.yaml` cached from:
https://raw.githubusercontent.com/microsoft/PowerApps-Tooling/refs/heads/master/schemas/pa-yaml/v3.0/pa.schema.yaml

Last fetched: 2026-09-19.

This is Microsoft's own JSON Schema (written in YAML) for the `pa.yaml` v3.0 canvas app source
format, from the `microsoft/PowerApps-Tooling` repo. Root-level structure: `App`, `Screens`,
`ComponentDefinitions`, `DataSources`, `EditorState`.

Re-fetch periodically (the schema version may bump) with:

```bash
curl -s -o reference/schema/pa.schema.yaml \
  "https://raw.githubusercontent.com/microsoft/PowerApps-Tooling/refs/heads/master/schemas/pa-yaml/v3.0/pa.schema.yaml"
```

Use this to structurally validate generated YAML (via `pyyaml` + `jsonschema` when a shell is
available) before handoff — it catches malformed structure, but **not** the empirically-discovered
Studio paste failures in `../syntax-gotchas.md` (those aren't schema violations, they're things
Studio's editor itself rejects at a level the schema doesn't model).
