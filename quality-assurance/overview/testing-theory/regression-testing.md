# Regression Testing

## Summary

Regression Testing - это testing activity, которая проверяет, что existing functionality продолжает работать после changes в application или code.

Любое изменение может случайно сломать уже работающую часть продукта. Это может быть bug fix, new feature, enhancement, refactoring, dependency update, configuration change или performance fix.

Главная цель regression testing - найти unexpected side effects и убедиться, что новый change не нарушил ранее протестированное поведение.

## Key Points

- Regression testing проверяет existing functionality после changes.
- Оно важно после bug fixes, new features, enhancements и performance fixes.
- Regression помогает найти bugs, случайно introduced new changes.
- Regression testing часто автоматизируют, потому что одни и те же checks повторяются много раз.
- Test cases для regression нужно prioritise based on risk and changed areas.
- Regression не заменяет confirmation testing.
- Confirmation testing проверяет, что конкретный defect fixed.
- Regression testing проверяет, что fix не сломал что-то еще.

## Notes

### What Is Regression Testing?

Regression testing выполняется, когда в application внесены changes.

Например:

- developer fixed bug;
- added new feature;
- changed existing functionality;
- improved performance;
- updated library;
- changed database query;
- refactored code;
- changed UI flow;
- modified API contract.

После этого QA должен проверить:

> Existing functionality still works as expected?

Regression testing особенно важно в products, где постоянно идут modifications и enhancements.

### Why Regression Testing Matters

Software systems связаны между собой.

Fix в одной части code может:

- сломать другой module;
- изменить shared function behavior;
- повлиять на database data;
- нарушить API response;
- повредить UI flow;
- открыть old defect again;
- создать new defect in related functionality.

Такие проблемы называют `unexpected side effects`.

Regression testing помогает поймать их до release.

### Confirmation Testing vs Regression Testing

Confirmation testing и regression testing часто идут рядом, но это разные вещи.

| Confirmation Testing | Regression Testing |
| --- | --- |
| Проверяет, что конкретный defect fixed. | Проверяет, что fix/change не сломал existing functionality. |
| Focus на one issue. | Focus на related and existing behavior. |
| Обычно выполняется после bug fix. | Выполняется после любых changes. |
| Ответ: "Bug fixed?" | Ответ: "Nothing else broke?" |

Example:

Если bug был в `Update` button, confirmation testing проверяет, что `Update` теперь работает.

Regression testing проверяет, что после добавления/fix `Update` button не сломались `Add`, `Save`, `Delete`, `Refresh` и related flows.

### Example

Представим school management application, которая хранит details of students.

В application есть buttons:

- Add;
- Save;
- Delete;
- Refresh.

Все buttons работают correctly.

Потом команда добавляет новый button:

- Update.

QA проверяет `Update` button и подтверждает, что он работает.

Но этого недостаточно. Нужно убедиться, что новый button не повлиял на existing functionality.

Regression testing проверит:

- Add still works;
- Save still works;
- Delete still works;
- Refresh still works;
- data updates correctly;
- no old bugs returned;
- student details remain consistent.

Этот процесс и называется regression testing.

## Types of Regression Testing Techniques

### 1. Corrective Regression Testing

Corrective Regression Testing используется, когда specifications не изменились.

В этом случае existing test cases can be reused.

Use when:

- requirements are stable;
- functionality did not change;
- fix is internal;
- previous test cases are still valid.

Example:

Developer optimizes code but expected behavior remains the same. QA can reuse existing regression suite.

### 2. Progressive Regression Testing

Progressive Regression Testing используется, когда specifications changed.

В этом случае нужно design new test cases или update existing test cases.

Use when:

- requirements changed;
- feature behavior changed;
- new flows were added;
- existing expected results changed.

Example:

Checkout logic now supports coupons and gift cards. Old test cases are not enough, so QA creates new ones.

### 3. Retest-All Strategy

Retest-All Strategy означает rerun all tests.

Это самый полный, но самый дорогой approach.

Advantages:

- maximum coverage;
- useful for critical systems;
- useful after large changes.

Disadvantages:

- very time-consuming;
- expensive;
- may execute unnecessary tests;
- usually impractical for small changes.

Use carefully.

### 4. Selective Regression Testing

Selective Strategy использует subset of existing test cases.

QA выбирает tests based on:

- changed module;
- impacted functionality;
- dependencies;
- risk;
- defect history;
- business criticality.

Advantages:

- reduces testing effort;
- faster feedback;
- more practical than retest-all.

Disadvantages:

- impact analysis can be difficult;
- dependencies may be missed;
- wrong selection can miss regression defects.

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

Good prioritization saves time and keeps regression practical.

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

But automation is not magic. Test cases still need maintenance.

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
