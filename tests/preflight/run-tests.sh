#!/usr/bin/env bash
# Regression test for tools/preflight.py. Run from the repo root: bash tests/preflight/run-tests.sh
set -u
fail=0
out=$(python3 tools/preflight.py tests/preflight/bad-fixture.yaml)
for code in PA2231 PA2108 PA1001 NOEQ ENUM PA2107 DUPNAME; do
  echo "$out" | grep -q " $code" || { echo "MISSING expected $code on bad-fixture"; fail=1; }
done
# files verified clean by paste test must stay clean
python3 tools/preflight.py examples/powerlibs-layout-*.yaml examples/msapp-docrouterfree-component-sidebar.yaml >/dev/null || { echo "known-good file now flagged"; fail=1; }
# the six msapp files with empty Event defaults must be flagged PA2231
for f in bar-list bottom-navigation breadcrumbs enhanced-dialog kpi my-table; do
  python3 tools/preflight.py examples/msapp-docrouterfree-component-$f.yaml | grep -q PA2231 || { echo "$f not flagged"; fail=1; }
done
[ $fail = 0 ] && echo "preflight tests passed"
exit $fail
