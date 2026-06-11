# CI/CD For QA: Pipelines, Checks, And Quality Gates

Source: user-provided Red Hat article "What is CI/CD?", expanded for practical QA work
Date added: 2026-06-11
Related plan item: Automation
Tags: QA, automation, CI/CD, pipeline, continuous integration, continuous delivery, continuous deployment
Language: English
Translation pair: quality-assurance/overview/07-automation/ci-cd-for-qa.md

## Summary

CI/CD is a set of practices for frequently integrating, validating, and delivering small changes.

It includes:

- **Continuous Integration (CI):** frequent integration with automated builds and checks;
- **Continuous Delivery:** the application is production-ready after the pipeline, but production deployment usually requires a human decision;
- **Continuous Deployment:** every change that passes the pipeline is automatically deployed to production.

For QA, a pipeline is more than a place to run automated tests. It is a feedback system that should:

- detect defects early;
- provide a clear failure reason;
- preserve evidence;
- block unsafe releases;
- avoid delaying the team with unreliable or unnecessary checks.

## Key Points

- Continuous Delivery and Continuous Deployment are different practices.
- Healthy CI depends on small changes integrated frequently.
- Run fast and inexpensive checks before slow and expensive ones.
- Not every test should block merge or deployment.
- Every quality gate needs a measurable criterion and an owner.
- Flaky tests reduce trust in the whole pipeline.
- Build an artifact once and promote it without rebuilding.
- Preserve logs, reports, and diagnostic artifacts.
- Production deployment requires monitoring, rollback, and clear ownership.
- Secrets, third-party dependencies, and runner permissions are part of CI/CD security.

## CI, Delivery, And Deployment

| Practice | Main goal | Production behavior |
| --- | --- | --- |
| Continuous Integration | Integrate and validate changes frequently | Deployment is not required |
| Continuous Delivery | Keep a validated release candidate ready | Usually has manual approval |
| Continuous Deployment | Release every passing change automatically | Deployment is automatic |

Useful questions:

```text
CI: Does the change integrate correctly?
Continuous Delivery: Can we safely release it now?
Continuous Deployment: Can the pipeline safely release it by itself?
```

The abbreviation `CD` is ambiguous. Documentation and conversations should clarify whether it means delivery or deployment.

## A Typical CI/CD Pipeline

```text
Commit / Pull Request
        |
        v
Lint + static checks + secret scan
        |
        v
Build + unit tests
        |
        v
Integration / component / API tests
        |
        v
Package immutable artifact
        |
        v
Deploy to test or staging
        |
        v
Smoke + selected E2E + security checks
        |
        v
Approval (Continuous Delivery) or automatic promotion
        |
        v
Production deployment
        |
        v
Post-deploy smoke + monitoring + rollback decision
```

The actual pipeline depends on the product. Mobile applications, backend services, web frontends, and infrastructure repositories need different stages.

## Checks At Different Stages

### Before Commit Or Push

- formatter;
- lint;
- unit tests for the affected module;
- secret detection;
- fast local checks.

The goal is to avoid publishing obviously broken changes.

### On A Pull Request

- compilation or build;
- unit tests;
- component and API tests;
- static analysis;
- dependency and security scans;
- a short smoke suite;
- migration and contract checks;
- risk-based test selection.

Feedback should arrive before the contributor loses context.

### After Merge

- full integration suite;
- broader regression;
- release artifact creation;
- image or package publication;
- deployment to a test environment;
- more expensive checks.

### Before Production

- staging smoke tests;
- critical E2E scenarios;
- compatibility checks;
- database migration validation;
- configuration validation;
- performance baseline or short threshold test;
- security and compliance gates;
- release approval for Continuous Delivery.

### After Deployment

- health checks;
- production smoke;
- synthetic monitoring;
- logs and error rate;
- latency and saturation;
- business metrics;
- automatic or manual rollback when criteria fail.

## The Test Pyramid In A Pipeline

Fast checks should form the foundation:

```text
         E2E / UI
      Integration / API
    Unit / component / static
```

Reasons:

- unit and component tests localize defects quickly;
- API tests are usually faster and more stable than UI tests;
- E2E tests protect critical user flows but are slower and more environment-sensitive;
- a complete UI regression suite on every commit may make CI unusable.

A pipeline should not contain every test without selection. The suite depends on the trigger, risk, and required feedback speed.

## Quality Gates

A quality gate is an automated or manual condition that must pass before a change can proceed.

| Gate | Example criterion |
| --- | --- |
| Build | Build completes successfully |
| Unit tests | No failed tests |
| API contract | No unapproved breaking changes |
| Security scan | No new critical vulnerabilities |
| Coverage | Does not fall below an agreed threshold |
| Smoke | All critical scenarios pass |
| Performance | p95 and error rate remain within budget |
| Manual approval | Release owner approves production deployment |

Weak gate:

```text
Quality must be good.
```

Measurable gate:

```text
All P0 smoke tests pass, no new Critical or High security findings exist,
and the threshold-test error rate is <= 1%.
```

A gate should have:

- a clear criterion;
- an owner;
- an exception process;
- waiver expiration;
- evidence;
- an escalation rule.

## Blocking And Non-Blocking Checks

Not every check should stop the pipeline.

**Common blocking checks:**

- build failure;
- unit or smoke failure;
- critical vulnerability;
- incompatible database migration;
- mandatory contract violation;
- missing required approval.

**Possible non-blocking checks:**

- experimental validation;
- a known flaky test;
- informational scan;
- long trend analysis;
- a test without an agreed threshold.

A non-blocking failure still needs visibility and ownership. Otherwise, pipeline output becomes noise that the team ignores.

## QA Responsibilities

QA can help:

- select tests for each stage;
- define quality gates;
- establish pass/fail criteria;
- design test data;
- maintain test independence;
- analyze failed jobs;
- reduce flaky tests;
- validate environments and configuration;
- preserve diagnostic artifacts;
- communicate release risk;
- design post-deployment validation;
- improve pipeline speed and trust.

QA does not need to own every test. Pipeline quality is a shared responsibility across development, QA, security, operations, and product stakeholders.

## Investigating A Failed Pipeline

1. Identify the first genuinely failed job, not only the final red stage.
2. Confirm the commit, branch, trigger, and environment.
3. Open the complete log and test report.
4. Check whether the failure reproduces.
5. Separate product, test, environment, data, configuration, and infrastructure failures.
6. Correlate the failure with the recent change.
7. Review screenshots, traces, dumps, and service logs.
8. Avoid blind retries before preserving evidence.
9. Record the root cause and owner.
10. Improve pipeline diagnostics when the problem is systemic.

| Category | Example |
| --- | --- |
| Product defect | API returns the wrong status code |
| Test defect | Incorrect locator or assertion |
| Flaky test | Result changes without a product change |
| Environment | Service, database, or browser is unavailable |
| Test data | Data has already been consumed or has the wrong state |
| Configuration | Variable is missing or endpoint is incorrect |
| Infrastructure | Runner loses network access or disk space |

Retries can be controlled resilience mechanisms, but they should not replace investigation.

## Artifacts And Reporting

Useful pipeline artifacts include:

- unit, API, and UI test reports;
- screenshots;
- browser traces and videos;
- application and service logs;
- network logs;
- crash dumps;
- coverage reports;
- security scan results;
- performance results;
- deployment manifests;
- build metadata;
- image digests or package versions.

Artifacts should:

- remain accessible after the job;
- have reasonable retention;
- exclude secrets and personal data;
- be linked to the commit and build;
- support reproduction and diagnosis.

## Build Once, Deploy Many

A reliable flow is:

```text
Source commit -> build artifact -> test -> staging -> production
```

The same immutable artifact moves between environments.

Rebuilding for production may produce something different from the validated staging artifact because of:

- a newly published dependency;
- a changed base image;
- different build configuration;
- an unstable external repository;
- toolchain differences.

Environment-specific values should be provided through configuration rather than artifact changes.

## Deployment Strategies

| Strategy | Idea | QA focus |
| --- | --- | --- |
| Rolling | Instances update gradually | Mixed-version compatibility |
| Blue-green | A new environment is prepared beside the old one | Traffic switch and rollback |
| Canary | A small traffic percentage receives the new version | Canary metrics and expansion criteria |
| Feature flags | Code is deployed while exposure is controlled separately | Flag states and user combinations |

Continuous Deployment without monitoring and rollback is automated risk rather than safe delivery.

## CI/CD Security

Common risks:

- secrets in repositories, logs, or artifacts;
- excessive runner permissions;
- untrusted code running with production credentials;
- vulnerable third-party actions, plugins, or dependencies;
- artifact tampering;
- unprotected branches or environments;
- unrestricted deployment access;
- test-environment data leakage.

Useful practices:

- store secrets in a secret manager;
- grant least privilege;
- separate build and production deployment credentials;
- protect branches and environments;
- pin third-party action versions;
- scan source, dependencies, and images;
- sign or verify artifact provenance;
- retain audit logs;
- update runners and plugins;
- prevent sensitive values from entering logs.

## Pipeline Metrics

Useful measurements:

- pipeline duration;
- queue time;
- success rate;
- flaky-test rate;
- mean time to repair a broken pipeline;
- deployment frequency;
- lead time for changes;
- change failure rate;
- time to restore service.

Metrics should improve the system rather than punish the team. Removing valuable tests may make duration look better while reducing quality.

## Common Mistakes

- CI runs infrequently;
- the main branch remains red;
- pipelines take hours without risk-based selection;
- flaky tests are only retried;
- reports and logs are not preserved;
- staging differs significantly from production;
- tests depend on execution order;
- test data is not isolated;
- secrets appear in logs;
- deployment has no rollback plan;
- every check is blocking;
- no one owns a failed job;
- deployment command success is treated as production success.

## QA Checklist

- [ ] Pipeline triggers are understood.
- [ ] Every stage has an owner.
- [ ] Fast checks run before expensive checks.
- [ ] Blocking gates have measurable criteria.
- [ ] Smoke tests protect critical flows.
- [ ] Flaky tests are tracked separately.
- [ ] Reports and diagnostic artifacts are preserved.
- [ ] Test data is isolated and reproducible.
- [ ] The validated artifact is the artifact being deployed.
- [ ] Secrets do not appear in code, logs, or artifacts.
- [ ] Staging is sufficiently production-like.
- [ ] Post-deployment checks exist.
- [ ] Monitoring identifies the release version.
- [ ] Rollback is tested and owned.

## Questions

### 1. How does Continuous Delivery differ from Continuous Deployment?

Continuous Delivery keeps the system ready for release but usually requires a human decision for production. Continuous Deployment releases every passing change automatically.

### 2. Why should fast tests run first?

They provide feedback quickly and stop bad changes before expensive environments and E2E suites are used.

### 3. What is a quality gate?

It is a measurable condition required before proceeding to another stage, merge, or deployment.

### 4. Should every test block a pipeline?

No. Blocking status depends on risk, reliability, and pipeline purpose. Non-blocking failures must still remain visible.

### 5. Why is a blind retry dangerous?

It can hide a product defect, flaky behavior, or environment problem and may discard useful evidence.

### 6. What does build once, deploy many mean?

One immutable artifact is validated and promoted through environments without rebuilding.

### 7. What should QA validate after production deployment?

Health, critical smoke, logs, error rate, latency, business metrics, and rollback conditions.

### 8. What security risks exist in CI/CD?

Secret exposure, dangerous permissions, vulnerable dependencies, artifact tampering, unprotected branches, and untrusted code with production access.

## What To Review Later

- GitHub Actions, GitLab CI, or Jenkins syntax;
- pipeline as code;
- container registries and image digests;
- test parallelization;
- contract testing;
- feature flags;
- blue-green and canary deployment;
- rollback and database migration strategy;
- software supply chain security;
- DORA metrics.

## Sources

- User-provided Red Hat article: "What is CI/CD?"
- [Red Hat: What is CI/CD?](https://www.redhat.com/en/topics/devops/what-is-ci-cd)
