[//]: # "SPDX-License-Identifier: CC-BY-4.0"

# Mid-year Review Instructions

Projects are required to create a mid-year report for their project.

Create a file in the `tac/project-updates` subdirectory for the current year and name the file `YYYY-MidYear-Project-Name.md` (e.g., `2026-MidYear-Hyperledger-Fabric.md`). That one file is the whole submission; do not edit `mkdocs.yml` or the year's `index.md`.

The report is listed from its file name, so keep to the pattern: `2026-MidYear-Hyperledger-Fabric.md` appears as "2026 Mid-Year Hyperledger Fabric". Once the pull request merges:

- the site build runs `scripts/generate-project-updates.py`, which adds the report to the navigation and to the year's index page, so it is listed on the published site straight away
- the "Generate Project Updates listings" workflow opens a follow-up pull request that refreshes the copy of those listings committed to the repository; a maintainer merges it, and there is nothing for the project to do

# What Should the Mid-Year Review Contain?

Mid-year reviews are intended to look at the 6 months since the annual review to see how the project is progressing against its goals. This allows for a wide audience to better understand the project's health. Starting in 2026, all projects submit two reports per year: an annual review and a mid-year review.

The review should answer the following questions:

- How are you progressing against your yearly goals?
- What deliverables/outputs did you have in the past 6 months?
- What are your goals for the second half of the year?
- Do you need any help?
- Changes to maintainer/contributor diversity

# What Does the TAC Evaluate

In general, the TAC will be looking at the health of the project overall and if it is in the correct lifecycle state. The following is what the TAC will specifically look for:

- Whether all requirements specified in the [LF Decentralized Trust TAC governance documents](../governing-documents/index.md) were met.
- Signs of consistent or increasing contribution activity.
- Whether the questions on Discord are being answered in a timely manner.
- Whether PRs and issues on GitHub are being resolved in a timely manner.
- Whether deliverable are being created (e.g., releases or standards updates)
- Understanding the diversity of maintainers in terms of organizations participating and whether the number of active maintainers has increased or decreased over the past year. Ensure your MAINTAINERS.md file is up-to-date.
- Understanding the adoption of the project and how that has changed since the last review or since being accepted into LF Decentralized Trust. Ensure your ADOPTERS.md file is up-to-date.
- Understanding how the project has performed against the goals set in the annual review. If you have not achieved the goals that you set out, that is okay. Feel free to include updates to your goals if things have changed. The TAC should look at what has been accomplished and what challenges the project had in meeting the goals. Ensure your roadmap is up-to-date and is publicly available.

# What is the Outcome of the Review

The TAC will approve and merge the pull request or request changes be made to the PR prior to approval and merge. In addition, any follow up action items should be captured in the [lf-decentralized-trust/governance] GitHub repo as issues.

[lf-decentralized-trust/governance]: https://github.com/lf-decentralized-trust/governance/
