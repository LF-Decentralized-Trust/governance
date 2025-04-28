---
layout: default
title: 2025 Q2 Hyperledger AnonCreds
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

A significant advance was completed since the last Hyperledger AnonCreds Quarterly Report with an update to make signature scheme in AnonCreds v2 pluggable, and the addition of support in the implementation for [BBS Signatures]. The momentum in other organizations, including W3C, to promote the use of BBS Signatures, this is a significant advance. AnonCreds v2 also supports [PS Signatures], and since there is a [post-quantum version of PS Signatures], it is conceivable that a PQ implementation of AnonCreds v2 could be investigated. No one has volunteered for that work, but it would be a fantastic initiative.  We considered it for a mentorship project, but felt it was too ambitious for that program.

[PS Signatures]: https://eprint.iacr.org/2015/525.pdf
[post-quantum version of PS Signatures]: https://eprint.iacr.org/2024/131.pdf

A successful [AnonCreds v2 Webinar] was held this Quarter (March 2025), with 227 Meetup registrants, 70+ live attendees on Zoom and YouTube, and 228 views of the [YouTube Recording] (so far). We'll see how that impacts the trajectory of the project.

[AnonCreds v2 Webinar]: https://www.meetup.com/lfdt-austin/events/306421179/?recId=538c6ded-cd29-470e-9840-128a7ea01f9e&recSource=event-search&searchId=81e5d87a-b836-4b7b-81f6-33fa704a0f51&eventOrigin=find_page$all
[YouTube Recording]: https://youtu.be/fElVhhBviUU

The [AnonCreds Quarterly Activity Dashboard] is not useful as of the writing of this report, as the LFX Insights scope for AnonCreds is for the newly created "anoncreds" organization, which is not where the AnonCreds repositories reside.

[AnonCreds Quarterly Activity Dashboard]: https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=anoncreds&routedFrom=Github&bestPractice=false&dateFilters=Last%20Quarter&dateRange=2024-10-01%20to%2025-03-31&compare=PP&granularity=week&hideBots=true&repository=

The AnonCreds 2024 Mentorship project was completed, with the implementation of an AnonCreds v2 Revocation Manager.

Attendance at the AnonCreds Working Group meetings continues to be low.

## Questions/Issues for the TAC

None.

## Releases

- [anoncreds-rs] -- None
- [anoncreds-clsignatures-rs] — None
- [anoncreds-v2-rs] - v2.0, v2.1

## Overall Activity in the Past Quarter

Since the last Quarterly Report, there has been the completion of a significant audit in the `agora-blsful` BLS Signatures implementation in the LFDT Labs [Agora]
project.

## Current Plans

Contributing to the conversation happening in the broader community
about new ways to use ZKPs for achieving unlinkable VCs, and determining how to
leverage that work into expanding efforts on AnonCreds, or using the resources
of AnonCreds together with those efforts.

Continuing to collaborate with a team from Oracle Labs in creating a ZKP abstraction layer
that isolates VC operations (issuing credentials, creating presentations, and
verifying presentations) from the cryptographic libraries used in specific
implementations.

Update the GitHub organization from "hyperledger" to "hyperledger-anoncreds". Evaluation is needed to determine the CI/CD impacts of that change.

## Maintainer Diversity

After the recent cleanup of inactive Hyperledger Maintainers, the AnonCreds
project now has nine maintainers from seven different organizations.

## Contributor Diversity

We don't have access to the LFX Insights for this report, but I'm aware of contributions in the quarter from
at least 3 different organizations.

## Additional Information

- Key channels on Hyperledger Discord: \#anoncreds, \#anoncreds-spec,
\#anoncreds-rs
- [AnonCreds Mailing List](https://lists.hyperledger.org/g/anoncreds)
- Meetings pages
  - [AnonCreds Working Group](https://wiki.hyperledger.org/display/ANONCREDS/Meetings%3A+AnonCreds+Working+Group)
