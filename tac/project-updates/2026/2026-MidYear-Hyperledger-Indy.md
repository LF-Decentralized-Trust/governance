# 2026 Mid-Year Review Hyperledger Indy

## Project Health

Reference: [Indy LFX Insights Page (past 12 months)](https://insights.linuxfoundation.org/project/indy?timeRange=past365days&start=2025-11-04&end=2026-11-04)

Hyperledger Indy is a very stable project. Because of this stability, there are a number of scaled deployments of Indy across the world. All are running smoothly, and there is little demand for new features in the existing Indy Node/Plenum code base. Hyperledger Indy has seen adoption of Indy Besu in deployments.

LFX Insights rates the project's health as Fair (59/100) for the past 12 months. The score is held down mainly by development activity (8/25), reflecting that no new Indy Node release has shipped while the Ubuntu 22.04 work was underway. Security and supply chain scored 33/35, with no open CVEs. The initial check-in of the Ubuntu 22.04 work for Indy Node has been handed off to testing, and testing has begun.

### OpenSSF Scorecard for key repositories:

Indy Node [![Indy Node](https://api.scorecard.dev/projects/github.com/hyperledger-indy/indy-node/badge)](https://scorecard.dev/viewer/?uri=github.com%2Fhyperledger-indy%2Findy-node) Indy Plenum [![Indy Plenum](https://api.scorecard.dev/projects/github.com/hyperledger-indy/indy-plenum/badge)](https://scorecard.dev/viewer/?uri=github.com%2Fhyperledger-indy%2Findy-plenum)

#### Notes on OpenSSF Scorecard Reports

The latest Scorecard results are 4.5 for Indy Node (scanned 08/28/2026) and 5.4 for Indy Plenum (scanned 03/11/2026). Code review, license, dependency update tooling, and contributor diversity score 10 in both repositories. While some of the current scores do not fully reflect the reality of our practices, we have identified key areas for improvement and added them to our roadmap. Below is a summary of the current status and our planned actions:

- Maintained: Due to the stable nature of the project, few updates are needed; the pending Ubuntu 22.04 update has been handed off to testing.
- Signed Releases: The score is 0 because packages are uploaded to a trusted Debian repository with a signing key, rather than releases being signed individually. Signing individual releases is a goal for the year.
- Branch Protection and Packaging: Both are in place, but the Scorecard does not fully recognize them (the Indy Node branch protection check fails with an error, and Indy Plenum scores 4). We will investigate and resolve the discrepancies.
- Token Permissions: Both repositories score 0. We will align our workflows with the latest requirements during the year.
- Vulnerabilities: Indy Node reports 52 known vulnerabilities, largely attributed to older dependencies (Indy Plenum reports none). The ongoing upgrade to Ubuntu 22.04 is expected to resolve most of these.
- Fuzzing, Pinned Dependencies, and SAST: Not yet in place (score 0 in both repositories). Tooling for each is a goal for the year, with SAST to follow the Ubuntu 22.04 upgrade.

## Maintainer Diversity

There are 7 active maintainers representing 10 organizations, as reported by the [LFX Insights page](https://insights.linuxfoundation.org/project/indy?timeRange=past365days&start=2025-11-04&end=2026-11-04) for the past 12 months.

## Project Adoption

As noted in the annual report, a company in Brazil adopted Indy Besu for its deployments last year. A small number of organizations are planning new Indy networks in the next 2 quarters.

The [Use Case Tracker](https://www.lfdecentralizedtrust.org/learn/use-case-tracker) shows 16 projects that are using Indy, up from 15 at the time of the annual report. Of these, 9 are listed as in production.

## Goals

### Performance Against Prior Goals

Below is a copy of the goals from the [Hyperledger Indy 2026 Annual Report](https://github.com/LF-Decentralized-Trust/governance/blob/main/tac/project-updates/2026/2026-annual-Hyperledger-Indy.md).

1. Meet all the OpenSSF scorecard requirements for graduated projects a. Ensure that individual releases are signed b. Implement token permissions model c. Introduce tooling for pinned dependencies (use dependabot report tooling), fuzzing, and SAST d. Ensure that OpenSSF detects branch protections and packaging practices e. Add code quality checking for project commits f. Reformat code base g. Add poetry package management

   - STATUS: **Not Started**

2. Complete the Indy-node upgrade to Ubuntu 22.04

   - STATUS: **In Progress**. The initial check-in has been handed off to testing, and testing has begun. This release also moves Indy Node installation to a Docker-based approach.

3. Ensure developer onboarding is a smooth process to attract new developers to the project

   - STATUS: **In Progress**. The Ubuntu 22.04 release of Indy Node, now in testing, moves installation to a Docker-based approach, which should simplify environment setup for new developers once released. We will continue improving onboarding documentation.

4. Research companies using Indy in testing or production and invite them to contribute to Indy

   - STATUS: **In Progress**. Outreach has begun, but so far it has not yielded any additional support.

5. Begin work on the Indy-node upgrade to Ubuntu 24.04

   - STATUS: **Not Started**. This work is pending the completion of the Ubuntu 22.04 release of Indy Node, which is where all current efforts are focused.

6. Update the Python version and related dependencies.

   - STATUS: **In Progress**. The Ubuntu 22.04 release of Indy Node, now in testing, moves the underlying Python version to 3.10, the version shipped with Ubuntu 22.04. A broader update of related dependencies has not yet been done.

**Desired functionality:**

- Ledger Redactibility (aka "tombstoning" transactions)

- Simplify the process for adding more types of transactions so that new object types can be published on the ledger with some verification. Currently, that requires more work than we would like, so it does not happen as often as we would need.

  - Simplify, but ideally without increasing the risk of "bad data" going on the ledger and requiring use of the "Ledger Redactibility" feature (e.g. permissioned writing, and at least some structural verification of the data)

  - With more types of transactions we can more easily transition to new kinds of verifiable credentials, such as AnonCreds v2.

  - With transitions to new VC formats, we get better functionality, such as much better revocation, which will reduce the number of transactions on the ledger and reduce the pressure on scalability.

    - Scalability is not an issue today, but will be some day.

- Additional DIDDoc support, such as support for additional key types

- Read replicas for performance

- Storing other document types on an Indy ledger, such as OCA Bundles

No significant progress was made on the desired functionality this period; teams remain focused on deployments with what is available.

**Indy on Besu:**

**STATUS**: The prior Indy on Besu goals were completed. Development has continued at a low level this year, with multi-ledger router improvements (including ETHR support and ledger client caching) added in May 2026, along with CI/release pipeline and dependency updates.

### Next Year's Goals

Here is a list of goals we intend to work towards during the coming year to help maintain and enhance the Hyperledger Indy project:

1. Meet all the OpenSSF scorecard requirements for graduated projects a. Ensure that individual releases are signed b. Implement token permissions model c. Introduce tooling for pinned dependencies (use dependabot report tooling), fuzzing, and SAST d. Ensure that OpenSSF detects branch protections and packaging practices e. Add code quality checking for project commits f. Reformat code base g. Add poetry package management
2. Complete the Indy-node upgrade to Ubuntu 22.04
3. Ensure developer onboarding is a smooth process to attract new developers to the project
4. Research companies using Indy in testing or production and invite them to contribute to Indy
5. Begin work on the Indy-node upgrade to Ubuntu 24.04
6. Update the Python version and related dependencies.

### Help Required

Help getting more contributors and organizations involved in the project would be appreciated.

## Project Lifecycle Status Recommendation

Graduated

Hyperledger Indy is a mature, stable product, and production-level Indy networks are in service around the globe. We recommend continuing the current graduated status for Hyperledger Indy.

We recognize the TAC's concern from the annual review about the OpenSSF Scorecard. Although some of the current Scorecard values fall below the criteria introduced by the TAC, improving them remains a priority: the Ubuntu 22.04 release now in testing is expected to resolve the dependency vulnerabilities, and the Scorecard improvements are the first goal for the remainder of the year. The Scorecard is a relatively new tool and adjustments are needed to align with its metrics, but this does not diminish the quality or robustness of the project. Hyperledger Indy remains a well-managed project with a clear roadmap to further enhance its security posture and alignment with OpenSSF standards.
