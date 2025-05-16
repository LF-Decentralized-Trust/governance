---
layout: default
title: 2025 Q2 Hyperledger Caliper
parent: 2024
grand_parent: Project Updates
---

# Project Health

Caliper is a fairly mature and stable tool for Hyperledger Fabric benchmarking and as such is in maintenance mode at this time. It supports Fabric 2.5 LTS and also works with Fabric 3.x releases. Hyperledger Caliper will officially support Fabric 3.x once an LTS release (ie production ready version) is made available.

* 2 active maintainers
* Questions on Discord and GitHub are responded to
* Contributor discussions happen mostly on Discord

# Questions/Issues for the TAC

Not at this time.

# Releases

The latest stable release is v0.6.0; we're also continuously publishing unstable releases after every merged PR (no new releases):

* [npm](https://www.npmjs.com/package/@hyperledger/caliper-cli/v/0.6.0)
* [DockerHub](https://hub.docker.com/layers/hyperledger/caliper/0.6.0/images/sha256-ace68b58b329a5f2c5bd569cc2f59b7f64e9bbee1f3bb9f4f8a97469b55d7b2b?context=explore)

# Overall Activity in the Past Quarter

The main activity has been around 2 things, the first being to engage with someone with the intent to include a new connector into Hyperledger Caliper for Polkadot. Technical and code review feedback has been provided and the hope is that they will submit a PR for the new connector sometime in the near future as they work on the feedback provided.
The second has been to remove unsupported and out of date components from Caliper plus a few minor improvements on the code and documentation.

[List of merged PRs (27)](https://github.com/hyperledger-caliper/caliper/pulls?q=is%3Apr+is%3Aclosed+merged%3A2024-12-12..2025-05-16)

Summary of activities:
* Remove support for Besu/Ethereum
* Remove support for Fabric Node SDK 1.4
* A few bug fixes


# Current Plans

* include a Polkadot connector for Hyperledger Caliper.
* Aim to have another Caliper release delivered by the end of the year.

# Maintainer Diversity

[Hyperledger Caliper maintainers](https://github.com/hyperledger-caliper/caliper/blob/08f732a484c93285fdc4df628f10cbc8d454d583/MAINTAINERS.md) in 2025 Q2 (unchanged compared to the previous quarter):
* Dave Kelsey (UK)
* Attila Klenik (NTCA|BME, Hungary)

# Contributor Diversity

Contributions from maintainers only this quarter

# Additional Information

[Insights dashboard link](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=caliper&routedFrom=Github&bestPractice=false&repository=all&dateFilters=2024-12-12%20to%202024-05-16&dateRange=2024-12-12%20to%202024-05-16&compare=PP&granularity=week&hideBots=true)
