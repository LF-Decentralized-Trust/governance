[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Annual Review CREDEBL

## Project Health

LF Decentralized Trust CREDEBL [LFX Insights Dashboard](https://insights.linuxfoundation.org/project/credebl/contributors?timeRange=past365days&start=2025-04-24&end=2026-04-24)

This project is a new project so the contribution activity is not as high as other projects. However, We have already seen some new contributors started exploring and the PRs are getting through.

## Maintainer Diversity

- Currently all the maintainers are from AYANWORKS and as we have already started receiving the contributions from the community, once we get Major PRs we will start adding more maintainers.
- The MAINTAINERS.md file is up to date and can be found [here](https://github.com/credebl/.github/blob/main/MAINTAINERS.md)

## Project Adoption

Several Government Entities and Enterprises are using the CREDEBL project for production & proof-of-concept use cases.

Following organizations have recently deployed CREDEBL as population scale:

- [Digi Yatra Foundation](https://digiyatrafoundation.com/) – Successfully completed the [IATA International Contactless Travel Proof-of-concept](https://www.iata.org/contentassets/a46387f9bc6b42368c0a72664f6f930f/cycle2-attachment-poc.pdf), leveraging the CREDEBL platform to validate Digi Yatra’s seamless interoperability and compliance with global travel standards. See *Use Case #6* in the linked document.
- [Bhutan NDI](https://www.bhutanndi.com) - Bhutan NDI for Royal Government of Bhutan.
- [Sevis Wallet](https://www.ict.gov.pg/sevis-wallet) - SevisPass Digital ID Pilot for Papua New Guinea.
- [SOVIO.id](https://sovio.id) - Sovio SaaS Platform for organizations and individuals to use reusable, cryptographically secure digital identities and credentials.

## Goals

### Performance Against Prior Goals

The current project roadmap is public and can be found here: [CREDEBL Roadmap](https://github.com/orgs/credebl/projects/5/views/1)

**Key outcomes delivered in 2025:**

- The weekly community calls are regularly running to have all roadmap and development discussions in the open community.
- After moving into LFDT, team has made a major release [v2.0](https://github.com/credebl/platform/releases/tag/v2.0.0) of the project
- The major outcomes include support for OpenID4VC protocol with SD-JWT & mDOC credential types
- Alignment with IATA Interoperability Profile for International Contactless Travel Use Case.
- Started work on supporting OID4VC/VP implementation with support for SD-JWTs, ISO mDoc & DC-API
- Started work on revocation support for SD-JWT credentials with IETF Token Status List 2021.
- Following are the minor releases for further enhancements :
  - [v2.1.3](https://github.com/credebl/platform/releases/tag/v2.1.3) - Improved session management, support for multiple email providers.
  - [v2.1.2](https://github.com/credebl/platform/releases/tag/v2.1.2) - Code refactoring and bug fixes
  - [v2.1.1](https://github.com/credebl/platform/releases/tag/v2.1.1) - Enhancements in SSO feature
  - [v2.1.0](https://github.com/credebl/platform/releases/tag/v2.1.0) - OpenTelemetry (OTEL) and Signoz integration for observability
- Delivered an introductory session in OpenWallet Foundation in [Wallet Interop SIG](https://lf-openwallet-foundation.atlassian.net/wiki/spaces/GROUP/pages/130187265/2025-04-07+Wallet+Interop+SIG)
- Participated in the LFX mentorship with following programs:
  - [LFDT - Test coverage and improved documentation for CREDEBL Platform project](https://mentorship.lfx.linuxfoundation.org/project/92df3acf-9c1e-4a27-b9a4-cb5ed4293435)
  - [LFDT - Evaluate use of Unikernals for scaling controller & mediator instances in CREDEBL deployments](https://mentorship.lfx.linuxfoundation.org/project/d501d6f7-b964-44f5-a079-1b20adc4f06a) 
- Delivered a session under LFDT India Chapter for building a digital credential solution using CREDEBL
- New TSC nomination process has completed. We have received 12 nominations through the open nomination call. Formation of new TSC is due in the next month (May '26) along with kick-starting the regular meetings for the next year.

### Next Year's Goals

The project has the following goals for the next year:
- Support for Native SDKs for Android & iOS, along with (current) React-Native
- VCDM 2.0 support
- W3C VC support in OpenID4VC
- External KMS support
- Revocation using IETF Token Status List
- Trust Registry
- Hedera/Hiero ledger support
- Wallet Utilities
  - Export wallet from shared agent -> import into a dedicated agent
  - Import X509 based cert/key

### Help Required

LF Decentralized Trust can help with the following:
- Promote the CREDEBL project within the LF Decentralized Trust community
- Help with the workshops

## Project Lifecycle Status Recommendation

The CREDEBL is already used in production with large scale deployments at a national level in various sectors such as National ID, Travel, Education, etc. However, based on the earlier suggestions from TAC, we will focus on increasing the maintainer diversity through LFDT events such as webinars, workshops. We hope to see improvement in the contributor diversity with the new TSC formation.