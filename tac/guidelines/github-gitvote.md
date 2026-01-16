[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# Asynchronous Voting Using GitVote

[GitVote](https://github.com/cncf/gitvote) is a GitHub application that allows holding a vote on issues and pull requests.
More background information and configuration options are described in the [GitVote documentation](https://github.com/cncf/gitvote/tree/main/docs).

## Configuring GitVote

GitVote allows for great flexibility of options to perform a vote. As described in the GitVote documentation, GitVote uses a configuration file [.gitvote.yml](https://github.com/cncf/gitvote/blob/main/docs/config/.gitvote.yml) that can be created:
- At the root of the repository where the vote was created
- In the .github directory of the repository where the vote was created
- At the root of the .github repository, for organization wide configuration

This file contains an array of options for teams to customize their vote on issues and pull requests.

Project maintainers can either create a local .gitvote.yml file in the root of their repo with the desired configuration that allows them to conform to their voting process. This configuration file will take precedence over an existing configuration file in the .github repository of the organization.

## When and How to Cast an Asynchronous Vote

Anyone can trigger a vote via issues and pull request comments. Detailed information on how the comments trigger votes can be found in the [GitVote usage documentation](https://github.com/cncf/gitvote?tab=readme-ov-file#usage).

The supported profiles to cast a vote using **"/vote-[profileName]"** via comments can be found under the [profile section](https://github.com/cncf/gitvote/blob/main/docs/config/.gitvote.yml#L63) of the .gitvote.yml configuration file. If the repo in question has a local .gitvote.yml file, the profile section in that file describes the different types of votes that can be performed. 

Depending on the profile called, GitVote will post a comment on the issue or pull request where it was invoked to the team/teams invited to participate in the vote. Votes from users outside those teams won't count towards the total of the vote.

It is up to project maintainers to decide when to run an asynchronous vote using GitVote vs calling for a vote on a project meeting. Similarly, the TSC can decide to run an asynchronous vote in cases where a meeting does not have enough quorum, for example. The important aspect is to keep all votes recorded and registered for later reference.

## Recommendations

It is strongly recommended that anyone invoking GitVote in an issue or pull request proactively notify participants, such as by announcing it during public meetings or posting an advance notice in relevant Discord channels, to ensure adequate awareness and participation.

## GitVote Usage Example

- [Governance PR #475 – Example GitVote usage in a pull request](https://github.com/hiero-ledger/governance/pull/475)
- [TSC Issue #277 – Example GitVote usage in an issue](https://github.com/hiero-ledger/tsc/issues/277)

