[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Annual Review Hyperledger Indy

## Project Health

Reference: [Indy LFX Insights Page](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=indy&repository=&routedFrom=Github)

Hyperledger Indy is a very stable project. Because of this stability, there are a number of scaled deployments of Indy across the world. All are running smoothly, and there is little demand for new features in the existing Indy Node/Plenum code base. Hyperledger Indy has seen adoption of Indy Besu in deployments.

### OpenSSF Scorecard for key repositories:

Indy Node [![Indy Node](https://api.scorecard.dev/projects/github.com/hyperledger-indy/indy-node/badge)](https://scorecard.dev/viewer/?uri=github.com/hyperledger-indy/indy-node) Indy Plenum [![Indy Plenum](https://api.scorecard.dev/projects/github.com/hyperledger-indy/indy-plenum/badge)](https://scorecard.dev/viewer/?uri=github.com/hyperledger-indy/indy-plenum)

#### Notes on OpenSSF Scorecard Reports

While some of the current scores for the Hyperledger Indy project do not fully reflect the reality of our practices, we have identified key areas for improvement and have added relevant goals to our roadmap for the coming year. Below is a summary of the current status and our planned actions:

- Maintained:
    - Due to the stable nature of the project, few updates are needed to keep the deployments functioning optimally; however, some updates are pending that are needed, such as the Ubuntu 22.04 update.

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
    - We plan to search for tooling to enforce pinned dependencies to improve dependency management practices.

- SAST:
    - Implementing SAST tooling is another priority, with a focus on applying it after the Ubuntu 22.04 upgrade.

The OpenSSF Scorecard items that need further investigation are similar in Indy Plenum.

## Maintainer Diversity

There are 12 current maintainers representing at least 9 organizations. This represents a decrease of 11 total maintainers but only 4 fewer organizations compared to last year.

## Project Adoption

Adoption of Indy Besu was seen this year. For one example, a company in Brazil in South America is adopting Indy Besu for their deployments.

The [Use Case Tracker](https://www.lfdecentralizedtrust.org/learn/use-case-tracker) shows 15 projects that are using Indy.

## Goals

### Performance Against Prior Goals

Below is a copy of the goals from last years [Hyperledger Indy Annual Report](https://github.com/LF-Decentralized-Trust/governance/blob/main/tac/project-updates/2025/2025-annual-Hyperledger-Indy.md).

* Complete the Indy-node upgrade to Ubuntu 22.04
  * STATUS: **In Progress**. The Ubuntu 22.04 release of Indy node had significant work performed on it during the year and will be completed during 2026
.
* Begin work on the Indy-node upgrade to Ubuntu 24.04
  * STATUS: **Not started**. This work is pending the completion of the Ubuntu 22.04 release of Indy node. Will be completed during 2026

* Increase OpenSSF Scorecard rating a. Ensure that individual releases are signed b. Implement token permissions model c. Introduce tooling for pinned dependencies (use dependabot report tooling), fuzzing, and SAST d. Ensure that OpenSSF detects branch protections and packaging practices e. Add code quality checking for project commits f. Reformat code base g. Add poetry package management
  * STATUS: **Not Started**. Migrating from Hyperledger to Hyperledger-indy took much of the available time for this task.


* Update the Python version and related dependencies.
  * STATUS: **Not Started**. This work is pending the completion of the Ubuntu 22.04 release of Indy node. Will be completed during 2026

* Update Indy on Besu with revocation, and integrate it into production deployments.
  * STATUS: **Completed**. 
* Test migrations from existing Indy ledgers to Indy on Besu.
  * STATUS: **Completed**. 

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


**STATUS**: The Ubuntu 22.04 work is becoming a hurdle for new developers and continuing work on the project. Getting the Ubuntu 22.04 work reviewed and adopted is a high priority for the first quarter of 2026.

### Next Year's Goals

Here is a list of goals we intend to work towards during the coming year to help maintain and enhance the Hyperledger Indy project:

1. Complete the Indy-node upgrade to Ubuntu 22.04
2. Ensure developer onboarding is a smooth process to attract new developers to the project
3. Research companies using Indy in testing or production and invite them to contribute to Indy
4. Begin work on the Indy-node upgrade to Ubuntu 24.04
5. Increase OpenSSF Scorecard rating
    a. Ensure that individual releases are signed
    b. Implement token permissions model
    c. Introduce tooling for pinned dependencies (use dependabot report tooling), fuzzing, and SAST
    d. Ensure that OpenSSF detects branch protections and packaging practices
    e. Add code quality checking for project commits
    f. Reformat code base
    g. Add poetry package management
6. Update the Python version and related dependencies.

### Help Required

No help needed at this time.

## Project Lifecycle Status Recommendation

Graduated

Because Hyperledger Indy is so stable, and efforts are being increased to continue that status, and production level Indy networks are in service around the globe, we recommend to continue the current graduated status for Hyperledger Indy.

Although some of the current OpenSSF Scorecard values fall below the new criteria introduced by the TAC, we firmly believe that Hyperledger Indy continues to qualify as a graduated project. The project has consistently adhered to best practices and demonstrated its maturity and reliability.

The OpenSSF Scorecard is a relatively new tool, and while adjustments are needed to align with its metrics, this does not diminish the quality or robustness of the project. We have recently integrated the Scorecard into our processes and are actively working to address the identified areas for improvement. Hyperledger Indy remains a well-rounded and well-managed project, with a clear roadmap to further enhance its security posture and alignment with OpenSSF standards.

## Indy Annual Review 2026 Notes from the TAC



### Project Health

### Progress and Releases

### Goal Review

### Compliance with Hyperledger Project Lifecycle Criteria

### Recommendations


### Decision
