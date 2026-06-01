# HTTP Headers

## Summary

HTTP headers are `name: value` pairs that send additional information together with an HTTP request or HTTP response.

Headers help client and server agree on details:

- what content type is sent;
- what language is preferred;
- what credentials are used;
- whether response can be cached;
- what cookies should be set;
- whether a cross-origin request is allowed;
- what security rules apply.

For QA, headers matter because many bugs cannot be understood from UI alone. You need to inspect the Network tab and see which headers went in the request and which headers came back in the response.

Main idea:

> HTTP headers are metadata of the conversation between client and server.

## What Is An HTTP Header?

An HTTP header consists of a case-insensitive name, a colon, and a value.

Example:

```http
Content-Type: application/json
Authorization: Bearer eyJ...
Cache-Control: no-store
```

Header name is not case-sensitive:

```text
content-type
Content-Type
CONTENT-TYPE
```

For HTTP, these are the same name. In real documentation and tools, the familiar format like `Content-Type` is usually used.

## Where QA Sees Headers

Headers can be inspected:

- in browser DevTools on the Network tab;
- in Postman, Insomnia, or similar API tools;
- in curl output;
- in server logs;
- in proxy tools such as Charles, Fiddler, mitmproxy;
- in automated API tests.

In DevTools, it is usually useful to inspect:

- Request Headers;
- Response Headers;
- Payload;
- Preview/Response;
- Cookies.

## Types Of HTTP Headers

Headers can be grouped by context.

| Type | Meaning |
| --- | --- |
| General headers | Apply to the message as a whole, not only to the body. |
| Request headers | Provide information about the client, requested resource, or request conditions. |
| Response headers | Provide additional information about the response or server. |
| Entity / representation headers | Describe the body: type, length, encoding, language. |

Modern documentation may use slightly different terms, but for QA the practical idea is important: some headers go from client, some come from server, and some describe content.

## Request Headers

Request headers are sent from client to server.

They may describe:

- browser/client;
- authentication;
- expected response format;
- cookies;
- language;
- origin;
- cache conditions;
- content sent in request body.

## Common Request Headers

| Header | Meaning | QA Focus |
| --- | --- | --- |
| `Host` | Domain/host target server. | Wrong host can break routing. |
| `User-Agent` | Client/browser/app information. | Useful for compatibility and device-specific behavior. |
| `Accept` | MIME types client can receive. | API may return wrong format. |
| `Accept-Language` | Preferred language. | Important for localization checks. |
| `Accept-Encoding` | Supported compression formats. | Compression issues can affect response handling. |
| `Authorization` | Credentials, often token. | Check auth flows and token leakage. |
| `Cookie` | Cookies sent to server. | Session and tracking behavior. |
| `Content-Type` | Type of request body. | Critical for API POST/PUT/PATCH requests. |
| `Origin` | Origin of cross-origin request. | Important for CORS. |
| `Referer` | Page that initiated request. | Privacy, analytics, anti-CSRF checks. |

## Response Headers

Response headers are returned from server to client.

They may describe:

- server response;
- content type;
- caching rules;
- cookies to set;
- redirects;
- CORS permissions;
- security policies.

## Common Response Headers

| Header | Meaning | QA Focus |
| --- | --- | --- |
| `Content-Type` | MIME type of response body. | Browser/API client must parse response correctly. |
| `Content-Length` | Body size in bytes. | Useful for downloads and truncated responses. |
| `Location` | Redirect target or new resource location. | Check redirects and `201 Created`. |
| `Set-Cookie` | Server asks browser to store cookie. | Session, auth, flags, expiration. |
| `Cache-Control` | Caching rules. | Stale content and sensitive data caching. |
| `ETag` | Resource version identifier. | Conditional requests and cache validation. |
| `Last-Modified` | Last resource modification time. | Cache and sync behavior. |
| `WWW-Authenticate` | Authentication method required. | Usually with `401`. |
| `Server` | Server software info. | Can leak unnecessary infrastructure details. |

## Entity / Representation Headers

These headers describe the content.

| Header | Meaning |
| --- | --- |
| `Content-Type` | MIME type, for example `application/json` or `text/html`. |
| `Content-Encoding` | Encoding/compression, for example `gzip` or `br`. |
| `Content-Language` | Language of the content. |
| `Content-Length` | Size of the body. |
| `Content-Range` | Range of partial content. |

QA checks:

- JSON API returns `application/json`;
- HTML page returns `text/html`;
- downloaded file has correct type;
- wrong `Content-Type` does not break frontend parsing;
- partial file/video responses use correct range headers.

## Authentication Headers

Authentication headers help control access.

| Header | Direction | Meaning |
| --- | --- | --- |
| `Authorization` | Request | Client sends credentials, token or auth scheme. |
| `WWW-Authenticate` | Response | Server tells client how to authenticate. |
| `Proxy-Authorization` | Request | Credentials for proxy server. |
| `Proxy-Authenticate` | Response | Proxy asks for authentication. |

Example:

```http
Authorization: Bearer <token>
```

QA checks:

- protected endpoint rejects request without `Authorization`;
- expired token returns expected status, often `401`;
- invalid token does not expose sensitive details;
- token is not sent to wrong domain;
- token is not stored or logged insecurely.

## Cookie Headers

Cookies are controlled through headers.

Request:

```http
Cookie: session_id=abc123
```

Response:

```http
Set-Cookie: session_id=abc123; HttpOnly; Secure; SameSite=Lax
```

Important cookie attributes:

| Attribute | Meaning |
| --- | --- |
| `HttpOnly` | JavaScript cannot read cookie. Helps reduce impact of XSS. |
| `Secure` | Cookie is sent only over HTTPS. |
| `SameSite` | Controls cross-site sending of cookie. |
| `Expires` / `Max-Age` | Cookie lifetime. |
| `Path` | URL path where cookie applies. |
| `Domain` | Domain where cookie applies. |

QA checks:

- auth cookies have `HttpOnly` and `Secure` where expected;
- logout clears or invalidates session cookie;
- cookie expiration matches requirements;
- cookie is not sent to unrelated domains;
- `SameSite` does not break login/payment redirects.

## CORS Headers

CORS, Cross-Origin Resource Sharing, controls whether browser allows frontend from one origin to access resources from another origin.

Common headers:

| Header | Meaning |
| --- | --- |
| `Origin` | Request origin sent by browser. |
| `Access-Control-Allow-Origin` | Which origin may access response. |
| `Access-Control-Allow-Methods` | Allowed methods for cross-origin request. |
| `Access-Control-Allow-Headers` | Allowed custom/request headers. |
| `Access-Control-Allow-Credentials` | Whether credentials are allowed. |
| `Access-Control-Expose-Headers` | Response headers visible to frontend JavaScript. |
| `Access-Control-Max-Age` | How long preflight result can be cached. |

QA checks:

- allowed origin works;
- disallowed origin blocked;
- credentials are not allowed with unsafe wildcard setup;
- preflight `OPTIONS` request succeeds when expected;
- frontend can read only exposed headers.

## Cache Headers

Cache headers affect whether browser or proxy can reuse response.

Common headers:

| Header | Meaning |
| --- | --- |
| `Cache-Control` | Main caching policy. |
| `Expires` | Old-style expiration time. |
| `ETag` | Resource version identifier. |
| `If-None-Match` | Client asks if ETag is still valid. |
| `Last-Modified` | Last modification time. |
| `If-Modified-Since` | Client asks if resource changed since time. |
| `Vary` | Which request headers affect cached response selection. |

Examples:

```http
Cache-Control: no-store
Cache-Control: max-age=31536000
```

QA checks:

- sensitive pages use safe cache policy;
- static assets can be cached if expected;
- after deployment user receives fresh assets;
- `304 Not Modified` behavior is correct;
- language-specific content respects `Vary: Accept-Language`.

## Security Headers

Security headers help reduce web security risks.

Important examples:

| Header | Purpose |
| --- | --- |
| `Strict-Transport-Security` | Forces browser to use HTTPS for future requests. |
| `Content-Security-Policy` | Controls sources for scripts, styles, images and other resources. |
| `X-Frame-Options` | Helps prevent clickjacking by controlling iframe embedding. |
| `X-Content-Type-Options` | Prevents MIME sniffing when set to `nosniff`. |
| `Referrer-Policy` | Controls how much referrer information is sent. |
| `Permissions-Policy` | Controls browser features like camera, geolocation, microphone. |

QA checks:

- security headers present on sensitive pages;
- CSP does not block required scripts/styles;
- app cannot be embedded if product forbids it;
- no mixed content with HTTPS;
- headers are consistent across environments.

## Hop-By-Hop Vs End-To-End Headers

Some headers are meant only for one network connection.

Hop-by-hop headers should not be blindly forwarded by proxies.

Examples:

- `Connection`;
- `Keep-Alive`;
- `Proxy-Authenticate`;
- `Proxy-Authorization`;
- `TE`;
- `Trailer`;
- `Transfer-Encoding`;
- `Upgrade`.

End-to-end headers should reach the final recipient and can be stored by caches when appropriate.

For QA this matters when bugs appear only behind proxy, gateway, CDN or load balancer.

## Custom Headers

Products often use custom headers.

Examples:

```http
X-Request-ID: 9f35...
X-Correlation-ID: 9f35...
X-Feature-Flag: new-checkout
```

Historically custom headers often started with `X-`, but this convention is no longer recommended as a strict rule.

QA checks:

- correlation/request ID appears in logs;
- required custom headers are sent by client;
- missing custom header returns expected error;
- custom headers do not expose secrets.

## Example Bug Investigation

Bug:

```text
User logs in successfully, but after refresh becomes logged out.
```

QA investigation:

1. Check login response headers.
2. Is `Set-Cookie` present?
3. Does cookie have correct `Domain`, `Path`, `Expires` or `Max-Age`?
4. Is `Secure` used while testing over HTTPS?
5. Is `SameSite` too strict for the login flow?
6. On refresh, does request include `Cookie` header?
7. Does server accept the cookie or return `401`?

This bug may be a cookie/header problem, not a UI problem.

## Common Mistakes

Common mistakes:

- checking response body but ignoring headers;
- wrong `Content-Type` for API response;
- missing `Authorization` header;
- storing token in unsafe place and leaking it through requests;
- incorrect cookie `Domain` or `Path`;
- missing `Secure` or `HttpOnly` on session cookie;
- broken CORS configuration;
- caching sensitive data;
- missing `Location` header for redirect/create flows;
- exposing server or framework details unnecessarily;
- inconsistent headers between staging and production.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| HTTP header | Metadata field sent with HTTP request or response. |
| Request header | Header sent from client to server. |
| Response header | Header sent from server to client. |
| `Content-Type` | Describes MIME type of body. |
| `Authorization` | Carries credentials or token. |
| `Cookie` | Sends cookies from browser to server. |
| `Set-Cookie` | Server instructs browser to store cookie. |
| `Cache-Control` | Defines caching rules. |
| `Location` | Redirect target or created resource location. |
| `Origin` | Origin of cross-origin request. |
| CORS | Browser mechanism for controlled cross-origin access. |
| CSP | Content Security Policy, security rule for resource loading. |
| HSTS | Strict-Transport-Security, forces HTTPS. |
| `ETag` | Resource version identifier for cache validation. |
| `Vary` | Tells cache which request headers affect response. |

## Questions

### 1. What are HTTP headers?

HTTP headers are metadata fields sent with HTTP requests and responses.

### 2. Where can QA inspect headers?

In DevTools Network tab, API tools, curl output, server logs or proxy tools.

### 3. Why is `Content-Type` important?

It tells client how to interpret response body or tells server what kind of request body is being sent.

### 4. What is the difference between `Cookie` and `Set-Cookie`?

`Cookie` is sent by browser to server. `Set-Cookie` is sent by server to browser to store or update cookie.

### 5. Why are CORS headers important?

They control whether browser allows frontend from one origin to access response from another origin.

### 6. What can go wrong with cache headers?

User may see stale content, sensitive pages may be cached, or new deployment assets may not update correctly.

### 7. Why are security headers useful?

They reduce risks like clickjacking, MIME sniffing, insecure transport and uncontrolled script execution.

### 8. Why are custom correlation headers useful?

They help trace one request through frontend, backend, gateway and logs.

## What To Review Later

- HTTP Status Codes
- HTTP Methods
- Cookies
- CORS
- Cache-Control
- Content Security Policy
- HTTPS and TLS
- DevTools Network Tab
