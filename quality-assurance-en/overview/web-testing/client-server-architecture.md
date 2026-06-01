# Client-Server Architecture

## Summary

Client-server architecture is a model where one side requests a service and another side provides it.

In this model:

- the client sends a request;
- the server processes the request;
- the server returns a response;
- the network connects the client and the server.

For web testing, this is a foundation topic. Almost every browser action - login, search, checkout, page loading, and form submission - becomes a request from the client to the server and a response back.

Main idea:

> QA should see not only the screen, but also the data exchange between client and server.

## What Is Client-Server Architecture?

Client-server architecture is a computing model where the server hosts, processes, or provides resources and services requested by the client.

A simple analogy:

A user orders pizza delivery. The user places an order, the store accepts it, prepares the pizza, and delivers the result. In this analogy:

- the user is the client;
- the pizza store is the server;
- the order is the request;
- the delivered pizza is the response.

In IT, the idea is similar:

- a browser requests a web page;
- a mail client sends or receives email;
- a mobile app asks the backend for a user profile;
- a desktop app asks a database to save a record.

## Client And Server

## Client

A client is the side that requests a service.

Examples of clients:

- browser;
- mobile app;
- desktop application;
- email client;
- API client;
- QA tool such as Postman.

The client usually handles user interaction: it shows the interface, collects input, and sends requests.

## Server

A server is the side that provides a service or resource.

Examples of servers:

- web server;
- file server;
- mail server;
- database server;
- application server.

A server is usually more powerful than a client because it may serve many users at the same time and store centralized data.

## Web Application In Client-Server Model

A web application is a type of client-server software.

In a typical web application:

- the browser acts as the client;
- the web server or backend acts as the server;
- the database stores structured information;
- the data transfer protocol defines how data is exchanged.

The main part of application logic often lives on the server side. The server receives a request, processes it according to business logic, accesses the database if needed, and generates a response for the user.

The browser receives the response and turns it into a graphical interface: page, buttons, forms, messages, tables, and other UI elements.

For QA, the important idea is:

> The browser shows the result, but the cause of a bug often lives on the server side or in the database.

## Database

A database is a repository for structured storage of information.

In client-server systems, a database may store:

- users;
- orders;
- payments;
- products;
- settings;
- permissions;
- logs;
- content.

The server usually accesses the database when it needs data for a response or when it needs to save the result of a user action.

Example:

User clicks `Save`.

```text
Browser -> Server -> Database
Database -> Server -> Browser
```

If data disappears after refresh, the problem may be in UI, request, server validation, database save logic, or cache.

## Everyday Examples

## Mail Server

Mail servers are used to send and receive emails.

The client can be:

- Gmail web interface;
- Outlook;
- mobile mail app.

The server stores emails, processes sending and delivery, and checks rules and authentication.

## File Server

A file server stores files in one place so different users can access them.

Example:

You create a document in Google Docs on a laptop and later open it from a phone. The file is stored in central storage, not only on one device.

## Web Server

A web server serves websites and web applications.

The browser sends a request, and the server returns HTML, CSS, JavaScript, images, or an API response.

For QA, this matters because a UI bug may actually be:

- wrong response from server;
- network error;
- missing file;
- backend validation issue;
- cache problem.

## Components Of Client-Server Architecture

Classic descriptions of client-server architecture often include three components:

- workstations or client computers;
- servers;
- networking devices.

## Workstations

Workstations are client computers that send requests to the server.

They can run applications, display UI, and access shared files or databases over the network.

Example:

In a hospital system, a workstation may be used to enter patient information while the server stores and manages the shared database.

## Servers

Servers are devices or applications that centrally provide resources.

A server can perform one or more roles:

- mail server;
- database server;
- file server;
- domain controller;
- web server;
- application server.

The server must handle multiple requests from different clients.

## Networking Devices

Networking devices connect clients and servers.

Examples:

- switch;
- router;
- hub;
- repeater;
- bridge;
- firewall;
- access point.

For web testing, the exact device is often less important than the fact that client-server communication depends on the network. If the network is unstable, users may see timeouts, partial loading, failed requests, or duplicate actions.

## How Client-Server Architecture Works In Web

Consider a normal website load in a browser.

1. The user enters a URL in the address bar.
2. The browser asks DNS for the IP address of the target server.
3. DNS returns the IP address.
4. The browser sends an HTTP or HTTPS request to the web server.
5. The server processes the request.
6. The server returns required files or data.
7. The browser processes the response and displays the page.

Simplified flow:

```text
Browser -> DNS -> IP address
Browser -> Web Server -> Response
Browser -> Rendered Page
```

If you open the DevTools Network tab, you can see many of these requests and responses almost in real time.

## Request And Response

Client-server interaction usually follows a request-response model.

A client request may contain:

- URL;
- HTTP method;
- headers;
- cookies;
- query parameters;
- request body.

A server response may contain:

- status code;
- headers;
- response body;
- cookies;
- error message;
- redirected location.

For QA, this is one of the main sources of information during troubleshooting.

## Basic Status Codes

Every server response usually contains a status code. It helps quickly understand how the server processed the request.

| Status Code | Meaning | QA Note |
| --- | --- | --- |
| `200 OK` | Request processed successfully. | Check that response body really contains correct data. |
| `201 Created` | Resource created. | Often expected after create actions. |
| `301 Moved Permanently` | Permanent redirect. | Check that redirect goes to the correct location. |
| `302 Found` | Temporary redirect. | Often appears after login/logout or route changes. |
| `400 Bad Request` | Request is invalid. | Check validation and error message. |
| `401 Unauthorized` | Authentication is required. | User is not logged in or token is invalid/expired. |
| `403 Forbidden` | User is authenticated, but access is denied. | Important for authorization checks. |
| `404 Not Found` | Resource not found. | Check broken links, routes, file paths. |
| `500 Internal Server Error` | Server-side error. | UI should not show stack traces or technical secrets. |

A status code does not replace a full check. `200 OK` may arrive with wrong data, and `400` may be the correct result for invalid input.

## Data Transfer Protocols

A data transfer protocol is a set of rules for how programs exchange data.

For web testing, HTTP and HTTPS matter most, but it is useful to know other protocols too.

| Protocol | Purpose |
| --- | --- |
| HTTP | Transfers web resources, such as HTML documents, API responses, images, and scripts. |
| HTTPS | HTTP over a secure encrypted connection. Used to protect sensitive data. |
| FTP | Transfers files between computers over a network. |
| POP3 | Downloads emails from a mail server to a device. |

## HTTP

HTTP, Hypertext Transfer Protocol, is the foundation of data exchange on the web.

Browsers use HTTP to request resources from servers:

- pages;
- images;
- scripts;
- styles;
- API data.

## HTTPS

HTTPS is HTTP with a security layer.

The letter `S` means secure. Data between client and server is encrypted, so an attacker cannot easily read login, password, token, or personal data.

QA should check:

- sensitive pages open over HTTPS;
- HTTP redirects to HTTPS;
- no mixed content;
- cookies have secure flags where needed;
- forms with credentials are not submitted over HTTP.

## FTP And POP3

FTP is used for transferring files.

POP3 is used for receiving emails on a local device.

They are not the foundation of modern browser web apps, but they help show that the client-server model is broader than browser and website only.

## Types Of Client-Server Architecture

Client-server architecture can be organized into tiers.

## 1-Tier Architecture

In 1-tier architecture, presentation, business logic, and data may live in one system.

Example:

A standalone desktop application where UI, logic, and local data storage are on one device.

Pros:

- simple installation;
- everything is close together;
- may work without a network.

Cons:

- difficult to scale;
- harder to update centrally;
- higher risk of duplicated data.

## 2-Tier Architecture

In 2-tier architecture, there is usually:

- client side with UI;
- server side with a database or shared service.

The client may connect directly to the database server.

Example:

A desktop application that connects directly to a central database.

Pros:

- fewer intermediate layers;
- can be faster for simple systems;
- easier to understand the flow.

Cons:

- direct database access can be a security risk;
- business logic can become split between client and database;
- harder to maintain large applications.

## 3-Tier Architecture

In 3-tier architecture, an application tier or middleware appears between the client and database.

Usually there are:

- presentation tier;
- application tier;
- data tier.

Flow:

```text
Client -> Application Tier -> Data Tier
```

The application tier controls business logic, validation, permissions, and data access.

This is a safer and more manageable approach for many web applications.

## N-Tier Architecture

N-tier architecture is an extended model with more than three tiers.

Additional tiers may include:

- API gateway;
- authentication service;
- caching layer;
- message queue;
- reporting service;
- microservices;
- CDN.

More tiers can improve separation of concerns, but they also make testing, monitoring, and troubleshooting more complex.

## Client-Server Vs Peer-To-Peer

Client-server architecture and peer-to-peer architecture solve different problems.

| Client-Server | Peer-to-Peer |
| --- | --- |
| Has separate clients and servers | Participants can be equal peers |
| Data management is often centralized | Each peer may store its own data |
| Client usually requests a service | Peer may request and provide a service |
| Works for small and large networks | Usually better for smaller networks |
| Server is a central control point | No single central control point |

For web testing, the client-server model is usually more important because the browser acts as the client and the backend or web server acts as the server.

## Advantages

Client-server architecture has several important advantages.

## Centralized Management

Data, rules, and permissions can be managed centrally.

This is useful for:

- access control;
- backups;
- audit;
- updates;
- monitoring.

## Resource Sharing

Multiple clients can use the same resources:

- files;
- databases;
- printers;
- APIs;
- authentication services.

## Better User Experience

The client can stay lightweight and convenient while heavy processing remains on the server.

Example:

The browser shows UI, while the backend calculates prices, checks permissions, and works with the database.

## Easier Maintenance

If business logic lives on the server, it can be updated centrally without manually updating every client device.

## Disadvantages

## Server Dependency

If the central server is unavailable, clients may lose access to the service.

Example:

If the authentication server is down, users cannot log in.

## Cost

Servers, infrastructure, monitoring, backups, and security require money and maintenance effort.

## Traffic Congestion

If too many clients access the server at the same time, overload may happen:

- slow responses;
- timeouts;
- failed requests;
- degraded user experience.

## Maintenance Complexity

Client-server systems require technical maintenance:

- server updates;
- database backups;
- network configuration;
- access control;
- performance monitoring;
- security patches.

## What QA Should Test

For QA, client-server architecture helps structure checks around interaction layers.

## UI Behavior

Check that the client:

- collects input correctly;
- shows loading states;
- displays success and error messages correctly;
- does not break on slow response;
- does not send duplicate requests without a reason.

## Network Requests

Check in DevTools or API tools:

- correct endpoint;
- correct HTTP method;
- status code;
- request payload;
- response body;
- headers;
- cookies;
- redirects.

## Server Behavior

Check:

- business validation;
- authorization;
- error handling;
- rate limits;
- database updates;
- correct response for invalid input.

## Failure Scenarios

Negative scenarios are very important:

- server returns `500`;
- network timeout;
- slow response;
- invalid session;
- expired token;
- DNS issue;
- duplicate submit;
- offline mode.

The user should not see chaos. Even when a server error happens, the UI should show a clear message and avoid corrupting data.

## Example Bug Investigation

Bug:

```text
User clicks Save, but changes disappear after page refresh.
```

QA investigation:

1. Client: does the button click actually send a request?
2. Request: does the payload contain the new values?
3. Server: does the response return success or error?
4. Data: were the values really saved in the database?
5. UI: after refresh, does frontend load fresh data or show cached state?

This approach helps locate the problem instead of guessing.

## Common Mistakes

Common mistakes when testing client-server systems:

- checking only UI and ignoring the Network tab;
- not distinguishing frontend bugs from backend bugs;
- ignoring status codes;
- not checking payloads;
- not testing server errors;
- not checking behavior on slow network;
- assuming that a green UI message proves the data was saved;
- not checking database or API response after actions.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Client | The side that requests a service or resource. |
| Server | The side that provides a service, resource, or processing. |
| Request | A message from client to server. |
| Response | A server answer to a request. |
| DNS | A service that resolves a domain name to an IP address. |
| HTTP/HTTPS | Protocols used by browsers to communicate with web servers. |
| FTP | Protocol for transferring files between computers over a network. |
| POP3 | Protocol for receiving emails from a mail server. |
| Status code | Numeric code in a response that shows the result of request processing. |
| Web server | A server that serves web pages, static files, or responses. |
| Application server | A server where business logic often lives. |
| Database | Structured storage for application data. |
| File server | A server for centralized file storage. |
| Mail server | A server for sending and receiving emails. |
| Peer-to-peer | A model where participants can both request and provide services. |
| N-tier architecture | Architecture with multiple tiers, often more than three. |

## Questions

### 1. What is client-server architecture?

It is a model where a client requests a service or resource, and a server processes the request and returns a response.

### 2. What does a client do?

A client sends requests, displays UI, collects user input, and shows responses.

### 3. What does a server do?

A server provides services, stores or processes data, executes business logic, and responds to clients.

### 4. How does a browser load a website in the client-server model?

The browser resolves the IP through DNS, sends an HTTP/HTTPS request to the web server, receives a response, and renders the page.

### 5. How is client-server different from peer-to-peer?

Client-server has separate client and server roles. In peer-to-peer, participants can be equal and can both request and provide services.

### 6. Why is it important for QA to inspect the Network tab?

Because it shows real requests, responses, status codes, payloads, and errors between client and server.

### 7. What can happen if the central server is down?

Clients may lose access to the service, such as being unable to log in or load data.

### 8. Why does a success message in UI not always prove that data was saved?

Because UI may show the message incorrectly. QA should also verify the server response, API result, or database state.

### 9. How is HTTP different from HTTPS?

HTTPS uses an encrypted connection, so it better protects sensitive data between client and server.

### 10. Why should QA check status codes, not only UI?

Because status codes show the result of server-side request processing and help distinguish success, redirect, client error, and server error.

## What To Review Later

- HTTP and HTTPS
- DNS
- DevTools Network Tab
- API Testing
- Three-Tier Architecture
- Status Codes
- Web Server
- Cryptography
- Client-Side Validation
- Server-Side Validation
