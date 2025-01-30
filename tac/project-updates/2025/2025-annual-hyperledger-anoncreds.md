---
layout: default
title: 2025 Annual Review Hyperledger AnonCreds
parent: Project Updates
grand_parent: LF Decentralized Trust TAC
nav_exclude: true
---

# 2025 Annual Review Hyperledger AnonCreds

## Project Health

Hyperledger AnonCreds LFX Insights Page for [Calendar Year 2024](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=anoncreds&routedFrom=Github&dateFilters=2024-01-01%20to%202024-12-31&dateRange=2024-01-01%20to%202024-12-31&compare=PP&granularity=month&hideBots=true) (v. [2023](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=anoncreds&routedFrom=Github&dateFilters=2023-01-01%20to%202023-12-31&dateRange=2023-01-01%20to%202023-12-31&compare=PP&granularity=month&hideBots=true))  and for [Q1 2025 Oct-Dec.](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=anoncreds&routedFrom=Github&dateFilters=2024-10-01%20to%202024-12-31&dateRange=2024-10-01%20to%202024-12-31&compare=PP&granularity=month&hideBots=true) (v. [Q4 2024](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=anoncreds&routedFrom=Github&dateFilters=2024-07-01%20to%202024-09-30&dateRange=2024-07-01%20to%202024-09-30&compare=PP&granularity=month&hideBots=true)).

Development activity in 2024 has slowed compared to 2023 as AnonCreds v1 has reached maturity, with stable specifications and continued maintenance releases. The major milestone in 2023 was making AnonCreds "ledger-agnostic" and fully compliant with the W3C VCDM. Since then, there has been no demand for substantial changes, and development has naturally dropped into maintenance and adoption.

Efforts on AnonCreds v2 have progressed intermittently. The broader landscape of ZKP-based verifiable credentials remains fragmented, with various groups pursuing their own solutions. Attempts to unify these efforts under a common vision have not yet been successful.

## Maintainer Diversity

The project currently has **9 maintainers** from **6 organizations**.

AnonCreds teams and a list of repositories can be found in the [Hyperledger GitHub organization Control file](https://github.com/hyperledger/governance/blob/main/access-control.yaml).

## Project Adoption

Information on adoption is hard to find about AnonCreds and the projects that build on AnonCreds (such as [ACA-Py], [Credo-TS], [Aries VCX], [Indy] and more). AnonCreds is in use wherever implementors want to use privacy-preserving credentials **today**.

[ACA-Py]: https://github.com/openwallet-foundation/acapy
[Credo-TS]: https://github.com/openwallet-foundation/credo-ts
[Aries VCX]: https://github.com/hyperledger/aries-vcx
[Indy]: https://github.com/hyperledger/indy

Adoption remains steady among pre-2023 implementors, but the use of non-privacy-preserving VC schemes (e.g., [SD-JWTs](https://datatracker.ietf.org/doc/draft-ietf-oauth-selective-disclosure-jwt/) and [ISO mDL](https://www.iso.org/standard/69084.html)) is gaining momentum. While various initiatives explore ZKP-based credentials, a **complete, easy-to-use solution** similar to AnonCreds v1 does not currently exist in the broader ecosystem.

## Performance Against Prior Goals

### **Achievements:**

✅ **Implemented abstraction of the signature scheme**, allowing AnonCreds v2 to support both [BBS](https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-signatures/) and [PS](https://eprint.iacr.org/2015/525) signatures—significantly enhancing flexibility.
✅ **Maintained and deployed AnonCreds v1** with W3C format support across Aries frameworks and implementations.
✅ **W3C VC/VP Data Model support**—Implemented in AnonCreds, [ACA-Py] and [Credo-TS].

### **Outstanding Tasks:**

❌ **Completion of AnonCreds v1 specification**—Technical aspects are complete, but editorial work was deprioritized due to lack of interest in formal standardization.
❌ **Draft AnonCreds v2 specification**—While the implementation is evolving, formalizing the data model remains incomplete.
❌ **Post-quantum security experimentation**—Some related work has been done with Post Quantum PS Signatures, but not directly in AnonCreds v2.
❌ **Enhancements for holder binding, date encodings, and migration paths from v1 to v2**—Work remains to be done.

### **Revocation Work:**
Progress was made via the [Hyperledger Mentorship Program](https://lf-hyperledger.atlassian.net/wiki/display/INTERN) and [Revocation Manager Project](https://lf-hyperledger.atlassian.net/wiki/spaces/INTERN/pages/21960785/Hyperledger+AnonCreds+v2+ZKP-based+Credential+Revocation+Manager+Implementation) to implement **ALLOSAUR**, a scalable ZKP-based revocation scheme.

## Next Year's Goals

🔹 **Maintain and support AnonCreds v1** for ongoing adoption.
🔹 **Foster collaboration across ZKP-based VC initiatives** to unify efforts.
🔹 **Enhance BBS+ Signatures in AnonCreds v2** to align with industry trends.
🔹 **Develop deployment-ready tools for AnonCreds v2 scalable revocation**.
🔹 **Rebrand AnonCreds v2?** Exploring "AnonCredsBBS" to differentiate it as a next-gen solution.

## Help Required

At this time, there are no specific areas where we require direct assistance from the TAC. While collaboration within the broader ZKP-based VC ecosystem remains a challenge, those efforts are primarily external to this committee's scope. The key focus for LFDT are the tools available for getting the word out about the progress on AnonCreds v2.

## Project Lifecycle Stage Recommendation

AnonCreds remains an **Incubation project**. While it is one of the most mature and widely used privacy-preserving credential frameworks, broader adoption of AnonCreds v2 will be the key factor in determining if it progresses toward Graduation.

## TAC Hyperledger AnonCreds Annual Review Notes

*To be added after the TAC Meeting that covers the AnonCreds Annual Report.*

[TAC Meeting Recording - 2025.02.XX](#) -- AnonCreds Annual Review discussion starts at the X:XX mark.
