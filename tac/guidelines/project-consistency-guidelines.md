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
   - Communication
      - **Readme structure that gives me a quick overview of what the project is/does** 
      - Release activity
      - **CVE resolution should be included in release notes including specific CVE numbers**
         - (Potentially GH built-in CVE labelling)
      - CVE advisories
   - Issue tracking
      - Progress on issues & bug fixes
   - Roadmap
      - Where to find it
      - How to contribute to it (raise issues? attend contributor calls?)
5. Project maintainers & contributors
   - Communication
      - **Readme structure that gives me a quick way to learn how to set up a development environment**
      - Release planning
         - **Public project tracking board**
            - **Github projects for tracking**
            - Alternatives acceptable, as long as public and not requiring authentication to view
         - **Project tracking board linked from repo landing page**
   - CVE reporting
      - **Raising GH advisories for at least HIGH and CRITICAL CVEs??**
   - Bug tracking
   - Roadmap
      - Where to find it 

## Areas that we do not feel require clear consistency between projects

 - Release process i.e. the buttons that are pushed and GHAs that are run to make a release happen
