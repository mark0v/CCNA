# Estimation Techniques Quick Guide

## Summary

Estimation is the process of finding an approximate value for effort, time, cost, resources, or size when input data may be incomplete, uncertain, or unstable.

In software and QA projects, estimation helps answer:

- how much work is needed;
- how many people are needed;
- how long the project may take;
- how much it may cost;
- what risks affect the plan;
- what trade-offs exist between scope, schedule, budget, and quality.

An estimate is not a promise. It is a forecast based on current knowledge.

## What Estimation Is Based On

Good estimates usually rely on:

- past data;
- past experience;
- available documents;
- requirements knowledge;
- assumptions;
- identified risks;
- expert judgment;
- historical metrics.

The more reliable the input data, the more reliable the estimate can be.

## Basic Estimation Steps

A practical software project estimation flow has four basic steps:

1. Estimate the size of the product.
2. Estimate the effort in person-hours, person-days, or person-months.
3. Estimate the schedule in calendar time.
4. Estimate the cost in agreed currency.

Size, effort, schedule, and cost are connected, but they are not the same thing.

## Important Observations

Estimation is not always a one-time task.

It can happen during:

- project acquisition;
- project planning;
- project execution;
- release planning;
- scope change review;
- re-planning after risks appear.

As more information becomes available, estimates should be reviewed and updated.

## Before Estimating

Before estimation starts, the team should understand:

- project scope;
- business goals;
- requirements;
- constraints;
- assumptions;
- risks;
- available resources;
- expected quality level.

Historical project data is especially useful because it gives the team a real baseline instead of pure guessing.

## Use More Than One Technique

A strong estimation practice uses at least two techniques and compares the results.

Example:

- bottom-up WBS estimate;
- analogous estimate from similar project;
- expert estimate through Wideband Delphi.

If estimates are close, confidence increases.

If estimates are far apart, investigate why.

## General Project Estimation Approach

One widely used approach is Decomposition Technique.

Decomposition means breaking the project into smaller functions, activities, or tasks.

This approach follows the divide-and-conquer idea:

1. Understand project scope.
2. Estimate software size.
3. Estimate effort and cost.
4. Compare estimates from different views.
5. Reconcile differences.

## Decomposition By Function

To estimate software size:

1. Start with scope.
2. Decompose software into functions.
3. Estimate each function.
4. Apply productivity metrics.
5. Combine function estimates.

Example:

| Function | Size | Notes |
| --- | --- | --- |
| Login | Small | Standard flow |
| Payment | Large | High risk, integrations |
| Reports | Medium | Calculations and export |
| Notifications | Medium | Email and push |

## Decomposition By Activity

To estimate effort and cost:

1. Identify project activities.
2. Divide activities into measurable tasks.
3. Estimate effort for each task.
4. Apply cost per effort unit.
5. Combine task and activity estimates.

Example:

| Activity | Tasks |
| --- | --- |
| Test planning | Scope, risks, schedule |
| Test design | Test cases, test data |
| Test execution | Smoke, functional, regression |
| Defect handling | Reporting, retesting |
| Closure | Summary report, lessons learned |

## Reconcile Estimates

After estimating by different methods, compare the numbers.

If estimates agree, confidence is higher.

If estimates differ widely, check:

- was scope misunderstood;
- was breakdown incomplete;
- was historical data inappropriate;
- were assumptions different;
- were risks ignored;
- was productivity data outdated.

Do not blindly average conflicting estimates. Understand why they differ.

## Estimation Accuracy

Accuracy means how close an estimate is to reality.

Factors affecting accuracy:

- quality of input data;
- correctness of calculations;
- relevance of historical data;
- predictability of the team process;
- stability of requirements;
- stability of environment;
- quality of monitoring and control;
- unexpected events.

Early estimates are usually less accurate because less is known.

## Express Estimates As Ranges

Avoid false precision.

Weak:

```text
The project will finish in 43 days.
```

Better:

```text
The project will likely take 5 to 7 weeks.
```

Even better:

```text
There is about 90% confidence that the project will finish within 7 weeks.
```

Ranges make uncertainty visible.

## Common Estimation Issues

Common issues:

- estimating schedule without estimating size;
- not documenting assumptions;
- treating estimates as commitments;
- not collecting historical project data;
- ignoring contingency;
- planning resources at 100% utilization;
- not accounting for scope creep;
- skipping re-estimation during the project.

## Resource Utilization

People are not productive 100% of the time.

They also spend time on:

- meetings;
- communication;
- support;
- context switching;
- reviews;
- unexpected blockers.

A common guideline is to plan resource utilization below 80%.

## Estimation Guidelines

Useful guidelines:

- ask experienced people;
- use your own previous experience;
- use historical data from similar projects;
- include management time;
- include contingency;
- involve people who will do the work;
- use several estimators;
- use several estimation techniques;
- reconcile estimates;
- re-estimate throughout the lifecycle.

Rushed estimates are high-risk estimates.

## Quick Overview Of Techniques

## Work Breakdown Structure

WBS breaks the project into smaller manageable components.

Use it when:

- you need detailed task-level estimates;
- you want to identify hidden work;
- you need schedule and cost control.

Key idea:

```text
Break work down before estimating it.
```

## Function Points

Function Points measure software size based on business functionality.

Useful when:

- requirements are available;
- technology-independent sizing is needed;
- estimation should happen before code exists.

Key components:

- ILF;
- EIF;
- EI;
- EO;
- EQ.

## Use-Case Points

Use-Case Points estimate software size using use cases and actors.

Useful when:

- requirements are written as use cases;
- use cases are goal-oriented and consistent;
- the team needs early functional size estimation.

Formula:

```text
UCP = UUCP x TCF x EF
```

## Wideband Delphi

Wideband Delphi uses expert estimates and structured discussion.

Useful when:

- expert judgment is needed;
- assumptions must be discussed;
- team consensus is important;
- historical data is limited.

Key idea:

```text
Estimate independently, discuss anonymously, converge through rounds.
```

## Three Point Estimation

Three Point Estimation uses:

- optimistic estimate;
- most likely estimate;
- pessimistic estimate.

Formula:

```text
E = (O + M + L) / 3
```

Useful when uncertainty should be visible.

## PERT

PERT also uses optimistic, most likely, and pessimistic estimates, but gives more weight to the most likely value.

Formula:

```text
E = (O + 4M + L) / 6
```

Standard deviation:

```text
SD = (L - O) / 6
```

Useful for uncertain and larger project tasks.

## Analogous Estimation

Analogous Estimation uses similar past project data.

Useful when:

- little detail is available;
- a quick early estimate is needed;
- similar historical projects exist.

Key idea:

```text
Use what similar past projects can teach you.
```

## Planning Poker

Planning Poker is a consensus-based Agile estimation technique.

It uses private voting, usually with Fibonacci cards.

Useful when:

- estimating Scrum user stories;
- the whole team should participate;
- hidden assumptions need discussion.

## Testing Estimation

Testing Estimation focuses specifically on QA effort.

It should include:

- test planning;
- test design;
- test data;
- execution;
- defects;
- retesting;
- regression;
- reporting.

Testing effort should not be reduced to execution time only.

## Which Technique To Use?

| Situation | Useful Technique |
| --- | --- |
| Early rough estimate | Analogous Estimation |
| Detailed task estimate | WBS |
| Team consensus needed | Wideband Delphi |
| Agile story sizing | Planning Poker |
| Requirements as use cases | Use-Case Points |
| Functional size needed | Function Points |
| Uncertainty is high | Three Point or PERT |
| QA effort estimate | Testing Estimation + WBS |

## Key Formulas

| Technique | Formula |
| --- | --- |
| Three Point | `E = (O + M + L) / 3` |
| PERT | `E = (O + 4M + L) / 6` |
| PERT SD | `SD = (L - O) / 6` |
| Use-Case Points | `UCP = UUCP x TCF x EF` |
| Test Cases From FP | `Test Cases = Function Points x 1.2` |

## Common Mistakes

Common estimation mistakes:

- using one exact number too early;
- not documenting assumptions;
- ignoring risks;
- ignoring scope creep;
- not including contingency;
- using historical data from unrelated projects;
- not involving the people doing the work;
- confusing effort with duration;
- not re-estimating after changes.

## Key Idea

Estimation is not about predicting the future perfectly.

It is about making uncertainty visible enough for planning and decision-making.

Главная мысль:

> A good estimate explains the number, the assumptions, the risks, and the confidence behind it.

## Questions

1. What is estimation?
2. Why should estimation use more than one technique?
3. What is the difference between size, effort, schedule, and cost?
4. Why are estimates better expressed as ranges?
5. Which estimation technique is useful for Scrum user stories?

## What To Review Later

- WBS
- Function Points
- Use-Case Points
- Wideband Delphi
- Three Point Estimation
- PERT
- Analogous Estimation
- Planning Poker
- Testing Estimation
