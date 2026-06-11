# NoSQL For QA

Source: user-provided Wikipedia material, corrected and adapted for QA  
Date added: 2026-06-11  
Related plan item: Database Testing  
Tags: QA, databases, NoSQL, CAP, BASE, eventual consistency, distributed systems  
Language: English  
Translation pair: quality-assurance/overview/05-database-testing/nosql-for-qa.md

## Summary

NoSQL, commonly expanded as **Not Only SQL**, is an umbrella term for database systems that do not use the classic relational table model as their only foundation.

Primary NoSQL families are:

- key-value;
- document;
- wide-column;
- graph.

NoSQL does not mean:

- no schema;
- no transactions;
- mandatory eventual consistency;
- automatic high performance;
- a complete replacement for SQL databases.

Each product has its own guarantees, query model, and operational trade-offs. QA should understand the specific system behavior instead of relying on the NoSQL label.

## Key Points

- NoSQL is a family of data models, not one technology.
- A schema often exists even when the database permits different fields across records.
- Many modern NoSQL systems support ACID operations or transactions of a defined scope.
- CAP describes a trade-off during a network partition, not a permanent choice of any two properties.
- CAP consistency and ACID consistency are different concepts.
- Eventual consistency promises convergence without new updates, but not a specific delay unless an additional SLA exists.
- Horizontal scaling requires suitable partition keys and is not automatic.
- Denormalization can accelerate reads while creating duplicated-data risks.
- Distributed failures, retries, and duplicate operations are central QA concerns.

## Notes

## Why NoSQL Emerged

Large internet systems increased demand for:

- horizontal scaling;
- distribution across nodes and regions;
- high write throughput;
- flexible data structures;
- predictable access patterns;
- availability during failures;
- large volumes of semi-structured data.

NoSQL systems often optimize specific workloads at the expense of some relational generality or ad hoc joins.

This does not make SQL obsolete. Modern architectures frequently use polyglot persistence, selecting different storage systems for different jobs.

## Primary Models

### Key-Value

Data is accessed by a unique key:

```text
session:8f31 -> serialized session
cart:user-17 -> cart state
```

Examples:

- Redis;
- Riak;
- DynamoDB in key-value scenarios.

Common uses:

- cache;
- sessions;
- counters;
- rate limits;
- temporary state.

QA focus:

- key uniqueness and format;
- TTL;
- expiration races;
- eviction;
- cache invalidation;
- atomic increments;
- fallback after cache failure;
- stale values.

### Document

Records are stored as nested documents:

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
- old and new document versions;
- nested arrays;
- missing versus `null`;
- document growth;
- validators;
- indexes;
- embedding and references.

### Wide-Column

Wide-column databases organize data around partition keys, rows, and column families.

Examples:

- Apache Cassandra;
- HBase;
- ScyllaDB.

Common uses:

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
- retries and duplicate writes.

A wide-column model is not the same as columnar OLAP storage. They are different architectures for different workloads.

### Graph

A graph database stores:

- nodes;
- relationships;
- properties.

Examples:

- Neo4j;
- Amazon Neptune;
- JanusGraph.

Common uses:

- social graphs;
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

GraphQL is not a graph database query language. It is an API query language. Graph databases can use Cypher, Gremlin, SPARQL, and other languages.

## Schema Flexibility

Schema-on-read or flexible schema does not mean no data contract.

Schema can be controlled through:

- database validators;
- application models;
- serialization;
- API contracts;
- event schemas;
- migration jobs;
- consumer compatibility rules.

QA should verify:

- required fields;
- permitted types;
- defaults;
- unknown fields;
- backward and forward compatibility;
- mixed versions in one collection;
- invalid historical data;
- index coverage.

Changing code can be easier than safely changing millions of existing records.

## Normalization And Denormalization

NoSQL models frequently duplicate data to optimize reads.

Example:

```json
{
  "orderId": "1042",
  "customerId": "17",
  "customerName": "Alex"
}
```

If the customer name changes, old orders can intentionally retain the original value or become inconsistent. The business rule determines which behavior is correct.

QA questions:

- Which copy is the source of truth?
- When are duplicates updated?
- Is stale data acceptable?
- Is there repair or reconciliation?
- What happens after a partial update?
- How are retries handled?

## ACID And BASE

### ACID

- **Atomicity:** an operation completes fully or not at all;
- **Consistency:** a transaction moves the database between valid states;
- **Isolation:** concurrent transactions avoid prohibited interference;
- **Durability:** committed data survives failure according to the guarantee.

### BASE

- **Basically Available;**
- **Soft State;**
- **Eventually Consistent.**

BASE describes some distributed-system designs. It is not mandatory for every NoSQL product.

A modern NoSQL database can combine:

- atomic single-record operations;
- multi-record transactions;
- tunable read and write consistency;
- eventual replica consistency;
- strong consistency for selected operations.

Always verify the specific DBMS and deployment documentation.

## CAP Theorem

CAP applies to distributed data systems during a **network partition**:

- **Consistency:** every read receives the latest successful write or an error;
- **Availability:** every request to a non-failing node receives a response;
- **Partition tolerance:** the system continues despite lost or delayed messages between node groups.

During a partition, the system must either:

- reject or wait to preserve consistency;
- respond while risking stale or conflicting data.

"Choose any two of three" is an oversimplification:

- distributed systems cannot simply exclude network partitions;
- the trade-off appears specifically during a partition;
- behavior can vary by operation;
- many products offer tunable consistency;
- latency and recovery also matter.

CAP consistency is not the C in ACID.

## Consistency Models

Possible guarantees:

| Model | Meaning |
| --- | --- |
| Strong consistency | A successful read sees the latest committed write |
| Eventual consistency | Replicas converge without new writes |
| Read-your-writes | A client sees its own successful writes |
| Monotonic reads | A client does not return to an older version |
| Causal consistency | Causally related operations are observed in order |
| Tunable consistency | The client selects read or write strength |

QA needs more than a label:

- scope;
- timeout;
- maximum expected lag;
- session behavior;
- failover behavior;
- conflict resolution.

## Partitioning And Sharding

Data is distributed using a partition or shard key.

A poor key causes:

- hot partitions;
- uneven storage;
- throttling;
- high latency;
- expensive cross-partition queries;
- difficult rebalancing.

Test:

- uniform and skewed key distribution;
- a high-volume single tenant;
- growing partitions;
- cross-partition queries;
- resharding or rebalancing;
- node addition and removal;
- migration under traffic.

## Replication And Failover

Test:

- replica lag;
- primary or leader failure;
- election;
- reads during failover;
- writes during failover;
- network split;
- node recovery;
- stale replica;
- regional outage;
- backup and restore.

Measure:

- rejected operations;
- unknown outcomes;
- potential data-loss window;
- recovery time;
- convergence time;
- duplicate operations.

## Retry And Idempotency

A distributed client might not know whether a write committed before a timeout.

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
- transaction or outbox pattern.

QA should test retry after timeout, connection reset, and leader change.

## Query And Index Testing

NoSQL does not mean no queries or indexes.

Verify:

- correct query results;
- filter semantics;
- sorting;
- pagination;
- missing fields;
- array and nested matching;
- index selection;
- full scans;
- compound-index order;
- index creation over existing data;
- write overhead;
- stale secondary index where the architecture permits it.

Use realistic volume. A query that is fast over 100 documents can fail over 100 million.

## Common Defects

- incompatible document versions;
- one logical ID stored in different formats;
- expired keys remain visible;
- stale cache overwrites new database state;
- hot partition;
- duplicate write after retry;
- lost update;
- unexpected stale read after write;
- tombstones degrade queries;
- denormalized copies disagree;
- failover produces an unknown transaction result;
- cleanup removes active data;
- production index is missing;
- permissive schema stores an invalid type.

## QA Test Matrix

- [ ] Data model and source of truth are documented.
- [ ] Schema and validation rules are tested.
- [ ] Missing, extra, null, and wrong-type fields are covered.
- [ ] Partition and shard keys are verified.
- [ ] Indexes match production queries.
- [ ] TTL, expiration, and cleanup are tested.
- [ ] Consistency guarantees are known and measured.
- [ ] Retries are idempotent.
- [ ] Node failure and network partition are covered.
- [ ] Replication lag and convergence are measured.
- [ ] Backup and restore are verified.
- [ ] Security, access control, and encryption are checked.
- [ ] Data migration supports mixed versions.
- [ ] Tests use representative data volume and distribution.

## Interview Focus

1. What does NoSQL mean?
2. Which four common NoSQL models do you know?
3. Does NoSQL mean schema-less?
4. How do ACID and BASE differ?
5. What does CAP actually describe?
6. How does eventual consistency affect testing?
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

