---
layout: default
title: 2026 Annual Review Hyperledger Fabric and Fabric-X
parent: 2026
grand_parent: Project Updates
---

# Fabric & Fabric-X Annual Report

## Governance Model Changes

In 2025, the Hyperledger Fabric project underwent a significant governance restructuring with the introduction of Fabric-X as a formal sub-project. The [Technical Charter was amended](https://github.com/hyperledger/fabric/pull/5223) (merged September 11, 2025) to establish two sub-projects, each with their own Technical Steering Committee (TSC):

### Hyperledger Fabric Sub-project
The TSC voting members are the maintainers listed in:
- [hyperledger/fabric](https://github.com/hyperledger/fabric/blob/main/MAINTAINERS.md)
- [hyperledger/fabric-gateway](https://github.com/hyperledger/fabric-gateway/blob/main/MAINTAINERS.md)

### Hyperledger Fabric-X Sub-project
The TSC voting members are the maintainers listed in:
- [hyperledger/fabric-x](https://github.com/hyperledger/fabric-x/blob/main/MAINTAINERS.md)
- [hyperledger/fabric-x-endorser](https://github.com/hyperledger/fabric-x-endorser/blob/main/MAINTAINERS.md)
- [hyperledger/fabric-x-orderer](https://github.com/hyperledger/fabric-x-orderer/blob/main/MAINTAINERS.md)
- [hyperledger/fabric-x-committer](https://github.com/hyperledger/fabric-x-committer/blob/main/MAINTAINERS.md)
- [hyperledger/fabric-x-common](https://github.com/hyperledger/fabric-x-common/blob/main/MAINTAINERS.md)

Both sub-projects share a common permissioned blockchain network governance model implemented with endorsement policies on top of PKI (X509 certificates), mTLS authentication for trusted communication, Fabric-CA/cryptogen compatible membership service providers, configuration block, {key, value, version} data model, and execute-order-validate transaction flow.

## Project Lifecycle Status Recommendation

**Hyperledger Fabric:** Graduated status still makes sense for Hyperledger Fabric.

**Hyperledger Fabric-X:** Fabric-X is recommended to continue as an Incubation project. The project has demonstrated technical viability with impressive performance benchmarks and has established the foundational repositories and documentation. The next phase should focus on expanding the contributor community, improving ease of adoption, and gathering production deployment feedback.


## Project Health

### Hyperledger Fabric

Hyperledger Fabric continues to be fairly mature and stable with a v2.5 long-term support (LTS) release and the v3.x release line now in active production use. The project maintained its focus on quality, maintenance, and support throughout 2025, with steady release cadence. New features continue to be proposed, approved, and implemented based on a community RFC process. Mailing list activity remains down compared to prior years, but there is significant Discord activity. PRs and mailing list questions are generally turned around quickly.

[LFX Insights report for Fabric 2025](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=fabric&routedFrom=Github&bestPractice=false&repository=all&dateFilters=Last%20Year&dateRange=2025-01-01%20to%202025-12-31&compare=PP&granularity=month&hideBots=true)
Highlights from the 2025 Fabric activity:
- Continued strong commit activity with contributions from IBM and a growing pool of external contributors
- v3.1.x release line delivered significant performance improvements for chaincode operations
- Docker images transitioned to Ubuntu 24.04 for v3.x releases
- Images now published to GitHub Container Registry (ghcr.io) in addition to Docker Hub

### Hyperledger Fabric-X

Hyperledger Fabric-X is a new addition to the Hyperledger ecosystem, representing a fundamental re-architecture of Hyperledger Fabric designed for high-performance enterprise use cases such as Central Bank Digital Currencies (CBDCs), stablecoins, tokenized deposits, and tokenized securities.

The project was contributed to Hyperledger in 2025 and has seen active development across its component repositories. The architecture decomposes the monolithic Fabric peer into independently scalable microservices for endorsement, validation, and committing, achieving throughput exceeding 200,000 transactions per second (TPS) — a two-orders-of-magnitude improvement over standard Hyperledger Fabric.

The project has established regular monthly community calls and hosted a workshop series introducing the architecture to the community.

**Fabric-X Repository Activity (2025):**

| Repository | Stars | Forks | Commits (2025) | Merged PRs (2025) | Description |
|------------|-------|-------|----------------|-------------------|-------------|
| fabric-x | 16 | 10 | 23 | ~20 | Main documentation and architecture overview |
| fabric-x-committer | 8 | 11 | 849+ | ~80 | Post-ordering transaction processing microservice |
| fabric-x-orderer | 7 | 9 | 500+ | ~70 | Arma BFT consensus ordering service |
| fabric-x-endorser | 2 | 1 | 50+ | ~10 | Transaction endorsement microservice |
| fabric-x-common | 3 | 4 | 100+ | ~15 | Shared CLIs and protocol buffers |

## Releases

### Hyperledger Fabric

The project delivered 8 releases in 2025:

**v2.5.x LTS releases:**
- v2.5.11 - January 31, 2025 (gossip handling of expired certificates fix)
- v2.5.12 - March 10, 2025 (peer panic fixes)
- v2.5.13 - April 29, 2025 (dependency updates)
- v2.5.14 - October 13, 2025 (dependency updates)

**v3.1.x releases:**
- v3.1.0 - March 18, 2025 (major feature release)
  - Batching of chaincode writes for significant performance improvement
  - Batching of chaincode reads via GetMultipleStates() and GetMultiplePrivateData()
  - New GetAllStatesCompositeKeyWithPagination() chaincode function
- v3.1.1 - May 10, 2025 (BFT bug fixes - goroutine leak and deadlock fixes)
- v3.1.2 - October 13, 2025 (config update via channel participation API, block fetch via API, BFT certificate rotation)
- v3.1.3 - October 18, 2025 (Docker image fix for orderer deployment)

### Hyperledger Fabric-X

The fabric-x main repository released 5 versions in 2025 (v0.0.1 through v0.0.5). Component repositories have had active development throughout the year with the fabric-x-committer repository accumulating 849+ commits.

## Fabric-X Architecture Components

### Fabric-X Orderer (Arma)
Arma is a Byzantine Fault Tolerant (BFT) consensus system designed for horizontal scalability. It separates transaction dissemination and validation from consensus, ordering only metadata of transaction batches. The orderer consists of:
- **Routers**: Accept and validate transactions from clients
- **Batchers**: Bundle transactions into batches across shards
- **Consenters**: Run BFT consensus on batch attestations
- **Assemblers**: Create the ordered ledger of blocks

### Fabric-X Committer
Responsible for post-ordering transaction processing with a microservice architecture:
- **Sidecar**: Manages block flow from ordering service
- **Coordinator**: Orchestrates validation pipeline using transaction dependency graph
- **Verification Service**: Validates signatures against namespace policies
- **Validator-Committer**: Performs optimistic concurrency control and commits
- **Query Service**: Provides read-only access with view-based isolation

### Fabric-X Endorser
Handles transaction endorsement in a scalable microservice architecture, replacing chaincode execution with peer-to-peer transaction negotiation protocols built on Fabric-Smart-Client and Fabric-Token-SDK.

## Maintainer Diversity

### Hyperledger Fabric
The project continues to work on maintainer diversity:
- 6 of 9 maintainers of core Fabric are from IBM
- Notable contributions in 2025 from external contributors including @pfi79 and @dviejokfs who contributed significant BFT improvements

A minority of the maintainers account for the majority of the maintainer activity, therefore the project continues to encourage additional Fabric users and contributors to increase activity and become maintainers. The project is happy to mentor anybody interested in becoming a contributor or future maintainer.

### Hyperledger Fabric-X
The project has 14 contributors across its repositories. The maintainers primarily come from IBM Research, who originally developed the architecture. The project is actively working to expand the contributor base and welcomes new contributors.

## Project Adoption

### Hyperledger Fabric
Based on what we see in mailing list and Discord there is significant adoption activity. Several large vendors and several smaller companies have commercial offerings based on Hyperledger Fabric, as well as consulting services. The Hyperledger Fabric Certified Practitioner exam and associated training course continue to see enrollment. The project does not maintain an ADOPTERS file since it is difficult to keep the information up-to-date and the project doesn't want to misrepresent reality or give preference to certain vendors.

### Hyperledger Fabric-X
Fabric-X is designed for national-scale payment systems and critical financial infrastructure. The project provides:
- Sample deployment scripts via Ansible for local and remote cluster deployments
- Integration with Fabric-Token-SDK for token-based applications
- Compatibility with existing Fabric tooling (Fabric-CA, cryptogen)

The project has generated interest from organizations exploring high-performance DLT solutions for digital currencies and tokenization use cases.

## Community Engagement

### Fabric-X Workshop Series (2025)
The Fabric-X project conducted a comprehensive workshop series:
1. Introduction to Fabric-X (architecture overview)
2. Programming model and application deployment
3. Fabric-Token-SDK integration
4. Orderer (Arma) deep dive
5. Committer architecture overview

### Monthly Calls
Fabric-X hosts monthly community calls on the 1st Wednesday of each month via the LF Decentralized Trust Zoom.

## Goals

### Performance Against Prior Goals

**Hyperledger Fabric 2025 goals:**
- Continue to provide maintenance releases at least quarterly for v2.5.x and v3.x (SUCCESSFULLY COMPLETED - 8 releases delivered)
- Publish images to Github Container Registry as the primary registry, while maintaining Dockerhub for existing users (SUCCESSFULLY COMPLETED)
- Improve OpenSSF Scorecard for other priority repositories (e.g. fabric-ca, fabric-chaincode-go, fabric-gateway SDK) (IN PROGRESS)
- Encourage contributions from community (ONGOING - external contributors contributed significant improvements to BFT ordering service)
- Continue to increase diversity of maintainers (ONGOING)

**Hyperledger Fabric-X 2025 accomplishments:**
- Successfully contributed Fabric-X to Hyperledger
- Established all component repositories (orderer, committer, endorser, common)
- Created comprehensive documentation and architecture diagrams
- Hosted workshop series to introduce the community to the architecture
- Published Ansible-based deployment scripts for local and remote deployments
- Achieved demonstrated throughput of 200,000+ TPS in benchmarks
- Established formal governance structure with dedicated TSC

**Other Fabric accomplishments:**
- Significant chaincode performance improvements with batch read/write capabilities in v3.1.0
- BFT ordering service improvements including certificate rotation without config updates
- Channel participation API enhancements for config updates and block fetching
- Docker images updated to Ubuntu 24.04 for improved security

### Next Year's Goals

**Hyperledger Fabric:**
- Continue to provide maintenance releases at least quarterly for v2.5.x and v3.x
- Continue to improve OpenSSF Scorecard for all priority repositories
- Encourage contributions from community
- Continue to increase diversity of maintainers
- Explore integration points with Fabric-X high-performance architecture

**Hyperledger Fabric-X:**
- Release sample token application on top of Fabric-X
- Develop Fabric-X Kubernetes Operator for easier deployment
- Expand contributor base beyond initial development team
- Improve documentation and getting-started guides
- Explore tighter integration with Hyperledger Fabric mainline
- Establish formal mentorship program for new contributors

### Help Required

**Hyperledger Fabric:** We continue to work with LFDT staff to identify contributors and potential maintainers.

**Hyperledger Fabric-X:** The project would benefit from:
- Contributors with experience in high-performance distributed systems
- Organizations interested in piloting Fabric-X for CBDC or tokenization use cases
- Documentation contributors to improve getting-started materials
- Kubernetes/cloud-native expertise for the operator development

## Useful Links

### Hyperledger Fabric
- [Fabric Repository](https://github.com/hyperledger/fabric)
- [Fabric Documentation](https://hyperledger-fabric.readthedocs.io/)
- [Fabric Releases](https://github.com/hyperledger/fabric/releases)
- [Technical Charter](https://github.com/hyperledger/fabric/blob/main/Hyperledger_Fabric_Technical_Charter.md)
- [Governance](https://github.com/hyperledger/fabric/blob/main/GOVERNANCE.md)

### Hyperledger Fabric-X
- [Fabric-X Main Repository](https://github.com/hyperledger/fabric-x)
- [Fabric-X Committer](https://github.com/hyperledger/fabric-x-committer)
- [Fabric-X Orderer](https://github.com/hyperledger/fabric-x-orderer)
- [Fabric-X Endorser](https://github.com/hyperledger/fabric-x-endorser)
- [Fabric-X Common](https://github.com/hyperledger/fabric-x-common)
- [Fabric-X Whitepaper](https://eprint.iacr.org/2023/1717.pdf)
- [Fabric-X Blog Announcement](https://www.lfdecentralizedtrust.org/blog/new-major-contribution-to-hyperledger-fabric-purpose-built-implementation-for-next-gen-digital-assets)
- [Deployment Scripts (Ansible)](https://github.com/LF-Decentralized-Trust-labs/fabric-x-ansible-collection)
