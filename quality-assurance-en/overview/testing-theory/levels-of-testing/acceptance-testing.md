# Acceptance Testing / User Acceptance Testing (UAT)

## Summary

Acceptance Testing is a testing level where a user, customer, or other stakeholders verify whether the system is ready for acceptance and real use.

It is usually performed after system testing, when most critical and major defects have been fixed. The goal is not only to find defects, but to establish confidence that the system satisfies business needs, acceptance criteria, contract requirements, or regulatory requirements.

User Acceptance Testing, or UAT, is the most common type of acceptance testing. It focuses on whether the system is fit for use by business users.

## Key Points

- Acceptance testing is usually performed by the user/customer side, although other stakeholders may be involved.
- The main goal is to establish confidence in the system.
- UAT is mostly connected to validation: "Did we build the right product?"
- Acceptance testing can happen at more than one level.
- Types of acceptance testing include User Acceptance, Operational Acceptance, Contract Acceptance, and Compliance Acceptance.
- Acceptance criteria should be clear before testing starts.

## Notes

### What Is Acceptance Testing?

Acceptance Testing checks whether the product is ready to be accepted by the user, customer, business side, or another responsible party.

If system testing asks:

> Does the system work according to requirements?

acceptance testing asks:

> Does the system satisfy user/customer/business expectations?

Acceptance testing is usually more focused on validation than only verification.

Verification checks:

- whether the product matches the specification;
- whether requirements are implemented correctly;
- whether the system is technically correct.

Validation checks:

- whether the product solves a real business problem;
- whether it is usable for users;
- whether it matches customer expectations;
- whether it can be accepted and used.

### When Acceptance Testing Happens

Most often, acceptance testing is performed after system testing.

Typical flow:

1. Unit Testing
2. Integration Testing
3. System Testing
4. Acceptance Testing

But acceptance testing can happen at other levels too.

Examples:

- Commercial Off-The-Shelf software may be acceptance tested after installation or integration.
- Usability acceptance for a component may happen during component testing.
- Acceptance testing of a new functional enhancement may happen before full system testing if the business wants early feature validation.

### Who Performs Acceptance Testing?

Acceptance testing may be performed by:

- end users;
- customer representatives;
- business users;
- product owner;
- application managers;
- system administrators;
- compliance specialists;
- legal or regulatory stakeholders.

QA often does not replace the user. QA helps prepare the process:

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

UAT is performed by users, business representatives, or application managers. They verify whether the system can be used for real business tasks.

Focus areas:

- business workflows;
- user journeys;
- acceptance criteria;
- real-life scenarios;
- usability from business perspective;
- correctness of business rules;
- readiness for release.

### 2. Operational Acceptance Testing (OAT)

Operational Acceptance Testing, or Production Acceptance Testing, verifies whether the system is ready for operation in production.

It is usually performed by system administration, DevOps, operations, or infrastructure teams before release.

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

### 3. Contract Acceptance Testing

Contract Acceptance Testing is performed against acceptance criteria formally defined in a contract.

This type is especially important for custom developed software.

Acceptance criteria should be agreed when the contract is signed.

Focus areas:

- contract requirements;
- agreed deliverables;
- formal acceptance criteria;
- milestone acceptance;
- documented pass/fail conditions.

### 4. Compliance Acceptance Testing

Compliance Acceptance Testing, or Regulation Acceptance Testing, verifies whether the system follows regulations, laws, safety standards, or industry rules.

Focus areas:

- governmental regulations;
- legal requirements;
- safety standards;
- financial compliance;
- healthcare compliance;
- privacy requirements;
- audit requirements;
- security policies.

## Acceptance Testing vs System Testing

| System Testing | Acceptance Testing |
| --- | --- |
| Performed by QA team. | Performed by users/customer/stakeholders, often with QA support. |
| Verifies the whole system against requirements. | Verifies readiness for business/user acceptance. |
| Focuses on functional and non-functional requirements. | Focuses on business value, acceptance criteria, and fitness-for-use. |
| Usually happens before acceptance testing. | Usually happens after system testing. |
| Defects are still actively found and fixed. | Main goal is confidence and acceptance decision. |

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
