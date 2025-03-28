---
layout: default
title: 2025 Annual Review Hyperledger Bevel
parent: 2025
grand_parent: Project Updates
---

## Project Health
1. Getting code contribution on Bevel still remains a challenge, though the community usage and interest is still there for both the projects as can be inferred from discussions and queries on discord channel and user participations on meetups. However, it has decreased compared to 2023 in every aspect (commits, PRs, issues created, forks). Reference: [Bevel LFX Insights Page](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=bevel&repository=&routedFrom=Github)

2. The projects have done well in terms of releases with 1.1.0 and 1.2.0. We have added numerous implementations described below, such as the use of Helm charts for DLT network deployment and the integration of AWS Secret Manager, among others.
3. Bevel-Operator-Fabric recently came out with its release v1.11.0, supporting Fabric 3.0.


## Maintainer Diversity
There are currently 4 maintainers, from Accenture(2), Walmart(1) and cheqd(1).
Existing maintainers:
- Alvaro Picazo (Accenture)
- Suvajit Sarkar (Accenture)
- Sownak Roy (cheqd)
- Aditya Joshi (Walmart)

Check CODEOWNERS file updated [here](https://github.com/hyperledger-bevel/bevel/blob/main/CODEOWNERS).
The project is happy to mentor anybody interested in becoming a contributor or a future maintainer.

There is no change in the maintainers Bevel-Operator-Fabric. You can find our current maintainer list here:
https://github.com/hyperledger/bevel-operator-fabric/blob/main/MAINTAINERS.md.

Existing maintainers:
- David Viejo (Kung Fu Software)
- Aditya Joshi (Walmart)

## Project Adoption
Based on what we see in Discord there is an adoption activity from people working on small companies and research purposes.
Consulting service companies are currently using Hyperledger Bevel for a CBDC PoC, which helps us keep the contributions alive and get enhancements for Bevels' source code.

## Goals
### Performance Against Prior Goals
- DLT Network deployments using just helm charts.
- Support of two possibilities of DLT Network deployments by using helm charts; 1. by using Vault and Ambassador or 2. without Vault and without ambassador
- Add support for cloud managed vaults.
- Use of Kubernetes operator for network orchestration.
- Support of Kubernetes 1.28+
- AWS Secrets manager integration.
- Stability of the operator and support of Fabric v3.0 using bevel-operator-fabric.
- Enhancements and bug fixes in the DLT platforms supported.
- Growing the community wise, we have done different workshop and demos throughout the year available on the LF Decentralized Trust youtube channel. Also, we have published different articles on the LF Decentralized Trust blog post which talk about different aspects of the technology and encourage people to get involved. [Check here](https://www.lfdecentralizedtrust.org/blog/using-hyperledger-bevel-to-add-a-privacy-layer-to-permissioned-besu-networks).

### Next Year's Goals
- Research of new privacy transaction managers for Ethereum based DLTs as Tessera has been deprecated.
- Support of new automation tools such as Terraform to deploy DLT networks on cloud environments.
- Fix bugs reported by the community that occur during the deployment of DLT networks, with greater emphasis on Fabric and Besu as they are the most widely used DLTs, although Besu is the most stable one we have. We need the DLTs we support to be consolidated and stable, as few reports from the community are related to deployment failures.
- Workshops and demos to help the community get introduced to the technology.
- Encourage contributions from community.

### Help Required
- Continue to work with LF Decentralized Trust staff to identify contributors and potential maintainers outside current maintainers and orgs, otherwise the project won't be able to be up to date with the latest versions and developments of every DLT we support.
- Mention Hyperledger Bevel as a means for deployment (on Kubernetes) on documentations of Hyperledger projects such as Fabric, Besu, Indy and Aries.

## Project Lifecycle Status Recommendation

Currently in `incubation`.
