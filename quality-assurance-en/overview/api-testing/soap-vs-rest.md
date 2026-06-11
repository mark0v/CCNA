# SOAP vs REST For API Testers

Source: pasted articles "SOAP vs. REST: What API Testers and Developers Need to Know" and SmartBear "SOAP vs REST: What's the Difference?"  
Date added: 2026-06-11  
Related plan item: API Testing  
Tags: QA, API testing, SOAP, REST, WSDL, XML, JSON  
Language: English  
Translation pair: quality-assurance/overview/api-testing/soap-vs-rest.md

## Summary

SOAP and REST both allow applications to exchange data, but they use different models:

- **SOAP** is a protocol with a strict XML message format and a formal WSDL contract.
- **REST** is an architectural style that represents data as resources and commonly uses HTTP for operations.

SOAP is often found in banking, healthcare, and enterprise integrations where strict contracts, compatibility, and WS-* standards matter. REST is common in web applications, mobile applications, public APIs, and microservices because it is simple and flexible.

For QA, the goal is not to decide which approach is universally better. The goal is to understand the contract, message format, error rules, and testing risks of each API.

## Key Points

- SOAP is a protocol; REST is an architectural style.
- SOAP messages use XML and a standard `Envelope`.
- A SOAP API is usually described by a WSDL contract.
- REST APIs commonly use HTTP and JSON, but REST does not require JSON.
- A REST request should carry enough information to be processed independently.
- SOAP returns structured `Fault` messages; REST commonly uses HTTP status codes and an error schema.
- SOAP testing requires careful validation of XML, namespaces, and contracts.
- REST testing requires careful validation of resources, methods, status codes, headers, and response bodies.
- The SOAP ecosystem is extended through separate WS-* standards.
- WSDL can be used to generate client code automatically, so some integration defects appear in generated clients.

## Notes

## What Is SOAP

SOAP stands for **Simple Object Access Protocol**. It defines a strict XML structure for exchanging messages between systems.

A SOAP message usually contains:

- `Envelope` - the root element;
- `Header` - optional metadata such as security information;
- `Body` - request or response payload;
- `Fault` - structured error information.

Example:

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

SOAP most commonly uses HTTP/HTTPS, but it can also use other transports.

## WSDL As A Contract

**WSDL** stands for Web Services Description Language. It describes:

- available operations;
- endpoint address;
- request and response messages;
- XML data types;
- bindings and transport;
- namespaces.

For a tester, the WSDL is a primary source of expected SOAP service behavior.

QA verifies:

- whether the request matches the operation;
- whether required elements are present;
- whether types and namespaces are correct;
- whether the response matches the contract;
- whether the expected SOAP Fault is returned.

## SOAP Extensibility And WS-* Standards

SOAP defines the base message format, while additional capabilities are commonly provided by separate WS-* specifications.

Examples:

- **WS-Security** - signatures, encryption, and security tokens;
- **WS-Addressing** - addressing information inside SOAP messages;
- **WS-Policy** - description of service requirements and capabilities;
- **WS-ReliableMessaging** - reliable message delivery;
- **WS-AtomicTransaction** - coordination of distributed transactions.

Using SOAP does not mean that all these features are enabled automatically. A team selects the required standards and configures them separately.

QA should determine:

- which WS-* standards are used;
- whether SOAP headers are required;
- whether timestamps, signatures, and message IDs are validated;
- how duplicate, delayed, and out-of-order messages are handled;
- what happens during a partial transaction failure.

## Generated SOAP Clients

Many IDEs and frameworks can read a WSDL and generate:

- service client;
- request and response classes;
- data types;
- serialization and parsing code;
- operation methods.

SOAP complexity therefore depends not only on the protocol, but also on the language and tooling. In one project, developers work with generated methods and rarely see XML. In another, XML is built manually.

QA risks:

- generated client was created from an outdated WSDL;
- client regeneration breaks backward compatibility;
- optional field is generated as required, or the opposite;
- schema enum does not match the service;
- namespace changes break deserialization;
- client hides useful SOAP Fault details;
- different teams use different WSDL versions.

## What Is REST

REST stands for **Representational State Transfer**. It models entities as resources available through URIs.

Resource examples:

```text
GET    /users
GET    /users/42
POST   /users
PUT    /users/42
PATCH  /users/42
DELETE /users/42
```

REST APIs commonly use JSON:

```json
{
  "id": 42,
  "name": "Alex",
  "active": true
}
```

REST does not require JSON or OpenAPI, although both are widely used in practice.

One resource can have several representations. For example, a service may return JSON, XML, or CSV depending on the `Accept` header. If the API supports content negotiation, QA should verify each supported format and the response to an unsupported media type.

## REST Constraints

REST includes these architectural constraints:

1. Client-server.
2. Stateless.
3. Cacheable.
4. Uniform interface.
5. Layered system.
6. Code on demand - optional.

**Stateless** means the server should not depend on previous request context to process the current request. An authentication token and other required context are sent with the request.

## SOAP And REST Comparison

| Characteristic | SOAP | REST |
| --- | --- | --- |
| Model | Protocol | Architectural style |
| Typical transport | HTTP/HTTPS; other transports are possible | Usually HTTP/HTTPS |
| Format | XML | Usually JSON; XML and other formats are possible |
| Contract | Usually WSDL | Often OpenAPI, but not formally required |
| Structure | Strict | More flexible |
| Interaction model | Operations/messages | Resources |
| Errors | SOAP Fault | HTTP status code + error body |
| Message size | Usually larger because of XML | Usually smaller when JSON is used |
| Caching | Depends on implementation | Supported through HTTP semantics |
| Common projects | Enterprise, finance, healthcare, legacy | Web, mobile, public APIs, microservices |

## SOAP And REST Similarities

Despite their differences, both approaches:

- support communication between systems;
- can work through HTTP/HTTPS;
- require agreed message and error rules;
- need authentication, authorization, and encryption;
- need a contract or documentation for consumers;
- require functional, negative, security, and performance testing.

SOAP is not automatically reliable, and REST is not automatically fast. Actual quality depends on API design, payload, infrastructure, implementation, and testing.

## Decision Matrix

| Question | Favors SOAP | Favors REST |
| --- | --- | --- |
| Is a strict formal contract required? | WSDL and XSD are central | OpenAPI can be used, but flexibility is higher |
| Are WS-* enterprise standards needed? | Strong fit | Usually implemented through separate HTTP/application mechanisms |
| Are clients web or mobile applications? | Possible, but XML may add complexity | Common and convenient |
| Is a small payload important? | XML adds overhead | JSON or compact formats are usually smaller |
| Does the API change frequently? | Contract changes require careful coordination | Easier to evolve, but consumers still need compatibility |
| Does existing infrastructure already use one style? | Existing SOAP ecosystem matters | Existing HTTP/REST ecosystem matters |
| Are multiple transports required? | SOAP supports this model | REST is normally tied to HTTP semantics |

In practice, the choice is often already determined by an existing system or external provider. QA then needs to understand its rules and risks rather than choose the architecture.

## What To Test In SOAP APIs

### Contract

- operation exists in WSDL;
- endpoint matches the environment;
- request matches the XML Schema;
- required elements are present;
- element order is correct when required by the schema;
- namespaces and prefixes are handled correctly.

### Data

- valid and invalid types;
- missing required elements;
- empty elements;
- `xsi:nil`;
- boundary values;
- special XML characters;
- unexpected elements;
- encoding.

### Errors

- correct SOAP Fault;
- `faultcode`;
- `faultstring` or `Reason`;
- fault details;
- no internal stack traces;
- correct HTTP status according to the contract and implementation.

### Security

- HTTPS;
- authentication;
- WS-Security headers when used;
- expired or invalid credentials;
- signature and timestamp validation;
- no secrets in logs or faults.

## What To Test In REST APIs

### Resource And HTTP Method

- correct URI;
- correct behavior of `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`;
- unsupported method;
- idempotency;
- query and path parameters;
- pagination, filtering, and sorting.

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
- supported representations such as JSON, XML, or CSV;
- error format;
- response time;
- absence of sensitive data.

## SOAP And REST Errors

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

QA should verify not only that an error occurs, but also that the error contract is consistent across endpoints.

## When SOAP Is Chosen

SOAP may be appropriate when:

- a strict formal contract is required;
- existing enterprise systems use it;
- WS-Security, reliable messaging, or transaction standards are needed;
- strict XML Schema validation is important;
- integrations require long-term contract stability.

This does not mean SOAP is automatically secure. Security still depends on configuration and implementation.

## When REST Is Chosen

REST is commonly appropriate when:

- the API serves a web or mobile client;
- simplicity and smaller payloads matter;
- the API is public or has many consumers;
- requirements change frequently;
- the system uses microservice or cloud-native architecture;
- the team uses HTTP tooling and OpenAPI.

REST still requires careful versioning, security, and contract management.

## Tools

For SOAP:

- SoapUI;
- ReadyAPI;
- Postman;
- WSDL validators;
- XML Schema validators.

For REST:

- Postman;
- Swagger UI / OpenAPI;
- Insomnia;
- cURL;
- REST Assured;
- Newman.

## Common Defects

- WSDL describes an element that the service does not accept;
- SOAP response contains an incorrect namespace;
- service returns a normal HTML error instead of a SOAP Fault;
- REST endpoint returns `200 OK` for a validation error;
- `PUT` updates only part of a resource against the contract;
- `DELETE` is not idempotent;
- REST response does not match the OpenAPI schema;
- REST API ignores `Accept` and returns the wrong representation;
- unsupported media type is handled inconsistently;
- different endpoints use different error formats;
- API exposes sensitive fields;
- authentication is enforced only for some operations.

## Bug Report Tips

An API bug report should include:

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

Do not publish real tokens, passwords, or personal data.

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
| Representation | A particular format of a resource, such as JSON, XML, or CSV. |

## Questions

### 1. What is the main difference between SOAP and REST?

Answer: SOAP is a protocol with a strict XML message format, while REST is an architectural style commonly implemented through HTTP resources.

### 2. What does WSDL describe?

Answer: SOAP service operations, endpoints, request and response messages, XML types, bindings, and namespaces.

### 3. Must a REST API use JSON?

Answer: No. JSON is the most common format, but REST does not require a specific representation format.

### 4. What does stateless mean?

Answer: Each request carries enough information to be processed independently of previous requests.

### 5. How are errors commonly represented?

Answer: SOAP uses SOAP Fault, while REST APIs commonly use an HTTP status code and a structured error body.

### 6. What is most important when testing SOAP?

Answer: WSDL/schema compliance, XML structure, namespaces, data types, SOAP Faults, and security headers.

### 7. What is most important when testing REST?

Answer: Resources, HTTP methods, parameters, status codes, schemas, headers, authorization, and error consistency.

### 8. Why does a SOAP API use WS-* standards?

Answer: They add standardized capabilities such as security, addressing, policy, reliable messaging, and transactions.

### 9. What risk is associated with a generated SOAP client?

Answer: The client may be generated from an outdated WSDL or incorrectly handle changed types, namespaces, and faults.

## What To Review Later

- SOAP Envelope, Header, Body, and Fault.
- WSDL structure and XML Schema.
- REST constraints.
- HTTP method semantics and idempotency.
- OpenAPI schema validation.
- WS-* standards and generated SOAP clients.
- HTTP content negotiation.
- SoapUI and Postman basics.
