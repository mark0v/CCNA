# Types Of Databases For QA

Source: user-provided Indeed article, corrected and expanded with official database documentation  
Date added: 2026-06-11  
Related plan item: Database Testing  
Tags: QA, databases, SQL, NoSQL, relational, document, graph, key-value  
Language: English  
Translation pair: quality-assurance/overview/05-database-testing/types-of-databases.md

## Summary

A database is an organized data store managed by a database management system, or DBMS.

Databases can be classified along several independent dimensions:

- **data model:** relational, document, key-value, wide-column, graph;
- **workload:** operational, analytical, transactional;
- **deployment:** centralized, distributed, cloud, embedded;
- **licensing:** open-source or commercial;
- **audience:** enterprise, application-specific, personal.

These labels are not mutually exclusive types. PostgreSQL, for example, can simultaneously be relational, open-source, operational, cloud-hosted, and distributed through extensions or services.

## Key Points

- Relational databases store data in tables with rows and typed columns.
- NoSQL is an umbrella for several non-relational models, not one format.
- Document databases store records as documents.
- Key-value databases optimize access by key.
- Wide-column databases support large distributed workloads.
- Graph databases make relationships a first-class part of the model.
- Cloud, distributed, commercial, and open-source describe deployment or licensing rather than the data model.
- An object-oriented database is not a relational database subtype.
- A spreadsheet can resemble a table but does not replace a DBMS.
- For QA, the database type changes query patterns, consistency expectations, and risks.

## Notes

## Core Terms

| Term | Meaning |
| --- | --- |
| Database | Organized collection of related data |
| DBMS | Software that stores, reads, changes, and protects data |
| Schema | Description of data structure and rules |
| Query | Request to read or modify data |
| Transaction | Operations executed as one logical unit |
| Index | Additional structure that accelerates access |
| Constraint | Data integrity rule |

A database is the data, while a DBMS is the system managing it. Everyday usage often mixes the terms.

## Classification By Data Model

### Relational Databases

A relational database stores data in relations, normally represented as tables.

Core elements:

- rows;
- typed columns;
- primary keys;
- foreign keys;
- constraints;
- joins;
- SQL;
- transactions.

Examples:

- PostgreSQL;
- MySQL/MariaDB;
- Microsoft SQL Server;
- Oracle Database;
- SQLite.

Suitable for:

- payments and orders;
- inventory;
- user accounts;
- systems with strong integrity rules;
- reporting over structured relationships.

QA verifies:

- column types and nullability;
- primary and foreign keys;
- unique constraints;
- referential integrity;
- transaction commit and rollback;
- joins and aggregation;
- data migrations;
- concurrent updates.

### Document Databases

A document database stores records as documents, often in BSON or JSON-like structures.

Example MongoDB-style document:

```json
{
  "_id": "order-1042",
  "customerId": "user-17",
  "status": "paid",
  "items": [
    { "sku": "A1", "quantity": 2 }
  ]
}
```

Examples:

- MongoDB;
- Couchbase;
- CouchDB.

Benefits:

- flexible document shape;
- nested data;
- convenient mapping to application objects;
- horizontal scaling options.

QA verifies:

- required fields despite flexible schema;
- old and new document versions;
- nested arrays and objects;
- missing, extra, and differently typed fields;
- indexes;
- update semantics;
- consistency between duplicated data.

Flexible schema does not mean no schema. Rules can live in application code, validation configuration, or data contracts.

### Key-Value Databases

A key-value database stores a value accessed by a unique key.

```text
session:8f31 -> serialized session data
cart:user-17 -> cart state
```

Examples:

- Redis;
- Amazon DynamoDB in key-value use cases;
- Riak.

Common uses:

- cache;
- sessions;
- counters;
- rate limits;
- queues and streams;
- short-lived state.

QA verifies:

- key format;
- TTL and expiration;
- cache invalidation;
- behavior after restart;
- eviction;
- stale values;
- atomic operations;
- fallback when storage is unavailable.

### Wide-Column Databases

Wide-column systems organize data around partition keys, rows, and column families and target large distributed workloads.

Examples:

- Apache Cassandra;
- HBase;
- ScyllaDB.

Suitable for:

- high write volume;
- time-series-like workloads;
- geographically distributed systems;
- predictable query patterns.

QA verifies:

- partition key selection;
- supported query patterns;
- eventual consistency;
- duplicate or retried writes;
- ordering;
- node failure;
- replication delay;
- large partitions.

### Graph Databases

A graph database stores:

- nodes;
- relationships;
- properties.

Examples:

- Neo4j;
- Amazon Neptune;
- JanusGraph.

Suitable for:

- social connections;
- fraud detection;
- recommendations;
- network topology;
- access relationships;
- route finding.

QA verifies:

- relationship direction and type;
- duplicate edges;
- missing nodes;
- traversal depth;
- cycles;
- authorization paths;
- query performance on dense graphs.

### Time-Series Databases

A time-series database is optimized for timestamped measurements.

Examples:

- InfluxDB;
- TimescaleDB;
- the Prometheus storage model.

QA verifies:

- timestamps and time zones;
- ordering;
- duplicate samples;
- late-arriving data;
- retention;
- downsampling;
- gaps;
- aggregation windows.

### Object-Oriented Databases

An object-oriented database stores data as objects with identity, attributes, and relationships that map to object-oriented programming concepts.

It is a separate model, not a relational database subtype.

These systems are less common but can support complex engineering, scientific, or domain object graphs.

## Classification By Workload

### Operational / OLTP

Operational databases serve day-to-day transactions:

- create an order;
- update a balance;
- change a profile;
- reserve inventory.

Low latency, concurrency, and correctness of small writes are usually important.

### Analytical / OLAP

Analytical systems perform scans, aggregations, and historical analysis.

Examples:

- data warehouse;
- columnar analytical database;
- reporting platform.

QA verifies source-to-target mapping, ETL/ELT, totals, dimensions, late data, and report consistency.

### Hybrid

Some platforms support operational and analytical workloads, but guarantees and performance profiles must be tested rather than inferred from a marketing category.

## Classification By Deployment

### Centralized

One primary database system or location serves users.

Risks:

- single point of failure;
- capacity limits;
- maintenance downtime.

### Distributed

Data is partitioned or replicated across nodes.

Potential benefits:

- availability;
- scalability;
- geographic proximity.

Risks:

- replication lag;
- split brain;
- conflict resolution;
- stale reads;
- partial failure.

### Cloud Database

A cloud database runs in cloud infrastructure or is offered as a managed service.

It is not a separate data model: a cloud service can be relational, document, graph, or another type.

QA considers:

- regions and availability zones;
- network security;
- backups;
- scaling;
- maintenance windows;
- service limits;
- managed failover.

### Embedded Database

An embedded database runs inside or alongside an application.

Examples:

- SQLite in mobile applications;
- local key-value stores;
- embedded analytical engines.

QA verifies file lifecycle, migrations, corruption recovery, concurrency, backup, and app update.

## Licensing And Ownership

`Open-source` and `commercial` do not describe how data is stored.

One product can have:

- an open-source core;
- a commercial edition;
- a paid cloud service;
- proprietary extensions.

Selection considers licensing, support, operating cost, ecosystem, and vendor lock-in, but QA test design primarily depends on behavior and guarantees.

## SQL Versus NoSQL

| Characteristic | Relational/SQL | NoSQL families |
| --- | --- | --- |
| Model | Tables and relations | Documents, keys, columns, graphs |
| Schema | Usually explicit and enforced | Often flexible or application-enforced |
| Relationships | Keys and joins | Embedding, references, edges, denormalization |
| Transactions | Common core capability | Depends on product and operation scope |
| Scaling | Vertical and horizontal options | Often designed for horizontal distribution |
| Best fit | Structured data and integrity | Specific access patterns and flexible/distributed workloads |

`SQL versus NoSQL` is not simply correctness versus scale. Modern products overlap in transactions, indexing, replication, and cloud deployment.

## Spreadsheet Versus Database

A spreadsheet:

- is optimized for interactive calculations;
- stores values and formulas in cells;
- is usually edited directly by users;
- has limited concurrency and integrity controls.

A DBMS:

- supports queries and controlled updates;
- manages concurrent users;
- enforces constraints;
- provides transactions, permissions, indexes, and recovery.

A spreadsheet can hold a small personal dataset but is not equivalent to a production database system.

## How Database Type Changes QA Work

| Database type | QA focus |
| --- | --- |
| Relational | Constraints, joins, transactions, migrations |
| Document | Shape variations, nested fields, schema evolution |
| Key-value | TTL, invalidation, eviction, atomicity |
| Wide-column | Partitions, consistency, replication, retry |
| Graph | Relationships, traversal, cycles, path authorization |
| Time-series | Time, retention, windows, late data |
| Distributed | Failover, stale reads, conflict, partial outage |
| Embedded | Local migration, file lifecycle, corruption recovery |

## Choosing A Database

Ask:

1. What are the primary entities and relationships?
2. Which queries must be fast?
3. Which consistency guarantees are required?
4. What are the read and write volumes?
5. How should the system scale?
6. Is offline or embedded storage required?
7. What are the retention and compliance requirements?
8. Which failures must the system survive?
9. Which operational skills does the team have?
10. What migration and backup strategy exists?

There is no universally best database. A product can use a relational store for orders, Redis for cache and sessions, a search engine for full-text search, and a warehouse for analytics.

## QA Checklist

- [ ] Data model and DBMS are identified.
- [ ] Schema or validation rules are documented.
- [ ] Keys, constraints, and indexes are understood.
- [ ] Consistency and transaction guarantees are known.
- [ ] Replication and failover behavior is defined.
- [ ] Backup, restore, and retention are tested.
- [ ] Migration paths are covered.
- [ ] Sensitive data and permissions are reviewed.
- [ ] Test queries are non-destructive.
- [ ] Production data is not copied without masking.

## Interview Focus

1. What is the difference between a database and a DBMS?
2. How do relational and document databases differ?
3. Which NoSQL models do you know?
4. When is a key-value store useful?
5. What does a graph database store?
6. Why are cloud and open-source not data models?
7. How does eventual consistency affect testing?
8. Is a spreadsheet a database?

## Sources

- User-provided article: "What Are the Different Types of Databases?"
- [PostgreSQL: Relational database concepts](https://www.postgresql.org/docs/current/tutorial-concepts.html)
- [MongoDB: Databases and collections](https://www.mongodb.com/docs/manual/core/databases-and-collections/)
- [Redis data types](https://redis.io/docs/latest/develop/data-types/)
- [Neo4j graph database concepts](https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/)

