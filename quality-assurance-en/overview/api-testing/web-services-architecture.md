# Web Services Architecture For QA

Source: pasted article "What are Web Services? Architecture, Types, Example"  
Date added: 2026-06-11  
Related plan item: API Testing  
Tags: QA, API testing, web services, SOAP, WSDL, UDDI, service architecture  
Language: English  
Translation pair: quality-assurance/overview/api-testing/web-services-architecture.md

## Summary

A **web service** is a software service available over a network through a defined interface or contract. It allows different applications to exchange data and invoke operations regardless of their programming language or internal implementation.

The classic Web Services Architecture is associated with SOAP, XML, WSDL, and UDDI. The modern concept is broader: web services can also be implemented with REST, JSON, GraphQL, gRPC, and other technologies.

For QA, it is important to understand:

- who invokes the service;
- where its contract is defined;
- how messages are transported;
- which dependencies participate;
- how the service is discovered and invoked;
- which states and failures need testing.

## Key Points

- A web service exposes functionality through a network interface.
- A service provider implements and publishes the service.
- A service consumer or requestor invokes it.
- A contract defines operations, messages, and rules.
- SOAP uses structured XML messages.
- WSDL describes a SOAP service and can support client generation.
- UDDI is a classic registry standard but is uncommon in modern projects.
- Web services can communicate synchronously or asynchronously.
- Interoperability depends on precise contracts and semantics, not only data format.

## Notes

## What Is A Web Service?

A web service is a network-accessible software component that provides specific business or technical functionality.

Examples:

- payment service;
- address validation service;
- product catalog;
- authentication service;
- currency conversion;
- notification service.

A client sends a request. The service processes it directly or calls dependencies, then returns a response or publishes an asynchronous result.

## API And Web Service

The terms are related but not identical.

- An **API** is any defined interface between software components.
- A **web service** is an API available through network or web technologies.

Therefore:

> Every web service exposes an API, but not every API is a web service.

For example, a local library function has an API but is not a network service.

## Architecture Participants

### Service Provider

The provider:

- implements the service;
- publishes its endpoint and contract;
- processes requests;
- owns availability, security, and versioning.

### Service Consumer

The consumer, client, or requestor:

- finds service information;
- builds a request;
- authenticates;
- invokes an operation;
- interprets the response or error.

### Service Registry

A registry stores service metadata and discovery information.

In classic SOAP architecture, this role could be performed by a UDDI registry. Modern systems more commonly use:

- internal developer portal;
- API gateway;
- service catalog;
- DNS;
- Kubernetes service discovery;
- configuration;
- OpenAPI registry.

### Dependencies

A service may depend on:

- database;
- another service;
- queue or broker;
- cache;
- external provider;
- file storage.

The dependency chain matters to QA because a backend dependency failure may surface as an API error, timeout, or incomplete response.

## Publish, Find, And Bind

The classic model describes three actions:

1. **Publish** - the provider publishes a service description.
2. **Find** - the consumer finds a suitable service.
3. **Bind** - the consumer uses contract and endpoint information to invoke it.

In a modern project:

1. A team publishes an OpenAPI document in a developer portal.
2. A consumer discovers the API and receives credentials.
3. The client invokes the endpoint through an API gateway.

## Classic SOAP Stack

The classic web services stack contains several layers.

| Layer | Typical technology | Purpose |
| --- | --- | --- |
| Transport | HTTP/HTTPS, SMTP, TCP | Carries messages between systems. |
| Messaging | SOAP/XML | Structures requests and responses. |
| Description | WSDL/XSD | Defines operations, messages, and data types. |
| Discovery | UDDI | Publishes and discovers services. |

Not every modern web service uses this stack.

## SOAP Message

A SOAP message is an XML document with a standard structure.

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

Main parts:

- `Envelope` - root element;
- `Header` - optional metadata;
- `Body` - application message;
- `Fault` - structured error inside the Body.

QA verifies XML structure, namespaces, schema, headers, data, and Fault behavior.

## WSDL

**WSDL** (Web Services Description Language) is an XML description of a web service.

It may define:

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

**UDDI** (Universal Description, Discovery, and Integration) is a standard for publishing and discovering service metadata.

Historically, UDDI was presented as a searchable directory of web services. Public UDDI registries are uncommon in current projects, but the architectural need for service discovery remains.

QA should not assume UDDI is used. Ask:

- where the service catalog is located;
- where the current contract is stored;
- how endpoints are discovered per environment;
- who owns the service;
- how deprecated services are marked.

## SOAP And RESTful Web Services

| Area | SOAP service | RESTful service |
| --- | --- | --- |
| Interaction | Operations/messages | Resources and HTTP methods |
| Common format | XML | Usually JSON |
| Contract | WSDL/XSD | Often OpenAPI/JSON Schema |
| Errors | SOAP Fault | HTTP status + error body |
| Discovery | Historically UDDI or catalog | Developer portal, gateway, catalog |
| Typical use | Enterprise and legacy integrations | Web, mobile, and public APIs |

Both styles require contracts, security, observability, and testing.

## Synchronous And Asynchronous Communication

### Synchronous

The client waits for an immediate response.

```text
Client -> Request -> Service
Client <- Response <- Service
```

QA verifies:

- response time;
- timeout;
- correct response;
- retry behavior;
- state after failure.

### Asynchronous

The client starts an operation without waiting for final processing.

Possible patterns:

- queue/message broker;
- callback/webhook;
- polling;
- event stream;
- `202 Accepted` with a status URL.

QA verifies:

- message delivery;
- duplicate handling;
- ordering;
- eventual result;
- retry and dead-letter behavior;
- correlation IDs;
- idempotency.

## Loose Coupling

Loosely coupled systems depend on a documented contract rather than internal implementation.

This does not mean changes are harmless. Contract changes can still break consumers.

Potential breaking changes:

- removing a field or operation;
- changing a data type;
- making an optional field required;
- changing an enum;
- changing error behavior;
- moving an endpoint;
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

- WSDL points to the wrong environment;
- request is accepted despite an invalid XML schema;
- namespace mismatch breaks client parsing;
- REST documentation differs from the actual response;
- timeout leaves a transaction in an unknown state;
- asynchronous message is processed twice;
- provider changes a required field without versioning;
- service returns an internal stack trace;
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

Sanitize tokens, passwords, and personal data.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Web service | Network-accessible software functionality. |
| Provider | System that implements and exposes a service. |
| Consumer | Client that invokes a service. |
| Registry | Catalog containing service metadata. |
| SOAP | XML-based messaging protocol. |
| WSDL | Description of SOAP operations, messages, and endpoints. |
| UDDI | Standard for publishing and discovering service metadata. |
| Binding | Rules connecting an interface to a protocol and endpoint. |
| RPC | Invocation of a procedure on a remote system. |
| Loose coupling | Dependency on a stable contract instead of implementation details. |
| Service discovery | Mechanism used to locate an available service endpoint. |

## Questions

### 1. What is a web service?

Answer: A network-accessible software component that provides functionality through a defined interface or contract.

### 2. How does an API differ from a web service?

Answer: API is a broader concept. A web service is an API available through network technologies.

### 3. Which roles exist in the classic architecture?

Answer: Provider, requestor/consumer, and service registry.

### 4. What is WSDL used for?

Answer: It describes SOAP operations, messages, types, bindings, and endpoints.

### 5. Is UDDI required for a web service?

Answer: No. It is a classic discovery standard that is uncommon in modern projects.

### 6. What is important when testing an asynchronous service?

Answer: Delivery, retries, duplicates, ordering, final state, idempotency, and correlation.

## What To Review Later

- SOAP message structure.
- WSDL and XML Schema.
- REST and OpenAPI.
- Service discovery and API gateways.
- Synchronous vs asynchronous APIs.
- Mocks and service virtualization.
