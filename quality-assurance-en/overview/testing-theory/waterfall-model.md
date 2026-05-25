# Waterfall Model

## Summary

The Waterfall Model is a traditional software development methodology where work moves through fixed phases: requirements, design, development, testing, deployment, and maintenance. Each phase is expected to be completed before the next one begins.

The model is simple, structured, and predictable. It works best when requirements are clear, stable, and unlikely to change.

## Key Points

- Waterfall follows a linear, phase-by-phase process.
- Backtracking is limited and changes are difficult after a phase is completed.
- Documentation is central to the process.
- QA is most visible during testing, but quality control exists throughout the lifecycle.
- Waterfall works well for small, stable, low-risk projects.
- It is not a good fit for projects with frequent requirement changes.

## Notes

### What Is the Waterfall Model?

The Waterfall Model is a sequential software development model. The project moves downward from one phase to the next, similar to water flowing down a waterfall.

This makes the process easy to manage: every phase has clear deliverables, milestones, and approval points. The tradeoff is flexibility. If requirements are misunderstood early, fixing the problem later can be expensive.

### Main Features

**Sequential Approach** means that development follows a step-by-step flow. Requirements come before design, design comes before development, and development comes before testing.

**Document-Driven Process** means that decisions, requirements, and designs are formally documented. The team works from approved documents instead of informal assumptions.

**Quality Control** means that each phase is reviewed before moving forward.

**Detailed Planning** helps define scope, schedule, deliverables, and resources before development begins.

### Phases of the Waterfall Model

#### 1. Requirements Analysis and Specification

The team gathers and analyzes customer requirements.

The goal is to understand what must be built, remove ambiguity, and document the approved requirements.

The main output is usually the **SRS (Software Requirement Specification)**. It describes functional and non-functional requirements and acts as a formal agreement between the customer and the development team.

#### 2. Design

The requirements are converted into a technical solution.

**HLD (High-Level Design)** describes the overall architecture, major components, and interactions.

**LLD (Low-Level Design)** describes component-level logic, data flow, interfaces, and implementation details.

The main output is the **SDD (Software Design Document)**.

#### 3. Development

Developers write code based on the design documents.

Each module is implemented according to the approved plan. Developers usually perform **unit testing** to verify that individual modules work correctly.

#### 4. Testing and Deployment

After development, modules are integrated and tested together.

QA verifies that the system matches the requirements, integrations work correctly, critical defects are fixed, and the product is ready for release.

Common testing stages include:

- **Alpha Testing** - testing by the internal development team.
- **Beta Testing** - testing by selected end users.
- **Acceptance Testing** - customer validation before final approval.

After successful testing, the software is deployed to a live environment. Deployment may include environment setup, user training, final checks, and early monitoring.

#### 5. Maintenance

After release, the system is supported and improved.

Main maintenance types:

- **Corrective Maintenance** - fixes defects found after release.
- **Perfective Maintenance** - improves features based on user needs.
- **Adaptive Maintenance** - updates the product for new operating systems, hardware, browsers, APIs, or infrastructure.

### Example: Online Food Delivery System

For an Online Food Delivery System, Waterfall may look like this:

1. **Analysis** - gather requirements for user registration, restaurant listings, menus, orders, payments, delivery tracking, and support.
2. **Design** - define app architecture, database structure, UI layout, payment gateway integration, and security.
3. **Implementation** - build login, restaurant search, order processing, payment, and notification modules.
4. **Testing** - verify order placement, payment processing, delivery tracking, performance, and main user flows.
5. **Maintenance** - fix bugs, add restaurants, improve tracking, update payment methods, and improve security.

## Commands / Terms

- **Waterfall Model** - a linear software development model.
- **SRS (Software Requirement Specification)** - a document describing system requirements.
- **SDD (Software Design Document)** - a document describing architecture and design decisions.
- **HLD (High-Level Design)** - system-level design.
- **LLD (Low-Level Design)** - detailed component-level design.
- **Unit Testing** - testing individual modules.
- **Alpha Testing** - internal team testing.
- **Beta Testing** - testing by selected users.
- **Acceptance Testing** - customer approval testing.
- **Maintenance** - post-release support and improvement.

## Questions

**1. Why is Waterfall called a sequential model?**  
Because each phase is completed before the next phase begins.

**2. Why is documentation important in Waterfall?**  
Because the team works from approved requirements and design documents. Late changes are expensive.

**3. When is Waterfall a good choice?**  
When requirements are clear, stable, and well documented, and the project is predictable and low risk.

**4. What is the main disadvantage of Waterfall?**  
Low flexibility. Late requirement changes can cause major rework.

**5. What is QA's role in Waterfall?**  
QA verifies that the product meets documented requirements and helps control quality, especially during the testing phase.

## What To Review Later

- Waterfall vs. V-Model vs. Agile.
- Why late testing can increase project risk.
- Which documents QA should read in a Waterfall project.
- What acceptance criteria are and how they relate to SRS.
- Common defects caused by weak requirements analysis.
