[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Annual Review AnonCreds

## Project Health

AnonCreds LFX Insights Page for [Calendar Year 2025](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=anoncreds&routedFrom=Github&dateFilters=2025-01-01%20to%202025-12-31&dateRange=2025-01-01%20to%202025-12-31&compare=PP&granularity=month&hideBots=true) (v. [2024](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=anoncreds&routedFrom=Github&dateFilters=2024-01-01%20to%202024-12-31&dateRange=2024-01-01%20to%202024-12-31&compare=PP&granularity=month&hideBots=true))  and for [Q1 2026 Oct-Dec.](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=anoncreds&routedFrom=Github&dateFilters=2025-10-01%20to%202025-12-31&dateRange=2025-10-01%20to%202025-12-31&compare=PP&granularity=month&hideBots=true) (v. [Q4 2025](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=anoncreds&routedFrom=Github&dateFilters=2025-07-01%20to%202025-09-30&dateRange=2025-07-01%20to%202025-09-30&compare=PP&granularity=month&hideBots=true)).

Development activity in 2025 continued at a maintenance mode level with AnonCreds v1 at maturity, stable specifications and regular maintenance releases. There has been no demand for substantial changes, and development has naturally dropped into maintenance and adoption. Where activity has continued is in the use of AnonCreds and the addition of new components linking Digital Trust frameworks such as [ACA-Py], [Credo-TS] and the [Bifold Wallet] to verifiable data registries (VDR) such as [Cheqd], [Hedera], and [did:webvh Server]. This expands the choices for those deploying AnonCreds v1 -- making it easy to root credentials in the VDR of their choice. Regular releases of the [AnonCreds JavaScript wrapper] continued to support evolving Mobile OS dependencies (e.g. the Android 16kb Page issue).

The transition of the AnonCreds repos from the Hyperledger GitHub organization to a new "anoncreds" GitHub organization has been completed, with [all repositories](https://github.com/orgs/anoncreds/repositories?type=all) in their new home. [Three remaining repositories](https://github.com/orgs/hyperledger/repositories?q=AnonCreds) in the Hyperledger GitHub organization provide for the automatic redirection of specs and docs published via GH-Pages. After the move, artifact generation (e.g. to PyPi, NPM, GHCR, etc.) was confirmed and as appropriate, new releases generated.

Little progress has been made on AnonCreds v2 due to the slow overall progress of ZK-based verifiable credentials/tweaks and the corresponding lack of interest from organizations wanting to contribute. In a repeat of information from last year's report, the broader landscape of ZKP-based verifiable credentials remains fragmented, with various groups pursuing their own solutions. The rush to get something out and distracted from getting something privacy-preserving. Different groups appear and highlight the need for ZK-based Credentials in all parts of the world -- but then they continue their local focus, often with under-funded efforts. Progress is being made (see Google's [Longfellow-ZK], [IETF CFRG BBS Work], and [ZK proposals in the EU], amongst others), but the work is not merging into a united effort. Worse, none of the ZK solutions include a ZK-based revocation scheme. AnonCreds v1 and AnonCreds v2 (based on [BBS Signatures] or [PS Signatures]) remain the only complete solutions. Key projects were keeping an eye on in the space include:

- Google's [Longfellow-ZK] project ([Longfellow-ZK analysis])
- Efforts to get the IETF [CFRG] to approve [BBS Signatures], [BBS Blind Secrets] and [BBS Per Verifier Linkability]
- [ZK Efforts in the EU] to meet the regulatory requirements for the EUDI Wallet and infrastructure

[CFRG]: https://datatracker.ietf.org/rg/cfrg/about/
[BBS Signatures]: https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-signatures/
[BBS Blind Signatures]: https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-blind-signatures/
[BBS Per Verifier Linkability]: https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-per-verifier-linkability/
[ZK Efforts in the EU]: https://hpi.de/lehmann/eudi.html
[Longfellow-ZK]: https://eprint.iacr.org/2024/2010
[Longfellow-ZK analysis]: https://news.dyne.org/longfellow-zero-knowledge-google-zk/

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

## TAC AnonCreds Annual Review Notes

Report approved at the 2026.03.26 TAC Meeting
[Recording](https://zoom.us/rec/play/NWRgHGflQ21cIByo2TwreYEBZDKJsXaUfGKtY6MTCwnGhkDqLUIFDKkMeZLGG21uQh0k3nnnrbSzAS7W.C1icA5Oy1G-zvUuU?accessLevel=meeting&canPlayFromShare=true&from=share_recording_detail&continueMode=true&oldStyle=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fzoom.us%2Frec%2Fshare%2Fj-Q1yi1p1nhdzx0MU_GOmxq2DP92ItYLuO2u796IGdHBkcZptxcyKN6dZgQZohDu.hRjthNCFaDdq9WXR)
-- AnonCreds Annual Review discussion starts at time 19:25 mark.

**The following notes are pulled from [this comment in the PR for this
report](https://github.com/LF-Decentralized-Trust/governance/pull/286#discussion_r2849854761).
The quoted sections come from the TAC review, with the response from the
AnonCreds team.**

Hi @dmueller2001 -- thanks for the thorough feedback on the Annual Report.  Here
is my response to the questions and points raised.

> From a TAC perspective, it would be helpful to more clearly articulate how
Longfellow-ZK relates strategically to AnonCreds. Is it viewed as complementary
(privacy layered into ISO ecosystems where AnonCreds could interoperate),
competitive (potentially reducing demand for AnonCreds-style credentials), or
something v2 should actively align with? Clarifying this positioning would help
us understand whether v2 is primarily waiting on ecosystem convergence or has an
opportunity to engage and influence it.

Longfellow-ZK is a different approach to ZKP from AnonCreds, so competitive. In
summary, Longfellow-ZK takes an arbitrary credential format (just ISO mDL at
this time) and provides a way for a Holder to present a Credential to a Verifier
in zero knowledge. Notably, I can selectively disclose data (already supported
in mDL), and prove control over the key used to bind the credential to my
device, **without sharing any linkable data**. Ideal for age verification.
Technically slower and more complicated than AnonCreds and BBS, and currently
without revocation or pseudonymous identifier support. However, it uses an
existing credential format — no change to the issuer or to the holder in
receiving the credential, and the same Credential can be used with
non-Longfellow-ZK verifiers. Implemented for ISO mDL and (maybe) planned for
SD-JWTs (although I understand their are extra challenges with that format).
Adding support in Wallets, and convincing/strong-arming Verifiers to use it will
be a challenge. However, the current Discord (and other platforms) age
verification mess might be the impetus needed.

> More broadly, the current framing reads as somewhat reactive — i.e., v2
progress is limited pending external alignment. It would be helpful to clarify
what forward progress is within the project’s control. Are there defined
milestones, interoperability pilots, or standards engagement efforts planned? Or
is v2 intentionally in a holding pattern?

Unfortunately, the slowdown is reactive — there is not a team to build on the
(excellent!) v2 capabilities. The majority of the code is from one Dev (Mike
Lodder) and he has moved to working in the PQ Cryptography space. No one else
has picked up the work. We’d love to have active development on the incredibly
valuable code base, but we’ve been unable to gain interest.

As well, with the focus of a broad (but very divided community) on what will be
the “winning” credential format and exchange protocol, it’s unlikely that
AnonCreds will be in the mix — we just don’t have the resources compared to ISO,
OpenID, and W3C VCs. AnonCreds v1 remains very relevant, but given the current
trajectory, deployers will either give in and use non-privacy preserving
technology, or will come together around either the extended BBS approaches (or
perhaps Longfellow-ZK). If they go with BBS, everything we have in AnonCreds v2
remains useful with the need to evolve to the “winning” credential format. To
date, I’ve been unsuccessful at getting organizations to contribute resources to
the project to move in that direction.

> ZK-based scalable revocation wasn’t the original driver of v2, but it has
become one of the few clear technical differentiators that would justify
ecosystem migration beyond simple cryptographic modernization. If v2 does not
materially advance revocation capabilities, it becomes less clear what would
compel existing v1 adopters — or new adopters — to migrate.

Revocation is a major issue for all ZK approaches, and while AnonCreds v2 has
the “best available” approach, it is not yet seen as crucial. Those advocating
for ZK and those developing their own ZK flavour are still focused on issuing,
holding, and verifying, haven’t looked yet at revocation/status. That will hit
them eventually — hard (pun intended)!

> Outstanding Tasks (Scalable Revocation & Rebranding) > > Regarding scalable
revocation for v2, this is a significant undertaking. It would be helpful to
understand whether this is an actively resourced priority or a longer-term
research objective. If scalable revocation is foundational to v2 viability and
differentiation, clearer roadmap signals would help set realistic expectations.

There is both a defined approach for improving v1 revocation scalability, and
the work already done in v2. There was some effort at pulling resources together
this past year to work on the v1 scalability, but the effort did not succeed.
The v2 approach is implemented and available — just not generating interest.

> Similarly, the potential rebranding (e.g., “AnonCredsBBS”) would benefit from
clearer articulation of intent. What specific problem does rebranding solve —
market positioning, ecosystem alignment, or technical differentiation? Without a
clearly defined strategic posture for v2 (primary growth vector vs. alignment
hedge), it is difficult to assess whether rebranding meaningfully advances the
project’s lifecycle trajectory.

Unfortunately, the rebranding discussion started after the horse had left the
barn. We tried very hard to position AnonCreds as independent of Indy, but in
the end, the casual observer not involved with LFDT did not get it.  That said,
if the progress on BBS continues, a team could evolve AnonCreds v2 to the
“winning” credential format and get value out of the source base.

> Lifecycle Clarity > > Overall, the ecosystem fragmentation is clear. The key
governance question for us as TAC members is not whether fragmentation exists,
but whether AnonCreds v2 has a defined and intentional path forward within that
environment. Clarifying that posture would help align expectations around
lifecycle status, future investment, and potential Graduation criteria.

Without much more interest in the AnonCreds v2 code base — maintainers! — it
does not seem to have a path forward. We worked on a roadmap previously and
could easily revive that and adjust to the current VC landscape. But that is
predicated on investment.  Can the TAC help with that?  And a related question —
is there a role for AnonCreds in the ZKP work that is part of the First Person
Project? To date there has been no crossover in those efforts.

AnonCreds v1 remains as relevant as ever, with the stable, mature code base
being kept current.