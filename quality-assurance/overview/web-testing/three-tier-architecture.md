# Three-Tier Architecture

## Summary

Three-tier architecture is a software application architecture that separates an application into three logical and physical tiers:

- presentation tier;
- application tier;
- data tier.

For QA, this architecture is important because it helps understand where a bug can live:

- in the UI;
- in business logic;
- in API or backend processing;
- in the database;
- in communication between tiers.

When QA understands the tiers, testing becomes more precise.

## What Is Three-Tier Architecture?

Three-tier architecture organizes an application into three separate parts.

Each tier has its own responsibility and can often run on separate infrastructure.

The three tiers are:

| Tier | Main Responsibility |
| --- | --- |
| Presentation tier | User interface and user interaction |
| Application tier | Business logic and processing |
| Data tier | Data storage and management |

The main benefit is separation of responsibilities.

Each tier can be developed, scaled, updated, and tested more independently.

## Presentation Tier

The presentation tier is the user interface of the application.

This is where the user interacts with the system.

Examples:

- web page;
- mobile application screen;
- desktop application UI;
- graphical user interface.

For web applications, the presentation tier is usually built with:

- HTML;
- CSS;
- JavaScript;
- frontend frameworks.

## What Presentation Tier Does

The presentation tier:

- displays information to the user;
- collects user input;
- validates simple UI behavior;
- sends user actions to the application tier;
- shows results, messages, and errors.

Example:

User enters login and password on a login page.

The UI collects that data and sends it to the backend.

## QA Focus In Presentation Tier

QA should check:

- layout;
- forms;
- buttons;
- validation messages;
- responsiveness;
- browser compatibility;
- accessibility;
- UI state changes;
- error messages;
- client-side behavior.

Typical bugs:

- button does not work;
- text does not fit;
- validation message is missing;
- page breaks on mobile;
- wrong error is shown;
- UI sends incorrect request payload.

## Application Tier

The application tier is also called:

- logic tier;
- middle tier;
- backend tier.

This tier contains the business logic.

It processes information from the presentation tier and communicates with the data tier.

Examples of technologies:

- Python;
- Java;
- PHP;
- Ruby;
- Node.js;
- C#;
- backend frameworks and services.

## What Application Tier Does

The application tier:

- validates business rules;
- processes user input;
- calculates results;
- applies permissions;
- handles API requests;
- creates, updates, or deletes data;
- communicates with databases and external services.

Example:

When a user places an order, the application tier checks product availability, applies discounts, calculates taxes, creates the order, and asks the payment service to process payment.

## QA Focus In Application Tier

QA should check:

- business rules;
- API behavior;
- request and response structure;
- authorization logic;
- calculations;
- error handling;
- integration with external services;
- data processing;
- backend validation.

Typical bugs:

- wrong discount calculation;
- user can access another user's data;
- API returns incorrect status code;
- backend accepts invalid data;
- duplicate order is created;
- error is not handled correctly.

## Data Tier

The data tier is where application data is stored and managed.

It can include:

- relational databases;
- NoSQL databases;
- file storage;
- cache;
- data warehouses.

Examples:

- PostgreSQL;
- MySQL;
- MariaDB;
- Oracle;
- Microsoft SQL Server;
- MongoDB;
- Cassandra;
- CouchDB.

## What Data Tier Does

The data tier:

- stores data;
- retrieves data;
- updates records;
- manages relationships;
- enforces constraints;
- supports queries;
- protects data consistency.

Example:

After an order is created, order details are stored in the database.

## QA Focus In Data Tier

QA should check:

- data is saved correctly;
- data is updated correctly;
- data is not duplicated;
- deleted data behaves as expected;
- database constraints work;
- data integrity is preserved;
- migration does not corrupt data;
- reports use correct data.

Typical bugs:

- record is not saved;
- wrong user data is returned;
- duplicate rows appear;
- status is not updated;
- deleted item still appears;
- report uses outdated data.

## Communication Between Tiers

In a three-tier application, all communication should normally go through the application tier.

The presentation tier should not directly talk to the data tier.

Typical flow:

```text
User Interface -> Application Tier -> Data Tier
Data Tier -> Application Tier -> User Interface
```

This matters because direct UI-to-database communication would create security, maintainability, and scalability problems.

## Web Development Mapping

In web development, the tiers often look like this:

| Architecture Tier | Web Example |
| --- | --- |
| Presentation tier | Browser, web page, frontend app |
| Application tier | Application server, API, backend service |
| Data tier | Database server |

Example eCommerce flow:

1. User adds product to cart in the browser.
2. Frontend sends request to backend.
3. Backend checks inventory and pricing.
4. Backend reads or writes data in database.
5. Backend sends response to frontend.
6. UI updates cart state.

## Benefits

## Faster Development

Different teams can work on different tiers at the same time.

Example:

- frontend team builds UI;
- backend team builds API;
- database team works on schema and queries;
- QA prepares tests for each tier.

## Scalability

Each tier can be scaled independently.

Example:

If UI traffic grows, web servers can be scaled.

If database load grows, database resources can be optimized separately.

## Reliability

A problem in one tier may not immediately break everything else if the system is designed well.

Example:

If a reporting service has issues, login may still work.

## Security

The application tier can act as a control point.

It can:

- validate input;
- check permissions;
- block direct database access;
- reduce SQL injection risk;
- enforce business rules.

The presentation tier and data tier should not communicate directly.

## Tiers Vs Layers

The words tier and layer are often used as if they mean the same thing, but they are different.

## Layer

A layer is a logical division in software design.

Example:

- UI layer;
- business logic layer;
- data access layer.

Layers can exist inside one application running on one machine.

## Tier

A tier is a physical or infrastructure-level separation.

Example:

- web server;
- application server;
- database server.

Each tier can run on separate infrastructure.

## Why The Difference Matters

Layers organize code.

Tiers organize runtime deployment.

Example:

A mobile contacts app may have UI, logic, and data layers, but if all of them run on the phone, it is not a three-tier application.

## Two-Tier Architecture

Two-tier architecture usually has:

- presentation tier;
- data tier.

Business logic may live in the client, in the database, or partly in both.

In two-tier architecture, the client often has direct access to the data tier.

Example:

A simple desktop application that connects directly to a database.

## N-Tier Architecture

N-tier architecture means an application has more than one tier.

In practice, it often refers to systems with three or more tiers.

Additional tiers can include:

- API gateway;
- caching tier;
- message queue;
- authentication service;
- reporting service;
- microservices layer.

More tiers can improve separation, but they can also add complexity and latency.

## How This Helps QA

Three-tier architecture helps QA localize defects.

When something fails, ask:

- Is the UI sending correct data?
- Is the API receiving the request?
- Is business logic processing correctly?
- Is the database storing correct values?
- Is the response correct?
- Is the UI displaying the response correctly?

This turns vague bug reports into focused investigation.

## Example Bug Investigation

Bug:

```text
User applies discount code, but total price is wrong.
```

QA can check:

1. Presentation tier: Did frontend send the discount code?
2. Application tier: Did backend apply correct business rules?
3. Data tier: Is discount configuration correct in database?
4. Response: Did backend return correct total?
5. UI: Did frontend display returned total correctly?

This tier-based thinking helps identify the real source of the defect.

## Common Testing Areas

| Tier | Testing Focus |
| --- | --- |
| Presentation | UI, forms, layout, validation, browser compatibility |
| Application | API, business rules, authorization, calculations |
| Data | persistence, integrity, queries, migrations |
| Communication | request/response, status codes, payloads, timeouts |

## Common Mistakes

Common mistakes:

- testing only UI and ignoring backend behavior;
- assuming every UI bug is a frontend bug;
- not checking request payloads;
- not checking database state;
- not testing error handling between tiers;
- ignoring authorization in the application tier;
- not testing data consistency after updates.

## Key Idea

Three-tier architecture separates UI, business logic, and data storage.

For QA, this separation makes testing and debugging much clearer.

Главная мысль:

> When you understand the tiers, you can test the system instead of just clicking the screen.

## Questions

1. What are the three tiers in three-tier architecture?
2. What does the presentation tier do?
3. What does the application tier do?
4. Why should the presentation tier not talk directly to the data tier?
5. What is the difference between layer and tier?

## What To Review Later

- Client-Server Architecture
- API Testing
- HTTP
- Database Testing
- DevTools Network Tab
- Authorization
