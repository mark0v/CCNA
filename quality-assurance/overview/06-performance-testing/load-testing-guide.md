# Load Testing для QA

Source: user-provided Guru99 article, corrected and expanded with current performance-testing practice  
Date added: 2026-06-11  
Related plan item: Performance Testing  
Tags: QA, performance testing, load testing, throughput, latency, percentiles, workload model  
Language: Russian  
Translation pair: quality-assurance-en/overview/06-performance-testing/load-testing-guide.md

## Summary

Load testing проверяет поведение системы под ожидаемой и peak business load.

Основные вопросы:

- выполняет ли система required throughput;
- укладывается ли latency в SLO;
- остаётся ли error rate допустимым;
- какие resources приближаются к saturation;
- стабильно ли поведение на протяжении steady state;
- как система масштабируется при росте нагрузки.

Load test не сводится к одновременному запуску большого числа virtual users. Нужны production-informed workload model, realistic data, observability и заранее определённые pass/fail criteria.

## Key Points

- Concurrent users, requests per second и transactions per second — разные metrics.
- Average response time скрывает slow tail; анализируйте percentiles `p50`, `p90`, `p95`, `p99`.
- Load test обычно проверяет expected and peak load, а stress test выходит за пределы target capacity.
- Throughput без acceptable latency и error rate не доказывает успех.
- Client-side results необходимо сопоставлять с server, database, cache, queue и network metrics.
- Load generator сам может стать bottleneck.
- Test environment должен быть достаточно production-like, а различия — задокументированы.
- Сценарии должны моделировать business mix, think time, arrival rate и realistic data.
- Результат одного запуска без baseline и repeatability слаб.

## Notes

## Что такое Load Testing

Load testing — non-functional testing, при котором system работает под заданным workload profile.

Example target:

```text
At 300 requests/second for 30 minutes:
- checkout p95 < 800 ms;
- checkout p99 < 1500 ms;
- HTTP error rate < 0.5%;
- no data loss or duplicate orders;
- database CPU < 75%;
- queue lag returns to normal within 5 minutes.
```

Хорошая цель связывает:

- load;
- duration;
- user/business scenario;
- latency;
- errors;
- throughput;
- resource limits;
- correctness.

## Зачем проводить Load Test

- проверить release capacity;
- подтвердить SLA/SLO;
- найти bottleneck до production;
- проверить autoscaling;
- оценить infrastructure sizing;
- сравнить versions;
- проверить database and cache behavior;
- измерить влияние campaign или seasonal peak;
- подтвердить recovery после load reduction.

Load testing снижает риск, но не гарантирует отсутствие production incidents: real traffic, dependencies и data distribution могут отличаться.

## Workload Terminology

### Virtual Users

Virtual user выполняет scripted sequence и часто содержит think time.

100 virtual users не означает 100 RPS. RPS зависит от:

- scenario duration;
- response time;
- think time;
- pacing;
- iteration logic.

### Concurrency

Количество одновременно active/in-flight operations или sessions. Определение должно быть явно указано.

### Throughput

Completed work per unit of time:

- requests per second;
- transactions per second;
- messages per second;
- orders per minute;
- bytes per second.

### Arrival Rate

Скорость появления новых iterations, requests или users.

Open workload часто задаёт arrival rate независимо от response time. Closed workload использует фиксированное число users, которые начинают новую iteration после завершения предыдущей.

## Open And Closed Models

| Model | Load control | Typical use |
| --- | --- | --- |
| Closed | Fixed virtual users | User sessions with think time |
| Open | Fixed arrival/request rate | External traffic arriving independently |

При saturation closed model может сам снижать offered load: users ждут медленный response и реже начинают новые iterations. Это называется coordinated omission risk in some measurements.

Выбирайте model по production behavior, а не по удобству tool.

## Core Metrics

### Latency And Response Time

Фиксируйте:

- `p50` — median;
- `p90`;
- `p95`;
- `p99`;
- maximum, cautiously;
- timeout count.

Example:

```text
p50 = 180 ms
p95 = 620 ms
p99 = 1400 ms
```

Среднее может выглядеть хорошим, даже если значительная часть пользователей видит slow responses.

### Throughput

Отличайте:

- offered load;
- accepted load;
- completed throughput;
- successful business transactions.

500 generated requests/s и 500 successful orders/s — не одно и то же.

### Error Rate

Учитывайте:

- HTTP 4xx/5xx;
- timeouts;
- connection errors;
- failed assertions;
- business errors;
- invalid or duplicate data;
- dropped messages.

Ожидаемые negative responses не всегда являются system failure, а HTTP `200` не всегда означает business success.

### Saturation

Наблюдайте:

- CPU;
- memory and GC;
- disk I/O;
- network;
- thread pools;
- connection pools;
- database connections and locks;
- cache hit ratio;
- queue depth and consumer lag;
- autoscaling state.

## Load Profile

Typical profile:

```text
5 min   warm-up
10 min  ramp from 0 to target load
30 min  steady state at target load
10 min  peak load
10 min  return to target load
5 min   ramp-down
```

Phases:

- **warm-up:** initialize caches, JIT and pools;
- **ramp-up:** increase load without unrealistic instant shock;
- **steady state:** collect stable measurements;
- **peak:** validate expected short peak;
- **ramp-down:** verify recovery and pending work.

Do not combine every goal into one test. Baseline, load, stress, spike and soak tests answer different questions.

## Scenario Design

Build a weighted business mix:

| Scenario | Share |
| --- | ---: |
| Browse catalog | 45% |
| Search | 25% |
| View product | 20% |
| Checkout | 8% |
| Account operations | 2% |

Include:

- authentication;
- realistic navigation;
- think time and pacing;
- cacheable and non-cacheable requests;
- reads and writes;
- file upload/download where relevant;
- third-party dependency behavior;
- valid correlation and dynamic tokens.

Avoid running only one convenient endpoint if production load contains several competing resources.

## Test Data

Prepare:

- unique accounts;
- reusable read-only records;
- inventory and balances;
- tokens and sessions;
- randomized search values;
- cleanup strategy;
- sufficient cardinality.

Poor data causes false bottlenecks:

- every VU logs in as one user;
- every request updates one row;
- cache always hits one key;
- test exhausts inventory;
- unique constraint creates artificial errors.

## Environment

Record:

- service versions and build;
- infrastructure sizes;
- node counts;
- autoscaling configuration;
- database size and indexes;
- cache state;
- network path;
- external dependency stubs or real services;
- monitoring configuration;
- differences from production.

If environment has half the production nodes, do not automatically claim exactly half the capacity. Scaling is rarely perfectly linear.

## Load Generator Validation

Monitor generators:

- CPU;
- memory;
- network;
- open sockets;
- dropped iterations;
- internal errors;
- clock synchronization.

Use multiple generators when one cannot sustain desired load. Validate generated rate with server-side received traffic.

## Execution Process

1. Define business goal and SLO.
2. Collect production traffic and usage data.
3. Select workload model.
4. Prepare environment and data.
5. Create and validate scripts with one user.
6. Run a baseline at low load.
7. Run a short calibration.
8. Execute target profile.
9. Monitor all system layers.
10. Validate business correctness.
11. Analyze bottlenecks.
12. Repeat after changes.

Change one important variable at a time when comparing results.

## Load Vs Stress Vs Spike Vs Soak

| Type | Main question |
| --- | --- |
| Load | Meets requirements under expected/peak workload? |
| Stress | Where does the system fail and how does it degrade/recover? |
| Spike | Handles sudden rapid changes in load? |
| Soak/endurance | Remains stable for a long duration? |
| Scalability | How does capacity change with resources? |
| Capacity | What sustainable load meets the SLO? |

A load test can reveal a capacity limit, but finding the breaking point is primarily a stress/capacity objective.

## Functional Correctness Under Load

Performance test must also assert:

- no duplicate orders;
- no lost writes;
- balances remain correct;
- inventory does not become negative;
- messages are processed once according to contract;
- response data belongs to correct user;
- retry is idempotent;
- final database state reconciles with requests.

A fast system producing wrong data fails.

## Common Bottlenecks

| Symptom | Possible causes |
| --- | --- |
| Latency rises, CPU saturated | CPU-bound code, serialization, compression |
| Latency rises, CPU low | Lock, pool, downstream wait, I/O |
| Errors rise at fixed concurrency | Connection/thread pool exhaustion |
| Database time dominates | Missing index, bad plan, lock contention, N+1 |
| Memory grows over time | Leak, unbounded cache, backlog |
| Queue depth grows | Consumers slower than producers |
| Throughput plateaus after adding users | Saturated resource or serialized section |
| Generator CPU reaches limit | Test tool is bottleneck |

Correlation is not proof. Use traces, profiles, logs and experiments to confirm root cause.

## Common Test Mistakes

- no pass/fail criteria;
- reporting only average;
- confusing users with RPS;
- no warm-up;
- too-short steady state;
- unrealistic data;
- debug logging enabled;
- generator saturation;
- no server monitoring;
- testing from unstable workstation network;
- comparing different environments;
- ignoring errors while celebrating throughput;
- changing several configurations between runs;
- using production without safeguards.

The old advice to disable all images or detailed logging is context-dependent. Exclude a resource only if it is outside the test scope, and keep enough observability to diagnose the run.

## Results Report

Include:

- objective;
- build and environment;
- workload model and profile;
- scenario mix;
- test data;
- pass/fail thresholds;
- latency percentiles;
- throughput;
- errors by type;
- infrastructure metrics;
- bottleneck evidence;
- business correctness;
- comparison with baseline;
- limitations;
- recommendations.

Example conclusion:

```text
FAIL: At 300 RPS, checkout p95 reached 1.4 s against an 800 ms SLO.
Error rate remained 0.2%, but the database connection pool was saturated
for 18 minutes and queue lag reached 42,000 messages.
```

## Basic k6 Example

```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '2m', target: 50 },
    { duration: '10m', target: 50 },
    { duration: '2m', target: 0 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500', 'p(99)<1000'],
  },
};

export default function () {
  const response = http.get('https://test.example.com/api/catalog');

  check(response, {
    'status is 200': (r) => r.status === 200,
  });

  sleep(1);
}
```

This is a learning example, not a complete production workload.

## QA Checklist

- [ ] Business goal and SLO are defined.
- [ ] Production traffic informed the workload.
- [ ] Open/closed model is chosen intentionally.
- [ ] Scenario weights are documented.
- [ ] Test data has sufficient cardinality.
- [ ] Environment differences are recorded.
- [ ] Generator capacity is validated.
- [ ] Warm-up, ramp and steady state exist.
- [ ] Percentiles, throughput and errors are collected.
- [ ] Server, database and queue metrics are available.
- [ ] Business correctness is verified.
- [ ] Test is repeatable and compared with baseline.
- [ ] Report contains limitations and decision.

## Interview Focus

1. What is load testing?
2. How does load testing differ from stress testing?
3. Why are concurrent users and RPS different?
4. Why is average response time insufficient?
5. What are open and closed workload models?
6. Which client and server metrics should be collected?
7. How can a load generator distort results?
8. How do you validate correctness under load?
9. What should a performance report contain?

## Sources

- User-provided Guru99 article: "What is Load Testing? (Examples)"
- [Grafana k6: Test lifecycle](https://grafana.com/docs/k6/latest/using-k6/test-lifecycle/)
- [Grafana k6: Scenarios](https://grafana.com/docs/k6/latest/using-k6/scenarios/)
- [Grafana k6: Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/)
- [Apache JMeter best practices](https://jmeter.apache.org/usermanual/best-practices.html)

