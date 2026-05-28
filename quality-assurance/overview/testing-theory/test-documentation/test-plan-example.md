# Test Plan Example

## Summary

A Test Plan is a detailed document that describes the test strategy, objectives, schedule, estimation, resources, environment, criteria, and deliverables required to test a software product.

It helps the team understand:

- what needs to be tested;
- what is out of scope;
- which testing types are needed;
- who will perform testing;
- when testing will happen;
- what risks exist;
- which artifacts must be produced.

According to ISTQB, a test plan describes the scope, approach, resources, and schedule of intended test activities.

## Why A Test Plan Is Important

A Test Plan is useful because it gives structure and visibility to testing.

It helps people outside the QA team understand the testing work:

- developers;
- business managers;
- customers;
- product owners;
- stakeholders.

It also documents important testing decisions:

- test scope;
- test strategy;
- test estimation;
- required resources;
- schedule;
- risks;
- deliverables.

The Test Plan works like a rulebook for the testing project. It gives the team a shared direction and helps management review and reuse testing decisions later.

## Types Of Test Plans

There are three common types of test plans.

### Master Test Plan

A Master Test Plan is a high-level document that describes the overall testing strategy, scope, resources, schedule, and responsibilities for the whole project.

It works as the main testing roadmap.

### Level-Specific Test Plan

A Level-Specific Test Plan focuses on one testing level.

Examples:

- unit testing plan;
- integration testing plan;
- system testing plan;
- acceptance testing plan.

Each plan defines the approach, environment, data, responsibilities, and deliverables for that specific level.

### Type-Specific Test Plan

A Type-Specific Test Plan focuses on a specific type of testing.

Examples:

- performance test plan;
- security test plan;
- usability test plan;
- automation test plan;
- compatibility test plan.

This type of plan usually defines specific tools, techniques, environments, and success criteria.

## How To Write A Test Plan

A practical test plan can be created in several steps.

## Step 1: Analyze The Product

Before testing a product, QA must understand it.

Questions to ask:

- Who will use the product?
- What is the product used for?
- How should it work?
- What problem does it solve?
- What hardware or software does it depend on?
- Which integrations are involved?
- Which features are most important for users?

Useful sources:

- requirements;
- user stories;
- product documentation;
- designs;
- architecture diagrams;
- API documentation;
- previous defect reports;
- stakeholder interviews.

If anything is unclear, QA should ask the customer, developer, designer, product owner, or business analyst.

## Step 2: Develop The Test Strategy

Test Strategy is a critical part of test planning.

It defines:

- testing objectives;
- testing approach;
- test levels;
- test types;
- tools;
- automation approach;
- defect process;
- risks;
- approximate effort and cost.

The strategy answers the question:

> How will we test this product effectively?

## Step 2.1: Define Scope Of Testing

Before testing starts, the team must understand what is in scope and what is out of scope.

In scope means the components, features, or integrations that will be tested.

Out of scope means the areas that will not be tested in this test cycle.

Example:

In scope:

- functional testing;
- login;
- user profile;
- payment flow;
- API testing.

Out of scope:

- database performance;
- hardware testing;
- unsupported browsers;
- external systems not controlled by the team.

Clear scope helps stakeholders understand what QA is responsible for and what is excluded.

## How To Determine Scope

To define scope, consider:

- customer requirements;
- project budget;
- product specification;
- timeline;
- business risks;
- skills of the test team;
- available environments;
- required tools.

If a customer asks to add extra testing work, such as API testing or performance testing, the team should explain the impact on budget, schedule, and resources.

## Step 2.2: Identify Testing Types

A testing type is a standard testing procedure used to find a specific category of defects.

Examples:

- functional testing;
- regression testing;
- smoke testing;
- sanity testing;
- API testing;
- performance testing;
- security testing;
- usability testing;
- compatibility testing.

The team cannot always perform every possible testing type.

The Test Manager should prioritize testing types based on:

- product risks;
- business value;
- budget;
- timeline;
- team skills;
- user impact.

## Step 2.3: Document Risks And Issues

A risk is a future uncertain event that may affect testing or product quality.

When the risk actually happens, it becomes an issue.

Examples:

| Risk | Mitigation |
| --- | --- |
| Team members lack required testing skills | Plan training or assign experienced support |
| Project schedule is too tight | Prioritize critical test activities |
| Test Manager lacks management experience | Provide mentoring or leadership support |
| Poor cooperation between teams | Improve communication and hold regular syncs |
| Budget estimate is wrong | Define scope early and track progress constantly |

Risk planning helps the team react before problems damage the release.

## Step 2.4: Create Test Logistics

Test logistics answers two practical questions:

- Who will test?
- When will testing happen?

### Who Will Test?

The Test Manager may not always know exact names at the beginning, but the required roles should be clear.

Example roles:

- QA Lead;
- Manual QA Engineer;
- Automation QA Engineer;
- Performance Tester;
- Security Tester;
- Test Administrator.

When assigning people, consider:

- technical skills;
- domain knowledge;
- availability;
- budget;
- communication skills;
- attention to detail.

### When Will Testing Happen?

Testing activities should align with development activities.

Testing usually starts when:

- requirements are ready;
- build is deployed;
- test environment is available;
- test data is prepared;
- test cases or checklists are ready;
- smoke testing passes.

## Step 3: Define Test Objectives

The test objective is the overall goal of test execution.

Common objectives:

- find as many defects as possible before release;
- verify that functionality works according to requirements;
- confirm that UI meets user expectations;
- validate usability;
- verify integration with external systems;
- check that critical business flows work in a real-like environment.

To define objectives:

1. List product features that may need testing.
2. Define the target or goal for each feature.
3. Prioritize objectives based on risk and business value.

Example objectives for a banking website:

- verify account functionality;
- verify deposit and withdrawal flows;
- check external interface behavior;
- validate usability of key user flows;
- confirm that critical transactions work without errors.

## Step 4: Define Test Criteria

Test criteria are rules used to decide when testing should continue, stop, or finish.

There are two important types:

- suspension criteria;
- exit criteria.

### Suspension Criteria

Suspension criteria define when active testing should be stopped.

Example:

If 40% of test cases fail because the build is unstable, testing may be suspended until the development team fixes the failed areas.

Suspension criteria protect the team from wasting time on a build that is not ready for deeper testing.

### Exit Criteria

Exit criteria define when testing can be considered complete.

Examples:

- 100% of planned critical test cases are executed;
- all blocker and critical defects are fixed and retested;
- regression testing is completed;
- pass rate meets the agreed target;
- test summary report is prepared;
- stakeholders approve release readiness.

Useful metrics:

| Metric | Meaning |
| --- | --- |
| Run rate | Executed test cases / total planned test cases |
| Pass rate | Passed test cases / executed test cases |

Example:

If there are 120 planned test cases and 100 were executed:

```text
Run rate = 100 / 120 = 83%
```

If 80 of those 100 executed test cases passed:

```text
Pass rate = 80 / 100 = 80%
```

If the required run rate is 100%, then exit criteria are not met.

## Step 5: Resource Planning

Resource planning defines what is needed to complete testing.

Resources can include:

- people;
- tools;
- environments;
- devices;
- servers;
- test data;
- budget;
- time.

## Human Resources

Typical testing roles:

| Role | Responsibilities |
| --- | --- |
| Test Manager | Manage the testing project, define direction, allocate resources |
| Tester | Design and execute tests, log defects, report results |
| Developer in Test | Build test scripts, test suites, and automation support |
| Test Administrator | Prepare and maintain test environments and assets |
| SQA Member | Verify that testing process follows quality requirements |

Choosing the wrong person for a task can delay testing or reduce quality.

## System Resources

For a web application, system resources may include:

| Resource | Description |
| --- | --- |
| Server | Hosts the application under test |
| Database server | Stores application data |
| Test tool | Supports automation, execution, or reporting |
| Network | Simulates real business and user environments |
| Computer or device | Represents the client-side user environment |

The goal is to make the test setup realistic enough to produce useful results.

## Step 6: Plan Test Environment

A test environment is the software and hardware setup where the QA team executes test cases.

It may include:

- application server;
- database;
- browser;
- mobile devices;
- operating systems;
- network configuration;
- test accounts;
- test data;
- third-party integrations;
- monitoring tools.

To plan the environment, QA should cooperate with developers, DevOps, and system administrators.

Questions to ask:

- What are the hardware and software requirements?
- How many users can the system handle?
- Which browsers or devices must be supported?
- Are there special configuration requirements?
- Which integrations are required?
- How will data be backed up and restored?

## Step 7: Schedule And Estimation

Schedule and estimation help the Test Manager monitor progress and control cost.

Inputs for scheduling:

- project deadline;
- employee availability;
- effort estimates;
- dependencies;
- risks;
- test environment readiness;
- bug fixing time;
- regression cycles.

Example testing tasks:

| Task | Role | Estimated Effort |
| --- | --- | --- |
| Create test specification | Test Designer | 170 man-hours |
| Perform test execution | Tester, Test Administrator | 80 man-hours |
| Prepare test report | Tester | 10 man-hours |
| Test delivery | QA Team | 20 man-hours |
| Total | Team | 280 man-hours |

A good schedule should include time for retesting and regression, not only first test execution.

## Step 8: Define Test Deliverables

Test deliverables are documents, tools, reports, and other artifacts created during testing.

### Before Testing

Examples:

- test plan;
- test cases;
- test design specification;
- test data plan.

### During Testing

Examples:

- test scripts;
- simulators;
- test data;
- traceability matrix;
- execution logs;
- defect reports.

### After Testing

Examples:

- test results;
- test summary report;
- defect report;
- release notes;
- installation or test procedure guidelines.

Deliverables provide evidence of testing work and support release decisions.

## Common Challenges In Test Planning

### Unclear Requirements

Problem: ambiguous or changing requirements lead to incomplete coverage.

Solution: hold requirement walkthroughs and maintain a requirement traceability matrix.

### Limited Resources

Problem: not enough tools, time, or skilled testers.

Solution: prioritize critical test cases and use automation for repetitive checks where possible.

### Unrealistic Deadlines

Problem: tight schedules reduce time for proper test design and execution.

Solution: estimate carefully and communicate risks early.

### Poor Communication

Problem: misalignment between QA, developers, and stakeholders causes delays and rework.

Solution: use regular sync meetings and shared dashboards.

### Inadequate Risk Management

Problem: ignored risks can break the schedule or reduce test quality.

Solution: identify risks early, maintain a risk log, and define mitigation actions.

## Key Idea

A Test Plan is a practical blueprint for testing.

It connects business expectations, QA activities, resources, schedule, risks, and deliverables into one shared document.

Главная мысль:

> A good test plan helps the team test with purpose, not panic.

## Questions

1. What is a Test Plan?
2. Why is a Test Plan important?
3. What are the main types of test plans?
4. What is the difference between suspension criteria and exit criteria?
5. Which test deliverables can be created before, during, and after testing?

## What To Review Later

- Test Strategy
- Test Scope
- Test Objectives
- Test Criteria
- Resource Planning
- Test Environment
- Test Deliverables
