# What Now? Cabling

Source: закрытая страница курса  
Date added: 2026-05-16  
Related plan item: Week 3 / Cabling next steps  
Tags: cabling, structured cabling, copper, fiber, network design, troubleshooting, infrastructure
Language: Russian
Translation pair: articles-en/2026-05/week-03/01-what-now-cabling.md

## Summary

Знание cabling нужно каждому networking professional, но это не значит, что именно он всегда будет физически тянуть кабели через потолки, стены и patch panels. Для CCNA важно понимать типы кабелей, категории copper, fiber, разъемы, ограничения по скорости и расстоянию, потому что эти знания помогают проектировать сеть, проверять чужую работу и принимать правильные технические решения.

Главная мысль: твоя задача часто не в том, чтобы самому установить каждый кабель, а в том, чтобы понимать, какой кабель нужен, почему он подходит и где неправильный выбор сломает весь проект.

## Key Points

- Cabling knowledge is required for network design and troubleshooting.
- Physical cable installation is often a separate job.
- Network engineers must understand cable types, speed limits, distance limits and connector types.
- Structured cabling is a real specialized skill, not a "lower" version of networking.
- In larger environments, installers often work from a plan created by engineers or designers.
- Engineers must know when copper is enough and when fiber is required.
- Good cabling knowledge helps communicate with installers and validate project scope.
- NetworkChuck Coffee examples show why media choices affect cost, uptime and deployment quality.
- Cabling can become its own career path.
- Starting in cabling can lead naturally into switching, routing, wireless and network engineering.
- You do not need to be the person terminating every run to be a legitimate network professional.

## Notes

### Знать cabling и делать cabling

После темы кабелей естественный вопрос: что теперь делать с этими знаниями?

Ответ немного неожиданный: cabling нужно знать хорошо, но в реальной работе network engineer не всегда сам физически прокладывает кабели.

Есть два разных слоя:

- понимать, какой cable type нужен;
- физически и аккуратно установить этот кабель в здании.

Они связаны, но это не всегда одна и та же роль.

### Что должен понимать network engineer

Когда ты проектируешь или проверяешь сеть, тебе нужно понимать:

- используется ли Cat5e, Cat6, Cat6a или fiber;
- какую скорость поддерживает выбранная среда;
- какие distance limits важны;
- какие connectors и transceivers нужны;
- где copper подходит, а где лучше использовать fiber;
- как кабельная инфраструктура повлияет на topology.

Это не trivia для экзамена. Это основа для решений, которые влияют на деньги, сроки и uptime.

### Пример NetworkChuck Coffee

Допустим, для NetworkChuck Coffee нужно:

- оценить текущую network infrastructure;
- найти слабые места;
- спроектировать новую topology;
- подключить и настроить network devices.

Для такого проекта cabling knowledge обязательно.

Если кассовая зона подключается к switch closet, нужно понять, достаточно ли copper run. Если нужно соединить разные части здания или удаленные wiring closets, возможно, copper уже не подходит по distance limit и нужна fiber.

Ошибка в выборе среды означает:

- лишние расходы;
- переделку работ;
- задержку проекта;
- риск downtime в рабочее время.

### Почему installer и engineer часто разные люди

В больших проектах человек, который прокладывает кабель, может не заниматься network design. Он работает по плану:

```text
Install Cat6 here.
Terminate it there.
Label it this way.
Patch it into this panel.
```

Installer отвечает за физическую сторону: аккуратную прокладку, маркировку, termination, pathways, safety и соответствие требованиям здания.

Engineer отвечает за то, чтобы сам план был правильным.

### Structured cabling - отдельная специализация

Правильная прокладка кабеля - это не просто "протянуть провод".

Там есть:

- ceiling tiles;
- conduits;
- cable trays;
- j-hooks;
- patch panels;
- labeling;
- bend radius;
- safety issues;
- building codes;
- тестирование и сертификация линий.

Это физически сложная и ответственная работа. Люди, которые делают ее хорошо, действительно заслуживают уважения.

### Что значит быть полезным в проекте

Network engineer часто должен уметь сказать:

```text
No, we cannot use that cable here.
Yes, this medium supports the required speed.
We need fiber between these closets because copper will not handle that distance.
This port, panel and cable label do not match the plan.
```

То есть ценность не только в руках, но и в решениях.

Иногда твоя работа - не установить вещь. Твоя работа - понять, имеет ли установленная вещь смысл.

### Можно ли построить карьеру на cabling

Да. Structured cabling может быть полноценной карьерой.

Это не запасной путь и не "менее важная" версия networking. Это отдельная практическая область, где можно хорошо зарабатывать и стать очень ценным специалистом.

Более того, cabling часто становится сильной точкой входа в networking:

```text
Structured cabling -> switching -> routing -> wireless -> network engineering
```

Такой путь дает мощное понимание сети снизу вверх: от floor tiles и patch panels до CLI.

### Практический вывод

На текущем этапе тебе нужно знать cabling достаточно хорошо, чтобы:

- проектировать с уверенностью;
- выбирать правильную среду передачи;
- понимать ограничения copper и fiber;
- разговаривать с installers на одном языке;
- проверять, соответствует ли работа плану;
- troubleshooting начинать не только с config, но и с physical layer.

Не нужно чувствовать себя "ненастоящим" network engineer только потому, что ты не terminating every cable run by hand.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Cabling | Физическая кабельная инфраструктура сети: copper, fiber, connectors, patch panels and pathways. |
| Structured cabling | Организованная система кабельной инфраструктуры здания с правилами прокладки, маркировки и termination. |
| Copper | Медная среда передачи, например twisted-pair Ethernet cable. |
| Fiber | Оптическая среда передачи, полезная для больших расстояний, высокой скорости и некоторых uplink-сценариев. |
| Cat5e | Категория copper cable, часто встречающаяся в старых и небольших сетях. |
| Cat6 | Категория copper cable, распространенная для современных Ethernet runs. |
| Distance limit | Максимальная полезная длина линии до проблем со скоростью, сигналом или стандартом. |
| Connector | Физический разъем, через который кабель подключается к устройству или panel. |
| Patch panel | Панель, где заканчиваются постоянные кабельные линии и откуда они patch-кабелями подключаются к оборудованию. |
| Termination | Правильное подключение жил кабеля к connector, jack или patch panel. |
| Installer | Специалист, который физически прокладывает, маркирует и завершает кабельные линии. |
| Network engineer | Специалист, который проектирует, настраивает, проверяет и troubleshooting network infrastructure. |
| Physical layer | Layer 1 модели OSI: кабели, сигналы, разъемы, физические интерфейсы. |

## Questions

### 1. Нужно ли network engineer знать cabling?

Да. Даже если он не прокладывает кабели сам, cabling knowledge нужен для design, troubleshooting и общения с installers.

### 2. Значит ли знание cabling, что engineer всегда сам тянет кабель?

Нет. Physical installation часто выполняют отдельные structured cabling specialists.

### 3. Какие cabling details особенно важны для CCNA-level networking?

Cable categories, speed limits, distance limits, connector types, copper vs fiber и роль physical layer.

### 4. Почему structured cabling считается отдельной специализацией?

Потому что там есть свои инструменты, standards, safety concerns, building constraints, labeling, pathways, patch panels и termination quality.

### 5. Что должен уметь engineer сказать при выборе среды передачи?

Подходит ли выбранный cable type для нужной скорости, расстояния и topology, или нужна другая среда, например fiber.

### 6. Когда fiber может быть лучше copper?

Когда нужно больше расстояние, высокая скорость, uplink между closets или сценарий, где copper не проходит по ограничениям.

### 7. Почему неправильный выбор cable medium опасен для бизнеса?

Он может привести к переделке, задержкам, лишним расходам и downtime.

### 8. Может ли cabling быть отдельной карьерой?

Да. Structured cabling - полноценная и ценная специализация.

### 9. Почему опыт cabling может помочь будущему network engineer?

Он дает понимание physical infrastructure, которое потом помогает в switching, routing, wireless и troubleshooting.

### 10. Какой главный вывод из этой темы?

Нужно знать cabling достаточно хорошо, чтобы принимать правильные решения, даже если физическую установку выполняет другой специалист.

## What To Review Later

- Copper vs fiber.
- Cat5e, Cat6 and Cat6a basics.
- Speed and distance limits.
- Connector types.
- Patch panels and termination.
- Physical layer troubleshooting.
- Difference between installer and network engineer roles.
- When cabling becomes a career path.
