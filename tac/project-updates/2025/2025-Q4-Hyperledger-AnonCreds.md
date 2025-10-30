[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2025 Q4 Hyperledger AnonCreds

Created by Stephen Curran with input from the Hyperledger AnonCreds Maintainers.

## Implementation Repositories

- [anoncreds-rs] - Rust implementation of AnonCreds
- [anoncreds-clsignatures-rs] - Rust implementation of CL Signatures used in [anoncreds-rs]. Moved from Ursa and enhanced.
- [anoncreds-v2-rs] - Rust implementation of AnonCreds v2, with support for both [BBS Signatures] and [PS Signatures].

[anoncreds-rs]: https://github.com/hyperledger/anoncreds-rs
[anoncreds-clsignatures-rs]: https://github.com/hyperledger/anoncreds-clsignatures-rs
[anoncreds-v2-rs]: https://github.com/hyperledger/anoncreds-v2-rs
[BBS Signatures]: https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-signatures/
[PS Signatures]: https://eprint.iacr.org/2015/525

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

Following last quarter's Webinars and Case Study highlighting deployments of the
AnonCreds project (from [Oracle Labs], [DSR]/[Hedera] and [InfoSys]) work this
quarter was mostly focused on enabling and updating integration components for
using AnonCreds in a variety of technical stacks. Support for Hedera with
AnonCreds was added to [Credo-TS] (via PRs for the [0.6 Alpha] and [0.5 Stable]
branches). As with the ACA-Py [Hedera] AnonCreds implementation, the heavy
lifting was done by [DSR], supported by [Hedera].

[Oracle Labs]: https://labs.oracle.com/
[DSR]: https://dsr-corporation.com/
[Hedera]: https://hedera.foundation/
[InfoSys]: https://www.infosys.com/
[Credo-TS]: https://github.com/openwallet-foundation/credo-ts
[0.6 Alpha]: https://github.com/openwallet-foundation/credo-ts/pull/2405
[0.5 Stable]: https://github.com/openwallet-foundation/credo-ts/pull/2437

The other effort this quarter was focused on library dependency updates and
(especially JavaScript) wrapper releases necessary for mobile wallets running on
Android -- supporting the "16kb page" requirement for Android apps. With a
deadline of November 2025 established by Google for apps in the Play Store, this
work was critical for mobile wallet developers using AnonCreds.

Few updates beyond maintenance activities were needed in the AnonCreds codebases
this quarter, as the implementations are stable and in use in production
systems. The focus remains on community engagement and supporting the broader
ecosystem of projects using AnonCreds. Minimal work was done on the AnonCreds v1
Revocation Registry size expansion this quarter, although the effort remains in
the plans.

The [AnonCreds Quarterly Activity Dashboard] has been updated to include the
existing repos as well as the new `hyperledger-anoncreds` organization. The
dashboard shows the activity in the past quarter, which is lower than previous
quarters, but still healthy.

[AnonCreds Quarterly Activity Dashboard]: https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=anoncreds&routedFrom=Github&bestPractice=false&dateFilters=Last%20Quarter&dateRange=2025-07-01%20to%2025-09-30&compare=PP&granularity=week&hideBots=true&repository=

## Questions/Issues for the TAC

None.

## Releases

- [anoncreds-rs] -- [v0.2.1](https://github.com/hyperledger/anoncreds-rs/releases/tag/v0.2.1), [v0.2.2](https://github.com/hyperledger/anoncreds-rs/releases/tag/v0.2.2)
- [anoncreds-clsignatures-rs] — None
- [anoncreds-v2-rs] - None

## Overall Activity in the Past Quarter

Since the last Quarterly Report, the key efforts are highlighted in the
[Project Health](#project-health) section above.

## Current Plans

Contributing to the conversation happening in the broader community about new
ways to use ZKPs for achieving unlinkable VC presentations, and determining how
to leverage that work into expanding efforts on AnonCreds, or using the
resources of AnonCreds together with those efforts. The new [longfellow-zk]
project and [BBS Signatures] are the key projects on the horizon.

[longfellow-zk]: https://github.com/google/longfellow-zk
[BBS Signatures]: https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-signatures/

Moving ahead with the work on the AnonCreds v1 Revocation Registry size
expansion, with a focus on the data management, performance and ease of
deployment aspects of the change.

Update the GitHub organization from "hyperledger" to "hyperledger-anoncreds".
Evaluation is needed to determine the CI/CD impacts of that change.

## Maintainer Diversity

The AnonCreds project now has nine maintainers from seven different
organizations.

## Contributor Diversity

The problem of supporting Android's 16kb page limit has driven contributions,
with developers from multiple organizations contributing to the effort to update
AnonCreds and other digital trust Rust libraries and wrappers.

## Additional Information

- Key channels on Hyperledger Discord: \#anoncreds, \#anoncreds-spec,
\#anoncreds-rs
- [AnonCreds Mailing List](https://lists.hyperledger.org/g/anoncreds)
- Meetings pages
  - [AnonCreds Working Group](https://wiki.hyperledger.org/display/ANONCREDS/Meetings%3A+AnonCreds+Working+Group)
