---
layout: default
title: 2025 Q3 Hyperledger AnonCreds
parent: 2025
grand_parent: Project Updates
---

Created by Stephen Curran with input from the Hyperledger AnonCreds Maintainers.

## Implementation Repositories

- [anoncreds-rs] - Rust implementation of AnonCreds
- [anoncreds-clsignatures-rs] - Rust implementation of CL Signatures used in [anoncreds-rs]. Moved from Ursa and enhanced.
- [anoncreds-v2-rs] - Rust implementation of AnonCreds v2, now with [BBS Signatures] support

[anoncreds-rs]: https://github.com/hyperledger/anoncreds-rs
[anoncreds-clsignatures-rs]: https://github.com/hyperledger/anoncreds-clsignatures-rs
[anoncreds-v2-rs]: https://github.com/hyperledger/anoncreds-v2-rs
[BBS Signatures]: https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-signatures/

### Specifications

- [AnonCreds Specification] published from the repository [anoncreds-spec]
- [AnonCreds Methods Registry] published from the repository [anoncreds-methods-registry]

[anoncreds-spec]: https://github.com/hyperledger/anoncreds-spec
[AnonCreds Specification]: https://hyperledger.github.io/anoncreds-spec/
[anoncreds-methods-registry]: https://github.com/hyperledger/anoncreds-methods-registry
[AnonCreds Methods Registry]: https://hyperledger.github.io/anoncreds-methods-registry

### Web and Wiki Pages

- [Hyperledger AnonCreds Website Home Page]
- [Hyperledger AnonCreds Wiki Home Page]

[Hyperledger AnonCreds Website Home Page]: https://www.lfdecentralizedtrust.org/projects/anoncreds
[Hyperledger AnonCreds Wiki Home Page]: https://lf-hyperledger.atlassian.net/wiki/spaces/ANONCREDS/overview

## Project Health

This quarter saw several excellent LFDT Webinars and a Case Study highlighting deployments of the AnonCreds project by large enterprise organizations, including [Oracle Labs], [DSR]/[Hedera] and [InfoSys]. These webinars are part of the LFDT and the broader AnonCreds community to raise awareness of the ease of deployment, privacy and power of AnonCreds-based digital trust services. The resources included:

* [LF Decentralized Trust webinar with **DSR**: Hiero - ACA-Py Plugin for the **Hedera** Ledger](https://www.lfdecentralizedtrust.org/learn/webinars/-hiero-aca-py-plugin-for-the-hedera-ledger)
* [LF Decentralized Trust webinar with **Oracle**: Self-Sovereign Identity on Hyperledger Fabric VDR with OWF Credo Agents and Privacy-preserving AnonCreds Verifiable Credentials](https://www.lfdecentralizedtrust.org/learn/webinars/oracle-self-sovereign-identity-on-hyperledger-fabric-vdr)
* [Trust (or not) but verify: **Infosys** uses Hyperledger Indy and ACA-Py to create fast, secure, and private credential verification](https://www.lfdecentralizedtrust.org/case-studies/infosys-uses-hyperledger-indy-and-aca-py-to-create-fast-secure-and-private-credential-verification)

[Oracle Labs]: https://labs.oracle.com/
[DSR]: https://dsr-corporation.com/
[Hedera]: https://hedera.foundation/
[InfoSys]: https://www.infosys.com/

On the technical front, work has begun on greatly expanding the size of the AnonCreds v1 Revocation Registry size from around 3k entries per registry to 500k or more entries per registry. The change does not impact the cryptography of the approach, but rather changes how the revocation data is managed, furthering the change from publishing credential revocation statuses as deltas (lists of identifiers for revoked credentials) to publishing the entire state of the registry as a bit array. This work is still in the planning/technical spike phase, so is not reflected in the Activity Dashboard below.

The [AnonCreds Quarterly Activity Dashboard] has been updated to include the existing repos as well as the new `hyperledger-anoncreds` organization. The dashboard shows the activity in the past quarter, which is lower than previous quarters, but still healthy.

[AnonCreds Quarterly Activity Dashboard]: https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=anoncreds&routedFrom=Github&bestPractice=false&dateFilters=Last%20Quarter&dateRange=2025-04-01%20to%2025-06-30&compare=PP&granularity=week&hideBots=true&repository=

## Questions/Issues for the TAC

None.

## Releases

- [anoncreds-rs] -- None
- [anoncreds-clsignatures-rs] — None
- [anoncreds-v2-rs] - None

## Overall Activity in the Past Quarter

Since the last Quarterly Report, the key efforts are hightlighted in the
[Project Health](#project-health) section above. The AnonCreds project has been
stable, with no new releases in the past quarter, and no major issues or changes
to the codebase. The focus has been on community engagement and experimenting
with large revocation registries for AnonCreds v1.

## Current Plans

Contributing to the conversation happening in the broader community about new
ways to use ZKPs for achieving unlinkable VCs, and determining how to leverage
that work into expanding efforts on AnonCreds, or using the resources of
AnonCreds together with those efforts. The new [zk-Longfellow] project and [BBS
Signatures] are the key projects on the horizon.

Moving ahead with the work on the AnonCreds v1 Revocation Registry size expansion, with a focus on the data management, performance and ease of deployment aspects of the change.

Update the GitHub organization from "hyperledger" to "hyperledger-anoncreds". Evaluation is needed to determine the CI/CD impacts of that change.

## Maintainer Diversity

After the recent cleanup of inactive Hyperledger Maintainers, the AnonCreds
project now has nine maintainers from seven different organizations.

## Contributor Diversity

There were few contributions in the past quarter because of the stability of the codebase. Conversations amongst the usual contributors continues.

## Additional Information

- Key channels on Hyperledger Discord: \#anoncreds, \#anoncreds-spec,
\#anoncreds-rs
- [AnonCreds Mailing List](https://lists.hyperledger.org/g/anoncreds)
- Meetings pages
  - [AnonCreds Working Group](https://wiki.hyperledger.org/display/ANONCREDS/Meetings%3A+AnonCreds+Working+Group)
