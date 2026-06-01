# PUT Vs PATCH

## Summary

`PUT` and `PATCH` are HTTP methods often used to update resources through an API.

Main difference:

- `PUT` usually replaces the entire resource;
- `PATCH` changes only specific fields or parts of the resource.

For QA, this matters because incorrect use of `PUT` or `PATCH` can cause data loss, unexpected defaults, wrong validation, or silent overwrites.

Main idea:

> `PUT` says "replace the resource with this state", while `PATCH` says "change these parts of the resource".

## Why This Matters For QA

In UI, this may look the same:

```text
User edited profile and clicked Save.
```

But under the hood, frontend may send:

```http
PUT /users/123
```

or:

```http
PATCH /users/123
```

If frontend sends `PUT` with incomplete body, the server may erase fields that were not sent.

If frontend sends `PATCH`, the server should change only provided fields and leave the others unchanged.

## Quick Comparison

| Feature | PUT | PATCH |
| --- | --- | --- |
| Purpose | Replace or update entire resource. | Apply partial modifications. |
| Request body | Usually full resource representation. | Only changed fields or patch instructions. |
| Missing fields | May be removed, reset or treated as defaults depending on API. | Usually remain unchanged. |
| Efficiency | Less efficient for large resources. | More efficient for small updates. |
| Creation behavior | May create resource if URL identifies new resource and API supports it. | Usually updates existing resource. |
| Common use case | Replace user profile. | Change only email or status. |

## PUT Request

`PUT` is used to update or replace a resource on the server.

Typical idea:

```text
Client sends complete representation.
Server replaces current resource with that representation.
```

Example:

```http
PUT /users/123
Content-Type: application/json
```

```json
{
  "id": 123,
  "name": "Anjali",
  "email": "anjali@example.com",
  "age": 20
}
```

Server receives complete user data and replaces the existing user resource.

## Important PUT Risk

If API treats `PUT` as full replacement, missing fields can be lost.

Example:

Current resource:

```json
{
  "id": 123,
  "name": "Anjali",
  "email": "anjali@example.com",
  "age": 20
}
```

Bad `PUT` request:

```json
{
  "name": "Anjali Sharma"
}
```

Possible bad result:

```json
{
  "id": 123,
  "name": "Anjali Sharma",
  "email": null,
  "age": null
}
```

This depends on API implementation, but QA should explicitly check the behavior.

## PUT Can Create Resource

Some APIs allow `PUT` to create a resource when client knows exact URL.

Example:

```http
PUT /users/123
```

If user `123` does not exist, server may create it.

But this is not universal. Some APIs return:

- `404 Not Found`;
- `409 Conflict`;
- `405 Method Not Allowed`;
- `201 Created`;
- `200 OK` or `204 No Content`.

QA should not assume. Expected behavior must be defined in API documentation.

## PATCH Request

`PATCH` is used to partially update a resource.

Typical idea:

```text
Client sends only changes.
Server applies those changes to existing resource.
```

Example:

```http
PATCH /users/123
Content-Type: application/json
```

```json
{
  "email": "new-email@example.com"
}
```

Only `email` should change. Other fields should remain unchanged.

## PATCH Is More Efficient For Small Changes

If resource has many fields, `PATCH` avoids sending full object.

Example:

To update only `age`, client can send:

```json
{
  "age": 40
}
```

This is smaller and clearer than sending the full user profile.

## PATCH Is Not Always Simple Merge

Different APIs implement `PATCH` differently.

Common approaches:

- merge only provided JSON fields;
- JSON Patch operations;
- custom partial update format.

Example JSON Patch style:

```json
[
  { "op": "replace", "path": "/email", "value": "new@example.com" }
]
```

QA should check API documentation and not assume every `PATCH` uses simple field merge.

## Idempotency

Idempotency means repeated same request produces same final state.

`PUT` is generally expected to be idempotent:

```text
PUT same full resource once -> final state A
PUT same full resource again -> final state still A
```

`PATCH` may or may not be idempotent depending on operation.

Idempotent PATCH example:

```json
{
  "email": "new@example.com"
}
```

Non-idempotent PATCH example:

```json
{
  "operation": "increment",
  "field": "loginCount",
  "by": 1
}
```

If repeated, `loginCount` changes again.

QA should test retry behavior carefully, especially when frontend retries failed requests.

## Status Codes For PUT And PATCH

Common successful responses:

| Status Code | Meaning |
| --- | --- |
| `200 OK` | Update succeeded and response body may contain updated resource. |
| `201 Created` | Resource created, possible for PUT when API supports creation. |
| `204 No Content` | Update succeeded, no response body. |

Common error responses:

| Status Code | Meaning |
| --- | --- |
| `400 Bad Request` | Invalid request body or syntax. |
| `401 Unauthorized` | Authentication required or invalid. |
| `403 Forbidden` | User has no permission to update resource. |
| `404 Not Found` | Resource does not exist. |
| `409 Conflict` | Update conflicts with current state. |
| `412 Precondition Failed` | Conditional update failed. |
| `415 Unsupported Media Type` | Wrong `Content-Type`. |
| `422 Unprocessable Content` | Business validation failed. |

## What QA Should Test For PUT

Check:

- full resource update works;
- all required fields are validated;
- missing fields behavior is defined;
- existing fields are not accidentally erased;
- resource creation behavior is clear;
- repeated same PUT does not create duplicates;
- correct status code returned;
- response body matches updated state;
- unauthorized user cannot update resource.

## What QA Should Test For PATCH

Check:

- only provided fields are changed;
- omitted fields remain unchanged;
- invalid field names are rejected;
- unsupported operations are rejected;
- partial validation works;
- business rules still enforced;
- repeated PATCH behavior is understood;
- correct status code returned;
- concurrent updates do not silently overwrite data.

## Common Test Scenarios

## Update One Field

PATCH:

```json
{
  "email": "new@example.com"
}
```

Expected:

- email changed;
- name, age and other fields unchanged.

## PUT With Full Body

PUT:

```json
{
  "id": 123,
  "name": "Anjali",
  "email": "new@example.com",
  "age": 20
}
```

Expected:

- resource replaced by full body;
- no unexpected data loss.

## PUT With Missing Field

PUT:

```json
{
  "id": 123,
  "name": "Anjali"
}
```

Expected depends on requirements:

- request rejected because required fields missing;
- or missing fields reset;
- or existing fields preserved if API intentionally behaves this way.

QA must verify expected behavior with product/API documentation.

## PATCH Unknown Field

PATCH:

```json
{
  "unknownField": "value"
}
```

Expected:

- API rejects unknown field;
- or ignores it only if documented.

Silent ignore can hide frontend bugs.

## Example Bug Investigation

Bug:

```text
User changed only email, but phone number disappeared after saving profile.
```

QA investigation:

1. Open DevTools Network tab.
2. Check method: `PUT` or `PATCH`.
3. Check request payload.
4. If method is `PUT`, was phone number missing from body?
5. Check response body after update.
6. Refresh page and verify backend state.
7. Check whether API documentation expects full replacement.

Likely root cause:

Frontend used `PUT` but sent only partial data, causing missing fields to be reset.

## Common Mistakes

Common mistakes:

- using `PUT` for partial update without full body;
- assuming missing fields are preserved in `PUT`;
- using `PATCH` without defining patch format;
- returning `200 OK` with hidden validation error;
- not checking database state after update;
- not testing repeated requests;
- ignoring `Content-Type`;
- not testing unauthorized update;
- not testing concurrent updates;
- not documenting expected status codes.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| `PUT` | HTTP method commonly used to replace/update entire resource. |
| `PATCH` | HTTP method used to partially update resource. |
| Resource | Entity addressed by URL, for example `/users/123`. |
| Full representation | Complete object state sent in request body. |
| Partial update | Updating only specific fields or operations. |
| Idempotent | Repeating same request leads to same final state. |
| Payload | Request body sent to server. |
| JSON Patch | Standardized patch format with operations like `replace`, `add`, `remove`. |
| `Content-Type` | Header that describes request body format. |
| `409 Conflict` | Status code for conflict with current resource state. |
| `422 Unprocessable Content` | Status code often used for semantic validation errors. |

## Questions

### 1. What is the main difference between PUT and PATCH?

`PUT` usually replaces the entire resource. `PATCH` updates only specific parts of the resource.

### 2. Why can PUT be risky for partial updates?

If client sends incomplete body, missing fields may be removed, reset or overwritten depending on API behavior.

### 3. When is PATCH a better choice?

When only specific fields need to be changed, such as email, status or phone number.

### 4. Is PUT idempotent?

Generally yes: repeating the same full PUT should lead to the same final resource state.

### 5. Is PATCH always idempotent?

No. It depends on patch operation. Setting a field can be idempotent, incrementing a value is not.

### 6. What should QA check after PATCH?

QA should verify changed fields were updated and omitted fields stayed unchanged.

### 7. What should QA check after PUT?

QA should verify full resource state, required fields, missing field behavior and no unexpected data loss.

### 8. Why is API documentation important for PUT/PATCH?

Because APIs can implement creation, validation, missing fields and patch format differently.

## What To Review Later

- HTTP Methods
- HTTP Status Codes
- HTTP Headers
- API Testing
- Idempotency
- JSON Patch
- Validation
- Concurrency
