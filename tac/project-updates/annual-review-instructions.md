[//]: # (SPDX-License-Identifier: CC-BY-4.0)

# Annual Review Instructions
Create a file in the `tac/project-updates` subdirectory for the current year and name the file `YYYY-annual-Project-Name.md` (e.g., `tac/project-updates/2024/2024-annual-lf-decentralized-trust-amazing.md`). Update the `mkdocs.yml` document in the root directory to include the file in the `nav` section under the appropriate year and quarter. If the year or quarter does not yet exist, please add it to match what you see in the `Project Updates` section.

# What Should the Annual Review Contain
Unlike the quarterly updates, the annual review process will be a "big picture" assessment of the project by reviewing the progress on goals from the prior year and goals for the next year. In addition, the annual review process will include a deep dive into the project health, including contributor and maintainer diversity and adoption metrics, and will include an assessment of the current project lifecycle state. The review will result in a set of recommendations for the project to improve and/or recommendation to move a project to another state.

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
