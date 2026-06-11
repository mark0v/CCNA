# Web Services Architecture For QA

Source: pasted article "What are Web Services? Architecture, Types, Example"  
Date added: 2026-06-11  
Related plan item: API Testing  
Tags: QA, API testing, web services, SOAP, WSDL, UDDI, service architecture  
Language: Russian  
Translation pair: quality-assurance-en/overview/api-testing/web-services-architecture.md

## Summary

**Web service** — это программный сервис, доступный через сеть по определённому interface or contract. Он позволяет разным applications обмениваться данными и вызывать operations независимо от языка программирования и внутренней реализации.

Классическая Web Services Architecture связана с SOAP, XML, WSDL и UDDI. Современное понятие шире: web services также реализуются через REST, JSON, GraphQL, gRPC и другие technologies.

Для QA важно понимать:

- кто вызывает service;
- где описан contract;
- как передаются messages;
- какие dependencies участвуют;
- как service обнаруживается и вызывается;
- какие состояния и ошибки нужно проверять.

## Key Points

- Web service предоставляет functionality через network interface.
- Service provider реализует и публикует service.
- Service consumer or requestor вызывает service.
- Contract описывает operations, messages and rules.
- SOAP использует structured XML messages.
- WSDL описывает SOAP service и помогает генерировать clients.
- UDDI — классический registry standard, но в современных проектах встречается редко.
- Web services могут работать синхронно или асинхронно.
- Interoperability зависит не только от format, но и от точного contract and semantics.

## Notes

## Что такое Web Service

Web service — это network-accessible software component, предоставляющий определённую business or technical functionality.

Examples:

- payment service;
- address validation service;
- product catalog;
- authentication service;
- currency conversion;
- notification service.

Client отправляет request, service обрабатывает его самостоятельно или обращается к dependencies, затем возвращает response либо публикует asynchronous result.

## API и Web Service

Эти понятия связаны, но не полностью одинаковы.

- **API** — любой определённый interface между software components.
- **Web service** — API, доступный через network/web technologies.

Следовательно:

> Каждый web service предоставляет API, но не каждый API является web service.

Например, локальная library function имеет API, но не является network service.

## Базовые участники архитектуры

### Service Provider

Provider:

- реализует service;
- публикует endpoint and contract;
- обрабатывает requests;
- отвечает за availability, security and versioning.

### Service Consumer

Consumer, client or requestor:

- находит service information;
- формирует request;
- authenticates;
- вызывает operation;
- интерпретирует response or error.

### Service Registry

Registry хранит service metadata and discovery information.

В классической SOAP architecture эту роль мог выполнять UDDI registry. В современных systems discovery чаще реализуется через:

- internal developer portal;
- API gateway;
- service catalog;
- DNS;
- Kubernetes service discovery;
- configuration;
- OpenAPI registry.

### Dependencies

Сам service может зависеть от:

- database;
- another service;
- queue or broker;
- cache;
- external provider;
- file storage.

Для QA dependency chain важна, потому что ошибка backend dependency может проявляться как API error, timeout or incomplete response.

## Publish, Find And Bind

Классическая модель описывает три действия:

1. **Publish** — provider публикует service description.
2. **Find** — consumer находит подходящий service.
3. **Bind** — consumer использует полученную contract and endpoint information для вызова service.

В современном проекте это может выглядеть так:

1. Team публикует OpenAPI document в developer portal.
2. Consumer находит API и получает credentials.
3. Client вызывает endpoint через API gateway.

## Классический SOAP Stack

Классический web services stack включает несколько уровней.

| Layer | Typical technology | Purpose |
| --- | --- | --- |
| Transport | HTTP/HTTPS, SMTP, TCP | Передача messages между systems. |
| Messaging | SOAP/XML | Структура request and response. |
| Description | WSDL/XSD | Operations, messages and data types. |
| Discovery | UDDI | Publication and discovery of services. |

Не каждый современный web service использует этот stack.

## SOAP Message

SOAP message — XML document со стандартной структурой.

```xml
<soap:Envelope
  xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
  xmlns:cat="http://example.com/catalog">
  <soap:Header/>
  <soap:Body>
    <cat:GetProductRequest>
      <cat:ProductId>101</cat:ProductId>
    </cat:GetProductRequest>
  </soap:Body>
</soap:Envelope>
```

Основные части:

- `Envelope` — root element;
- `Header` — optional metadata;
- `Body` — application message;
- `Fault` — structured error inside Body.

QA проверяет XML structure, namespaces, schema, headers, data and Fault behavior.

## WSDL

**WSDL** (Web Services Description Language) — XML description of a web service.

WSDL может описывать:

- messages;
- operations;
- input and output;
- port types or interfaces;
- bindings;
- transport;
- service endpoints.

Simplified example:

```xml
<definitions>
  <message name="ProductRequest">
    <part name="productId" type="xsd:string"/>
  </message>

  <portType name="CatalogPortType">
    <operation name="GetProduct">
      <input message="tns:ProductRequest"/>
      <output message="tns:ProductResponse"/>
    </operation>
  </portType>
</definitions>
```

Real WSDL documents also include namespaces and related schemas.

QA uses WSDL to verify:

- available operations;
- endpoint address;
- required fields;
- data types;
- message direction;
- binding and protocol;
- contract changes.

## UDDI

**UDDI** (Universal Description, Discovery, and Integration) — standard for publishing and discovering service metadata.

Historically, UDDI was presented as a searchable directory of web services. In current projects public UDDI registries are uncommon, but the architectural need for service discovery remains.

QA should not assume UDDI is used. Instead ask:

- where is service catalog;
- where is the current contract;
- how are endpoints discovered per environment;
- who owns the service;
- how are deprecated services marked.

## SOAP And RESTful Web Services

| Area | SOAP service | RESTful service |
| --- | --- | --- |
| Interaction | Operations/messages | Resources and HTTP methods |
| Common format | XML | Usually JSON |
| Contract | WSDL/XSD | Often OpenAPI/JSON Schema |
| Errors | SOAP Fault | HTTP status + error body |
| Discovery | Historically UDDI or catalog | Developer portal, gateway, catalog |
| Typical use | Enterprise and legacy integrations | Web, mobile and public APIs |

Both styles require contract, security, observability and testing.

## Synchronous And Asynchronous Communication

### Synchronous

Client waits for immediate response.

```text
Client -> Request -> Service
Client <- Response <- Service
```

QA checks:

- response time;
- timeout;
- correct response;
- retry behavior;
- state after failure.

### Asynchronous

Client starts operation without waiting for final processing.

Possible patterns:

- queue/message broker;
- callback/webhook;
- polling;
- event stream;
- `202 Accepted` with status URL.

QA checks:

- message delivery;
- duplicate handling;
- ordering;
- eventual result;
- retry and dead-letter behavior;
- correlation IDs;
- idempotency.

## Loose Coupling

Loosely coupled systems depend on documented contract rather than internal implementation.

This does not mean changes are harmless. Contract changes can still break consumers.

Potential breaking changes:

- removing field or operation;
- changing data type;
- making optional field required;
- changing enum;
- changing error behavior;
- moving endpoint;
- changing authentication.

QA should include compatibility and consumer-impact checks.

## RPC And Document Styles

Some services are operation-oriented:

```text
CalculatePrice(customerId, productId)
```

Others exchange business documents:

```text
PurchaseOrder
Invoice
ShippingNotice
```

Document exchange is common in enterprise integrations where message schemas represent complete business records.

QA focus:

- required document sections;
- schema and business validation;
- duplicate documents;
- document version;
- partial processing;
- audit trail.

## What To Test

### Contract

- operation or endpoint exists;
- request/response matches schema;
- required fields;
- types and formats;
- backward compatibility;
- documentation matches implementation.

### Communication

- correct transport;
- TLS;
- headers;
- encoding;
- content type;
- timeout;
- retry;
- message size limits.

### Functionality

- positive scenarios;
- negative scenarios;
- boundary values;
- business rules;
- state changes;
- idempotency.

### Dependencies

- unavailable database;
- slow external service;
- invalid dependency response;
- queue delay;
- partial failure;
- cache inconsistency.

### Security

- authentication;
- authorization;
- sensitive data;
- injection;
- secrets in errors;
- rate limiting;
- replay protection where required.

### Observability

- correlation ID;
- logs;
- metrics;
- audit events;
- alerts;
- trace across services.

## Typical Defects

- WSDL points to wrong environment;
- request accepted despite invalid XML schema;
- namespace mismatch breaks client parsing;
- REST documentation differs from actual response;
- timeout leaves transaction in unknown state;
- asynchronous message is processed twice;
- provider changes required field without versioning;
- service returns internal stack trace;
- dependency failure is incorrectly returned as success;
- correlation ID is lost between services.

## Bug Report Tips

Include:

- service and operation/endpoint;
- environment and build;
- contract version;
- request and response;
- transport and headers;
- expected and actual behavior;
- dependency state;
- timestamps;
- correlation ID;
- business impact.

Sanitize tokens, passwords and personal data.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Web service | Network-accessible software functionality. |
| Provider | System that implements and exposes a service. |
| Consumer | Client that invokes a service. |
| Registry | Catalog containing service metadata. |
| SOAP | XML-based messaging protocol. |
| WSDL | Description of SOAP operations, messages and endpoints. |
| UDDI | Standard for publishing and discovering service metadata. |
| Binding | Rules connecting an interface to a protocol and endpoint. |
| RPC | Invocation of a procedure on a remote system. |
| Loose coupling | Dependency on a stable contract instead of implementation details. |
| Service discovery | Mechanism used to locate an available service endpoint. |

## Questions

### 1. Что такое web service?

Answer: Network-accessible software component, который предоставляет functionality через defined interface or contract.

### 2. Чем API отличается от web service?

Answer: API — более широкое понятие. Web service является API, доступным через network technologies.

### 3. Какие роли есть в классической architecture?

Answer: Provider, requestor/consumer and service registry.

### 4. Для чего нужен WSDL?

Answer: Для описания SOAP operations, messages, types, bindings and endpoints.

### 5. Обязателен ли UDDI для web service?

Answer: Нет. Это классический discovery standard, который редко используется в современных проектах.

### 6. Что важно тестировать в asynchronous service?

Answer: Delivery, retries, duplicates, ordering, final state, idempotency and correlation.

## What To Review Later

- SOAP message structure.
- WSDL and XML Schema.
- REST and OpenAPI.
- Service discovery and API gateways.
- Synchronous vs asynchronous APIs.
- Mocks and service virtualization.
