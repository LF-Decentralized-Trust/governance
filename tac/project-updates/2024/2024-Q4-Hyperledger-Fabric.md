---
layout: default
title: 2024 Q4 Hyperledger Fabric
parent: 2024
grand_parent: Project Updates
---

# Project Health

Hyperledger Fabric is fairly mature and stable with a v2.5 long-term support (LTS) release and a new v3.0 release.
There is less churn and fewer commits than in years past, with continued focus on quality, maintenance, and support.
New features get proposed, approved, and implemented based on a community RFC process.
Mailing list activity is down a bit compared to prior years.
PRs and mailing list questions are generally turned around quickly.
There is significant Discord activity.

# Questions/Issues for the TAC

We would like to shift the project release images from DockerHub to Github Container Registry (ghcr). Note that the project release images are intended for trial use rather than production use, since they are not maintained regularly for security vulnerabilities, etc (production users should work with a vendor for commercially supported images). But still, there are a few concerns we'd like to raise for feedback.
- Existing deployments and users may have scripts that pull images from DockerHub, for example as part of CI jobs. Would it be acceptable to break these scripts with the move?
- We could leave all old images on DockerHub, and publish new images to Github Container Registry. Would this be confusing to users?
- We've seen some usage limits associated with Github Container Registry in various docs, has this become an issue in practice for other projects?

# Releases

LTS release:
- v2.5 is the current LTS release with patch releases at least quarterly.

[Releases](https://github.com/hyperledger/fabric/releases) past quarter:
- Fabric v2.5.10 - September 20, 2024
- Fabric v3.0.0 - September 17, 2024

# Overall Activity in the Past Quarter

The project delivered patch releases for the Fabric v2.5 long-term support release. The patch releases primarily include updates to third party dependencies. See [release notes](https://github.com/hyperledger/fabric/releases) for details.

The project also delivered the v3.0 release, see the release [announcement](https://www.lfdecentralizedtrust.org/announcements/version-3.0-of-hyperledger-fabric-an-lf-decentralized-trust-project-now-available). The headline feature in v3.0 is Byzantine Fault Tolerant support for the ordering service, using the SmartBFT consensus library. BFT support has been worked on for multiple years, so this was a major milestone fulfilling one of the early visions for Hyperledger Fabric. See the [SmartBFT blog article](https://www.lfdecentralizedtrust.org/blog/hyperledger-fabric-v3-delivering-smart-byzantine-fault-tolerant-consensus) for more details.

# Current Plans

The project continues to maintain and keep Fabric v2.5 and v3.0 branches current (release-2.5 and main branches). There have been great community contributions in the area of currency and improvements, even for some non-trivial updates that required refactoring across Fabric repositories, such as the recent update to v2 protocol buffers.

We intend to start publishing images to Github Container Registry, see the Questions for TAC above.

There are no new significant features currently planned. There have been some new features proposed, either at community meetings, initial pull requests, or in issues. However, they often don't make it beyond the starting block when we ask potential contributors to open a Request for Comment (RFC) with their design and development thoughts. 

# Maintainer Diversity

One retirement this quarter. 5 of 8 [Fabric core maintainers](https://github.com/hyperledger/fabric/blob/main/MAINTAINERS.md) from IBM.

The IBM maintainers have been less active recently. If there are users or developers interested in becoming more active contributors, and eventually maintainers, the project could use your help!

# Contributor Diversity

- 51% of code activities were performed by top 3 contributors. Remaining 49% performed by 101 other contributors.
- IBM contributors accounted for 83% of activity.
- Of top 10 contributors, 6 of 10 from IBM.

# Additional Information

[Insights dashboard link](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=fabric&routedFrom=Github&bestPractice=false&repository=all&dateFilters=2024-07-01%20to%202024-10-01&dateRange=2024-07-01%20to%202024-10-01&compare=PP&granularity=week&hideBots=true)