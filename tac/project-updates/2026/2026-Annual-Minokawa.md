[//]: # (SPDX-License-Identifier: CC-BY-4.0)

---
layout: default
title: 2026 Minokawa Annual Review
parent: 2026
grand_parent: Project Updates
---

# 2026 Annual Review Minokawa

This is the first review of Minokawa Compact and it covers
**30 September 2025 through 31 August 2026**.

## Project Health

The Minokawa repositories can be found [here](https://github.com/LFDT-Minokawa).

The open-source Minokawa project began in September 2025 and has been growing since then.
The Compact programming language implementation was moved from its private Midnight Network
repository to `LFDT-Minokawa/compact`.
While continuing to develop Compact, the maintainers have onboarded new community contributors.

In addition to switching to the open-source repository,
the Minokawa TSC has set up an open governance model for the project.
There are weekly public meetings where the project and its plans for the future are discussed.

Since September there have been 15 software component releases.
Since January there have been over 1000 commits to the repository and 750 issues opened.

## Progress Against Prior Goals 

There have been several major accomplishments in Minokawa's first year as an open-source project.
The private Compact language repository was successfully moved to the open-source LFDT-Minokawa repository.
Along with this source code move, the maintainers also transitioned to working in the open,
including issue reporting and project planning.
Disentangling the project's GitHub workflows from private systems and tooling was a challenge in early 2026.
Additionally, the release process, based on GitHub workflows, was streamlined and improved.

The TSC has adopted a mechanism for open design of language and tooling features: the Compact Improvement Proposal (CoIP) process.
This process is modeled after other successful programming language processes, mainly the Python Enhancement Proposal (PEP) process.

There was a major effort in the first half of 2026 to improve the primary source of documentation for the Compact programming language:
the [Compact Reference](https://docs.midnight.network/compact/reference/compact-reference).

Specific goals and results, along with work in progress and planned work are discussed below.

### Project Health

Compact was contributed to LFDT and at the end of Sep 2025. The first release of Compact under LFDT was toolchain 0.28.0-rc.0 (this does not show up under [LFDT-Minokawa/compact/releases](https://github.com/LFDT-Minokawa/compact/releases) due to taking the team some time to migrate release processes). Since then the toolchain has advanced steadily through 0.34.x with regular, detailed releases (CHANGELOG.md tracks breaking changes, fixes, and additions ), plus companion releases of the `compact` CLI/devtools (up to 0.5.2) and compact runtime (up to 0.19.0). The repo shows sustained activity (1,037+ commits on `main`) and healthy triage — LFX Insights rates the project **Lifecycle: Active** with a median maintainer response time of **3 days**. Overall LFX Health Score is **59/100 ("Excellent")**, with development cadence cited as the main drag and maintainer coverage as the main strength. 111 open issues / 46 open PRs at time of writing. The development cadence has ebbs and flows due to when a feature gets designed and implemented. The team is actively practicing to conduct design decisions in public and on the repo to better reflect the active development of the project. Since Q2 of 2026, the project has experienced more irregular releases and the team is working on getting back to more regular releases.

Continued compiler-internals work (both improvements and new features), improvements to Compact developer tool, ongoing release-engineering (including publishing `RELEASE.md` which is currently missing) and testing hardening.

### Maintainer Diversity

Per LFX Insights: **5 active maintainers with merge rights**, contributors spanning **2 organizations**, and "excellent" quarter-over-quarter contributor retention. However, the project is still flagged as having **low contributor diversity** (4 contributors account for 51%+ of activity) and **high org dependency** (1 organizations account for 51%+ of activity) — expected for a project only a year removed from being a single-vendor codebase (formerly maintained solely by Shielded Technologies) before moving under LFDT governance. Note: LFX Insights misrepresents the number of active maintainers (it states it as 14) and organization diversity (it states contributors span over 29 organizations). Note: the repo does not currently have a `MAINTAINERS.md`; instead this is replaced by `CODEOWNERS` designates the `@LFDT-Minokawa/compact-maintainers` team as sole reviewer.

Growing the maintainer/contributor base beyond the founding team now that the project is under open LFDT governance.

### Project Adoption

Compact is the primary smart-contract language for the **Midnight Network**, which has progressed through Preprod/Preview and is now referenced as live on **Mainnet**. It's consumed transitively by the broader Midnight ecosystem — Compact.js/midnight-js runtimes, the DApp Connector API, and the Wallet SDK — and the toolchain has kept pace with ledger upgrades (e.g., toolchain 0.30 and 0.33 added support for ledger version 8 and 9, respectively). On GitHub: 43 stars, 30 forks. Community usage includes hackathon/template projects built against it. Furthermore, in Q2 of 2026 we did a full rewrite of Compact langauge reference to ensure a smooth onboarding of new contributors. More recently, Compact has been getting traction by other ecosystems (see [Adoption](#adoption)). Note: the repo does not currently have an `ADOPTERS.md`, so adopters aren't formally enumerated as the LFDT process asks for.

Continued lowering of the barrier to building real dapps: cross-contract module resolution work (CoIP-3, dynamic module resolution), documentation/tutorial improvements (`doc/writing.mdx`, language reference), and example/template maintenance to support more complex production use cases. Adding `ADOPTERS.md`.

## Deliverables and Outputs (September 2025 – August 2026)

The Minokawa project primarily releases two software artifacts:
the Compact developer tools (devtools) and the Compact toolchain.
The devtools include the Compact updater tool which allows downloading new versions
and switching between versions.
The devtools also provide the command-line interface for invoking tools provided by the toolchain,
such as the Compact compiler, the Compact formatter, and a "fixup" tool to automate
language updates, deprecations, etc.
The devtools and the toolchain are versioned separately and released independently.

The Compact compiler generates TypeScript interfaces and JavaScript (JS) implementations for Compact contracts.
The generated JavaScript code imports the Compact runtime JS package.
This package provides common services used by Compact contracts.
The Compact runtime is slightly more stable than the Compact toolchain;
not every Compact toolchain update uses a different Compact runtime.
Therefore, the Compact runtime is versioned separately from the toolchain.

Additionally, the Compact language itself is versioned.
Again, the language is slightly more stable than the Compact toolchain;
not every Compact toolchain update will change the langauge version.

### Releases

The devtools are released irregularly, as new features are developed.
In contast, the toolchain and thus the runtime and the language, strive to adhere to a regular four-week release cadence.
This cadence has occasionally been disrupted by external responsibilities such as the launch of the Midnight Network's Mainnet and the preparation for the first Midnight network hard fork.

During the reporting year, there were devtools releases 0.3.0, 0.5.0, 0.5.1, and 0.5.2.
There were toolchain releases 0.28.0, 0.29.0, 0.30.0, 0.31.0, 0.31.1, and 0.34.0.
The Compact runtime went from version 0.14.0 to version 0.19.0;
and the Compact language went from version 0.20.0 to version 0.26.0.

Skipped version numbers are due to hiccups around the mentioned release of Midnight Mainnet (in March 2026),
and preparation for the first Midnight hard fork (expected in the fourth quarter of 2026).

### Release Notes and Change Log

The features added during the year are too many to mention.
Releases include detailed release notes that are in the repository in the [doc/release-notes](https://github.com/LFDT-Minokawa/compact/tree/main/doc/release-notes) subdirectory.
There is a detailed change log kept in the repository at [CHANGELOG.md](https://github.com/LFDT-Minokawa/compact/blob/main/CHANGELOG.md).

### Release Candidates and Developer Builds

As part of the toolchain release process, the maintainers will make a series of "release candidate" builds which are also released on the `LFDT-Minokawa/compact` repository.

A contributor provided a mechanism for making "developer builds" from work in progress on the project's developer branch (`main`).
Developer builds are triggered by a button press by a maintainer,
they build binary toolchain artifacts from the developer branch,
tag it with a version including the commit hash,
and publish it as a GitHub release.

This workflow simplifies development and testing for downstream projects.

## Community Calls

The Minokawa project has been holding consistent community calls on Wednesday ([zoom link](https://zoom-lfx.platform.linuxfoundation.org/meeting/92376999403?password=23e83ac5-4334-4da3-9e07-2afb5065fa28)), meeting notes are kept udner a [subdirectory](https://github.com/LFDT-Minokawa/compact/tree/main/meetings), and recordings are available on [LFDT calendar](https://www.lfdecentralizedtrust.org/meeting-calendar).

During recent calls, the community has engaged significantly asking for new proposals. We welcome all engagements. We are particularly interested in creating a potential experimental repo under Minokawa for ideas and implementations that we are excited about but we do not have capacity to commit to maintain, test, and release yet. 

## Adoption

The community has engaged greatly with the project. This is particularly exciting for the team and the project since new contributors from different organizations are engainign with Minokawa/Compact. Interesting examples:

- [MinoCrab](https://github.com/sig-net/minocrab)--a Rust eDSL of Compact
- [CoIP on adding a Rust backend to Compact](https://github.com/LFDT-Minokawa/compact/pull/730)
- [CoIP on language-agnostic representation](https://github.com/LFDT-Minokawa/compact/pull/700)

We remain committed to diversifying Minokawa adoption among a variety of organizations.

## Goals for the Second Half of 2026

- Maintain Compact and provide frequent releases at least every other month
- Encourage and engage community to contribute to Compact
- Adopt CoIPs from the community and plan to implement them
- Engage with the community and share design discussions on discord
- Develop a public roadmap that contains timelines, priorities, aspirations, and asking explicitly for help from the community

## Help Required

We would like to ask TAC to help enable opportunities for mentorship and adoption cross project/organization collaboration. Additionally, we extremely feel the need to develop an AI policy and would like to ask TAC for their recommendations/requirements. 

As mentioned earlier, we are excited to create a new repo under Minokawa for experimental projects suggested and contributed by the community which the TSC does not have capacity to fully maintain and test at this time. We ask TAC if they have experience with such a scenario and if so what have they learned that will be useful for us.

## Maintainer and Contributor Diversity

On the project's management front, the team hasn't had bandwith to evaluate and analyze key project health metrics that track our progress towards a thriving and diverse community. However, these are important metric that enable us to assess the project's performance by measuring contributions, code velocity, and issue response and resolution times. 

We anticipate continued growth in our community's diversity, enabling the adoption of more community-driven components. Given that anticipation we plan to focus on these metrics in 2027:

- **Grow our TSC** - Following the recent adoption, we expect increased community participation to the point of becoming members of the Technical Steering Committee (TSC). This growth will enable more companies to take an active role in shaping the project and help expand our community further.
- **Grow our maintainers and committers** - We are actively encouraging participation from new contributors and raising awareness among current maintainers and committers to review their contributions in line with our project guidelines. The goal is to identify and nominate qualified individuals for committer roles, while also assessing our current resources for opportunities to promote existing committers to maintainer roles.
- **Recruit more participating companies** - As we continue to analyze our contributor metrics, we remain committed to promoting Minokawa through events, seminars, and forums to raise the project's visibility. Our goal is to attract interest from a broader range of companies to participate and contribute to the project's objectives. Through these efforts, we aim to increase both the diversity and reach of our community.

## Project Lifecycle Status Recommendation

The Minokawa project requests to keep the current Graduated state.

Minokawa has demonstrated sustained growth in contributor engagement and technical maturity which reflect the expectations of a Graduated LF Decentralized Trust project. We continue to focus on reducing contributor retention, expanding the project visibility, enhancing the project's security health, releasing the toolchain frequently, and improving the user experience to lower the barrier of entry for new contributors.

## Useful Links

- Compact toolchain releases: https://github.com/LFDT-Minokawa/compact/releases
- Compact developer tool releases: https://github.com/LFDT-Minokawa/compact/tags
- LFX Insights on Minokawa: https://insights.linuxfoundation.org/project/minokawa
- Compact language reference: https://github.com/LFDT-Minokawa/compact/blob/main/doc/compact-reference.mdx
