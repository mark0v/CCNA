# HTTP Status Codes

## Summary

An HTTP status code is a numeric code in a response that shows how the server handled an HTTP request.

For QA, status codes are important because they help quickly understand:

- whether the request succeeded;
- whether the problem is on the client or server side;
- whether a redirect happened;
- whether authentication is required;
- whether a resource was found;
- whether backend handles negative scenarios correctly.

Main idea:

> UI may hide the problem, but the status code often shows the real state of the request first.

## What Is An HTTP Status Code?

An HTTP status code comes in the response from the server.

Example:

```text
HTTP/1.1 200 OK
```

A status code has three digits. The first digit shows the response class.

| Class | Range | Meaning |
| --- | --- | --- |
| `1xx` | `100-199` | Informational responses |
| `2xx` | `200-299` | Successful responses |
| `3xx` | `300-399` | Redirection messages |
| `4xx` | `400-499` | Client errors |
| `5xx` | `500-599` | Server errors |

Status codes are defined in RFC 9110 and related HTTP specifications. In practice, non-standard or product-specific codes can appear, but QA should first understand common standard codes.

## Why QA Should Care

Status code helps avoid guessing.

Example:

User sees "Something went wrong".

In DevTools Network tab, QA may see:

- `400` - frontend sent invalid request;
- `401` - user is not authenticated;
- `403` - user is authenticated, but access is forbidden;
- `404` - endpoint or resource not found;
- `409` - conflict with current state;
- `500` - server crashed or failed;
- `503` - service temporarily unavailable.

The same UI message may hide different technical causes.

## 1xx Informational Responses

`1xx` codes mean that the request was received and processing continues.

In normal UI testing, QA rarely works with them directly, but the meaning is useful.

| Code | Meaning | QA Note |
| --- | --- | --- |
| `100 Continue` | Client may continue the request. | May appear with large request body. |
| `101 Switching Protocols` | Server switches protocol after `Upgrade` request. | For example, related to WebSocket upgrade. |
| `102 Processing` | Server received the request and is processing it. | WebDAV-specific. |
| `103 Early Hints` | Server sends hints before final response. | May help preload/preconnect resources. |

## 2xx Successful Responses

`2xx` codes mean that the request was successfully received, understood, and processed.

Important: a success code does not always mean the business outcome is correct. Check response body, database state, and UI behavior.

## 200 OK

`200 OK` is the most common success response.

Meaning depends on HTTP method:

- `GET` - resource returned in response body;
- `HEAD` - headers returned, no body;
- `POST` or `PUT` - response may describe the result of the action.

QA checks:

- response body contains correct data;
- UI shows current information;
- no hidden business error inside `200`;
- data matches permissions of current user.

## 201 Created

`201 Created` means that the request succeeded and created a new resource.

Often expected for:

- registration;
- create order;
- create comment;
- upload file;
- create entity through API.

QA checks:

- new resource is really created;
- response contains ID or location if expected;
- repeated request does not create duplicate if operation should be idempotent or protected.

## 202 Accepted

`202 Accepted` means that the request was accepted, but processing is not finished yet.

Typical use cases:

- async job;
- report generation;
- background processing;
- batch operation.

QA checks:

- UI shows pending state;
- user understands that operation is not completed yet;
- there is a way to check final result;
- repeated polling or notifications work correctly.

## 204 No Content

`204 No Content` means success without response body.

Often appears after:

- delete action;
- save action without need to return body;
- update where UI already knows final state.

QA checks:

- frontend does not try to parse empty body as JSON;
- UI updates correctly;
- resource is really deleted or changed.

## 206 Partial Content

`206 Partial Content` is used when client requests part of a resource with the `Range` header.

Examples:

- video streaming;
- file download resume;
- partial content loading.

QA checks:

- media playback works;
- download resume works;
- range requests do not corrupt file.

## 3xx Redirection Messages

`3xx` codes mean that client should go to another location or use cached response.

QA should check redirects carefully for:

- login/logout;
- HTTP -> HTTPS;
- old URL -> new URL;
- language/region redirects;
- trailing slash behavior.

## 301 Moved Permanently

`301` means permanent redirect.

QA checks:

- redirect target correct;
- old URL is no longer used in navigation;
- method behavior matches expectations;
- no redirect loop.

## 302 Found

`302` means temporary redirect.

Often used after:

- login;
- logout;
- temporary route changes;
- feature flag routing.

QA checks:

- user lands on correct page;
- cookies/session set correctly;
- redirect does not break browser Back behavior.

## 303 See Other

`303` asks the client to get another resource with `GET`.

Often used after form submission to avoid resubmitting form on refresh.

QA checks:

- refresh does not repeat destructive action;
- user sees correct result page.

## 304 Not Modified

`304` is related to caching. It means the resource has not changed, so client can use cached version.

QA checks:

- after deployment user does not see old broken assets;
- cache invalidation works;
- browser gets fresh content when needed.

## 307 Temporary Redirect

`307` is similar to `302`, but client must preserve original HTTP method.

If the first request was `POST`, the next request must also be `POST`.

QA checks:

- method does not change unexpectedly;
- body is not lost during redirect.

## 308 Permanent Redirect

`308` is similar to `301`, but preserves original HTTP method.

QA checks:

- permanent redirect correct;
- method and body preserved;
- no accidental duplicate submissions.

## 4xx Client Errors

`4xx` codes mean that the server considers the request problematic from the client side.

This is not always a "user mistake". Sometimes frontend formed the request incorrectly or client uses an old API version.

## 400 Bad Request

`400` means malformed or invalid request.

QA checks:

- invalid input returns `400`;
- error message understandable;
- frontend does not send broken JSON;
- validation errors map to correct fields.

## 401 Unauthorized

Despite the name, `401` means unauthenticated.

The client must authenticate itself.

QA checks:

- not logged-in user gets `401`;
- expired token gets `401`;
- UI redirects to login or shows proper message;
- response does not leak sensitive data.

## 403 Forbidden

`403` means: server understood the request, user may be authenticated, but access is forbidden.

QA checks:

- user without permission cannot access resource;
- UI hides or disables forbidden actions;
- direct API call also blocked;
- response safe and not too detailed.

## 404 Not Found

`404` means resource not found.

In browser, this may be a wrong URL. In API, it may mean endpoint exists but requested entity does not exist.

QA checks:

- no broken links;
- deleted resources return expected response;
- custom 404 page works;
- API does not reveal private resource existence if product hides it.

## 405 Method Not Allowed

`405` means method is known by server, but is not allowed for target resource.

Example:

```text
DELETE /users/123 -> 405 Method Not Allowed
```

QA checks:

- unsupported methods rejected;
- `Allow` header present if expected;
- UI/API clients use correct method.

## 408 Request Timeout

`408` means server waited too long for request.

QA checks:

- slow network handled gracefully;
- user can retry;
- no duplicate actions after retry.

## 409 Conflict

`409` means conflict with current state of resource.

Examples:

- two users edit same record;
- duplicate email registration;
- order already processed;
- optimistic locking conflict.

QA checks:

- conflict message clear;
- user can resolve conflict;
- data not silently overwritten.

## 410 Gone

`410` means resource was deleted and is no longer available.

QA checks:

- deleted promotional pages or expired links handled correctly;
- UI does not keep dead links;
- API behavior matches product decision.

## 413 Payload Too Large

`413` means request body exceeds server limits.

QA checks:

- large file upload rejected gracefully;
- user sees max size message;
- server does not crash;
- retry rules clear if `Retry-After` exists.

## 415 Unsupported Media Type

`415` means unsupported request content type.

QA checks:

- wrong `Content-Type` rejected;
- file upload validates type;
- API documentation matches actual behavior.

## 422 Unprocessable Content

`422` means request is syntactically correct, but semantic validation failed.

Example:

```text
email format valid, but email already taken
```

QA checks:

- business validation returns useful errors;
- fields map correctly;
- UI displays errors near correct inputs.

## 429 Too Many Requests

`429` means rate limit exceeded.

QA checks:

- brute force protection works;
- repeated requests limited;
- UI shows retry message;
- `Retry-After` handled if present.

## 5xx Server Errors

`5xx` codes mean that the server failed to fulfill a valid request.

QA should especially check that users do not see stack traces, secrets, SQL errors, or internal infrastructure details.

## 500 Internal Server Error

`500` is a general server-side error.

QA checks:

- user sees friendly error;
- logs contain diagnostic info;
- no sensitive technical details in UI;
- error is reproducible with steps.

## 501 Not Implemented

`501` means server does not support request method/functionality.

QA checks:

- unsupported API features documented;
- client does not call not implemented endpoints.

## 502 Bad Gateway

`502` often means that gateway/proxy received invalid response from upstream server.

QA checks:

- reverse proxy/backend integration works;
- fallback page is friendly;
- monitoring catches upstream failure.

## 503 Service Unavailable

`503` means server is temporarily unavailable.

Common reasons:

- maintenance;
- overload;
- service startup;
- dependency unavailable.

QA checks:

- user sees understandable message;
- `Retry-After` used if expected;
- temporary response not cached incorrectly;
- system recovers after service returns.

## 504 Gateway Timeout

`504` means gateway/proxy did not receive timely response from upstream server.

QA checks:

- slow dependencies handled;
- UI timeout message clear;
- retry does not duplicate business action.

## QA Checklist For Status Codes

When testing web applications, check:

- expected success code for happy path;
- correct error code for invalid input;
- `401` vs `403` distinction;
- `404` for missing resource;
- redirects do not loop;
- `429` for rate limits;
- `5xx` responses do not expose internals;
- UI shows correct message for each important code;
- API documentation matches actual status codes;
- response body format is consistent.

## Example Bug Investigation

Bug:

```text
User clicks Pay, sees "Payment failed".
```

QA investigation:

1. Open DevTools Network tab.
2. Find payment request.
3. Check status code.
4. If `400` or `422`, inspect request payload and validation error.
5. If `401`, check session/token.
6. If `403`, check permissions or payment access rules.
7. If `409`, check duplicate order or already processed payment.
8. If `500`, check server logs and report backend error.
9. If `504`, check timeout or downstream payment provider.

Same UI message can hide very different root causes.

## Common Mistakes

Common mistakes:

- treating every non-`200` as the same bug;
- returning `200 OK` with error inside body for failed operation;
- using `500` for validation errors;
- confusing `401` and `403`;
- not testing redirects;
- ignoring `204 No Content` body behavior;
- not checking behavior for `429`;
- exposing stack traces for `5xx`;
- not documenting expected codes in API docs;
- relying only on UI messages.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Status code | Three-digit code that describes result of HTTP request. |
| `1xx` | Informational response. |
| `2xx` | Successful response. |
| `3xx` | Redirection response. |
| `4xx` | Client error response. |
| `5xx` | Server error response. |
| `200 OK` | Request succeeded. |
| `201 Created` | New resource created. |
| `204 No Content` | Success without response body. |
| `301/308` | Permanent redirects. |
| `302/307` | Temporary redirects. |
| `304 Not Modified` | Cached version can be used. |
| `400 Bad Request` | Invalid request. |
| `401 Unauthorized` | Authentication required. |
| `403 Forbidden` | Access denied. |
| `404 Not Found` | Resource not found. |
| `409 Conflict` | Request conflicts with current state. |
| `422 Unprocessable Content` | Semantic validation failed. |
| `429 Too Many Requests` | Rate limit exceeded. |
| `500 Internal Server Error` | Server-side failure. |
| `503 Service Unavailable` | Service temporarily unavailable. |
| `504 Gateway Timeout` | Upstream service did not respond in time. |

## Questions

### 1. What does an HTTP status code show?

It shows how the server handled an HTTP request.

### 2. What are the five main classes of status codes?

`1xx` informational, `2xx` success, `3xx` redirect, `4xx` client error, `5xx` server error.

### 3. What is the difference between `401` and `403`?

`401` means authentication is required or invalid. `403` means the user is authenticated or known, but access is forbidden.

### 4. Why can `200 OK` still be a bug?

Because response body may contain wrong data, wrong permissions, stale content or hidden business error.

### 5. When is `201 Created` expected?

When request successfully creates a new resource.

### 6. What does `204 No Content` mean?

The request succeeded, but response has no body.

### 7. Why is `304 Not Modified` important?

It affects caching. Wrong cache behavior can show stale files or old UI.

### 8. What does `429 Too Many Requests` help protect against?

Too many repeated requests, brute force attempts and abusive traffic.

### 9. What should QA check for `5xx` responses?

Friendly UI message, no sensitive details, useful logs and reproducible steps.

### 10. Why should API documentation include status codes?

Because clients and testers need to know expected success and error behavior.

## What To Review Later

- HTTP Methods
- Client-Server Architecture
- Web Server
- API Testing
- DevTools Network Tab
- Authentication
- Authorization
- Rate Limiting
- Caching
- Error Handling
