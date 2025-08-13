[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2025 Annual Review Hiero

## Project Health

The LFX Insights page of Hiero can be found [here](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=hiero)

The Hiero project began in September 2024 and has been growing ever since.
Along with the transition of all Hedera repositories that are needed to run a network, we added  other community driven repositories.
While developing those projects, we were able to onboard new contributors to Hiero and new maintainers coming from the community.

Next to transitioning the repositories, we are setting up an open governance model for the project.
We kickstarted several public meetings that run on a weekly basis where we discuss the project and its plans for the future.

All repositories within the Hiero organization are regularly updated and actively maintained by the project maintainers.

## Maintainer Diversity

Building a diverse community is always a challenge, particularly in the early stages of a new project. Our community is made up of both maintainers and contributors from a range of backgrounds, including individuals from various companies as well as independent contributors.

We are proud to include a growing number of new committers and maintainers, as reflected in the contributor list of [hiero-solo-action](https://github.com/hiero-ledger/hiero-solo-action), a community-driven project that has successfully attracted contributors from regions such as India and Africa.

Another great example of community engagement is the [YouTube tutorial series for our Python SDK](https://www.youtube.com/playlist?list=PL6uVtTx-oqY8V-HBfenONJrsA0Z8xJymX), created independently by one of our community members.

The team remains committed to expanding the project’s reach and engaging with broader communities. Recently, the maintainers hosted a Hiero booth at events such as HederaCon and ETHDenver, with plans to participate in upcoming conferences like Rare Evo. We continue to seek opportunities to present the project to wider audiences and foster meaningful connections across the ecosystem.

The project’s current call for nominations to the Technical Steering Committee (TSC) is another step toward encouraging broader participation from companies and organizations, helping to further strengthen and grow the community.

## Project Adoption

The project announced the upcoming elections for two vital positions on the Hiero Technical Steering Committee (TSC): the End User Seat and the Contributor Seat.
These roles are instrumental in guiding the technical direction and ensuring the diverse representation of our community within the Hiero project.

This election will be held on May 7th until May 31st, 2025.

At the moment, we continue to welcome and encorage nominations.

Our current nominees can be viewed [here](https://github.com/hiero-ledger/governance/tree/main/elections/nominees/mar-2025-election)

## Goals

### Performance Against Prior Goals

Our initial target was to move all Hedera repositories to Hiero.
While we've mostly finished this transition, we've initiated the process of refactoring the code to a more vendor-agnostic and unbranded architecture.
Our main focus is our SDKs in addition to discussing workflows, roadmaps, and patterns.
Information and current state on the transition from Hedera can be found [here](https://github.com/hiero-ledger/hiero/blob/main/transition.md).
Information about our work on making the SDKs vendor neutral can be found [here](https://github.com/hiero-ledger/hiero/blob/main/blog/2025-03-17-sdk-workflows.md).

With all of this work in progress, we plan to release the initial minor versions of all projects in the near future.
Next, we plan a major release that will contain all the work from moving the code to a more vendor neutral release.

Another main goal is the onboarding of community projects from the Hiero ecosystem.
At the moment, we moved 3 community projects to Hiero and a new proposal is in the pipeline.
Information about the onboarding of new projects can be found [here](https://github.com/hiero-ledger/hiero/blob/main/community-transition.md).

On the project's management front, the team is focusing on evaluating and analyzing key project health metrics that track our progress in fostering a thriving and diverse community.
These metrics enable us to assess the project's performance by measuring contributions, code velocity, and issue response and resolution times.

In hiero-ledger we rely on meassuring tools like LFX Insights, Bitergia and GitHub Insights. With the help of Bitergia, we are able to visualize in detail the contributions data for all the work that happened by the Hedera team before September 2024 (which is when the projects started transitioning to Hiero in hiero-ledger GitHub Organization). LFX Insights helps us confirm the contribution statistics for the work that is happening as we continue to move forward in the projects. Other statistics like GH Insights helps us confirm the data in a specific repository at a time whenever we need to direct focus to a particular component. Leveraging all these metrics tools helps us staying accurate and caught up with the fast pace at which the repos continue to transition into https://github.com/hiero-ledger/.
Our metrics report can be found [here](https://docs.google.com/document/d/e/2PACX-1vRxg-3wU-eg0EWEhAu9SRab_sXwJBy5YDQqoeV6BLq0FnVnoO4V41kPYEDYJovtns6tpq9gkaSaSzlO/pub).

### Next Year's Goals

Hiero is a rapidly growing project that is gaining significant traction. We anticipate continued growth in our community's diversity, enabling the adoption of more community-driven components.

The project is expected:

- **Grow their TSC** - Following the recent elections, we anticipate increased participation from members of the Technical Steering Committee (TSC). This growth will enable more companies to take an active role in shaping the project and contribute to the continued expansion of our community.
- **Grow their maintainers and committers** - We are actively encouraging participation from new contributors and raising awareness among current maintainers and committers to review their contributions in accordance with our project guidelines. The goal is to identify and nominate qualified individuals for committer roles. Simultaneously, we are supporting projects in assessing their current resources to identify opportunities for promoting existing committers to maintainer roles, aligned with the newly established criteria.
- **Recruit more participating companies** - As we continue to analyze our contributor metrics, we remain committed to promoting Hiero through events, seminars, and forums to enhance the project's visibility. Our goal is to attract interest from a broader range of companies willing to participate and contribute to the project's objectives. Through these efforts, we aim to increase both the diversity and reach of our community.

Our vendor-neutral releases will provide the project with enhanced flexibility and adaptability, supporting its long-term success.

As a project, we anticipate continued progress in the following areas for Hiero:

- **Reliability** - We remain committed to continue growing our community engagement by encouraging contributions to support both our current and upcoming SDKs, as well as helping to build a more comprehensive Technology Compatibility Kits (TCKs) with richer test coverage to ensure robust end-to-end validation of our software implementation in our SDKs. We continue to review and adhere to our security policies, staying informed about potential threats and vulnerabilities that need to be addressed in our codebase. Additionally, we promote active participation in our security efforts by offering bounty opportunities to encourage contributions in this critical area.
- **Scalability** - The team continuously evaluates opportunities for collaboration with other LFDT projects. We remain actively informed about the focus areas of these projects to identify potential synergies where Hiero can contribute and collaborate effectively. At the same time, we are focused on acquiring new adopters, end users and chair members.
- **Performance** - Additionally, we are focused on achieving faster finality, lower latency, and continuously increasing capacity to support larger transactions. As we conclude our project transition phase into hiero-ledger, the team's focus will shift towards supporting the development of new and improved releases for each component.

## Project Lifecycle Status Recommendation

The project continues to work towards the goals set by the TAC in order for the project to move to Graduated state.

- **Legal Criteria** - The project has established a dedicated security team tasked with monitoring the latest security reports and implementing OpenSSF best practices, with the goal of achieving a score of 10.
- **Diversity Criteria** - As we continue to aquire new contributors, we are hoping that their contributions continue to be meaningful enough to be elected as Committers and Maintainers. The team is offering guidance on the project development front and promoting active collaboration in order to qualify as Committers or Maintainers of the project.
- **Releases** - All code repos in Hiero have at least 2 or more minor releases. We are working towards developing a vendor neutral first major release that will be easily adoptable, flexible and independent.
- **Testing and Q/A** - Along with projects transitioning into hiero-ledger, the team is focused on strengtening the CI workflows that cover unit and integration tests with other project components. These tests are being monitored and adapted to project changes as we move towards a vendor neutrality state.
- **Structure** - As new projects move into hiero-ledger, we continue to review them in LFX Insights to make sure their best practices are reflected in the project's performance.
- **Maintenance** - The team continues to remain active. We have initiated new component dedicated bi-weekly calls with the maintainers of each component where new features and future work is being discussed. In discord, we are promoting more collaboration and inclusion of new members.
- **Production** - We are working on our project's Adopters file for each hiero-ledger repo.
- **Documentation** - docs.hiero.org is live and currently maintained under the hiero-docs repo in GitHub. This site contains extended technical information on hiero-ledger's components and guided instruction on how to locally run the project.
