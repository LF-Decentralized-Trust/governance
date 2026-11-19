[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# Annual Review Instructions

The main annual review for a project takes place at the beginning of the year, and is based on the project's annual report write-up. An interim report is submitted by projects in the middle of the year.

Create a file in the `tac/project-updates` subdirectory for the current year and name the file `YYYY-annual-Project-Name.md` (e.g., `tac/project-updates/2024/2024-annual-lf-decentralized-trust-amazing.md`). That one file is the whole submission; do not edit `mkdocs.yml` or the year's `index.md`.

The report is listed from its file name, so keep to the pattern: `2026-annual-Hyperledger-Fabric.md` appears as "2026 Annual Hyperledger Fabric". Once the pull request merges:

- the site build runs `scripts/generate-project-updates.py`, which adds the report to the navigation and to the year's index page, so it is listed on the published site straight away
- the "Generate Project Updates listings" workflow opens a follow-up pull request that refreshes the copy of those listings committed to the repository; a maintainer merges it, and there is nothing for the project to do

If one report serves as both the annual and the mid-year review, add the line `[//]: # (project-updates: also midyear)` directly under the license line at the top of the file and it is listed under both.

# What Should the Annual Review Contain
Unlike the mid-year updates, the annual review process will be a "big picture" assessment of the project by reviewing the progress on goals from the prior year and goals for the next year. In addition, the annual review process will include a deep dive into the project health, including contributor and maintainer diversity and adoption metrics, and will include an assessment of the current project lifecycle state. The review will result in a set of recommendations for the project to improve and/or recommendation to move a project to another state.

The annual review should answer the following questions:

- How did you progress against your goals for last year?
- What deliverables/outputs did you have in the past year?
- What are your goals for this year?
- Do you need any help?
- What is the Maintainer/Contributor diversity?

# What Does the TAC Evaluate
In general, the TAC will be looking at the health of the project overall and if it is in the correct lifecycle state. The following is what the TAC will specifically look for:

- Whether all requirements specified in the [LF Decentralized Trust TAC governance documents](../governing-documents/index.md) were met.
- Signs of consistent or increasing contribution activity.
- Understanding the diversity of maintainers in terms of organizations participating and whether the number of active maintainers has increased or decreased over the past year. Ensure your MAINTAINERS.md file is up-to-date.
- Understanding the adoption of the project and how that has changed since the last review or since being accepted into LF Decentralized Trust. Ensure your ADOPTERS.md file is up-to-date.
- Understanding how the project has performed against the goals set in the last review or since the project proposal has been approved. If you have not achieved the goals that you set out, that is okay. The TAC should look at what has been accomplished and what challenges the project had in meeting the goals.
- Understanding the goals that the project wants to achieve including stretch goals and if there is a plan for how those goals will be achieved. Ensure your roadmap is up-to-date and publically available.

# What Should the Responsible TAC Members Provide
The primary and secondary reviewers will ensure that they evaluate the project based on the [evaluation criteria](#what-does-the-tac-evaluate). They will then ensure that the pull request contains information about what requirements have not been met and a set of recommendations for the project for improvements and possible lifecycle state changes. After the discussion has been held at a TAC meeting, the responsible reviewers will create a PR against the committed annual review to include the evaluation and recommendations made. In addition, any follow up action items should be captured in the [lf-decentralized-trust/governance] GitHub repo as issues.

[lf-decentralized-trust/governance]: https://github.com/lf-decentralized-trust/governance/
