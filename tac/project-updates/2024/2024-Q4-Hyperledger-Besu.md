---
layout: default
title: 2024 Q4 Hyperledger Besu
parent: 2024
grand_parent: Project Updates
---

# Project Health

The Besu project continues to thrive. [Fleet Mode](https://consensys.io/blog/besu-fleet-the-future-of-rpc-scaling) has bolstered interest in Besu from public blockchain networks and private chains, with both Layer 2 and RPC providers considering Besu for their infrastructure. Community activity on Discord is stable, though external contributions are at a seasonal lull. Overall, the project remains healthy. 

# Questions/Issues for the TOC

Besu contributors have been asking to use a single [CLA](https://en.wikipedia.org/wiki/Contributor_License_Agreement) instead of the DCO requirement for every commit, which is a source of unnecessary friction. The new [LFDT Charter](https://www.lfdecentralizedtrust.org/about/charter) does not mention anything about requiring either, and as such the Besu team intends to relax the DCO requirement in favor of a single CLA.

# Releases

This quarters releases:

- 24.10.0
- 24.12.0
- 24.12.1
- 24.12.2

Highlights include:

- named network support for the Ephemery testnet. This is a public testnet that will be torn down and rebuilt from scratch periodically. This implementation was submitted by a non-maintainer, thanks [@gconnect](https://github.com/gconnect)!

As usual, each release also included important bug fixes.

Challenges include:

- post release of 24.12.0 we noticed that some nodes can freeze up to 2 hours when opening RocksDB database. Besu was impacted by an upstream change in RocksDB (our database) as we moved from RocksDB 8.3.2 in Besu 24.10.0 to RocksDB 9.7.3 in Besu 24.12.0. This change triggers some compaction work depending on the size of the database to apply the new configuration (recommended). Not all upgraded nodes  faced the freeze, and this was not seen during testing. The compaction can still happen in the background, but some users reported up to 2 hours freeze.
- 24.12.1 was a hotfix to address publishing besu maven artifacts. 



# Overall Activity in the Past Quarter

Over the past several months, the Besu team and community contributors have addressed a variety of enhancements, bug fixes, and performance optimizations. A number of improvements target transaction processing speed, and accompanying metrics to better visualize and analyze those improvements. 

Equally notable is the growing community involvement in troubleshooting, code reviews, and feature proposals. Contributors have tackled concurrency issues, refactored internal modules, updated dependencies, and implemented new configuration options—efforts that reduce technical debt while enabling better customization for diverse use cases. 

Since the deprecation of the Hyperledger brand, the Besu project has begun the process of migrating their repositories to the `besu-eth` organization on GitHub.

The team has adopted automation to better manage issues- GitHub actions are used to mark any issues or prs that have had no activity for the last 2 weeks as stale, and if they are not tended to in in the subsequent 2 weeks the will be closed. This will enforce regular review of issues.

# Current Plans

The Prague and Osaka upgrades will be the primary focus in Q1 2025. We continue to invest in our plugin architecture and modularizing the codebase to accommodate that. Integration with the Portal Network will be invested in to reduce the storage footprint required by mainnet nodes.

# Contributor Diversity

Due to an increase in trivial or automatically generated PRs, we have had to refine our [policies around insignificant contributions](https://github.com/hyperledger/besu/blob/main/CONTRIBUTING.md#guidelines-for-non-code-and-other-trivial-contributions) likely intended to farm future rewards.

# Additional Information

