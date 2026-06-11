# NoSQL для QA

Source: user-provided Wikipedia material, corrected and adapted for QA  
Date added: 2026-06-11  
Related plan item: Database Testing  
Tags: QA, databases, NoSQL, CAP, BASE, eventual consistency, distributed systems  
Language: Russian  
Translation pair: quality-assurance-en/overview/05-database-testing/nosql-for-qa.md

## Summary

NoSQL, или **Not Only SQL**, — общее название database systems, которые не используют классическую relational table model как единственную основу.

Основные NoSQL families:

- key-value;
- document;
- wide-column;
- graph.

NoSQL не означает:

- отсутствие schema;
- отсутствие transactions;
- обязательную eventual consistency;
- автоматическую высокую производительность;
- полную замену SQL databases.

Каждый продукт имеет собственные guarantees, query model и operational trade-offs. Для QA важнее знать конкретное поведение системы, чем прикреплять к ней общий ярлык NoSQL.

## Key Points

- NoSQL — семейство разных data models, а не одна технология.
- Schema часто существует, даже если database не требует одинаковых fields во всех records.
- Многие современные NoSQL systems поддерживают ACID operations или transactions определённого scope.
- CAP описывает trade-off во время network partition, а не постоянный выбор «любых двух свойств».
- Consistency в CAP и consistency в ACID — разные понятия.
- Eventual consistency означает convergence при отсутствии новых updates, но не гарантирует конкретную задержку без дополнительного SLA.
- Horizontal scaling требует правильных partition keys и не происходит автоматически.
- Denormalization ускоряет некоторые reads, но создаёт риск рассогласования копий данных.
- Distributed failure, retry и duplicate operations являются основными QA-рисками.

## Notes

## Почему появился NoSQL

Рост интернет-систем усилил требования к:

- горизонтальному масштабированию;
- распределению данных между nodes и regions;
- высокой write throughput;
- flexible data structures;
- predictable access patterns;
- availability при отказах;
- обработке больших объёмов semi-structured data.

NoSQL systems часто оптимизируют конкретные workloads, жертвуя универсальностью relational model или ad hoc joins.

Это не делает SQL устаревшим. Современные architectures часто используют polyglot persistence: разные storage systems для разных задач.

## Основные модели

### Key-Value

Data доступно по unique key:

```text
session:8f31 -> serialized session
cart:user-17 -> cart state
```

Examples:

- Redis;
- Riak;
- DynamoDB in key-value scenarios.

Typical use:

- cache;
- sessions;
- counters;
- rate limits;
- temporary state.

QA focus:

- key uniqueness and format;
- TTL;
- expiration race;
- eviction;
- cache invalidation;
- atomic increment;
- fallback after unavailable cache;
- stale value.

### Document

Records хранятся как nested documents:

```json
{
  "_id": "order-1042",
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

QA focus:

- required and optional fields;
- field types;
- old/new document versions;
- nested arrays;
- missing versus `null`;
- document growth;
- validators;
- indexes;
- embedding and references.

### Wide-Column

Wide-column databases organize data around partition keys, rows and column families.

Examples:

- Apache Cassandra;
- HBase;
- ScyllaDB.

Typical use:

- high write volume;
- telemetry;
- large distributed datasets;
- known query patterns.

QA focus:

- partition key;
- hot and oversized partitions;
- clustering order;
- tombstones;
- TTL;
- consistency level;
- replication lag;
- node failure;
- retry and duplicate writes.

Wide-column model не равен columnar OLAP storage. Это разные architectures с разными workloads.

### Graph

Graph database stores:

- nodes;
- relationships;
- properties.

Examples:

- Neo4j;
- Amazon Neptune;
- JanusGraph.

Typical use:

- social graph;
- fraud detection;
- recommendations;
- network topology;
- authorization relationships.

QA focus:

- edge direction and type;
- missing or duplicate relationships;
- cycles;
- traversal depth;
- path authorization;
- dense graph performance;
- deletion of connected nodes.

GraphQL не является graph database query language. Это API query language. Graph databases могут использовать Cypher, Gremlin, SPARQL и другие languages.

## Schema Flexibility

Schema-on-read или flexible schema не означает отсутствия data contract.

Schema может контролироваться через:

- database validators;
- application models;
- serialization;
- API contracts;
- event schemas;
- migration jobs;
- consumer compatibility rules.

QA должен проверить:

- какие fields обязательны;
- допустимые types;
- defaults;
- unknown fields;
- backward/forward compatibility;
- mixed versions in one collection;
- invalid historical data;
- index coverage.

Изменить code проще, чем безопасно изменить миллионы существующих records.

## Normalization И Denormalization

NoSQL models часто дублируют data для быстрых reads.

Example:

```json
{
  "orderId": "1042",
  "customerId": "17",
  "customerName": "Alex"
}
```

Если имя customer изменится, old orders могут сохранить старое значение намеренно или стать inconsistent — это определяется business rule.

QA questions:

- какая копия является source of truth;
- когда обновляются duplicates;
- допустима ли stale data;
- есть ли repair/reconciliation;
- что происходит при partial update;
- как обрабатывается retry.

## ACID И BASE

### ACID

- **Atomicity:** операция выполняется целиком или не выполняется;
- **Consistency:** transaction переводит database из одного valid state в другой;
- **Isolation:** concurrent transactions не создают запрещённое взаимодействие;
- **Durability:** committed data сохраняется после failure согласно guarantee.

### BASE

- **Basically Available;**
- **Soft State;**
- **Eventually Consistent.**

BASE — архитектурное описание некоторых distributed systems, а не обязательное свойство всех NoSQL products.

Современная NoSQL database может сочетать:

- atomic single-record operations;
- multi-record transactions;
- tunable read/write consistency;
- eventual consistency for replicas;
- strong consistency for selected operations.

Проверяйте документацию конкретного DBMS и deployment.

## CAP Theorem

CAP относится к distributed data systems при **network partition**:

- **Consistency:** каждый read получает последнее successful write или error;
- **Availability:** каждый request к non-failing node получает response;
- **Partition tolerance:** system продолжает работать при потере/delay сообщений между groups of nodes.

Во время partition система должна решить:

- отказать или ждать, сохраняя consistency;
- ответить, рискуя вернуть stale/conflicting data.

Фраза «выбрать любые два из трёх» слишком груба:

- network partitions нельзя просто исключить в distributed system;
- trade-off особенно проявляется именно во время partition;
- behavior может отличаться по operation;
- многие products позволяют настраивать consistency;
- latency и recovery также важны.

CAP consistency не равна букве C в ACID.

## Consistency Models

Possible guarantees:

| Model | Meaning |
| --- | --- |
| Strong consistency | Successful read видит latest committed write |
| Eventual consistency | Replicas converge без новых writes |
| Read-your-writes | Client видит собственные successful writes |
| Monotonic reads | Client не возвращается к более старой версии |
| Causal consistency | Причинно связанные operations наблюдаются в порядке |
| Tunable consistency | Client выбирает read/write strength |

QA должен знать не только label, но и:

- scope;
- timeout;
- maximum expected lag;
- session behavior;
- behavior after failover;
- conflict resolution.

## Partitioning And Sharding

Data распределяется по nodes с помощью partition/shard key.

Плохой key вызывает:

- hot partition;
- uneven storage;
- throttling;
- high latency;
- expensive cross-partition queries;
- difficult rebalancing.

Test:

- uniform and skewed key distribution;
- high-volume single tenant;
- growing partition;
- cross-partition query;
- resharding/rebalancing;
- node addition/removal;
- migration during traffic.

## Replication And Failover

Test scenarios:

- replica lag;
- primary/leader failure;
- election;
- read during failover;
- write during failover;
- network split;
- node recovery;
- stale replica;
- regional outage;
- backup and restore.

Measure:

- rejected operations;
- unknown outcomes;
- data loss window;
- recovery time;
- convergence time;
- duplicate operations.

## Retry And Idempotency

Distributed client может не знать, был ли write committed before timeout.

Dangerous flow:

1. client sends create order;
2. server commits;
3. response is lost;
4. client retries;
5. duplicate order appears.

Protection:

- idempotency key;
- unique business key;
- compare-and-set;
- atomic conditional write;
- deduplication table;
- transaction/outbox pattern.

QA должен тестировать retry после timeout, connection reset и leader change.

## Query And Index Testing

NoSQL does not mean no queries or indexes.

Check:

- query returns correct records;
- filter semantics;
- sorting;
- pagination;
- missing fields;
- array/nested matching;
- index selection;
- full scan;
- compound index order;
- index creation on existing data;
- write overhead;
- stale secondary index, if architecture permits it.

Test with realistic volume. A query that is fast on 100 documents may fail on 100 million.

## Common Defects

- documents of incompatible versions;
- same logical ID stored in different formats;
- expired keys remain visible;
- stale cache overrides new database state;
- hot partition;
- duplicate write after retry;
- lost update;
- read after write returns stale data unexpectedly;
- tombstones degrade queries;
- denormalized copies disagree;
- failover produces unknown transaction result;
- cleanup deletes active data;
- index is missing in production;
- permissive schema stores invalid type.

## QA Test Matrix

- [ ] Data model and source of truth are documented.
- [ ] Schema/validation rules are tested.
- [ ] Missing, extra, null and wrong-type fields are covered.
- [ ] Partition and shard keys are verified.
- [ ] Indexes match production queries.
- [ ] TTL, expiration and cleanup are tested.
- [ ] Consistency guarantees are known and measured.
- [ ] Retries are idempotent.
- [ ] Node failure and network partition are covered.
- [ ] Replication lag and convergence are measured.
- [ ] Backup and restore are verified.
- [ ] Security, access control and encryption are checked.
- [ ] Data migration supports mixed versions.
- [ ] Tests use representative data volume and distribution.

## Interview Focus

1. What does NoSQL mean?
2. Which four common NoSQL models do you know?
3. Does NoSQL mean schema-less?
4. How do ACID and BASE differ?
5. What does CAP actually describe?
6. How does eventual consistency affect tests?
7. What is a hot partition?
8. Why must retries be idempotent?
9. How do document and wide-column databases differ?

## Sources

- User-provided Wikipedia article: "NoSQL"
- [MongoDB data modeling](https://www.mongodb.com/docs/manual/data-modeling/)
- [Redis data types](https://redis.io/docs/latest/develop/data-types/)
- [Apache Cassandra architecture](https://cassandra.apache.org/doc/latest/cassandra/architecture/)
- [Neo4j graph database concepts](https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/)
- [A Critique of the CAP Theorem](https://arxiv.org/abs/1509.05393)

