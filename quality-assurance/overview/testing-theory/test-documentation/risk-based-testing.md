# Risk Based Testing

## Summary

Risk Based Testing, or RBT, is a testing approach where test planning, prioritization, design, and execution are based on product risks.

Instead of testing everything with the same intensity, the QA team focuses first on features and areas that are:

- more critical for the business;
- more likely to fail;
- more complex;
- used more often;
- connected to security, money, data, or customer trust;
- historically defect-prone.

The goal is to spend limited testing time where it reduces the most risk.

## What Is Risk?

Risk is an uncertain event that can affect project or product success.

In software testing, risk is often connected to:

- business impact;
- technical complexity;
- product quality;
- schedule;
- cost;
- security;
- reliability;
- user satisfaction.

Risks can be positive or negative.

Positive risks are opportunities. They can help the business, for example by opening a new market or improving a process.

Negative risks are threats. They can damage the project, product, users, or company reputation.

In QA, we mostly focus on negative risks and ways to reduce them through testing.

## Why Risk Based Testing Matters

Testing time is always limited.

Teams usually do not have enough time, people, environments, or budget to test every possible scenario.

Risk Based Testing helps answer:

- What should we test first?
- What should we test deeper?
- What can be tested lightly?
- Which areas are too risky to ignore?
- Which risks remain before release?
- Is the product safe enough to ship?

RBT makes testing more focused and helps stakeholders understand release risk.

## When To Use Risk Based Testing

Risk Based Testing is useful when:

- the project has tight deadlines;
- resources are limited;
- budget is limited;
- requirements are unstable;
- product complexity is high;
- technology is new for the team;
- domain knowledge is limited;
- security or compliance matters;
- the project uses iterative or incremental development;
- not all tests can be executed before release.

It is especially useful when the team must choose what to test first.

## Risk Management Process

Risk Based Testing is connected to risk management.

The common process includes:

1. Risk identification.
2. Risk analysis.
3. Risk response planning.
4. Risk monitoring and control.

## Risk Identification

Risk identification means finding possible risks before they become real issues.

Techniques:

- brainstorming;
- risk workshops;
- checklists;
- interviews;
- lessons learned from previous projects;
- root cause analysis;
- cause and effect diagrams;
- consulting domain experts;
- reviewing requirements and architecture.

Examples of product risks:

- payment can fail;
- user data can be exposed;
- system can crash under load;
- API can return incorrect data;
- report calculations can be wrong;
- user cannot complete checkout;
- mobile app fails on a popular device.

## Risk Register

A Risk Register is a document or spreadsheet used to track risks.

It can include:

- risk ID;
- risk description;
- affected feature;
- probability;
- impact;
- risk level;
- mitigation plan;
- owner;
- status;
- related test cases;
- residual risk.

Example:

| Risk ID | Risk | Probability | Impact | Priority | Mitigation |
| --- | --- | --- | --- | --- | --- |
| R-001 | Payment gateway fails during checkout | High | High | Critical | Prioritize payment flow tests and add API mocks |
| R-002 | Search returns irrelevant results | Medium | Medium | Medium | Add functional and exploratory search tests |
| R-003 | App layout breaks on old browser | Low | Medium | Low | Test supported browsers only |

The risk register should be updated during the project, not written once and forgotten.

## Risk Analysis

Risk analysis evaluates how important each risk is.

Two common factors:

- probability: how likely the risk is to happen;
- impact: how serious the damage will be if it happens.

Simple formula:

```text
Risk rating = Probability x Impact
```

Example:

```text
Probability = 5
Impact = 4

Risk rating = 5 x 4 = 20
```

Higher rating means higher priority for testing.

## Risk Matrix

A Risk Matrix helps visualize risk priority.

| Impact / Probability | Low | Medium | High |
| --- | --- | --- | --- |
| High Impact | Medium | High | Critical |
| Medium Impact | Low | Medium | High |
| Low Impact | Low | Low | Medium |

Typical priority groups:

- Critical or Serious: test immediately and deeply;
- High: test early and with strong coverage;
- Medium: test with reasonable coverage;
- Low: monitor or test lightly.

The exact scoring can differ between teams.

## Probability

Probability means the chance that a risk will happen.

Example scale:

| Level | Meaning |
| --- | --- |
| 5 | Frequent |
| 4 | Probable |
| 3 | Occasional |
| 2 | Remote |
| 1 | Improbable |

Factors that increase probability:

- complex code;
- recent changes;
- unclear requirements;
- many integrations;
- weak test coverage;
- inexperienced team;
- known history of defects.

## Impact

Impact means the damage if the risk happens.

Example scale:

| Level | Meaning |
| --- | --- |
| 5 | Catastrophic |
| 4 | Critical |
| 3 | Major |
| 2 | Minor |
| 1 | Negligible |

Factors that increase impact:

- financial loss;
- legal or compliance issue;
- customer data leak;
- blocked business process;
- damaged reputation;
- inability to use the system;
- safety risk.

## Risk Response Planning

After risks are analyzed, the team decides how to respond.

Common responses:

- avoid the risk;
- reduce the probability;
- reduce the impact;
- transfer the risk;
- accept the risk;
- prepare a contingency plan.

In testing, mitigation often means:

- write more tests for high-risk areas;
- test high-risk features earlier;
- assign experienced testers;
- add automation for critical flows;
- use reviews and static testing;
- prepare better test data;
- improve environment stability;
- add monitoring and reporting.

## Contingency Plan

A contingency plan is a backup plan for a bad scenario.

Examples:

- if third-party API is unavailable, use mocks;
- if performance environment is not ready, run limited load tests in staging;
- if key QA is unavailable, reassign critical tests;
- if build is unstable, suspend testing and return it to development;
- if critical defects remain, delay release or reduce scope.

Contingency planning helps the team react calmly when problems happen.

## Risk Monitoring And Control

Risks should be monitored throughout the project.

Useful activities:

- review the risk register;
- update risk probability and impact;
- identify new risks;
- monitor residual risks;
- run risk review meetings;
- analyze defect trends;
- review test results;
- track key risk indicators;
- update mitigation plans.

Risk is not static. It changes when requirements, code, team, environment, or timeline changes.

## Risk Based Testing Approach

A practical RBT process can look like this.

## 1. Analyze Requirements

Review:

- SRS;
- FRS;
- user stories;
- use cases;
- acceptance criteria;
- architecture;
- business rules.

The goal is to find unclear, complex, or risky areas early.

Requirements sign-off helps reduce late changes, but if requirements change later, the risk analysis should also be updated.

## 2. Identify Risks

For each feature or requirement, identify possible failures.

Example:

| Requirement | Risk |
| --- | --- |
| User can pay by card | Payment can fail or charge incorrect amount |
| User can reset password | Reset link can expose account access |
| Admin can export report | Report can contain incorrect financial data |

## 3. Assess Probability And Impact

Rate each risk.

Example:

| Risk | Probability | Impact | Rating |
| --- | --- | --- | --- |
| Incorrect payment amount | 4 | 5 | 20 |
| Search results sorted incorrectly | 3 | 2 | 6 |
| UI typo on settings page | 2 | 1 | 2 |

## 4. Prioritize Requirements And Tests

High-risk items should be tested first.

High-risk tests can include:

- deeper functional testing;
- negative testing;
- boundary testing;
- integration testing;
- security checks;
- performance checks;
- end-to-end scenarios.

Low-risk items may receive lighter coverage.

## 5. Design Tests Based On Risk

Choose test design techniques based on risk.

Examples:

- Decision Table Testing for complex business rules;
- Boundary Value Analysis for risky numeric limits;
- State Transition Testing for workflows with states;
- Use Case Testing for end-to-end business flows;
- Pairwise Testing for configuration combinations;
- Exploratory Testing for unclear or defect-prone areas.

The highest-risk areas should get the strongest test design.

## 6. Execute Tests By Priority

Run tests in risk priority order.

This is important when time is limited.

If testing is stopped early, at least the most critical areas were tested first.

## 7. Maintain Traceability

Track links between:

- risks;
- requirements;
- test cases;
- defects;
- test results.

This helps explain what risks were covered and what residual risks remain.

## 8. Report Results Based On Risk

Risk-based reporting should show more than pass/fail numbers.

It should explain:

- which high-risk areas were tested;
- which risks were reduced;
- which high-risk defects remain;
- which areas are not covered;
- what residual risk exists;
- whether release is acceptable.

## Residual Risk

Residual Risk is the risk that remains after testing and mitigation.

Testing reduces risk, but it rarely removes it completely.

Example:

Before testing:

- payment failure risk is high.

After testing:

- core payment flow passed;
- negative scenarios passed;
- gateway timeout scenario still not covered.

Residual risk remains because one scenario is still untested.

## Inherent, Residual, Secondary, And Recurrent Risk

### Inherent Risk

Risk that exists before controls or mitigation are applied.

Also called gross risk.

### Residual Risk

Risk that remains after controls, testing, or mitigation.

Also called net risk.

### Secondary Risk

New risk created by a risk response.

Example: using mocks solves API unavailability, but creates the risk that mocks do not match real API behavior.

### Recurrent Risk

Risk that can happen again after appearing before.

Example: a defect type that keeps returning in similar releases.

## Generic Checklist For Risk Based Testing

Consider giving higher priority to:

- important business functionality;
- user-visible functionality;
- safety-critical functionality;
- features with financial impact;
- complex source code;
- recently changed areas;
- last-minute features;
- areas that caused problems in previous projects;
- unclear requirements;
- integrations;
- end-to-end business flows;
- functionality that is expensive to fix after release.

Also ask:

- Which tests provide the best risk coverage for the time required?
- Which failures would damage users most?
- Which failures would damage the business most?
- Which defects would be hardest to recover from?

## Risk Based Testing Metrics

Useful metrics:

- planned vs executed test cases;
- passed vs failed test cases;
- defects by severity;
- open critical defects;
- test execution coverage;
- requirements coverage;
- risk coverage;
- defect leakage;
- defect detection efficiency;
- risk mitigation efficiency;
- residual risk level.

Metrics should help the team make decisions, not just create reports.

## Benefits Of Risk Based Testing

Risk Based Testing can provide:

- better use of limited testing time;
- earlier testing of critical areas;
- improved test prioritization;
- reduced residual risk;
- clearer release decisions;
- better stakeholder visibility;
- improved customer satisfaction;
- early detection of problem areas;
- more focused regression testing;
- better connection between testing and business impact.

## Common Mistakes

Common mistakes:

- treating all features as equally important;
- ignoring business impact;
- using risk scores without discussion;
- never updating the risk register;
- focusing only on technical risks;
- not linking risks to test cases;
- ignoring residual risk before release;
- testing low-risk areas first because they are easier.

Risk Based Testing requires both analysis and discipline.

## Key Idea

Risk Based Testing helps QA focus on what matters most.

It does not mean ignoring low-risk areas completely. It means testing smarter when time and resources are limited.

Главная мысль:

> Test the riskiest things first, because not all failures hurt equally.

## Questions

1. What is Risk Based Testing?
2. How do probability and impact affect risk priority?
3. What is a Risk Register?
4. What is residual risk?
5. Why should high-risk items be tested first?

## What To Review Later

- Risk Register
- Risk Matrix
- Residual Risk
- Requirements Coverage
- Test Coverage
- Defect Severity
- Test Prioritization
