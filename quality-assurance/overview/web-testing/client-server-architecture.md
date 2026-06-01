# Client-Server Architecture

## Summary

Client-server architecture - это модель, в которой одни участники системы запрашивают service, а другие предоставляют его.

В этой модели:

- client отправляет request;
- server обрабатывает request;
- server возвращает response;
- network соединяет client и server.

Для web testing это базовая тема. Почти каждое действие в браузере - login, search, checkout, загрузка страницы, отправка формы - превращается в request от client к server и response обратно.

Главная мысль:

> QA должен видеть не только экран, но и обмен данными между client и server.

## What Is Client-Server Architecture?

Client-server architecture - это computing model, где server хранит, обрабатывает или предоставляет resources and services, а client их запрашивает.

Простая аналогия:

Пользователь заказывает pizza delivery. Пользователь делает заказ, магазин принимает его, готовит pizza и доставляет результат. В этой аналогии:

- user - client;
- pizza store - server;
- order - request;
- delivered pizza - response.

В IT это работает похоже:

- browser просит web page;
- mail client просит отправить или получить email;
- mobile app просит backend вернуть user profile;
- desktop app просит database сохранить record.

## Client And Server

## Client

Client - это сторона, которая запрашивает service.

Примеры clients:

- browser;
- mobile app;
- desktop application;
- email client;
- API client;
- QA tool вроде Postman.

Client обычно отвечает за user interaction: показать interface, собрать input и отправить request.

## Server

Server - это сторона, которая предоставляет service или resource.

Примеры servers:

- web server;
- file server;
- mail server;
- database server;
- application server.

Server обычно мощнее client, потому что может одновременно обслуживать много users и хранить централизованные данные.

## Everyday Examples

## Mail Server

Mail servers используются для отправки и получения emails.

Client может быть:

- Gmail web interface;
- Outlook;
- mobile mail app.

Server хранит emails, обрабатывает отправку и доставку, проверяет rules and authentication.

## File Server

File server хранит files в одном месте, чтобы разные users могли получить к ним доступ.

Пример:

Ты создаешь документ в Google Docs на laptop, а потом открываешь его с phone. Файл физически хранится не только на твоем устройстве, а в central storage.

## Web Server

Web server обслуживает websites and web applications.

Browser отправляет request, server возвращает HTML, CSS, JavaScript, images или API response.

Для QA это особенно важно, потому что UI bug может на самом деле быть:

- wrong response from server;
- network error;
- missing file;
- backend validation issue;
- cache problem.

## Components Of Client-Server Architecture

В классическом описании client-server architecture часто выделяют три компонента:

- workstations или client computers;
- servers;
- networking devices.

## Workstations

Workstations - это client computers, которые отправляют requests к server.

Они могут запускать applications, отображать UI и обращаться к shared files или databases через network.

Пример:

В hospital system workstation может использоваться для ввода patient information. Server в это время хранит и управляет общей database.

## Servers

Servers - это устройства или приложения, которые централизованно предоставляют resources.

Server может выполнять одну или несколько ролей:

- mail server;
- database server;
- file server;
- domain controller;
- web server;
- application server.

Server должен выдерживать multiple requests from different clients.

## Networking Devices

Networking devices соединяют clients и servers.

Примеры:

- switch;
- router;
- hub;
- repeater;
- bridge;
- firewall;
- access point.

Для web testing важны не только сами devices, а факт, что client-server communication зависит от network. Если network нестабильна, user может видеть timeouts, partial loading, failed requests или duplicate actions.

## How Client-Server Architecture Works In Web

Рассмотрим обычную загрузку сайта в browser.

1. User вводит URL в address bar.
2. Browser обращается к DNS, чтобы найти IP address нужного server.
3. DNS возвращает IP address.
4. Browser отправляет HTTP или HTTPS request на web server.
5. Server обрабатывает request.
6. Server возвращает нужные files или data.
7. Browser обрабатывает response и показывает page.

Упрощенный flow:

```text
Browser -> DNS -> IP address
Browser -> Web Server -> Response
Browser -> Rendered Page
```

Если открыть DevTools Network tab, можно увидеть эти requests and responses почти вживую.

## Request And Response

Client-server interaction обычно строится вокруг request-response model.

Client request может содержать:

- URL;
- HTTP method;
- headers;
- cookies;
- query parameters;
- request body.

Server response может содержать:

- status code;
- headers;
- response body;
- cookies;
- error message;
- redirected location.

Для QA это один из главных источников информации при troubleshooting.

## Types Of Client-Server Architecture

Client-server architecture может быть организована в tiers.

## 1-Tier Architecture

В 1-tier architecture presentation, business logic и data могут находиться в одной системе.

Пример:

Standalone desktop application, где UI, logic и local data storage находятся на одном устройстве.

Плюсы:

- простая установка;
- все рядом;
- может работать без network.

Минусы:

- сложно масштабировать;
- сложнее централизованно обновлять;
- выше риск дублирования данных.

## 2-Tier Architecture

В 2-tier architecture обычно есть:

- client side с UI;
- server side с database или shared service.

Client может напрямую обращаться к database server.

Пример:

Desktop application, которая подключается напрямую к central database.

Плюсы:

- меньше intermediate layers;
- может быть быстрее для простых systems;
- проще понять flow.

Минусы:

- direct database access может быть security risk;
- business logic может оказаться размазанной между client и database;
- сложнее поддерживать большие приложения.

## 3-Tier Architecture

В 3-tier architecture между client и database появляется application tier или middleware.

Обычно есть:

- presentation tier;
- application tier;
- data tier.

Flow:

```text
Client -> Application Tier -> Data Tier
```

Application tier контролирует business logic, validation, permissions и доступ к data.

Это более безопасный и управляемый подход для многих web applications.

## N-Tier Architecture

N-tier architecture - это расширенная модель, где tiers может быть больше трех.

Дополнительные tiers могут включать:

- API gateway;
- authentication service;
- caching layer;
- message queue;
- reporting service;
- microservices;
- CDN.

Чем больше tiers, тем лучше separation of concerns, но тем сложнее testing, monitoring и troubleshooting.

## Client-Server Vs Peer-To-Peer

Client-server architecture и peer-to-peer architecture решают разные задачи.

| Client-Server | Peer-to-Peer |
| --- | --- |
| Есть отдельные clients и servers | Участники могут быть равноправными peers |
| Data management часто centralized | Каждый peer может хранить свои data |
| Client обычно запрашивает service | Peer может и запрашивать, и предоставлять service |
| Хорошо подходит для small and large networks | Обычно подходит для меньших сетей |
| Server становится central control point | Нет единой центральной точки управления |

Для web testing чаще всего важна client-server model, потому что browser обычно выступает client, а backend или web server - server.

## Advantages

Client-server architecture дает несколько важных преимуществ.

## Centralized Management

Data, rules и permissions можно управлять централизованно.

Это удобно для:

- access control;
- backups;
- audit;
- updates;
- monitoring.

## Resource Sharing

Несколько clients могут использовать одни и те же resources:

- files;
- databases;
- printers;
- APIs;
- authentication services.

## Better User Experience

Client может быть легким и удобным, а тяжелая обработка остается на server.

Пример:

Browser показывает UI, а backend считает prices, проверяет permissions и работает с database.

## Easier Maintenance

Если business logic живет на server, ее можно обновить централизованно, не обновляя вручную каждое client device.

## Disadvantages

## Server Dependency

Если central server недоступен, clients могут потерять доступ к service.

Пример:

Если authentication server down, users не смогут login.

## Cost

Servers, infrastructure, monitoring, backups и security требуют расходов.

## Traffic Congestion

Если слишком много clients одновременно обращаются к server, может возникнуть overload:

- slow responses;
- timeouts;
- failed requests;
- degraded user experience.

## Maintenance Complexity

Client-server systems требуют technical maintenance:

- server updates;
- database backups;
- network configuration;
- access control;
- performance monitoring;
- security patches.

## What QA Should Test

Для QA client-server architecture помогает строить проверки по слоям взаимодействия.

## UI Behavior

Проверяем, что client:

- корректно собирает input;
- показывает loading states;
- правильно отображает success and error messages;
- не ломается при slow response;
- не отправляет duplicate requests без причины.

## Network Requests

Проверяем в DevTools или API tools:

- правильный endpoint;
- правильный HTTP method;
- status code;
- request payload;
- response body;
- headers;
- cookies;
- redirects.

## Server Behavior

Проверяем:

- business validation;
- authorization;
- error handling;
- rate limits;
- database updates;
- correct response for invalid input.

## Failure Scenarios

Очень важны negative scenarios:

- server returns `500`;
- network timeout;
- slow response;
- invalid session;
- expired token;
- DNS issue;
- duplicate submit;
- offline mode.

Пользователь не должен видеть хаос. Даже при server error UI должен показать понятное сообщение и не испортить данные.

## Example Bug Investigation

Bug:

```text
User clicks Save, but changes disappear after page refresh.
```

QA investigation:

1. Client: button click действительно отправляет request?
2. Request: payload содержит новые values?
3. Server: response возвращает success или error?
4. Data: values реально сохранились в database?
5. UI: после refresh frontend берет fresh data или показывает cached state?

Такой подход помогает не гадать, а локализовать проблему.

## Common Mistakes

Частые ошибки при тестировании client-server systems:

- проверять только UI и не смотреть Network tab;
- не различать frontend bug и backend bug;
- игнорировать status codes;
- не проверять payload;
- не тестировать server errors;
- не проверять behavior на slow network;
- считать, что если message на экране зеленый, данные точно сохранились;
- не проверять database или API response после actions.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Client | Сторона, которая запрашивает service или resource. |
| Server | Сторона, которая предоставляет service, resource или обработку. |
| Request | Сообщение от client к server. |
| Response | Ответ server на request. |
| DNS | Сервис, который помогает найти IP address по domain name. |
| HTTP/HTTPS | Protocols, по которым browser общается с web server. |
| Web server | Server, который отдает web pages, static files или responses. |
| Application server | Server, где обычно живет business logic. |
| File server | Server для централизованного хранения files. |
| Mail server | Server для отправки и получения emails. |
| Peer-to-peer | Модель, где participants могут одновременно запрашивать и предоставлять services. |
| N-tier architecture | Architecture с несколькими tiers, часто больше трех. |

## Questions

### 1. Что такое client-server architecture?

Это модель, где client запрашивает service или resource, а server обрабатывает request и возвращает response.

### 2. Что делает client?

Client отправляет requests, показывает UI, собирает user input и отображает response.

### 3. Что делает server?

Server предоставляет services, хранит или обрабатывает data, выполняет business logic и отвечает clients.

### 4. Как browser загружает сайт в client-server model?

Browser получает IP через DNS, отправляет HTTP/HTTPS request на web server, получает response и отображает page.

### 5. Чем client-server отличается от peer-to-peer?

В client-server есть отдельные роли client и server. В peer-to-peer участники могут быть равноправными и одновременно запрашивать или предоставлять services.

### 6. Почему QA важно смотреть Network tab?

Потому что там видно реальные requests, responses, status codes, payloads и errors между client и server.

### 7. Что может случиться, если central server down?

Clients могут потерять доступ к service, например users не смогут login или загрузить data.

### 8. Почему success message на UI не всегда доказывает, что данные сохранились?

Потому что UI может показать message ошибочно. Нужно проверить server response, API result или database state.

## What To Review Later

- HTTP and HTTPS
- DNS
- DevTools Network Tab
- API Testing
- Three-Tier Architecture
- Status Codes
- Client-Side Validation
- Server-Side Validation
