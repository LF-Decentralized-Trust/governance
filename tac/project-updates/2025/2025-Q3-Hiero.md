---
layout: default
title: 2025 Q3 Hiero
parent: Project Updates
grand_parent: LF Decentralized Trust TAC
---

# Project Health

Hiero has recently achieved graduated status which highlights the project's maturity, achieved through rigorous evaluation of its legal, technical, community, and documentation aspects. Hiero is the first project that has graduated under the new LFDT standards which continue to develop in order to ensure that projects are able to be evaluated in a meticulous and careful way.

At the moment, the hiero-ledger organization consists on [32 repositories](https://github.com/orgs/hiero-ledger/repositories) and continues to plan the inclusion of new projects designed to work together and provide additional support, strengthening the platform’s robustness and expanding its ecosystem.

Nearly 800 contributors from 80+ organizations and 50+ adopters continue to shape the future of Hiero.

After the addition of two new members of the Technical Steering Committee (TSC), in July, we had [Brandon Davenport](https://github.com/itsbrandondev) (Contributor seat) joining as well. In September, the team is looking to run another round of elections to rotate one of the existing TSC Contributor Seat positions. These actions are helping the governance maintain a diverse approach and provide a fresh perspective of the direction of the project.

Hiero also was present at RareEvo's conference in August. Hendrik Ebbers directed a [workshop](https://www.youtube.com/watch?v=4saglmQVxU0) to help new and current contributors set up a network and create a simple application that connected to the network using one of the project's SDKs.

# Questions/Issues for the TAC

There are no issues or questions to bring up to the TAC at this time.

# Releases

The Hiero project maintainers continue to focus and work on tasks related to recent minor version releases. Below is a summary of the most notable recent releases for Q3:

- [hiero-sdk-js](https://github.com/hiero-ledger/hiero-sdk-js) - The team released v2.72.0, which introduces important improvements to transaction validation and fee flexibility in the Hiero SDK. These changes enhance both security and usability for developers working with smart contracts and scheduled transactions.
- [hiero-sdk-java](https://github.com/hiero-ledger/hiero-sdk-java) - v2.63.0 release that introduced validation to ensure that TopicMessageSubmitTransaction messages cannot be empty and added support for customFeeLimits in scheduled transactions, starting with TopicSubmitTransaction. Several dependency upgrades were made.
- [hiero-sdk-go](https://github.com/hiero-ledger/hiero-sdk-go) - Release v2.69.0 introduces several enhancements to transaction handling and contract updates, including support for setting AutoRenewPeriod in seconds, mutual exclusivity between SetStakedAccountID and SetStakedNodeID, the ability to use both private and public keys in SetAdminKey for contract updates, the option to remove an auto-renew account by setting it to 0.0.0, and new customFeeLimits support for scheduled transactions
- [hiero-solo-action](https://github.com/hiero-ledger/hiero-solo-action) - Release v0.12.0 improves developer experience and adds additional fixes.
- [hiero-sdk-cpp](https://github.com/hiero-ledger/hiero-sdk-cpp) - v0.45.0 introduces new JSON-RPC endpoints for file transactions, enhances GRPC proxy management with e2e test support, and includes multiple dependency and CI version updates.
- [hiero-mirror-node](https://github.com/hiero-ledger/hiero-mirror-node) - Release v0.137.1, includes several fixes and remove duplicate functionality.
- [hiero-block-node](https://github.com/hiero-ledger/hiero-block-node) - Version 0.17.1 delivers adds improvements to security and bugfixes.
- [hiero-consensus-node](https://github.com/hiero-ledger/hiero-consensus-node) - Release v0.65.1 adds progress output to the export command, improves state validator stability, and includes a fix for transaction parsing fallback logic.
- [hiero-mirror-node](https://github.com/hiero-ledger/hiero-mirror-node-explorer) - v25.1.1 includes updates and bug fixes.

Documentation and hiero-website repos are also receiving updates. Hiero-website continues to add more information that can easily help new contributors getting started, update information on TSC members and make continuous [blog updates](https://hiero.org/blog/) related to the state of the project and collaboration opportunities. 

All hiero-ledger components continue to add security fixes and adopt CI practices from StepSecurity. 

All hiero-ledger repositories are up to date with the TAC repo structure requirements. 

# Overall Activity in the Past Quarter

The Hiero project is building traction and momentum in our goal to acquire more collaborators and participants. Our [community calls](https://zoom-lfx.platform.linuxfoundation.org/meetings/hiero?view=week) continue to run and recently we were able to host a new Solo Community call, Python SDK Office Hours and Website community call. We also had a short series of calls to discuss the direction of the projects and the baseline and requirements for new projects to join hiero-ledger. We continue to promote openness in the community and continue to welcome the opinion of new users.

The community was able to obtain Graduated project status. Each repo in hiero-ledger comforms to the TSC guidelines for repo structure, security policies and quality of the code. We continue to work on adopting more [community projects](https://github.com/hiero-ledger/hiero/blob/main/community-transition.md) and seeking the participation of new members from different backgrounds and affiliations.

The project maintainers are helping shaping the scores from the OpenSSF reports. We have been working on improving the overall project quality by focusing in the reports obtained by our tools like GitHub Insights, LFX Insights, OpenSSF, Snyk and Step Security.

# Current Plans

The Hiero project continues to build momentum, with community awareness and adoption receiving continuous expansion. Current priorities include preparing for upcoming conference participation, expanding the contributor and maintainer base, and reinforcing the project’s foundation by leveraging metrics tools and implementing strong security measures to guard against vulnerabilities and potential threats.

The project will continue to work with the LFDT TAC to maintain and preserve project status. The main areas of focus will be the project's diversity in contributors and maintainers as well as the improvement of OpenSSF scoring. In the following month, the TSC will renew one TSC position for Contributor Seat with the rest of the governance. We are organizing a Maintainer's Community Call that will allow us to work with the maintainers and explain the roles, participation and impact that the members of the TSC in the project along with how they can influence their desision making when selecting new candidates.

We are also continuing our efforts in cross-project collaboration with other open source communities. The team has started a communication with the Identus maintainers to potentially bring in Hiero's usage for the Identus project development. 

Additionally, the project is planning a First Year Anniversary webinar to promote the project's achievement and welcome interested audiences to participate in the project.

# Maintainer Diversity

In Q3 we continue to add acquire new projects into our hiero-ledger organization.
- [hiero-hederium](https://github.com/hiero-ledger/hiero-hederium) - Hederium is Golang implementation of Hedera JSON-RPC Relay or Hashio.
- [hiero-did-sdk-js](https://github.com/hiero-ledger/hiero-did-sdk-js) - A TypeScript/JavaScript SDK for building decentralized identity solutions on Hiero.
- We are currently working on transfering hiero-cli.

In summary, the [following repos have received changes](https://github.com/hiero-ledger/governance/commits/main/config.yaml?since=2025-06-14&until=2025-09-04): 

- Create the hiero-cli-committers team with several new members. 
- Nominations are created for the upcoming September elections.
- LFStaff received an updated with one more member.
- Additional Roles for supporting onboarding & management are created.
- Block Node received a re-structuring of their maintainers team.
- Python SDK acquired a new maintainer.
- Contributors are allowed to perform triage activities for sdk-tck and sdk-js.
- Consensus Node maintainers team acquired two new members.
- Added new maintainers team for hashgraph online.

As of today, maintainers in the Hiero Ledger organization are primarily represented by contributors from Hashgraph and LimeChain. The entire composition of the maintainers affiliation can he found [here](https://docs.google.com/spreadsheets/d/1O4wTFxw9rUQbgc3YvCKyDYlAKwmoz7sD0ATJ_rJiWp0/edit?usp=sharing)

These updates reflect the growing adoption and participation in the project, as well as the ongoing efforts to expand and strengthen the project's contributor base.

# Contributor Diversity

Projects in Hiero continue to promote more participation from external contributors. For example, the Python SDK team recently held one of their [Office Hours events](https://hiero.org/blog/introducing-the-hiero-python-sdk-office-hour/) to help the community get started, understand the project's proposed feature requests, get familiar with the codebase, troubleshooting their tests and even help new collaborators create their first PR.

Our workshop to help users create their own test network and communicate to it via our SDKs will continue to be promoted in future events.

Our [latest community calls](https://hiero.org/#contribute) are easily visible for the community to select one and join with the rest of the maintainers. For any of these calls, there are no expertise requirements. We welcome anyone in the community interested in using, adopting and contributing to Hiero.

In this quarter, 50% of the organization dependency contines to belong to Hashgraph and LimeChain among [35 active companies collaborating](https://insights.linuxfoundation.org/project/hiero/contributors?timeRange=custom&start=2025-06-20&end=2025-09-04&widget=organization-dependency) in GitHub commits/issues/discussions. 

Overall, [266 organizations](https://insights.linuxfoundation.org/project/hiero/contributors?timeRange=alltime&widget=organization-dependency) have contributed to Hiero activities (compared to 199 organizations reported in Q2). The team continues to seek diversity and promote more inclusion of new organizations and participating maintainers. It is a goal as a community overall to increase the number of participating organizations to be able to preserve project status.

# Additional Information

The Hiero team continues to work closely with the LFX team to have a more accurate representation of the Hiero project in LFX Insights and encouraging more contributors to provide their observations. With the recent re-introduction of the [Security & Best Practices](https://insights.linuxfoundation.org/project/hiero/security?timeRange=custom&start=2025-06-12&end=2025-09-04) scores in May, the team is focused on ensuring that the data remains consistent with the status of the repositories. At the same time, we will work with the OpenSSF team to help us adjusting our repo's scores to reflect any exceptions to the scores and work on improving those scores that are in our maintainer's hands.
