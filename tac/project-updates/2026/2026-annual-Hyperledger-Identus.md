[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Annual Review Identus

## Project Health

Following its transition to the Hyperledger Identus GitHub organization, the project continues to demonstrate steady, sustained development activity. Over the past 12 months, LFX Insights reports 37 active contributors, with approximately 51% quarterly retention, indicating a stable and engaged contributor base. Development activity was recorded on 313 of the last 365 days, reflecting consistent year-round [momentum](https://insights.linuxfoundation.org/project/open-enterprise-agent?timeRange=past365days&start=2025-02-10&end=2026-02-10).

Overall contribution volume remains strong, with roughly 4,800–5,000 contribution events annually (including commits, pull requests, issues, and reviews), averaging around 400 activity events per month. The project maintains healthy delivery cycles, with a median merge lead time of about 6 days and an average issue resolution time of approximately 39 days.

At the same time, there has been a 50% decrease in commits and a 58.2% decrease in PRs compared to the previous [year](https://insights.linuxfoundation.org/project/open-enterprise-agent/development?timeRange=past365days&start=2025-01-01&end=2026-01-01). This indicator is related to the restructuring of the Atala Tribe at the end of 2024 and its transformation into the Identus Team, and to the fact that part of the focus shifted to integrating the Identus Platform into the Lace Wallet (the Lace Wallet repositories are not listed under the LFDT umbrella).

Contribution patterns remain concentrated, however: the top three individual contributors account for roughly 55% of total activity, and two organizations contribute about 62% of all contributions. Improving reviewer capacity and broadening organizational participation, therefore, remain important focus areas for long-term sustainability.

Security/compliance: the team kicked off work on the **OpenSSF Best Practices** and **Scorecard**; status is tracked at [ssf.identus.work](https://ssf.identus.work/).

Infrastructure: ongoing optimizations are in flight. **Neoprism** is being positioned to replace `prism-node` and the default Cardano infrastructure; it is more efficient and configurable (see [repo](https://github.com/hyperledger-identus/neoprism) and [docs](https://hyperledger-identus.github.io/neoprism/)).

Community engagement is healthy across the LFDT Discord, weekly maintainer calls, and GitHub discussions. Workshops such as RareEvo 2025 (offline-first + Lace wallet demo) and ongoing roadmap discussions continue to attract external participation. Repository migration is complete, improving transparency and aligning metrics. The [video](https://www.youtube.com/watch?v=vlBsXzNqvDc) of the workshop is publicly available on YouTube.

## Maintainer Diversity

There are **10 maintainers** across IOG and external partners (Socious, CSign, Blocktrust, Trust0); the **number of companies and maintainers is unchanged** year over year. The MAINTAINERS.md file is current in the [Identus repo](https://github.com/hyperledger/identus/blob/main/MAINTAINERS.md); the [`identus-maintainers` team](https://github.com/hyperledger/governance/blob/main/access-control.yaml#L625-L655) reflects the same roster. Diversity is improving, but IOG still provides the majority of maintainer capacity, so onboarding additional reviewers is an explicit objective.

## Project Adoption

Identus is in production or advanced pilots with:
- [Socious.io](https://socious.io/) (production)
- [Blocktrust](https://blocktrust.dev/) (identity wallet)
- [csign.io](https://csign.io/) (contributor and adopter)

Adoption momentum is reinforced by offline-first SDK work, issuance support now live in SDK-TS and SDK-Swift, stabilization of **SDK-KMP** (feature parity nearing completion), and early React Native enablement via the Kotlin rewrite and Apollo downgrade. The team is actively adapting Identus components for React Native applications, integrating SSI capabilities into the **Lace** wallet, and continuing Midnight alignment, which should broaden Cardano ecosystem usage.

## Goals

### Performance Against Prior Goals

Roadmap board: [Identus Roadmap](https://github.com/orgs/hyperledger-identus/projects/2)

Key outcomes delivered in 2025:
- Shipped platform releases **v2.15** and **v2.16**, bringing issuance to SDK-TS/Swift, offline-first improvements, and an Ed25519 fix for revocation lists.
- Advanced **Neoprism** as the successor to `prism-node`; Cardano VDR milestones 3–4 are underway with `prism-node` deprecation targeted within six months.
- Added the **DID Prism AnonCreds** method for schema/credential-definition resolution.
- Refactored Cloud-Agent, Mediator, and SDKs for better error handling, message queuing, and Problem Report support.
- Ran a documentation audit, refreshed Quick Start and tutorials, and aligned docs with the 2025 releases.
- Drove community engagement through Discord, weekly maintainer calls, GitHub discussions, and the RareEvo 2025 workshop.
- Completed the **VDR Catalyst Project**, introducing the VDR driver and API to the Identus platform (final stage wraps in **February 2026**). More details: [Project Catalyst VDR](https://projectcatalyst.io/funds/13/cardano-open-developers/verifiable-data-registry-for-identus-in-cardano).
- Stabilized **SDK-KMP**, moving it toward feature parity with other SDKs.

### Next Year's Goals (2026)

- Finish platform simplification: replace `prism-node` with **Neoprism**, close remaining Cardano VDR milestones (final Catalyst stage completes **February 2026**), and complete offline-first parity across SDKs (including the Kotlin rewrite).
- Harden developer experience: unify issuance guidance, expand tutorials, and deliver React/React Native support as SDK-KMP parity lands.
- Broaden interoperability: ship **OID4VCI/OID4VP/SIOP 2.0**, **VCDM 2.0**, **mDoc**, and **OpenBadges 3.0** support; continue exploring JSON-LD VC support.
- Security and compliance: complete **OpenSSF Best Practices** and **Scorecard** badges (target **Q1 2026**) and feed findings into CI/CD and dependency hygiene.
- Community & programs: grow the maintainer/reviewer pool, run **1–2 LFDT workshops** to promote Identus, and continue collaboration with Aries/CREDEBL.
- Developer enablement: deliver a **unified environment setup** suitable for workshops, development, and as a production reference deployment.
- Adoption: continue **Lace wallet** integration and broader React Native enablement.
- Governance: prepare to **apply for project incubation in Q3 2026** in line with the LFDT incubation exit criteria.

### Help Required

No TAC help requested at this time; the team is already coordinating directly with LFDT community managers.

## Project Lifecycle Status Recommendation

Identus remains an incubating project in the LF Decentralized Trust ecosystem and should stay in **Incubation** while maintainer diversity and OpenSSF compliance mature.

---

## Identus Annual Review 2026 Notes from the TAC

__TAC Reviewers__: Enrique Lacal (primary), VRamakrishna (secondary)

### Project Health

- Pleased to see the project's completed transition to the Hyperledger Identus GitHub organization. This move improves transparency, enables proper LFX Insights tracking, and aligns the project more clearly within the LFDT ecosystem. All of which were recommendations from the 2025 TAC review.
- The project continues to demonstrate consistent development activity with 37 active contributors, approximately 51% quarterly contributor retention, and development recorded on 313 of the last 365 days. Median merge lead time of around 6 days and an average issue resolution time of approximately 39 days reflect a well-maintained codebase.
- A notable concern is the 50% decrease in commits and 58.2% decrease in PRs compared to the prior year. The maintainers have attributed this to two factors: a reduction in the size of the maintainer team following the Atala Team restructuring at the end of 2024, and a portion of the team's focus shifting to work in repositories outside the LFDT umbrella. While the explanation is reasonable, this trend should be closely monitored over the next review cycle.
- Contribution remains concentrated: the top three individual contributors account for roughly 55% of total activity, and two organizations account for approximately 62% of all contributions. Broadening organizational participation remains an important area of focus for long-term project sustainability.
- It is encouraging to see that the team has done a lot of work on **OpenSSF Best Practices** and **Scorecard** compliance, tracking progress at [ssf.identus.work](https://ssf.identus.work/). This was a recommendation from the 2025 TAC review and the project has made a great effort.
- The advancement of **Neoprism** as a more efficient and configurable successor to `prism-node` is a positive infrastructure development that should reduce operational complexity going forward.

### Progress and Releases

Overall, the project has made good progress against its 2025 goals. Mapping deliverables against each original strategic goal:

- **Reduce maintenance cost and complexity**: The advancement of **Neoprism** as a more efficient successor to `prism-node` is the primary vehicle here. The project self-assesses approximately 80% completion on this strategic goal, which is reasonable given the ongoing Cardano VDR milestones.
- **Increase platform adoption**: **Platform releases v2.15 and v2.16** delivered issuance capabilities to SDK-TS and SDK-Swift, and **SDK-KMP** is approaching feature parity. The **Cardano VDR** (via the VDR Catalyst Project) was completed, introducing the VDR driver and API to the platform. The **DID Prism AnonCreds** method for schema and credential-definition resolution was also added.
- **Improve platform interoperability**: The **Cardano VDR** work directly addresses this goal. However, **OID4VCI/OID4VP/SIOP 2.0** and **Authentication using the PRISM DID method** were not delivered and have been carried into 2026. The **Pollux Plugin** abstraction was similarly not completed. These are the most significant outstanding items from the 2025 plan and should remain a priority.
- **Improve documentation and tutorials**: Documentation was refreshed with an updated Quick Start guide and tutorials, and a community workshop (RareEvo 2025) was run. This goal is largely met, with ongoing improvements expected.

The carryovers (OID4VCI/OID4VP/SIOP 2.0, Authentication with PRISM DID, Pollux Plugin) are noted without major concern given the overall scope of work undertaken.

#### View on 2026 Goals

We view the 2026 goals positively overall. The direction is right with large pieces via Neoprism, broader SDK parity, interoperability improvements, and a graduation application as something to look to. Making sure the above concerns on maintainer diversity and project health are met before the graduation application will be key.

That said, the 2026 goal list carries a significant amount of work that was originally planned for 2025 (OID4VCI/OID4VP/SIOP 2.0, Authentication with PRISM DID, Pollux Plugin). Combined with an already ambitious set of new goals (VCDM 2.0, mDoc, OpenBadges 3.0, React Native enablement, OpenSSF completion, and a graduation application), the scope is substantial. We encourages the project to be deliberate about prioritization and to set realistic expectations with the community about what will be delivered versus what may slip. A graduation application in Q3 2026 is a welcomed goal, but it will require the compliance items particularly maintainer diversity and following the project lifecycle documents to include things such as the ADOPTERS.md.

### Compliance with Hyperledger Project Lifecycle Criteria

- **OpenSSF Best Practices and Scorecard badges**: great work has been done and just needs the badges added to the main repository following the guidance in the [repository structure](https://github.com/LF-Decentralized-Trust/governance/blob/main/tac/governing-documents/repository-structure.md#required-content-in-home-page) and [project lifecycle](https://github.com/LF-Decentralized-Trust/governance/blob/main/tac/governing-documents/project-lifecycle.md#links) governing documents. 
- **MAINTAINERS.md**: current and up to date.
- **ADOPTERS.md**: not yet created. This was raised during the PR review and the maintainers have committed to creating it. It should be added to the main Identus repository.
- **Roadmap**: a public GitHub Projects board exists and provides a clear view of the project's priorities and progress.

### Recommendations

- **Create an ADOPTERS.md file** in the main Identus repository, as discussed in the PR. This improves transparency and is a governance best practice.
- **Monitor the commit and PR trend** over the next two quarters. If the downward trend does not stabilize or reverse, the project should actively work to diversify its contributor base to ensure long-term sustainability.
- **Grow the maintainer and reviewer pool** by setting a concrete goal to increase the number of active reviewers from organizations beyond the current primary contributors.
- Given all of the above, the project should **remain in Incubation** status. 
