// Create the project report reminder issues that fall due today.
//
// Runs under actions/github-script from
// .github/workflows/report-reminders.yml. The schedule is
// .github/configs/project-report-reminders.yml, converted to JSON by
// the workflow before this script reads it.
//
// A schedule is due when the number of whole days from now until
// midnight UTC of its date, truncated toward zero, equals
// buffer_window_days. This is the arithmetic of the
// github-issue-schedule Go action the workflow used before, kept so
// the switch neither skips nor repeats a reminder: a run at 01:00 UTC
// with a seven day window picks up dates eight calendar days ahead.

const fs = require('fs');

const DAY_MS = 24 * 60 * 60 * 1000;

function readConfig(configFile) {
  const config = JSON.parse(fs.readFileSync(configFile, 'utf8'));
  const window = Number(config.buffer_window_days);
  if (!Number.isInteger(window) || window < 0 || window > 100000) {
    throw new Error(`buffer_window_days must be an integer between 0 and 100000, got ${config.buffer_window_days}`);
  }
  if (!Array.isArray(config.projects)) {
    throw new Error('projects must be a list');
  }
  return { window, projects: config.projects };
}

function dueSchedules(config, now) {
  const due = [];
  for (const project of config.projects) {
    for (const schedule of project.schedules || []) {
      const requested = Date.parse(`${schedule.date}T00:00:00Z`);
      if (Number.isNaN(requested)) {
        throw new Error(`invalid date "${schedule.date}" in the schedule for ${project.name}`);
      }
      const days = Math.trunc((requested - now.getTime()) / DAY_MS);
      if (days === config.window) {
        due.push({ project, schedule });
      }
    }
  }
  return due;
}

module.exports = async ({ github, core, configFile, dryRun = false, now = new Date() }) => {
  const config = readConfig(configFile);
  const due = dueSchedules(config, now);
  core.info(`${now.toISOString()}: ${due.length} reminder(s) due with a ${config.window} day window`);

  const failures = [];
  for (const { project, schedule } of due) {
    const target = `${project.github_org}/${project.github_repo}`;
    if (dryRun) {
      core.info(`dry run: would create "${schedule.title}" in ${target} for ${schedule.date}`);
      continue;
    }
    try {
      const { data: issue } = await github.rest.issues.create({
        owner: project.github_org,
        repo: project.github_repo,
        title: schedule.title,
        body: schedule.description,
        assignees: project.maintainers || [],
      });
      core.info(`created ${issue.html_url} for ${project.name} (${schedule.date})`);
    } catch (error) {
      core.error(`could not create "${schedule.title}" in ${target}: ${error.message}`);
      failures.push(target);
    }
  }
  if (failures.length > 0) {
    core.setFailed(`could not create ${failures.length} reminder(s): ${failures.join(', ')}`);
  }
};

module.exports.dueSchedules = dueSchedules;
module.exports.readConfig = readConfig;
