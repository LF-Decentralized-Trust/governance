[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# Dependabot Configuration Example<!-- omit in toc -->

- [How to use this document](#how-to-use-this-document)
- [Key concepts](#key-concepts)
  - [One grouped PR per ecosystem](#one-grouped-pr-per-ecosystem)
  - [The 30-day cooldown](#the-30-day-cooldown)
  - [`target-branch` does not accept wildcards](#target-branch-does-not-accept-wildcards)
- [File header](#file-header)
- [Default branch entries](#default-branch-entries)
  - [npm](#npm)
  - [GitHub Actions](#github-actions)
  - [Docker](#docker)
  - [Go modules](#go-modules)
  - [Cargo](#cargo)
- [Release branch entries](#release-branch-entries)
- [Complete file](#complete-file)
- [References](#references)

## How to use this document

This is an annotated walkthrough of a `.github/dependabot.yml` that projects can
copy as a starting point. Each section explains one block of the file; the
[complete file](#complete-file) at the end can be copied verbatim.

Adjust the ecosystem list to match what the repository actually uses — an entry
for an ecosystem that is not present in the repository is harmless but noisy in
the Dependabot job logs.

## Key concepts

### One grouped PR per ecosystem

Each ecosystem below groups **all** of its updates into a single pull request
per run. Both regular version updates and security fixes are grouped, so
Dependabot opens at most one PR per ecosystem. This matters because security
updates are otherwise opened individually and ungrouped by default, which is how
a repository ends up with a dozen open Dependabot PRs. Every grouped PR lands on
its own Dependabot branch.

Grouping is expressed with two named groups per ecosystem, split by
`applies-to`:

```yaml
groups:
  npm:
    applies-to: version-updates
    patterns: ["*"]
  npm-security:
    applies-to: security-updates
    patterns: ["*"]
```

`patterns: ["*"]` puts every dependency in that ecosystem into the group.
`open-pull-requests-limit: 1` keeps the ecosystem to a single outstanding PR.

### The 30-day cooldown

Every ecosystem sets a 30-day `cooldown`: a newly published version is not
proposed until it has been on the registry for 30 days. That window is the one
in which a compromised or typosquatted release is usually yanked, so waiting it
out avoids pulling a malicious release into the repository.

Two properties of `cooldown` are worth being explicit about:

- It applies to **version updates only**. Security updates driven by a published
  advisory are never delayed by it, so a real CVE fix still arrives immediately.
- A dependency still inside its cooldown is simply left out of that run's group
  PR and picked up on a later run once it becomes eligible. Nothing is lost.

Ecosystems with semver-aware version data can also set per-bump-type windows;
where they are set below they use the same 30 days as the default:

```yaml
cooldown:
  default-days: 30
  semver-major-days: 30
  semver-minor-days: 30
  semver-patch-days: 30
```

### `target-branch` does not accept wildcards

Dependabot does not support wildcards in `target-branch`. It accepts exactly one
branch name, and the repository default branch when omitted.

To run on `release/*` branches, every release branch needs its own duplicated
set of entries with `target-branch` set. The example below defines the
default-branch entries (no `target-branch`) plus one release branch; copy the
release block and change `target-branch` for any additional release branch.

## File header

```yaml
version: 2

updates:
```

`version: 2` is the only supported configuration version. Everything else lives
under `updates:` as a list of ecosystem entries.

## Default branch entries

These entries omit `target-branch`, so they run against the repository's default
branch.

### npm

```yaml
  - package-ecosystem: npm
    directory: "/"
    schedule:
      interval: weekly
    open-pull-requests-limit: 1
    cooldown:
      default-days: 30
      semver-major-days: 30
      semver-minor-days: 30
      semver-patch-days: 30
    groups:
      npm:
        applies-to: version-updates
        patterns: ["*"]
      npm-security:
        applies-to: security-updates
        patterns: ["*"]
```

`directory: "/"` (singular) points at a single manifest location — here the
`package.json` at the repository root. Use `directories:` (plural) instead when
the manifests are spread across the tree.

### GitHub Actions

```yaml
  - package-ecosystem: github-actions
    directories:
      - "/"
      - "/.github/actions/*"
      - "/.github/workflows/*"
    schedule:
      interval: weekly
    open-pull-requests-limit: 1
    cooldown:
      default-days: 30
    groups:
      github-actions:
        applies-to: version-updates
        patterns: ["*"]
      github-actions-security:
        applies-to: security-updates
        patterns: ["*"]
```

The three directories cover the reusable workflows and composite actions a
repository may define in addition to the workflows themselves. Action versions
are not semver-addressable in the way registry packages are, so only
`default-days` is set.

### Docker

```yaml
  - package-ecosystem: docker
    directories:
      - "**/*"
    schedule:
      interval: weekly
    open-pull-requests-limit: 1
    cooldown:
      default-days: 30
    groups:
      docker:
        applies-to: version-updates
        patterns: ["*"]
      docker-security:
        applies-to: security-updates
        patterns: ["*"]
```

`directories: ["**/*"]` searches the whole repository for Dockerfiles, which
avoids having to enumerate them. As with GitHub Actions, image tags are not
reliably semver, so only `default-days` is set.

### Go modules

```yaml
  - package-ecosystem: gomod
    directories:
      - "**/*"
    schedule:
      interval: weekly
    open-pull-requests-limit: 1
    cooldown:
      default-days: 30
      semver-major-days: 30
      semver-minor-days: 30
      semver-patch-days: 30
    groups:
      gomod:
        applies-to: version-updates
        patterns: ["*"]
      gomod-security:
        applies-to: security-updates
        patterns: ["*"]
```

`directories: ["**/*"]` picks up every `go.mod` in the repository, which covers
multi-module layouts without listing each module.

### Cargo

```yaml
  - package-ecosystem: cargo
    directories:
      - "**/*"
    schedule:
      interval: weekly
    open-pull-requests-limit: 1
    cooldown:
      default-days: 30
      semver-major-days: 30
      semver-minor-days: 30
      semver-patch-days: 30
    groups:
      cargo:
        applies-to: version-updates
        patterns: ["*"]
      cargo-security:
        applies-to: security-updates
        patterns: ["*"]
```

Same shape as the Go entry: a repository-wide search for `Cargo.toml`, weekly,
one grouped PR, 30-day cooldown on version updates.

## Release branch entries

Because [`target-branch` takes a single branch name](#target-branch-does-not-accept-wildcards),
supporting release branches means duplicating the entries above with
`target-branch` added. For example, for `release/1.0`:

```yaml
  - package-ecosystem: npm
    directory: "/"
    target-branch: "release/1.0"
    schedule:
      interval: weekly
    open-pull-requests-limit: 1
    cooldown:
      default-days: 30
      semver-major-days: 30
      semver-minor-days: 30
      semver-patch-days: 30
    groups:
      npm:
        applies-to: version-updates
        patterns: ["*"]
      npm-security:
        applies-to: security-updates
        patterns: ["*"]
```

Repeat for each ecosystem the release branch uses, then copy the whole block and
change `target-branch` for every additional release branch. Keeping this list
pruned as release branches reach end of life avoids Dependabot jobs failing
against branches that no longer exist.

## Complete file

```yaml
# Dependabot configuration
# https://docs.github.com/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file
#
# Each ecosystem groups ALL of its updates into a single PR per run. Both regular
# version updates and security fixes are grouped, so Dependabot opens at most one
# PR per ecosystem (security updates are otherwise opened individually and
# ungrouped by default). Every grouped PR lands on its own Dependabot branch.
#
# Every ecosystem also sets a 30-day `cooldown`: a newly published version is not
# proposed until it has been on the registry for 30 days, which is the window in
# which a compromised or typosquatted release is usually yanked. `cooldown`
# applies to version updates ONLY -- security updates driven by a published
# advisory are never delayed by it. A dependency still inside its cooldown is
# simply left out of that run's group PR and picked up once it becomes eligible.
#
# NOTE: Dependabot does not support wildcards in `target-branch` (it accepts
# exactly one branch name, and the default branch when omitted). To run on the
# release/* branches, every release branch needs its own duplicated set of
# entries with `target-branch` set. The default-branch entries (no
# `target-branch`) plus one release branch are defined below; copy the release
# block and change `target-branch` for any additional release/* branch.

version: 2

updates:
  # ----------------------------------------------------------------------------
  # Default branch
  # ----------------------------------------------------------------------------
  - package-ecosystem: npm
    directory: "/"
    schedule:
      interval: weekly
    open-pull-requests-limit: 1
    cooldown:
      default-days: 30
      semver-major-days: 30
      semver-minor-days: 30
      semver-patch-days: 30
    groups:
      npm:
        applies-to: version-updates
        patterns: ["*"]
      npm-security:
        applies-to: security-updates
        patterns: ["*"]

  - package-ecosystem: github-actions
    directories:
      - "/"
      - "/.github/actions/*"
      - "/.github/workflows/*"
    schedule:
      interval: weekly
    open-pull-requests-limit: 1
    cooldown:
      default-days: 30
    groups:
      github-actions:
        applies-to: version-updates
        patterns: ["*"]
      github-actions-security:
        applies-to: security-updates
        patterns: ["*"]

  - package-ecosystem: docker
    directories:
      - "**/*"
    schedule:
      interval: weekly
    open-pull-requests-limit: 1
    cooldown:
      default-days: 30
    groups:
      docker:
        applies-to: version-updates
        patterns: ["*"]
      docker-security:
        applies-to: security-updates
        patterns: ["*"]

  - package-ecosystem: gomod
    directories:
      - "**/*"
    schedule:
      interval: weekly
    open-pull-requests-limit: 1
    cooldown:
      default-days: 30
      semver-major-days: 30
      semver-minor-days: 30
      semver-patch-days: 30
    groups:
      gomod:
        applies-to: version-updates
        patterns: ["*"]
      gomod-security:
        applies-to: security-updates
        patterns: ["*"]

  - package-ecosystem: cargo
    directories:
      - "**/*"
    schedule:
      interval: weekly
    open-pull-requests-limit: 1
    cooldown:
      default-days: 30
      semver-major-days: 30
      semver-minor-days: 30
      semver-patch-days: 30
    groups:
      cargo:
        applies-to: version-updates
        patterns: ["*"]
      cargo-security:
        applies-to: security-updates
        patterns: ["*"]
```

## References

- [Configuration options for the `dependabot.yml` file](https://docs.github.com/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file)
- [Controlling when Dependabot opens pull requests (cooldown)](https://docs.github.com/code-security/dependabot/working-with-dependabot/dependabot-options-reference#cooldown-)
- [Configuring Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates)
- [Automated Pipelines Best Practices](./automated-pipelines-best-practices.md)
