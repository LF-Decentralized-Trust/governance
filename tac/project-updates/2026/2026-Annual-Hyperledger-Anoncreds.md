[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Annual Review Hyperledger AnonCreds

## Project Health

Hyperledger AnonCreds LFX Insights Page for [Calendar Year 2025](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=anoncreds&routedFrom=Github&dateFilters=2025-01-01%20to%202025-12-31&dateRange=2025-01-01%20to%202025-12-31&compare=PP&granularity=month&hideBots=true) (v. [2024](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=anoncreds&routedFrom=Github&dateFilters=2024-01-01%20to%202024-12-31&dateRange=2024-01-01%20to%202024-12-31&compare=PP&granularity=month&hideBots=true))  and for [Q1 2026 Oct-Dec.](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=anoncreds&routedFrom=Github&dateFilters=2025-10-01%20to%202025-12-31&dateRange=2025-10-01%20to%202025-12-31&compare=PP&granularity=month&hideBots=true) (v. [Q4 2025](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=anoncreds&routedFrom=Github&dateFilters=2025-07-01%20to%202025-09-30&dateRange=2025-07-01%20to%202025-09-30&compare=PP&granularity=month&hideBots=true)).

Development activity in 2025 continued at a maintenance mode level with AnonCreds v1 at maturity, stable specifications and regular maintenance releases. There has been no demand for substantial changes, and development has naturally dropped into maintenance and adoption. Where activity has continued is in the use of AnonCreds and the addition of new components linking Digital Trust frameworks such as [ACA-Py], [Credo-TS] and the [Bifold Wallet] to verifiable data registries (VDR) such as [Cheqd], [Hedera], and [did:webvh Server]. This expands the choices for those deploying AnonCreds v1 -- making it easy to root credentials in the VDR of their choice. Regular releases of the [AnonCreds JavaScript wrapper] continued to support evolving Mobile OS dependencies (e.g. the Android 16kb Page issue).

The transition of the AnonCreds repos from the Hyperledger GitHub organization to a new "anoncreds" GitHub organization has been completed, with [all repositories](https://github.com/orgs/anoncreds/repositories?type=all) in their new home. [Three remaining repositories](https://github.com/orgs/hyperledger/repositories?q=AnonCreds) in the Hyperledger GitHub organization provide for the automatic redirection of specs and docs published via GH-Pages. After the move, artifact generation (e.g. to PyPi, NPM, GHCR, etc.) was confirmed and as appropriate, new releases generated.

Little progress has been made on AnonCreds v2 due to the slow overall progress of ZK-based verifiable credentials/tweaks and the corresponding lack of interest in . In a repeat of information from last year's report, the broader landscape of ZKP-based verifiable credentials remains fragmented, with various groups pursuing their own solutions. The rush to get something out and distracted from getting something privacy-preserving. Different groups appear and highlight the need for ZK-based Credentials in all parts of the world -- but then they continue their local focus, often with under-funded efforts. Progress is being made (see Google's [Longfellow-ZK], [IETF CFRG BBS Work], and [ZK proposals in the EU], amongst others), but the work is not merging into a united effort. Worse, none of the ZK solutions include a ZK-based revocation scheme. AnonCreds v1 and AnonCreds v2 (based on [BBS Signatures] or [PS Signatures]) remain the only complete solutions. Key projects were keeping an eye on in the space include:

- Google's [Longfellow-ZK] project
- Efforts to get the IETF [CFRG] to approve [BBS Signatures], [BBS Blind Secrets] and [BBS Per Verifier Linkability]
- [ZK Efforts in the EU] to meet the regulatory requirements for the EUDI Wallet and infrastructure

[CFRG]: https://datatracker.ietf.org/rg/cfrg/about/
[BBS Signatures]: https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-signatures/
[BBS Blind Signatures]: https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-blind-signatures/
[BBS Per Verifier Linkability]: https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-per-verifier-linkability/
[ZK Efforts in the EU]: https://hpi.de/lehmann/eudi.html

A consideration going into last year was trying to rebrand AnonCreds v2 and while that would still be a good path, there were enough naysayers in the ZK-based verifiable credentials community that we did not put effort into that approach.

## Maintainer Diversity

The project currently has **10 maintainers** from **6 organizations**.

AnonCreds teams and a list of repositories can be found in the [AnonCreds GitHub organization Control file](https://github.com/anoncreds/governance/blob/main/config.yaml).

## Project Adoption

Information on adoption is hard to find about AnonCreds and the projects that build on AnonCreds (such as [ACA-Py], [Credo-TS], [VCX], [Indy], [Cheqd], [Hedera], [did:webvh], and more). AnonCreds is in use wherever implementors want to use privacy-preserving credentials **today**.

[ACA-Py]: https://github.com/openwallet-foundation/acapy
[Credo-TS]: https://github.com/openwallet-foundation/credo-ts
[Bifold Wallet]: https://github.com/openwallet-foundation/bifold-wallet
[VCX]: https://github.com/openwallet-foundation/aries-vcx
[Indy]: https://github.com/hyperledger-indy/indy
[AnonCreds JavaScript wrapper]: https://github.com/anoncreds/anoncreds-wrapper-javascript
[Cheqd]: https://cheqd.io/
[Hedera]: https://hedera.com/
[did:webvh]: https://didwebvh.info
[did:webvh Server]: https://github.com/decentralized-identity/didwebvh-server-py

Adoption remains steady among early implementors, but the use of non-privacy-preserving VC schemes (e.g., [SD-JWTs] and [ISO mDL]) continues to (unfortunately) gain momentum. Google's [Longfellow-ZK] project stands as a possibility to enable privacy with existing [ISO mDL] infrastructure. While various initiatives explore ZKP-based credentials, a **complete, easy-to-use solution** similar to AnonCreds v1 does not currently exist in the broader ecosystem.

[SD-JWTs]: https://datatracker.ietf.org/doc/draft-ietf-oauth-selective-disclosure-jwt/
[ISO mDL]: https://www.iso.org/standard/69084.html

## Performance Against Prior Goals

### **Achievements:**

✅ **Maintain and support AnonCreds v1** for ongoing adoption.
✅ **Enhance BBS+ Signatures in AnonCreds v2** to align with industry trends.
❌ **Foster collaboration across ZKP-based VC initiatives** to unify efforts.

The latter was worked on throughout the year to limited success. The broader ZK-based verifiable credential communities remain stubbornly isolated.

### **Outstanding Tasks:**

❌ **Develop deployment-ready tools for AnonCreds v2 scalable revocation**.
❌ **Rebrand AnonCreds v2?** Exploring "AnonCredsBBS" to differentiate it as a next-gen solution.

## Next Year's Goals

🔹 **Maintain and support AnonCreds v1** for ongoing adoption.
🔹 **Foster collaboration across ZKP-based VC initiatives** to unify efforts.

## Help Required

At this time, there are no specific areas where the AnonCreds project itself requires direct assistance from the TAC. While collaboration within the broader ZKP-based VC ecosystem remains a challenge, those efforts are primarily external to this committee's scope. Help from the organizations represented on the TAC would be appreciated!

While not specific to AnonCreds, but fundamental to verifiable credentials overall, the most critical requirement for Digital Trust deployers is **long-term flexibility** across credential formats and exchange protocols. As these inevitably evolve, a **standard abstraction layer** that isolates business logic from protocol and format churn is essential. Such an abstraction would allow organizations to confidently issue, revoke, hold, request, present, and verify credentials without coupling their systems to what happens to be the “best” format or protocol today—or facing costly rewrites when that answer changes. We recommend the LFDT TAC prioritize a project explicitly focused on delivering this capability.

## Project Lifecycle Stage Recommendation

AnonCreds remains an **Incubation project**. While it is one of the most mature and widely used privacy-preserving credential frameworks, broader adoption of ZK-based verifiable credentials and the whether the work already put into AnonCreds v2 will be the factors in determining if it progresses toward Graduation.

## TAC Hyperledger AnonCreds Annual Review Notes

TAC Meeting Recording - 2026.XX.YY (to be added) -- AnonCreds Annual Review discussion starts at time XX:XX. mark.

*Notes from the TAC reviewers to be added.*
