[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Mid-Year Review CREDEBL

## Project Health

CREDEBL continued active development during the first half of 2026, with coordinated work across the platform, agent controller, Studio, installer, mobile SDK, and documentation repositories. The May 2026 v2.2.0 releases delivered a significant expansion of OpenID4VC issuance and verification, trust and ecosystem capabilities, and deployment support.

The project remains in use for production and proof-of-concept deployments, including Digi Yatra, Bhutan NDI, and SOVIO.id, as described in the [2026 annual review](./2026-Annual-CREDEBL.md). No new adoption figures were available for this mid-year update.

## Progress Against 2026 Goals

The [public CREDEBL roadmap](https://github.com/orgs/credebl/projects/5/views/1) and the goals in the [2026 annual review](./2026-Annual-CREDEBL.md) set the direction for this period. The v2.2.0 release represents substantial progress on OpenID4VC, revocation, trust services, and wallet capabilities. The status notes below also include post-release work & distinguish it from outputs delivered during January–June.

Post-v2.2.0, alpha work has achieved additional goals, including integration with RustFS for filesystem & OpenBao for secret manager to acheive goal of becoming cloud agnostic.

## Deliverables and Outputs (January–June 2026)

### Releases

- [Platform v2.2.0](https://github.com/credebl/platform/releases/tag/v2.2.0) — 13 May 2026. Added OpenID4VC issuance and verification for SD-JWT and mDoc, HAIP-compatible presentation flows, SD-JWT revocation using IETF Token Status List 2021, X.509 certificate and trust management, signed webhooks, consent notices, SMTP email, and platform administration enhancements.
- [Agent Controller v2.2.0](https://github.com/credebl/agent-controller/releases/tag/v2.2.0) — 13 May 2026. Added OpenID4VC issuance and verification support, SD-JWT and mDoc, status-list revocation, trust-service integration, and improvements to DIDComm, wallet persistence, and deployment security.
- [Studio v2.2.0](https://github.com/credebl/studio/releases/tag/v2.2.0) — 13 May 2026. Added user interfaces and API integration for ecosystem creation, management, and intent workflows, with improvements to platform administration and authentication handling.
- [Install v2.2.0](https://github.com/credebl/install/releases/tag/v2.2.0) — 13 May 2026. Improved local deployment portability, added Terraform support for NATS clusters, and updated setup and deployment scripts for the current platform components.

### Repository activity and other outputs

- The [documentation repository](https://github.com/credebl/docs) added API reference material for basic OpenID4VC/VP flows and updated the related documentation structure in April.
- Across the repositories, commits also included fixes and maintenance for issuance and verification flows, schemas, authentication, deployment configuration, dependency versions, and developer setup.

### Post-v2.2.0 alpha and post-period updates

- **W3C VC for OID4VC:** W3C VC/JWT VC JSON-LD issuance and presentation support for OID4VC was merged in the [platform](https://github.com/credebl/platform/pull/1646) and [agent controller](https://github.com/credebl/agent-controller/pull/389) in June. The platform changes are present in the [v2.2.1-alpha.4 tag](https://github.com/credebl/platform/tree/v2.2.1-alpha.4).
- **Deployment flexibility:** The platform added selectable S3 and local-filesystem storage in [PR #1670](https://github.com/credebl/platform/pull/1670), present in the v2.2.1-alpha.4 tag.
- **OpenBao secret storage:** [Platform PR #1679](https://github.com/credebl/platform/pull/1679) added OpenBao-backed secret storage was merged. Provider refactoring followed in [PR #1712](https://github.com/credebl/platform/pull/1712). This work was completed and released in an August alpha;
- **RustFS for filesystem:** [Platform PR #1670](https://github.com/credebl/platform/pull/1670) added RustFS, an S3-compatible backend, as a selectable file-storage option alongside AWS S3 and local filesystem storage. The PR was merged and the change is included in the [v2.2.1-alpha.4 tag](https://github.com/credebl/platform/tree/v2.2.1-alpha.4).
- **Mobile SDK:** [PR #109](https://github.com/credebl/mobile-sdk/pull/109) added dcql support for W3C credential records in proof-request selection; was included in the [v2.2.0 alpha tag from 26 June](https://github.com/credebl/mobile-sdk/tree/v2.2.0-alpha-20260626075404).
Stable [v2.2.0](https://github.com/credebl/mobile-sdk/releases/tag/v2.2.0) and [v2.2.1](https://github.com/credebl/mobile-sdk/releases/tag/v2.2.1) releases followed on 8 September.

- The platform also grouped Swagger UI endpoints by module in [PR #1608](https://github.com/credebl/platform/pull/1608), merged in August as a Q3 item, supporting API discoverability and developer documentation.

## Goals for the Second Half of 2026

- Continue maturing VCDM 2.0 interoperability, W3C credential revocation, external KMS integration, and wallet import/export.
- Continue improving deployment, documentation, and testing alongside regular maintenance releases.
- Confirm and sustain the renewed TSC and regular community meetings, and broaden contributor and maintainer participation beyond AYANWORKS.

## Help Required

LF Decentralized Trust can help promote CREDEBL through community events, webinars, and workshops; connect the project with potential adopters and contributors; and support outreach that brings more organizations into project governance and maintenance. No specific technical blocker requiring TAC intervention was identified for this update.

## Maintainer and Contributor Diversity

The 2026 annual review reports that maintainers are currently from AYANWORKS. Compared with the previous quarter, we have seen an increase in contributor diversity. The project continues to seek broader community participation, including through the planned TSC and regular meetings.

## Questions or Issues for the TAC

No specific questions or issues for the TAC at this time.
