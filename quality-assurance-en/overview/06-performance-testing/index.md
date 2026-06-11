# 06 - Performance Testing

Language: English  
Translation pair: quality-assurance/overview/06-performance-testing/index.md

## Section Goal

This section covers the performance-testing knowledge required for QA:

- load, stress, spike, soak, and scalability testing;
- latency, response time, throughput, error rate, and saturation;
- open and closed workload models;
- realistic scenarios and test data;
- environment and observability;
- bottleneck analysis;
- performance reporting and release decisions.

## Learning Path

1. Define measurable service-level objectives.
2. Build a production-informed workload model.
3. Create deterministic scripts and test data.
4. Establish a low-load baseline.
5. Run load, stress, spike, and endurance tests.
6. Correlate client results with application, database, and infrastructure metrics.
7. report percentiles, throughput, errors, saturation, and conclusions.

## QA Focus

A performance test is not simply "many requests." It needs:

- a documented purpose;
- a representative workload;
- controlled environment and data;
- measurable pass/fail criteria;
- server-side monitoring;
- repeatable execution;
- comparison with a baseline.

One number cannot describe performance. A successful report combines latency distribution, throughput, errors, resource saturation, and business outcomes.

