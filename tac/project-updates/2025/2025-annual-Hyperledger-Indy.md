[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2025 Annual Review Hyperledger Indy

## Project Health

Reference: [Indy LFX Insights Page](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=indy&repository=&routedFrom=Github)

Hyperledger Indy is a very stable project. Because of this stability, there are a number of scaled deployments of Indy across the world. All are running smoothly, and there is little demand for new features in the existing Indy Node/Plenum code base.

A Hyperledger Mentorship project was completed and has produced an Indy Read Replica implementation that can be found [here](https://github.com/hyperledger/indy-read-replica).

An [Indy on Besu Article] was recently published which describes the progress being made towards the next generation of Hyperledger Indy.

[Indy on Besu Article]: https://www.lfdecentralizedtrust.org/blog/lf-decentralized-trusts-hyperledger-indy-on-besu-joins-the-didindy-method-six-months-of-progress

### OpenSSF Scorecard for key repositories:

Indy Node [![Indy Node](https://api.scorecard.dev/projects/github.com/hyperledger/indy-node/badge)](https://scorecard.dev/viewer/?uri=github.com/hyperledger/indy-node) Indy Plenum [![Indy Plenum](https://api.scorecard.dev/projects/github.com/hyperledger/indy-plenum/badge)](https://scorecard.dev/viewer/?uri=github.com/hyperledger/indy-plenum)

#### Notes on OpenSSF Scorecard Reports

While some of the current scores for the Hyperledger Indy project do not fully reflect the reality of our practices, we have identified key areas for improvement and have added relevant goals to our roadmap for the coming year. Below is a summary of the current status and our planned actions:

- Signed Releases:
    - The current score is 0 because packages are uploaded to a trusted Debian repository with a signing key, rather than releases being signed individually. We recognize the importance of this feature and have added it to our goals for the year.
- Branch Protection:
    - Branch protection is in place. However, the Scorecard does not currently detect this. We will investigate and address any configuration or tooling issues to ensure accurate recognition.

- Packaging:
    - Packaging is implemented, but this is also not being recognized by the Scorecard. We will review and resolve this discrepancy.

- Token Permissions:
    - The permissions model has evolved since our implementation. We will align our processes with the latest requirements during the year.

- Vulnerabilities:
    - The identified vulnerabilities are largely attributed to older dependencies. The ongoing upgrade to Ubuntu 22.04 is expected to resolve these issues.

- Fuzzing:
    - Fuzzing tooling is not currently in place. Adding fuzzing support has been added as a goal for the year.

- Pinned Dependencies:
    - We plan to search for tooling to enforce pinned dependencies to improve dependency management practices. In 2024 we improved the `dependabot` configuration to enable vulnerability visibility.

- SAST:
    - Implementing SAST tooling is another priority, with a focus on applying it after the Ubuntu 22.04 upgrade.

The OpenSSF Scorecard items that need further investigation are similar in Indy Plenum.

## Maintainer Diversity

There are 23 current maintainers on 18 Indy GitHub Teams representing at least 13 organizations. This represents a decrease of 12 total maintainers but only 3 fewer organizations compared to last year. The maintainers and teams can be seen in the Hyperledger [Access Control YAML file](https://github.com/hyperledger/governance/blob/main/access-control.yaml). The Indy maintainers file ([example](https://github.com/hyperledger/indy/blob/main/MAINTAINERS.md)) links to the Access Control YAML as the "source of truth."

## Project Adoption

Several private Indy networks were created during the past year, with some being preparatory for production usage of Hyperledger Indy. For one example, a travel technology company built both a test and a demo network during 2024 and plans to build a production Indy network during 2025.

The [Use Case Tracker](https://www.lfdecentralizedtrust.org/learn/use-case-tracker) shows 12 projects that are using Indy.

## Goals

### Performance Against Prior Goals

Below is a copy of the goals from last years [Hyperledger Indy Annual Report](https://github.com/hyperledger/toc/blob/gh-pages/project-reports/2024/2024-annual-Hyperledger-Indy.md).

* Increased awareness of Indy, its usefulness, and a corresponding increase in contributors to enable it to continue to evolve.
* Formally release the Ubuntu 20.04 release of Indy Node.
    * Look into updating the solution to later releases.
    * STATUS: **Completed**. The Ubuntu 20.04 official formal release of Indy node was accomplished February 2, 2024. The Ubuntu 22.04 release of Indy node had significant work performed on it during the year and will be completed during 2025. 
* Tools and guidance in updating existing networks to the 20.04 release.
    * STATUS: **Completed**. Documentation repo's were updated to include instructions for building networks based on the Ubuntu 20.04 codebase with the latest update being done in March, 2024.
* Continue to support the migration of Indy clients away from the Indy SDK.
    * Update the Indy documentation to point people to current “best practices”.
    * Update and release the Indy VDR component as needed.
    * STATUS: **Completed**. Indy documentation and all Discord and other community communications all point people away from the deprecated Indy SDK and towards its replacements.
* Address the “Corporate Firewall” issue, where users behind a corporate firewall cannot access an Indy network because of the ZMQ ports being used.
    * STATUS: **Partially Completed**. Several implementers (teams in Brazil and Canada) implemented "one-off" solutions to this using a local instance of an "indy-proxy". A Hyperledger Mentorship Program Project called "Indy Read Replica" ([repository](https://github.com/hyperledger/indy-read-replica)) implements a more general approach, allowing anyone to run a component that is configured to retrieve and server Indy transactions from multiple networks.
* Evolve Indy so as to be ready for when the current implementation will need more functionality, such via the Indy on Besu approach.
  * STATUS: **In Progress**. Excellent progress has been made on Indy on Besu, and the work on the project continues. See the recent [Indy on Besu article] for details about the progress, and additional updates below.

**Desired functionality:**

* Ledger Redactibility (aka "tombstoning" transactions)
* Simplify the process for adding more types of transactions so that new object types can be published on the ledger with some verification. Currently, that requires more work than we would like, so it does not happen as often as we would need.
    * Simplify, but ideally without increasing the risk of "bad data" going on the ledger and requiring use of the "Ledger Redactibility" feature (e.g. permissioned writing, and at least some structural verification of the data)
    * With more types of transactions we can more easily transition to new of kinds of verifiable credentials, such as AnonCreds v2.
    * With transitions to new VC formats, we get better functionality, such as much better revocation — which will reduce the number of transactions on the ledger — reducing the pressure on scalability.
        * Scalability is not an issue today, but will be some day.
* Additional DIDDoc support, such support for additional key types
* Read replicas for performance
* Storing other document types on an Indy ledger, such as OCA Bundles

Beyond the "Read Replica" work referenced earlier in this report, little progress was made on the desired functionality. Teams are focused on deployments with what is available.  

**Indy on Besu:**

* Transitioning from the existing PoC and design to a concrete implementation.
  * Improvement of existing modules
  * Integration with Aries Frameworks
  * Implementation of migration tools
* Some of the general desired functionality above might be done in the Indy on Besu implementation.

**STATUS**: Great progress on this was accomplished in 2024. Large companies have started making significant contributions to the codebase, and the community has expanded considerably. The smooth integration of Indy on Besu into production networks is underway. The next year will bring us statistical data on the productivity of this system in real projects.

### Next Year's Goals

Here is a list of goals we intend to work towards during the coming year to help maintain and enhance the Hyperledger Indy project:

1. Complete the Indy-node upgrade to Ubuntu 22.04
2. Begin work on the Indy-node upgrade to Ubuntu 24.04
3. Increase OpenSSF Scorecard rating
    a. Ensure that individual releases are signed
    b. Implement token permissions model
    c. Introduce tooling for pinned dependencies (use dependabot report tooling), fuzzing, and SAST
    d. Ensure that OpenSSF detects branch protections and packaging practices
    e. Add code quality checking for project commits
    f. Reformat code base
    g. Add poetry package management
4. Update the Python version and related dependencies.
5. Update Indy on Besu with revocation, and integrate it into production deployments.
6. Test migrations from existing Indy ledgers to Indy on Besu.

### Help Required

No help needed at this time.

## Project Lifecycle Status Recommendation

Graduated

Because Hyperledger Indy is so stable, and efforts are being increased to continue that status, and production level Indy networks are in service around the globe, we recommend to continue the current graduated status for Hyperledger Indy.

Although some of the current OpenSSF Scorecard values fall below the new criteria introduced by the TAC, we firmly believe that Hyperledger Indy continues to qualify as a graduated project. The project has consistently adhered to best practices and demonstrated its maturity and reliability.

The OpenSSF Scorecard is a relatively new tool, and while adjustments are needed to align with its metrics, this does not diminish the quality or robustness of the project. We have recently integrated the Scorecard into our processes and are actively working to address the identified areas for improvement. Hyperledger Indy remains a well-rounded and well-managed project, with a clear roadmap to further enhance its security posture and alignment with OpenSSF standards.

## Indy Annual Review 2025 Notes from the TAC

TAC Reviewers: Enrique Lacal (primary), Peter Somogyvari (secondary)

Great written report!

### Project Health

Using data from https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=indy&routedFrom=Github&bestPractice=false

The project is in good health, there is a substantial amount of community involvement and a varied list of organizations contributing.

- The maintainer diversity has decreased but still at a great level with 13 organizations involved.
- Most contributions performed by 3 organizations
- Metrics for commits, contributors, issues and pull requests have all gone down and is related to the maturity of the project.

The stability of the project mentioned in the annual review highlights the big pieces of work this year:

- Keeping up with the Ubuntu releases, there was a release of indy-node this year v1.13.2
- Indy on Besu was a new stream of work that continues into 2025

Project is widely adopted across the world with a varied list of use cases: https://www.lfdecentralizedtrust.org/learn/use-case-tracker

Increased awareness for Indy on Besu through a webinar titled: Evolution of Indy Project as eIDAS2/EUDI Compliant Verifiable Credentials

Discord channels have engaging discussions:

- Separate channels exist for domain specific discussions.
- Including a new Discord Channel for Indy on Besu, which has been big focus this year and will continue to be next year.

Community calls are well run and have good attendance.

Fantastic to see the project getting involved in the Mentorship program!

### Progress and Releases

- There has been a constant stream of contributions across most of the Indy Repositories
- Ubuntu 20.04 release of Indy Node
- Indy on Besu maturing and substantial traction from the community
- Community calls are fantastically ran, great meeting notes!

### Goal Review

- Achieved most of the goals set out for the year 👏🏼
- Goals for the year are clear and precise!
    - There is a stretch goal as a recommendation to specify some of the new features
    - A lot of the goals are about upgrading versions, OpenSSF, testing migration...

### Compliance with Hyperledger Project Lifecycle Criteria

- As mentioned in the annual review, the OpenSSF Scorecard reports have only come into effect and it's great to see them enabled in the key repositories.
- A goal is established to increase the OpenSSF Scorecard rating.
- Add as a goal for next year to move to it's own GitHub organization, it was discussed in the community call so already progress there!

### Recommendations

1. Ecosystem mapping

- Hyperledger Indy has a large amount of repositories and there is a lot of wikis, posts, README and it can be difficult to get a grasp of all the features it has.
  
2. Release documentation needs Improvement

- As part of the review, it was difficult to keep track of releases and versions. The cadence of releases and documenting this would improve adoption and communicating to users of new updates. Just looking at the v.13.2 release https://github.com/hyperledger/indy-node/releases/tag/v1.13.2 and the README points to using a branch. It might just need clean as the team mentioned they have move to GitHub release.
- Think about how frequently you are releasing CVE fixes and patches to users. I think the OpenSFF will enable to spot these quicker.

### Decision

The project should remain in the Graduated status given the amount of engagement, maturity and project adoption.
