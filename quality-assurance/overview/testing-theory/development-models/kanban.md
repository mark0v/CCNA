# Kanban

## Summary

Kanban - это Agile framework для управления работой через визуализацию workflow, ограничение work in progress и постоянное улучшение процесса. Команда видит все задачи на Kanban board, понимает текущую нагрузку и быстрее замечает bottlenecks.

Главная идея Kanban - сделать работу прозрачной и управлять потоком задач. В отличие от Scrum, Kanban не требует fixed-length sprints, ролей или ceremonies. Работа движется непрерывно: новая задача берется тогда, когда у команды появляется capacity.

## Key Points

- Kanban визуализирует работу через board и cards.
- Work in progress ограничивается через WIP limits.
- Команда оптимизирует flow, а не планирует работу только sprint-блоками.
- Kanban помогает находить bottlenecks и уменьшать cycle time.
- Основные метрики: cycle time, lead time, cumulative flow diagram и control chart.
- Kanban хорошо подходит для support, operations, maintenance и команд с постоянным потоком входящих задач.
- Scrum использует fixed sprints, Kanban использует continuous flow.

## Notes

### Что такое Kanban

Kanban - это метод управления работой, который помогает командам видеть задачи, контролировать загрузку и улучшать delivery process.

В software development Kanban часто используют Agile и DevOps команды. Он помогает синхронизировать работу в реальном времени: каждый участник видит, какие задачи запланированы, какие выполняются сейчас, какие заблокированы и какие уже завершены.

### Kanban Flow

Kanban flow - это движение задач через workflow от начала до завершения.

Простейший flow может выглядеть так:

- **To Do**
- **In Progress**
- **Done**

В реальной software-команде workflow может быть детальнее:

- Backlog
- Ready
- In Progress
- Code Review
- Testing
- Done

Смысл не в количестве колонок, а в прозрачности. Board должен отражать настоящий процесс команды.

### Как структурировать Kanban Flow

#### 1. Visualize Workflow

Сначала команда визуализирует процесс на Kanban board.

Каждая колонка представляет stage работы. Каждая задача представлена Kanban card. Это помогает быстро понять, где находится работа и что происходит прямо сейчас.

#### 2. Standardize Workflow

Workflow должен быть понятным и согласованным.

Команда договаривается, что означает каждая колонка, когда задача может перейти дальше и какие критерии должны быть выполнены.

Например, колонка `Testing` может означать, что задача уже разработана, задеплоена на test environment и готова к QA-проверке.

#### 3. Identify Blockers and Dependencies

Kanban board должен помогать быстро видеть blockers и dependencies.

Если задача застряла в одной колонке, это сигнал: возможно, не хватает информации, есть техническая проблема, кто-то перегружен или есть dependency от другой команды.

#### 4. Set WIP Limits

**WIP limit** - это ограничение количества задач, которые могут одновременно находиться в определенной колонке.

Например, если `Code Review` имеет WIP limit 2, команда не должна держать больше двух задач на review одновременно.

WIP limits помогают:

- уменьшить multitasking;
- быстрее завершать начатую работу;
- выявлять bottlenecks;
- сфокусировать команду;
- стабилизировать flow.

#### 5. Encourage Collaboration

Kanban работает лучше, когда команда думает не "моя задача", а "наш flow".

Если колонка `Testing` перегружена, developers могут помочь QA: уточнить acceptance criteria, исправить окружение, проверить простые кейсы или быстрее реагировать на defects.

#### 6. Use Kanban Cards

Kanban card представляет отдельную work item.

Карточка обычно содержит:

- title;
- description;
- assignee;
- priority;
- acceptance criteria;
- estimate или size;
- links на requirements, design, tickets, pull requests;
- status и blockers.

Хорошая card помогает понять работу без лишних meetings.

### История Kanban

Kanban появился не в software development. Его корни связаны с Toyota и manufacturing process в конце 1940-х.

Toyota хотела лучше управлять inventory и производить детали just in time. Идея была похожа на работу supermarket: держать ровно столько inventory, сколько нужно, и пополнять его по фактическому спросу.

Слово **kanban** с японского часто переводят как "signboard" или "card". В производстве карточка сигнализировала, какие материалы нужны, в каком количестве и когда их нужно пополнить.

Позже этот подход был адаптирован для software teams: вместо физических материалов команда управляет flow задач.

### Kanban for Software Teams

Software teams используют Kanban, чтобы сопоставить количество work in progress с реальной capacity команды.

Это дает:

- гибкое planning;
- прозрачность работы;
- меньшую перегрузку;
- более быстрый delivery;
- фокус на continuous improvement;
- более понятные bottlenecks.

Kanban особенно полезен, когда задачи приходят постоянно и их трудно упаковать в sprint заранее: support issues, production bugs, operations, maintenance, DevOps tasks.

### Kanban Board

Kanban board - это основной инструмент команды.

Он может быть физическим или digital. В modern software teams чаще используют digital boards, потому что они дают traceability, remote access, links, history и интеграцию с другими tools.

Board должен быть single source of truth. Если работа не отображена на board, команда ее не видит и не может управлять flow.

### Kanban Cards

Kanban cards показывают отдельные work items.

Главная польза cards - visibility. Команда видит:

- кто работает над задачей;
- на каком этапе она находится;
- есть ли blockers;
- сколько задач в работе;
- где накапливается очередь.

Для QA Kanban cards особенно полезны, потому что позволяют видеть, какие задачи готовы к testing, какие возвращены на fixing и какие уже прошли проверку.

### Benefits of Kanban

#### Planning Flexibility

Kanban-команда фокусируется на текущей работе.

Когда задача завершена, команда берет следующую задачу из backlog. Product Owner или manager может менять приоритеты в backlog, не ломая текущий sprint forecast, потому что Kanban не завязан на fixed sprint commitment.

#### Shorter Cycle Time

**Cycle time** - это время от начала работы над задачей до ее завершения.

Kanban помогает уменьшать cycle time, потому что команда видит, где задачи застревают, и может улучшать flow.

Если только один человек умеет выполнять определенный тип задач, он становится bottleneck. Поэтому Kanban-команды часто развивают shared skills, code review, mentoring и cross-training.

#### Fewer Bottlenecks

Multitasking снижает эффективность. Когда слишком много задач начато одновременно, команда чаще переключается между контекстами и медленнее завершает работу.

WIP limits делают bottlenecks видимыми. Если колонка заполнена до лимита, команда не должна начинать новую работу. Вместо этого нужно помочь завершить уже начатую.

#### Visual Metrics

Kanban использует метрики для continuous improvement.

Полезные метрики:

- **Cycle Time** - сколько времени задача находится в active work.
- **Lead Time** - сколько времени проходит от request до delivery.
- **Throughput** - сколько задач команда завершает за период.
- **Cumulative Flow Diagram** - показывает количество задач в разных состояниях.
- **Control Chart** - помогает отслеживать cycle time и стабильность процесса.

Метрики нужны не для наказания команды, а для поиска улучшений.

#### Continuous Delivery

Kanban хорошо сочетается с CI/CD.

Обе идеи фокусируются на частой поставке value и уменьшении задержек. Команда не ждет конца sprint, чтобы выпустить результат. Если работа готова и прошла Definition of Done, ее можно доставлять пользователям.

### Scrum vs Kanban

Scrum и Kanban оба относятся к Agile-подходам, но работают по-разному.

| Area | Scrum | Kanban |
|---|---|---|
| Delivery | Fixed-length sprints | Continuous flow |
| Roles | Product Owner, Scrum Master, Developers | Не требует специальных ролей |
| Planning | Sprint Planning | Continuous prioritization |
| Main metric | Velocity | Cycle time / Lead time |
| Change | Не желательно менять sprint forecast | Change can happen anytime |
| Best fit | Product/feature development | Support, operations, continuous work |

Некоторые команды смешивают подходы в **Scrumban**: берут planning и backlog discipline из Scrum, но используют WIP limits и flow из Kanban.

### Common Kanban Mistakes

Kanban выглядит простым, но его легко использовать поверхностно.

Частые ошибки:

- board не отражает реальный workflow;
- нет WIP limits;
- команда игнорирует bottlenecks;
- cards слишком vague;
- нет Definition of Done;
- метрики не используются;
- board превращается в красивую картинку, а не рабочий инструмент.

### Когда использовать Kanban

Kanban подходит, когда:

- задачи приходят постоянно;
- приоритеты часто меняются;
- команда занимается support или maintenance;
- сложно планировать fixed sprint scope;
- важна скорость реакции;
- нужно увидеть bottlenecks;
- команда хочет улучшать flow постепенно.

## Commands / Terms

- **Kanban** - Agile framework для визуального управления потоком работы.
- **Kanban Board** - доска, показывающая workflow и задачи.
- **Kanban Card** - карточка отдельной work item.
- **WIP (Work in Progress)** - работа, которая уже начата, но еще не завершена.
- **WIP Limit** - ограничение количества задач в определенном состоянии.
- **Cycle Time** - время от начала работы над задачей до завершения.
- **Lead Time** - время от запроса до доставки результата.
- **Throughput** - количество завершенных задач за период.
- **Cumulative Flow Diagram** - диаграмма распределения задач по состояниям.
- **Control Chart** - график для анализа cycle time.
- **Scrumban** - гибрид Scrum и Kanban.

## Questions

**1. Что такое Kanban?**  
Kanban - это Agile framework, который визуализирует работу, ограничивает WIP и помогает улучшать flow.

**2. Зачем нужны WIP limits?**  
Они уменьшают multitasking, помогают фокусироваться и делают bottlenecks видимыми.

**3. Чем Kanban отличается от Scrum?**  
Scrum работает через fixed sprints и роли. Kanban работает через continuous flow и не требует специальных ролей.

**4. Что такое cycle time?**  
Cycle time - это время от момента, когда команда начала работать над задачей, до момента ее завершения.

**5. Когда Kanban особенно полезен?**  
Когда задачи приходят непрерывно, приоритеты часто меняются, а команде важно быстро реагировать и видеть bottlenecks.

**6. Какая типичная ошибка в Kanban?**  
Использовать board без WIP limits и без анализа flow. Тогда Kanban превращается просто в список задач.

## What To Review Later

- Difference between Scrum and Kanban.
- WIP limits.
- Cycle time vs lead time.
- Cumulative flow diagram.
- Control chart.
- Scrumban.
- How QA work moves through Kanban flow.
