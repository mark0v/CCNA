# Testing Estimation

## Summary

Testing Estimation is the process of predicting the effort, duration, resources, and cost needed to complete testing activities.

Test effort is difficult to estimate because testing depends on many changing factors:

- requirement clarity;
- build stability;
- defect count;
- retesting effort;
- regression scope;
- environment availability;
- test data readiness;
- team experience.

In many projects, testing is still estimated as a percentage of development effort. But for better planning, QA work should be estimated directly whenever possible.

## Why Testing Estimation Is Difficult

Testing does not always have a natural finish line.

In theory, the team can continue testing and finding more edge cases for a long time.

In practice, testing usually stops because of:

- release deadline;
- budget limit;
- agreed exit criteria;
- acceptable residual risk;
- completed scope;
- management decision.

That is why test estimation should be connected to scope, risk, priorities, and exit criteria.

## Testing As Part Of Development Estimation

Traditionally, test effort is often included inside the overall development estimate.

This can be too vague.

Example:

```text
Development estimate: 1000 hours
Testing estimate: 25% of development effort
Testing effort = 250 hours
```

This can be useful for early rough planning, but it may hide actual QA work.

Better estimation separates testing activities:

- test planning;
- test design;
- test data preparation;
- environment setup;
- execution;
- defect reporting;
- retesting;
- regression;
- reporting.

## When WBS Helps

Estimation techniques based on WBS can estimate testing activities more directly.

Examples:

- WBS;
- Wideband Delphi;
- Three Point Estimation;
- PERT.

With WBS, testing work is broken into smaller tasks that can be estimated independently.

Example:

| Testing Task | Estimate |
| --- | --- |
| Test planning | 8h |
| Test case design | 24h |
| Test data preparation | 8h |
| Smoke testing | 4h |
| Functional testing | 40h |
| Regression testing | 24h |
| Defect retesting | 16h |
| Test summary report | 4h |

This gives a more transparent estimate than a single percentage.

## Function Points And Test Cases

If software size is estimated in Function Points, testing effort can be derived from that.

One commonly cited formula from Capers Jones:

```text
Number of Test Cases = Number of Function Points x 1.2
```

Example:

```text
Function Points = 200
Number of Test Cases = 200 x 1.2 = 240
```

After estimating the number of test cases, the team can use productivity data.

Example:

```text
Test execution productivity = 30 test cases per day
Total test cases = 240

Execution effort = 240 / 30 = 8 tester-days
```

This should still include time for:

- test design;
- test data;
- defect reporting;
- retesting;
- regression;
- reporting.

## Percentage Of Development Effort Method

In this method, test effort is estimated as a percentage of development effort.

Development effort can be estimated using:

- Lines of Code;
- Function Points;
- Use-Case Points;
- historical project data.

Then the testing percentage is taken from the organization database.

Formula:

```text
Testing Effort = Development Effort x Testing Percentage
```

Example:

```text
Development effort = 1000 hours
Testing percentage = 30%

Testing effort = 1000 x 0.30 = 300 hours
```

This method is simple, but it depends heavily on historical data and project similarity.

## Estimating Independent Testing Projects

Some organizations provide independent verification and validation services.

In such projects, the whole project may consist mainly of testing activities.

When estimating a testing project, consider:

- team skills;
- domain knowledge;
- application complexity;
- historical data;
- bug cycles;
- resource availability;
- productivity variation;
- system environment;
- downtime;
- test data availability;
- automation coverage.

Testing projects need their own estimation model, not just a percentage of development work.

## Common Testing Estimation Techniques

Widely used testing estimation techniques include:

- PERT;
- Use-Case Points;
- WBS;
- Wideband Delphi;
- Function Point or Testing Point Analysis;
- Percentage Distribution;
- Experience-Based Estimation.

## PERT For Testing Estimation

PERT uses three estimates for each testing task:

- optimistic estimate;
- most likely estimate;
- pessimistic estimate.

Formula:

```text
Test Estimate = (O + 4M + L) / 6
```

Where:

- `O` = optimistic estimate;
- `M` = most likely estimate;
- `L` = pessimistic estimate.

Standard deviation:

```text
SD = (L - O) / 6
```

PERT is useful when testing tasks have uncertainty.

Example:

```text
Regression testing:
O = 3 days
M = 5 days
L = 11 days

Estimate = (3 + 4 x 5 + 11) / 6
Estimate = 5.67 days
```

## Use-Case Point Method

Use-Case Point estimation is based on use cases and actors.

Simplified process:

1. Count actors.
2. Calculate actor weights.
3. Count use cases.
4. Calculate use-case weights.
5. Calculate unadjusted use-case points.
6. Apply technical and environmental factors.
7. Calculate adjusted use-case points.
8. Convert use-case points to effort.

A simplified formula:

```text
Unadjusted Use-Case Points =
Unadjusted Actor Weight + Unadjusted Use-Case Weight
```

Then adjusted effort can be calculated using productivity assumptions.

Use-Case Points are useful when requirements are written as use cases.

## Work Breakdown Structure

WBS breaks testing work into smaller tasks.

Steps:

1. Create WBS for the testing project.
2. Divide modules into sub-modules.
3. Divide sub-modules into functionalities.
4. Divide functionalities into smaller testable parts.
5. Review all testing requirements.
6. Identify all tasks the team must complete.
7. Estimate effort for each task.
8. Estimate duration for each task.

WBS makes hidden QA work visible.

## Wideband Delphi

Wideband Delphi is a consensus-based estimation technique.

The process:

- WBS is shared with a group of experts;
- each person estimates independently;
- estimates are compared anonymously;
- assumptions are discussed;
- estimates are revised;
- final estimate is based on team consensus.

This method is useful because it combines team experience and structured discussion.

## Function Point And Testing Point Analysis

Function Points measure software functionality from the user perspective.

Testing effort can be derived from:

- requirement specification;
- prototype;
- function point count;
- historical productivity data.

Major Function Point components include:

- Internal Logical Files;
- External Interface Files;
- External Inputs;
- External Outputs;
- External Inquiries.

Capers Jones formula:

```text
Number of Test Cases = Number of Function Points x 1.2
```

Testing effort can then be estimated from the number of test cases and organizational productivity metrics.

## Percentage Distribution

Percentage Distribution assigns effort percentages to SDLC phases based on historical data.

Example:

| Phase | Percent Of Effort |
| --- | --- |
| Project Management | 7% |
| Requirements | 9% |
| Design | 16% |
| Coding | 26% |
| Testing | 27% |
| Documentation | 9% |
| Installation and Training | 6% |

Testing effort can be further distributed across test phases.

Example:

| Testing Phase | Percent |
| --- | --- |
| Integration Testing | 24% |
| System Testing | 52% |
| Acceptance Testing | 24% |

This method is simple, but it should be based on real historical data from similar projects.

## Experience-Based Testing Estimation

Experience-Based Estimation uses:

- expert judgment;
- previous project experience;
- historical metrics;
- domain knowledge;
- similar applications.

This method is useful when:

- formal data is limited;
- the team has strong experience;
- the project is similar to past work;
- quick estimation is needed.

It is less reliable when the domain or technology is new for the team.

## Factors That Affect Testing Effort

Testing effort can increase because of:

- unclear requirements;
- high application complexity;
- many integrations;
- unstable builds;
- many supported browsers or devices;
- strict compliance needs;
- weak test data;
- unavailable environments;
- high defect density;
- frequent changes;
- low automation coverage.

Testing effort can decrease because of:

- stable requirements;
- reusable test cases;
- reliable automation;
- good test data;
- mature CI/CD;
- experienced team;
- clear acceptance criteria.

## Common Mistakes

Common testing estimation mistakes:

- estimating only execution and forgetting test design;
- ignoring retesting;
- ignoring regression;
- not including test data preparation;
- assuming environment will always be available;
- using development percentage without project context;
- using FP/UCP formulas without productivity data;
- treating estimates as promises;
- not updating estimates when defect rate is higher than expected.

## Best Practices

Good practices:

- estimate testing separately when possible;
- break testing work into WBS tasks;
- use historical productivity data;
- include retesting and regression;
- document assumptions;
- account for environment downtime;
- include defect cycles;
- use multiple estimation techniques;
- revisit estimates during the project;
- communicate uncertainty as a range.

## Key Idea

Testing Estimation helps QA plan realistic effort and explain trade-offs between scope, time, quality, and risk.

Главная мысль:

> Testing effort is not just test execution. It includes planning, design, data, defects, regression, reporting, and uncertainty.

## Questions

1. Why is testing effort difficult to estimate?
2. How can Function Points be used to estimate test cases?
3. What is the Percentage of Development Effort method?
4. Why is WBS useful for testing estimation?
5. What factors can increase testing effort?

## What To Review Later

- PERT
- WBS
- Function Points
- Use-Case Points
- Wideband Delphi
- Percentage Distribution
- Experience-Based Estimation
