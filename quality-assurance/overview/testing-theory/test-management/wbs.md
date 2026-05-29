# Work Breakdown Structure

## Summary

Work Breakdown Structure, or WBS, is a deliverable-oriented decomposition of a project into smaller manageable parts.

In simple words, WBS breaks a large project into smaller pieces of work that can be estimated, assigned, scheduled, monitored, and controlled.

WBS helps with:

- size estimation;
- effort estimation;
- cost estimation;
- schedule planning;
- task assignment;
- progress tracking;
- risk visibility.

According to PMBOK, WBS is a deliverable-oriented hierarchical decomposition of the work to be executed by the project team.

## Why WBS Matters

A project can feel too big to estimate directly.

WBS helps by turning:

```text
Test the application
```

into smaller tasks:

- review requirements;
- create test plan;
- design test cases;
- prepare test data;
- execute smoke tests;
- execute regression tests;
- retest defects;
- prepare test summary report.

Smaller tasks are easier to understand and estimate.

## WBS Element

A WBS element can represent:

- product;
- service;
- data;
- deliverable;
- activity;
- task;
- combination of these.

In QA, WBS elements can include:

- test plan;
- test cases;
- test data;
- test environment;
- automation scripts;
- test execution;
- defect reports;
- test summary report.

## WBS Representation

WBS is usually represented in two common formats:

- outline view;
- tree structure view.

## Outline View

Outline view uses an indented hierarchical list.

Example:

```text
Software Testing Project

1. Test Planning
   1.1 Review requirements
   1.2 Define test scope
   1.3 Identify risks
   1.4 Create test plan

2. Test Design
   2.1 Create test scenarios
   2.2 Write test cases
   2.3 Prepare test data
   2.4 Review test cases

3. Test Execution
   3.1 Run smoke tests
   3.2 Run functional tests
   3.3 Run regression tests
   3.4 Log defects

4. Test Closure
   4.1 Prepare test summary report
   4.2 Archive test artifacts
   4.3 Conduct retrospective
```

This format is simple, readable, and easy to update.

## Tree Structure View

Tree structure view shows the WBS as a hierarchy, similar to an organization chart.

Example:

```text
Software Testing Project
├── Test Planning
├── Test Design
├── Test Execution
└── Test Closure
```

This view is useful when stakeholders need a quick visual overview of the project structure.

## Types Of WBS

There are two common types:

- Functional WBS;
- Activity WBS.

## Functional WBS

Functional WBS breaks the system based on functions or features.

Example:

```text
Application
├── Login
├── User Profile
├── Search
├── Checkout
└── Reports
```

This is useful for estimating software size and functional scope.

For QA, functional WBS helps identify what features need test coverage.

## Activity WBS

Activity WBS breaks the project based on activities and tasks.

Example:

```text
Testing
├── Test Planning
├── Test Case Design
├── Test Data Preparation
├── Test Execution
├── Defect Retesting
└── Test Reporting
```

This is useful for estimating effort, schedule, and resource needs.

## Estimating Size With WBS

To estimate size:

1. Start with Functional WBS.
2. Look at the leaf nodes.
3. Estimate each feature or function.
4. Use Analogous Estimation, Function Points, Use-Case Points, or Wideband Delphi.
5. Combine estimates into total project size.

Leaf nodes are the lowest-level elements in the WBS.

Example:

```text
Checkout
├── Add item to cart
├── Apply discount
├── Calculate shipping
├── Process payment
└── Create order
```

Each leaf node can be estimated more easily than the whole checkout flow.

## Estimating Effort With WBS

To estimate effort:

1. Create an Activity WBS.
2. Split large tasks into smaller tasks.
3. Estimate each task.
4. Use Wideband Delphi or Three Point Estimation.
5. Combine estimates.

A useful rule of thumb:

> If a task is larger than one working day, consider splitting it.

Smaller tasks are easier to estimate and track.

## QA Example

Example WBS for testing a payment feature:

```text
Payment Testing
├── Requirement Review
│   ├── Review payment requirements
│   └── Clarify edge cases
├── Test Design
│   ├── Create positive test cases
│   ├── Create negative test cases
│   ├── Create boundary test cases
│   └── Review test cases
├── Test Data
│   ├── Prepare valid cards
│   ├── Prepare declined cards
│   └── Prepare refund scenarios
├── Test Execution
│   ├── Execute smoke tests
│   ├── Execute functional tests
│   ├── Execute integration tests
│   └── Execute regression tests
└── Reporting
    ├── Log defects
    ├── Retest fixes
    └── Prepare test summary
```

This structure makes estimation more concrete.

## Scheduling With WBS

Once the WBS is ready and estimates are known, the team can schedule tasks.

Scheduling should consider:

- precedence;
- concurrence;
- critical path;
- task dependencies;
- resource availability;
- milestones.

## Precedence

Precedence means one task must happen before another.

Example:

```text
Test cases must be written before they can be executed.
```

## Concurrence

Concurrent tasks can happen at the same time.

Example:

```text
One QA prepares test data while another QA writes test cases.
```

Parallel work can shorten the schedule, but only when dependencies allow it.

## Critical Path

Critical Path is the sequence of tasks that determines the project completion date.

If a task on the critical path is delayed, the whole project may be delayed.

Example:

```text
Requirements approval → Test design → Environment setup → Test execution → Sign-off
```

If environment setup is delayed, test execution cannot start, so the release may slip.

## Critical Path Method

Critical Path Method, or CPM, is used to identify and optimize the critical path.

Important idea:

> Accelerating non-critical tasks does not directly shorten the project schedule.

If the bottleneck is test environment setup, making documentation faster may not change the final release date.

## Task Dependency Relationships

Common dependency relationships:

- Finish-to-Start;
- Finish-to-Finish.

## Finish-To-Start

Finish-to-Start, or FS, means Task B cannot start until Task A is completed.

Example:

```text
Test execution cannot start until build deployment is complete.
```

## Finish-To-Finish

Finish-to-Finish, or FF, means Task B cannot finish until Task A is completed.

Example:

```text
Test summary report cannot be completed until test execution is completed.
```

## Gantt Chart

A Gantt chart is a bar chart that shows a project schedule.

It usually shows:

- tasks;
- start dates;
- finish dates;
- task duration;
- dependencies;
- milestones.

WBS can be used as input for a Gantt chart.

This helps the team see when each task starts and ends.

## Milestones

Milestones are important points in the schedule.

They usually have zero duration.

Examples:

- Requirements Approved;
- Test Plan Approved;
- Test Design Complete;
- Environment Ready;
- Regression Complete;
- Release Sign-off.

Milestones are often shown as diamonds in a Gantt chart.

They help stakeholders track major progress points.

## Advantages Of WBS

WBS gives several advantages:

- identifies the full scope of work;
- reduces the chance of missing important tasks;
- improves cost and schedule estimation;
- encourages team participation;
- creates a basis for task assignment;
- supports task-level monitoring and control;
- helps communicate project structure to stakeholders;
- makes large work easier to manage.

When the team reviews WBS together, hidden work becomes visible.

## WBS And Estimation Techniques

WBS works well with other estimation techniques:

- Analogous Estimation;
- Wideband Delphi;
- Three Point Estimation;
- PERT;
- Function Points;
- Use-Case Points.

WBS provides the structure. Estimation techniques provide the numbers.

## Common Mistakes

Common mistakes:

- creating WBS without stakeholder review;
- breaking work down too little;
- breaking work down too much;
- mixing deliverables and random activities without structure;
- forgetting QA activities like retesting and reporting;
- ignoring dependencies;
- not updating WBS after scope changes;
- treating WBS as documentation only, not as a planning tool.

## Best Practices

Good practices:

- start with deliverables;
- decompose work into manageable parts;
- involve the team;
- keep tasks measurable;
- document assumptions;
- review WBS with stakeholders;
- connect WBS to estimates and schedule;
- update WBS when scope changes.

## Key Idea

WBS helps teams estimate and manage projects by breaking large work into smaller, clearer components.

Главная мысль:

> If you cannot break the work down, you probably do not understand it well enough to estimate it.

## Questions

1. What is WBS?
2. What is the difference between Functional WBS and Activity WBS?
3. How does WBS help with estimation?
4. What is the critical path?
5. What is the difference between Finish-to-Start and Finish-to-Finish?

## What To Review Later

- Work Breakdown Structure
- Critical Path Method
- Gantt Chart
- Milestones
- Task Dependencies
- Project Estimation
