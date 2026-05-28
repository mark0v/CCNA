# Static Testing vs Dynamic Testing

## Summary

Static Testing and Dynamic Testing are two different approaches to software quality evaluation.

Static Testing is performed without executing the program. QA, developers, or reviewers check requirements, design documents, source code, test plans, test cases, and other work products to find defects early.

Dynamic Testing is performed by executing the program. The team checks actual product behavior, compares actual results with expected results, and finds functional or non-functional defects.

In short:

- `Static Testing` = checking artifacts without execution.
- `Dynamic Testing` = running software and validating behavior.

## Key Points

- Static testing is performed without code execution.
- Dynamic testing is performed by executing code.
- Static testing is more about defect prevention.
- Dynamic testing is more about defect detection.
- Static testing is related to verification.
- Dynamic testing is related to validation.
- Static testing can be performed early, even before compilation.
- Dynamic testing is performed after software can run.
- Static testing is usually cheaper because defects are found earlier.
- Dynamic testing shows real system behavior under test.

## Notes

### What Is Static Testing?

Static Testing is a testing approach where software artifacts are checked without running the application.

The goal is to find errors as early as possible in the SDLC/STLC.

Static testing can be manual or automated.

Examples of work products:

- requirement specifications;
- design documents;
- source code;
- test plans;
- test cases;
- test scripts;
- help/user documentation;
- web page content;
- API documentation;
- diagrams and architecture documents.

Static testing is also called:

- non-execution testing;
- verification testing;
- review-based testing.

### Why Static Testing Matters

Defects are cheaper to fix early.

If an ambiguous requirement is found during review, it can be fixed before design, coding, and testing. If the same defect is found after development, it may require changes in code, tests, documentation, and business logic.

Static testing helps:

- prevent defects;
- improve requirements quality;
- improve design quality;
- enforce coding standards;
- find missing scenarios;
- improve test cases before execution;
- reduce rework later.

### Static Testing Techniques

#### Informal Review

Informal Review is a simple review without a strict process.

The reviewer reads a document or code and gives comments.

#### Technical Review

Technical Review is performed by peers or technical specialists.

The goal is to check technical correctness, feasibility, standards, and consistency.

#### Walkthrough

Walkthrough is a session where the author explains the work product to the team.

Participants ask questions, discuss unclear points, and suggest improvements.

#### Inspection

Inspection is a formal review technique with a strict process.

The goal is to find defects systematically.

Usually includes:

- trained moderator;
- reviewers;
- checklist;
- defect logging;
- follow-up;
- rework confirmation.

#### Static Code Review

Static Code Review is a systematic review of source code without executing it.

It can check:

- syntax issues;
- coding standards;
- code style;
- readability;
- maintainability;
- security problems;
- duplicated code;
- code optimization opportunities;
- possible logical errors.

## What Is Dynamic Testing?

Dynamic Testing is a testing approach where software is executed and tested during runtime.

Dynamic testing validates actual system behavior.

It checks:

- functional behavior;
- inputs and outputs;
- business workflows;
- memory usage;
- CPU usage;
- performance;
- security behavior;
- integration behavior;
- reliability.

Dynamic testing is also called:

- execution-based testing;
- validation testing.

### Why Dynamic Testing Matters

Static testing can find many issues early, but it does not show full runtime behavior.

Dynamic testing is needed because some defects appear only when software runs:

- wrong output;
- broken flow;
- crash;
- memory leak;
- slow response;
- database error;
- API timeout;
- security vulnerability;
- browser/device issue;
- integration failure.

## Dynamic Testing Techniques / Levels

### Unit Testing

Unit Testing verifies individual units or modules.

### Integration Testing

Integration Testing verifies grouped modules and their interactions.

### System Testing

System Testing verifies the whole system against requirement specification.

### Non-Functional Dynamic Testing

Dynamic testing also includes non-functional testing.

Examples:

- performance testing;
- load testing;
- stress testing;
- security testing;
- usability testing;
- compatibility testing;
- reliability testing.

## Static Testing vs Dynamic Testing

| Static Testing | Dynamic Testing |
| --- | --- |
| Done without executing the program. | Done by executing the program. |
| Verification process. | Validation process. |
| Focus on prevention of defects. | Focus on finding defects. |
| Checks code and documentation. | Checks running software behavior. |
| Can be performed before compilation. | Performed after software can run. |
| Uses reviews, inspections, static analysis. | Uses test cases, test execution, runtime checks. |
| Cost of finding/fixing defects is usually lower. | Cost of finding/fixing defects is usually higher. |
| Finds issues in requirements, design, code, tests. | Finds functional, integration, performance and runtime issues. |
| Requires review process and checklists. | Requires test environment, test data and executable build. |
| ROI is high because it starts early. | ROI depends on coverage, timing and execution quality. |

### Verification vs Validation

Static testing is mostly verification.

Verification asks:

> Are we building the product right?

Dynamic testing is mostly validation.

Validation asks:

> Are we building the right product?

Both are needed.

## Advantages of Static Testing

- Finds defects early.
- Reduces cost of fixing defects.
- Improves requirement and design quality.
- Helps prevent defects before code execution.
- Can improve test cases before execution.
- Supports standards and consistency.
- Good ROI because it starts early.

## Limitations of Static Testing

- Does not show actual runtime behavior.
- Cannot detect all integration or environment issues.
- Requires time for reviews and meetings.
- Review quality depends on reviewer skill.
- Some defects appear only during execution.

## Advantages of Dynamic Testing

- Shows actual product behavior.
- Finds functional defects.
- Finds runtime and integration issues.
- Validates outputs against expected results.
- Can measure performance, memory and CPU usage.
- Gives confidence before release.

## Limitations of Dynamic Testing

- Starts later than static testing.
- Defects can be more expensive to fix.
- Requires executable build.
- Requires environment and test data.
- Can be time-consuming.
- Coverage depends on selected test cases.

## Best Practices

- Use static testing early in SDLC.
- Review requirements before design/coding.
- Review test cases before execution.
- Use checklists for formal reviews.
- Automate static analysis where useful.
- Use dynamic testing to validate real behavior.
- Combine static and dynamic testing in one QA strategy.
- Do not treat one approach as replacement for the other.

## Commands / Terms

- `Static Testing` - testing without executing software.
- `Dynamic Testing` - testing by executing software.
- `Verification` - checking whether product is built correctly against specifications.
- `Validation` - checking whether product meets user/business needs.
- `Review` - examination of a work product.
- `Inspection` - formal review with defined process.
- `Walkthrough` - author-led explanation and review of work product.
- `Static Code Review` - source code review without execution.
- `Test Execution` - running test cases against software.
- `Runtime Behavior` - behavior observed while software is running.

## Questions

1. What is static testing?
2. What is dynamic testing?
3. What is the main difference between static and dynamic testing?
4. Why is static testing useful early in SDLC?
5. What documents can be checked during static testing?
6. What are common static testing techniques?
7. Why is dynamic testing needed if static testing is done?
8. How are verification and validation different?
9. Which testing approach is usually cheaper for defect detection?
10. Why should QA use both static and dynamic testing?

## What To Review Later

- Verification vs validation
- Review techniques
- Inspection
- Walkthrough
- Static code analysis
- Functional testing
- Non-functional testing
- Test execution
