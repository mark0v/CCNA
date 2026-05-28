# Functional Testing

## Summary

Functional Testing проверяет, что software application работает according to defined requirements.

QA подает inputs, выполняет user actions, проверяет outputs и сравнивает actual behavior с expected behavior. Главная цель - убедиться, что features, workflows, business rules и user interactions работают так, как должны.

Проще:

> Functional testing checks what the system does.

Если user должен иметь возможность login, search, submit form, pay, create order или edit profile, functional testing проверяет именно это поведение.

## Key Points

- Functional testing проверяет application against functional requirements.
- Основной фокус - inputs, outputs, actions, workflows и business rules.
- Это black-box focused testing, хотя некоторые functional checks могут использовать internal knowledge.
- Functional testing может выполняться manually или through automation.
- Важны clear requirements, realistic test data и expected outcomes.
- Functional testing покрывает core features, user journeys, data validation, logic, integrations, error handling и state changes.
- Цель не просто увеличить coverage, а найти product risks и behavior issues, влияющие на users.

## Notes

### What Is Functional Testing?

Functional Testing - это testing type, который отвечает на вопрос:

> Does the system do what it is supposed to do?

QA проверяет system behavior against:

- functional specifications;
- user stories;
- acceptance criteria;
- business rules;
- use cases;
- product requirements.

Functional testing не фокусируется на internal code structure. В большинстве случаев tester смотрит на product from outside: вводит data, выполняет actions и проверяет result.

### What Gets Tested Under Functional Testing?

Functional testing может покрывать разные parts of application.

#### Core Features and Functionality

QA проверяет, что main features работают individually.

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

QA проверяет complete user journeys from start to finish.

Examples:

- user registers, logs in, adds item to cart, pays, receives confirmation;
- admin creates product, updates price, publishes product, sees it in catalogue;
- customer resets password and logs in with new credentials.

#### Data Validation

QA проверяет, как system обрабатывает valid, invalid и edge case inputs.

Examples:

- required fields;
- invalid email format;
- too long password;
- negative quantity;
- special characters;
- boundary values;
- duplicate records.

#### System Logic and Business Rules

QA проверяет conditions, calculations и decision logic.

Examples:

- discount applies only for eligible users;
- tax is calculated correctly;
- user cannot withdraw more than balance;
- order cannot be cancelled after shipment;
- access is denied for user without permission.

#### Integration Points

Functional testing может включать проверки points where modules, APIs, databases и external systems interact.

Examples:

- frontend sends correct request to backend;
- API returns expected response;
- database stores correct values;
- payment gateway result updates order status;
- email service sends confirmation.

#### Error Handling and Messages

QA проверяет, как system handles failures and bad inputs.

Examples:

- clear error message for wrong password;
- friendly validation message for required fields;
- fallback when payment fails;
- proper message when file upload exceeds size limit.

#### State Management and Dependencies

QA проверяет, что behavior зависит от previous actions and state correctly.

Examples:

- cart keeps items after login;
- order status changes from `Pending` to `Paid`;
- user cannot access checkout with empty cart;
- button becomes enabled only after required fields are filled.

## Functional Testing Process

### 1. Start With Test Requirements

Functional testing начинается с clear requirements.

QA изучает:

- functional specifications;
- user stories;
- acceptance criteria;
- business rules;
- mockups;
- API documentation;
- product notes.

Цель - понять expected behavior.

### 2. Build Realistic Test Data

Test data должна отражать реальное использование product.

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

Чем ближе test data к real usage, тем выше шанс поймать real defects.

### 3. Define Expected Outcomes

Для каждого test scenario нужно определить expected result.

Expected outcome помогает понять:

- что должно произойти;
- какие данные должны измениться;
- какое сообщение должно появиться;
- какой status должен быть установлен;
- какой page должен открыться;
- какой API response ожидается.

Без expected result testing становится guessing.

### 4. Run Tests in Realistic Environments

Tests можно выполнять manually или through automation.

Важно запускать проверки в realistic environments:

- real browsers;
- real devices where possible;
- realistic network conditions;
- test database;
- integration environment;
- production-like configuration.

Controlled setup может скрыть bugs, которые проявятся у users.

### 5. Log Defects Clearly

Когда actual result отличается от expected result, QA logs defect.

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

Unit Testing проверяет individual functions, methods или classes independently.

Обычно выполняется developers.

### Component Testing

Component Testing проверяет individual component isolated from the rest of the system.

Это уровень выше unit testing.

### Integration Testing

Integration Testing проверяет interactions and data flow between components.

Focus: modules work together correctly.

### End-to-End Testing

End-to-End Testing проверяет complete user workflow across multiple features and components.

Focus: real user journey from start to finish.

### User Acceptance Testing (UAT)

UAT выполняется users, customers или business representatives.

Focus: product meets real-world requirements and is ready for deployment.

### Regression Testing

Regression Testing проверяет, что changes не сломали existing functionality.

Useful after bug fixes, new features, refactoring or enhancements.

### Smoke Testing

Smoke Testing - quick preliminary check after new build.

Focus: core functionality works and build is stable enough for deeper testing.

### Sanity Testing

Sanity Testing - focused check after minor change or bug fix.

Focus: changed area works rationally.

### Black Box Testing

Black Box Testing проверяет functionality through inputs and outputs without knowing internal code.

### White Box Testing

White Box Testing проверяет internal logic and code structure.

Tester has source code visibility.

### Exploratory Testing

Exploratory Testing - unscripted investigation of software.

Tester learns, designs and executes tests at the same time.

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
