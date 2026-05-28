# Static Testing vs Dynamic Testing

## Summary

Static Testing и Dynamic Testing - это два разных подхода к проверке software quality.

Static Testing выполняется без запуска program. QA, developers или reviewers проверяют requirements, design documents, source code, test plans, test cases и другие work products, чтобы найти defects early.

Dynamic Testing выполняется с запуском program. Команда проверяет actual behavior продукта, сравнивает actual results с expected results и ищет functional или non-functional defects.

Проще:

- `Static Testing` = проверяем artifacts without execution.
- `Dynamic Testing` = запускаем software and validate behavior.

## Key Points

- Static testing выполняется без code execution.
- Dynamic testing выполняется by executing code.
- Static testing больше про defect prevention.
- Dynamic testing больше про defect detection.
- Static testing относится к verification.
- Dynamic testing относится к validation.
- Static testing можно выполнять early, еще до compilation.
- Dynamic testing выполняется после того, как software можно запустить.
- Static testing обычно дешевле, потому что defects находятся раньше.
- Dynamic testing показывает реальное поведение system under test.

## Notes

### What Is Static Testing?

Static Testing - это testing approach, при котором software artifacts проверяются без запуска application.

Цель static testing - найти ошибки как можно раньше в SDLC/STLC.

Static testing может быть manual или automated.

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

Static testing также называют:

- non-execution testing;
- verification testing;
- review-based testing.

### Why Static Testing Matters

Defects дешевле исправлять early.

Если ambiguous requirement найден во время review, его можно исправить до design, coding and testing. Если этот же defect найден после development, он может потребовать changes in code, tests, documentation and business logic.

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

Informal Review - простой review без strict process.

Reviewer читает document или code и дает comments.

Use when:

- нужно быстро получить feedback;
- artifact небольшой;
- team wants lightweight review.

#### Technical Review

Technical Review выполняется peers или technical specialists.

Цель - проверить technical correctness, feasibility, standards and consistency.

Common artifacts:

- test strategy;
- test plan;
- requirement specification;
- architecture document;
- API design;
- database design.

#### Walkthrough

Walkthrough - это session, где author объясняет work product команде.

Participants ask questions, discuss unclear points and suggest improvements.

Обычно:

- author leads the meeting;
- participants ask questions;
- scribe records comments;
- team identifies issues and improvements.

#### Inspection

Inspection - formal review technique with strict process.

Цель - найти defects systematically.

Usually includes:

- trained moderator;
- reviewers;
- checklist;
- defect logging;
- follow-up;
- rework confirmation.

Inspection is more formal and structured than informal review or walkthrough.

#### Static Code Review

Static Code Review - systematic review of source code without executing it.

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

Static code review can be manual or automated using tools.

## What Is Dynamic Testing?

Dynamic Testing - это testing approach, при котором software запускается and tested during execution.

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

Dynamic testing также называют:

- execution-based testing;
- validation testing.

### Why Dynamic Testing Matters

Static testing может найти many issues early, но оно не показывает full runtime behavior.

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

Dynamic testing confirms whether product works according to business requirements.

## Dynamic Testing Techniques / Levels

### Unit Testing

Unit Testing проверяет individual units or modules.

Usually performed by developers.

Focus:

- functions;
- methods;
- classes;
- small code units.

### Integration Testing

Integration Testing проверяет grouped modules and their interactions.

Focus:

- data flow between modules;
- API contracts;
- interfaces;
- database interactions;
- third-party integrations.

### System Testing

System Testing проверяет whole system against requirement specification.

Focus:

- complete product behavior;
- functional requirements;
- non-functional requirements;
- end-to-end user journeys.

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

Static testing can catch unclear requirements before coding starts. Dynamic testing can prove how the product actually behaves when users interact with it.

### Examples

#### Static Testing Example

QA reviews a requirement:

> The page should load quickly.

This is not testable enough. QA comments that the requirement should be specific:

> The product search results page should load within 2 seconds for 95% of requests under normal load.

Defect prevented before development.

#### Dynamic Testing Example

QA opens the application, searches for a product, and measures response time.

Actual result:

- search results load in 5 seconds.

Expected result:

- search results load within 2 seconds.

Defect found during execution.

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
