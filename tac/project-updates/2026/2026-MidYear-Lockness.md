[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2026 Mid-Year Lockness Report

# Project Health
The project remains in a healthy, active state: [LFX Insights](https://insights.linuxfoundation.org/project/lockness/repository/lfdt-lockness).

We updated our project to be compliant with LFDT requirements: now every repo has OpenSSF scorecard (and we worked on improving the score across all repos), maintainers file, contribution and security guidelines, etc. We have also finally accepted [the technical charter](https://github.com/LFDT-Lockness/governance/blob/main/charter.md), and founded the [Technical Steering Committee](https://github.com/LFDT-Lockness/governance/blob/main/MAINTAINERS.md).

We released a new MPC protocol: [tecdh](https://github.com/lfdt-lockness/tecdh), threshold Elliptic Curve Diffie-Hellman protocol. We did a few other releases shipping new features and bug fixes. We have accepted interesting incoming contributions. In parallel, we're also working on a new project: coordinated networking layer designed for MPC protocols. It has been [submitted to NIST](https://csrc.nist.gov/csrc/media/Projects/threshold-cryptography/documents/TCall-1/Dfns-CoordMPC-PW02.pdf) for [MPTC program](https://csrc.nist.gov/projects/threshold-cryptography). It's planned for opensourcing in Lockness in Q4/Q1.

# Questions/Issues for the TAC

Now that we have OpenSSF scorecards, is there any other LFDT requirement that the Lockness project is not compliant with?

# Releases

* givre [github](https://github.com/LFDT-Lockness/givre) [crates-io](https://crates.io/crates/givre)
  * v0.3.0 (Published on: 2026-08-12)
* tecdh [github](https://github.com/LFDT-Lockness/tecdh) [crates-io](https://crates.io/crates/tecdh)
  * v0.3.0 (Published on: 2026-08-12)
  * v0.2.0 (Published on: 2026-03-27)
* generic-ec [github](https://github.com/LFDT-Lockness/generic-ec) [crates-io](https://crates.io/crates/generic-ec)
  * v0.5.2 (Published on: 2026-08-06)
  * v0.5.1 (Published on: 2026-07-14)
  * v0.5.0 (Published on: 2026-03-20)
* generic-ec-zkp [github](https://github.com/LFDT-Lockness/generic-ec) [crates-io](https://crates.io/crates/generic-ec-zkp)
  * v0.5.0 (Published on: 2026-03-20)
* generic-ec-core [github](https://github.com/LFDT-Lockness/generic-ec) [crates-io](https://crates.io/crates/generic-ec-core)
  * v0.3.0 (Published on: 2026-03-20)
* generic-ec-curves [github](https://github.com/LFDT-Lockness/generic-ec) [crates-io](https://crates.io/crates/generic-ec-curves)
  * v0.3.0 (Published on: 2026-03-20)
* cggmp24 [github](https://github.com/LFDT-Lockness/cggmp24) [crates-io](https://crates.io/crates/cggmp24)
  * v0.7.0-alpha.4 (Published on: 2026-03-23)
* cggmp24-keygen [github](https://github.com/LFDT-Lockness/cggmp24) [crates-io](https://crates.io/crates/cggmp24-keygen)
  * v0.7.0-alpha.4 (Published on: 2026-03-23)
* paillier-zk [github](https://github.com/LFDT-Lockness/cggmp24) [crates-io](https://crates.io/crates/paillier-zk)
  * v0.7.0-alpha.4 (Published on: 2026-03-23)
* key-share [github](https://github.com/LFDT-Lockness/cggmp24) [crates-io](https://crates.io/crates/key-share)
  * v0.7.0 (Published on: 2026-03-23)
* generic-ecies [github](https://github.com/LFDT-Lockness/generic-ecies) [crates-io](https://crates.io/crates/generic-ecies)
  * v0.3.0 (Published on: 2026-07-15)
* rand_hash [github](https://github.com/LFDT-Lockness/rand_hash) [crates-io](https://crates.io/crates/rand_hash)
  * v0.3.0 (Published on: 2026-07-13)
  * v0.2.0 (Published on: 2026-07-15)
* hd-wallet [github](https://github.com/LFDT-Lockness/hd-wallet) [crates-io](https://crates.io/crates/hd-wallet)
  * v0.7.0 (Published on: 2026-03-23)
* udigest [github](https://github.com/LFDT-Lockness/udigest) [crates-io](https://crates.io/crates/udigest)
  * v0.4.0 (Published on: 2026-02-19)
* udigest-derive [github](https://github.com/LFDT-Lockness/udigest) [crates-io](https://crates.io/crates/udigest-derive)
  * v0.5.0 (Published on: 2026-02-19)

# Current Plans

* Mentorship project: weekly calls with mentees, design and code reviews
* Coordinated networking layer for MPC protocols:
  * The write-up is already [submitted to NIST](https://csrc.nist.gov/csrc/media/Projects/threshold-cryptography/documents/TCall-1/Dfns-CoordMPC-PW02.pdf) for [MPTC program](https://csrc.nist.gov/projects/threshold-cryptography)
  * Finish the submission: formal description of the protocol, security proofs
  * Opensourcing is planned for Q4/Q1
* Work on adoption of `round-based`, our MPC framework, among researchers: provide tools for benchmarking, guides, preferrably give talks about it on conferences.

# Maintainer Diversity

We have 3 maintainers, all of them from the same company.

No changes in maintainers since last report.

# Contributor Diversity

No changes in contibutors since last report.

# Additional Information

None
