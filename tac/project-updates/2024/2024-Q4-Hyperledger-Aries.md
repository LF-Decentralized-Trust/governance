---
layout: default
title: 2024 Q4 Hyperledger Aries
parent: 2024
grand_parent: Project Updates
---

## Project Health

Work on [Hyperledger Aries] related projects continues at a healthy pace, albeit
with some of that work now outside of the Aries itself. [ACA-Py] (formerly Aries
Cloud Agent Python) achieved two significant milestones this quarter. Release
1.0.0 was published, and the project moved to the [OpenWallet Foundation].
Within [Hyperledger Aries], progress was made on all of the frameworks -- [Aries VCX],
[Aries Framework Swift] and [Aries Framework Kotlin]. Other [Open Wallet
Foundation]-hosted projects, [Credo-TS] and [Bifold Wallet], continue to evolve
rapidly, with [Animo Solutions], key maintainers of [Credo-TS], selected by the
German Government into the next round of the the [Funke] ("sparkle") initiative
to create innovative wallet prototypes in preparation for the promised German
[EUDI Wallet] to be released by 2026. Exciting times!

In light of the move of ACA-Py and some related repositories, including [Askar]
to the [OpenWallet Foundation], there is some uncertainty about the other
sub-projects in Aries and whether they will stay in [Hyperledger Aries] or move
elsewhere. Stay tuned as the maintainers on the different projects decide how to
move forward.

[Funke]: https://www.sprind.org/en/challenges/eudi-wallet-prototypes/
[Animo Solutions]: https://animo.id/
[EUDI Wallet]: https://digital-strategy.ec.europa.eu/en/policies/eudi-wallet-implementation

[Hyperledger Aries]: https://www.lfdecentralizedtrust.org/projects/aries
[Credo-TS]: https://github.com/openwallet-foundation/credo-ts
[ACA-Py Repository]: https://github.com/openwallet-foundation/acapy
[Aries VCX]: https://github.com/hyperledger/aries-vcx
[OpenWallet Foundation]: https://openwallet.foundation/
[Aries Framework Swift]: https://github.com/hyperledger/aries-framework-swift
[Aries Framework Kotlin]: https://github.com/hyperledger/aries-framework-kotlin
[Askar]: https://github.com/openwallet-foundation/askar

## Questions/Issues for the TOC

None at this time.

## Releases

The following Aries releases occurred in the last two quarters (including the
time covered by the Annual Report and so not yet reported):

- [ACA-Py] ([ACA-Py Repository]) -- 0.11.2, 0.11.3, 0.12.2, **1.0.0** (w00t!!!!)
    - Note: 1.0.1 was published as the last ACA-Py release before the move of the repository to [OpenWallet Foundation] was made.
    - Additional LTS releases of ACA-Py (0.11.x, 0.12.x) may still occur from Hyperledger, if they are deemed necessary.
- [Askar] -- 0.3.2
- [Aries VCX] -- 0.65.0
- [Aries Framework Swift] -- 2.4.0, 2.5.0
- [Aries Framework Kotlin] -- 2.4.1

Interoperability status can be still be seen
here: [https://aries-interop.info](https://aries-interop.info).

## Overall Activity in the Past Quarter

Per the [Aries Activity Dashboard] for the months of July-September 2024, Aries
codebases had 396 Commits and 105 contributors representing at least 10
organizations.  The numbers do include the repositories
that have moved from Hyperledger to the Open Wallet Foundation, as well as some
obsolete (but unchanging) repositories. Per Ry Jones there is not a good way for
us to control the included list of repos.

[Aries Activity Dashboard]: https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=aries&routedFrom=Github&bestPractice=false&dateFilters=Last%20Quarter&dateRange=2024-07-01%20to%202024-09-30&compare=PP&granularity=week&hideBots=true

[DIDComm v2]: https://identity.foundation/didcomm-messaging/spec/
[ACA-Py]: https://aca-py.org

## Aries Framework Reports

### [Aries VCX]

Work is in-progress on fixing and enhancing fixing Android support, as well as
adding support for iOS. Support for usage via React Native will be considered in
the future as well. Additionally, work is planned and underway to improve the
overall ease of use of Aries VCX to boost its adoption.

### [ACA-Py]

As noted, the [ACA-Py] project completed the milestone 1.0.0 release this
quarter, and organized and executed the move from Hyperledger to the [OpenWallet
Foundation]. There is lots happening in the community, with PRs arriving daily
on things ranging from OpenID4VC support, improving DID handling (including the
[`did:tdw` DID Method]), cleaning up technical debt, improving the test
pipelines and more. There is a lot going on!

## Current Plans

- Determining where the repos remaining in Hyperledger should be long-term.
- Organizing the new calls that replace the Aries Working Group call.

[`did:tdw` DID Method]: https://bcgov.github.io/trustdidweb/

## Maintainer Diversity

After the removal by Hyperledger of the inactive maintainers, there are currently 33 people on the 29 Hyperledger Aries teams representing at least 18 organizations.

## Contributor Diversity

In the quarter there were commits from 105 individuals representing at least 10 organizations.

## Additional Information

None
