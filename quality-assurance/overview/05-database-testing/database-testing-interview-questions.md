# Database Testing: вопросы на собеседовании

Source: user-provided Guru99 interview material, corrected and modernized  
Date added: 2026-06-11  
Related plan item: Database Testing  
Tags: QA, database testing, SQL, interview questions, backend testing  
Language: Russian  
Translation pair: quality-assurance-en/overview/05-database-testing/database-testing-interview-questions.md

## Summary

Database testing проверяет structure, stored data, business rules, transactions, database code, migrations, security и performance.

На собеседовании хороший ответ должен включать:

1. определение;
2. конкретный риск;
3. пример проверки;
4. ограничения и безопасность.

Ниже — 25 актуальных вопросов с короткими ответами и QA-примерами.

## Key Points

- Проверяйте не только CRUD, но и constraints, transactions, concurrency и migrations.
- UI или API success не доказывает корректность persisted data.
- Перед `UPDATE` или `DELETE` проверяйте условие через `SELECT`.
- Trigger и stored procedure тестируются по observable effects, outputs, errors и transactions.
- Index ускоряет определённые reads, но увеличивает стоимость writes и storage.
- Data loading требует mapping, counts, reconciliation и обработку invalid records.
- Performance оценивается на representative volume и через execution plans.
- Production data требует masking и least-privilege access.

## Questions And Answers

## 1. Что такое Database Testing?

Database testing — проверка database layer и данных, которые система сохраняет, изменяет и читает.

Основные области:

- schema;
- data integrity;
- CRUD;
- transactions;
- stored procedures, functions и triggers;
- migrations;
- security;
- performance;
- backup and recovery.

Термин backend testing шире: backend также включает APIs, services, queues, cache и integrations.

## 2. Что обычно проверяют в базе данных?

- tables, columns и data types;
- primary/foreign keys;
- `NOT NULL`, `UNIQUE`, `CHECK`, defaults;
- field length and precision;
- indexes;
- correct data after UI/API operations;
- transaction commit and rollback;
- stored database code;
- permissions;
- migration results;
- query performance.

## 3. Как проверить CRUD через UI или API?

Сопоставьте business action с database state:

| Operation | UI/API example | Database verification |
| --- | --- | --- |
| Create | `POST /users` | New row/document with correct values |
| Read | Open profile | UI/API matches stored data |
| Update | `PATCH /users/42` | Only intended fields changed |
| Delete | Delete account | Hard delete or expected soft-delete state |

Проверяйте также timestamps, audit data, related records и side effects.

## 4. Что такое Data-Driven Testing?

Один test scenario выполняется с разными datasets.

Example:

| Email | Age | Expected |
| --- | ---: | --- |
| valid@example.com | 25 | Accepted |
| invalid | 25 | Rejected |
| valid@example.com | -1 | Rejected |

Data can come from CSV, JSON, database, fixture factory или parameterized test.

## 5. Что такое JOIN и какие бывают JOIN?

JOIN объединяет rows из двух или нескольких table sets.

Основные виды:

- `INNER JOIN`;
- `LEFT OUTER JOIN`;
- `RIGHT OUTER JOIN`;
- `FULL OUTER JOIN`;
- `CROSS JOIN`;
- self join as a usage pattern.

```sql
SELECT u.id, u.email, o.id AS order_id
FROM users u
LEFT JOIN orders o ON o.user_id = u.id;
```

Не все DBMS поддерживают каждый syntax, например `FULL OUTER JOIN`.

## 6. Чем INNER JOIN отличается от LEFT JOIN?

`INNER JOIN` возвращает только matching rows.

`LEFT JOIN` возвращает все rows слева и matching rows справа; при отсутствии совпадения right-side columns равны `NULL`.

Для поиска users без orders:

```sql
SELECT u.*
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
WHERE o.id IS NULL;
```

## 7. Что такое Index?

Index — дополнительная data structure, ускоряющая определённые queries.

Распространённые варианты:

- B-tree;
- hash;
- unique;
- composite;
- partial/filtered;
- covering/included columns;
- full-text;
- specialized indexes such as GIN/GiST.

Конкретные types зависят от DBMS.

QA проверяет query plan, uniqueness, sort/filter coverage и влияние на writes.

## 8. Почему Index может ухудшить систему?

Каждый index:

- занимает storage;
- обновляется при `INSERT`, `UPDATE`, `DELETE`;
- может увеличить lock/contention;
- требует maintenance;
- может быть бесполезен при неправильном column order.

Больше indexes не всегда лучше.

## 9. Как тестировать Stored Procedure или Function?

Проверьте:

- input parameters;
- output/result set;
- boundary and invalid values;
- changed tables;
- transaction behavior;
- errors and return codes;
- permissions;
- repeated calls;
- concurrency;
- execution time.

```sql
BEGIN;
CALL create_order(17, 'A1', 2);
-- Verify affected records.
ROLLBACK;
```

Syntax зависит от DBMS.

## 10. Как проверить Trigger?

1. Определите triggering event: insert, update или delete.
2. Выполните action.
3. Проверьте observable effect: audit row, derived value, related table или rejection.
4. Проверьте, что trigger не срабатывает при irrelevant change.
5. Проверьте rollback, recursion, bulk operation и concurrency.

Audit log существует не во всех systems и не является единственным доказательством.

## 11. Как написать Database Test Case?

Укажите:

- objective;
- preconditions;
- input/action;
- query or observation method;
- expected database state;
- cleanup;
- required permissions;
- environment and dataset.

Example: после отмены order status становится `cancelled`, inventory возвращается один раз, payment record не удаляется.

## 12. Чем DDL, DML, DCL и TCL отличаются?

| Group | Purpose | Examples |
| --- | --- | --- |
| DDL | Define database objects | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| DML | Read/change data | `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MERGE` |
| DCL | Control privileges | `GRANT`, `REVOKE` |
| TCL | Control transactions | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

Classification can vary slightly by source and DBMS.

Correct command is `DROP TABLE`, not `DELETE TABLE`.

## 13. Что такое Primary Key и Foreign Key?

Primary key uniquely identifies a row and cannot be `NULL`.

Foreign key требует, чтобы referenced value existed in parent table, если constraint это не разрешает иначе.

QA проверяет:

- duplicate primary key;
- missing parent;
- update/delete parent;
- cascade/restrict/set-null behavior;
- composite keys.

## 14. Что такое Constraint?

Constraint — declarative data rule:

- `NOT NULL`;
- `UNIQUE`;
- `PRIMARY KEY`;
- `FOREIGN KEY`;
- `CHECK`;
- `DEFAULT` is related schema behavior, though not always classified as a constraint.

Тестируйте valid, invalid и boundary data, а также existing records during migration.

## 15. Что такое Data Integrity?

Data integrity означает correctness и consistency данных на протяжении lifecycle.

Включает:

- entity integrity;
- referential integrity;
- domain rules;
- uniqueness;
- transaction integrity;
- consistency across copies.

Example: paid order должен ссылаться на существующего user и иметь non-negative total.

## 16. Что такое Transaction и ACID?

- **Atomicity:** all or nothing;
- **Consistency:** valid state to valid state;
- **Isolation:** concurrent operations follow defined rules;
- **Durability:** committed data survives according to guarantee.

Test partial failure:

```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
ROLLBACK;
```

После rollback оба balances должны остаться прежними.

## 17. Какие Concurrency Problems вы знаете?

- lost update;
- dirty read;
- non-repeatable read;
- phantom read;
- write skew;
- deadlock.

Проверяйте реальные parallel operations: последний товар, coupon usage, balance transfer, duplicate booking.

## 18. Что такое Isolation Level?

Isolation level определяет, какие concurrent effects видит transaction.

Common SQL levels:

- Read Uncommitted;
- Read Committed;
- Repeatable Read;
- Serializable.

Точное поведение зависит от DBMS и MVCC implementation. Не делайте вывод только по названию level.

## 19. Как тестировать Data Loading или ETL?

Проверьте:

- source-to-target mapping;
- source and target types;
- row counts;
- transformed values;
- null handling;
- duplicates;
- rejected records;
- encoding and special characters;
- dates/timezones;
- incremental load;
- rerun/idempotency;
- reconciliation totals.

Не ограничивайтесь сравнением общего count: одинаковое количество rows может содержать разные данные.

## 20. Как проверить Database Migration?

- schema version;
- columns, constraints и indexes;
- data counts and checksums;
- defaults and backfills;
- old/new application compatibility;
- large-table duration and locks;
- rollback;
- interrupted migration;
- rerun safety;
- permissions;
- performance after migration.

Migration должна тестироваться на production-like data volume.

## 21. Что такое Database Performance Testing?

Проверка latency, throughput, resource use и stability database workload.

Measure:

- query duration;
- transactions per second;
- lock waits;
- CPU, memory and I/O;
- connection pool;
- cache hit ratio;
- replication lag;
- slow queries.

Используйте representative data, indexes и concurrency.

## 22. Как найти медленный Query?

1. Reproduce with realistic parameters.
2. Record duration and returned rows.
3. Inspect execution plan.
4. Check scans, estimates, joins, sorting and indexes.
5. Check locks and resource pressure.
6. Compare before/after change.

PostgreSQL example:

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT *
FROM orders
WHERE user_id = 42
ORDER BY created_at DESC;
```

`ANALYZE` executes the query. Be careful with data-changing statements.

## 23. Как безопасно тестировать Database вручную?

- use test/staging environment;
- use read-only account when possible;
- verify `WHERE` through `SELECT`;
- use transaction and rollback;
- avoid production personal data;
- document cleanup;
- never share credentials;
- limit result size;
- record database/version/schema.

```sql
BEGIN;

SELECT * FROM users WHERE id = 42;
UPDATE users SET status = 'inactive' WHERE id = 42;
SELECT * FROM users WHERE id = 42;

ROLLBACK;
```

## 24. Как тестировать Database Security?

- authentication;
- role-based permissions;
- least privilege;
- unauthorized table/column access;
- SQL injection at application boundary;
- encryption in transit/at rest;
- secrets management;
- audit events;
- backup access;
- masking;
- row/column-level security where used.

Tester account не должен иметь admin permissions без необходимости.

## 25. Что приложить к Database Defect?

- environment and DBMS version;
- schema/migration version;
- application build;
- safe reproduction steps;
- sanitized query;
- expected and actual result;
- relevant record identifiers;
- timestamps/timezone;
- execution plan or error code;
- transaction/isolation context;
- evidence without credentials or personal data.

Не прикладывайте полный production dump.

## Practical SQL Tasks

### Найти duplicates

```sql
SELECT email, COUNT(*) AS count
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

### Найти orphan records

```sql
SELECT o.*
FROM orders o
LEFT JOIN users u ON u.id = o.user_id
WHERE u.id IS NULL;
```

### Проверить totals

```sql
SELECT order_id, SUM(quantity * unit_price) AS calculated_total
FROM order_items
GROUP BY order_id;
```

### Найти unexpected nulls

```sql
SELECT *
FROM users
WHERE email IS NULL;
```

## Interview Focus

Перед собеседованием уметь объяснить:

- CRUD and joins;
- keys and constraints;
- transactions and ACID;
- isolation and concurrency;
- stored procedures and triggers;
- data migration;
- indexes and execution plans;
- safe manual SQL;
- security and masking.

## Sources

- User-provided Guru99 article: "Top 25 Database Testing Interview Questions & Answers"
- [PostgreSQL SQL commands](https://www.postgresql.org/docs/current/sql-commands.html)
- [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
- [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html)

