[//]: # (SPDX-License-Identifier: CC-BY-4.0)

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

[TAC Meeting Recording - 2025.03.06](https://zoom.us/rec/play/eq8yfXAkOWIPbqfjWAwmzsIPzRKDTXBoXY27NQReWGeLWuATDrIU7bQb6J0wgLvJPTwFtXKTnebWA0bG.AukIVgJR1j5hTz9G?accessLevel=meeting&canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fzoom.us%2Frec%2Fshare%2FEWc7elJj8J5ulXwXZG8aOZuoQjK5ZNrb1beOs4CoJZuiFXq051wiks8wU3Dm8j-l.46-6EBHM5lY-RcRi) -- AnonCreds Annual Review discussion starts at time 41:45. mark.

### Project Health & Activity

The Hyperledger AnonCreds project has reached a stable phase for v1, with development efforts shifting toward maintenance and adoption rather than active feature expansion. The transition to a ledger-agnostic model and alignment with the W3C Verifiable Credentials Data Model (VCDM) represent significant milestones that reduce the need for frequent updates.

Development on AnonCreds v2, however, has been inconsistent, reflecting broader challenges in the ZKP-based credentialing ecosystem. Competing approaches and a fragmented industry landscape continue to slow standardization and adoption, leaving the project's long-term trajectory uncertain.

### Maintainer Diversity & Governance

The project is supported by nine maintainers representing six organizations, providing a stable governance structure. However, sustained engagement from contributors, particularly in advancing AnonCreds v2, will be essential to driving future progress.

### Adoption & Market Positioning

AnonCreds remains a core component of the Hyperledger Aries and Indy ecosystems, though new public deployments have been limited. The lack of an ADOPTERS file makes it difficult to measure real-world traction. Meanwhile, competing credentialing approaches, such as SD-JWTs and ISO mDL, continue to gain industry attention, increasing competitive pressure.

To reinforce its market position, the project would benefit from improved adoption tracking and stronger messaging around AnonCreds’ privacy-preserving advantages compared to emerging alternatives.

### Key Ecosystem Dependencies

AnonCreds adoption is primarily driven by integrations with:

[ACA-Py](https://github.com/openwallet-foundation/acapy) – The primary mechanism for issuing and verifying AnonCreds-based credentials.

[Credo-TS](https://github.com/openwallet-foundation/credo-ts) – A TypeScript-based credentialing library, extending support to JavaScript/Node.js environments.

[Bifold Wallet](https://github.com/openwallet-foundation/bifold-wallet) - A React Native wallet based on [Credo-TS](https://github.com/openwallet-foundation/credo-ts).

These frameworks remain critical to AnonCreds’ ecosystem, but integration of AnonCreds v2 has been slow. Ensuring a smooth migration path from v1 to v2 will be a priority as Aries-based ecosystems explore alternative credential formats.

### Challenges & Future Focus Areas

Specification & Standardization – While AnonCreds v1 has stabilized, finalizing the AnonCreds v2 specification remains an outstanding task. Broader industry alignment on ZKP-based credentials is still a challenge.

Interoperability & Competing Models – The growing adoption of SD-JWTs and non-ZKP-based credential formats requires AnonCreds to emphasize its unique privacy-preserving advantages.

Scalability & Revocation – Progress has been made on the ALLOSAUR revocation model, but further work is needed to ensure deployment-ready solutions.

### Next Steps & Recommendations

Accelerate AnonCreds v2 implementation in ACA-Py and Credo-TS to provide a clear transition path.

Improve transparency in adoption tracking through an ADOPTERS file or detailed case studies.

Strengthen competitive positioning by highlighting the privacy benefits of ZKP-based credentials.

Consider refining branding for AnonCreds v2 to clarify its role as a next-generation credentialing solution.

### Project Lifecycle Recommendation

AnonCreds remains in Incubation. While it is one of the most widely deployed privacy-preserving credentialing solutions, the adoption of AnonCreds v2 will be a critical factor in determining its path toward Graduation. Stronger industry collaboration and more structured adoption tracking will be key to ensuring continued relevance.
