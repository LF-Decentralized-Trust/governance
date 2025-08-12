---
layout: default
title: 2024 Annual Review Besu
parent: Project Updates
grand_parent: LF Decentralized Trust TAC
nav_exclude: true
---



## Project Health

The Besu project continues to thrive. [Fleet Mode](https://consensys.io/blog/besu-fleet-the-future-of-rpc-scaling) has bolstered interest in Besu from public blockchain networks and private chains, with both Layer 2 and RPC providers considering Besu for their infrastructure. Community activity on Discord is stable, though external contributions are at a seasonal lull. Overall, the project remains healthy.


## Maintainer Diversity

The Besu project currently has 21 maintainers, 18 of which work for Consensys Software Inc.  2 work for Kaleido. Existing maintainers give special attention to new pull requests and are very timely in moving those forward.

## Project Adoption

Besu's share of mainnet stake is around 18%. This value is very hard to measure reliably, but anywhere between 15-20% is a good place for an execution client to be.

## Goals

### Performance Against Prior Goals

Feature consolidation is well underway. The sunset plan remains in effect, and work is already ongoing to remove/deprecate private network features which are no longer on our roadmap.

Testing and CI/CD pipelines are much improved after the migration from CircleCI to Github Actions. Every release now has a "burn-in" phase that is run consistently and reproducibly prior to release.

Great strides were made with the Plugin API, so much so that Linea now runs their rollup on mainline Besu with plugins, instead of running their own fork. 


### Next Year's Goals

The Besu team continues to focus its roadmap on performance, stability, modularity, and upcoming protocol changes like PeerDAS and Stateless ethereum. The Besu Maintainers intend to support the Fusaka and Glamsterdam hard forks and take an active role in delivery.

### Help Required

Organize more technical feedback meetups on Besu, not only user or application oriented sessions. 

## Project Lifecycle Status Recommendation

This report recommends continuing the graduated status. 