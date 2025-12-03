[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# Project Health

In the latest quarter, Hiero has grown considerably with new projects becoming part of the ecosystem. In recent TSC meetings, project maintainers conducted in-depth discussions and presentations of multiple project proposals and voted either to transfer the projects into the hiero-ledger organization or initiate new development aligned with the project specifications.

The list of issues show the recent [project proposals approved in recent weeks](https://github.com/hiero-ledger/tsc/issues?q=is%3Aissue%20state%3Aclosed%20label%3A%22project%20proposal%22). The specifics of these new projects will be discussed in more detail in the **Overall Activity** section below.

In the month of September and October, the Hiero maintainers participated in the re-structuring, clean and creation of the project's [Good First Issues](https://github.com/issues?q=is%3Aopen+is%3Aissue+org%3Ahiero-ledger+archived%3Afalse+label%3A%22good+first+issue%22+) attracting new contributors across the Hiero projects. During October's [Hacktoberfest](https://hacktoberfest.com/), the [hiero-sdk-python](https://github.com/hiero-ledger/hiero-sdk-python) in particular, saw a considerable increase of new contributons which will also be dicussed in the following sections. 

The LF Decentralized Trust is proud to welcome six of the Hiero project maintainers to January's [Member's Summit and Maintainer Days](https://www.lfdecentralizedtrust.org/member-summit-10th-anniversary) where three presentations will be taking part of the schedule. The team is also planning to boost colaboration with other maintainers from the communities represented in this event.

In general, the project is on track for seeing an increse in project participation and diversity with new organizations able to contribute to the new projects that are becoming part of the hiero-ledger organization.

# Questions/Issues for the TAC

There are no issues or questions to bring up to the TAC at this time.

# Releases (NEEDS WORK)

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

The community is implementing new ways to track overall project exposure to the release and project updates announcements. One of these metrics is the implementation of Google Analytics for the hiero.org webpage as well as the Hiero's blog. The Google Analytics data for hiero.org indicates that the main page accounts for 72% of all page views with 1,385 views and 782 active users. Compared to this, the Hiero blog contributs 10% of total views, while individual blog posts each capture between 1–2% of traffic. While these statistics are a bit low, we are expecting to register more views as 2026 new goals take place regarding project updates and transparency.


# Overall Activity in the Past Quarter (NEEDS WORK)

The Hiero project is building traction and momentum in our goal to acquire more collaborators and participants. Our [community calls](https://zoom-lfx.platform.linuxfoundation.org/meetings/hiero?view=week) continue to run and recently we were able to host a new Solo Community call, Python SDK Office Hours and Website community call. We also had a short series of calls to discuss the direction of the projects and the baseline and requirements for new projects to join hiero-ledger. We continue to promote openness in the community and continue to welcome the opinion of new users.

The community was able to obtain Graduated project status. Each repo in hiero-ledger comforms to the TAC guidelines for repo structure, security policies and quality of the code. We continue to work on adopting more [community projects](https://github.com/hiero-ledger/hiero/blob/main/community-transition.md) and seeking the participation of new members from different backgrounds and affiliations.

The project maintainers are helping to shape the scores from the OpenSSF reports. We have been working on improving the overall project quality by focusing in the reports obtained by our tools like GitHub Insights, LFX Insights, OpenSSF, Snyk and Step Security.

# Current Plans (NEEDS WORK)

The Hiero project continues to build momentum, with community awareness and adoption receiving continuous expansion. Current priorities include preparing for upcoming conference participation, expanding the contributor and maintainer base, and reinforcing the project’s foundation by leveraging metrics tools and implementing strong security measures to guard against vulnerabilities and potential threats.

The project will continue to work with the LFDT TAC to maintain and preserve project status. The main areas of focus will be the project's diversity in contributors and maintainers as well as the improvement of OpenSSF scoring. In the following month, the TSC will renew one TSC position for Contributor Seat with the rest of the governance. We are organizing a Maintainer's Community Call that will allow us to work with the maintainers and explain the roles, participation and impact that the members of the TSC in the project along with how they can influence their desision making when selecting new candidates.

We are also continuing our efforts in cross-project collaboration with other open source communities. The team has started a communication with the Identus maintainers to potentially bring in Hiero's usage for the Identus project development. 

Additionally, the project is planning a First Year Anniversary webinar to promote the project's achievement and welcome interested audiences to participate in the project.

# Maintainer Diversity (NEEDS WORK)

In Q3 we continue to add new projects into our hiero-ledger organization.
- [hiero-hederium](https://github.com/hiero-ledger/hiero-hederium) - Hederium is Golang implementation of Hedera JSON-RPC Relay or Hashio.
- [hiero-did-sdk-js](https://github.com/hiero-ledger/hiero-did-sdk-js) - A TypeScript/JavaScript SDK for building decentralized identity solutions on Hiero.
- We are currently working on transfering hiero-cli.

In summary, the [following repos have received changes](https://github.com/hiero-ledger/governance/commits/main/config.yaml?since=2025-06-14&until=2025-09-04): 

- Create the hiero-cli-committers team with several new members. 
- Nominations are created for the upcoming September elections.
- LFStaff received an update with one more member.
- Additional Roles for supporting onboarding & management are created.
- Block Node received a re-structuring of their maintainers team.
- Python SDK acquired a new maintainer.
- Contributors are allowed to perform triage activities for sdk-tck and sdk-js.
- Consensus Node maintainers team acquired two new members.
- Added new maintainers team for hashgraph online.

As of today, maintainers in the Hiero Ledger organization are primarily represented by contributors from Hashgraph and LimeChain. The entire composition of the maintainers affiliation can he found [here](https://docs.google.com/spreadsheets/d/1O4wTFxw9rUQbgc3YvCKyDYlAKwmoz7sD0ATJ_rJiWp0/edit?usp=sharing)

These updates reflect the growing adoption and participation in the project, as well as the ongoing efforts to expand and strengthen the project's contributor base.

# Contributor Diversity (NEEDS WORK)

Projects in Hiero continue to promote more participation from external contributors. For example, the Python SDK team recently held one of their [Office Hours events](https://hiero.org/blog/introducing-the-hiero-python-sdk-office-hour/) to help the community get started, understand the project's proposed feature requests, get familiar with the codebase, troubleshooting their tests and even help new collaborators create their first PR.

Our workshop to help users create their own test network and communicate to it via our SDKs will continue to be promoted in future events.

Our [latest community calls](https://hiero.org/#contribute) are easily visible for the community to select one and join with the rest of the maintainers. For any of these calls, there are no expertise requirements. We welcome anyone in the community interested in using, adopting and contributing to Hiero.

In this quarter, 50% of the organization dependency continues to belong to Hashgraph and LimeChain among [35 active companies collaborating](https://insights.linuxfoundation.org/project/hiero/contributors?timeRange=custom&start=2025-06-20&end=2025-09-04&widget=organization-dependency) in GitHub commits/issues/discussions. 

Overall, [266 organizations](https://insights.linuxfoundation.org/project/hiero/contributors?timeRange=alltime&widget=organization-dependency) have contributed to Hiero activities (compared to 199 organizations reported in Q2). The team continues to seek diversity and promote more inclusion of new organizations and participating maintainers. It is a goal as a community overall to increase the number of participating organizations to be able to preserve project status.

# Additional Information (NEEDS WORK)

The Hiero team continues to work closely with the LFX team to have a more accurate representation of the Hiero project in LFX Insights and encouraging more contributors to provide their observations. With the recent re-introduction of the [Security & Best Practices](https://insights.linuxfoundation.org/project/hiero/security?timeRange=custom&start=2025-06-12&end=2025-09-04) scores in May, the team is focused on ensuring that the data remains consistent with the status of the repositories. At the same time, we will work with the OpenSSF team to help us adjusting our repo's scores to reflect any exceptions to the scores and work on improving those scores that are in our maintainer's hands.
