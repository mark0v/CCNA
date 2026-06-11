# MongoDB vs PostgreSQL для QA

Source: user-provided MongoDB comparison, balanced with official MongoDB and PostgreSQL documentation  
Date added: 2026-06-11  
Related plan item: Database Testing  
Tags: QA, databases, MongoDB, PostgreSQL, SQL, NoSQL, transactions, schema  
Language: Russian  
Translation pair: quality-assurance-en/overview/05-database-testing/mongodb-vs-postgresql.md

## Summary

MongoDB и PostgreSQL — general-purpose database systems с разными основными data models:

- **PostgreSQL** — relational DBMS с SQL, tables, constraints, joins и mature transaction model;
- **MongoDB** — document database, хранящая BSON documents в collections и использующая MongoDB Query API и aggregation pipeline.

Обе системы поддерживают:

- indexes;
- ACID transactions;
- replication;
- high availability;
- JSON-like data;
- aggregation;
- managed cloud deployment.

Выбор нельзя свести к формуле «PostgreSQL для простого, MongoDB для масштаба» или наоборот. Он зависит от data relationships, query patterns, consistency, schema evolution, operations и опыта команды.

## Key Points

- PostgreSQL rows имеют declared columns and types, но также могут хранить и индексировать `jsonb`.
- MongoDB documents могут иметь flexible shape, но production collections часто требуют schema validation.
- PostgreSQL relationships обычно моделируются foreign keys и joins.
- MongoDB часто использует embedding или references; `$lookup` предоставляет join-like operation.
- Обе системы поддерживают multi-operation ACID transactions.
- MongoDB single-document write atomic, поэтому embedding может уменьшить необходимость multi-document transaction.
- PostgreSQL scaling не ограничивается только увеличением одного сервера: доступны read replicas, partitioning, extensions и distributed services.
- MongoDB sharding встроен в platform, но shard key и distributed operations требуют отдельного тестирования.
- Performance определяется workload, indexes, data model и queries, а не названием database.

## Notes

## Terminology

| PostgreSQL | MongoDB |
| --- | --- |
| Database | Database |
| Table | Collection |
| Row | Document |
| Column | Field |
| Primary key | `_id` |
| Foreign key | Reference by stored identifier |
| JOIN | Embedding, `$lookup`, application join |
| `GROUP BY` | `$group` in aggregation pipeline |
| Index | Index |
| View/materialized view | View/on-demand materialized result pattern |

Это приблизительное соответствие. Collection не обеспечивает автоматически те же constraints, что relational table.

## Data Model

### PostgreSQL

```sql
CREATE TABLE customers (
    id BIGSERIAL PRIMARY KEY,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE orders (
    id BIGSERIAL PRIMARY KEY,
    customer_id BIGINT NOT NULL REFERENCES customers(id),
    status TEXT NOT NULL,
    total NUMERIC(12, 2) NOT NULL CHECK (total >= 0)
);
```

Преимущества:

- explicit schema;
- typed columns;
- declarative constraints;
- normalized relationships;
- powerful joins;
- predictable cross-record integrity.

Риски для QA:

- incorrect migration;
- broken foreign key;
- wrong nullability/default;
- decimal precision;
- lock contention;
- query plan regression.

### MongoDB

```javascript
db.orders.insertOne({
  customerId: "user-17",
  status: "paid",
  total: Decimal128("49.90"),
  items: [
    { sku: "A1", quantity: 2 }
  ]
})
```

Преимущества:

- related data can be embedded;
- nested arrays and objects;
- document shape can evolve incrementally;
- application object often maps naturally to one document.

Риски для QA:

- missing or differently typed fields;
- incompatible old documents;
- uncontrolled document growth;
- duplicate denormalized data;
- array update errors;
- absent validation.

## Schema: Strict Vs Flexible

PostgreSQL schema is normally declared through DDL:

```sql
ALTER TABLE users
ADD COLUMN preferred_language TEXT;
```

MongoDB allows documents with different shapes in one collection, but can enforce rules with JSON Schema validation.

Flexible schema is useful for gradual evolution, but it moves responsibility:

- validation may live in app code;
- readers must tolerate old/new shapes;
- migrations can become lazy;
- analytics must handle absent fields;
- indexes may exist only for some documents.

For QA, ask:

1. Which fields are required?
2. Which versions of documents exist?
3. Who applies defaults?
4. Are invalid writes rejected by app, database, or both?
5. How is backward compatibility verified?

## PostgreSQL JSONB

PostgreSQL is not limited to scalar relational columns. `jsonb` stores parsed JSON-like data and supports operators and GIN indexes.

```sql
CREATE TABLE events (
    id BIGSERIAL PRIMARY KEY,
    payload JSONB NOT NULL
);

CREATE INDEX events_payload_gin
ON events USING GIN (payload);

SELECT *
FROM events
WHERE payload @> '{"type":"purchase"}';
```

QA considerations:

- `jsonb` does not preserve whitespace or object key order;
- duplicate object keys keep only the last value;
- SQL `NULL` and JSON `null` differ;
- whole-row updates can affect contention for large documents;
- flexible JSON still benefits from predictable structure.

This overlap means the choice is not simply tables versus JSON.

## Relationships: Normalize Or Embed

### PostgreSQL normalized model

Store customers, orders and items in separate tables and connect them through keys.

Best when:

- entities change independently;
- many relationships reuse the same record;
- cross-record integrity is critical;
- ad hoc joins and reports are common.

### MongoDB embedded model

Store order items inside the order document.

Best when:

- data is usually read together;
- child lifecycle belongs to parent;
- the aggregate fits document size limits;
- one-document atomic update is valuable.

Use references when:

- embedded data grows without bounds;
- many documents share one entity;
- related data changes independently;
- duplication becomes risky.

Neither normalization nor embedding is universally correct. Model for actual access patterns.

## Query Comparison

### Insert

PostgreSQL:

```sql
INSERT INTO users (user_id, age, status)
VALUES ('bcd001', 45, 'A');
```

MongoDB:

```javascript
db.users.insertOne({
  user_id: "bcd001",
  age: 45,
  status: "A"
})
```

### Read

PostgreSQL:

```sql
SELECT *
FROM users
WHERE age > 25;
```

MongoDB:

```javascript
db.users.find({ age: { $gt: 25 } })
```

### Update Many

PostgreSQL:

```sql
UPDATE users
SET status = 'C'
WHERE age > 25;
```

MongoDB:

```javascript
db.users.updateMany(
  { age: { $gt: 25 } },
  { $set: { status: "C" } }
)
```

Important correction: `updateOne()` updates one matching document. Use `updateMany()` when SQL would update every matching row.

## Transactions

### PostgreSQL

```sql
BEGIN;

INSERT INTO orders (customer_id, status, total)
VALUES (17, 'paid', 49.90);

UPDATE inventory
SET quantity = quantity - 2
WHERE sku = 'A1' AND quantity >= 2;

COMMIT;
```

### MongoDB

```javascript
const session = db.getMongo().startSession()
session.startTransaction()

// Run operations through collections associated with this session.

session.commitTransaction()
```

Both support multi-operation ACID transactions, but test:

- commit;
- explicit rollback/abort;
- application exception;
- timeout;
- retry;
- write conflict;
- connection loss;
- duplicate request;
- partial business failure.

MongoDB documentation recommends good data modeling instead of using distributed transactions as a substitute for every relationship. Multi-document and cross-shard transactions add cost and complexity.

## Concurrency And Consistency

PostgreSQL uses MVCC and provides transaction isolation levels. MongoDB provides atomic document writes, transactions, read concerns and write concerns.

QA must know:

- required isolation;
- read preference;
- write concern;
- replication lag tolerance;
- whether stale reads are acceptable;
- retry behavior;
- idempotency guarantees.

Examples:

- two users purchase the last item;
- two workers update one order;
- a read immediately follows a write;
- primary node fails during commit;
- client retries after an unknown result.

Database defaults may not match business guarantees.

## Indexes

Both systems support multiple index types. Indexes accelerate reads but consume storage and make writes more expensive.

PostgreSQL:

```sql
CREATE INDEX orders_status_created_idx
ON orders (status, created_at DESC);
```

MongoDB:

```javascript
db.orders.createIndex({ status: 1, createdAt: -1 })
```

QA checks:

- expected index exists;
- field order matches query;
- unique constraint/index rejects duplicates;
- query uses index;
- sorting is covered;
- partial/sparse behavior;
- index build and migration;
- write performance after adding indexes.

Compare `EXPLAIN`/`EXPLAIN ANALYZE` in PostgreSQL with `explain()` in MongoDB.

## Aggregation And Joins

PostgreSQL offers SQL joins, window functions, CTEs and grouping.

MongoDB aggregation pipeline supports stages such as:

- `$match`;
- `$project`;
- `$group`;
- `$sort`;
- `$unwind`;
- `$lookup`;
- `$unionWith`.

`$lookup` is useful but does not mean every normalized relational workload maps efficiently to MongoDB. Test cardinality, memory, indexes and result correctness.

## Scaling And Availability

### PostgreSQL

Common options:

- vertical scaling;
- streaming/logical replication;
- read replicas;
- table partitioning;
- connection pooling;
- sharding extensions or distributed PostgreSQL products;
- managed cloud services.

### MongoDB

Common options:

- replica sets;
- horizontal sharding;
- distributed reads and writes;
- managed MongoDB Atlas clusters.

QA for distributed deployment:

- primary election;
- node outage;
- regional failure;
- replication lag;
- stale reads;
- shard key distribution;
- hot shard;
- chunk migration;
- retryable writes;
- backup and restore.

Built-in sharding reduces some implementation work but does not eliminate data-model or operational risks.

## Data Types

MongoDB BSON includes types such as:

- string;
- int32/int64;
- double;
- Decimal128;
- date;
- binary;
- ObjectId;
- arrays/documents.

PostgreSQL offers:

- numeric types;
- text;
- date/time;
- UUID;
- arrays;
- JSON/JSONB;
- ranges;
- network types;
- geometric types;
- extensions and custom types.

For QA, verify numeric precision, timezone, null semantics, identifier conversion and driver serialization.

## Migration Risks

Moving PostgreSQL to MongoDB is a data-model redesign, not just syntax conversion.

Test:

- table-to-document mapping;
- joins converted to embedding/references;
- primary/foreign key conversion;
- numeric and timestamp precision;
- null versus missing field;
- duplicate keys;
- ordering;
- transaction boundaries;
- sequence/identity replacement;
- row counts and checksums;
- ongoing sync during cutover;
- rollback plan.

The reverse migration has similar risks because flexible documents must map into explicit columns and constraints.

## When PostgreSQL Often Fits Better

- complex relationships and joins;
- strong declarative integrity;
- financial or transactional records;
- ad hoc SQL reporting;
- broad SQL tooling and skills;
- mixed relational and JSONB data;
- workloads requiring rich SQL features.

## When MongoDB Often Fits Better

- document-shaped aggregates;
- rapidly evolving but governed document structures;
- nested data read together;
- built-in sharding is a core requirement;
- high-volume distributed document workloads;
- application teams centered on MongoDB Query API and Atlas ecosystem.

These are tendencies, not automatic decisions. Benchmark with representative data and queries.

## QA Comparison Matrix

| Area | PostgreSQL focus | MongoDB focus |
| --- | --- | --- |
| Schema | DDL, columns, constraints | Document versions, validators |
| Integrity | PK/FK/check/unique | Validators, app rules, references |
| Relations | Joins and cardinality | Embed/reference and `$lookup` |
| Transactions | Isolation and locks | Session, concerns, multi-document cost |
| JSON | `jsonb`, operators, GIN | Native BSON document model |
| Scaling | Replicas, partitioning, distribution layer | Replica sets, shards, shard key |
| Migration | DDL and data migrations | Shape evolution and backfill |
| Diagnostics | SQL plans, locks, statistics | Pipeline plans, profiler, replication |

## Interview Focus

1. How do table/row and collection/document differ?
2. Does MongoDB have a schema?
3. Does PostgreSQL support JSON documents?
4. When should MongoDB embed data rather than reference it?
5. Do both systems support ACID transactions?
6. Why are multi-document transactions not a replacement for data modeling?
7. How do scaling approaches differ?
8. What would you test during PostgreSQL-to-MongoDB migration?

## Sources

- User-provided MongoDB comparison
- [PostgreSQL JSON types](https://www.postgresql.org/docs/current/datatype-json.html)
- [PostgreSQL transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)
- [MongoDB data modeling](https://www.mongodb.com/docs/manual/data-modeling/)
- [MongoDB transactions](https://www.mongodb.com/docs/manual/core/transactions/)
- [MongoDB schema validation](https://www.mongodb.com/docs/manual/core/schema-validation/)

