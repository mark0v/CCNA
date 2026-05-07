# Data Center NETWORKS (What do they look like??)

Source: закрытая страница курса  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 00 Lesson 07  
Tags: data center, spine-leaf, east-west traffic, north-south traffic, tor, stp, underlay, overlay

## Summary

Data center network - это не просто “офисная сеть побольше”. Старые data center designs часто строились по campus-style three-tier model, но modern data centers требуют другой подход из-за большого количества server-to-server communication. Поэтому появился spine-leaf design, который дает predictable low-hop connectivity между racks и лучше использует bandwidth.

Главная мысль статьи: современные data centers проектируются вокруг east-west traffic, а не только north-south traffic.

## Key Points

- Data center может быть огромным зданием, colocated rack space или маленькой server room.
- Cloud тоже работает на data centers, просто это чужое hardware и чужая building.
- Traditional three-tier data center design хорошо подходил для north-south traffic.
- North-south traffic - traffic into and out of the data center.
- Virtualization увеличила east-west traffic: server-to-server communication внутри data center.
- East-west traffic часто является основной нагрузкой modern data center.
- Traditional three-tier design может давать слишком много hops для server-to-server traffic.
- STP может блокировать redundant links, снижая usable bandwidth.
- Spine-leaf design: every leaf switch connects to every spine switch.
- В spine-leaf any server-to-server path обычно занимает максимум two hops: leaf -> spine -> leaf.
- Leaf-spine links часто являются Layer 3 links.
- Layer 3 spine-leaf помогает использовать all uplinks через load balancing и уменьшает зависимость от STP.
- Underlay - physical and routed foundation.
- Overlay - abstraction/segmentation/automation layer поверх underlay.
- Cisco Nexus - data center-focused switching platform.

## Notes

### Data Centers Are Different

Data center network не стоит воспринимать как просто larger office network. У data center другие traffic patterns, другие performance requirements и другая tolerance к latency, congestion и downtime.

Data centers поддерживают почти всё, чем мы пользуемся online:

- websites;
- applications;
- messaging;
- video streaming;
- databases;
- ordering platforms;
- business services.

Для NetworkChuck Coffee data center может означать:

- собственную server room;
- rented rack space в colocation facility;
- cloud services.

Важно: cloud всё равно означает data center. Просто hardware находится у cloud provider.

### What Companies Use Data Centers For

Data center не обязательно выглядит как огромный campus уровня Google. Иногда это одна room с несколькими racks, которая держит весь business.

Типичные workloads:

- company website;
- ordering platform;
- databases;
- internal applications;
- internet edge;
- file/storage systems;
- business-critical servers.

Многие companies живут в hybrid world:

| Location | Example |
| --- | --- |
| On premises | Local server room |
| Colocation | Rented rack space |
| Cloud | AWS, Azure, GCP |

Network engineer должен понимать, что это не отдельные миры. Это части одной business infrastructure, которую нужно reliable connect.

### Old Design: Three-Tier Data Center

Раньше data centers часто строили похожими на campus networks.

Traditional design:

```text
Servers -> Top-of-Rack switches -> Distribution -> Core
```

Top-of-Rack switch, или ToR, находится в rack и подключает servers этого rack.

Core switches были backbone, который связывал network together.

Такой model хорошо работал, когда main traffic pattern был user-to-server.

### North-South Traffic

North-south traffic - это traffic, который входит в data center или выходит из него.

Пример:

```text
User on internet -> Core -> Distribution -> ToR -> Server
Server -> ToR -> Distribution -> Core -> User
```

Такой pattern был common, когда clients в основном обращались к servers, а servers меньше общались между собой.

### Virtualization Changed Everything

Virtualization изменила traffic pattern.

Servers перестали быть isolated islands. Modern applications часто состоят из multiple services, databases, storage systems и clusters, которые постоянно общаются друг с другом.

Примеры east-west communication:

- app server talks to database server;
- web tier talks to application tier;
- virtual machines migrate or replicate;
- storage systems exchange data;
- clusters sync state.

### East-West Traffic

East-west traffic - это traffic внутри data center, особенно server-to-server.

В modern data centers east-west traffic может быть 70-80% всего traffic.

Это меняет design priority:

```text
Old priority: optimize users reaching servers.
Modern priority: optimize servers talking to servers.
```

### Problem With Traditional Three-Tier

В traditional three-tier design server-to-server traffic может проходить слишком длинный путь.

Пример:

```text
Rack A server
-> ToR/access
-> Distribution
-> Core
-> Distribution
-> ToR/access
-> Rack B server
```

Когда таких communications много, extra hops создают:

- higher latency;
- less predictable paths;
- congestion points;
- harder troubleshooting;
- inefficient bandwidth usage.

### STP Problem

STP, Spanning Tree Protocol, предотвращает Layer 2 loops.

Если между switches есть redundant Layer 2 links, STP может заблокировать часть links, чтобы network не попала в switching loop.

Это полезно для loop prevention, но больно для data center bandwidth.

Проблема:

```text
We install redundant links, but STP may block some of them.
```

В modern data center хочется использовать all available links, а не держать часть bandwidth idle.

### Spine-Leaf Design

Spine-leaf architecture решает проблемы old design.

Components:

- leaf switches connect to servers/racks;
- spine switches connect all leaf switches together;
- every leaf connects to every spine.

Basic design:

```text
Servers -> Leaf switches -> Spine switches -> Leaf switches -> Servers
```

Главная ценность:

```text
Any leaf to any other leaf = maximum two hops.
```

Path:

```text
Leaf -> Spine -> Leaf
```

Это дает predictable latency and forwarding behavior.

### Why Spine-Leaf Helps

Spine-leaf design хорошо подходит для east-west traffic.

Плюсы:

- predictable hop count;
- better scalability;
- better bandwidth usage;
- easier expansion by adding leaf/spine capacity;
- less dependency on blocked Layer 2 links;
- more consistent server-to-server performance.

Пример NetworkChuck Coffee:

```text
Application server in Rack A -> Leaf -> Spine -> Leaf -> Database server in Rack B
```

Вместо multiple layers and unpredictable path мы получаем simple consistent path.

### Layer 3 Leaf-Spine Links

Links между leaf и spine часто являются Layer 3 links.

Это значит:

- routing by IP;
- less reliance on Spanning Tree;
- all uplinks can stay active;
- traffic can be load balanced across multiple paths.

Layer 3 spine-leaf позволяет лучше использовать available bandwidth, потому что redundant paths не просто простаивают blocked.

### Cisco Nexus

В data center environments часто встречаются Cisco Nexus switches.

Сравнение:

| Environment | Common Cisco platform |
| --- | --- |
| Campus | Catalyst |
| Data center | Nexus |

Nexus switches ориентированы на data center throughput, low latency, high port density и modern data center features.

### Underlay and Overlay

В статье подчеркивается, что spine-leaf discussion - это mainly underlay.

Underlay - это physical and routed foundation:

- switches;
- links;
- IP routing;
- basic reachability.

Overlay - это layer поверх underlay:

- automation;
- abstraction;
- segmentation;
- software-defined networking;
- virtual networks.

Modern data centers часто используют both:

```text
Underlay moves packets.
Overlay provides abstraction and segmentation.
```

### Main Takeaway

Modern data centers are built to optimize east-west traffic.

Старые designs больше подходили для traffic между users и servers. Но modern applications, virtualization, storage и clusters требуют быстрых, predictable server-to-server paths.

Поэтому spine-leaf стал standard design для modern data center networking.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Data center | Facility or room where servers, storage and networking infrastructure run business services. |
| Colocation | Rented data center space where a company places its own equipment. |
| Cloud | Provider-managed data center infrastructure consumed as services. |
| Top-of-Rack (ToR) switch | Switch placed in a rack to connect servers in that rack. |
| North-south traffic | Traffic entering or leaving the data center. |
| East-west traffic | Traffic moving server-to-server inside the data center. |
| Three-tier design | Access/ToR, distribution and core architecture. |
| STP | Spanning Tree Protocol; prevents Layer 2 loops, sometimes by blocking redundant links. |
| Spine-leaf | Data center architecture where every leaf connects to every spine. |
| Leaf switch | Switch connecting servers/racks to the spine layer. |
| Spine switch | Switch providing fast interconnection between leaf switches. |
| Layer 3 link | Routed IP link, often used between leaf and spine switches. |
| Load balancing | Sharing traffic across multiple active paths. |
| Cisco Nexus | Cisco switching platform focused on data center environments. |
| Underlay | Physical and routed network foundation. |
| Overlay | Virtual/abstracted network layer built on top of the underlay. |

## Questions

### 1. Почему data center network - это не просто большая office network?

Потому что data centers имеют другие traffic patterns, особенно много server-to-server communication, и требуют predictable low-latency high-throughput design.

### 2. Что такое north-south traffic?

North-south traffic - это traffic, который входит в data center или выходит из него, например user-to-server traffic.

### 3. Что такое east-west traffic?

East-west traffic - это traffic внутри data center, особенно server-to-server communication.

### 4. Почему virtualization изменила data center networking?

Virtualization и modern applications увеличили количество communication между servers, storage systems, clusters и application components.

### 5. Почему traditional three-tier design стал проблемой для data centers?

Он может создавать too many hops и less predictable paths для east-west traffic.

### 6. Что делает STP и почему он может быть проблемой в data center?

STP предотвращает Layer 2 loops, но может блокировать redundant links, из-за чего часть bandwidth не используется.

### 7. Что такое spine-leaf architecture?

Spine-leaf - это architecture, где leaf switches подключают servers/racks, spine switches соединяют leaf switches, и каждый leaf подключен к каждому spine.

### 8. Какой максимальный путь между servers на разных leaf switches в spine-leaf design?

Обычно максимум two hops: leaf -> spine -> leaf.

### 9. Почему Layer 3 links между leaf и spine полезны?

Они позволяют routing, уменьшают зависимость от STP и помогают использовать multiple active paths через load balancing.

### 10. Что такое Cisco Nexus?

Cisco Nexus - это Cisco switching platform, ориентированная на data center environments.

### 11. Чем underlay отличается от overlay?

Underlay - physical and routed foundation. Overlay - abstraction/segmentation/automation layer поверх underlay.

### 12. Какая главная design priority modern data centers?

Оптимизировать east-west traffic: быстрый и predictable server-to-server communication.

## What To Review Later

- North-south vs east-west traffic.
- Why virtualization increased east-west traffic.
- Problems with traditional three-tier data center design.
- STP and blocked redundant links.
- Spine-leaf architecture.
- Leaf -> spine -> leaf two-hop model.
- Layer 3 leaf-spine links and load balancing.
- Underlay vs overlay.
