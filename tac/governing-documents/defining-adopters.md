[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# Defining Adopters

## Introduction

The **ADOPTERS** file serves as a living registry of organizations — and occasionally individuals — that actively **adopt and use LFDT-hosted open source projects**. It differs from membership or contribution lists; rather, it showcases those who:

- **Use LFDT technologies internally or publicly**, integrating them into their systems, platforms, or services.
- Provide **real-world validation**, demonstrating that LFDT solutions are stable, scalable, and production-ready.
- May offer **feedback, use cases, or success stories**, helping guide project direction and priorities.

### Why It Matters

1. **Transparency & Credibility**  
   Displaying a diverse and growing list of adopters builds confidence in our ecosystem — signaling to others that LFDT projects are trusted and battle-tested.

2. **Community Insight**  
   The ADOPTERS file helps the LFDT Technical Steering Committee and governance bodies understand adoption trends, key use cases, and potential areas of improvement.

3. **Recognition & Encouragement**  
   Acknowledging adopters encourages broader involvement and can motivate organizations to deepen their collaboration with LFDT.

As LFDT continues to grow, maintaining an up-to-date ADOPTERS file will be instrumental in telling the story of our impact, forging stronger community bonds, and steering future development based on real-world usage.

## Definitions

Adopters of an LF Decentralized Trust (LFDT) project are organizations or communities that successfully leverage the project as intended—whether integrating it into their systems, building on top of it, or offering it as a foundational component of a service or solution.

To better understand how a project is adopted, we distinguish between **direct adopters** and **transitive adopters**. For example, if a service provider uses a decentralized identity project from LFDT as the backbone of a digital credentialing solution, the service provider is a *direct adopter*. If their customers use that solution without directly engaging with or deploying the underlying project, those customers are *transitive adopters*.

* **Direct adopters** are responsible for actively developing, packaging, configuring, or deploying the LFDT project as part of their use.

* **Transitive adopters** benefit from the project indirectly but are not responsible for its integration or operation. However, if a transitive adopter gains the ability to configure or extend the project due to the service provider’s implementation, they may become direct adopters as well.

The intent of identifying adopters within the LFDT community is to gain insight into real-world, production-level usage of its projects or specifications. This helps assess project maturity, community engagement, and long-term viability within the decentralized trust ecosystem.

In some cases, original sponsoring organizations or maintainers may also be recognized as adopters. The LFDT and the associated LFDT projects’ technical and community leadership reserves the discretion to determine whether an adopter can offer meaningful feedback to guide the evolution of a project.

Adopters of LFDT projects may include the following (noting that a single organization may fit more than one category):

* **Ecosystem Participant** – An organization actively engaged in developing, deploying, or operating one or more LFDT projects.

* **Service Provider** – An entity offering LFDT projects as part of a larger solution (e.g., a platform or product). This entity repackages an open source project as a core component of a service offering and sells decentralized trust services externally. Examples might include:  
  * APIs  
  * SaaS  
  * Blockchain networks both public and private cloud providers.   
  * Repackaged supported software

  NOTE: A Service Provider’s customers are considered transitive adopters and should be excluded from identification within the ADOPTERS.md file.

* **Upstream or Downstream Project** – An open source project that depends on or integrates with an LFDT project for functionality, compatibility, or supply chain inclusion.

* **End user** – A company or institution that uses an LFDT-hosted open source technologies internally to build, deploy, and operate software, systems, or services — but does not commercially distribute, support, or sell software derived from LFDT projects, nor sell related services or training. An end-user organization may not necessarily contribute upstream.

  An **end user** can also mean any individual or organization that utilizes or benefits from LFDT-hosted project deliverables, and may provide feedback, requirements, or real-world usage data to guide project direction and priorities.

* **Consultancy** - an entity whose purpose is to assist other organizations in developing a solution leveraging decentralized trust technology. They may be embedded in the end user team and are responsible for the execution of the service. Service Providers may also provide consultancy services, they may also package decentralized trust technologies for reuse as part of their offerings. These function as proxies for an end user.  
    
Projects may leverage the above guidelines to list organizations in their ADOPTERS.md file within their repo, projects are not required to identify the type of adopter in their ADOPTERS.md file; however, projects are encouraged to identify the category or categories each adopter fits under, but to list the adopter only once. This helps the LFDT community track usage patterns and adoption trends more effectively.

If you’re not sure if your organization falls into any of these categories you can ask in the \#tac discord channel, on the TAC mailing list, or email [tac@lists.lfdecentralized.org](mailto:tac@lists.lfdecentralizedtrust.org)  and we’ll help you.  

## ADOPTERS.md File

### Maintenance Guidelines

Projects are encouraged to keep their ADOPTERS file **accurate and up-to-date**. Adopters may wish to remove their usage from the ADOPTERS file, and the maintainers must allow pull requests to do so.  If the adopting organization cannot find the time to submit the pull request it is also acceptable for a maintainer of the project to create the adoption record's pull request and then have someone belonging to the adopting organization's GitHub account sign off in a PR comment. This way their required level of effort is minimized.

To ensure both transparency and respect for commercially sensitive information:

- **Self-submission is preferred**: Where possible, the adopter organization should submit the pull request (PR) to add or update their entry in the ADOPTERS file.
  This ensures explicit consent for their inclusion.
- **Commercial sensitivity**: Some organizations may be unable or unwilling to disclose their technology stack publicly. In such cases, maintainers should respect this decision and only add adopters that have given explicit permission.

###  Contribution Instructions

Contributions instructions should include:

1. **File location** – `ADOPTERS.md` in the root folder for ease of discoverability.
2. **Required fields**, such as:
     - Organization name
     - Link to public information or case study
     - Date of first known use
3. **Formatting guidance**, perhaps with a sample snippet
4. **Review Process** – indicate that PRs will be reviewed by the project maintainers for formatting, accuracy, or duplicates—but not added without the adopter’s explicit submission.
5. **Link to relevant governance benefits**, such as eligibility for steering committee roles (e.g., “Note: Being listed as an adopter may qualify your organization for certain governance participation, such as End User representation.”).

###  Example Entry

| Organization Name | Link | Date of First Use | Description |
| ----------------- | ---- | ----------------- | ----------- |
| **HashPack Inc.** | https://www.hashpack.app/ | 2020 | HashPack is a pioneering force in the Hedera ecosystem since 2020, developing critical infrastructure that enabled the growth of Hedera's retail DeFi ecosystem. As builders of wallet technology used by 95% of Hedera's retail users, HashPack brings essential perspective on user experience, developer needs, and technical implementation challenges that will inform Hiero's development priorities and adoption strategy.  (Added via self-submitted PR, YYYY-MM-DD) |
 
## References

- [CNCF Definitions](https://github.com/cncf/toc/blob/main/FAQ.md#what-is-the-definition-of-an-adopter)

- [Hiero Adopters.md](https://github.com/hiero-ledger/hiero/blob/main/ADOPTERS.md)
