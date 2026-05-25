# 🌐 02 — Web тестирование

> **Твой уровень:** 🟡 Частично (Web basics — Familiar with; архитектура и сети — 🔴 ПРОБЕЛ)  
> **Приоритет:** ⭐⭐⭐ ВЫСОКИЙ — основа для большинства проектов

---

## 2.1 Архитектура Web-приложений
**Твой уровень:** 🔴 ПРОБЕЛ (Not Started в IDP)

### Темы

#### Client-Server Architecture
- Что такое клиент и сервер
- Типы взаимодействия: синхронное / асинхронное
- Thin Client vs Thick Client

#### 3-Tier Architecture (3-уровневая)
- **Presentation Tier** (UI) — браузер, мобильное приложение
- **Application/Logic Tier** (Backend) — бизнес-логика, API
- **Data Tier** (Database) — хранение данных
- Как это влияет на тестирование каждого слоя

#### SOA (Service-Oriented Architecture)
- Что такое сервисы и микросервисы
- Как тестируется SOA vs Monolith
- Отличие SOA от Microservices

### Ресурсы
- 🔗 [3-Tier Architecture (IBM)](https://www.ibm.com/topics/three-tier-architecture)
- 🔗 [Client-Server Architecture](https://intellipaat.com/blog/what-is-client-server-architecture/)
- 🔗 [SOA Guide](https://www.guru99.com/microservices-tutorial.html)
- 🔗 [QA & Client-Server](https://www.qamadness.com/knowledge-base/client-server-architecture-for-qa-engineers)

---

## 2.2 Сетевые технологии и протоколы
**Твой уровень:** 🔴 ПРОБЕЛ

### Темы

#### Основы сетей
- **TCP/IP модель** — 4 уровня, что на каждом
- **OSI модель** — 7 уровней, сравнение с TCP/IP
- **DNS** — как работает разрешение имён, что тестировать
- **DHCP** — динамическое назначение IP
- **LAN** — локальная сеть, топологии

#### HTTP / HTTPS
- Методы: **GET, POST, PUT, PATCH, DELETE** — различия и применение
- **PUT vs PATCH** — частичное vs полное обновление ресурса
- **HTTP vs HTTPS** — шифрование, SSL/TLS сертификаты
- Структура HTTP запроса и ответа (Headers, Body, Status Code)

#### HTTP Status Codes (ОБЯЗАТЕЛЬНО знать)
| Группа | Коды | Значение |
|--------|------|----------|
| 2xx | 200 OK, 201 Created, 204 No Content | Успех |
| 3xx | 301 Moved, 302 Found, 304 Not Modified | Редиректы |
| 4xx | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 422 | Ошибки клиента |
| 5xx | 500 Internal Server Error, 502 Bad Gateway, 503 Unavailable | Ошибки сервера |

#### Прокси и Fiddler/Charles
- Что такое прокси-сервер
- Как настроить proxy на браузере
- Перехват трафика в Charles / Fiddler

### Ресурсы
- 🔗 [TCP/IP vs OSI](https://community.fs.com/ru/blog/tcpip-vs-osi-whats-the-difference-between-the-two-models.html)
- 🔗 [HTTP Status Codes (MDN)](https://developer.mozilla.org/ru/docs/Web/HTTP/Status)
- 🔗 [HTTP Status Codes (Moz)](https://moz.com/learn/seo/http-status-codes)
- 🔗 [PUT vs PATCH](https://www.geeksforgeeks.org/difference-between-put-and-patch-request/)
- 🔗 [DNS Best Practices (Cisco)](https://tools.cisco.com/security/center/resources/dns_best_practices)
- 🔗 [TCP/IP объяснение (YouTube)](https://www.youtube.com/watch?v=GlZC4Jwf3xQ)

---

## 2.3 Виды аутентификации
**Твой уровень:** 🔴 ПРОБЕЛ (тема не покрыта в матрице, но критична)

### Темы
- **Basic Auth** — Base64 логин:пароль в заголовке
- **Session / Cookie Auth** — сессионный токен в куках
- **Token-Based Auth (JWT)** — структура токена (Header.Payload.Signature)
- **OAuth 2.0** — авторизация через третьи сервисы (Google, GitHub)
- **API Key** — статический ключ в заголовке или параметре
- **SSO (Single Sign-On)** — одна точка входа для нескольких сервисов

### Что тестировать в аутентификации
- Доступ с правильными/неправильными кредами
- Истечение токена / сессии
- Повторное использование токена
- Доступ к чужим данным (IDOR — Insecure Direct Object Reference)
- Поведение при logout

### Ресурсы
- 🔗 [Web Auth Types Overview](https://www.softwaretestinghelp.com/web-application-testing/)

---

## 2.4 Инструменты Web-тестирования
**Твой уровень:** 🟡 Familiar with (знаешь, но применяешь не уверенно)

### Chrome DevTools
- **Elements** — инспектирование и редактирование DOM/CSS
- **Console** — JavaScript ошибки, логи, тестирование выражений
- **Network** — перехват запросов, просмотр payload, status codes, timing
- **Application** — Cookies, LocalStorage, SessionStorage, IndexedDB
- **Sources** — отладка JavaScript
- **Lighthouse** — аудит производительности и доступности

### Прокси-инструменты (Fiddler / Charles)
- Перехват HTTP/HTTPS трафика
- Изменение запросов и ответов (mock)
- Тестирование на медленных соединениях
- Breakpoints для запросов

### Браузеры и кросс-браузерное тестирование
- Движки: **Chromium** (Chrome, Edge), **Gecko** (Firefox), **WebKit** (Safari)
- Что значит кросс-браузерное тестирование
- Использование BrowserStack / Sauce Labs для тестирования
- Расширения для тестировщиков

### Ресурсы
- 🔗 [Chrome DevTools Overview](https://developer.chrome.com/docs/devtools/overview/)
- 🔗 [DevTools DOM](https://developer.chrome.com/docs/devtools/dom/)
- 🔗 [Chrome DevTools Guide (DOU)](https://dou.ua/lenta/articles/chrome-dev-tools-guide/)
- 🔗 [Cross Browser Testing](https://www.browserstack.com/cross-browser-testing)
- 🔗 [Browser Rendering Engines](https://www.browserstack.com/guide/browser-rendering-engine)

---

## 2.5 HTML и CSS (базовые основы)
**Твой уровень:** 🔴 ПРОБЕЛ

### Что нужно знать тестировщику
- Структура HTML страницы: `<!DOCTYPE>`, `<html>`, `<head>`, `<body>`
- Основные теги: `<div>`, `<span>`, `<a>`, `<input>`, `<form>`, `<button>`, `<img>`
- Атрибуты: `id`, `class`, `name`, `href`, `src`, `type`, `placeholder`
- CSS селекторы: по `id` (#), `class` (.), тегу — важно для автоматизации
- Понятие **CSS Box Model** — margin, border, padding, content
- Адаптивный дизайн — media queries, viewport

### Зачем это тестировщику
- Понимание DOM структуры при работе с DevTools
- Нахождение элементов для автоматизации (XPath, CSS Selectors)
- Проверка отображения и вёрстки

### Ресурсы
- 🔗 [HTML Basics (Wikipedia)](https://en.wikipedia.org/wiki/HTML)
- 🔗 [HTML & CSS Fundamentals (Medium)](https://medium.com/@iampika/html-and-css-fundamentals-6b8f7d90911b)
- 🔗 [CSS (Wikipedia)](https://en.wikipedia.org/wiki/CSS)

---

## 2.6 Web-серверы и инфраструктура
**Твой уровень:** 🔴 ПРОБЕЛ

### Темы
- **Apache HTTP Server** — конфигурация, vhosts, .htaccess
- **Nginx** — proxy, load balancer, статика
- **Apache vs Nginx** — сравнение производительности и сценариев применения
- **Docker** — что такое контейнер, образ, зачем нужен тестировщику
  - `docker run`, `docker logs`, `docker ps`
  - Как запустить тестовое окружение в Docker
- **Redis** — in-memory кэш, когда используется, что может сломаться
- **Amazon RDS** — облачные базы данных, базовые понятия

### Ресурсы
- 🔗 [Apache vs Nginx](https://serverguy.com/comparison/apache-vs-nginx/)
- 🔗 [Docker: Get Started](https://docs.docker.com/get-started/overview/)
- 🔗 [Docker для QA](https://qagroup.com.ua/publications/shcho-take-docker-i-navishcho-vin/)
- 🔗 [Redis Docs](https://redis.io/docs/about)

---

## 2.7 Responsive Design тестирование
**Твой уровень:** 🟡 Familiar with

### Темы
- Что такое адаптивный дизайн
- Breakpoints — mobile, tablet, desktop
- Тестирование в DevTools (режим эмуляции устройства)
- Инструменты: BrowserStack, Responsively App
- Типичные баги: перекрывающиеся элементы, неправильные отступы, текст не влезает

### Ресурсы
- 🔗 [Responsive Design Testing](https://www.browserstack.com/responsive-design)
- 🔗 [Responsive Testing Tools](https://www.webfx.com/blog/web-design/responsive-design-testing-tools/)

---

## 2.8 Web Performance тестирование
**Твой уровень:** 🟡 Familiar with (инструменты знает)

### Темы
- Метрики производительности: **LCP, FCP, TTI, CLS** (Core Web Vitals)
- Инструменты: **Google Lighthouse**, PageSpeed Insights, GTMetrix, WebPageTest
- Что влияет на скорость: размер изображений, кэш, CDN, минификация JS/CSS
- Как проверить скорость через DevTools → Network

### Ресурсы
- 🔗 [Web Performance Tools](https://www.softwaretestinghelp.com/performance-testing-tools-load-testing-tools/)
- 🔗 [Speed Test Tools](https://phoenixnap.com/kb/best-website-speed-performance-test-tools)
- 🔗 [Website Speed Factors](https://www.plerdy.com/blog/website-speed-factors-and-tools/)

---

## 2.9 Безопасность Web (базовый уровень)
**Твой уровень:** 🔴 ПРОБЕЛ (не в матрице, но важно знать)

### Темы (что должен знать Manual QA)
- **OWASP Top 10** — знать основные уязвимости:
  - SQL Injection — вредоносный SQL в полях ввода
  - XSS (Cross-Site Scripting) — инъекция скриптов
  - IDOR — доступ к чужим данным через подмену ID
  - CSRF — межсайтовые подделки запросов
  - Broken Auth — уязвимости аутентификации
- **Базовые тест-кейсы безопасности:**
  - Проверка авторизации (доступ без токена)
  - Проверка на SQL injection в полях ввода
  - Проверка заголовков безопасности

### Ресурсы
- 🔗 [OWASP Top 10](https://owasp.org/www-project-top-ten/)

---

## ✅ Чеклист по разделу

- [ ] Могу объяснить 3-Tier Architecture и роль QA на каждом уровне
- [ ] Знаю все основные HTTP методы и статус-коды (200, 201, 400, 401, 403, 404, 500)
- [ ] Умею пользоваться Chrome DevTools (Network, Console, Elements)
- [ ] Умею перехватывать запросы в Fiddler/Charles
- [ ] Понимаю базовую структуру HTML/CSS (нахожу элементы)
- [ ] Знаю разницу Apache vs Nginx (зачем нужен каждый)
- [ ] Умею запустить Docker-контейнер и посмотреть логи
- [ ] Знаю виды аутентификации и что тестировать в каждом
- [ ] Знаю OWASP Top 10 на базовом уровне
