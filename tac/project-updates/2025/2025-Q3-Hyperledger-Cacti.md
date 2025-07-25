---
layout: default
title: 2025 Q3 Hyperledger Cacti
parent: 2025
grand_parent: Project Updates
---

# Project Health

- Unfortunately, we had a major setback in the form of losing Accenture's maintainers, including Peter Somogyvari, who had ably led the maintenance and evangelization of the project from its inception.
- Losing Accenture led to a significant slowdown in maintenance and release activity as other maintainers have limited bandwidth and been busy with their day jobs.
- Innovative feature development continues apace though, with the completion of a major SATP (the IETF standard-in-works) implementation, albeit the merge hasn't completely happened yet as it's a huge chunk of code.
- Cacti still has the reputation of a flagship interoperability project with maintainers involved in drafting and implementation of IETF standards.
- We got a very capable LFDT mentee in the form of Carlos Amaro, who has been contributing to Cacti for a while and is an expert in the SATP implementation. He is working on integrating the Cactus and Weaver connectors, following up on work done by last year's LFDT mentee.

# Questions/Issues for the TAC

For most of the legacy maintainers (specifically, IBM and Fujitsu), project maintenance and development is strictly a part-time activity, as our day jobs involve very different tasks these days. We'd love to find replacements for Accenture to share maintenance and ownership of the project. As a start, we will try to reach out to some of the companies that have collaborated with Cacti and helped build plugins in the past, and who are active in the interoperability space (e.g., Chainlink, Huawei). But any assistance we can get from the TAC in this regard would be much appreciated.

# Releases

None this quarter unfortunately. The latest release is still `v2.1.0`, which was offered last December.

There were issues with producing a next release that Peter was on top of (mentioned in the Q2 report) but couldn't complete before stepping down as maintainer. That's not an excuse as the other maintainers have the capability, but no one could spend the time to fix those issues.

That said, there has been significant development activity and we do plan to issue at least one release in the upcoming quarter.

# Overall Activity in the Past Quarter

As in the previous quarter, the mailing list is pretty quiet. The Discord channels and DMs are where most of the communication happens. The #cacti-contributors channel is quite active, with queries about code and tooling and requests for code reviews dominating the conversations. Questions get answered generally in a timely manner.

Coding and PR activity in the quarter involved:
- Some bug fixes and security patches
- The main feature development was in the SATP Dev branch (led by Andre Augusto and Rafael Belchior). This was approved for merge recently but the code increment was deemed too large for a single PR, and so the contributors are currently merging the code in meaningfully divided chunks.
- The Fabric-related code is somewhat out-of-date, and there are efforts by several people to upgrade Fabric dependencies in different packages.
- The mentee, Carlos Amaro, has been working on upgrading the Weaver Fabric driver as a prelude to merging its functionality with the Cactus Fabric connector.

A couple of maintainers (Rafael and Ramakrishna) have also been active in the IETF SATP Working Group, guiding the draft specifications toward RFC status.

# Current Plans

We need to revisit the plans from the previous quarter and make some progress on them, which includes the following:
- Complete the SATP feature merge to the `main` branch, and in the same vein, incorporate up-to-date specifications from the IETF SATP drafts.
- Produce at least one release (`v2.2.0` and hopefully `v3.0.0`) according to the plans Peter had made before stepping down
- Try to find additional maintainers
- Connect with Chainlink to find volunteers to finish the CCIP Connector feature and possibly also solicit maintainers from them

# Maintainer Diversity

Despite losing Accenture and its maintainers, we still have active maintainers from three different companies (Fujitsu, IBM, and Blockdaemon) who meet occasionally, respond to questions on Discord, monitor PRs, and contribute code. So at least on the diversity criterion, we still meet the bar for a Graduated project.

# Contributor Diversity

|Rank|Organization                   |Contributions|% Contributions|
|----|-------------------------------|-------------|---------------|
|1   |INESC-ID                       |195          |45%            |
|2   |Ework Group                    |85           |20%            |
|3   |Accenture                      |71           |16%            |
|4   |Blockdaemon                    |54           |54%            |
|5   |IBM                            |27           |27%            |

Source: [LFX Cacti Project Page](https://insights.linuxfoundation.org/project/cacti/contributors?timeRange=previousQuarter&start=2025-04-01&end=2025-06-30&widget=organization-dependency)

# Additional Information

N/A
