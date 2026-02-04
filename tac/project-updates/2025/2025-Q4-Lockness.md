[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2025 Q4 Lockness

# Project Health
The project remains in a healthy, active state, highlighted by the release of a major CGGMP24 update that addresses disclosed vulnerabilities and proactively implements significant security enhancements. A key achievement this quarter was the removal of the default dependency on an AGPL library, which is now an opt-in feature for users requiring higher performance, thereby improving licensing flexibility. Additionally, the team is continuing its work on refactoring the fundamental `round-based` library to upgrade its API and feature set, alongside delivering various minor improvements across the ecosystem.

[LFX Insights](https://insights.linuxfoundation.org/project/lockness/repository/lfdt-lockness)

# Questions/Issues for the TAC

We still have not submitted Q2 report. Given that we submitted Q3 updates cover Q2 as well, it's difficult to prioritize this and allocate time. Happy to discuss this though.

# Releases

* cggmp21 [github](https://github.com/LFDT-Lockness/cggmp21) [crates-io](https://crates.io/crates/cggmp21)
  * v0.6.3 (Published on: 2025-11-24)
* cggmp24 [github](https://github.com/LFDT-Lockness/cggmp21) [crates-io](https://crates.io/crates/cggmp24/0.7.0-alpha.1)
  * v0.7.0-alpha.2 (Published on: 2025-11-24)
  * v0.7.0-alpha.3 (Published on: 2025-11-26)
* cggmp24-keygen [github](https://github.com/LFDT-Lockness/cggmp21) [crates-io](https://crates.io/crates/cggmp24-keygen/0.7.0-alpha.1)
  * v0.7.0-alpha.2 (Published on: 2025-11-24)
  * v0.7.0-alpha.3 (Published on: 2025-11-26)
* fast-paillier [github](https://github.com/LFDT-Lockness/fast-paillier) [crates-io](https://crates.io/crates/fast-paillier)
  * v0.2.0 (Published on: 2025-11-03)
  * v0.3.0 (Published on: 2025-11-05)
  * v0.3.2 (Published on: 2025-11-25)
* paillier-zk [github](https://github.com/LFDT-Lockness/paillier-zk) [crates-io](https://crates.io/crates/paillier-zk)
  * v0.4.3 (Published on: 2025-11-24)
  * v0.7.0-alpha.2 (Published on: 2025-11-24)
  * v0.7.0-alpha.3 (Published on: 2025-11-26)
* udigest [github](https://github.com/LFDT-Lockness/udigest) [crates-io](https://crates.io/crates/udigest)
  * v0.2.3 (Published on: 2025-09-24)
  * v0.2.4 (Published on: 2025-10-22)
  * v0.3.0 (Published on: 2025-10-24)
* udigest-derive [github](https://github.com/LFDT-Lockness/udigest) [crates-io](https://crates.io/crates/udigest-derive)
  * v0.3.2 (Published on: 2025-10-22)
  * v0.4.0 (Published on: 2025-10-24)
* round-based [github](https://github.com/LFDT-Lockness/round-based) [crates-io](https://crates.io/crates/round-based)
  * v0.5.0-alpha.1 (Published on: 2025-09-26)
* round-based-derive [github](https://github.com/LFDT-Lockness/round-based) [crates-io](https://crates.io/crates/round-based-derive)
  * v0.5.0-alpha.1 (Published on: 2025-09-26)

# Overall Activity in the Past Quarter

Development was focused on releasing a big CGGMP24 update that addresses disclosed vulnerabilities and proactively enhances security by adding many more security improvements. See the [blog post](https://www.dfns.co/article/cggmp21-vulnerabilities-patched-and-explained) that covers this update.

We also dedicated a lot of time into removing a dependency on the only AGPL library in our dependency tree. Since `cggmp24 v0.7.0-alpha.3`, AGPL dependency is exluded from the build by default, with the ability to opt in for users who require better performance and are okay with the licensing.

There's ongoing work that comes from previous quarter, that is reworking some fundamental concepts of `round-based` library, which is the central library in our tech stack that powers all MPC protocols. We are working on improving API, adding more features.

Other minor changes and improvements were made in ecosystem of our libraries.

# Current Plans

Development-wise, the plan is stable release of cggmp24 and round-based libraries.

On admin side, we still have these items as to do:
* Add the OpenSSF Scorecard for each repository.
* Add an option for our users to reach out so they can be included in `ADOPTERS.md`.

# Maintainer Diversity

No changes in maintainers since last report.

# Contributor Diversity

No changes in contibutors since last report.

# Additional Information

None
