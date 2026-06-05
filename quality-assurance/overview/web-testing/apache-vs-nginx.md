# Apache Vs Nginx

Source: pasted article about Apache vs Nginx  
Date added: 2026-06-05  
Related plan item: Web Testing  
Tags: QA, web testing, web server, Apache, Nginx, reverse proxy, performance  
Language: Russian  
Translation pair: quality-assurance-en/overview/web-testing/apache-vs-nginx.md

## Summary

Apache и Nginx - два популярных open-source web servers. Оба принимают HTTP/HTTPS requests и возвращают responses, но отличаются архитектурой, производительностью, конфигурацией и типичными сценариями использования.

Главная мысль:

> Apache чаще выбирают за гибкость и совместимость, а Nginx - за эффективность, reverse proxy, load balancing и работу с высокой concurrency.

Для QA это важно, потому что web server влияет на redirects, static files, caching, headers, compression, TLS, error pages, request limits и поведение приложения под нагрузкой.

## Key Points

- Apache использует process/thread-based подход и хорошо подходит для flexible configuration, legacy apps и большого набора modules.
- Nginx использует event-driven asynchronous architecture и обычно лучше справляется с большим количеством concurrent connections.
- Apache поддерживает `.htaccess`, что удобно для directory-level configuration, но может стоить производительности.
- Nginx часто используют как reverse proxy, load balancer и server для static content.
- На практике Apache и Nginx могут работать вместе: Nginx принимает traffic снаружи и проксирует requests на Apache/backend.

## Notes

## Why QA Should Know Apache And Nginx

QA не обязан администрировать production server, но должен понимать, что часть web bugs появляется не в frontend и не в backend code, а на уровне web server configuration.

Примеры:

- static file возвращает `404`;
- после deploy browser получает старый CSS из cache;
- HTTP redirects ведут не туда;
- request body слишком большой и server возвращает `413`;
- API request timeout появляется только через proxy;
- HTTPS certificate настроен неправильно;
- security headers отсутствуют;
- compression ломает response;
- upload работает локально, но падает на staging из-за server limits.

Если QA понимает роль web server, bug report становится точнее.

## What Apache And Nginx Do

Оба web servers могут:

- принимать HTTP/HTTPS requests;
- отдавать static files;
- проксировать traffic на application server;
- управлять redirects;
- настраивать headers;
- писать access/error logs;
- поддерживать TLS/SSL;
- работать с compression;
- ограничивать requests;
- обслуживать несколько websites через virtual hosts/server blocks.

Но они делают это по-разному.

## Apache: Traditional And Flexible

Apache HTTP Server долго был standard choice для web hosting.

Его сильные стороны:

- большая история и mature ecosystem;
- много documentation и examples;
- широкий набор modules;
- хорошая совместимость с legacy applications;
- `.htaccess` для directory-level configuration;
- удобен для shared hosting;
- гибкая настройка authentication, URL rewriting, caching и access control.

Apache может использовать process-based или threaded model. В упрощении это значит, что server выделяет отдельный handler/thread/process для обработки incoming requests.

Плюсы:

- проще понять новичкам;
- много готовых recipes;
- удобно менять конфигурацию на уровне directory;
- хорошо работает с классическими PHP/legacy setups.

Минусы:

- может потреблять больше memory;
- хуже справляется с очень большим количеством concurrent connections;
- `.htaccess` может снижать performance, потому что server проверяет файлы конфигурации во время request processing;
- гибкость иногда приводит к сложной конфигурации.

## Nginx: Event-Driven And Efficient

Nginx создавался как high-performance web server для большого количества simultaneous connections.

Его architecture:

- master process управляет workers;
- worker processes обрабатывают много connections через event loop;
- server не создает отдельный process на каждый connection.

Сильные стороны Nginx:

- высокая concurrency;
- низкое resource usage;
- быстрый static content serving;
- reverse proxy;
- load balancing;
- TLS termination;
- caching;
- хорош для VPS, containers и cloud environments.

Плюсы:

- эффективно обрабатывает много connections;
- хорошо подходит для high-traffic sites;
- часто проще как front proxy;
- стабилен для static assets;
- удобен в microservices/container environments.

Минусы:

- нет `.htaccess`;
- часть changes требует reload config;
- меньше built-in modules, чем у Apache;
- configuration style может быть сложнее для beginners;
- dynamic module ecosystem менее гибкая, чем у Apache в некоторых сценариях.

## Key Differences

| Area | Apache | Nginx |
| --- | --- | --- |
| Architecture | Process/thread-based. | Event-driven asynchronous. |
| Concurrency | Может потреблять больше ресурсов при большом количестве connections. | Хорошо держит много concurrent connections. |
| Static files | Хорошо, но часто менее эффективно под высокой нагрузкой. | Очень хорошо и эффективно. |
| Dynamic content | Часто работает напрямую с modules/interpreters. | Обычно проксирует dynamic requests на backend/application server. |
| Configuration | `.htaccess`, virtual hosts, modules. | Central config, server blocks, location blocks. |
| Reverse proxy | Возможен. | Один из сильнейших сценариев. |
| Load balancing | Возможен через modules. | Частый built-in use case. |
| Learning curve | Обычно проще для classic hosting. | Требует понимания proxy/location/config rules. |
| Legacy compatibility | Очень сильная. | Хорошая, но не всегда замена legacy Apache setups. |

## Apache Configuration Notes

Apache часто использует:

- `httpd.conf` или `apache2.conf`;
- virtual hosts;
- `.htaccess`;
- modules вроде `mod_rewrite`, `mod_ssl`, `mod_headers`;
- directory-level rules.

Для QA `.htaccess` важен, потому что он может влиять на:

- redirects;
- URL rewriting;
- access permissions;
- caching;
- custom error pages;
- auth rules.

Пример проблемы:

На staging URL `/profile` работает, а `/profile/` делает неправильный redirect. Причина может быть в rewrite rule.

## Nginx Configuration Notes

Nginx часто использует:

- `nginx.conf`;
- `server` blocks;
- `location` blocks;
- `proxy_pass`;
- `try_files`;
- `upstream`;
- `add_header`;
- `client_max_body_size`.

Для QA Nginx важен, потому что он часто стоит перед application server.

Пример:

Frontend отправляет upload 20 MB, но Nginx возвращает `413 Request Entity Too Large`, потому что `client_max_body_size` меньше нужного значения.

## Reverse Proxy

Reverse proxy принимает request от client и передает его дальше на backend server.

Nginx часто используют так:

```text
Browser -> Nginx -> Application server -> Database
```

Зачем это нужно:

- TLS termination;
- routing requests;
- load balancing;
- caching;
- hiding internal services;
- rate limiting;
- compression;
- centralized access logs.

QA должен понимать, что response может быть изменен или заблокирован reverse proxy до того, как request дошел до backend.

## Load Balancing

Load balancing распределяет traffic между несколькими backend instances.

Пример:

```text
Browser -> Nginx -> app-1 / app-2 / app-3
```

Что может пойти не так:

- один instance имеет старую версию;
- session не закреплена за нужным server;
- sticky sessions настроены неправильно;
- health check пропускает broken instance;
- часть users получает intermittent errors.

QA может заметить такие баги как "плавающие": один refresh работает, другой падает.

## Which One To Choose

Выбор зависит от context.

Apache может быть хорошим выбором, если:

- нужна максимальная compatibility;
- проект legacy;
- используется shared hosting;
- важны `.htaccess` rules;
- нужны specific Apache modules;
- команда хорошо знает Apache.

Nginx может быть хорошим выбором, если:

- ожидается high traffic;
- нужны reverse proxy и load balancing;
- важно low memory usage;
- много static assets;
- приложение работает в containers/cloud;
- нужно эффективно держать много open connections.

На практике часто используют оба:

```text
Internet -> Nginx -> Apache/backend app
```

Nginx принимает внешний traffic, отдает static files, завершает TLS и проксирует dynamic requests.

## QA Checklist

При тестировании приложения за Apache/Nginx проверить:

- correct HTTP status codes;
- redirects: HTTP -> HTTPS, trailing slash, canonical URLs;
- static files load: CSS, JS, images, fonts;
- cache headers;
- compression headers;
- CORS headers;
- security headers;
- cookies flags;
- file upload limits;
- request timeout behavior;
- custom error pages;
- access control for private paths;
- logs contain enough request information;
- behavior under concurrent users;
- same behavior across instances behind load balancer.

## Common Bugs

Типичные server-related bugs:

- `404` for static assets after deploy;
- `403 Forbidden` because of permissions;
- infinite redirect loop;
- wrong HTTP -> HTTPS redirect;
- old JS/CSS served from cache;
- missing `Content-Type`;
- missing `Cache-Control`;
- missing security headers;
- upload blocked by size limit;
- API timeout at proxy layer;
- WebSocket not upgraded correctly;
- backend response works directly but fails through proxy;
- one load-balanced instance returns different result.

## Bug Report Tips

Для server/proxy bugs указать:

- URL;
- environment;
- browser/client;
- exact status code;
- request method;
- request/response headers;
- response body or error page;
- timestamp;
- whether issue reproduces after cache clear;
- whether issue happens directly against backend or only through proxy;
- logs/correlation id, если доступно.

Пример:

> Upload fails on staging through Nginx with `413 Request Entity Too Large` for files above 10 MB. Same file uploads successfully against local backend. Expected limit is 25 MB. Request timestamp: 2026-06-05 14:10 UTC.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Apache HTTP Server | Flexible open-source web server with broad module support and `.htaccess`. |
| Nginx | Event-driven web server often used for static files, reverse proxy and load balancing. |
| `.htaccess` | Apache directory-level configuration file. |
| Reverse proxy | Server that accepts client requests and forwards them to backend servers. |
| Load balancer | Component that distributes traffic across multiple backend instances. |
| Worker process | Process that handles connections in Nginx architecture. |
| Virtual host | Apache configuration for hosting multiple sites/domains. |
| Server block | Nginx configuration block for a site/domain. |
| `proxy_pass` | Nginx directive that forwards requests to another server. |
| `client_max_body_size` | Nginx directive controlling maximum request body size. |

## Questions

### 1. Чем Apache и Nginx отличаются архитектурно?

Answer: Apache чаще использует process/thread-based model, а Nginx использует event-driven asynchronous model.

### 2. Почему Nginx часто выбирают для high-traffic сайтов?

Answer: Он эффективно обрабатывает много concurrent connections с меньшим потреблением ресурсов.

### 3. Что такое `.htaccess`?

Answer: Это Apache file для directory-level configuration, например redirects, rewrite rules, access control и cache rules.

### 4. Что такое reverse proxy?

Answer: Server, который принимает request от client и передает его на backend server.

### 5. Какой server чаще используют как reverse proxy и load balancer?

Answer: Nginx.

### 6. Какой bug может быть связан с `client_max_body_size`?

Answer: File upload может падать с `413 Request Entity Too Large`.

### 7. Почему QA нужно знать, какой web server используется?

Answer: Потому что redirects, headers, cache, static files, limits, TLS, proxy behavior и error pages могут зависеть от web server configuration.

## What To Review Later

- Apache process/thread-based model vs Nginx event-driven model.
- `.htaccess`, virtual hosts, server blocks и location blocks.
- Reverse proxy и load balancing.
- Server-related bugs: redirects, cache, upload limits, headers, static files.
- Что добавить в bug report для web server issue.
