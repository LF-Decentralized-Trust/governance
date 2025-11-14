[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2025 Q4 Hyperledger Iroha

# Project Health

This quarter, Iroha 2 has maintained a stable, consistent development trajectory, with a strategic focus on enhancing functionality, scalability, and stability to meet the rigorous demands of commercial applications. Key focus areas include advancing its suitability for Central Bank Digital Currencies (CBDCs) and intergovernmental payment solutions. Concurrently, significant architectural improvements and the development of a new virtual machine are underway to provide foundational support for the upcoming SORA 3 public blockchain network (SORA Nexus), positioning Iroha 2 as a robust platform for both private and public blockchain implementations.

# Questions/Issues for the TAC

There are no questions or issues at this time.

# # Releases

<a href="https://github.com/hyperledger-iroha/iroha/releases/tag/v2.0.0-rc.2.1">2.0.0-rc.2.1</a></br>
<a href="https://github.com/hyperledger-iroha/iroha/compare/v2.0.0-rc.2.0...v2.0.0-rc.2.1">Full Change Log</a>

# Overall Activity in the Past Quarter

The Iroha 2 team has continued executing on a long-term development roadmap, delivering both community-driven features and commercial enhancements.

<u>Community-Driven Features:</u>
<ul>
<li>New VM Architecture: A redesigned execution environment for improved smart contract performance and flexibility.</li>
<li><a href="https://github.com/hyperledger-iroha/hub-chain-poc">Iroha 2 hubchain.</a></li>
<li>Nominated Proof-of-Stake (NPoS): Developing a dynamic consensus mechanism to replace the static model for greater decentralization.</li>
<li>Kotodama Language Evolution: Ongoing refinement of the native smart contract language for a better developer experience.</li>
<li>Erasure-Coded Storage: Enhances data resilience and reduces storage burdens by redundantly sharding block data across the network.</li>
<li>Sora Network Support: Key features like Missing Triggers and advanced Node Syncing are being developed to support the Sora public blockchain.</li>
</ul>

<u>Commercial-Driven Features:</u>
<ul>
<li><a href="https://github.com/hyperledger-iroha/iroha/issues/1177">Transaction Fees Module</a>: A flexible and configurable system for managing on-chain transaction fees.</li>
<li>API Simplification: Streamlined and refined interfaces specifically tailored for CBDC project requirements.</li>
<li>Horizontal Scalability (Multi-Lane): Parallel transaction processing to deliver the high throughput required for enterprise and government use cases.</li>
<li>Data Spaces: A new ledger partitioning concept designed to enable scalable state and transaction management for complex commercial applications.</li>
</ul>

# Current Plans

Our roadmap is centred on advancing network performance, scalability, and security and will include the following initiatives:

Planned initiatives include:
<ul>
<li>Dynamic Lane Management: Auto-adjusting transaction lanes based on load to protect network performance.</li>
<li>Stricter Data Controls: Enforcing block size limits for more reliable data verification.</li>
<li>Global Address Format (IH-B32): A new standard to prevent cross-chain errors and improve interoperability.</li>
<li>Enhanced Testing Tools: Upgrading tooling to support multi-lane architecture fully.</li>
</ul>

# Contributor Diversity

<ul>
<li>7 active contributors in the past quarter
 Source: <a href="https://insights.linuxfoundation.org/project/iroha?timeRange=past365days&start=2024-08-11&end=2025-08-11">LF Insights – Iroha</a></li>
</ul>

<u>External contributors mainly worked on:</u>
<ul>
<li>Added a Torii `/server_version` endpoint and a client `version` subcommand to display versions and git SHAs.</li>
<li>Fixed minor issues in code comments.</li>
<li>Added a test for failed transfers with an incorrect `AssetId`.</li>
<li>Deprecated the direct `--profile` flag in the Kagami WASM CLI in favor of `--cargo-args`.</li>
<li>Fixed minor documentation nits in code comments.</li>
</ul>

# Additional Information

As a proven and stable solution, Iroha 2 is already deployed in live environments, supporting critical blockchain infrastructure in Japan, the UK, the UAE, and Thailand.
