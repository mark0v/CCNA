# Configuration Testing For QA

Source: user-provided Guru99 article, modernized for current software and performance testing  
Date added: 2026-06-11  
Related plan item: Performance Testing  
Tags: QA, configuration testing, compatibility, performance testing, test matrix, pairwise  
Language: English  
Translation pair: quality-assurance/overview/06-performance-testing/configuration-testing-guide.md

## Summary

Configuration testing evaluates a system across combinations of software, hardware, infrastructure, and runtime settings.

It answers two related questions:

1. **Compatibility:** does the product work on supported configurations?
2. **Performance/configuration:** how do resources or settings affect latency, throughput, stability, and cost?

Example dimensions:

- OS and architecture;
- browser, runtime, and database versions;
- CPU, memory, and storage;
- node and replica count;
- connection and thread pools;
- cache size;
- load balancer and network;
- locale, timezone, and feature flags;
- peripheral devices.

Testing the full Cartesian product is normally impossible, so the matrix is selected using risk, usage data, boundaries, and interactions.

## Key Points

- Configuration testing is not limited to hardware.
- The supported matrix should be explicit and versioned.
- Change one factor in a controlled experiment when measuring performance impact.
- Risk-based and pairwise combinations help cover compatibility regression.
- Virtual machines and containers accelerate software coverage but do not always model physical hardware accurately.
- Configuration drift makes results irreproducible.
- Defaults, invalid values, missing dependencies, and upgrades need separate tests.
- Faster is not always better; consider correctness, stability, and cost.
- Secrets and production values must not appear in test artifacts.

## Notes

## What Counts As Configuration?

### Software

- operating system;
- browser;
- JVM, .NET, Node.js, or Python runtime;
- database and driver;
- web or application server;
- library and dependency versions;
- firmware;
- feature flags;
- locale and timezone.

### Hardware And Infrastructure

- CPU count and architecture;
- RAM;
- disk type, size, and IOPS;
- network latency and bandwidth;
- node count;
- load balancer;
- GPU;
- printers, scanners, cameras, and specialized peripherals.

### Runtime Settings

- heap size;
- thread or worker count;
- database connection pool;
- timeout;
- retry;
- cache size and TTL;
- batch size;
- queue limits;
- compression;
- autoscaling thresholds;
- logging level.

## Configuration Testing Versus Compatibility Testing

Compatibility testing normally covers supported external environments:

- OS;
- browser;
- device;
- database version;
- peripheral.

Configuration testing is broader and includes internal settings and resource combinations.

One test can belong to both. Running a service with PostgreSQL 16 is compatibility coverage, while comparing pool sizes of 20, 50, and 100 is a performance configuration experiment.

## Configuration Testing Versus Performance Tuning

A configuration test measures behavior under a documented setup.

Performance tuning changes the setup or code to improve a result.

Safe loop:

1. establish a baseline;
2. state a hypothesis;
3. change one factor;
4. run the same workload;
5. compare;
6. check side effects;
7. repeat to confirm.

Changing memory, pool size, and node count together makes the cause of the result uncertain.

## Building A Configuration Matrix

Example dimensions:

| Factor | Values |
| --- | --- |
| OS | Ubuntu LTS, RHEL, Windows Server |
| Runtime | Java 17, Java 21 |
| Database | PostgreSQL 15, 16 |
| CPU | 2, 4, 8 cores |
| RAM | 4, 8, 16 GB |
| Region | local, cross-region |

Full combinations:

```text
3 * 2 * 2 * 3 * 3 * 2 = 216
```

You do not necessarily need 216 suites.

Prioritize:

- most-used configurations;
- minimum and maximum supported;
- newly added versions;
- previous defect combinations;
- risky interactions;
- upgrade paths;
- unsupported or invalid configurations;
- representative performance tiers.

## Pairwise And Combinatorial Coverage

Pairwise testing selects combinations so every pair of factor values appears at least once.

It reduces the matrix but does not guarantee detection of defects involving three or more factors.

Use pairwise when:

- the full matrix is too large;
- factors are relatively independent;
- critical combinations are added manually;
- the baseline and common configuration are always included.

Pairwise selection does not replace business risk analysis.

## Supported, Unsupported, And Unknown

Each configuration should have a status:

| Status | Expected behavior |
| --- | --- |
| Supported | Full quality and support commitment |
| Limited or conditional | Works with documented limitations |
| Unsupported | Installation or startup is blocked, or a clear error appears |
| Unknown | Not tested and no promise exists |

An unsupported configuration should not silently corrupt data. The product should fail clearly where practical.

## Functional Configuration Tests

For each selected combination, verify:

- installation and startup;
- upgrade;
- primary business flow;
- storage and network access;
- authentication;
- integrations;
- error handling;
- shutdown and restart;
- logs and diagnostics;
- cleanup or uninstall where relevant.

You do not need full functional regression on every combination. Use tiers:

- smoke on a broad matrix;
- critical regression on the supported matrix;
- full regression on primary configurations.

## Performance Configuration Experiments

Example hypothesis:

```text
Increasing the database connection pool from 20 to 50
will improve checkout throughput at 300 RPS without
raising database CPU above 75% or increasing lock waits.
```

Compare:

- latency percentiles;
- achieved throughput;
- errors;
- resource utilization;
- queue or pool saturation;
- cost;
- recovery;
- business correctness.

A larger pool can reduce performance by overloading the database or increasing contention.

## Common Performance Factors

### CPU And Workers

Test:

- too few workers;
- workers aligned with CPU guidance;
- excessive workers;
- CPU throttling;
- NUMA or architecture differences where relevant.

More threads can create context switching and lock contention.

### Memory And Heap

Test:

- minimum supported;
- typical;
- high memory;
- a container limit below runtime heap configuration;
- garbage collection;
- out-of-memory behavior.

A larger heap can reduce GC frequency but increase pause or recovery time.

### Connection Pools

Check:

- minimum and maximum size;
- acquisition timeout;
- idle timeout;
- leak detection;
- dependency capacity;
- behavior after reconnect.

Pool capacity must align with downstream limits.

### Cache

Check:

- enabled and disabled;
- cold and warm;
- size;
- TTL;
- eviction policy;
- invalidation;
- unavailable cache.

Report whether results use a cold or warm cache.

### Storage

Check:

- local and network storage;
- SSD, HDD, or storage class;
- IOPS and throughput;
- free-space threshold;
- file-system behavior;
- fsync and durability settings.

Do not weaken durability merely to improve benchmark numbers without explicit business approval.

### Network And Geography

Check:

- same-region and cross-region;
- latency;
- bandwidth;
- packet loss;
- proxy and load balancer;
- TLS;
- DNS;
- MTU where relevant.

## Negative Configuration Testing

Test:

- missing required variable;
- invalid type;
- out-of-range value;
- duplicate or conflicting setting;
- deprecated option;
- unknown option;
- inaccessible file or secret;
- malformed endpoint;
- wrong certificate;
- insufficient permission;
- partially updated configuration.

Expected behavior:

- validation before startup where possible;
- a useful error naming the setting;
- no secret value in logs;
- no partial destructive initialization;
- safe fallback only when documented.

## Defaults And Precedence

Configuration can come from:

- built-in defaults;
- configuration files;
- environment variables;
- command-line arguments;
- remote configuration;
- feature-flag service;
- deployment templates.

Test precedence:

```text
command line > environment > file > default
```

The actual order depends on the product and must be documented.

Verify:

- omitted value;
- explicit default;
- override;
- conflicting sources;
- reload or restart requirement;
- dynamic change;
- rollback.

## Feature Flags

Test:

- on and off;
- default state;
- targeted user or tenant;
- gradual rollout;
- stale cached flag;
- unavailable flag service;
- interaction between flags;
- rollback;
- old application version receiving a new flag.

A feature flag is production configuration and can create combinations as complex as code branches.

## Version And Upgrade Matrix

Cover:

- clean install on a supported version;
- application upgrade;
- OS, runtime, or database upgrade;
- rollback where supported;
- mixed-version rolling deployment;
- old client with new server;
- new client with old server;
- deprecated-configuration migration.

Compatibility during a rolling deployment can differ from final steady state.

## Virtualized Versus Physical Environments

VMs and containers provide:

- repeatability;
- snapshots;
- fast provisioning;
- automation;
- broad software matrix.

Physical hardware remains important for:

- peripherals;
- firmware and drivers;
- GPU;
- exact storage and network devices;
- hardware timing;
- mobile and embedded systems.

Record the virtualization layer, host contention, and resource limits.

## Configuration As Code

Prefer versioned definitions:

- Dockerfiles and images;
- Compose;
- Kubernetes manifests and Helm;
- Terraform;
- Ansible;
- VM images;
- checked-in templates.

For every test, record:

- commit or image digest;
- environment variables with secrets redacted;
- resource limits;
- feature flags;
- database schema;
- dependency versions.

This reduces configuration drift and improves reproducibility.

## Observability And Diagnostics

Collect:

- application version;
- configuration hash;
- startup validation logs;
- resource limits;
- runtime flags;
- metrics;
- traces;
- dependency versions;
- autoscaling events.

Do not log:

- passwords;
- tokens;
- private keys;
- full connection strings containing credentials.

## Sample Test Matrix

| ID | OS | Runtime | DB | CPU/RAM | Purpose |
| --- | --- | --- | --- | --- | --- |
| C1 | Ubuntu LTS | Java 21 | PostgreSQL 16 | 4/8 GB | Primary baseline |
| C2 | Ubuntu LTS | Java 17 | PostgreSQL 16 | 4/8 GB | Minimum runtime |
| C3 | RHEL | Java 21 | PostgreSQL 16 | 4/8 GB | Enterprise OS |
| C4 | Ubuntu LTS | Java 21 | PostgreSQL 15 | 4/8 GB | Previous DB |
| C5 | Ubuntu LTS | Java 21 | PostgreSQL 16 | 2/4 GB | Minimum resources |
| C6 | Ubuntu LTS | Java 21 | PostgreSQL 16 | 8/16 GB | Scaling experiment |

Each row needs an expected support status and test-suite level.

## Example Test Cases

### Missing Dependency

**Given:** the required database driver is unavailable.  
**When:** the service starts.  
**Then:** startup fails with a clear non-secret error and no partial migration.

### Pool Size

**Given:** the same build, data, and 300 RPS workload.  
**When:** the pool changes from 20 to 50.  
**Then:** compare percentiles, throughput, database CPU, waits, and errors.

### Locale And Timezone

**Given:** `en-US/UTC` and `de-DE/Europe-Berlin`.  
**When:** a user creates a scheduled transaction.  
**Then:** the stored instant and displayed local time remain correct.

### Peripheral

**Given:** each supported scanner model and driver.  
**When:** scan, disconnect, reconnect, and send invalid input.  
**Then:** data is correct, errors are recoverable, and no process restart is needed.

## Common Defects

- a default differs between environments;
- an environment variable is silently ignored;
- an invalid value is accepted and fails later;
- a larger pool overloads the database;
- cache size causes out-of-memory failure;
- an old runtime serializes data differently;
- timezone changes scheduled execution;
- a rolling deployment breaks protocol compatibility;
- feature flags create an unsupported state;
- configuration reload applies to only some nodes;
- secrets appear in startup logs;
- a VM benchmark is limited by a noisy host.

## Reporting

Include:

- objective;
- selected matrix and rationale;
- supported or unsupported status;
- exact versions and configuration;
- workload and data;
- functional results;
- performance percentiles and throughput;
- resources and cost;
- failures and limitations;
- recommended configuration;
- evidence that the result is repeatable.

Avoid calling one configuration optimal without explaining workload, SLO, cost, and operational constraints.

## QA Checklist

- [ ] Supported configuration dimensions are documented.
- [ ] Primary, minimum, and boundary combinations are included.
- [ ] Pairwise coverage is supplemented with risk-based cases.
- [ ] Defaults and precedence are tested.
- [ ] Invalid and missing settings fail safely.
- [ ] Upgrades and mixed versions are covered.
- [ ] One factor changes per performance experiment.
- [ ] Build, image, and configuration hashes are recorded.
- [ ] Generator and environment capacity are monitored.
- [ ] Functional correctness accompanies performance metrics.
- [ ] Secrets are redacted.
- [ ] Recommended configuration includes cost and limitations.

## Interview Focus

1. What is configuration testing?
2. How does it differ from compatibility testing?
3. Why is exhaustive configuration coverage impractical?
4. What is pairwise testing?
5. Why change one factor at a time?
6. Which configurations should be prioritized?
7. How do defaults and precedence create defects?
8. Why can a larger connection pool reduce performance?
9. What should be recorded for reproducibility?

## Sources

- User-provided Guru99 article: "What is Configuration Testing? Example Test Cases"
- [NIST ACTS combinatorial testing](https://csrc.nist.gov/projects/automated-combinatorial-testing-for-software)
- [Apache JMeter best practices](https://jmeter.apache.org/usermanual/best-practices.html)
- [Grafana k6 test lifecycle](https://grafana.com/docs/k6/latest/using-k6/test-lifecycle/)

