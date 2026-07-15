#!/bin/bash
set +e

VERIFIER_DIR="${VERIFIER_DIR:-/logs/verifier}"
mkdir -p "$VERIFIER_DIR"

pytest /tests/test_outputs.py --ctrf "$VERIFIER_DIR/ctrf.json" -q
status=$?

if [ "$status" -eq 0 ]; then
  echo 1 > "$VERIFIER_DIR/reward.txt"
else
  echo 0 > "$VERIFIER_DIR/reward.txt"
fi

exit 0
