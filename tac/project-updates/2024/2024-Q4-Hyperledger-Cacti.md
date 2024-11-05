---
layout: default
title: 2024 Q4 Hyperledger Cacti
parent: 2024
grand_parent: Project Updates
---

# Project Health

- Cacti is doing great, there is steady interest in the project as interoperability is becoming more and more important to organizations wishing to deploy distributed ledger technologies.
- There was a significant increase in new contributors this last quarter according to LFX (75%) and the pair programming sessions get more attendance than ever.
- The project repository was successfully moved to [its own repository](https://github.com/hyperledger-cacti) following the move from the Hyperledger Foundation to Linux Foundation's Decentralized Trust. Cacti was one of the first projects on which this experiment was carried out, and it was successful thanks to the LFDT administrators.
- The mentorship projects are progressing nicely, with solid code contributions from the mentees, including Cactus-Weaver integration.
- Work on keeping Cacti up-to-date with the IETF SATP interoperability protocol standard is going well.
  * Cacti maintainers continue to be actively involved in the IETF SATP Working Group, co-authoring protocol specifications.
- We are not doing too badly on the [OpenSSF Scorecard Metrics](https://scorecard.dev/viewer/?uri=github.com%2Fhyperledger-cacti%2Fcacti) with a present score (as of the time of this file's commit) of 6.3, but there is a lot of scope to improve.

# Questions/Issues for the TAC

No questions at the moment, thank you.

# Releases

Issued releases:
- v2.0.0-rc.4
- v2.0.0-rc.5
- v2.0.0-rc.6
- v2.0.0-rc.7
- v2.0.0

Caveat: We are still working on the publishing workflows that broke down after our latest org migration.
v2.0.0 was affected in the sense that the artifacts are not yet published on npm due to our token not being right.

Upcoming releases:
- v2.0.1
- v2.1.0

# Overall Activity in the Past Quarter

- The vast majority of the community's communication happens on the Discord channel. The mailing list is not used much nowadays.
- The maintainers try to respond to all queries in a timely manner. On average our response time is likely around a couple of days with the tail end being a couple of weeks.
  * Note that we don't have hard data on above from Discord, so this is just a personal estimate.
- We are working on a number of technical initiatives: new features, improvements to the CI speed, artifact signing and improving our OpenSSF score in general.
- The migration to the Jest test runner from tap is still underway but is about 80% finished now, we are close.
- One of these mentorship projects involves a major change to the Cacti code base and architecture, namely the integration of the Cactus and Weaver modules into a common and comprehensive set of capabilities for cross-network operations. A first-cut version of these common COPM modules is [close to being merged](https://github.com/hyperledger-cacti/cacti/pull/3546) into the main branch.
- There was a lot of work done on the SATP-Hermes framework (part of the IETF standardization compliance work) in the past quarter (see the [satp-dev](https://github.com/hyperledger-cacti/cacti/tree/satp-dev) branch).
  * The SATP-Weaver-Relay framework (the other sample implementation of the SATP standard under Cacti) did not make any progress since the [May 23 workshop](https://lf-hyperledger.atlassian.net/wiki/spaces/events/pages/21794363/Standardizing+DLT+Interoperation+Implementing+IETF+Secure+Asset+Transfer+Protocol+in+Hyperledger+Cacti), but we hope to get more code contributions in the future, especially after the IETF published official RFCs.
- We successfully removed outdated and deprecated connector plugins from the project that lacked OpenAPI compatibility.
- The Ledger Browser plugin (GUI) was fully redesigned to enhance extensibility and improve the user interface. Additionally, we significantly expanded and refined the documentation to improve the onboarding experience and simplify project setup for new users.

# Current Plans

Main features planned:
1. Finishing the IETF SATP Typescript reference implementation (currently most of the code for it is on the `satp-dev` branch)
2. Implementing a Chainlink Fabric and/or Corda integration (the details are still being worked out)
3. Explore opportunities to add support for [EEA DLT Interoperability Specification Version 1.0](https://entethalliance.org/specs/dlt-interop/) which came out last month (September 19th, 2024)
4. Improve our OpenSSF Scorecard numbers.
5. Working on a more automated and sustainable way to maintain package references in source code and configuration files so that if (or when) the repository is migrated to a new organization, the relevant GitHub Actions will automatically publish packages to the new organization's namespace whenever a release is made. (FYI, the publish actions for many packages failed to take effect in the recent `2.0.0` release because of hardcoded references to `hyperledger`. We will fix this in the next release.)
6. Continue improving the Ledger Browser plugin, promote it and engage the community to attract new contributors.

Releases planned:
- v2.0.1
- v2.1.0
- Potentially v3.0.0 if the number requested breaking changes reaches above threshold sooner than next Spring.

# Maintainer Diversity

We have 8 active maintainers from 4 different organizations total:

- Izuru Sato 
- Michal Bajer 
- Peter Somogyvari 
- Takuma TAKEUCHI 
- Jagpreet Singh Sasan 
- Venkatraman Ramakrishna 
- Sandeep Nishad 
- Rafael Belchior 

# Contributor Diversity

We estimate that the the number of contributing organizations have grown slightly since last quarter, but
LFX seems to be buggy at the moment showing that there are 17 **thousand** organizations contributing to the project which
is definitely wrong.
See: https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/reports/organizations?project=cacti

# Additional Information

- Different collaborations with the academia and industry are still taking place. In particular, one of them is [Portugal's BLOCKCHAIN.PT project](https://www.hyperledger.org/blog/portugals-blockchain.pt-uses-hyperledger-cacti-as-its-interoperability-framework).
