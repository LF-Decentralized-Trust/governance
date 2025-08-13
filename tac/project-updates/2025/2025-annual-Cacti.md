[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2025 Annual Review Cacti

## Project Health

Overall the project is in good health, chugging along and growing the maintainers as we speak. 
The highlight here is that in the Spring of 2024 we've added the wonderful [Rafael Belchior](https://github.com/RafaelAPB) to our ranks and he's been doing an excellent job of advancing our Typescript reference implementation for the IETF's Secure Asset Transfer Protocol (SATP).

[LFX Insights Page for Cacti](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=cacti&routedFrom=Github&bestPractice=false&repository=all&dateFilters=Last%20Year&dateRange=2024-01-01%20to%202024-12-31&compare=PP&granularity=month&hideBots=true)

1. Best Practices Score: The governance repo that we now have received poor scores overall and the average of the two gets shown on the main page. The governance repo itself is a templated repository that doesn't contain production code (or any code for that matter) so ideally those numbers would be excluded from the calculations. Even without the governance repo's scores in the mix, we wouldn't have a perfect score, but the picture would look much more rosy than the initial glance lets the user believe. One more thing that we've struggled with is that when attempting to run a FOSSA scan on the Cacti repository, it crashes with an out-of-memory error on a machine that has 48GB RAM so the size of the mono-repo is making it a bit of a challenge to execute the scans but we are working on solutions for this as well.
2. Contributor growth has slowed a little bit, partially due to the maintainers having much less time last year to host LFX mentorship projects which is always a steady stream of new contributors for us.
3. Pull requests are still up compared to the previous year as we are relentlessly pursuing our goals in the codebase.

[OpenSSF Scorecard Page](https://scorecard.dev/viewer/?uri=github.com/hyperledger-cacti/cacti)

- The 6.3 score is less than ideal on scorecard, but we are still in the process of figuring out how to tell scorecard about certain things such as our fuzzer (Nuclei DAST) which the report says we do not have. 
- Another false-negative in scorecard is the old CII-Best-Practices badge which we do have, but it might've gotten lost in translation at the time when we moved to the new GitHub org from `hyperledger/cacti` to `hyperledger-cacti/cacti`.

## Maintainer Diversity

- We have **8 maintainers** at present from 4 different organizations: Fujitsu, IBM, Tecnico Lisboa, Accenture.
- The number of active maintainers has **increased** from 7 to 8.
- The number of maintaining organizations has **increased** from 3 to 4.

Current [MAINTAINERS.md](https://github.com/hyperledger-cacti/cacti/blob/36959b326f8a4c08c99fe2bf87b00c7996d49edd/MAINTAINERS.md)
and previous (Jan 1st, 2024) [MAINTAINERS.md](https://github.com/hyperledger-cacti/cacti/blob/1fb2551a055daf202d2def0fcb3de990a44cfb03/MAINTAINERS.md)

## Project Adoption

The detailed answer about adoption has been published earlier and can be read through this link: https://github.com/LF-Decentralized-Trust/project-proposals/blob/gh-pages/proposals/graduated/cacti.md#real-world-use

## Goals

### Performance Against Prior Goals

The main theme is to carry on with the integration work with our multi-phase plan:

> Packaging as a monorepo,

Great success here! With the introduction of our new bundler (`npm:@vercel/ncc`) we now have the capability to bundle
any package within the monorepo that has application characteristics (e.g. anything that's runnable instead of designed
to be imported as a library only) along with it's mono-repo dependencies into a single executable file. This helps
tremendously with container sizes and container build times for the `cmd-api-server` package for example and the IETF SATP
gateway package recently started using it as well.

> Eliminating and merging redundant packages,
> Finally consolidating packages as per our target architecture (this may be too ambitious for 2024, given other priorities in the roadmap).

Semi-success. We have a long way to with this task still, but much progress has been achieved.
Our excellent mentee Jennifer has done an outstanding job of bringing it all together through the new COPM module which 
was also recently presented at an LFDT meetup.
This package increases re-use by enabling certain Weaver components to be used from other non-weaver packages.

> Adding more plugins for other forms of DLTs and also legacy/centralized systems that need to trade assets.

Great success! The daily pair programming sessions shined on this one! Peter and Cheesecake Labs' Fifo have worked together on
the Stellar connector which was then also presented at a conference by Cheesecake Labs.
https://github.com/hyperledger-cacti/cacti/pull/3296
https://github.com/hyperledger-cacti/cacti/pull/3274

> Issuance of the much anticipated v2.0.0 final/GA/etc. release in Q1 or Q2 the latest!

We've successfully released v2.0.0 and v2.1.0 in the meantime. 
Artifact publishing is on hold at the moment due to the migration effort from the old org to the new org.


### Next Year's Goals

1. Have the Typescript reference implementation of the IETF Secure Asset Transfer Protocol (SATP) and helping production project with a dedicated discord channel and support.
2. Increase our security posture when it comes to the OpenSSF and LFX scores (a lot of this is just figuring out how to tell the tools about what we already have)
3. Bring down our average pull request merge time. This was one of the earlier year's goals as well and we have made significant progress on it a couple of years ago but recently there's been a bit of a relapse on this metric so it's worth putting it down as a goal again.
4. Finish migrating the release automation to the new repository.
5. About 80% of all requests will be handled within 3 days.
6. Attempt to work together with the verifiable credentials community within the LFDT to explore more use-cases that could be of interest to our prospective users.


### Help Required

As always, we'll grab any chance we can get to promote the project so if there's an opportunity to do so please keep us in mind. :-)

## Project Lifecycle Status Recommendation

`Graduated`
