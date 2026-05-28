# PERT

## Summary

PERT means Project Evaluation and Review Technique.

PERT is an estimation technique that uses three values:

- optimistic estimate;
- most likely estimate;
- pessimistic estimate.

Unlike simple Three Point Estimation, PERT gives more weight to the most likely estimate.

It is useful when project work has uncertainty and the team wants to calculate a more realistic weighted estimate.

## Three Estimates

PERT uses:

| Symbol | Meaning |
| --- | --- |
| O | Optimistic estimate |
| M | Most likely estimate |
| L | Pessimistic estimate |

## Optimistic Estimate

The optimistic estimate is the best reasonable case.

It assumes:

- no major blockers;
- stable environment;
- clear requirements;
- few defects;
- available resources.

## Most Likely Estimate

The most likely estimate is the expected realistic case.

It represents the duration or effort that is most probable under normal conditions.

PERT gives this estimate more weight than the optimistic and pessimistic estimates.

## Pessimistic Estimate

The pessimistic estimate is the worst reasonable case.

It includes realistic problems such as:

- unclear requirements;
- unstable builds;
- more defects than expected;
- environment issues;
- delays from dependencies.

## PERT Formula

PERT estimate is based on weighted average.

Formula:

```text
E = (O + 4M + L) / 6
```

Where:

- `E` = PERT estimate;
- `O` = optimistic estimate;
- `M` = most likely estimate;
- `L` = pessimistic estimate.

The most likely estimate is multiplied by `4`, so it has stronger influence on the final result.

PERT follows a beta distribution approach.

## Example

Suppose a QA task has these estimates:

```text
O = 3 days
M = 5 days
L = 11 days
```

PERT estimate:

```text
E = (3 + 4 x 5 + 11) / 6
E = (3 + 20 + 11) / 6
E = 34 / 6
E = 5.67 days
```

So the PERT estimate is about:

```text
5.7 days
```

## Standard Deviation

Standard deviation measures uncertainty in the estimate.

In PERT:

```text
SD = (L - O) / 6
```

Example:

```text
O = 3
L = 11

SD = (11 - 3) / 6
SD = 8 / 6
SD = 1.33 days
```

The larger the gap between optimistic and pessimistic estimates, the higher the uncertainty.

## PERT Estimation Steps

## Step 1: Create WBS

Start with a Work Breakdown Structure.

Break the project into tasks.

Examples:

- requirements review;
- test planning;
- test case design;
- test data preparation;
- test execution;
- defect retesting;
- regression testing;
- test reporting.

## Step 2: Estimate Each Task

For each task, identify:

- optimistic estimate;
- most likely estimate;
- pessimistic estimate.

Example:

| Task | O | M | L |
| --- | --- | --- | --- |
| Test case design | 2d | 4d | 8d |
| Regression testing | 3d | 5d | 11d |
| Defect retesting | 1d | 2d | 6d |

## Step 3: Calculate PERT Estimate For Each Task

Formula:

```text
E = (O + 4M + L) / 6
```

Example:

```text
Test case design = (2 + 4 x 4 + 8) / 6 = 4.33d
Regression testing = (3 + 4 x 5 + 11) / 6 = 5.67d
Defect retesting = (1 + 4 x 2 + 6) / 6 = 2.5d
```

## Step 4: Calculate Standard Deviation For Each Task

Formula:

```text
SD = (L - O) / 6
```

Example:

```text
Regression testing SD = (11 - 3) / 6 = 1.33d
```

## Step 5: Repeat For All Tasks

Calculate `E` and `SD` for every task in the WBS.

## Step 6: Calculate Project Estimate

Project estimate is the sum of task estimates.

Formula:

```text
E(Project) = sum of E(Task)
```

Example:

```text
E(Project) = 4.33 + 5.67 + 2.5
E(Project) = 12.5 days
```

## Step 7: Calculate Project Standard Deviation

Project standard deviation is calculated as:

```text
SD(Project) = sqrt(sum of SD(Task)^2)
```

This combines task uncertainty into project-level uncertainty.

## Confidence Levels

PERT estimate and standard deviation can be converted to confidence ranges.

Common ranges:

| Confidence Level | Range |
| --- | --- |
| About 68% | E +/- SD |
| About 90% | E +/- 1.645 x SD |
| About 95% | E +/- 2 x SD |
| About 99.7% | E +/- 3 x SD |

Commonly, 95% confidence is used:

```text
E +/- 2 x SD
```

## Example Confidence Range

Suppose:

```text
Project estimate = 12.5 days
Project SD = 1.8 days
```

95% confidence range:

```text
12.5 +/- (2 x 1.8)
12.5 +/- 3.6
```

Result:

```text
8.9 to 16.1 days
```

This is more honest than claiming the project will take exactly `12.5 days`.

## PERT And Critical Path Method

PERT is often used with Critical Path Method, or CPM.

CPM identifies the tasks that are critical to the project schedule.

If a critical path task is delayed, the whole project may be delayed.

Together:

- PERT helps estimate uncertain task durations;
- CPM helps understand which tasks drive the project timeline.

## Three Point Estimation Vs PERT

Three Point Estimation and PERT both use optimistic, most likely, and pessimistic values.

But they calculate estimates differently.

| Aspect | Three Point Estimation | PERT |
| --- | --- | --- |
| Average type | Simple average | Weighted average |
| Distribution | Triangular distribution | Beta distribution |
| Formula | `E = (O + M + L) / 3` | `E = (O + 4M + L) / 6` |
| Most likely estimate | Same weight as others | 4 times stronger |
| Standard deviation | `sqrt(((O - E)^2 + (M - E)^2 + (L - E)^2) / 2)` | `(L - O) / 6` |
| Common use | Smaller repetitive projects | Larger uncertain or non-repetitive projects |

## When To Use PERT

PERT is useful when:

- work has uncertainty;
- project is large;
- work is non-repetitive;
- estimates should include probability thinking;
- dependencies matter;
- task duration can vary significantly;
- the team wants confidence ranges.

For QA, PERT can be useful for:

- large regression cycles;
- performance testing preparation;
- test automation setup;
- environment migration testing;
- compliance testing;
- complex release validation.

## Benefits

Benefits:

- handles uncertainty better than a single estimate;
- gives more weight to realistic estimate;
- supports confidence ranges;
- works well with WBS;
- useful for planning complex projects;
- can be combined with CPM;
- helps communicate risk in schedules.

## Limitations

Limitations:

- depends on quality of O, M, and L values;
- requires task breakdown;
- can look more precise than it really is;
- formula does not remove uncertainty;
- estimates can still be biased;
- needs explanation for stakeholders.

## Common Mistakes

Common mistakes:

- confusing PERT with simple Three Point Estimation;
- using unrealistic optimistic or pessimistic values;
- skipping WBS;
- reporting only the final number without confidence range;
- ignoring task dependencies;
- treating the estimate as a commitment;
- forgetting to update estimates when project conditions change.

## Key Idea

PERT helps estimate uncertain work by using optimistic, most likely, and pessimistic values, while giving extra weight to the most likely outcome.

Главная мысль:

> PERT does not make uncertainty disappear. It helps turn uncertainty into a usable planning range.

## Questions

1. What is PERT?
2. How is PERT estimate calculated?
3. Why is the most likely estimate weighted more heavily?
4. What is the standard deviation formula in PERT?
5. What is the difference between PERT and Three Point Estimation?

## What To Review Later

- Three Point Estimation
- Work Breakdown Structure
- Standard Deviation
- Confidence Level
- Critical Path Method
- Project Estimation
