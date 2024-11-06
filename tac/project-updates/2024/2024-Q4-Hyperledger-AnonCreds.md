---
layout: default
title: 2024 Q4 Hyperledger AnonCreds
parent: 2024
grand_parent: Project Updates
---

Created by Stephen Curran with input from the Hyperledger AnonCreds Maintainers.

## Implementation Repositories

- [anoncreds-rs] - Rust implementation of AnonCreds
- [anoncreds-clsignatures-rs] - Rust implementation of CL Signatures used in [anoncreds-rs]. Moved from Ursa and enhanced.
- [anoncreds-v2-rs] - Rust draft implementation of AnonCreds v2 -- **new contribution this quarter**

[anoncreds-rs]: https://github.com/hyperledger/anoncreds-rs
[anoncreds-clsignatures-rs]: https://github.com/hyperledger/anoncreds-clsignatures-rs
[anoncreds-v2-rs]: https://github.com/hyperledger/anoncreds-v2-rs

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

Limited progress was made on the "next generation" AnonCreds project in the
quarter -- [anoncreds-v2-rs]. Contributions to the Hyperledger Labs [Agora] project
continued. Agora includes the [audited cryptographic libraries] that upon which
AnonCreds V2 is built. A Hyperledger Mentorship project has resulted in the
creation of an implementation of the scalable, privacy preserving
[ALLOSAUR revocation scheme] that is used in AnonCreds v2.

[ALLOSAUR revocation scheme]: https://eprint.iacr.org/2022/1362.pdf

The [AnonCreds Quarterly Activity Dashboard] shows the activity on the project
repositories from July to September 2024.

[AnonCreds Quarterly Activity Dashboard]: https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=anoncreds&routedFrom=Github&bestPractice=false&dateFilters=Last%20Quarter&dateRange=2024-07-01%20to%202024-09-30&compare=PP&granularity=week&hideBots=true&repository=

Attendance at the AnonCreds Working Group meetings has been low this quarter.

## Questions/Issues for the TOC

None.

## Releases

- [anoncreds-rs] -- None
- [anoncreds-clsignatures-rs] — None

## Overall Activity in the Past Quarter

There have been additional, significant contributions of code in the Hyperledger Labs [Agora]
project -- [audited cryptographic libraries].

[Agora]: https://labs.hyperledger.org/labs/agora.html
[audited cryptographic libraries]: https://github.com/hyperledger-labs?q=agora

## Current Plans

Completion of the new Revocation Manager Hyperledger Mentorship project. That
includes seeing where that implementation might be useful in AnonCreds v2 and
beyond.

Contributing to the conversation happening in the broader community
about new ways to use ZKPs for achieving unlinkable VCs, and determining how to
leverage that work into expanding efforts on AnonCreds, or using the resources
of AnonCreds together with those efforts.

Collaborating with a team for Oracle Labs in creating a ZKP abstraction layer
that isolates VC operations (issuing credentials, creating presentations, and
verifying presentations) from the cryptographic libraries used in specific
implementations.

## Maintainer Diversity

After the recent cleanup of inactivity Hyperledger Maintainers, the AnonCreds
project now has nine developers from from seven different organizations.

## Contributor Diversity

LFX Insights seems to suggest there have been contributions in the quarter from
at least 3 different organizations.

## Additional Information

- Key channels on Hyperledger Discord: \#anoncreds, \#anoncreds-spec,
\#anoncreds-rs
- [AnonCreds Mailing List](https://lists.hyperledger.org/g/anoncreds)
- Meetings pages
  - [AnonCreds Working Group](https://wiki.hyperledger.org/display/ANONCREDS/Meetings%3A+AnonCreds+Working+Group)
