[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# 2025 Q3 Lockness

# Project Health

The project is in a healthy and active state, with development focused on two major efforts: a significant upgrade to the CGGMP core protocol and a foundational rework of the `round-based` library. The CGGMP update has already resulted in new alpha releases, while the crucial `round-based` update is a key work-in-progress. Our community is engaged and growing; questions are being answered on Discord and GitHub, and we've seen a new, highly active outside contributor make significant contributions this quarter.

[LFX Insights](https://insights.linuxfoundation.org/project/lockness/repository/lfdt-lockness)

# Questions/Issues for the TAC

In Discord, when people reach out to ask questions in the public channel, sometimes a scam bot tries impersonate stuff by posting a message like "please use this link to open a support ticket", and after a few minutes deletes a message. 

I'd like to bring your attention to this issue. Assuming other channels fall victim for this, it looks like a massive attack. It'd be great if we could deploy any countermeasures.

# Releases

* cggmp24 [github](https://github.com/LFDT-Lockness/cggmp21) [crates-io](https://crates.io/crates/cggmp24/0.7.0-alpha.1)
  * v0.7.0-alpha.1 (Published on: 2025-08-20)
* cggmp24-keygen [github](https://github.com/LFDT-Lockness/cggmp21) [crates-io](https://crates.io/crates/cggmp24-keygen/0.7.0-alpha.1)
  * v0.7.0-alpha.1 (Published on: 2025-08-20)
* paillier-zk [github](https://github.com/LFDT-Lockness/cggmp21) [crates-io](https://crates.io/crates/paillier-zk)
  * v0.7.0-alpha.1 (Published on: 2025-08-20)

# Overall Activity in the Past Quarter

We actively work on existing projects, adding new features, improving the codebase. Mainly, we were focused on improving `round-based` library, which is the central library in our tech stack that powers all MPC protocols. It gets better API, more features, and all MPC protocols in ecosystem will benefit from it (it's [WIP](https://github.com/LFDT-Lockness/round-based/pull/17)). Our other focus was updating our implementation of [CGGMP protocol](https://github.com/LFDT-Lockness/cggmp21) to latest revision of the paper it's based on. It features better performance and security. Upgrade is also WIP, but we're already released an `alpha.1` release.

In this quarter we had an active outside contributor who helped us a lot with CGGMP implementation update, see [his PRs](https://github.com/LFDT-Lockness/cggmp21/pulls?q=is%3Apr%20is%3Aclosed%20author%3Ajfdreis).

Many people reached out to us asking questions about protocols, through github issues and Discord, some of them were providing a helpful feedback for us.

# Current Plans

Current plan is to continue updating CGGMP protocol to latest revision, and wrapping up `round-based` update, and then updating all protocols that depend on it.

On admin side, we still have these items as to do:
* Add the OpenSSF Scorecard for each repository.
* Add an option for our users to reach out so they can be included in `ADOPTERS.md`.

# Maintainer Diversity

No changes in maintainers since last report.

# Contributor Diversity

No changes in contibutors since last report.

# Additional Information

None
