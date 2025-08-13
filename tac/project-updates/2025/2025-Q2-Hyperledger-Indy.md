[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2025 Q2 Hyperledger Indy

## Project Health

Over the past quarter, the Indy community has been actively working on upgrading components to support Ubuntu 22.04, with significant collaboration happening on Discord. Key progress includes updates to CI/CD workflows, test automation, and the Indy VDR upgrade for Plenum. The project remains highly stable, with globally deployed networks running smoothly and ongoing efforts focused on long-term maintainability and security improvements.

## Questions/Issues for the TAC

There are no issues at this time.

## Releases

The current focus is the Ubuntu 22.04 upgrade, so there have been no releases in this first quarter.

Most recent prior release:
- [indy-node v1.31.2](https://github.com/hyperledger/indy-node/releases/tag/v1.13.2)
- [indy-plenum v1.31.1](https://github.com/hyperledger/indy-plenum/releases/tag/v1.13.1)

## Overall Activity in the Past Quarter

Progress on the project is going well. The primary focus of the current technical work is upgrading Hyperledger Indy components to support Ubuntu 22.04.

There has been significant community activity, particularly on the Discord server. The Ubuntu-related channels are highly active, with maintainers responding promptly and consistently. Notably, there has been a lot of engagement in the ##indy, #indy-node, and #indy-ubuntu-2204-upgrade channels.

Although the team initially experimented with using Tatsu for standups, it proved ineffective, and coordination has since moved back to Discord.

Key areas of work include:
- Updating CI/CD workflows to support Ubuntu 22.04
- Upgrading indy-test-automation to support Ubuntu 22.04
- Indy VDR upgrade for Plenum
    - Progressing unit test pass rates
    - Next step will be to build a new release of Plenum
- Indy VDR upgrade for Node following the upgrade in Plenum.

The GitHub organization transition is planned for after the removal of obsolete dependencies.

The Quebec team has made significant contributions to this work. Although they have been temporarily reassigned due to a leadership change, they may rejoin the project in June.

Hyperledger Indy remains a highly stable project. As a result of this stability, there are numerous scaled deployments of Indy networks operating reliably across the globe. Demand for new features in the existing Indy Node and Plenum codebases is low, reflecting the maturity and robustness of the platform. Efforts are ongoing to maintain and strengthen this level of stability, ensuring that production-grade Indy networks continue to serve critical identity infrastructure needs worldwide.

## Current Plans

- Complete the upgrade to Ubuntu 22.04
- Complete the GitHub organization change
- Increase OpenSSF Scorecard rating
    - Ensure that individual releases are signed
    - Implement token permissions model
    - Introduce tooling for pinned dependencies (use dependabot report tooling), fuzzing, and SAST
    - Ensure that OpenSSF detects branch protections and packaging practices
    - Add code quality checking for project commits
    - Reformat code base
    - Add poetry package management


## Maintainer Diversity

There are currently 14 maintainers. The maintainers and teams can be seen in the [Governance Access Control YAML file](https://github.com/hyperledger/governance/blob/main/access-control.yaml).


## Contributor Diversity

|Rank|Organization                   |Activities|% Contributions|Change|
|----|-------------------------------|----------|---------------|------|
|1   |Quartech Systems               |47        |35.07%         |+4    |
|2   |Sovrin Foundation              |41        |30.60%         |+32   |
|3   |Indicio                        |29        |21.65%         |+26   |
|4   |The Linux Foundation           |9         |6.72%          |+1    |
|5   |Animo Solution                 |3         |2.24%          |+3    |
|6   |DSR Corporation                |2         |1.49%          |-25   |

Source: [LFX Insights](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=indy&routedFrom=Github&bestPractice=false&repository=all&dateFilters=Last%20Quarter&dateRange=2025-01-01%20to%202025-03-31&compare=PP&granularity=week&hideBots=true)

## Additional Information

A new use case reported within the first quarter: [South African blockchain-powered Uber rival](https://mybroadband.co.za/news/internet/580104-south-african-blockchain-powered-uber-rival.html?utm_campaign=LFDT%20Decentralized%20Digest&utm_medium=email&_hsmi=345935392&utm_content=345936564&utm_source=hs_email)

"South African ride-hailing platform Twytch uses blockchain technology to improve passenger and driver safety by verifying both users’ identities while ensuring that this private data is not vulnerable to a data breach…To protect this personal information from data breaches, Secure Citizen uses the Hyperledger Indy blockchain, which is specifically designed to manage digital identities."
