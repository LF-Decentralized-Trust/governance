[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Mid-Year Review CREDEBL

## Project Health

CREDEBL continued active development during the first half of 2026, with coordinated work across the platform, agent controller, Studio, installer, mobile SDK, and documentation repositories. The May 2026 v2.2.0 releases delivered a significant expansion of OpenID4VC issuance and verification, trust and ecosystem capabilities, and deployment support.

The project remains in use for production and proof-of-concept deployments, including Digi Yatra, Bhutan NDI, and SOVIO.id, as described in the [2026 annual review](./2026-Annual-CREDEBL.md). No new adoption figures were available for this mid-year update.

## Progress Against 2026 Goals

The [public CREDEBL roadmap](https://github.com/orgs/credebl/projects/5/views/1) and the goals in the [2026 annual review](./2026-Annual-CREDEBL.md) set the direction for this period. The v2.2.0 release represents substantial progress on OpenID4VC, revocation, trust services, and wallet capabilities. Work on other roadmap goals remains in progress or is not evidenced by the releases and commits reviewed for this report.

## Deliverables and Outputs (January–June 2026)

### Releases

- [Platform v2.2.0](https://github.com/credebl/platform/releases/tag/v2.2.0) — 13 May 2026. Added experimental OpenID4VC issuance and verification for SD-JWT and mDoc, HAIP-compatible presentation flows, SD-JWT revocation using IETF Token Status List 2021, X.509 certificate and trust management, digital trust ecosystems, signed webhooks, consent notices, SMTP email, and platform administration enhancements.
- [Agent Controller v2.2.0](https://github.com/credebl/agent-controller/releases/tag/v2.2.0) — 13 May 2026. Added OpenID4VC issuance and verification support, SD-JWT and mDoc, status-list revocation, trust-service integration, and improvements to DIDComm, wallet persistence, and deployment security.
- [Studio v2.2.0](https://github.com/credebl/studio/releases/tag/v2.2.0) — 13 May 2026. Added user interfaces and API integration for ecosystem creation, management, and intent workflows, with improvements to platform administration and authentication handling.
- [Install v2.2.0](https://github.com/credebl/install/releases/tag/v2.2.0) — 13 May 2026. Improved local deployment portability, added Terraform support for NATS clusters, and updated setup and deployment scripts for the current platform components.

### Repository activity and other outputs

- The [mobile SDK](https://github.com/credebl/mobile-sdk) added support for W3C credential records in credential selection for requests. Its v2.2.0 release was published in September 2026, after this report's January–June reporting period, and is not counted as a first-half release.
- The [documentation repository](https://github.com/credebl/docs) added API reference material for basic OpenID4VC/VP flows and updated the related documentation structure in April.
- Across the repositories, commits also included fixes and maintenance for issuance and verification flows, schemas, authentication, deployment configuration, dependency versions, and developer setup.

## Goals for the Second Half of 2026

- Continue maturing the platform to improve interoperability with VCDM 2.0 and W3C VC support in OpenID4VC, external KMS integration, trust registry capabilities, and wallet import/export utilities.
- Continue improving deployment, documentation, and testing alongside regular maintenance releases.
- Confirm and sustain the renewed TSC and regular community meetings, and broaden contributor and maintainer participation beyond AYANWORKS.

## Help Required

LF Decentralized Trust can help promote CREDEBL through community events, webinars, and workshops; connect the project with potential adopters and contributors; and support outreach that brings more organizations into project governance and maintenance. No specific technical blocker requiring TAC intervention was identified for this update.

## Maintainer and Contributor Diversity

The 2026 annual review reports that maintainers are currently from AYANWORKS. Compared with the previous quarter, we have seen an increase in contributor diversity. The project continues to seek broader community participation, including through the planned TSC and regular meetings.

## Questions or Issues for the TAC

No specific questions or issues for the TAC at this time.
