# Functional Testing

## Summary

Functional Testing verifies that a software application works according to defined requirements.

QA provides inputs, performs user actions, checks outputs, and compares actual behavior with expected behavior. The main goal is to make sure features, workflows, business rules, and user interactions work as intended.

In short:

> Functional testing checks what the system does.

If a user should be able to log in, search, submit a form, pay, create an order, or edit a profile, functional testing verifies that behavior.

## Key Points

- Functional testing checks the application against functional requirements.
- The main focus is inputs, outputs, actions, workflows, and business rules.
- It is black-box focused, although some functional checks may use internal knowledge.
- Functional testing can be performed manually or through automation.
- Clear requirements, realistic test data, and expected outcomes are important.
- Functional testing covers core features, user journeys, data validation, logic, integrations, error handling, and state changes.
- The goal is not only to increase coverage, but to find product risks and behavior issues that affect users.

## Notes

### What Is Functional Testing?

Functional Testing answers the question:

> Does the system do what it is supposed to do?

QA verifies system behavior against:

- functional specifications;
- user stories;
- acceptance criteria;
- business rules;
- use cases;
- product requirements.

Functional testing does not focus on internal code structure. In most cases, the tester looks at the product from the outside: enters data, performs actions, and checks the result.

### What Gets Tested Under Functional Testing?

Functional testing can cover different parts of an application.

#### Core Features and Functionality

QA verifies that main features work individually.

Examples:

- login;
- registration;
- search;
- forms;
- payments;
- profile update;
- file upload;
- report generation.

#### User Workflows and Scenarios

QA verifies complete user journeys from start to finish.

Examples:

- user registers, logs in, adds item to cart, pays, receives confirmation;
- admin creates product, updates price, publishes product, sees it in catalogue;
- customer resets password and logs in with new credentials.

#### Data Validation

QA verifies how the system handles valid, invalid, and edge case inputs.

Examples:

- required fields;
- invalid email format;
- too long password;
- negative quantity;
- special characters;
- boundary values;
- duplicate records.

#### System Logic and Business Rules

QA verifies conditions, calculations, and decision logic.

Examples:

- discount applies only for eligible users;
- tax is calculated correctly;
- user cannot withdraw more than balance;
- order cannot be cancelled after shipment;
- access is denied for user without permission.

#### Integration Points

Functional testing may include checks where modules, APIs, databases, and external systems interact.

Examples:

- frontend sends correct request to backend;
- API returns expected response;
- database stores correct values;
- payment gateway result updates order status;
- email service sends confirmation.

#### Error Handling and Messages

QA verifies how the system handles failures and bad inputs.

Examples:

- clear error message for wrong password;
- friendly validation message for required fields;
- fallback when payment fails;
- proper message when file upload exceeds size limit.

#### State Management and Dependencies

QA verifies that behavior depends correctly on previous actions and state.

Examples:

- cart keeps items after login;
- order status changes from `Pending` to `Paid`;
- user cannot access checkout with empty cart;
- button becomes enabled only after required fields are filled.

## Functional Testing Process

### 1. Start With Test Requirements

Functional testing starts with clear requirements.

QA studies:

- functional specifications;
- user stories;
- acceptance criteria;
- business rules;
- mockups;
- API documentation;
- product notes.

The goal is to understand expected behavior.

### 2. Build Realistic Test Data

Test data should reflect real product usage.

Include:

- valid inputs;
- invalid inputs;
- boundary values;
- edge cases;
- empty values;
- duplicate data;
- different user roles;
- different permissions;
- production-like examples.

### 3. Define Expected Outcomes

Each test scenario needs an expected result.

Expected outcome helps define:

- what should happen;
- which data should change;
- which message should appear;
- which status should be set;
- which page should open;
- which API response is expected.

### 4. Run Tests in Realistic Environments

Tests can be executed manually or through automation.

It is important to run checks in realistic environments:

- real browsers;
- real devices where possible;
- realistic network conditions;
- test database;
- integration environment;
- production-like configuration.

### 5. Log Defects Clearly

When actual result differs from expected result, QA logs a defect.

Good defect report includes:

- what was tested;
- steps to reproduce;
- actual result;
- expected result;
- environment;
- test data;
- screenshots/video/logs;
- severity and priority suggestion;
- affected requirement or user story.

## Types of Functional Testing

### Unit Testing

Unit Testing verifies individual functions, methods, or classes independently.

### Component Testing

Component Testing verifies an individual component isolated from the rest of the system.

### Integration Testing

Integration Testing verifies interactions and data flow between components.

### End-to-End Testing

End-to-End Testing verifies a complete user workflow across multiple features and components.

### User Acceptance Testing (UAT)

UAT is performed by users, customers, or business representatives.

### Regression Testing

Regression Testing verifies that changes did not break existing functionality.

### Smoke Testing

Smoke Testing is a quick preliminary check after a new build.

### Sanity Testing

Sanity Testing is a focused check after a minor change or bug fix.

### Black Box Testing

Black Box Testing verifies functionality through inputs and outputs without knowing internal code.

### White Box Testing

White Box Testing verifies internal logic and code structure.

### Exploratory Testing

Exploratory Testing is an unscripted investigation of software.

## Functional Testing vs Non-Functional Testing

| Functional Testing | Non-Functional Testing |
| --- | --- |
| Checks what the system does. | Checks how the system behaves. |
| Focus on features, workflows and business rules. | Focus on performance, security, usability, reliability, scalability. |
| Based on functional requirements. | Based on quality attributes. |
| Example: user can log in. | Example: login completes within 2 seconds. |
| Example: payment is processed correctly. | Example: system handles 5,000 users under load. |

## Advantages

- Validates product behavior against requirements.
- Helps catch core feature defects.
- Improves user satisfaction.
- Supports release decisions.
- Can be manual or automated.
- Works across different testing levels.
- Helps verify business workflows.

## Limitations

- Poor requirements can lead to weak functional testing.
- Functional tests may miss performance/security/usability problems.
- Manual execution can be time-consuming.
- Automation requires maintenance.
- Test coverage does not guarantee product quality by itself.
- Hidden edge cases may remain if test data is weak.

## Best Practices

- Start from requirements and acceptance criteria.
- Use realistic test data.
- Include positive, negative and edge cases.
- Prioritize critical business flows.
- Combine scripted and exploratory testing.
- Keep test cases clear and maintainable.
- Automate stable repetitive flows.
- Review defects and update test cases after production issues.

## Commands / Terms

- `Functional Testing` - testing what the system does against requirements.
- `Expected Result` - what should happen during a test.
- `Actual Result` - what actually happened.
- `Test Data` - input data used for testing.
- `User Workflow` - sequence of user actions to complete a goal.
- `Business Rule` - condition or logic defined by business requirements.
- `Black Box Testing` - testing external behavior without code knowledge.
- `End-to-End Testing` - testing complete user flow across the system.
- `Regression Testing` - checking that changes did not break existing functionality.
- `Exploratory Testing` - learning and testing at the same time.

## Questions

1. What is functional testing?
2. What does functional testing verify?
3. What is the difference between functional and non-functional testing?
4. Why are requirements important for functional testing?
5. What should be included in functional test data?
6. What is expected result?
7. What kinds of defects can functional testing find?
8. How is functional testing related to UAT?
9. When should functional tests be automated?
10. Why is exploratory testing useful in functional testing?

## What To Review Later

- Functional requirements
- Non-functional testing
- Test case design
- Boundary value analysis
- Equivalence partitioning
- Regression testing
- UAT
- Exploratory testing
