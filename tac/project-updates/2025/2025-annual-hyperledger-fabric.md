---
layout: default
title: 2025 Annual Review Hyperledger Fabric
parent: 2025
grand_parent: Project Updates
---

## Project Health

Hyperledger Fabric is fairly mature and stable with a v2.5 long-term support (LTS) release and a new v3.0 release.
There is less churn and fewer commits than in years past, with continued focus on quality, maintenance, and support.
New features get proposed, approved, and implemented based on a community RFC process.
Mailing list activity is down a bit compared to prior years.
PRs and mailing list questions are generally turned around quickly.
There is significant Discord activity.

[LFX Insights report for 2024](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=fabric&routedFrom=Github&bestPractice=false&repository=all&dateFilters=Last%20Year&dateRange=2024-01-01%20to%202024-12-31&compare=PP&granularity=month&hideBots=true)

Highlights from the 2024 Insights report:
- 373 contributors (-11% from 2023)
- 1662 commits (+29% from 2023)
- 52% of code activities were performed by 5 people (3 of the 5 from IBM)
- 80% of code activities were performed by 1 organization (IBM)
- Total of 38 organizations contributed, which indicates that there are many contributors and organizations with small contributions

## Maintainer Diversity

The project made good progress around maintainer diversity in the last year:
- 5 of 9 maintainers of core Fabric are from IBM (7 of 8 were IBM in 2023)

A minority of the maintainers account for the majority of the maintainer activity, therefore the project would still encourage additional Fabric users and contributors to increase activity and become maintainers.
The project is happy to mentor anybody interested in becoming a contributor or future maintainer.

[Maintainers file for core Fabric](https://github.com/hyperledger/fabric/blob/main/MAINTAINERS.md)

## Project Adoption

Based on what we see in mailing list and Discord there is significant adoption activity.
Several large vendors and several smaller companies have commercial offerings based on Hyperledger Fabric, as well as consulting services.
The project does not maintain an ADOPTERS file since it is difficult to keep the information up-to-date and the project doesn't want to misrepresent reality or give preference to certain vendors (deployments that want to publicize their adoption typically have press releases which are already searchable).

## Goals

### Performance Against Prior Goals

2024 goals:
- Shift users to Fabric v2.5 as the actively maintained long-term support (LTS) release, and to Gateway SDKs as the actively maintained SDKs (GOOD PROGRESS - v2.5 is the sole LTS release currently and many users have shifted to it)
- Provide maintenance releases at least quarterly (SUCCESSFULLY COMPLETED AND ONGOING)
- Release Fabric v3.0 with a production quality byzantine fault tolerant ordering service (SUCCESSFULLY COMPLETED)
- Increase diversity of maintainers (SUCCESSFULLY COMPLETED AND ONGOING)

Other accomplishments:
- Completed transition to Github Actions
- New Hyperledger Fabric Certified Practitioner exam and associated Hyperledger Fabric Design, Develop and Deploy training course sponsored by LF Decentralized Trust
- OpenSSF Scorecard was significantly improved in 2024 for the core Fabric runtime repository

### Next Year's Goals

- Continue to provide maintenance releases at least quarterly for v2.5.x and v3.x.
- Publish images to Github Container Registry as the primary registry, while maintaining Dockerhub for existing users.
- Improve OpenSSF Scorecard for other priority repositories (e.g. fabric-ca, fabric-chaincode-go, fabric-gateway SDK).
- Encourage contributions from community.
- Continue to increase diversity of maintainers.

### Help Required

We continue to work with LFDT staff to identify contributors and potential maintainers.

## Project Lifecycle Status Recommendation

Graduated status still makes sense for Hyperledger Fabric.