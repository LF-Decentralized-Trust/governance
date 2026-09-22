[//]: # "SPDX-License-Identifier: CC-BY-4.0"

# 2026 MidYear Review - Paladin

Paladin is a platform for programmable, privacy-preserving tokens on EVM.

This report covers the period since the [2026 annual review](2026-annual-paladin.md).

## Project Health

The headline for this period is the that V1.0 of Paladin was released in June. This was the result of a substantial effort over the first half of the year and included the new distributed sequencing engine, a key part of Paladin's long-term architecture requirements.

Summary of the period:

1. V1.0 released
2. Over 162 PRs merged
3. Monthly community calls being run and attended by a small but engaged group
4. LFDT Java SDK mentorship programme starts and well under way
5. New example plugin demonstrating a proof-of-technology for Railgun shielded token support
6. New versions of the Noto notarised token domain

Also in this period two of the lead maintainers attended the LFDT Privacy Workshop in London, running a live-demo of Paladin being used in a Cash/Bond DvP scenario.

### Areas of development since V1.0

Work has continued in a number of areas

- Refined of the distributed sequencing algorithm. Various edge cases, particularly around the design of the engine's state machines, have been worked through and the design iterated on
- Performance testing, specifically of Noto transfers with the intention to performance test other domains + domain combinations over the second half of the year
- Java SDK progress, which is on-track to complete by the end of the mentorship programme

### OpenSSF Scorecard

The OpenSSF Scorecard scanning action was merged in the first half and the current scorecard is available at https://scorecard.dev/viewer/?uri=github.com/LFDT-Paladin/paladin

As of 22nd September 2026 the repo scores **4.7** which is a slight improvement over the previous report. Areas we have specifically addressed:

- Adding a security.md (this was raised some time ago butn hand't been merged)
- Enabling dependabot on some of the code areas
- Updating branch protection rules to ensure higher branch protection standards

We'll continue to bump these scores iteratively over the coming 6 months.

### LFX Insights

The LFX insights for Paladin can be found here: https://insights.linuxfoundation.org/project/paladin?timeRange=past180days

The project currently has a score of 45/65.

We currently have a small-ish number of active maintainers, with 54% of contributions being from just 2 maintainers. The maintainer base is entirely from Kaleido currently, although it has been really positive having Divyam Jha contributing to the Java SDK for the past couple of months.

GitHub metrics as of 17th September 2026:

| Metric      | paladin | zeto |
| ----------- | ------- | ---- |
| Stars       | 87      | 39   |
| Forks       | 75      | 30   |
| Open issues | 72      | -    |
| Open PRs    | 54      | -    |

## Maintainer Diversity

There are currently 7 maintainers (see [MAINTAINERS.md](https://github.com/LFDT-Paladin/paladin/blob/main/MAINTAINERS.md)), with a slight split between the core Paladin project and the Zeto project (4 hold Zeto maintainer status). All current maintainers are from Kaleido, which remains an area for improvement over the coming year or two.

We have seen growth in the number of individual contributors. 10 have had commits merged to `main` since the previous review, 3 of whom aren't from Kaleido.

## Project Adoption

With Paladin V1.0 being available we are seeing strong interest in the project. Attendance of workshops such as the LFDT Privacy Workshop have helped demonstrate Paladin's suitability for real-world private tokens and smart contracts on permissioned and public EVM networks. While we don't yet have an adopters file there are several public projects that have used Paladin in financial settings.

For example see the Project Agorá project report https://www.bis.org/publications/project-agora-shared-programmable-platform-wholesale-cross-border-payments.pdf

The Railgun domain plugin is a new integration intended to demonstration Paladin's flexibility and technology-agnostic approach to privacy.

## Goals

### Performance Against Prior Goals

The 2026 goals from the annual review, and progress against them:

| #   | 2026 Goal                                                                                  | Status                                                                                                                                                |
| --- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Meet all of the OpenSSF requirements for incubating projects                               | **In progress.** Scorecard scanning is enabled and published. Score is currently 4.7                                                                  |
| 2   | Ship a V1 beta release (1-2Q)                                                              | **Done.** Release candidates `rc.8` - `rc.12` shipped between April and June 2026.                                                                    |
| 3   | Ship V1 with the new distributed sequencing engine and related enhancements over 0.x       | **Done.** V1.0 released June 2026.                                                                                                                    |
| 4   | Meet any new or remaining LFDT project requirements                                        | Slowly working on any remaining project requirements                                                                                                  |
| 5   | Grow the list of cases in `ADOPTERS.md`                                                    | **Not started.**                                                                                                                                      |
| 6   | Integrate the output of the Java SDK mentor programme as a first class part of the project | **In progress.** Mentorship started June 2026 working on the `java-sdk-main` side branch so far. Project is on track to complete in the alloted time. |

### Goals for the remainder of 2026

Paladin is working on a number of enhancements following the V1 release:

1. Designing a multi-tenant approach to hosting multiple discrete identities from the same Paladin wallet/node
2. Reducing the state bloat intrinsic in the current design of Pente domain states
3. Improving performance in a number of scenarios across different reference domains
4. Improve the OpenSSF scorecard
5. Merge the in-progress Java SDK into main and a new release

We are planning to pause the specific goal of adding an adopters file for the time being.

### Help Required

No help required at this time. The project would always benefit from more contributors in the Ethereum privacy space though.

## Project Lifecycle Stage Recommendation

Paladin is currently in **incubating** status. While there has been a first V1 release during 2026, the maintainer & org diversity is still somewhat limited and some of the OpenSSF etc. scores need improving to meet the requirements of graduated projects. Paladin itself is being actively used in industry-wide projects and the expectation of maintainers is that Paladin would migrate to **graduated** status in the next 1-2 years.
