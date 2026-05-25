# Software Testing Life Cycle (STLC)

## Summary

Software Testing Life Cycle, or STLC, is a structured testing process that helps a team validate software quality in a systematic way.

STLC usually includes six major phases: requirement analysis, test planning, test case development, test environment setup, test execution, and test cycle closure. Unlike ad-hoc testing, STLC defines clear activities, deliverables, entry criteria, and exit criteria for each stage.

The core idea is simple: testing should be a managed process, not a random set of checks at the end of development.

## Key Points

- STLC focuses on testing activities inside the broader SDLC.
- Each STLC phase has its own goals, activities, and deliverables.
- Requirement Traceability Matrix, or RTM, connects requirements to test cases.
- Entry and exit criteria work as quality gates between phases.
- STLC improves coverage, communication, and visibility into product quality.
- In Agile, CI/CD, and DevOps, STLC becomes more iterative and continuous.

## Notes

### STLC vs SDLC

SDLC, or Software Development Life Cycle, describes the full lifecycle of software creation: requirements, design, development, testing, deployment, and maintenance.

STLC is the testing-focused part of that process. It answers questions such as:

- what needs to be tested;
- how it should be tested;
- where and with which data testing will happen;
- who performs testing activities;
- which defects were found;
- whether the testing cycle can be closed.

In Waterfall, STLC often looks more sequential. In the V-Model, STLC aligns closely with development phases: requirements map to acceptance testing, system design maps to system testing, architecture maps to integration testing, and module design maps to unit testing.

In Agile, STLC happens iteratively inside each sprint. QA participates in requirement refinement, acceptance criteria review, testing increments, and regression checks.

### 1. Requirement Analysis

Requirement Analysis is the first and one of the most important STLC phases.

The QA team studies requirements from a testability perspective. The goal is to understand what can be tested, which conditions need coverage, and where requirements are ambiguous, conflicting, or incomplete.

Key activities:

- analyzing functional and non-functional requirements;
- clarifying requirements with business analysts, product owners, developers, and stakeholders;
- identifying test conditions;
- defining testing priorities;
- preparing the RTM;
- documenting environment, security, and data needs.

Deliverables:

- Requirement Traceability Matrix;
- requirement questions;
- feasibility notes;
- clarified testable requirements.

### 2. Test Planning

Test Planning defines the testing strategy.

At this stage, the QA lead or senior QA defines scope, objectives, risks, resources, schedule, tools, test approach, and deliverables. The Test Plan becomes the blueprint for the testing cycle.

Key activities:

- defining test scope;
- selecting manual, automation, or mixed approach;
- estimating effort;
- planning resources and roles;
- choosing tools and frameworks;
- defining risks, dependencies, and assumptions;
- agreeing on entry and exit criteria.

Deliverables:

- approved Test Plan;
- test strategy;
- effort estimation;
- schedule and milestones.

### 3. Test Case Development

Test Case Development turns the plan into executable checks.

The QA team creates test cases, checklists, test scripts, test data, and automation scripts where automation is appropriate. Each test case should have clear preconditions, steps, expected result, and test data.

Key activities:

- writing test cases;
- preparing test data;
- reviewing test cases;
- creating automation scripts for stable repetitive scenarios;
- updating the RTM;
- removing duplicates and improving coverage.

Deliverables:

- reviewed test cases;
- test scripts;
- test data;
- updated RTM.

### 4. Test Environment Setup

Test Environment Setup prepares the conditions where testing will be performed.

The environment may include hardware, operating systems, browser versions, mobile devices, databases, application servers, network settings, integrations, credentials, and test data.

Key activities:

- defining required hardware, software, and network configuration;
- deploying the application build;
- configuring databases and services;
- preparing test accounts and test data;
- checking integrations;
- running smoke tests for environment readiness.

Deliverables:

- environment setup checklist;
- smoke test results;
- ready test environment.

### 5. Test Execution

Test Execution is the phase where testers run prepared test cases against the build in the prepared environment.

Results are logged as pass, fail, blocked, or skipped. If the actual result differs from the expected result, QA reports a defect with severity, priority, steps to reproduce, environment details, logs, screenshots, or video.

Key activities:

- executing planned tests;
- running manual and automated tests;
- reporting defects;
- retesting fixed defects;
- performing regression testing;
- updating RTM and execution status.

Common execution cycles:

- sanity testing;
- smoke testing;
- functional testing;
- re-testing;
- regression testing.

Deliverables:

- test execution logs;
- defect reports;
- updated RTM;
- test status report.

### 6. Test Cycle Closure

Test Cycle Closure closes the testing cycle and turns team experience into useful insights.

The QA team analyzes results, collects metrics, prepares final reports, and documents lessons learned.

Key activities:

- preparing the test summary report;
- analyzing defect trends;
- checking exit criteria;
- running a retrospective;
- archiving test artifacts;
- creating recommendations for future cycles.

Deliverables:

- test closure report;
- quality metrics dashboard;
- lessons learned;
- archived artifacts.

## Entry and Exit Criteria

Entry criteria are the conditions required before a phase can begin.

Exit criteria are the conditions required before a phase can be closed.

They work as quality gates. A team should not move forward if inputs are not ready or phase outputs are not verified.

| STLC Phase | Entry Criteria | Exit Criteria |
| --- | --- | --- |
| Requirement Analysis | Requirements are available, business specifications are finalized | RTM is created, test strategy is defined |
| Test Planning | Requirements analysis is complete | Test plan is approved, resources are allocated |
| Test Case Development | Test plan is approved, requirements are understood | Test cases are reviewed, test data is prepared |
| Test Environment Setup | Environment requirements are defined | Environment is ready, smoke testing passed |
| Test Execution | Test cases are ready, build is deployed, environment is stable | Test cases are executed, critical defects are resolved |
| Test Closure | Test execution is complete, exit criteria are met | Closure report is signed off, artifacts are archived |

### Automation in STLC

Automation can be considered during requirement analysis and planning, when the team evaluates which checks are good candidates for automation.

Best candidates for automation:

- regression tests;
- smoke tests;
- stable repetitive functional tests;
- tests that run across multiple environments;
- high-value scenarios with frequent execution.

Automation does not replace STLC. It strengthens STLC, especially during execution and regression cycles.

### STLC in Agile, CI/CD and DevOps

In Agile, STLC becomes shorter and more repetitive. Requirement analysis, planning, test design, and execution may happen inside each sprint.

In CI/CD, testing becomes part of the pipeline. Automated tests run on code commit, build, or deployment. This gives faster feedback and helps catch defects earlier.

In DevOps, STLC becomes continuous testing: quality is checked throughout the delivery process, not only before release.

### Metrics and Quality Reports

STLC becomes stronger when the team collects metrics.

Useful metrics:

- test execution rate;
- pass/fail ratio;
- defect density;
- defect severity distribution;
- defect resolution time;
- test coverage;
- requirement coverage;
- escaped defects;
- automation coverage.

A quality dashboard helps stakeholders see testing progress and release readiness.

### Common Pitfalls and Best Practices

#### Testing Starts Too Late

If QA joins only after development, defects become more expensive.

Best practice: use shift-left testing. QA participates in requirements and design discussions.

#### Unclear Requirements

Unclear requirements lead to invalid test cases.

Best practice: ask questions early, use RTM, and review acceptance criteria.

#### Weak Test Data

Without proper test data, some scenarios cannot be verified.

Best practice: plan test data during test case development.

#### Poor Communication

Gaps between QA, development, and business create coverage gaps.

Best practice: use shared tools, regular syncs, and clear defect reports.

#### Automation Without Strategy

Automating everything can become expensive and fragile.

Best practice: automate stable, repetitive, and business-critical checks.

## Commands / Terms

- `STLC` - Software Testing Life Cycle.
- `SDLC` - Software Development Life Cycle.
- `RTM` - Requirement Traceability Matrix.
- `Entry Criteria` - conditions required to start a phase.
- `Exit Criteria` - conditions required to close a phase.
- `Test Plan` - document describing strategy, scope, resources, risks, and schedule.
- `Test Case` - a specific check with steps and expected result.
- `Test Environment` - environment where tests are executed.
- `Test Execution` - running tests and recording results.
- `Test Closure Report` - final report for a testing cycle.
- `Shift-left testing` - involving QA early in requirements and design.
- `Continuous testing` - testing embedded into the delivery pipeline.

## Questions

1. What is STLC?
2. How is STLC different from SDLC?
3. What are the main phases of STLC?
4. Why is requirement analysis important for QA?
5. What is RTM and why is it useful?
6. What is the difference between entry criteria and exit criteria?
7. What deliverables are created during test planning?
8. What happens during test execution?
9. Why is test cycle closure important?
10. How does STLC change in Agile or CI/CD?

## What To Review Later

- STLC phases and deliverables
- Entry vs exit criteria
- RTM and requirement coverage
- Test Plan structure
- Defect lifecycle
- Test closure report
- STLC in Agile and CI/CD
