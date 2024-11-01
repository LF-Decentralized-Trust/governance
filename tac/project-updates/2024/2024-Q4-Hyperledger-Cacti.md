---
layout: default
title: 2024 Q4 Hyperledger Cacti
parent: 2024
grand_parent: Project Updates
---

# Project Health

Cacti is doing great, there is steady interest in the project as interoperability is becoming more and more important to organizations wishing to deploy distributed ledger technologies.
There was a significant increase in new contributors this last quarter according to LFX (75%) and the pair programming sessions get more attendance than ever.

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

The vast majority of the community's communication happens on the Discord channel. The mailing list is not used much nowadays.

The maintainers try to respond to all queries in a timely manner. On average our response time is likely around a couple of days with the tail end being a couple of weeks. 
Note that we don't have hard data on above from Discord, so this is just a personal estimate.

We are working on a number of technical initiatives: new features, improvements to the CI speed, artifact signing and improving our OpenSSF score in general.

The migration to the Jest test runner from tap is still underway but is about 80% finished now, we are close.

# Current Plans

Main features planned:
1. Finishing the IETF SATP Typescript reference implementation (currently most of the code for it is on the `satp-dev` branch)
2. Implementing a Chainlink Fabric and/or Corda integration (the details are still being worked out)
3. Explore opportunities to add support for [EEA DLT Interoperability Specification Version 1.0](https://entethalliance.org/specs/dlt-interop/) which came out last month (September 19th, 2024)

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


# Additional Information

- Different collaborations with the academia and industry are still taking place. In particular, one of them is [Portugal's BLOCKCHAIN.PT project](https://www.hyperledger.org/blog/portugals-blockchain.pt-uses-hyperledger-cacti-as-its-interoperability-framework).