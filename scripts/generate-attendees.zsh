#!/usr/bin/env zsh
#
# Generate attendees.md for TAC meeting minutes directories.
#
# Usage: scripts/generate-attendees.zsh [--stdout] [--quorum N] [year|directory ...]
#
#   With no arguments, every year directory under tac/meeting-minutes is
#   processed. A bare year ("2026") is resolved relative to tac/meeting-minutes;
#   anything else is treated as a path.
#
#   --stdout    print the report instead of writing attendees.md
#               (only valid with a single directory)
#   --quorum N  fixed quorum threshold. By default quorum follows the charter
#               rule of fifty percent of the roster listed for that meeting,
#               rounded up -- 6 of 11.
#
# Each YYYY-MM-DD.md file is read, its "# Attended by" checklist parsed
# ("- [x] Name" present, "- [ ] ~~Name~~" absent), and a report written with
# per-attendee stats at the top followed by a per-meeting breakdown.

emulate -L zsh
setopt extended_glob no_unset err_exit pipe_fail

repo_root=${0:A:h:h}
minutes_root=$repo_root/tac/meeting-minutes

to_stdout=0
quorum_override=0
typeset -a targets
targets=()

while (( $# )); do
  arg=$1
  case $arg in
    --stdout) to_stdout=1 ;;
    --quorum)
      shift
      if [[ ${1-} != <-> ]]; then
        print -u2 "generate-attendees: --quorum needs a number"
        exit 2
      fi
      quorum_override=$1
      ;;
    -h|--help)
      sed -n '3,20p' ${0:A} | sed 's/^# \{0,1\}//'
      exit 0
      ;;
    -*)
      print -u2 "generate-attendees: unknown option: $arg"
      exit 2
      ;;
    <->) targets+=($minutes_root/$arg) ;;
    *)   targets+=(${arg:A}) ;;
  esac
  shift
done

if (( ! $#targets )); then
  targets=($minutes_root/[0-9][0-9][0-9][0-9](N/))
  targets=(${targets%/})
fi

if (( ! $#targets )); then
  print -u2 "generate-attendees: no meeting minutes directories found under $minutes_root"
  exit 1
fi

if (( to_stdout && $#targets > 1 )); then
  print -u2 "generate-attendees: --stdout requires exactly one directory"
  exit 2
fi

# report <directory> -- writes the markdown report for one year to stdout
report() {
  local src_dir=$1
  local -a files dates roster sortable here away no_quorum
  local -A att n_present n_absent seen rate streak first_seen last_seen
  local -A m_present m_listed m_quorum
  local f date line mark name key entry d s i listed total_present in_section
  local p l quorum_cell

  files=(${src_dir}/[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9].md(N.on))
  if (( ! $#files )); then
    print -u2 "generate-attendees: no YYYY-MM-DD.md files in $src_dir"
    return 1
  fi

  for f in $files; do
    date=${${f:t}:r}
    in_section=0
    local -a found
    found=()
    while IFS= read -r line || [[ -n $line ]]; do
      if [[ $line == '# Attended by'* ]]; then
        in_section=1
        continue
      fi
      (( in_section )) || continue
      [[ $line == '#'* ]] && { in_section=0; continue }   # a later heading ends it
      [[ $line == (#b)[-*][[:space:]]##\[([xX[:space:]])\][[:space:]]##(*) ]] || continue
      mark=$match[1]
      # strip strike-through markers and surrounding space; tolerate a
      # mistyped single "~" on either end
      name=$match[2]
      name=${${name##[[:space:]~]#}%%[[:space:]~]#}
      [[ -n $name ]] || continue

      if (( ! ${+seen[$name]} )); then
        seen[$name]=1
        roster+=($name)
        n_present[$name]=0
        n_absent[$name]=0
      fi

      key="$date|$name"
      found+=($name)
      if [[ $mark == [xX] ]]; then
        att[$key]=x
        n_present[$name]=$(( ${n_present[$name]} + 1 ))
      else
        att[$key]=-
        n_absent[$name]=$(( ${n_absent[$name]} + 1 ))
      fi
    done < $f
    # only count files that actually carry an attendance roster
    (( $#found )) && dates+=($date)
  done

  if (( ! $#dates )); then
    print -u2 "generate-attendees: no attendance rosters found in $src_dir"
    return 1
  fi

  # --- derived stats ---------------------------------------------------------

  # per-meeting turnout and quorum. The charter puts quorum at fifty percent
  # of the voting representatives, so default to half the roster listed for
  # that meeting, rounded up (6 of 11).
  no_quorum=()
  for d in $dates; do
    p=0
    l=0
    for name in $roster; do
      key="$d|$name"
      (( ${+att[$key]} )) || continue
      l=$(( l + 1 ))
      [[ $att[$key] == x ]] && p=$(( p + 1 ))
    done
    m_present[$d]=$p
    m_listed[$d]=$l
    if (( quorum_override > 0 )); then
      m_quorum[$d]=$quorum_override
    else
      m_quorum[$d]=$(( (l + 1) / 2 ))
    fi
    (( p < ${m_quorum[$d]} )) && no_quorum+=($d)
  done

  for name in $roster; do
    listed=$(( ${n_present[$name]} + ${n_absent[$name]} ))
    rate[$name]=$(( listed ? 100.0 * ${n_present[$name]} / listed : 0 ))

    # current streak: consecutive most-recent meetings attended.
    # meetings where the person was not on the list at all are skipped.
    s=0
    for (( i = $#dates; i > 0; i-- )); do
      key="$dates[i]|$name"
      (( ${+att[$key]} )) || continue
      [[ $att[$key] == x ]] || break
      (( ++s ))
    done
    streak[$name]=$s

    first_seen[$name]="-"
    last_seen[$name]="-"
    for d in $dates; do
      key="$d|$name"
      [[ ${att[$key]:-} == x ]] || continue
      [[ $first_seen[$name] == "-" ]] && first_seen[$name]=$d
      last_seen[$name]=$d
    done

    # sort key: attendance desc, then name asc
    sortable+=("${(l:4::0:)$(( 9999 - ${n_present[$name]} ))}|$name")
  done
  sortable=(${(o)sortable})

  total_present=0
  for name in $roster; do
    total_present=$(( total_present + ${n_present[$name]} ))
  done

  # --- output ----------------------------------------------------------------

  print -r -- "[//]: # (SPDX-License-Identifier: CC-BY-4.0)"
  print -r -- ""
  print -r -- "# ${src_dir:t} TAC Meeting Attendance"
  print -r -- ""
  print -r -- "Generated by \`scripts/generate-attendees.zsh\` from the meeting minutes in this directory. Do not edit by hand."
  print -r -- ""
  print -r -- "- Meetings: **$#dates** ($dates[1] through $dates[-1])"
  print -r -- "- People on the roster: **$#roster**"
  printf -- "- Average attendance per meeting: **%.1f**\n" $(( 1.0 * total_present / $#dates ))
  if (( quorum_override > 0 )); then
    print -r -- "- Quorum: **$quorum_override** attendees"
  else
    print -r -- "- Quorum: **fifty percent of the roster, rounded up** (6 of 11)"
  fi
  printf -- "- Meetings without quorum: **%d** (%.0f%%)\n" \
    $#no_quorum $(( 100.0 * $#no_quorum / $#dates ))
  print -r -- ""
  print -r -- "## Per-attendee stats"
  print -r -- ""
  # the wrapper carries the CSS that keeps this eight column table inside the
  # content width; the blank lines keep the table markdown on GitHub too
  print -r -- "<div class=\"attendance-stats\" markdown=\"1\">"
  print -r -- ""
  print -r -- "| Attendee | Attended | Absent | Listed | Rate | Current streak | First attended | Last attended |"
  print -r -- "| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |"
  for entry in $sortable; do
    name=${entry#*|}
    listed=$(( ${n_present[$name]} + ${n_absent[$name]} ))
    printf -- "| %s | %d | %d | %d | %.0f%% | %d | %s | %s |\n" \
      $name $n_present[$name] $n_absent[$name] $listed \
      $rate[$name] $streak[$name] $first_seen[$name] $last_seen[$name]
  done
  print -r -- ""
  print -r -- "</div>"
  print -r -- ""
  print -r -- "## Meetings without quorum"
  print -r -- ""
  if (( ! $#no_quorum )); then
    print -r -- "Every meeting reached quorum."
  else
    print -r -- "| Meeting | Present | Listed | Quorum | Short by |"
    print -r -- "| --- | ---: | ---: | ---: | ---: |"
    for d in $no_quorum; do
      print -r -- "| [$d](./$d.md) | ${m_present[$d]} | ${m_listed[$d]} | ${m_quorum[$d]} | $(( ${m_quorum[$d]} - ${m_present[$d]} )) |"
    done
  fi
  print -r -- ""
  print -r -- "## Per-meeting attendance"
  print -r -- ""
  print -r -- "| Meeting | Present | Absent | Quorum | Attendees |"
  print -r -- "| --- | ---: | ---: | :---: | --- |"
  for d in $dates; do
    here=() away=()
    for name in $roster; do
      key="$d|$name"
      case ${att[$key]:-} in
        x) here+=($name) ;;
        -) away+=($name) ;;
      esac
    done
    if (( $#here >= ${m_quorum[$d]} )); then
      quorum_cell="yes"
    else
      quorum_cell="**no**"
    fi
    print -r -- "| [$d](./$d.md) | $#here | $#away | $quorum_cell | ${(j:, :)here} |"
  done
}

rc=0
for dir in $targets; do
  if [[ ! -d $dir ]]; then
    print -u2 "generate-attendees: not a directory: $dir"
    rc=1
    continue
  fi
  if (( to_stdout )); then
    report $dir || rc=1
  elif report $dir > $dir/attendees.md; then
    print -r -- "generate-attendees: wrote ${dir#$repo_root/}/attendees.md"
  else
    rm -f $dir/attendees.md
    rc=1
  fi
done

exit $rc
