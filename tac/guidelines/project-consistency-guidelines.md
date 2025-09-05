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

**MRW** - There is potentially a lot of overlap with [project best practices](./project-best-practices.md)

**MRW** - Perhaps this document should be wrapped into that document?

## Relationship to existing guidelines

 - MRW: Suggest some discussion around consistency vs guidelines

### Areas of consistency by stakeholder

1. LFDT
   - Communication
      - Release activity
3. Project users
   - Communication
      - Release activity
      - CVE reporting & fixes (should release notes include all fixed CVEs?)
   - Issue tracking
      - Progress on issues & bug fixes
   - Roadmap
      - Where to find it
      - How to contribute to it (raise issues? attend contributor calls?)
5. Project maintainers & contributors
   - Communication
      - Release planning
   - Bug tracking
   - Roadmap
      - Where to find it 


---
**OLD NOTES BELOW**
---

### Communication

### Bug tracking

 - MRW: There is already guidance about using Github practices such as "bug: ..." issue naming

### Release planning

 - MRW: Post on the "maintainers" or "contributors" discord channel that a new release is planned with an approximate timeline
   - MRW: Is this being too prescriptive?

### Release communication

 - MRW: Use Github releases to communicate new releases
 - MRW: Post on the main project discord channel (i.e. not just the "maintainers" or "contributors" channels

### Technical discussion that contributes to project direction

 - Where is discussion, context and background that helps understand story prioritization and the current roadmap
 - 

### Feature/story tracking

 - How well can someone "external" to the project easily follow what the community is currently working on
 - Can people easily identify the priorities of the project, for this release and the next release?
 - Where is this information stored - github wiki, atlassian wiki, github issues

### Roadmap

 - How can I see what the current roadmap is for a project?
 - e.g. roadmap.md for consistency, but with the option to hyperlink to somewhere that is project-specific e.g. wiki, Git wiki, discord channel...

### Issue templates

### Vulnerability tracking and disclosure

 - MRW: CVE reporting
 - MRW: CVE disclosures outside of public domain comms

### Security

 - MRW: I'm less convinced this needs tracking under "consistency" as it's already reporting in annual reports and existing guidelines for e.g. security.md
   - Maintainer/GH access control
   - GH branch protection rules (e.g. number of approvals)

## Areas that we do not feel require clear consistency between projects

 - Release process i.e. the buttons that are pushed and GHAs that are run to make a release happen
