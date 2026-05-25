# V-Model

## Summary

V-Model - это модель разработки и тестирования ПО, в которой каждой фазе разработки соответствует своя фаза тестирования. Ее также называют **Verification and Validation model**.

Модель выглядит как буква `V`: левая сторона описывает анализ и проектирование, нижняя точка - coding, правая сторона - уровни тестирования. Главная идея V-Model в том, что тестирование планируется рано, а не начинается только после завершения разработки.

## Key Points

- V-Model расширяет Waterfall и уменьшает риск позднего обнаружения дефектов.
- Каждая development phase имеет соответствующую testing phase.
- Требования связываются с тестами через traceability.
- Тестирование планируется уже на ранних этапах.
- Модель хорошо подходит для стабильных требований, compliance и safety-critical систем.
- V-Model менее гибкая, чем Agile, и плохо переносит частые изменения требований.

## Notes

### Что такое V-Model

V-Model - это structured software development methodology, где разработка и тестирование связаны напрямую.

В Waterfall testing обычно появляется поздно, после реализации. V-Model исправляет эту слабость: тестовые активности планируются параллельно с анализом требований и design. Это помогает находить дефекты раньше и лучше понимать, как именно будет проверяться каждая часть системы.

### Почему V-Model появился после Waterfall

Главная проблема Waterfall - late testing. Если ошибка в требованиях или design обнаруживается только после coding, исправление становится дорогим.

Типичные проблемы Waterfall:

- дефекты обнаруживаются слишком поздно;
- требования не валидируются достаточно рано;
- стоимость исправления растет к концу lifecycle;
- продукт может не совпасть с ожиданиями пользователей.

V-Model снижает эти риски, потому что каждая стадия разработки заранее связывается с проверкой.

### Verification и Validation

**Verification** отвечает на вопрос: "Мы строим продукт правильно?"  
Это проверка требований, design-документов, архитектуры, модулей и соответствия стандартам.

**Validation** отвечает на вопрос: "Мы строим правильный продукт?"  
Это проверка работающего software против требований, ожиданий пользователей и бизнес-целей.

### Левая сторона V: Verification Phase

#### 1. Business Requirement Analysis

На этом этапе команда собирает и документирует functional и non-functional requirements.

Business analysts и stakeholders уточняют ожидания, ограничения, бизнес-цели и критерии приемки. Для QA это важная точка входа: уже здесь можно искать ambiguity, missing requirements и противоречия.

#### 2. System Design

System Design переводит требования в high-level technical solution.

Архитекторы определяют общую структуру системы: software components, hardware requirements, network infrastructure, integrations и deployment-подход.

#### 3. Architectural Design / High-Level Design

Architectural Design, или HLD, разбивает систему на крупные модули и компоненты.

На этом уровне определяются основные patterns, frameworks, interfaces и взаимодействия между частями приложения.

#### 4. Module Design / Low-Level Design

Module Design, или LLD, описывает детали отдельных компонентов.

Здесь фиксируются algorithms, data flow, database design, API specifications и логика модулей. На этом же уровне можно заранее проектировать unit test cases.

#### 5. Coding

Coding находится в нижней точке V.

Developers реализуют модули по design-документам, coding standards и best practices. Code reviews, static analysis и continuous integration помогают контролировать качество еще до полноценного testing.

### Правая сторона V: Validation Phase

#### 1. Unit Testing

Unit Testing проверяет отдельные modules или components изолированно.

Этот уровень связан с Module Design. Цель - убедиться, что каждая маленькая часть системы работает корректно сама по себе.

#### 2. Integration Testing

Integration Testing проверяет взаимодействие между модулями.

Этот уровень связан с Architectural Design. QA и developers проверяют interfaces, API calls, data flow, database interactions и message passing.

#### 3. System Testing

System Testing проверяет всю интегрированную систему.

Этот уровень связан с System Design. Проверяются functional и non-functional requirements: performance, security, usability, compatibility и общая стабильность.

#### 4. User Acceptance Testing

UAT проверяет, готова ли система для business use.

Этот уровень связан с Business Requirement Analysis. Customer или business users проверяют реальные workflows, business scenarios и соответствие ожиданиям.

### Соответствие фаз

В V-Model каждая development phase имеет зеркальную testing phase:

- **Requirements** ↔ **Acceptance Testing**
- **System Design** ↔ **System Testing**
- **Architecture Design** ↔ **Integration Testing**
- **Module Design** ↔ **Unit Testing**

Это дает traceability: можно увидеть, каким тестом покрывается каждое требование или design-решение.

### Принципы V-Model

**Large to Small** - требования постепенно уточняются от высокого уровня к деталям, а тестирование идет в обратном направлении: от unit к acceptance.

**Traceability** - каждое требование должно быть связано с test cases.

**Early Testing** - testing activities начинаются до coding.

**Documentation Focus** - каждая стадия создает документы и artifacts для review.

**Scalability** - модель может использоваться в маленьких и больших проектах, если requirements стабильны.

### Advantages

- помогает находить дефекты раньше;
- снижает стоимость исправлений;
- дает четкую связь между requirements и tests;
- улучшает коммуникацию между developers, testers и stakeholders;
- хорошо подходит для compliance-heavy проектов;
- удобна для safety-critical систем.

### Disadvantages

- rigid and inflexible;
- изменения после старта процесса стоят дорого;
- плохо подходит для сложных и iterative проектов;
- требует стабильных требований;
- много документации и planning overhead;
- менее адаптивна, чем Agile.

### V-Model vs Agile

V-Model делает акцент на строгих фазах, documentation, verification и validation. Agile делает акцент на итерациях, быстрой обратной связи и изменяемых требованиях.

V-Model лучше подходит, когда требования стабильны, compliance обязателен, а цена ошибки высокая. Agile лучше подходит, когда продукт активно меняется, нужна частая customer collaboration и быстрые releases.

На практике команды иногда смешивают подходы: сохраняют traceability и formal testing из V-Model, но используют automation, CI и короткие feedback loops из Agile/DevOps.

### Где V-Model используется

V-Model часто встречается там, где важны надежность, документация и контроль качества:

- healthcare software;
- banking and finance systems;
- aviation and aerospace;
- automotive embedded systems;
- safety-critical systems;
- regulated enterprise applications.

## Commands / Terms

- **V-Model** - модель разработки, где каждой фазе разработки соответствует фаза тестирования.
- **Verification** - проверка, что продукт строится правильно.
- **Validation** - проверка, что строится правильный продукт.
- **Traceability** - связь требований с test cases.
- **Unit Testing** - проверка отдельных модулей.
- **Integration Testing** - проверка взаимодействия модулей.
- **System Testing** - проверка всей системы.
- **UAT (User Acceptance Testing)** - приемочное тестирование пользователями или заказчиком.
- **HLD (High-Level Design)** - высокоуровневый дизайн.
- **LLD (Low-Level Design)** - детальный дизайн модуля.

## Questions

**1. Почему V-Model называют Verification and Validation model?**  
Потому что левая сторона модели фокусируется на verification, а правая - на validation через соответствующие уровни тестирования.

**2. Какую проблему Waterfall решает V-Model?**  
Он уменьшает риск позднего тестирования, потому что тесты планируются уже на этапах requirements и design.

**3. Какие пары фаз есть в V-Model?**  
Requirements ↔ Acceptance Testing, System Design ↔ System Testing, Architecture Design ↔ Integration Testing, Module Design ↔ Unit Testing.

**4. Когда V-Model подходит лучше всего?**  
Когда требования стабильны, проект регулируемый, нужна документация, traceability и высокая надежность.

**5. Почему V-Model плохо подходит для быстро меняющихся проектов?**  
Потому что модель жесткая: изменения требований после начала процесса приводят к дорогим переделкам документов, design и test cases.

## What To Review Later

- Difference between verification and validation.
- V-Model vs Waterfall.
- V-Model vs Agile.
- Traceability matrix.
- Test levels: unit, integration, system, acceptance.
- Role of QA during requirements review.
