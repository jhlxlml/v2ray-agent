"""Check Bash against warnings present at the original audit commit."""
import collections
import json
import subprocess

from audit import ROOT, SCRIPTS

BASE = "140b1659f1874aaefb1cdde412c6baefaf196198"


def findings(source):
    result = subprocess.run(
        ["shellcheck", "--shell=bash", "--format=json", "-"],
        input=source, capture_output=True, encoding="utf-8",
    )
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stderr)
    lines = source.splitlines()
    diagnostics = json.loads(result.stdout)
    for entry in diagnostics:
        if entry["level"] == "error":
            raise RuntimeError(entry)
    return collections.Counter(
        (entry["code"], entry["message"], lines[entry["line"] - 1].strip())
        for entry in diagnostics
    )


def main():
    failed = False
    for name in SCRIPTS:
        result = subprocess.run(
            ["git", "cat-file", "-e", f"{BASE}:{name}"], cwd=ROOT, capture_output=True
        )
        if result.returncode:
            baseline = collections.Counter()
        else:
            original = subprocess.check_output(["git", "show", f"{BASE}:{name}"], cwd=ROOT)
            baseline = findings(original.decode("utf-8"))
        current = findings((ROOT / name).read_text(encoding="utf-8"))
        for (code, message, line), count in sorted((current - baseline).items()):
            print(f"{name}: SC{code} ({count}): {message}\n    {line}")
            failed = True
    if failed:
        raise SystemExit(1)
    print("ShellCheck: no new diagnostics relative to the audit commit")


if __name__ == "__main__":
    main()
