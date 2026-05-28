# Three Point Estimation

## Summary

Three Point Estimation is an estimation technique that uses three values for each task:

- optimistic estimate;
- most likely estimate;
- pessimistic estimate.

Instead of pretending that one exact number is always realistic, this method captures uncertainty.

It is useful for QA and software projects because testing work often depends on unclear requirements, unstable builds, defect count, environment readiness, and team availability.

## Three Estimates

Three Point Estimation uses:

| Symbol | Meaning |
| --- | --- |
| O | Optimistic estimate |
| M | Most likely estimate |
| L | Pessimistic estimate |

## Optimistic Estimate

The optimistic estimate is the best-case scenario.

It assumes:

- requirements are clear;
- environment works;
- few defects are found;
- no major blockers appear;
- team members are available.

Example:

```text
Regression testing will take 3 days if everything goes smoothly.
```

## Most Likely Estimate

The most likely estimate is the realistic expected scenario.

It assumes normal project conditions:

- some defects;
- some questions;
- some retesting;
- some small blockers.

Example:

```text
Regression testing will probably take 5 days.
```

## Pessimistic Estimate

The pessimistic estimate is the worst reasonable scenario.

It assumes:

- unstable build;
- many defects;
- environment issues;
- unclear requirements;
- additional retesting;
- delays from dependencies.

Example:

```text
Regression testing may take 9 days if several things go wrong.
```

## Formula

Three Point Estimate is based on the simple average.

Formula:

```text
E = (O + M + L) / 3
```

Where:

- `E` = estimate;
- `O` = optimistic estimate;
- `M` = most likely estimate;
- `L` = pessimistic estimate.

This follows a triangular distribution approach.

## Example

Suppose a QA task has these estimates:

```text
O = 3 days
M = 5 days
L = 9 days
```

Then:

```text
E = (3 + 5 + 9) / 3
E = 17 / 3
E = 5.67 days
```

So the task estimate is about:

```text
5.7 days
```

## Standard Deviation

Standard deviation shows how much uncertainty exists in the estimate.

For triangular distribution:

```text
SD = sqrt(((O - E)^2 + (M - E)^2 + (L - E)^2) / 2)
```

Where:

- `SD` = standard deviation;
- `E` = three point estimate.

## Example Standard Deviation

Using the same example:

```text
O = 3
M = 5
L = 9
E = 5.67
```

Formula:

```text
SD = sqrt(((3 - 5.67)^2 + (5 - 5.67)^2 + (9 - 5.67)^2) / 2)
```

Approximate result:

```text
SD = 3.06 days
```

A higher standard deviation means more uncertainty.

## Three Point Estimation Steps

## Step 1: Create WBS

Start with a Work Breakdown Structure.

Break the project or testing work into tasks.

Example:

- review requirements;
- create test cases;
- prepare test data;
- execute smoke tests;
- execute regression tests;
- retest defects;
- prepare test report.

## Step 2: Estimate Each Task

For each task, define:

- optimistic estimate;
- most likely estimate;
- pessimistic estimate.

Example:

| Task | O | M | L |
| --- | --- | --- | --- |
| Create test cases | 2d | 4d | 6d |
| Execute regression | 3d | 5d | 9d |
| Retest defects | 1d | 2d | 5d |

## Step 3: Calculate Mean For Each Task

For every task:

```text
E = (O + M + L) / 3
```

Example:

```text
Create test cases = (2 + 4 + 6) / 3 = 4d
Execute regression = (3 + 5 + 9) / 3 = 5.67d
Retest defects = (1 + 2 + 5) / 3 = 2.67d
```

## Step 4: Calculate Standard Deviation For Each Task

For each task:

```text
SD = sqrt(((O - E)^2 + (M - E)^2 + (L - E)^2) / 2)
```

This helps identify tasks with high uncertainty.

## Step 5: Calculate Project Estimate

Project estimate is the sum of task estimates.

Formula:

```text
E(Project) = sum of E(Task)
```

Example:

```text
E(Project) = 4 + 5.67 + 2.67
E(Project) = 12.34 days
```

## Step 6: Calculate Project Standard Deviation

Project standard deviation is calculated as:

```text
SD(Project) = sqrt(sum of SD(Task)^2)
```

This combines uncertainty across tasks.

## Confidence Levels

The estimate and standard deviation can be used to create confidence ranges.

Common confidence levels:

| Confidence Level | Range |
| --- | --- |
| About 68% | E +/- SD |
| About 90% | E +/- 1.645 x SD |
| About 95% | E +/- 2 x SD |
| About 99.7% | E +/- 3 x SD |

In project estimation, 95% confidence is commonly used:

```text
E +/- 2 x SD
```

This gives a wider and safer range than a single estimate.

## Example Confidence Range

Suppose:

```text
Project E = 12.34 days
Project SD = 2 days
```

95% confidence range:

```text
12.34 +/- (2 x 2)
12.34 +/- 4
```

Result:

```text
8.34 to 16.34 days
```

This communicates uncertainty more honestly than saying:

```text
The project will take exactly 12.34 days.
```

## Three Point Estimation Vs PERT

Three Point Estimation and PERT are related, but they are not exactly the same.

Three Point Estimation often uses a simple average:

```text
E = (O + M + L) / 3
```

PERT gives more weight to the most likely estimate:

```text
E = (O + 4M + P) / 6
```

Where `P` means pessimistic estimate.

The difference is important because PERT assumes the most likely estimate should influence the final estimate more strongly.

## When To Use Three Point Estimation

Use it when:

- uncertainty is high;
- tasks can be broken down clearly;
- the team wants realistic ranges;
- there are known risks;
- management needs confidence levels;
- historical data is limited;
- estimates should show best, likely, and worst cases.

It is especially useful for QA tasks where blockers and defect retesting can significantly change the schedule.

## Benefits

Benefits:

- captures uncertainty;
- avoids false precision;
- encourages risk discussion;
- gives more realistic ranges;
- helps identify high-risk tasks;
- supports better negotiation with stakeholders;
- can be combined with WBS and historical data.

## Limitations

Limitations:

- depends on quality of input estimates;
- optimistic and pessimistic values can be subjective;
- requires task breakdown;
- can be misunderstood as exact math;
- confidence levels are only as good as the assumptions behind them.

## Common Mistakes

Common mistakes:

- using unrealistic optimistic estimate;
- making pessimistic estimate too extreme;
- skipping WBS;
- not discussing assumptions;
- reporting only the mean and hiding uncertainty;
- confusing Three Point Estimation with PERT;
- treating the estimate as a promise.

## Key Idea

Three Point Estimation helps QA and project teams estimate with uncertainty instead of pretending every task has one exact duration.

Главная мысль:

> Good estimation does not remove uncertainty. It makes uncertainty visible.

## Questions

1. What are the three values in Three Point Estimation?
2. How is the Three Point Estimate calculated?
3. What does standard deviation show?
4. How can confidence levels be used?
5. What is the difference between Three Point Estimation and PERT?

## What To Review Later

- Work Breakdown Structure
- PERT
- Standard Deviation
- Confidence Level
- Estimation Range
- Project Risk
