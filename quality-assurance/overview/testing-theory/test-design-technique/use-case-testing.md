# Use Case Testing

## Summary

Use Case Testing - это black-box test design technique, которая помогает создавать test cases на основе real user interactions with the system.

Use case описывает, как actor использует system to achieve a specific goal or produce value. Test cases, derived from use cases, проверяют full transaction or user flow from start to finish.

Эта техника особенно полезна на system testing и acceptance testing levels, потому что она фокусируется на real-world use of the product.

## Key Points

- Use case describes a particular use of the system by an actor.
- Actor can be a user or another system.
- Use cases describe what actor does and sees, not internal system implementation.
- Use case testing helps test complete flows from start to finish.
- Technique is useful for finding integration defects.
- Each use case usually has main success scenario and alternative/exception scenarios.
- Use case should specify preconditions and postconditions.
- Use case testing is valuable for system and acceptance testing.

## Notes

### What Is a Use Case?

A use case is a description of interaction between actor and system.

Actor can be:

- human user;
- external system;
- subsystem;
- communication link;
- service.

Use case describes:

- actor goal;
- sequence of steps;
- system responses;
- alternative flows;
- exceptions;
- preconditions;
- postconditions.

Use cases are usually written in business language, especially when actor is a business user.

### What Is Use Case Testing?

Use Case Testing uses use cases as a basis for designing test cases.

It answers:

> Can the actor complete this real task from start to finish?

Instead of testing isolated fields or functions, QA tests complete transactions.

Examples:

- user withdraws cash from ATM;
- customer places an order;
- admin approves request;
- user resets password;
- customer books appointment;
- support agent closes ticket.

### Why Use Case Testing Matters

Use cases describe likely paths through the system.

This makes use case tests good at finding defects that users are likely to meet during real work.

Use case testing can uncover:

- broken workflows;
- missing steps;
- confusing business rules;
- integration defects;
- incorrect system responses;
- missing validation;
- unclear error handling;
- wrong final state.

## Main Scenario and Extensions

Each use case usually includes:

- main success scenario;
- alternative branches;
- exception flows;
- special cases.

### Main Success Scenario

Main success scenario is the normal, most likely flow.

Example:

ATM PIN entry:

1. Actor inserts card.
2. System asks for PIN.
3. Actor enters correct PIN.
4. System validates card and PIN.
5. Actor gets access to account.

### Extensions / Alternative Flows

Extensions describe what happens when something differs from the main flow.

Examples:

- card is invalid;
- PIN is incorrect;
- PIN is incorrect three times;
- actor cancels operation;
- timeout occurs;
- system is unavailable.

For use case testing, QA should create:

- one test for main success scenario;
- one or more tests for each important extension.

## Preconditions and Postconditions

### Preconditions

Preconditions describe what must be true before use case starts.

Examples:

- user has active account;
- ATM is online;
- card is valid;
- product exists in catalogue;
- user is logged in;
- booking slot is available.

### Postconditions

Postconditions describe observable result and final system state after use case completes.

Examples:

- cash is dispensed;
- account balance is updated;
- order is created;
- confirmation email is sent;
- ticket status is closed;
- failed login attempt is recorded.

Good use case tests verify both steps and final state.

## Example: ATM PIN Entry

Use case: Access account with bank card and PIN.

Actor:

- bank customer.

Preconditions:

- ATM is working;
- card is readable;
- account exists.

Main success scenario:

1. Customer inserts card.
2. System reads card.
3. System asks for PIN.
4. Customer enters valid PIN.
5. System validates PIN.
6. System allows access to account.

Postconditions:

- customer can access account menu;
- session is active.

### Alternative / Exception Scenarios

#### Extension 1: Invalid Card

1. Customer inserts card.
2. System cannot validate card.
3. System shows error.
4. System ejects card.

Expected result:

- account access is not allowed.

#### Extension 2: Incorrect PIN First Time

1. Customer inserts card.
2. Customer enters incorrect PIN.
3. System shows error.
4. System allows another attempt.

Expected result:

- account access is not allowed yet;
- attempt counter increases.

#### Extension 3: Incorrect PIN Three Times

1. Customer enters incorrect PIN three times.
2. System blocks access.
3. System retains card or locks session, depending on business rule.

Expected result:

- access denied;
- security rule applied.

From security perspective, the third invalid PIN scenario may have higher priority than a single invalid PIN attempt.

## How To Design Use Case Tests

Typical steps:

1. Identify use case.
2. Identify actor.
3. Define goal.
4. Check preconditions.
5. Write main success scenario.
6. Identify alternative and exception flows.
7. Define postconditions.
8. Create test case for main scenario.
9. Create test cases for important extensions.
10. Prioritize scenarios by risk and business value.

### What To Check

In use case testing, verify:

- actor can complete goal;
- each step produces expected response;
- data is updated correctly;
- integrations work;
- errors are handled clearly;
- security/business rules are respected;
- final state matches postconditions.

## Use Case Testing and Testing Levels

Use case testing is especially common at:

- system testing level;
- acceptance testing level;
- end-to-end testing;
- integration-heavy flows.

It can also help during requirements review because use cases make user behavior visible and easier to discuss with business stakeholders.

## Advantages

- Focuses on real user behavior.
- Tests complete business flows.
- Helps find integration defects.
- Useful for system and acceptance testing.
- Uses business language.
- Helps involve users in requirements discussion.
- Reveals missing alternative flows.
- Connects requirements to test cases.

## Limitations

- May miss low-level input validation issues.
- Depends on quality of use cases.
- Complex systems can have many alternative flows.
- Not ideal for testing all combinations.
- Needs support from business/product side.
- Should be combined with EP, BVA, decision tables and state transition testing.

## Common Mistakes

- Testing only main success scenario.
- Ignoring extensions and exception flows.
- Not defining preconditions.
- Not checking postconditions.
- Writing use cases from system internals instead of actor perspective.
- Missing non-human actors.
- Not prioritizing high-risk flows.
- Treating use case testing as replacement for all other techniques.

## Commands / Terms

- `Use Case` - description of actor interaction with system to achieve a goal.
- `Actor` - user, system or external entity interacting with system.
- `Main Success Scenario` - normal expected flow.
- `Extension` - alternative or exception flow.
- `Precondition` - condition required before use case starts.
- `Postcondition` - observable result/final state after use case completes.
- `Transaction` - complete business operation from start to finish.
- `System Testing` - testing complete integrated system.
- `Acceptance Testing` - testing readiness for user/customer acceptance.

## Questions

1. What is use case testing?
2. What is a use case?
3. Who or what can be an actor?
4. Why are use cases written from actor perspective?
5. What is a main success scenario?
6. What are extensions in a use case?
7. Why are preconditions important?
8. Why should postconditions be checked?
9. How can use case testing find integration defects?
10. At which testing levels is use case testing most useful?

## What To Review Later

- System Testing
- Acceptance Testing
- End-to-End Testing
- State Transition Testing
- Decision Table Testing
- Preconditions and postconditions
- Business workflows
