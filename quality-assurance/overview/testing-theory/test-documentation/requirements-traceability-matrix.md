# Requirements Traceability Matrix

## Summary

A Requirements Traceability Matrix, or RTM, is a document that links requirements to related test cases, test results, defects, and deliverables.

It helps the team understand:

- which requirements are covered by tests;
- which requirements are not covered;
- which test cases verify each requirement;
- which defects are connected to each requirement;
- what needs to be retested when requirements change;
- whether testing is aligned with business goals.

RTM is especially useful when requirements coverage, compliance, audit readiness, or release confidence matters.

## What Is Traceability?

Traceability means the ability to follow a relationship between project artifacts.

In QA, traceability often connects:

- requirements;
- design documents;
- user stories;
- test cases;
- test runs;
- defects;
- change requests;
- release notes.

The purpose is to understand how one artifact affects another.

Example:

If a requirement changes, traceability helps identify which test cases, defects, and business flows may also need updates.

## What Is A Traceability Matrix?

A traceability matrix is a structured document that shows relationships between requirements and other project artifacts.

For testing, it usually shows whether each requirement has corresponding test coverage.

It helps answer:

- did we create tests for this requirement;
- did we execute those tests;
- did they pass or fail;
- were defects found;
- is the requirement ready for release.

## What Is A Requirements Traceability Matrix?

A Requirements Traceability Matrix is a specific type of traceability matrix focused on project or product requirements.

It tracks requirements from definition through testing and delivery.

In software testing, RTM commonly links:

- requirement ID;
- requirement description;
- test case ID;
- test execution status;
- defect ID;
- requirement status.

The main goal is to make sure every important requirement is tested and accounted for.

## Why RTM Is Important

RTM helps ensure that the project does what it set out to do.

It supports:

- requirements coverage;
- test planning;
- test design;
- change impact analysis;
- defect analysis;
- audit readiness;
- compliance evidence;
- release decisions.

RTM also helps identify process problems.

For example:

- requirements with no tests;
- tests with no linked requirements;
- requirements with many defects;
- requirements that changed but were not retested;
- missing UAT coverage.

## Benefits Of RTM

## Better Requirements Coverage

RTM shows whether every requirement has at least one related test case.

This reduces the chance that a requirement is forgotten during testing.

## Clearer Test Scope

RTM helps the team understand what is actually being tested.

If a test case does not connect to any requirement, the team can review whether it is still useful or redundant.

## Change Impact Analysis

When a requirement changes, RTM helps identify affected tests and defects.

This is useful for regression testing because the team can quickly decide what needs to be updated or rerun.

## Better Defect Analysis

By linking defects to requirements, the team can see which requirements produce the most issues.

This can reveal:

- unclear requirements;
- complex business logic;
- unstable features;
- weak design;
- insufficient development review.

## Audit And Compliance Support

In regulated domains, teams often need to prove that requirements were implemented and tested.

RTM helps provide evidence for:

- medical systems;
- finance systems;
- safety-critical systems;
- government projects;
- compliance-heavy products.

## Release Confidence

Before release, RTM helps stakeholders see:

- what is covered;
- what is not covered;
- which tests passed;
- which defects remain;
- what risk is still present.

This supports smarter release decisions.

## What To Include In RTM

A simple RTM can include:

| Column | Meaning |
| --- | --- |
| Requirement ID | Unique identifier of the requirement |
| Requirement Description | What the requirement says |
| Priority | Business or risk priority |
| Test Case ID | Test cases linked to the requirement |
| Test Scenario | High-level scenario or flow |
| Test Status | Passed, Failed, Blocked, Not Run |
| Defect ID | Related bugs |
| Defect Status | Open, Fixed, Retested, Closed |
| UAT Status | User acceptance status |
| Comments | Notes, assumptions, or deviations |

The exact columns depend on the project.

## RTM Example

| Requirement ID | Requirement | Priority | Test Cases | Test Status | Defects | Status |
| --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | User can log in with valid credentials | High | TC-001, TC-002 | Passed | - | Covered |
| REQ-002 | User sees error for invalid password | High | TC-003 | Failed | BUG-014 | Covered with defect |
| REQ-003 | User can reset password by email | Medium | TC-010, TC-011 | Not Run | - | Pending |
| REQ-004 | Account locks after 5 failed attempts | High | - | Not Run | - | Not Covered |

This table immediately shows that `REQ-004` has no test coverage and needs attention.

## Types Of Traceability

## Forward Traceability

Forward traceability maps requirements to test cases.

It answers:

- do all requirements have tests;
- what test cases verify this requirement.

## Backward Traceability

Backward traceability maps test cases back to requirements.

It answers:

- why does this test case exist;
- which requirement does it verify.

## Bidirectional Traceability

Bidirectional traceability combines both directions.

It allows the team to move from requirement to tests and from tests back to requirement.

This is the strongest and most useful form of traceability.

## How To Create An RTM

## 1. Gather Requirements

Start with the approved list of requirements.

Sources:

- business requirements;
- product requirements;
- system specifications;
- user stories;
- acceptance criteria;
- compliance requirements.

Each requirement should have a unique ID.

## 2. Break Requirements Into Testable Items

Requirements should be clear enough to test.

If a requirement is too broad, split it into smaller testable parts.

Bad example:

```text
The system should be user-friendly.
```

Better example:

```text
The login page should show validation messages for empty email and password fields.
```

## 3. Create Or Link Test Cases

For each requirement, link one or more test cases.

Some requirements may need many test cases:

- positive scenarios;
- negative scenarios;
- boundary checks;
- role-based checks;
- integration checks;
- regression checks.

## 4. Add Execution Status

Update RTM when tests are executed.

Common statuses:

- Not Run;
- Passed;
- Failed;
- Blocked;
- Skipped.

## 5. Link Defects

If a test fails, link the defect to the requirement.

This helps understand which requirements are affected by open bugs.

## 6. Review Gaps

Analyze RTM regularly.

Look for:

- requirements without tests;
- tests without requirements;
- failed critical requirements;
- blocked requirements;
- requirements with many defects;
- outdated links after changes.

## 7. Keep RTM Updated

RTM should be created early and maintained during the project.

It should be updated when:

- requirements change;
- test cases are added;
- test cases are removed;
- tests are executed;
- defects are found;
- defects are fixed;
- scope changes.

Outdated RTM can become misleading.

## RTM And Test Coverage

RTM is one of the best tools for requirements coverage.

It supports the formula:

```text
Requirements Coverage =
(Requirements covered by test cases / Total requirements) x 100%
```

Example:

```text
Covered requirements: 45
Total requirements: 50

Requirements Coverage = 90%
```

This does not prove the product is bug-free, but it shows how much of the requirement set has test coverage.

## RTM And Defect Management

RTM can show which requirements are unstable.

Example:

| Requirement | Number Of Defects |
| --- | --- |
| Login | 2 |
| Checkout | 12 |
| Reports | 7 |

If `Checkout` has many defects, it may need deeper testing, better requirements review, or architecture discussion.

## RTM And UAT

RTM can also track User Acceptance Testing.

Useful UAT columns:

- business owner;
- UAT test case;
- UAT status;
- acceptance decision;
- comments.

This helps confirm that business-critical requirements were validated by the right stakeholders.

## Common Mistakes

Common RTM mistakes:

- creating RTM too late;
- not assigning unique requirement IDs;
- linking tests vaguely;
- not updating test execution status;
- not linking defects;
- keeping outdated requirements;
- adding too many unnecessary columns;
- treating RTM as paperwork instead of a decision tool.

RTM should be simple enough to maintain and useful enough to guide testing.

## Key Idea

A Requirements Traceability Matrix connects requirements with test cases, results, and defects.

It helps the team prove coverage, analyze gaps, and make better release decisions.

Главная мысль:

> RTM shows whether testing is connected to what the product promised to deliver.

## Questions

1. What is a Requirements Traceability Matrix?
2. Why is RTM useful for QA?
3. What is the difference between forward and backward traceability?
4. How does RTM support requirements coverage?
5. What should be included in an RTM?

## What To Review Later

- Requirements Coverage
- Test Coverage
- Test Cases
- Defect Management
- UAT
- Change Impact Analysis
