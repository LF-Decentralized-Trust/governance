[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Mid-Year Review of Hyperledger Iroha

This review covers progress since the 2026 annual review through August 13,
2026. Hyperledger Iroha remains an active Graduated project. The reporting
period included the Minamoto mainnet launch, live central-bank adoption,
continued Taira testnet hardening, and substantial work on consensus,
deterministic execution, SDKs, privacy, and operator tooling for Iroha 3.

## Project Health

Graduated status remains appropriate. The project delivered public-network
milestones, continued sustained engineering activity, expanded the maintainer
roster, and kept its public roadmap and implementation status current.

Core Hyperledger Iroha 3 capabilities are operational and in active use. Minamoto is live,
and the [Central Bank of Solomon Islands](https://bokolo.soramitsu.io/) is
advancing Bokolo Cash on a private SORA Nexus data space built with Hyperledger
Iroha. Together with three other central-bank projects, this brought the total
number of central banks using Iroha 3 / SORA Nexus during the first half of
2026 to four. Multiple companies are also building projects on the platform,
with releases planned for Q3 2026.

The project has moved from proving the architecture to expanding an operational
platform. Current roadmap work builds on capabilities that are already deployed
and focuses on further performance, resilience, operator experience,
integration coverage, and broadly consumable release packaging. Contribution
activity remains concentrated in one organization and is the clearest area for
community-health improvement.

## Progress Against 2026 Goals

### Platform direction: Hyperledger Iroha 3 is the current generation

The annual review included a goal of continuing the Iroha 2 GA path. The
project's direction has since consolidated around Iroha 3 as the current and
future Hyperledger Iroha platform. Iroha 2 is not in active use and will not be
promoted as part of the project's 2026 goals.

Engineering, documentation, SDK, operator, and adoption work is now centered on
Iroha 3 / SORA Nexus. This includes asset and query APIs, offline-wallet flows,
transaction-fee handling, ISO 20022 payment messages, privacy, and integration
surfaces for regulated-finance deployments.

### Taira hardening and Hyperledger Iroha 3 mainnet rollout: Strong progress

The [Taira public testnet](https://medium.com/sora-xor/sora-taira-testnet-be8cfc924b58),
announced on March 3, 2026, is the integration and pre-production hardening
environment for SORA Nexus. Since the annual review, the project has continued
to improve multi-validator deployment profiles, signed rollout canaries,
routing and topology checks, restart handling, telemetry, and operator
runbooks.

On April 26, 2026, SORA launched the
[Minamoto mainnet](https://sora-xor.medium.com/sora-nexus-minamoto-mainnet-launch-5ef2819a5deb),
powered by Hyperledger Iroha 3. Minamoto introduced a public, value-bearing
environment with a burn-backed XOR claim path, while Taira remains available
for testing and changes that need to fail safely. This achieved the annual
goal of beginning the Iroha 3 / SORA Nexus mainnet rollout. Routine hardening,
capacity growth, and operational-evidence collection continue as usage expands.

### Multilane and multidataspace architecture: Substantial progress

The implementation and specifications advanced lane-native routing, dynamic
lane lifecycle, dataspace manifests and policy boundaries, data-availability
commitments, per-lane evidence, and cross-dataspace atomic coordination. The
project also clarified the separation between logical lanes, physical
dataspaces, and namespace bindings in deployment profiles.

The core model is in use across Taira, Minamoto, and private data spaces. The
public [roadmap](https://github.com/hyperledger-iroha/iroha/blob/optimizations/roadmap.md)
tracks further topology refinements, multi-validator evidence, and release
closeout work as the network expands.

### Security, runtime validation, and end-to-end integration: Substantial progress

Work continued on Sumeragi v2 consensus and recovery, Kura durability, mandatory
data availability and reliable broadcast, canonical network identity, IVM ABI
and gas-policy enforcement, deterministic Norito wire formats, privacy proofs,
and cross-SDK conformance. The project also expanded fail-closed validation and
restart testing across consensus, Torii, wallets, and deployment tooling.

The current [implementation status](https://github.com/hyperledger-iroha/iroha/blob/optimizations/status.md)
records the extensive completed work as well as continuing validation. Current
priorities build on the functioning stack: completing the latest consensus
ownership and recovery integration, expanding deterministic multi-peer
validation, collecting security-release evidence, and regenerating release
artifacts from a clean source candidate.

### Community visibility and adoption: Strong progress; diversity remains a focus

Taira, Minamoto, public explorers, and the refreshed
[Iroha 3 documentation portal](https://docs.iroha.tech/) have made the current
platform more accessible to operators and builders. The documentation now
provides quickstarts, SDK entry points, architecture and reference material,
operator guidance, and multilingual navigation.

Adoption advanced materially. During the first half of 2026, four central
banks used Iroha 3 / SORA Nexus in their projects. The publicly named example
is the Central Bank of Solomon Islands: its 2026 Bokolo Cash pilot is led by
CBSI and built with SORAMITSU on SORA Nexus and Hyperledger Iroha.
[Three other central-bank projects](https://medium.com/sora-xor/sora-nexus-e32cfd1edef6)
also used the platform during the period. Multiple companies are building
additional Iroha 3 / SORA Nexus projects, with releases planned for Q3 2026.

To turn this adoption into a broader user and contributor community, the
project plans to devote more effort in the second half of 2026 to recurring
online workshops and in-person educational meetups. These sessions will
introduce the Iroha 3 / SORA Nexus architecture, teach developers and operators
how to use the platform and its SDKs, provide hands-on guidance for building
and running projects, and explain how newcomers can contribute code, tests,
documentation, examples, and reviews.

Maintainer diversity improved, but contribution activity became more
concentrated during the reporting window. The detailed figures are recorded
below.

## Deliverables and Outputs (Past Six Months)

| Deliverable | Outcome |
|---|---|
| Taira public-testnet hardening | Continued rollout validation, recovery, routing, telemetry, and operator hardening for the public Iroha 3 / SORA Nexus integration environment. |
| Minamoto mainnet | Public SORA Nexus mainnet deployment powered by Iroha 3, with a value-bearing XOR migration path and public Torii and explorer surfaces. |
| Central-bank adoption | Four central banks used Iroha 3 / SORA Nexus during the first half of 2026, including the publicly announced CBSI Bokolo Cash pilot. |
| Ecosystem builder pipeline | Multiple companies began building projects on Iroha 3 / SORA Nexus, with releases planned for Q3 2026. |
| Sumeragi and Kura hardening | Continued multilane consensus, finality, durable recovery, restart safety, queue ownership, and storage-ordering work, including mandatory Kura persistence before state commit, formal recovery models, four-peer Byzantine soak testing, and memory/backpressure guards. |
| Nexus lane and dataspace model | Dynamic routing and lifecycle work, dataspace policy and manifest handling, data-availability evidence, and cross-dataspace atomic-transaction support. |
| IVM, Kotodama, Musubi, and Norito | Further first-release ABI enforcement, deterministic execution and gas controls, contract/toolchain work, canonical serialization, and cross-platform artifact checks. |
| Privacy and regulated-finance flows | Advances in zero-knowledge and confidential-transfer paths, offline cash and wallet protocols, fee handling, ISO 20022 integration, and cross-chain settlement proofs. |
| SoraFS V1 | Delivered deterministic reputation scoring, canonical schemas, proofs, governance and orderbook flows, Torii and CLI surfaces, and JavaScript/Python SDK helpers; rollout work continues on production ingest and publishing. |
| SDK and mobile delivery | Continued Kotlin, Java, Swift, JavaScript, Python, Rust, and C# alignment with Iroha 3, mobile/offline-wallet interoperability work, and reproducible native-artifact workflows. |
| Documentation and operations | A refreshed, multilingual Iroha 3 portal with Taira and Minamoto examples, plus expanded deployment checks, runbooks, and release-provenance tooling. |

## Goals for the Second Half of 2026

- Build on the operational Iroha 3 foundation by completing the latest
  Sumeragi v2 integration and release-closeout work, expanding crash/restart
  and deterministic four-validator validation, and regenerating ABI,
  wire-format, OpenAPI, and release-provenance artifacts from a clean source
  candidate.
- Continue operating Taira as the pre-production proving ground and expand
  Minamoto operations with signed canaries, multi-validator topology evidence,
  recovery rehearsals, observability, and operator documentation.
- Establish Iroha 3 as the sole current product line across releases, SDKs,
  documentation, examples, operator guidance, and adopter onboarding.
- Close the remaining lane/dataspace topology work and validate routing,
  data-availability, privacy, and cross-dataspace atomic flows end to end.
- Improve developer experience through stable SDK packages, cross-SDK fixture
  tests, reproducible mobile artifacts, examples, and a more predictable public
  release-note cadence.
- Support the planned Q3 launches from companies building on Iroha 3 / SORA
  Nexus and turn those launches into reusable examples for future adopters.
- Recruit and mentor contributors from additional organizations, grow repeat
  reviewers into maintainers, and publish a current `ADOPTERS.md` containing
  only adopters that have approved public attribution.
- Establish a regular programme of online workshops and in-person educational
  meetups that teaches developers and operators how to use Iroha 3 / SORA
  Nexus, build and run projects, and contribute code, tests, documentation,
  examples, and reviews.

## Help Required

There are no immediate blockers requiring TAC intervention. The project would
benefit from LF Decentralized Trust support in the following areas:

- introductions to independent contributors, reviewers, academic groups, and
  organizations interested in deterministic ledger, CBDC, privacy, or
  interoperability work;
- greater visibility for Taira, Minamoto, and Iroha's regulated-finance use
  cases, plus help promoting online workshops and connecting in-person meetups
  with relevant LFDT communities and events; and
- guidance and connections for independent security review, release-readiness
  assessment, and contributor mentorship.

## Maintainer and Contributor Diversity

The [2026 annual review](https://lf-decentralized-trust.github.io/governance/project-updates/2026/2026-annual-Hyperledger-Iroha/)
reported 19 maintainers, 18 of whom used Soramitsu email addresses. The current
[maintainer roster](https://github.com/hyperledger-iroha/iroha/blob/main/MAINTAINERS.md)
lists 21 maintainers: 18 with Soramitsu addresses and 3 without them. The
entries for Emiliano and Nikita landed on the main-branch
roster during this reporting period, so the number of non-Soramitsu maintainers
increased from one to three.

[LFX Insights for the 180 days ending August 13, 2026](https://insights.linuxfoundation.org/project/iroha/contributors?timeRange=past180days&start=2026-02-14&end=2026-08-13)
reports:

- 10 active contributors, compared with 15 in the preceding period;
- 3 active organizations, compared with 5 in the preceding period;
- 74% of recorded contribution activity coming from the top two contributors;
  and
- 98% of recorded contribution activity attributed to Soramitsu (partly explainable by the large commitment Soramitsu made in the first half to support the CBDC projects).

The maintainer-roster change is positive, but the activity figures show that
organizational and contributor concentration remains the project's clearest
community-health risk. Reducing that dependency is a priority for the second
half of 2026, and we hope community outreach efforts will be successful in increasing the number of contributors.

## Useful Links

- [Hyperledger Iroha repository](https://github.com/hyperledger-iroha/iroha)
- [Public roadmap](https://github.com/hyperledger-iroha/iroha/blob/optimizations/roadmap.md)
- [Implementation status](https://github.com/hyperledger-iroha/iroha/blob/optimizations/status.md)
- [Documentation portal](https://docs.iroha.tech/)
- [Releases](https://github.com/hyperledger-iroha/iroha/releases)
- [Bokolo Cash](https://bokolo.soramitsu.io/)
- [Taira explorer](https://taira-explorer.sora.org/)
- [Minamoto explorer](https://minamoto-explorer.sora.org/)
- [LFDT mailing list](https://lists.lfdecentralizedtrust.org/g/iroha)
- [Telegram community chat](https://t.me/hyperledgeriroha)
- [Discord](https://discord.com/channels/905194001349627914/905205848547155968)
