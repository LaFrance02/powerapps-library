#!/usr/bin/env python3
"""Pre-flight checker for pa.yaml files, run BEFORE pasting into Power Apps Studio.

Line-based on purpose: PyYAML chokes on bare `=` values that Studio accepts, so this does not
parse the file as YAML. Every rule below was learned from a real Studio paste failure or a
paste-tested fact in reference/ (see tests/paste-test-2026-10-28.md).

Usage:  python3 tools/preflight.py FILE [FILE...]
Exit code 1 if any ERROR is found, 0 otherwise (warnings do not fail).
"""
import re
import sys
from collections import defaultdict

# --- facts (keep in step with reference/confirmed-versions.md and syntax-gotchas.md) ---------
# Properties known NOT to exist on a control type -> suggested replacement
INVALID_PROPS = {
    "Text@0.0.51": {"TextAlign": "Align: ='TextCanvas.Align'.Center (or .Start / .End)"},
}
# Enum members seen/confirmed valid. A member outside the set is a WARNING (paste does not
# validate enums; the property just turns red afterward).
ENUMS = {
    "LayoutJustifyContent": {"Start", "Center", "End", "SpaceBetween"},
    "LayoutAlignItems": {"Start", "Center", "End", "Stretch"},
    "LayoutDirection": {"Horizontal", "Vertical"},
}
KNOWN_BAD_ENUM = {"LayoutJustifyContent.SpaceEvenly": "not a real value; use SpaceBetween"}

KEY_RE = re.compile(r"^(\s*)(?:- )?([A-Za-z_][\w.']*)\s*:(?:\s(.*))?$")
CONTROL_RE = re.compile(r"^\s*Control:\s*(\S+)")
NAME_RE = re.compile(r"^(\s*)- ([A-Za-z_]\w*):\s*$")
BLOCK_RE = re.compile(r"^[|>][+-]?\d*$")


def check(path):
    issues = []  # (line, level, code, message)
    try:
        lines = open(path, encoding="utf-8").read().split("\n")
    except OSError as e:
        return [(0, "ERROR", "IO", str(e))]

    versions = defaultdict(dict)       # control type -> {version: first line}
    names = defaultdict(list)          # control name -> [lines]
    block_indent = None                # indent of key that opened a block scalar
    props_indent = None                # indent of the current `Properties:` key
    cur_control = None                 # control type@ver of the nearest Control: line above
    cur_control_indent = -1
    prop_kind = None                   # last PropertyKind seen (CustomProperties)
    pk_line = 0

    for i, raw in enumerate(lines, 1):
        line = raw.rstrip("\r")
        if "\t" in line[: len(line) - len(line.lstrip())]:
            issues.append((i, "ERROR", "TAB", "tab used for indentation; YAML needs spaces"))
        stripped = line.strip()
        indent = len(line) - len(line.lstrip())

        # inside a block scalar: skip content lines
        if block_indent is not None:
            if stripped == "" or indent > block_indent:
                continue
            block_indent = None
        if stripped == "" or stripped.startswith("#"):
            continue

        m = NAME_RE.match(line)
        if m:
            names[m.group(2)].append(i)

        cm = CONTROL_RE.match(line)
        if cm:
            ctrl = cm.group(1)
            cur_control, cur_control_indent = ctrl, indent
            if "@" in ctrl:
                t, v = ctrl.split("@", 1)
                versions[t].setdefault(v, i)

        km = KEY_RE.match(line)
        if not km:
            continue
        kindent, key, val = len(km.group(1)), km.group(2), km.group(3)
        val = (val or "").strip()

        if key == "Properties":
            props_indent = kindent
        elif props_indent is not None and kindent <= props_indent:
            props_indent = None

        if val and BLOCK_RE.match(val):
            block_indent = kindent + (2 if line.lstrip().startswith("- ") else 0)
            continue

        # PropertyKind / Default bookkeeping for PA2231
        if key == "PropertyKind":
            prop_kind, pk_line = val, i
        if key == "Default" and prop_kind == "Event" and re.fullmatch(r"=\s*|\"\"?", val or "="):
            issues.append((i, "ERROR", "PA2231",
                           "custom Event property needs a non-empty Default; use `Default: =false`"))
        if key == "Default" and prop_kind == "Event" and val == "":
            pass  # covered above

        # PA2108: property not valid on control type
        if cur_control in INVALID_PROPS and key in INVALID_PROPS[cur_control] and kindent > cur_control_indent:
            issues.append((i, "ERROR", "PA2108",
                           f"'{key}' is not a property of {cur_control}; use {INVALID_PROPS[cur_control][key]}"))

        # PA1001: `: ` inside a plain scalar value
        if val and val[0] not in "\"'|>[{&*!%@`" and re.search(r":(\s|$)", val):
            issues.append((i, "ERROR", "PA1001",
                           "': ' inside a plain-scalar value (YamlInvalidSyntax); use ' - ' or a |- block scalar"))

        # property value without leading `=` under Properties:
        inner = val[1:] if val[:1] in "'\"" else val  # quoted formulas like '=Parent.Width ' are valid
        if props_indent is not None and kindent > props_indent and val and inner[:1] not in "=|>":
            issues.append((i, "ERROR", "NOEQ",
                           f"property '{key}' value must start with '=' (got {val[:30]!r})"))

        # enums
        for em in re.finditer(r"\b(Layout\w+)\.(\w+)\b", val):
            full = f"{em.group(1)}.{em.group(2)}"
            if full in KNOWN_BAD_ENUM:
                issues.append((i, "WARN", "ENUM", f"{full}: {KNOWN_BAD_ENUM[full]}"))
            elif em.group(1) in ENUMS and em.group(2) not in ENUMS[em.group(1)]:
                issues.append((i, "WARN", "ENUM", f"{full}: member not in the confirmed set {sorted(ENUMS[em.group(1)])}"))

    # PA2107: one version per control type
    for t, vs in versions.items():
        if len(vs) > 1:
            detail = ", ".join(f"{v} (line {ln})" for v, ln in vs.items())
            issues.append((min(vs.values()), "ERROR", "PA2107",
                           f"control type {t} referenced with several versions: {detail}"))
    # duplicate control names (must be unique across the whole paste)
    for n, ls in names.items():
        if len(ls) > 1:
            issues.append((ls[1], "ERROR", "DUPNAME",
                           f"control name '{n}' used {len(ls)} times (lines {', '.join(map(str, ls))})"))
    return sorted(issues)


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    errors = 0
    for p in argv:
        issues = check(p)
        for ln, level, code, msg in issues:
            print(f"{p}:{ln}: {level} {code}: {msg}")
            errors += level == "ERROR"
        if not issues:
            print(f"{p}: ok")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
