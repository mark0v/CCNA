# Test Coverage

## Summary

Test Coverage is a QA metric that helps evaluate how much of the product has been covered by testing.

It can measure coverage of:

- requirements;
- source code;
- execution paths;
- business flows;
- test conditions.

The main idea is simple: stakeholders need to understand not only whether the product was tested, but also how much and what exactly was tested.

## Why Test Coverage Matters

In software testing, we often talk about product quality:

- are features working;
- are defects fixed;
- is the product stable;
- is the release ready.

But the quality of testing itself also needs to be evaluated.

QA metrics help answer questions like:

- Were the most important requirements tested?
- Are there requirements without test cases?
- Are there redundant tests?
- Which parts of the code were executed during testing?
- Which areas still need more coverage?
- Is testing effort focused on the right risks?

Test Coverage is one of those metrics.

It helps teams see what is already covered and where gaps remain.

## Important Limitation

Higher test coverage usually means better visibility, but it does not automatically mean better quality.

Also, 100% full testing is usually impossible.

Software can have too many:

- input combinations;
- user flows;
- environments;
- edge cases;
- data states;
- integrations;
- timing conditions.

So test coverage should be used as a guide, not as a magic guarantee.

Главная мысль:

> High coverage helps reduce risk, but it does not prove that there are no defects.

## Main Types Of Test Coverage

There are several common approaches to evaluating test coverage.

## Requirements Coverage

Requirements Coverage shows how many product requirements are covered by test cases.

This metric is especially useful when requirements are clear and atomic.

Formula:

```text
Requirements Coverage =
(Number of requirements covered by test cases / Total number of requirements) x 100%
```

Example:

```text
Total requirements: 100
Requirements covered by test cases: 85

Requirements Coverage = 85 / 100 x 100% = 85%
```

This means 85% of requirements have at least one related test case.

## How To Track Requirements Coverage

To track requirements coverage:

1. Break requirements into clear requirement items.
2. Create test cases for those requirements.
3. Link each test case to the requirement it verifies.
4. Analyze uncovered requirements.
5. Remove or review test cases that do not map to any requirement.

The links between requirements and test cases are usually stored in a Requirements Traceability Matrix, or RTM.

## Requirements Traceability Matrix

A traceability matrix shows the relationship between requirements and test cases.

It helps answer:

- which test cases cover this requirement;
- which requirements have no test cases;
- which requirements have too many test cases;
- which test cases do not cover any requirement;
- what should be retested when a requirement changes.

Example:

| Requirement ID | Requirement | Test Cases | Status |
| --- | --- | --- | --- |
| REQ-001 | User can log in with valid credentials | TC-001, TC-002 | Covered |
| REQ-002 | User can reset password | TC-010, TC-011 | Covered |
| REQ-003 | User account locks after failed attempts | - | Not Covered |

In this example, `REQ-003` needs test cases because it is currently uncovered.

## Code Coverage

Code Coverage shows how much executable code was executed while running tests.

Formula:

```text
Code Coverage =
(Number of lines of code covered by tests / Total number of lines of code) x 100%
```

Example:

```text
Total executable lines: 1000
Lines executed by tests: 760

Code Coverage = 760 / 1000 x 100% = 76%
```

Code coverage is usually measured with special tools.

Examples of coverage tools:

- Clover;
- JaCoCo;
- Istanbul;
- Coverage.py;
- nyc.

These tools help identify which lines, branches, methods, or files were executed during tests.

## What Code Coverage Can Show

Code coverage can help identify:

- untested code;
- dead code;
- duplicated tests;
- risky modules;
- missing unit tests;
- areas that need more checks.

It is often used during white box testing and automated testing.

Common levels:

- unit testing;
- integration testing;
- system testing.

## Code Coverage Does Not Equal Good Testing

High code coverage can still miss important bugs.

Example:

A test can execute a line of code but not verify the result properly.

So code coverage tells us what was executed, but not always whether behavior was checked well.

That is why code coverage should be combined with:

- assertions;
- requirements coverage;
- risk analysis;
- exploratory testing;
- reviews.

## Control Flow Coverage

Control Flow Coverage focuses on execution paths through the code.

It checks whether tests cover different paths in the program logic.

To analyze control flow, teams can build a Control Flow Graph.

A control flow graph usually contains:

- process blocks;
- decision or alternative points;
- connection points;
- entry and exit points.

## Control Flow Graph Blocks

### Process Block

A process block represents a simple action or operation.

It usually has:

- one entry point;
- one exit point.

Example:

```text
Calculate total price
```

### Alternative Point

An alternative point represents a decision.

It usually has:

- one entry point;
- two or more exit points.

Example:

```text
If user is authenticated:
  allow access
Else:
  show login page
```

### Connection Point

A connection point combines multiple paths.

It usually has:

- two or more entry points;
- one exit point.

Example:

```text
Both successful login and restored session lead to dashboard
```

## Levels Of Control Flow Coverage

Control flow can be checked at different levels.

Examples:

- statement coverage;
- branch coverage;
- condition coverage;
- path coverage.

### Statement Coverage

Checks whether each statement was executed at least once.

### Branch Coverage

Checks whether each branch of a decision was executed.

Example:

- `if` branch;
- `else` branch.

### Condition Coverage

Checks whether each condition inside a decision was evaluated as both true and false.

### Path Coverage

Checks different possible paths through the program.

Full path coverage can become very large and is often impossible for complex systems.

## Test Coverage In Practice

Test coverage should help the team make decisions.

Useful questions:

- Which requirements are not covered?
- Which critical flows have no tests?
- Which modules have low code coverage?
- Which risk areas need more attention?
- Which tests are redundant?
- Which areas changed recently and need regression coverage?

Coverage is most valuable when it guides better testing decisions.

## Common Mistakes

Common mistakes with test coverage:

- treating 100% coverage as proof that the product has no bugs;
- measuring coverage but not analyzing gaps;
- focusing only on code coverage and ignoring requirements;
- writing weak tests just to increase coverage percentage;
- ignoring high-risk areas with low coverage;
- keeping test cases that do not verify any requirement or risk.

Coverage is a tool. It should not become the goal by itself.

## Key Idea

Test Coverage helps evaluate how thoroughly testing covers the product.

It gives visibility into coverage gaps, but it does not replace good test design, risk analysis, and critical thinking.

Главная мысль:

> Coverage tells us where we looked. It does not guarantee that we looked well.

## Questions

1. What is Test Coverage?
2. What is Requirements Coverage?
3. What is Code Coverage?
4. Why does 100% coverage not guarantee a bug-free product?
5. What is a Requirements Traceability Matrix?

## What To Review Later

- Requirements Traceability Matrix
- Code Coverage
- Statement Coverage
- Branch Coverage
- Path Coverage
- QA Metrics
