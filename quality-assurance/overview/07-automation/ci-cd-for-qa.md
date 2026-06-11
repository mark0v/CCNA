# CI/CD для QA: pipeline, проверки и quality gates

Source: user-provided Red Hat article "What is CI/CD?", expanded for practical QA work
Date added: 2026-06-11
Related plan item: Automation
Tags: QA, automation, CI/CD, pipeline, continuous integration, continuous delivery, continuous deployment
Language: Russian
Translation pair: quality-assurance-en/overview/07-automation/ci-cd-for-qa.md

## Summary

CI/CD — набор практик, которые помогают часто интегрировать, проверять и доставлять небольшие изменения.

Аббревиатура включает:

- **Continuous Integration (CI)** — частое объединение изменений с автоматической сборкой и проверками;
- **Continuous Delivery** — приложение после pipeline готово к production, но финальный запуск deployment обычно требует решения человека;
- **Continuous Deployment** — каждое изменение, прошедшее pipeline, автоматически попадает в production.

Для QA pipeline — это не просто место запуска автотестов. Это система быстрого feedback, которая должна:

- обнаруживать дефекты как можно раньше;
- давать понятную причину падения;
- сохранять evidence;
- блокировать опасный release;
- не задерживать команду ненадёжными или избыточными проверками.

## Key Points

- Continuous Delivery и Continuous Deployment — разные процессы.
- Хороший CI начинается с небольших и часто интегрируемых изменений.
- Проверки располагают от быстрых и дешёвых к медленным и дорогим.
- Не каждый test должен блокировать merge или deployment.
- Quality gate должен иметь измеримый критерий и владельца.
- Flaky test снижает доверие ко всему pipeline.
- Build artifact следует создать один раз и продвигать между environments без пересборки.
- Pipeline обязан сохранять logs, reports и другие diagnostic artifacts.
- Production deployment требует monitoring, rollback и понятной ответственности.
- Secrets, third-party dependencies и runner permissions являются частью CI/CD security.

## CI, Delivery и Deployment

| Практика | Главная цель | Что происходит с production |
| --- | --- | --- |
| Continuous Integration | Часто объединять и автоматически проверять code changes | Deployment не обязателен |
| Continuous Delivery | Всегда иметь проверенный release candidate | Обычно есть manual approval |
| Continuous Deployment | Автоматически выпускать каждое прошедшее изменение | Deployment выполняется автоматически |

Удобные вопросы:

```text
CI: изменение корректно интегрируется?
Continuous Delivery: его можно безопасно выпустить сейчас?
Continuous Deployment: pipeline может безопасно выпустить его сам?
```

Слово `CD` неоднозначно. В документации и разговоре нужно уточнять, означает ли оно delivery или deployment.

## Типичный CI/CD pipeline

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

Реальный pipeline зависит от продукта. Mobile application, backend service, web frontend и infrastructure repository требуют разных stages.

## Что запускается на разных этапах

### До commit или push

- formatter;
- lint;
- unit tests затронутого модуля;
- проверка secrets;
- быстрые локальные checks.

Цель — не отправлять очевидно сломанные изменения.

### На Pull Request

- compilation или build;
- unit tests;
- component и API tests;
- static analysis;
- dependency и security scans;
- короткий smoke;
- проверка миграций и контрактов;
- test selection по затронутым областям.

Feedback должен приходить достаточно быстро, чтобы разработчик не переключался на другую задачу.

### После merge

- полный integration suite;
- расширенная regression;
- сборка release artifact;
- публикация image или package;
- deployment в test environment;
- более дорогие проверки.

### Перед production

- smoke на staging;
- критичные E2E scenarios;
- compatibility checks;
- миграции базы данных;
- configuration validation;
- performance baseline или короткий threshold test;
- security и compliance gates;
- release approval, если используется Continuous Delivery.

### После deployment

- health checks;
- production smoke;
- synthetic monitoring;
- logs и error rate;
- latency и saturation;
- business metrics;
- автоматический или ручной rollback при нарушении критериев.

## Test pyramid в pipeline

Быстрые проверки должны составлять основу:

```text
         E2E / UI
      Integration / API
    Unit / component / static
```

Причины:

- unit и component tests быстро локализуют дефект;
- API tests обычно стабильнее и быстрее UI tests;
- E2E нужны для критичных пользовательских flows, но они медленнее и чувствительнее к environment;
- полный UI regression на каждый commit может сделать CI непригодным.

Pipeline — не место, куда без отбора складывают все тесты. Набор зависит от trigger, риска и требуемой скорости feedback.

## Quality gates

Quality gate — автоматическое или ручное условие, без выполнения которого изменение не двигается дальше.

Примеры:

| Gate | Возможный критерий |
| --- | --- |
| Build | Сборка завершилась без ошибки |
| Unit tests | Нет failed tests |
| API contract | Нет breaking changes без одобрения |
| Security scan | Нет новых critical vulnerabilities |
| Coverage | Не упало ниже согласованного порога |
| Smoke | Все critical scenarios прошли |
| Performance | p95 и error rate не превышают budget |
| Manual approval | Release owner подтвердил production deployment |

Плохой gate:

```text
Quality must be good.
```

Хороший gate:

```text
Все P0 smoke tests прошли, новых Critical/High security findings нет,
error rate в threshold test <= 1%.
```

У gate должны быть:

- понятный критерий;
- владелец;
- процедура исключения;
- срок действия waiver;
- evidence;
- правило эскалации.

## Blocking и non-blocking checks

Не каждая проверка должна останавливать pipeline.

**Blocking:**

- build failure;
- unit or smoke failure;
- критичная vulnerability;
- несовместимая database migration;
- нарушение обязательного contract;
- отсутствие обязательного approval.

**Non-blocking:**

- экспериментальная проверка;
- известный flaky test;
- informational scan;
- долгий trend analysis;
- тест, для которого ещё не согласован threshold.

Non-blocking failure всё равно должен быть видимым и иметь владельца. Иначе pipeline создаёт шум, который команда перестаёт замечать.

## Роль QA

QA помогает:

- выбрать tests для каждого stage;
- определить quality gates;
- установить pass/fail criteria;
- проектировать test data;
- поддерживать независимость tests;
- анализировать failed jobs;
- уменьшать flaky tests;
- проверять environment и configuration;
- сохранять диагностические artifacts;
- оценивать release risk;
- проектировать post-deploy validation;
- улучшать скорость и доверие к pipeline.

QA не обязан единолично владеть всеми tests. Качество pipeline — общая ответственность developers, QA, security, operations и product stakeholders.

## Как разбирать failed pipeline

1. Определить первый реально упавший job, а не последний красный stage.
2. Проверить commit, branch, trigger и environment.
3. Открыть полный log и test report.
4. Найти, воспроизводится ли ошибка повторно.
5. Отделить product defect от test defect и infrastructure failure.
6. Сопоставить падение с недавним изменением.
7. Проверить screenshots, traces, dumps и service logs.
8. Не перезапускать job вслепую до потери evidence.
9. Зафиксировать root cause и владельца исправления.
10. Если проблема системная, улучшить pipeline или observability.

### Классификация падений

| Категория | Пример |
| --- | --- |
| Product defect | API возвращает неправильный status code |
| Test defect | Неверный locator или assertion |
| Flaky test | Результат меняется без изменения продукта |
| Environment | Service, database или browser недоступен |
| Test data | Данные уже использованы или имеют неверное состояние |
| Configuration | Не задана переменная или выбран неправильный endpoint |
| Infrastructure | Runner потерял сеть или disk space |

Простой retry может скрыть причину. Retry допустим как контролируемая техника, но не как замена расследованию.

## Artifacts и отчётность

Полезные pipeline artifacts:

- unit, API и UI test reports;
- screenshots;
- browser traces и videos;
- application и service logs;
- network logs;
- crash dumps;
- coverage reports;
- security scan results;
- performance results;
- deployment manifest;
- build metadata;
- ссылки на image digest или package version.

Artifacts должны:

- открываться после завершения job;
- иметь разумный retention;
- не содержать secrets и персональные данные;
- быть связаны с commit и build;
- помогать воспроизвести проблему.

## Build once, deploy many

Надёжный подход:

```text
Source commit -> build artifact -> test -> staging -> production
```

Один и тот же immutable artifact продвигается между environments.

Если для production приложение пересобирается заново, результат может отличаться от проверенного artifact из staging из-за:

- новой dependency;
- изменившегося base image;
- другой build configuration;
- нестабильного external repository;
- различий toolchain.

Environment-specific значения передаются через configuration, а не через изменение artifact.

## Deployment strategies

| Стратегия | Идея | Что проверяет QA |
| --- | --- | --- |
| Rolling | Instances обновляются постепенно | Смешанные версии и совместимость |
| Blue-green | Новый environment готовится рядом со старым | Переключение traffic и rollback |
| Canary | Новая версия получает небольшую долю traffic | Метрики canary и критерии расширения |
| Feature flags | Код deployed, feature скрыта или включается отдельно | Состояния flag и комбинации пользователей |

Continuous Deployment без monitoring и rollback — это просто автоматизированный риск.

## CI/CD security

Основные риски:

- secrets в repository, logs или artifacts;
- чрезмерные permissions у runner;
- запуск недоверенного code с production credentials;
- уязвимые third-party actions, plugins и dependencies;
- подмена build artifact;
- незащищённый branch или environment;
- неограниченный доступ к deployment;
- утечка данных из test environment.

Практики:

- хранить secrets в secret manager;
- выдавать минимальные permissions;
- разделять build и production deployment credentials;
- защищать branches и environments;
- фиксировать версии third-party actions;
- сканировать dependencies, images и source code;
- подписывать или проверять provenance artifacts;
- вести audit log;
- регулярно обновлять runners и plugins;
- не выводить чувствительные значения в logs.

## Метрики pipeline

Полезно отслеживать:

- pipeline duration;
- queue time;
- success rate;
- flaky test rate;
- mean time to repair a broken pipeline;
- deployment frequency;
- lead time for changes;
- change failure rate;
- time to restore service.

Метрики нужны для улучшения процесса, а не для наказания команды. Например, сокращение duration за счёт удаления нужных tests ухудшит качество, хотя график станет красивее.

## Частые ошибки

- CI запускается редко;
- main branch долго остаётся красной;
- pipeline занимает часы без risk-based selection;
- flaky tests просто перезапускают;
- test reports и logs не сохраняются;
- staging сильно отличается от production;
- один test зависит от результата другого;
- test data не изолированы;
- secrets попадают в logs;
- deployment выполняется без rollback plan;
- все checks являются blocking;
- никто не владеет failed job;
- production считается успешным только потому, что deployment command завершился.

## Практический чек-лист QA

- [ ] Понятны triggers каждого pipeline.
- [ ] Для stages определены владельцы.
- [ ] Быстрые проверки выполняются раньше дорогих.
- [ ] Blocking gates имеют измеримые criteria.
- [ ] Smoke покрывает критичные flows.
- [ ] Flaky tests отслеживаются отдельно.
- [ ] Reports и diagnostic artifacts сохраняются.
- [ ] Test data изолированы и воспроизводимы.
- [ ] Проверяется именно тот artifact, который будет deployed.
- [ ] Secrets не появляются в code, logs и artifacts.
- [ ] Staging достаточно близок к production.
- [ ] Есть post-deploy checks.
- [ ] Monitoring связан с release version.
- [ ] Rollback проверен и имеет владельца.

## Questions

### 1. Чем Continuous Delivery отличается от Continuous Deployment?

В Continuous Delivery система всегда готова к release, но production deployment обычно запускается после ручного решения. В Continuous Deployment каждое прошедшее изменение выпускается автоматически.

### 2. Почему быстрые tests нужно запускать раньше?

Они быстрее дают feedback и дешевле останавливают заведомо плохое изменение до запуска дорогих environments и E2E suites.

### 3. Что такое quality gate?

Это измеримое условие, которое должно быть выполнено для перехода к следующему stage, merge или deployment.

### 4. Должны ли все tests блокировать pipeline?

Нет. Blocking status зависит от риска, надёжности теста и назначения pipeline. Но non-blocking failures должны оставаться видимыми.

### 5. Почему нельзя просто перезапустить упавший test?

Без анализа retry может скрыть product defect, flaky behavior или проблему environment и уничтожить полезный evidence.

### 6. Что означает build once, deploy many?

Один immutable artifact проходит проверки и продвигается между environments без повторной сборки.

### 7. Что QA проверяет после production deployment?

Health, critical smoke, logs, error rate, latency, business metrics и условия rollback.

### 8. Какие угрозы есть в CI/CD?

Утечка secrets, опасные permissions, уязвимые dependencies, подмена artifacts, незащищённые branches и запуск недоверенного code с production access.

## What To Review Later

- GitHub Actions, GitLab CI или Jenkins syntax;
- pipeline as code;
- container registries и image digests;
- test parallelization;
- contract testing;
- feature flags;
- blue-green и canary deployment;
- rollback и database migration strategy;
- supply chain security;
- DORA metrics.

## Sources

- User-provided Red Hat article: "What is CI/CD?"
- [Red Hat: What is CI/CD?](https://www.redhat.com/en/topics/devops/what-is-ci-cd)
