[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Annual Review of Hyperledger Cacti

## Project Health and Highlights

- Overall, the project is progressing in its mission and fulfilling its goals, despite meeting setbacks related to the reduction of active maintainers.
  - Specifically, we lost Accenture as a maintainer, and Fujitsu's and IBM's contributions have diminished as their maintainers have other commitments.
- An increase in activity has been observed by members of INESC-ID, namely André Augusto and Carlos Amaro, in addition to Rafael Belchior.
  - Thanks primarily to these maintainers, Cacti continues to be the leading implementor and adopter of the IETF's Secure Asset Transfer Protocol (SATP) interoperability standard.
- We successfully concluded a mentorship project where we made more progress on the Cactus-Weaver integration
- We conducted a workshop in November 2025 showcasing the recent SATP-related developments in Cacti.
- We are generally active on Discord, interacting with the LFDT and open-source community.
- Some maintainers continue to be key shapers of DLT interoperability standards by participating in the IETF's SATP working group.
- We faced technical issues pushing new full releases because of the move from the `hyperledger` to the `hyperledger-cacti` organization, but we have identified the reasons and are actively engaged in pushing a v3 release.
  - Instead, we pushed a separate beta release just for the SATP-related packages and examples.
- We are committed to improve the Cacti codebase, notably with the [cleanup initiative](https://github.com/orgs/hyperledger-cacti/projects/2) as the guiding light.

[LFX Insights Page for Cacti](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=cacti&routedFrom=Github&bestPractice=false&repository=all&dateFilters=Last%20Year&dateRange=2025-01-01%20to%202025-12-31&compare=PP&granularity=month&hideBots=true)

[OpenSSF Scorecard Page](https://scorecard.dev/viewer/?uri=github.com/hyperledger-cacti/cacti)

## Maintainer Diversity

- We have **6 maintainers** at present from 3 different organizations: (Técnico Lisboa)/Blockdaemon, Fujitsu, IBM. (We had maintainers from Accenture until May 2025).
- The number of active maintainers has **decreased** from 8 to 6.
- The number of maintaining organizations has **decreased** from 4 to 3.

Current [MAINTAINERS.md](https://github.com/hyperledger-cacti/cacti/blob/main/MAINTAINERS.md)
and previous (January 1, 2025) [MAINTAINERS.md](https://github.com/hyperledger-cacti/cacti/blob/6baaf6617b3b5336f938d8f004e2e22679abb87c/MAINTAINERS.md)

## Project Adoption

The detailed answer about adoption has been published earlier and can be read through this link: https://github.com/LF-Decentralized-Trust/project-proposals/blob/gh-pages/proposals/graduated/cacti.md#real-world-use

## Goals
Broadly, we seek to:
- Align Cacti with developing interoperability standards and providing PoCs for real-world networks that must adhere to those standards
- Produce an integrated code base with minimal redundancy in functionality
- Streamline the project to have more depth than breadth (i.e., mainain few but widely-usable packages for active DLTs rather than accommodate a huge diversity of DLT connectors)
  
### Performance Against Prior Goals

- We produced a reference TypeScript implementation of the IETF Secure Asset Transfer Protocol (SATP) in the form of a SATP-Hermes feature `0.0.3-beta` version release.
  - The SATP-Hermes implementation of IETF's Secure Asset Transfer Protocol is [publicly tracked](https://github.com/orgs/hyperledger-cacti/projects/1/views/1). Highlights include release SATP v0.0.3-beta, which adds supporting packages to SATP such as bungee-hermes and updates to the Ethereum and Besu connectors.
  - (In greater detail) For SATP, we delivered data transfer functionality (oracle), in release 0.0.1-beta;  gateway monitoring and dashboard, test and ci improvements, and bug fixes ( 0.0.2-beta release), documentation and bug fixes, support for NFT transfers, and refactored the SATP bridge. For the next release, we are planning to deliver the adapter layer and audit endpoints.
- We produced an integrated Cactus-Weaver Fabric connector through Carlos' mentorship project (Carlos became a maintainer toward the end of the project).
- We were unable to work on the issues highlighted by the OpenSSF scorecard and the LFX Insights. But the "good news" is that our scores are hovering more or less in the same place as they were a year ago.
- Because of the reduction in maintainers, our average pull request merge time likely went up, but we are not doing too badly there either. PRs get reviewed and merged within reasonable timeframes.
- We could not complete the release automation migration to the new `hyperledger-cacti` organization, but we did diagnose the blockers. We fixed some of them and pushed through releases of Weaver packages to the latest version number (`v2.1.0`), but most packages are still stuck and there's a PR under review to fix this.
- Thanks to the efforts of Carlos, we were able to diagnose the reasons for heavy resource usage in the execution of GitHub Actions and fix them with a major CI refactor: https://github.com/hyperledger-cacti/cacti/pull/4059.
- On community engagement: maintainers participated and presented in:
  - An LFDT Interoperability Workshop hosted by J.P. Morgan in Jersey City, NJ in February 2025: https://www.lfdecentralizedtrust.org/interoperability-workshop-2025?hs_preview=wjaeykIk-162942155838&hsLang=en.
  - A Cacti workshop/webinar organized by the LFDT in November 2025 on Zoom: https://www.youtube.com/watch?v=Bcqd475U0WA.

### Next Year's Goals
- Continue developing SATP implementations in Cacti, aligning closely with the standard as it develops through the IETF process to RFC status.
  - Maintainers who are authors of those standards specifications (Rafael, Rama) will ensure such alignment and prompt updates.
- Prioritize project cleanup and focus our maintenance efforts on packages with higher demand.
  - Please refer to the  [cleanup initiative](https://github.com/orgs/hyperledger-cacti/projects/2) and [SATP project board](https://github.com/orgs/hyperledger-cacti/projects/1/views/1).
- Improve OpenSSF and LFX Insights scores, especially those impacting security.
- Fix release automation and push releases (`v3.0.0` and up) throughout the year.
- Carry out more Cactus-Weaver integration as time permits.

### Help Required

Nothing in particular at this time. We are still trying to attract more contributors and maintainers, and we've had some help from the TAC in that respect: organizing a workshop in November 2025, for one.

## Project Lifecycle Status Recommendation

__Graduated__

(Despite the setbacks and reduced activity, we still have enough maintainer diversity to qualify, and we've continued to make progress toward the project's vision.)
