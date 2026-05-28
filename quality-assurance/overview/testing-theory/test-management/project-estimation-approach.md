# Project Estimation Approach

## Summary

Project estimation is the process of predicting the size, effort, cost, and schedule needed to complete a project.

One widely used approach is the Decomposition Technique.

Decomposition means breaking a large project into smaller parts that are easier to understand and estimate.

This follows the classic divide-and-conquer idea:

- estimate smaller pieces;
- combine those estimates;
- compare results;
- reconcile differences;
- update estimates when more information appears.

## What Is Decomposition Technique?

Decomposition Technique is an estimation approach where a project is divided into:

- major functions;
- software engineering activities;
- smaller tasks;
- measurable work items.

Instead of trying to estimate the whole project at once, the team estimates each part separately.

This makes the estimate more realistic and easier to explain.

## Step 1: Understand The Scope

Before estimating, the team must understand the scope of the software to be built.

Scope answers:

- what should be built;
- what is included;
- what is excluded;
- which features are required;
- which constraints exist;
- which assumptions are being made.

If scope is misunderstood, every estimate built on top of it will be weak.

## Step 2: Estimate Software Size

Start with the statement of scope.

Then decompose the software into functions that can be estimated individually.

For each function:

1. Understand what it should do.
2. Estimate its size.
3. Apply baseline productivity metrics.
4. Derive effort and cost.

After estimating all functions, combine them to produce an overall estimate.

Example:

| Function | Estimated Size | Effort |
| --- | --- | --- |
| Login | Small | 2 days |
| Payment | Large | 10 days |
| Reports | Medium | 5 days |
| Notifications | Medium | 4 days |

Total estimate is built from the smaller function estimates.

## Step 3: Estimate Effort And Cost

Effort and cost can also be estimated by breaking the project into software engineering activities.

Typical activities:

- requirements analysis;
- design;
- development;
- test planning;
- test design;
- test execution;
- defect fixing;
- regression testing;
- deployment;
- reporting.

For each activity:

1. Identify tasks.
2. Estimate effort in person-hours or person-days.
3. Identify dependencies.
4. Apply cost per effort unit.
5. Calculate total activity cost.
6. Combine all activity estimates.

Example:

| Activity | Effort | Cost Per Day | Total Cost |
| --- | --- | --- | --- |
| Test planning | 2 days | 400 | 800 |
| Test design | 5 days | 400 | 2000 |
| Test execution | 8 days | 400 | 3200 |
| Regression | 3 days | 400 | 1200 |

This gives a clearer view of where time and money go.

## Step 4: Reconcile Estimates

After estimating by size and by activities, compare the results.

If both estimates are close, confidence is higher.

If estimates are very different, investigate why.

Possible reasons:

- project scope is not understood;
- requirements were misinterpreted;
- function breakdown is inaccurate;
- activity breakdown missed important tasks;
- historical data is outdated;
- productivity metrics do not match this project;
- assumptions are wrong.

Reconciliation helps avoid false confidence.

## Step 5: Determine The Cause Of Divergence

When estimates diverge, the team should not simply average them without thinking.

Instead, ask:

- Which estimate is based on better data?
- Which assumptions are different?
- Which tasks were missed?
- Is the project similar to historical examples?
- Are requirements stable enough?
- Are dependencies clear?
- Are risks included?

Then update the estimate based on the investigation.

## Estimation Accuracy

Accuracy means how close the estimate is to reality.

Every team wants accurate estimates, but estimates are based on the information available at the time.

Early estimates are usually less accurate because the team knows less.

Later estimates can be more accurate because:

- requirements are clearer;
- risks are better understood;
- architecture is more stable;
- team velocity is visible;
- dependencies are known.

## Factors That Affect Accuracy

Important factors:

- accuracy of input data;
- quality of estimate calculations;
- relevance of historical data;
- similarity between past projects and current project;
- predictability of the development process;
- stability of requirements;
- stability of the technical environment;
- quality of planning, monitoring, and control;
- unexpected delays or surprises.

The better the input data, the better the estimate can be.

## Guidelines For Reliable Estimates

Useful guidelines:

- base estimates on similar completed projects;
- use decomposition techniques;
- use empirical estimation models when possible;
- estimate with more than one technique;
- compare results;
- document assumptions;
- revisit estimates during the project.

Using at least two estimation techniques is a good practice because it helps validate the result.

## Estimation Issues

Estimation problems are common in real projects.

## Estimating Schedule Without Estimating Size

Sometimes managers estimate only the schedule and skip size estimation.

This is risky.

If the team does not understand size and scope, later scope changes become hard to handle.

Schedule should be connected to:

- size;
- effort;
- complexity;
- dependencies;
- resources;
- risks.

## Missing Assumptions

Every estimate includes assumptions.

Examples:

- requirements will not change significantly;
- test environment will be ready on time;
- required people will be available;
- third-party API will be stable;
- defect rate will be similar to previous projects.

Assumptions should be documented in the estimation sheet.

If assumptions change, the estimate should be reviewed.

## False Confidence

Even good estimates contain uncertainty.

A common mistake is presenting an estimate as if it were exact.

Bad:

```text
The project will finish on August 15.
```

Better:

```text
The project will likely take 5 to 7 months.
```

Even better:

```text
There is a 90% probability that the project will complete by the end of August.
```

Ranges communicate uncertainty more honestly.

## Lack Of Historical Data

Organizations often do not collect accurate project data.

This makes future estimates weaker.

Useful historical data:

- project size;
- actual effort;
- actual duration;
- defect count;
- test execution speed;
- rework effort;
- environment downtime;
- team size;
- release delays.

If historical data does not exist, start collecting it now.

## Schedule Constraints

Sometimes management or clients set a fixed deadline.

If the schedule is shorter than the realistic estimate, the team should negotiate scope and risk.

Options:

- reduce scope;
- add resources;
- reduce lower-priority testing;
- increase automation where realistic;
- split release into phases;
- accept higher residual risk.

The team should avoid pretending that full scope, full quality, and shorter time are all possible without trade-offs.

## Scope Creep

Scope creep means uncontrolled growth of project scope.

It often causes schedule overruns.

To manage it:

- agree how change requests will be handled;
- document new requirements;
- estimate impact;
- update schedule and budget;
- get approval before adding work.

## Missing Contingency

Estimates should include contingency for:

- meetings;
- blockers;
- defect investigation;
- environment issues;
- organizational events;
- unexpected rework;
- communication overhead.

Ignoring contingency makes estimates fragile.

## Resource Utilization

Resources should not be planned at 100% utilization.

People are not productive every minute of the day.

They spend time on:

- meetings;
- communication;
- context switching;
- support;
- code reviews;
- documentation;
- unexpected issues.

A practical guideline is to assume people are productive for about 80% of their time or less.

If resources are assigned above that level, delays are likely.

## Estimation Guidelines

When estimating a project:

- ask other people for their experience;
- use your own previous experience;
- assume resource utilization below 80%;
- remember that people working on multiple projects are slower because of context switching;
- include management time;
- include contingency;
- allow enough time to estimate properly;
- use documented historical data when possible;
- involve the people who will do the work;
- use several estimators;
- use several estimation techniques;
- reconcile estimates;
- re-estimate throughout the project lifecycle.

## Wideband Delphi

Wideband Delphi is a group estimation technique.

The idea is to gather estimates from multiple people, discuss differences, and move toward a more accurate and less biased estimate.

It is useful because:

- different people notice different risks;
- extreme estimates can be explained;
- assumptions become visible;
- team knowledge is combined;
- estimates become more defensible.

## Re-Estimation

Estimation should not happen only once.

Projects change.

Re-estimate when:

- requirements change;
- scope changes;
- team capacity changes;
- new risks appear;
- actual progress differs from plan;
- defect rate is higher than expected;
- dependencies are delayed;
- environment issues appear.

Re-estimation keeps planning connected to reality.

## Key Idea

Project estimation is not about guessing a perfect number.

It is about using available information, decomposition, historical data, assumptions, and team knowledge to create a realistic forecast.

Главная мысль:

> A useful estimate shows not only the number, but also the assumptions, risks, and uncertainty behind it.

## Questions

1. What is Decomposition Technique?
2. Why should estimates be reconciled?
3. What factors affect estimation accuracy?
4. Why is it better to estimate with a range?
5. Why should projects be re-estimated during the lifecycle?

## What To Review Later

- Decomposition Technique
- Work Breakdown Structure
- Bottom-Up Estimation
- Top-Down Estimation
- Wideband Delphi
- Contingency
- Scope Creep
