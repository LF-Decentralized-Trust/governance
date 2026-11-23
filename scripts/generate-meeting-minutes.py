#!/usr/bin/env python3
"""List the TAC meeting minutes on tac/meeting-minutes/index.md.

The dated minutes are deliberately not in the mkdocs nav: there are about a
hundred of them, and on a phone the nav is behind the hamburger menu, which
left the Meetings landing page looking blank. This script writes the list into
the page itself, between the BEGIN/END GENERATED markers, from the files in
tac/meeting-minutes/<year>/. Run it before the site build; to add minutes, add
the file and nothing here or in mkdocs.yml needs editing.

Usage: scripts/generate-meeting-minutes.py [--check] [--stdout]

  --check   exit 1 if the committed page is not what would be generated
  --stdout  print the generated block instead of writing the page
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MINUTES = REPO_ROOT / "tac" / "meeting-minutes"
INDEX = MINUTES / "index.md"

BEGIN = "BEGIN GENERATED meeting-minutes"
END = "END GENERATED meeting-minutes"

YEAR_RE = re.compile(r"^[0-9]{4}$")
DATE_RE = re.compile(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})\.md$")


def scan():
    """Return [(year, [date, ...]), ...], newest year and date first."""
    years = []
    for year_dir in sorted(MINUTES.iterdir(), reverse=True):
        if not year_dir.is_dir() or not YEAR_RE.match(year_dir.name):
            continue
        dates = []
        for path in year_dir.iterdir():
            match = DATE_RE.match(path.name)
            if not match:
                continue
            if match.group(1) != year_dir.name:
                raise SystemExit(
                    f"generate-meeting-minutes: {path.relative_to(REPO_ROOT)} "
                    f"is dated {match.group(1)} but sits in {year_dir.name}/"
                )
            dates.append(path.stem)
        if dates:
            years.append((year_dir.name, sorted(dates, reverse=True)))
    if not years:
        raise SystemExit("generate-meeting-minutes: no minutes found")
    return years


def block(years):
    lines = []
    for year, dates in years:
        lines.append("")
        lines.append(f"### {year}")
        lines.append("")
        for date in dates:
            lines.append(f"- [{date}]({year}/{date}.md)")
    lines.append("")
    return lines


def splice(path, body):
    """Return the text of path with the lines between its markers replaced by
    body. The marker lines themselves are kept."""
    lines = path.read_text(encoding="utf-8").split("\n")
    begin = [i for i, line in enumerate(lines) if BEGIN in line]
    end = [i for i, line in enumerate(lines) if END in line]
    if len(begin) != 1 or len(end) != 1 or begin[0] >= end[0]:
        raise SystemExit(
            f"generate-meeting-minutes: {path.relative_to(REPO_ROOT)} needs "
            f"exactly one '{BEGIN}' line followed by one '{END}' line"
        )
    return "\n".join(lines[: begin[0] + 1] + body + lines[end[0]:])


def main(argv):
    check = "--check" in argv
    to_stdout = "--stdout" in argv
    for arg in argv:
        if arg not in ("--check", "--stdout"):
            raise SystemExit(f"generate-meeting-minutes: unknown argument {arg}")

    years = scan()
    body = block(years)
    count = sum(len(dates) for _, dates in years)
    summary = f"{count} meetings over {len(years)} years"

    if to_stdout:
        print("\n".join(body))
        return 0

    wanted = splice(INDEX, body)
    if INDEX.read_text(encoding="utf-8") == wanted:
        print(f"generate-meeting-minutes: up to date ({summary})")
        return 0
    if check:
        print(
            f"generate-meeting-minutes: {INDEX.relative_to(REPO_ROOT)} is stale; "
            "run scripts/generate-meeting-minutes.py",
            file=sys.stderr,
        )
        return 1
    INDEX.write_text(wanted, encoding="utf-8")
    print(f"generate-meeting-minutes: wrote {INDEX.relative_to(REPO_ROOT)} ({summary})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
