# Seven Testing Principles

## Summary

Seven Testing Principles are foundational ideas that explain how to think about software testing.

They help teams avoid unrealistic expectations, set priorities, start QA activities earlier, update test cases, and remember that quality is not only about the absence of defects but also about meeting real user needs.

## Key Points

- Testing shows the presence of defects, but not their complete absence.
- Exhaustive testing is almost always impossible.
- Testing should start as early as possible.
- Most defects are often concentrated in a small number of modules.
- Repeating the same tests forever eventually stops finding new bugs.
- Testing depends on the product context.
- Software with no known errors can still be poor if it does not meet user needs.

## Notes

### 1. Testing Shows Presence of Defects

Testing can show that defects are present, but it cannot prove that there are no defects.

Even if an application is tested thoroughly and all test cases pass, it is not accurate to say the product is 100% defect-free. Testing reduces the number of undiscovered defects, but the absence of found defects is not proof of complete correctness.

Practical meaning:

- QA does not guarantee that no bugs exist.
- QA provides information about quality and risk.
- Better testing strategy lowers the probability of missed critical defects.

### 2. Exhaustive Testing Is Impossible

Exhaustive testing means testing all possible inputs, states, combinations, and preconditions.

In real projects, this is almost always impossible because of the number of combinations, time, and resources.

Example:

If a form has 15 input fields, and each field has 5 possible values, the number of combinations is:

```text
5^15 = 30,517,578,125
```

Testing more than 30 billion combinations is unrealistic for a normal project.

That is why testing should be risk-based and priority-based.

### 3. Early Testing

Testing activities should begin as early as possible in the SDLC.

This is also called shift-left testing: QA participates not only after development, but also during requirements, design, planning, and refinement.

Early testing helps:

- find ambiguity in requirements;
- prevent defects before code is written;
- improve acceptance criteria;
- reduce the cost of fixing defects;
- make the product more testable.

### 4. Defect Clustering

Defect clustering means defects are often distributed unevenly.

A small number of modules may contain most defects or cause most operational failures.

Common causes:

- complex business logic;
- frequent changes;
- poor code quality;
- weak ownership;
- legacy code;
- integrations;
- unclear requirements.

### 5. Pesticide Paradox

Pesticide paradox means that if the same tests are repeated again and again, eventually they stop finding new defects.

This does not mean regression tests are useless. They are important for known risks. But if a test suite is never updated, it becomes stale.

Ways to avoid pesticide paradox:

- review test cases regularly;
- add new scenarios;
- change test data;
- use exploratory testing;
- analyze production defects;
- update regression suite after new features;
- remove outdated or duplicate tests.

### 6. Testing Is Context Dependent

Testing depends on context.

Different products require different testing approaches. A medical system, banking application, game, landing page, embedded system, and e-commerce website cannot be tested in exactly the same way.

Context affects:

- testing depth;
- documentation level;
- regulatory requirements;
- risk tolerance;
- test environments;
- security requirements;
- performance expectations;
- release process.

### 7. Absence-of-Errors Fallacy

Absence-of-errors fallacy means that even if no defects are found or all known defects are fixed, the software may still be unsuccessful.

A product can work technically correctly but still be useless if it:

- does not solve a user problem;
- does not meet business needs;
- is inconvenient to use;
- is built according to the wrong requirements;
- is too complex for its audience;
- does not deliver expected value.

QA should ask not only "does it work according to specification?" but also "does it help the user achieve the goal?"

## Commands / Terms

- `Testing shows presence of defects` - testing finds defects, but cannot prove their absence.
- `Exhaustive testing` - attempt to test all possible combinations, usually impossible.
- `Early testing` - starting testing activities as early as possible.
- `Shift-left testing` - moving QA involvement earlier in SDLC.
- `Defect clustering` - most defects are often concentrated in a small number of modules.
- `Pesticide paradox` - repeated unchanged tests stop finding new defects.
- `Context dependent testing` - testing approach depends on product/domain/risk.
- `Absence-of-errors fallacy` - defect-free software can still fail user needs.
- `Risk-based testing` - focusing testing effort on high-risk areas.

## Questions

1. What are the seven testing principles?
2. Why can't testing prove that there are no defects?
3. Why is exhaustive testing impossible?
4. What is early testing?
5. What does defect clustering mean?
6. What is the pesticide paradox?
7. Why is testing context dependent?
8. What is absence-of-errors fallacy?
9. How can QA avoid pesticide paradox?
10. Why should QA use risk-based testing?

## What To Review Later

- STLC phases
- Risk-based testing
- Shift-left testing
- Test case review
- Regression testing
- Exploratory testing
- Requirement testability
