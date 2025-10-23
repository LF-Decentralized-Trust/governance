[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2025 Q4 Hyperledger Cacti

# Project Health

- We continued to be strongly aligned with the [IETF standard for cross-network asset transfers](https://datatracker.ietf.org/wg/satp/about/) with the [0.0.3-beta version release](https://github.com/hyperledger-cacti/cacti/pull/3922) of the SATP implementation. Continuous work in the Typescript and Rust implementations is being done to make the reference implementations production-ready.
- Maintainers have continued [to be active in the IETF](https://github.com/ietf-satp/draft-ietf-satp-core), promoting and adopting DLT interoperability standards.
- Integration of Cactus and Weaver connectors is continuing apace within a LF 2025 mentorship project.
- A workshop has been scheduled in November to present the latest feature developments in Cacti.
- We've started to solicit contributors and receive communication from potential contributors. Onboarding new contributors to the project.	

# Questions/Issues for the TAC

None at this time

# Releases

- There was a SATP-Hermes feature `0.0.3-beta` version release.
- There was no major Cacti release aside from this feature. The latest release is still `v2.1.0`, which was offered last December. As we mentioned in the previous quarterly report, a new version release (either `v2.2.0` `v3.0.0`) is overdue, and we will attempt to do that before the winter break.

# Overall Activity in the Past Quarter

- The mailing list is pretty quiet but the Discord channels are active, with regular interactions among maintainers, between maintainers and users and between new users and contributors.
- Apart from the SATP feature and the Cactus-Weaver connection integration work, the project is in maintenance mode with PRs involving bug fixes, security patches, and dependency upgrades.
- SATP development activity (0.0.3-beta): full refactor, support for audits, monitoring, bug fixes, bridge support for Fabric, Besu, and EVM-based chains, data transfer mode, and more. 
- 2025 mentee, Carlos Amaro, has produced a draft PR integrating the Cactus Fabric ledger connector with the Weaver Fabric driver into a unified Fabric connector. This PR is under review. Once merged, this will provide a reference for other DLT connector integrations as well as building new DLT connectors from scratch.

A couple of maintainers (Rafael and Ramakrishna) have continued to be active in the IETF SATP Working Group, which is now moving beyond asset transfers to tackle other interoperability modes.

# Current Plans

- Prepare for and run the November workshop.
- Continue to develop the SATP feature, and try to port it to work with Weaver relays.
- Complete the connector integration feature work and demonstrative examples by the end of the 2025 mentorship.
- Produce a new Cacti release (`v2.2.0` or `v3.0.0`).
- Connect with interested parties (other projects' maintainers, other companies) to contribute to Cacti and/or join the Cacti maintenance team.

# Maintainer Diversity

We have active maintainers from three different companies (Fujitsu, IBM, and Blockdaemon) and a research institution (INESC-ID). Accenture left the project.

# Contributor Diversity

|Rank|Organization                   |Contributions|% Contributions|
|----|-------------------------------|-------------|---------------|
|1   |Blockdaemon                    |522          |73%            |
|2   |INESC-ID                       |107          |15%            |
|3   |IBM                            |36           |5%             |
|4   |Ework Group                    |21           |3%             |
|5   |The Linux Foundation           |12           |2%             |
|6   |Hyperledger                    |6            |1%             |
|7   |Accenture                      |4            |1%             |

Source: [LFX Cacti Project Page](https://insights.linuxfoundation.org/project/cacti/contributors?timeRange=previousQuarter&start=2025-07-01&end=2025-09-30&widget=organization-dependency)

# Additional Information

N/A
