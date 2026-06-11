# Docker For Test Automation

Source: user-provided official Docker overview, expanded for test automation and CI/CD
Date added: 2026-06-11
Related plan item: Automation
Tags: QA, automation, Docker, containers, CI/CD, test environment
Language: English
Translation pair: quality-assurance/overview/07-automation/docker-for-test-automation.md

## Summary

Docker packages an application or test runner with its runtime and dependencies in an image and runs it as a container.

For automation, it solves two separate problems:

1. **Containerize the tests:** run test code in a known runtime.
2. **Create a test environment:** start the application, database, cache, broker, and other dependencies.

```text
Test image -> test container -> exit code + reports

Compose project:
app + database + cache + mock + test runner
```

Docker improves reproducibility but does not guarantee it automatically. Floating tags, external dependencies, CPU architecture, test data, and uncontrolled networks can still change results.

## Key Points

- An image is a read-only template; a container is its runnable instance.
- Containers should be treated as temporary and replaceable.
- The test process exit code communicates success or failure.
- Reports must be stored outside the temporary container filesystem.
- Docker Compose describes multi-container test environments.
- Process startup is not service readiness; use health checks or explicit waiting.
- Tests reach Compose services through service names and internal ports.
- Floating tags such as `latest` do not identify an immutable build.
- Never bake secrets into images or print them in logs.
- Clean up environments and data predictably after each run.

## Why Automation Uses Docker

### A Known Runtime

A test image can pin:

- language version;
- package manager;
- browser and driver;
- system libraries;
- test framework;
- helper tools;
- default command.

This reduces differences between developer laptops and CI runners.

### Isolated Environments

Each pipeline can receive separate:

- containers;
- networks;
- test databases;
- caches;
- queues;
- volumes;
- configuration.

Isolation reduces conflicts between parallel jobs.

### Fast Recreation

Instead of repairing an environment manually:

```bash
docker compose down -v
docker compose up -d
```

The `-v` option removes Compose volumes. It is useful for a complete data reset but destroys persisted data for that project.

## Main Objects

| Object | Automation role |
| --- | --- |
| Image | Versioned application or test runtime |
| Container | One test run or running service |
| Dockerfile | Image build instructions |
| Registry | Image storage |
| Network | Communication inside a test environment |
| Volume | Persistent data or artifact exchange |
| Bind mount | Container access to a host path |
| Compose | Multi-container stack definition |
| Health check | Service health or readiness signal |

## Docker Architecture

```text
docker CLI / Docker Compose
          |
          v
Docker API
          |
          v
Docker daemon (dockerd)
          |
          +-- images
          +-- containers
          +-- networks
          +-- volumes
```

The client sends commands to the daemon. The daemon builds images, starts containers, and manages Docker objects.

Access to the Docker daemon provides broad control over the host. Do not expose the Docker socket to untrusted containers without understanding the risk.

## Containerizing A Test Runner

Example Python test image:

```dockerfile
FROM python:3.12-slim

WORKDIR /tests

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "-q", "--junitxml=/artifacts/junit.xml"]
```

Build and run:

```bash
docker build -t qa-api-tests:local .

docker run --rm \
  -e BASE_URL=http://host.docker.internal:8080 \
  -v "$PWD/artifacts:/artifacts" \
  qa-api-tests:local
```

Here:

- `--rm` removes the container after completion;
- `-e` passes configuration;
- `-v` persists the report on the host;
- the `pytest` exit code becomes the container exit code;
- the pipeline job should fail when the test process returns non-zero.

## Exit Codes

```bash
docker run --rm qa-api-tests:local
echo $?
```

General rule:

```text
0     -> success
non-0 -> failure or a tool-specific status
```

Do not hide failures:

```bash
pytest || true
```

If a check is intentionally non-blocking, configure that behavior in CI while keeping the failed result visible.

## Artifacts

The container filesystem is usually temporary. Reports disappear when the container is removed unless they are exported.

Options:

- bind mount a host directory;
- use a named volume;
- run `docker cp` before removal;
- publish CI artifacts from a mounted path.

Useful artifacts:

- JUnit/XML or HTML reports;
- screenshots;
- videos;
- traces;
- application logs;
- network captures;
- coverage.

Artifacts must not expose passwords, tokens, cookies, or personal data.

## Docker Compose For Integration Tests

```yaml
services:
  api:
    image: example/api:1.8.3
    environment:
      DATABASE_URL: postgres://test:test@db:5432/app
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:17
    environment:
      POSTGRES_DB: app
      POSTGRES_USER: test
      POSTGRES_PASSWORD: test
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U test -d app"]
      interval: 2s
      timeout: 3s
      retries: 20

  tests:
    build: ./tests
    environment:
      BASE_URL: http://api:8080
    volumes:
      - ./artifacts:/artifacts
    depends_on:
      api:
        condition: service_started
```

Typical commands:

```bash
docker compose up -d db api
docker compose run --rm tests
docker compose logs --no-color > artifacts/services.log
docker compose down -v
```

The test runner should wait for an API health endpoint or use a wait script. `service_started` confirms process startup, not application readiness.

## Networking

Services inside a Compose network are reachable by service name:

```text
http://api:8080
postgres://db:5432/app
```

Inside the test container, `localhost` refers to the test container itself, not the API, database, or host.

Distinguish:

- **container port:** the port listened to by the process;
- **published host port:** a host port mapped with `ports`;
- **service name:** the DNS name inside the Compose network.

Communication between Compose services often does not require publishing ports to the host.

## Readiness And Health Checks

A container can be running while the application is still:

- applying migrations;
- loading configuration;
- warming caches;
- waiting for a database;
- unable to accept requests.

Example readiness probe:

```bash
curl --fail http://api:8080/health/ready
```

A useful wait mechanism:

- has a timeout;
- retries at an interval;
- fails the job clearly;
- prints diagnostics;
- does not sleep forever.

## Test Data

Common strategies:

- migration and seed on startup;
- a separate setup job;
- API fixtures;
- database snapshots;
- transaction rollback;
- unique data per test;
- a separate database or schema per job.

Do not depend on data left by a previous run.

For a full reset:

```bash
docker compose down -v
docker compose up -d
```

Preserve required logs and dumps before removing volumes.

## Images, Tags, And Reproducibility

```bash
docker pull example/api:latest
```

does not guarantee the same image over time because the tag can move.

For reproducibility:

- use a release tag or commit SHA;
- record the image digest;
- pin base images;
- keep dependency lock files;
- include the image reference in reports;
- do not rebuild between staging and production.

Immutable reference:

```text
example/api@sha256:...
```

## Test Dockerfile Practices

- choose the smallest suitable base image;
- pin dependencies;
- use `.dockerignore`;
- copy dependency files before source files for better caching;
- never store secrets in `ARG`, `ENV`, or image layers;
- use a non-root user where practical;
- use multi-stage builds when build tools are not needed at runtime;
- update base images regularly;
- scan images.

Example `.dockerignore`:

```text
.git
.venv
node_modules
artifacts
reports
.env
```

Do not treat `.dockerignore` as the only protection against secrets.

## Volumes And Bind Mounts

| Mechanism | Suitable use |
| --- | --- |
| Named volume | Database data and Docker-managed persistence |
| Bind mount | Source code, local configuration, and CI artifacts |
| Container layer | Temporary files for one run |

Bind mounts couple tests to the host filesystem. Permissions, line endings, and performance may differ across Windows, macOS, and Linux.

## Useful Commands

```bash
docker version
docker info
docker ps
docker ps -a
docker images

docker logs <container>
docker logs --tail 200 <container>
docker inspect <container>
docker stats
docker exec -it <container> sh

docker build -t qa-tests:local .
docker pull example/api:1.8.3
docker image inspect example/api:1.8.3

docker compose config
docker compose pull
docker compose build
docker compose up -d
docker compose ps
docker compose logs
docker compose run --rm tests
docker compose down -v
```

`docker compose config` shows the effective configuration after interpolation and file merging. Avoid exposing secrets when its output is written to public logs.

## Diagnosing A Failed Container

1. Run `docker ps -a`.
2. Check status and exit code.
3. Read `docker logs`.
4. Confirm image tag and digest.
5. Inspect command and entrypoint.
6. Validate environment variables without exposing secrets.
7. Check network and service names.
8. Check mounts and permissions.
9. Inspect health status.
10. Preserve evidence before cleanup.

Common causes:

- the main process exits;
- command or entrypoint is wrong;
- an environment variable is missing;
- port configuration is incorrect;
- a dependency is not ready;
- image architecture is incompatible;
- volume permissions are wrong;
- disk space is exhausted;
- artifacts are written outside the mounted path;
- the container is killed by a memory limit.

## Docker In CI/CD

```text
Build application image
-> scan
-> start isolated test stack
-> run tests in test container
-> collect reports and logs
-> remove stack
-> publish verified image
```

Good practices:

- use a unique Compose project name for parallel jobs;
- avoid shared databases between pipelines;
- apply CPU and memory limits when relevant;
- always clean up, including after failure;
- collect logs before cleanup;
- never provide production credentials to pull-request jobs;
- promote the validated image without rebuilding.

## Containers And Virtual Machines

A container is not a lightweight virtual machine.

| Property | Container | Virtual machine |
| --- | --- | --- |
| Kernel | Uses the host kernel | Has a guest OS and kernel |
| Startup | Usually faster | Usually slower |
| Size | Usually smaller | Usually larger |
| Isolation | Process and namespace isolation | VM boundary |
| Use | Services, tests, CI jobs | Full OS, stronger isolation, legacy systems |

On Windows and macOS, Linux containers normally run through a Linux VM managed by Docker Desktop.

## Limitations

Docker does not remove:

- CPU architecture differences;
- external network instability;
- flaky tests;
- race conditions;
- incorrect test data;
- kernel differences;
- browser rendering differences;
- the need for real mobile devices;
- production configuration defects.

A containerized test can be more reproducible, but still needs a correct environment model.

## QA Checklist

- [ ] Application image and tag are recorded.
- [ ] The test runner returns the correct exit code.
- [ ] Reports persist outside the temporary container.
- [ ] Logs are collected before cleanup.
- [ ] Services have readiness checks.
- [ ] Tests use service names and correct ports.
- [ ] Test data is reproducible.
- [ ] Parallel jobs are isolated.
- [ ] Floating tags are not used for release validation.
- [ ] Secrets are absent from images, logs, and artifacts.
- [ ] Cleanup runs after both success and failure.
- [ ] The validated image is promoted without rebuilding.

## Questions

### 1. How does an image differ from a container?

An image is a read-only template. A container is a runnable instance with configuration and a writable layer.

### 2. Why does `localhost` not reach the API from a test container?

Inside a container, `localhost` refers to that same container. Use the other Compose service's name.

### 3. How does CI know that tests failed?

The test process returns a non-zero exit code, which becomes the container exit code.

### 4. Why can reports disappear?

Files written only to a temporary container layer disappear when the container is removed. Use a mount, volume, or copy operation.

### 5. Why is `depends_on` not always enough?

A started process may not be ready to accept requests. Use a health check or explicit readiness wait.

### 6. Why is `latest` risky?

It can identify different image builds over time and reduces reproducibility.

### 7. Why remove volumes between tests?

It prevents old state from affecting a new run. Preserve required diagnostics first.

### 8. What should be checked when a container stops unexpectedly?

Status, exit code, logs, command, environment, health, mounts, limits, and image architecture.

## What To Review Later

- Dockerfile syntax;
- Compose profiles and multiple files;
- Testcontainers;
- image scanning and SBOM;
- BuildKit secrets;
- rootless containers;
- resource limits;
- container orchestration;
- Kubernetes test environments.

## Sources

- User-provided official Docker documentation: "What is Docker?"
- [Docker overview](https://docs.docker.com/get-started/docker-overview/)
- [Docker run reference](https://docs.docker.com/reference/cli/docker/container/run/)
- [Docker Compose reference](https://docs.docker.com/reference/cli/docker/compose/)
- [Docker build best practices](https://docs.docker.com/build/building/best-practices/)
