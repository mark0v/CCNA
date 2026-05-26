# Integration Testing

## Summary

Integration Testing - это уровень тестирования, на котором проверяется взаимодействие между modules, components, services или external systems.

После unit testing отдельные parts продукта могут работать корректно сами по себе, но это не гарантирует, что они правильно работают вместе. Integration testing помогает найти defects на interfaces: неправильные data formats, broken API contracts, ошибки в business flow, проблемы с authentication, payment gateway, database, file system, operating system, hardware или third-party integrations.

Главная идея: проверить не только "работает ли module", а "работают ли modules вместе".

## Key Points

- Integration testing выполняется после unit testing и обычно перед system testing.
- Основной фокус - interfaces и interactions между components.
- Defects часто появляются именно на границах между modules.
- Integration testing может выполняться разными approaches: Big Bang, Top-Down, Bottom-Up, Incremental, Sandwich, Functional Incremental.
- Для incomplete components могут использоваться `stubs` и `drivers`.
- Хорошая integration strategy снижает риск late defects, когда весь system уже собран.

## Notes

### What Is Integration Testing?

Integration testing проверяет, как разные parts системы работают вместе после объединения.

Например, `Module A` и `Module B` могут успешно проходить unit tests отдельно. Но после integration может оказаться, что:

- один module отправляет data в неправильном format;
- другой module ожидает другое field name;
- authentication token не передается;
- order status обновляется не там;
- payment service возвращает response, который billing module не умеет обработать;
- database transaction работает иначе, чем ожидалось.

Это и есть зона integration testing.

### Example: Online Shopping Website

Представим online shopping website для компании, которая продает camping gear.

Система состоит из modules:

- user registration and login;
- product catalogue;
- shopping cart;
- billing;
- payment gateway integration;
- shipping and package tracking.

Developers написали и проверили каждый module отдельно через unit testing. На этом уровне все выглядит хорошо.

Но после deployment всех modules в общий environment появляются defects:

- после login shopping cart не показывает items, которые user добавил раньше;
- billing amount не включает shipping cost;
- payment response не обновляет order status;
- tracking number не появляется после successful payment;
- user session теряется между cart и checkout.

Каждый module мог быть "правильным" отдельно, но integration между ними была broken. Integration testing как раз и помогает найти такие issues.

### Why Integration Testing Matters

Integration defects часто дорогие, потому что они появляются на стыке responsibilities.

Например:

- frontend считает, что backend возвращает `totalPrice`;
- backend возвращает `total_amount`;
- payment service ожидает amount in cents;
- billing module отправляет amount in dollars;
- shipping service требует address line 2;
- registration flow не сохраняет user id, который нужен cart service.

Без integration testing такие defects могут попасть ближе к release или даже production.

## Types / Approaches

### 1. Big Bang Integration Testing

Big Bang Integration Testing - это approach, при котором все modules интегрируются одновременно, а затем тестируются как единое целое.

Advantages:

- не нужно постепенно собирать system;
- удобно для маленьких systems;
- все components уже готовы до начала integration testing.

Disadvantages:

- defects находятся поздно;
- трудно понять root cause failure;
- debugging может быть долгим;
- если system большая, approach становится risky.

Example:

Команда сначала полностью разрабатывает login, catalogue, cart, billing, payment и shipping, а потом соединяет все сразу. Если checkout ломается, нужно разбираться, где проблема: в cart, billing, payment, shipping или data mapping.

### 2. Top-Down Integration Testing

Top-Down Integration Testing начинается с верхних levels system architecture и постепенно идет вниз.

Обычно сначала тестируются high-level modules: UI, main menu, orchestration layer или main business flow. Lower-level modules, которые еще не готовы, заменяются `stubs`.

`Stub` - это temporary component, который имитирует поведение lower-level module.

Advantages:

- можно рано проверить main flows;
- product выглядит ближе к реальному user experience;
- stubs обычно проще писать, чем drivers;
- high-level design defects находятся раньше.

Disadvantages:

- low-level functionality тестируется позже;
- нужны stubs;
- некоторые technical details могут долго оставаться непроверенными.

Example:

QA тестирует checkout UI и order flow, но real payment service еще не готов. Вместо него используется stub, который всегда возвращает "payment successful".

### 3. Bottom-Up Integration Testing

Bottom-Up Integration Testing начинается с lower-level modules и постепенно движется вверх.

Сначала проверяются базовые components: database access, utility modules, payment connector, shipping connector, calculation services. Higher-level modules, которые еще не готовы, заменяются `drivers`.

`Driver` - это temporary component, который вызывает lower-level module во время testing.

Advantages:

- low-level modules проверяются рано;
- development и testing могут идти параллельно;
- полезно, когда core services критичны.

Disadvantages:

- high-level user flows проверяются позже;
- нужны test drivers;
- key interface defects на верхнем уровне могут обнаружиться ближе к концу.

Example:

Команда сначала тестирует billing calculation service и payment connector через driver, даже если checkout UI еще не готов.

### 4. Incremental Integration Testing

Incremental Integration Testing - это approach, при котором modules интегрируются постепенно, one by one или group by group.

После каждого integration step выполняется testing.

Advantages:

- defects находятся раньше;
- root cause проще определить;
- lower risk than Big Bang;
- system grows in controlled steps.

Disadvantages:

- может занимать больше времени;
- нужны stubs и drivers;
- требуется дисциплина и planning.

Example:

Сначала интегрируем login + user profile. Затем добавляем product catalogue. Потом shopping cart. Потом billing. Потом payment. После каждого шага проверяем affected flows.

### 5. Sandwich Integration Testing

Sandwich Integration Testing, или Hybrid Integration Testing, комбинирует Top-Down и Bottom-Up approaches.

System условно делится на layers:

- upper layer;
- middle target layer;
- lower layer.

Testing starts from top and bottom layers and converges toward the middle layer.

Advantages:

- top и bottom layers можно тестировать parallel;
- combines benefits of top-down and bottom-up;
- useful for layered architecture.

Disadvantages:

- planning сложнее;
- нужны и stubs, и drivers;
- middle layer может стать bottleneck;
- sub-systems могут быть недостаточно глубоко протестированы до final integration.

### 6. Functional Incremental Testing

Functional Incremental Testing строит integration вокруг business functions.

Modules объединяются и тестируются по functional areas или user flows, описанным в functional specification.

Example:

Вместо технического порядка modules команда строит testing around features:

- user registration flow;
- search and product details flow;
- add to cart flow;
- checkout flow;
- payment and shipping flow.

Этот approach удобен, когда QA хочет видеть integration through real user behavior.

## How To Do Integration Testing

Typical steps:

1. Choose integration strategy: Big Bang, Top-Down, Bottom-Up, Incremental, Sandwich или functional flow.
2. Confirm unit testing is completed for selected components.
3. Identify interfaces between modules.
4. Prepare test data and test environment.
5. Deploy selected modules together.
6. Create needed stubs or drivers.
7. Run functional integration tests.
8. Run structural/interface tests where needed.
9. Record results and defects.
10. Fix integration issues.
11. Retest and run regression checks.
12. Repeat until the complete system is integrated and tested.

### What To Test During Integration Testing

Focus areas:

- data transfer between modules;
- API request/response format;
- database updates;
- authentication and authorization between components;
- error handling;
- timeout behavior;
- retries;
- logs and audit events;
- transaction consistency;
- third-party integrations;
- file handling;
- event/message queues;
- state transitions;
- end-to-end business flow across modules.

## Unit Testing vs Integration Testing

| Unit Testing | Integration Testing |
| --- | --- |
| Проверяет отдельный unit/module. | Проверяет interaction между modules/components. |
| Обычно выполняется developer. | Обычно выполняется QA/test team или mixed team. |
| Module тестируется isolated. | Components могут зависеть друг от друга или external systems. |
| Первый уровень testing в STLC/SDLC flow. | Выполняется после unit testing и перед system testing. |
| Focus: code logic inside one unit. | Focus: interfaces, data flow, contracts and collaboration. |
| Bugs обычно local. | Bugs часто появляются на границах modules. |

## Commands / Terms

- `Integration Testing` - testing interactions between components, modules, services or systems.
- `Interface` - boundary where two components communicate.
- `Stub` - fake lower-level component used in top-down testing.
- `Driver` - fake higher-level caller used in bottom-up testing.
- `Big Bang` - all modules integrated at once.
- `Top-Down` - testing starts from high-level modules and moves down.
- `Bottom-Up` - testing starts from low-level modules and moves up.
- `Incremental Integration` - modules integrated and tested gradually.
- `Sandwich Testing` - hybrid of top-down and bottom-up.
- `Functional Incremental Testing` - integration testing by business function or user flow.

## Questions

1. What is integration testing?
2. Why is integration testing needed after unit testing?
3. What kinds of defects can integration testing find?
4. What is Big Bang integration testing?
5. What is Top-Down integration testing?
6. What is Bottom-Up integration testing?
7. What is the difference between a stub and a driver?
8. What are the advantages of incremental integration testing?
9. How is integration testing different from unit testing?
10. What should QA check during integration testing?

## What To Review Later

- STLC levels
- Unit testing vs integration testing
- System testing
- API testing
- Contract testing
- Test environment setup
- Stubs and drivers
- End-to-end testing
