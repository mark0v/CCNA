# MongoDB Vs PostgreSQL For QA

Source: user-provided MongoDB comparison, balanced with official MongoDB and PostgreSQL documentation  
Date added: 2026-06-11  
Related plan item: Database Testing  
Tags: QA, databases, MongoDB, PostgreSQL, SQL, NoSQL, transactions, schema  
Language: English  
Translation pair: quality-assurance/overview/05-database-testing/mongodb-vs-postgresql.md

## Summary

MongoDB and PostgreSQL are general-purpose database systems with different primary data models:

- **PostgreSQL** is a relational DBMS with SQL, tables, constraints, joins, and a mature transaction model;
- **MongoDB** is a document database that stores BSON documents in collections and uses the MongoDB Query API and aggregation pipeline.

Both support:

- indexes;
- ACID transactions;
- replication;
- high availability;
- JSON-like data;
- aggregation;
- managed cloud deployment.

The choice is not "PostgreSQL for simple systems and MongoDB for scale," or the reverse. It depends on relationships, query patterns, consistency, schema evolution, operations, and team skills.

## Key Points

- PostgreSQL rows use declared columns and types, but can also store and index `jsonb`.
- MongoDB documents can have flexible shapes, but production collections often need schema validation.
- PostgreSQL relationships normally use foreign keys and joins.
- MongoDB commonly uses embedding or references; `$lookup` provides a join-like operation.
- Both systems support multi-operation ACID transactions.
- A MongoDB single-document write is atomic, so embedding can reduce the need for multi-document transactions.
- PostgreSQL scaling is not limited to a larger single server: read replicas, partitioning, extensions, and distributed services are available.
- MongoDB includes platform-level sharding, but shard keys and distributed operations require dedicated testing.
- Performance depends on workload, indexes, data model, and queries rather than the database name.

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
| `GROUP BY` | `$group` in the aggregation pipeline |
| Index | Index |
| View/materialized view | View/on-demand materialized result pattern |

This is an approximate mapping. A collection does not automatically provide the same constraints as a relational table.

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

Benefits:

- explicit schema;
- typed columns;
- declarative constraints;
- normalized relationships;
- powerful joins;
- predictable cross-record integrity.

QA risks:

- incorrect migration;
- broken foreign key;
- wrong nullability or default;
- decimal precision;
- lock contention;
- query-plan regression.

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

Benefits:

- related data can be embedded;
- nested arrays and objects;
- document shape can evolve incrementally;
- an application object often maps naturally to one document.

QA risks:

- missing or differently typed fields;
- incompatible old documents;
- uncontrolled document growth;
- duplicated denormalized data;
- array update errors;
- missing validation.

## Schema: Strict Versus Flexible

PostgreSQL schema is normally declared through DDL:

```sql
ALTER TABLE users
ADD COLUMN preferred_language TEXT;
```

MongoDB allows different document shapes in one collection, but can enforce rules with JSON Schema validation.

Flexible schema moves responsibility:

- validation can live in application code;
- readers must tolerate old and new shapes;
- migrations can become lazy;
- analytics must handle absent fields;
- indexes may cover only part of the collection.

QA should ask:

1. Which fields are required?
2. Which document versions exist?
3. Who applies defaults?
4. Are invalid writes rejected by the app, database, or both?
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

- `jsonb` does not preserve whitespace or object-key order;
- duplicate object keys keep only the last value;
- SQL `NULL` and JSON `null` differ;
- whole-row updates can cause contention for large documents;
- flexible JSON still benefits from predictable structure.

This overlap means the choice is not simply tables versus JSON.

## Relationships: Normalize Or Embed

### PostgreSQL Normalized Model

Store customers, orders, and items in separate tables connected through keys.

Best when:

- entities change independently;
- many relationships reuse the same record;
- cross-record integrity is critical;
- ad hoc joins and reports are common.

### MongoDB Embedded Model

Store order items inside the order document.

Best when:

- data is normally read together;
- child lifecycle belongs to the parent;
- the aggregate fits document-size limits;
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

Important correction: `updateOne()` changes one matching document. Use `updateMany()` when the SQL statement would update every matching row.

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

Both support multi-operation ACID transactions. Test:

- commit;
- explicit rollback or abort;
- application exception;
- timeout;
- retry;
- write conflict;
- connection loss;
- duplicate request;
- partial business failure.

MongoDB documentation recommends sound data modeling rather than using distributed transactions as a substitute for every relationship. Multi-document and cross-shard transactions add cost and complexity.

## Concurrency And Consistency

PostgreSQL uses MVCC and provides transaction isolation levels. MongoDB provides atomic document writes, transactions, read concerns, and write concerns.

QA must know:

- required isolation;
- read preference;
- write concern;
- replication-lag tolerance;
- whether stale reads are acceptable;
- retry behavior;
- idempotency guarantees.

Examples:

- two users purchase the last item;
- two workers update one order;
- a read immediately follows a write;
- the primary node fails during commit;
- the client retries after an unknown result.

Database defaults may not match business guarantees.

## Indexes

Both systems support multiple index types. Indexes speed up reads but consume storage and increase write cost.

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
- field order matches the query;
- unique constraint or index rejects duplicates;
- query uses the index;
- sorting is covered;
- partial or sparse behavior;
- index build and migration;
- write performance after adding indexes.

Compare `EXPLAIN` or `EXPLAIN ANALYZE` in PostgreSQL with `explain()` in MongoDB.

## Aggregation And Joins

PostgreSQL offers SQL joins, window functions, CTEs, and grouping.

The MongoDB aggregation pipeline includes stages such as:

- `$match`;
- `$project`;
- `$group`;
- `$sort`;
- `$unwind`;
- `$lookup`;
- `$unionWith`.

`$lookup` is useful but does not mean every normalized relational workload maps efficiently to MongoDB. Test cardinality, memory, indexes, and result correctness.

## Scaling And Availability

### PostgreSQL

Common options:

- vertical scaling;
- streaming or logical replication;
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

For distributed deployment, test:

- primary election;
- node outage;
- regional failure;
- replication lag;
- stale reads;
- shard-key distribution;
- hot shard;
- chunk migration;
- retryable writes;
- backup and restore.

Built-in sharding reduces implementation work but does not remove data-model or operational risks.

## Data Types

MongoDB BSON includes:

- string;
- int32 and int64;
- double;
- Decimal128;
- date;
- binary;
- ObjectId;
- arrays and documents.

PostgreSQL offers:

- numeric types;
- text;
- date and time;
- UUID;
- arrays;
- JSON and JSONB;
- ranges;
- network types;
- geometric types;
- extensions and custom types.

QA should verify numeric precision, timezone, null semantics, identifier conversion, and driver serialization.

## Migration Risks

Moving from PostgreSQL to MongoDB is a data-model redesign, not a syntax conversion.

Test:

- table-to-document mapping;
- joins converted to embedding or references;
- primary and foreign key conversion;
- numeric and timestamp precision;
- null versus missing field;
- duplicate keys;
- ordering;
- transaction boundaries;
- sequence or identity replacement;
- row counts and checksums;
- ongoing synchronization during cutover;
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
- built-in sharding as a core requirement;
- high-volume distributed document workloads;
- teams centered on MongoDB Query API and Atlas.

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

1. How do a table/row and collection/document differ?
2. Does MongoDB have a schema?
3. Does PostgreSQL support JSON documents?
4. When should MongoDB embed data rather than reference it?
5. Do both systems support ACID transactions?
6. Why are multi-document transactions not a replacement for data modeling?
7. How do the scaling approaches differ?
8. What would you test during a PostgreSQL-to-MongoDB migration?

## Sources

- User-provided MongoDB comparison
- [PostgreSQL JSON types](https://www.postgresql.org/docs/current/datatype-json.html)
- [PostgreSQL transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)
- [MongoDB data modeling](https://www.mongodb.com/docs/manual/data-modeling/)
- [MongoDB transactions](https://www.mongodb.com/docs/manual/core/transactions/)
- [MongoDB schema validation](https://www.mongodb.com/docs/manual/core/schema-validation/)

