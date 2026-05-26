# Acceptance Testing / User Acceptance Testing (UAT)

## Summary

Acceptance Testing - это уровень testing, на котором user, customer или другие stakeholders проверяют, готова ли система к acceptance и реальному использованию.

Обычно acceptance testing выполняется после system testing, когда большинство critical и major defects уже исправлены. Цель - не просто найти defects, а подтвердить confidence в том, что system соответствует business needs, acceptance criteria, contract requirements или regulatory requirements.

User Acceptance Testing, или UAT, - самый известный вид acceptance testing. Он фокусируется на том, подходит ли system для использования business users.

## Key Points

- Acceptance testing обычно выполняется user/customer side, но могут участвовать и другие stakeholders.
- Основная цель - establish confidence in the system.
- UAT больше связан с validation: "Built the right product?"
- Acceptance testing может происходить не только после system testing, но и на разных уровнях.
- Виды acceptance testing: User Acceptance, Operational Acceptance, Contract Acceptance, Compliance Acceptance.
- Acceptance criteria должны быть понятны заранее.

## Notes

### What Is Acceptance Testing?

Acceptance Testing проверяет, готов ли продукт быть accepted пользователем, заказчиком, business side или другой ответственной стороной.

Если system testing отвечает на вопрос:

> Does the system work according to requirements?

то acceptance testing спрашивает:

> Does the system satisfy user/customer/business expectations?

Acceptance testing чаще сфокусирован на validation, а не только verification.

Verification проверяет:

- соответствует ли продукт specification;
- правильно ли реализованы requirements;
- работает ли system technically correct.

Validation проверяет:

- решает ли продукт реальную business problem;
- удобен ли он для users;
- соответствует ли он ожиданиям customer;
- можно ли его принять и использовать.

### When Acceptance Testing Happens

Чаще всего acceptance testing выполняется после system testing.

Typical flow:

1. Unit Testing
2. Integration Testing
3. System Testing
4. Acceptance Testing

Но acceptance testing может происходить и на других уровнях.

Examples:

- Commercial Off-The-Shelf software может acceptance tested после installation или integration.
- Usability acceptance для component может выполняться уже во время component testing.
- Acceptance testing of a new functional enhancement может происходить до full system testing, если business хочет рано validate feature.

### Who Performs Acceptance Testing?

Acceptance testing может выполнять:

- end users;
- customer representatives;
- business users;
- product owner;
- application managers;
- system administrators;
- compliance specialists;
- legal or regulatory stakeholders.

Роль QA часто состоит не в том, чтобы "заменить пользователя", а в том, чтобы подготовить процесс:

- test environment;
- test data;
- UAT scenarios;
- acceptance criteria;
- defect reporting flow;
- support during execution;
- final test summary.

## Types of Acceptance Testing

### 1. User Acceptance Testing (UAT)

User Acceptance Testing focuses mainly on functionality and fitness-for-use.

UAT выполняется users, business representatives или application managers. Они проверяют, можно ли использовать system для реальных business tasks.

Focus areas:

- business workflows;
- user journeys;
- acceptance criteria;
- real-life scenarios;
- usability from business perspective;
- correctness of business rules;
- readiness for release.

Example:

Для online shopping system business users проверяют:

- customer can register;
- customer can add product to cart;
- discount is applied correctly;
- order can be paid;
- invoice is generated;
- order status is visible;
- cancellation works according to business rules.

### 2. Operational Acceptance Testing (OAT)

Operational Acceptance Testing, или Production Acceptance Testing, проверяет, готова ли system к operation in production.

Обычно OAT выполняется system administration, DevOps, operations или infrastructure team перед release.

Focus areas:

- backup and restore;
- disaster recovery;
- deployment procedure;
- monitoring and alerts;
- logging;
- maintenance tasks;
- security checks;
- access control;
- failover;
- scheduled jobs;
- operational documentation.

Example:

Перед release команда проверяет, что database backup создается автоматически, restore procedure работает, monitoring alerts приходят, а production logs доступны support team.

### 3. Contract Acceptance Testing

Contract Acceptance Testing выполняется against acceptance criteria, которые были formally defined in contract.

Этот вид особенно важен для custom developed software.

Acceptance criteria должны быть согласованы заранее, когда contract подписывается.

Focus areas:

- contract requirements;
- agreed deliverables;
- formal acceptance criteria;
- milestone acceptance;
- documented pass/fail conditions.

Example:

В contract указано, что report generation must complete within 10 seconds for 10,000 records. Acceptance testing проверяет именно это условие.

### 4. Compliance Acceptance Testing

Compliance Acceptance Testing, или Regulation Acceptance Testing, проверяет соответствие system regulations, laws, safety standards или industry rules.

Focus areas:

- governmental regulations;
- legal requirements;
- safety standards;
- financial compliance;
- healthcare compliance;
- privacy requirements;
- audit requirements;
- security policies.

Example:

Healthcare system проверяется на соответствие privacy/security requirements. Banking application проверяется на regulatory rules для обработки transactions и customer data.

## Acceptance Testing vs System Testing

| System Testing | Acceptance Testing |
| --- | --- |
| Выполняется QA team. | Выполняется users/customer/stakeholders, часто при поддержке QA. |
| Проверяет whole system against requirements. | Проверяет readiness for business/user acceptance. |
| Фокус на functional and non-functional requirements. | Фокус на business value, acceptance criteria и fitness-for-use. |
| Обычно перед acceptance testing. | Обычно после system testing. |
| Defects still actively found and fixed. | Главная цель - confidence and acceptance decision. |

## UAT Process

Typical UAT flow:

1. Define acceptance criteria.
2. Prepare UAT plan.
3. Select business users or customer representatives.
4. Prepare UAT environment.
5. Prepare realistic test data.
6. Create UAT scenarios.
7. Execute UAT.
8. Log defects or change requests.
9. Retest fixes if needed.
10. Get sign-off or acceptance decision.

### UAT Deliverables

Common deliverables:

- UAT plan;
- acceptance criteria;
- UAT scenarios;
- test data;
- defect list;
- UAT summary report;
- sign-off document.

### Common UAT Risks

UAT can fail or become messy when:

- acceptance criteria are unclear;
- business users are unavailable;
- UAT environment is unstable;
- test data is unrealistic;
- users test new change requests instead of agreed scope;
- defects are reported without enough details;
- stakeholders disagree on acceptance decision.

### Practical Tips

- Define acceptance criteria before UAT starts.
- Use realistic business scenarios, not only technical test cases.
- Keep UAT scope clear.
- Prepare users and explain defect reporting rules.
- Make sure environment is stable.
- Separate defects from change requests.
- Track blockers and sign-off status.

## Commands / Terms

- `Acceptance Testing` - testing to decide whether the system can be accepted.
- `UAT` - User Acceptance Testing.
- `OAT` - Operational Acceptance Testing.
- `Validation` - checking whether the right product was built for user needs.
- `Acceptance Criteria` - conditions that must be met for acceptance.
- `Sign-off` - formal approval that the system is accepted.
- `COTS` - Commercial Off-The-Shelf software.
- `Contract Acceptance Testing` - testing against contract acceptance criteria.
- `Compliance Acceptance Testing` - testing against laws, regulations, or standards.
- `Production Acceptance Testing` - another name for operational acceptance testing.

## Questions

1. What is acceptance testing?
2. What is UAT?
3. Who usually performs acceptance testing?
4. What is the main goal of acceptance testing?
5. How is acceptance testing different from system testing?
6. What is operational acceptance testing?
7. What is contract acceptance testing?
8. What is compliance acceptance testing?
9. Why are acceptance criteria important?
10. What does UAT sign-off mean?

## What To Review Later

- System testing
- UAT process
- Acceptance criteria
- Validation vs verification
- Sign-off
- Business scenarios
- Operational readiness
- Compliance testing
