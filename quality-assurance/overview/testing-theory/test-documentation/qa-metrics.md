# QA Metrics

## Summary

QA Metrics - это измеряемые показатели, которые помогают оценивать качество продукта, эффективность тестирования, прогресс команды и уровень рисков.

Метрики помогают отвечать на вопросы:

- насколько хорошо покрыты требования;
- сколько дефектов найдено;
- как быстро команда находит и исправляет bugs;
- насколько стабилен продукт;
- где остаются риски;
- насколько эффективно работает QA process;
- готов ли продукт к release.

Метрики нужны не для красивых отчетов. Они помогают принимать решения.

## Why QA Metrics Matter

QA metrics позволяют команде видеть реальную картину проекта.

Они помогают оценивать:

- бюджет;
- сроки;
- риски;
- test coverage;
- product quality;
- team productivity;
- release readiness;
- reliability of the system.

Без метрик команда часто спорит на уровне ощущений:

- "кажется, тестирование идет нормально";
- "похоже, дефектов много";
- "вроде бы продукт готов".

С метриками разговор становится конкретнее.

## Important Warning

Метрики полезны только тогда, когда они используются правильно.

Плохой подход:

- собирать слишком много метрик;
- измерять ради отчетности;
- использовать метрики для давления на людей;
- сравнивать testers только по количеству найденных дефектов;
- считать одну метрику абсолютной правдой.

Хороший подход:

- выбирать метрики под цель;
- смотреть на trends;
- анализировать причины;
- использовать данные для улучшения процесса;
- сочетать количественные данные с контекстом.

## Test Coverage Metrics

Test Coverage metrics помогают понять, какие части продукта проверены, а какие остаются в зоне риска.

## Requirements Coverage

Requirements Coverage показывает, какой процент требований покрыт test cases.

Formula:

```text
Requirements Coverage =
(Covered requirements / Total requirements) x 100%
```

Example:

```text
Covered requirements: 80
Total requirements: 100

Requirements Coverage = 80%
```

Эта метрика особенно полезна, если requirements достаточно атомарные и хорошо описаны.

## Code Coverage

Code Coverage показывает, какой процент кода был выполнен во время тестирования.

Чаще всего используется в unit testing и automated testing.

Formula:

```text
Code Coverage =
(Executed code lines / Total executable code lines) x 100%
```

Важно: высокий code coverage не гарантирует отсутствие bugs. Он показывает, что код был выполнен, но не всегда показывает, что поведение было проверено правильно.

## Executed Tests

Executed Tests показывает, какая часть запланированных tests была выполнена.

Formula:

```text
Executed Tests =
(Executed tests / Planned tests) x 100%
```

Example:

```text
Executed tests: 90
Planned tests: 120

Executed Tests = 75%
```

Эта метрика помогает понимать прогресс test execution.

## Defects Per Requirement

Defects per Requirement показывает, сколько дефектов найдено в рамках конкретного requirement.

Эта метрика помогает находить:

- сложные требования;
- плохо описанные требования;
- рискованные areas;
- требования, которые требуют дополнительного анализа.

Example:

| Requirement | Defects |
| --- | --- |
| Login | 2 |
| Payment | 9 |
| Reports | 5 |

Если в `Payment` много defects, возможно, эта область сложнее, рискованнее или хуже покрыта design/review process.

## Defect Metrics

Defect metrics помогают анализировать качество продукта и эффективность обнаружения дефектов.

## Defect Density

Defect Density показывает количество дефектов относительно размера продукта или модуля.

Formula example:

```text
Defect Density =
Number of defects / Module size
```

Module size может измеряться по-разному:

- lines of code;
- function points;
- user stories;
- modules;
- requirements.

Эта метрика помогает сравнивать defect concentration между модулями.

## Mean Time To Detect

Mean Time To Detect, or MTTD, показывает среднее время, которое требуется команде, чтобы обнаружить defect.

Example:

```text
MTTD = Average time from defect injection to defect detection
```

Чем ниже MTTD, тем быстрее команда находит проблемы.

## Mean Time To Repair

Mean Time To Repair, or MTTR, показывает среднее время, которое требуется на исправление defect после его обнаружения.

Example:

```text
MTTR = Average time from defect report to fix completion
```

MTTR помогает понимать скорость реакции команды на bugs.

## Defect Injection Rate

Defect Injection Rate показывает, сколько новых дефектов вносится в систему при изменениях кода.

Эта метрика полезна, когда команда хочет понять:

- насколько рискованны changes;
- ухудшается ли качество после fixes;
- появляются ли новые bugs после refactoring;
- насколько стабильна development process.

## Escape Rate

Escape Rate показывает количество дефектов, которые были пропущены в production и найдены пользователями после release.

Formula example:

```text
Escape Rate =
(Production defects / Total defects) x 100%
```

Высокий escape rate может означать:

- слабое test coverage;
- плохую regression strategy;
- недостаточное exploratory testing;
- проблемы с requirements;
- неподходящую test environment;
- слишком быстрый release без контроля рисков.

## Test Effort And Team Metrics

Эти метрики помогают планировать нагрузку, понимать скорость команды и улучшать процесс.

## Number Of Tests Per Time Period

Показывает, сколько tests команда может выполнить за определенный период:

- день;
- неделя;
- sprint;
- release cycle.

Эту метрику можно использовать для планирования test execution.

Важно: количество выполненных tests не равно качеству тестирования.

## Test Design Efficiency

Test Design Efficiency показывает, сколько времени требуется на разработку tests для одного requirement или feature.

Example:

```text
Test Design Efficiency =
Time spent on test design / Number of covered requirements
```

Эта метрика помогает оценивать сложность требований и улучшать planning.

## Distribution Of Discovered Defects

Эта метрика показывает, сколько дефектов найдено разными участниками команды.

Ее можно использовать осторожно для анализа:

- распределения нагрузки;
- зон ответственности;
- необходимости mentoring;
- сложности модулей.

Важно: нельзя оценивать tester только по количеству найденных bugs. Иногда хороший tester предотвращает defects через review, уточнение requirements и улучшение test design.

## Pass Rate

Pass Rate показывает процент успешно пройденных tests.

Formula:

```text
Pass Rate =
(Passed tests / Executed tests) x 100%
```

Example:

```text
Passed tests: 80
Executed tests: 100

Pass Rate = 80%
```

Pass Rate помогает оценить текущую стабильность build, но его нужно анализировать вместе с severity найденных defects.

## Test Economics Metrics

Test economics metrics помогают оценивать стоимость качества и финансовые риски.

## Cost Per Bug Fix

Cost per bug fix показывает стоимость исправления одного defect.

Упрощенно:

```text
Cost per bug fix =
Time spent on fix x Hourly rate
```

Более полный расчет может включать:

- investigation;
- development fix;
- code review;
- retesting;
- regression testing;
- deployment;
- customer support impact.

## Cost Of Not Testing

Cost of not testing показывает потенциальные потери, если testing недостаточно или отсутствует.

Examples:

- потеря клиентов;
- репутационный ущерб;
- production outage;
- emergency hotfix;
- refunds;
- legal or compliance issues;
- снижение revenue;
- рост support requests.

Эта метрика помогает объяснять, почему testing - это не expense without value, а risk reduction activity.

## Automation ROI

Automation ROI показывает, насколько automation оправдывает вложения.

Automation может помочь:

- ускорить regression testing;
- чаще запускать проверки;
- раньше находить defects;
- сократить manual effort;
- повысить стабильность release process.

Но automation тоже имеет стоимость:

- initial development;
- maintenance;
- flaky test fixes;
- infrastructure;
- code review;
- test data management.

Поэтому ROI нужно оценивать на реальных данных, а не просто считать, что automation всегда выгодна.

## Performance Metrics

Technical performance metrics используются в non-functional testing.

## Response Time

Response Time показывает, сколько времени система обрабатывает запрос.

Для web applications часто стремятся к response time менее 2 секунд для ключевых операций, но точный target зависит от продукта и business expectations.

## Throughput

Throughput показывает, сколько операций система обрабатывает за единицу времени.

Examples:

- requests per second;
- transactions per second;
- messages per minute.

Эта метрика важна для load и performance testing.

## Error Rate

Error Rate показывает процент неуспешных запросов.

Formula:

```text
Error Rate =
(Failed requests / Total requests) x 100%
```

Для стабильных production-like scenarios команда часто стремится держать error rate очень низким, например ниже 1%, но target зависит от системы.

## CPU And Memory Usage

CPU и Memory Usage показывают, сколько ресурсов потребляет система.

Они помогают находить:

- bottlenecks;
- memory leaks;
- inefficient algorithms;
- infrastructure limitations;
- degradation under load.

## Mobile Metrics

Для mobile applications могут быть важны специфические метрики.

## Uninstall Rate

Uninstall Rate показывает, как часто пользователи удаляют application.

Высокий uninstall rate может указывать на:

- poor UX;
- crashes;
- annoying notifications;
- low product value;
- performance issues.

## Opt-In Rate

Opt-In Rate показывает процент пользователей, которые согласились получать push notifications.

Эта метрика важна для продуктов, где engagement зависит от notifications.

## Engagement Rate

Engagement Rate показывает активность пользователей после взаимодействия с приложением или notification.

Example:

- number of sessions after push notification;
- average sessions in the first week;
- feature usage after release.

## Metrics In Waterfall And Agile

Выбор метрик зависит от methodology.

## Waterfall

В Waterfall чаще важны:

- requirements coverage;
- test plan progress;
- defect density;
- pass rate;
- exit criteria;
- release readiness;
- cost of quality;
- test summary reports.

Так как scope обычно фиксирован заранее, больше внимания уделяется полному покрытию требований и readiness к release.

## Agile

В Agile чаще важны:

- sprint quality;
- open defects at sprint end;
- escaped defects;
- automation stability;
- regression execution time;
- velocity context;
- cycle time;
- defect trends;
- risk coverage for each increment.

Agile metrics должны помогать команде быстро адаптироваться, а не превращаться в жесткую бюрократию.

## Monitoring Levels

Разные роли смотрят на разные уровни метрик.

## Project Managers

Чаще смотрят на:

- test progress;
- schedule;
- scope;
- risks;
- open defects;
- release readiness.

## QA Leads

Чаще смотрят на:

- test coverage;
- defect trends;
- pass rate;
- automation results;
- test execution progress;
- risk-based coverage.

## Department Leads Or Management

Чаще смотрят на:

- MTTR;
- escape rate;
- cost of quality;
- automation ROI;
- process efficiency;
- long-term quality trends.

## Best Practices

Good practices for QA metrics:

- choose metrics based on goals;
- use a small meaningful set;
- track trends, not only single values;
- combine metrics with context;
- review metrics regularly;
- use metrics to improve process;
- avoid using metrics as a punishment tool;
- explain metrics to stakeholders clearly.

## Common Mistakes

Common mistakes:

- measuring everything;
- focusing only on quantity;
- ignoring business risk;
- comparing testers by bug count;
- treating metrics as absolute truth;
- improving numbers without improving quality;
- collecting metrics nobody uses;
- hiding bad metrics instead of learning from them.

Metrics should help the team think better.

## Key Idea

QA Metrics give visibility into product quality and testing effectiveness.

They help the team understand progress, risks, defects, coverage, and release readiness.

Главная мысль:

> Good metrics do not replace judgment. They improve it.

## Questions

1. What are QA Metrics?
2. What is the difference between Requirements Coverage and Code Coverage?
3. What does Escape Rate show?
4. Why is Automation ROI important?
5. Why should metrics be adapted to the project methodology?

## What To Review Later

- Test Coverage
- Defect Density
- MTTR
- MTTD
- Escape Rate
- Automation ROI
- Performance Metrics
