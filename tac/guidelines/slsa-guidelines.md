[//]: # (SPDX-License-Identifier: CC-BY-4.0)

## Supply Chain Levels for Software Artifacts Recommendations

As a general rule of guidance, the project may ask the following questions to determine the Supply Chain Levels for Software Artifacts (SLSA) compliance level.

### SLSA Level 1
The focus is on documenting the build and artifact release process. The goal is to have an audit record of incorporating new processes.
- Is the build environment and tools documented?
- Is the project leveraging automated security checks to identify vulnerabilities in the build process?
- Is there version control in place for the source code and build scripts?
- Are all changes to the build process tracked and reviewed by authorized personnel?
- Do you have a release process, and are you granting access only to the maintainers, following the principles of least privilege for generating the artifacts?

### SLSA Level 2
The focus is to ensure that the artifacts generated are verifiable. Any tampering in the generated artifacts must be caught by the user of the artifacts.
- Is the signing process incorporated for the artifacts?
- Is the signing integrated into the CI pipeline?
- Is auditing in place for regularly monitoring and auditing the signing practices and build process?
- Is a trusted tool (e.g., cosign) used to sign the artifacts?
- Is the build process reproducible, ensuring that the build generates consistent artifacts from the same source code?
- Is there provenance metadata that details how each artifact was built and its dependencies?

### SLSA Level 3
The focus is to ensure that the build environment is verified and trusted.
- Is there access control implemented to secure the build environment?
- Do you validate the signatures and checksums of all dependencies before ingesting them in the build stage?
- Do you sign the output of every step in your build pipeline to provide a verifiable guarantee?
- Do you use separate build workers/containers for each step in your build pipeline?
- Do you network isolate your build workers and pipeline as much as possible?
- Are you securing the keys and injecting them just in time?
- Are you leveraging an immutable record for the verification of signed artifacts?
