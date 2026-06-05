# Docker Basics For QA

Source: pasted article about Docker  
Date added: 2026-06-05  
Related plan item: Web Testing  
Tags: QA, web testing, Docker, containers, CI/CD, environment  
Language: English  
Translation pair: quality-assurance/overview/web-testing/docker-basics-for-qa.md

## Summary

Docker is a platform for developing, shipping, and running applications in containers.

A container is an isolated runtime environment where an application runs together with its dependencies. This helps the same application work consistently on a developer laptop, test environment, CI/CD pipeline, and production-like server.

Main idea:

> For QA, Docker helps create stable test environments, reproduce bugs faster, and test applications in conditions closer to production.

## Key Points

- Docker separates the application from infrastructure and packages the application together with dependencies.
- An image is a read-only template for creating a container.
- A container is a runnable instance of an image.
- Docker client sends commands to Docker daemon, and the daemon manages containers, images, networks, and volumes.
- Docker registry stores images; Docker Hub is a public example.
- Docker Compose helps run several containers as one application stack.
- For QA, Docker is useful in local testing, CI/CD, test data setup, API testing, and reproduction of environment-specific bugs.

## Notes

## What Is Docker?

Docker is an open platform for:

- building applications;
- packaging applications;
- shipping applications;
- running applications.

Instead of manually installing required runtime versions, libraries, database, cache, and configuration on every machine, the team describes the environment in a Docker image.

Then this image can be started as a container.

Simple idea:

```text
Image -> Container -> Running application
```

## Why QA Should Know Docker

QA often hears:

> "It works locally for me."

Docker reduces such differences because the team can run the same application stack in a standardized environment.

QA uses Docker to:

- start a local test environment;
- run backend, database, cache, message broker;
- verify a bug in the same service version;
- recreate an environment quickly;
- run tests in CI/CD;
- inspect container logs;
- verify migrations, seed data, configs;
- test integration between services.

## Containers

A container is a runnable instance of an image.

A container includes:

- application code;
- runtime;
- libraries;
- environment variables;
- filesystem layer;
- process;
- network configuration.

A container is isolated from other containers and the host machine, but it uses the host system kernel.

You can:

- create;
- start;
- stop;
- restart;
- remove;
- inspect;
- view logs;
- connect to a network;
- mount a volume.

Important:

> If a container is removed, changes inside it disappear unless they are stored in a volume or external storage.

## Images

An image is a read-only template for creating containers.

An image may contain:

- operating system base layer, such as Ubuntu or Alpine;
- runtime, such as Node.js, Python, Java;
- application files;
- dependencies;
- configuration;
- startup command.

Images are built from a `Dockerfile`.

Concept:

```text
Dockerfile -> docker build -> Image -> docker run -> Container
```

Images consist of layers. If only one Dockerfile instruction changes, Docker can reuse cached layers, so builds are often faster.

## Dockerfile

Dockerfile is a text file with instructions for building an image.

Example:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

For QA, reading a Dockerfile helps understand:

- which base image is used;
- which dependencies are installed;
- which command starts the application;
- which files are copied into the image;
- which ports may be used;
- where behavior may differ between environments.

## Docker Architecture

Docker uses client-server architecture.

Main parts:

- Docker client;
- Docker daemon;
- Docker objects;
- Docker registry.

Simplified flow:

```text
docker command -> Docker client -> Docker daemon -> images/containers/networks/volumes
```

## Docker Client

Docker client is the command line tool `docker`.

When QA runs:

```bash
docker run nginx
```

the client sends the command to Docker daemon.

## Docker Daemon

Docker daemon (`dockerd`) does the main work:

- builds images;
- runs containers;
- manages networks;
- manages volumes;
- communicates with registries;
- handles Docker API requests.

The daemon can run on the same machine or on a remote host.

## Docker Desktop

Docker Desktop is an application for Windows, macOS, and Linux that installs Docker tooling conveniently.

It usually includes:

- Docker daemon;
- Docker client;
- Docker Compose;
- Kubernetes option;
- credential helper;
- UI for containers/images/logs.

For QA on Windows/macOS, Docker Desktop is often the easiest way to start.

## Docker Registry

A Docker registry stores Docker images.

Examples:

- Docker Hub;
- GitHub Container Registry;
- GitLab Container Registry;
- private company registry.

Commands:

```bash
docker pull nginx
docker push my-app:1.0
```

For QA, it is important to know which registry and tag the application is started from. Different tags may mean different builds.

## Docker Objects

## Images

Images are templates for containers.

Example:

```bash
docker images
```

## Containers

Containers are running or stopped instances of images.

Example:

```bash
docker ps
docker ps -a
```

## Networks

Networks allow containers to communicate with each other.

Example:

```text
web container -> api container -> database container
```

QA may see a bug where a service is unreachable because of incorrect network configuration.

## Volumes

Volumes store data outside the container lifecycle.

They are used for:

- database data;
- uploaded files;
- logs;
- persistent application data.

If a database container is recreated without a volume, test data may disappear.

## Docker Compose

Docker Compose helps run a multi-container application through `docker-compose.yml` or `compose.yaml`.

Example stack:

- web;
- api;
- postgres;
- redis;
- nginx.

Commands:

```bash
docker compose up -d
docker compose ps
docker compose logs
docker compose down
```

For QA, Docker Compose is convenient because the whole test environment can be started with one command.

## Example: docker run

Command:

```bash
docker run -i -t ubuntu /bin/bash
```

What happens:

1. Docker checks whether the `ubuntu` image exists locally.
2. If the image is missing, Docker downloads it from the registry.
3. Docker creates a container.
4. Docker adds a writable filesystem layer.
5. Docker connects the container to a network.
6. Docker starts `/bin/bash`.
7. QA gets an interactive shell inside the container.

When the user runs `exit`, the process finishes and the container stops.

## Docker In CI/CD

Docker fits CI/CD well:

- build application image;
- run automated tests in a container;
- run integration tests with database/cache containers;
- publish image to registry;
- deploy the same image to staging/production.

For QA, this means:

- test result depends less on a specific CI machine;
- failed pipeline is easier to reproduce locally;
- test environment can be recreated;
- service versions are fixed through image tags.

## Docker Vs Virtual Machines

Docker containers are lighter than classic virtual machines.

| Area | Container | Virtual machine |
| --- | --- | --- |
| OS | Uses host kernel. | Has full guest OS. |
| Startup | Usually fast. | Usually slower. |
| Size | Usually smaller. | Usually larger. |
| Isolation | Process/container isolation. | Stronger VM-level isolation. |
| Use case | Apps, services, CI/CD, local env. | Full OS isolation, legacy environments. |

QA does not have to choose the technology, but should understand that a container starts faster and is easier to recreate.

## Common QA Scenarios

QA can use Docker to:

- run a local website;
- run API with database;
- test migrations;
- reproduce a production-like bug;
- reset test environment;
- inspect logs;
- run automated tests;
- test integration with Redis/PostgreSQL/RabbitMQ;
- compare behavior between image tags;
- verify that app starts after deploy.

## Common Docker-Related Bugs

Typical problems:

- wrong image tag deployed;
- container exits immediately;
- environment variable missing;
- database container not ready when app starts;
- port not exposed or mapped incorrectly;
- volume missing, so data disappears;
- network name/service name wrong;
- old image cached locally;
- permission issue inside container;
- health check failing;
- logs not written or collected;
- different behavior between local and container environment.

## Useful Commands For QA

| Command | Purpose |
| --- | --- |
| `docker ps` | Show running containers. |
| `docker ps -a` | Show all containers. |
| `docker logs <container>` | View container logs. |
| `docker exec -it <container> sh` | Open shell inside container. |
| `docker images` | Show local images. |
| `docker pull <image>` | Download image from registry. |
| `docker run <image>` | Create and run container from image. |
| `docker stop <container>` | Stop container. |
| `docker rm <container>` | Remove container. |
| `docker compose up -d` | Start compose stack in background. |
| `docker compose down` | Stop and remove compose stack. |
| `docker compose logs` | View compose services logs. |

## Bug Report Tips

For Docker/environment bugs include:

- image name and tag;
- container name;
- command used to start it;
- environment variables, if safe to share;
- exposed ports;
- logs;
- compose file/service name;
- expected and actual result;
- whether rebuild/restart changes behavior;
- whether issue reproduces outside container.

Example:

> API container `qa-api:2026-06-05.1` exits on startup in staging compose stack. `docker compose logs api` shows missing `DATABASE_URL`. Expected: API starts and health check returns `200`.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Docker | Platform for building, shipping and running applications in containers. |
| Container | Runnable isolated instance of an image. |
| Image | Read-only template used to create containers. |
| Dockerfile | File with instructions for building a Docker image. |
| Docker daemon | Background service that manages Docker objects. |
| Docker client | CLI/tool that sends commands to Docker daemon. |
| Registry | Storage for Docker images. |
| Docker Hub | Public Docker registry. |
| Volume | Persistent storage managed by Docker. |
| Network | Docker object that allows containers to communicate. |
| Docker Compose | Tool for running multi-container applications. |

## Questions

### 1. What is Docker?

Answer: Docker is a platform for packaging and running applications in containers.

### 2. How is an image different from a container?

Answer: An image is a read-only template, while a container is a running or stopped instance created from that image.

### 3. Why does QA need Docker?

Answer: To run stable test environments, reproduce bugs, inspect logs, and test application stacks closer to production.

### 4. What does Docker daemon do?

Answer: It manages images, containers, networks, volumes, and handles Docker API requests.

### 5. What is a Docker registry?

Answer: A storage for Docker images, such as Docker Hub or a private company registry.

### 6. Why are volumes needed?

Answer: To persist data outside the container lifecycle, such as database data or uploaded files.

### 7. What does Docker Compose do?

Answer: It runs and manages a multi-container application stack through a compose file.

## What To Review Later

- Image vs container.
- Docker client, Docker daemon, registry.
- Dockerfile basics.
- Docker Compose basics.
- Commands: `docker ps`, `docker logs`, `docker exec`, `docker compose up`.
- Common QA issues with ports, env vars, volumes, networks and logs.
