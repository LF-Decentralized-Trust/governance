[//]: # "SPDX-License-Identifier: CC-BY-4.0"

# 2026 Annual Review Paladin

## Project Health

Paladin is a platform for programmable, privacy-preserving tokens on EVM.

We have had a busy few months since migrating from a lab to an incubating project:

- 164 PRs raised and merged
- 3 releases (`0.14`-`0.16`)
- Monthly contributor calls
  - We're currently using the GH Wiki approach to track calls & agendas (https://github.com/LFDT-Paladin/paladin/wiki/Community-calls)

A lot of the active work has been on a pre-release branch towards the V1 release, called [v1-develop](https://github.com/LFDT-Paladin/paladin/tree/v1-develop). This branch has had the majority of commits in the past 6 months and is where the main new function (distributed sequencing, new V1 version of the Noto domain, increased component test coverage etc.).

This branch will continue to be developed as we work towards the V1 release of Paladin in 2026.

### OpenSSF Scorecard

Writing this report highlighted that our OpenSSF scorecard setup had not yet been merged (https://github.com/LFDT-Paladin/paladin/pull/909). This has now been rectified so scorecard results can be included in future reports.

### LFX Insights (summary)

The LFX insights for Paladin can be found here: https://insights.linuxfoundation.org/project/paladin?timeRange=past365days&start=2025-04-01&end=2026-04-01

The project has good scores for most metrics and is currently classed as **Healthy**.

## Maintainer Diversity

There are currently **6** active maintainers on the main project, with **5** maintainers on the Zeto project. Currently all maintainers are from Kaleido so over time we will work towards having contributors from a more diverse set of organisations.

## Project Adoption

Paladin has a number of wide-reaching proof-of-concepts taking place across financial institutions. A number of users on discord have been engaging to understand how best to use Paladin for their use-cases and to understand the technology better. Over time we hope to have specific public use-cases to include in the adopters file.

## Goals

### Performance Against Prior Goals

As a relatively new LFDT incubating project, migrated from lab to project in 4Q 2025 Paladin does not have a previous list of specific goals to compare against.

The main aims of the project in the time since have been:

- To meet all of the incubating project requirements
- To release periodically reflecting the active ongoing development
- To work towards a V1 release as an evolution of the existing releases
- To work on substantial new function as part of the V1 release, including:
  - A new decentralized sequencing engine for assembling transactions efficiently ahead of the blockchain
  - Production enhancements such as logging, metrics, and PD.

These have all been delivered more or less in line with our original intentions. The goals for next year are outlined in the next section.

### Next Year’s Goals (2026)

1. Ship a V1 beta release (1-2Q)
2. Ship V1 with the new distributed sequencing engine and related enhancements over `0.x`
3. Meet any new or remaining LFDT project requirements
4. Grow the list of cases in `ADOPTERS.md` to help potential users understand Paladin's use-cases
5. Integrate the output of the Java SDK mentor programme as a first class part of the project

### Help Required

No specific help required at this time. We have proposed (and had accepted) a mentoring project for the development of a Java SDK which we will report on in next year's review.

## Project Lifecycle Stage Recommendation

**Incubating**

Paladin has only recently graduated to incubating status. The project is moving forward at a rapid pace and has good maturity of docs, process etc. but should remain incubating at the present time.
