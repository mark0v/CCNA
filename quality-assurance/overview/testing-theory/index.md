# 📖 01 — Теория тестирования

> **Твой уровень:** 🟡 Частично (есть базовые знания, но несколько критических пробелов)  
> **Приоритет:** ⭐⭐⭐ ВЫСОКИЙ — основа для всего остального

---

## 1.1 Методологии разработки ПО
**Твой уровень:** 🟡 Familiar with

### Темы
- **Waterfall** — фазы, плюсы/минусы, роль QA
- **V-Model** — параллельность разработки и тестирования
- **XP (Extreme Programming)** — TDD, парное программирование
- **Agile: Scrum** — Спринты, церемонии, роль QA в команде
- **Agile: Kanban** — Доска, WIP лимиты, Flow
- **Scrum vs Kanban** — когда что применять

### Ресурсы
- 🔗 [Classical Waterfall Model](https://www.geeksforgeeks.org/software-engineering-classical-waterfall-model/)
- 🔗 [V-Model Testing](https://www.guru99.com/v-model-software-testing.html)
- 🔗 [Agile / Scrum (Atlassian)](https://www.atlassian.com/agile/scrum)
- 🔗 [Agile / Kanban (Atlassian)](https://www.atlassian.com/agile/kanban)
- 🔗 [XP (Agile Alliance)](https://www.agilealliance.org/glossary/xp/)

---

## 1.2 Терминология и базовые понятия
**Твой уровень:** 🟡 Familiar with / Able to

### Темы
- **QA vs QC vs Tester** — разница в ролях и ответственности
- **SDLC фазы** — Planning, Analysis, Design, Development, Testing, Deployment, Maintenance
- **STLC фазы** — Requirements, Planning, Analysis, Design, Execution, Closure
- **Error / Defect / Failure** — разница и примеры
- **Verification vs Validation** — "Build the right product" vs "Build the product right"
- **Priority vs Severity** — матрица, примеры HIGH/LOW комбинаций
- **7 принципов тестирования** — уметь объяснить каждый с примером

### Ресурсы
- 🔗 [QA vs QC vs Tester](https://testmatick.com/ru/v-chem-raznitsa-mezhdu-qa-i-qc/)
- 🔗 [STLC Guide](https://www.guru99.com/software-testing-life-cycle.html)
- 🔗 [Error vs Defect vs Failure](http://okiseleva.blogspot.com/2015/05/blog-post_29.html)
- 🔗 [Priority vs Severity](https://www.guru99.com/defect-severity-in-software-testing.html)
- 🔗 [7 Principles of Testing](https://tryqa.com/what-are-the-principles-of-testing/)
- 🔗 [Verification vs Validation](https://training.qatestlab.com/blog/technical-articles/verification-validation-testing)

---

## 1.3 Уровни тестирования
**Твой уровень:** 🟡 Familiar with (теория есть, практики мало)

### Темы
- **Unit / Component Testing** — тестирование изолированного модуля
- **Integration Testing** — стратегии: Big Bang, Top-Down, Bottom-Up, Sandwich
- **System Testing** — тестирование всей системы целиком
- **Acceptance Testing (UAT)** — виды: Alpha, Beta, Contract, Regulation
- **Разница System vs Integration** — когда и что тестируем

### Ресурсы
- 🔗 [Levels of Testing](https://software-testing.org/testing/urovni-testirovaniya-testing-levels-v-testirovanii-po.html)
- 🔗 [Integration Testing](https://tryqa.com/what-is-integration-testing/)
- 🔗 [System Testing](https://tryqa.com/what-is-system-testing/)
- 🔗 [Acceptance Testing](https://tryqa.com/what-is-acceptance-testing/)
- 🔗 [System vs Integration](https://u-tor.com/topic/system-vs-integration)

---

## 1.4 Виды тестирования
**Твой уровень:** 🟡 Functional — Able to; Non-Functional — Familiar with

### Функциональное тестирование
- Smoke Testing — быстрая проверка работоспособности
- Sanity Testing — проверка конкретной фичи после фикса
- Regression Testing — не сломали ли старое
- Re-testing — проверка закрытого дефекта
- UI Testing — проверка интерфейса

### 🔴 Нефункциональное тестирование (ПРОБЕЛ)
- **Performance** — Load, Stress, Stability (подробно — в файле 06)
- **Usability** — удобство использования
- **Security** — базовые понятия
- **Compatibility / Configuration** — разные среды

### 🔴 Статическое vs Динамическое (ПРОБЕЛ)
- **Static Testing** — review, walkthrough, inspection (без запуска кода)
- **Dynamic Testing** — запуск и проверка в работе
- Чем отличаются, примеры каждого

### Ресурсы
- 🔗 [Smoke vs Sanity](https://www.guru99.com/smoke-sanity-testing.html)
- 🔗 [Regression Testing](https://tryqa.com/what-is-regression-testing-in-software/)
- 🔗 [Functional Testing](https://www.browserstack.com/guide/functional-testing)
- 🔗 [Static vs Dynamic](https://www.guru99.com/static-dynamic-testing.html)
- 🔗 [Static Testing Uses](https://tryqa.com/what-are-the-uses-of-static-testing)
- 🔗 [Non-Functional Types](http://www.protesting.ru/testing/testtypes.html)

---

## 1.5 Техники тест-дизайна
**Твой уровень:** 🟡 EP/BVA — Able to; остальные 🔴 ПРОБЕЛ

### Уже знаешь
- ✅ **Equivalence Partitioning** — деление на классы эквивалентности
- ✅ **Boundary Value Analysis** — граничные значения
- ✅ **Error Guessing** — опыт + интуиция
- ✅ **Exploratory Testing** — исследовательское без скриптов

### 🔴 Нужно изучить (критические пробелы)
- **Decision Table Testing** — таблицы решений, комбинации условий
- **State Transition Testing** — диаграммы состояний и переходов
- **Use Case Testing** — тест-кейсы на базе Use Cases
- **Pairwise / Combinatorial Testing** — попарное тестирование, инструмент PICT

### Ресурсы
- 🔗 [Equivalence Partitioning](https://tryqa.com/what-is-equivalence-partitioning-in-software-testing/)
- 🔗 [Boundary Value Analysis](https://tryqa.com/what-is-boundary-value-analysis-in-software-testing)
- 🔗 [Decision Table](https://tryqa.com/what-is-decision-table-in-software-testing/)
- 🔗 [State Transition](https://tryqa.com/what-is-state-transition-testing-in-software-testing)
- 🔗 [Use Case Testing](https://tryqa.com/what-is-use-case-testing-in-software-testing)
- 🔗 [Pairwise Testing](https://training.qatestlab.com/blog/technical-articles/pairwise-testing)
- 🔗 [Experience-Based Techniques](https://toolsqa.com/software-testing/ISTQB/experience-based-testing-technique)

---

## 1.6 Тестовая документация (Test Artifacts)
**Твой уровень:** 🟡 Большинство — Familiar with / Able to

### Знаешь хорошо
- ✅ Checklist — Able to
- ✅ Test Case / Test Suite — Able to
- ✅ Bug Report — Able to

### Требует углубления
- **Test Plan** — разделы IEEE 829, цели, scope, exit criteria
- **Test Strategy** — 🔴 Not Started (из IDP): подходы, уровни, риски
- **Traceability Matrix (RTM)** — построение, связь требований и тест-кейсов
- **Test Report** — метрики, summary, pass/fail статистика
- **Release Notes** — структура, audience, best practices

### 🔴 Критические пробелы (из IDP — Not Started)
- **Test Coverage** — метрики, виды покрытия, как измерять
- **Risks** — Project Risk vs Product Risk, матрица рисков, risk-based testing
- **Test Impact Analysis** — что тестировать после изменений
- **Metrics** — defect density, pass rate, test coverage %, escape rate
- **UML Diagram** — Use Case, Sequence, Activity — чтение и создание

### Ресурсы
- 🔗 [Test Plan Guide](https://katalon.com/resources-center/blog/test-plan)
- 🔗 [Test Strategy](https://www.guru99.com/how-to-create-test-strategy-document.html)
- 🔗 [Test Coverage](https://en.training.qatestlab.com/blog/technical-articles/test-coverage/)
- 🔗 [Risks in Testing](https://www.guru99.com/risk-based-testing.html)
- 🔗 [Test Impact Analysis](https://www.launchableinc.com/blog/what-is-test-impact-analysis/)
- 🔗 [QA Metrics](https://www.indeed.com/career-advice/career-development/qa-metrics/)
- 🔗 [UML Diagrams](https://www.smartdraw.com/uml-diagram)
- 🔗 [UML Intro (YouTube)](https://www.youtube.com/watch?v=zid-MVo7M-E)
- 🔗 [Traceability Matrix](https://www.wrike.com/blog/what-is-requirements-traceability-matrix/)

---

## 1.7 Управление тестированием (Management)
**Твой уровень:** 🔴 Большинство — ПРОБЕЛ

### 🔴 Нужно изучить
- **Test Estimation Techniques** — широта/глубина, three-point, expert judgment, PERT
- **Planning and Strategy selection** — когда какой подход применять
- **Brainstorming** — техника для генерации тест-идей
- **Test Coverage Evaluation** — как оценить полноту тестирования

### Ресурсы
- 🔗 [Estimation Techniques](https://tryqa.com/what-are-the-estimation-techniques-in-software-testing/)
- 🔗 [Estimation Overview (TutorialsPoint)](https://www.tutorialspoint.com/estimation_techniques/estimation_techniques_overview.htm)
- 🔗 [Brainstorming](https://www.semrush.com/blog/brainstorming/)
- 🔗 [Test Coverage Evaluation](https://tryqa.com/how-we-can-measure-the-coverage)

---

## ✅ Чеклист по разделу

- [ ] Могу объяснить разницу QA/QC/Tester на интервью
- [ ] Знаю все фазы SDLC и STLC с примерами
- [ ] Умею составить Test Plan (структура по IEEE 829)
- [ ] Знаю разницу Test Plan vs Test Strategy
- [ ] Применяю 5+ техник тест-дизайна
- [ ] Умею строить RTM (Traceability Matrix)
- [ ] Знаю ключевые QA метрики
- [ ] Знаю Risk-Based Testing подход
- [ ] Читаю UML диаграммы (Use Case, Sequence, Activity)
