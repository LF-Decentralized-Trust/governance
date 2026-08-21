[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Mid-Year Review of Hyperledger Cacti

## Progress Against 2026 Goals

### 1. Prioritize Project Cleanup and High-Demand Packages

The [cleanup initiative](https://github.com/orgs/hyperledger-cacti/projects/2) has been the single largest workstream of the first half of 2026. Since 24 November 2025 through 4 August 2026, the team has accomplished:

- Archived unmaintained packages.
- Moved test packages and examples to the new [cacti-demos](https://github.com/hyperledger-cacti/cacti-demos) repository, resulting in a leaner core codebase.
- Fixed critical security vulnerabilities identified during the review process.
- Reviewed all project issues (~around 350). As a result we closed 77 outdated issues. We recently re-reviewed the ~127 open issues, significantly cleaning up and reducing the backlog.
- All PRs were reviewed. Stale PRs were revised and incorporated or closed: we merged approximately 80 pull requests, achieving an average time-to-merge of 16 days. We currently have less than 20 PRs opened.
- Improved CI/CD pipelines — fixed lint, build, and test failures across the repository; significantly reduced GitHub Actions costs; and created a CD pipeline that automatically publishes npm packages and Docker images on release.

The next focus area within the cleanup initiative is a documentation revamp to make the project easier to navigate for new contributors and adopters.

### 2. Continue SATP Implementations Aligned with IETF

SATP-Hermes development has continued steadily (you may consult the public [SATP project board](https://github.com/orgs/hyperledger-cacti/projects/1/views/1)). The main focus in the first half of 2026 has been the addition of ERC6909 support to the SATP bridge, bug fixing, and stability improvements.

Maintainers continue to participate in the IETF SATP working group, keeping the implementation aligned with the draft standard as it progresses toward RFC status.


### 3. Improve OpenSSF and LFX Insights Scores

The security vulnerability fixes carried out as part of the cleanup initiative have produced a significant and measurable result: GitHub security alerts were reduced from ~4,000 down to ~400, with zero critical vulnerabilities remaining. We plan to continue addressing the security and OpenSSF score for the second half of 2026, aligned with the documentation revamp.

### 4. Fix Release Automation and Push v3+ Releases

A v3 beta release has been pushed, resolving the release-pipeline blockers identified in the 2026 Annual Review. After that, we released the first major release in many months, that brings substantial improvements to the project - [v3.0.0](https://github.com/hyperledger-cacti/cacti/releases/tag/v3.0.0).

### 5. Cactus-Weaver Integration

Progress here has been limited given the focus on cleanup and release automation. 

---

## Deliverables and Outputs (First Half of 2026)
[LFX Insights for the past half-year](https://insights.linuxfoundation.org/project/cacti/contributors?timeRange=past180days&start=2026-02-14&end=2026-08-13&widget=organization-dependency&auth=success)


| Deliverable | Details |
|---|---|
| [cacti v3 beta](https://github.com/hyperledger-cacti/cacti/releases?page=2#release-v3.0.0-beta.1) | v3 beta release |
| [cacti v3 release](https://github.com/hyperledger-cacti/cacti/releases/tag/v3.0.0) | Major release |
| [cacti-demos v1.0.0](https://github.com/hyperledger-cacti/cacti-demos/releases/tag/1.0.0) | Standalone demos and examples repository, separated from the core codebase |
| Security vulnerability fixes | Security alerts reduced from ~4,000 to ~400; zero critical vulnerabilities remaining |
| Cleanup initiative milestone | 77 issues closed, ~80 PRs merged, unmaintained packages archived |
| LFDT Mentorship | Mentee onboarded via [LFX Mentorship](https://mentorship.lfx.linuxfoundation.org/project/ab089edb-738d-4cdb-bbdb-e0ce2c17f57f) and contributing to cleanup and documentation ([project board](https://github.com/orgs/hyperledger-cacti/projects/3)) |

---

## Goals for the Second Half of 2026

- Ship v3.1.0 (or v3.0.1) release and continue release-automation improvements.
- Complete Cacti [documentation revamp](https://hyperledger-cacti.github.io/cacti/) — the next major milestone of the [cleanup initiative](https://github.com/orgs/hyperledger-cacti/projects/2), driven jointly by the LFDT mentorship and the core maintainer team.
- Expand [cacti-demos](https://github.com/hyperledger-cacti/cacti-demos) — consider adding more documentation, application examples, and integration showcases to lower the barrier for new adopters.
- Continue SATP-Hermes development in line with IETF draft updates, tracking the standard toward RFC status.
- Consider new DLT connectors — evaluate community demand and prioritise connectors that broaden Cacti's reach without conflicting with the depth-over-breadth strategy.
- Security and usability improvements: continue hardening the codebase, building on the alert reduction achieved in the first half, with an eye toward the next major or minor version milestone.
- Improve OpenSSF and LFX Insights scores, especially those impacting security.
- Carry out more Cactus-Weaver integration as time permits.
- LFDT Mentorship — support the mentee through to the end of the programme and land their contributions.

---

## Maintainer Diversity

The project counts with 5 maintainers:

| Name | GitHub | Chat | Institution |
|------|--------|------|------|
| Michal Bajer | [outSH] | bajerm | Fujitsu |
| Venkatraman Ramakrishna | [VRamakrishna] | vramaiitkgp | IBM |
| Sandeep Nishad | [sandeepnRES] | sandeepn | IBM |
| Rafael Belchior | [RafaelAPB] | rafaelapb | INESC-ID |
| André Augusto | [AndreAugusto11] | andreaugusto | INESC-ID |
| Carlos Amaro | [LordKubaya] | kubaya |INESC-ID |

---

## Help Required

We would appreciate TAC assistance in the following subjects:
1 - in finding and onboarding new maintainers. The project's contributor and organization concentration (2 contributors and 2 organizations accounting for the majority of contributions) is a known risk, and growing the maintainer base is a priority. The ongoing cleanup initiative and the documentation revamp are intentionally designed to be approachable entry points for new contributors who may grow into maintainers. Action step would be helping us with the project marketing, which we would be in a good position to reinforce after the v3 release.

2 - any support for AI tokens, e.g., Copilot subsription. Some maintainers are using their subscriptions out of pocket exclusively for the project. We are happy to explain how we are planning to use such tokens to advance the project (of course, aligned with our AI policy).

## Acknowledgments

We thank the LFDT staff for the continued support of Cacti and its community. We would like to thank in particular to Ry Jones, who made substantial contributions to our codebase in the last quarter. 


---

## Project Lifecycle Status Recommendation

Graduated

The project has maintained sufficient maintainer diversity, continued delivering against its roadmap, and is progressing through a significant quality-improvement cycle. Lifecycle status is unchanged.
