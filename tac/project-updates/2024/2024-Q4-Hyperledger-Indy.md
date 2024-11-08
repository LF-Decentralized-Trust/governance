---
layout: default
title: 2024 Q4 Hyperledger Indy
parent: 2024
grand_parent: Project Updates
---

Created by Stephen Curran and Lynn Bendixsen with input from the Hyperledger Indy community.

## Sub-Projects

### **Distributed Ledger**

- [indy-node]
- [indy-plenum]
- [indy-test-automation]
- [indy-node-monitor]
- [indy-node-container]
- [indy-blssignatures-rs]
- [indy-besu]

[indy-node]: https://github.com/hyperledger/indy-node
[indy-plenum]: https://github.com/hyperledger/indy-plenum
[indy-test-automation]: https://github.com/hyperledger/indy-test-automation
[indy-node-monitor]: https://github.com/hyperledger/indy-node-monitor
[indy-node-container]: https://github.com/hyperledger/indy-node-container
[indy-blssignatures-rs]: https://github.com/hyperledger/indy-blssignatures-rs
[indy-besu]: https://github.com/hyperledger/indy-besu

### **Client Tools**

- [indy-vdr]
- [indy-shared-rs] -- for AnonCreds, [Hyperledger AnonCreds] should be used
- [indy-cli-rs] -- Indy CLI based on Indy VDR

[indy-vdr]: https://github.com/hyperledger/indy-vdr
[indy-shared-rs]: https://github.com/hyperledger/indy-shared-rs
[indy-cli-rs]: https://github.com/hyperledger/indy-cli-rs
[Hyperledger AnonCreds]: https://github.com/hyperledger/anoncreds-rs

### **Specifications**

- [did:indy Specification], [did:indy Specification source repository]
- [did:indy Networks]
- [Indy HIPE] (Hyperledger Indy Project Enhancements)
- [indy-did-method]

[did:indy Specification]: https://hyperledger.github.io/indy-did-method/
[did:indy Specification source repository]: https://github.com/hyperledger/indy-did-method
[did:indy Networks]: https://github.com/hyperledger/indy-did-networks
[Indy HIPE]: https://github.com/hyperledger/indy-hipe
[indy-did-method]: https://github.com/hyperledger/indy-did-method

## Project Health

The project had a further drop in contributor activity over the quarter. Per the
[Indy Quarterly Activity Dashboard], in the months July through September, 2024
there were just 18 commits (down about 80%) and 26 contributors (down about
25%). Work was mainly on the [Indy Besu] initiative and in Indy monitoring
tools. There is still a number of scaled deployments of Indy across the world,
but all are running relatively smoothly, and there is little demand for new
features in the existing Indy Node/Plenum code base.

The Hyperledger Mentorship project has produced an [Indy Read Replica]
implementation. We expect to have a
[repository](https://github.com/rxbryan/indyread) containing a first cut of the
functionality and documentation completed in November.

[Indy Quarterly Activity Dashboard]: https://insights.lfx.linuxfoundation.org/foundation/lf-decentralized-trust/overview/github?project=indy&routedFrom=Github&bestPractice=false&dateFilters=Last%20Quarter&dateRange=2024-07-01%20to%202024-09-30&compare=PP&granularity=week&hideBots=true

## Questions/Issues for the TAC

None

### Issues from previous reports

#### **Diversity of Contributor Community**

See the updated type of information in the appropriate section of this report.

## Releases

Releases since the last quarterly report:

- indy-plenum - v1.14.0rc0 -- included in the last Quarterly report, but occurred in the period covered by this report.
- indy-vdr - v0.4.3 -- included in the last Quarterly report, but occurred in the period covered by this report.

## Overall Activity in the Past Quarter

Work was done this quarter on the Ubuntu 22.04 version of Indy, with a PR
submitted for Indy Node in July. However, that PR has not been approved/merged
into the codebase. That has prevented the completion of a release candidate for
the Indy on Ubuntu 22.04.

Work continued on the [Indy Besu] implementation of Indy capabilities on
a Besu base, and in defining the Indy Besu updates to the [Indy DID Method].

[Indy Besu]: https://github.com/hyperledger/indy-besu
[Indy DID Method]: https://github.com/hyperledger/indy-did-method

Progress was made on the Indy [Hyperledger Mentorship] project kicked off last
quarter to implement an [Indy Read Replica] capability. Mentee [Bryan Elee] will
wrap up the project this month, November, 2024.

[Hyperledger Mentorship]: https://wiki.hyperledger.org/display/INTERN/Hyperledger+Mentorship+Program
[Indy Read Replica]: https://wiki.hyperledger.org/display/INTERN/Project+Plan+-+Indy+Read+Replica+Implementation
[Bryan Elee]: https://github.com/rxbryan

A submission for EU funding to implement Ledger Redactibility in Indy (as
mentioned in the last quarterly report) was unsuccessful.

A pioneering user of Hyperledger Indy technology, the [Sovrin Foundation], announced in October that
the operation of the Sovrin MainNet would likely stop at the end of March, 2025. The post on LinkedIn
can be seen [here](https://www.linkedin.com/posts/sovrin-foundation_to-the-sovrin-community-after-seven-years-activity-7253082729443930112-069C).

[Sovrin Foundation]: https://sovrin.org

## Current Plans

The maintainers would like to see the publication of an official Indy release
supporting Ubuntu 22.04. While the work is well underway, with [indy-plenum] work
complete, the [indy-node] PR is stalled.

[Indy Besu] work continues and is gaining interest. Work has begun towards
adding a verifiable credential revocation capability to the implementation. The
team behind the project held a successful meetup/webinar about Indy on Besu in
September.

## Maintainer Diversity

After the removal of inactive maintainers from the Hyperledger GitHub
organization's teams, there are 23 individuals on 18 Indy GitHub Teams
representing at least 13 organizations.

## Contributor Diversity

See the [Indy Quarterly Activity Dashboard] for information about contributors
this quarter. The contributions came from at least 5 different
organizations.

## Additional Information

- Key channels on Hyperledger Discord: \#indy, \#indy-sdk,
\#indy-node, \#indy-maintainers, \#indy-vdr
- [Indy Mailing List](https://lists.hyperledger.org/g/indy)
