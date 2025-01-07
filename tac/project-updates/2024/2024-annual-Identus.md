---
layout: default
title: 2024 Annual Review Identus
parent: 2024
grand_parent: Project Updates
---

## Project Health

Hyperledger Identus [LFX Insights Dashboard](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/reports/contributors?project=identus&bestPractice=false&dateFilters=Last%20Year&dateRange=2024-01-01%20to%202024-12-31&compare=PP&granularity=month&hideBots=true&repository=all)
The project is relatively new to the Hyperledger Ecosystem and is mainly supported by the IOG maintainers.
At the same time, over the past year, we have seen several new contributors and evidence of usage of the Identus Platform by another companies: 
- https://socious.io/, Socious production use case.
- https://ahau.io/, Ahau PoC.
- https://blocktrust.dev/, - identity wallet.

We currently utilize two Discord servers: the Hyperledger Discord and the Identus Discord. 
The Identus Discord has seen significantly more engagement. 
Since January 2024, our membership has grown from 258 to 476 members. 
On average, there are 348 activities across various channels monthly, with about 39 users online daily.

## Maintainer Diversity

There are currently 30 maintainers from IOG and other companies. 

The MAINTAINERS.md file is up to date and can be found [here](https://github.com/hyperledger/identus/blob/main/MAINTAINERS.md)
The `identus-maintainers` [team](https://github.com/hyperledger/governance/blob/main/access-control.yaml#L625-L655) includes around 30 members from IOG and other companies.

The number of active maintainers has decreased due to the restructure of the Atala Team at IOG. 
However, the diversity of maintainers has increased over the past six months, with more companies contributing to the project.

## Project Adoption

A number of companies are using the Identus project for prototyping and production use cases.

The following companies are using the project:
- https://socious.io/, Socious production use case.
- https://ahau.io/, Ahau PoC.
- https://blocktrust.dev/, - identity wallet.

Developers are actively participating in the weekly meetings and considering using the Identus platform for their use cases.

## Goals

### Performance Against Prior Goals

The current project roadmap is public and can be found here: [Identus Roadmap](https://github.com/orgs/hyperledger/projects/48)  

During the last six months, the project has achieved the following goals:
- Connectionless Issuance and Verification of VC via DIDCommV2
- DID Prism AnonCreds method to resolve the resources from the DID Prism URL (for the schema and credential definition)
- Crypto Agility of the DID Prism Method (added Ed25519 cryptography suite)
- Transitioning the project from the IOHK to the Hyperledger organization
- OID4VCI specification implementation in the Cloud Agent and SDKs (for JWT VC only)
- Major refactoring: a. improved error handling in the Cloud Agent, the Mediator, and SDKs, b. added Problem Report protocol to other protocols, c. Background jobs are replaced with the message queue (in-memory or Kafka)
- SD-JWT-VC implementation in the Cloud Agent and SDKs
- Status List revocation implementation in JWT VC
- Improved documentation with the Quick Start Guide and Tutorials

The roadmap is actively discussed with the community members in the GitHub [Discussions](https://github.com/hyperledger/identus/discussions)

### Next Year's Goals

The project has the following strategic goals for the next year:
- Reduce maintenance cost and complexity of the Identus platform
- Increase the Identus platform adoption by the developers and companies
- Improve the platform interoperability with other SSI platforms
- Improve the platform documentation and tutorials

The following features are planned for the next year among others:
- Cardano Identus VDR
- Bring Issuance capabilities to the SDKs
- Continue with UAS Wrapper implementation
- Pollux Plugin abstraction SDK
- OIDC specifications for the SSI: OID4VCI, OID4VP, SIOP2.0
- Authentication using the PRISM DID method

### Help Required

LF Decentralized Trust can help with the following:
- Promote the Identus project within the Hyperledger community
- Help with the workshops and hackathons
- Help to collaborate with the Hyperledger Aries project as the Identus platform leveraging the Aries specs and protorols


## Project Lifecycle Status Recommendation

The Identus is a fairly new graduated project in the Hyperledger Ecosystem and should remain so.
