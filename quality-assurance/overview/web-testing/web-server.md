# Web Server

## Summary

Web server - это hardware и software, которые принимают requests от clients и возвращают web content через HTTP или HTTPS.

Проще:

- browser просит страницу, файл или данные;
- web server принимает request;
- находит или генерирует нужный response;
- отправляет response обратно browser.

Для QA web server важен потому, что многие "UI problems" на самом деле связаны с server response, missing files, wrong status code, redirects, cache, permissions или server errors.

Главная мысль:

> Web server - это место, где browser request превращается в response, который видит user.

## What Is A Web Server?

Web server можно понимать в двух смыслах:

| Meaning | Explanation |
| --- | --- |
| Hardware | Физическая или virtual machine, где размещены website files, application files или services. |
| Software | Программа, которая принимает HTTP/HTTPS requests и возвращает responses. |

Примеры web server software:

- Apache HTTP Server;
- NGINX;
- Microsoft IIS;
- lighttpd;
- Apache Tomcat.

Web server может отдавать:

- HTML;
- CSS;
- JavaScript;
- images;
- videos;
- files for download;
- API responses;
- dynamically generated pages.

## Why We Use Web Servers

Web servers нужны, чтобы делать websites and web applications доступными через network или internet.

Они помогают:

- store website data;
- deliver website content;
- process HTTP/HTTPS requests;
- control access to hosted files;
- manage traffic;
- support server-side scripting;
- host multiple websites or applications;
- log requests and errors;
- improve security.

Без web server browser не сможет просто так получить page по URL.

## How A Web Server Works

Обычный flow выглядит так:

1. User вводит URL или кликает link.
2. Browser определяет IP address server через DNS.
3. Browser отправляет HTTP или HTTPS request.
4. Web server принимает request.
5. Server ищет нужный file или передает request в application logic.
6. Server возвращает response.
7. Browser отображает page или обрабатывает data.

Упрощенно:

```text
Browser -> HTTP/HTTPS Request -> Web Server
Browser <- HTTP/HTTPS Response <- Web Server
```

Если file не найден, server может вернуть `404 Not Found`. Если server сломался при обработке request, user может получить `500 Internal Server Error`.

## Static And Dynamic Content

Web server может отдавать static или dynamic content.

## Static Content

Static content отправляется browser почти без изменений.

Примеры:

- HTML file;
- CSS file;
- JavaScript file;
- image;
- PDF;
- font file.

Static web server просто берет hosted file и возвращает его client.

Пример:

```text
GET /styles.css -> web server returns styles.css
```

## Dynamic Content

Dynamic content создается или изменяется во время request.

Для этого web server может взаимодействовать с:

- application server;
- database;
- cache;
- external API;
- server-side scripts.

Пример:

```text
GET /profile -> server checks logged-in user -> returns that user's profile page
```

Dynamic content гибче, но сложнее для testing, потому что response зависит от user, session, data, permissions, time, feature flags и других условий.

## Web Server Architecture

Web server architecture описывает, как server принимает, обрабатывает и распределяет requests.

На architecture влияют:

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

Для QA это важно при performance testing, reliability checks и troubleshooting.

## Concurrent Approach

Concurrent approach позволяет web server обрабатывать multiple client requests одновременно.

Варианты:

- multi-process;
- multithreaded;
- hybrid.

## Multi-Process

Parent process создает child processes. Каждый child process может обрабатывать отдельный request.

Такой подход изолирует обработку, но может потреблять больше resources.

## Multithreaded

Server использует threads для обработки multiple requests.

Это может быть эффективнее по ресурсам, но требует аккуратной работы с shared state.

## Hybrid

Hybrid approach комбинирует processes и threads.

Пример:

Server запускает несколько processes, а внутри каждого process несколько threads.

## Single-Process Event-Driven Approach

Single-process event-driven approach использует один process, который обрабатывает multiple connections через event loop.

Такой подход может быть эффективным для большого количества concurrent connections, особенно когда server часто ждет network или file I/O.

## Common Types Of Web Servers

## Apache HTTP Server

Apache - один из самых известных web servers.

Особенности:

- open-source;
- работает на Linux, Windows, macOS;
- поддерживает modules;
- часто используется для classic web hosting.

## NGINX

NGINX часто используется как:

- web server;
- reverse proxy;
- load balancer;
- static file server.

Он хорошо известен работой с большим количеством concurrent connections.

## Microsoft IIS

IIS, Internet Information Services, - web server от Microsoft.

Обычно используется в Windows Server environments и хорошо интегрируется с Microsoft ecosystem.

## Apache Tomcat

Tomcat часто используют для Java web applications.

Технически его часто называют servlet container, но в учебных материалах он также встречается рядом с web servers.

## lighttpd

lighttpd - lightweight web server, который рассчитан на low memory and CPU usage.

Может использоваться в embedded devices, routers, cameras и других constrained environments.

## Localhost And XAMPP

Web server может работать не только на production server, но и локально.

Localhost - это твой собственный computer как server для testing или development.

Пример URL:

```text
http://localhost/index.html
```

XAMPP - один из популярных local development packages. Он может включать Apache, PHP, MariaDB и другие tools.

Пример local flow:

1. Установить XAMPP.
2. Поместить `index.html` в folder вроде `htdocs`.
3. Запустить Apache.
4. Открыть `http://localhost/index.html` в browser.

Для QA это полезно, когда нужно быстро проверить static page, prototype или local web app.

## Web Hosting Vs Web Server

Web hosting и web server связаны, но это не одно и то же.

| Aspect | Web Hosting | Web Server |
| --- | --- | --- |
| Meaning | Service, который размещает сайт в internet. | Hardware/software, который обрабатывает requests и отдает content. |
| Purpose | Дать storage, network access и management для сайта. | Принять request и вернуть response. |
| Ownership | Обычно hosting provider. | Может принадлежать provider, company или developer. |
| Examples | GoDaddy, Bluehost, HostGator, cloud hosting. | Apache, NGINX, IIS, Tomcat. |

Просто:

> Hosting - это услуга размещения. Web server - это механизм, который обслуживает requests.

## Web Server Vs Application Server

Web server и application server тоже часто путают.

| Web Server | Application Server |
| --- | --- |
| Лучше подходит для static content. | Лучше подходит для business logic и dynamic behavior. |
| Основные protocols: HTTP/HTTPS. | Может использовать HTTP, RPC, RMI и другие protocols. |
| Часто отдает HTML, CSS, JS, images. | Выполняет application code, rules, workflows. |
| Может работать как reverse proxy. | Часто работает с database, queues, services. |
| Примеры: Apache, NGINX, IIS. | Примеры: Java application server, backend runtime, enterprise app platform. |

В современных web systems граница может быть размытой. Например, backend framework может сам принимать HTTP requests и выполнять application logic.

Но для QA полезно различать:

- server отдал файл;
- server прокинул request дальше;
- application logic вернула wrong data;
- database сохранила wrong state.

## Web Server Configuration

Web server configuration влияет на reliability, performance и security.

Администраторы обычно настраивают:

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

Для QA configuration bugs часто выглядят как:

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

Web servers дают:

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

Cloud web server - это virtual server в cloud environment.

Он выполняет те же задачи, что и physical server, но обычно проще масштабируется и управляется через cloud provider.

Преимущества:

- scalable resources;
- high availability options;
- easier provisioning;
- monitoring integrations;
- backup and snapshot options;
- global deployment options.

Для QA cloud environment может добавлять новые testing areas:

- region-specific latency;
- autoscaling behavior;
- load balancer configuration;
- CDN cache;
- environment variables;
- deployment rollback.

## Web Server Security

Web server security критически важна.

Без защиты server может быть уязвим к:

- DoS attacks;
- SQL injection через backend;
- cross-site scripting impact;
- unpatched software vulnerabilities;
- unauthorized access;
- data leakage;
- misconfiguration.

Базовые practices:

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

QA не всегда администрирует web server, но должен понимать симптомы server-side проблем.

## Availability

Проверить:

- site opens;
- important pages return `200 OK`;
- health endpoints work;
- downtime is handled gracefully.

## Status Codes

Проверить:

- valid pages return correct status;
- missing pages return `404`;
- forbidden resources return `403`;
- server errors do not expose sensitive details;
- redirects use correct `301` or `302`.

## Static Files

Проверить:

- CSS loads;
- JS loads;
- images load;
- fonts load;
- files have correct MIME type;
- caching does not break updates.

## HTTPS And Certificates

Проверить:

- site opens over HTTPS;
- certificate is valid;
- no mixed content;
- HTTP redirects to HTTPS if expected.

## Error Handling

Проверить:

- user sees friendly error page;
- technical stack traces are not exposed;
- retry behavior is reasonable;
- logs contain useful diagnostic information.

## Performance

Проверить:

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

This helps distinguish UI rendering bug from web server or hosting issue.

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

Web server is hardware and software that accepts HTTP/HTTPS requests and returns web content or responses.

### 2. What does a browser receive from a web server?

It can receive HTML, CSS, JavaScript, images, files, videos, API responses or error responses.

### 3. What is the difference between static and dynamic content?

Static content is returned mostly as stored. Dynamic content is generated or changed during request processing.

### 4. Why is localhost useful?

It allows developers and QA to run a web server locally for testing without deploying to production.

### 5. How is web hosting different from a web server?

Web hosting is a service for placing a site online. Web server is the software/hardware that handles requests and serves content.

### 6. Why should QA check status codes?

Because status codes show whether the server returned success, redirect, client error or server error.

### 7. What can cause missing images on a page?

Wrong path, missing file, `404`, permissions issue, CDN/cache problem, certificate issue or mixed content.

### 8. Why is web server security important?

Because misconfigured or outdated servers can expose data, allow attacks or make the application unavailable.

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
