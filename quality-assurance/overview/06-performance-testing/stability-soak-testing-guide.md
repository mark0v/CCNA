# Stability и Soak Testing для QA

Source: user-provided Guru99 article, corrected and expanded for endurance testing  
Date added: 2026-06-11  
Related plan item: Performance Testing  
Tags: QA, performance testing, stability testing, soak testing, endurance, memory leak  
Language: Russian  
Translation pair: quality-assurance-en/overview/06-performance-testing/stability-soak-testing-guide.md

## Summary

Stability testing, также называемое soak или endurance testing, проверяет систему под sustained workload в течение длительного времени.

Цель — найти проблемы, которые не видны в коротком load test:

- memory and resource leaks;
- рост queues и backlog;
- connection/thread/file descriptor leaks;
- cache growth;
- log and disk accumulation;
- degradation after repeated operations;
- scheduled-job conflicts;
- token, certificate и session expiry;
- failure to recover after a long run.

Главная переменная stability test — время. Нагрузка обычно realistic and sustainable, а не обязательно максимальная.

## Key Points

- Stability/soak и stress testing отвечают на разные вопросы.
- Test duration должна быть достаточной для relevant cycles: hours, days, rotation или scheduled jobs.
- Смотрите на trends and slopes, а не только начало и конец.
- Stable average может скрывать ухудшение `p95`/`p99`.
- Memory growth не всегда leak: учитывайте cache, GC и warm-up.
- Queue depth должна возвращаться к baseline или оставаться bounded.
- Test data и storage могут закончиться раньше, чем проявится application issue.
- Clock synchronization, metric retention и reliable generators обязательны для длинного прогона.
- После теста проверяйте recovery, data integrity и cleanup.

## Notes

## Что такое Stability Testing

Example objective:

```text
Run the production-like business mix at 65% of expected peak load
for 24 hours.

Pass criteria:
- checkout p95 < 800 ms and p99 < 1500 ms;
- error rate < 0.5%;
- no unbounded memory, connection or queue growth;
- no instance restart caused by resource exhaustion;
- disk free space remains above 25%;
- all accepted orders reconcile after queue drain.
```

Stability test проверяет, может ли system сохранять acceptable behavior длительно, а не только пройти моментальный peak.

## Stability Vs Other Performance Tests

| Test | Main variable | Main question |
| --- | --- | --- |
| Load | Target workload | Meets SLO under expected load? |
| Stress | Load/resource pressure beyond limits | How does it degrade and recover? |
| Spike | Rate of load change | Handles sudden bursts? |
| Stability/soak | Duration | Does behavior degrade over time? |
| Volume | Data volume | Handles large datasets? |

Long stress test возможен, но это не делает все stability tests stress tests.

## Когда нужен Soak Test

- service работает continuously;
- release changes memory/resource management;
- asynchronous processing is important;
- traffic has long sessions;
- system performs scheduled jobs;
- database/cache grows during operation;
- previous incidents appeared after hours or days;
- autoscaling repeatedly changes capacity;
- connections or tokens have long expiration periods.

## Choosing Duration

Duration должна покрывать relevant operational cycles:

- several cache expiration periods;
- token/session renewal;
- log rotation;
- backup;
- cron or batch jobs;
- queue retention;
- autoscaling scale-in;
- database maintenance;
- daily timezone boundary;
- daylight-saving transition, if relevant.

Common durations: 8, 12, 24, 48 or 72 hours. Выбор должен исходить из risk and cycles, а не традиции.

## Workload Profile

### Constant Load

Подходит для выявления slow drift.

```text
30 min warm-up
24 h at 200 RPS
30 min ramp-down
```

### Realistic Daily Cycle

```text
6 h low load
10 h normal load
4 h peak load
4 h low load
repeat
```

### Mixed Background Work

Добавьте:

- scheduled imports;
- report generation;
- cache refresh;
- backup;
- cleanup;
- message retry;
- index maintenance where relevant.

Нагрузка должна быть ниже known breaking point, иначе test прежде всего измеряет overload.

## Baseline And Trend Analysis

Перед long run выполните:

1. low-load baseline;
2. short target-load calibration;
3. warm-up;
4. stable measurement window.

Сравнивайте:

- first stable hour;
- middle period;
- last stable hour;
- post-test recovery.

Ищите:

- positive slope;
- periodic spikes;
- step changes;
- saw-tooth pattern;
- failure after scheduled event.

## Latency And Throughput

Track over time:

- `p50`, `p95`, `p99`;
- throughput;
- errors by type;
- timeouts;
- dropped iterations;
- business transactions.

Example warning:

```text
Throughput remained 200 RPS, but checkout p95 increased
from 420 ms in hour 1 to 1.3 s in hour 20.
```

Total test average может скрыть такой drift.

## Memory And Garbage Collection

Memory patterns:

- bounded saw-tooth: memory rises and falls after GC;
- cache warm-up: growth reaches stable plateau;
- probable leak: post-GC baseline keeps rising;
- backlog growth: memory follows queue depth;
- fragmentation or native leak: process RSS grows while managed heap appears stable.

Collect:

- process/container RSS;
- heap used/committed;
- GC frequency and pause;
- allocation rate;
- off-heap/native memory;
- OOM/restarts.

Не объявляйте leak только по одному rising graph. Correlate with GC, traffic, cache and object/profile evidence.

## Resource Leaks

Monitor:

- database connections;
- HTTP client connections;
- threads;
- file descriptors;
- sockets;
- temporary files;
- worker slots;
- locks;
- sessions;
- browser handles where applicable.

Test repeated operation:

```text
open -> use -> close
```

Количество resources после each cycle должно возвращаться к bounded level.

## Queues And Asynchronous Work

Check:

- queue depth;
- oldest-message age;
- consumer lag;
- processing throughput;
- retries;
- dead-letter queue;
- redelivery;
- delayed scheduled messages.

Если producers устойчиво быстрее consumers, queue может расти медленно и выглядеть harmless в short run.

Pass criteria может требовать:

```text
queue depth never exceeds 20,000
and returns below 1,000 within 15 minutes after peak.
```

## Disk, Logs And Temporary Data

Long tests often reveal:

- unbounded logs;
- missing rotation;
- temporary file leak;
- database WAL/binlog growth;
- core/heap dumps;
- report exports;
- object storage accumulation.

Monitor:

- free disk;
- inode/file count;
- log rate;
- retention;
- rotation/compression;
- cleanup jobs.

Debug logging can distort performance and exhaust disk, but removing all diagnostic data makes the test impossible to analyze. Use production-like logging plus targeted metrics.

## Database And Cache Stability

Database:

- query latency trend;
- active/idle connections;
- locks and deadlocks;
- buffer/cache hit rate;
- table/index growth;
- replication lag;
- vacuum/compaction/maintenance;
- slow-query accumulation.

Cache:

- memory;
- hit/miss ratio;
- eviction;
- hot keys;
- expiration storms;
- stale entries;
- reconnect behavior.

## Scheduled And Expiring Events

Include:

- access/refresh token expiration;
- session timeout;
- TLS certificate rollover in dedicated tests;
- daily/monthly reset;
- midnight/timezone transition;
- cron jobs;
- backup;
- log rotation;
- key rotation;
- cache expiry;
- autoscaling scale-in.

Long duration is valuable only if these events actually occur or are accelerated safely.

## Test Environment And Generators

Long tests fail when test infrastructure is unstable.

Validate:

- generator CPU/memory/network;
- generator disk for results;
- clock synchronization;
- monitoring retention;
- dashboard sampling;
- test runner reconnect/restart policy;
- credentials that will not expire unexpectedly;
- sufficient test data;
- cost limits.

Do not treat generator failure as application failure.

## Data Management

Calculate expected growth:

```text
200 writes/s * 86,400 s = 17,280,000 writes/day
```

Prepare:

- storage capacity;
- unique keys;
- cleanup;
- inventory/balance reset;
- test-user lifecycle;
- database partitioning;
- safe deletion after test.

Data exhaustion can create artificial errors late in the run.

## Recovery And Post-Test Checks

After steady load:

1. Ramp down.
2. Allow queues to drain.
3. Measure latency return.
4. Observe memory after GC/idle period.
5. Check leaked connections, threads and files.
6. Reconcile transactions.
7. Check delayed jobs and DLQ.
8. Verify disk cleanup.
9. Confirm service health without restart.

If restart is needed, report it as operational recovery, not natural recovery.

## Common Defects

- memory baseline rises every hour;
- connection pool gradually exhausts;
- one thread leaks per transaction;
- queue grows slowly and never catches up;
- log rotation fails after file-size threshold;
- cache eviction causes periodic database overload;
- scheduled report blocks user traffic;
- expired token causes retry loop;
- autoscaling scale-in drops long connections;
- database maintenance causes increasing latency;
- temporary files fill disk;
- metrics disappear before long test ends.

## Execution Process

1. Define risk and duration.
2. Identify operational cycles.
3. Establish baseline.
4. Prepare realistic sustained workload.
5. Define trend and absolute thresholds.
6. Validate generators and monitoring.
7. Warm up.
8. Run steady workload.
9. Observe trends and scheduled events.
10. Ramp down and measure recovery.
11. Reconcile data and resources.
12. Repeat after fixes.

## Basic k6 Soak Profile

```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '10m', target: 100 },
    { duration: '8h', target: 100 },
    { duration: '10m', target: 0 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.005'],
    http_req_duration: ['p(95)<800', 'p(99)<1500'],
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

В реальном soak test используйте production-informed scenario mix, distributed generators if needed и external monitoring.

## Reporting

Include:

- duration and reason;
- load profile;
- business mix;
- build/environment;
- start/end data volume;
- latency trend;
- throughput and error trend;
- memory/GC trend;
- resource counts;
- queue and lag trend;
- disk/log growth;
- scheduled events;
- recovery results;
- data reconciliation;
- restarts or operator actions.

Example:

```text
FAIL: During the 24-hour run, API throughput remained stable at 180 RPS,
but post-GC memory increased from 2.1 GB to 5.8 GB. The service restarted
from OOM at hour 21. Database and queue metrics remained stable.
```

## QA Checklist

- [ ] Duration covers relevant operational cycles.
- [ ] Workload is sustainable and production-informed.
- [ ] Warm-up and stable measurement windows are defined.
- [ ] Percentiles are tracked over time.
- [ ] Memory and GC are monitored.
- [ ] Connections, threads, files and sockets are counted.
- [ ] Queues and oldest-message age are monitored.
- [ ] Disk, logs and temporary data are monitored.
- [ ] Scheduled jobs and expiration are covered.
- [ ] Generators and metric retention are validated.
- [ ] Recovery and queue drain are measured.
- [ ] Final data is reconciled.

## Interview Focus

1. What is stability or soak testing?
2. How does it differ from stress testing?
3. How do you choose test duration?
4. How do you distinguish cache warm-up from a memory leak?
5. Which resource leaks should be monitored?
6. Why can a stable average hide degradation?
7. Which scheduled events belong in a soak test?
8. What should be checked after ramp-down?

## Sources

- User-provided Guru99 article: "Stability Testing in Software Testing"
- [Grafana k6 test lifecycle](https://grafana.com/docs/k6/latest/using-k6/test-lifecycle/)
- [Grafana k6 scenarios](https://grafana.com/docs/k6/latest/using-k6/scenarios/)
- [Apache JMeter best practices](https://jmeter.apache.org/usermanual/best-practices.html)

