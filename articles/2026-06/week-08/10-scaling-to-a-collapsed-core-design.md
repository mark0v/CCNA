# Scaling To A Collapsed Core Design

Source: закрытая страница курса  
Date added: 2026-06-20  
Related plan item: Week 8 / Scaling the lab topology  
Tags: collapsed core, access layer, distribution layer, STP, HSRP, redundancy, Packet Tracer
Language: Russian
Translation pair: articles-en/2026-06/week-08/10-scaling-to-a-collapsed-core-design.md

## Кратко

Маленькая cafe network хороша для первых labs. Несколько switches и router достаточно, чтобы понять VLANs, trunks и базовую routing логику.

Но для более серьезных тем такая сеть слишком маленькая. Она не заставляет думать о:

- redundancy;
- failure impact;
- access и distribution layers;
- STP behavior;
- gateway resilience;
- design trade-offs;
- росте сети;
- downstream locations.

Поэтому lab расширяется до Fallout Shelter network - более крупной среды, где design choices начинают иметь реальные последствия.

Главный переход:

```text
Small network teaches features.
Larger network teaches consequences.
```

## Почему Маленькой Сети Уже Недостаточно

SOHO network, то есть small office/home office, может быть простой:

```text
Router
Two switches
Several clients
Basic VLANs
Basic routing
```

Для первых уроков этого хватает.

Но когда появляются VLANs, redundancy, STP, HSRP и более серьезный switching design, слишком маленькая topology скрывает причины, зачем эти технологии нужны.

Если в сети всего один switch path и один router path, ты не чувствуешь:

- что будет при отказе switch;
- что будет при отказе router;
- почему loop prevention важен;
- почему redundant links могут быть blocked;
- почему gateway failover нужен users;
- почему traffic path может быть не optimal.

Большая topology делает эти вопросы видимыми.

## Fallout Shelter Как Более Реалистичная Среда

Fallout Shelter network поддерживает около 50 people и множество downstream locations.

Это уже не просто "один маленький офис".

Если такой site падает, impact может затронуть:

- connected shops;
- services;
- business operations;
- users в нескольких locations;
- communication paths;
- access to shared resources.

Здесь network failure становится business problem.

Поэтому design должен учитывать не только number of users, но и:

- physical layout;
- business criticality;
- growth;
- redundancy;
- operational support;
- future services.

## От "Подключить Devices" К Architecture

В cafe network мы в основном изучали features.

В Fallout Shelter нужно думать уже как о network architecture.

Появляется более structured design:

- access switches;
- distribution switches;
- redundant links;
- routers;
- future VLAN segmentation;
- future HSRP;
- STP behavior.

Это не обязательно огромная enterprise network, но она уже похожа на real design, а не просто на учебный набор devices.

## Collapsed Core Design

Collapsed core design - это design, где core и distribution responsibilities объединены в один слой.

В классической трехуровневой модели есть:

```text
Access layer
Distribution layer
Core layer
```

В collapsed core:

```text
Access layer
Collapsed core / distribution layer
```

То есть отдельного core layer нет. Distribution switches одновременно выполняют роль aggregation и core-like forwarding внутри site.

Такой design часто подходит для:

- single building;
- medium office;
- campus building;
- небольшого enterprise site;
- environments, где отдельный core layer был бы overkill.

## Access Layer

Access layer - это место, где подключаются endpoints.

Например:

- PCs;
- laptops;
- printers;
- cameras;
- access points;
- phones;
- POS terminals;
- IoT devices.

Access switches ближе всего к users и devices.

Именно здесь обычно настраивают:

- access ports;
- VLAN assignment;
- port security;
- edge STP features;
- voice VLAN;
- endpoint-facing policies.

## Distribution Layer

Distribution layer агрегирует access switches.

Здесь появляются более серьезные responsibilities:

- aggregation access switches;
- routing boundary;
- policy enforcement;
- VLAN boundaries;
- uplinks toward routers/services;
- redundant paths;
- gateway services;
- traffic control.

В collapsed core design distribution layer также выполняет роль local core для site.

## Почему Design Может Выглядеть "Слишком Мощным"

Если environment поддерживает около 50 people, topology может выглядеть крупнее, чем ожидаешь.

Но number of users - не единственный фактор.

Design определяется также:

- сколько downstream locations зависят от site;
- насколько важен uptime;
- где physically расположены devices;
- какой growth ожидается;
- какие services будут добавлены позже;
- какой failure impact допустим.

Небольшой site может заслуживать серьезную redundancy, если его outage влияет на many stores или key services.

## Redundant Links

В topology access switches подключаются к двум distribution switches.

Routers тоже подключаются redundantly.

Цель:

```text
If one switch fails, another path remains.
If one router fails, another path can take over.
```

Это не overkill, если site важен для business.

Redundancy нужна, чтобы отказ одного элемента не превращался сразу в outage для всех.

## HSRP В Будущем

HSRP означает Hot Standby Router Protocol.

Он позволяет двум routers выглядеть для clients как один default gateway.

Идея:

```text
Router A active
Router B standby
Clients use virtual gateway IP
If Router A fails, Router B takes over
```

Users не должны вручную менять gateway. Devices продолжают использовать тот же virtual default gateway.

HSRP становится полезным именно в topology, где есть redundant routers.

## Когда Нужен Отдельный Core Layer

Collapsed core может масштабироваться достаточно далеко.

В зависимости от hardware и layout он может поддерживать:

- hundreds of users;
- иногда low thousands;
- один building;
- несколько floors;
- medium site.

Отдельный core layer обычно появляется, когда нужно соединять multiple buildings или крупные части campus.

Пример:

```text
Building A: 500 users
Building B: 200 users
Building C: 300 users
```

Тогда core layer становится high-speed backbone между distribution blocks разных buildings.

## Addressing Для Fallout Shelter

Для Fallout Shelter уже был выделен subnet:

```text
10.0.16.0/23
```

Это address range для этой environment.

На этом этапе цель не в полной настройке всех VLANs и routing features, а в создании physical и logical foundation.

Дальше на эту foundation будут накладываться:

- VLANs;
- trunks;
- STP;
- HSRP;
- routing;
- switch optimization.

## Packet Tracer И Topology

Topology была добавлена в Packet Tracer под cafe network.

Так проще:

- сравнивать маленькую и большую implementation;
- видеть оба designs;
- быстро переключаться между ними;
- не усложнять lab physical views;
- сфокусироваться на network behavior.

Иногда лучше держать lab визуально простой, если цель - понять design и protocols.

## Red Links

Красные links на router interfaces в Packet Tracer обычно означают, что interfaces shutdown.

На routers interfaces часто выключены по умолчанию.

Это исправляется later через:

```text
no shutdown
```

Такой red state не обязательно означает сложную проблему. Часто interface просто еще не включен.

## Orange Links И STP

Orange links в switching topology часто намекают, что Spanning Tree Protocol уже работает.

STP предотвращает Layer 2 loops.

Если в switching network есть redundant physical links, без STP могут появиться:

- broadcast storms;
- duplicate frames;
- MAC table instability;
- network meltdown.

STP может заблокировать некоторые links, чтобы network не создала loop.

Важно понимать:

```text
More cables does not automatically mean more active bandwidth.
```

Если STP заблокировал link, этот link дает standby redundancy, а не active forwarding.

## Почему Default STP Может Быть Неидеален

STP защищает от loops, но default path selection не всегда optimal.

Network может работать, но traffic может идти awkward path:

- через лишний switch;
- через не лучший uplink;
- через менее desirable distribution switch;
- с неэффективным root bridge placement.

Именно поэтому позже нужны:

- STP tuning;
- intentional root bridge selection;
- EtherChannel;
- VLAN-aware design;
- topology planning.

## Почему Сначала Строится "Неидеальная" Сеть

Можно сразу построить идеальную topology и скрыть messy parts.

Но в real networking часто происходит иначе:

1. Строишь baseline.
2. Наблюдаешь behavior.
3. Видишь blocked links и strange paths.
4. Понимаешь, почему protocol выбрал такой path.
5. Оптимизируешь design.

Так обучение становится реальнее.

Сначала полезно увидеть imperfect behavior, чтобы потом понимать, зачем нужны STP tuning, HSRP и switch optimization.

## Главный Вывод

Этот урок переводит lab из tiny network в topology, которая может поддерживать более глубокие CCNA topics.

Cafe network была хороша для basics.

Fallout Shelter network нужна для:

- VLAN design в более крупной среде;
- redundant switching paths;
- STP behavior;
- future HSRP;
- gateway resilience;
- collapsed core architecture;
- real design trade-offs.

Коротко:

```text
Small topology shows commands.
Larger topology shows consequences.
```

Теперь есть environment, где VLANs, STP, HSRP и switching optimization будут выглядеть не как отдельные темы, а как части одной живой сети.

