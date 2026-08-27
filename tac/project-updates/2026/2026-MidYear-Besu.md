[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Mid-Year Review: Besu

## Progress Against 2026 Goals

The 2026 annual review set six goals. Here is the status at mid-year:

### 1. Performance Optimization Toward Gigagas Targets — On Track

Substantial arithmetic optimization work landed in the first half of the year. A systematic series of UInt256 long-limb implementations covered ADD, SUB, MUL, DIV, SDIV, MULMOD, ADDMOD, and DIVMOD. Shift opcodes (SAR, SHR, SHL) received cache-locality improvements. Power-of-two fast paths were added for `div`, `addMod`, and `mulMod`. Taken together, 70% of EEST execution benchmarks showed improvement as of the 26.2.0 release. A JMH GasProfiler that emits mgas/s was added to make performance tracking more rigorous. Cross-block code caching and parallel Bonsai state root computation also landed. Concurrent Engine API execution (26.7.0) means light requests no longer queue behind block import.

### 2. Glamsterdam Hard Fork — In Progress, On Track for Devnet

Extensive EIP implementation is underway across the period. EIPs shipped or in-flight include: EIP-7928 (Block Access Lists), EIP-8037 (state creation gas cost increase), EIP-8038 (calldata floor, SSTORE ordering), EIP-7954 (64 KiB/128 KiB code and initcode size limits), EIP-7843 (SLOTNUM opcode), EIP-8246 (SELFDESTRUCT preserves originator balance), EIP-2780/7702 (resource-based intrinsic gas and per-authorization refund), EIP-8282 (builder deposit/exit execution requests), and EIP-8070 (`engine_getBlobsV4` and custodyColumns). P2P exchange protocols for BAL (eth/71, snap/2) and partial block receipt lists (eth/70) also landed. Besu has been tracking Amsterdam devnet milestones, with devnet-8 shipping in August 2026. Mainnet activation is not yet scheduled.

### 3. Technical Debt Removal — COMPLETE

All three goals from the annual review are fully delivered ahead of schedule:

- **Fast Sync removed** (26.2.0, February): `CHECKPOINT` sync mode now redirects to `SNAP` sync.
- **Clique removed** (26.4.0, April): Production mining code removed. PoS-transitioned Clique chains (e.g., Linea Mainnet) still sync correctly.
- **Proof of Work fully removed** (26.7.0, July): Removed in four coordinated PRs covering mining infrastructure, Ethash and validation code, the `miner_start`/`miner_stop`/`eth_mining` RPC methods, and the `PowAlgorithm` enum.

Additional debt cleared: ETC Classic support removed (26.2.0), Holesky network deprecated and removed (26.4.0), `--network=dev` removed, deprecated plugin API methods removed.

### 4. Maintainer Diversity — Limited Progress

Three maintainers moved to emeritus status in February 2026. One new maintainer was added: Miroslav Kovář in April 2026 (PR #10033). The project currently has 19 active maintainers, with organizational distribution still heavily skewed toward Consensys. No new organizations have been onboarded into the maintainer set in this period. See the maintainer/contributor diversity section below.

### 5. Bonsai Archive and Archive Proofs — On Track

Bonsai Archive hybrid mode landed in 26.5.0, providing a migration path for nodes that want archive depth without a full archive node. A Bonsai-to-archive migration tool shipped in 26.4.0. Separate column families for archive data landed in 26.4.0. Archive proofs with a simple trie implementation is in progress (PR #11016, unreleased at time of writing). Stateroot refactoring to support this is also underway.

### 6. Contributor Community Growth — On Track

86 unique contributors have made commits in 2026 (January through August), with 860 total commits across that period. Formal data on documentation improvements to onboarding materials is not yet available.

---

## Deliverables and Outputs (January–August 2026)

### Releases

Ten GA releases and 14 release candidate tags were published:

| Release | Date |
|---------|------|
| 26.1.0 | 2026-02-03 |
| 26.2.0 | 2026-03-04 |
| 26.3.0 | 2026-03-10 |
| 26.4.0 | 2026-04-18 |
| 26.5.0 | 2026-05-07 |
| 26.6.0 | 2026-05-28 |
| 26.6.1 | 2026-06-08 |
| 26.7.0 | 2026-07-10 |
| 26.7.1 | 2026-07-24 |
| 26.8.0 | 2026-08-18 |

### Security Releases

26.7.1 and 26.8.0 included coordinated security fixes for 10 published GHSAs, addressing denial-of-service and memory exhaustion vectors in the filter/subscription system, snap sync, DiscV4, BFT message handling, and RLPx connection handling, as well as bounded range queries in GraphQL and `eth_getFilterLogs`. A fix for a BLAKE2F/precompile cache collision was also included.

### Plugin API Modularization

The monolithic `besu-plugin-api` artifact is being decomposed into fine-grained Maven modules (`besu-plugin-api-core`, `-metrics`, `-permissioning`, `-security`, `-txpool`, `-p2p`, `-sync`, `-rpc`, `-chain`, `-worldstate`, `-worldstate-backend`, `-storage`, `-execution`) while retaining full backward compatibility via re-export. Binary compatibility checking via japicmp was added. This work is ongoing into H2 2026.

### Repository Migration

The repository migrated from `hyperledger/besu` to `besu-eth/besu`, announced with the 26.4.0 release.

### JDK 25

Starting with 26.6.0, JDK 25 is required to build and run Besu.

---

## Goals for the Second Half of 2026

- **Glamsterdam mainnet readiness**: Continue tracking Amsterdam devnet milestones, deliver remaining EIP implementations, and prepare for mainnet activation once Ethereum Foundation announces a target.
- **Complete plugin API modularization**: Finish decomposing the remaining plugin-api modules and publish stable artifact boundaries.
- **Bonsai archive proofs**: Land archive proofs (simple trie) and advance the stateroot refactoring that underpins it.
- **Continue performance work**: Further EVM arithmetic and serialization improvements building on the UInt256 foundation. Target improved standing in EEST mgas/s benchmarks.
- **Vert.x 5.x migration**: Complete the upgrade started in unreleased work.

---

## Help Needed

Maintainer organizational diversity remains the project's most persistent structural challenge. LFDT staff assistance in identifying contributors from CSP organizations (Kaleido, Cheesecake Labs, CPQD, DSR Corporation, Kerala Blockchain Academy) who are candidates for maintainer onboarding would be valuable. The project has formal pathways in place; the bottleneck is identifying and engaging the right individuals.

---

## Maintainer and Contributor Diversity

**Active maintainers (19):** Ameziane Hamlat, Daniel Lehrner, Diego López León, Fabio Di Fabio, Gabriel Trintinalia, Gary Schulte, Gabriel Fukushima, Jason Frame, Justin Florentine, Karim Taam, Lucas Saldanha, Luis Pinto, Matilda Clerke, Matthew Whitehead, Miroslav Kovář, Sally MacFarlane, Simon Dudley, Stefan Pingel, Usman Saleem.

**Changes since annual review:**
- Moved to emeritus (February 2026): cdivitotawela, pullurib
- Added as maintainer (April 2026): Miroslav Kovář

**Organizational distribution** remains predominantly Consensys (~18 of 19). Miroslav Kovář (Kaleido) is the only maintainer from outside Consensys. This is unchanged from the annual review.

**Contributors in 2026:** 86 unique contributors by author name, 860 commits (January–August). Commit activity has been consistent, with monthly commit counts ranging from 65 (January) to 146 (March).
