---
layout: default
title: 2025 Q3 Hyperledger Indy
parent: 2025
grand_parent: Project Updates
---


# Project Health

Over the past quarter, the Indy community continued working on upgrading components to support Ubuntu 22.04. The project remains highly stable, with globally deployed networks running smoothly and ongoing efforts focused on long-term maintainability and security improvements.

# Questions/Issues for the TAC

There are no questions or issues at this time.

# Releases

The current focus is the Ubuntu 22.04 upgrade, so there have been no releases in this past quarter.

Most recent prior release:
- [indy-node v1.31.2](https://github.com/hyperledger/indy-node/releases/tag/v1.13.2)
- [indy-plenum v1.31.1](https://github.com/hyperledger/indy-plenum/releases/tag/v1.13.1)

# Overall Activity in the Past Quarter

The primary focus of the current technical work is upgrading Hyperledger Indy components to support Ubuntu 22.04.

Unfortunately, since new contributors working on the upgrade were abruptly pulled from the project, momentum has slowed compared with the previous quarter. It had appeared that they would be able to return to the project, but there have not been additional updates on a potential return.
Current maintainers are planning to increase contributions in the next quarter to move the upgrade forward. We also plan to seek contributions from those maintaining production use cases.

There has also been development on Indy on Besu over the past quarter. This is a good MVP, but there is not yet a final release. There has been development on the revocation feature, and a group with the Brazil government is moving towards production with Indy on Besu.

There has been some community activity on the Discord server. Maintainers respond promptly and consistently. We have continued to hold synchronous biweekly meetings.

Key areas of work include:
- Updating CI/CD workflows to support Ubuntu 22.04
- Upgrading indy-test-automation to support Ubuntu 22.04
- Indy VDR upgrade for Plenum
    - Progressing unit test pass rates
    - Next step will be to build a new release of Plenum
- Indy VDR upgrade for Node following the upgrade in Plenum.

The GitHub organization transition is planned for after the removal of obsolete dependencies.

Hyperledger Indy remains a highly stable project. As a result of this stability, there are numerous scaled deployments of Indy networks operating reliably across the globe. Demand for new features in the existing Indy Node and Plenum codebases is low, reflecting the maturity and robustness of the platform. Efforts are ongoing to maintain and strengthen this level of stability, ensuring that production-grade Indy networks continue to serve critical identity infrastructure needs worldwide.

# Current Plans

- Complete the upgrade to Ubuntu 22.04
- Complete the GitHub organization change
- Increase OpenSSF Scorecard rating
    - Ensure that individual releases are signed
    - Implement token permissions model
    - Introduce tooling for pinned dependencies (use dependabot report tooling), fuzzing, and SAST
    - Ensure that OpenSSF detects branch protections and packaging practices
    - Add code quality checking for project commits
    - Reformat code base
    - Add poetry package management


# Maintainer Diversity

There are currently 14 maintainers. The maintainers and teams can be seen in the [Governance Access Control YAML file](https://github.com/hyperledger/governance/blob/main/access-control.yaml).


# Contributor Diversity

https://insights.linuxfoundation.org/project/indy?timeRange=past365days&start=2024-07-29&end=2025-07-29
- 12 active contributors in the last quarter


# Additional Information

Indy continues to be a stable project that provides an important utility layer to real-world use cases. Indy is in production in the United States, Canada, Japan, the Caribbean, and South Africa, with others in pilots headed to production around the world.