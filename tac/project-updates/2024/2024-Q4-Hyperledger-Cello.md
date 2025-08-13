[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2024 Q4 Hyperledger Cello

## Project Health

The Hyperledger Cello project maintains strong momentum and good health. Our key accomplishments and initiatives this quarter include:

* Technical Upgrades: Cello team upgraded Hyperledger Fabric to version 2.5.10 and modernized outdated command implementations, following our planned roadmap for infrastructure improvements.

* Development Environment Enhancement: Completed major modernization efforts by upgrading from Node.js v14 to v20, along with migrating from npm to yarn package manager. These changes have significantly improved the development experience.

* Mentorship Program: Our mentorship program has shown excellent results, with two mentees rapidly adapting to the project. They have gained deep understanding of the codebase and project architecture, contributing significantly to project development.

* Long-term Goals: Established clear objectives for future development, including:
    * Transitioning from command-line interfaces to Fabric SDK implementation

    * Expanding test coverage across the platform
    
    * Enhancing and expanding project documentation


## Questions/Issues for the TAC
N/A

## Releases
* v1.1.0-rc.1

## Overall Activity in the Past Quarter

The Cello team focuses on substantial strategic planning and technical enhancements in the past quarter. We began by establishing a comprehensive roadmap that outlines both short-term and long-term goals, providing clear direction for project development and community efforts.

A major focus of our activities centered on modernizing the project's infrastructure. After identifying outdated dependencies in both Node.js and Python components, we completed a major upgrade to Node.js v20 LTS, and upgrade Python Django to v4.2 LTS, improving development efficiency, we transitioned from npm to yarn as our package manager, which has increased build speeds and dependency management reliability.


We also upgraded our Hyperledger Fabric implementation from version 2.2.0 to 2.5.10, ensuring compatibility with the latest platform features. 

Throughout the quarter, we maintained project stability through active bug fixing and timely responses to GitHub issues, supporting our community of users and contributors.

### Current Plans

The Cello team is currently focused on several key technical initiatives. We are conducting testing of Hyperledger Fabric v2.5.10 chaincode operations, particularly with the approve and commit functionalities to ensure robust integration.

A significant effort is underway to clean and improve our test suite by removing outdated test cases and implementing new ones.

Additionally, we are evaluating stable Fabric SDKs as part of our planned transition from command-line tools to SDK-based implementation, scheduled for the coming year.

### Maintainer Diversity

We currently have four maintainers, with the following team members consistently contributing for over three months:

Baohua Yang (Oracle)
Feng Yang (H3C)
Yuanmao Zhu (Coinbase)
Xichen Pan (University of British Columbia)


### Contributor Diversity

In this quarter, the team had 20 pull requests. There are a total of 41 commits from 8 contributors.

### Additional Information
[Contribution Metrics](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=cello&routedFrom=Github&bestPractice=false&repository=all&dateFilters=2024-09-01%20to%202024-12-31&dateRange=2024-09-01%20to%202024-12-31&compare=PP&granularity=week&hideBots=true)
