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

After the adition of two new members of the Technical Steering Committee (TSC), in July, we had [Brandon Davenport](https://github.com/itsbrandondev) (Contributor seat) joining as well. In September, the team is looking to run another round of elections to rotate of of the existing TSC Contributor Seat positions. These actions, are helping the governance maintain a diverse approach and a provide a fresh perspective of the direction of the project.

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

Documentation and hiero-website repos are also receiving updates. Hiero-website continues to add more information that can easily help new contributors getting started, update information on TSC members and make continuous [blog updates](https://hiero.org/blog/) related to the state of the project and collaboration oportunities. 

All hiero-ledger components continue to add security fixes and adopt CI practices from StepSecurity. 

All hiero-ledger repositories are up to date with the TAC repo structure requirements. 

# Overall Activity in the Past Quarter -- Needs update

Hiero Ledger has seen a notable increase in activity in recent months. The project has successfully launched new project specific community calls, which remain publicly accessible via the [Hiero calendar](https://zoom-lfx.platform.linuxfoundation.org/meetings/hiero?view=week). Currently, we are collaborating with the Python SDK team to organize their first "Office Hours" and Hackathon session, scheduled to take place in the coming weeks. Additionally, the team has proposed initiating a recurring monthly Hackathon focused on development for the [Hiero](https://hiero.org/) website.

As more [components continue to be transitioned](https://github.com/hiero-ledger/hiero/blob/main/community-transition.md) into the hiero-ledger ecosystem, we are encouraging project teams to host regular community calls to support collaboration, accelerate development, and enhance overall project performance.

While activity on the public mailing lists has remained minimal, we are actively directing community engagement toward the Hiero Discord channel, which continues to serve as the primary hub for discussion and support. At the same time, we continue to observe consistent community engagement through GitHub Issues and Discussions.

Following the recent approval of updated [roles and groups guidelines](https://github.com/hiero-ledger/governance/blob/main/roles-and-groups.md) by the TSC, and their subsequent adoption by the community, we are encouraging teams to review their structures and consider promoting additional committers and maintainers where appropriate. These guidelines provide a clear framework for aligning with best practices, allowing teams to assess their current processes and make informed improvements. We continue to offer support and guidance to team leads seeking assistance in implementing these standards.

# Current Plans  -- Needs update

The Hiero project continues to experience rapid growth and increased visibility across the broader community, driven by ongoing promotion and community engagement and traction efforts. The team is preparing for upcoming conference participation and onboarding new contributors and maintainers as well as remaining focused on maintaining project health through our metrics tooling and upholding strong security practices to protect against threats and vulnerabilities. 

Given the origins of hiero-ledger, where the majority of the codebase was initially donated by Hedera/Hashgraph, it is understandable that much of the current maintenance and ownership remains with the original contributing parties. However, the project is now entering an exciting phase of growth, with a clear focus on expanding contributor and maintainer diversity. This momentum is already evident in the [latest proposals](https://github.com/hiero-ledger/tsc/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22project%20proposal%22) currently in the pipeline. As these proposals are taking place over the coming weeks, we are confident they will significantly enhance the diversity and inclusivity of the project community.

The team is also actively working on the Hiero renaming initiative and brand neutralization, with particular attention to dependency related issues to ensure a smooth and seamless transition.

In addition, Hiero has formally adopted and now maintains the Hedera Improvement Proposal (HIP) process, leveraging its established success to foster open, transparent, and community driven technical decision making.

We are also continuing our efforts in cross-project collaboration with other open source communities, including the **OpenWallet Foundation**, **Hyperledger Besu**, and **AnonCreds**, to advance shared goals and strengthen the broader decentralized ecosystem.

# Maintainer Diversity -- Needs update

In this Q2 quarter, the Hiero project has undergone a number of maintainer team updates, including the addition of new members, team restructurings, and role assignments. Several contributors have been granted both maintainer and committer roles within some of our repositories, reflecting their active engagement and contributions to the project.

In summary, the [following repos have received changes](https://github.com/hiero-ledger/governance/commits/main/config.yaml?since=2025-04-01&until=2025-06-13): 

- solo: The team designated 3 maintainers and 8 committers.
- tsc-eligibility-check: Added 2 maintainers and 3 committers.
- hiero-consensus-node: Underwent a team restructuring, resulting in updated maintainer assignments across its associated teams within the repo.
- governance-triage: A newly formed team, launched with 6 maintainers.
- tsc: Welcomed 2 new members following the most recent elections.
- hiero-sdk-swift: Added 1 new maintainer.
- hiero-python-sdk: Added 1 new committer.
- hiero-rust-sdk: Added 1 new maintainer.

As of today, maintainers in the Hiero Ledger organization are primarily represented by contributors from Hashgraph (67%) and LimeChain (18%). Given that the majority of the project was originally donated by Hashgraph/Hedera, this distribution is to be expected. However, following our recent round of elections, new adoptions, and increased project visibility, we are beginning to see greater participation from additional organizations taking on maintainer roles. Both the project team and the TSC are actively working to further broaden this diversity and participation. In parallel, efforts to transition additional community donated repositories is ongoing, which is expected to further enhance diversity within the maintainer groups in the next months. Detailed composition of the maintainer groups can be viewed [here](https://docs.google.com/spreadsheets/d/1LjBhaaZMiDAvYlBAwzLbC5Z-ySc3BucMuJs25kbnsAc/edit?usp=sharing)

These updates reflect the growing adoption and participation in the project, as well as the ongoing efforts to expand and strengthen the project's contributor base.

# Contributor Diversity -- Needs update

With the recent round of elections, increased promotion of the Hiero project in recent events and through new announcements, the expansion of the Technical Steering Committee (TSC), and a steady growth of new adopter organizations joining the community, we anticipate continued growth in contributor diversity. In the latest TSC elections, over 50 companies were added to our list of [adopters](https://github.com/hiero-ledger/hiero/blob/main/ADOPTERS.md), and more than 100 active contributors participated in the voting for the Contributor Seat elections. Currently, a significant portion of contributions comes from Hashgraph, LimeChain, and Devlabs, among over [30 active companies collaborating](https://insights.linuxfoundation.org/project/hiero/contributors?timeRange=custom&start=2025-04-01&end=2025-06-12&widget=organization-dependency) via GitHub commits/issues/discussions in the second quarter alone.

Overall, [more than 190 organizations](https://insights.linuxfoundation.org/project/hiero/contributors?timeRange=alltime&widget=organization-dependency) have contributed to Hiero actuvites, reflecting strong momentum toward a more diverse and inclusive contributor community.

# Additional Information

The Hiero team continues to work closely with the LFX team to have a more accurate representation of the Hiero project in LFX Insights and encouraging more contributors to provide their observations. With the recent re-introduction of the [Security & Best Practices](https://insights.linuxfoundation.org/project/hiero/security?timeRange=custom&start=2025-06-12&end=2025-09-04) scores in May, the team is focused on ensuring that the data remains consistent with the status of the repositories. At the same time, we will work with the OpenSSF team to help us adjusting our repo's scores to reflect any exceptions to the scores and work on improving those scores that are in our maintainer's hands.
