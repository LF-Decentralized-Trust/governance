[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2025 Q2 Hiero

## Project Health

Hiero has experienced a 45% increase in [active contributors](https://insights.linuxfoundation.org/project/hiero/contributors?timeRange=custom&start=2025-04-01&end=2025-06-12&widget=active-contributors) compared to the previous quarter. In recent months, the project successfully completed the transfer of Hedera owned components and is now focusing on the migration of community driven projects. Concurrently, we remain committed to advancing brand neutrality and are preparing for future releases under the Hiero namespace. In parallel, we have been actively preparing for the upcoming graduation application, which is scheduled for submission on August 1.

Our number of [active organizations](https://insights.linuxfoundation.org/project/hiero/contributors?timeRange=custom&start=2025-04-01&end=2025-06-12&widget=active-organizations) remains stable, with new communities continuing to discover Hiero and recognize the project's potential impact. During the recent elections, we observed a notable increase in project adopters and successfully onboarded [two new TSC members](https://hiero.org/blog/results-of-the-hiero-technical-steering-committee-elections/), representing the Contributor and End User seats.

Hiero has experienced a noticeable increase in the number of issues opened and resolved, along with a rise in [commit activity](https://insights.linuxfoundation.org/project/hiero/development?timeRange=custom&start=2025-04-01&end=2025-06-12) which is an encouraging indicator of the project's growing popularity and discovery by new contributors and adopters. To further promote community engagement, we launched a new [Hiero blog](https://hiero.org/blog/) section, where technical documentation and project updates are being published. Additionally, Hiero is scheduled to present a project seminar at Rare Evo in August, further expanding its visibility within the broader ecosystem along with other LFDT projects.

# Questions/Issues for the TAC

There are no issues or questions to bring up to the TAC at this time. We appreciate the TAC's support on helping us address recent guidelines and adoption for Contribute and Changelog project requirements.

# Releases

The Hiero project maintainers are actively focusing and working on tasks related to recent minor version releases. At the same time, the team is addressing outstanding dependency issues, which are required to enable publishing of Maven packages under the official Hiero org namespace. Below is a summary of the most notable recent releases for Q2:

- [hiero-sdk-js](https://github.com/hiero-ledger/hiero-sdk-js) - The team released v2.66.0, which addresses multiple feature and bug issues (e.g., JSON‑RPC endpoints for TokenAirdropClaimTransaction, TokenCancelAirdropTransaction, browser mirror-node support).
- [hiero-sdk-java](https://github.com/hiero-ledger/hiero-sdk-java) - v2.58.0 release enhances enterprise-grade transaction signing capabilities with new HSM support and improves code maintainability through strategic refactoring of core transaction handling methods.
- [hiero-sdk-go](https://github.com/hiero-ledger/hiero-sdk-go) - Release v2.64.0 introduces enhanced transaction size inspection APIs, enabling developers to measure transaction sizes with and without signatures. It also includes bug fixes for protobuf methods in Pause and Unpause transactions.
- [hiero-solo-action](https://github.com/hiero-ledger/hiero-solo-action) - Release v0.8 improves developer experience with updated documentation, compatibility warnings, and a new account-check script. It also enhances Solo setup performance, adds ED25519 key outputs, and enables gRPC port forwarding for better integration.
- [hiero-sdk-cpp](https://github.com/hiero-ledger/hiero-sdk-cpp) - v0.41.0 includes improvement proposals to update NodeCreate, NodeUpdate APIs.
- [hiero-mirror-node](https://github.com/hiero-ledger/hiero-mirror-node) - The latest release v0.131.1, includes ongoing migration effort to fully shift naming from Hedera to Hiero namespaces.
- [hiero-block-node](https://github.com/hiero-ledger/hiero-block-node) - Version 0.12.0 delivers significant improvements to observability and security, introducing new Prometheus metrics and dashboards across core components and plugins, along with full metrics coverage for block provider tiers and system status.
- [hiero-consensus-node](https://github.com/hiero-ledger/hiero-consensus-node) - Release v0.61.10 includes changes that allows operators the option to disable node rewards, fixes an issue where throttle capacity was not properly reclaimed after ingestion failures among other fixes and incremental improvements.
- [hiero-local-node](https://github.com/hiero-ledger/hiero-local-node) - v2.37.1 includes a feature that enables mirror node modularized services, improves devex in the CLI and adds support to multinode scenario.
- [hiero-mirror-node](https://github.com/hiero-ledger/hiero-mirror-node-explorer) - v25.0.0 includes updates that prioritize improved observability, accessibility, and developer utility in the explorer interface.
- [solo](https://github.com/hiero-ledger/solo) - v0.37.1 introduces full compatibility with Apple Silicon improving the reliability of network deployments on macOS. It also features an updated requirements table that clarifies supported versions for critical dependencies ensuring a smoother setup and clearer user guidance.

In general, all hiero-ledger components are actively adding security fixes and adopting CI practices from StepSecurity. At the same time, the repositories are adding additional structure to their local documentation and maintainer information according to the best practices.
In terms of documentation, sdk collaboration hub, website, and improvement proposals are maintained and updated several times a week.

# Overall Activity in the Past Quarter

Hiero Ledger has seen a notable increase in activity in recent months. The project has successfully launched new project specific community calls, which remain publicly accessible via the [Hiero calendar](https://zoom-lfx.platform.linuxfoundation.org/meetings/hiero?view=week). Currently, we are collaborating with the Python SDK team to organize their first "Office Hours" and Hackathon session, scheduled to take place in the coming weeks. Additionally, the team has proposed initiating a recurring monthly Hackathon focused on development for the [Hiero](https://hiero.org/) website.

As more [components continue to be transitioned](https://github.com/hiero-ledger/hiero/blob/main/community-transition.md) into the hiero-ledger ecosystem, we are encouraging project teams to host regular community calls to support collaboration, accelerate development, and enhance overall project performance.

While activity on the public mailing lists has remained minimal, we are actively directing community engagement toward the Hiero Discord channel, which continues to serve as the primary hub for discussion and support. At the same time, we continue to observe consistent community engagement through GitHub Issues and Discussions.

Following the recent approval of updated [roles and groups guidelines](https://github.com/hiero-ledger/governance/blob/main/roles-and-groups.md) by the TSC, and their subsequent adoption by the community, we are encouraging teams to review their structures and consider promoting additional committers and maintainers where appropriate. These guidelines provide a clear framework for aligning with best practices, allowing teams to assess their current processes and make informed improvements. We continue to offer support and guidance to team leads seeking assistance in implementing these standards.

# Current Plans

The Hiero project continues to experience rapid growth and increased visibility across the broader community, driven by ongoing promotion and community engagement and traction efforts. The team is preparing for upcoming conference participation and onboarding new contributors and maintainers as well as remaining focused on maintaining project health through our metrics tooling and upholding strong security practices to protect against threats and vulnerabilities. 

Given the origins of hiero-ledger, where the majority of the codebase was initially donated by Hedera/Hashgraph, it is understandable that much of the current maintenance and ownership remains with the original contributing parties. However, the project is now entering an exciting phase of growth, with a clear focus on expanding contributor and maintainer diversity. This momentum is already evident in the [latest proposals](https://github.com/hiero-ledger/tsc/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22project%20proposal%22) currently in the pipeline. As these proposals are taking place over the coming weeks, we are confident they will significantly enhance the diversity and inclusivity of the project community.

The team is also actively working on the Hiero renaming initiative and brand neutralization, with particular attention to dependency related issues to ensure a smooth and seamless transition.

In addition, Hiero has formally adopted and now maintains the Hedera Improvement Proposal (HIP) process, leveraging its established success to foster open, transparent, and community driven technical decision making.

We are also continuing our efforts in cross-project collaboration with other open source communities, including the **OpenWallet Foundation**, **Hyperledger Besu**, and **AnonCreds**, to advance shared goals and strengthen the broader decentralized ecosystem.

# Maintainer Diversity

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

# Contributor Diversity

With the recent round of elections, increased promotion of the Hiero project in recent events and through new announcements, the expansion of the Technical Steering Committee (TSC), and a steady growth of new adopter organizations joining the community, we anticipate continued growth in contributor diversity. In the latest TSC elections, over 50 companies were added to our list of [adopters](https://github.com/hiero-ledger/hiero/blob/main/ADOPTERS.md), and more than 100 active contributors participated in the voting for the Contributor Seat elections. Currently, a significant portion of contributions comes from Hashgraph, LimeChain, and Devlabs, among over [30 active companies collaborating](https://insights.linuxfoundation.org/project/hiero/contributors?timeRange=custom&start=2025-04-01&end=2025-06-12&widget=organization-dependency) via GitHub commits/issues/discussions in the second quarter alone.

Overall, [more than 190 organizations](https://insights.linuxfoundation.org/project/hiero/contributors?timeRange=alltime&widget=organization-dependency) have contributed to Hiero actuvites, reflecting strong momentum toward a more diverse and inclusive contributor community.

# Additional Information

The team is actively working to address the feedback and outstanding issues from the most recent Hiero annual report in preparation for reapplying for graduation by August 1. Additionally, we continue to work closely with the LFX team to have a more accurate representation of the Hiero project in LFX Insights and encouraging more contributors to provide their observations.
