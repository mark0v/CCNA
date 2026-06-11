# Stress Testing For QA

Source: user-provided Guru99 article, corrected and expanded for modern performance testing  
Date added: 2026-06-11  
Related plan item: Performance Testing  
Tags: QA, performance testing, stress testing, resilience, recovery, graceful degradation  
Language: English  
Translation pair: quality-assurance/overview/06-performance-testing/stress-testing-guide.md

## Summary

Stress testing evaluates a system beyond normal or expected capacity.

It asks:

- Where does degradation begin?
- Which resource becomes the bottleneck?
- How does the system limit incoming work?
- Do critical functions remain available?
- Is data integrity preserved?
- How does the system recover after load decreases or a failure ends?

A stress test does not need to end in a complete crash. A well-designed system can reject some requests, apply backpressure, and preserve critical operations.

## Key Points

- Load testing validates target workload; stress testing exceeds target limits.
- A breaking point should be measurable behavior, not only a crash.
- Graceful degradation is preferable to silent corruption or uncontrolled timeouts.
- Recovery is part of the stress test.
- Stop conditions protect the environment and data.
- Stress can come from traffic or constrained CPU, memory, disk, network, and dependencies.
- Stress and endurance testing are not synonyms.
- After overload, verify queues, retries, duplicates, and persisted data.

## Notes

## What Is Stress Testing?

Stress testing is performance and resilience testing under abnormal, extreme, or constrained conditions.

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

A stress target should include:

- overload profile;
- expected degradation;
- safety boundary;
- recovery criteria;
- correctness checks.

## Stress Vs Load Vs Endurance

| Type | Purpose |
| --- | --- |
| Load | Validate expected and peak workload against the SLO |
| Stress | Exceed normal capacity and study failure, degradation, and recovery |
| Spike | Apply a sudden rapid load change |
| Endurance/soak | Hold workload for a long duration |
| Capacity | Find the highest sustainable workload meeting requirements |

A stress test can be short or long. An endurance test is defined primarily by duration rather than extreme load.

## Defining A Breaking Point

A breaking point can mean:

- latency exceeds the SLO;
- error rate exceeds its threshold;
- throughput stops growing;
- queue backlog grows without recovery;
- a resource remains saturated;
- autoscaling cannot catch up;
- data correctness fails;
- the service becomes unavailable;
- recovery time exceeds the requirement.

A system crash is only one possible limit and often a point reached too late.

## Graceful Degradation

Under overload, a system can:

- return `429 Too Many Requests`;
- reject non-critical work;
- serve cached or reduced data;
- disable expensive features;
- limit concurrency;
- apply queues or backpressure;
- trip a circuit breaker;
- prioritize critical traffic.

Verify that:

- the error response is explicit and stable;
- `Retry-After` or retry policy is correct;
- the user sees an actionable message;
- accepted requests are not lost;
- rejected requests are not partially processed;
- critical paths remain available;
- degradation switches recover automatically or operationally.

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
- nearly full disk;
- I/O throttling;
- connection-pool limit;
- file-descriptor limit;
- thread exhaustion.

### Dependency Stress

- slow database;
- unavailable cache;
- delayed third-party API;
- message-broker backlog;
- DNS failure;
- packet loss and latency;
- unavailable region or node.

### Data Stress

- very large tables;
- hot partition or tenant;
- oversized document;
- large result set;
- high-cardinality keys;
- simultaneous updates to one record.

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

Step load helps correlate degradation with a particular load level.

### Ramp Beyond Capacity

Increase load gradually until a predefined failure threshold is reached.

### Sudden Overload

Increase arrival rate quickly to test admission control, autoscaling, and queue behavior.

### Resource Reduction

Keep traffic constant while reducing available capacity or disabling a component.

Do not combine every fault type in the first run because root cause will become unclear.

## Safety And Stop Conditions

Define an automatic or manual stop before execution:

- error rate exceeds a critical limit;
- a data-integrity assertion fails;
- free disk falls below a threshold;
- queue growth becomes uncontrolled;
- database replication lag exceeds a safe limit;
- the environment affects other teams;
- the generator loses control;
- a security or personal-data risk appears.

Also:

- use an isolated or approved environment;
- back up necessary data;
- define rollback;
- confirm monitoring and access;
- notify environment owners;
- protect paid external services;
- cap cost and autoscaling.

Stress testing without a safety boundary can become an unplanned outage.

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
- thread or event-loop utilization;
- circuit-breaker state;
- retries;
- rate-limit responses;
- garbage-collection pauses;
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

After overload:

1. Return traffic to baseline.
2. Do not restart the system immediately when natural recovery is the target.
3. Measure latency normalization.
4. Verify queue drain.
5. Verify instance and dependency health.
6. Reconcile accepted business operations.
7. Check retries, duplicates, and delayed events.
8. Record the recovery time objective.

Distinguish:

- recovery without intervention;
- recovery after autoscaling;
- recovery after component restart;
- recovery after operator action.

## Data Integrity Under Stress

Verify:

- every accepted request has exactly one result;
- a rejected request has no hidden side effect;
- balances and inventory remain valid;
- transaction rollback is complete;
- events are not lost or duplicated beyond the contract;
- idempotency keys work;
- order and status sequences remain valid;
- cache converges with the source of truth;
- delayed tasks complete or enter the DLQ.

Example reconciliation:

```text
successful client checkouts
= committed orders
= successful payment records
= emitted order-created events
```

Any permitted difference should be explained by the asynchronous contract.

## Common Failure Patterns

| Pattern | Symptom |
| --- | --- |
| Cascading failure | One slow dependency exhausts upstream pools |
| Retry storm | Errors trigger retries that multiply load |
| Thundering herd | Many clients retry or refresh simultaneously |
| Queue collapse | Backlog grows faster than consumers recover |
| Autoscaling lag | New instances start after the SLO is already broken |
| Cache stampede | An expired hot key sends many requests to the database |
| Load-shedding failure | The system accepts work it cannot complete |
| Recovery oscillation | Service repeatedly becomes healthy and unhealthy |

## Execution Process

1. Define the hypothesis and business risk.
2. Establish a baseline.
3. Document target and stop criteria.
4. Validate scripts and test data.
5. Confirm monitoring.
6. Increase stress in controlled steps.
7. Observe degradation and the bottleneck.
8. Reduce load or restore the resource.
9. Measure recovery.
10. Reconcile data and queues.
11. Repeat to confirm.
12. Report the safe operating limit and recommendations.

## Tools

Traffic generation:

- k6;
- JMeter;
- Gatling;
- Locust;
- LoadRunner.

Fault and resource injection:

- container or orchestration resource limits;
- network emulation;
- dependency stubs or proxies;
- controlled node termination;
- chaos engineering platforms.

Tool selection depends on protocols, scale, team skills, observability, and safety controls.

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

This example shows the profile, but a production test also needs a realistic scenario mix, data, and recovery assertions.

## Reporting

Include:

- hypothesis;
- environment and build;
- stress dimensions;
- load profile;
- stop criteria;
- baseline;
- degradation point;
- breaking-point definition;
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
- [ ] Stress increases in controlled stages.
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

