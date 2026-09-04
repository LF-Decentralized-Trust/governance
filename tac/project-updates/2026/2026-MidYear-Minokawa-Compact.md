[//]: # (SPDX-License-Identifier: CC-BY-4.0)

---
layout: default
title: 2026 Mid-Year Review Minokawa Compact
parent: 2026
grand_parent: Project Updates
---

# 2026 Mid-Year Review of Minokawa Compact

This is the first review of Minokawa Compact and it covers **30 September 2025 through 31 August 2026**.

## Project Health

The LFDT page of Minokawa can be found [here](https://github.com/LFDT-Minokawa).

The Minokawa project began in September 2025 and has been growing ever since. We have transitioned Compact repository into Minokawa/Compact. While developing Compact, we were able to onboard new contributors to Minokawa coming from the community.

Next to transitioning the repositories, we have set up an open governance model for the project. We run public meetings on a weekly basis where we discuss the project and its plans for the future.

## Progress Against Prior Goals 

Our initial target was to move Compact repository to Minokawa. We have accomplished this goal along with setting up mechanisms for proposing new features (CoIP: **Co**mpact **I**mprovement **P**roposal), mainstreaming the release process of Compact, disintangle workflows from the previous host of Compact, developing new features, improving existing features of Compact, increasing independent testing of Compact, and improving the documentation of the Compact language.

| Goal | Sep 2025 – Aug 2026 Result | 2026 Work in Progress and Planned |
|---|---|---|
| **Project Health** | Compact was contributed to LFDT and at the end of Sep 2025. The first release of Compact under LFDT was toolchain 0.28.0-rc.0 (this does not show up under [LFDT-Minokawa/compact/releases](https://github.com/LFDT-Minokawa/compact/releases) due to taking the team some time to migrate release processes). Since then the toolchain has advanced steadily through 0.34.x with regular, detailed releases (CHANGELOG.md tracks breaking changes, fixes, and additions ), plus companion releases of the `compact` CLI/devtools (up to 0.5.2) and compact runtime (up to 0.19.0). The repo shows sustained activity (1,037+ commits on `main`) and healthy triage — LFX Insights rates the project **Lifecycle: Active** with a median maintainer response time of **3 days**. Overall LFX Health Score is **59/100 ("Excellent")**, with development cadence cited as the main drag and maintainer coverage as the main strength. 111 open issues / 46 open PRs at time of writing. The development cadence has ebbs and flows due to when a feature gets designed and implemented. The team is actively practicing to conduct design decisions in public and on the repo to better reflect the active development of the project. Since Q2 of 2026, the project has experienced more irregular releases and the team is working on getting back to more regular releases.  | Continued compiler-internals work (both improvements and new features), improvements to Compact developer tool, ongoing release-engineering (including publishing `RELEASE.md` which is currently missing) and testing hardening. |
| **Maintainer Diversity** | Per LFX Insights: **5 active maintainers with merge rights**, contributors spanning **2 organizations**, and "excellent" quarter-over-quarter contributor retention. However, the project is still flagged as having **low contributor diversity** (4 contributors account for 51%+ of activity) and **high org dependency** (1 organizations account for 51%+ of activity) — expected for a project only a year removed from being a single-vendor codebase (formerly maintained solely by Shielded Technologies) before moving under LFDT governance. Note: LFX Insights misrepresents the number of active maintainers (it states it as 14) and organization diversity (it states contributors span over 29 organizations). Note: the repo does not currently have a `MAINTAINERS.md`; instead this is replaced by `CODEOWNERS` designates the `@LFDT-Minokawa/compact-maintainers` team as sole reviewer. | Growing the maintainer/contributor base beyond the founding team now that the project is under open LFDT governance. |
| **Project Adoption** | Compact is the primary smart-contract language for the **Midnight Network**, which has progressed through Preprod/Preview and is now referenced as live on **Mainnet**. It's consumed transitively by the broader Midnight ecosystem — Compact.js/midnight-js runtimes, the DApp Connector API, and the Wallet SDK — and the toolchain has kept pace with ledger upgrades (e.g., toolchain 0.30 and 0.33 added support for ledger version 8 and 9, respectively). On GitHub: 43 stars, 30 forks. Community usage includes hackathon/template projects built against it. Furthermore, in Q2 of 2026 we did a full rewrite of Compact langauge reference to ensure a smooth onboarding of new contributors. More recently, Compact has been getting traction by other ecosystems (see [Adoption](#adoption)). Note: the repo does not currently have an `ADOPTERS.md`, so adopters aren't formally enumerated as the LFDT process asks for. | Continued lowering of the barrier to building real dapps: cross-contract module resolution work (CoIP-3, dynamic module resolution), documentation/tutorial improvements (`doc/writing.mdx`, language reference), and example/template maintenance to support more complex production use cases. Adding `ADOPTERS.md`.|

## Deliverables and Outputs (September 2025 – August 2026)

The following is the list of releases of Compact toolchain and Compact developer tool since moving the project under LFDT. This list does not include neither the release candidates nor the developer releases. Note that the very first release of Compact toolchain appearing under Minokawa is `0.30.0` due the team taking some time to migrate the release process. Compact toolchain releases appear under [releases](https://github.com/LFDT-Minokawa/compact/releases) while Compact developer tool releases appear under [tags](https://github.com/LFDT-Minokawa/compact/tags). Compact runtime is published on [npm](https://www.npmjs.com/package/@midnight-ntwrk/compact-runtime?activeTab=versions).

| release | date |
|---|---|
| Compact runtime 0.19.0 | 2026-08-25 |
| Compact toolchain 0.34.0 (language 0.26.0) | 2026-08-18 |
| Compact developer tool 0.5.2 | 2026-08-13 |
| Compact toolchain 0.31.1 (language 0.23.0) | 2026-06-25 |
| Compact runtime 0.16.0 | 2026-04-29 |
| Compact toolchain 0.31.0 (language 0.23.0) | 2026-04-28 |
| Compact developer tool 0.5.1 | 2026-03-25 |
| Compact runtime 0.15.0 | 2026-03-17 |
| Compact developer tool 0.5.0 | 2026-03-17 |
| Compact toolchain 0.30.0 (language 0.22.0) | 2026-03-16 |
| Compact toolchain 0.29.0 (language 0.21.0) | 2026-02-11 |
| Compact toolchain 0.28.0 (language 0.20.0) | 2026-01-28 |
| Compact runtime 0.14.0 | 2026-01-28 |
| Compact developer tool 0.3.0 | 2025-12-05 |
| Compact runtime 0.9.0 | 2025-10-07 |

**Notes**

- Developer builds (`dev-<commit-hash>` tags) are on-demand, unsupported builds and they are vulnerable to deletion.
- The jumps in some of the releases are due to finding bugs during validation of a release candidate at which point following the semver model it was appropriate to move on to the next release.
- All releases of Compact toolchain on Minokawa are accompanied with detailed [release notes](https://github.com/LFDT-Minokawa/compact/tree/main/doc/release-notes).

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
