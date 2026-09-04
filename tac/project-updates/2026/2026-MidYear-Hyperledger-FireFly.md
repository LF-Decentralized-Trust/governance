[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 MidYear Hyperledger FireFly

## Project Health

Hyperledger FireFly is healthy and active across the whole project — core, connectors, transaction manager, CLI, Helm charts, sandbox, common libraries, and the doc site. The main story of H1 2026 is the move of every FireFly repository into its own dedicated `hyperledger-firefly` GitHub organization, and the coordinated v1.5.0 release on August 4, 2026 — the first release cut from the new org.

LFX Insights rates the project Healthy at 78/100. Security posture across the project is tracked with the OpenSSF Scorecard on the key repositories, with dependency updates and CVE remediation handled on an ongoing basis. Contributor retention is rated excellent.

The main watch item is contributor and organizational diversity — see the Contributor Diversity section.

### Contributor activity updates

- No maintainer changes across the project in this period.
- Cardano connector contributors from Sundae continue to submit updates on the connector they own.
- A handful of first-time contributors this period across the project on release tooling, workflow fixes, and docs.

## Releases

### [FireFly v1.5.0 (08/04/2026)](https://github.com/hyperledger-firefly/firefly/releases/tag/v1.5.0)

Coordinated release across the FireFly project — first release from the new `hyperledger-firefly` GitHub org, with corresponding updates in the connectors, transaction manager, CLI, and Helm charts. Highlights:

- New GitHub org: all repos now under <https://github.com/hyperledger-firefly>; images under `ghcr.io/hyperledger-firefly/*`; Go imports moved from `github.com/hyperledger/firefly-*` to `github.com/hyperledger-firefly/*`.
- New transaction submission and management APIs in the FireFly Transaction Manager (used in EVMConnect): `POST /submit` for batched submits, `PATCH /transactions/{id}` to update an in-flight transaction, receipts now returned with the confirmation.
- Lightweight block-tracking mode in the connector framework — connectors can track blocks and confirmations without holding a full in-memory chain.
- Better error reporting for smart contract reverts, including nested error strings.
- Go 1.26 across all Go components. gRPC and Alpine base images refreshed.
- Cardano connector maintenance updates.
- New networking metrics and IP/server config options in the common HTTP/TLS/DNS layer.
- Kubo (IPFS) bumped to v0.42.0 in the CLI and Helm charts, with a CLI workaround for a Docker Desktop peer-discovery quirk.
- CVE fixes and general bug fixes.

Across the FireFly project, LFX Insights records around 308 pull requests merged over the trailing 12 months to early September 2026, spanning core, connectors, transaction manager, CLI, and Helm charts.

## Overall Activity in the First Half of 2026

The big piece of work this half was moving every FireFly repository out of the shared `hyperledger` org and into its own `hyperledger-firefly` org. This was a stated goal in the 2025 annual report, aligned with LFDT guidance for projects to move to their own dedicated GitHub organizations, and had been on the roadmap since 2024 — it is now delivered, landing alongside v1.5.0.

Why we did it:

- A dedicated org gives FireFly a clear home and identity now that LFDT projects each stand on their own.
- We control our own GitHub Actions permissions, branch protection, Dependabot, secret scanning, and package publishing — which matters for OpenSSF Scorecard work.
- Container images live under a namespace that clearly identifies FireFly.
- We can grant repo access to contributors without it spilling into unrelated repos.
- New FireFly repos can be added without a governance conversation each time.

Downstream impact for users:

- Container images: pull from `ghcr.io/hyperledger-firefly/*`. The old paths won't get further updates.
- Go modules: update import paths from `github.com/hyperledger/firefly-*` to `github.com/hyperledger-firefly/*`. GitHub redirects handle git clone, but Go's module proxy needs the new path.

To soften the transition we left GitHub redirects on, updated the CLI to use the new image paths, updated the doc site and manifest files, and called out the migration in the v1.5.0 release notes. Rebuilding CI workflows and release tag handling on top of the new org's Actions permissions was the largest hidden cost.

Still catching up: some third-party tutorials and sample repos outside our control still point at the old paths.

Alongside the migration and v1.5.0: continued OpenSSF Scorecard adoption, refreshed Dependabot coverage, doc site updates, and initial work on `main` toward the next release (including a new webhook `confirmationMode` subscription option).

## Adoption

Against the roadmap, we continue to see continued production adoption and scale of FireFly across enterprise deployments.

## Maintainer Diversity

FireFly has 15 maintainers across all repositories, drawn from three organizations: Kaleido, Instinctools, and Sundae. No maintainer changes this period. The list is dominated by Kaleido — broadening it further remains a goal; the Cardano connector work brought Sundae in, and we would like more of the same via community-led connectors. Full list on the [FireFly Maintainers wiki page](https://wiki.hyperledger.org/display/FIR/Maintainers).

## Contributor Diversity

LFX Insights view of the FireFly project for the first half of 2026 (roughly the last 8 months):

- 16 distinct organizations contribute across the project.
- Contributor retention rated excellent.
- LFX flags low contributor diversity and high single-organization dependency across the project.

Kaleido remains the largest single contributing organization by a wide margin. The Cardano connector (added in v1.4.0) brought Sundae in as a new contributing organization, and Instinctools contributes to the Tezos side of the project.

What we're doing about it: making the connector framework and common libraries easier to consume, so external teams can build and maintain their own connectors with less coordination overhead. v1.5.0's connector-framework changes are the concrete step here.

# Additional Information

- Release notes: <https://github.com/hyperledger-firefly/firefly/releases/tag/v1.5.0>
- LFX Insights: <https://insights.linuxfoundation.org/project/firefly>
- Maintainers wiki: <https://wiki.hyperledger.org/display/FIR/Maintainers>
- New GitHub organization: <https://github.com/hyperledger-firefly>
- Issue this report closes: <https://github.com/hyperledger-firefly/firefly/issues/1774>

No questions for the TOC.
