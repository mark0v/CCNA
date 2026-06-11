# API Testing Interview Questions

Source: Postman article "API testing interview questions"  
Date added: 2026-06-11  
Related plan item: API Testing  
Tags: QA, API testing, interview, test strategy, automation, Postman  
Language: Russian  
Translation pair: quality-assurance-en/overview/api-testing/api-testing-interview-questions.md

## Summary

На собеседовании по API testing важно не только знать определения, но и уметь объяснить свой подход:

- как анализировать API contract;
- какие positive and negative checks выполнять;
- как работать с environment and test data;
- что автоматизировать;
- как тестировать errors, performance, security and dependencies;
- как поддерживать несколько API versions.

Хороший ответ обычно содержит определение, практический пример и объяснение риска.

## Key Points

- API связывает software components через определённый contract.
- Manual и automated testing дополняют друг друга.
- API testing включает functional, contract, integration, end-to-end, performance and security checks.
- Хорошая strategy начинается с requirements, contract, risks and dependencies.
- Test environment должен быть изолирован от production.
- Negative testing проверяет не только status code, но и error schema, state and security.
- Versioning требует проверки backward compatibility.
- External dependencies можно контролировать через mocks, stubs and service virtualization.
- Автоматизировать стоит стабильные, повторяемые и критичные scenarios.

## Notes

## 1. Что такое API?

**API** (Application Programming Interface) — это интерфейс и набор правил, позволяющих software systems обмениваться данными и вызывать функции друг друга.

API contract может определять:

- endpoints or operations;
- methods;
- parameters;
- request and response schemas;
- authentication;
- status codes and errors;
- limits and versioning.

Пример ответа:

> REST API интернет-магазина позволяет frontend получить каталог, создать корзину и оформить заказ через HTTP endpoints. Клиенту не нужно знать внутреннюю реализацию backend, но он должен соблюдать API contract.

## 2. Чем manual API testing отличается от automated?

**Manual testing** удобно для:

- изучения нового API;
- exploratory testing;
- быстрой проверки гипотезы;
- отладки request;
- исследования unusual response.

**Automated testing** удобно для:

- regression;
- repeated checks;
- data-driven scenarios;
- CI/CD;
- проверки множества endpoints and environments;
- раннего обнаружения contract changes.

Лучший подход обычно комбинированный: сначала исследовать API вручную, затем автоматизировать стабильные critical scenarios.

## 3. Какие бывают виды API testing?

| Вид | Что проверяет |
| --- | --- |
| Functional | Соответствует ли endpoint business requirements. |
| Contract | Соответствуют ли request and response API schema. |
| Integration | Правильно ли API взаимодействует с database and services. |
| End-to-end | Работает ли полный workflow через несколько endpoints. |
| Performance | Latency, throughput, error rate and scalability. |
| Security | Authentication, authorization, validation and data exposure. |
| Reliability | Retries, timeouts, duplicate requests and recovery. |
| Compatibility | Не ломают ли изменения существующих consumers. |

Unit tests обычно выполняются developers на уровне отдельных functions or components. QA чаще работает с deployed API и проверяет service behavior.

## 4. Как построить API testing strategy?

1. Изучить requirements and API contract.
2. Определить consumers, critical workflows and risks.
3. Составить inventory endpoints.
4. Выделить positive, negative and boundary scenarios.
5. Определить environments, roles and test data.
6. Учесть dependencies.
7. Выбрать manual and automated coverage.
8. Определить performance and security scope.
9. Согласовать entry, exit and pass/fail criteria.
10. Настроить reporting and CI/CD execution.

Для каждого endpoint полезно проверить:

- method and URL;
- parameters and body;
- authentication and authorization;
- status code;
- headers;
- response schema and values;
- database or system state;
- error handling;
- idempotency;
- response time.

## 5. Что такое API test environment?

Test environment — это комбинация:

- deployed application version;
- configuration;
- database;
- test accounts and roles;
- network;
- dependencies;
- secrets and environment variables;
- monitoring and logs.

Environment должен быть достаточно похож на production, но изолирован от real users and data.

QA должен знать:

- какая build version установлена;
- какие services mocked;
- можно ли безопасно изменять data;
- кто ещё использует environment;
- как выполнить reset or cleanup;
- какие feature flags включены.

## 6. Как тестировать errors and exceptions?

Negative scenarios:

- missing required field;
- invalid data type;
- malformed JSON or XML;
- invalid or expired token;
- forbidden operation;
- unknown resource ID;
- unsupported method;
- unsupported `Content-Type`;
- timeout or unavailable dependency;
- duplicate request.

Проверить:

- correct status code;
- stable error schema;
- useful but safe message;
- correlation ID;
- отсутствие stack trace and secrets;
- отсутствие unintended state changes;
- consistent behavior across endpoints.

## 7. Как тестировать performance and scalability?

Сначала определить workload model:

- expected users or requests per second;
- traffic distribution by endpoints;
- test duration;
- ramp-up and ramp-down;
- payload sizes;
- acceptable thresholds.

Основные metrics:

- average and percentile latency;
- throughput;
- error rate;
- CPU and memory;
- database metrics;
- saturation point;
- recovery after load.

Следует различать load, stress, spike and soak testing. Запускать нагрузку нужно только в согласованном environment.

## 8. Что такое API versioning?

Versioning позволяет изменять API, сохраняя предсказуемое поведение для consumers.

Примеры:

```text
/api/v1/users
/api/v2/users
```

Или version может передаваться через header/media type.

QA проверяет:

- behavior каждой supported version;
- backward compatibility;
- deprecated fields;
- migration path;
- documentation;
- одинаковую authentication policy;
- корректное отключение старой версии;
- отсутствие пересечения data between versions.

## 9. Что такое dynamic test data?

Dynamic test data создаётся во время test execution.

Examples:

- unique email;
- random order ID;
- current timestamp;
- generated boundary string;
- resource created in a setup request.

Преимущества:

- меньше конфликтов между runs;
- шире coverage;
- tests less dependent on fixed records;
- удобнее parallel execution.

Риски:

- невоспроизводимые failures;
- плохой cleanup;
- случайные данные без meaningful boundaries.

Для воспроизводимости сохраняйте generated values and random seed в report.

## 10. Как тестировать dependencies?

API может зависеть от:

- database;
- payment provider;
- email or SMS service;
- another internal API;
- message broker;
- file storage.

Подходы:

- real integration environment;
- mock;
- stub;
- fake;
- service virtualization;
- contract testing.

Нужно проверить не только success response dependency, но и:

- timeout;
- slow response;
- malformed response;
- authentication failure;
- rate limit;
- partial failure;
- duplicate delivery;
- temporary unavailability.

## 11. Как отвечать на вопрос о сложном случае?

Используйте структуру **STAR**:

- **Situation** — context;
- **Task** — responsibility;
- **Action** — what you investigated and changed;
- **Result** — measurable outcome.

Пример:

> После обновления payment API часть tests стала нестабильной. Я сопоставил failures с token expiration, разделил authentication setup и business requests, добавил автоматическое обновление token и assertions для error responses. Flaky failures исчезли, а collection стала стабильно запускаться в CI.

Не придумывайте production experience. Если опыта мало, опишите учебный project и объясните reasoning.

## 12. API testing best practices

- использовать отдельный test environment;
- хранить secrets вне collection and source code;
- поддерживать API contract актуальным;
- проверять response schema and business values;
- делать tests independent where possible;
- очищать созданные данные;
- использовать reusable helpers;
- разделять smoke and regression;
- добавлять negative checks;
- запускать tests в CI/CD;
- хранить requests and tests в version control;
- не проверять только status code;
- собирать logs and correlation IDs.

## 13. Какие tools используются?

Варианты:

- Postman and Newman;
- Swagger UI / OpenAPI tools;
- SoapUI / ReadyAPI;
- Insomnia;
- cURL;
- REST Assured;
- pytest with HTTP clients;
- Playwright APIRequest;
- k6 or JMeter for performance;
- WireMock or MockServer for dependencies.

На интервью лучше подробно рассказать о нескольких инструментах, которыми вы действительно пользовались.

Для Postman полезно знать:

- collections;
- environments and variables;
- pre-request scripts;
- tests;
- Collection Runner;
- chaining requests;
- data files;
- Newman;
- CI/CD integration;
- mock servers.

## Example Test Design

Endpoint:

```text
POST /api/v1/users
```

Минимальный набор scenarios:

- valid user returns `201`;
- response matches schema;
- user is saved;
- missing required field returns `400` or `422`;
- duplicate email follows business rule;
- invalid token returns `401`;
- user without permission returns `403`;
- unsupported media type returns `415`;
- oversized field is rejected;
- response does not expose password;
- duplicate retry does not create unintended records;
- response time meets agreed threshold.

## Common Interview Mistakes

- давать только определения без examples;
- путать authentication and authorization;
- утверждать, что каждый error должен возвращать `400`;
- проверять только response body;
- не учитывать system state after request;
- говорить, что все tests нужно автоматизировать;
- называть tool без объяснения, как он применялся;
- описывать performance без workload and metrics;
- забывать про cleanup and test isolation.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| API contract | Agreed structure and behavior of an API. |
| Contract testing | Verification that producer and consumer follow the contract. |
| Mock | Controlled imitation of a dependency. |
| Stub | Simplified implementation returning predefined responses. |
| Service virtualization | Simulation of dependent systems and their behavior. |
| Dynamic data | Test data generated during execution. |
| Backward compatibility | New version does not break existing consumers. |
| Correlation ID | Identifier used to trace a request across services. |
| Test isolation | A test does not depend on or damage other tests. |
| CI/CD | Automated integration and delivery pipeline. |

## Questions

### 1. Какие checks обязательны почти для каждого endpoint?

Answer: Method, URL, authentication, authorization, status, headers, schema, values, errors, state changes and response time.

### 2. Когда manual testing полезнее automation?

Answer: При изучении нового API, exploratory testing, debugging and rapidly changing requirements.

### 3. Зачем нужны mocks?

Answer: Чтобы контролировать dependencies, моделировать errors and test independently from unavailable or expensive external services.

### 4. Почему dynamic data полезна?

Answer: Она уменьшает conflicts, расширяет scenarios and supports parallel execution.

### 5. Что проверять при API versioning?

Answer: Supported versions, backward compatibility, deprecated behavior, migration and documentation.

### 6. Как сделать ответ на интервью сильнее?

Answer: Дать краткое определение, практический example, назвать risks and explain verification.

## What To Review Later

- API test strategy.
- Contract and schema testing.
- Postman collections and environments.
- Mocking and service virtualization.
- API performance metrics.
- Authentication vs authorization.
- STAR method for interview answers.
