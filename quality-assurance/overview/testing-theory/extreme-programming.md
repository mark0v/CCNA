# Extreme Programming

## Summary

Extreme Programming, или XP, - это Agile framework для разработки ПО, который делает сильный акцент на инженерных практиках, качестве кода, быстрой обратной связи и устойчивом темпе работы команды.

XP помогает командам работать с изменяющимися требованиями, снижать технические риски и выпускать качественный software через короткие cycles, automated tests, continuous integration, pair programming и simple design.

## Key Points

- XP - один из самых инженерно-конкретных Agile frameworks.
- Главная цель XP - higher quality software и better quality of life для development team.
- XP особенно полезен при changing requirements и technical uncertainty.
- Основные values: communication, simplicity, feedback, courage, respect.
- XP делает акцент на practices: pair programming, test-first programming, continuous integration, small releases, refactoring.
- XP лучше работает в небольших, тесно взаимодействующих cross-functional teams.
- Многие команды не используют XP полностью, но берут отдельные engineering practices.

## Notes

### Что такое Extreme Programming

Extreme Programming - это Agile framework, который фокусируется не только на process management, но и на software engineering practices.

Если Scrum больше говорит о ролях, events и artifacts, то XP подробнее отвечает на вопрос: "Как именно команде писать качественный код в условиях изменений?"

Название "Extreme" не означает хаос или радикальность ради радикальности. Идея в том, что полезные практики доводятся до высокого уровня дисциплины. Если code review полезен, XP предлагает pair programming как постоянный review. Если testing полезен, XP предлагает писать tests до production code.

### Когда XP подходит

XP особенно уместен, когда:

- software requirements динамически меняются;
- проект имеет fixed time и использует новую technology;
- команда небольшая и тесно взаимодействует;
- team members могут часто общаться face-to-face;
- technology stack позволяет automated unit и functional tests;
- важны быстрый feedback и high code quality.

XP не всегда получается внедрить полностью. Например, distributed teams, rigid organizations или проекты без test automation могут испытывать трудности. Но даже тогда можно брать отдельные XP practices.

### Values of XP

#### Communication

Software development - это team sport. Команда постоянно передает знания: о requirements, code, architecture, risks и defects.

XP делает акцент на прямой коммуникации, желательно face-to-face, с использованием whiteboard, diagrams или других visual tools.

#### Simplicity

Simplicity отвечает на вопрос: "What is the simplest thing that will work?"

Команда не должна строить сложный design на будущее, если текущие требования этого не требуют. Simple design проще поддерживать, тестировать и менять.

#### Feedback

XP строится вокруг коротких feedback loops.

Feedback приходит из tests, customer conversations, pair programming, continuous integration и working software. Команда быстро видит, что работает, а что нужно изменить.

#### Courage

Courage - это готовность действовать, даже когда есть uncertainty или fear.

Команде нужна смелость, чтобы говорить о проблемах, менять неработающие practices, принимать сложный feedback, refactor code и не прятать blockers.

#### Respect

XP невозможен без respect.

Team members должны уважать друг друга, чтобы честно общаться, давать feedback, принимать criticism и вместе искать simple solutions.

### Core XP Practices

XP practices связаны между собой. Их можно применять отдельно, но максимальный эффект появляется, когда они поддерживают друг друга.

Классические XP practices включают:

- Planning Game;
- Small Releases;
- Metaphor;
- Simple Design;
- Testing;
- Refactoring;
- Pair Programming;
- Collective Ownership;
- Continuous Integration;
- Sustainable pace;
- On-site Customer;
- Coding Standard.

Позже описание practices было уточнено и стало более практичным.

### Sit Together

Так как communication - одна из главных values XP, команда должна иметь возможность быстро и удобно общаться.

Идеальный вариант - общая рабочая зона без барьеров для коммуникации. Для distributed teams это можно частично заменить качественными calls, shared boards, chats и documentation.

### Whole Team

XP предполагает cross-functional team, где вместе работают все, кто нужен для delivery.

Это могут быть developers, QA, customer representative, analyst, UX, DevOps и другие роли. Главное - команда ежедневно работает над общей целью, а не передает задачи между silo.

### Informative Workspace

Workspace должен делать работу прозрачной.

Команда использует information radiators: boards, charts, test status, build status, blockers, progress indicators. Важно, чтобы текущее состояние проекта было видно без долгих отчетов.

### Energized Work

XP поддерживает sustainable pace.

Knowledge work требует focus и mental energy. Постоянные переработки ухудшают качество, повышают количество defects и разрушают команду.

Energized work означает, что команда работает интенсивно, но без хронического overwork.

### Pair Programming

Pair Programming означает, что production code пишут два человека за одной рабочей станцией или в одной remote session.

Один человек может быть driver и писать код, другой - navigator и думать о design, edge cases, readability и risks. Роли регулярно меняются.

Преимущества:

- continuous code review;
- меньше defects;
- быстрее spread knowledge;
- меньше bottlenecks;
- лучше focus.

### Stories

XP использует stories для описания того, что пользователь хочет делать с продуктом.

Story - это короткое описание user need, которое помогает planning и становится reminder для будущей conversation.

Story не должна заменять общение. Она должна запускать разговор между customer и team.

### Weekly Cycle

Weekly Cycle похож на короткую iteration.

В начале недели команда и customer выбирают stories, которые нужно реализовать. Команда разбивает stories на tasks и работает над tested features.

В конце цикла команда показывает результат и получает feedback.

### Quarterly Cycle

Quarterly Cycle помогает связать короткие weekly cycles с более широким release plan.

Customer определяет high-level features на quarter или release. План может меняться каждую неделю по мере появления новой информации.

### Slack

Slack - это запас в плане.

Команда может добавлять low-priority tasks, которые можно убрать, если более важная работа занимает больше времени. Это помогает учитывать uncertainty и не ломать весь forecast.

### Ten-Minute Build

Ten-Minute Build означает, что вся система должна собираться и запускать tests примерно за 10 минут.

Если build слишком долгий, команда запускает его реже. Чем реже build и tests, тем позже обнаруживаются ошибки.

Эта practice поддерживает Continuous Integration и Test-First Programming.

### Continuous Integration

Continuous Integration означает, что code changes часто интегрируются в main codebase и автоматически проверяются.

XP исходит из идеи: if integration hurts, do it more often.

Частая integration уменьшает размер changes, быстрее показывает conflicts и снижает риск большого integration disaster в конце.

### Test-First Programming

Test-First Programming меняет обычный порядок:

```text
write failing automated test -> run failing test -> write code -> run test -> refactor -> repeat
```

Это близко к TDD.

Польза:

- короткий feedback cycle;
- меньше bugs;
- clearer design;
- больше уверенности при refactoring;
- executable specification в виде tests.

### Incremental Design

Incremental Design означает, что команда делает достаточно upfront thinking, чтобы понимать общую direction, но детальный design уточняет по мере реализации features.

Это снижает cost of change, потому что design decisions принимаются на основе актуальной информации.

Refactoring поддерживает incremental design: команда постоянно улучшает структуру кода, убирает duplication и сохраняет simple design.

### Roles in XP

XP не делает сильный акцент на formal roles, но обычно выделяют несколько ролей.

#### Customer

Customer принимает business decisions:

- какие features нужны;
- как понять, что system done;
- какие acceptance criteria использовать;
- какой budget и business case;
- что делать next.

XP Customer должен быть активно вовлечен и давать clear direction.

#### Developer

Developers реализуют stories, выбранные customer.

В XP "developer" может включать всех, кто участвует в создании продукта, потому что команда cross-functional.

#### Tracker

Tracker следит за metrics, если команда считает это полезным.

Например:

- velocity;
- причины изменения velocity;
- overtime;
- passing/failing tests;
- build health.

Эта роль не обязательна.

#### Coach

Coach помогает команде применять XP practices.

Обычно это человек с опытом XP, который помогает избежать типичных ошибок и поддерживает discipline.

### XP Lifecycle

XP lifecycle можно описать через stories, release planning, quarterly cycle и weekly cycles.

1. Customer описывает desired results через stories.
2. Team оценивает stories.
3. Customer расставляет priorities по value.
4. Если есть technical uncertainty, команда делает spike.
5. Team и customer создают release plan.
6. Команда работает серией weekly cycles.
7. В конце каждого cycle customer review решает, продолжать, менять priority или завершать work.

**Spike** - это короткое time-boxed research activity, которое помогает разобраться с technical unknowns.

### Origins of XP

XP стал известен благодаря проекту Chrysler Comprehensive Compensation (C3) в 1990-х.

Kent Beck был приглашен улучшить работу проекта и применил подход, который позже стал Extreme Programming. Ron Jeffries и другие участники помогли развить и распространить эти идеи.

### Primary Contribution

Главный вклад XP - набор взаимосвязанных engineering practices.

Многие Agile-команды начинают со Scrum или Kanban, а позже добавляют XP practices, когда понимают, что им не хватает technical discipline.

XP напоминает важную вещь: Agile без engineering excellence быстро превращается в красивый процесс поверх слабого кода.

## Commands / Terms

- **Extreme Programming (XP)** - Agile framework с сильным фокусом на engineering practices.
- **Pair Programming** - разработка production code двумя людьми вместе.
- **Test-First Programming** - сначала test, потом code.
- **TDD** - test-driven development.
- **Continuous Integration** - частая интеграция changes с automated checks.
- **Ten-Minute Build** - build и tests должны выполняться достаточно быстро, чтобы запускаться часто.
- **Incremental Design** - design развивается постепенно вместе с продуктом.
- **Refactoring** - улучшение структуры кода без изменения поведения.
- **Story** - краткое описание user need.
- **Spike** - короткое исследование technical uncertainty.
- **Sustainable Pace** - устойчивый темп без хронического overwork.

## Questions

**1. Что такое Extreme Programming?**  
XP - это Agile framework, который фокусируется на качестве software и engineering practices.

**2. Какие пять values есть в XP?**  
Communication, simplicity, feedback, courage и respect.

**3. Почему XP делает акцент на automated tests?**  
Tests дают быстрый feedback, снижают риск defects и позволяют безопаснее менять код.

**4. Что такое pair programming?**  
Это практика, где два человека вместе пишут production code, постоянно reviewing design, logic и implementation.

**5. Когда XP особенно полезен?**  
Когда требования меняются, есть technical uncertainty, нужна высокая quality и команда может часто общаться.

**6. Почему XP practices лучше работают вместе?**  
Потому что они усиливают друг друга: test-first поддерживает CI, CI поддерживает refactoring, pair programming улучшает design и knowledge sharing.

## What To Review Later

- XP values.
- Pair programming.
- Test-first programming and TDD.
- Continuous integration.
- Refactoring.
- Incremental design.
- Difference between Scrum and XP.
- How QA participates in XP.
