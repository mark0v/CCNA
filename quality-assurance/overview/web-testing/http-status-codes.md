# HTTP Status Codes

## Summary

HTTP status code - это числовой код в response, который показывает, как server обработал HTTP request.

Для QA status codes важны потому, что они помогают быстро понять:

- request прошел успешно или нет;
- проблема на стороне client или server;
- был ли redirect;
- нужна ли authentication;
- найден ли resource;
- правильно ли backend обрабатывает negative scenarios.

Главная мысль:

> UI может скрыть проблему, но status code часто первым показывает реальное состояние request.

## What Is An HTTP Status Code?

HTTP status code приходит в response от server.

Пример:

```text
HTTP/1.1 200 OK
```

Status code состоит из трех цифр. Первая цифра показывает class response.

| Class | Range | Meaning |
| --- | --- | --- |
| `1xx` | `100-199` | Informational responses |
| `2xx` | `200-299` | Successful responses |
| `3xx` | `300-399` | Redirection messages |
| `4xx` | `400-499` | Client errors |
| `5xx` | `500-599` | Server errors |

Status codes defined in RFC 9110 and related HTTP specifications. На практике иногда встречаются non-standard или product-specific codes, но QA должен сначала уверенно понимать common standard codes.

## Why QA Should Care

Status code помогает не гадать.

Пример:

User видит "Something went wrong".

В DevTools Network tab QA может увидеть:

- `400` - frontend отправил invalid request;
- `401` - user не authenticated;
- `403` - user authenticated, но access forbidden;
- `404` - endpoint или resource not found;
- `409` - conflict with current state;
- `500` - server crashed or failed;
- `503` - service temporarily unavailable.

Одинаковое UI-сообщение может скрывать разные technical causes.

## 1xx Informational Responses

`1xx` codes означают, что request received и processing продолжается.

В обычном UI testing QA редко работает с ними напрямую, но полезно знать смысл.

| Code | Meaning | QA Note |
| --- | --- | --- |
| `100 Continue` | Client может продолжать request. | Может встречаться при large request body. |
| `101 Switching Protocols` | Server switches protocol after `Upgrade` request. | Например, related to WebSocket upgrade. |
| `102 Processing` | Server получил request и обрабатывает его. | WebDAV-specific. |
| `103 Early Hints` | Server отправляет hints до final response. | Может помогать preload/preconnect resources. |

## 2xx Successful Responses

`2xx` codes означают, что request был успешно принят, понят и обработан.

Важно: success code не всегда означает, что business outcome правильный. Нужно проверять response body, database state и UI behavior.

## 200 OK

`200 OK` - самый частый success response.

Meaning зависит от HTTP method:

- `GET` - resource returned in response body;
- `HEAD` - headers returned, body отсутствует;
- `POST` или `PUT` - response может описывать result of action.

QA checks:

- response body содержит правильные data;
- UI показывает актуальную информацию;
- нет hidden business error inside `200`;
- data соответствует permissions current user.

## 201 Created

`201 Created` означает, что request выполнен и created new resource.

Часто expected для:

- registration;
- create order;
- create comment;
- upload file;
- create entity через API.

QA checks:

- new resource реально создан;
- response содержит ID или location, если это expected;
- повторный request не создает duplicate, если operation должна быть idempotent или protected.

## 202 Accepted

`202 Accepted` означает, что request принят, но processing еще не завершен.

Типичный use case:

- async job;
- report generation;
- background processing;
- batch operation.

QA checks:

- UI показывает pending state;
- user понимает, что operation not completed yet;
- есть способ проверить final result;
- repeated polling или notifications работают корректно.

## 204 No Content

`204 No Content` означает success без response body.

Часто встречается после:

- delete action;
- save action без need to return body;
- update where UI already knows final state.

QA checks:

- frontend не пытается parse empty body как JSON;
- UI обновляется корректно;
- resource действительно удален или изменен.

## 206 Partial Content

`206 Partial Content` используется, когда client запрашивает часть resource через `Range` header.

Примеры:

- video streaming;
- file download resume;
- partial content loading.

QA checks:

- media playback works;
- download resume works;
- range requests do not corrupt file.

## 3xx Redirection Messages

`3xx` codes означают, что client должен перейти к другому location или использовать cached response.

QA должен проверять redirects особенно внимательно при:

- login/logout;
- HTTP -> HTTPS;
- old URL -> new URL;
- language/region redirects;
- trailing slash behavior.

## 301 Moved Permanently

`301` означает permanent redirect.

QA checks:

- redirect target correct;
- old URL больше не используется в navigation;
- method behavior соответствует expectations;
- no redirect loop.

## 302 Found

`302` означает temporary redirect.

Часто используется после:

- login;
- logout;
- temporary route changes;
- feature flag routing.

QA checks:

- user попадает на correct page;
- cookies/session set correctly;
- redirect не ломает browser Back behavior.

## 303 See Other

`303` просит client получить другой resource через `GET`.

Часто используется после form submission, чтобы избежать повторной отправки form при refresh.

QA checks:

- refresh не повторяет destructive action;
- user видит correct result page.

## 304 Not Modified

`304` связан с caching. Он означает, что resource не изменился, и client может использовать cached version.

QA checks:

- after deployment user не видит old broken assets;
- cache invalidation работает;
- browser получает fresh content when needed.

## 307 Temporary Redirect

`307` похож на `302`, но client должен сохранить original HTTP method.

Если first request был `POST`, next request тоже должен быть `POST`.

QA checks:

- method не меняется unexpectedly;
- body не теряется при redirect.

## 308 Permanent Redirect

`308` похож на `301`, но сохраняет original HTTP method.

QA checks:

- permanent redirect correct;
- method and body preserved;
- no accidental duplicate submissions.

## 4xx Client Errors

`4xx` codes означают, что server считает request проблемным со стороны client.

Это не всегда "ошибка пользователя". Иногда frontend неправильно сформировал request или client использует старую API version.

## 400 Bad Request

`400` означает malformed or invalid request.

QA checks:

- invalid input returns `400`;
- error message understandable;
- frontend не отправляет broken JSON;
- validation errors map to correct fields.

## 401 Unauthorized

Несмотря на название, `401` означает unauthenticated.

Client должен authenticate себя.

QA checks:

- not logged-in user gets `401`;
- expired token gets `401`;
- UI redirects to login or shows proper message;
- response does not leak sensitive data.

## 403 Forbidden

`403` означает: server понял request, user может быть authenticated, но access запрещен.

QA checks:

- user without permission cannot access resource;
- UI hides or disables forbidden actions;
- direct API call also blocked;
- response safe and not too detailed.

## 404 Not Found

`404` означает resource not found.

В browser это может быть wrong URL. В API это может означать, что endpoint exists, но requested entity не существует.

QA checks:

- broken links отсутствуют;
- deleted resources return expected response;
- custom 404 page works;
- API does not reveal private resource existence if product hides it.

## 405 Method Not Allowed

`405` означает, что method известен server, но не разрешен для target resource.

Пример:

```text
DELETE /users/123 -> 405 Method Not Allowed
```

QA checks:

- unsupported methods rejected;
- `Allow` header present if expected;
- UI/API clients use correct method.

## 408 Request Timeout

`408` означает, что server waited too long for request.

QA checks:

- slow network handled gracefully;
- user can retry;
- no duplicate actions after retry.

## 409 Conflict

`409` означает conflict with current state of resource.

Примеры:

- two users edit same record;
- duplicate email registration;
- order already processed;
- optimistic locking conflict.

QA checks:

- conflict message clear;
- user can resolve conflict;
- data not silently overwritten.

## 410 Gone

`410` означает, что resource был удален и больше не доступен.

QA checks:

- deleted promotional pages or expired links handled correctly;
- UI does not keep dead links;
- API behavior matches product decision.

## 413 Payload Too Large

`413` означает, что request body превышает server limits.

QA checks:

- large file upload rejected gracefully;
- user sees max size message;
- server does not crash;
- retry rules clear if `Retry-After` exists.

## 415 Unsupported Media Type

`415` означает unsupported request content type.

QA checks:

- wrong `Content-Type` rejected;
- file upload validates type;
- API documentation matches actual behavior.

## 422 Unprocessable Content

`422` означает, что request syntactically correct, но semantic validation failed.

Пример:

```text
email format valid, but email already taken
```

QA checks:

- business validation returns useful errors;
- fields map correctly;
- UI displays errors near correct inputs.

## 429 Too Many Requests

`429` означает rate limit exceeded.

QA checks:

- brute force protection works;
- repeated requests limited;
- UI shows retry message;
- `Retry-After` handled if present.

## 5xx Server Errors

`5xx` codes означают, что server failed to fulfill a valid request.

QA особенно важно проверять, что user не видит stack traces, secrets, SQL errors или internal infrastructure details.

## 500 Internal Server Error

`500` - general server-side error.

QA checks:

- user sees friendly error;
- logs contain diagnostic info;
- no sensitive technical details in UI;
- error is reproducible with steps.

## 501 Not Implemented

`501` означает, что server не поддерживает request method/functionality.

QA checks:

- unsupported API features documented;
- client does not call not implemented endpoints.

## 502 Bad Gateway

`502` часто означает, что gateway/proxy получил invalid response from upstream server.

QA checks:

- reverse proxy/backend integration works;
- fallback page is friendly;
- monitoring catches upstream failure.

## 503 Service Unavailable

`503` означает, что server temporarily unavailable.

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

`504` означает, что gateway/proxy did not receive timely response from upstream server.

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
