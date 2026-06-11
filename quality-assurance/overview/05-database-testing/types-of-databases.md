# Типы баз данных для QA

Source: user-provided Indeed article, corrected and expanded with official database documentation  
Date added: 2026-06-11  
Related plan item: Database Testing  
Tags: QA, databases, SQL, NoSQL, relational, document, graph, key-value  
Language: Russian  
Translation pair: quality-assurance-en/overview/05-database-testing/types-of-databases.md

## Summary

Database — организованное хранилище данных, которым управляет database management system, или DBMS.

Базы данных можно классифицировать по разным независимым признакам:

- **data model:** relational, document, key-value, wide-column, graph;
- **workload:** operational, analytical, transactional;
- **deployment:** centralized, distributed, cloud, embedded;
- **licensing:** open-source или commercial;
- **audience:** enterprise, application-specific, personal.

Эти признаки нельзя считать взаимоисключающими типами. Например, PostgreSQL может быть relational, open-source, operational, distributed through extensions/services и deployed in cloud одновременно.

## Key Points

- Relational databases хранят данные в tables with rows and typed columns.
- NoSQL — общее название нескольких разных non-relational models, а не один формат.
- Document databases хранят records как documents.
- Key-value databases оптимизированы для доступа по key.
- Wide-column databases подходят для больших распределённых workloads.
- Graph databases делают relationships частью основной модели.
- Cloud, distributed, commercial и open-source описывают deployment или licensing, а не data model.
- Object-oriented database не является разновидностью relational database.
- Spreadsheet может выглядеть как table, но не заменяет DBMS.
- Для QA тип базы определяет запросы, consistency expectations и характер рисков.

## Notes

## Основные термины

| Term | Meaning |
| --- | --- |
| Database | Организованный набор связанных данных |
| DBMS | Software для хранения, чтения, изменения и защиты данных |
| Schema | Описание структуры и правил данных |
| Query | Запрос на чтение или изменение |
| Transaction | Набор операций, выполняемый как логическая единица |
| Index | Дополнительная структура для ускорения доступа |
| Constraint | Правило целостности данных |

Database — это данные, а DBMS — система, которая ими управляет. В разговорной речи эти понятия часто смешивают.

## Классификация по Data Model

### Relational Databases

Relational database хранит данные в relations, обычно представленных tables.

Основные элементы:

- rows;
- typed columns;
- primary keys;
- foreign keys;
- constraints;
- joins;
- SQL;
- transactions.

Примеры:

- PostgreSQL;
- MySQL/MariaDB;
- Microsoft SQL Server;
- Oracle Database;
- SQLite.

Подходит для:

- payments и orders;
- inventory;
- user accounts;
- systems with strong integrity rules;
- reporting with structured relationships.

QA проверяет:

- column types и nullability;
- primary/foreign keys;
- unique constraints;
- referential integrity;
- transaction commit/rollback;
- joins и aggregation;
- data migrations;
- concurrent updates.

### Document Databases

Document database хранит records как documents, часто BSON или JSON-like structures.

Пример MongoDB document:

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

Примеры:

- MongoDB;
- Couchbase;
- CouchDB.

Преимущества:

- flexible document shape;
- nested data;
- convenient mapping to application objects;
- horizontal scaling options.

QA проверяет:

- required fields despite flexible schema;
- old and new document versions;
- nested arrays and objects;
- missing, extra и differently typed fields;
- indexes;
- update semantics;
- consistency between duplicated data.

Flexible schema не означает отсутствие schema. Правила могут находиться в application code, validation configuration или data contracts.

### Key-Value Databases

Key-value database хранит value, доступное по unique key.

```text
session:8f31 -> serialized session data
cart:user-17 -> cart state
```

Примеры:

- Redis;
- Amazon DynamoDB in key-value use cases;
- Riak.

Типичные задачи:

- cache;
- sessions;
- counters;
- rate limits;
- queues and streams;
- short-lived state.

QA проверяет:

- key format;
- TTL and expiration;
- cache invalidation;
- behavior after restart;
- eviction;
- stale values;
- atomic operations;
- fallback when storage is unavailable.

### Wide-Column Databases

Wide-column systems organize data around partition keys, rows и column families and are designed for large distributed workloads.

Примеры:

- Apache Cassandra;
- HBase;
- ScyllaDB.

Подходит для:

- high write volume;
- time-series-like workloads;
- geographically distributed systems;
- predictable query patterns.

QA проверяет:

- partition key selection;
- supported query patterns;
- eventual consistency;
- duplicate/retried writes;
- ordering;
- node failure;
- replication delay;
- large partitions.

### Graph Databases

Graph database хранит:

- nodes;
- relationships;
- properties.

Примеры:

- Neo4j;
- Amazon Neptune;
- JanusGraph.

Подходит для:

- social connections;
- fraud detection;
- recommendations;
- network topology;
- access relationships;
- route finding.

QA проверяет:

- relationship direction and type;
- duplicate edges;
- missing nodes;
- traversal depth;
- cycles;
- authorization paths;
- query performance on dense graphs.

### Time-Series Databases

Time-series database оптимизирована для timestamped measurements.

Примеры:

- InfluxDB;
- TimescaleDB;
- Prometheus storage model.

QA проверяет:

- timestamps and time zones;
- ordering;
- duplicate samples;
- late-arriving data;
- retention;
- downsampling;
- gaps;
- aggregation windows.

### Object-Oriented Databases

Object-oriented database хранит data as objects with identity, attributes and relationships that map to object-oriented programming concepts.

Это отдельный model, а не subtype relational database.

Такие systems встречаются реже, но могут использоваться для complex engineering, scientific или domain object graphs.

## Классификация по Workload

### Operational / OLTP

Operational databases обслуживают ежедневные transactions:

- create order;
- update balance;
- change profile;
- reserve inventory.

Обычно важны low latency, concurrency и correctness of small writes.

### Analytical / OLAP

Analytical systems выполняют scans, aggregations и historical analysis.

Примеры:

- data warehouse;
- columnar analytical database;
- reporting platform.

QA проверяет source-to-target mapping, ETL/ELT, totals, dimensions, late data и report consistency.

### Hybrid

Некоторые platforms поддерживают operational and analytical workloads, но конкретные guarantees и performance profile нужно проверять, а не выводить из marketing category.

## Классификация по Deployment

### Centralized

Один primary database system или location обслуживает пользователей.

Риски:

- single point of failure;
- capacity limits;
- maintenance downtime.

### Distributed

Data размещается или реплицируется между несколькими nodes.

Возможные преимущества:

- availability;
- scalability;
- geographic proximity.

Риски:

- replication lag;
- split brain;
- conflict resolution;
- stale reads;
- partial failure.

### Cloud Database

Cloud database размещена в cloud infrastructure или предоставляется как managed service.

Она не обязана быть отдельным data model: cloud service может быть relational, document, graph или другим.

QA учитывает:

- regions and availability zones;
- network security;
- backups;
- scaling;
- maintenance windows;
- service limits;
- managed failover.

### Embedded Database

Embedded database работает внутри application или рядом с ним.

Примеры:

- SQLite in mobile applications;
- local key-value stores;
- embedded analytical engines.

QA проверяет file lifecycle, migrations, corruption recovery, concurrency, backup and app update.

## Licensing И Ownership

`Open-source` и `commercial` не описывают способ хранения данных.

Один product может иметь:

- open-source core;
- commercial edition;
- paid cloud service;
- proprietary extensions.

При выборе учитывают license, support, operational cost, ecosystem и vendor lock-in, но QA test design в первую очередь зависит от behavior and guarantees.

## SQL Vs NoSQL

| Characteristic | Relational/SQL | NoSQL families |
| --- | --- | --- |
| Model | Tables and relations | Documents, keys, columns, graphs |
| Schema | Usually explicit and enforced | Often flexible or application-enforced |
| Relationships | Keys and joins | Embedding, references, edges, denormalization |
| Transactions | Common core capability | Depends on product and operation scope |
| Scaling | Vertical and horizontal options | Often designed for horizontal distribution |
| Best fit | Structured data and integrity | Specific access patterns and flexible/distributed workloads |

`SQL vs NoSQL` is not a simple choice between correctness and scale. Modern products overlap in transactions, indexing, replication and cloud deployment.

## Spreadsheet Vs Database

Spreadsheet:

- optimized for interactive calculations;
- stores values and formulas in cells;
- usually edited directly by users;
- has limited concurrency and integrity controls.

DBMS:

- supports queries and controlled updates;
- manages concurrent users;
- enforces constraints;
- provides transactions, permissions, indexes and recovery.

A spreadsheet can act as a small personal dataset, but it is not equivalent to a production database system.

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

1. What are the main entities and relationships?
2. Which queries must be fast?
3. What consistency guarantees are required?
4. What is the read/write volume?
5. How should the system scale?
6. Is offline or embedded storage required?
7. What are retention and compliance requirements?
8. What failures must the system survive?
9. Which operational skills does the team have?
10. What migration and backup strategy exists?

There is no universally best database. A product can use several types for different jobs: relational storage for orders, Redis for cache and sessions, a search engine for full-text search, and a warehouse for analytics.

## QA Checklist

- [ ] Data model and DBMS are identified.
- [ ] Schema or validation rules are documented.
- [ ] Keys, constraints and indexes are understood.
- [ ] Consistency and transaction guarantees are known.
- [ ] Replication and failover behavior is defined.
- [ ] Backup, restore and retention are tested.
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

