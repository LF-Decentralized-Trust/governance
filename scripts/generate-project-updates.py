#!/usr/bin/env python3
"""Generate the Project Updates listings from the report files on disk.

Usage: scripts/generate-project-updates.py [--check]

Projects file a report by adding one file to tac/project-updates/<year>/.
This script turns the files it finds there into

  * the Project Updates entries in the `nav` of mkdocs.yml, and
  * the list of reports in tac/project-updates/<year>/index.md,

so that nobody has to edit either by hand. Both are rewritten between
BEGIN/END GENERATED marker lines; everything outside the markers is left
alone. The Documentation workflow runs this before every site build, so the
published site always matches the files. The copy committed to the repository
is a snapshot that may lag behind; rerun the script to refresh it.

A year is generated when it has a directory under tac/project-updates and is
not already listed by hand in the nav outside the markers (2024 and 2025 are).

Reports are recognised by file name, `YYYY-<kind>-<Project-Name>.md`, where
<kind> is annual, midyear or q1..q4 in any letter case, and are titled from
that name: `2026-MidYear-Hyperledger-Fabric.md` becomes
"2026 Mid-Year Hyperledger Fabric". Any other markdown file in the directory
is listed directly under the year and reported on stderr.

A report can carry a directive, a markdown comment line of its own near the
top of the file, for the two cases the file name cannot express:

  [//]: # (project-updates: unlisted)
      leave the file out of both listings (a project that has become a lab)
  [//]: # (project-updates: also midyear)
      list the file under a second kind as well (one report filed as both
      the annual and the mid-year review)

  --check   write nothing; exit 1 if either listing is out of date
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MKDOCS = REPO_ROOT / "mkdocs.yml"
UPDATES = REPO_ROOT / "tac" / "project-updates"

BEGIN = "BEGIN GENERATED project-updates"
END = "END GENERATED project-updates"

# (key matched against the lower-cased file name, heading, title word),
# in the order the groups are listed
KINDS = [
    ("annual", "Annual", "Annual"),
    ("midyear", "MidYear", "Mid-Year"),
    ("q1", "Q1", "Q1"),
    ("q2", "Q2", "Q2"),
    ("q3", "Q3", "Q3"),
    ("q4", "Q4", "Q4"),
]
REPORT_RE = re.compile(
    r"^(\d{4})[-_](annual|mid-?year|q[1-4])[-_](.+)\.md$", re.IGNORECASE
)


DIRECTIVE_RE = re.compile(
    r"^\[//\]: # [(\"]project-updates:\s*(unlisted|also\s+(\S+?))\s*[)\"]\s*$",
    re.IGNORECASE,
)
DIRECTIVE_LINES = 20  # directives are only looked for this far into a file


def directives(path):
    """Return (unlisted, [extra kinds]) from the directive lines in path."""
    unlisted, also = False, []
    with path.open(encoding="utf-8") as handle:
        for number, line in enumerate(handle):
            if number >= DIRECTIVE_LINES:
                break
            match = DIRECTIVE_RE.match(line.strip())
            if not match:
                continue
            if match.group(2) is None:
                unlisted = True
                continue
            kind = match.group(2).lower().replace("-", "")
            if any(k[0] == kind for k in KINDS):
                also.append(kind)
            else:
                print(
                    f"generate-project-updates: {path.parent.name}/{path.name}: "
                    f"unknown kind in directive: also {match.group(2)}",
                    file=sys.stderr,
                )
    return unlisted, also


def words(stem):
    """File name fragment to title: separators become spaces, and a name
    written entirely in lower case gets its first letter capitalised."""
    text = re.sub(r"[-_]+", " ", stem).strip()
    if text == text.lower():
        text = text[:1].upper() + text[1:]
    return text


def scan(year_dir):
    """Return (top, groups) for one year directory.

    top is a list of (title, file name) listed directly under the year;
    groups is a list of (heading, [(title, file name), ...]).
    """
    year = year_dir.name
    top, by_kind = [], {}
    for path in sorted(year_dir.glob("*.md"), key=lambda p: p.name.lower()):
        name = path.name
        if name == "index.md":
            continue
        unlisted, also = directives(path)
        if unlisted:
            continue
        match = REPORT_RE.match(name)
        if match and match.group(1) == year:
            kinds = [match.group(2).lower().replace("-", "")]
            kinds += [kind for kind in also if kind not in kinds]
            for kind in kinds:
                title_word = next(k[2] for k in KINDS if k[0] == kind)
                title = f"{year} {title_word} {words(match.group(3))}"
                by_kind.setdefault(kind, []).append((title, name))
            continue
        stem = path.stem
        if stem.startswith(year):
            stem = stem[len(year):]
        title = f"{year} {words(stem)}"
        if name != f"{year}-schedule.md":
            print(
                f"generate-project-updates: {year}/{name} does not match "
                f"YYYY-<kind>-<Project-Name>.md; listed as \"{title}\"",
                file=sys.stderr,
            )
        top.append((title, name))
    # the schedule leads; anything else unrecognised follows it
    top.sort(key=lambda item: (item[1] != f"{year}-schedule.md", item[1].lower()))
    groups = []
    for kind, heading, _ in KINDS:
        if kind in by_kind:
            reports = sorted(by_kind[kind], key=lambda item: item[0].lower())
            groups.append((heading, reports))
    return top, groups


def yaml_key(title):
    """Quote a nav title when YAML would otherwise misread it."""
    if re.search(r"[:#\[\]{}&*!|>'\"%@`,]", title) or title != title.strip():
        return '"' + title.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return title


def nav_block(year, top, groups):
    lines = [f"      - {year}:"]
    for title, name in top:
        lines.append(f"          - {yaml_key(title)}: project-updates/{year}/{name}")
    for heading, reports in groups:
        lines.append(f"          - {heading}:")
        for title, name in reports:
            lines.append(
                f"              - {yaml_key(title)}: project-updates/{year}/{name}"
            )
    return lines


def index_block(year, top, groups):
    lines = [f"- {year}:"]
    for title, name in top:
        lines.append(f"  - [{title}]({name})")
    for heading, reports in groups:
        lines.append(f"  - {heading}:")
        for title, name in reports:
            lines.append(f"     - [{title}]({name})")
    return lines


def splice(path, body):
    """Return the text of path with the lines between its markers replaced
    by body. The marker lines themselves are kept."""
    lines = path.read_text(encoding="utf-8").split("\n")
    begin = [i for i, line in enumerate(lines) if BEGIN in line]
    end = [i for i, line in enumerate(lines) if END in line]
    if len(begin) != 1 or len(end) != 1 or begin[0] >= end[0]:
        raise SystemExit(
            f"generate-project-updates: {path.relative_to(REPO_ROOT)} needs exactly "
            f"one '{BEGIN}' line followed by one '{END}' line"
        )
    return "\n".join(lines[: begin[0] + 1] + body + lines[end[0]:])


def outside_markers(path):
    lines = path.read_text(encoding="utf-8").split("\n")
    begin = next((i for i, line in enumerate(lines) if BEGIN in line), None)
    end = next((i for i, line in enumerate(lines) if END in line), None)
    if begin is None or end is None:
        return lines
    return lines[:begin] + lines[end + 1:]


def main(argv):
    check = False
    for arg in argv:
        if arg == "--check":
            check = True
        elif arg in ("-h", "--help"):
            print(__doc__.strip())
            return 0
        else:
            print(f"generate-project-updates: unknown option: {arg}", file=sys.stderr)
            return 2

    # years kept by hand in the nav, outside the generated block
    by_hand = set()
    in_section = False
    for line in outside_markers(MKDOCS):
        if re.match(r"^  - Project Updates:\s*$", line):
            in_section = True
        elif re.match(r"^ {0,2}\S", line):
            in_section = False
        elif in_section:
            match = re.match(r"^      - (\d{4}):\s*$", line)
            if match:
                by_hand.add(match.group(1))

    years = sorted(
        (
            d
            for d in UPDATES.iterdir()
            if d.is_dir() and re.fullmatch(r"\d{4}", d.name) and d.name not in by_hand
        ),
        key=lambda d: d.name,
        reverse=True,
    )

    outputs = []  # (path, new text, summary)
    nav = []
    for year_dir in years:
        top, groups = scan(year_dir)
        count = sum(len(reports) for _, reports in groups)
        nav += nav_block(year_dir.name, top, groups)
        index = year_dir / "index.md"
        if index.exists():
            body = [""] + index_block(year_dir.name, top, groups) + [""]
            outputs.append((index, splice(index, body), f"{count} reports"))
        else:
            print(
                f"generate-project-updates: {year_dir.name}/index.md is missing; "
                "skipped",
                file=sys.stderr,
            )
    summary = ", ".join(d.name for d in years) or "no generated years"
    outputs.insert(0, (MKDOCS, splice(MKDOCS, nav), f"nav for {summary}"))

    stale = 0
    for path, text, note in outputs:
        rel = path.relative_to(REPO_ROOT)
        if path.read_text(encoding="utf-8") == text:
            print(f"generate-project-updates: {rel} is up to date ({note})")
        elif check:
            print(f"generate-project-updates: {rel} is out of date ({note})")
            stale += 1
        else:
            path.write_text(text, encoding="utf-8")
            print(f"generate-project-updates: wrote {rel} ({note})")
    return 1 if stale else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
