[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2025 Annual Review Besu

## Project Health

Besu had a strong 2025, successfully delivering support for two major Ethereum hard forks (Pectra and Fusaka), making significant progress on performance optimization toward Gigagas targets, and continuing to mature its plugin architecture. Community engagement on Discord remained active, with particular interest around performance improvements and protocol development. The project delivered at least 7 major releases throughout the year, maintaining a consistent release cadence. Besu holds approximately 16-18% of Ethereum mainnet execution layer stake, maintaining its position as the third most popular execution client and contributing to healthy client diversity.

## Maintainer Diversity

The Besu project has 21 active maintainers. Organizational diversity among maintainers remains a challenge:

- Consensys Software Inc.: ~19 maintainers (~90%)
- Kaleido: 1 maintainer (~5%)
- Other/Unknown: 1 maintainer (~5%)

While maintainer diversity is limited at the organizational level, the project has seen increased contributor diversity. Notable contributions in 2025 came from cross-client developers at the Ethereum Foundation, performance optimization contributors from quadratic-labs, enterprise users, and individual developers. Q4 alone welcomed 12 first-time contributors. The Besu Certified Service Provider (CSP) program launched in Q2 2025 with six certified companies: Consensys, Kaleido, Cheesecake Labs, CPQD, DSR Corporation, and Kerala Blockchain Academy.

## Project Adoption

Besu maintains approximately 16-18% of Ethereum mainnet execution layer stake, a healthy position for client diversity within the Ethereum ecosystem. Major staking providers include Besu in their multi-client infrastructure.

Enterprise adoption continues to grow across several sectors:
- **Financial Services**: Institutions leveraging Besu's QBFT consensus and enterprise features for both pilot projects and production deployments, including participation in the Hyperledger Besu for Financial Services Working Group.
- **Layer 2 Integration**: Besu serves as execution layer infrastructure for rollup projects including Linea. The expanded Plugin API enabled Linea to run their rollup on mainline Besu with plugins instead of maintaining a fork.
- **CBDC Projects**: Multiple national and regional Central Bank Digital Currency pilot projects building on Besu.
- **Private Networks**: Continued adoption for permissioned networks leveraging QBFT consensus.

## Goals

### Performance Against Prior Goals

The 2024 annual review set the following goals for 2025:

**Performance, stability, modularity, and upcoming protocol changes like PeerDAS and Stateless Ethereum:**
- ACHIEVED. Significant performance optimization work was completed throughout 2025, including EVM opcode optimizations (EQ, MOD, AND, OR, XOR, NOT), Engine API performance improvements (5-6x faster toFastHex for engine_getBlobsV2), EcRecover precompile and CallDataCopy optimizations, block header caching, parallel world state root hash calculation, and Java 25 optimized VM options. PeerDAS dependency updates were delivered. Plugin architecture was significantly enhanced, enabling Linea to run on mainline Besu.

**Support the Fusaka and Glamsterdam hard forks:**
- ACHIEVED (Fusaka) / IN PROGRESS (Glamsterdam). Besu successfully delivered Pectra hard fork support (May 7, 2025) and Fusaka hard fork support with mainnet activation in December 2025, including Osaka, BPO1, and BPO2 fork scheduling and the gas limit increase from 36M to 60M. Glamsterdam development is underway with active work on EIP-7928 (Block Access Lists) with 33+ merged PRs.

**Additional accomplishments in 2025:**
- Launched the Besu Certified Service Provider (CSP) program
- Implemented ERA1 file export functionality for Ethereum's history expiry roadmap
- Continued removal of PoW features and technical debt (PoW RPC methods, CLI options, tests, and JSON block importer)
- Improved block creation resilience and transaction pool management
- Migrated testing and CI/CD to GitHub Actions with consistent burn-in release process

### Next Year's Goals

- Continue performance optimization toward Gigagas targets, including further EVM arithmetic optimizations and serialization improvements
- Complete Glamsterdam hard fork implementation and support future Ethereum protocol upgrades
- Continue removing technical debt and deprecated features (PoW, Clique, Fast Sync)
- Increase maintainer diversity beyond Consensys, establishing formal pathways for new maintainer onboarding
- Advance Bonsai archive and Bonsai archive proofs data storage options
- Grow the contributor community and improve onboarding documentation

### Help Required

- Continued collaboration with LFDT staff to identify contributors and potential maintainers from additional organizations

## Project Lifecycle Status Recommendation

This report recommends continuing the graduated status. Besu continues to demonstrate strong project health with consistent releases, active community engagement, significant protocol contributions, and broad adoption across public and enterprise networks.
