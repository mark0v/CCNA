# Проектирование Load Model

Source: user-provided TMAP material, expanded for practical performance testing  
Date added: 2026-06-11  
Related plan item: Performance Testing  
Tags: QA, performance testing, load model, workload model, RPS, virtual users  
Language: Russian  
Translation pair: quality-assurance-en/overview/06-performance-testing/load-model-design.md

## Summary

Load model — логическое описание того:

- какой system or component тестируется;
- какие users и transactions создают нагрузку;
- с какой частотой выполняются operations;
- как load меняется во времени;
- в каком initial state начинается test;
- какие metrics и requirements определяют результат.

Load model связывает business usage с настройками performance tool. Он должен появиться до test script и не зависеть от конкретного инструмента.

## Key Points

- Concurrent users недостаточно для описания нагрузки без pace, think time и transaction frequency.
- Business transactions per hour необходимо перевести в arrival rate, throughput и scenario mix.
- Open и closed workload models создают разное поведение при saturation.
- Test object определяет boundaries, environment и monitoring.
- Initial data, cache, queues and sessions являются частью model.
- Ramp, steady state, peak и recovery phases должны быть явными.
- Client load и background jobs нужно учитывать вместе.
- Planned load необходимо сравнивать с фактически generated and received load.
- Representativeness всегда балансируется с risk, time, environment и cost.

## Notes

## Из чего состоит Load Model

Минимальный документ содержит:

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

Нечёткое требование:

```text
System supports 500 simultaneous users.
```

Неизвестно:

- сколько users actively send requests;
- какие actions они выполняют;
- сколько длится session;
- есть ли think time;
- какой response time допустим;
- какая доля errors разрешена.

Более точное требование:

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

Test object может быть:

- complete user-to-database chain;
- public API;
- application service;
- database;
- queue consumer;
- cache;
- isolated component.

Документируйте:

- included components;
- excluded components;
- real versus stubbed dependencies;
- entry and exit points;
- network path;
- data stores;
- background processing.

Boundary влияет на interpretation. API latency without browser and CDN is not end-user page time.

## 3. User And Traffic Types

Users отличаются behavior:

| User type | Behavior |
| --- | --- |
| Visitor | Opens home and catalog |
| Searcher | Runs searches and filters |
| Buyer | Adds items and checks out |
| Support agent | Reads and updates customer records |
| Integration client | Sends API requests continuously |

Также учитывайте non-user traffic:

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
| Search/browse | 50 | 0.014 | 8.6% |
| Add to cart | 20 | 0.006 | 3.4% |
| Purchase | 10 | 0.003 | 1.7% |
| **Total** | **580** | **0.161** | **100%** |

Formula:

```text
transactions per second = transactions per hour / 3600
```

For 50 times more peak traffic:

```text
total target rate = 0.161 * 50 = 8.05 transactions/s
```

Do not round low-frequency critical transactions to zero. Use a longer run or scheduled arrival.

## Users Are Not Transactions

Одинаковую transaction volume можно создать по-разному:

- many users with rare actions;
- fewer active users with frequent actions;
- open arrival stream without persistent users.

Эти models по-разному влияют на:

- sessions;
- authentication;
- connections;
- cache locality;
- concurrency;
- data contention.

Выбирайте модель, похожую на production.

## 5. Open And Closed Workloads

### Closed Model

Fixed users repeatedly execute scenarios:

```text
iteration -> response -> think time -> next iteration
```

При slow response iteration rate снижается.

Подходит для:

- interactive sessions;
- limited user population;
- workflows with think time.

### Open Model

New iterations arrive at a defined rate independently of response completion.

Подходит для:

- public traffic;
- messages/events;
- external clients;
- traffic that does not slow down when system becomes slow.

При saturation open model создаёт growing concurrency and queues, как реальный incoming traffic.

## Little's Law

Для stable system приблизительно:

```text
concurrency = arrival rate * average time in system
```

Example:

```text
100 requests/s * 0.5 s = 50 concurrent requests
```

Если response time вырастет до 2 seconds:

```text
100 requests/s * 2 s = 200 concurrent requests
```

Это объясняет, почему latency growth увеличивает in-flight work даже при постоянном arrival rate.

Little's Law требует stable averages and consistent units. Это estimate, не замена measurement.

## Estimating Virtual Users

Approximation for closed model:

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

Validate with calibration because scenarios have variable paths and response times.

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

Document for each phase:

- duration;
- arrival rate or VUs;
- scenario mix;
- background jobs;
- expected autoscaling;
- measurement inclusion/exclusion.

Warm-up data often should not be combined with steady-state results.

## Daily And Seasonal Patterns

Production traffic can have:

- morning ramp;
- lunch peak;
- evening peak;
- weekday/weekend differences;
- payday;
- campaign;
- Black Friday;
- batch windows.

Choose:

- representative normal day;
- expected peak;
- known risk event.

Do not create an arbitrary smooth ramp when production traffic arrives in bursts.

## 7. Initial State

Define before each run:

- database volume;
- record distribution;
- cache cold/warm state;
- queue depth;
- active sessions;
- inventory and balances;
- file/storage volume;
- replica health;
- autoscaling minimum;
- feature flags;
- clock/timezone.

The same scripts with different initial state can produce incomparable results.

## Test Data Model

Document:

- unique and shared users;
- data cardinality;
- hot and cold records;
- read/write ratio;
- tenant distribution;
- cleanup;
- data growth per run;
- sensitive-data policy.

Example risk: all virtual users update one account, creating artificial lock contention.

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

If the environment is smaller, describe expected limitations instead of applying an unproven linear multiplier.

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

Define thresholds per important transaction:

| Transaction | Load | p95 | p99 | Error rate |
| --- | ---: | ---: | ---: | ---: |
| Home | 250 RPS | 300 ms | 700 ms | < 0.2% |
| Search | 25 RPS | 700 ms | 1500 ms | < 0.5% |
| Checkout | 10 TPS | 800 ms | 1500 ms | < 0.2% |

Add resource and recovery criteria where they are real requirements.

Avoid universal rules such as every web response must be below two seconds.

## Architecture Diagram

An optional diagram should show:

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
- async flows.

## Validate The Model

Before the full test:

1. Run one user and validate correctness.
2. Run a short low-rate calibration.
3. Compare configured and achieved rates.
4. Confirm transaction proportions.
5. Confirm server receives expected traffic.
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

Differences require explanation.

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
- use peak windows, not only daily averages.

## Cost And Scope Trade-Offs

Balance:

- production representativeness;
- business risk;
- environment cost;
- generator/tool cost;
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
User/traffic types:
Transactions and hourly volume:
Scenario mix:
Open or closed model:
Think time/pacing:
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
- copying daily average instead of peak;
- ignoring background traffic;
- using equal scenario shares without evidence;
- confusing requests with business transactions;
- omitting think time;
- failing to define initial data/cache state;
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
- [ ] Think time, pacing and session behavior are defined.
- [ ] Ramp, steady, peak and recovery phases exist.
- [ ] Initial state and test data are reproducible.
- [ ] Environment differences are documented.
- [ ] Client, server and business metrics are included.
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

