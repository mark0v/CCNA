# 🎯 QA Interview — Шпаргалка (Cheatsheet)

> Быстрый справочник для подготовки к интервью  
> Читай перед собеседованием — всё самое важное на одном листе

---

## ⚡ САМЫЕ ЧАСТЫЕ ВОПРОСЫ

### "Расскажи о себе как QA"
Структура: Опыт → Специализация → Достижение → Почему эта компания
> "Работаю Manual QA {N} лет. Специализируюсь на [web/mobile]. На последнем проекте [достижение]. Хочу развиваться в [направлении], в вашей компании привлекает [что-то конкретное]."

### "Какой баг тебя больше всего запомнил?"
Структура: Контекст → Как нашёл → Серьёзность → Что узнал
> Заготовь реальный пример из практики с деталями.

---

## 📋 КЛЮЧЕВЫЕ ОПРЕДЕЛЕНИЯ (в одно предложение)

| Термин | Определение |
|--------|-------------|
| **QA** | Предотвращение дефектов через улучшение процессов |
| **QC** | Обнаружение дефектов в конкретном продукте |
| **Bug/Defect** | Отклонение реального поведения от ожидаемого |
| **Test Case** | Задокументированный набор условий для проверки фичи |
| **Test Plan** | Документ описывающий что/как/когда/кем тестируется |
| **Test Strategy** | Высокоуровневый подход к тестированию проекта |
| **Regression** | Проверка что новый код не сломал существующий |
| **RTM** | Матрица связи требований и тест-кейсов |

---

## 🔢 ЧИСЛА, КОТОРЫЕ НУЖНО ПОМНИТЬ

- **7** принципов тестирования
- **6** фаз STLC
- **7** фаз SDLC
- **4** уровня тестирования (Unit, Integration, System, Acceptance)
- **6** уровней TCP/IP+OSI → знать 4-уровневую TCP/IP модель
- **10** уязвимостей OWASP Top 10

---

## 🌐 HTTP СТАТУС-КОДЫ (обязательно наизусть)

```
200 OK              — успешный запрос
201 Created         — ресурс создан (ответ на POST)
204 No Content      — успех, нет тела ответа (DELETE)
301 Moved Permanently — постоянный редирект
302 Found           — временный редирект
400 Bad Request     — неверный синтаксис запроса
401 Unauthorized    — нужна аутентификация
403 Forbidden       — нет прав (аутентифицирован, но запрещено)
404 Not Found       — ресурс не найден
409 Conflict        — конфликт (дубликат)
422 Unprocessable   — валиден синтаксически, но не семантически
429 Too Many Req.   — rate limit превышен
500 Internal Error  — ошибка сервера
502 Bad Gateway     — проблема с upstream сервером
503 Unavailable     — сервер недоступен (перегрузка/обслуживание)
```

---

## 🔌 HTTP МЕТОДЫ

| Метод | CRUD | Идемпотентный | Тело запроса |
|-------|------|---------------|--------------|
| GET | Read | ✅ Да | Нет |
| POST | Create | ❌ Нет | Да |
| PUT | Update (full) | ✅ Да | Да |
| PATCH | Update (partial) | ❌ Нет | Да |
| DELETE | Delete | ✅ Да | Нет |

---

## 🎨 ТЕХНИКИ ТЕСТ-ДИЗАЙНА

| Техника | Когда применять |
|---------|----------------|
| **Equivalence Partitioning** | Поля с диапазонами значений |
| **Boundary Value Analysis** | Граничные значения диапазона |
| **Decision Table** | Несколько условий → разные результаты |
| **State Transition** | Объект имеет состояния (order: NEW→PAID→SHIPPED) |
| **Use Case Testing** | Тест-кейсы из пользовательских сценариев |
| **Pairwise** | Много параметров, нужно сократить комбинации |
| **Error Guessing** | На основе опыта + интуиции |
| **Exploratory** | Без скриптов, изучение нового функционала |

---

## 🗄️ SQL ШПАРГАЛКА

```sql
-- SELECT с условиями
SELECT id, name, email FROM users
WHERE status = 'active' AND age > 18
ORDER BY created_at DESC
LIMIT 10;

-- JOINS
SELECT u.name, o.amount FROM users u
INNER JOIN orders o ON u.id = o.user_id;  -- только с заказами
LEFT JOIN orders o ON u.id = o.user_id;   -- все пользователи

-- АГРЕГАЦИИ
SELECT status, COUNT(*), SUM(amount) FROM orders
GROUP BY status HAVING COUNT(*) > 5;

-- INSERT
INSERT INTO users (name, email) VALUES ('Alex', 'alex@test.com');

-- UPDATE (ВСЕГДА с WHERE!)
UPDATE users SET status = 'inactive' WHERE id = 5;

-- DELETE (ВСЕГДА с WHERE!)
DELETE FROM users WHERE id = 5;

-- Найти дубликаты
SELECT email, COUNT(*) FROM users GROUP BY email HAVING COUNT(*) > 1;
```

---

## 📱 MOBILE QUICK REFERENCE

### ADB команды
```bash
adb devices              # список устройств
adb logcat               # все логи
adb logcat *:E           # только ошибки
adb logcat -s "MyTag"    # фильтр по тегу
adb install app.apk      # установить APK
adb shell                # shell устройства
```

### Искать в логах
```bash
adb logcat | grep "FATAL EXCEPTION"   # крэши
adb logcat | grep "ERROR"             # ошибки
```

---

## ⚡ PERFORMANCE ТЕСТИРОВАНИЕ

| Тип | Цель | Инструменты |
|-----|------|-------------|
| **Load** | Ожидаемая нагрузка | JMeter, k6 |
| **Stress** | Точка отказа | JMeter, Gatling |
| **Stability** | Долгосрочная нагрузка (Memory Leaks) | JMeter, k6 |
| **Spike** | Резкий скачок нагрузки | k6, Artillery |

**Метрики:** Response Time < 2с | Error Rate < 1% | CPU < 80%

---

## 🤖 ПИРАМИДА ТЕСТИРОВАНИЯ

```
        /\
       /  \
      / E2E \     ← мало, медленно, дорого (Selenium, Playwright)
     /--------\
    /   API    \  ← баланс (Postman Newman, RestAssured)
   /------------\
  /  Unit Tests  \ ← много, быстро, дёшево (JUnit, pytest)
 /----------------\
```

---

## 🔐 OWASP TOP 10 (краткий список)

1. **Broken Access Control** — нарушение контроля доступа (IDOR)
2. **Cryptographic Failures** — слабое шифрование
3. **Injection** — SQL/Command/LDAP injection
4. **Insecure Design** — небезопасный дизайн
5. **Security Misconfiguration** — неправильная конфигурация
6. **Vulnerable Components** — устаревшие компоненты
7. **Authentication Failures** — проблемы аутентификации
8. **Integrity Failures** — нарушение целостности данных
9. **Logging Failures** — недостаточное логирование
10. **SSRF** — Server-Side Request Forgery

---

## 💬 ВОПРОСЫ ДЛЯ ЗАДАНИЯ ИНТЕРВЬЮЕРУ

_(показывает зрелость кандидата)_

- "Как устроен процесс тестирования на проекте?"
- "Какой стек технологий использует команда QA?"
- "Есть ли автоматизация? Какие фреймворки?"
- "Как организована работа QA с командой разработки?"
- "Какие задачи будут у меня в первые 3 месяца?"
- "Каков roadmap по развитию для QA в вашей компании?"

---

*Удачи на интервью! 🚀*
