[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Mid-Year Review of Web3j

# Progress Against 2026 Goals

This review covers progress since the 2026 annual review through August 15, 2026. Web3j remains an active `incubation` project.

## Project Health

LF Decentralized Trust Web3j [LFX Insights Dashboard](https://insights.linuxfoundation.org/project/web3j)

Since the beginning of this year, we have seen several new contributors, as well as continued evidence of Web3j usage by other companies, similar to what we observed during the first months of 2025. There has been a small decrease in the number of contributors, which is discussed in the following sections.

Contributors have shown less interest in joining the biweekly Web3j Contributors meetings ([calendar](https://zoom-lfx.platform.linuxfoundation.org/meetings/lf-decentralized-trust?view=month)). As a result, the current maintainers have moved project communication and updates primarily to Discord.

Discord remains active.

Highlights from the 2026 Insights report so far:

- 42 contributors
- 349 commits
- 75% of code activity was performed by one organization (Web3 Labs), a decrease of 1 percentage point compared with last year
- 12 active organizations, 6 fewer than in the previous period

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

At the moment, there are only 3 active maintainers, all from Web3 Labs. They have been the project's maintainers since it was donated to LF Decentralized Trust. During the second half of 2026, Web3 Labs stopped funding and supporting Web3j contributions. This may have a significant impact on the project's ongoing maintenance. The current maintainers will continue their efforts to maintain Web3j despite the loss of the previous funding and support.

The MAINTAINERS.md file is up to date and can be found [here](https://github.com/LFDT-web3j/web3j/blob/main/MAINTAINERS.md).

The project is happy to mentor anyone interested in becoming a contributor or future maintainer. In terms of mentoring, Web3j is participating in the 2026 LF Decentralized Trust Mentorship Program for the third time. One mentorship is currently ongoing:

1. [LFDT - Web3j Libraries Full Development Lifecycle](https://mentorship.lfx.linuxfoundation.org/project/54546ffa-df1d-4985-a366-0e03780f5208/mentees), which is progressing well and helping the project achieve its roadmap goals and close a considerable number of open issues. Since the mentorship began, all commits made to the repositories have been part of the mentorship work.

The Web3j maintainers also mentor new contributors who are interested in resolving open issues in the project repositories—many of which are easy to fix—or in adding new functionality to the project. Prospective contributors can find detailed instructions in the project's CONTRIBUTING.md file and are encouraged to seek help through GitHub comments or Discord.

## Project Adoption

Based on research into enterprise users of Web3j, at least 10 organizations are using Web3j in production, according to the available statistics. This represents 3 fewer organizations than in the same period last year.

The project does not maintain an ADOPTERS file because it is difficult to keep this information up to date, and the project does not want to misrepresent actual adoption or give preference to certain vendors.

Developers occasionally organize events to showcase Web3j features and help increase enterprise adoption.

To promote new features, several blog posts were published:

- [Web3j 5.0.2: A Community Release That Moves Us Forward](https://www.lfdecentralizedtrust.org/blog/web3j-5.0.2-a-community-release-that-moves-us-forward)
- [Web3j 6 Release: Fusaka and Agentic Ready](https://www.lfdecentralizedtrust.org/blog/web3j-6-release-fusaka-and-agentic-ready)
- [How to Create and Validate EIP-4844 Blob Transactions With Sidecar](https://www.lfdecentralizedtrust.org/blog/how-to-create-and-validate-eip-4844-blob-transactions-with-sidecar)

## Goals

### Performance Against Prior Goals

During the first part of this year, the project has achieved or made progress toward the following goals:

- Update the project roadmap - DONE
- Continue to provide maintenance, resolve issues, and release at least once a month - ONGOING; releasing every month has been difficult due to limited maintainer availability
- Continue enhancing support for the Prague/Electra Upgrade - DONE
- Fusaka Upgrade support - DONE
- Glamsterdam Upgrade
- Updates to web3j-unit and web3j-evm
- Improve the process for generating Kotlin wrappers for Solidity smart contracts

### Help Required

We continue to work with LFDT staff to organize events and identify contributors and potential maintainers.

LF Decentralized Trust can help with the following:

- Promote the Web3j project within the LF Decentralized Trust community
- Help attract active contributors who could eventually commit to serving as maintainers

## Project Lifecycle Status Recommendation

This report recommends continuing the `incubation` status.