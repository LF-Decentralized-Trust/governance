[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Annual Review Identus

## Project Health

Following its transition to the Hyperledger Identus GitHub organization, the project continues to demonstrate steady, sustained development activity. Over the past 12 months, LFX Insights reports 37 active contributors, with approximately 51% quarterly retention, indicating a stable and engaged contributor base. Development activity was recorded on 313 of the last 365 days, reflecting consistent year-round [momentum](https://insights.linuxfoundation.org/project/open-enterprise-agent?timeRange=past365days&start=2025-02-10&end=2026-02-10).

Overall contribution volume remains strong, with roughly 4,800–5,000 contribution events annually (including commits, pull requests, issues, and reviews), averaging around 400 activity events per month. The project maintains healthy delivery cycles, with a median merge lead time of about 6 days and an average issue resolution time of approximately 39 days.

Contribution patterns remain concentrated, however: the top three individual contributors account for roughly 55% of total activity, and two organizations contribute about 62% of all contributions. Improving reviewer capacity and broadening organizational participation therefore remain important focus areas for long-term sustainability.

Security/compliance: the team kicked off **OpenSSF Best Practices** and **Scorecard** work; status is tracked at [ssf.identus.work](https://ssf.identus.work/).

Infrastructure: ongoing optimizations are in flight. **Neoprism** is being positioned to replace `prism-node` and the default Cardano infrastructure; it is more efficient and configurable (see [repo](https://github.com/hyperledger-identus/neoprism) and [docs](https://hyperledger-identus.github.io/neoprism/)).

Community engagement is healthy across the LFDT Discord, weekly maintainer calls, and GitHub discussions. Workshops such as RareEvo 2025 (offline-first + Lace wallet demo) and ongoing roadmap discussions continue to attract external participation. Repository migration is complete, improving transparency and aligning metrics.

## Maintainer Diversity

There are **10 maintainers** across IOG and external partners (Socious, CSign, Blocktrust, Trust0); the **number of companies and maintainers is unchanged** year over year. The MAINTAINERS.md file is current in the [Identus repo](https://github.com/hyperledger/identus/blob/main/MAINTAINERS.md); the [`identus-maintainers` team](https://github.com/hyperledger/governance/blob/main/access-control.yaml#L625-L655) reflects the same roster. Diversity is improving, but IOG still provides the majority of maintainer capacity, so onboarding additional reviewers is an explicit objective.

## Project Adoption

Identus is in production or advanced pilots with:
- [Socious.io](https://socious.io/) (production)
- [Blocktrust](https://blocktrust.dev/) (identity wallet)
- [csign.io](https://csign.io/) (contributor and adopter)

Adoption momentum is reinforced by offline-first SDK work, issuance support now live in SDK-TS and SDK-Swift, stabilization of **SDK-KMP** (feature parity nearing completion), and early React Native enablement via the Kotlin rewrite and Apollo downgrade. The team is actively adapting Identus components for React Native applications, integrating SSI capabilities into the **Lace** wallet, and continuing Midnight alignment, which should broaden Cardano ecosystem usage.

## Goals

### Performance Against Prior Goals

Roadmap board: [Identus Roadmap](https://github.com/orgs/hyperledger/projects/48)

Key outcomes delivered in 2025:
- Shipped platform releases **v2.15** and **v2.16**, bringing issuance to SDK-TS/Swift, offline-first improvements, and an Ed25519 fix for revocation lists.
- Advanced **Neoprism** as the successor to `prism-node`; Cardano VDR milestones 3–4 are underway with `prism-node` deprecation targeted within six months.
- Added the **DID Prism AnonCreds** method for schema/credential-definition resolution.
- Refactored Cloud-Agent, Mediator, and SDKs for better error handling, message queuing, and Problem Report support.
- Ran a documentation audit, refreshed Quick Start and tutorials, and aligned docs with the 2025 releases.
- Drove community engagement through Discord, weekly maintainer calls, GitHub discussions, and the RareEvo 2025 workshop.
- Completed the **VDR Catalyst Project**, introducing the VDR driver and API to the Identus platform (final stage wraps in **February 2026**). More details: [Project Catalyst VDR](https://projectcatalyst.io/funds/13/cardano-open-developers/verifiable-data-registry-for-identus-in-cardano).
- Stabilized **SDK-KMP**, moving it toward feature parity with other SDKs.

### Next Year's Goals (2026)

- Finish platform simplification: replace `prism-node` with **Neoprism**, close remaining Cardano VDR milestones (final Catalyst stage completes **February 2026**), and complete offline-first parity across SDKs (including the Kotlin rewrite).
- Harden developer experience: unify issuance guidance, expand tutorials, and deliver React/React Native support as SDK-KMP parity lands.
- Broaden interoperability: ship **OID4VCI/OID4VP/SIOP 2.0**, **VCDM 2.0**, **mDoc**, and **OpenBadges 3.0** support; continue exploring JSON-LD VC support.
- Security and compliance: complete **OpenSSF Best Practices** and **Scorecard** badges (target **Q1 2026**) and feed findings into CI/CD and dependency hygiene.
- Community & programs: grow the maintainer/reviewer pool, run **1–2 LFDT workshops** to promote Identus, and continue collaboration with Aries/CREDEBL.
- Developer enablement: deliver a **unified environment setup** suitable for workshops, development, and as a production reference deployment.
- Adoption: continue **Lace wallet** integration and broader React Native enablement.
- Governance: prepare to **apply for project incubation in Q3 2026** in line with the LFDT incubation exit criteria.

### Help Required

No TAC help requested at this time; the team is already coordinating directly with LFDT community managers.

## Project Lifecycle Status Recommendation

Identus remains an incubating project in the LF Decentralized Trust ecosystem and should stay in **Incubation** while maintainer diversity and OpenSSF compliance mature.
