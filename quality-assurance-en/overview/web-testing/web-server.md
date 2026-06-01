# Web Server

## Summary

A web server is hardware and software that accepts requests from clients and returns web content over HTTP or HTTPS.

In simple terms:

- the browser asks for a page, file, or data;
- the web server receives the request;
- it finds or generates the required response;
- it sends the response back to the browser.

For QA, web servers matter because many "UI problems" are actually related to server responses, missing files, wrong status codes, redirects, cache, permissions, or server errors.

Main idea:

> A web server is where a browser request becomes the response the user sees.

## What Is A Web Server?

A web server can mean two things:

| Meaning | Explanation |
| --- | --- |
| Hardware | A physical or virtual machine where website files, application files, or services are hosted. |
| Software | A program that receives HTTP/HTTPS requests and returns responses. |

Examples of web server software:

- Apache HTTP Server;
- NGINX;
- Microsoft IIS;
- lighttpd;
- Apache Tomcat.

A web server can return:

- HTML;
- CSS;
- JavaScript;
- images;
- videos;
- files for download;
- API responses;
- dynamically generated pages.

## Why We Use Web Servers

Web servers make websites and web applications available over a network or the internet.

They help:

- store website data;
- deliver website content;
- process HTTP/HTTPS requests;
- control access to hosted files;
- manage traffic;
- support server-side scripting;
- host multiple websites or applications;
- log requests and errors;
- improve security.

Without a web server, a browser cannot simply receive a page by URL.

## How A Web Server Works

A normal flow looks like this:

1. The user enters a URL or clicks a link.
2. The browser resolves the server IP address through DNS.
3. The browser sends an HTTP or HTTPS request.
4. The web server receives the request.
5. The server finds the required file or passes the request to application logic.
6. The server returns a response.
7. The browser renders the page or processes the data.

Simplified:

```text
Browser -> HTTP/HTTPS Request -> Web Server
Browser <- HTTP/HTTPS Response <- Web Server
```

If a file is not found, the server may return `404 Not Found`. If the server fails while processing a request, the user may receive `500 Internal Server Error`.

## Static And Dynamic Content

A web server can serve static or dynamic content.

## Static Content

Static content is sent to the browser almost exactly as stored.

Examples:

- HTML file;
- CSS file;
- JavaScript file;
- image;
- PDF;
- font file.

A static web server simply takes the hosted file and returns it to the client.

Example:

```text
GET /styles.css -> web server returns styles.css
```

## Dynamic Content

Dynamic content is created or modified during request processing.

For this, a web server may interact with:

- application server;
- database;
- cache;
- external API;
- server-side scripts.

Example:

```text
GET /profile -> server checks logged-in user -> returns that user's profile page
```

Dynamic content is more flexible, but it is also harder to test because the response may depend on user, session, data, permissions, time, feature flags, and other conditions.

## Web Server Architecture

Web server architecture describes how the server receives, processes, and distributes requests.

Architecture depends on:

- storage;
- memory;
- CPU;
- throughput;
- latency;
- operating system;
- network connectivity;
- supported platform;
- application tiers;
- expected traffic.

For QA, this matters during performance testing, reliability checks, and troubleshooting.

## Concurrent Approach

A concurrent approach allows a web server to process multiple client requests at the same time.

Variants:

- multi-process;
- multithreaded;
- hybrid.

## Multi-Process

A parent process creates child processes. Each child process can handle a separate request.

This approach isolates processing, but it may use more resources.

## Multithreaded

The server uses threads to handle multiple requests.

This can be more resource-efficient, but it requires careful handling of shared state.

## Hybrid

A hybrid approach combines processes and threads.

Example:

The server starts several processes, and each process starts multiple threads.

## Single-Process Event-Driven Approach

A single-process event-driven approach uses one process that handles multiple connections through an event loop.

This can be efficient for a large number of concurrent connections, especially when the server often waits for network or file I/O.

## Common Types Of Web Servers

## Apache HTTP Server

Apache is one of the best-known web servers.

Features:

- open-source;
- works on Linux, Windows, macOS;
- supports modules;
- often used for classic web hosting.

## NGINX

NGINX is often used as:

- web server;
- reverse proxy;
- load balancer;
- static file server.

It is known for handling many concurrent connections well.

## Microsoft IIS

IIS, Internet Information Services, is a Microsoft web server.

It is usually used in Windows Server environments and integrates well with the Microsoft ecosystem.

## Apache Tomcat

Tomcat is often used for Java web applications.

Technically, it is often called a servlet container, but in learning materials it also appears near web servers.

## lighttpd

lighttpd is a lightweight web server designed for low memory and CPU usage.

It may be used in embedded devices, routers, cameras, and other constrained environments.

## Localhost And XAMPP

A web server can run not only on a production server, but also locally.

Localhost means your own computer acting as a server for testing or development.

Example URL:

```text
http://localhost/index.html
```

XAMPP is a popular local development package. It can include Apache, PHP, MariaDB, and other tools.

Example local flow:

1. Install XAMPP.
2. Put `index.html` into a folder such as `htdocs`.
3. Start Apache.
4. Open `http://localhost/index.html` in a browser.

For QA, this is useful when you need to quickly test a static page, prototype, or local web app.

## Web Hosting Vs Web Server

Web hosting and web server are related, but they are not the same thing.

| Aspect | Web Hosting | Web Server |
| --- | --- | --- |
| Meaning | A service that places a website on the internet. | Hardware/software that processes requests and serves content. |
| Purpose | Provides storage, network access, and management for a site. | Receives requests and returns responses. |
| Ownership | Usually a hosting provider. | May belong to a provider, company, or developer. |
| Examples | GoDaddy, Bluehost, HostGator, cloud hosting. | Apache, NGINX, IIS, Tomcat. |

Simply:

> Hosting is the placement service. A web server is the mechanism that serves requests.

## Web Server Vs Application Server

Web servers and application servers are also often confused.

| Web Server | Application Server |
| --- | --- |
| Better suited for static content. | Better suited for business logic and dynamic behavior. |
| Main protocols: HTTP/HTTPS. | May use HTTP, RPC, RMI, and other protocols. |
| Often serves HTML, CSS, JS, images. | Executes application code, rules, workflows. |
| May work as a reverse proxy. | Often works with databases, queues, services. |
| Examples: Apache, NGINX, IIS. | Examples: Java application server, backend runtime, enterprise app platform. |

In modern web systems, the boundary can be blurry. For example, a backend framework can receive HTTP requests and execute application logic itself.

But for QA, it is useful to distinguish:

- the server returned a file;
- the server forwarded the request;
- application logic returned wrong data;
- the database saved wrong state.

## Web Server Configuration

Web server configuration affects reliability, performance, and security.

Administrators usually configure:

- ports;
- TLS certificates;
- virtual hosts;
- request limits;
- connection timeouts;
- cache behavior;
- compression;
- redirects;
- access logs;
- error logs;
- firewall rules;
- allowed file types;
- reverse proxy rules.

For QA, configuration bugs often look like:

- page not loading;
- `403 Forbidden`;
- `404 Not Found`;
- redirect loop;
- mixed content warning;
- CORS error;
- invalid certificate;
- file download instead of page rendering;
- stale cached file.

## Benefits Of Web Servers

Web servers provide:

- centralized content delivery;
- scalability;
- logging and auditing;
- uptime management;
- bandwidth control;
- support for static and dynamic content;
- secure access via HTTPS;
- support for multiple websites;
- integration with backend applications;
- backup and recovery options.

## Cloud Web Servers

A cloud web server is a virtual server in a cloud environment.

It performs the same tasks as a physical server, but it is usually easier to scale and manage through a cloud provider.

Advantages:

- scalable resources;
- high availability options;
- easier provisioning;
- monitoring integrations;
- backup and snapshot options;
- global deployment options.

For QA, cloud environments can add new testing areas:

- region-specific latency;
- autoscaling behavior;
- load balancer configuration;
- CDN cache;
- environment variables;
- deployment rollback.

## Web Server Security

Web server security is critical.

Without protection, a server may be vulnerable to:

- DoS attacks;
- SQL injection through backend;
- cross-site scripting impact;
- unpatched software vulnerabilities;
- unauthorized access;
- data leakage;
- misconfiguration.

Basic practices:

- keep software updated;
- disable unnecessary services;
- separate development, testing, and production environments;
- use firewall;
- automate backups;
- use HTTPS;
- restrict admin access;
- use least privilege;
- monitor logs;
- do regular security audits.

## What QA Should Test

QA does not always administer the web server, but should understand symptoms of server-side problems.

## Availability

Check:

- site opens;
- important pages return `200 OK`;
- health endpoints work;
- downtime is handled gracefully.

## Status Codes

Check:

- valid pages return correct status;
- missing pages return `404`;
- forbidden resources return `403`;
- server errors do not expose sensitive details;
- redirects use correct `301` or `302`.

## Static Files

Check:

- CSS loads;
- JS loads;
- images load;
- fonts load;
- files have correct MIME type;
- caching does not break updates.

## HTTPS And Certificates

Check:

- site opens over HTTPS;
- certificate is valid;
- no mixed content;
- HTTP redirects to HTTPS if expected.

## Error Handling

Check:

- user sees friendly error page;
- technical stack traces are not exposed;
- retry behavior is reasonable;
- logs contain useful diagnostic information.

## Performance

Check:

- response time;
- behavior under load;
- large file downloads;
- compression;
- caching;
- server behavior during traffic spikes.

## Example Bug Investigation

Bug:

```text
User opens product page, but images are missing.
```

QA investigation:

1. Open DevTools Network tab.
2. Check image requests.
3. Are image requests returning `200`, `404`, `403`, or `500`?
4. Is the path correct?
5. Is the file stored on server or CDN?
6. Is there a mixed content or certificate problem?
7. Is cache returning an old broken path?

This helps distinguish a UI rendering bug from a web server or hosting issue.

## Common Mistakes

Common mistakes in web server testing:

- checking only page content and ignoring Network tab;
- not checking status codes;
- ignoring redirects;
- not testing missing pages;
- not checking HTTPS;
- not checking static files separately;
- assuming `localhost` behavior equals production behavior;
- ignoring cache;
- not checking logs when server errors happen.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Web server | Hardware/software that processes HTTP/HTTPS requests and returns web content. |
| HTTP | Protocol used for communication between browser and web server. |
| HTTPS | Secure HTTP over TLS. |
| Static content | Content returned as stored, such as CSS, JS, images. |
| Dynamic content | Content generated or changed during request processing. |
| Localhost | Local machine used as server for development or testing. |
| XAMPP | Local development package that can run Apache, PHP, MariaDB and tools. |
| Apache | Popular open-source web server. |
| NGINX | Web server often used for static files, reverse proxying and load balancing. |
| IIS | Microsoft web server for Windows Server environments. |
| Tomcat | Java servlet container often used with Java web applications. |
| MIME type | Header that tells browser what kind of file was returned. |
| TLS certificate | Certificate used to secure HTTPS connection. |
| Reverse proxy | Server that receives requests and forwards them to another server. |
| CDN | Distributed network for delivering static or cached content closer to users. |

## Questions

### 1. What is a web server?

A web server is hardware and software that accepts HTTP/HTTPS requests and returns web content or responses.

### 2. What does a browser receive from a web server?

It can receive HTML, CSS, JavaScript, images, files, videos, API responses, or error responses.

### 3. What is the difference between static and dynamic content?

Static content is returned mostly as stored. Dynamic content is generated or changed during request processing.

### 4. Why is localhost useful?

It allows developers and QA to run a web server locally for testing without deploying to production.

### 5. How is web hosting different from a web server?

Web hosting is a service for placing a site online. A web server is the software/hardware that handles requests and serves content.

### 6. Why should QA check status codes?

Because status codes show whether the server returned success, redirect, client error, or server error.

### 7. What can cause missing images on a page?

Wrong path, missing file, `404`, permissions issue, CDN/cache problem, certificate issue, or mixed content.

### 8. Why is web server security important?

Because misconfigured or outdated servers can expose data, allow attacks, or make the application unavailable.

## What To Review Later

- Client-Server Architecture
- HTTP Status Codes
- HTTPS and TLS
- DevTools Network Tab
- Static vs Dynamic Content
- Reverse Proxy
- CDN
- Caching
- Web Server Logs
