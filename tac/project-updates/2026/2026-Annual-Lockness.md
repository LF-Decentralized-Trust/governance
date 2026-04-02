[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Annual Review Lockness

## Project Health

[![LFX Health Score](https://insights.linuxfoundation.org/api/badge/health-score?project=lockness)](https://insights.linuxfoundation.org/project/lockness/repository/lfdt-lockness)

## Maintainer Diversity

We currently have two maintainers: [@survived] and [@maurges] from Dfns. Maintainers did not change since the last year.

Maintainers file per projects:
* CGGMP21: https://github.com/LFDT-Lockness/cggmp21/blob/m/MAINTAINERS.md
* givre: https://github.com/LFDT-Lockness/givre/blob/m/MAINTAINERS.md
* round-based: https://github.com/LFDT-Lockness/round-based/blob/m/MAINTAINERS.md
* etc.

[@survived]: https://github.com/survived
[@maurges]: https://github.com/maurges

## Project Adoption

Our projects are widely adopted, with people from over 40 companies starring our repositories and engaging with us via support channels and social media. However, we choose not to maintain the adopters file as accurately tracking adoption is inherently difficult and prone to misrepresentation.

## Goals

### Performance Against Prior Goals

In the last year we delivered 34 releases across all the libraries. Notably, we did a big update in [CGGMP crate](https://github.com/LFDT-Lockness/cggmp21), aligning the implementation with the latest changes in the paper and fixing [disclosed vulnerabilities](https://www.dfns.co/article/cggmp21-vulnerabilities-patched-and-explained). Besides, we were working on improving the [`round-based` framework](https://github.com/LFDT-Lockness/round-based) for MPC protocols, the new version is more ergonomic and has more features.

### Next Year's Goals

Next year goal is to increase our engagement with the community, keep up with the maintainance duties, and deliver new projects into the Lockness ecosystem.

- Increase our engagement with the community
  - Host community calls quarterly
  - Participate in the mentorship program
    - We have already [proposed 3 projects](https://github.com/LF-Decentralized-Trust-Mentorships/mentorship-program/issues) to the program, and we may propose more
    - If we get accepted, we consider hosting multiple calls to give an introduction into MPC cryptography for the mentees, which may be also interesting for general audience.
- Maintain and improve existing projects
- Develop a NIST-compatible Threshold Post-Quantum Signing protocol

### Help Required

We may need help to organize community calls & workshops mentioned above.

## Project Lifecycle Status Recommendation

We suggest to keep the project in Incubation.

---

## Lockness Annual Review 2026 Notes from the TAC

**TAC Reviewers**: Matthew Whitehead (primary), Hendrik Ebbers (secondary)

### Project Health

- The project has a very small developer base but appears to be in active development.
- The libraries seem to have a reasonable number of users and deployments
- As a security-related project it is good to see that CVEs/vulnerability disclosures are being publicly reported under the Github security section.
- The LFDT stats are generally positive, with the obvious outlier being the dependency on such a small number of contributors
- It is really positive to see that mentorship projects have been submitted by the maintainers

### Progress and Releases

It appears there has been a lot of development across the most of the repos within the project. The annual review lists 34 releases which is extremely positive. The major update of CGGMP appears to have been a lot of the development time, but it is also very positive to see that disclosed vulnerabilies being called out as areas of improvement during the course of the year.

#### View on 2026 Goals

The reviewers fully support the aims of growing the community and hopefully the mentorship projects can help with that.

One aim the maintainers should consider including on their 2026 goals is to enable the OpenSSF scorecard and address any issues it highlights, especially those that don't meet the current LFDT project requirements for incubating projects. This aim was mentioned in the Q4 2025 report and it would be good to see it actioned this year, which the lowest scores being addressed as quickly as possible.

### Compliance with Hyperledger Project Lifecycle Criteria

- There is a SECURITY.md in all of the repos
- There is currently no OpenSSF scorecard for any of the repos I checked. This should be enabled and any very low scores addressed
- The SLSA guidelines for incubating projects are [here](https://github.com/LF-Decentralized-Trust/governance/blob/main/tac/guidelines/slsa-guidelines.md) and level 1 should be achieved as an incubating project
- The LFDT encourages release notes for releases but it doesn't appear that all of the repos have them. Some, such as `fast-paillier` have a `CHANGELOG.md` file, others such as `cggmp21`, `round-based` and `givre` don't have a change log file or GH releases. There have been efforts to encourage consistency where possible across LFDT projects so the reviewers encourage the project maintainers to consider whether GH releases could be used in the future to help users understand the release cadence, release notes and contents/fixes/CVEs etc.

### Recommendations

The TAC agrees with the proposal to remain in `incubating` state, and also with the majority of the goals. We would strongly encourage some work to meet the LFDT's requirements for repos as outlined above.
