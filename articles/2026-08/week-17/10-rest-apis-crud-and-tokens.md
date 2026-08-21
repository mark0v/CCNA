# REST APIs CRUD And Tokens

Source: закрытая страница курса  
Date added: 2026-08-21  
Related plan item: Week 17 / REST APIs, CRUD, and tokens  
Tags: REST, API, HTTP, status codes, CRUD, token, Postman, network automation  
Language: Russian  
Translation pair: articles-en/2026-08/week-17/10-rest-apis-crud-and-tokens.md

## Кратко

- `REST` - самый распространенный стиль API, построенный вокруг HTTP request и response.
- RESTful API работает похоже на web: клиент отправляет запрос, server возвращает ответ.
- HTTP status codes быстро показывают, что произошло с request.
- `200` series - успех, `300` - перенаправление, `400` - ошибка client/request, `500` - проблема server.
- `CRUD` означает Create, Read, Update, Delete.
- Token подтверждает, что ты имеешь право использовать API.
- Token нужно защищать как пароль.
- `Postman` помогает вручную тестировать API requests перед автоматизацией.

## Главное

- API не обязательно что-то экзотическое для developers. Это обычный способ систем разговаривать друг с другом.
- REST стал популярным, потому что использует знакомую модель HTTP.
- Status codes нужны не только для экзамена, но и для troubleshooting.
- CRUD описывает базовые действия: создать, прочитать, обновить, удалить.
- APIs дают automation силу, потому что действия можно повторять, планировать и масштабировать.
- Та же сила делает APIs опасными, если плохо обращаться с tokens.

## Заметки

Когда люди слышат слово `API`, оно может звучать слишком разработчески.

Но идея проще:

```text
Система хочет поговорить с другой системой.
Ей нужен понятный способ отправить запрос и получить ответ.
API дает этот способ.
```

В network automation API становится дверью в устройство, controller или cloud service.

Через эту дверь можно читать данные, менять настройки и строить повторяемые workflows.

## REST как стиль общения

`REST`, или Representational State Transfer, вырос из web-подхода.

Web уже давно работает по модели:

```text
Browser отправляет HTTP request.
Server возвращает HTTP response.
```

REST использует похожий pattern.

Он не пытается держать вечную session и постоянно "разговаривать". Чаще это выглядит так:

```text
Дай мне это.
Вот ответ.
```

Именно поэтому REST стал таким популярным для APIs.

Если browser может запросить страницу, script или application может запросить данные, состояние device или изменение configuration.

## Запрос и ответ

RESTful communication строится вокруг пары:

```text
Request -> response.
```

Request может содержать:

- адрес ресурса;
- method;
- headers;
- token;
- body с данными.

Response обычно содержит:

- status code;
- headers;
- data;
- error details, если что-то пошло не так.

Для network engineer это важно, потому что API troubleshooting часто начинается именно с ответа.

## Коды состояния HTTP

HTTP status codes - один из самых быстрых способов понять, где проблема.

Не нужно знать каждый редкий code. Но нужно знать группы:

| Code group | Значение |
| --- | --- |
| `200` series | Успех. Request сработал. |
| `300` series | Перенаправление или нужен дополнительный шаг. |
| `400` series | Ошибка со стороны client/request. |
| `500` series | Проблема на стороне server. |

Пример:

```text
404 = скорее всего, неправильный URL или resource.
500 = server получил request, но сам не смог его нормально обработать.
```

Это меняет troubleshooting.

Если приходит `404`, сначала проверь:

- endpoint;
- путь;
- spelling;
- нужный resource;
- параметры request.

Если приходит `500`, уже логичнее смотреть на server-side проблему или поведение platform.

## CRUD

Если REST - это стиль общения, то `CRUD` описывает действия, которые чаще всего выполняются через API.

`CRUD`:

| Letter | Action | Идея |
| --- | --- | --- |
| C | Create | Создать объект или настройку. |
| R | Read | Прочитать данные. |
| U | Update | Обновить существующую настройку. |
| D | Delete | Удалить объект или настройку. |

В networking это может быть:

- создать object на controller;
- прочитать interface statistics;
- обновить password;
- изменить interface description;
- удалить старую policy.

Target может быть разным:

- router;
- switch;
- wireless controller;
- phone;
- smart TV;
- cloud service.

Если у системы есть API, очень вероятно, что ты делаешь с ней какой-то вариант CRUD.

## Почему APIs важны для automation

GUI полезен, когда нужно сделать что-то один раз.

API полезен, когда нужно:

- повторить действие много раз;
- сделать изменение по расписанию;
- собрать данные с разных systems;
- встроить network device в workflow;
- проверить состояние автоматически;
- масштабировать работу на десятки или сотни устройств.

Вместо ручного кликанья можно отправить request:

```text
Read this value.
Update that setting.
Create this object.
Delete that old entry.
```

Так automation становится повторяемой.

## Токен

Сила API требует security.

Если API может create, update или delete, доступ к нему нельзя оставлять открытым.

`Token` - это доказательство, что тебе разрешено использовать API.

Обычно flow выглядит так:

```text
Пользователь проходит authentication.
System выдает token.
Client добавляет token в API requests.
Server проверяет token перед выполнением action.
```

Token часто выглядит как длинная случайная строка. Он не обязан быть читаемым.

Смысл не в красоте, а в том, что server может проверить:

```text
Этот request пришел от того, кому разрешено выполнять action?
```

## Почему token опасен

Token нужно воспринимать как password.

Иногда даже серьезнее, потому что token легко случайно:

- вставить в screenshot;
- отправить в chat;
- оставить в notes;
- закоммитить в repository;
- показать в terminal output;
- сохранить в shared document.

Если кто-то получает твой token, он может получить твой access.

Хорошие системы уменьшают риск:

- expiration time;
- IP restrictions;
- scoped permissions;
- extra authentication;
- token rotation.

Но главное правило остается простым:

```text
Не делись token.
Не храни token где попало.
Не вставляй token в публичные места.
```

## Инструмент Postman

`Postman` - популярный tool для ручной работы с APIs.

Он помогает:

- собрать request;
- выбрать method;
- указать URL;
- добавить headers;
- вставить token;
- отправить request;
- увидеть response;
- проверить status code;
- изучить data.

Это хороший мост между теорией и automation.

Сначала можно вручную проверить request в Postman.

Потом уже переносить идею в script, playbook или automation workflow.

## Практический совет

API troubleshooting часто выглядит скучно, но именно там находятся ошибки.

Проверяй по порядку:

1. Правильный ли endpoint?
2. Правильный ли method?
3. Нужны ли headers?
4. Не истек ли token?
5. Правильно ли оформлен body?
6. Что говорит status code?

Одна неверная буква в endpoint или один пропущенный header могут сломать весь request.

## Главный вывод

RESTful APIs используют тот же request-and-response подход, который сделал web рабочим.

Ты отправляешь HTTP request, server возвращает response и status code.

CRUD описывает базовые действия: create, read, update, delete.

Token решает, разрешено ли тебе это делать.

Если хочешь почувствовать APIs руками, начни с Postman: отправь request, посмотри response, разбери status code и только потом автоматизируй.

## Команды и термины

| Термин | Значение |
| --- | --- |
| `API` | Способ программного взаимодействия с system или device. |
| `REST` | Популярный API style на базе HTTP request/response. |
| `HTTP` | Protocol, который web использует для communication между client и server. |
| request | Запрос от client к server. |
| response | Ответ server на request. |
| status code | Число, которое показывает result request. |
| `200` series | Успешные responses. |
| `300` series | Перенаправление или дополнительный шаг. |
| `400` series | Ошибка client/request. |
| `500` series | Ошибка server. |
| `CRUD` | Create, Read, Update, Delete. |
| token | Временное доказательство access для API. |
| `Postman` | Tool для ручного тестирования API requests. |

## Вопросы

### 1. Почему REST стал таким популярным?

Ответ: Он использует знакомую HTTP-модель request и response, на которой уже построен web.

### 2. Что означает status code из группы 200?

Ответ: Request успешно выполнен.

### 3. Что обычно означает 400-series error?

Ответ: Проблема в client, request, URL, syntax или parameters.

### 4. Что означает CRUD?

Ответ: Create, Read, Update, Delete.

### 5. Зачем нужен token?

Ответ: Token подтверждает, что client имеет право использовать API.

### 6. Почему token нужно защищать?

Ответ: Если кто-то получит token, он может получить access к API с твоими permissions.

## Что повторить позже

- REST как request/response модель.
- Группы HTTP status codes.
- CRUD: create, read, update, delete.
- Роль token в API security.
- Почему Postman полезен перед написанием automation scripts.
