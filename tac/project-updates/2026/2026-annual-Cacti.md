[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Annual Review Cacti

## Project Health

- Overall, the project is progressing in its mission and fulfilling its goals, despite meeting setbacks related to the reduction of active maintainers
- Specifically, we lost Accenture as a maintainer, and Fujitsu's and IBM's contributions have diminished as their maintainers have other commitments.
- An increase in activity has been observed by members of INESC-ID, namely André Augusto and Carlos Amaro, in addition to Rafael Belchior.
- Thanks primarily to the Blockdaemon maintainers, Cacti continues to be the leading implementor and adopter of the IETF's Secure Asset Transfer Protocol (SATP) interoperability standard.
- We successfully concluded a mentorship project where we made more progress on the Cactus-Weaver intgeration, and conducted a workshop in November 2025 showcasing the recent SATP-related developments in Cacti.
- We are generally active on Discord, interacting with the LFDT and open-source community. Some maintainers continue to be key shapers of DLT interoperability standards by participating in the IETF's SATP working group.
- We faced technical issues pushing new full releases because of the move from the `hyperledger` to the `hyperledger-cacti` organization, but we have identified the reasons and are actively engaged in pushing a v3 release. Instead, we pushed a separate beta release just for the SATP-related packages and examples.
- We are committed to improve the Cacti codebase, notably with the [cleanup initiative](https://github.com/orgs/hyperledger-cacti/projects/2) as the guiding light
- The SATP-Hermes implementation of IETF's Secure Asset Transfer Protocol is [publicly tracked](https://github.com/orgs/hyperledger-cacti/projects/1/views/1). Highlights include release SATP v0.0.3-beta, which adds supporting packages to SATP such as bungee-hermes and updates to the Ethereum and Besu connectors. 
  - In greater detail, for SATP we delivered data transfer functionality (oracle), in release 0.0.1-beta;  gateway monitoring and dashboard, test and ci improvements, and bug fixes ( 0.0.2-beta release), documentation and bug fixes, support for NFT transfers, and refactored the SATP bridge. For the next release, we are planning to deliver the adapter layer and audit endpoints.

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
- Continue developing SATP implementations in Cacti
- Supporting high-priority packages
- Prioritize project cleanup and resource allocation to packages with higher demand
  
### Performance Against Prior Goals
Please refer to the  [cleanup initiative](https://github.com/orgs/hyperledger-cacti/projects/2) and [SATP project board](https://github.com/orgs/hyperledger-cacti/projects/1/views/1)

### Next Year's Goals
- Continue developing SATP implementations in Cacti
- Supporting high-priority packages
- Prioritize project cleanup and resource allocation to packages with higher demand

### Help Required


## Project Lifecycle Status Recommendation

`Graduated`
