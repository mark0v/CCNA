# 🗄️ 05 — Базы данных и SQL

Language: Russian  
Translation pair: quality-assurance-en/overview/05-database-testing/index.md

> **Твой уровень:** 🟡 Частично (SELECT/DELETE — Familiar with; JOINs/INSERT/UPDATE — 🔴 ПРОБЕЛ)  
> **Приоритет:** ⭐⭐ СРЕДНИЙ

---

## 5.1 Типы баз данных
**Твой уровень:** 🟡 Familiar with

### Реляционные (SQL)
- **PostgreSQL** — открытый, мощный, популярный
- **MySQL / MariaDB** — очень распространён в веб
- **Oracle** — корпоративный
- **SQLite** — встроенный, используется в мобильных приложениях
- Хранение в таблицах со строгой схемой (Primary Key, Foreign Key, constraints)

### Нереляционные (NoSQL)
- **MongoDB** — документо-ориентированная (JSON-like documents)
- **Redis** — key-value, in-memory (кэш, очереди)
- **Cassandra** — column-family, распределённая
- Когда NoSQL лучше SQL: гибкая схема, горизонтальное масштабирование

### Ресурсы
- 🔗 [Types of Databases](https://www.indeed.com/career-advice/career-development/types-of-databases)
- 🔗 [MongoDB vs PostgreSQL](https://www.mongodb.com/compare/mongodb-postgresql)
- 🔗 [NoSQL (Wikipedia)](https://ru.wikipedia.org/wiki/NoSQL)
- 🔗 [PostgreSQL (Wikipedia)](https://ru.wikipedia.org/wiki/PostgreSQL)

---

## 5.2 SQL — основные команды
**Твой уровень:** SELECT/DELETE — 🟡; INSERT/UPDATE/JOIN — 🔴 ПРОБЕЛ

### SELECT (уже знаешь — углубить)
```sql
-- Базовый SELECT
SELECT * FROM users;

-- Выборка конкретных полей
SELECT id, name, email FROM users;

-- Условие WHERE
SELECT * FROM users WHERE status = 'active';

-- Сортировка
SELECT * FROM users ORDER BY created_at DESC;

-- Ограничение количества
SELECT * FROM users LIMIT 10 OFFSET 20;

-- Агрегации
SELECT COUNT(*), AVG(age), MAX(salary) FROM employees;

-- Группировка
SELECT department, COUNT(*) as count 
FROM employees 
GROUP BY department 
HAVING COUNT(*) > 5;
```
- 🔗 [SQL SELECT (W3Schools)](https://www.w3schools.com/sql/sql_select.asp)

### INSERT (ПРОБЕЛ — изучить)
```sql
-- Вставка одной записи
INSERT INTO users (name, email, status) 
VALUES ('Oleksandr', 'test@test.com', 'active');

-- Вставка нескольких записей
INSERT INTO users (name, email) VALUES 
  ('Alice', 'alice@test.com'),
  ('Bob', 'bob@test.com');
```
- 🔗 [SQL INSERT (W3Schools)](https://www.w3schools.com/sql/sql_insert.asp)

### UPDATE (ПРОБЕЛ — изучить)
```sql
-- Обновление одного поля
UPDATE users SET status = 'inactive' WHERE id = 5;

-- Обновление нескольких полей
UPDATE users SET name = 'Alex', email = 'alex@test.com' WHERE id = 5;

-- ⚠️ ОПАСНО: UPDATE без WHERE обновит ВСЕ строки!
```
- 🔗 [SQL UPDATE (W3Schools)](https://www.w3schools.com/sql/sql_update.asp)

### DELETE (знаешь — закрепить)
```sql
-- Удалить запись
DELETE FROM users WHERE id = 5;

-- ⚠️ ОПАСНО: DELETE без WHERE удалит ВСЕ строки!

-- Безопасная практика: сначала проверь SELECT
SELECT * FROM users WHERE id = 5; -- убедись что нашёл правильную запись
DELETE FROM users WHERE id = 5;   -- только потом удаляй
```
- 🔗 [SQL DELETE (W3Schools)](https://www.w3schools.com/sql/sql_delete.asp)

---

## 5.3 SQL JOINs (КРИТИЧЕСКИЙ ПРОБЕЛ)
**Твой уровень:** 🔴 ПРОБЕЛ

### Типы JOIN

#### INNER JOIN — только совпадающие записи
```sql
SELECT u.name, o.total_amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```
> Вернёт только пользователей, у которых есть заказы

#### LEFT JOIN — все из левой таблицы + совпадения из правой
```sql
SELECT u.name, o.total_amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;
```
> Вернёт ВСЕХ пользователей. У кого нет заказов — NULL в поле total_amount

#### RIGHT JOIN — все из правой таблицы + совпадения из левой
```sql
SELECT u.name, o.total_amount
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

#### FULL OUTER JOIN — все записи из обеих таблиц
```sql
SELECT u.name, o.total_amount
FROM users u
FULL OUTER JOIN orders o ON u.id = o.user_id;
```

### Визуальная схема JOINs
```
INNER JOIN:  A ∩ B (пересечение)
LEFT JOIN:   A + (A ∩ B)
RIGHT JOIN:  B + (A ∩ B)
FULL JOIN:   A + B (всё)
```

- 🔗 [SQL JOINs (W3Schools)](https://www.w3schools.com/sql/sql_join.asp)
- 🔗 [SQLZoo — практика JOIN](https://sqlzoo.net/)

---

## 5.4 Практика SQL для QA
**Твой уровень:** 🔴 Практики мало

### Типичные QA запросы
```sql
-- Найти дубликаты email
SELECT email, COUNT(*) as cnt 
FROM users 
GROUP BY email 
HAVING COUNT(*) > 1;

-- Последние созданные записи
SELECT * FROM orders ORDER BY created_at DESC LIMIT 10;

-- Пользователи без заказов
SELECT u.* FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NULL;

-- Сумма по статусам
SELECT status, COUNT(*), SUM(amount) 
FROM orders 
GROUP BY status;

-- Проверка данных после API запроса
SELECT * FROM users WHERE email = 'test@test.com';
```

### Практика онлайн
- 🔗 [SQLZoo — интерактивные уроки](https://sqlzoo.net/)
- 🔗 [W3Schools SQL Exercises](https://www.w3schools.com/sql/sql_select.asp)

---

## 5.5 MongoDB (NoSQL) — базовые знания
**Твой уровень:** 🟡 Familiar with

### Основные концепции
- **Document** — аналог строки в SQL (JSON формат)
- **Collection** — аналог таблицы
- **Database** — та же база данных

### Основные операции
```javascript
// Найти всех пользователей
db.users.find()

// Найти с условием
db.users.find({ status: "active" })

// Вставить документ
db.users.insertOne({ name: "Alex", email: "alex@test.com" })

// Обновить документ
db.users.updateOne({ _id: ObjectId("...") }, { $set: { status: "inactive" } })

// Удалить документ
db.users.deleteOne({ _id: ObjectId("...") })
```

### Ресурсы
- 🔗 [MongoDB Pros & Cons](https://www.knowledgenile.com/blogs/pros-and-cons-of-mongodb/)

---

## 5.6 Database Testing — что проверять
**Твой уровень:** 🔴 ПРОБЕЛ

### Виды проверок
1. **Schema Testing** — соответствие структуры БД требованиям
   - Правильные типы данных (varchar(255) не int)
   - Наличие обязательных полей (NOT NULL)
   - Первичные и внешние ключи

2. **Data Integrity Testing** — целостность данных
   - Данные сохраняются корректно после API запроса
   - Каскадное удаление работает правильно
   - Транзакции (commit/rollback)

3. **CRUD Verification** — после каждой операции API
   - POST → запись появилась в БД с правильными данными
   - PUT/PATCH → данные обновились правильно
   - DELETE → запись удалена (или статус изменён)

4. **Performance** — скорость запросов, индексы

5. **Data Quality (8 критериев)**
   - Accuracy (точность)
   - Completeness (полнота)
   - Consistency (согласованность)
   - Uniqueness (уникальность)
   - Timeliness (актуальность)

### Ресурсы
- 🔗 [Database Testing (Guru99)](https://www.guru99.com/database-testing.html)
- 🔗 [Data Quality Criteria](https://www.prospecta.com/what-are-the-8-data-quality-criteria/)

---

## ✅ Чеклист по разделу

- [ ] Знаю разницу SQL и NoSQL, когда что применять
- [ ] Умею писать SELECT с WHERE, ORDER BY, LIMIT, GROUP BY
- [ ] Умею писать INSERT (одна и несколько записей)
- [ ] Умею писать UPDATE (с WHERE, без WHERE знаю опасность)
- [ ] Умею писать DELETE (безопасная практика через SELECT сначала)
- [ ] Знаю все типы JOIN и когда использовать каждый
- [ ] Умею написать запрос для проверки данных после API операции
- [ ] Знаю базовые операции MongoDB
- [ ] Понимаю что такое транзакция, ACID
- [ ] Прошёл практику на SQLZoo
