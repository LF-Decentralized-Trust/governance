[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Mid-Year Review Hyperledger Identus

This review covers activity since the [2026 annual review](2026-annual-Hyperledger-Identus.md), from 29 January through 16 September 2026. It follows the [mid-year review instructions](../mid-year-update-instructions.md) and reflects the project status at the time of writing.

## Project Health

Hyperledger Identus remains active and continues to deliver releases while moving through a technical and staffing transition. The core team lost several engineers during the period, which reduced language-specific capacity, particularly for the Swift and Kotlin SDKs. The team maintained delivery by simplifying the architecture, increasing automation, and concentrating new cross-platform work in the shared [SDK-Rust](https://github.com/hyperledger-identus/sdk-rust) implementation. This consolidation is intended to reduce duplicated work across TypeScript, Scala, Kotlin, and Swift.

The [LFX Insights overview](https://insights.linuxfoundation.org/project/open-enterprise-agent?timeRange=past365days&start=2025-09-16&end=2026-09-16) currently rates the project **Healthy (75/100)**. The corresponding [contributors dashboard](https://insights.linuxfoundation.org/project/open-enterprise-agent/contributors?timeRange=past365days&start=2025-09-16&end=2026-09-16) reports 70 active contributors and 10 active organizations, while the [development dashboard](https://insights.linuxfoundation.org/project/open-enterprise-agent/development?timeRange=past365days&start=2025-09-16&end=2026-09-16) reports 2,326 commits, 274 active days, an average pull-request merge time of 5 days, and an average issue resolution velocity of 13 days. These trailing-365-day figures are useful health indicators, but they do not exactly match the review window and include bot activity.

The [LFX contributor data](https://insights.linuxfoundation.org/project/open-enterprise-agent/contributors?timeRange=past365days&start=2025-09-16&end=2026-09-16) also shows that the top two contributors account for 56% of contribution activity. LFX separates Input Output Global, Input Output Group, and Input Output HK into different organization records; taken together, those records account for approximately 95% of attributed activity. Participation is broadening through mentorship and community contributions, while growing review capacity outside the IOG-funded core remains an important objective.

The team reports that LLM-assisted development and stronger automation have helped the smaller group maintain delivery throughput. All changes remain subject to maintainer review and the project's normal quality controls.

Security and governance work progressed. OpenSSF Scorecard workflows are present in ten of the 17 public repositories, and eight component READMEs currently display OpenSSF Best Practices badges. Per-repository results are published in the [OpenSSF Scorecard viewer](https://securityscorecards.dev), and registered components are listed in the [OpenSSF Best Practices registry](https://www.bestpractices.dev/en/projects?q=identus). The team plans to complete OpenSSF Best Practices adoption by the end of 2026. The main project also added the requested [ADOPTERS.md](https://github.com/hyperledger-identus/hyperledger-identus/blob/main/ADOPTERS.md), listing CSIGN, Blocktrust, Socious, and Trust0 across production use and active development.

## Progress Against 2026 Goals

The goals are those recorded in the [2026 annual review](2026-annual-Hyperledger-Identus.md).

| 2026 goal | Mid-year status | Evidence and assessment |
| --- | --- | --- |
| Replace `prism-node` with NeoPRISM and finish the Cardano VDR work | **Delivered in practice; formal deprecation pending** | [Platform v2.17](https://github.com/hyperledger-identus/hyperledger-identus/releases/tag/v2.17) integrated NeoPRISM and the PRISM VDR driver into Cloud Agent, and the [deployment documentation](https://identus.io/documentation/develop/cloud-agent/node-backend/) recommends NeoPRISM for new deployments. Since the annual review, NeoPRISM recorded [more than 100 commits](https://github.com/hyperledger-identus/neoprism/commits/main/?since=2026-01-29&until=2026-09-16) and [eight releases](https://github.com/hyperledger-identus/neoprism/releases), compared with [two compatibility commits](https://github.com/input-output-hk/atala-prism/commits/main/?since=2026-01-29&until=2026-09-16) and no release for `prism-node`. The team reports that it announced during an [Identus community call](https://zoom-lfx.platform.linuxfoundation.org/meetings/identus?view=list) that formal deprecation is planned for Q4 2026. |
| Complete offline-first parity across SDKs | **Strategic consolidation in progress** | SDK-TS and SDK-Swift passed the [v2.17 integration tests](https://github.com/hyperledger-identus/hyperledger-identus/releases/tag/v2.17). SDK-KMP 5.0.0 was not included because of its known functional limitations, and staffing changes reduced Swift and Kotlin capacity. The project is addressing this sustainably through the shared [SDK-Rust](https://github.com/hyperledger-identus/sdk-rust) foundation rather than continuing full independent reimplementation in every language. |
| Improve React and React Native support | **Good foundation; integration continues** | SDK-TS 8.0.0 included Expo compatibility and WASM packaging improvements in the [v8 refactor](https://github.com/hyperledger-identus/sdk-ts/pull/511). SDK-Rust has begun experimental WASM and UniFFI host foundations, while work supporting Lace and React Native continues across the wider Identus ecosystem. |
| Deliver OID4VCI/OID4VP/SIOP 2.0 and additional credential formats | **Partial / carried forward** | SDK-Rust contains active OID4VCI, presentation, JOSE, credential, and COSE work. The repository is explicitly pre-release, and the broader OID4VP/SIOP 2.0, VCDM 2.0, mDoc, OpenBadges 3.0, and JSON-LD goals are not yet complete platform deliverables. |
| Complete OpenSSF Best Practices and Scorecard adoption | **On track** | Scorecard workflows and Best Practices badges now cover many core repositories. The remaining work is visible in the [OpenSSF Best Practices registry](https://www.bestpractices.dev/en/projects?q=identus) and the [Scorecard results](https://securityscorecards.dev), and is planned for completion by the end of 2026. |
| Deliver a unified development/workshop environment | **Active testing** | The internal `workspace` repository assembles NeoPRISM, Cloud Agent, Mediator, VDR, SDKs, documentation, and integration tests under a Nix-based development environment. The team is actively testing it and plans to adopt it during 2026 to automate routine work and support cross-cutting feature development. |
| Grow community participation and run LFDT programs | **Good mentorship progress** | Identus maintainers joined the LFDT Mentorship Program and launched the [Identity Portal mentorship](https://github.com/LF-Decentralized-Trust-Mentorships/mentorship-program/issues/77). The resulting [identity-portal](https://github.com/hyperledger-identus/identity-portal) repository is active. Additional LFDT workshops remain planned. |
| Prepare for lifecycle advancement in Q3 2026 | **Timing under review** | The project has continued the readiness work, including [adopter documentation](https://github.com/hyperledger-identus/hyperledger-identus/blob/main/ADOPTERS.md), OpenSSF adoption, mentorship, and maintainer governance. The Q3 application may be postponed so the team can complete the SDK support transition, OpenSSF rollout, and maintainer-record alignment before applying. |

## Deliverables and Outputs

### Identus Platform v2.17

The team published [Identus Platform v2.17](https://github.com/hyperledger-identus/hyperledger-identus/releases/tag/v2.17) on 19 June 2026. The coordinated release included:

- **Cloud Agent 2.2.0:** VDR capabilities, PRISM VDR driver integration, and NeoPRISM REST API support as a backend, alongside the legacy `prism-node` path.
- **Mediator 1.2.1:** compatibility fixes and dependency maintenance.
- **NeoPRISM 0.14.1:** the platform-tested NeoPRISM release. NeoPRISM has since reached [0.14.2](https://github.com/hyperledger-identus/neoprism/releases/tag/v0.14.2), adding atomic transaction indexing, input validation, SQLite cleanup, and broader tests.
- **SDK-TS 8.0.0:** the SDK was [significantly refactored](https://github.com/hyperledger-identus/sdk-ts/pull/511) from a single package into a workspace of smaller domain, protocol, WASM, and SDK packages, reducing coupling between components while preserving the primary SDK interface. The release also added `jwt` and `prism/jwt` credential-format support, deferred seeds, a default Identus store, SD-JWT key-binding fixes, JWT time-claim validation, long-form PRISM DID state-hash verification, and a DID-agnostic DIDComm bridge. Follow-up [8.1.x releases](https://github.com/hyperledger-identus/sdk-ts/releases) added PRISM DID update/deactivation and maintenance fixes.
- **SDK-Swift 8.1.0/8.1.1:** an asynchronous seed callback so applications can retrieve seed material from secure storage on demand, followed by adaptation of the end-to-end tests to the new API.
- **SDK-KMP 5.0.0:** publication under the stable `org.hyperledger.identus:sdk` Maven coordinates, but with a documented warning that the SDK is currently non-functional and was not validated in the platform integration suite.

The platform integration suite passed for SDK-TS and SDK-Swift. SDK-KMP was skipped because of its known state. These manually dispatched runs validated the June release snapshot; they should not be read as evidence of continuous coverage for every component. At the cutoff, follow-up work included Cloud Agent DID-deactivation defects ([#1883](https://github.com/hyperledger-identus/cloud-agent/issues/1883), [#1884](https://github.com/hyperledger-identus/cloud-agent/issues/1884), and [#1885](https://github.com/hyperledger-identus/cloud-agent/issues/1885)) and broader OID4VCI/OID4VP and VCDM 2.0 capabilities.

### Rust SDK consolidation

The team made a strategic shift toward [SDK-Rust](https://github.com/hyperledger-identus/sdk-rust) as a chain-agnostic foundation for SSI domain models, protocol engines, cryptographic utilities, conformance evidence, and future language bindings. Since the annual review, it has recorded [438 commits](https://github.com/hyperledger-identus/sdk-rust/commits/develop/?since=2026-01-29&until=2026-09-16) and [139 merged pull requests](https://github.com/hyperledger-identus/sdk-rust/pulls?q=is%3Apr+is%3Amerged+merged%3A2026-01-29..2026-09-16).

The work includes cryptographic and DID foundations, credential and presentation models, JOSE/COSE support, OID4VCI flows, and experimental WASM and UniFFI integration. The [repository documentation](https://github.com/hyperledger-identus/sdk-rust/blob/develop/README.md) identifies `develop` as a pre-release integration line, so it should not yet be treated as a stable production SDK.

### LFDT Mentorship and Identity Portal

Identus maintainers are mentoring the [Hyperledger Identus Identity Portal](https://github.com/LF-Decentralized-Trust-Mentorships/mentorship-program/issues/77) project. The portal is intended to reduce the adoption barrier by providing a reference React interface that works with either the offline-first TypeScript Edge Agent or a connected Cloud Agent.

The public [identity-portal repository](https://github.com/hyperledger-identus/identity-portal) was created in June and has delivered its project foundation, Keycloak-based authentication, local and Cloud Agent DID resolution, PRISM DID management, and schema-management foundations. Credential issuance is the current phase. Of 49 pull requests opened during the period, 45 were merged; 27 came from the mentee and 22 from a mentor. This provides a concrete new-contributor pathway rather than only a training exercise.

The project also maintained a regular community-call cadence. The [LFX calendar](https://zoom-lfx.platform.linuxfoundation.org/meetings/identus?view=list) records 27 calls during the review period, although recent calls had approximately five participants. The calls provide continuity and mentorship access, but do not yet demonstrate a large active community.

### Infrastructure, adoption, and documentation

- NeoPRISM produced seven releases from 0.10.0 through 0.14.1 during the core review period, adding Blockfrost as a Cardano data source, VDR support, deployment modes, release automation, and documentation. Version 0.14.2 followed in September with reliability and test improvements.
- The [ADOPTERS.md](https://github.com/hyperledger-identus/hyperledger-identus/blob/main/ADOPTERS.md) requested in the annual TAC review was added in April.
- Documentation was updated for v2.17 and expanded around NeoPRISM, VDR, connectionless presentation, and development workflows.
- The team continues work to integrate Identus capabilities into Lace and to improve React Native adoption. The [SDK-TS v8 workspace refactor](https://github.com/hyperledger-identus/sdk-ts/pull/511) and Expo/WASM fixes provide a more modular foundation for that work. Much of the Lace-specific activity is outside the LFDT-tracked repositories, so LFX does not capture all of it.
- The internal `workspace` repository is under active testing and is planned for adoption during 2026. It will automate recurring development routines and provide a shared environment for features that span NeoPRISM, Cloud Agent, Mediator, VDR, and the SDKs.

## Goals for the Remainder of 2026

1. **Define and deliver the first SDK-Rust release boundary.** Complete the planned cryptographic, DID, credential, presentation, OID4VCI, WASM, and UniFFI slices; publish explicit stability and compatibility criteria before positioning it as a replacement for existing SDKs.
2. **Publish a support and migration plan for SDK-KMP and SDK-Swift.** Restore tested platform compatibility where practical and clearly communicate maintenance and migration expectations while SDK-KMP integration coverage is being restored.
3. **Formalize the NeoPRISM transition.** Continue hardening NeoPRISM as the default Cloud Agent backend and complete the announced Q4 2026 deprecation of `prism-node`, with clear migration documentation for existing deployments.
4. **Advance React Native and Lace integration.** Turn the current Expo/WASM/UniFFI foundations into documented, tested integration paths for React Native applications and wallet use cases.
5. **Complete the Identity Portal mentorship deliverables and run an LFDT workshop.** Finish credential issuance, presentation, and verification flows, reusable SSI modules, and workshop-quality documentation; use the resulting environment in at least one planned LFDT workshop.
6. **Finish OpenSSF rollout by the end of 2026.** Extend Scorecard and Best Practices coverage to all actively maintained repositories and resolve the remaining priority findings recorded in the [OpenSSF Best Practices registry](https://www.bestpractices.dev/en/projects?q=identus) and the [Scorecard results](https://securityscorecards.dev).
7. **Reconcile governance records and reduce key-person dependency.** Align the organization and repository `MAINTAINERS.md` files, operational GitHub permissions, and LFX's active-maintainer view; record affiliations consistently; and develop additional active reviewers outside the current core.
8. **Refresh the public roadmap.** Update the organization project board to include SDK-Rust, Identity Portal, SDK support decisions, and the revised consolidation strategy.
9. **Continue the community-led AI/MCP initiative.** Support the community effort to expose Identus platform capabilities through Model Context Protocol integrations, while keeping security boundaries and human accountability explicit.
10. **Reassess lifecycle advancement timing.** Continue preparing the application, while allowing the Q3 2026 target to move if more time is needed to complete support commitments, maintainer alignment, security coverage, and adopter evidence.

## Help Required

No TAC help is requested at this time. The team remains in regular contact with LFDT community managers about mentorship, workshops, and project promotion.

## Maintainer and Contributor Diversity

The canonical organization [MAINTAINERS.md](https://github.com/hyperledger-identus/.github/blob/main/MAINTAINERS.md) remains at **10 active maintainers**: eight from IOG, one from Blocktrust, and one from Ahau. This count and organization mix are unchanged from the annual review.

The main repository's separate [MAINTAINERS.md](https://github.com/hyperledger-identus/hyperledger-identus/blob/main/MAINTAINERS.md) now lists **15 active maintainers**, and the operational permissions configuration is different again. The [LFX overview](https://insights.linuxfoundation.org/project/open-enterprise-agent?timeRange=past365days&start=2025-09-16&end=2026-09-16) identifies **10 active maintainers with merge rights**. Reconciling these records will give the TAC a clearer view of project maintainers, repository maintainers, active reviewers, and organizational diversity.

Contributor participation is broader numerically, although core development remains concentrated. The [LFX contributors dashboard](https://insights.linuxfoundation.org/project/open-enterprise-agent/contributors?timeRange=past365days&start=2025-09-16&end=2026-09-16) reports 70 active contributors, up from 56 in the preceding period, across 10 active organizations. A GitHub audit of the review window found 37 PR-author accounts, approximately 33 human and four automation accounts. Automation authored about 49% of PRs, while the top three human accounts authored about 66% of human-authored PRs. The [Identity Portal mentorship](https://github.com/LF-Decentralized-Trust-Mentorships/mentorship-program/issues/77) has added a substantive external contributor and a repeatable path for onboarding. The next community-health priority is to convert more of this broader participation into sustained review and maintainer capacity.
