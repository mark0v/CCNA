# System Testing

## Summary

System Testing - это уровень software testing, на котором проверяется поведение всего system или product целиком в рамках defined project scope.

Обычно system testing выполняется после unit testing и integration testing. На этом этапе отдельные modules уже разработаны, проверены и объединены. Теперь QA оценивает полностью integrated application как единый продукт.

Главная цель system testing - убедиться, что total build соответствует business specifications, functional requirements и non-functional requirements перед переходом к acceptance testing.

## Key Points

- System testing проверяет whole system, а не отдельные modules.
- Это обычно третий уровень testing после unit и integration testing.
- Основной подход - black box testing.
- Тестирование выполняется в environment, максимально похожем на production.
- Проверяются functional и non-functional requirements.
- System testing обычно выполняет independent QA team.
- После fixes выполняется regression testing, чтобы убедиться, что новые changes не сломали existing functionality.

## Notes

### What Is System Testing?

System testing оценивает fully integrated software product как single entity.

Если unit testing отвечает на вопрос "работает ли отдельный component?", а integration testing отвечает "работают ли components вместе?", то system testing спрашивает:

> Работает ли весь продукт как complete system according to requirements?

На этом этапе QA проверяет не только отдельные functions, но и complete user journeys, business processes, system behavior, error handling, compatibility, performance, security и usability.

### Place in Testing Hierarchy

Typical testing levels:

1. Unit Testing
2. Integration Testing
3. System Testing
4. Acceptance Testing

System testing находится после integration testing и перед acceptance testing.

Это важный transition point: продукт уже собран как единое целое, но еще не передан customer/users для final acceptance.

### Key Characteristics

#### Independent Testing

System testing часто выполняется independent QA team или specialist testers, а не developers, которые писали code.

Это помогает получить более объективную оценку продукта.

#### Black Box Technique

System testing обычно использует black box approach.

QA не обязан знать internal code structure. Фокус на:

- inputs;
- outputs;
- user behavior;
- business rules;
- requirements;
- external system behavior.

#### Realistic Environment

Testing environment должен быть максимально похож на production.

Это важно, потому что system-level defects могут проявляться только при реальных configuration, data, integrations, permissions, load или infrastructure conditions.

### Scope of System Testing

System testing comprehensive по своей природе. Он может включать разные виды проверок.

#### Functional Requirements

QA проверяет, что core features и user journeys работают according to requirements.

Examples:

- user can register and log in;
- customer can place an order;
- admin can manage products;
- system calculates totals correctly;
- notifications are sent;
- reports are generated.

#### Non-Functional Requirements

System testing также покрывает quality attributes.

Examples:

- performance;
- security;
- usability;
- compatibility;
- load behavior;
- stress behavior;
- reliability;
- recovery;
- accessibility.

#### System Interactions

QA проверяет, как application взаимодействует с environment и resources.

Examples:

- operating system;
- browser;
- database;
- file system;
- hardware;
- network;
- external services;
- permissions;
- logs and monitoring.

### System Testing Process

#### 1. Test Planning

Команда создает formal test plan.

В нем описываются:

- scope;
- test objectives;
- test strategy;
- required environment;
- risks;
- test cases;
- use cases;
- resources;
- schedule;
- entry and exit criteria.

#### 2. Test Data Preparation

QA подготавливает realistic test data.

Good test data должна покрывать:

- normal usage;
- boundary values;
- negative scenarios;
- edge cases;
- different user roles;
- valid and invalid data;
- production-like datasets where possible.

#### 3. Test Execution

Test cases выполняются manually или through automation.

QA фиксирует:

- passed tests;
- failed tests;
- blocked tests;
- skipped tests;
- actual results;
- defects;
- environment details.

#### 4. Reporting and Debugging

Если actual result отличается от expected result, QA logs defect.

Developers fix bugs, после чего QA выполняет:

- retesting;
- regression testing;
- status update;
- defect closure if fix is valid.

#### 5. Recycling / Re-testing Cycle

Testing cycle повторяется, пока system не достигнет required quality standards.

Обычно команда продолжает cycle до тех пор, пока:

- critical defects fixed;
- high priority defects resolved or accepted;
- regression passed;
- exit criteria met;
- stakeholders agree on release readiness.

### System Testing vs Integration Testing

| Integration Testing | System Testing |
| --- | --- |
| Проверяет interaction между modules/components. | Проверяет whole integrated product. |
| Фокус на interfaces, APIs, data flow между parts. | Фокус на complete requirements and end-to-end behavior. |
| Выполняется после unit testing. | Выполняется после integration testing. |
| Может использовать stubs/drivers. | Обычно тестирует full real system. |
| Ищет defects на границах components. | Ищет defects в product behavior as a whole. |

### Common System Testing Types

System testing can include:

- functional testing;
- regression testing;
- usability testing;
- performance testing;
- load testing;
- stress testing;
- security testing;
- compatibility testing;
- recovery testing;
- installation testing;
- configuration testing;
- accessibility testing.

Конкретный набор зависит от project scope, risks и requirements.

## Commands / Terms

- `System Testing` - testing the complete integrated system against requirements.
- `Black Box Testing` - testing without knowing internal code structure.
- `Functional Requirements` - what the system should do.
- `Non-Functional Requirements` - how the system should behave.
- `Production-like Environment` - test environment close to real production.
- `Retesting` - checking a fixed defect again.
- `Regression Testing` - checking that changes did not break existing functionality.
- `Acceptance Testing` - validation by customer/users before final acceptance.
- `Exit Criteria` - conditions required to complete testing.

## Questions

1. What is system testing?
2. When is system testing performed?
3. Why is system testing usually black box testing?
4. Who usually performs system testing?
5. What is the difference between system testing and integration testing?
6. What functional areas can system testing cover?
7. What non-functional areas can system testing cover?
8. Why should system testing use production-like environment?
9. What happens after defects are fixed?
10. Why is regression testing important during system testing?

## What To Review Later

- Testing levels
- Unit vs integration vs system testing
- Acceptance testing
- Functional testing
- Non-functional testing
- Regression testing
- Test planning
- Test environment setup
