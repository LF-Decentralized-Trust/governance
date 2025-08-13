[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2025 Annual Review Identus

## Project Health

LF Decentralized Trust Identus [LFX Insights Dashboard](https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/reports/contributors?project=identus&bestPractice=false&dateFilters=Last%20Year&dateRange=2024-01-01%20to%202024-12-31&compare=PP&granularity=month&hideBots=true&repository=all)
The project is relatively new to the LF Decentralized Trust Ecosystem and is mainly supported by the IOG maintainers.
At the same time, over the past year, we have seen several new contributors and evidence of usage of the Identus platform by other companies: 
- https://socious.io/, Socious production use case.
- https://ahau.io/, Ahau PoC.
- https://blocktrust.dev/, - identity wallet.

We currently utilize two Discord servers: the LF Decentralized Trust Discord and the private Identus Discord server. 
The Identus Discord has seen significantly more engagement. 
Since January 2024, our membership has grown from 258 to 476 members. 
On average, there are 348 activities across various channels monthly, with about 39 users online daily.

## Maintainer Diversity

There are currently 10 maintainers from IOG and other companies. 

The MAINTAINERS.md file is up to date and can be found [here](https://github.com/hyperledger/identus/blob/main/MAINTAINERS.md)
The `identus-maintainers` [team](https://github.com/hyperledger/governance/blob/main/access-control.yaml#L625-L655) includes around 10 members from IOG and other companies.

The number of active maintainers has decreased due to restructuring the Atala Team at IOG. 
However, the diversity of maintainers has increased over the past six months, with more companies contributing to the project.

## Project Adoption

Several companies are using the Identus project for prototyping and production use cases.

The following companies are using the project:
- https://socious.io/, Socious production use case.
- https://ahau.io/, Ahau PoC.
- https://blocktrust.dev/, - identity wallet.

Developers actively participate in the weekly meetings and consider using the Identus platform for their use cases.

## Goals

### Performance Against Prior Goals

The current project roadmap is public and can be found here: [Identus Roadmap](https://github.com/orgs/hyperledger/projects/48)  

During the last six months, the project has achieved the following goals:
- Connectionless Issuance and Verification of VC via DIDCommV2
- DID Prism AnonCreds method to resolve the resources from the DID Prism URL (for the schema and credential definition)
- Crypto Agility of the DID Prism Method (added Ed25519 cryptography suite)
- Transitioning the project from the IOHK to the LF Decentralized Trust organization
- OID4VCI specification implementation in the Cloud Agent and SDKs (for JWT VC only)
- Major refactoring:
-- a. improved error handling in the Cloud Agent, the Mediator, and SDKs,
-- b. added Problem Report protocol to other protocols,
-- c. Background jobs are replaced with the message queue (in-memory or Kafka)
- SD-JWT-VC implementation in the Cloud Agent and SDKs
- Status List revocation implementation in JWT VC
- Improved documentation with the Quick Start Guide and Tutorials

The roadmap is actively discussed with the community members in the GitHub [Discussions](https://github.com/hyperledger/identus/discussions)

### Next Year's Goals

The project has the following strategic goals for the next year:
- Reduce maintenance cost and complexity of the Identus platform
- Increase the Identus platform adoption by the developers and companies
- Improve the platform interoperability with other SSI platforms
- Improve the platform documentation and tutorials

The following features are planned for the next year, among others:
- Cardano Identus VDR
- Bring Issuance capabilities to the SDKs
- Continue with UAS Wrapper implementation
- Pollux Plugin abstraction SDK
- OIDC specifications for the SSI: OID4VCI, OID4VP, SIOP2.0
- Authentication using the PRISM DID method

### Help Required

LF Decentralized Trust can help with the following:
- Promote the Identus project within the LF Decentralized Trust community
- Help with the workshops and hackathons
- Help to collaborate with the LF Decentralized Trust Aries project as the Identus platform leveraging the Aries specs and protocols


## Project Lifecycle Status Recommendation

The Identus is a reasonably new incubation project in the LF Decentralized Trust Ecosystem and should remain so.


## Identus Annual Review 2025 Notes from the TAC

[TAC Meeting Recording 2025.01.30](https://zoom.us/rec/play/HBFR6uCLwhy7qUxqHGAhLGjvBbgZSklBtGzVnB7js1EIZDvqqJUq3FIY4wM36zCWm6RIREsHwi7dNd-D.L53jN2jLjtRD7WUL?canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fzoom.us%2Frec%2Fshare%2Fw3bujVyRZRw8UDKGjc5Y-JRF1MVzhBNNt0u0BTdtyWdVbjU56jGk1snGiNjyTq1D.5MKrIQkwxw3H-Bd1) -- Identus Annual report discussion starts at the 29:44 mark.

__TAC Reviewers__: Venkatraman Ramakrishna (primary), Matthew Whitehead (secondary)

### Project Health

- Overall, the project seems to be in good health as indicated in the review and by looking at the development activity in the project's repositories. Here are the caveats:
  * A problem we found was that the repositories had not been moved to the new org, so LFX Insights did not reveal anything meaningful about the project.
  * Also, the repositories are not being tracked by the OpenSSF Scorecard, so we can't see how well the project is performing on several OpenSSF metrics.
- There's a decent amount of community interest and participation, as indicated by observing the activity in Discord and the mailing list, and watching the replays of their recent community calls.
- Discord channels are easonably well structured, indicating that the project is active enough to need separate channels for high-level topics.
- Frequent releases are being published for the various Identus components.
- The documentation looks very well-done and comprehensive.
- The fact that the Identus platform is being used in three distinct use cases by other companies indicates the interest in the project as well as its utility, which is a good sign for a project in the incubation stage.
- Produced their annual report ahead of schedule which shows their level of engagement as a project.
- There are 3 distinct organizations from which the project's maintainers are drawn, but there's a significant skew toward IOG (8 out of 10 maintainers). It's not possible to tell how diverse the code contributions are because the LFX Insights dashboard is not configured for the code repositories yet.

### Recent Maintenance Activity and Progress

- As a new incubating project, there is a lot of development activity that is identifiable by inspection of the repositories, which supports the points made in the review by the project's maintainers.
- We can see a lot of PRs having ben approved over time with relatively few outstanding PRs, indicating active and timely maintenance.
- The project plan indicates several tasks that have been fulfilled, currently worked on, or in the pipeline. This, in addition to the notes made in the review, indicate that the maintainers have identified specific features and improvements and have actively been fulfilling these over time.
- There is no roadmap defined at a somewhat macro level, i.e., which tells us how the overall Identus platform and its components are supposed to be evolving as per the maintainers' visions. What we see in the roadmap link provided in the review is a set of low-level GitHub issues.

### Compliance with Hyperledger Project Lifecycle Criteria

- There are no red flags when it comes to development and maintenance activity, but none of the project's repositories have the OpenSSF Best Practices and OpenSSF Scorecard badges enabled. This should be fixed ASAP.
- Should remain in Incubated status as requested by the maintainers in the review.

### Suggestions for Improvement

- As mentioned earlier, migrate the repositories to the new organization so we can track its health using LFX Insights, enable the OpenSSF Best Practices Badge, and enable the OpenSSF Scorecard badge so we can identify the precise metrics on which the project is lacking.
- Try to increase maintainer diversity over time (currently skewed toward IOG).
- The documentation looks good, but do strive to create a process for community-driven feature proposals and brainstorming. As a suggestion, several LFDT projects do this using project-specific RFCs, which you can support within a folder or a separate repository.
- Maintain a high-level ROADMAP.md file in your main repository ('identus') that spells out your vision and a near- or medium-term plan in plain language and illustrations.

### General Recommendations

- Do try to collaborate with other projects in your space, like Aries or CREDEBL. Avoid reinventing the wheel and leverage dependencies instead, keeping the code as modular and reusable as possible. (The project has done a good job of this so far!).
- To promote the project, write blog articles and deliver talks/demos or run workshops with LFDT staff's help.
- Keep connections with the W3C standardization community and strive for compliance with those standards.
