# Load Model Design

Source: user-provided TMAP material, expanded for practical performance testing  
Date added: 2026-06-11  
Related plan item: Performance Testing  
Tags: QA, performance testing, load model, workload model, RPS, virtual users  
Language: English  
Translation pair: quality-assurance/overview/06-performance-testing/load-model-design.md

## Summary

A load model is a logical description of:

- which system or component is tested;
- which users and transactions create load;
- how frequently operations occur;
- how load changes over time;
- which initial state starts the test;
- which metrics and requirements define the result.

The load model connects business usage to performance-tool configuration. It should exist before test scripts and remain independent of a specific tool.

## Key Points

- Concurrent users do not define load without pace, think time, and transaction frequency.
- Convert business transactions per hour into arrival rate, throughput, and scenario mix.
- Open and closed workload models behave differently during saturation.
- Test-object boundaries determine environment and monitoring.
- Initial data, caches, queues, and sessions belong in the model.
- Ramp, steady-state, peak, and recovery phases should be explicit.
- Include client traffic and background jobs together.
- Compare planned load with generated and received load.
- Representativeness must balance risk, time, environment, and cost.

## Notes

## Load Model Contents

A minimum document contains:

1. performance requirements;
2. test object and boundaries;
3. user and traffic sources;
4. transactions and scenario mix;
5. workload model;
6. load profile over time;
7. initial state and test data;
8. environment;
9. metrics and observability;
10. pass/fail criteria;
11. assumptions and limitations.

## 1. Performance Requirements

Vague requirement:

```text
System supports 500 simultaneous users.
```

It does not define:

- how many users actively send requests;
- which actions they perform;
- session duration;
- think time;
- acceptable response time;
- permitted errors.

Better requirement:

```text
During the 30-minute peak:
- 500 active sessions;
- 250 browse requests/s;
- 25 search requests/s;
- 10 checkout transactions/s;
- checkout p95 < 800 ms;
- total error rate < 0.5%;
- no duplicate order or payment.
```

## 2. Test Object And Boundaries

The test object can be:

- complete user-to-database chain;
- public API;
- application service;
- database;
- queue consumer;
- cache;
- isolated component.

Document:

- included components;
- excluded components;
- real versus stubbed dependencies;
- entry and exit points;
- network path;
- data stores;
- background processing.

Boundaries affect interpretation. API latency without a browser and CDN is not end-user page time.

## 3. User And Traffic Types

| User type | Behavior |
| --- | --- |
| Visitor | Opens home and catalog |
| Searcher | Runs searches and filters |
| Buyer | Adds items and checks out |
| Support agent | Reads and updates customer records |
| Integration client | Sends API requests continuously |

Also include non-user traffic:

- scheduled jobs;
- webhooks;
- imports;
- message consumers;
- monitoring;
- retries;
- mobile background sync.

## 4. Transactions And Mix

Example hourly volume:

| Transaction | Per hour | Per second | Share |
| --- | ---: | ---: | ---: |
| Home page | 500 | 0.139 | 86.2% |
| Search or browse | 50 | 0.014 | 8.6% |
| Add to cart | 20 | 0.006 | 3.4% |
| Purchase | 10 | 0.003 | 1.7% |
| **Total** | **580** | **0.161** | **100%** |

Formula:

```text
transactions per second = transactions per hour / 3600
```

At 50 times higher peak traffic:

```text
total target rate = 0.161 * 50 = 8.05 transactions/s
```

Do not round a low-frequency critical transaction to zero. Use a longer run or scheduled arrival.

## Users Are Not Transactions

The same transaction volume can come from:

- many users taking rare actions;
- fewer active users acting frequently;
- an open arrival stream without persistent users.

These models affect:

- sessions;
- authentication;
- connections;
- cache locality;
- concurrency;
- data contention.

Choose the model closest to production.

## 5. Open And Closed Workloads

### Closed Model

Fixed users repeatedly execute scenarios:

```text
iteration -> response -> think time -> next iteration
```

When responses slow down, iteration rate decreases.

Suitable for:

- interactive sessions;
- limited user population;
- workflows with think time.

### Open Model

New iterations arrive at a defined rate independently of response completion.

Suitable for:

- public traffic;
- messages and events;
- external clients;
- traffic that does not slow down when the system becomes slow.

At saturation, an open model creates growing concurrency and queues like real incoming traffic.

## Little's Law

For a stable system, approximately:

```text
concurrency = arrival rate * average time in system
```

Example:

```text
100 requests/s * 0.5 s = 50 concurrent requests
```

If response time rises to two seconds:

```text
100 requests/s * 2 s = 200 concurrent requests
```

This explains why latency growth increases in-flight work even at a constant arrival rate.

Little's Law requires stable averages and consistent units. It is an estimate, not a replacement for measurement.

## Estimating Virtual Users

Approximation for a closed model:

```text
VUs ~= target iteration rate * (iteration duration + think time)
```

Example:

```text
target = 20 iterations/s
average iteration = 2 s
think time = 3 s

VUs ~= 20 * (2 + 3) = 100
```

Validate through calibration because scenarios have variable paths and response times.

## 6. Load Profile Over Time

Example:

```text
10 min warm-up
15 min ramp-up
45 min normal load
15 min peak
20 min normal load
10 min ramp-down
15 min recovery observation
```

For each phase, document:

- duration;
- arrival rate or VUs;
- scenario mix;
- background jobs;
- expected autoscaling;
- whether measurements are included.

Warm-up data should normally remain separate from steady-state results.

## Daily And Seasonal Patterns

Production traffic can include:

- morning ramp;
- lunch peak;
- evening peak;
- weekday and weekend differences;
- payday;
- campaign;
- Black Friday;
- batch windows.

Select:

- representative normal day;
- expected peak;
- known risk event.

Do not create an arbitrary smooth ramp when production traffic arrives in bursts.

## 7. Initial State

Define before every run:

- database volume;
- record distribution;
- cold or warm cache;
- queue depth;
- active sessions;
- inventory and balances;
- file and storage volume;
- replica health;
- autoscaling minimum;
- feature flags;
- clock and timezone.

Identical scripts with different initial states can produce incomparable results.

## Test Data Model

Document:

- unique and shared users;
- data cardinality;
- hot and cold records;
- read and write ratio;
- tenant distribution;
- cleanup;
- data growth per run;
- sensitive-data policy.

Example risk: every virtual user updates one account, creating artificial lock contention.

## 8. Test Environment

Record:

- component versions;
- node counts and resources;
- database and cache;
- load balancer;
- network;
- autoscaling;
- storage;
- observability;
- load generators;
- differences from production.

For a smaller environment, describe limitations rather than applying an unproven linear multiplier.

## 9. Indicators And Measurements

Client:

- planned and achieved rate;
- VUs and concurrency;
- latency percentiles;
- throughput;
- errors;
- dropped arrivals;
- business checks.

Server:

- CPU and memory;
- pools and queues;
- database latency and locks;
- cache hit ratio;
- messaging lag;
- disk and network;
- autoscaling;
- dependency latency.

Business:

- orders per minute;
- successful payments;
- processed messages;
- duplicate or lost operations.

## 10. Pass/Fail Criteria

Define thresholds for each important transaction:

| Transaction | Load | p95 | p99 | Error rate |
| --- | ---: | ---: | ---: | ---: |
| Home | 250 RPS | 300 ms | 700 ms | < 0.2% |
| Search | 25 RPS | 700 ms | 1500 ms | < 0.5% |
| Checkout | 10 TPS | 800 ms | 1500 ms | < 0.2% |

Add resource and recovery criteria when they represent real requirements.

Avoid universal rules such as every web response being below two seconds.

## Architecture Diagram

An optional diagram can show:

```text
Load generators
    -> CDN/load balancer
    -> application services
    -> cache/database
    -> queue/workers
    -> external dependencies
```

Mark:

- generated traffic;
- measured points;
- stubs;
- network boundaries;
- asynchronous flows.

## Validate The Model

Before the full test:

1. Run one user and verify correctness.
2. Run a short low-rate calibration.
3. Compare configured and achieved rates.
4. Confirm transaction proportions.
5. Confirm the server receives expected traffic.
6. Check data distribution.
7. Check generator saturation.
8. Verify monitoring timestamps.

Example:

```text
Planned checkout: 10 TPS
Generated: 10 TPS
Received by gateway: 9.9 TPS
Committed orders: 9.9 TPS
```

Explain any differences.

## Model From Production Data

Useful sources:

- access logs;
- API gateway metrics;
- analytics;
- APM traces;
- database metrics;
- queue metrics;
- business reports;
- capacity forecasts.

Clean the data:

- separate bots;
- exclude health checks;
- identify retries;
- distinguish success and failure;
- account for sampling;
- use peak windows rather than daily averages alone.

## Cost And Scope Trade-Offs

Balance:

- production representativeness;
- business risk;
- environment cost;
- generator and tool cost;
- data preparation;
- test duration;
- observability;
- analysis effort.

If a full-chain test is too expensive, combine:

- component benchmark;
- API load test;
- limited end-to-end test;
- production monitoring.

Document what remains untested.

## Load Model Template

```text
Objective:
Requirements:
Test object and boundaries:
Production evidence:
User and traffic types:
Transactions and hourly volume:
Scenario mix:
Open or closed model:
Think time and pacing:
Load phases:
Initial state:
Test data:
Environment:
Client metrics:
Server metrics:
Business checks:
Pass/fail criteria:
Stop conditions:
Assumptions:
Limitations:
```

## Common Mistakes

- specifying only concurrent users;
- copying a daily average instead of a peak;
- ignoring background traffic;
- using equal scenario shares without evidence;
- confusing requests with business transactions;
- omitting think time;
- failing to define initial data and cache state;
- measuring only client latency;
- not validating achieved rate;
- using one shared record for all users;
- excluding recovery phase;
- hiding environment differences.

## QA Checklist

- [ ] Requirements are measurable.
- [ ] Test boundaries are explicit.
- [ ] Production evidence supports the model.
- [ ] User and background traffic types are included.
- [ ] Transaction rates and proportions are calculated.
- [ ] Open or closed model is justified.
- [ ] Think time, pacing, and session behavior are defined.
- [ ] Ramp, steady, peak, and recovery phases exist.
- [ ] Initial state and test data are reproducible.
- [ ] Environment differences are documented.
- [ ] Client, server, and business metrics are included.
- [ ] Planned and achieved load are compared.
- [ ] Pass/fail and stop criteria are defined.

## Interview Focus

1. What is a load model?
2. Why are concurrent users insufficient?
3. How do you calculate TPS from hourly volume?
4. How do open and closed models differ?
5. What does Little's Law explain?
6. How do you estimate virtual users?
7. What belongs in the initial state?
8. How do you validate generated load?
9. How do you derive a model from production?

## Sources

- User-provided TMAP material: "Load model | Performance testing"
- [Grafana k6 scenarios](https://grafana.com/docs/k6/latest/using-k6/scenarios/)
- [Grafana k6 arrival-rate VUs](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/arrival-rate-vu-allocation/)
- [Apache JMeter best practices](https://jmeter.apache.org/usermanual/best-practices.html)

