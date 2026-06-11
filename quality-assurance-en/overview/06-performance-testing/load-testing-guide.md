# Load Testing For QA

Source: user-provided Guru99 article, corrected and expanded with current performance-testing practice  
Date added: 2026-06-11  
Related plan item: Performance Testing  
Tags: QA, performance testing, load testing, throughput, latency, percentiles, workload model  
Language: English  
Translation pair: quality-assurance/overview/06-performance-testing/load-testing-guide.md

## Summary

Load testing evaluates a system under expected and peak business load.

Primary questions:

- Does the system deliver the required throughput?
- Does latency meet the SLO?
- Does the error rate remain acceptable?
- Which resources approach saturation?
- Is behavior stable throughout steady state?
- How does the system scale as load increases?

A load test is more than launching many virtual users. It requires a production-informed workload model, realistic data, observability, and predefined pass/fail criteria.

## Key Points

- Concurrent users, requests per second, and transactions per second are different metrics.
- Average response time hides the slow tail; analyze `p50`, `p90`, `p95`, and `p99`.
- Load testing normally covers expected and peak load, while stress testing exceeds target capacity.
- Throughput without acceptable latency and error rate does not demonstrate success.
- Correlate client results with server, database, cache, queue, and network metrics.
- The load generator can become the bottleneck.
- The environment should be sufficiently production-like, with differences documented.
- Scenarios should model business mix, think time, arrival rate, and realistic data.
- A single run without a baseline and repeatability provides weak evidence.

## Notes

## What Is Load Testing?

Load testing is non-functional testing in which a system runs under a defined workload profile.

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

A useful target connects:

- load;
- duration;
- user or business scenario;
- latency;
- errors;
- throughput;
- resource limits;
- correctness.

## Why Run A Load Test?

- verify release capacity;
- confirm an SLA or SLO;
- find bottlenecks before production;
- validate autoscaling;
- estimate infrastructure sizing;
- compare versions;
- test database and cache behavior;
- evaluate a campaign or seasonal peak;
- verify recovery after load decreases.

Load testing reduces risk but cannot guarantee that production incidents will not occur because real traffic, dependencies, and data distribution can differ.

## Workload Terminology

### Virtual Users

A virtual user runs a scripted sequence and often includes think time.

One hundred virtual users does not mean 100 RPS. RPS depends on:

- scenario duration;
- response time;
- think time;
- pacing;
- iteration logic.

### Concurrency

The number of simultaneously active or in-flight operations or sessions. Define the term explicitly.

### Throughput

Completed work per unit of time:

- requests per second;
- transactions per second;
- messages per second;
- orders per minute;
- bytes per second.

### Arrival Rate

The rate of new iterations, requests, or users.

An open workload often controls arrival rate independently of response time. A closed workload uses a fixed user count that starts another iteration after completing the previous one.

## Open And Closed Models

| Model | Load control | Typical use |
| --- | --- | --- |
| Closed | Fixed virtual users | User sessions with think time |
| Open | Fixed arrival or request rate | External traffic arriving independently |

At saturation, a closed model can reduce offered load because users wait longer for responses and start fewer iterations. This contributes to coordinated omission risk in some measurements.

Choose the model based on production behavior rather than tool convenience.

## Core Metrics

### Latency And Response Time

Record:

- `p50`, the median;
- `p90`;
- `p95`;
- `p99`;
- maximum, with caution;
- timeout count.

Example:

```text
p50 = 180 ms
p95 = 620 ms
p99 = 1400 ms
```

The average can look healthy while a meaningful portion of users receives slow responses.

### Throughput

Distinguish:

- offered load;
- accepted load;
- completed throughput;
- successful business transactions.

Five hundred generated requests per second and 500 successful orders per second are not the same result.

### Error Rate

Include:

- HTTP 4xx and 5xx;
- timeouts;
- connection errors;
- failed assertions;
- business errors;
- invalid or duplicate data;
- dropped messages.

Expected negative responses are not always system failures, while HTTP `200` does not always mean business success.

### Saturation

Observe:

- CPU;
- memory and garbage collection;
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

- **warm-up:** initialize caches, JIT, and pools;
- **ramp-up:** increase load without an unrealistic instant shock;
- **steady state:** collect stable measurements;
- **peak:** validate an expected short peak;
- **ramp-down:** verify recovery and pending work.

Do not combine every purpose into one test. Baseline, load, stress, spike, and soak tests answer different questions.

## Scenario Design

Create a weighted business mix:

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
- file upload or download where relevant;
- third-party dependency behavior;
- valid correlation and dynamic tokens.

Do not run only one convenient endpoint when production traffic contains several resources competing for capacity.

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
- the cache always uses one key;
- the test exhausts inventory;
- a unique constraint creates artificial errors.

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

If the environment has half the production node count, do not automatically claim exactly half the capacity. Scaling is rarely perfectly linear.

## Load Generator Validation

Monitor generators:

- CPU;
- memory;
- network;
- open sockets;
- dropped iterations;
- internal errors;
- clock synchronization.

Use several generators when one cannot sustain the desired load. Validate the generated rate against server-side received traffic.

## Execution Process

1. Define the business goal and SLO.
2. Collect production traffic and usage data.
3. Select a workload model.
4. Prepare the environment and data.
5. Create and validate scripts with one user.
6. Run a low-load baseline.
7. Run a short calibration.
8. Execute the target profile.
9. Monitor every system layer.
10. Verify business correctness.
11. Analyze bottlenecks.
12. Repeat after changes.

Change one important variable at a time when comparing results.

## Load Vs Stress Vs Spike Vs Soak

| Type | Main question |
| --- | --- |
| Load | Does the system meet requirements under expected or peak workload? |
| Stress | Where does it fail, and how does it degrade and recover? |
| Spike | Does it handle sudden rapid load changes? |
| Soak/endurance | Does it remain stable for a long duration? |
| Scalability | How does capacity change with resources? |
| Capacity | Which sustainable load still meets the SLO? |

A load test can expose a capacity limit, but finding the breaking point is primarily a stress or capacity objective.

## Functional Correctness Under Load

Performance tests should also assert:

- no duplicate orders;
- no lost writes;
- balances remain correct;
- inventory does not become negative;
- messages are processed according to the delivery contract;
- response data belongs to the correct user;
- retries are idempotent;
- final database state reconciles with requests.

A fast system producing incorrect data fails.

## Common Bottlenecks

| Symptom | Possible causes |
| --- | --- |
| Latency rises and CPU saturates | CPU-bound code, serialization, compression |
| Latency rises while CPU is low | Lock, pool, downstream wait, I/O |
| Errors rise at fixed concurrency | Connection or thread-pool exhaustion |
| Database time dominates | Missing index, poor plan, lock contention, N+1 |
| Memory grows over time | Leak, unbounded cache, backlog |
| Queue depth grows | Consumers are slower than producers |
| Throughput plateaus after adding users | Saturated resource or serialized section |
| Generator CPU reaches its limit | Test tool is the bottleneck |

Correlation is not proof. Use traces, profiles, logs, and controlled experiments to confirm root cause.

## Common Test Mistakes

- no pass/fail criteria;
- reporting only the average;
- confusing users with RPS;
- no warm-up;
- too-short steady state;
- unrealistic data;
- debug logging enabled;
- generator saturation;
- no server monitoring;
- testing from an unstable workstation network;
- comparing different environments;
- ignoring errors while celebrating throughput;
- changing several configurations between runs;
- using production without safeguards.

Old advice to disable all images or detailed logging is context-dependent. Exclude a resource only when it is outside the scope, and retain enough observability to diagnose the run.

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
- baseline comparison;
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
- [ ] Open or closed model is chosen intentionally.
- [ ] Scenario weights are documented.
- [ ] Test data has sufficient cardinality.
- [ ] Environment differences are recorded.
- [ ] Generator capacity is validated.
- [ ] Warm-up, ramp, and steady state exist.
- [ ] Percentiles, throughput, and errors are collected.
- [ ] Server, database, and queue metrics are available.
- [ ] Business correctness is verified.
- [ ] The test is repeatable and compared with a baseline.
- [ ] The report contains limitations and a decision.

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

