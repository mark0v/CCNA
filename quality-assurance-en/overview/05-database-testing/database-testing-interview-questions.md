# Database Testing Interview Questions

Source: user-provided Guru99 interview material, corrected and modernized  
Date added: 2026-06-11  
Related plan item: Database Testing  
Tags: QA, database testing, SQL, interview questions, backend testing  
Language: English  
Translation pair: quality-assurance/overview/05-database-testing/database-testing-interview-questions.md

## Summary

Database testing covers structure, stored data, business rules, transactions, database code, migrations, security, and performance.

A strong interview answer should provide:

1. a definition;
2. a concrete risk;
3. a verification example;
4. limitations and safety considerations.

Below are 25 current questions with concise answers and practical QA examples.

## Key Points

- Test constraints, transactions, concurrency, and migrations in addition to CRUD.
- A successful UI or API response does not prove correct persistence.
- Verify an `UPDATE` or `DELETE` condition with `SELECT` first.
- Test triggers and stored procedures through observable effects, outputs, errors, and transaction behavior.
- An index accelerates selected reads while increasing write and storage cost.
- Data loading requires mapping, counts, reconciliation, and invalid-record handling.
- Evaluate performance with representative volume and execution plans.
- Production data requires masking and least-privilege access.

## Questions And Answers

## 1. What Is Database Testing?

Database testing verifies the database layer and the data a system stores, modifies, and reads.

Primary areas:

- schema;
- data integrity;
- CRUD;
- transactions;
- stored procedures, functions, and triggers;
- migrations;
- security;
- performance;
- backup and recovery.

Backend testing is broader because it also covers APIs, services, queues, caches, and integrations.

## 2. What Do You Normally Check In A Database?

- tables, columns, and data types;
- primary and foreign keys;
- `NOT NULL`, `UNIQUE`, `CHECK`, and defaults;
- field length and precision;
- indexes;
- correct data after UI or API operations;
- transaction commit and rollback;
- stored database code;
- permissions;
- migration results;
- query performance.

## 3. How Do You Verify CRUD Through A UI Or API?

Map a business action to database state:

| Operation | UI/API example | Database verification |
| --- | --- | --- |
| Create | `POST /users` | New row or document with correct values |
| Read | Open profile | UI or API matches stored data |
| Update | `PATCH /users/42` | Only intended fields changed |
| Delete | Delete account | Hard delete or expected soft-delete state |

Also verify timestamps, audit data, related records, and side effects.

## 4. What Is Data-Driven Testing?

One test scenario runs against several datasets.

Example:

| Email | Age | Expected |
| --- | ---: | --- |
| valid@example.com | 25 | Accepted |
| invalid | 25 | Rejected |
| valid@example.com | -1 | Rejected |

Data can come from CSV, JSON, a database, a fixture factory, or a parameterized test.

## 5. What Is A JOIN And Which Types Exist?

A JOIN combines rows from two or more table sets.

Primary types:

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

Not every DBMS supports every syntax, such as `FULL OUTER JOIN`.

## 6. How Does INNER JOIN Differ From LEFT JOIN?

`INNER JOIN` returns matching rows only.

`LEFT JOIN` returns every row from the left side and matching rows from the right; unmatched right-side columns are `NULL`.

Find users without orders:

```sql
SELECT u.*
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
WHERE o.id IS NULL;
```

## 7. What Is An Index?

An index is an additional data structure that accelerates selected queries.

Common variants:

- B-tree;
- hash;
- unique;
- composite;
- partial or filtered;
- covering or included columns;
- full-text;
- specialized indexes such as GIN and GiST.

Available types depend on the DBMS.

QA verifies query plans, uniqueness, sort and filter coverage, and write impact.

## 8. Why Can An Index Harm A System?

Each index:

- consumes storage;
- changes during `INSERT`, `UPDATE`, and `DELETE`;
- can increase locks or contention;
- requires maintenance;
- can be useless with incorrect column order.

More indexes are not always better.

## 9. How Do You Test A Stored Procedure Or Function?

Verify:

- input parameters;
- output or result set;
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

Syntax varies by DBMS.

## 10. How Do You Test A Trigger?

1. Identify its triggering insert, update, or delete event.
2. Perform the action.
3. Verify the observable audit row, derived value, related table, or rejection.
4. Confirm that irrelevant changes do not trigger it.
5. Test rollback, recursion, bulk operations, and concurrency.

An audit log does not exist in every system and is not the only evidence.

## 11. How Do You Write A Database Test Case?

Include:

- objective;
- preconditions;
- input or action;
- query or observation method;
- expected database state;
- cleanup;
- required permissions;
- environment and dataset.

Example: after cancellation, order status becomes `cancelled`, inventory returns exactly once, and the payment record remains.

## 12. How Do DDL, DML, DCL, And TCL Differ?

| Group | Purpose | Examples |
| --- | --- | --- |
| DDL | Define database objects | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| DML | Read or change data | `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MERGE` |
| DCL | Control privileges | `GRANT`, `REVOKE` |
| TCL | Control transactions | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

Classification can vary slightly by source and DBMS.

The correct command is `DROP TABLE`, not `DELETE TABLE`.

## 13. What Are Primary And Foreign Keys?

A primary key uniquely identifies a row and cannot be `NULL`.

A foreign key requires a referenced value to exist in the parent table unless its definition permits otherwise.

QA verifies:

- duplicate primary key;
- missing parent;
- parent update or deletion;
- cascade, restrict, or set-null behavior;
- composite keys.

## 14. What Is A Constraint?

A constraint is a declarative data rule:

- `NOT NULL`;
- `UNIQUE`;
- `PRIMARY KEY`;
- `FOREIGN KEY`;
- `CHECK`;
- `DEFAULT` is related schema behavior, though not always classified as a constraint.

Test valid, invalid, and boundary data, including existing records during migration.

## 15. What Is Data Integrity?

Data integrity is the correctness and consistency of data throughout its lifecycle.

It includes:

- entity integrity;
- referential integrity;
- domain rules;
- uniqueness;
- transaction integrity;
- consistency across copies.

Example: a paid order references an existing user and has a non-negative total.

## 16. What Is A Transaction And ACID?

- **Atomicity:** all or nothing;
- **Consistency:** valid state to valid state;
- **Isolation:** concurrent operations follow defined rules;
- **Durability:** committed data survives according to the guarantee.

Test partial failure:

```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
ROLLBACK;
```

Both balances should remain unchanged after rollback.

## 17. Which Concurrency Problems Do You Know?

- lost update;
- dirty read;
- non-repeatable read;
- phantom read;
- write skew;
- deadlock.

Test realistic parallel operations such as the final inventory item, coupon use, balance transfer, or duplicate booking.

## 18. What Is An Isolation Level?

An isolation level determines which concurrent effects a transaction can observe.

Common SQL levels:

- Read Uncommitted;
- Read Committed;
- Repeatable Read;
- Serializable.

Exact behavior depends on the DBMS and MVCC implementation. Do not infer behavior only from the level name.

## 19. How Do You Test Data Loading Or ETL?

Verify:

- source-to-target mapping;
- source and target types;
- row counts;
- transformed values;
- null handling;
- duplicates;
- rejected records;
- encoding and special characters;
- dates and timezones;
- incremental load;
- rerun and idempotency;
- reconciliation totals.

An equal row count can still contain different data.

## 20. How Do You Test A Database Migration?

- schema version;
- columns, constraints, and indexes;
- data counts and checksums;
- defaults and backfills;
- old and new application compatibility;
- large-table duration and locks;
- rollback;
- interrupted migration;
- rerun safety;
- permissions;
- performance after migration.

Test migrations against production-like data volume.

## 21. What Is Database Performance Testing?

It evaluates latency, throughput, resource use, and stability under a database workload.

Measure:

- query duration;
- transactions per second;
- lock waits;
- CPU, memory, and I/O;
- connection pool;
- cache hit ratio;
- replication lag;
- slow queries.

Use representative data, indexes, and concurrency.

## 22. How Do You Investigate A Slow Query?

1. Reproduce with realistic parameters.
2. Record duration and returned rows.
3. Inspect the execution plan.
4. Check scans, estimates, joins, sorting, and indexes.
5. Check locks and resource pressure.
6. Compare before and after a change.

PostgreSQL example:

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT *
FROM orders
WHERE user_id = 42
ORDER BY created_at DESC;
```

`ANALYZE` executes the query. Be careful with data-changing statements.

## 23. How Do You Test A Database Manually And Safely?

- use a test or staging environment;
- use a read-only account where possible;
- verify `WHERE` through `SELECT`;
- use a transaction and rollback;
- avoid production personal data;
- document cleanup;
- never share credentials;
- limit result size;
- record database, version, and schema.

```sql
BEGIN;

SELECT * FROM users WHERE id = 42;
UPDATE users SET status = 'inactive' WHERE id = 42;
SELECT * FROM users WHERE id = 42;

ROLLBACK;
```

## 24. How Do You Test Database Security?

- authentication;
- role-based permissions;
- least privilege;
- unauthorized table or column access;
- SQL injection at the application boundary;
- encryption in transit and at rest;
- secrets management;
- audit events;
- backup access;
- masking;
- row or column-level security where used.

A tester account should not have administrator permissions without a reason.

## 25. What Should A Database Defect Include?

- environment and DBMS version;
- schema or migration version;
- application build;
- safe reproduction steps;
- sanitized query;
- expected and actual result;
- relevant record identifiers;
- timestamp and timezone;
- execution plan or error code;
- transaction and isolation context;
- evidence without credentials or personal data.

Never attach a complete production dump.

## Practical SQL Tasks

### Find Duplicates

```sql
SELECT email, COUNT(*) AS count
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

### Find Orphan Records

```sql
SELECT o.*
FROM orders o
LEFT JOIN users u ON u.id = o.user_id
WHERE u.id IS NULL;
```

### Verify Totals

```sql
SELECT order_id, SUM(quantity * unit_price) AS calculated_total
FROM order_items
GROUP BY order_id;
```

### Find Unexpected Nulls

```sql
SELECT *
FROM users
WHERE email IS NULL;
```

## Interview Focus

Be ready to explain:

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

