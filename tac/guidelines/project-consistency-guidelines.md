---
layout: default
title: Project Consistency
parent: Guidelines
grand_parent: LF Decentralized Trust TAC
---
[//]: # (SPDX-License-Identifier: CC-BY-4.0)

This document describes various considerations projects should consider in order to maintain consistency across different projects.

There are several reasons why consistency across projects is beneficial.

## Benefits to the LFDT

The LFDT manages a growing number of projects and labs and must review and discuss all of the projects on a regular basis. This process of governance is much easier when projects are managed and run in a consistent way.

## Benefits to project maintainers

The more consistent projects are, the easier it is for collaboration and contribution across projects.

## Benefits to contributors

Due to the common technology basis of LFDT projects it is likely that some contributors will be active on multiple projects. The more consitent they are, the easier it is to participate in multiple projects effectively.



## Scope and relationship to existing guidelines

  - This document should be read in conjunction with the other project guidelines and best practice documentation
    - The LFDT already sets out `MUST` and `SHOULD` and `MAY` directives that projects should treat accordingly. This document
is not intended to replace any of the existing governance rules set out by the LFDT. 
  - The LFDT does not expect projects to be run in an identical fashion.
    - Technology choices, communication channels, release cadence etc. are all expected to be project-specific. These guidelines are intended as a reminder to projects to consider consistency but still make choices most suitable to the project.

## Recommended areas of consistency

### Communication platform

While the LFDT does not prescribe the use of Discord for project discussion, the majority of projects and labs use the LFDT Discord server.

Unless there is a particular reason to use an alternative communication platform, using the LFDT Discord server allows maintainers and users to keep abreast of all LFDT projects in a single place.

### Repository landing page experience

The `README` for a repository is often the first place maintainers and users go to understand the project and find resources to help them with next steps.

In the past projects have varied a lot in what they attempt to cover in their landing page `README.md` file. We encourage maintainers to look at READMEs from other projects and aim to provide information - or links to information - on the follow:

 - What the project is and what does it do?
 - Project/code architecture
 - Getting started information, with links to tutorials/examples
 - Getting started as a contributor, with links to IDE setup, dev environment help etc.
 - Information about the project roadmap

It is not typically recommended to go into lengthy detail in any one area in the root `README.md`. Instead, providing a high level overview and then linked to more detailed information on each topic is typically easier for users to consume.

### Public release tracking

There are many tools available for tracking releases and roadmaps. Our recommendation is to use Github project boards for release tracking, unless there are specific limitations that make release tracking difficult for maintainers.

Boards for future releases can be created to help users understand what the project roadmap looks like. If some areas of the roadmap are less certain, a page outlining the community's current thoughts on future direction of the project is recommended. While much discussion on project direction is likely to happen in Git issues and on Discord, summarizing the current outlook somewhere makes it easier for users to get an at-a-glance view of project direction.

### Release communication

It is useful for projects to have a dedicated place to discuss releases. Keeping this discussion separate to other maintainer/contributor discussion makes it easier for project consumers to identify that a new release is on its way, and for them to keep an eye out for any possible issues that have been highlighted in a particular release.

The amount of discussion on general maintainer/contributor channels can make it hard to spot this sort of information easily. A project consumer may not be interested in bugs being worked during development, but they will certainly care if a regression is found in a newly released version.

It is also recommended that releases are communicated through Github release artifacts. If a project has followed [existing best practices](https://discord.com/channels/905194001349627914/1435984838388875284) to use conventional commit messaging, auto-generated release content will be produced that makes it easy for project consumers to know whether changes in a release are particularly relevant to them.

Once a release has been produced, announcing it on the project's main or announce channel makes it easy for consumers to know there is a new release to look at.

### Including fixed `HIGH` and `CRITICAL` CVEs in release notes

Release notes should highlight all `HIGH` and `CRITICAL` CVEs that have been resolved in a new release.

This ensures users can easily identify if they should plan an upgrade based on the severity of CVEs resolved in newer releases.

### Commit messages

In some cases commit messages are minimal and rely on context from the Git issue or PR.

For substantial commits it is beneficial to use more detailed commit messages to help understand the reason behind a change in case of a migration to another source control platform.
