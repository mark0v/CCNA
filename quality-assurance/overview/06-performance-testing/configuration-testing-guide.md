# Configuration Testing для QA

Source: user-provided Guru99 article, modernized for current software and performance testing  
Date added: 2026-06-11  
Related plan item: Performance Testing  
Tags: QA, configuration testing, compatibility, performance testing, test matrix, pairwise  
Language: Russian  
Translation pair: quality-assurance-en/overview/06-performance-testing/configuration-testing-guide.md

## Summary

Configuration testing проверяет систему при разных combinations of software, hardware, infrastructure и runtime settings.

Оно отвечает на два связанных вопроса:

1. **Compatibility:** работает ли product на supported configurations?
2. **Performance/configuration:** как изменение resources или settings влияет на latency, throughput, stability и cost?

Примеры dimensions:

- OS and architecture;
- browser/runtime/database versions;
- CPU, memory and storage;
- node and replica count;
- connection/thread pool;
- cache size;
- load balancer and network;
- locale, timezone and feature flags;
- peripheral devices.

Проверить полный Cartesian product обычно невозможно, поэтому matrix строится по риску, usage data, boundaries и interactions.

## Key Points

- Configuration testing не ограничивается hardware.
- Supported matrix должна быть явной и versioned.
- Меняйте один factor за controlled experiment, если исследуете performance impact.
- Для compatibility regression полезны risk-based и pairwise combinations.
- Virtual machines and containers ускоряют software coverage, но не всегда точно моделируют physical hardware.
- Configuration drift делает результаты невоспроизводимыми.
- Defaults, invalid values, missing dependencies и upgrades требуют отдельных tests.
- «Быстрее» не всегда означает «лучше»: учитывайте correctness, stability и cost.
- Configuration secrets и production values не должны попадать в test artifacts.

## Notes

## Что считается Configuration

### Software

- operating system;
- browser;
- JVM, .NET, Node.js or Python runtime;
- database and driver;
- web/application server;
- library and dependency versions;
- firmware;
- feature flags;
- locale and timezone.

### Hardware And Infrastructure

- CPU count and architecture;
- RAM;
- disk type, size and IOPS;
- network latency and bandwidth;
- node count;
- load balancer;
- GPU;
- printers, scanners, cameras and specialized peripherals.

### Runtime Settings

- heap size;
- thread/worker count;
- database connection pool;
- timeout;
- retry;
- cache size and TTL;
- batch size;
- queue limits;
- compression;
- autoscaling thresholds;
- logging level.

## Configuration Testing Vs Compatibility Testing

Compatibility testing обычно проверяет supported external environments:

- OS;
- browser;
- device;
- database version;
- peripheral.

Configuration testing шире и включает internal settings and resource combinations.

Один test может относиться к обоим направлениям. Например, работа service с PostgreSQL 16 — compatibility, а сравнение pool size 20/50/100 — performance configuration experiment.

## Configuration Testing Vs Performance Tuning

Configuration test измеряет behavior under a documented setup.

Performance tuning изменяет setup or code для достижения better result.

Safe loop:

1. establish baseline;
2. state hypothesis;
3. change one factor;
4. run the same workload;
5. compare;
6. check side effects;
7. repeat to confirm.

Если одновременно изменить memory, pool size и node count, невозможно уверенно определить причину результата.

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

Не обязательно запускать 216 suites.

Prioritize:

- most-used configurations;
- minimum and maximum supported;
- newly added version;
- previous defect combinations;
- risky interactions;
- upgrade paths;
- unsupported/invalid configurations;
- representative performance tiers.

## Pairwise And Combinatorial Coverage

Pairwise testing выбирает combinations так, чтобы каждая pair of values встретилась хотя бы один раз.

Оно уменьшает matrix, но не гарантирует обнаружение defects, зависящих от three or more factors.

Use pairwise when:

- full matrix too large;
- factors relatively independent;
- critical combinations are added manually;
- baseline/common configuration always included.

Do not use pairwise as a substitute for business risk analysis.

## Supported, Unsupported And Unknown

Каждая configuration должна иметь status:

| Status | Expected behavior |
| --- | --- |
| Supported | Full quality and support commitment |
| Limited/conditional | Works with documented limitations |
| Unsupported | Installation/start is blocked or clear error shown |
| Unknown | Not tested; no promise |

Unsupported configuration не должна silently corrupt data. Product должен fail clearly where practical.

## Functional Configuration Tests

For each selected combination, verify:

- install and startup;
- upgrade;
- main business flow;
- storage and network access;
- authentication;
- integrations;
- error handling;
- shutdown/restart;
- logs and diagnostics;
- cleanup/uninstall where relevant.

Не обязательно запускать full functional regression на каждой combination. Use tiers:

- smoke on broad matrix;
- critical regression on supported matrix;
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
- queue/pool saturation;
- cost;
- recovery;
- business correctness.

Larger pool may worsen performance by overloading database or increasing contention.

## Common Performance Factors

### CPU And Workers

Test:

- too few workers;
- workers equal to CPU guidance;
- excessive workers;
- CPU throttling;
- NUMA or architecture differences where relevant.

More threads can create context switching and lock contention.

### Memory And Heap

Test:

- minimum supported;
- typical;
- high memory;
- container limit lower than runtime heap;
- garbage collection;
- OOM behavior.

More heap can reduce GC frequency but increase pause or recovery time.

### Connection Pools

Check:

- minimum/maximum size;
- acquisition timeout;
- idle timeout;
- leak detection;
- dependency capacity;
- behavior after reconnect.

Pool capacity must align with downstream limits.

### Cache

Check:

- enabled/disabled;
- cold/warm;
- size;
- TTL;
- eviction policy;
- invalidation;
- unavailable cache.

Report whether results use a cold or warm cache.

### Storage

Check:

- local/network storage;
- SSD/HDD or storage class;
- IOPS and throughput;
- free-space threshold;
- file-system behavior;
- fsync/durability settings.

Do not change durability merely to make benchmark numbers look better without explicit business approval.

### Network And Geography

Check:

- same-region and cross-region;
- latency;
- bandwidth;
- packet loss;
- proxy/load balancer;
- TLS;
- DNS;
- MTU where relevant.

## Negative Configuration Testing

Test:

- missing required variable;
- invalid type;
- out-of-range value;
- duplicate/conflicting setting;
- deprecated option;
- unknown option;
- inaccessible file/secret;
- malformed endpoint;
- wrong certificate;
- insufficient permission;
- partially updated configuration.

Expected behavior:

- validation before startup where possible;
- useful error naming the setting;
- no secret value in logs;
- no partial destructive initialization;
- safe fallback only when documented.

## Defaults And Precedence

Configuration can come from:

- built-in defaults;
- config files;
- environment variables;
- command-line arguments;
- remote configuration;
- feature-flag service;
- deployment templates.

Test precedence:

```text
command line > environment > file > default
```

Actual order depends on product and must be documented.

Verify:

- omitted value;
- explicit default;
- override;
- conflicting sources;
- reload/restart requirement;
- dynamic change;
- rollback.

## Feature Flags

Test:

- on/off;
- default state;
- targeted user/tenant;
- gradual rollout;
- stale cached flag;
- flag service unavailable;
- interaction between flags;
- rollback;
- old application version receiving new flag.

Feature flag is production configuration and can create combinations as complex as code branches.

## Version And Upgrade Matrix

Cover:

- clean install on supported version;
- application upgrade;
- OS/runtime/database upgrade;
- rollback where supported;
- mixed-version rolling deployment;
- old client with new server;
- new client with old server;
- deprecated configuration migration.

Compatibility may differ during rolling deployment from final steady state.

## Virtualized Vs Physical Environments

VMs and containers provide:

- repeatability;
- snapshots;
- fast provisioning;
- automation;
- broad software matrix.

Physical hardware remains important for:

- peripherals;
- firmware/driver;
- GPU;
- exact storage/network devices;
- hardware timing;
- mobile/embedded systems.

Record virtualization layer, host contention and resource limits.

## Configuration As Code

Prefer versioned definitions:

- Dockerfiles/images;
- Compose;
- Kubernetes manifests/Helm;
- Terraform;
- Ansible;
- VM images;
- checked-in templates.

For each test record:

- commit/image digest;
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
- full connection strings with credentials.

## Sample Test Matrix

| ID | OS | Runtime | DB | CPU/RAM | Purpose |
| --- | --- | --- | --- | --- | --- |
| C1 | Ubuntu LTS | Java 21 | PostgreSQL 16 | 4/8 GB | Primary baseline |
| C2 | Ubuntu LTS | Java 17 | PostgreSQL 16 | 4/8 GB | Minimum runtime |
| C3 | RHEL | Java 21 | PostgreSQL 16 | 4/8 GB | Enterprise OS |
| C4 | Ubuntu LTS | Java 21 | PostgreSQL 15 | 4/8 GB | Previous DB |
| C5 | Ubuntu LTS | Java 21 | PostgreSQL 16 | 2/4 GB | Minimum resources |
| C6 | Ubuntu LTS | Java 21 | PostgreSQL 16 | 8/16 GB | Scaling experiment |

Each row needs expected support status and test suite level.

## Example Test Cases

### Missing Dependency

**Given:** required database driver is unavailable.  
**When:** service starts.  
**Then:** startup fails with a clear non-secret error and no partial migration.

### Pool Size

**Given:** same build, data and 300 RPS workload.  
**When:** pool changes from 20 to 50.  
**Then:** compare percentiles, throughput, DB CPU, waits and errors.

### Locale And Timezone

**Given:** `en-US/UTC` and `de-DE/Europe-Berlin`.  
**When:** user creates a scheduled transaction.  
**Then:** stored instant and displayed local time remain correct.

### Peripheral

**Given:** each supported scanner model and driver.  
**When:** scan, disconnect, reconnect and send invalid input.  
**Then:** data is correct, errors are recoverable and no process restart is needed.

## Common Defects

- default differs between environments;
- environment variable silently ignored;
- invalid value accepted and fails later;
- larger pool overloads database;
- cache size causes OOM;
- old runtime serializes data differently;
- timezone changes scheduled execution;
- rolling deployment breaks protocol compatibility;
- feature flags create unsupported state;
- config reload applies only to some nodes;
- secrets appear in startup logs;
- VM benchmark is limited by noisy host.

## Reporting

Include:

- objective;
- selected matrix and rationale;
- supported/unsupported status;
- exact versions and configuration;
- workload and data;
- functional results;
- performance percentiles and throughput;
- resources and cost;
- failures and limitations;
- recommended configuration;
- evidence that the result is repeatable.

Avoid calling one configuration "optimal" without explaining workload, SLO, cost and operational constraints.

## QA Checklist

- [ ] Supported configuration dimensions are documented.
- [ ] Primary, minimum and boundary combinations are included.
- [ ] Pairwise coverage is supplemented by risk-based cases.
- [ ] Defaults and precedence are tested.
- [ ] Invalid and missing settings fail safely.
- [ ] Upgrades and mixed versions are covered.
- [ ] One factor changes per performance experiment.
- [ ] Build, image and configuration hashes are recorded.
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

