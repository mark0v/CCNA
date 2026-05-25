# 🔌 03 — API тестирование

> **Твой уровень:** 🔴 КРИТИЧЕСКИЙ ПРОБЕЛ (Not Started в IDP)  
> **Приоритет:** ⭐⭐⭐ ВЫСОКИЙ — обязательный навык для любого QA

---

## 3.1 Основы API
**Твой уровень:** 🔴 ПРОБЕЛ

### Что такое API
- **API** (Application Programming Interface) — интерфейс взаимодействия между системами
- **Web API** — API, работающее через HTTP протокол
- **Endpoint** — конкретный URL, к которому обращается клиент
- **Request / Response** — структура запроса и ответа
- **Base URL + Endpoint** — как составляется полный адрес

### Архитектурные стили
| Стиль | Описание | Когда используется |
|-------|----------|-------------------|
| **REST** | Stateless, HTTP методы, JSON/XML | Большинство современных API |
| **SOAP** | XML протокол, строгая схема (WSDL) | Банки, legacy системы |
| **GraphQL** | Гибкие запросы, клиент выбирает данные | Современные SPA |

### REST принципы (6 constraints)
1. **Client-Server** — разделение ответственности
2. **Stateless** — каждый запрос самодостаточен
3. **Cacheable** — ответы могут кэшироваться
4. **Uniform Interface** — единообразный интерфейс
5. **Layered System** — многоуровневая система
6. **Code on Demand** (опционально)

### Ресурсы
- 🔗 [REST vs SOAP (SoapUI)](https://www.soapui.org/learn/api/soap-vs-rest-api/)
- 🔗 [SOAP vs REST Differences (SmartBear)](https://smartbear.com/blog/soap-vs-rest-whats-the-difference/)
- 🔗 [REST API Guide (YouTube)](https://www.youtube.com/watch?v=XR0YXH0ue2I)
- 🔗 [REST простым языком (Medium)](https://medium.com/@andr.ivas12/rest-простым-языком-90a0bca0bc78)
- 🔗 [REST vs SOAP (GeeksForGeeks)](https://www.geeksforgeeks.org/difference-between-rest-api-and-soap-api/)

---

## 3.2 HTTP методы в API
**Твой уровень:** 🔴 ПРОБЕЛ

### CRUD → HTTP методы
| HTTP Метод | CRUD | Описание | Идемпотентный? |
|-----------|------|----------|----------------|
| **GET** | Read | Получить ресурс | ✅ Да |
| **POST** | Create | Создать ресурс | ❌ Нет |
| **PUT** | Update (full) | Полностью заменить ресурс | ✅ Да |
| **PATCH** | Update (partial) | Частично обновить ресурс | ❌ Нет |
| **DELETE** | Delete | Удалить ресурс | ✅ Да |

### PUT vs PATCH — важное отличие
- **PUT** — заменяет весь объект целиком (если поле не передано — оно обнуляется)
- **PATCH** — обновляет только переданные поля
- 🔗 [PUT vs PATCH](https://www.geeksforgeeks.org/difference-between-put-and-patch-request/)

---

## 3.3 Форматы данных
**Твой уровень:** 🔴 ПРОБЕЛ

### JSON (JavaScript Object Notation)
```json
{
  "id": 1,
  "name": "Oleksandr",
  "email": "test@example.com",
  "roles": ["qa", "tester"],
  "address": {
    "city": "Kharkiv",
    "country": "Ukraine"
  },
  "active": true
}
```
- Типы данных: string, number, boolean, null, array, object
- Обязательно: понимание вложенных структур
- 🔗 [JSON Guide (W3Schools)](https://www.w3schools.com/whatis/whatis_json.asp)

### XML (eXtensible Markup Language)
```xml
<user>
  <id>1</id>
  <name>Oleksandr</name>
  <email>test@example.com</email>
</user>
```
- Используется в SOAP, некоторых REST API
- Атрибуты vs элементы
- 🔗 [XML Guide (W3Schools)](https://www.w3schools.com/xml/xml_whatis.asp)

---

## 3.4 Инструменты API тестирования
**Твой уровень:** 🔴 ПРОБЕЛ

### Postman (ПРИОРИТЕТ #1)
#### Базовое использование
- Создание запросов (GET, POST, PUT, DELETE)
- Параметры: **Params** (query params), **Headers**, **Body** (raw JSON / form-data)
- Просмотр ответа: Status code, Response body, Headers, Time

#### Продвинутые возможности
- **Collections** — группировка запросов по модулям
- **Environments** — переменные для dev/staging/prod окружений
- **Pre-request Scripts** — выполнение кода до запроса
- **Tests (Assertions)** — автоматические проверки ответа
- **Newman** — запуск Postman коллекций из командной строки

#### Примеры Postman тестов
```javascript
// Проверка статус-кода
pm.test("Status code is 200", () => {
    pm.response.to.have.status(200);
});

// Проверка поля в теле ответа
pm.test("User name is correct", () => {
    const jsonData = pm.response.json();
    pm.expect(jsonData.name).to.eql("Oleksandr");
});

// Проверка времени ответа
pm.test("Response time < 500ms", () => {
    pm.expect(pm.response.responseTime).to.be.below(500);
});
```

### Другие инструменты
- **Swagger / OpenAPI** — документация и тестирование API прямо из браузера
- **Insomnia** — альтернатива Postman
- **cURL** — командная строка для API запросов
- **SoapUI** — для SOAP API

### Ресурсы
- 🔗 [Postman API Testing Q&A](https://blog.postman.com/api-testing-interview-questions/)
- 🔗 [Web Service Architecture](https://www.guru99.com/web-service-architecture.html)

---

## 3.5 Что тестировать в API
**Твой уровень:** 🔴 ПРОБЕЛ

### Функциональное тестирование API
1. **Позитивные тест-кейсы** — корректные данные → ожидаемый результат
2. **Негативные тест-кейсы:**
   - Пустые/null поля
   - Неверный тип данных (строка вместо числа)
   - Отсутствие обязательных полей
   - Очень длинные строки (overflow)
   - Спецсимволы в полях
3. **Граничные значения** — max/min длина строки, числа

### Проверки статус-кодов
| Ситуация | Ожидаемый код |
|----------|---------------|
| Успешное создание ресурса | 201 Created |
| Ресурс не найден | 404 Not Found |
| Нет авторизации | 401 Unauthorized |
| Нет доступа | 403 Forbidden |
| Некорректные данные | 400 Bad Request / 422 |
| Серверная ошибка | 500 Internal Server Error |

### Проверки заголовков
- `Content-Type: application/json` — тип данных в ответе
- `Authorization: Bearer <token>` — токен аутентификации
- `Cache-Control` — параметры кэширования

### Аутентификация API
- **API Key** — в Headers или Query Params
- **Bearer Token** — `Authorization: Bearer eyJ...`
- **Basic Auth** — Base64(login:password)
- **OAuth 2.0** — получение access_token

### Ресурсы
- 🔗 [API Testing Interview Q](https://blog.postman.com/api-testing-interview-questions/)
- 🔗 [REST API vs SOAP](https://www.geeksforgeeks.org/difference-between-rest-api-and-soap-api/)
- 🔗 [YouTube REST API](https://youtu.be/2YWfJHDNQy0)

---

## 3.6 Перехват и анализ трафика
**Твой уровень:** 🔴 ПРОБЕЛ

### Инструменты
- **Fiddler Classic / Fiddler Everywhere** — Windows, перехват HTTP/HTTPS
- **Charles Proxy** — macOS/Windows, популярен у мобильных QA
- **Wireshark** — сетевой снифер (низкий уровень, TCP/UDP)
- **mitmproxy** — open-source, командная строка

### Что можно делать с proxy
- Смотреть все HTTP запросы от браузера/приложения
- Изменять запросы "на лету" (Breakpoints)
- Имитировать медленное соединение
- Заменять ответы сервера (Mock)
- Запись и воспроизведение сессий

---

## ✅ Чеклист по разделу

- [ ] Знаю разницу REST vs SOAP vs GraphQL
- [ ] Понимаю все HTTP методы (GET/POST/PUT/PATCH/DELETE) и их идемпотентность
- [ ] Знаю разницу PUT vs PATCH
- [ ] Умею читать и писать JSON/XML
- [ ] Умею отправлять запросы в Postman (все методы)
- [ ] Настраиваю переменные окружения в Postman
- [ ] Пишу базовые тесты (assertions) в Postman
- [ ] Знаю какой статус-код ожидать в каждой ситуации
- [ ] Умею перехватывать трафик в Fiddler/Charles
- [ ] Могу составить API Test Plan для нового эндпоинта
