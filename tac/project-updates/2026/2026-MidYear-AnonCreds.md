[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Mid-Year Review AnonCreds

## Project Health

AnonCreds LFX Insights Page for [YTD 2026](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=anoncreds&routedFrom=Github&dateFilters=2026-01-01%20to%202026-08-31&dateRange=2026-01-01%20to%202026-08-31&compare=PP&granularity=month&hideBots=true) (v. [2025](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=anoncreds&routedFrom=Github&dateFilters=2025-01-01%20to%202025-08-31&dateRange=2025-01-01%20to%202025-12-31&compare=PP&granularity=month&hideBots=true)).

Development activity in 2026 has continued at a maintenance mode level with
AnonCreds v1 at maturity, stable specifications and regular maintenance code
updates. There has been no demand for substantial changes, and development has
naturally dropped into maintenance and adoption. Where activity has continued is
in the use of AnonCreds and the addition of new components linking Digital Trust
frameworks such as [ACA-Py], [Credo-TS] and the [Bifold Wallet] to verifiable
data registries (VDR) such as [Cheqd], [Hedera], and [did:webvh Server].
Recently added to the stable of DID Methods supporting ACA-Py is the [Archon
AnonCreds] plugin for [ACA-Py] that supports AnonCreds using the [did:cid] DID
Method and [Archon] as the verifiable data registry. This expands the choices
for those deploying AnonCreds v1. The variety of choices makes it easy for
deployers to root credentials in the VDR of their choice. Regular releases of
the [AnonCreds JavaScript wrapper] continued to support evolving Mobile OS
dependencies.

No progress has been made on AnonCreds v2 and it is clear it will not be a path
to a "modern" ZKP solution. In an update of information from past reports, the
broader landscape of ZKP-based verifiable credentials remains fragmented, but
with some progress recent. Notably, Google's [Longfellow-ZK] in the [Multipaz
Project], [BBS Signatures] and the [IETF CFRG BBS Work] (plus the [BBS Per
Verifier Linkability]), and [ZK Efforts in the EU]. Those efforts are not
merging into a united outcome, but there is progress being made on each individually.
As far as we are aware, AnonCreds v1 and AnonCreds v2 (based on [BBS Signatures]
or [PS Signatures]) remain the only complete verifiable credential ZKP solutions
that include zero-knowledge revocation capabilities.

[IETF CFRG BBS Work]: https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-signatures/
[BBS Signatures]: https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-signatures/
[BBS Per Verifier Linkability]: https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-per-verifier-linkability/
[ZK Efforts in the EU]: https://hpi.de/lehmann/eudi.html
[Longfellow-ZK]: https://github.com/google/longfellow-zk
[Multipaz Project]: https://github.com/openwallet-foundation/multipaz
[PS Signatures]: https://eprint.iacr.org/2015/525

## Maintainer Diversity

The project currently has **10 maintainers** from **6 organizations**.

AnonCreds teams and a list of repositories can be found in the [AnonCreds GitHub organization Control file](https://github.com/anoncreds/governance/blob/main/config.yaml).

## Project Adoption

Information on adoption is hard to find about AnonCreds and the projects that
build on AnonCreds (such as [ACA-Py], [Credo-TS], [VCX], [Indy], [Cheqd],
[Hedera], [did:webvh], [Archon], and more). AnonCreds is in use wherever
implementors want to use privacy-preserving credentials **today**.

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
[Archon]: https://github.com/archetech/archon
[did:cid]: https://archon.technology/specs
[Archon AnonCreds]: https://github.com/Flaxscrip/anoncreds-didcid

Adoption remains steady among early implementors, but the use of non-privacy-preserving VC schemes (e.g., [SD-JWTs] and [ISO mDL]) continues to (unfortunately) gain momentum. Google's [Longfellow-ZK], as found in the OWF [Multipaz Project] stands as a possibility to enable privacy with existing [ISO mDL] infrastructure. While various initiatives explore ZKP-based credentials, a **complete, easy-to-use solution** similar to AnonCreds v1 does not currently exist in the broader ecosystem.

[SD-JWTs]: https://datatracker.ietf.org/doc/draft-ietf-oauth-selective-disclosure-jwt/
[ISO mDL]: https://www.iso.org/standard/69084.html

## Performance Against Prior Goals

### **Achievements:**

✅ **Maintain and support AnonCreds v1** for ongoing adoption.
❌ **Enhance BBS+ Signatures in AnonCreds v2** to align with industry trends.
❌ **Foster collaboration across ZKP-based VC initiatives** to unify efforts.

The latter was worked on throughout the year to limited success. The broader ZK-based verifiable credential communities remain stubbornly isolated.

### **Outstanding Tasks:**

❌ **Develop deployment-ready tools for AnonCreds v2 scalable revocation**.
❌ **Rebrand AnonCreds v2?** Exploring "AnonCredsBBS" to differentiate it as a next-gen solution.

## Next Year's Goals

🔹 **Maintain and support AnonCreds v1** for ongoing adoption.

## Help Required

At this time, there are no specific areas where the AnonCreds project itself requires direct assistance from the TAC. While collaboration within the broader ZKP-based VC ecosystem remains a challenge, those efforts are primarily external to this committee's scope. Help from the organizations represented on the TAC would be appreciated!

## Project Lifecycle Stage Recommendation

AnonCreds remains an **Incubation project**. While it is one of the most mature
and widely used privacy-preserving credential frameworks, broader adoption of
ZK-based verifiable credentials and the lack of success of AnonCreds v2 (despite
an impressive and complete outcome) will be the factors in determining if it
progresses toward Graduation.
