[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2025 Q3 Hyperledger Fabric

## Project Health

Hyperledger Fabric is fairly mature and stable with a v2.5 long-term support (LTS) release and a new v3.1 release.
There is less churn and fewer commits than in years past, with continued focus on quality, maintenance, and support.
New features get proposed, approved, and implemented based on a community RFC process.
Mailing list activity is down a bit compared to prior years.
PRs and mailing list questions are generally turned around quickly.
There is significant Discord activity.

## Questions/Issues for the TAC

None

## Releases

LTS release:
- v2.5 is the current LTS release with patch releases at least quarterly.

[Releases](https://github.com/hyperledger/fabric/releases) since last report:

- Fabric v2.5.13 - Apr 29, 2025
  - Dependency updates
- Fabric v3.1.1 - May 10, 2025
  - Bug fixes related to BFT

## Overall Activity in the Past Quarter

The project delivered patch releases for the Fabric v2.5 long-term support release. The patch releases primarily include updates to third party dependencies, as well as a few bug fixes. See [release notes](https://github.com/hyperledger/fabric/releases) for details.

The project also delivered the v3.1.1 release. The focus of the v3.1.1 release was to fix liveness bugs in the BFT implementation (deadlock and goroutine leaks). For details see the [v3.1.1 release note](https://github.com/hyperledger/fabric/releases/tag/v3.1.1).

## Current Plans

The project continues to maintain and keep Fabric v2.5 and v3.1 branches current (release-2.5 and main branches).

The project is largely in maintenance mode with only occasional new features. 

- There is a new [UX improvement PR](https://github.com/hyperledger/fabric/pull/5268) that will let BFT orderers rotate their enrollment certificate without the need of a channel update if the public key is preserved. Will appear in the next v3.1.2 release.


There is currently an RFC for [Private Chaincode Events](https://github.com/hyperledger/fabric-rfcs/pull/62) in progress. 

## Maintainer Diversity

5 of 9 [Fabric core maintainers](https://github.com/hyperledger/fabric/blob/main/MAINTAINERS.md) from IBM.

The IBM maintainers have been less active recently. If there are users or developers interested in becoming more active contributors, and eventually maintainers, the project could use your help!

## Contributor Diversity (past 90 days)

- 56% of code activities were performed by contributors from IBM.
- Remaining 44% by ATME, Oracle, LF, KFS, Hitachi, IdeaDLT, etc.
- Among the top 5 contributors, 3 are from IBM.
- Commit authors hail from the Israel(9%), USA(9%), Japan(5%), India(5%), and UK(5%)


## Additional Information

[Insights dashboard link](https://insights.linuxfoundation.org/project/fabric?timeRange=past90days&start=2025-05-24&end=2025-08-22)
