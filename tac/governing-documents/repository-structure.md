# Common Repository Structure

LF Decentralized Trust (LFDT) projects are required to maintain a standard set of files in each repository. This
document describes the required and recommended files.

## Required Files with Specified Content

Repositories MUST have these files with the specific content in the linked files, or a file with a
link to the specified content with minimal exposition. These files MUST be at the root of the
repository.

-   [`LICENSE`](https://www.apache.org/licenses/LICENSE-2.0.txt) (Unless an exception has been made by the LFDT Governing Board)
-   [`CODE_OF_CONDUCT.md`](./code-of-conduct.md)
-   [`SECURITY.md`](./security.md)

## Required Files with Variable Content

Repositories MUST have these files. Named files MUST be at the root of the repository, and may have
format suffixes such as `.md`, `.rst`, or `.txt`.

-   `README` \
    A description of the project and contain information or links to information such as
    -   A reference to the license (required).
    -   The current and important past releases
    -   Documentation for developers and users
    -   Suggestion for users to update the `ADOPTERS.md` file (see further below) upon awareness of practical usage
-   `MAINTAINERS` \
    A list of all current maintainers with contact info. [A separate document](./MAINTAINERS-file.md)
    covers the specifics.
-   `CONTRIBUTING` \
    Directions on how to contribute code to the project, or a pointer to that information.
    If a repository contains more than one CONTRIBUTING file, then the file shown in links is chosen from locations in the following order:
    the .github directory, then the repository's root directory, and finally the docs directory.
-   Continuous Integration / Continuous Delivery (CI/CD) configurations \
    Configurations needed to run CI/CD on LFDT Trust provided systems.

## Required Content in Home Page

The `README.md` in the root folder of the repository MUST display the following badges right below the title:

-   License: `![GitHub License](https://img.shields.io/github/license/:user/:repo)`
-   OpenSSF Best Practices: `[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/:project-id/badge)](https://bestpractices.coreinfrastructure.org/projects/:project-id)`
-   OpenSSF Scorecard: `[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/:user/:repo/badge)](https://scorecard.dev/viewer/?uri=github.com/:user/:repo)`

## Recommended

Repositories SHOULD have these files. Named files SHOULD be at the root of the repository.

-   `NOTICE`
    -   As per section 4, subsection (d), of the
        [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0)
-   License Header information in each source code file. \
    For new files added to LFDT repositories they SHOULD include the snippet `SPDX-License-Identifier: Apache-2.0` as part of the header.
    (see the [Copyright and Licencing Policy](https://wiki.hyperledger.org/display/TSC/Copyright+and+License+Policy))
-   Build files consistent with the implementation language, such as...
    -   For JavaScript/Node.js a `package.json` file
    -   For Ruby a `Gemfile` file
    -   For Java, one of a Maven `pom.xml`, an Apache Ant `build.xml`, or a Gradle `build.gradle`, file
    -   For Python `setup.py` and `requirements.txt` files
    -   For Go `go.mod` and optionally `go.sum`
    -   For Rust a `cargo.toml` file
    -   For multi-lingual repositories a `Makefile` or executable `build.sh` script
    -   For other languages, other standard build files a practitioner of the language would expect.
-   Testing code \
    Code to test the code in the repository (such as unit tests), in a location appropriate for the language.
    \
    Not all repositories can be tested (homebrew, docs), which is the only reason this is a SHOULD.
-   `ADOPTERS.md`
    -   Contains a list of notable usages of the project's releases and/or source code
    -   MUST contain publicly verifiable references in the form of URLs or article info
    -   Can be updated by maintainers as well as by adopters or any third party who is aware of adoption and can provide verifiable links.
    -   See [Defining Adopters](./defining-adopters.md) for more information on what an adopter is
-   `CHANGELOG` \
    A human-readable list of recent changes. Changes should at least include the current release. This
    file may be maintainer curated or mechanically produced. Consider making this file a link that points to
    the GitHub release notes.

## Prohibited

Repositories MUST NOT have these files.

-   Executable binaries and shared library files built by code in the repository \
    This includes `.exe`, `.dll`, `.so`, `.a` and `.dylib` files not otherwise part of a third party
    library.

# Tooling

In order to help automate checks a repolinter file and supporting scripts can be found in
[LFDT Community Management Tools](https://github.com/hyperledger-labs/hyperledger-community-management-tools/tree/main/repo_structure).

Note that this document takes precedence over documents in the folder linked above, wherever the instructions and tooling differ between the two.

## Community Standards Verification for GitHub based Projects

GitHub provides an Insights feature called Community Standards that helps ensure a repository adheres to recommended structural guidelines.
This feature is accessible via the Insights tab of a repository and evaluates whether the repository includes key components aligned with community best practices.

Specifically, the Community Standards tool checks for the presence of the following files and configurations, as outlined by the TAC's "must" and "recommended" criteria:

- Repository description
- README
- Code of Conduct
- Contribution guidelines (CONTRIBUTING)
- License file
- Security policy
- Issue templates
- Pull request templates
- Repository administrators' ability to receive content reports

For additional details, please refer to the [GitHub public documentation](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/accessing-a-projects-community-profile).
