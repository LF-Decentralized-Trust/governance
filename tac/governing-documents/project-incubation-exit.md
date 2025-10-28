[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# Project Incubation Exit Criteria

## Introduction

LF Decentralized Trust has defined a [lifecycle](./project-lifecycle.md) for its
projects.

This definition specifies the evaluation criteria for a project to be able
to transition from the *Incubation* phase to the *Graduated* phase. These
are listed in the [evaluation section of the project lifecycle document](./project-lifecycle.md#evaluation-of-criteria-for-state-transition-decisions)
(see criteria in box (1)) as follows:

- Legal
- Diversity (>=3 maintaining organizations)
- Releases
- Testing and Q/A
- Security
- Structure
- Documentation
- Maintenance
- Production

This document augments the above set of criteria by fleshing out in more
detail the standards a project must meet for the TAC to approve its upgrade
from *Incubation* to *Graduated*. (*Note*: the requirements specified below
do not exactly correspond to the above list, but largely overlap with it.
This is because the below requirements were created earlier for manual inspection,
when automated OpenSSF and CLOMonitor tools were not enabled on the projects.)

It is important to note that *Graduated* in this case refers to
the project itself rather than its product and it is therefore more
about the maturity of process than the maturity of the product or
General Availability (GA).

For this reason this document defines two sets of exit criteria. The
first one is made of requirements expected to be met by all projects
before moving to *Graduated*. The second set lists examples of
additional requirements typically defined at the onset of the project as
goals to be met to exit *Incubation*. These are expected to be documented
in a [Project Proposal](https://lf-decentralized-trust.github.io/project-proposals/)
Because not all projects have the same goals, the importance of each
criteria and the exact definition of this second set of criteria may
vary from one project to another. Ultimately the TAC is responsible for
determining whether a project deserves to move to *Graduated* or
not and this decision does not need to be solely based on these exit
criteria. The purpose of these exit criteria is to help the TAC in its
decision process by informing its members of key aspects of the project.

# Minimum requirements

-   Legal

    -   All code has been made available under the Apache License and is
        free of incompatible dependencies
    -   Project name has been checked for trademark issues

-   Community support

    -   The project must have an active and diverse set of contributing
        members representing various constituencies
    -   The project is not highly dependent on any single contributor
        (there are at least 3 legally independent committers and there
        is no single company or entity that is vital to the success of
        the project)
    -   Release plans are developed and executed in public by the
        community.

-   Sufficient test coverage

    The project must include a comprehensive unit and integration test
    suite and document its coverage. Additional performance and scale
    test capability is desirable.

-   Sufficient user documentation

    The project must including enough documentation for anyone to test
    or deploy any of the modules.

-   Alignment

    -   Requirements fulfillment

        The project must document what requirements and use cases it addresses.

    -   Compatibility with other LF Decentralized Trust projects

        Where applicable, the project should be compatible with other
        *Graduated* projects.

    -   Release numbering: the project should use the LF Decentralized Trust
        standard [release taxonomy](./release-taxonomy.md), once that is agreed upon.

    -   Project must make a [release](./release-taxonomy.md), even a "developer preview",
        before graduation.

-   Infrastructure

    -   Github repo has been created
    -   Mailing lists have been created and are archived
    -   Other communication means used, such as chat channels, are set up
    -   Project is set up with Continuous Integration
    -   All project repos have implemented the [common repository structure](./repository-structure.md)

-   Security

    The project must identify key contact points to address
    security related questions and concerns.
    Some of the other responsibilities for them include:

    -   Address automated alerts, such as depend-a-bot, in a timely manner.

    -   Participate in LF Decentralized Trust wide security discussions.

-   OpenSSF Best Practices Badge

    A project seeking to graduate from *Incubation* shall have started the
    OpenSSF Best Practices Badge application and be nearly complete with
    incomplete badge requirements referenced in their graduation proposal.
    That does not mean the project must have 100% of all criteria, just
    100% of the applicable criteria. This is to allow for projects such
    as test harnesses, that have "N/A" answers for questions that don\'t
    offer that as an option.

-   OpenSSF Scorecard

    A project seeking to graduate from *Incubation* shall have added the
    OpenSSF Scorecard generation to its GitHub Actions. A project does not
    need to score a perfect 10, but should be considered in the green overall.

# Additional considerations

In addition to the above, requirements such as the following may be
defined at the onset of the project and considered as goals to be met to
exit *Incubation*:

-   Sufficient real world use

    The project should be used in real applications and not just in
    demos. Because not all real applications may be discussed publicly,
    in such cases statements providing as much details as possible
    should be made.

-   Sufficient scalability

    The project must demonstrate sufficient scalability and document its
    scalability over various dimensions such as:

    -   Maximum number of transactions per second
    -   Maximum number of transactions per chain
    -   Maximum size of a block

-   Minimum test code coverage expected, such as, for example:

    -   Minimum coverage for security & cryptography
    -   Minimum coverage for other functionality
    -   Minimum coverage for business logic/smart contract

# Acknowledgements

The above borrows from the [ASF\'s Minimum Graduation Requirements](https://incubator.apache.org/incubation/Incubation_Policy.html#Graduating+from+the+Incubator).
