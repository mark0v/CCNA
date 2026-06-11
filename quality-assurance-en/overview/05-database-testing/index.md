# 05 - Databases And SQL

Language: English  
Translation pair: quality-assurance/overview/05-database-testing/index.md

## Section Goal

This section covers database knowledge required for QA work:

- database models and use cases;
- relational databases and SQL;
- CRUD verification;
- joins, filtering, grouping, and aggregation;
- constraints and referential integrity;
- transactions and ACID properties;
- NoSQL basics;
- schema, data integrity, migration, and performance testing.

## Learning Path

1. Understand how relational, document, key-value, wide-column, and graph databases differ.
2. Learn safe `SELECT`, `INSERT`, `UPDATE`, and `DELETE` operations.
3. Practice `INNER`, `LEFT`, `RIGHT`, and `FULL OUTER JOIN`.
4. Verify database state after API and UI operations.
5. Test constraints, transactions, concurrency, migrations, and data quality.
6. Learn the basic query model of at least one NoSQL database.

## QA Focus

A tester does not need to be a database administrator, but should be able to:

- locate relevant records;
- compare persisted data with API and UI results;
- recognize invalid, missing, duplicate, or stale data;
- avoid destructive queries;
- understand transaction boundaries;
- provide reproducible evidence without exposing production data.

## Safety

Before changing data:

```sql
SELECT *
FROM users
WHERE id = 42;
```

Use a transaction when the environment and permissions allow it:

```sql
BEGIN;

UPDATE users
SET status = 'inactive'
WHERE id = 42;

-- Verify the result, then choose one:
ROLLBACK;
-- COMMIT;
```

Never run an `UPDATE` or `DELETE` in a shared environment until the `WHERE` condition has been verified.

