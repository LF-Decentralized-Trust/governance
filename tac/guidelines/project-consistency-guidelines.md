---
layout: default
title: Project Consistency
parent: Guidelines
grand_parent: LF Decentralized Trust TAC
---
[//]: # (SPDX-License-Identifier: CC-BY-4.0)

This document outlines consistent approaches to certain aspects of running and maintaining an LFDT project.

LFDT projects will always have their own approaches to how they manage and govern themselves, how they
communicate and collaborate, and how they track and communicate progress.

The LFDT already sets out `MUST` and `SHOULD` and `MAY` behaviours that projects should treat accordingly. This document
is not intended to replace any of the existing governance rules set out by the LFDT. Instead it is designed improve
consistency across projects such that inter-project collaboration is easier, and to make it easier for individuals to
collaborate to multiple LFDT projects.

## Relationship to existing guidelines

  - This document should be read in conjunction with the other project guidlines and best practice documentation
  - The **bold** items below are strong recommendations for project characteristics that will encourage good core consistency between projects

### Areas of consistency by stakeholder

1. LFDT
   - Communication
   - Release activity
   - CVE bounties
3. Project users
   - Release communication
      - **Readme structure that gives me a quick overview of what the project is/does** 
      - **Public release tracking board can be viewed by project users and used to determine approximate contents of upcoming release**
   - Release contents - CVEs
      - **CVE resolution should be included in release notes including specific CVE numbers**
         - (Potentially GH built-in CVE labelling)
      - CVE advisories? There is very mixed use of these across current projects
   - Issue tracking
      - Progress on issues & bug fixes
      - MRW: I'm erring on the side of not wanting to be over zealous in what we stipulate here
   - Roadmap
      - **Readme structure makes it easy to find the current project roadmap** 
      - **Readme structure makes it easy to understand how the roadmap is determined and where it is discussed**
5. Project maintainers & contributors
   - Developers/contributors
      - **Readme structure should gives me a quick way to learn how to set up a development environment**
   - Maintainers
      - **Major & minor releases should be planned and tracked on a public project tracking board**
        - Github projects are encouraged, alternatives acceptable, as long as public and not requiring authentication to view
      - **Project tracking board linked from repo landing page**
   - CVE reporting
      - **Raising GH advisories for at least HIGH and CRITICAL CVEs??**
   - Bug tracking
   - Roadmap
      - **Readme structure makes it easy to find the current project roadmap** 
      - **Readme structure makes it easy to understand how the roadmap is determined and where it is discussed**

## Areas that we do not feel require clear consistency between projects

 - Release process i.e. the buttons that are pushed and GHAs that are run to make a release happen
