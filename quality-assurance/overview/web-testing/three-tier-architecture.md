# Three-Tier Architecture

## Summary

Three-tier architecture - это архитектура приложения, где система разделена на три уровня:

- presentation tier;
- application tier;
- data tier.

Для QA это важно не как сухая теория, а как способ быстрее понимать, где живет defect:

- в UI;
- в business logic;
- в API или backend processing;
- в database;
- в коммуникации между уровнями.

Когда QA понимает tiers, тестирование становится точнее: мы не просто кликаем экран, а проверяем путь данных через систему.

## What Is Three-Tier Architecture?

Three-tier architecture делит приложение на три отдельные части. У каждой части своя ответственность.

| Tier | Main Responsibility |
| --- | --- |
| Presentation tier | User interface и взаимодействие с пользователем |
| Application tier | Business logic и обработка данных |
| Data tier | Хранение и управление данными |

Главная идея - separation of responsibilities. UI не должен напрямую работать с database, а database не должна решать, какие business rules применять к пользователю.

Каждый tier можно разрабатывать, масштабировать, обновлять и тестировать более независимо.

## Presentation Tier

Presentation tier - это пользовательский интерфейс приложения.

Именно здесь user взаимодействует с системой.

Примеры:

- web page;
- mobile application screen;
- desktop application UI;
- graphical user interface.

Для web applications presentation tier обычно состоит из:

- HTML;
- CSS;
- JavaScript;
- frontend frameworks.

## What Presentation Tier Does

Presentation tier:

- показывает информацию пользователю;
- собирает user input;
- выполняет простую client-side validation;
- отправляет действия пользователя в application tier;
- показывает результаты, сообщения и ошибки.

Пример:

Пользователь вводит login и password на странице входа. UI собирает эти данные и отправляет request на backend.

## QA Focus In Presentation Tier

QA проверяет:

- layout;
- forms;
- buttons;
- validation messages;
- responsiveness;
- browser compatibility;
- accessibility;
- UI state changes;
- error messages;
- client-side behavior.

Типичные bugs:

- button не работает;
- текст не помещается в блок;
- validation message не появляется;
- страница ломается на mobile;
- показывается неправильная ошибка;
- UI отправляет неправильный request payload.

## Application Tier

Application tier также называют:

- logic tier;
- middle tier;
- backend tier.

Это уровень business logic. Он получает данные от presentation tier, обрабатывает их и обращается к data tier.

Примеры технологий:

- Python;
- Java;
- PHP;
- Ruby;
- Node.js;
- C#;
- backend frameworks and services.

## What Application Tier Does

Application tier:

- проверяет business rules;
- обрабатывает user input;
- выполняет calculations;
- применяет permissions;
- обрабатывает API requests;
- создает, обновляет или удаляет данные;
- общается с databases и external services.

Пример:

Когда user оформляет order, backend проверяет availability товара, применяет discounts, считает taxes, создает order и отправляет запрос в payment service.

## QA Focus In Application Tier

QA проверяет:

- business rules;
- API behavior;
- request and response structure;
- authorization logic;
- calculations;
- error handling;
- integration with external services;
- data processing;
- backend validation.

Типичные bugs:

- discount считается неправильно;
- user может увидеть данные другого user;
- API возвращает неправильный status code;
- backend принимает invalid data;
- создается duplicate order;
- ошибка не обрабатывается корректно.

## Data Tier

Data tier - это уровень, где данные хранятся и управляются.

Он может включать:

- relational databases;
- NoSQL databases;
- file storage;
- cache;
- data warehouses.

Примеры:

- PostgreSQL;
- MySQL;
- MariaDB;
- Oracle;
- Microsoft SQL Server;
- MongoDB;
- Cassandra;
- CouchDB.

## What Data Tier Does

Data tier:

- stores data;
- retrieves data;
- updates records;
- manages relationships;
- enforces constraints;
- supports queries;
- protects data consistency.

Пример:

После создания order его details сохраняются в database.

## QA Focus In Data Tier

QA проверяет:

- данные сохраняются корректно;
- данные обновляются корректно;
- данные не дублируются;
- удаление работает ожидаемо;
- database constraints работают;
- data integrity сохраняется;
- migration не портит данные;
- reports используют правильные данные.

Типичные bugs:

- record не сохраняется;
- возвращаются данные неправильного user;
- появляются duplicate rows;
- status не обновляется;
- удаленный item все еще отображается;
- report использует устаревшие данные.

## Communication Between Tiers

В three-tier application коммуникация обычно идет через application tier.

Presentation tier не должен напрямую общаться с data tier.

Типичный flow:

```text
User Interface -> Application Tier -> Data Tier
Data Tier -> Application Tier -> User Interface
```

Это важно для security, maintainability и scalability.

Если UI напрямую ходит в database, становится сложнее контролировать permissions, validation, business rules и изменения схемы данных.

## Web Development Mapping

В web development tiers часто выглядят так:

| Architecture Tier | Web Example |
| --- | --- |
| Presentation tier | Browser, web page, frontend app |
| Application tier | Application server, API, backend service |
| Data tier | Database server |

Пример eCommerce flow:

1. User добавляет product в cart в browser.
2. Frontend отправляет request на backend.
3. Backend проверяет inventory и pricing.
4. Backend читает или записывает данные в database.
5. Backend отправляет response во frontend.
6. UI обновляет cart state.

## Benefits

## Faster Development

Разные команды могут работать над разными tiers параллельно.

Пример:

- frontend team строит UI;
- backend team строит API;
- database team работает со schema и queries;
- QA готовит проверки для каждого tier.

## Scalability

Каждый tier можно масштабировать отдельно.

Если растет UI traffic, можно масштабировать web servers. Если упираемся в database load, можно отдельно оптимизировать database resources, indexes или queries.

## Reliability

Если система спроектирована хорошо, проблема в одном tier не всегда ломает все приложение.

Пример:

Если reporting service временно работает плохо, login и базовые user actions могут продолжать работать.

## Security

Application tier становится контрольной точкой.

Он может:

- validate input;
- check permissions;
- block direct database access;
- reduce SQL injection risk;
- enforce business rules.

Presentation tier и data tier не должны общаться напрямую.

## Tiers Vs Layers

Слова tier и layer часто используют как синонимы, но между ними есть разница.

## Layer

Layer - это логическое разделение кода.

Пример:

- UI layer;
- business logic layer;
- data access layer.

Layers могут жить внутри одного приложения на одной машине.

## Tier

Tier - это физическое или infrastructure-level разделение.

Пример:

- web server;
- application server;
- database server.

Каждый tier может запускаться на отдельной infrastructure.

## Why The Difference Matters

Layers организуют code.

Tiers организуют runtime deployment.

Пример:

Mobile contacts app может иметь UI, logic и data layers, но если все они работают на телефоне, это не three-tier application.

## Two-Tier Architecture

Two-tier architecture обычно состоит из:

- presentation tier;
- data tier.

Business logic может находиться в client, database или частично в обоих местах.

В two-tier architecture client часто имеет direct access к data tier.

Пример:

Простое desktop application, которое напрямую подключается к database.

## N-Tier Architecture

N-tier architecture означает, что приложение имеет больше одного tier.

На практике этим термином часто называют системы с тремя и более tiers.

Дополнительные tiers могут включать:

- API gateway;
- caching tier;
- message queue;
- authentication service;
- reporting service;
- microservices layer.

Больше tiers может улучшить separation, но также добавляет complexity и latency.

## How This Helps QA

Three-tier architecture помогает QA локализовать defects.

Когда что-то ломается, стоит спросить:

- UI отправляет правильные данные?
- API получает request?
- Business logic обрабатывает данные правильно?
- Database сохраняет правильные values?
- Backend возвращает правильный response?
- UI правильно отображает response?

Так vague bug report превращается в нормальное investigation.

## Example Bug Investigation

Bug:

```text
User applies discount code, but total price is wrong.
```

QA может проверить:

1. Presentation tier: frontend отправил discount code?
2. Application tier: backend применил правильные business rules?
3. Data tier: discount configuration в database корректная?
4. Response: backend вернул правильный total?
5. UI: frontend правильно показал returned total?

Tier-based thinking помогает найти настоящий источник defect.

## Common Testing Areas

| Tier | Testing Focus |
| --- | --- |
| Presentation | UI, forms, layout, validation, browser compatibility |
| Application | API, business rules, authorization, calculations |
| Data | persistence, integrity, queries, migrations |
| Communication | request/response, status codes, payloads, timeouts |

## Common Mistakes

Частые ошибки:

- тестировать только UI и игнорировать backend behavior;
- считать, что каждый UI bug - это frontend bug;
- не проверять request payloads;
- не проверять database state;
- не тестировать error handling между tiers;
- игнорировать authorization в application tier;
- не проверять data consistency после updates.

## Key Idea

Three-tier architecture разделяет UI, business logic и data storage.

Для QA это разделение делает testing и debugging намного понятнее.

Главная мысль:

> Когда ты понимаешь tiers, ты тестируешь систему, а не просто кликаешь экран.

## Questions

### 1. Какие три уровня есть в three-tier architecture?

Presentation tier, application tier и data tier.

### 2. За что отвечает presentation tier?

За user interface: отображение данных, сбор user input, client-side behavior и передачу действий пользователя в backend.

### 3. За что отвечает application tier?

За business logic, API behavior, validation, permissions, calculations и связь с database или external services.

### 4. Почему presentation tier не должен напрямую обращаться к data tier?

Потому что это ухудшает security, maintainability и control over business rules. Доступ к данным должен проходить через application tier.

### 5. Чем tier отличается от layer?

Layer - логическое разделение кода. Tier - физическое или infrastructure-level разделение runtime частей системы.

### 6. Как QA может использовать three-tier thinking при анализе bug?

QA может пройти цепочку UI -> API -> backend logic -> database -> response -> UI и понять, на каком уровне появляется ошибка.

## What To Review Later

- Client-Server Architecture
- API Testing
- HTTP
- Database Testing
- DevTools Network Tab
- Authorization
