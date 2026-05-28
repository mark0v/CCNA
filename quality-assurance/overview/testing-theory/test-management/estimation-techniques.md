# Estimation Techniques In Software Testing

## Summary

Test estimation is the process of predicting the effort, time, resources, and cost needed to complete testing activities.

Good estimation helps the team answer practical questions:

- how many testers are needed;
- how long testing may take;
- what milestones are realistic;
- what dependencies can affect the schedule;
- what risks can change the estimate;
- whether the planned scope fits the available time and budget.

The ISTQB Foundation Syllabus describes two broad estimation approaches:

- estimation based on expertise and past metrics;
- estimation by consulting the people who will do the work.

In real projects, teams often combine both.

## Why Test Estimation Matters

Testing is constrained by:

- time;
- budget;
- team size;
- environments;
- tools;
- requirements quality;
- development stability;
- defect fixing speed.

Without estimation, testing plans become guesses.

With estimation, QA can explain:

- what can be tested;
- what cannot be tested;
- what trade-offs exist;
- what risks remain if testing time is reduced.

## Estimation Based On Expertise

One approach is to involve people who have expertise in the testing tasks.

These can include:

- experienced QA engineers;
- QA leads;
- automation engineers;
- performance testers;
- domain experts;
- developers;
- DevOps engineers.

The team works together to break testing work into smaller tasks and estimate each part.

## Work Breakdown Structure

A Work Breakdown Structure, or WBS, splits the testing work into manageable tasks.

Example:

| Testing Activity | Example Tasks |
| --- | --- |
| Test planning | Define scope, risks, schedule, resources |
| Test design | Create test cases, checklists, test data |
| Environment setup | Prepare accounts, devices, services, integrations |
| Test execution | Execute smoke, functional, regression tests |
| Defect management | Report bugs, retest fixes, update statuses |
| Reporting | Prepare test summary and release recommendation |

After the work is broken down, each task can be estimated by:

- effort;
- duration;
- dependencies;
- required resources.

## Bottom-Up Estimation

Bottom-up estimation starts from the smallest tasks and builds the total estimate upward.

Example:

| Task | Estimate |
| --- | --- |
| Review requirements | 4 hours |
| Create test cases | 16 hours |
| Prepare test data | 6 hours |
| Execute functional tests | 20 hours |
| Retest defects | 8 hours |
| Regression testing | 12 hours |
| Test report | 3 hours |

Total:

```text
4 + 16 + 6 + 20 + 8 + 12 + 3 = 69 hours
```

This technique is called bottom-up because the estimate starts at the task level.

## Benefits Of Bottom-Up Estimation

Benefits:

- detailed;
- easier to explain;
- helps identify dependencies;
- supports milestone planning;
- encourages team discussion;
- makes hidden work visible.

Limitations:

- can take time;
- requires enough information;
- can become inaccurate if requirements change;
- may miss tasks if the WBS is incomplete.

## Estimation Based On Metrics

Another approach is to use metrics from previous projects or industry data.

Simple examples:

- how many testers are usually needed per developer;
- how long similar projects took;
- how many test cases a tester executes per day;
- how many defects are usually found per module;
- how much regression time is usually needed.

Historical data can make estimation more grounded.

## Project Size And Complexity

A simple metric-based approach is to classify the project by size and complexity.

Example:

| Size | Complexity | Typical Testing Duration |
| --- | --- | --- |
| Small | Simple | 2-3 days |
| Small | Complex | 1 week |
| Medium | Moderate | 2-3 weeks |
| Large | Complex | 1-2 months |

This is not exact, but it gives a starting point.

## Parametric Estimation

Parametric estimation uses measurable parameters to predict effort.

Examples of parameters:

- number of requirements;
- number of test cases;
- test execution rate;
- defect rate;
- retesting effort;
- automation maintenance effort;
- environment setup time.

Example:

```text
Planned test cases: 300
Average execution speed: 30 test cases per tester per day
Number of testers: 2

Execution duration = 300 / (30 x 2) = 5 days
```

This estimate should still include time for:

- blocked tests;
- defect reporting;
- retesting;
- regression;
- meetings;
- environment issues.

## Top-Down Estimation

Top-down estimation starts from the project level rather than the task level.

Example:

- a similar project took 4 weeks;
- this project is slightly smaller;
- estimate testing at 3 weeks.

Another example:

- typical ratio is 1 tester for every 3 developers;
- project has 9 developers;
- estimated QA team size is 3 testers.

Top-down estimation can be fast, but it may be less precise.

## Combining Bottom-Up And Top-Down

A strong approach is to combine techniques.

Practical flow:

1. Use team expertise to create a WBS.
2. Estimate tasks bottom-up.
3. Compare with historical metrics.
4. Check with top-down rules of thumb.
5. Adjust based on risks and constraints.
6. Review with the team.

This creates an estimate that is both detailed and defensible.

## Consulting The People Who Will Do The Work

The second ISTQB-related approach is to consult the people who will actually perform the work.

This matters because estimates are better when they come from people who understand:

- the product;
- the technology;
- the test environment;
- the tools;
- the team capacity;
- the risks;
- the real work involved.

If a QA engineer will execute the tests, that person should help estimate execution effort.

If an automation engineer will create test scripts, that person should help estimate automation effort.

## Why Team Estimation Works

Team estimation helps because different people see different risks.

Examples:

- QA may notice missing requirements;
- developers may warn about unstable components;
- DevOps may know environment setup is complex;
- automation engineers may see high maintenance cost;
- product owners may clarify business priority.

The estimate becomes better when these perspectives are included.

## Estimation Negotiation

Even a strong estimate often needs to be discussed with management.

Management may ask:

- can we test faster;
- can we reduce scope;
- can we use fewer people;
- can we automate more;
- can we release earlier.

The test lead may need to explain:

- what value testing adds;
- what risks increase if testing is reduced;
- which areas are critical;
- which activities can be skipped safely;
- which activities should not be skipped.

Good negotiation is not about winning. It is about balancing:

- quality;
- schedule;
- budget;
- features;
- risk.

## Example Of Negotiation

Suppose QA estimates 10 days for regression testing, but management asks to finish in 5 days.

Possible response:

- keep full regression: needs 10 days;
- run risk-based regression: 5 days, but lower coverage;
- add one more tester: about 6 days;
- reduce release scope: 5 days with lower risk;
- automate stable regression checks: future cycles become faster, but current setup needs extra time.

This turns pressure into options.

## Factors That Affect Test Estimates

Common factors:

- number of requirements;
- requirement clarity;
- product complexity;
- number of integrations;
- supported browsers and devices;
- test data availability;
- environment stability;
- team experience;
- automation coverage;
- defect rate;
- retesting effort;
- regression scope;
- release deadline;
- domain knowledge.

Estimates should include uncertainty when these factors are unstable.

## Common Estimation Mistakes

Common mistakes:

- estimating only test execution and forgetting test design;
- ignoring defect retesting;
- ignoring regression testing;
- assuming environment will always work;
- not including meetings and reporting;
- not consulting the people doing the work;
- using old metrics without context;
- accepting unrealistic deadlines without explaining risk;
- treating estimates as promises instead of forecasts.

An estimate is not magic. It is a reasoned forecast based on current information.

## Best Practices

Good practices:

- break work into smaller tasks;
- involve experienced people;
- consult the actual team;
- use historical metrics;
- include buffers for risk;
- document assumptions;
- separate effort from duration;
- review estimates when scope changes;
- communicate trade-offs clearly.

## Key Idea

Test estimation helps QA plan realistic testing work and explain trade-offs to stakeholders.

Главная мысль:

> A good estimate is not just a number. It is a conversation about scope, risk, time, and quality.

## Questions

1. What is test estimation?
2. What is bottom-up estimation?
3. What is top-down estimation?
4. Why should the people doing the work participate in estimation?
5. Why should estimates be negotiated with management?

## What To Review Later

- Work Breakdown Structure
- Test Planning
- Risk Based Testing
- Test Schedule
- Test Effort
- QA Metrics
