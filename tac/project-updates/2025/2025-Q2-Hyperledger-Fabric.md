---
layout: default
title: 2025 Q2 Hyperledger Fabric
parent: 2025
grand_parent: Project Updates
---

# Project Health

Hyperledger Fabric is fairly mature and stable with a v2.5 long-term support (LTS) release and a new v3.1 release.
There is less churn and fewer commits than in years past, with continued focus on quality, maintenance, and support.
New features get proposed, approved, and implemented based on a community RFC process.
Mailing list activity is down a bit compared to prior years.
PRs and mailing list questions are generally turned around quickly.
There is significant Discord activity.

# Questions/Issues for the TAC

None

# Releases

LTS release:
- v2.5 is the current LTS release with patch releases at least quarterly.

[Releases](https://github.com/hyperledger/fabric/releases) past quarter:
- Fabric v2.5.11 - January 31, 2025
- Fabric v2.5.12 - March 10, 2025
- Fabric v3.1.0 - March 18, 2025

# Overall Activity in the Past Quarter

The project delivered patch releases for the Fabric v2.5 long-term support release. The patch releases primarily include updates to third party dependencies, as well as a few bug fixes. See [release notes](https://github.com/hyperledger/fabric/releases) for details.

The project also delivered the v3.1 release. The focus of the v3.1 release was to add support for batch updates for chaincodes that read or write many keys. For details see the [v3.1.0 release note](https://github.com/hyperledger/fabric/releases/tag/v3.1.0).

Publishing images to GitHub Container Registry has been an objective and this work has now been completed for the various fabric repositories. The Dockerhub images will continue to be pushed as well so as to not break any existing users. Additionally the GitHub Actions have been updated to build the amd64 and arm64 images natively, this has proved to more reliable and faster than using the prior emulation approach using qemu.

# Current Plans

The project continues to maintain and keep Fabric v2.5 and v3.1 branches current (release-2.5 and main branches).

The project is largely in maintenance mode with only occasional new features. There is currently an RFC for [Private Chaincode Events](https://github.com/hyperledger/fabric-rfcs/pull/62) in progress. 

# Maintainer Diversity

5 of 9 [Fabric core maintainers](https://github.com/hyperledger/fabric/blob/main/MAINTAINERS.md) from IBM.

The IBM maintainers have been less active recently. If there are users or developers interested in becoming more active contributors, and eventually maintainers, the project could use your help!

# Contributor Diversity

- 65% of code activities were performed by top 3 contributors. Remaining 35% performed by 47 other contributors.
- Of top 10 contributors, 4 of 10 from IBM.

# Additional Information

[Insights dashboard link](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=fabric&routedFrom=Github&bestPractice=false&repository=all&dateFilters=Last%20Quarter&dateRange=2025-01-01%20to%202025-03-31&compare=PP&granularity=week&hideBots=true)