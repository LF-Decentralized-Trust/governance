[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2025 Q4 Hyperledger Identus

## Project Health

The [LF Decentralized Trust Identus LFX Insight Dashboard](https://insights.linuxfoundation.org/project/open-enterprise-agent?timeRange=past365days&start=2024-11-19&end=2025-11-19) shows that we sustained **16 active contributors** during the past quarter with a **46% quarterly contributor retention rate**. The project stayed active on **307 of the last 365 days**, merged pull requests within **6 days on average**, and processed roughly **300 new pull requests per month**, highlighting a healthy development cadence. At the same time, the dashboard reiterates our dependency on a small set of contributors (3 people and essentially 1 sponsoring organization supplying >51% of the work) and a 43-day average issue resolution time, so expanding reviewer bandwidth and triage capacity remains a priority.

While Input Output Global (IOG) continues to be the primary maintainer, community members from [Blocktrust](https://www.blocktrust.dev/), [Socious.io](https://socious.io/), and [csign.io](https://csign.io/) kept contributing code and roadmap discussions, keeping the contributor and partner mix identical to Q3. `Neoprism` continued to mature as the high-volume PRISM DID indexer and is on track to fully replace the legacy `prism-node` component within the next six months.

---

## Questions/Issues for the TAC

No questions for the TAC.

---

## Releases

The Identus team shipped the [Identus Platform v2.16 release](https://github.com/hyperledger-identus/hyperledger-identus/releases/tag/v2.16) during Q4. Highlights include:

- **Mediator 1.2.0** – new MongoDB connection string configuration, dependency upgrades, and documentation polish.
- **Cloud Agent 2.1.0** – critical Ed25519 fix for revocation lists plus refreshed dependencies for the issuance stack.
- **`Neoprism` 0.6.2** – first-class onboarding of the standalone Cardano DID indexer that will eventually supplant `prism-node`.
- **SDK-TS 7.0.0** – plugin-based architecture, DIDComm internals overhaul, and a lightweight `did:prism` resolver, making issuance and wallet integrations easier to extend.
- Documentation portal updates to reflect all component-level changes.

Offline-first improvements and SDK issuance features that were planned earlier in the year landed in the TypeScript and Swift SDKs as part of this release; SDK-KMP will follow after its planned restructuring.

---

## Overall Activity in the Past Quarter

Community engagement on LFDT Discord, GitHub discussions, and the weekly maintainer syncs stayed steady, with contributors continuing to raise issues, test releases, and challenge roadmap assumptions. Offline-first work is nearing completion, and issuance capabilities are now available in SDK-TS and SDK-Swift; SDK-KMP is still outdated until the Kotlin refactor described below is complete.

Documentation improvements made significant headway thanks to the sustained collaboration with the technical writing audit team, and we expect to close the current iteration before the year's end. We also kicked off the OpenSSF Best Practices Badge and OpenSSF Scorecard Badge tasks; both efforts are on track for a Q1 delivery after we finish collecting evidence across the repositories.

---

## Current Plans

The strategic direction continues to align with the annual review while we incorporate the new initiatives raised by the community:

- **Platform simplification** – finish swapping `prism-node` out for `Neoprism`, complete the offline-first SDK rollout, and close the last two [Cardano VDR milestones](https://milestones.projectcatalyst.io/projects/1300189/milestones/4) before year's end.
- **Developer experience & documentation** – complete the first iteration of the documentation improvement plan, keep expanding tutorial coverage, and ensure issuance guidance stays in sync across SDK-TS, SDK-Swift, and the upcoming Kotlin rewrite.
- **SDK & client evolution** – adopt the Identus platform for React/React Native builders by downgrading Kotlin’s Apollo version for compatibility and converting SDK-KMP into a pure Kotlin codebase. We have already started implementing the Verifiable Credentials Data Model (VCDM) 2.0 payloads inside SDK-Swift, with mDoc and OpenBadges 3.0 support queued next.
- **Security & compliance** – continue executing on the OpenSSF Best Practices and Scorecard badges so that we can check both items off in Q1, and leverage their findings to tighten CI/CD and dependency hygiene.

Additional features under consideration remain unchanged versus Q3, but the VCDM 2.0 implementation work gives us an early foothold in that backlog.

---

## Maintainer Diversity

Maintainer organizations are unchanged from the previous quarter: Socious, CSign, Blocktrust, and Trust0 work alongside IOG to review and merge contributions. We continue to mentor additional reviewers so that the dependency on IOG can trend down over the next few quarters.

---

## Contributor Diversity

The contributor base remains anchored by IOG, with Blocktrust and Socious continuing to provide code and roadmap input. Per the LF Insights dashboard, we averaged 16 active contributors with high pull-request throughput, but 3 people still account for the majority of code, underscoring the need to keep onboarding new maintainers and to land the OpenSSF work that will make that onboarding easier.

---

## Additional Information

- The Identus platform work for React/React Native is underway; downgrading the Kotlin Apollo dependency and reworking SDK-KMP into a pure Kotlin module will unlock consistent developer ergonomics across Android, iOS, and React Native.
- Offline-first parity and the Cardano VDR deliverables are still targeted for completion this calendar year, after which we will shift to hardening issuance at scale.
