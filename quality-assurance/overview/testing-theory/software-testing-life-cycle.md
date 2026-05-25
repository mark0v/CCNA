# Software Testing Life Cycle (STLC)

## Summary

Software Testing Life Cycle, или STLC, - это structured process тестирования software, который помогает команде системно проверять качество продукта.

STLC обычно включает шесть основных фаз: requirement analysis, test planning, test case development, test environment setup, test execution и test cycle closure. В отличие от хаотичного ad-hoc testing, STLC задает понятную последовательность действий, deliverables, entry criteria и exit criteria для каждого этапа.

Главная идея STLC: тестирование должно быть управляемым процессом, а не набором случайных проверок в конце разработки.

## Key Points

- STLC фокусируется именно на testing activities внутри более широкого SDLC.
- Каждая фаза STLC имеет свои цели, активности и deliverables.
- Requirement Traceability Matrix, или RTM, помогает связать requirements с test cases.
- Entry и exit criteria работают как quality gates между фазами.
- STLC улучшает test coverage, коммуникацию между QA/dev/business и прозрачность качества.
- В Agile, CI/CD и DevOps STLC не исчезает, а становится более iterative и continuous.

## Notes

### STLC vs SDLC

SDLC, или Software Development Life Cycle, описывает весь жизненный цикл создания software: requirements, design, development, testing, deployment и maintenance.

STLC - это часть этого процесса, сфокусированная на testing. Он отвечает на вопросы:

- что нужно протестировать;
- как это тестировать;
- где и какими данными тестировать;
- кто выполняет testing activities;
- какие defects найдены;
- можно ли завершать testing cycle.

В Waterfall STLC может выглядеть более последовательным. В V-Model STLC хорошо отражает development phases: requirements связаны с acceptance testing, system design - с system testing, architecture - с integration testing, module design - с unit testing.

В Agile STLC выполняется итеративно внутри sprint. QA не ждет конца разработки, а участвует в уточнении requirements, acceptance criteria, тестировании increments и regression.

### 1. Requirement Analysis

Requirement Analysis - первая и очень важная фаза STLC.

QA team изучает requirements с точки зрения testability. Цель - понять, что можно проверить, какие условия должны быть покрыты тестами, где есть ambiguity, conflicts или missing details.

Key activities:

- анализ functional и non-functional requirements;
- уточнение требований с business analysts, product owners, developers и stakeholders;
- выявление test conditions;
- определение приоритетов тестирования;
- подготовка RTM;
- фиксация environment, security и data needs.

Deliverables:

- Requirement Traceability Matrix;
- список вопросов по требованиям;
- feasibility notes;
- уточненные testable requirements.

Эта фаза помогает избежать ситуации, когда команда пишет test cases на основе непонятных или противоречивых требований.

### 2. Test Planning

Test Planning определяет стратегию тестирования.

На этом этапе QA lead или senior QA описывает scope, objectives, risks, resources, schedule, tools, test approach и deliverables. Test Plan становится blueprint для всего testing cycle.

Key activities:

- определение test scope;
- выбор manual, automation или mixed approach;
- оценка усилий;
- планирование ресурсов и ролей;
- выбор tools и frameworks;
- определение risks, dependencies и assumptions;
- согласование entry/exit criteria.

Deliverables:

- approved Test Plan;
- test strategy;
- effort estimation;
- schedule и milestones.

Хороший test plan помогает заранее увидеть ограничения: нехватку environment, отсутствие test data, слабые требования или риски по срокам.

### 3. Test Case Development

Test Case Development превращает план в конкретные проверки.

QA team создает test cases, checklists, test scripts, test data и automation scripts, если automation применима. Каждый test case должен иметь понятные preconditions, steps, expected result и test data.

Key activities:

- написание test cases;
- подготовка test data;
- review test cases;
- создание automation scripts для стабильных и повторяемых сценариев;
- обновление RTM;
- удаление дубликатов и уточнение coverage.

Deliverables:

- reviewed test cases;
- test scripts;
- test data;
- updated RTM.

Peer review на этой фазе особенно важен: он помогает найти пропущенные scenarios еще до начала execution.

### 4. Test Environment Setup

Test Environment Setup - подготовка условий, в которых будет выполняться тестирование.

Environment может включать hardware, OS, browser versions, mobile devices, databases, application servers, network settings, integrations, credentials и test data.

Key activities:

- определение required hardware/software/network configuration;
- установка application build;
- настройка databases и services;
- подготовка test accounts и test data;
- проверка integrations;
- smoke testing environment readiness.

Deliverables:

- environment setup checklist;
- smoke test results;
- ready test environment.

Эта фаза может идти параллельно test case development. Главное - не начинать полноценное execution, пока environment нестабилен.

### 5. Test Execution

Test Execution - фаза, где testers запускают подготовленные test cases на готовом build в подготовленном environment.

Результаты фиксируются как pass, fail, blocked или skipped. Если actual result отличается от expected result, QA заводит defect с severity, priority, steps to reproduce, environment details, logs, screenshots или video.

Key activities:

- выполнение planned tests;
- запуск manual и automated tests;
- defect reporting;
- retesting fixed defects;
- regression testing;
- обновление RTM и test execution status.

Common execution cycles:

- sanity testing;
- smoke testing;
- functional testing;
- re-testing;
- regression testing.

Deliverables:

- test execution logs;
- defect reports;
- updated RTM;
- test status report.

Эта фаза показывает, соответствует ли software требованиям и бизнес-ожиданиям.

### 6. Test Cycle Closure

Test Cycle Closure закрывает testing cycle и превращает опыт команды в полезные выводы.

QA team анализирует результаты, собирает metrics, готовит final reports и фиксирует lessons learned.

Key activities:

- подготовка test summary report;
- анализ defect trends;
- проверка exit criteria;
- retrospective;
- архивирование test artifacts;
- формирование recommendations для следующих cycles.

Deliverables:

- test closure report;
- quality metrics dashboard;
- lessons learned;
- archived artifacts.

Эта фаза важна не только для отчетности. Она помогает улучшить будущие testing cycles.

## Entry and Exit Criteria

Entry criteria - это условия, которые должны быть выполнены перед началом фазы.

Exit criteria - это условия, которые должны быть выполнены перед завершением фазы.

Они работают как quality gates. Команда не должна переходить дальше, если входные данные не готовы или результаты фазы не проверены.

| STLC Phase | Entry Criteria | Exit Criteria |
| --- | --- | --- |
| Requirement Analysis | Requirements доступны, business specifications согласованы | RTM создана, test strategy определена |
| Test Planning | Requirements analysis завершен | Test plan approved, resources allocated |
| Test Case Development | Test plan approved, requirements понятны | Test cases reviewed, test data prepared |
| Test Environment Setup | Environment requirements определены | Environment ready, smoke testing passed |
| Test Execution | Test cases ready, build deployed, environment stable | Test cases executed, critical defects resolved |
| Test Closure | Test execution complete, exit criteria met | Closure report signed off, artifacts archived |

### Automation in STLC

Automation может появляться уже на requirement analysis и planning phases, когда команда оценивает, какие проверки имеют смысл автоматизировать.

Лучшие кандидаты для automation:

- regression tests;
- smoke tests;
- stable repetitive functional tests;
- tests that run across multiple environments;
- high-value scenarios with frequent execution.

Automation не заменяет STLC. Она усиливает STLC, особенно в test execution и regression cycles.

### STLC in Agile, CI/CD and DevOps

В Agile STLC становится более коротким и повторяемым. Requirement analysis, planning, test design и execution могут происходить внутри каждого sprint.

В CI/CD testing встраивается в pipeline. Automated tests запускаются при code commit, build или deployment. Это позволяет быстрее получать feedback и ловить defects раньше.

В DevOps подходе STLC превращается в continuous testing: качество проверяется на протяжении всего delivery process, а не только перед release.

### Metrics and Quality Reports

STLC становится сильнее, когда команда собирает metrics.

Useful metrics:

- test execution rate;
- pass/fail ratio;
- defect density;
- defect severity distribution;
- defect resolution time;
- test coverage;
- requirement coverage;
- escaped defects;
- automation coverage.

Quality dashboard помогает stakeholders видеть реальное состояние testing progress и release readiness.

### Common Pitfalls and Best Practices

#### Testing Starts Too Late

Если QA подключается только после разработки, defects становятся дороже.

Best practice: shift-left testing. QA участвует в requirements и design discussions.

#### Unclear Requirements

Непонятные requirements приводят к неправильным test cases.

Best practice: задавать вопросы рано, использовать RTM и review acceptance criteria.

#### Weak Test Data

Без корректных test data часть scenarios невозможно проверить.

Best practice: планировать test data на этапе test case development.

#### Poor Communication

Разрывы между QA, dev и business создают coverage gaps.

Best practice: использовать общие tools, регулярные syncs и прозрачные defect reports.

#### Automation Without Strategy

Автоматизация всего подряд может стать дорогой и хрупкой.

Best practice: автоматизировать стабильные, повторяемые и бизнес-важные checks.

## Commands / Terms

- `STLC` - Software Testing Life Cycle.
- `SDLC` - Software Development Life Cycle.
- `RTM` - Requirement Traceability Matrix.
- `Entry Criteria` - условия для начала фазы.
- `Exit Criteria` - условия для завершения фазы.
- `Test Plan` - документ со стратегией, scope, resources, risks и schedule.
- `Test Case` - конкретная проверка с steps и expected result.
- `Test Environment` - окружение для выполнения тестов.
- `Test Execution` - запуск тестов и фиксация результатов.
- `Test Closure Report` - итоговый отчет по testing cycle.
- `Shift-left testing` - раннее подключение QA к требованиям и дизайну.
- `Continuous testing` - тестирование, встроенное в delivery pipeline.

## Questions

1. What is STLC?
2. How is STLC different from SDLC?
3. What are the main phases of STLC?
4. Why is requirement analysis important for QA?
5. What is RTM and why is it useful?
6. What is the difference between entry criteria and exit criteria?
7. What deliverables are created during test planning?
8. What happens during test execution?
9. Why is test cycle closure important?
10. How does STLC change in Agile or CI/CD?

## What To Review Later

- STLC phases and deliverables
- Entry vs exit criteria
- RTM and requirement coverage
- Test Plan structure
- Defect lifecycle
- Test closure report
- STLC in Agile and CI/CD
