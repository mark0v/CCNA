# Stability And Soak Testing For QA

Source: user-provided Guru99 article, corrected and expanded for endurance testing  
Date added: 2026-06-11  
Related plan item: Performance Testing  
Tags: QA, performance testing, stability testing, soak testing, endurance, memory leak  
Language: English  
Translation pair: quality-assurance/overview/06-performance-testing/stability-soak-testing-guide.md

## Summary

Stability testing, also known as soak or endurance testing, evaluates a system under sustained workload for a long period.

It targets problems that short load tests can miss:

- memory and resource leaks;
- growing queues and backlogs;
- connection, thread, and file-descriptor leaks;
- cache growth;
- log and disk accumulation;
- degradation after repeated operations;
- scheduled-job conflicts;
- token, certificate, and session expiration;
- failure to recover after a long run.

Time is the primary variable in a stability test. The workload is normally realistic and sustainable, not necessarily maximum.

## Key Points

- Stability or soak testing and stress testing answer different questions.
- Duration should cover relevant cycles such as hours, days, rotations, and scheduled jobs.
- Analyze trends and slopes rather than only start and end values.
- A stable average can hide worsening `p95` and `p99`.
- Memory growth is not always a leak; consider caches, garbage collection, and warm-up.
- Queue depth should return to baseline or remain bounded.
- Test data and storage can run out before an application defect appears.
- Clock synchronization, metric retention, and reliable generators are essential for a long run.
- After the test, verify recovery, data integrity, and cleanup.

## Notes

## What Is Stability Testing?

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

A stability test verifies that acceptable behavior can continue over time, not only through a momentary peak.

## Stability Versus Other Performance Tests

| Test | Main variable | Main question |
| --- | --- | --- |
| Load | Target workload | Does it meet the SLO under expected load? |
| Stress | Load or resource pressure beyond limits | How does it degrade and recover? |
| Spike | Rate of load change | Does it handle sudden bursts? |
| Stability/soak | Duration | Does behavior degrade over time? |
| Volume | Data volume | Does it handle large datasets? |

A long stress test is possible, but that does not make every stability test a stress test.

## When To Run A Soak Test

- the service runs continuously;
- a release changes memory or resource management;
- asynchronous processing is important;
- traffic includes long sessions;
- the system performs scheduled jobs;
- database or cache grows during operation;
- previous incidents appeared after hours or days;
- autoscaling repeatedly changes capacity;
- connections or tokens have long expiration periods.

## Choosing Duration

Duration should cover relevant operational cycles:

- several cache-expiration periods;
- token or session renewal;
- log rotation;
- backup;
- cron or batch jobs;
- queue retention;
- autoscaling scale-in;
- database maintenance;
- a daily timezone boundary;
- daylight-saving transition where relevant.

Common durations are 8, 12, 24, 48, or 72 hours. Select based on risks and cycles rather than tradition.

## Workload Profile

### Constant Load

Useful for finding slow drift.

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

Include:

- scheduled imports;
- report generation;
- cache refresh;
- backup;
- cleanup;
- message retry;
- index maintenance where relevant.

The load should remain below the known breaking point, or the test primarily measures overload.

## Baseline And Trend Analysis

Before the long run:

1. run a low-load baseline;
2. run a short target-load calibration;
3. warm up the system;
4. define a stable measurement window.

Compare:

- the first stable hour;
- the middle period;
- the final stable hour;
- post-test recovery.

Look for:

- positive slope;
- periodic spikes;
- step changes;
- saw-tooth pattern;
- failure after a scheduled event.

## Latency And Throughput

Track over time:

- `p50`, `p95`, and `p99`;
- throughput;
- errors by type;
- timeouts;
- dropped iterations;
- business transactions.

Warning example:

```text
Throughput remained 200 RPS, but checkout p95 increased
from 420 ms in hour 1 to 1.3 s in hour 20.
```

The whole-test average can hide such drift.

## Memory And Garbage Collection

Memory patterns:

- bounded saw-tooth: memory rises and falls after GC;
- cache warm-up: growth reaches a stable plateau;
- probable leak: the post-GC baseline keeps rising;
- backlog growth: memory follows queue depth;
- fragmentation or native leak: process RSS grows while managed heap remains stable.

Collect:

- process or container RSS;
- heap used and committed;
- garbage-collection frequency and pauses;
- allocation rate;
- off-heap or native memory;
- out-of-memory events and restarts.

Do not declare a leak from one rising graph. Correlate with GC, traffic, caches, and profile evidence.

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

Resource counts after each cycle should return to a bounded level.

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

When producers remain slightly faster than consumers, a queue can grow slowly and appear harmless in a short run.

A pass criterion can require:

```text
queue depth never exceeds 20,000
and returns below 1,000 within 15 minutes after peak.
```

## Disk, Logs, And Temporary Data

Long tests often reveal:

- unbounded logs;
- missing rotation;
- temporary-file leaks;
- database WAL or binlog growth;
- core or heap dumps;
- report exports;
- object-storage accumulation.

Monitor:

- free disk;
- inode or file count;
- log rate;
- retention;
- rotation and compression;
- cleanup jobs.

Debug logging can distort performance and exhaust disk, while removing all diagnostics makes analysis impossible. Use production-like logging plus targeted metrics.

## Database And Cache Stability

Database:

- query-latency trend;
- active and idle connections;
- locks and deadlocks;
- buffer or cache hit rate;
- table and index growth;
- replication lag;
- vacuum, compaction, or maintenance;
- slow-query accumulation.

Cache:

- memory;
- hit and miss ratio;
- eviction;
- hot keys;
- expiration storms;
- stale entries;
- reconnect behavior.

## Scheduled And Expiring Events

Include:

- access and refresh token expiration;
- session timeout;
- TLS certificate rollover in a dedicated test;
- daily or monthly reset;
- midnight and timezone transition;
- cron jobs;
- backup;
- log rotation;
- key rotation;
- cache expiration;
- autoscaling scale-in.

Long duration is valuable only if these events occur or are safely accelerated.

## Test Environment And Generators

Long tests fail when the test infrastructure is unstable.

Validate:

- generator CPU, memory, and network;
- generator disk for results;
- clock synchronization;
- monitoring retention;
- dashboard sampling;
- runner reconnect and restart policy;
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
- inventory and balance reset;
- test-user lifecycle;
- database partitioning;
- safe deletion after the test.

Data exhaustion can cause artificial errors late in the run.

## Recovery And Post-Test Checks

After steady load:

1. Ramp down.
2. Allow queues to drain.
3. Measure latency return.
4. Observe memory after GC or an idle period.
5. Check leaked connections, threads, and files.
6. Reconcile transactions.
7. Check delayed jobs and the DLQ.
8. Verify disk cleanup.
9. Confirm service health without a restart.

If a restart is needed, report operational recovery rather than natural recovery.

## Common Defects

- memory baseline rises every hour;
- connection pool gradually exhausts;
- one thread leaks per transaction;
- queue grows slowly and never catches up;
- log rotation fails after a file-size threshold;
- cache eviction causes periodic database overload;
- a scheduled report blocks user traffic;
- an expired token causes a retry loop;
- autoscaling scale-in drops long connections;
- database maintenance increases latency;
- temporary files fill the disk;
- metrics expire before the test ends.

## Execution Process

1. Define risk and duration.
2. Identify operational cycles.
3. Establish a baseline.
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

In a real soak test, use a production-informed scenario mix, distributed generators where needed, and external monitoring.

## Reporting

Include:

- duration and reason;
- load profile;
- business mix;
- build and environment;
- start and end data volume;
- latency trend;
- throughput and error trend;
- memory and GC trend;
- resource counts;
- queue and lag trend;
- disk and log growth;
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
- [ ] Memory and garbage collection are monitored.
- [ ] Connections, threads, files, and sockets are counted.
- [ ] Queues and oldest-message age are monitored.
- [ ] Disk, logs, and temporary data are monitored.
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

