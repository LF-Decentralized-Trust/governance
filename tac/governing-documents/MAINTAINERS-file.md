---
layout: default
title: MAINTAINERS Guidelines
parent: Governing Documents
grand_parent: LF Decentralized Trust TAC
nav_order: 6
---
[//]: # (SPDX-License-Identifier: CC-BY-4.0)

## Introduction

All LF Decentralized Trust (LFDT) repositories **MUST** have a `MAINTAINERS.md` file at the top-level directory of the source code. The [SAMPLE-MAINTAINERS.md](./SAMPLE-MAINTAINERS) can be used as a template by projects creating a new repository.

The Technical Steering Committee (TSC) for the project to which a repository belongs **MUST** periodically send out notifications about missing `MAINTAINERS.md` files.

The LFDT GitHub organization administrators (i.e., LFDT TAC) **SHOULD** periodically send out notifications about missing `MAINTAINERS.md` files.

The following provides guidelines and suggested content to include in the `MAINTAINERS.md` file.

## Maintainer Scopes and GitHub Roles

Becoming a Maintainer for a repository implies being granted special privileges
within that repository to do the additional scope(s) of work required of a
Maintainer. In most cases, the additional privileges are implemented by giving
maintainers one of the elevated [GitHub
roles](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization)
within the repository.

In most repositories, the "Maintainer" scope is given to all repository
Maintainers. The "Maintainer" scope is defined as the "Maintain" GitHub role.
This is usually sufficient to do all of the work required of a Maintainer. From
time to time, Maintainers may have to request certain administrative tasks by
performed by the LFDT GitHub organization administrators.

In some repositories, the maintainers may decide to define additional scopes and
each Maintainer given one or more of those designated scopes:

- In rare cases, Maintainers in a repository may request that the project's TSC enable designating some Maintainers with different GitHub roles, such as "Admin" (more capable than "Maintain") or "Triage" (less capable than "Maintain").
  - Each elevated GitHub role needed in a repository requires the project's TSC to create and maintain an additional GitHub Team.
  - The LFDT TAC manages a team per LFDT Project that includes all contributors to the project. That team is given the "Read" GitHub role in all project repositories. This team need not be documented in the "MAINTAINERS" file.
- Maintainers **MAY** define Maintainer scopes within a repository that don't require
  elevated GitHub privileges. For example, a scope might include hosting
  community meetings, or contributing to the LFDT Project's Quarterly
  report.

If there is more than the single "Maintainer" scope used in a repository, there **MUST** be a list of the repository specific scopes in the MAINTAINERS file. The list must include the scope name, the definition of the scope, and if applicable, the related GitHub Role and Team for the scope.

| Scope      | Definition               | GitHub Role | GitHub Team               |
| ---------- | ------------------------ | ----------- | ------------------------- |
| Maintainer | The GitHub Maintain role | Maintain    | `<repository> committers` |

## List of Repository Maintainers

Lists of active and emeritus maintainers **MUST** be included in the `MAINTAINERS.md` file.

Changes to the maintainers lists **MUST** be made via Pull Requests. Once a new `MAINTAINERS.md` file is created or a PR changing the maintainer lists within the file is merged, a corresponding update to the affected GitHub Teams within the LFDT GitHub organization must be made. This is a manual process and the maintainers must ensure that it occurs.

It is recommended that the lists be sorted alphabetically and **MUST** contain at least the Maintainers name, GitHub ID, Scope, and at least one contact method. The reasons for populating columns are:

- A GitHub ID **MUST** be provided to add the Maintainer to a GitHub Team, and to recognize the action the Maintainer takes in the repository.
- The Scope **MUST** be provided to know the role of each Maintainer, and to know the GitHub Team to update when adding/removing Maintainers.
- A LFID (Linux Foundation ID), Discord ID and/or Email are the most effective ways for the LFDT to contact the Maintainer when necessary.
- A Company Affiliation is helpful for monitoring the diversity of the Maintainer community for a project.

The following table format **MUST** be used for both Maintainers lists (active and emeritus):

**Active Maintainers**

| Name | GitHub ID | Scope | LFID | Discord ID | Email | Company Affiliation |
| ---- | --------- | ----- | ---- | ---------- | ----- | ------------------- |
|      |           |       |      |            |       |                     |

**Emeritus Maintainers**

| Name | GitHub ID | Scope | LFID | Discord ID | Email | Company Affiliation |
| ---- | --------- | ----- | ---- | ---------- | ----- | ------------------- |
|      |           |       |      |            |       |                     |

## Maintainer Duties

The `MAINTAINERS.md` file **SHOULD** contain information about the different
maintainer scopes, and for each, the maintainers duties (e.g., maintainers
calls, quarterly reports, code reviews, issue cleansing). See the [Sample
Maintainers](./SAMPLE-MAINTAINERS) for an example of what to include in this
section for an open source software project. Feel free to evolve that text to
match the needs of the repository and project.

If the repository is for a community specification, or other governance or
documentation purpose, the tasks of the Maintainers (often called "Editors"
in such cases) might be different than for Maintainers of an open source code
project. The Maintainer role is more about approving and merging pull requests
that reflect the agreement of the community, as opposed to code related metrics
(quality, fit for purpose, tests, etc.). In some cases, a GOVERNANCE.md file
like the [AnonCreds Methods Registry governance file] might further define the duties of the maintainers.

[AnonCreds Methods Registry governance file]: https://github.com/hyperledger/anoncreds-methods-registry/blob/main/registry/governance.md

## How to Become a Maintainer

The `MAINTAINERS.md` file **SHOULD** contain information about how to become a
maintainer for the project. This section **SHOULD** list specific information
about what is required. Information that **SHOULD** be included in this section:

* What is required before someone can be considered to become a maintainer.
  * Include a statement on how an emeritus maintainer can be changed to active again.
* Consider whether there should be different requirements based on the scope of a given maintainer.
* Whether sponsorship by an existing maintainer is required.
* How maintainers are proposed to the community. Proposals are typically done by creating PR against the `MAINTAINERS.md` file, and including information in the PR about how the proposed contributor meets the criteria to be a maintainer.
* How many maintainers must approve the proposed maintainer.
* How long the existing maintainers have to respond to the proposal.

## How Maintainers are Removed or Moved to Emeritus Status

The `MAINTAINERS.md` file **SHOULD** contain information about how a maintainer is removed from the list of active maintainers. Information that **SHOULD** be included in this section:

* The reasons a maintainer would be removed from the list of active maintainers.
* How a removal is proposed. Typically, this is similar to the way in which maintainers are added, such as via a PR against the `MAINTAINERS.md` file.

# References
* [TAC Decision Log - Common Maintainers Management Policy](https://wiki.hyperledger.org/display/TSC/Common+Maintainers+management+policy)