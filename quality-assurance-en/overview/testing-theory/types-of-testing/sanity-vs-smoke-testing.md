# Sanity Testing vs Smoke Testing

## Summary

Smoke Testing and Sanity Testing are quick checks that help a team avoid wasting time on deep testing of an unstable build.

Smoke Testing verifies whether a build is stable enough for further testing. It is performed after a new build and covers critical functionality across the whole application.

Sanity Testing verifies whether specific changes, bug fixes, or small enhancements work in a rational and expected way. It is performed on a relatively stable build and focuses on a narrow area.

In short:

- `Smoke Testing` = can this build be tested further?
- `Sanity Testing` = does this specific change work correctly?

## Key Points

- Smoke testing is broad and shallow.
- Sanity testing is narrow and deeper.
- Smoke testing is usually performed before sanity testing.
- Smoke testing can be performed by developers or testers.
- Sanity testing is usually performed by testers.
- Smoke testing is often automated and included in CI/CD pipelines.
- Sanity testing can be manual, exploratory, or automated.
- Smoke testing belongs to build verification.
- Sanity testing is often treated as a subset of regression testing.

## Notes

### What Is a Software Build?

A software build is the result of assembling source code, dependencies, configuration, and resources into an executable or deployable version of a product.

In a small program, a build may be simple: compile one file and run it.

In a real software project, a build may include:

- hundreds or thousands of source files;
- multiple services;
- frontend and backend;
- database migrations;
- third-party dependencies;
- configuration files;
- CI/CD pipeline;
- automated tests;
- deployment artifacts.

After a new build, QA first needs to know whether it is usable for testing or broken at a basic level.

### What Is Smoke Testing?

Smoke Testing is a quick verification after a software build that checks whether the most critical functionality works.

The goal is to reject a broken build quickly so the QA team does not spend hours or days on detailed functional or regression testing.

Smoke testing is not exhaustive. It checks basic stability.

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

If a smoke test fails, testing usually stops and the build returns to the development team.

### What Is Sanity Testing?

Sanity Testing is performed after minor code changes, bug fixes, or small functionality updates.

The goal is to verify that the specific change works roughly as expected and does not look logically broken.

Sanity testing does not check the whole system. It focuses on the changed area and nearby functionality.

Example:

If a developer fixed a bug in the shopping cart, sanity testing verifies:

- item can be added to cart;
- quantity can be updated;
- item can be removed;
- totals are recalculated correctly;
- related checkout flow still starts.

If sanity testing fails, deeper regression for that area may not make sense yet.

### Origin of the Terms

The term `smoke testing` comes from hardware and electronics.

When engineers powered up a circuit board for the first time, they checked whether smoke appeared. If it did, there was a fundamental flaw and further testing was pointless.

In software, the term means initial build verification.

The term `sanity testing` is connected to checking rationality. The team asks:

> Does this change make sense?

If a calculator returns `2 + 2 = 5`, there is no reason to test advanced functions.

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

### Sanity Test

After smoke passes, QA focuses on shopping cart:

- add item to cart;
- update quantity;
- remove item;
- verify price calculation;
- check discount or shipping calculation if affected.

### Regression Test

If smoke and sanity pass, the team can proceed to wider regression testing.

## When To Use Smoke Testing

Use smoke testing when:

- new build is deployed to testing environment;
- CI/CD pipeline creates a fresh build;
- QA needs to decide whether detailed testing can begin;
- critical functionalities need quick verification;
- application stability is uncertain;
- build was recently compiled, deployed, or migrated.

## When To Use Sanity Testing

Use sanity testing when:

- minor code change was implemented;
- bug fix was delivered;
- small feature enhancement was added;
- build is already relatively stable;
- QA needs to verify changed functionality quickly;
- full regression is too expensive before targeted validation.

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
