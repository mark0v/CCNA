# Docker для автоматизации тестирования

Source: user-provided official Docker overview, expanded for test automation and CI/CD
Date added: 2026-06-11
Related plan item: Automation
Tags: QA, automation, Docker, containers, CI/CD, test environment
Language: Russian
Translation pair: quality-assurance-en/overview/07-automation/docker-for-test-automation.md

## Summary

Docker позволяет упаковать приложение или test runner вместе с runtime и dependencies в image, а затем запускать его как container.

Для автоматизации это решает две разные задачи:

1. **Контейнеризировать tests** — запускать test code в известном runtime.
2. **Поднять test environment** — запустить application, database, cache, broker и другие dependencies.

```text
Test image -> test container -> exit code + reports

Compose project:
app + database + cache + mock + test runner
```

Docker повышает воспроизводимость, но не гарантирует её автоматически. Floating tags, внешние dependencies, различия CPU architecture, test data и неконтролируемая сеть всё ещё могут менять результат.

## Key Points

- Image — read-only template, container — его запущенный экземпляр.
- Container должен рассматриваться как временный и заменяемый.
- Test result передаётся через process exit code.
- Reports нужно сохранять вне временной filesystem container.
- Docker Compose удобно описывает multi-container test environment.
- Service startup не означает readiness; нужны health checks или явное ожидание.
- Tests должны обращаться к Compose services по service name и внутреннему port.
- Image tags вроде `latest` не гарантируют неизменность build.
- Secrets нельзя встраивать в image или печатать в logs.
- После test run environment и данные должны очищаться предсказуемо.

## Что даёт Docker автоматизации

### Одинаковый runtime

Test image может фиксировать:

- версию языка;
- package manager;
- browser и driver;
- system libraries;
- test framework;
- helper tools;
- default command.

Это уменьшает различия между laptop и CI runner.

### Изолированное окружение

Каждый pipeline может получить отдельные:

- containers;
- network;
- test database;
- cache;
- queues;
- volumes;
- configuration.

Изоляция снижает конфликты между параллельными jobs.

### Быстрое пересоздание

Вместо ручного ремонта environment:

```bash
docker compose down -v
docker compose up -d
```

Флаг `-v` удаляет Compose volumes. Он полезен для полного reset test data, но уничтожает сохранённые данные этого project.

## Основные объекты

| Объект | Роль в автоматизации |
| --- | --- |
| Image | Версионируемый runtime приложения или tests |
| Container | Один test run или запущенный service |
| Dockerfile | Инструкции сборки image |
| Registry | Хранилище images |
| Network | Связь services внутри test environment |
| Volume | Persistent data или обмен artifacts |
| Bind mount | Доступ container к host path |
| Compose | Описание multi-container stack |
| Health check | Сигнал готовности или состояния service |

## Архитектура Docker

Docker использует client-server model:

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

Docker client отправляет команды daemon. Daemon собирает images, запускает containers и управляет Docker objects.

Доступ к Docker daemon даёт широкие возможности на host. Не передавайте Docker socket недоверенному container без понимания риска.

## Контейнеризация test runner

Пример Python test image:

```dockerfile
FROM python:3.12-slim

WORKDIR /tests

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "-q", "--junitxml=/artifacts/junit.xml"]
```

Сборка:

```bash
docker build -t qa-api-tests:local .
```

Запуск:

```bash
docker run --rm \
  -e BASE_URL=http://host.docker.internal:8080 \
  -v "$PWD/artifacts:/artifacts" \
  qa-api-tests:local
```

Обратите внимание:

- `--rm` удаляет container после завершения;
- `-e` передаёт configuration;
- `-v` сохраняет report на host;
- exit code `pytest` становится exit code container;
- pipeline job должен упасть, если test process вернул ненулевой код.

## Exit codes

Docker сообщает код завершения основного process:

```bash
docker run --rm qa-api-tests:local
echo $?
```

Общее правило:

```text
0     -> success
non-0 -> failure или специальный status test tool
```

Не маскируйте код так:

```bash
pytest || true
```

Такая команда делает job зелёной даже при failed tests. Если падение должно быть non-blocking, оформляйте это средствами CI и сохраняйте видимый результат.

## Artifacts

Container filesystem обычно временная. После удаления container reports исчезнут, если их не вынести.

Варианты:

- bind mount host directory;
- named volume;
- `docker cp` до удаления container;
- публикация CI artifacts из mounted path.

Полезно сохранять:

- JUnit/XML или HTML reports;
- screenshots;
- videos;
- traces;
- application logs;
- network dumps;
- coverage.

Artifacts не должны содержать passwords, tokens, cookies или персональные данные.

## Docker Compose для integration tests

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

Запуск:

```bash
docker compose up -d db api
docker compose run --rm tests
docker compose logs --no-color > artifacts/services.log
docker compose down -v
```

В реальном проекте test runner должен дождаться готовности API через health endpoint или wait script. `service_started` подтверждает запуск process, но не готовность приложения принимать запросы.

## Networking

Внутри Compose network services доступны по именам:

```text
http://api:8080
postgres://db:5432/app
```

`localhost` внутри test container указывает на сам test container, а не на API, database или host.

Различайте:

- **container port** — port, который слушает process внутри container;
- **published host port** — port host, проброшенный через `ports`;
- **service name** — DNS name внутри Compose network.

Для communication между Compose services публикация port на host часто не нужна.

## Readiness и health checks

Container может быть `running`, хотя application ещё:

- выполняет migrations;
- загружает configuration;
- прогревает cache;
- ждёт database;
- не готова отвечать.

Проверка readiness может включать:

```bash
curl --fail http://api:8080/health/ready
```

Хороший wait mechanism:

- имеет timeout;
- повторяет check с interval;
- завершает job с ошибкой;
- печатает понятную диагностику;
- не использует бесконечный `sleep`.

## Test data

Стратегии:

- migration + seed при старте;
- отдельный setup job;
- API fixtures;
- database snapshot;
- transaction rollback;
- уникальные данные на test;
- отдельная database/schema на job.

Плохая практика — зависеть от данных, оставшихся после предыдущего запуска.

Для полного reset:

```bash
docker compose down -v
docker compose up -d
```

Перед удалением volumes сохраните нужные logs и dumps.

## Images, tags и reproducibility

Команда:

```bash
docker pull example/api:latest
```

не гарантирует один и тот же image в разные моменты. Tag может быть переназначен.

Для воспроизводимости:

- используйте release tag или commit SHA;
- сохраняйте image digest;
- фиксируйте base images;
- храните lock files;
- записывайте image reference в report;
- не пересобирайте artifact между staging и production.

Пример immutable reference:

```text
example/api@sha256:...
```

## Dockerfile для tests

Практики:

- выбирать минимальный подходящий base image;
- фиксировать dependencies;
- использовать `.dockerignore`;
- копировать dependency files до source для build cache;
- не хранить secrets в `ARG`, `ENV` или layers;
- запускать process от non-root user, когда возможно;
- использовать multi-stage build, если build tools не нужны в final image;
- регулярно обновлять base image;
- сканировать image.

`.dockerignore` может исключать:

```text
.git
.venv
node_modules
artifacts
reports
.env
```

Не полагайтесь на него как на единственную защиту secrets.

## Volumes и bind mounts

| Механизм | Подходит для |
| --- | --- |
| Named volume | Database data и Docker-managed persistence |
| Bind mount | Source code, local config и CI artifacts |
| Container layer | Временные файлы одного run |

Bind mount связывает test с host filesystem. Это удобно, но может создавать различия в permissions, line endings и производительности между Windows, macOS и Linux.

## Полезные команды

```bash
# Состояние
docker version
docker info
docker ps
docker ps -a
docker images

# Диагностика
docker logs <container>
docker logs --tail 200 <container>
docker inspect <container>
docker stats
docker exec -it <container> sh

# Images
docker build -t qa-tests:local .
docker pull example/api:1.8.3
docker image inspect example/api:1.8.3

# Compose
docker compose config
docker compose pull
docker compose build
docker compose up -d
docker compose ps
docker compose logs
docker compose run --rm tests
docker compose down -v
```

`docker compose config` полезен перед запуском: он показывает итоговую configuration после interpolation и объединения Compose files. Следите, чтобы вывод не попал в публичный log вместе с secrets.

## Диагностика failed container

1. Выполнить `docker ps -a`.
2. Посмотреть exit code и status.
3. Открыть `docker logs`.
4. Проверить image tag и digest.
5. Проверить command и entrypoint.
6. Проверить environment variables без публикации secrets.
7. Проверить network и service names.
8. Проверить mounts и permissions.
9. Проверить health status через `docker inspect`.
10. Сохранить evidence до cleanup.

Типичные причины:

- process завершился;
- неправильный command;
- отсутствует environment variable;
- port указан неверно;
- dependency ещё не ready;
- image для другой CPU architecture;
- volume имеет неверные permissions;
- disk заполнен;
- test artifacts записываются не в mounted path;
- container killed из-за memory limit.

## Docker в CI/CD

Типичный flow:

```text
Build application image
-> scan
-> start isolated test stack
-> run tests in test container
-> collect reports and logs
-> remove stack
-> publish verified image
```

Правила:

- назначать уникальный Compose project name для parallel jobs;
- не использовать общую database между pipelines;
- ограничивать CPU и memory, если это важно для сценария;
- всегда выполнять cleanup, в том числе после failure;
- сохранять logs до cleanup;
- не передавать production credentials в Pull Request jobs;
- продвигать проверенный image, а не пересобирать его.

## Containers и virtual machines

Container не является лёгкой virtual machine.

| Свойство | Container | Virtual machine |
| --- | --- | --- |
| Kernel | Использует kernel host | Имеет guest OS и kernel |
| Startup | Обычно быстрее | Обычно медленнее |
| Размер | Обычно меньше | Обычно больше |
| Isolation | Process и namespace isolation | VM boundary |
| Применение | Services, tests, CI jobs | Полная OS, сильная изоляция, legacy |

На Windows или macOS Linux containers обычно всё равно работают через Linux VM, которой управляет Docker Desktop.

## Ограничения

Docker не устраняет:

- различия CPU architecture;
- внешнюю network instability;
- flaky tests;
- race conditions;
- неверные test data;
- различия kernel;
- browser rendering differences;
- необходимость testing на реальных mobile devices;
- ошибки production configuration.

Containerized test может быть воспроизводимее, но он всё ещё требует корректной модели environment.

## QA Checklist

- [ ] Image и tag тестируемого приложения записаны.
- [ ] Test runner возвращает правильный exit code.
- [ ] Reports сохраняются вне временного container.
- [ ] Logs собираются до cleanup.
- [ ] Services имеют readiness checks.
- [ ] Tests используют service names и правильные ports.
- [ ] Test data создаются воспроизводимо.
- [ ] Parallel jobs изолированы.
- [ ] Floating tags не используются для release validation.
- [ ] Secrets отсутствуют в image, logs и artifacts.
- [ ] Cleanup выполняется и после failure.
- [ ] Проверенный image продвигается без пересборки.

## Questions

### 1. Чем image отличается от container?

Image — read-only template. Container — созданный из него runnable instance с configuration и writable layer.

### 2. Почему `localhost` не ведёт к API из test container?

Внутри container `localhost` означает этот же container. Для другого Compose service используется его service name.

### 3. Как CI узнаёт, что tests упали?

По ненулевому exit code основного test process в container.

### 4. Почему reports могут исчезнуть?

Если они записаны только во временный container layer, удаление container уничтожит их. Нужен mount, volume или copy.

### 5. Почему `depends_on` не всегда достаточно?

Запущенный process может быть ещё не готов принимать запросы. Нужен health check или отдельное ожидание readiness.

### 6. Чем опасен tag `latest`?

Он может указывать на разные image builds в разные моменты и снижает воспроизводимость.

### 7. Зачем удалять volumes между тестами?

Чтобы предыдущие данные не влияли на новый run. Но перед удалением нужно сохранить нужную диагностику.

### 8. Что проверить при внезапной остановке container?

Status, exit code, logs, command, environment, health, mounts, limits и image architecture.

## What To Review Later

- Dockerfile syntax;
- Compose profiles и multiple files;
- Testcontainers;
- image scanning и SBOM;
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
