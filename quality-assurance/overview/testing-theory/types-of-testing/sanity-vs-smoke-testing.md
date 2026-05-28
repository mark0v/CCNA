# Sanity Testing vs Smoke Testing

## Summary

Smoke Testing и Sanity Testing - это быстрые проверки, которые помогают команде не тратить время на глубокое тестирование unstable build.

Smoke Testing проверяет, достаточно ли build стабилен для дальнейшего testing. Он выполняется после новой сборки и покрывает critical functionality всего application.

Sanity Testing проверяет, работают ли конкретные изменения, bug fixes или small enhancements рационально и ожидаемо. Он выполняется на relatively stable build и фокусируется на narrow area.

Проще:

- `Smoke Testing` = можно ли вообще тестировать этот build дальше?
- `Sanity Testing` = конкретное изменение работает нормально?

## Key Points

- Smoke testing broad and shallow: широкий scope, небольшая глубина.
- Sanity testing narrow and deep: узкий scope, более глубокая targeted проверка.
- Smoke testing обычно выполняется перед sanity testing.
- Smoke testing может выполняться developers или testers.
- Sanity testing обычно выполняется testers.
- Smoke testing часто автоматизируют и добавляют в CI/CD pipeline.
- Sanity testing может быть manual, exploratory или automated.
- Smoke testing относится к build verification.
- Sanity testing часто рассматривают как subset of regression testing.

## Notes

### What Is a Software Build?

Software build - это результат сборки source code, dependencies, configuration и resources в executable или deployable version продукта.

В маленькой программе build может быть простым: compile one file and run.

В реальном software project могут быть:

- сотни или тысячи source files;
- multiple services;
- frontend and backend;
- database migrations;
- third-party dependencies;
- configuration files;
- CI/CD pipeline;
- automated tests;
- deployment artifacts.

Поэтому после новой сборки QA сначала должен понять: build вообще пригоден для testing или он broken at the basic level?

### What Is Smoke Testing?

Smoke Testing - это quick verification после software build, которая проверяет, работают ли самые critical functionalities.

Цель smoke testing - быстро reject broken build, чтобы QA team не тратила часы или дни на detailed functional или regression testing.

Smoke testing не является exhaustive testing. Он проверяет basic stability.

Typical smoke checks:

- application launches successfully;
- main page loads;
- login works;
- navigation works;
- critical API responds;
- database connection works;
- basic CRUD flow works;
- checkout starts;
- user can access key pages.

Если smoke test fails, testing обычно останавливается, build возвращается development team.

### What Is Sanity Testing?

Sanity Testing выполняется после minor code changes, bug fixes или small functionality updates.

Цель sanity testing - проверить, что конкретное изменение работает roughly as expected и не выглядит logically broken.

Sanity testing не проверяет весь system. Он фокусируется на changed area и nearby functionality.

Example:

Если developer fixed bug в shopping cart, sanity testing проверит:

- item can be added to cart;
- quantity can be updated;
- item can be removed;
- totals are recalculated correctly;
- related checkout flow still starts.

Если sanity test fails, нет смысла запускать deeper regression для этой области.

### Origin of the Terms

Термин `smoke testing` пришел из hardware/electronics.

Когда engineers впервые включали circuit board, они смотрели, не идет ли smoke. Если smoke появился, значит есть fundamental flaw и дальше testing бессмысленен.

В software этот термин стал означать initial build verification.

Термин `sanity testing` связан с проверкой rationality. Команда как бы спрашивает:

> Does this change make sense?

Если calculator после fix показывает `2 + 2 = 5`, нет смысла тестировать advanced functions.

## Smoke Testing vs Sanity Testing

| Aspect | Smoke Testing | Sanity Testing |
| --- | --- | --- |
| Primary Goal | Verify build stability. | Verify specific changes or fixes. |
| Scope | Broad, covers entire application basics. | Narrow, focused on specific modules. |
| Depth | Shallow. | Deeper but targeted. |
| Performed By | Developers or testers. | Usually testers. |
| Build State | New or potentially unstable build. | Relatively stable build. |
| Documentation | Often scripted and documented. | Often less formal or unscripted. |
| Testing Subset | Build verification / acceptance-style gate. | Regression testing subset. |
| Automation | Highly recommended. | Can be manual or automated. |
| Timing | Before detailed testing. | After smoke testing, when changes need focused validation. |

### Smoke vs Sanity vs Regression Testing

These three testing types work together.

#### Smoke Testing

Comes first.

It answers:

> Is this build stable enough to test?

#### Sanity Testing

Comes after smoke testing when specific changes need validation.

It answers:

> Does this fix/change work rationally?

#### Regression Testing

More comprehensive.

It answers:

> Did new changes break existing functionality?

Think of them as a funnel:

1. Smoke testing filters broken builds.
2. Sanity testing checks targeted changes.
3. Regression testing gives broader confidence.

## Real-World Scenario: E-Commerce Application

Imagine an e-commerce website receives a new build with a shopping cart bug fix.

### Smoke Test

QA first verifies basic build stability:

- website loads;
- user can log in;
- products display;
- search works;
- checkout page opens.

This may take 15-30 minutes or run automatically in CI/CD.

### Sanity Test

After smoke passes, QA focuses on shopping cart:

- add item to cart;
- update quantity;
- remove item;
- verify price calculation;
- check discount or shipping calculation if affected.

This targeted check may take 30-60 minutes depending on complexity.

### Regression Test

If smoke and sanity pass, team can proceed to wider regression testing:

- checkout;
- payment;
- order history;
- user profile;
- inventory updates;
- email notifications.

## When To Use Smoke Testing

Use smoke testing when:

- new build is deployed to testing environment;
- CI/CD pipeline creates a fresh build;
- QA needs to decide whether detailed testing can begin;
- critical functionalities need quick verification;
- application stability is uncertain;
- build was recently compiled, deployed or migrated.

Best candidates for smoke suite:

- login;
- app launch;
- main navigation;
- core API health;
- database connection;
- most critical business flow.

## When To Use Sanity Testing

Use sanity testing when:

- minor code change was implemented;
- bug fix was delivered;
- small feature enhancement was added;
- build is already relatively stable;
- QA needs to verify changed functionality quickly;
- full regression is too expensive before targeted validation.

Best candidates for sanity testing:

- fixed defect area;
- changed module;
- nearby impacted functionality;
- main happy path around the change;
- one or two important negative scenarios.

## Advantages

### Smoke Testing Advantages

- Quickly rejects broken builds.
- Saves QA time.
- Works well in CI/CD.
- Gives fast feedback to developers.
- Protects detailed testing from unstable builds.

### Sanity Testing Advantages

- Quickly validates specific changes.
- Helps confirm bug fixes.
- Reduces unnecessary regression effort.
- Supports focused exploratory checks.
- Helps catch obvious side effects near changed areas.

## Limitations

Smoke and sanity testing are useful, but limited.

They do not replace:

- full functional testing;
- regression testing;
- integration testing;
- system testing;
- exploratory testing;
- performance/security testing.

Possible limitations:

- limited coverage;
- hidden edge cases may be missed;
- integration issues may remain;
- false confidence if teams treat them as complete testing.

## Best Practices

### For Smoke Testing

- Automate smoke tests where possible.
- Run smoke tests on every build.
- Keep smoke suite small and focused.
- Include only critical functionality.
- Update smoke tests when critical features change.
- Fail fast if build is unstable.

### For Sanity Testing

- Review change documentation before testing.
- Focus on changed area and adjacent functionality.
- Use exploratory thinking.
- Keep scope controlled.
- Separate sanity testing from full regression.
- Document important findings even if testing is informal.

## Common Mistakes

- Confusing smoke testing and sanity testing.
- Skipping smoke testing to "save time".
- Making smoke suite too large.
- Treating sanity testing as full regression.
- Continuing deep testing after smoke failure.
- Testing only happy path for risky changes.
- Not updating smoke suite after product changes.

## Useful Tools

Common tools that can support smoke and sanity testing:

- Selenium WebDriver;
- Cypress;
- Playwright;
- TestNG;
- JUnit;
- Jenkins;
- GitHub Actions;
- Postman;
- REST Assured.

Tool choice depends on project stack, automation strategy and team skills.

## Commands / Terms

- `Smoke Testing` - quick build stability verification.
- `Sanity Testing` - targeted verification of specific changes or fixes.
- `Build` - compiled/deployed version of software ready for testing.
- `Regression Testing` - checking that changes did not break existing functionality.
- `CI/CD` - continuous integration and delivery/deployment pipeline.
- `Build Verification Test` - another common meaning of smoke testing.
- `Critical Functionality` - core behavior required for product use.
- `Happy Path` - normal successful user flow.

## Questions

1. What is smoke testing?
2. What is sanity testing?
3. What is the main difference between smoke and sanity testing?
4. Which one usually comes first?
5. Why should smoke testing be quick?
6. Why is sanity testing narrow in scope?
7. How are sanity testing and regression testing related?
8. Can smoke testing be automated?
9. When should QA stop testing a build?
10. What are common mistakes with smoke and sanity testing?

## What To Review Later

- Regression testing
- Build verification
- CI/CD testing
- Functional testing
- System testing
- Test automation basics
- Exploratory testing
- Impact analysis
