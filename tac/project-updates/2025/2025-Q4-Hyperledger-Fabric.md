[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2025 Q4 Hyperledger Fabric

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

- Fabric v2.5.14 - October 13, 2025: Contains only dependency updates.
- Fabric v3.1.2 - October 13, 2025: Introduces minor UX improvements:
  - Extends admin REST API by allowing submission of config updates, formerly only possible through the regular broadcast gRPC API, by @pfi79
  - Extends admin REST API by allowing fetching of blocks, formerly only possible through the regular deliver gRPC API, by @pfi79
  - Allowing BFT orderers to have their enrollment certificates rotated without requiring a config update as long as the public keys remain the same, which further reducing the difference in administration to Raft orderers. Contributed by @dviejokfs.
- Fabric v3.1.3 - October 18, 2025: Urgent release which fixes a bug introduced in v3.1.2 that causes a docker mount issue when building the orderer Dockerfile. Does not affect binary builds or self provided Dockerfiles.

## Overall Activity in the Past Quarter

The project delivered patch releases for the Fabric v2.5 long-term support release. The patch releases primarily include updates to third party dependencies, as well as a few bug fixes. See [release notes](https://github.com/hyperledger/fabric/releases) for details.

The project also delivered the v3.1.2 and v3.1.3 releases. The former contains UX improvements and the latter fixes a bug introduced in the former release. 
For details see the [v3.1.2](https://github.com/hyperledger/fabric/releases/tag/v3.1.2) and [v3.1.3](https://github.com/hyperledger/fabric/releases/tag/v3.1.3) release notes.

## Current Plans

The project continues to maintain and keep Fabric v2.5 and v3.1 branches current (release-2.5 and main branches).

The project is largely in maintenance mode with only occasional new features. 

The RFC for [Private Chaincode Events](https://github.com/hyperledger/fabric-rfcs/pull/62) has been closed. 

## Maintainer Diversity

5 of 9 [Fabric core maintainers](https://github.com/hyperledger/fabric/blob/main/MAINTAINERS.md) from IBM.

The IBM maintainers have been less active recently. If there are users or developers interested in becoming more active contributors, and eventually maintainers, the project could use your help!

## Contributor Diversity (past 90 days)

- 62% of code activities were performed by contributors from IBM.
- Remaining 38% by ATME, LF, KFS, IdeaDLT, etc.
- Among the top 5 contributors, 1 is from IBM.
- Commit authors hail from the USA (11%), Australia, Bahrain, China and Spain (6%) and others.


## Additional Information

[Insights dashboard link](https://insights.linuxfoundation.org/project/fabric/contributors?timeRange=past90days&start=2025-07-20&end=2025-10-18)


## Project Structure and Governance Update

A significant update to the Hyperledger Fabric technical charter was merged, establishing a new governance structure. This change formally positions Hyperledger Fabric as an umbrella project, designed to host a family of Fabric-related projects.

This is detailed in a new [GOVERNANCE.md](https://github.com/hyperledger/fabric/blob/main/GOVERNANCE.md) file, which outlines the initial sub-projects and their respective Technical Steering Committees (TSCs) as of July 22, 2025:

* **Hyperledger Fabric:** Governed by a TSC composed of maintainers from the [`hyperledger/fabric`](https://github.com/hyperledger/fabric/blob/main/MAINTAINERS.md) and [`hyperledger/fabric-gateway`](https://github.com/hyperledger/fabric-gateway/blob/main/MAINTAINERS.md) repositories.
* **Hyperledger Fabric-X:** Governed by a TSC composed of maintainers from the [`fabric-x-endorser`](https://github.com/hyperledger/fabric-x-endorser), [`fabric-x-orderer`](https://github.com/hyperledger/fabric-x-orderer), [`fabric-x-committer`](https://github.com/hyperledger/fabric-x-committer), [`fabric-x-common`](https://github.com/hyperledger/fabric-x-common), and [`fabric-x`](https://github.com/hyperledger/fabric-x) repositories.

## Hyperledger Fabric-X

This new sub-project is currently in an incubation state and is expected to be ready for production deployment around the end of this year. Activity has been high, with 140 PRs from 21 contributors, though currently all 6 maintainers and all contributors are from IBM. The project is actively working to attract a broader community by conducting webinars (3 so far through LFDT) and is actively seeking new developers who can eventually become maintainers. 