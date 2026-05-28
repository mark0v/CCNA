# Use-Case Points

## Summary

Use-Case Points, or UCP, is a software estimation technique used to measure software size based on use cases.

A use case describes a series of related interactions between an actor and a system that helps the actor achieve a goal.

Use-Case Points are similar in purpose to Function Points: both help estimate software size from a functional perspective.

UCP estimation is based on:

- number and complexity of use cases;
- number and complexity of actors;
- technical complexity factors;
- environmental complexity factors.

## What Is A Use Case?

A use case captures a functional requirement of a system.

It usually describes:

- actor;
- goal;
- preconditions;
- main flow;
- alternative flows;
- postconditions.

An actor can be:

- a user;
- another system;
- an external application;
- a device;
- a service.

Use cases are usually written in text form.

## What Are Use-Case Points?

Use-Case Points measure software size using use cases.

The method was introduced by Gustav Karner in 1993.

It is useful when requirements are already described as use cases.

Before using UCP, the team should make sure that use cases are:

- goal-oriented;
- written at a similar level of detail;
- clear enough to count transactions;
- complete enough for estimation.

If use cases are inconsistent or vague, the estimate will be weak.

## UCP Counting Process

The Use-Case Points process has four main steps:

1. Calculate Unadjusted Use-Case Points.
2. Adjust for technical complexity.
3. Adjust for environmental complexity.
4. Calculate adjusted Use-Case Points.

Formula:

```text
UCP = UUCP x TCF x EF
```

Where:

- `UUCP` = Unadjusted Use-Case Points;
- `TCF` = Technical Complexity Factor;
- `EF` = Environmental Factor.

## Step 1: Calculate Unadjusted Use-Case Points

Unadjusted Use-Case Points are calculated from:

- Unadjusted Use-Case Weight;
- Unadjusted Actor Weight.

Formula:

```text
UUCP = UUCW + UAW
```

Where:

- `UUCW` = Unadjusted Use-Case Weight;
- `UAW` = Unadjusted Actor Weight.

## Step 1.1: Determine Unadjusted Use-Case Weight

First, count transactions in each use case.

If use cases are written at user-goal level, a transaction is usually equivalent to a step in the use case.

Then classify each use case.

| Use Case Complexity | Number Of Transactions | Weight |
| --- | --- | --- |
| Simple | 3 or fewer | 5 |
| Average | 4 to 7 | 10 |
| Complex | More than 7 | 15 |

Then calculate:

```text
UUCW = (5 x NSUC) + (10 x NAUC) + (15 x NCUC)
```

Where:

- `NSUC` = number of simple use cases;
- `NAUC` = number of average use cases;
- `NCUC` = number of complex use cases.

Example:

```text
Simple use cases: 4
Average use cases: 6
Complex use cases: 2

UUCW = (5 x 4) + (10 x 6) + (15 x 2)
UUCW = 20 + 60 + 30 = 110
```

## Step 1.2: Determine Unadjusted Actor Weight

Actors are classified by complexity.

| Actor Complexity | Example | Weight |
| --- | --- | --- |
| Simple | System with defined API | 1 |
| Average | System interacting through protocol | 2 |
| Complex | User interacting through GUI | 3 |

Then calculate:

```text
UAW = (1 x NSA) + (2 x NAA) + (3 x NCA)
```

Where:

- `NSA` = number of simple actors;
- `NAA` = number of average actors;
- `NCA` = number of complex actors.

Example:

```text
Simple actors: 2
Average actors: 1
Complex actors: 3

UAW = (1 x 2) + (2 x 1) + (3 x 3)
UAW = 2 + 2 + 9 = 13
```

## Step 1.3: Calculate UUCP

After calculating `UUCW` and `UAW`, add them.

Example:

```text
UUCW = 110
UAW = 13

UUCP = 110 + 13 = 123
```

This gives the unadjusted size before technical and environmental adjustments.

## Step 2: Adjust For Technical Complexity

Technical Complexity Factor adjusts the estimate based on technical characteristics of the project.

Technical factors include:

| Factor | Description | Weight |
| --- | --- | --- |
| T1 | Distributed system | 2.0 |
| T2 | Response time or throughput objectives | 1.0 |
| T3 | End-user efficiency | 1.0 |
| T4 | Complex internal processing | 1.0 |
| T5 | Reusable code required | 1.0 |
| T6 | Easy to install | 0.5 |
| T7 | Easy to use | 0.5 |
| T8 | Portable | 2.0 |
| T9 | Easy to change | 1.0 |
| T10 | Concurrent processing | 1.0 |
| T11 | Special security objectives | 1.0 |
| T12 | Direct access for third parties | 1.0 |
| T13 | Special user training required | 1.0 |

Each factor is rated from `0` to `5`:

- `0` = irrelevant;
- `5` = very important.

For each factor:

```text
Impact = Weight x Rated Value
```

Then sum all impacts to get `TFactor`.

Formula:

```text
TCF = 0.6 + (0.01 x TFactor)
```

Example:

```text
TFactor = 42

TCF = 0.6 + (0.01 x 42)
TCF = 0.6 + 0.42 = 1.02
```

## Step 3: Adjust For Environmental Complexity

Environmental Factor adjusts the estimate based on the project environment and team context.

Environmental factors include:

| Factor | Description | Weight |
| --- | --- | --- |
| F1 | Familiar with the project model | 1.5 |
| F2 | Application experience | 0.5 |
| F3 | Object-oriented experience | 1.0 |
| F4 | Lead analyst capability | 0.5 |
| F5 | Motivation | 1.0 |
| F6 | Stable requirements | 2.0 |
| F7 | Part-time staff | -1.0 |
| F8 | Difficult programming language | -1.0 |

Each factor is rated from `0` to `5`.

For each factor:

```text
Impact = Weight x Rated Value
```

Then sum all impacts to get `EFactor`.

Formula:

```text
EF = 1.4 + (-0.03 x EFactor)
```

Example:

```text
EFactor = 20

EF = 1.4 + (-0.03 x 20)
EF = 1.4 - 0.6 = 0.8
```

## Step 4: Calculate Adjusted Use-Case Points

After `UUCP`, `TCF`, and `EF` are known:

```text
UCP = UUCP x TCF x EF
```

Example:

```text
UUCP = 123
TCF = 1.02
EF = 0.8

UCP = 123 x 1.02 x 0.8
UCP = 100.368
```

So the adjusted size is about:

```text
100 UCP
```

## Using UCP For Effort Estimation

After calculating UCP, the team can estimate effort using productivity rate.

Example:

```text
UCP = 100
Productivity = 20 hours per UCP

Estimated effort = 100 x 20 = 2000 hours
```

The productivity rate should come from:

- historical team data;
- organization metrics;
- similar past projects;
- industry benchmarks.

Without a realistic productivity rate, UCP gives size but not reliable effort.

## Advantages

Advantages of Use-Case Points:

- can be measured early in the project lifecycle;
- based on use cases that describe functional requirements;
- independent of implementation technology;
- useful for overall project size estimation;
- easy to understand when use cases are well-written;
- works well when use cases are the main requirements format.

## Disadvantages

Disadvantages:

- can be used only when requirements are written as use cases;
- depends on well-structured and consistent use cases;
- inaccurate if use cases have different levels of detail;
- technical and environmental factor ratings can be subjective;
- less useful for iteration-by-iteration Agile planning;
- requires experience to assign values reliably.

## UCP Vs Function Points

| Aspect | Use-Case Points | Function Points |
| --- | --- | --- |
| Based on | Use cases and actors | Functional data and transactions |
| Best when | Requirements are written as use cases | Functional requirements are available |
| Main components | Use cases, actors, technical/environmental factors | ILF, EIF, EI, EO, EQ |
| Estimation timing | Early, if use cases exist | Early, if functional scope is clear |
| Risk | Depends on use case quality | Depends on correct function counting |

Both approaches measure functional size, but they use different inputs.

## Common Mistakes

Common mistakes:

- estimating with vague use cases;
- counting steps inconsistently;
- mixing use cases written at different detail levels;
- assigning factor ratings without team discussion;
- ignoring environmental risks;
- using UCP without historical productivity data;
- treating UCP as exact instead of approximate.

## Key Idea

Use-Case Points help estimate software size from use cases and actors, then adjust the result based on technical and environmental complexity.

Главная мысль:

> UCP is useful when use cases are clear, consistent, and detailed enough to support estimation.

## Questions

1. What are Use-Case Points?
2. How is UUCW calculated?
3. How is UAW calculated?
4. What is the purpose of TCF and EF?
5. What are the main limitations of UCP?

## What To Review Later

- Use Cases
- Actors
- Technical Complexity Factor
- Environmental Factor
- Function Points
- Project Estimation
