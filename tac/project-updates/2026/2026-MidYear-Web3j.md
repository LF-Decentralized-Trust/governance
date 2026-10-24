[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Mid-Year Review of Web3j

# Progress Against 2026 Goals

This review covers progress since the 2026 annual review through August 15, 2026, with monthly usage metrics from July through September 30, a September maturity snapshot and a development and maintenance update dated October 21, 2026. The original LFX activity figures and release list retain their August reporting cutoff. The newer metrics below have their own stated periods and scopes. Web3j remains an `incubation` project.

## Project Health

LF Decentralized Trust Web3j [LFX Insights Dashboard](https://insights.linuxfoundation.org/project/web3j)

Since the beginning of this year, we have seen several new contributors, as well as continued evidence of Web3j usage by other companies, similar to what we observed during the first months of 2025. There has been a small decrease in the number of contributors, which is discussed in the following sections.

Contributors have shown less interest in joining the biweekly Web3j Contributors meetings ([calendar](https://zoom-lfx.platform.linuxfoundation.org/meetings/lf-decentralized-trust?view=month)). As a result, the current maintainers have moved project communication and updates primarily to Discord.

Discord remains active.

Highlights from the 2026 LFX Insights report at the original August reporting cutoff:

- 42 contributors
- 349 commits
- 75% of code activity was performed by one organization (Web3 Labs), a decrease of 1 percentage point compared with last year
- 12 active organizations, 6 fewer than in the previous period

### Maturity — September 2026 snapshot

As of September 2026, the [core Web3j repository](https://github.com/LFDT-web3j/web3j) has recorded 232 unique contributors, 2,591 commits and 123 releases since 2016. These cumulative figures reflect a decade of open-source development and complement the year-to-date LFX activity figures above.

### Agent-assisted development and maintenance — 21 October 2026

Web3j is making greater use of agentic capabilities across development and maintenance to make better use of maintainers' time. By automating routine investigation, preparing reviews and assisting with implementation, the project can focus human attention on assessing changes and keeping the library reliable for its users.

Since September, scheduled agents have been collecting issues and pull requests across the Web3j repositories, preparing reviews, checking Ethereum specification changes and producing ecosystem health briefs. Governance deadlines and TAC review follow-ups are now included in the weekly checks. These jobs provide evidence and recommendations for maintainers; implementation proceeds through separately authorized work, with human review and merge decisions.

This approach is already contributing to practical improvements. On 21 October, Conor merged [Web3j PR #2315](https://github.com/LFDT-web3j/web3j/pull/2315), developed with agent assistance, to improve validation and publication from the same commit. Build, integration tests and CodeQL passed on the merged revision, and the [snapshot publication workflow](https://github.com/LFDT-web3j/web3j/actions/runs/39586680664) completed successfully.

The immediate focus is routine maintenance: triaging issues, assessing contributed fixes, keeping builds and releases reliable, and identifying Ethereum compatibility work. Agentic tooling provides a practical way to cover more of this work within the time maintainers have available. Priorities and release timing remain guided by user impact, validated changes and available capacity.

## Releases

### Web3j

The project delivered 3 releases in 2026 ([Releases](https://github.com/LFDT-web3j/web3j/releases)):

- v5.0.2 - January 21, 2026
- v5.0.3 - May 27, 2026
- v6.0.0 - June 29, 2026

### web3j-evm

The project delivered 4 releases in 2026 ([Releases](https://github.com/LFDT-web3j/web3j-evm/releases)):

- v5.0.1 - January 16, 2026
- v5.0.2 - February 5, 2026
- v5.0.3 - June 17, 2026
- v6.0.0 - June 30, 2026

### web3j-unit

The project delivered 5 releases in 2026 ([Releases](https://github.com/LFDT-web3j/web3j-unit/releases)):

- v5.0.1 - January 16, 2026
- v5.0.1-hf - January 19, 2026
- v5.0.2 - February 6, 2026
- v5.0.3 - June 18, 2026
- v6.0.0 - June 30, 2026

### web3j-sokt

The project delivered 1 release in 2026 ([Releases](https://github.com/LFDT-web3j/web3j-sokt/releases)):

- v0.6.0 - January 15, 2026

### web3j-solidity-gradle-plugin

The project delivered 1 release in 2026 ([Releases](https://github.com/LFDT-web3j/web3j-solidity-gradle-plugin/releases)):

- v0.6.1 - January 16, 2026

### web3j-gradle-plugin

The project delivered 1 release in 2026 ([Releases](https://github.com/LFDT-web3j/web3j-gradle-plugin/releases)):

- v5.0.2 - January 29, 2026

### web3j-maven-plugin

The project delivered 1 release in 2026 ([Releases](https://github.com/LFDT-web3j/web3j-maven-plugin/releases)):

- v5.0.2 - January 31, 2026

### web3j-cli

The project delivered 1 release in 2026 ([Releases](https://github.com/LFDT-web3j/web3j-cli/releases)):

- v1.8.0 - February 9, 2026

## Maintainer Diversity

At the August reporting cutoff, the report identified three active maintainers, all from Web3 Labs. Paid maintainer capacity remains limited following the funding change described in the [1 September response](https://github.com/LF-Decentralized-Trust/governance/pull/360#discussion_r3904128245). The growing use of agentic tooling is intended to reduce the time required for routine development and maintenance. Conor's available time is focused on core maintenance and review; individual maintainers' continuing involvement depends on their own availability. Contributions from the wider JVM and Ethereum community remain valuable in broadening the maintainer base.

The [MAINTAINERS.md file](https://github.com/LFDT-web3j/web3j/blob/main/MAINTAINERS.md) records the listed maintainers; their current availability and responsibilities need to be reconfirmed.

Web3j participated in the 2026 LF Decentralized Trust Mentorship Program for the third time. At the August reporting cutoff, the following mentorship was ongoing:

1. [LFDT - Web3j Libraries Full Development Lifecycle](https://mentorship.lfx.linuxfoundation.org/project/54546ffa-df1d-4985-a366-0e03780f5208/mentees), which was progressing well and helping the project achieve its roadmap goals and close open issues. The August report attributed all repository commits since the mentorship began to that work.

Contributors can use the project's CONTRIBUTING.md guidance to prepare reproductions, tests, fixes and new functionality for review through GitHub.

## Project Adoption

According to Scarf.sh, Web3j recorded approximately 4.3 million Maven Central downloads during September 2026.

### Usage — July–September 2026

**Sources: Maven Central and Scarf.sh.** The following rounded figures cover download activity for the `org.web3j` namespace. September covers the full calendar month, 1–30 September. Scarf's [free plan](https://about.scarf.sh/pricing/) only provides access to the most recent three months of data.

| Metric | July 2026 | August 2026 | September 2026 |
| --- | --- | --- | --- |
| Downloads | ~4.6 million | 4.3 million | 4.3 million |
| Unique download sources | 34,000 | 35,500 | 47,100 |
| Companies identified from download traffic | — | 2,000 | 3,300 |

According to Scarf.sh's figures, unique download sources increased by approximately 39% from July to September, including approximately 33% growth from August to September. Scarf.sh also reports around 4.3 million downloads in both August and September.

July's company count is not available.

These figures measure download activity across the namespace. Unique sources are not necessarily individual developers, and traffic-identified companies are not a verified count of production deployments. Monthly unique-source and company counts can overlap across months. October activity is excluded.

The [core GitHub repository](https://github.com/LFDT-web3j/web3j) had approximately 5,400 stars and 1,800 forks in September 2026.

The project does not maintain an ADOPTERS file because it is difficult to keep this information up to date, and the project does not want to misrepresent actual adoption or give preference to certain vendors.

To promote new features, several blog posts were published:

- [Web3j 5.0.2: A Community Release That Moves Us Forward](https://www.lfdecentralizedtrust.org/blog/web3j-5.0.2-a-community-release-that-moves-us-forward)
- [Web3j 6 Release: Fusaka and Agentic Ready](https://www.lfdecentralizedtrust.org/blog/web3j-6-release-fusaka-and-agentic-ready)
- [How to Create and Validate EIP-4844 Blob Transactions With Sidecar](https://www.lfdecentralizedtrust.org/blog/how-to-create-and-validate-eip-4844-blob-transactions-with-sidecar)

## Goals

### Performance Against Prior Goals

During the first part of this year, the project has achieved or made progress toward the following goals:

- Update the project roadmap - DONE
- Continue maintenance and resolve issues - ONGOING, with greater use of agentic tooling to make effective use of maintainer time. Releases follow validated changes and available capacity.
- Continue enhancing support for the Prague/Electra Upgrade - DONE
- Fusaka Upgrade support - DONE
- Glamsterdam Upgrade
- Updates to web3j-unit and web3j-evm
- Improve the process for generating Kotlin wrappers for Solidity smart contracts

### Help Required

Web3j's established user base provides an opportunity for downstream organizations to contribute to the library they rely on. Useful contributions include issue reproductions and regression tests, reviews of transaction encoding and signing changes, Ethereum compatibility work, CI and release engineering, documentation, and testing generated applications across the related tooling.

The proposed requests to LFDT are:

- Introductions to organizations that rely on Web3j and could contribute funded maintainer time, sponsorship, or recurring engineering support.
- Help recruiting additional JVM/Ethereum reviewers and maintainers, including someone able to share release and incident responsibilities.
- Promotion of existing contribution opportunities through LFDT's channels, with an emphasis on practical engineering contributions to routine maintenance.

## Project Lifecycle Status Recommendation

This report recommends continuing the `incubation` status. Web3j combines a decade of development and substantial ongoing usage with an evolving approach to maintenance. Greater use of agentic tooling, human review and improved release automation supports continued development within available maintainer time. Broadening community participation and access to funded engineering support remain useful next steps for the project.
