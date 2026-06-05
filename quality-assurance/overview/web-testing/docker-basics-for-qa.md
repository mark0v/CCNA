# Docker Basics For QA

Source: pasted article about Docker  
Date added: 2026-06-05  
Related plan item: Web Testing  
Tags: QA, web testing, Docker, containers, CI/CD, environment  
Language: Russian  
Translation pair: quality-assurance-en/overview/web-testing/docker-basics-for-qa.md

## Summary

Docker - это platform для разработки, доставки и запуска приложений в containers.

Container - это изолированная runtime environment, в которой приложение запускается вместе со своими dependencies. Благодаря этому одна и та же application может работать одинаково на laptop developer, test environment, CI/CD pipeline и production-like server.

Главная мысль:

> Для QA Docker помогает получать стабильные test environments, быстрее воспроизводить bugs и проверять application в условиях, близких к production.

## Key Points

- Docker отделяет application от infrastructure и упаковывает application вместе с dependencies.
- Image - read-only template для создания container.
- Container - runnable instance of an image.
- Docker client отправляет команды Docker daemon, а daemon создает и управляет containers, images, networks и volumes.
- Docker registry хранит images; публичный пример - Docker Hub.
- Docker Compose помогает запускать несколько containers как один application stack.
- Для QA Docker полезен в локальном тестировании, CI/CD, test data setup, API testing и reproduction of environment-specific bugs.

## Notes

## What Is Docker?

Docker - это open platform для:

- building applications;
- packaging applications;
- shipping applications;
- running applications.

Вместо того чтобы вручную устанавливать нужные versions of runtime, libraries, database, cache и configuration на каждой машине, команда описывает environment в Docker image.

Затем этот image можно запустить как container.

Простой смысл:

```text
Image -> Container -> Running application
```

## Why QA Should Know Docker

QA часто сталкивается с фразой:

> "У меня локально работает."

Docker уменьшает такие расхождения, потому что team может запускать одинаковый application stack в standardized environment.

QA использует Docker, чтобы:

- поднять local test environment;
- запустить backend, database, cache, message broker;
- проверить bug в той же version service;
- быстро пересоздать environment;
- запускать tests in CI/CD;
- смотреть logs containers;
- проверить migrations, seed data, configs;
- тестировать integration between services.

## Containers

Container - это runnable instance of an image.

Container содержит:

- application code;
- runtime;
- libraries;
- environment variables;
- filesystem layer;
- process;
- network configuration.

Container изолирован от других containers и host machine, но использует kernel host system.

Что можно делать с container:

- create;
- start;
- stop;
- restart;
- remove;
- inspect;
- view logs;
- connect to network;
- mount volume.

Важно:

> Если container удалили, все изменения внутри него исчезнут, если они не сохранены в volume или external storage.

## Images

Image - это read-only template для создания containers.

Image может содержать:

- operating system base layer, например Ubuntu or Alpine;
- runtime, например Node.js, Python, Java;
- application files;
- dependencies;
- configuration;
- startup command.

Images строятся из `Dockerfile`.

Пример идеи:

```text
Dockerfile -> docker build -> Image -> docker run -> Container
```

Images состоят из layers. Если меняется только одна instruction в Dockerfile, Docker может переиспользовать cached layers, поэтому build often faster.

## Dockerfile

Dockerfile - это текстовый файл с instructions для сборки image.

Пример:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

Для QA полезно читать Dockerfile, чтобы понять:

- какая base image используется;
- какие dependencies установлены;
- какой command запускает application;
- какие files попадают внутрь image;
- какие ports могут использоваться;
- где может отличаться behavior between environments.

## Docker Architecture

Docker использует client-server architecture.

Основные части:

- Docker client;
- Docker daemon;
- Docker objects;
- Docker registry.

Упрощенный flow:

```text
docker command -> Docker client -> Docker daemon -> images/containers/networks/volumes
```

## Docker Client

Docker client - это command line tool `docker`.

Когда QA вводит:

```bash
docker run nginx
```

client отправляет command Docker daemon.

## Docker Daemon

Docker daemon (`dockerd`) выполняет основную работу:

- builds images;
- runs containers;
- manages networks;
- manages volumes;
- communicates with registries;
- handles Docker API requests.

Daemon может работать на той же machine или remote host.

## Docker Desktop

Docker Desktop - это приложение для Windows, macOS и Linux, которое удобно ставит Docker tooling.

Обычно включает:

- Docker daemon;
- Docker client;
- Docker Compose;
- Kubernetes option;
- credential helper;
- UI для containers/images/logs.

Для QA на Windows/macOS Docker Desktop часто самый простой способ начать.

## Docker Registry

Docker registry хранит Docker images.

Примеры:

- Docker Hub;
- GitHub Container Registry;
- GitLab Container Registry;
- private company registry.

Команды:

```bash
docker pull nginx
docker push my-app:1.0
```

Для QA важно знать, из какого registry и с каким tag запускается application. Разные tags могут означать разные builds.

## Docker Objects

## Images

Images - templates для containers.

Пример:

```bash
docker images
```

## Containers

Containers - running or stopped instances of images.

Пример:

```bash
docker ps
docker ps -a
```

## Networks

Networks позволяют containers общаться друг с другом.

Пример:

```text
web container -> api container -> database container
```

QA может столкнуться с bug, когда service недоступен из-за неправильной network configuration.

## Volumes

Volumes сохраняют data вне lifecycle container.

Их используют для:

- database data;
- uploaded files;
- logs;
- persistent application data.

Если database container пересоздали без volume, test data может исчезнуть.

## Docker Compose

Docker Compose помогает запускать multi-container application через `docker-compose.yml` или `compose.yaml`.

Пример stack:

- web;
- api;
- postgres;
- redis;
- nginx.

Команды:

```bash
docker compose up -d
docker compose ps
docker compose logs
docker compose down
```

Для QA Docker Compose удобен, потому что можно поднять весь test environment одной командой.

## Example: docker run

Команда:

```bash
docker run -i -t ubuntu /bin/bash
```

Что происходит:

1. Docker проверяет, есть ли `ubuntu` image локально.
2. Если image нет, Docker скачивает его из registry.
3. Docker создает container.
4. Docker добавляет writable filesystem layer.
5. Docker подключает container к network.
6. Docker запускает `/bin/bash`.
7. QA получает interactive shell внутри container.

Когда user выполняет `exit`, process завершается и container останавливается.

## Docker In CI/CD

Docker хорошо подходит для CI/CD:

- build application image;
- run automated tests in container;
- run integration tests with database/cache containers;
- publish image to registry;
- deploy same image to staging/production.

Для QA это значит:

- test result меньше зависит от конкретной CI machine;
- проще воспроизвести failed pipeline locally;
- test environment можно пересоздать;
- версии services фиксируются через image tags.

## Docker Vs Virtual Machines

Docker containers легче, чем classic virtual machines.

| Area | Container | Virtual machine |
| --- | --- | --- |
| OS | Uses host kernel. | Has full guest OS. |
| Startup | Usually fast. | Usually slower. |
| Size | Usually smaller. | Usually larger. |
| Isolation | Process/container isolation. | Stronger VM-level isolation. |
| Use case | Apps, services, CI/CD, local env. | Full OS isolation, legacy environments. |

QA не обязан выбирать technology, но должен понимать: container starts faster and is easier to recreate.

## Common QA Scenarios

QA может использовать Docker для:

- run local website;
- run API with database;
- test migrations;
- reproduce production-like bug;
- reset test environment;
- check logs;
- run automated tests;
- test integration with Redis/PostgreSQL/RabbitMQ;
- compare behavior between image tags;
- verify that app starts after deploy.

## Common Docker-Related Bugs

Типичные проблемы:

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
- logs not written or not collected;
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

### 1. Что такое Docker?

Answer: Docker - это platform для упаковки и запуска applications в containers.

### 2. Чем image отличается от container?

Answer: Image - read-only template, а container - running or stopped instance created from that image.

### 3. Зачем QA Docker?

Answer: Чтобы запускать стабильные test environments, воспроизводить bugs, смотреть logs и проверять application stack ближе к production.

### 4. Что делает Docker daemon?

Answer: Он управляет images, containers, networks, volumes и выполняет Docker API requests.

### 5. Что такое Docker registry?

Answer: Хранилище Docker images, например Docker Hub или private company registry.

### 6. Зачем нужны volumes?

Answer: Чтобы сохранять data вне lifecycle container, например database data или uploaded files.

### 7. Что делает Docker Compose?

Answer: Позволяет запускать и управлять multi-container application stack через compose file.

## What To Review Later

- Image vs container.
- Docker client, Docker daemon, registry.
- Dockerfile basics.
- Docker Compose basics.
- Commands: `docker ps`, `docker logs`, `docker exec`, `docker compose up`.
- Common QA issues with ports, env vars, volumes, networks and logs.
