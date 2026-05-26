# System Testing

## Summary

System Testing is a level of software testing where the behavior of the whole system or product is evaluated according to the defined project scope.

It is usually performed after unit testing and integration testing. At this stage, individual modules have already been developed, tested, and integrated. QA now evaluates the fully integrated application as one complete product.

The main goal of system testing is to make sure the total build satisfies business specifications, functional requirements, and non-functional requirements before it moves to acceptance testing.

## Key Points

- System testing verifies the whole system, not individual modules.
- It is usually the third testing level after unit and integration testing.
- The main technique is black box testing.
- Testing is performed in an environment close to production.
- Functional and non-functional requirements are verified.
- System testing is usually performed by an independent QA team.
- After fixes, regression testing is performed to make sure new changes did not break existing functionality.

## Notes

### What Is System Testing?

System testing evaluates the fully integrated software product as a single entity.

If unit testing asks "does this individual component work?" and integration testing asks "do these components work together?", system testing asks:

> Does the complete product work as a system according to requirements?

At this level, QA verifies not only individual functions but also complete user journeys, business processes, system behavior, error handling, compatibility, performance, security, and usability.

### Place in Testing Hierarchy

Typical testing levels:

1. Unit Testing
2. Integration Testing
3. System Testing
4. Acceptance Testing

System testing happens after integration testing and before acceptance testing.

It is an important transition point: the product is already assembled as one complete system but has not yet been handed to customer/users for final acceptance.

### Key Characteristics

#### Independent Testing

System testing is often performed by an independent QA team or specialist testers, not by the developers who wrote the code.

This helps provide a more objective evaluation of the product.

#### Black Box Technique

System testing usually uses a black box approach.

QA does not need to know the internal code structure. The focus is on:

- inputs;
- outputs;
- user behavior;
- business rules;
- requirements;
- external system behavior.

#### Realistic Environment

The test environment should be as close to production as possible.

This matters because system-level defects may appear only under real configuration, data, integrations, permissions, load, or infrastructure conditions.

### Scope of System Testing

System testing is comprehensive by nature. It can include many kinds of checks.

#### Functional Requirements

QA verifies that core features and user journeys work according to requirements.

Examples:

- user can register and log in;
- customer can place an order;
- admin can manage products;
- system calculates totals correctly;
- notifications are sent;
- reports are generated.

#### Non-Functional Requirements

System testing also covers quality attributes.

Examples:

- performance;
- security;
- usability;
- compatibility;
- load behavior;
- stress behavior;
- reliability;
- recovery;
- accessibility.

#### System Interactions

QA verifies how the application interacts with the environment and resources.

Examples:

- operating system;
- browser;
- database;
- file system;
- hardware;
- network;
- external services;
- permissions;
- logs and monitoring.

### System Testing Process

#### 1. Test Planning

The team creates a formal test plan.

It describes:

- scope;
- test objectives;
- test strategy;
- required environment;
- risks;
- test cases;
- use cases;
- resources;
- schedule;
- entry and exit criteria.

#### 2. Test Data Preparation

QA prepares realistic test data.

Good test data should cover:

- normal usage;
- boundary values;
- negative scenarios;
- edge cases;
- different user roles;
- valid and invalid data;
- production-like datasets where possible.

#### 3. Test Execution

Test cases are executed manually or through automation.

QA records:

- passed tests;
- failed tests;
- blocked tests;
- skipped tests;
- actual results;
- defects;
- environment details.

#### 4. Reporting and Debugging

If the actual result differs from the expected result, QA logs a defect.

Developers fix bugs, then QA performs:

- retesting;
- regression testing;
- status update;
- defect closure if the fix is valid.

#### 5. Recycling / Re-testing Cycle

The testing cycle repeats until the system reaches the required quality standards.

Usually the team continues until:

- critical defects are fixed;
- high priority defects are resolved or accepted;
- regression passed;
- exit criteria are met;
- stakeholders agree on release readiness.

### System Testing vs Integration Testing

| Integration Testing | System Testing |
| --- | --- |
| Verifies interaction between modules/components. | Verifies the whole integrated product. |
| Focuses on interfaces, APIs, and data flow between parts. | Focuses on complete requirements and end-to-end behavior. |
| Performed after unit testing. | Performed after integration testing. |
| May use stubs/drivers. | Usually tests the full real system. |
| Finds defects at component boundaries. | Finds defects in product behavior as a whole. |

### Common System Testing Types

System testing can include:

- functional testing;
- regression testing;
- usability testing;
- performance testing;
- load testing;
- stress testing;
- security testing;
- compatibility testing;
- recovery testing;
- installation testing;
- configuration testing;
- accessibility testing.

The exact set depends on project scope, risks, and requirements.

## Commands / Terms

- `System Testing` - testing the complete integrated system against requirements.
- `Black Box Testing` - testing without knowing internal code structure.
- `Functional Requirements` - what the system should do.
- `Non-Functional Requirements` - how the system should behave.
- `Production-like Environment` - test environment close to real production.
- `Retesting` - checking a fixed defect again.
- `Regression Testing` - checking that changes did not break existing functionality.
- `Acceptance Testing` - validation by customer/users before final acceptance.
- `Exit Criteria` - conditions required to complete testing.

## Questions

1. What is system testing?
2. When is system testing performed?
3. Why is system testing usually black box testing?
4. Who usually performs system testing?
5. What is the difference between system testing and integration testing?
6. What functional areas can system testing cover?
7. What non-functional areas can system testing cover?
8. Why should system testing use production-like environment?
9. What happens after defects are fixed?
10. Why is regression testing important during system testing?

## What To Review Later

- Testing levels
- Unit vs integration vs system testing
- Acceptance testing
- Functional testing
- Non-functional testing
- Regression testing
- Test planning
- Test environment setup
