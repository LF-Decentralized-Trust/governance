---
layout: default
title: 2026 Mid-Year Review Hyperledger Fabric and Fabric-X
parent: 2026
grand_parent: Project Updates
---

[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Mid-Year Review of Hyperledger Fabric and Fabric-X

This review covers **1 January 2026 through 30 June 2026** and follows the [2026 annual review](2026-annual-Hyperledger-Fabric.md). It reports on both sub-projects of the Fabric umbrella: **Hyperledger Fabric** (referred to below as Fabric, the original architecture) and **Hyperledger Fabric-X** (the high-performance re-architecture).

## Scope and methodology

This report treats seven repositories as the Fabric-X technical scope: [fabric-x](https://github.com/hyperledger/fabric-x), [fabric-x-orderer](https://github.com/hyperledger/fabric-x-orderer), [fabric-x-committer](https://github.com/hyperledger/fabric-x-committer), [fabric-x-common](https://github.com/hyperledger/fabric-x-common), [fabric-x-endorser](https://github.com/hyperledger/fabric-x-endorser), plus [fabric-x-evm](https://github.com/hyperledger/fabric-x-evm) and [fabric-x-sdk](https://github.com/hyperledger/fabric-x-sdk), both created in March 2026 and therefore new since the annual review. The Fabric [GOVERNANCE.md](https://github.com/hyperledger/fabric/blob/main/GOVERNANCE.md) still lists only the five pre-existing repositories as sources of Fabric-X TSC voting members; the governance status of EVM and SDK maintainers therefore needs clarification.

The Fabric-X ecosystem also includes three closely-coupled repositories outside the `hyperledger` org, so this report covers them too: the [Ansible collection](https://github.com/LF-Decentralized-Trust-labs/fabric-x-ansible-collection) and [block explorer](https://github.com/LF-Decentralized-Trust-labs/fabric-x-block-explorer) in LF Decentralized Trust Labs, and [Fabric Smart Client](https://github.com/hyperledger-labs/fabric-smart-client) in Hyperledger Labs, which provides the programming model used in place of chaincode in Fabric-X. They are reported in a separate table and excluded from the seven-repository totals. `fabric-x-samples` and `fabric-x-rfcs` hold samples and design documents rather than product code and are cited as evidence but not measured.

Methodology, briefly: commit and contributor counts are `git log` on each repository's default branch, bounded to the window, with bot authors excluded and contributors counted by author display name (Fabric-X also gives a deduplicated figure). Fabric's `release-2.5` commits are counted separately, but its contributor counts are `main`-only; H1 2025 comparison figures were recomputed the same way. Merged pull request counts are GitHub search by merge date and are branch-agnostic; since both projects squash-merge, PR and commit counts measure related but not identical events. Issue counts are issues *opened in* and issues *closed during* the window — two independent sets, not a completion ratio. Tag dates use annotated tagger dates where available and target-commit dates for lightweight tags; counts include prereleases, exclude documentation and tooling tags, and are not the same as published GitHub Releases. Fabric-X totals are not comparable to the 2025 annual figures because scope grew. Employer affiliation cannot be derived from commit metadata; where the report refers to affiliation, it attributes the characterization to the annual review or notes that public maintainer files are insufficient to verify it.

## Project Health

### Hyperledger Fabric

Fabric remains mature and stable, with the v2.5.x long-term support line and the v3.1.x line both under active maintenance. The half-year was deliberately a maintenance and hardening period: no new architectural features landed. Work concentrated on crash and race-condition fixes (gossip, private data storage, Byzantine fault tolerant (BFT) block delivery, SmartBFT consensus, orderer stream teardown), Docker Engine v29 compatibility, and continuous Go toolchain and dependency upgrades. Two coordinated release trains shipped, in February and June, each covering both supported lines.

Throughput of contributions is healthy: 90 pull requests merged, 12 issues opened and 6 closed in the window. Median time from pull request creation to merge was 29 hours (90th percentile 329 hours). Fabric documentation directs support questions to Discord and Stack Overflow; response latency was not measured for this report.

Two health concerns need naming honestly:

1. **Contribution volume declined.** Non-bot commits on `main` fell from 79 in H1 2025 to 64 in H1 2026, and distinct non-bot authors fell from 32 to 23 over the same comparison. The project lists nine core maintainers, but the trend is downward, not flat; the separate LFDT maintaining-organization test is addressed below, where Fabric does have maintainers from more than one organization.
2. **Maintainer roster is static and load is heavily concentrated.** No maintainer was added or retired in the half-year. One contributor authored 32 commits under one identity and 35 of the 64 non-bot commits on `main` (55%) after their two Git identities are merged; the same contributor submitted 54 of the 90 merged pull requests.

The open-issue backlog stood at 182 at the time of writing. Maintainers characterize much of it as aged enhancement work, but the project has not yet run a triage pass that would substantiate its composition.

### Hyperledger Fabric-X

Fabric-X reached its most significant milestone since being contributed to Hyperledger: the umbrella, the orderer, and the committer all cut **v1.0.0** in May 2026. Other supporting repositories remained on `v0.x` or untagged during H1. The project also grew in scope by adding an Ethereum Virtual Machine (EVM) compatibility layer and a client SDK. It merged and configured a unified MkDocs documentation site, established an end-to-end integration test spanning the orderer and the committer, and delivered Kubernetes and OpenShift deployment automation through the Ansible collection.

Activity is high — 744 non-bot commits and 739 merged pull requests across the seven repositories in scope, plus a further 369 non-bot commits in the three coupled labs repositories — and review turnaround is fast: median time to merge ranges from 19 hours (`fabric-x-common`) to 43 hours (`fabric-x-orderer`), with 90th percentiles between 99 and 317 hours.

Issue activity in the window, by repository:

| Repository | Issues opened | Issues closed | Median time to merge (h) |
|---|---:|---:|---:|
| fabric-x | 83 | 48 | 20 |
| fabric-x-orderer | 120 | 108 | 43 |
| fabric-x-committer | 207 | 201 | 26 |
| fabric-x-common | 30 | 22 | 19 |
| fabric-x-evm | 101 | 18 | 24 |
| fabric-x-sdk | 3 | 2 | 22 |
| fabric-x-endorser | 0 | 0 | — |
| fabric-x-ansible-collection (labs) | 56 | 52 | — |
| fabric-smart-client (labs) | 198 | 203 | — |
| fabric-x-block-explorer (labs) | 2 | 0 | — |

As noted in the methodology, opened and closed counts are independent sets and should not be read as a completion ratio. Two figures deserve attention: `fabric-x-evm`, where 101 issues were opened against 18 closed — expected for a repository in its first quarter, but it needs a triage pass — and `fabric-x`, where the umbrella repository accumulates cross-cutting issues faster than they are closed. Elsewhere, closure roughly keeps pace with opening. Support and design discussion happens on the monthly Fabric/Fabric-X community call and in GitHub issues rather than on a dedicated Discord channel.

One health concern stands out: **maintainer concentration.** The orderer and the committer carry most of the commit volume but list only two maintainers each. Organizational concentration is sharper still: every current Fabric-X maintainer is from IBM, so the sub-project does not today meet the LFDT Incubation expectation of at least two maintaining organizations. Notably, the wider ecosystem has broader contributor participation — Fabric Smart Client had 16 distinct contributors in the window against 4 on the committer — which suggests a pool the core repositories have not yet drawn on.

## Questions for the TAC

1. **Adoption and roadmap gaps.** Neither sub-project maintains an `ADOPTERS.md`, despite the lifecycle guidance that one should be present, and neither publishes a consolidated, prioritized roadmap. Both gaps are explained below; publishing roadmaps is an H2 goal. We ask the TAC to confirm required remediation and timing.

## Progress Against 2026 Goals

### Hyperledger Fabric

Goals are those recorded in the [2026 annual review](2026-annual-Hyperledger-Fabric.md).

| 2026 goal | Mid-year status | Evidence |
|---|---|---|
| Maintenance releases at least quarterly for v2.5.x and v3.x | **Met** | v2.5.15 and v3.1.4 (23 Feb 2026); v2.5.16 and v3.1.5 (18 Jun 2026) |
| Continue improving OpenSSF Scorecard for priority repositories | **Not measurable** | Vulnerability-check remediation ([#5486](https://github.com/hyperledger/fabric/pull/5486)), archived-dependency replacement ([#5476](https://github.com/hyperledger/fabric/pull/5476), [#5480](https://github.com/hyperledger/fabric/pull/5480)), and sustained dependency bumps all landed, but the project published no before/after Scorecard numbers for the period, so progress cannot be asserted |
| Encourage contributions from the community | **Missed — activity declined** | Distinct non-bot authors on `main` fell from 32 (H1 2025) to 23 (H1 2026); non-bot commits fell from 79 to 64. External contributors still landed substantive gossip, private-data, ledger, and BFT fixes (see the [v3.1.5 release notes](https://github.com/hyperledger/fabric/releases/tag/v3.1.5)) |
| Continue to increase diversity of maintainers | **Missed** | Active maintainer roster unchanged at 9 in [MAINTAINERS.md](https://github.com/hyperledger/fabric/blob/main/MAINTAINERS.md); no additions or retirements |
| Explore integration points with the Fabric-X architecture | **Partial, and driven from the Fabric-X side** | No integration RFC or code change in `hyperledger/fabric`. Progress came instead from Fabric-X: `fabric-x-evm` and `fabric-x-sdk` both target Fabric 3 as well as Fabric-X |

### Hyperledger Fabric-X

| 2026 goal | Mid-year status | Evidence |
|---|---|---|
| Release sample token application on top of Fabric-X | **Met** | Samples moved to [fabric-x-samples](https://github.com/hyperledger/fabric-x-samples) ([fabric-x#208](https://github.com/hyperledger/fabric-x/pull/208)); item checked off in the umbrella README |
| Develop a Fabric-X Kubernetes Operator | **Partial — deployment automation delivered, operator not built** | The Ansible collection delivered substantial Kubernetes support in H1: Fabric CA, orderer, and committer deployments on Kubernetes ([#203](https://github.com/LF-Decentralized-Trust-labs/fabric-x-ansible-collection/pull/203), [#205](https://github.com/LF-Decentralized-Trust-labs/fabric-x-ansible-collection/pull/205)), OpenShift support ([#273](https://github.com/LF-Decentralized-Trust-labs/fabric-x-ansible-collection/pull/273)), configurable resource requests and limits ([#303](https://github.com/LF-Decentralized-Trust-labs/fabric-x-ansible-collection/pull/303)), NodePort and LoadBalancer services ([#296](https://github.com/LF-Decentralized-Trust-labs/fabric-x-ansible-collection/pull/296)), and an observability stack on Kubernetes — Prometheus and Grafana ([#215](https://github.com/LF-Decentralized-Trust-labs/fabric-x-ansible-collection/pull/215)), Jaeger ([#208](https://github.com/LF-Decentralized-Trust-labs/fabric-x-ansible-collection/pull/208)), Elasticsearch ([#206](https://github.com/LF-Decentralized-Trust-labs/fabric-x-ansible-collection/pull/206)), node and Postgres exporters. 59 releases shipped. A Kubernetes *operator* — a controller reconciling custom resources — was not built and remains unchecked in the umbrella README. Given how much operational ground Ansible now covers, the sub-project should decide in H2 whether a distinct operator is still the right goal |
| Expand contributor base beyond the initial development team | **Partial — directional improvement** | 35 distinct non-bot author names (33 after merging the two duplicate identities) across the seven repositories, versus 14 contributors reported for 2025. The scope and counting method differ, so these figures show broader participation but do not establish a like-for-like increase |
| Improve documentation and getting-started guides | **Met** | Unified MkDocs site configuration ([fabric-x#267](https://github.com/hyperledger/fabric-x/pull/267)); committer operational guide ([#498](https://github.com/hyperledger/fabric-x-committer/pull/498)), coordinator architecture walkthrough ([#583](https://github.com/hyperledger/fabric-x-committer/pull/583)), CLI reference ([#575](https://github.com/hyperledger/fabric-x-committer/pull/575)); Arma architecture doc ([fabric-x-orderer#876](https://github.com/hyperledger/fabric-x-orderer/pull/876)); `configtx` documentation in fabric-x-common ([#114](https://github.com/hyperledger/fabric-x-common/pull/114)) |
| Explore tighter integration with Hyperledger Fabric mainline | **Partial** | `fabric-x-evm` and `fabric-x-sdk` both support Fabric 3 and Fabric-X; no changes merged into `hyperledger/fabric` itself |
| Establish a formal mentorship program for new contributors | **Not started** | No program artifact found in any Fabric-X repository |

## Deliverables and Outputs (January–June 2026)

### Hyperledger Fabric

Four releases, two per supported line:

| Release | Date | Content |
|---|---|---|
| [v2.5.15](https://github.com/hyperledger/fabric/releases/tag/v2.5.15) | 2026-02-23 | LTS maintenance: Docker Engine v29 compatibility (replaced `go-dockerclient` with the native Moby client, [#5355](https://github.com/hyperledger/fabric/pull/5355)), `CORE_PEER_DELIVERYCLIENT_ADDRESSOVERRIDES` parsing fix ([#5400](https://github.com/hyperledger/fabric/pull/5400)), dependency updates |
| [v3.1.4](https://github.com/hyperledger/fabric/releases/tag/v3.1.4) | 2026-02-23 | Docker Engine v29 compatibility (replaced `go-dockerclient` with the native Moby client), gossip membership-tracker and shutdown fixes, `CORE_PEER_DELIVERYCLIENT_ADDRESSOVERRIDES` parsing fix |
| [v2.5.16](https://github.com/hyperledger/fabric/releases/tag/v2.5.16) | 2026-06-18 | LTS maintenance: panic recovery in chaincode transaction handling ([#5473](https://github.com/hyperledger/fabric/pull/5473)), restored configurable chaincode base-image pull behaviour ([#5498](https://github.com/hyperledger/fabric/pull/5498)), Go-version-independent chaincode builds ([#5492](https://github.com/hyperledger/fabric/pull/5492)), dependency updates |
| [v3.1.5](https://github.com/hyperledger/fabric/releases/tag/v3.1.5) | 2026-06-18 | Peer startup optimization (skip full chaincode package reads), private-data iterator and lock fixes, orderer stream abort fix, BFT deliverer data-race fix, SmartBFT error-reporting fix, panic recovery in transaction handling, Go-version-independent chaincode builds |

Note that the private-data, ledger, gossip, and BFT fixes listed for v3.1.x were not backported to the v2.5.x LTS line in this window; no gossip, private-data, or ledger change landed on `release-2.5`.

Other outputs:

- **Reliability hardening across the peer:** a time-of-check-to-time-of-use race in gossip discovery ([#5379](https://github.com/hyperledger/fabric/pull/5379)), state-provider shutdown panic ([#5378](https://github.com/hyperledger/fabric/pull/5378)), private-data storage iterator and purge-lock ordering ([#5424](https://github.com/hyperledger/fabric/pull/5424), [#5430](https://github.com/hyperledger/fabric/pull/5430)), ledger snapshot reader leaks ([#5431](https://github.com/hyperledger/fabric/pull/5431)).
- **Performance:** peer startup no longer reads full chaincode packages ([#5418](https://github.com/hyperledger/fabric/pull/5418)).
- **Toolchain and supply chain:** Go moved from 1.25.5 to 1.26.4 over the period; SmartBFT to v1.0.1, gRPC to 1.79.3, etcd to v3.6.10, Moby to 1.54.2, plus `x/net`, OpenTelemetry, and `fabric-lib-go` updates; two archived dependencies replaced; broken-link checking extended to the release-2.5 docs.
- **Activity:** 69 commits on `main` (64 non-bot) plus 21 on `release-2.5`; 90 merged pull requests.

### Hyperledger Fabric-X

Repository activity in the window:

| Repository | Commits (non-bot) | Distinct non-bot authors | Merged PRs | Version tags¹ | Role |
|---|---:|---:|---:|---:|---|
| [fabric-x](https://github.com/hyperledger/fabric-x) | 55 | 19 | 57 | 12 | Umbrella docs, `fxconfig` CLI, compatibility matrix; reached v1.0.0 |
| [fabric-x-orderer](https://github.com/hyperledger/fabric-x-orderer) | 318 | 11 | 319 | 11 | Arma, the sharded Byzantine fault tolerant ordering service; reached v1.0.0 |
| [fabric-x-committer](https://github.com/hyperledger/fabric-x-committer) | 206 | 4 | 210 | 11 | Post-ordering transaction validation and commit pipeline; tags through v1.0.3 |
| [fabric-x-common](https://github.com/hyperledger/fabric-x-common) | 46 | 8 | 47 | 8 | Shared CLIs, protobufs, and code used by orderer and committer |
| [fabric-x-evm](https://github.com/hyperledger/fabric-x-evm) | 90 | 10 | 79 | 2 | New in March 2026; EVM and Ethereum JSON-RPC over Fabric-X and Fabric |
| [fabric-x-sdk](https://github.com/hyperledger/fabric-x-sdk) | 29 | 4 | 27 | 0 | New in March 2026; preview client SDK for Fabric-X and Fabric 3 |
| [fabric-x-endorser](https://github.com/hyperledger/fabric-x-endorser) | 0 | 0 | 0 | 0 | Sample endorser built on Fabric Smart Client; no changes recorded in the window |
| **Total** | **744** | **35 names (33 deduplicated)** | **739** | — | |

¹ Version tags exclude documentation and tooling tags such as `fabric-x-docs-local` and `list`, which are not releases. Dates use annotated tagger dates where available and target-commit dates for lightweight tags. Only `fabric-x` and `fabric-x-orderer` published GitHub Release entries in the window; the committer, common, and EVM repositories are tag-only, so any single "number of releases" figure for Fabric-X depends on which definition is used. Making this consistent is an H2 goal.

Per-repository author counts sum to 56 because contributors work across repositories; the deduplicated figure of 33 merges the two duplicate identities `Arne`/`Arne Rutjes` and `Storm`/`Storm1289`.

Three closely-coupled repositories outside the `hyperledger` org carry substantial Fabric-X work and are reported separately:

| Repository | Commits (non-bot) | Distinct non-bot authors | Merged PRs | Releases | Role |
|---|---:|---:|---:|---:|---|
| [fabric-x-ansible-collection](https://github.com/LF-Decentralized-Trust-labs/fabric-x-ansible-collection) (LFDT Labs) | 149 | 4 | 153 | 59 | Deployment automation for local, Kubernetes, OpenShift, and multi-node networks |
| [fabric-smart-client](https://github.com/hyperledger-labs/fabric-smart-client) (Hyperledger Labs) | 189 | 16 | 187 | 10 | Programming model and peer-to-peer transaction negotiation that replaces chaincode in Fabric-X |
| [fabric-x-block-explorer](https://github.com/LF-Decentralized-Trust-labs/fabric-x-block-explorer) (LFDT Labs) | 31 | 4 | 15 | 0 | Block explorer ingesting from the committer sidecar into PostgreSQL, with a REST API and web UI |

These matter for two reasons. The Ansible collection is where much of the Fabric-X deployment automation ships — 59 releases in six months, from `0.5.0` to `0.8.2`. Fabric Smart Client is the most contributor-diverse repository in the wider Fabric-X ecosystem, with 16 distinct authors against 4 on the committer. Its Fabric-X platform driver remained explicitly experimental and unsuitable for production during H1, however. Because both repositories live in labs rather than under the Fabric-X sub-project, their activity and contributor diversity are invisible in the seven-repository totals above.

Key deliverables:

- **v1.0.0 for the umbrella, orderer, and committer (May 2026).** These three repositories cut v1.0.0, with the committer continuing to v1.0.3 by mid-June, alongside a published version compatibility matrix pinning orderer, committer, Ansible collection, Fabric CA, and Fabric Smart Client versions. Other supporting repositories remained on `v0.x` or untagged during H1.
- **Orderer (Arma):** Arma is the sharded BFT consensus protocol underlying the ordering service. It separates payload dissemination from consensus: consenters order batch-attestation metadata, while assemblers retrieve full batches and build blocks. Work in the window: dynamic reconfiguration with configuration sequence numbers and acknowledgements; consensus state serialization migrated from ASN.1 to protobuf ([#864](https://github.com/hyperledger/fabric-x-orderer/pull/864)); configurable cryptographic service provider (BCCSP) for local membership service providers and config blocks; certificate-authority consistency validation in orderer config ([#909](https://github.com/hyperledger/fabric-x-orderer/pull/909)); operations endpoints including a Prometheus `/metrics` endpoint ([#870](https://github.com/hyperledger/fabric-x-orderer/pull/870)) and health checking ([#928](https://github.com/hyperledger/fabric-x-orderer/pull/928)); the `configtxlator` and `protolator` configuration-translation tools imported from fabric-x-common; removal of the `fabric/msp` dependency ([#967](https://github.com/hyperledger/fabric-x-orderer/pull/967)); crash-handling fixes in the Armageddon network configuration tool; and a documented Arma architecture guide.
- **Committer:** transaction-metadata support end to end ([#627](https://github.com/hyperledger/fabric-x-committer/pull/627), [#628](https://github.com/hyperledger/fabric-x-committer/pull/628)); a `StreamAllTransactions` notification stream ([#620](https://github.com/hyperledger/fabric-x-committer/pull/620)); dynamic TLS certificate-authority rotation for the sidecar — the component that ingests blocks from the ordering service — and the query service ([#530](https://github.com/hyperledger/fabric-x-committer/pull/530)); Arma BFT block-verifier detection in the sidecar ([#597](https://github.com/hyperledger/fabric-x-committer/pull/597)); Prometheus metric fixes; YugabyteDB driver testing; and a full documentation site with operational and architecture guides.
- **Common:** notification service API extended with `StreamAllTransactions` ([#117](https://github.com/hyperledger/fabric-x-common/pull/117)) and transaction metadata ([#120](https://github.com/hyperledger/fabric-x-common/pull/120)); block signature and validation-policy encoding fixes for Arma ([#107](https://github.com/hyperledger/fabric-x-common/pull/107), [#108](https://github.com/hyperledger/fabric-x-common/pull/108)); a length-delimited block data hash fix ([#97](https://github.com/hyperledger/fabric-x-common/pull/97)); and removal of a GPL-flagged build dependency ([#98](https://github.com/hyperledger/fabric-x-common/pull/98)).
- **EVM (new):** a native EVM plus Ethereum JSON-RPC endpoint (chain ID `4011`) usable against both Fabric-X and Fabric, enabling unmodified Solidity contracts and standard Ethereum tooling subject to [documented compatibility gaps](https://github.com/hyperledger/fabric-x-evm/blob/main/docs/COMPATIBILITY.md); expanded OpenZeppelin Hardhat-suite coverage ([#167](https://github.com/hyperledger/fabric-x-evm/pull/167)) with Hardhat tests in CI ([#160](https://github.com/hyperledger/fabric-x-evm/pull/160)); Cancun and Osaka fork support; Ethereum-compatible JSON-RPC error codes; notification-based transaction completion ([#190](https://github.com/hyperledger/fabric-x-evm/pull/190)); performance-testing infrastructure and multi-namespace performance runs; block-explorer and demo compose files.
- **SDK (new):** modular client, identity, network, and block-processing packages for Fabric-X and Fabric 3; notification service v2 support ([#28](https://github.com/hyperledger/fabric-x-sdk/pull/28)) and an all-transactions notifier ([#30](https://github.com/hyperledger/fabric-x-sdk/pull/30)); Go package documentation. The SDK is explicitly labelled a preview with unstable APIs and is not yet suitable for production.
- **Deployment and operations (Ansible collection, LFDT Labs):** 59 releases from `0.5.0` to `0.8.2`. Kubernetes support extended to Fabric CA, orderer, and committer with liveness and readiness probes, plus OpenShift support, configurable resource requests and limits, optional NodePort and new LoadBalancer services, image pull secrets, and an optional `k8s_namespace`. Observability on Kubernetes now covers Prometheus and Grafana, Jaeger tracing, Elasticsearch, and node and Postgres exporters, with an updated committer Grafana dashboard and query-service metrics. Default Postgres moved to 17.9.
- **Programming model (Fabric Smart Client, Hyperledger Labs):** 10 top-level releases from `v0.8.0` to `v0.13.0`. The [Fabric-X platform driver](https://github.com/hyperledger-labs/fabric-smart-client/blob/main/docs/platform/fabric-x/README.md) remained explicitly experimental and unsuitable for production during H1. Fabric-X integration tracked the committer through v1.0.0 ([#1472](https://github.com/hyperledger-labs/fabric-smart-client/pull/1472)), added mTLS for the committer gRPC client ([#1222](https://github.com/hyperledger-labs/fabric-smart-client/pull/1222)) and TLS for the committer container ([#1298](https://github.com/hyperledger-labs/fabric-smart-client/pull/1298)), added Fabric-X support to `fsccli` ([#1371](https://github.com/hyperledger-labs/fabric-smart-client/pull/1371)), supported multi-endorser transactions ([#1190](https://github.com/hyperledger-labs/fabric-smart-client/pull/1190)), and expanded membership-service and transaction unit tests.
- **Block explorer (LFDT Labs):** a Go service that ingests blocks from the committer sidecar over gRPC into PostgreSQL, exposing a REST API for blocks, transactions, and namespace policies, with a Next.js UI. It had 31 commits and 15 merged pull requests but no tag or GitHub Release as of 30 June 2026; `v0.1.0` was tagged on 20 July 2026.
- **Integration and ecosystem:** an end-to-end orderer-plus-committer integration test ([fabric-x#85](https://github.com/hyperledger/fabric-x/pull/85)); membership-service-provider-based namespace policies in `fxconfig`, the Fabric-X network configuration CLI ([#59](https://github.com/hyperledger/fabric-x/pull/59)); sample applications moved to `fabric-x-samples`.
- **Community:** monthly Fabric/Fabric-X community calls moved to the third Wednesday of the month ([fabric-x#42](https://github.com/hyperledger/fabric-x/pull/42)). The 2025 workshop series (architecture, programming model, Fabric-Token-SDK, orderer, committer) remains published and linked from the umbrella README.

**Performance note.** The orderer's published multi-region benchmark (four AWS regions, `c5a.8xlarge` instances, 300-byte transactions, latency around 0.8 seconds) was run on 20 January 2026, i.e. before most of the work described above. The 200,000+ TPS figure cited in the annual review derives from the [Fabric-X whitepaper](https://eprint.iacr.org/2023/1717.pdf) and has not been re-measured against v1.0.0. Publishing a v1.0.0-based benchmark with a documented methodology is an H2 goal.

## Adoption

**Hyperledger Fabric.** The annual review reports commercial offerings, consulting services, and continued enrolment in the Hyperledger Fabric Certified Practitioner exam and associated course, but this report has no new H1 adoption metric. The project does not maintain an `ADOPTERS.md`; maintainers have characterized such a file as difficult to keep accurate and as risking misrepresentation or apparent vendor preference. Because LFDT lifecycle guidance says an `ADOPTERS.md` should document verifiable real-world usage, the missing file remains a governance gap for TAC review.

**Hyperledger Fabric-X.** The sub-project does not maintain an `ADOPTERS.md`, and we have no publicly documented production deployment to report. H1 lowered the barrier to evaluation through v1.0.0 releases, a published compatibility matrix, Kubernetes and OpenShift deployment automation with observability features, a block explorer, a samples repository, and the EVM layer. These capabilities do not by themselves establish production readiness: the Fabric Smart Client Fabric-X driver remained explicitly experimental and unsuitable for production. Securing and documenting at least one external pilot remains the sub-project's most important H2 objective and a key input to any future graduation discussion.

## Roadmap

Both sub-projects expose public planning signals, but neither publishes the consolidated, prioritized, and current roadmap requested by the mid-year review guidance:

- **Fabric** documents proposed and accepted designs in the [fabric-rfcs](https://github.com/hyperledger/fabric-rfcs) repository and completed release content in `release_notes/` and GitHub releases. The RFC process explicitly states that acceptance does not assign implementation priority or a developer, so RFCs are not a roadmap by themselves.
- **Fabric-X** uses [fabric-x-rfcs](https://github.com/hyperledger/fabric-x-rfcs) and an undated "Coming soon" checklist in the [umbrella README](https://github.com/hyperledger/fabric-x). Its version compatibility matrix records compatible released versions rather than future plans. Deployment capability is recorded in the [Ansible collection](https://github.com/LF-Decentralized-Trust-labs/fabric-x-ansible-collection) releases and inventory examples.

Publishing an explicit, dated roadmap per sub-project is an H2 goal for both.

## Goals for the Second Half of 2026

Goals are listed with the role that owns them. Where a goal is a TSC decision rather than a delivery item, it is marked *(decision)*. Unless noted, the target is end of 2026.

### Hyperledger Fabric

1. **Release cadence** (release managers): keep quarterly maintenance releases for v2.5.x and v3.x.
2. **OpenSSF Scorecard** (maintainers, with a security/CI reviewer): publish before/after Scorecard numbers for `fabric`, `fabric-ca`, `fabric-chaincode-go`, and `fabric-gateway`, rather than reporting dependency-update activity as a proxy.
3. **Reverse the contribution decline** (maintainers): grow distinct non-bot authors above the H1 figure of 23, and convert at least one repeat external contributor into a reviewer or maintainer candidate. This directly addresses both the volume decline and the static roster.
4. **Reduce single-person dependency** (maintainers): distribute release and review load so no individual accounts for a majority of merged pull requests.
5. **Issue backlog triage** (maintainers): run a triage pass over the open-issue backlog so the remaining count is a meaningful health signal.
6. **Continued hardening** (maintainers): panic, race, and resource-lifecycle work in gossip, private data, ledger, and BFT paths.
7. **Fabric/Fabric-X convergence** *(decision)* (Fabric and Fabric-X maintainers jointly): produce a concrete artifact — an RFC, a prototype, or a documented decision not to pursue a given integration point.
8. **Roadmap** (maintainers): publish a consolidated, dated roadmap.

### Hyperledger Fabric-X

1. **Decide the Kubernetes operator question** *(decision)* (Fabric-X TSC, with Ansible collection maintainers): the Ansible collection now covers Kubernetes, OpenShift, resource management, and observability. Decide whether a distinct operator still adds enough value to build, and either commit to it with upgrade, backup, and failure-recovery paths, or record the decision to keep Ansible as the supported deployment path and drop the operator from the roadmap.
2. **Release process consistency** (per-repository maintainers, coordinated by the committer maintainers): publish GitHub Releases with release notes for committer, common, EVM, and SDK, and exclude documentation/tooling tags from release-facing metrics.
3. **SDK stabilisation** (EVM/SDK maintainers): stabilise the API surface, begin versioning and tagging, and document production-readiness criteria.
4. **EVM transparency** (EVM/SDK maintainers): publish the compatibility matrix, benchmark methodology and results, and security model.
5. **Re-measure performance** (orderer and committer maintainers): publish a v1.0.0-based benchmark with documented methodology, replacing the January 2026 and whitepaper figures.
6. **First public pilot** (umbrella maintainers): run at least one production-like deployment with an organization outside the core development team and publish the resulting operator feedback.
7. **Cross-repository compatibility testing** (umbrella maintainers): extend the existing end-to-end test into a matrix that pins exact orderer, committer, common, SDK, and EVM versions.
8. **Maintainer growth and mentorship** (orderer and committer maintainers): add maintainers to the orderer and committer beyond two each, including at least one maintainer from an organization other than IBM so the Incubation two-organization expectation is met, formalise onboarding and a maintainer-promotion path, and establish a named mentorship program or documented equivalent. Maintainer growth alone would not complete the mentorship-program goal that did not start in H1.
9. **Broaden the contributor base beyond the core repositories** (umbrella maintainers): Fabric Smart Client shows what a more diverse Fabric-X contributor pool looks like (16 authors versus 4 on the committer). Identify which of those contributors can be drawn into the orderer, committer, and common repositories.
10. **Roadmap** *(decision)* (Fabric-X TSC): publish a consolidated, dated roadmap replacing the README checklist, covering the labs repositories the deployment story depends on.
11. **Publish block-explorer release notes** (block explorer maintainers): the explorer had no tagged release at the H1 cutoff, but `v0.1.0` was tagged on 20 July 2026. Publish a corresponding GitHub Release with release notes so adopters can identify and pin the supported artifact.

## Help Required

**Hyperledger Fabric:**

- LFDT help identifying and mentoring contributors who could become reviewers and maintainers. This is now more urgent than at the annual review, since contribution volume declined in H1.
- A security or CI reviewer who can help the project measure and report OpenSSF Scorecard progress properly.

**Hyperledger Fabric-X:**

- Contributors with high-performance distributed systems experience, especially for the orderer and committer, where maintainer counts are at two each. Contributors from organizations other than IBM are the priority, since every current Fabric-X maintainer is from IBM.
- Organizations willing to pilot Fabric-X for central bank digital currency, tokenization, or high-throughput settlement use cases and share deployment feedback. Introductions here are the single most valuable thing the TAC and LFDT staff can offer the sub-project.
- Kubernetes and cloud-native expertise to evaluate the operator decision and, if retained, implement it.
- Reviewers for EVM security and Ethereum conformance, and for SDK API design.
- Documentation and onboarding contributors.

## Maintainer and Contributor Diversity

### Hyperledger Fabric

The active maintainer roster is **unchanged at 9**: Alessandro Sorniotti, Andrew Coleman, Artem Barger, Dave Enyeart, Fedor Partanskiy, Manish Sethi, Tatsuya Sato, Yacov Manevich, Yoav Tock. No maintainers were added or retired in the period.

Release manager changes did occur: Yacov Manevich was removed as a release manager ([#5369](https://github.com/hyperledger/fabric/pull/5369)), and Dave Enyeart stepped down, nominating Fedor Partanskiy to replace him ([#5396](https://github.com/hyperledger/fabric/pull/5396)). This took the roster from three to two: Artem Barger and Fedor Partanskiy.

Contributor diversity moved in the wrong direction. Distinct non-bot authors on `main` fell from **32 in H1 2025 to 23 in H1 2026**, and non-bot commits from 79 to 64 (both 2025 figures recomputed with the same method). Contribution is also heavily concentrated: one contributor authored 32 commits under one identity and 35 of 64 (55%) after their two Git identities are merged; the same contributor submitted 54 of 90 merged pull requests.

Organizational diversity is better than individual diversity. Of the nine active maintainers, five are from IBM (Andrew Coleman, Dave Enyeart, Alessandro Sorniotti, Manish Sethi, and Yoav Tock) and four are not (Artem Barger, Yacov Manevich, Fedor Partanskiy, and Tatsuya Sato). The maintainer file records email addresses rather than employers, so we state these affiliations as maintainers rather than as file-verifiable data; the non-IBM maintainers span more than one organization, which we believe satisfies the Graduated threshold of at least three maintaining organizations. Recording affiliations explicitly in `MAINTAINERS.md` would let the TAC verify this without relying on our statement.

### Hyperledger Fabric-X

Maintainer rosters at the end of the period:

| Repository | Maintainers |
|---|---|
| fabric-x | 7 — Hagar Meir, Ilie Circiumaru, Liran Funaro, Marcus Brandenburger, Pasquale Convertini, Senthilnathan Natarajan, Yoav Tock |
| fabric-x-orderer | 2 — Hagar Meir, Yoav Tock |
| fabric-x-committer | 2 — Liran Funaro, Senthilnathan Natarajan |
| fabric-x-common | 3 — Liran Funaro, Senthilnathan Natarajan, Yoav Tock |
| fabric-x-evm | 4 — Alessandro Sorniotti, Arne Rutjes, Eyal Kushnir, Marcus Brandenburger |
| fabric-x-sdk | 4 — Alessandro Sorniotti, Arne Rutjes, Eyal Kushnir, Marcus Brandenburger |
| fabric-x-endorser | 3 — Angelo De Caro, Alessandro Sorniotti, Marcus Brandenburger |

Counted as distinct individuals across the sub-project, Fabric-X went from **7 maintainers at the start of the window to 11 at the end — 4 net new** (Ilie Circiumaru, Pasquale Convertini, Arne Rutjes, Eyal Kushnir). Three changes produced this: the umbrella repository gained a `MAINTAINERS.md` in January ([#34](https://github.com/hyperledger/fabric-x/pull/34)) and added the orderer and committer maintainers to it in March ([#70](https://github.com/hyperledger/fabric-x/pull/70)); and the EVM and SDK repositories arrived with maintainer files in their initial imports. Notably, **no maintainer was added to the orderer or the committer**, the two repositories carrying the most change.

The reported contributor count is higher: **35 distinct non-bot author names** (**33** after merging the two duplicate identities) across the seven repositories, versus the 14 contributors reported for 2025. The two new repositories and different counting method prevent a like-for-like comparison, so this should be read only as directional evidence of broader participation.

Organizational diversity is the sub-project's weakest dimension: **all 11 current Fabric-X maintainers are from IBM**, which originally developed the architecture. Combined with two-maintainer counts on the highest-traffic repositories, this remains the sub-project's clearest community-health risk, and it means Fabric-X does not currently satisfy the Incubation expectation of at least two maintaining organizations. Recruiting maintainers from at least one other organization is therefore an H2 priority rather than a documentation task; contributor participation in the wider ecosystem, particularly Fabric Smart Client, is the most likely source of such candidates.

## Project Lifecycle Status Recommendation

- **Hyperledger Fabric: Graduated, no change.** Release cadence, maintenance activity, and nine active core maintainers support the current status. Five of the nine maintainers are from IBM and four are not, spanning more than one additional organization, so we believe the Graduated expectation of at least three maintaining organizations is met; because `MAINTAINERS.md` records email addresses rather than employers, we ask the TAC to accept these affiliations as maintainer-stated. The declining contributor trend remains an H2 concern.
- **Hyperledger Fabric-X: Incubation, with an explicit organizational-diversity gap.** No change in status is requested. The v1.0.0 milestones, documentation work, Kubernetes and observability delivery through the Ansible collection, and maintainer growth are strong signals. Remaining concerns include no project-maintained adopter evidence, an experimental Fabric Smart Client driver, two-maintainer counts on the busiest repositories, and inconsistent release publishing. Most importantly, all current Fabric-X maintainers are from IBM, so the Incubation expectation of at least two maintaining organizations is not yet met; adding maintainers from another organization is an H2 goal. The TAC should confirm that Fabric-X meets the Incubation requirement of at least two maintaining organizations.

## Useful Links

### Hyperledger Fabric

- [Repository](https://github.com/hyperledger/fabric) · [Releases](https://github.com/hyperledger/fabric/releases) · [Documentation](https://hyperledger-fabric.readthedocs.io/)
- [RFCs](https://github.com/hyperledger/fabric-rfcs) · [MAINTAINERS.md](https://github.com/hyperledger/fabric/blob/main/MAINTAINERS.md) · [SECURITY.md](https://github.com/hyperledger/fabric/blob/main/SECURITY.md)
- [Technical Charter](https://github.com/hyperledger/fabric/blob/main/Hyperledger_Fabric_Technical_Charter.md) · [Governance](https://github.com/hyperledger/fabric/blob/main/GOVERNANCE.md)

### Hyperledger Fabric-X

- [fabric-x](https://github.com/hyperledger/fabric-x) · [fabric-x-orderer](https://github.com/hyperledger/fabric-x-orderer) · [fabric-x-committer](https://github.com/hyperledger/fabric-x-committer) · [fabric-x-common](https://github.com/hyperledger/fabric-x-common) · [fabric-x-endorser](https://github.com/hyperledger/fabric-x-endorser)
- [fabric-x-evm](https://github.com/hyperledger/fabric-x-evm) · [fabric-x-sdk](https://github.com/hyperledger/fabric-x-sdk) · [fabric-x-samples](https://github.com/hyperledger/fabric-x-samples) · [fabric-x-rfcs](https://github.com/hyperledger/fabric-x-rfcs)
- [Committer documentation](https://hyperledger.github.io/fabric-x-committer/) · [Fabric-X whitepaper](https://eprint.iacr.org/2023/1717.pdf) · [Arma paper](https://arxiv.org/abs/2405.16575)
- [Ansible collection](https://github.com/LF-Decentralized-Trust-labs/fabric-x-ansible-collection) · [Block explorer](https://github.com/LF-Decentralized-Trust-labs/fabric-x-block-explorer) · [Fabric Smart Client](https://github.com/hyperledger-labs/fabric-smart-client) · [Fabric Token SDK](https://github.com/hyperledger-labs/fabric-token-sdk)
- [Fabric/Fabric-X monthly call — 3rd Wednesday](https://zoom-lfx.platform.linuxfoundation.org/meetings/fabric?view=month)
