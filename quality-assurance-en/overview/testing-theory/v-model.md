# V-Model

## Summary

The V-Model is a software development and testing model where each development phase has a corresponding testing phase. It is also known as the **Verification and Validation model**.

The model looks like the letter `V`: the left side represents analysis and design activities, the bottom represents coding, and the right side represents testing levels. The main idea is that testing is planned early instead of starting only after development is complete.

## Key Points

- The V-Model extends Waterfall and reduces the risk of late defect discovery.
- Each development phase is paired with a testing phase.
- Requirements are connected to tests through traceability.
- Testing activities start early in the lifecycle.
- The model works well for stable requirements, compliance, and safety-critical systems.
- It is less flexible than Agile and does not handle frequent requirement changes well.

## Notes

### What Is the V-Model?

The V-Model is a structured software development methodology where development and testing are directly connected.

In Waterfall, testing often appears late, after implementation. The V-Model addresses this weakness by planning testing activities alongside requirements analysis and design. This helps teams detect defects earlier and understand how each part of the system will be verified.

### Why the V-Model Exists

The main problem with Waterfall is late testing. If a requirement or design defect is found only after coding, fixing it can be expensive.

Common Waterfall risks include:

- defects are discovered too late;
- requirements are not validated early enough;
- defect-fixing cost increases near the end of the lifecycle;
- the final product may not match user expectations.

The V-Model reduces these risks because every development stage is connected to a validation activity.

### Verification and Validation

**Verification** asks: "Are we building the product correctly?"  
It checks requirements, design documents, architecture, modules, and compliance with standards.

**Validation** asks: "Are we building the right product?"  
It checks working software against requirements, user expectations, and business goals.

### Left Side of the V: Verification Phase

#### 1. Business Requirement Analysis

The team gathers and documents functional and non-functional requirements.

Business analysts and stakeholders clarify expectations, constraints, business goals, and acceptance criteria. QA can already help by finding ambiguity, missing requirements, and contradictions.

#### 2. System Design

System Design converts requirements into a high-level technical solution.

Architects define the overall system structure, including software components, hardware requirements, network infrastructure, integrations, and deployment approach.

#### 3. Architectural Design / High-Level Design

Architectural Design, or HLD, breaks the system into major modules and components.

This level defines patterns, frameworks, interfaces, and interactions between application parts.

#### 4. Module Design / Low-Level Design

Module Design, or LLD, describes individual components in detail.

It includes algorithms, data flow, database design, API specifications, and module logic. Unit test cases can also be planned at this level.

#### 5. Coding

Coding sits at the bottom of the V.

Developers implement modules according to design documents, coding standards, and best practices. Code reviews, static analysis, and continuous integration help control quality before full testing begins.

### Right Side of the V: Validation Phase

#### 1. Unit Testing

Unit Testing verifies individual modules or components in isolation.

This level maps to Module Design. The goal is to confirm that each small part works correctly on its own.

#### 2. Integration Testing

Integration Testing verifies that modules work together correctly.

This level maps to Architectural Design. Teams check interfaces, API calls, data flow, database interactions, and message passing.

#### 3. System Testing

System Testing verifies the fully integrated system.

This level maps to System Design. It covers functional and non-functional requirements such as performance, security, usability, compatibility, and stability.

#### 4. User Acceptance Testing

UAT verifies that the system is ready for business use.

This level maps to Business Requirement Analysis. Customers or business users validate real workflows, business scenarios, and expected outcomes.

### Phase Mapping

In the V-Model, each development phase has a matching testing phase:

- **Requirements** ↔ **Acceptance Testing**
- **System Design** ↔ **System Testing**
- **Architecture Design** ↔ **Integration Testing**
- **Module Design** ↔ **Unit Testing**

This creates traceability: the team can see which tests cover each requirement or design decision.

### Principles of the V-Model

**Large to Small** - requirements move from high-level to detailed, while testing mirrors this from unit level back to acceptance level.

**Traceability** - every requirement should map to test cases.

**Early Testing** - testing activities begin before coding.

**Documentation Focus** - each stage produces artifacts for review and reference.

**Scalability** - the model can work for small or large projects when requirements are stable.

### Advantages

- detects defects earlier;
- reduces rework cost;
- creates a clear link between requirements and tests;
- improves communication between developers, testers, and stakeholders;
- works well for compliance-heavy projects;
- fits safety-critical systems.

### Disadvantages

- rigid and inflexible;
- late changes are expensive;
- not ideal for complex iterative projects;
- depends on stable requirements;
- requires significant documentation and planning;
- less adaptive than Agile.

### V-Model vs Agile

The V-Model emphasizes structured phases, documentation, verification, and validation. Agile emphasizes iteration, fast feedback, and changing requirements.

The V-Model is better when requirements are stable, compliance is mandatory, and the cost of failure is high. Agile is better when the product changes often, customer collaboration is frequent, and releases must happen quickly.

In practice, teams sometimes combine both approaches: they keep V-Model traceability and formal testing while using automation, CI, and short feedback loops from Agile and DevOps.

### Where the V-Model Is Used

The V-Model is common where reliability, documentation, and quality control matter:

- healthcare software;
- banking and finance systems;
- aviation and aerospace;
- automotive embedded systems;
- safety-critical systems;
- regulated enterprise applications.

## Commands / Terms

- **V-Model** - a development model where each development phase has a matching testing phase.
- **Verification** - checking that the product is being built correctly.
- **Validation** - checking that the right product is being built.
- **Traceability** - linking requirements to test cases.
- **Unit Testing** - testing individual modules.
- **Integration Testing** - testing module interactions.
- **System Testing** - testing the full system.
- **UAT (User Acceptance Testing)** - acceptance testing by users or customers.
- **HLD (High-Level Design)** - high-level system design.
- **LLD (Low-Level Design)** - detailed module design.

## Questions

**1. Why is the V-Model called the Verification and Validation model?**  
Because the left side focuses on verification and the right side focuses on validation through matching test levels.

**2. Which Waterfall problem does the V-Model address?**  
It reduces late testing risk because tests are planned during requirements and design phases.

**3. What are the main phase pairs in the V-Model?**  
Requirements ↔ Acceptance Testing, System Design ↔ System Testing, Architecture Design ↔ Integration Testing, Module Design ↔ Unit Testing.

**4. When is the V-Model a good fit?**  
When requirements are stable, the project is regulated, and documentation, traceability, and reliability are important.

**5. Why is the V-Model weak for fast-changing projects?**  
Because it is rigid: changing requirements after the process starts can require expensive rework in documents, design, and test cases.

## What To Review Later

- Difference between verification and validation.
- V-Model vs Waterfall.
- V-Model vs Agile.
- Traceability matrix.
- Test levels: unit, integration, system, acceptance.
- Role of QA during requirements review.
