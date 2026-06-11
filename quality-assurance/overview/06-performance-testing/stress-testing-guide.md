# Stress Testing для QA

Source: user-provided Guru99 article, corrected and expanded for modern performance testing  
Date added: 2026-06-11  
Related plan item: Performance Testing  
Tags: QA, performance testing, stress testing, resilience, recovery, graceful degradation  
Language: Russian  
Translation pair: quality-assurance-en/overview/06-performance-testing/stress-testing-guide.md

## Summary

Stress testing проверяет систему за пределами normal or expected capacity.

Цель — узнать:

- где начинается degradation;
- какой resource становится bottleneck;
- как система ограничивает нагрузку;
- остаются ли critical functions доступными;
- сохраняется ли data integrity;
- как система восстанавливается после снижения нагрузки или failure.

Stress test не обязан завершаться полным crash. Хорошо спроектированная система может отклонять часть requests, применять backpressure и сохранять critical operations.

## Key Points

- Load testing проверяет target workload, stress testing выходит за target limits.
- Breaking point должен определяться через measurable behavior, а не только crash.
- Graceful degradation лучше silent corruption или uncontrolled timeout.
- Recovery является частью stress test, а не отдельным необязательным наблюдением.
- Stop conditions защищают environment и данные.
- Нагрузку можно создавать не только users, но и ограничением CPU, memory, disk, network или dependencies.
- Stress и endurance testing не являются синонимами.
- После overload необходимо проверить queues, retries, duplicates и persisted data.

## Notes

## Что такое Stress Testing

Stress testing — performance and resilience testing under abnormal, extreme or constrained conditions.

Example goal:

```text
Increase checkout traffic from 200 to 1200 RPS.
Identify the highest sustainable rate where:
- p95 remains below 2 seconds;
- error rate remains below 2%;
- no duplicate payment or order occurs.

After reducing traffic to 200 RPS:
- p95 returns below 700 ms within 5 minutes;
- queue lag returns below 1,000 messages within 10 minutes;
- all accepted orders reconcile with database records.
```

Stress target должен включать:

- overload profile;
- expected degradation;
- safety boundary;
- recovery criteria;
- correctness checks.

## Stress Vs Load Vs Endurance

| Type | Purpose |
| --- | --- |
| Load | Validate expected and peak workload against SLO |
| Stress | Exceed normal capacity and study failure/degradation/recovery |
| Spike | Apply a sudden rapid load change |
| Endurance/soak | Hold workload for a long duration |
| Capacity | Find the highest sustainable workload meeting requirements |

Stress test может быть коротким или длительным. Endurance test определяется прежде всего duration, а не экстремальной нагрузкой.

## Что считать Breaking Point

Breaking point может означать:

- latency exceeds SLO;
- error rate exceeds threshold;
- throughput stops growing;
- queue backlog grows without recovery;
- resource reaches sustained saturation;
- autoscaling cannot catch up;
- data correctness fails;
- service becomes unavailable;
- recovery time exceeds requirement.

System crash — лишь один возможный предел и часто уже слишком поздняя точка.

## Graceful Degradation

При перегрузке система может:

- return `429 Too Many Requests`;
- reject non-critical work;
- serve cached or reduced data;
- disable expensive features;
- limit concurrency;
- apply queue/backpressure;
- trip a circuit breaker;
- prioritize critical traffic.

Проверяйте:

- error response is explicit and stable;
- `Retry-After` or retry policy is correct;
- user sees actionable message;
- accepted requests are not lost;
- rejected requests are not partially processed;
- critical paths remain available;
- degradation switches restore automatically or operationally.

## Stress Dimensions

### Traffic Stress

- increasing RPS;
- increasing virtual users;
- high write ratio;
- expensive query mix;
- large payloads;
- burst traffic.

### Resource Stress

- limited CPU;
- memory pressure;
- disk nearly full;
- I/O throttling;
- connection pool limit;
- file descriptor limit;
- thread exhaustion.

### Dependency Stress

- slow database;
- unavailable cache;
- delayed third-party API;
- message broker backlog;
- DNS failure;
- packet loss and latency;
- unavailable region or node.

### Data Stress

- very large tables;
- hot partition or tenant;
- oversized document;
- large result set;
- high-cardinality keys;
- simultaneous update of one record.

## Designing The Stress Profile

### Step Load

```text
5 min  100 RPS
5 min  200 RPS
5 min  400 RPS
5 min  600 RPS
5 min  800 RPS
10 min return to 100 RPS
```

Step load помогает связать degradation с конкретным level.

### Ramp Beyond Capacity

Постепенно увеличивайте load, пока predefined failure threshold не будет достигнут.

### Sudden Overload

Резко увеличьте arrival rate, чтобы проверить admission control, autoscaling и queue behavior.

### Resource Reduction

Сохраняйте traffic, одновременно уменьшая available capacity или отключая component.

Не смешивайте все fault types в одном первом запуске. Иначе root cause станет неясным.

## Safety And Stop Conditions

До запуска определите automatic or manual stop:

- error rate above a critical limit;
- data integrity assertion fails;
- disk free space below threshold;
- uncontrolled queue growth;
- database replication lag exceeds safe limit;
- environment affects other teams;
- generator loses control;
- security or personal data risk appears.

Дополнительно:

- use isolated or approved environment;
- back up necessary data;
- define rollback;
- confirm monitoring and access;
- notify environment owners;
- protect external paid services;
- cap cost and autoscaling.

Stress testing без safety boundary может превратиться в незапланированный outage.

## Metrics

### Client

- latency percentiles;
- achieved throughput;
- failed iterations;
- timeouts;
- connection errors;
- business assertions;
- dropped arrivals.

### Application

- request queue;
- active workers;
- thread/event-loop utilization;
- circuit-breaker state;
- retries;
- rate-limit responses;
- GC pauses;
- instance restarts.

### Database And Messaging

- connections;
- locks and deadlocks;
- query latency;
- replication lag;
- disk I/O;
- queue depth;
- consumer lag;
- redelivery and dead-letter messages.

### Infrastructure

- CPU;
- memory;
- network;
- disk;
- container throttling;
- autoscaling events;
- load-balancer health.

## Recovery Testing

После overload:

1. Верните traffic к baseline.
2. Не перезапускайте system сразу, если цель — natural recovery.
3. Измерьте latency normalization.
4. Проверьте queue drain.
5. Проверьте instance and dependency health.
6. Reconcile accepted business operations.
7. Проверьте retries, duplicates и delayed events.
8. Зафиксируйте recovery time objective.

Различайте:

- recovery without intervention;
- recovery after autoscaling;
- recovery after component restart;
- recovery after operator action.

## Data Integrity Under Stress

Проверьте:

- accepted request has exactly one result;
- rejected request has no hidden side effect;
- balances and inventory remain valid;
- transaction rollback is complete;
- events are not lost or duplicated beyond contract;
- idempotency keys work;
- order/status sequence remains valid;
- cache converges with source of truth;
- delayed tasks eventually complete or enter DLQ.

Пример reconciliation:

```text
successful client checkouts
= committed orders
= successful payment records
= emitted order-created events
```

Допустимые differences должны быть объяснены asynchronous contract.

## Common Failure Patterns

| Pattern | Symptom |
| --- | --- |
| Cascading failure | One slow dependency exhausts upstream pools |
| Retry storm | Errors trigger retries that multiply load |
| Thundering herd | Many clients retry or refresh simultaneously |
| Queue collapse | Backlog grows faster than consumers recover |
| Autoscaling lag | New instances start after SLO is already broken |
| Cache stampede | Expired hot key sends many requests to database |
| Load shedding failure | System accepts work it cannot complete |
| Recovery oscillation | Service repeatedly becomes healthy/unhealthy |

## Execution Process

1. Define hypothesis and business risk.
2. Establish baseline.
3. Document target and stop criteria.
4. Validate scripts and test data.
5. Confirm monitoring.
6. Increase stress in controlled steps.
7. Observe degradation and bottleneck.
8. Reduce load or restore resource.
9. Measure recovery.
10. Reconcile data and queues.
11. Repeat to confirm.
12. Report safe operating limit and recommendations.

## Tools

Traffic generation:

- k6;
- JMeter;
- Gatling;
- Locust;
- LoadRunner.

Fault/resource injection:

- container or orchestration resource limits;
- network emulation;
- dependency stubs/proxies;
- controlled node termination;
- chaos engineering platforms.

Tool choice зависит от protocol, scale, team skills, observability и safety controls.

## Basic k6 Stress Profile

```javascript
import http from 'k6/http';
import { check } from 'k6';

export const options = {
  stages: [
    { duration: '2m', target: 100 },
    { duration: '5m', target: 100 },
    { duration: '2m', target: 300 },
    { duration: '5m', target: 300 },
    { duration: '2m', target: 600 },
    { duration: '5m', target: 600 },
    { duration: '5m', target: 50 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.05'],
    http_req_duration: ['p(95)<2000'],
  },
};

export default function () {
  const response = http.get('https://test.example.com/api/catalog');
  check(response, {
    'expected status': (r) => r.status === 200 || r.status === 429,
  });
}
```

Этот пример показывает profile, но production test также требует realistic scenario mix, data и recovery assertions.

## Reporting

Report should include:

- hypothesis;
- environment and build;
- stress dimensions;
- load profile;
- stop criteria;
- baseline;
- degradation point;
- breaking point definition;
- graceful-degradation behavior;
- bottleneck evidence;
- recovery timeline;
- data reconciliation;
- operational intervention;
- recommended safe limit.

Example:

```text
At 720 RPS, the database pool reached 100% utilization and checkout p95
exceeded 2 seconds. At 810 RPS, 429 responses began as designed.
No duplicate orders were found. After returning to 200 RPS, latency
recovered in 4 minutes, while the queue required 11 minutes to drain.
```

## QA Checklist

- [ ] Hypothesis and target risk are defined.
- [ ] Baseline is recorded.
- [ ] Breaking point has measurable criteria.
- [ ] Safety and stop conditions are approved.
- [ ] Stress is increased in controlled stages.
- [ ] Client and server metrics are synchronized.
- [ ] Graceful degradation is verified.
- [ ] Retry and backpressure behavior are covered.
- [ ] Data integrity is reconciled.
- [ ] Recovery is measured.
- [ ] Test generator is not saturated.
- [ ] Result is repeatable.
- [ ] Safe operating limit is documented.

## Interview Focus

1. How does stress testing differ from load testing?
2. Is a crash required for a successful stress test?
3. What is graceful degradation?
4. How do you define a breaking point?
5. Which stop conditions would you use?
6. What is a retry storm?
7. How do you test recovery?
8. How do you verify data integrity after overload?
9. Why are stress and endurance tests different?

## Sources

- User-provided Guru99 article: "What is STRESS Testing in Software Testing?"
- [Grafana k6 scenarios](https://grafana.com/docs/k6/latest/using-k6/scenarios/)
- [Grafana k6 thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/)
- [Apache JMeter best practices](https://jmeter.apache.org/usermanual/best-practices.html)

