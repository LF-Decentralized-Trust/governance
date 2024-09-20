---
layout: default
title:  Release Signing
parent: Governing Documents
grand_parent: LF Decentralized Trust TAC
nav_order: 10
---
[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# Securing and Verifying Releases

The LF Decentralized Trust (LFDT) emphasizes a structured approach to governance, particularly in the context of artifact signing for its projects. Artifacts, which are essential outputs from each release, include binaries, container images, checksum files, documentation, provenance metadata, and software bills of materials (SBOM).

LFDT has a holistic approach to governing the security of projects and implements the highest levels of standards. The objective is to establish a consistent and secure approach to signing artifacts, leveraging industry-standard tools and practices while allowing flexibility for individual project implementations. Software verification processes are made available to ensure the integrity and authenticity of all artifacts throughout their lifecycle. A monitoring framework is introduced to score the project, rating the release process.

This policy aligns with efforts to establish a secure software supply chain for LFDT projects and achieve full [SLSA (Supply Chain Levels for Software Artifacts) compliance](https://slsa.dev/spec/v1.0/levels) in the release process.

This governance framework prioritizes understanding the "what" of artifact signing, which includes:
- The importance of signing artifacts to ensure their integrity and authenticity.
- The necessity of meeting security standards, such as SLSA compliance.

The technical "how" of implementing will be left to the discretion of individual projects, allowing for flexibility and innovation.

## LFDT Project Compliance

1. The LFDT Technical Advisory Committee (TAC) standardizes the signing of artifacts and confirmation of signing using tools from the Linux Foundation’s digital signing project, Open Source Security Foundation (OpenSSF) -- [OpenSSF Sigstore](https://openssf.org/projects/sigstore/) and [OpenSSF Scorecard](https://openssf.org/projects/scorecard/), respectively.
2. Each project must document the process of signing and verifying the artifacts using [OpenSSF Sigstore](https://openssf.org/projects/sigstore/) in a file called `RELEASE.md`.
3. Each project must enable and apply for an [OpenSSF's scorecard](https://openssf.org/projects/scorecard/). The project must capture the scorecard's result and generate a badge visible on the `README.md` file.
4. An LFDT incubation project must meet at least SLSA Level 1, while graduated projects must meet at least SLSA Level 2. Reference [SLSA guidelines](../guidelines/slsa-guidelines.md) to know if your project is compliant.

## Responsibilities
- **Project Team:**
  - Add a `RELEASE.md` file containing the build and release process of artifacts. Capture the information such as versioning followed, steps to reproduce the build, current release process, resources for verifying the signed artifacts at the least.
  - Generate the scorecard and upload as a badge on `README.md` file.
  - Each project will be responsible for the technical integration of Sigstore's cosign and OpenSSF's scorecard into its build process. This approach allows projects to adapt the implementation to their specific needs while adhering to the overarching governance framework.
  - Projects may opt to utilize existing infrastructure, such as Rekor, to record immutable copies of their build artifacts. This adds an additional layer of integrity and auditability to the signing process.
  - Enable tools, process and scans to catch the unintentional leakage of build secrets.
  - Enable branch protection rules for monitoring artifact releases.
- **LFDT Staff:**
  - The LFDT staff will maintain and secure the signing keys and the relevant infrastructure necessary for managing these keys. This centralization ensures a high level of security and reliability for key management practices.
  - Scan for SBOM compliance.
