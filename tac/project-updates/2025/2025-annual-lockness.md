---
layout: default
title: 2025 Annual Review Lockness
parent: 2025
grand_parent: Project Updates
---

## Project Health

Lockness is not yet onboarded to LFX Insights.

## Maintainer Diversity

We currently have two maintainers: [@survived] and [@maurges] from Dfns. Maintainers did not change since the last year.

Maintainers file per projects:
* CGGMP21: https://github.com/LFDT-Lockness/cggmp21/blob/m/MAINTAINERS.md
* givre: https://github.com/LFDT-Lockness/givre/blob/m/MAINTAINERS.md
* round-based: https://github.com/LFDT-Lockness/round-based/blob/m/MAINTAINERS.md
* etc.

[@survived]: https://github.com/survived
[@maurges]: https://github.com/maurges

## Project Adoption

We see that several companies that are trying out our project: they reach out to us asking questions about the project. We don't know for sure if any company is using the project in production (except ourselves).

## Goals

### Performance Against Prior Goals

In [project proposal](https://github.com/dfns/hyperledger-hip-private/blob/proposal/HIPs/incubation/xkey.md), we set and accomplished following goals:

- [x] Develop a framework for writing MPC protocols, reducing boilerplate and making the code easy to
  write and read.
- [x] Develop a library for generic elliptic curve cryptography, enabling seamless curve switching and
  secure arithmetic operations, while managing small subgroups and memory security.
- [x] Develop primitives and ZK proofs like Schnorr Proof of Knowledge, unambiguous hashing,
  secret sharing, and more.
- [x] Develop applied libraries like fast Paillier encryption, using CRT to speed up (de)encryption
  and homomorphic operations, among others.

The ultimate goal of the proposal was to make developing and maintaining TSS/MPC protocols 
easier: improve their reliability, readability, and security. That's a long-standing core
value that we continue to promote.

### Next Year's Goals

We want to continue building an ecosystem for TSS/MPC protocols, and contributing more MPC/TSS implementations to the project to cover
more cryptographic primitives and use-cases.

Our (vague) plans:
- Improve `round_based` framework (that we use for building MPC/TSS protocols) to make it even more ergonomic, provide functionalities
  like running a sub-protocol, echo-broadcast, etc.
- Maintain existing protocols, keep them up-to-date with their papers (e.g. update CGGMP21 to the latest paper revision)
- Contribute more protocols, like threshold Diffie-Hellman
- Explore Hierarchical Threshold Signing Schemes and their applicability in existing TSS protocols
- Host a few talks/workshops

### Help Required

We keep up with the technical part of our duty (maintaining the code, delivering new features), but we're not at the capacity to do community work, e.g. host workshops or talks. Not sure if TAC can help us with that, but it would be helpful if we had a platform for talks/workshops once we have capacity for that.

## Project Lifecycle Status Recommendation

We suggest to keep the project status "Graduated".
