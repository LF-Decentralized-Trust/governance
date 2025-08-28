[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2025 Q3 Hyperledger Identus

## Project Health

The [LF Decentralized Trust Identus LFX Insight Dashboard](https://insights.linuxfoundation.org/project/open-enterprise-agent/development?timeRange=past180days&start=2025-02-28&end=2025-08-27) indicates growth of commits and PR having the same number of contributors.

While the primary maintainer of the Identus Platform is the Input Output (IOG) organization, community members and external organizations have also actively contributed, including:
- [Blocktrust](https://www.blocktrust.dev/)
- [Socious.io](https://socious.io/)
- [csign.io](https://csign.io/)

---

## Questions/Issues for the TAC

No questions for the TAC.

---

## Releases

In the previous quarter, the Identus Team released the [Identus Platform v2.15 release](https://github.com/hyperledger-identus/.github/releases/tag/v2.15).
The next release (v2.16) is planned for October and will include the following features:
- Issuance capability in the SDKs
- Offline-First SDKs improvements
- Bugfixes and refactoring based on the community feedback
- `Neoprism` PRISM DID indexer (we are planning to deprecate the existing `prism-node` component by the end of 2025)
- Phase 3 of the VDR driver for Identus on the Cardano blockchain
- Documentation improvements based on the community feedback and the audit of the Technical Writers

---

## Overall Activity in the Past Quarter

The Identus community remains active across the LFDT Discord, Identus Maintainers' weekly community meetings, and GitHub [discussions](https://github.com/hyperledger-identus/hyperledger-identus/discussions)
Community members continue to ask questions, report issues, and discuss various use cases, as well as discussing the Identus RoadMap. 
The core team and community contributors actively support these interactions.

---

## Current Plans

The strategic direction remains consistent with the annual report. The main goals are to:

- Continue reducing the maintenance cost and complexity of the Identus Platform by introducing and adopting alternative ways to resolve the DID Prism ([`Neoprism` project](https://github.com/hyperledger-identus/neoprism) and community initiative to use the file system and GitHub as the [indexer](https://github.com/FabioPinheiro/prism-vdr) for the PRISM DID)
- Increase adoption among developers and organizations
- Enhance interoperability with other Self-Sovereign Identity (SSI) platforms
- Continue the documentation improvement and developer tutorials (documentation audit was completed, and the plan for improvements is defined)

Planned features for the upcoming year include:
- Complete the Cardano Identus VDR initiative (the current progress can be tracked [here](https://milestones.projectcatalyst.io/projects/1300189/milestones/3))
- Complete the Issuance capabilities in the SDKs
- OIDC support: OID4VCI, OID4VP, and SIOP 2.0
- Authentication via the PRISM DID method

Additional features under consideration:
- Support of JSON-LD Verifiable Credentials
- Support of mDoc Verifiable Credentials
- Support of the Verifiable Credentials Data Model v2
- Support of OpenBadges 3.0 Verifiable Credentials
- Integration with WebWallets (the Lace Wallet will use the Identus Platform to enable the SSI capabilities)

To align with LF Decentralized Trust's Project Lifecycle Criteria, the team also plans to:
- Enable the OpenSSF Best Practices Badge
- Enable the OpenSSF Scorecard Badge

---

## Maintainer Diversity

Socious, CSign, 

---

## Contributor Diversity

The primary contributor to the Identus project remains Input Output Global (IOG). 
However, Blocktrust and Socious also actively contribute to the codebase and discussions. 

---

## Additional Information

The Identus team is also focused on integrating SSI capabilities into IOG’s **Midnight** and **Lace** projects.
The new DID method we are developing for the Midnight project will also be supported by the Identus Platform.
These efforts are expected to boost the adoption of the Identus Platform within the broader Cardano ecosystem.
