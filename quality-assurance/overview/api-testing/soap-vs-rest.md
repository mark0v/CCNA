# SOAP vs REST для API-тестировщиков

Source: pasted articles "SOAP vs. REST: What API Testers and Developers Need to Know" and SmartBear "SOAP vs REST: What's the Difference?"  
Date added: 2026-06-11  
Related plan item: API Testing  
Tags: QA, API testing, SOAP, REST, WSDL, XML, JSON  
Language: Russian  
Translation pair: quality-assurance-en/overview/api-testing/soap-vs-rest.md

## Summary

SOAP и REST позволяют приложениям обмениваться данными, но делают это по-разному:

- **SOAP** — протокол со строгим XML-форматом сообщений и формальным контрактом WSDL.
- **REST** — архитектурный стиль, в котором данные представлены как ресурсы, а операции обычно выполняются через HTTP.

SOAP часто встречается в банковских, медицинских и корпоративных интеграциях, где важны строгие контракты, совместимость и WS-* стандарты. REST распространён в web applications, mobile applications, public APIs и microservices благодаря простоте и гибкости.

Для QA главное не решить, какой подход «лучше», а понимать контракт, формат сообщений, правила обработки ошибок и риски каждого API.

## Key Points

- SOAP является протоколом, REST — архитектурным стилем.
- SOAP-сообщения используют XML и стандартный `Envelope`.
- SOAP API обычно описывается контрактом WSDL.
- REST API чаще всего использует HTTP и JSON, но JSON не является обязательным требованием REST.
- REST-запрос должен содержать достаточно информации для обработки независимо от предыдущих запросов.
- В SOAP ошибки возвращаются как `Fault`; REST обычно использует HTTP status codes и собственную error schema.
- SOAP требует строгой проверки XML, namespaces и контракта.
- REST требует тщательной проверки ресурсов, методов, status codes, headers и response body.
- SOAP ecosystem расширяется через отдельные WS-* standards.
- WSDL может использоваться для автоматической генерации client code, поэтому часть integration bugs появляется в generated clients.

## Notes

## Что такое SOAP

SOAP расшифровывается как **Simple Object Access Protocol**. Он определяет строгую XML-структуру для обмена сообщениями между системами.

SOAP message обычно содержит:

- `Envelope` — корневой элемент;
- `Header` — дополнительные данные, например security metadata;
- `Body` — request или response payload;
- `Fault` — структурированное описание ошибки.

Пример:

```xml
<soap:Envelope
  xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
  xmlns:usr="http://example.com/users">
  <soap:Header/>
  <soap:Body>
    <usr:GetUserRequest>
      <usr:UserId>42</usr:UserId>
    </usr:GetUserRequest>
  </soap:Body>
</soap:Envelope>
```

SOAP чаще всего работает через HTTP/HTTPS, но может использовать и другие transports.

## WSDL как контракт

**WSDL** (Web Services Description Language) описывает:

- доступные operations;
- endpoint address;
- request and response messages;
- XML data types;
- bindings and transport;
- namespaces.

Для тестировщика WSDL является основным источником ожидаемого поведения SOAP service.

QA проверяет:

- соответствует ли request описанию;
- обязательны ли нужные elements;
- правильны ли types and namespaces;
- соответствует ли response контракту;
- возвращается ли ожидаемый SOAP Fault.

## Расширяемость SOAP и WS-* Standards

SOAP определяет базовый message format, а дополнительные возможности обычно предоставляются отдельными WS-* specifications.

Examples:

- **WS-Security** — signatures, encryption and security tokens;
- **WS-Addressing** — addressing information inside SOAP messages;
- **WS-Policy** — описание requirements and capabilities service;
- **WS-ReliableMessaging** — reliable message delivery;
- **WS-AtomicTransaction** — coordination of distributed transactions.

Использование SOAP не означает, что все эти возможности включены автоматически. Команда выбирает необходимые standards и настраивает их отдельно.

QA должен выяснить:

- какие WS-* standards используются;
- обязательны ли SOAP headers;
- проверяются ли timestamp, signature and message ID;
- как обрабатываются duplicate, delayed and out-of-order messages;
- что происходит при partial transaction failure.

## Generated SOAP Clients

Многие IDE and frameworks умеют читать WSDL и генерировать:

- service client;
- request and response classes;
- data types;
- serialization and parsing code;
- operation methods.

Поэтому сложность SOAP зависит не только от protocol, но и от language and tooling. В одном проекте разработчик работает с generated methods и почти не видит XML, а в другом XML формируется вручную.

QA risks:

- generated client создан из устаревшего WSDL;
- client regeneration ломает backward compatibility;
- optional field generated as required or наоборот;
- enum из schema не совпадает с service;
- namespace changes break deserialization;
- client hides useful SOAP Fault details;
- different teams use different WSDL versions.

## Что такое REST

REST расшифровывается как **Representational State Transfer**. API моделирует сущности как resources, доступные по URI.

Примеры ресурсов:

```text
GET    /users
GET    /users/42
POST   /users
PUT    /users/42
PATCH  /users/42
DELETE /users/42
```

REST API обычно использует JSON:

```json
{
  "id": 42,
  "name": "Alex",
  "active": true
}
```

REST не требует JSON или OpenAPI, но на практике они используются очень часто.

Один resource может иметь несколько representations. Например, service может возвращать JSON, XML или CSV в зависимости от `Accept` header. Если API заявляет content negotiation, QA должен проверить каждый поддерживаемый format и реакцию на unsupported media type.

## Основные ограничения REST

REST включает следующие architectural constraints:

1. Client-server.
2. Stateless.
3. Cacheable.
4. Uniform interface.
5. Layered system.
6. Code on demand — optional.

**Stateless** означает, что server не должен зависеть от контекста предыдущего запроса для обработки текущего. Authentication token или другие необходимые данные передаются с запросом.

## SOAP и REST: сравнение

| Характеристика | SOAP | REST |
| --- | --- | --- |
| Модель | Protocol | Architectural style |
| Типичная передача | HTTP/HTTPS, также возможны другие transports | Обычно HTTP/HTTPS |
| Формат | XML | Чаще JSON, возможны XML и другие formats |
| Контракт | Обычно WSDL | Часто OpenAPI, но формально не обязателен |
| Структура | Строгая | Более гибкая |
| Объект взаимодействия | Operations/messages | Resources |
| Ошибки | SOAP Fault | HTTP status code + error body |
| Размер сообщений | Обычно больше из-за XML | Обычно меньше при использовании JSON |
| Кэширование | Зависит от реализации | Поддерживается HTTP semantics |
| Типичные проекты | Enterprise, finance, healthcare, legacy | Web, mobile, public APIs, microservices |

## Сходства SOAP и REST

Несмотря на различия, оба подхода:

- обеспечивают communication between systems;
- могут работать через HTTP/HTTPS;
- требуют согласованных message and error rules;
- нуждаются в authentication, authorization and encryption;
- должны иметь contract or documentation для consumers;
- требуют functional, negative, security and performance testing.

SOAP не является автоматически надёжным, а REST не является автоматически быстрым. Реальное качество зависит от API design, payload, infrastructure, implementation and testing.

## Матрица выбора

| Вопрос | В пользу SOAP | В пользу REST |
| --- | --- | --- |
| Нужен строгий formal contract? | WSDL and XSD are central | OpenAPI can be used, but flexibility is higher |
| Нужны WS-* enterprise standards? | Strong fit | Usually implemented through separate HTTP/application mechanisms |
| Клиенты web or mobile? | Possible, but XML may add complexity | Common and convenient |
| Важен небольшой payload? | XML adds overhead | JSON or compact formats are usually smaller |
| Часто меняется API? | Contract changes require careful coordination | Easier to evolve, but consumers still need compatibility |
| Existing infrastructure already uses one style? | Existing SOAP ecosystem matters | Existing HTTP/REST ecosystem matters |
| Нужно несколько transports? | SOAP supports this model | REST is normally tied to HTTP semantics |

На практике выбор часто уже определён existing system или external provider. Задача QA в таком случае — не выбирать architecture, а понять её rules and risks.

## Что проверять в SOAP API

### Контракт

- operation существует в WSDL;
- endpoint соответствует environment;
- request соответствует XML Schema;
- обязательные elements присутствуют;
- порядок elements корректен, если schema этого требует;
- namespace and prefixes обрабатываются правильно.

### Данные

- valid and invalid types;
- missing required elements;
- empty elements;
- `xsi:nil`;
- boundary values;
- special XML characters;
- unexpected elements;
- encoding.

### Ошибки

- корректный SOAP Fault;
- `faultcode`;
- `faultstring` или `Reason`;
- fault details;
- отсутствие внутренних stack traces;
- корректный HTTP status согласно контракту и реализации.

### Security

- HTTPS;
- authentication;
- WS-Security headers, если используются;
- expired or invalid credentials;
- signature and timestamp validation;
- отсутствие secrets в logs and faults.

## Что проверять в REST API

### Resource и HTTP method

- правильный URI;
- корректная работа `GET`, `POST`, `PUT`, `PATCH`, `DELETE`;
- неподдерживаемый method;
- idempotency;
- query and path parameters;
- pagination, filtering and sorting.

### Request

- required and optional fields;
- data types;
- null and empty values;
- boundary values;
- malformed JSON;
- unsupported `Content-Type`;
- authorization headers.

### Response

- status code;
- response schema;
- field values and types;
- response headers;
- content negotiation through `Accept`;
- correct `Content-Type`;
- supported representations such as JSON, XML or CSV;
- error format;
- response time;
- absence of sensitive data.

## Ошибки SOAP и REST

SOAP Fault example:

```xml
<soap:Fault>
  <faultcode>soap:Client</faultcode>
  <faultstring>User ID is required</faultstring>
</soap:Fault>
```

REST error example:

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json
```

```json
{
  "code": "VALIDATION_ERROR",
  "message": "User ID is required"
}
```

QA должен проверять не только факт ошибки, но и consistency error contract across endpoints.

## Когда выбирают SOAP

SOAP может быть подходящим выбором, когда:

- необходим строгий formal contract;
- используются существующие enterprise systems;
- нужны WS-Security, reliable messaging или transaction standards;
- важна строгая XML schema validation;
- integration должна долго сохранять backward compatibility.

Это не означает, что SOAP автоматически безопаснее. Безопасность зависит от configuration и implementation.

## Когда выбирают REST

REST обычно подходит, когда:

- API используется web или mobile client;
- важны простота и небольшой payload;
- API публичный или предназначен для многих consumers;
- requirements часто меняются;
- применяется microservice or cloud-native architecture;
- команда использует HTTP tooling and OpenAPI.

REST также требует продуманного versioning, security и contract management.

## Инструменты

Для SOAP:

- SoapUI;
- ReadyAPI;
- Postman;
- WSDL validators;
- XML Schema validators.

Для REST:

- Postman;
- Swagger UI / OpenAPI;
- Insomnia;
- cURL;
- REST Assured;
- Newman.

## Типичные дефекты

- WSDL описывает element, который service не принимает;
- SOAP response содержит неправильный namespace;
- service возвращает обычный HTML error вместо SOAP Fault;
- REST endpoint возвращает `200 OK` для validation error;
- `PUT` обновляет только часть resource вопреки контракту;
- `DELETE` не является idempotent;
- REST response не соответствует OpenAPI schema;
- REST API игнорирует `Accept` и возвращает неправильный representation;
- unsupported media type обрабатывается непоследовательно;
- разные endpoints используют разные error formats;
- API раскрывает sensitive fields;
- authentication проверяется только на части operations.

## Bug Report Tips

Для API bug report полезно приложить:

- environment and endpoint;
- API type: SOAP or REST;
- operation or HTTP method;
- sanitized request;
- actual response;
- expected result;
- WSDL/OpenAPI version;
- headers and authentication type;
- status code or SOAP Fault;
- correlation/request ID;
- impact.

Не публикуйте реальные tokens, passwords и personal data.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| SOAP | Protocol for exchanging structured XML messages. |
| REST | Architectural style based on resources and a uniform interface. |
| WSDL | XML document describing a SOAP service contract. |
| OpenAPI | Machine-readable description commonly used for HTTP APIs. |
| Envelope | Root container of a SOAP message. |
| SOAP Fault | Standard SOAP error structure. |
| Resource | Entity exposed by a REST API through a URI. |
| Stateless | Each request carries the context needed for its processing. |
| Namespace | XML mechanism used to distinguish elements with similar names. |
| WS-Security | Standards for adding security features to SOAP messages. |
| WS-* | Family of specifications extending SOAP web services. |
| Generated client | Client code created automatically from an API contract such as WSDL. |
| Content negotiation | HTTP mechanism for selecting a response representation. |
| Representation | A particular format of a resource, such as JSON, XML or CSV. |

## Questions

### 1. В чём главное отличие SOAP от REST?

Answer: SOAP является протоколом со строгим XML message format, а REST является архитектурным стилем, обычно реализованным через HTTP resources.

### 2. Что описывает WSDL?

Answer: Operations, endpoints, request and response messages, XML types, bindings and namespaces SOAP service.

### 3. Обязан ли REST API использовать JSON?

Answer: Нет. JSON является самым распространённым форматом, но REST не требует конкретного representation format.

### 4. Что означает stateless?

Answer: Каждый request содержит достаточно информации для обработки независимо от предыдущих requests.

### 5. Как обычно представлены ошибки?

Answer: SOAP использует SOAP Fault, а REST API обычно использует HTTP status code и structured error body.

### 6. Что важнее всего проверять в SOAP?

Answer: WSDL/schema compliance, XML structure, namespaces, data types, SOAP Faults and security headers.

### 7. Что важнее всего проверять в REST?

Answer: Resources, HTTP methods, parameters, status codes, schemas, headers, authorization and error consistency.

### 8. Зачем SOAP API использует WS-* standards?

Answer: Они добавляют стандартизированные capabilities, например security, addressing, policy, reliable messaging and transactions.

### 9. Какой риск связан с generated SOAP client?

Answer: Client может быть создан из устаревшего WSDL или неправильно обрабатывать изменённые types, namespaces and faults.

## What To Review Later

- SOAP Envelope, Header, Body and Fault.
- WSDL structure and XML Schema.
- REST constraints.
- HTTP method semantics and idempotency.
- OpenAPI schema validation.
- WS-* standards and generated SOAP clients.
- HTTP content negotiation.
- SoapUI and Postman basics.
