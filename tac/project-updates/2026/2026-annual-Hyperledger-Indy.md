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

The report is really well written and gives a clear overview of Indy's status at the end of 2025.

A look through one of the main repos, `indy-node`, shows that the project is exercising good practices in terms of issue tagging (e.g. using `good-first-issue`, `help-wanted` and so on) to help with project development.

Discussion is clearly very active on the project's Discord channels. This is clearly a project that is active and has a lot of live discussion.

Contributor calls are very well run with a very clear agenda, for example https://lf-hyperledger.atlassian.net/wiki/spaces/indy/pages/527925249/2025-10-07+Indy+Contributors+Call from October 2025.

### Project Health

LFX Insights gives the project an Excellent score (see https://insights.linuxfoundation.org/project/indy?timeRange=past365days&start=2025-02-18&end=2026-02-18) with a couple of warnings:

 - 4 orgs provide the majority of contributors

Compared to other LFDT projects this probably puts Indy in a slightly healthier position than other projects, so is not particularly concerning.

 - 4 contributors account for the majority of commits
  
While not ideal, again this is somewhat on par with other LFDT projects and isn't seen as a concern by TAC reviewers.

### Progress and Releases

As the previous annual report highlighted some of the focus has been on Indy Besu. As such there haven't been any new releases of Indy Node in 2025 but work on upgrading it to Ubuntu 22.04 has been active. 

There has been active work on other repos, including at least 1 release in 2025. Particularly:

 - `indy-besu`
 - `indy-vdr`
 - `indy-node-container`

### Goal Review

There has been some clear progress on the goals set for 2025. Indy Besu particularly has had a lot of focus, with the 2 main goals completed.

While the work to upgrade Indy Node hasn't closed out in 2025, it has been progressing and is due to close out in 2026.

Work on the OpenSSF scorecard is the biggest area for attention on Indy. Scores of particular concern are:

 - `Maintained` (0/10)
 - `SAST` (0/10)
 - `Signed Releases` (0/10)
 - `Vulnerabilities` (0/10)
 - `Branch protection` (?)

The annual report has highlighted the fact that the scorecard is relatively new, but as a graduated project it is important to address these as a priority.

### Compliance with Hyperledger Project Lifecycle Criteria

 - The project completed its move to the new `hyperledger-indy` org which is a big success given the amount of admin required to shift all of the repositories from the `hyperledger` org.
 - The project has a security policy including a named security team, identified in `SECURITY.md` 
 - Most repositories have all the requisite files as per the [repository structure](https://github.com/LF-Decentralized-Trust/governance/blob/d34f0806ffaab3f48ac728e5354da1f86dd780b2/tac/governing-documents/repository-structure.md) guidelines. There are a small number of areas to tidy up in this regard:
   - Most repos have `SECURITY.md`, but since the file is duplicated across them it is liable to get out of date. It might be better to have most repos have a minimal `SECURITY.md` that links to the main `indy` repo (or perhaps the `governance` repo)
   - Some repos are missing `SECURITY.md`, for example `indy-cli-rs`
   - The project doesn't have a `NOTICES` file in any of the repos. This is a `SHOULD` recommendation of the repository structure guidelines.
   - The project doesn't have an `ADOPTERS.md` file. This would be a useful addition to help the TSC and potential users understand the use-cases for Indy

### Recommendations

It will be difficult for the TAC to agree for Indy to remain in `graduated` status after 2026 if there is not a noticeable improvement in the OpenSSF scorecard.

Since the project is stable and still in active development, and the project maintainers assert in this report that they have a goal for 2026 to address the scorecard, it feels acceptable to leave the project in `graduated` status for 2026, with the following recommendations:

 - That the scorecard goal for 2026 be one of their highest priority items
 - That they acknowledge the possiblity of been moved out of `graduated` at the end of 2026 if this has not been sufficiently improved.

### Decision
