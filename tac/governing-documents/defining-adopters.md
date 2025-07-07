---
layout: default
title: Defining Adopters
parent: Governing Documents
grand_parent: LF Decentralized Trust TAC
---
[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# Defining Adopters

Adopters of an LF Decentralized Trust (LFDT) project are organizations or communities that successfully leverage the project as intended—whether integrating it into their systems, building on top of it, or offering it as a foundational component of a service or solution.

To better understand how a project is adopted, we distinguish between **direct adopters** and **transitive adopters**. For example, if a service provider uses a decentralized identity project from LFDT as the backbone of a digital credentialing solution, the service provider is a *direct adopter*. If their customers use that solution without directly engaging with or deploying the underlying project, those customers are *transitive adopters*.

* **Direct adopters** are responsible for actively developing, packaging, configuring, or deploying the LFDT project as part of their use.

* **Transitive adopters** benefit from the project indirectly but are not responsible for its integration or operation. However, if a transitive adopter gains the ability to configure or extend the project due to the service provider’s implementation, they may become direct adopters as well.

The intent of identifying adopters within the LFDT community is to gain insight into real-world, production-level usage of its projects or specifications. This helps assess project maturity, community engagement, and long-term viability within the decentralized trust ecosystem.

In some cases, original sponsoring organizations or maintainers may also be recognized as adopters. The LFDT and the associated LF/DT projects’ technical and community leadership reserves the discretion to determine whether an adopter can offer meaningful feedback to guide the evolution of a project.

Adopters of LFDT projects may include the following (noting that a single organization may fit more than one category):

* **Ecosystem Participant** – An organization actively engaged in developing, deploying, or operating one or more LFDT projects.

* **Service Provider** – An entity offering LFDT projects as part of a larger solution (e.g., a platform or product).

* **Upstream or Downstream Project** – An open source project that depends on or integrates with an LFDT project for functionality, compatibility, or supply chain inclusion.

* **End-user Organization** – A company or institution that uses an LFDT project to power part of its infrastructure, services, or internal workflows, without necessarily contributing upstream.

When documenting adopters (e.g., in an `ADOPTERS.md` file), projects are encouraged to identify the category or categories each adopter fits under, but to list the adopter only once. This helps the LFDT community track usage patterns and adoption trends more effectively.

* End users \- companies and organizations that are not LFDT End-User members that use the project and decentralized trust technologies internally, or build upon a decentralized trust open source project but do not sell the decentralized trust project externally as a service offering. This group is identified in the written form by the convention end user, uncapitalized and unhyphenated.  
* A Service Provider \- a Service Provider is an organization that repackages an open source project as a core component of a service offering and sells decentralized trust services externally. Examples might include:  
  * APIs  
  * SaaS  
  * Blockchain networks both public and private~~cloud providers~~.   
* Consultancy \- an entity whose purpose is to assist other organizations in developing a solution leveraging decentralized trust technology. They may be embedded in the end user team and are responsible for the execution of the service. Service Providers may also provide consultancy services, they may also package decentralized trust technologies for reuse as part of their offerings. These function as proxies for an end user.  
    
  NOTE: A Service Provider’s customers are considered transitive adopters and should be excluded from identification within the ADOPTERS.md file.

Projects may leverage the above guidelines to list organizations in their ADOPTERS.md file within their repo, projects are not required to identify the type of adopter in their ADOPTERS.md file.

If you’re not sure if your organization falls into any of these categories you can ask in the \#tac discord channel, on the TAC mailing list, or email [tac@lists.lfdecentralized.org](mailto:tac@lists.lfdecentralizedtrust.org)  and we’ll help you.  

## References

- [CNCF Definitions](https://github.com/cncf/toc/blob/main/FAQ.md#what-is-the-definition-of-an-adopter)

- [Hiero Adopters.md](https://github.com/hiero-ledger/governance/blob/main/elections/ADOPTERS.md)
