---
layout: default
title: 2025 Q2 Hyperledger Bevel
parent: 2025
grand_parent: Project Updates
---

# Project Health

The Bevel project is currently in a stable maturity state. Recently, we have updated some CI workflows and fixed typos. Our most significant improvement is a new logging system to improve visibility and facilitate easier debugging of playbook executions. This enhancement is still under review and was contributed by an external contributor.

There has been less commit and PR activity compared to the previous quarter, as we are currently focusing more on stability and support, including responding to questions in our Discord channel. We are still aiming to introduce Fabric version 3.0, and since we need help with the development, we hope to achieve this with support from our maintainers and new contributions coming through the mentorship program.

# Questions/Issues for the TAC

None

# Releases

[Releases](https://github.com/hyperledger/bevel/releases) during the quarter:
- Bevel Release v1.3.0 - April 1, 2025

[Releases](https://github.com/hyperledger-bevel/bevel-operator-fabric/releases) during the quarter:
- Bevel Operator Fabric Version 1.11.2 - Feb 11, 2025


# Overall Activity in the Past Quarter

The project delivered the Bevel 1.3.0 release on April 1st, 2025. For this release, we added multi-organization support for Substrate and implemented several bug fixes and enhancements for Besu and Quorum, including compatibility updates for MySQL 8.0+.
Also fixed documentation typos and resolved deployment issues related to the orderer chart on Minikube.

Furthermore, we have improved logging and error messaging across the Bevel codebase to enhance visibility and debugging capabilities for Fabric playbooks.
We addressed prior gaps in diagnostics, making playbook execution issues easier to identify and resolve.

# Current Plans

The main goal is to add support for Fabric 3.0.

By using bevel-operator-fabric you can handle this, but our aim is to update the source code in order to deploy Fabric 3.0 on the cloud using the Helm Charts standalone way or running the Bevel playbooks.

Furthermore, some users have experienced difficulties to deploy the chaincode operations for Fabric, and we are planning to fix the bugs with the help of the contributors who are experiencing the issues.

As Besu has been our other most deployed DLT using Bevel, we also have in sight to update our Helm Charts to support 25.4.0 version of Besu.

# Maintainer Diversity

[Bevel core maintainers](https://github.com/hyperledger/bevel/blob/main/MAINTAINERS.md) 2 maintainers from Accenture, 1 from Cheqd and 1 from Walmart India.

We are always open to welcoming new contributors and hope to see that number grow in the coming months. We have had new contributors this quarter who have made valuable implementations.
