---
layout: default
title: 2025 Q2 Cacti
parent: 2025
grand_parent: Project Updates
---

# Project Health

- We are forging ahead with the IETF SATP reference implementations, the codebase integration and a mentorship project proposal which was granted acceptance just a few days ago.
- We are still working on the Cacti Chainlink CCIP connector which we've presented in the February LFDT Interoperability Workshop mid-February this year.
- We had an LFDT mentorship project approved for the summer, which will further the goal of creating an integrated architecture as envisioned in the project's roadmap.
- A steady stream of questions are being answered on Discord where most of our activity is happening these days.
- There haven't been any violations of the code of conduct by contributors so we count ourselves lucky so far.
- There's been a bit of a slowdown this quarter, the number of active Contributors are decreased by 9.09%.

# Questions/Issues for the TAC

N/A

# Releases

2025-12-02 - `v2.1.0`

We've had plans to issue v2.2.0 in this quarter but there is a chain of dependencies tied in a bit of a gordian knot with the release process, the package renaming and the `satp-dev` branch which contains most of the work of the IETF SATP team. We are hoping to have the new release issued within a few weeks from now when the `satp-dev` branch is properly merged onto `main`.

# Overall Activity in the Past Quarter

We regularly respond to questions! 
With that said the mailing list is pretty quiet. 
The Discord channels and DMs are where most of the communication happens.

New features are being developed and we have at least 3 active maintaniers who can step in when needed.

Technical changes that we are working on:
1. Get release process fully migrated to the new GitHub organization
2. Better package.json validation across the board with the declarative constraint validation feature of a library called `joi` (we have 60+ packages)
3. Bringing down the Dependabot alerts
4. Increasing our OpenSSF score, particularly with the low hanging fruit such as not committing binaries into the git repository
   
# Current Plans

We'll want to do a major release this summer because we have to have some breaking changes.
We need to migrate away from Web3JS which was unfortunately deprecated and retired as of last month (March 2025).
This will be a particularly big amount of work and also lots of breaking changes in the APIs of the EVM flavored connector plugins.

> What are the main features planned? 

- IETF SATP reference implementation + bridges
- Cacti Chainlink CCIP Connector Plugin

> What releases are planned?

- v2.2.0
- v3.0.0

> Are there any specific efforts or branches of development underway?

The SATP Dev branch is the big one but we also have the Cacti CCIP Connector which is
a major piece of work as well.

There is also ongoing effort to migrate away from Web3JS which has been in progress for a while now.

# Maintainer Diversity

**Active Maintainers**

| Name | GitHub | Chat |
|------|--------|------|
| Izuru Sato | [izuru0][izuru0] | izurusato |
| Michal Bajer | [outSH][outSH] | - |
| Peter Somogyvari | [petermetz][petermetz] | peter_somogyvari |
| Takuma TAKEUCHI | [takeutak][takeutak] | takeutak |
| Jagpreet Singh Sasan | [jagpreetsinghsasan][jagpreetsinghsasan] | jagpreetsinghsasan |
| Venkatraman Ramakrishna | [VRamakrishna][VRamakrishna] | vramaiitkgp |
| Sandeep Nishad | [sandeepnRES][sandeepnRES] | sandeepn |
| Rafael Belchior | [RafaelAPB][RafaelAPB] | rafaelapb |


# Contributor Diversity

|Rank|Organization                   |Activities|% Contributions|Change|
|----|-------------------------------|----------|---------------|------|
|1   |Accenture                      |102       |48.57%         |-78   |
|2   |Blockdaemon                    |57        |27.14%         |-63   |
|3   |INESC-ID                       |18        |8.57%          |13    |
|4   |IBM                            |18        |8.57%          |-79   |
|5   |The Linux Foundation           |12        |5.71%          |-14   |
|6   |Mitsubishi Electric Corporation|2         |0.95%          |-4    |
|7   |Fujitsu Limited                |2         |0.95%          |2     |

Source: [LFX Cacti Project Page](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=cacti&routedFrom=Github&bestPractice=false&repository=all&dateFilters=Last%20Quarter&dateRange=2025-01-01%20to%202025-03-31&compare=PP&granularity=week&hideBots=true)

# Additional Information

N/A
