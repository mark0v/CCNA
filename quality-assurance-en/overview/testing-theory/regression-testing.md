# Regression Testing

## Summary

Regression Testing is a testing activity that verifies whether existing functionality continues to work after changes in the application or code.

Any change can accidentally break a part of the product that was already working. This can be a bug fix, new feature, enhancement, refactoring, dependency update, configuration change, or performance fix.

The main goal of regression testing is to find unexpected side effects and make sure a new change did not break previously tested behavior.

## Key Points

- Regression testing checks existing functionality after changes.
- It is important after bug fixes, new features, enhancements, and performance fixes.
- Regression helps find bugs accidentally introduced by new changes.
- Regression testing is often automated because the same checks are repeated many times.
- Regression test cases should be prioritized based on risk and changed areas.
- Regression does not replace confirmation testing.
- Confirmation testing verifies that a specific defect was fixed.
- Regression testing verifies that the fix did not break something else.

## Notes

### What Is Regression Testing?

Regression testing is performed when changes are made to an application.

Examples:

- developer fixed a bug;
- added a new feature;
- changed existing functionality;
- improved performance;
- updated library;
- changed database query;
- refactored code;
- changed UI flow;
- modified API contract.

After that, QA checks:

> Does existing functionality still work as expected?

Regression testing is especially important in products with continuous modifications and enhancements.

### Why Regression Testing Matters

Software systems are interconnected.

A fix in one part of code can:

- break another module;
- change shared function behavior;
- affect database data;
- change API response;
- damage UI flow;
- reopen an old defect;
- create a new defect in related functionality.

These problems are called `unexpected side effects`.

Regression testing helps catch them before release.

### Confirmation Testing vs Regression Testing

Confirmation testing and regression testing often happen together, but they are different.

| Confirmation Testing | Regression Testing |
| --- | --- |
| Verifies that a specific defect was fixed. | Verifies that the fix/change did not break existing functionality. |
| Focuses on one issue. | Focuses on related and existing behavior. |
| Usually performed after a bug fix. | Performed after any changes. |
| Answers: "Is the bug fixed?" | Answers: "Did anything else break?" |

### Example

Imagine a school management application that stores student details.

The application has buttons:

- Add;
- Save;
- Delete;
- Refresh.

All buttons work correctly.

Then the team adds a new button:

- Update.

QA verifies the `Update` button and confirms that it works.

But that is not enough. QA also needs to make sure the new button did not affect existing functionality.

Regression testing verifies:

- Add still works;
- Save still works;
- Delete still works;
- Refresh still works;
- data updates correctly;
- no old bugs returned;
- student details remain consistent.

## Types of Regression Testing Techniques

### 1. Corrective Regression Testing

Corrective Regression Testing is used when specifications have not changed.

Existing test cases can be reused.

### 2. Progressive Regression Testing

Progressive Regression Testing is used when specifications changed.

New test cases need to be designed or existing test cases need to be updated.

### 3. Retest-All Strategy

Retest-All Strategy means rerunning all tests.

It gives maximum coverage, but it is expensive and time-consuming.

### 4. Selective Regression Testing

Selective Strategy uses a subset of existing test cases.

QA selects tests based on:

- changed module;
- impacted functionality;
- dependencies;
- risk;
- defect history;
- business criticality.

Selective regression is common in real projects.

## When To Use Regression Testing

Regression testing is used when:

- new feature is added;
- enhancement is implemented;
- bug is fixed;
- performance issue is fixed;
- code is refactored;
- dependency/library is updated;
- configuration is changed;
- database schema is changed;
- environment is changed;
- integration is modified.

Rule of thumb:

> If something changed, think about regression risk.

## Test Case Prioritization

Regression test cases should be prioritized.

High priority:

- changed functionality;
- adjacent impacted modules;
- critical business flows;
- high defect history areas;
- payment/login/security flows;
- customer-visible features;
- frequently used functionality.

Medium priority:

- related but less critical flows;
- secondary user journeys;
- important edge cases.

Low priority:

- rarely used features;
- cosmetic checks;
- stable low-risk areas.

## Automation in Regression Testing

Regression testing is often automated because the same tests are repeated many times.

Good automation candidates:

- stable functionality;
- repetitive checks;
- critical paths;
- smoke tests;
- high-value regression scenarios;
- API checks;
- data validation;
- cross-browser flows.

Automation helps:

- reduce manual effort;
- run tests more frequently;
- support CI/CD;
- catch defects earlier;
- improve confidence before release.

## Advantages

- Verifies that changes did not break existing functionality.
- Helps detect unexpected side effects.
- Helps ensure old bugs are not reproducible again.
- Improves product quality.
- Supports frequent releases.
- Works well with automation.
- Gives confidence after bug fixes and enhancements.

## Disadvantages

- Can be tedious and time-consuming if fully manual.
- Requires repeated execution of similar test cases.
- Needs maintenance when product changes.
- Can become too large without prioritization.
- Selective regression can miss issues if impact analysis is weak.
- Automation requires initial investment.

## Common Mistakes

- Running no regression after a "small" code change.
- Retesting only the fixed bug and ignoring related areas.
- Keeping outdated regression test cases.
- Automating unstable functionality too early.
- Running all tests every time without prioritization.
- Ignoring defect history during test selection.
- Not updating regression suite after new features.

## Commands / Terms

- `Regression Testing` - testing existing functionality after changes.
- `Confirmation Testing` - retesting a specific fixed defect.
- `Unexpected Side Effects` - new issues caused by a change.
- `Corrective Regression Testing` - reuse test cases when specifications did not change.
- `Progressive Regression Testing` - update/create tests when specifications changed.
- `Retest-All` - rerun all tests.
- `Selective Regression` - run selected tests based on impact/risk.
- `Impact Analysis` - identifying what areas may be affected by a change.
- `Regression Suite` - set of tests used for regression testing.

## Questions

1. What is regression testing?
2. Why is regression testing needed after a bug fix?
3. What is the difference between confirmation testing and regression testing?
4. When should regression testing be performed?
5. What is corrective regression testing?
6. What is progressive regression testing?
7. Why is retest-all strategy expensive?
8. What is selective regression testing?
9. Why is automation useful for regression testing?
10. How should QA prioritize regression test cases?

## What To Review Later

- Confirmation testing
- Smoke testing
- Sanity testing
- Regression suite
- Test automation
- Impact analysis
- Test case prioritization
- CI/CD testing
