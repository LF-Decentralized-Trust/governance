[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# Project Health

In the latest quarter, Hiero has grown considerably with new projects becoming part of the ecosystem. In recent TSC meetings, project maintainers conducted in-depth discussions and presentations of multiple project proposals and voted either to transfer the projects into the hiero-ledger organization or initiate new development aligned with the project specifications.

The list of issues show the recent [project proposals approved in recent weeks](https://github.com/hiero-ledger/tsc/issues?q=is%3Aissue%20state%3Aclosed%20label%3A%22project%20proposal%22). The specifics of these new projects will be discussed in more detail in the **Overall Activity** section below.

In the month of September and October, the Hiero maintainers participated in the re-structuring, clean and creation of the project's [Good First Issues](https://github.com/issues?q=is%3Aopen+is%3Aissue+org%3Ahiero-ledger+archived%3Afalse+label%3A%22good+first+issue%22+) attracting new contributors across the Hiero projects. During October's [Hacktoberfest](https://hacktoberfest.com/), the [hiero-sdk-python](https://github.com/hiero-ledger/hiero-sdk-python) in particular, saw a considerable increase of new contributons which will also be dicussed in the following sections. 

The LF Decentralized Trust is proud to welcome six of the Hiero project maintainers to January's [Member's Summit and Maintainer Days](https://www.lfdecentralizedtrust.org/member-summit-10th-anniversary) where three presentations will be taking part of the schedule. The team is also planning to boost colaboration with other maintainers from the communities represented in this event.

In general, the project is on track for seeing an increse in project participation and diversity with new organizations able to contribute to the new projects that are becoming part of the hiero-ledger organization.

# Questions/Issues for the TAC

There are no issues or questions to bring up to the TAC at this time.

# Releases

Below is a summary of the most notable recent releases for Q4:

- [hiero-sdk-js](https://github.com/hiero-ledger/hiero-sdk-js) - The team released [v2.78.0](https://github.com/hiero-ledger/hiero-sdk-js/releases/tag/v2.78.0), which  introduces improved network resilience and reliability within the SDK through an enhanced retry mechanism and corrected React Native polyfills. These updates ensure smoother transaction execution, automatic network correction, and consistent behavior across environments.
- [hiero-sdk-java](https://github.com/hiero-ledger/hiero-sdk-java) - [v2.64.0](https://github.com/hiero-ledger/hiero-sdk-java/releases/tag/v2.64.0) release that introduced fixes for disable retries when customer unsubscribes from a topic and do not call errorHandler when topic cancelled by client as well as some dependency changes.
- [hiero-sdk-go](https://github.com/hiero-ledger/hiero-sdk-go) - Release [v2.74.0](https://github.com/hiero-ledger/hiero-sdk-go/releases/tag/v2.74.0) introduces full support for HIP-1299, adding automatic retries, dynamic address book updates, and intelligent node failover to seamlessly handle node account ID rotations. It also adds the first set of programmable Hiero hooks starting with EVM hooks and account-allowance hooks by enabling customizable entity behavior.
- [hiero-solo-action](https://github.com/hiero-ledger/hiero-solo-action) - Release [v0.16.0](https://github.com/hiero-ledger/hiero-solo-action/releases/tag/v0.16.0) which forwards the grpc proxy port of node 2 if dual mode is enabled. It also brought in new contributions by new members.
- [hiero-sdk-cpp](https://github.com/hiero-ledger/hiero-sdk-cpp) - [v0.47.0](https://github.com/hiero-ledger/hiero-sdk-cpp/releases/tag/v0.47.0) updates several GitHub Actions and build dependencies while improving CI stability and tooling. It also adds NodeId validation and introduces request-timeout validation with a new grpcDeadline example to enhance reliability and developer experience.
- [hiero-mirror-node](https://github.com/hiero-ledger/hiero-mirror-node) - Release [v0.143.0](https://github.com/hiero-ledger/hiero-mirror-node/releases/tag/v0.143.0), delivers major progress on HIP-1195 hooks with full ingestion support, persistence of new transaction types, and a new REST API for listing an account’s hooks. It also advances HIP-1056 block stream compatibility with extensive testing and fixes, and introduces a rewritten Java-based network fees API that improves performance by 8x.
- [hiero-block-node](https://github.com/hiero-ledger/hiero-block-node) - Version [0.23.2](https://github.com/hiero-ledger/hiero-block-node/releases/tag/v0.23.2) includes a fix for update Unparsed Proto to support Block Footer.
- [hiero-consensus-node](https://github.com/hiero-ledger/hiero-consensus-node) - Release [v0.68.3](https://github.com/hiero-ledger/hiero-consensus-node/releases/tag/v0.68.3) includes several backports and cherry-picked improvements, including initializing from the latest block for streaming, expanded throttle accumulator tests, and alignment of gas throttling with throughput throttling. It also updates references from Hashgraph to the new Hiero-ledger packages.

Additionally, the [hiero blog](https://hiero.org/blog/) published several updates for the community:
- For a great part of these updates, the Python SDK project demostrated how the past [Hacktoberfest](https://hiero.org/blog/a-month-of-merges-how-hacktoberfest-turned-our-python-sdk-into-a-pull-request-party/) became really successful for the community in attracting new contributions and major development updates. At the same time, the Python SDK project announced several releases [v0.1.6](https://hiero.org/blog/hiero-python-sdk-announcing-release-v0.1.6/) and [v0.1.7](https://hiero.org/blog/hiero-python-sdk-announcing-release-v0.1.7/) which were reported by new community members. 
- As part of Hiero's 2026 goals, we are looking forward to make more project announcements to the community and provide more transparency overall. During this quarter, the Hiero blog published updates regarding the new [Hiero CLI](https://hiero.org/blog/join-the-next-chapter-of-the-cli-explore-hiero-cli/) project.
- The Hiero community also promoted Hiero's participation in [Hacktoberfest](https://hiero.org/blog/hacktoberfest-2025-contribute-to-hiero/) and called for action to all new contributors to participate for the first time in the project. 

Overall, it is a 2026 goal for the Hiero community to make release and roadmap information available and transparent to the community and the Python SDK project is exceeding expectations in this goal. We are inviting all Hiero project maintainers to also participate in the publication of their project roadmap in the TSC meetings, project events and project blog posts with the participation of the project's marketing group. 

# Overall Activity in the Past Quarter

## Project Proposals

In recent weeks, the Hiero project has approved the following project proposals, further expanding the ecosystem’s capabilities and accelerating development across its components. This is also a step forward towards building a strong and diverse community and attract more organizations to collaborate.
Included in these new projects we have:

- [hiero-ethereum-execution-spec-tests](https://github.com/hiero-ledger/hiero-ethereum-execution-spec-tests) - A fork of https://github.com/ethereum/execution-spec-tests to ensure Ethereum compatibility.
- [hiero-contracts](https://github.com/hiero-ledger/hiero-contracts) - A fork of https://github.com/hashgraph/hedera-smart-contracts exposing, grouping all the system-contracts, hiero hooks and any solidity interfaces or extension points of the hiero network.
- [identity-collaboration-hub](https://github.com/hiero-ledger/identity-collaboration-hub) - This hub is modeled after the existing SDK Collaboration Hub and will act as the unified home for identity-related standards, documentation, and source-code collaboration across the Hiero identity ecosystem.
- [hiero-enterprise-java](https://github.com/hiero-ledger/hiero-enterprise-java) - Transfer the project https://github.com/OpenElements/hiero-enterprise-java to Hiero.
- [hiero-cli](https://github.com/hiero-ledger/hiero-cli) - Command-line interface designed to simplify, automate, and accelerate development workflows on Hedera and Hiero networks.
- [homebrew-tools](https://github.com/hiero-ledger/homebrew-tools) - Central repository for maintaining Homebrew Formulas for Hiero tools.

At the moment, the TSC is reviewing an additional project proposal for [hiero-hol-specs](https://github.com/hiero-ledger/tsc/issues/261) which will serve as the canonical repository for Hashgraph Consensus Standards (HCS), which define application-layer metaprotocol specifications built on the Hiero Consensus Service.

## Community Calls

The public calendar continues to expand including new ways that the community can participate in the Hiero project. These meetings includes:
- **Marketing and Community Engagement Meeting** - Where the community can interact with the marketing team to promote events, plan semminars and overall expand the project's visibility to the open source community
- **Maintainers Monthly Meeting** - Maintainers can gather once a month to discuss issues and plan strategies to encourage participation and reduce project bottlenecks.
- **Identity Community Call** - Discuss all the latest and greatest in Decentralized Identity on Hiero/Hedera. Target participants can include operators of identity platforms supporting Hedera, and developers interested in using and contributing to Hiero identity repos.
- **Hiero SDKs Good First Issue Refinement** - Teams meet to cleanup and create new good first issues to attract new participants to the community.

The team also created a [public wiki site](https://github.com/hiero-ledger/governance/wiki) to host more information for all project meetings and help members identify oportunities where they can participate in the project.

## Community Exposure and Events

The Hiero project successfully concluded its participation on October's Hacktoberfest where new contributors where invited to explore the project and contribute to it. This event resulted in the total contribution of [137 issues closed](https://github.com/issues?q=is%3Aclosed%20is%3Aissue%20org%3Ahiero-ledger%20archived%3Afalse%20label%3A%22good%20first%20issue%22%20closed%3A%3E%40today-90d&page=1) across several Hiero projects. As a highlight, the [Python SDK project exceeded expectations](https://hiero.org/blog/a-month-of-merges-how-hacktoberfest-turned-our-python-sdk-into-a-pull-request-party/) by attracting 39 new authors who contributed to 74 merged pull requests just in the month of October.

For LFDT's upcomming Maitainer Days in Jan, the Hiero project is contributing to three presentations discussing strategies to atract and guide new contributors via good first issues, promote open source collaboration best practices and build healthy open source ecosystems with diverse stakeholders. 

Additionally, the community is implementing new ways to track overall project exposure to the release and project updates announcements. One of these metrics is the implementation of Google Analytics for the hiero.org webpage as well as the Hiero's blog. The Google Analytics data for hiero.org indicates that the main page accounts for 72% of all page views with 1,385 views and 782 active users. Compared to this, the Hiero blog contributs 10% of total views, while individual blog posts each capture between 1–2% of traffic. While these statistics are a bit low, we are expecting to register more views as 2026 new goals take place regarding project updates and transparency.

# Current Plans

The Hiero community's main focus is to shape 2026 Project Goals. These goals have a strong focus on strengthening the project’s long-term sustainability by growing a diverse, engaged community and implementing practices that encourage contributor and maintainer retention. On the security front, we are looking to implement practices that polish our overal CI/CD practices and hardens our overall security. We are also inviting leaders and maintainers of the project's core component and sub-projects to maintain their own technical roadmap and report progress to the Hiero TSC, enabling transparent planning and effective cross-project coordination. The project will continue serving as the community-governed home for specifications and reference implementations derived from Hedera standards, with an emphasis on consistent and open stewardship of these specifications. The project will also expand community engagement through training, collaboration opportunities, and initiatives that welcome new talent while demonstrating real world adoption through documented use cases and public references. Finally, Hiero will invest in future-readiness by exploring emerging technologies, advancing research prototypes, and deepening technical collaboration across the LFDT ecosystem to promote interoperability and shared innovation.

# Maintainer Diversity

The Hiero project still has some [project proposals in the pipeline](https://github.com/hiero-ledger/tsc/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22project%20proposal%22) to be reviewed and discussed in the short future. This will open new doors for new maintainers from diverse organizations to find an oportunity to participate in the project development.

In summary, the [following repos have received changes](https://github.com/hiero-ledger/governance/commits/main/config.yaml?since=2025-09-04&until=2025-12-03): 

- Release Managers team aquire a new maintainer.
- Hiero Consensus Node aquire a new maintainer.
- Identity Collaboration Hub has two new community maintainers working along two of our current maintainers.
- Hiero Contracts Maintainers bring in several new maintainers into the project.
- Hiero Ethereum Execution Spec bring in several new maintainers into the project.

## TODO: Add organization representation graph 

# Contributor Diversity (NEEDS WORK)

Projects in Hiero continue to promote more participation from external contributors. For example, the Python SDK team recently held one of their [Office Hours events](https://hiero.org/blog/introducing-the-hiero-python-sdk-office-hour/) to help the community get started, understand the project's proposed feature requests, get familiar with the codebase, troubleshooting their tests and even help new collaborators create their first PR.

Our workshop to help users create their own test network and communicate to it via our SDKs will continue to be promoted in future events.

Our [latest community calls](https://hiero.org/#contribute) are easily visible for the community to select one and join with the rest of the maintainers. For any of these calls, there are no expertise requirements. We welcome anyone in the community interested in using, adopting and contributing to Hiero.

In this quarter, 50% of the organization dependency continues to belong to Hashgraph and LimeChain among [35 active companies collaborating](https://insights.linuxfoundation.org/project/hiero/contributors?timeRange=custom&start=2025-06-20&end=2025-09-04&widget=organization-dependency) in GitHub commits/issues/discussions. 

Overall, [266 organizations](https://insights.linuxfoundation.org/project/hiero/contributors?timeRange=alltime&widget=organization-dependency) have contributed to Hiero activities (compared to 199 organizations reported in Q2). The team continues to seek diversity and promote more inclusion of new organizations and participating maintainers. It is a goal as a community overall to increase the number of participating organizations to be able to preserve project status.

# Additional Information

The Hiero project is actively working on defining and shaping its 2026 goals with a strong focus on maturity, transparency, and ecosystem growth. These goals will emphasize increased project participation and community engagement, strengthened security practices and greater transparency across all project activities. The goals will also includes more consistent publication of releases and transparency of project roadmaps and releases, enhanced stewardship of core specifications and continued investment in high-quality reference implementations and innovation. Additionally, training initiatives and deeper cross-project collaboration will play a central role in ensuring that Hiero continues to evolve as a trusted, vendor-neutral project.
