# REST APIs CRUD And Tokens

Source: closed course page  
Date added: 2026-08-21  
Related plan item: Week 17 / REST APIs, CRUD, and tokens  
Tags: REST, API, HTTP, status codes, CRUD, token, Postman, network automation  
Language: English  
Translation pair: articles/2026-08/week-17/10-rest-apis-crud-and-tokens.md

## Summary

- `REST` is the most common API style, built around HTTP requests and responses.
- A RESTful API works like the web: the client sends a request, and the server returns a response.
- HTTP status codes quickly show what happened to the request.
- `200` series means success, `300` means redirect, `400` means a client/request problem, and `500` means a server problem.
- `CRUD` means Create, Read, Update, Delete.
- A token proves that you are allowed to use an API.
- Treat tokens like passwords.
- `Postman` helps you manually test API requests before automating them.

## Key Points

- APIs are not only exotic developer tools. They are how modern systems talk to each other.
- REST became popular because it uses the familiar HTTP model.
- Status codes matter for exams and for real troubleshooting.
- CRUD describes the basic API actions: create, read, update, and delete.
- APIs make automation powerful because actions can be repeated, scheduled, and scaled.
- That same power makes APIs risky if tokens are handled carelessly.

## Notes

When people hear `API`, it can sound too developer-focused.

The idea is simpler:

```text
One system wants to talk to another system.
It needs a clear way to send a request and receive a response.
An API provides that way.
```

In network automation, the API becomes the doorway into a device, controller, or cloud service.

Through that doorway, you can read data, change settings, and build repeatable workflows.

## REST As a Communication Style

`REST`, or Representational State Transfer, grew out of the web.

The web already works like this:

```text
The browser sends an HTTP request.
The server returns an HTTP response.
```

REST uses the same pattern.

It usually does not try to keep one long emotional session alive. It is more like:

```text
Give me this.
Here is the answer.
```

That is why REST became so popular for APIs.

If a browser can request a page, a script or application can request data, device state, or a configuration change.

## Request and Response

RESTful communication is built around this pair:

```text
Request -> response.
```

A request can include:

- resource address;
- method;
- headers;
- token;
- body data.

A response usually includes:

- status code;
- headers;
- data;
- error details, if something failed.

For a network engineer, this matters because API troubleshooting often starts with the response.

## HTTP Status Codes

HTTP status codes are one of the fastest ways to understand where a problem lives.

You do not need to know every rare code. But you should know the groups:

| Code Group | Meaning |
| --- | --- |
| `200` series | Success. The request worked. |
| `300` series | Redirect or another step is needed. |
| `400` series | Client/request problem. |
| `500` series | Server-side problem. |

Example:

```text
404 = probably the wrong URL or resource.
500 = the server received the request but failed to process it correctly.
```

That changes troubleshooting.

If you receive `404`, first check:

- endpoint;
- path;
- spelling;
- required resource;
- request parameters.

If you receive `500`, it is more reasonable to look for a server-side or platform-side issue.

## CRUD

If REST is the communication style, `CRUD` describes the actions commonly performed through an API.

`CRUD`:

| Letter | Action | Idea |
| --- | --- | --- |
| C | Create | Create an object or setting. |
| R | Read | Read data. |
| U | Update | Update an existing setting. |
| D | Delete | Delete an object or setting. |

In networking, that could mean:

- creating an object on a controller;
- reading interface statistics;
- updating a password;
- changing an interface description;
- deleting an old policy.

The target can vary:

- router;
- switch;
- wireless controller;
- phone;
- smart TV;
- cloud service.

If a system has an API, there is a good chance you are doing some version of CRUD with it.

## Why APIs Matter for Automation

A GUI is useful when you need to do something once.

An API is useful when you need to:

- repeat an action many times;
- make a change on a schedule;
- collect data from different systems;
- connect a network device to a workflow;
- verify state automatically;
- scale work across tens or hundreds of devices.

Instead of clicking manually, you can send a request:

```text
Read this value.
Update that setting.
Create this object.
Delete that old entry.
```

That is how automation becomes repeatable.

## Token

API power requires security.

If an API can create, update, or delete things, access to it cannot be left open.

A `token` is proof that you are allowed to use the API.

The flow often looks like this:

```text
The user authenticates.
The system issues a token.
The client adds the token to API requests.
The server checks the token before performing the action.
```

A token often looks like a long random string. It does not need to be readable.

The point is that the server can verify:

```text
Did this request come from someone allowed to perform this action?
```

## Why Tokens Are Risky

Treat tokens like passwords.

Sometimes they are even easier to leak because people accidentally:

- paste them into screenshots;
- send them in chats;
- leave them in notes;
- commit them to repositories;
- show them in terminal output;
- store them in shared documents.

If someone gets your token, they may get your access.

Good systems reduce the risk with:

- expiration times;
- IP restrictions;
- scoped permissions;
- extra authentication;
- token rotation.

But the main rule stays simple:

```text
Do not share tokens.
Do not store tokens carelessly.
Do not paste tokens into public places.
```

## Postman

`Postman` is a common tool for manually working with APIs.

It helps you:

- build a request;
- choose a method;
- enter a URL;
- add headers;
- include a token;
- send a request;
- inspect the response;
- check the status code;
- study the data.

It is a useful bridge between theory and automation.

First, test the request manually in Postman.

Then move the same idea into a script, playbook, or automation workflow.

## Real World Tip

API troubleshooting can feel boring, but this is where many failures live.

Check in order:

1. Is the endpoint correct?
2. Is the method correct?
3. Are the required headers present?
4. Has the token expired?
5. Is the body formatted correctly?
6. What does the status code say?

One wrong character in an endpoint or one missing header can break the entire request.

## Takeaway

RESTful APIs use the same request-and-response approach that made the web work.

You send an HTTP request, and the server returns a response and a status code.

CRUD describes the basic actions: create, read, update, and delete.

A token decides whether you are allowed to do those things.

If you want APIs to feel real, start with Postman: send a request, inspect the response, read the status code, and only then automate it.

## Commands and Terms

| Term | Meaning |
| --- | --- |
| `API` | A way for software to interact with a system or device. |
| `REST` | A popular API style based on HTTP request/response. |
| `HTTP` | The protocol the web uses for communication between clients and servers. |
| request | A query from a client to a server. |
| response | A server's answer to a request. |
| status code | A number that indicates the result of a request. |
| `200` series | Successful responses. |
| `300` series | Redirects or additional steps. |
| `400` series | Client/request errors. |
| `500` series | Server errors. |
| `CRUD` | Create, Read, Update, Delete. |
| token | Temporary proof of API access. |
| `Postman` | A tool for manually testing API requests. |

## Questions

### 1. Why did REST become so popular?

Answer: It uses the familiar HTTP request-and-response model that already powers the web.

### 2. What does a 200-series status code mean?

Answer: The request succeeded.

### 3. What does a 400-series error usually mean?

Answer: A problem with the client, request, URL, syntax, or parameters.

### 4. What does CRUD mean?

Answer: Create, Read, Update, Delete.

### 5. Why is a token needed?

Answer: A token proves that the client is allowed to use the API.

### 6. Why should tokens be protected?

Answer: If someone gets the token, they may get API access with your permissions.

## Review Later

- REST as a request/response model.
- HTTP status code groups.
- CRUD: create, read, update, delete.
- The role of tokens in API security.
- Why Postman is useful before writing automation scripts.
