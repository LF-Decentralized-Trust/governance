---
layout: default
title: 2025 Q2 Hiero
parent: Project Updates
grand_parent: LF Decentralized Trust TAC
nav_exclude: true
---

# Project Health

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
- [hiero-local-node](https://github.com/hiero-ledger/hiero-local-node) - v2.37.1 inclues a feature that enables mirror node modularized services, improve devex in the CLI and add support to multinode scenario.
- [hiero-mirror-node](https://github.com/hiero-ledger/hiero-mirror-node-explorer) - v25.0.0 includes updates that prioritize improved observability, accessibility, and developer utility in the explorer interface.
- [solo](https://github.com/hiero-ledger/solo) - v0.37.1 introduces full compatibility with Apple Silicon improving the reliability of network deployments on macOS. It also features an updated requirements table that clarifies supported versions for critical dependencies ensuring a smoother setup and clearer user guidance.

In general, all hiero-ledger components are actively adding security fixes and adopting CI practices from StepSecurity. At the same time, the repositories are adding additional structure to their local documentation and maintainer information acoording to the best practices.
In terms of documentation, sdk collaboration hub, website, and improvement proposals are maintained and updated several times a week.

# Overall Activity in the Past Quarter

Hiero Ledger has seen a notable increase in activity in recent months. The project has successfully launched new project specific community calls, which remain publicly accessible via the [Hiero calendar](https://zoom-lfx.platform.linuxfoundation.org/meetings/hiero?view=week). Currently, we are collaborating with the Python SDK team to organize their first "Office Hours" and Hackathon session, scheduled to take place in the coming weeks. Additionally, the team has proposed initiating a recurring monthly Hackathon focused on development for the [Hiero](https://hiero.org/) website.

As more [components continue to be transitioned](https://github.com/hiero-ledger/hiero/blob/main/community-transition.md) into the hiero-ledger ecosystem, we are encouraging project teams to host regular community calls to support collaboration, accelerate development, and enhance overall project performance.

While activity on the public mailing lists has remained minimal, we are actively directing community engagement toward the Hiero Discord channel, which continues to serve as the primary hub for discussion and support. At the same time, we continue to observe consistent community engagement through GitHub Issues and Discussions.

Following the recent approval of updated [roles and groups guidelines](https://github.com/hiero-ledger/governance/blob/main/roles-and-groups.md) by the TSC, and their subsequent adoption by the community, we are encouraging teams to review their structures and consider promoting additional committers and maintainers where appropriate. These guidelines provide a clear framework for aligning with best practices, allowing teams to assess their current processes and make informed improvements. We continue to offer support and guidance to team leads seeking assistance in implementing these standards.

# Current Plans

<mark>_Required: A healthy project will often be working towards a common goal, or have a shared understanding of what is being done next - even if individual contributors have their own "itches". What are the main features planned? What releases are planned? Are there any specific efforts or branches of development underway? This does not need to be described in technical detail. Conversely, if the activity is minimal, discuss how the project plans to address that - whether through seeking out new contributors, maintaining in a dormant but available state, or planning towards a move to a Deprecated (and ultimately End of Life) state._
</mark>

# Maintainer Diversity

<mark>_Required: Please include the maintainers that were added since your last report. This information will allow us to track the diversity and growth of the maintainers of the project. NOTE: If no maintainers were added since your last report, provide the list of existing maintainers._
</mark>

# Contributor Diversity

<mark>_Required: A healthy project should survive the departure of any single contributor or employer of contributors. Healthy projects also serve the needs of many parties. Include information on the number of unique organizations currently contributing to the project. NOTE: The contributions do not need to be source code._
</mark>

# Additional Information

The team is actively working to address the feedback and outstanding issues from the most recent Hiero annual report in preparation for reapplying for graduation by August 1. Additionally, we continue to work closely with the LFX team to have a more accurate representation of the Hiero project in LFX Insights and encouraging more contributors to provide their observations.
