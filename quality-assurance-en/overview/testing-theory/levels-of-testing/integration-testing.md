# Integration Testing

## Summary

Integration Testing is a testing level where interactions between modules, components, services, or external systems are verified.

After unit testing, individual parts of a product may work correctly on their own, but that does not guarantee that they work correctly together. Integration testing helps find defects at interfaces: incorrect data formats, broken API contracts, business flow issues, authentication problems, payment gateway issues, database problems, file system interactions, operating system dependencies, hardware interactions, or third-party integration problems.

The main idea is to test not only "does the module work?" but "do the modules work together?"

## Key Points

- Integration testing is performed after unit testing and usually before system testing.
- The main focus is interfaces and interactions between components.
- Defects often appear at module boundaries.
- Integration testing can use different approaches: Big Bang, Top-Down, Bottom-Up, Incremental, Sandwich, and Functional Incremental.
- `Stubs` and `drivers` can be used when components are incomplete.
- A good integration strategy reduces the risk of late defects after the whole system is assembled.

## Notes

### What Is Integration Testing?

Integration testing verifies how different parts of a system work together after being combined.

For example, `Module A` and `Module B` may pass unit tests separately. But after integration, the team may discover that:

- one module sends data in the wrong format;
- another module expects a different field name;
- authentication token is not passed;
- order status is not updated correctly;
- payment service returns a response that billing cannot process;
- database transaction behavior differs from expectations.

That is the area of integration testing.

### Example: Online Shopping Website

Imagine an online shopping website for a company that sells camping gear.

The system includes modules such as:

- user registration and login;
- product catalogue;
- shopping cart;
- billing;
- payment gateway integration;
- shipping and package tracking.

Developers implement and unit test each module separately. At that level, everything may look fine.

But after deploying all modules into a shared environment, defects appear:

- after login, the shopping cart does not show items the user added earlier;
- billing amount does not include shipping cost;
- payment response does not update order status;
- tracking number does not appear after successful payment;
- user session is lost between cart and checkout.

Each module may be correct individually, but integration between them is broken. Integration testing helps find these issues.

### Why Integration Testing Matters

Integration defects are often expensive because they happen between responsibilities.

Examples:

- frontend expects `totalPrice`;
- backend returns `total_amount`;
- payment service expects amount in cents;
- billing module sends amount in dollars;
- shipping service requires address line 2;
- registration flow does not save user id needed by cart service.

Without integration testing, these defects may appear close to release or even in production.

## Types / Approaches

### 1. Big Bang Integration Testing

Big Bang Integration Testing is an approach where all modules are integrated at the same time and then tested as one whole system.

Advantages:

- no need to assemble the system gradually;
- useful for small systems;
- all components are ready before integration testing starts.

Disadvantages:

- defects are found late;
- root cause is hard to identify;
- debugging may take a long time;
- risky for large systems.

### 2. Top-Down Integration Testing

Top-Down Integration Testing starts from the upper levels of system architecture and gradually moves downward.

High-level modules such as UI, main menu, orchestration layer, or main business flow are tested first. Lower-level modules that are not ready are replaced by `stubs`.

`Stub` is a temporary component that simulates the behavior of a lower-level module.

Advantages:

- main flows can be verified early;
- product feels closer to real user experience;
- stubs are usually easier to write than drivers;
- high-level design defects are found earlier.

Disadvantages:

- low-level functionality is tested later;
- stubs are required;
- some technical details remain unverified until later.

### 3. Bottom-Up Integration Testing

Bottom-Up Integration Testing starts from lower-level modules and gradually moves upward.

Core components such as database access, utility modules, payment connectors, shipping connectors, and calculation services are tested first. Higher-level modules that are not ready are replaced by `drivers`.

`Driver` is a temporary component that calls a lower-level module during testing.

Advantages:

- low-level modules are verified early;
- development and testing can happen in parallel;
- useful when core services are critical.

Disadvantages:

- high-level user flows are tested later;
- test drivers are required;
- key interface defects at upper levels may be found late.

### 4. Incremental Integration Testing

Incremental Integration Testing integrates modules gradually, one by one or group by group.

Testing is performed after each integration step.

Advantages:

- defects are found earlier;
- root cause is easier to identify;
- lower risk than Big Bang;
- system grows in controlled steps.

Disadvantages:

- can take more time;
- stubs and drivers may be required;
- requires discipline and planning.

### 5. Sandwich Integration Testing

Sandwich Integration Testing, or Hybrid Integration Testing, combines Top-Down and Bottom-Up approaches.

The system is divided into layers:

- upper layer;
- middle target layer;
- lower layer.

Testing starts from top and bottom layers and converges toward the middle layer.

Advantages:

- top and bottom layers can be tested in parallel;
- combines benefits of top-down and bottom-up;
- useful for layered architecture.

Disadvantages:

- planning is more complex;
- both stubs and drivers may be required;
- middle layer can become a bottleneck;
- sub-systems may not be deeply tested before final integration.

### 6. Functional Incremental Testing

Functional Incremental Testing builds integration around business functions.

Modules are integrated and tested by functional areas or user flows documented in the functional specification.

Example flows:

- user registration flow;
- search and product details flow;
- add to cart flow;
- checkout flow;
- payment and shipping flow.

This approach is useful when QA wants to see integration through real user behavior.

## How To Do Integration Testing

Typical steps:

1. Choose integration strategy: Big Bang, Top-Down, Bottom-Up, Incremental, Sandwich, or functional flow.
2. Confirm unit testing is completed for selected components.
3. Identify interfaces between modules.
4. Prepare test data and test environment.
5. Deploy selected modules together.
6. Create needed stubs or drivers.
7. Run functional integration tests.
8. Run structural/interface tests where needed.
9. Record results and defects.
10. Fix integration issues.
11. Retest and run regression checks.
12. Repeat until the complete system is integrated and tested.

### What To Test During Integration Testing

Focus areas:

- data transfer between modules;
- API request/response format;
- database updates;
- authentication and authorization between components;
- error handling;
- timeout behavior;
- retries;
- logs and audit events;
- transaction consistency;
- third-party integrations;
- file handling;
- event/message queues;
- state transitions;
- end-to-end business flow across modules.

## Unit Testing vs Integration Testing

| Unit Testing | Integration Testing |
| --- | --- |
| Verifies an individual unit/module. | Verifies interaction between modules/components. |
| Usually performed by developer. | Usually performed by QA/test team or mixed team. |
| Module is tested in isolation. | Components may depend on each other or external systems. |
| First testing level in the STLC/SDLC flow. | Performed after unit testing and before system testing. |
| Focus: code logic inside one unit. | Focus: interfaces, data flow, contracts and collaboration. |
| Bugs are usually local. | Bugs often appear at module boundaries. |

## Commands / Terms

- `Integration Testing` - testing interactions between components, modules, services or systems.
- `Interface` - boundary where two components communicate.
- `Stub` - fake lower-level component used in top-down testing.
- `Driver` - fake higher-level caller used in bottom-up testing.
- `Big Bang` - all modules integrated at once.
- `Top-Down` - testing starts from high-level modules and moves down.
- `Bottom-Up` - testing starts from low-level modules and moves up.
- `Incremental Integration` - modules integrated and tested gradually.
- `Sandwich Testing` - hybrid of top-down and bottom-up.
- `Functional Incremental Testing` - integration testing by business function or user flow.

## Questions

1. What is integration testing?
2. Why is integration testing needed after unit testing?
3. What kinds of defects can integration testing find?
4. What is Big Bang integration testing?
5. What is Top-Down integration testing?
6. What is Bottom-Up integration testing?
7. What is the difference between a stub and a driver?
8. What are the advantages of incremental integration testing?
9. How is integration testing different from unit testing?
10. What should QA check during integration testing?

## What To Review Later

- STLC levels
- Unit testing vs integration testing
- System testing
- API testing
- Contract testing
- Test environment setup
- Stubs and drivers
- End-to-end testing
