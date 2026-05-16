# Network Design Model - Three Tiered Architecture

Source: закрытая страница курса  
Date added: 2026-05-16  
Related plan item: Week 3 / Network design models  
Tags: network design, three-tier architecture, access layer, distribution layer, core layer, collapsed core, spine leaf, soho
Language: Russian
Translation pair: articles-en/2026-05/week-03/05-network-design-model-three-tiered-architecture.md

## Summary

Network design model помогает строить сеть осознанно, а не просто подключать устройства друг к другу, пока не закончились порты. Three-tier architecture делит campus network на access layer, distribution layer и core layer. Это дает понятную структуру, redundancy и scalability.

Для маленькой сети SOHO model может быть нормальной: router, switch и несколько devices. Но когда сеть становится критичной для бизнеса, случайная daisy-chain схема превращается в риск. Для одного-двух зданий часто подходит two-tier / collapsed core design. Для трех и более зданий нужен отдельный core layer.

## Key Points

- Bad network design often starts as devices randomly plugged together.
- SOHO model can work for a very small office or home network.
- A growing business quickly outgrows unmanaged daisy-chained switches.
- Three-tier architecture is a classic Cisco network design model.
- Access layer is where end devices connect.
- Distribution layer aggregates access switches and provides redundancy.
- Core layer connects buildings or major network blocks at scale.
- Access switches should connect upward, not randomly to each other.
- Redundant links to two distribution switches reduce single points of failure.
- Two-tier design is also called collapsed core.
- Collapsed core combines distribution and core functions.
- One or two buildings often use two-tier design.
- Three or more buildings usually need a core layer.
- Spine-leaf is another architecture, mostly used in data centers.
- Good design prevents fragile, hard-to-troubleshoot networks.

## Notes

### Почему design matters

Самые болезненные network outages часто появляются не из-за сложных технологий, а из-за отсутствия design.

Плохой подход:

```text
Plug in a router.
Add a switch.
Run out of ports.
Add another switch.
Daisy-chain more switches.
Hope nothing breaks.
```

Поначалу это работает. Потом сеть становится частью бизнеса, и случайная схема превращается в проблему.

### SOHO Model

SOHO означает:

```text
Small Office, Home Office
```

Типичная SOHO-сеть:

- router;
- one switch;
- maybe a wireless access point;
- a few end devices.

Для маленького кафе, домашнего офиса или временной сети это может быть нормально.

Проблема начинается, когда сеть растет:

- больше computers;
- IP phones;
- printers;
- cameras;
- access points;
- servers;
- payment systems;
- coffee roasting equipment.

Если просто добавлять switches one after another, получится fragile daisy-chain.

### Daisy-chain Risk

Daisy-chain выглядит примерно так:

```text
Router -> Switch 1 -> Switch 2 -> Switch 3 -> Switch 4
```

Проблема:

- один failed switch может отрезать все, что стоит дальше;
- один unplugged cable может остановить целую часть бизнеса;
- traffic path становится неочевидным;
- troubleshooting усложняется;
- redundancy почти нет.

Для домашней сети это может быть терпимо. Для бизнеса - уже опасно.

### Three-Tier Architecture

Three-tier architecture делит сеть на три layers:

1. Access layer.
2. Distribution layer.
3. Core layer.

Каждый layer имеет свою роль. Это делает сеть понятнее, масштабируемее и надежнее.

### Access Layer

Access layer - это место, где devices получают доступ к сети.

Сюда подключаются:

- user computers;
- printers;
- IP phones;
- wireless access points;
- cameras;
- point-of-sale terminals;
- other end devices.

Простая мысль:

```text
End devices plug into the access layer.
```

Это closest layer к пользователю.

### Distribution Layer

Distribution layer - это consolidation point для access switches.

Access switches не должны хаотично подключаться друг к другу. Они поднимаются вверх к distribution layer.

Distribution layer часто отвечает за:

- aggregation of access switches;
- policy boundaries;
- routing between VLANs;
- redundancy;
- connection to shared services;
- summarization or control points in larger designs.

В учебном примере сюда можно поместить важные shared services:

- DNS;
- DHCP;
- internal servers.

### Redundancy at Distribution

Сильная идея three-tier/two-tier design:

```text
Each access switch connects to both distribution switches.
```

Это дает redundancy.

Если один distribution switch fails, access layer still has a path через второй distribution switch.

Так сеть здания продолжает работать лучше, чем при одиночной цепочке switches.

### Core Layer

Core layer нужен, когда сеть становится campus-scale.

Представь несколько зданий:

- Building A;
- Building B;
- Building C;
- Building D.

Если каждое здание напрямую соединять с каждым другим зданием, получится full mesh nightmare.

Пример плохого роста:

```text
A connects to B, C, D
B connects to A, C, D
C connects to A, B, D
D connects to A, B, C
```

Чем больше зданий, тем сложнее topology.

Core layer решает это:

```text
All buildings connect to the core.
Core carries traffic between buildings.
```

Core должен быть быстрым, надежным и простым. Его задача - transport between major network blocks.

### Two-Tier / Collapsed Core

Не каждой сети нужен отдельный core.

Для одной или двух buildings часто подходит two-tier design:

```text
Access layer + Distribution layer
```

Это также называется:

```text
Collapsed core
```

Core functions collapsed into distribution.

Такой design проще, дешевле и нормален для небольших campus environments.

### When to Use Three Tiers

Простое правило:

| Environment | Recommended Design |
| --- | --- |
| Home or tiny office | SOHO |
| One or two buildings | Two-tier / collapsed core |
| Three or more buildings | Three-tier architecture |
| Data center with many servers | Spine-leaf |

Это не абсолютный закон, но хороший стартовый mental model.

### Spine and Leaf

Spine-leaf - отдельная architecture, чаще всего для data center.

В data center много:

- servers;
- racks;
- east-west traffic;
- redundant paths;
- high bandwidth needs.

Leaf switches connect to servers and spine switches. Spine switches connect the leaf layer together.

Это похоже на collapsed core по идее, но оптимизировано для massive compute environments.

Для NetworkChuck Coffee это пока не первый design. Но полезно знать, что такая architecture существует.

### NetworkChuck Coffee Example

На первом этапе Harvey может начать с SOHO:

```text
Router -> Switch -> AP and devices
```

Когда появляются roasters, IP phones, staff computers, POS terminals and servers, сеть уже должна стать более структурной.

Хороший design:

```text
End devices -> Access switches -> Distribution switches -> Core if needed
```

Так легче:

- масштабироваться;
- добавлять новые devices;
- troubleshooting outages;
- документировать topology;
- избегать single points of failure;
- подключать новые buildings.

### Main Takeaway

Не надо просто подключать devices, пока сеть "как-то работает".

Правильная мысль:

```text
Design first.
Then connect.
Then configure.
Then troubleshoot from a known structure.
```

Three-tier architecture дает framework, который помогает строить network infrastructure intentionally.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Network design model | Framework for structuring a network before devices are connected. |
| SOHO | Small Office, Home Office; simple small-network model. |
| Daisy-chain | Connecting switches one after another in a chain, often creating fragile paths. |
| Three-tier architecture | Design model with access, distribution and core layers. |
| Access layer | Layer where end devices connect to the network. |
| Distribution layer | Aggregation layer for access switches; often provides policy, routing and redundancy. |
| Core layer | High-speed layer connecting major network blocks or buildings. |
| Redundancy | Extra path or device that keeps service working if one component fails. |
| Collapsed core | Two-tier design where core functions are combined with distribution. |
| Campus network | Network connecting multiple areas or buildings in one organization/location. |
| Full mesh | Topology where every node connects directly to every other node. |
| Spine-leaf | Data center architecture with leaf switches connected to spine switches. |
| Single point of failure | Component whose failure can break a larger part of the network. |

## Questions

### 1. Почему случайное подключение switches становится проблемой?

Потому что сеть становится fragile, плохо документированной и сложной для troubleshooting.

### 2. Что такое SOHO model?

Small Office, Home Office model: простая сеть с router, switch, возможно AP и небольшим числом devices.

### 3. Когда SOHO model перестает быть достаточной?

Когда бизнес начинает зависеть от сети и появляются many devices, services, payment systems or multiple switches.

### 4. Какие три layers есть в three-tier architecture?

Access, Distribution and Core.

### 5. Что подключается к access layer?

End devices: computers, printers, IP phones, APs, cameras, POS terminals.

### 6. Какую роль выполняет distribution layer?

Он агрегирует access switches, дает redundancy, policy/routing boundaries и connection to shared services.

### 7. Почему access switch полезно подключать к двум distribution switches?

Чтобы получить redundancy: при отказе одного distribution switch остается второй path.

### 8. Зачем нужен core layer?

Чтобы cleanly and scalably connect multiple buildings or major network blocks.

### 9. Что такое collapsed core?

Two-tier design, где функции core объединены с distribution layer.

### 10. Когда обычно используется two-tier design?

Для одной или двух buildings, где отдельный core еще не нужен.

### 11. Когда стоит переходить к three-tier design?

Когда сеть соединяет три или больше buildings или становится campus-scale.

### 12. Где чаще используется spine-leaf architecture?

В data centers с большим количеством servers, racks, redundant paths and high bandwidth needs.

## What To Review Later

- SOHO vs business network design.
- Access layer role.
- Distribution layer role.
- Core layer role.
- Redundancy between access and distribution.
- Two-tier / collapsed core.
- Three-tier campus design.
- Full mesh problem between buildings.
- Spine-leaf basics.
