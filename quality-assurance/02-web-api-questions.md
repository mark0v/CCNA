# Web, Desktop и REST API Questions

Source: Interview Prep  
Date added: 2026-05-25  
Related plan item: QA interview preparation  
Tags: QA, API testing, REST, HTTP, Postman, web testing  
Language: Russian  

## Summary

Материал помогает повторить web/desktop testing, REST API validation, backend-heavy функциональность, client-server взаимодействие, интеграционное тестирование и типовые вопросы по HTTP, Postman, cookies, storage и cache.

## Key Points

- API contract описывает endpoints, методы, request/response, обязательные поля, типы, status codes, ошибки и правила доступа.
- QA проверяет не только status code, но и соответствие ответа ситуации, структуру body, auth, validation, данные на backend и error handling.
- HTTP methods отличаются не названием, а семантикой: GET получает данные, POST выполняет действие или создает ресурс, PUT заменяет, PATCH меняет частично.
- Postman удобно использовать для collections, environments, переменных, smoke API checks и базовых tests.
- Cookies, Web Storage и Cache решают разные задачи и дают разные QA-риски.

## Заметки

- Делаем упор на практические QA-ответы, а не только на теорию.
- По возможности связываем ответы с контекстом poker platform: реальные пользователи, высокая нагрузка, real-time gameplay, money/risk-sensitive flows, CI/CD и частые релизы.

## 1. Что и как проверить в контрактах API

**API contract** - это договоренность между клиентом и сервером: какие endpoints есть, какие request/response они принимают и возвращают, какие поля обязательны, какие типы данных используются, какие status codes и ошибки возможны.

Что проверять в API-контракте:

- **Endpoint и HTTP method** - правильный URL и метод: GET, POST, PUT, PATCH, DELETE.
- **Request parameters** - path params, query params, headers, body.
- **Required/optional fields** - какие поля обязательные, какие необязательные.
- **Data types** - string, number, boolean, array, object, enum, date/time format.
- **Validation rules** - min/max length, allowed values, numeric ranges, required format.
- **Response structure** - все ли поля возвращаются, правильные ли типы и вложенность.
- **Status codes** - корректные коды для success и error cases.
- **Error response format** - единый формат ошибок: code, message, details, field errors.
- **Authentication/authorization** - нужен ли token, какие роли имеют доступ.
- **Backward compatibility** - не сломался ли старый клиент после изменения API.
- **Idempotency** - особенно для опасных операций: повторный request не должен создавать некорректное состояние.

Как проверять:

1. Сравнить API с документацией: Swagger/OpenAPI, Confluence, Jira, spec.
2. Отправить positive requests с валидными данными.
3. Проверить negative cases: отсутствующие поля, неверные типы, пустые значения, слишком длинные строки, невалидные enum.
4. Проверить auth: без token, с истекшим token, с чужой ролью.
5. Проверить response schema: структура, типы, обязательные поля.
6. Проверить, что данные реально изменились на backend: через GET, БД или логи.
7. Проверить error handling: понятные ошибки, правильные status codes, без stack trace и технической информации наружу.

Пример для poker platform: если есть endpoint для действия игрока `POST /tables/{tableId}/actions`, нужно проверить allowed actions, required fields, валидность bet amount, состояние стола, баланс игрока, повторную отправку request, ошибку при истекшем таймере и синхронизацию результата с другими клиентами.

## 2. Описание HTTP status codes

HTTP status codes показывают результат обработки request.

Основные группы:

- **1xx Informational** - информационные ответы. В обычном API-тестировании встречаются редко.
- **2xx Success** - request успешно обработан.
- **3xx Redirection** - redirect или ресурс находится по другому адресу.
- **4xx Client errors** - ошибка на стороне клиента: неверный request, нет доступа, ресурс не найден.
- **5xx Server errors** - ошибка на стороне сервера.

Частые status codes:

- **200 OK** - успешный request, обычно с response body.
- **201 Created** - ресурс успешно создан.
- **202 Accepted** - request принят, но обработка может быть асинхронной.
- **204 No Content** - успешно, но response body нет.
- **301/302 Redirect** - перенаправление.
- **400 Bad Request** - некорректный request, например неверный формат данных.
- **401 Unauthorized** - пользователь не аутентифицирован или token отсутствует/невалиден.
- **403 Forbidden** - пользователь аутентифицирован, но нет прав.
- **404 Not Found** - ресурс не найден.
- **405 Method Not Allowed** - endpoint существует, но метод не поддерживается.
- **409 Conflict** - конфликт состояния, например действие уже выполнено или данные устарели.
- **422 Unprocessable Entity** - request синтаксически корректный, но не проходит бизнес-валидацию.
- **429 Too Many Requests** - слишком много запросов, rate limit.
- **500 Internal Server Error** - внутренняя ошибка сервера.
- **502 Bad Gateway** - проблема между gateway/proxy и upstream service.
- **503 Service Unavailable** - сервис временно недоступен.
- **504 Gateway Timeout** - timeout при ожидании ответа от upstream service.

Важная мысль для интервью: QA проверяет не только сам код ответа, но и то, что он соответствует ситуации. Например, если игрок пытается сделать ставку больше баланса, это не должно быть `500`, это должна быть ожидаемая клиентская или бизнес-ошибка, например `400` или `422`.

## 3. HTTP methods и частые вопросы по ним

Основные REST methods:

- **GET** - получить данные. Не должен изменять состояние на сервере.
- **POST** - создать ресурс или выполнить действие.
- **PUT** - полностью заменить ресурс.
- **PATCH** - частично обновить ресурс.
- **DELETE** - удалить ресурс.
- **HEAD** - как GET, но без body, часто для проверки headers/availability.
- **OPTIONS** - показывает, какие методы разрешены, часто связан с CORS.

Частые вопросы:

**Чем отличается GET от POST?**

GET используется для получения данных, параметры часто передаются в URL. POST обычно используется для создания ресурса или выполнения действия, данные чаще передаются в body. GET должен быть safe, то есть не менять состояние сервера.

**Чем отличается PUT от PATCH?**

PUT обычно заменяет ресурс полностью. PATCH обновляет только переданные поля.

Пример:

- PUT `/users/10` - заменить данные пользователя целиком.
- PATCH `/users/10` - изменить только email или status.

**Что такое idempotency?**

Idempotent method - метод, который при повторном выполнении с теми же данными приводит к тому же результату.

Обычно idempotent:

- GET
- PUT
- DELETE

Обычно не idempotent:

- POST

Но POST можно сделать идемпотентным через idempotency key, особенно для платежей, ставок, транзакций и других рискованных операций.

**Может ли GET иметь body?**

Технически некоторые инструменты позволяют отправить body в GET, но на практике это плохая идея: многие серверы, прокси и библиотеки могут его игнорировать. Для GET лучше использовать query parameters.

**Когда использовать 400, 401, 403, 404?**

- 400 - request некорректный.
- 401 - нет валидной аутентификации.
- 403 - пользователь известен, но нет прав.
- 404 - ресурс не найден.

**Что важно проверять для методов?**

- правильный status code;
- правильный response body;
- изменение или отсутствие изменения данных;
- validation;
- auth/permissions;
- повторный request;
- error cases;
- влияние на связанные сущности;
- логи и БД, если доступно.

Пример для poker platform: POST может использоваться для действия игрока: call, fold, raise. Тут важно проверить, что повторный POST не приводит к двойному списанию баланса или двойному действию, особенно при network retry.

## 4. Postman: коллекции, environments, параметры в URL и body

**Postman** - популярный инструмент для ручного и полуавтоматизированного API testing. В нем удобно отправлять requests, хранить коллекции, использовать переменные окружения, писать pre-request scripts и tests.

### Collections

**Collection** - это набор API requests, сгруппированных по проекту, фиче или сервису.

В коллекции можно хранить:

- endpoints;
- request methods;
- headers;
- body;
- tests;
- pre-request scripts;
- auth settings;
- папки по модулям, например Auth, Users, Tables, Payments.

Зачем нужны collections:

- быстро повторять проверки;
- делиться API checks с командой;
- запускать smoke/regression API checks;
- использовать в CI через Newman.

### Environments

**Environment** - это набор переменных для конкретного окружения: dev, staging, prod-like, local.

Примеры переменных:

- `base_url`
- `auth_token`
- `user_id`
- `table_id`
- `game_id`
- `currency`

Пример:

```text
{{base_url}}/tables/{{table_id}}/actions
```

Так один и тот же request можно запускать на разных окружениях, меняя только environment.

### Параметры в URL

В URL могут передаваться:

**Path parameters** - часть пути, обычно идентификатор ресурса.

```text
GET /users/123
GET /tables/456
```

Здесь `123` и `456` - path params.

**Query parameters** - параметры после `?`, обычно для фильтрации, сортировки, пагинации.

```text
GET /tables?status=active&limit=20&page=1
```

Здесь `status`, `limit`, `page` - query params.

Что проверять в URL params:

- обязательные и необязательные параметры;
- валидные/невалидные значения;
- пустые значения;
- спецсимволы;
- слишком длинные значения;
- пагинацию, сортировку, фильтры;
- поведение при неизвестных параметрах.

### Параметры в body

Body чаще используется в POST, PUT, PATCH.

Популярные форматы body:

- **JSON** - самый частый формат для REST API.
- **form-data** - часто для загрузки файлов.
- **x-www-form-urlencoded** - форма в key-value формате.
- **raw text/xml** - реже, зависит от API.

Пример JSON body:

```json
{
  "action": "raise",
  "amount": 100
}
```

Что проверять в body:

- обязательные поля;
- типы данных;
- формат дат;
- enum values;
- min/max values;
- пустой body;
- лишние поля;
- вложенные объекты;
- массивы;
- null values;
- неверный `Content-Type`.

### Headers

Часто важные headers:

- `Authorization: Bearer <token>`
- `Content-Type: application/json`
- `Accept: application/json`
- `Idempotency-Key`
- `X-Request-Id` или correlation id

Для backend-heavy продукта важно уметь связать API request с логами через request id/correlation id. Это помогает быстрее анализировать баги.

### Tests в Postman

В Postman можно писать простые проверки:

```javascript
pm.test("Status code is 200", function () {
  pm.response.to.have.status(200);
});

pm.test("Response has table id", function () {
  const json = pm.response.json();
  pm.expect(json).to.have.property("tableId");
});
```

Что можно проверять tests-скриптами:

- status code;
- response time;
- наличие полей;
- типы и значения;
- сохранение token/id в переменные;
- бизнес-условия.

Хороший ответ на интервью:

"В Postman я обычно организую requests в collections по модулям, использую environments для dev/staging/prod-like переменных, выношу `base_url`, tokens и ids в переменные. Параметры могут передаваться в path, query или body. Path params обычно идентифицируют ресурс, query params используются для фильтров, сортировки и пагинации, а body - для создания или изменения данных. Дополнительно я проверяю headers, auth, status codes, response body, validation и могу писать Postman tests для базовой автоматизации API checks."

## 5. Cookies, Web Storage и Cache: отличия

**Cookies**, **Web Storage** и **browser cache** - это разные механизмы хранения данных в браузере.

### Cookies

**Cookies** - небольшие данные, которые браузер хранит для конкретного сайта и может автоматически отправлять на сервер с каждым HTTP request.

Часто используются для:

- session id;
- auth/session cookies;
- remember me;
- tracking/analytics;
- user preferences.

Особенности:

- отправляются на сервер автоматически, если подходят domain/path/rules;
- имеют небольшой размер, обычно около 4 KB на cookie;
- могут иметь срок жизни: session cookie или persistent cookie;
- могут быть защищены флагами `HttpOnly`, `Secure`, `SameSite`;
- доступны JavaScript, если не стоит `HttpOnly`.

Важные flags:

- `HttpOnly` - cookie нельзя прочитать через JavaScript, защита от XSS-кражи токена.
- `Secure` - cookie отправляется только по HTTPS.
- `SameSite` - помогает защищаться от CSRF.

Что проверять QA:

- cookie создается после login;
- удаляется после logout;
- корректный expiration;
- есть `HttpOnly`, `Secure`, `SameSite` для sensitive cookies;
- пользователь не остается залогинен после истечения сессии;
- cookie не отправляется на неправильный domain/path.

### Web Storage

**Web Storage** - это хранение данных на стороне браузера в формате key-value. Есть два основных вида: `localStorage` и `sessionStorage`.

**localStorage**:

- хранит данные без срока истечения;
- данные остаются после закрытия браузера;
- доступен JavaScript;
- не отправляется автоматически на сервер.

**sessionStorage**:

- хранит данные только в рамках текущей вкладки/сессии;
- очищается после закрытия вкладки;
- доступен JavaScript;
- не отправляется автоматически на сервер.

Часто используется для:

- UI settings;
- feature flags;
- temporary client state;
- draft data;
- некритичных preferences.

Что проверять QA:

- данные сохраняются/очищаются в правильный момент;
- logout очищает sensitive client state;
- sessionStorage очищается при закрытии вкладки;
- localStorage не хранит чувствительные данные без необходимости;
- приложение корректно работает, если storage очищен вручную;
- нет рассинхронизации UI из-за устаревших данных в storage.

Важный момент: access token в `localStorage` - потенциальный security risk, потому что JavaScript может его прочитать. При XSS такой token можно украсть.

### Browser Cache

**Cache** - это механизм, который сохраняет ресурсы, чтобы не скачивать их повторно.

Что может кешироваться:

- HTML;
- CSS;
- JS bundles;
- images;
- fonts;
- API responses, если настроены cache headers;
- service worker cache.

Зачем нужен cache:

- быстрее загрузка страниц;
- меньше сетевых запросов;
- меньше нагрузка на сервер;
- лучше user experience.

Что проверять QA:

- после релиза пользователь получает новую версию JS/CSS, а не старую;
- cache не показывает устаревшие данные;
- logout/login другим пользователем не показывает данные предыдущего пользователя;
- правильные cache headers: `Cache-Control`, `ETag`, `Expires`;
- sensitive API responses не кешируются небезопасно;
- hard refresh/clear cache решает или не решает проблему;
- service worker не держит старую версию приложения.

### Главное отличие

- **Cookies** могут автоматически отправляться на сервер с request.
- **Web Storage** хранится только на клиенте и не отправляется автоматически.
- **Cache** хранит ресурсы или responses для ускорения загрузки и уменьшения запросов.

Коротко:

| Механизм | Где хранится | Отправляется на сервер автоматически | Типичное использование |
|---|---|---:|---|
| Cookies | Браузер | Да | Сессии, auth cookies, preferences |
| localStorage | Браузер | Нет | Долгоживущие client-side настройки |
| sessionStorage | Вкладка браузера | Нет | Временные данные вкладки |
| Cache | Браузер/cache storage | Нет как данные формы, но влияет на загрузку ресурсов | CSS/JS/images/API cache |

Хороший ответ на интервью:

"Cookies, Web Storage и cache решают разные задачи. Cookies маленькие и могут автоматически уходить на сервер, поэтому часто используются для сессий и auth, особенно с флагами HttpOnly, Secure и SameSite. Web Storage - это localStorage и sessionStorage, они доступны на клиенте через JavaScript и не отправляются на сервер автоматически. Cache нужен для ускорения загрузки ресурсов и может быть причиной проблем, когда после релиза пользователь видит старую версию приложения или устаревшие данные."

## Commands / Terms

| Term | Meaning |
| --- | --- |
| API contract | Договоренность о request/response, полях, типах, статусах и ошибках API. |
| REST API | API в request-response стиле, обычно поверх HTTP. |
| Idempotency | Свойство операции давать тот же результат при повторном одинаковом request. |
| Path parameter | Параметр внутри URL path, например `/users/{id}`. |
| Query parameter | Параметр после `?`, часто для фильтрации, сортировки и пагинации. |
| Header | Служебная часть request/response: auth, content type, request id. |
| Cookie | Небольшие данные браузера, которые могут автоматически отправляться на сервер. |
| localStorage | Client-side storage без автоматической отправки на сервер. |
| Cache-Control | Header, который управляет кешированием ресурсов или responses. |

## What To Review Later

- Что проверять в API contract.
- Отличия `400`, `401`, `403`, `404`, `409`, `422` и `5xx`.
- Разницу между GET, POST, PUT, PATCH и DELETE.
- Как организовать Postman collection и environments.
- QA-риски cookies, Web Storage и browser cache.
