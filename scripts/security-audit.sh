#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.."
python3 tests/security/audit.py
python3 tests/security/regression.py
python3 tests/security/shellcheck_baseline.py
