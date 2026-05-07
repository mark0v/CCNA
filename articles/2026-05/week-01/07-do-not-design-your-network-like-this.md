# DO NOT Design Your Network Like This!!

Source: закрытая страница курса  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 00 Lesson 06  
Tags: network design, redundancy, single point of failure, two-tier, three-tier, collapsed core

## Summary

Плохая network design часто работает ровно до первого отказа. Если один cable, switch или router может уронить большую часть сети, значит в дизайне есть single point of failure. Статья показывает, почему daisy-chain switches опасны для бизнеса и почему network engineers проектируют сети layers: access, distribution и core.

Главная мысль статьи: сеть должна проектироваться не только “чтобы работала”, но и “чтобы переживала отказ”. Хороший дизайн учитывает failure, cost, business risk и scale.

## Key Points

- Daisy-chain design может работать, но создает опасные dependencies.
- Single point of failure - компонент, отказ которого ломает большую часть network.
- Redundancy не означает просто “добавить больше cables”.
- Access layer подключает end devices к network.
- Distribution layer агрегирует access switches и часто выполняет routing between VLANs.
- Multilayer switch, или Layer 3 switch, умеет switching и routing.
- Two-tier design состоит из access layer и distribution layer.
- Two-tier design часто называют collapsed core, потому что distribution layer выполняет роль backbone.
- Three-tier design добавляет core layer для campus-scale networks.
- Core layer должен быть fast, reliable и low latency.
- Network design - это не только technology, но и business decision: risk vs cost.

## Notes

### Your Network Should Survive Failure

Если одна проблема с cable, switch или router может уронить всю сеть за ним, design плохой. Это особенно опасно в small business networks, где сеть может начинаться как “просто добавим ещё один switch”.

Домашняя network может терпеть такой подход, потому что чаще всего обслуживает Netflix, phones и random devices. Но в business environment downtime означает потерю продаж, платежей, Wi-Fi для клиентов, доступа к servers и рабочих процессов.

Практический принцип:

```text
If one failure takes down too much, the design is weak.
```

### The Big Problem: Daisy Chain

Daisy chain - это когда switches подключаются цепочкой:

```text
Router -> Switch A -> Switch B -> Switch C -> Devices
```

Такой design выглядит простым и быстрым, но создает single points of failure.

Если cable между Switch A и Switch B падает, всё за Switch B становится недоступно. Если Switch B умирает, всё за ним тоже исчезает.

Проблема не в том, что сеть совсем не работает. Проблема в том, что она зависит от слишком малого количества critical components.

### Single Point of Failure

Single point of failure - это компонент, отказ которого вызывает большой outage.

Примеры:

| Failure | Result |
| --- | --- |
| One uplink cable dies | Devices behind it lose connectivity |
| One access switch dies | Devices on that switch go offline |
| One distribution switch dies | Many access switches may lose connectivity |
| One router dies | Off-network or internet access may fail |

При чтении network diagram полезно задавать вопросы:

```text
What happens if this link dies?
What happens if this switch dies?
What happens if this router dies?
```

Если ответ - “half the office goes down”, найден weak spot.

### Redundancy Is Not Just More Cables

Добавить extra links в daisy-chain design может немного помочь, но это не решает всю проблему. Если сам switch умирает, дополнительные cables не спасают devices behind it.

Redundancy должна уменьшать dependency on one device or one path.

Плохой подход:

```text
One critical switch must always survive.
```

Лучший подход:

```text
Network can continue when one link or device fails.
```

### A Better Design: Two-Tier Model

Вместо daisy chain лучше думать layers.

Two-tier architecture обычно включает:

- access layer;
- distribution layer.

Access switches подключаются не друг к другу цепочкой, а вверх к central distribution layer.

Общая идея:

```text
End devices -> Access switches -> Distribution layer
```

Такой design чище, понятнее и проще масштабировать.

### Access Layer

Access layer - это место, куда подключаются end devices.

Примеры devices:

- computers;
- phones;
- printers;
- Raspberry Pis;
- edge servers;
- POS terminals;
- cameras.

Главная задача access layer - дать устройствам доступ к network.

Access layer не должен быть “центром вселенной”. Его роль понятна: подключить endpoints и передать traffic дальше.

### Distribution Layer

Distribution layer агрегирует traffic от access switches и часто выполняет routing между logical networks.

В business networks здесь часто используется multilayer switch, также называемый Layer 3 switch.

Multilayer switch умеет:

- Layer 2 switching by MAC addresses;
- Layer 3 routing by IP addresses;
- routing between VLANs;
- fast forwarding inside business network.

Distribution switch становится traffic boss: devices отправляют traffic вверх к нему, через него и наружу.

### VLANs and Layer 3 Switches

VLANs - это separate logical networks на одной physical infrastructure.

Distribution layer часто занимается routing between VLANs. Например:

| VLAN | Example use |
| --- | --- |
| Staff VLAN | Office computers |
| POS VLAN | Payment terminals |
| Guest VLAN | Customer Wi-Fi |
| Camera VLAN | Security cameras |

Layer 3 switch полезен, потому что может быстро routing traffic между VLANs без отдельного router для каждой local decision.

### Downtime Costs Money

Даже two-tier design может иметь failure point, если distribution switch один.

Более надежная версия:

- two distribution switches;
- dual uplinks from access switches;
- redundant upstream routers;
- multiple paths for traffic.

Но redundancy стоит денег:

- better switches;
- more switches;
- more routers;
- more links;
- more modules;
- more planning.

Network design всегда связан с business:

```text
What can we afford to lose?
What can we afford to protect?
```

Идеальный design на бумаге бесполезен, если business не может его оплатить.

### When Two Tiers Are Not Enough

Two-tier design хорошо подходит для многих small and medium environments. Но когда business растет до campus scale, например multiple buildings, many users and lots of traffic, two-tier design может стать тесным.

Если каждый building distribution switch напрямую соединять со всеми остальными, получится complex mesh:

- too many links;
- too many ports consumed;
- more troubleshooting complexity;
- bandwidth pressure;
- expensive maintenance.

В такой ситуации появляется three-tier architecture.

### Three-Tier Architecture

Three-tier architecture добавляет core layer:

```text
Access -> Distribution -> Core
```

Роли:

| Layer | Role |
| --- | --- |
| Access | Connect end devices |
| Distribution | Aggregate access, route locally, apply policies |
| Core | Fast reliable backbone between distribution blocks/buildings |

Core layer должен быть:

- fast;
- reliable;
- low latency;
- high throughput;
- simple in function;
- not overloaded with unnecessary features.

Core не должен быть местом для хаоса. Его задача - move traffic quickly and reliably.

### Collapsed Core

Two-tier model часто называют collapsed core design.

Причина: distribution layer делает double duty. Он выполняет distribution tasks и одновременно играет роль backbone для network.

Collapsed core часто встречается в real world, потому что многим businesses не нужен full three-tier campus design.

Когда dedicated core имеет смысл:

- multiple buildings;
- campus-scale network;
- high performance between buildings;
- lots of users and traffic;
- need for better scalability.

### Match Design to Business Need

Не нужно думать “two-tier bad, three-tier good”. Правильнее смотреть на:

- company size;
- traffic demands;
- budget;
- downtime cost;
- security requirements;
- expected growth.

Хороший engineer не просто выбирает “самую красивую” architecture. Он выбирает design, который подходит business risk and budget.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Daisy chain | Подключение switches цепочкой, где каждый следующий зависит от предыдущего. |
| Single point of failure | Компонент, отказ которого вызывает большой outage. |
| Redundancy | Дублирование paths/devices/functions для уменьшения impact от failure. |
| Access layer | Layer, где end devices подключаются к network. |
| Distribution layer | Layer, который агрегирует access switches и часто выполняет routing/policies. |
| Core layer | Fast backbone layer for large/campus networks. |
| Two-tier architecture | Design with access and distribution layers. |
| Three-tier architecture | Design with access, distribution and core layers. |
| Collapsed core | Two-tier design, где distribution layer также выполняет роль core/backbone. |
| Multilayer switch | Switch that can perform Layer 2 switching and Layer 3 routing. |
| Layer 3 switch | Другое название multilayer switch. |
| VLAN | Logical network separated on shared physical infrastructure. |
| Uplink | Connection from lower layer switch toward higher layer network device. |
| Downtime | Period when network/service is unavailable. |

## Questions

### 1. Почему daisy-chain switch design опасен?

Потому что он создает single points of failure: отказ одного cable или switch может отключить всё, что находится дальше по цепочке.

### 2. Что такое single point of failure?

Single point of failure - это компонент, отказ которого вызывает существенный outage или ломает большую часть network.

### 3. Почему redundancy - это не просто “добавить больше cables”?

Потому что если critical device умирает, дополнительные cables к нему не помогут. Redundancy должна уменьшать зависимость от одного device или path.

### 4. Что делает access layer?

Access layer подключает end devices к network: computers, phones, printers, POS terminals и другие endpoints.

### 5. Что делает distribution layer?

Distribution layer агрегирует access switches, может выполнять routing between VLANs и направляет traffic дальше по network.

### 6. Что такое multilayer switch?

Multilayer switch - это switch, который умеет Layer 2 switching и Layer 3 routing.

### 7. Почему two-tier design называют collapsed core?

Потому что distribution layer выполняет и distribution role, и core/backbone role.

### 8. Когда нужен three-tier design?

Three-tier design нужен, когда network растет до campus scale: multiple buildings, много users, много traffic и требуется scalable backbone.

### 9. Какова главная роль core layer?

Core layer должен быстро и надежно перемещать traffic между distribution blocks/buildings, не становясь bottleneck.

### 10. Почему network design - это business decision?

Потому что redundancy and reliability стоят денег. Нужно балансировать downtime risk, budget и business requirements.

### 11. Какие вопросы полезно задавать при чтении network diagram?

“What happens if this link dies?”, “What happens if this switch dies?”, “What happens if this router dies?”

### 12. Почему сеть, которая “работает большую часть времени”, всё равно может быть плохим design?

Потому что она может упасть именно в момент, когда downtime наиболее дорогой, если в ней есть очевидные single points of failure.

## What To Review Later

- Daisy chain vs layered network design.
- Single points of failure.
- Difference between access, distribution and core layers.
- Two-tier vs three-tier architecture.
- Collapsed core design.
- Multilayer switch / Layer 3 switch.
- Why redundancy must match business risk and budget.
