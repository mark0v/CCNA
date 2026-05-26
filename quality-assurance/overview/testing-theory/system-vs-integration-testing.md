# System Testing vs Integration Testing

## Summary

System Testing и Integration Testing - это разные уровни software testing.

Integration Testing проверяет, как modules, components или services взаимодействуют друг с другом после объединения. System Testing проверяет весь fully integrated product как единое целое against functional и non-functional requirements.

Проще:

- `Integration Testing` = работают ли joined units together?
- `System Testing` = работает ли весь product as a complete system?

Оба уровня важны в SDLC, но они отвечают на разные вопросы, выполняются в разное время и помогают находить разные types of defects.

## Key Points

- Integration testing выполняется после unit testing.
- System testing выполняется после integration testing.
- Integration testing ищет interface errors между modules.
- System testing ищет system-level errors в whole build.
- Integration testing может использовать black box, white box или gray box techniques.
- System testing обычно выполняется как black box testing.
- Integration testing больше focused на component interaction.
- System testing больше focused на business requirements, end-to-end behavior и non-functional quality.

## Notes

### Main Difference

Integration Testing проверяет combined units.

System Testing проверяет complete build.

Example:

В online shop integration testing проверит, правильно ли shopping cart передает данные в billing module, а billing module - в payment service.

System testing проверит весь checkout flow end-to-end:

- user logs in;
- user adds product to cart;
- discount applies correctly;
- shipping cost is calculated;
- payment succeeds;
- order is created;
- confirmation email is sent;
- order appears in user profile.

### Comparison Table

| Area | System Testing | Integration Testing |
| --- | --- | --- |
| Intention | Проверить, что total build fulfills business specifications. | Проверить, что joined units interact correctly. |
| Testing Level | Обычно 3rd level. | Обычно 2nd level. |
| Performed After | Integration testing. | Unit testing. |
| Focus | Whole system behavior. | Interfaces between modules/components. |
| Type | Functional and non-functional testing. | Mostly functional/interface testing. |
| Technique | Mostly black box testing. | Black box, white box or gray box testing. |
| Main Value | Finds system-level errors. | Finds interface/integration errors. |
| Team | QA team, sometimes with developers/support. | QA, developers or mixed technical team. |
| Environment | Close to production. | Integration environment, sometimes partial. |
| Dependencies | Full system is usually available. | Some modules may be replaced by stubs/drivers. |

### Similarities

System testing and integration testing still have important similarities.

Both:

- are levels of testing in SDLC;
- involve QA participation;
- can include functional testing;
- can use black box technique;
- need realistic test data;
- benefit from stable test environment;
- help improve quality before release;
- are especially effective when combined with Agile feedback cycles.

They are not competitors. They complement each other.

### What Is System Testing?

System Testing evaluates the complete integrated application as one product.

It checks whether the system meets:

- functional requirements;
- non-functional requirements;
- business rules;
- user journeys;
- design expectations;
- operational expectations.

System testing usually happens after unit and integration testing.

The product may then move to acceptance testing, where customer/users validate whether the system is ready for real use.

### When System Testing Is Done

System testing is performed when:

- unit testing is complete;
- integration testing is complete;
- complete build is available;
- requirements are defined;
- test conditions are prepared;
- test environment is ready;
- QA can validate end-to-end system behavior.

System testing may also happen during alpha or beta phases, depending on project process.

### What Tests Are Included in System Testing?

System testing can include functional and non-functional checks.

Functional examples:

- login;
- registration;
- checkout;
- search;
- reporting;
- permissions;
- notifications;
- business workflows.

Non-functional examples:

- performance testing;
- load testing;
- stress testing;
- security testing;
- usability testing;
- compatibility testing;
- compliance testing;
- recovery testing.

### System Testing Approaches

#### Requirements-Based

Test cases are created directly from requirements.

This approach helps verify that documented requirements are covered.

#### Use Case-Based

Test cases are based on user flows and use cases.

This approach helps validate how the system behaves from the user perspective.

### How System Testing Is Done

Typical flow:

1. Create test plan.
2. Define test cases and use cases.
3. Prepare test data.
4. Prepare production-like environment.
5. Execute manual and/or automated tests.
6. Review test results.
7. Log defects.
8. Developers fix defects.
9. QA performs retesting.
10. QA performs regression testing.
11. Repeat until exit criteria are met.

### What Is Integration Testing?

Integration Testing verifies whether combined units interact correctly.

It starts after unit testing, when individual components have already been tested in isolation.

Integration testing helps find:

- data mapping errors;
- wrong API contracts;
- broken interfaces;
- authentication issues between components;
- transaction problems;
- dependency issues;
- incorrect error handling;
- communication setup mismatches.

### When Integration Testing Is Done

Integration testing is performed when:

- unit testing is complete;
- two or more modules are ready to be joined;
- interfaces need verification;
- modules communicate with each other;
- external systems are connected;
- QA/dev team wants to detect interface defects early.

### Why Interface Errors Happen

Integration defects can appear because:

- modules were developed by different developers;
- external systems use different communication protocols;
- expected data format differs from actual format;
- one component changed its contract;
- modules were integrated incorrectly;
- environment configuration differs between machines;
- authentication/session handling is inconsistent.

### Integration Testing Approaches

#### Top-Down

Testing starts from upper modules and moves downward.

Stubs simulate lower-level modules.

Advantages:

- main business flows can be tested early;
- high-level design issues are detected sooner.

Disadvantages:

- lower-level modules may be tested late.

#### Bottom-Up

Testing starts from lower modules and moves upward.

Drivers simulate higher-level callers.

Advantages:

- low-level modules are deeply tested early;
- useful for core services and technical components.

Disadvantages:

- top-level flows may be tested late.

#### Hybrid / Sandwich

Hybrid testing combines top-down and bottom-up approaches.

Stubs and drivers can both be used.

Advantages:

- top and bottom layers can be tested in parallel.

Disadvantages:

- planning is more complex.

### Integration Tests vs Unit Tests vs End-to-End Tests

| Test Type | Focus | Typical Order |
| --- | --- | --- |
| Unit Testing | Individual code unit in isolation. | First |
| Integration Testing | Communication between modules/components. | Second |
| System Testing | Complete system against requirements. | Third |
| End-to-End Testing | Full user/business flow across the system, often from user perspective. | Later / system-level |
| Acceptance Testing | Business/customer acceptance. | Final validation |

These testing levels are not mutually exclusive. A healthy test strategy uses them together.

### Practical Example

Imagine a payment flow:

Unit testing checks:

- discount calculation function;
- tax calculation function;
- payment response parser.

Integration testing checks:

- checkout sends correct amount to payment module;
- payment module handles gateway response;
- billing updates invoice;
- order service receives paid status.

System testing checks:

- complete checkout flow works for real user scenario;
- performance is acceptable;
- error messages are clear;
- security rules are applied;
- confirmation email is sent;
- order appears correctly in user account.

Acceptance testing checks:

- business users agree that checkout meets their expectations and can be released.

## Commands / Terms

- `System Testing` - testing the complete integrated system against requirements.
- `Integration Testing` - testing interactions between joined modules/components.
- `Interface Error` - defect at the boundary between components.
- `Black Box Testing` - testing from external behavior without code knowledge.
- `White Box Testing` - testing with knowledge of internal code/structure.
- `Gray Box Testing` - testing with partial internal knowledge.
- `Stub` - simulated lower-level module.
- `Driver` - simulated higher-level caller.
- `End-to-End Testing` - testing a complete user/business flow.
- `Regression Testing` - checking that fixes/changes did not break existing behavior.

## Questions

1. What is the main difference between system testing and integration testing?
2. Which testing level comes first: integration or system testing?
3. What defects does integration testing usually find?
4. What defects does system testing usually find?
5. Why can integration testing use stubs and drivers?
6. Why is system testing usually black box testing?
7. What is top-down integration testing?
8. What is bottom-up integration testing?
9. How are unit, integration, system, and acceptance testing related?
10. Why are both integration and system testing needed?

## What To Review Later

- Unit testing
- Integration testing
- System testing
- Acceptance testing
- Stubs and drivers
- Black box vs white box vs gray box
- End-to-end testing
- Regression testing
