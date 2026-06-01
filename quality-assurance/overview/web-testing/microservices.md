# Microservices

## Summary

Microservices - это architectural style, где приложение строится как набор небольших independent services.

Каждый microservice обычно:

- отвечает за одну business capability;
- имеет well-defined interface;
- может deploy independently;
- может иметь свой data store;
- общается с другими services через lightweight protocols, часто HTTP/REST или messaging.

Для QA microservices важны, потому что bug может находиться не в одном приложении, а на границе между services:

- wrong request;
- wrong response;
- timeout;
- version mismatch;
- failed dependency;
- inconsistent data;
- cascading failure.

Главная мысль:

> В microservices QA тестирует не только отдельную feature, но и цепочку взаимодействий между services.

## What Are Microservices?

Microservices - это подход, при котором большое приложение разбивается на маленькие services.

Каждый service решает свою задачу и может развиваться отдельно.

Пример eCommerce application:

- Search service;
- Product catalog service;
- Review and rating service;
- Cart service;
- Payment service;
- Order service;
- Notification service.

Вместо одного большого application package система состоит из набора smaller units.

## Monolithic Architecture

Monolithic architecture - это подход, где все основные части приложения собраны в один deployable unit.

В monolith обычно вместе находятся:

- UI или web layer;
- business logic;
- integrations;
- data access logic;
- modules for different features.

Пример eCommerce monolith:

```text
One application:
- Search
- Reviews
- Payments
- Orders
- Users
```

Когда developer deploys monolith, deploy идет как единый package.

Чтобы scale приложение, часто приходится запускать additional instances всего приложения, даже если нагрузка выросла только на Search.

## Microservice Architecture

Microservice architecture делит систему на autonomous services.

Пример:

```text
Search Service
Review Service
Payment Service
Order Service
Notification Service
```

Каждый service:

- имеет focused responsibility;
- communicates with other services through APIs or messages;
- can be deployed separately;
- can be owned by small team;
- can use its own database or data model.

В eCommerce example Search может масштабироваться отдельно от Payments, потому что users чаще ищут товары, чем оплачивают заказы.

## Microservices Vs Monolith

| Microservices | Monolithic Architecture |
| --- | --- |
| Application split into small services. | Application packaged as one large unit. |
| Each service focuses on specific business capability. | One codebase covers many business goals. |
| Services can be deployed independently. | Whole application is usually deployed together. |
| Fault isolation is easier. | One broken module can affect the whole application. |
| Services can scale independently. | Scaling often means scaling the whole application. |
| Different services may use different technologies. | Technology stack is usually more uniform. |
| Data can be federated across services. | Data is often centralized. |
| Monitoring is more complex. | Monitoring can be simpler because system is centralized. |

Neither approach is automatically better. Microservices solve some problems, but they also introduce distributed system complexity.

## Communication Between Microservices

Microservices must communicate with each other.

Common communication styles:

- synchronous HTTP/REST;
- gRPC;
- asynchronous messaging;
- event streaming;
- queues.

Example order flow:

```text
Frontend -> Order Service
Order Service -> Payment Service
Order Service -> Inventory Service
Order Service -> Notification Service
```

For QA, this means a single user action may trigger several internal calls.

If final result is wrong, QA needs to inspect the chain, not only the screen.

## Stateless And Stateful Services

## Stateless Service

Stateless service does not store request-specific state between requests.

Each request contains enough information to be processed independently.

Advantages:

- easier scaling;
- easier replacement;
- easier load balancing.

Example:

An API service receives token, validates request and returns response without storing session state locally.

## Stateful Service

Stateful service keeps some state between requests.

Examples:

- database service;
- session storage;
- shopping cart service if cart state is stored inside service;
- cache service.

Stateful services require more careful testing around persistence, failover and data consistency.

## Data In Microservices

In microservices, each service often owns its own data.

Example:

- Payment service owns payment data;
- Order service owns order data;
- Product service owns product catalog;
- Review service owns reviews.

This helps services stay independent, but creates testing challenges:

- data duplication;
- eventual consistency;
- synchronization problems;
- reporting across services;
- migrations per service;
- test data preparation.

Important:

> In microservices, "saved successfully" in one service does not always mean the whole business process completed everywhere.

## Benefits Of Microservices

## Independent Deployment

Teams can deploy one service without redeploying the whole system.

QA impact:

- regression scope can be more focused;
- compatibility with other services must still be checked;
- versioning becomes important.

## Fault Isolation

If one service fails, other services may continue working.

Example:

If Review service is down, product browsing and payment may still work.

QA impact:

- test graceful degradation;
- check fallback behavior;
- verify user-friendly error messages.

## Scalability

Services can scale independently.

Example:

Search service can receive more resources than Payment service if search traffic is higher.

QA impact:

- performance testing may target specific services;
- load testing should check bottlenecks in service chains.

## Team Autonomy

Small teams can own services end to end.

QA impact:

- test ownership may be distributed;
- contracts between teams become critical;
- documentation and API agreements matter.

## Technology Flexibility

Different services may use different languages, frameworks or databases.

QA impact:

- test environments are more complex;
- logs and monitoring may differ per service;
- debugging requires cross-service visibility.

## Challenges Of Microservices

Microservices introduce serious complexity.

Common challenges:

- many services to monitor;
- distributed logs;
- network latency;
- timeouts;
- retries;
- duplicated data;
- service version mismatch;
- cascading failures;
- complicated deployments;
- hard-to-reproduce bugs;
- more infrastructure cost;
- need for skilled teams.

In monolith, function call is local.

In microservices, the same business flow may cross network, authentication, serialization, service discovery, database and message broker.

## Cascading Failure

Cascading failure happens when one failing service causes other services to fail.

Example:

```text
Payment Service is slow
Order Service waits too long
Frontend waits for Order Service
User retries several times
System creates duplicate pressure
```

QA should test:

- timeout behavior;
- retry behavior;
- duplicate request handling;
- fallback response;
- partial failure scenarios.

## SOA Vs Microservices

SOA, Service-Oriented Architecture, and microservices are related but not identical.

| SOA | Microservices |
| --- | --- |
| Often larger enterprise services. | Smaller focused services. |
| May use centralized service registry or ESB. | Prefer lightweight communication and independent services. |
| Services may perform multiple business tasks. | Each service usually focuses on one business capability. |
| More centralized governance. | More team autonomy. |
| Can be more cost-effective in some enterprise setups. | Can be more expensive operationally. |

Simple idea:

> Microservices can be seen as a more lightweight and independently deployable style of service-oriented design.

## Tools Around Microservices

## Docker

Docker packages an application and its dependencies into containers.

Why it matters:

- services can run consistently across environments;
- local and CI testing becomes easier;
- deployment is more predictable.

## WireMock

WireMock is used for stubbing and mocking HTTP services.

Why it matters:

- QA/dev can test one service when another service is unavailable;
- negative responses can be simulated;
- contract-like behavior can be checked.

## Circuit Breakers

Circuit breaker tools help prevent cascading failures.

Old example from Java ecosystem:

- Hystrix.

Modern systems may use other libraries, service mesh features or gateway-level resilience.

Idea:

If dependency is failing, stop calling it for a while and return fallback faster.

## Best Practices

Common microservices practices:

- keep each service focused on one business capability;
- define clear API contracts;
- use separate data store per service when appropriate;
- keep services loosely coupled;
- automate builds and deployments;
- use centralized logging and tracing;
- monitor health and performance;
- test failure scenarios;
- version APIs carefully;
- avoid sharing database tables directly between services.

## What QA Should Test

## Service Contract

Check:

- request schema;
- response schema;
- required fields;
- optional fields;
- error format;
- backward compatibility.

Contract changes are one of the most common sources of integration bugs.

## Service Integration

Check:

- service A sends correct request to service B;
- service B handles valid and invalid data;
- status codes and error messages are correct;
- retries do not create duplicates;
- timeouts are handled.

## End-To-End Business Flow

Check complete user flows:

- registration;
- login;
- search;
- add to cart;
- checkout;
- payment;
- notification.

End-to-end testing is important, but should not be the only testing layer because E2E tests can be slow and fragile.

## Observability

Check whether the system gives enough diagnostic information:

- logs;
- correlation IDs;
- traces;
- metrics;
- meaningful error messages;
- service health status.

Without observability, microservice bugs become painful to investigate.

## Failure Scenarios

Test what happens when:

- dependency is down;
- dependency is slow;
- dependency returns `500`;
- message queue is delayed;
- database is temporarily unavailable;
- one service has old API version;
- duplicate request is sent.

## Data Consistency

Check:

- order status across services;
- payment status synchronization;
- inventory updates;
- duplicate event handling;
- eventual consistency delay;
- rollback or compensation behavior.

## Example Bug Investigation

Bug:

```text
User paid for order, but order status still shows Pending.
```

QA investigation:

1. Did Frontend send checkout request?
2. Did Order Service create order?
3. Did Payment Service process payment?
4. Did Payment Service send event or callback?
5. Did Order Service receive payment confirmation?
6. Is there a delay due to asynchronous processing?
7. Did UI refresh from correct source?
8. Are logs connected by correlation ID?

In microservices, this bug may involve multiple services and asynchronous events.

## Common Mistakes

Common mistakes:

- testing only UI and ignoring service chain;
- assuming service response means full business process is complete;
- not testing timeouts;
- not checking retries;
- not checking duplicate requests;
- ignoring backward compatibility;
- not using mocks/stubs for unavailable services;
- not checking logs and correlation IDs;
- relying only on end-to-end tests;
- sharing one database between services without clear ownership.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Microservice | Small independent service focused on a business capability. |
| Monolith | Application packaged and deployed as one large unit. |
| Service contract | Agreement about request/response structure and behavior. |
| Loose coupling | Services can change with minimal impact on each other. |
| API gateway | Entry point that routes requests to internal services. |
| Eventual consistency | Data becomes consistent after some delay. |
| Circuit breaker | Pattern that prevents repeated calls to failing dependency. |
| Container | Packaged runtime unit for an application/service. |
| Docker | Tool for building and running containers. |
| WireMock | Tool for stubbing/mocking HTTP services. |
| Correlation ID | ID used to trace one request across multiple services. |
| Cascading failure | Failure that spreads from one service to others. |
| Stateless service | Service that does not keep request-specific state between requests. |
| Stateful service | Service that keeps or depends on state. |

## Questions

### 1. What are microservices?

Microservices are small independent services that together form an application and usually focus on separate business capabilities.

### 2. How is microservice architecture different from monolithic architecture?

Monolith is deployed as one large unit. Microservices are split into independently deployable services.

### 3. Why can microservices be easier to scale?

Because each service can be scaled independently based on its own load.

### 4. Why are microservices harder to test?

Because bugs can appear in service communication, data synchronization, timeouts, retries, version mismatch and distributed workflows.

### 5. What is a service contract?

It is an agreement about how a service API behaves, including request fields, response fields, status codes and errors.

### 6. What is cascading failure?

It is a situation where failure of one service causes failures or overload in other services.

### 7. Why are correlation IDs useful?

They help trace one user request across multiple services in logs and monitoring tools.

### 8. What should QA check when a dependency service is down?

QA should check timeout handling, fallback behavior, error messages, retries and whether the system avoids duplicate or corrupted data.

## What To Review Later

- API Testing
- Contract Testing
- Integration Testing
- Distributed Systems
- Docker
- Message Queues
- Observability
- Circuit Breaker Pattern
