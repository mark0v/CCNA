# From Working VLANs To Layer 2 Optimization

Source: закрытая страница курса  
Date added: 2026-06-28  
Related plan item: Week 9 / Layer 2 optimization after VLAN deployment  
Tags: VLAN, STP, Layer 2, redundancy, trunk, router-on-a-stick, verification
Language: Russian
Translation pair: articles-en/2026-06/week-09/01-from-working-vlans-to-layer-2-optimization.md

## Кратко

Рабочая VLAN-сегментация - это не конец дизайна.

Это момент, когда сеть впервые начинает показывать, где Layer 2 topology сделана осознанно, а где она просто "как получилось".

В Fallout Shelter уже были построены:

- четыре VLAN;
- четыре subnet;
- default gateways для VLAN;
- DHCP scopes;
- access ports для конечных устройств;
- trunks между switches;
- router-on-a-stick для inter-VLAN routing.

После этого clients получили адреса, DHCP bindings появились, pings прошли, и сеть стала working segmented LAN.

Но именно после этого появился следующий вопрос:

```text
The network works.
But is the Layer 2 design optimal?
```

Это нормальный следующий этап. Сначала ты добиваешься connectivity. Потом проверяешь, как эта connectivity проходит через switching topology.

## Почему Working Не Значит Finished

Когда VLANs начинают работать, легко решить, что задача закончена.

Но VLAN implementation меняет не только switch config. Она меняет:

- broadcast domains;
- IP subnets;
- gateway placement;
- DHCP boundaries;
- trunk requirements;
- routing paths;
- security boundaries;
- troubleshooting model.

Если все это заработало, это значит только одно: базовая схема жизнеспособна.

Это еще не значит, что:

- redundancy используется правильно;
- traffic идет по ожидаемому пути;
- STP выбрал лучший root bridge;
- blocked ports находятся там, где ты хотел;
- uplinks используются эффективно;
- failure behavior понятен заранее.

Для production mindset это важная разница.

Lab может быть "green" по ping, но design все еще может быть слабым.

## Где Появляется STP

STP, Spanning Tree Protocol, защищает Layer 2 network от loops.

Если между switches есть redundant links, STP должен оставить topology loop-free. Для этого он может заблокировать один из путей.

Это правильно с точки зрения безопасности.

Но default STP decision не всегда совпадает с твоим design intent.

Например:

- root bridge может оказаться не на том switch;
- main uplink может быть blocked;
- traffic может идти через менее удобный path;
- backup link может стать active не там, где ты ожидал;
- разные VLANs могут использовать не те forwarding paths, которые ты планировал.

Сеть при этом может работать.

Именно поэтому простая проверка `ping` не отвечает на вопрос Layer 2 optimization.

`ping` говорит: "маршрут есть".

STP analysis говорит: "сеть использует правильный Layer 2 path или просто нашла любой безопасный path?"

## Что Проверять После VLAN Deployment

После того как VLANs, trunks, DHCP и router-on-a-stick заработали, проверь Layer 2 behavior отдельным этапом.

Минимальный checklist:

```text
1. Какие switches участвуют в VLAN path?
2. Какие links являются trunks?
3. Какие VLANs allowed на каждом trunk?
4. Где STP root bridge для каждой VLAN?
5. Какие ports forwarding?
6. Какие ports blocking?
7. Совпадает ли forwarding path с design?
8. Что произойдет при отказе active uplink?
```

Это уже не настройка одной команды.

Это проверка того, что topology ведет себя предсказуемо.

## Почему Redundancy Может Обмануть

Redundancy часто выглядит хорошо на diagram.

Два uplinks лучше, чем один. Несколько paths лучше, чем один path. Несколько switches лучше, чем single point of failure.

Но в Layer 2 redundant links без loop prevention опасны.

Поэтому STP блокирует часть topology.

Проблема не в том, что STP блокирует link. Это его работа.

Проблема появляется, когда blocked link оказывается не тем, который ты ожидал.

Пример мышления:

```text
I built redundancy.
STP made it safe.
Now I must make it intentional.
```

То есть надо не просто радоваться, что loop не случился. Надо понимать, какой switch управляет tree, какие links активны, какие links standby, и насколько быстро сеть восстановится после failure.

## Связь С VLAN Design

VLAN design и STP design связаны.

Каждая VLAN - отдельный broadcast domain. Если topology использует multiple switches и trunks, то каждая VLAN должна иметь понятный Layer 2 path.

В простой lab topology это может выглядеть очевидно.

В реальной сети быстро появляются вопросы:

- Management VLAN должна идти через тот же uplink, что guest VLAN?
- Video traffic должен использовать отдельный preferred path?
- Guest VLAN должна иметь доступ только до firewall/router?
- Где должен быть root bridge для critical VLANs?
- Нужно ли распределять load между links для разных VLANs?

Пока сеть маленькая, эти вопросы можно игнорировать.

Но именно маленькая lab дает шанс научиться видеть их без production pressure.

## Practical Verification Flow

После VLAN deployment не ограничивайся проверкой IP.

Проверяй layers по порядку.

### 1. VLAN Database

Убедись, что VLANs существуют там, где должны существовать.

```text
show vlan brief
```

Проверь:

- VLAN IDs;
- VLAN names;
- access port membership.

### 2. Trunks

Проверь, что switch-to-switch links и router-facing link действительно trunk.

```text
show interfaces trunk
```

Проверь:

- trunk status;
- native VLAN;
- allowed VLANs;
- VLANs active in management domain.

### 3. Router-On-A-Stick

Проверь, что router subinterfaces соответствуют VLAN tags.

```text
show ip interface brief
show running-config interface ...
```

Ищи:

- correct encapsulation dot1Q;
- correct gateway IP;
- interface up/up;
- no missing trunk on the switch side.

### 4. DHCP

Проверь, что clients получают адреса из правильных scopes.

```text
show ip dhcp binding
```

Для каждого client проверь:

- IP address;
- subnet mask;
- default gateway;
- DNS, если он нужен в lab;
- VLAN membership на switch port.

### 5. STP

Теперь переходи к Layer 2 optimization.

```text
show spanning-tree
show spanning-tree vlan 10
show spanning-tree vlan 20
show spanning-tree vlan 30
show spanning-tree vlan 40
```

Проверь:

- root bridge;
- root port;
- designated ports;
- blocked ports;
- bridge priority;
- port cost;
- whether the path matches the design.

## Что Считать Красным Флагом

После VLAN implementation обрати внимание на такие признаки:

- STP root bridge выбран случайно;
- access switch стал root bridge без причины;
- trunk blocked там, где ожидался main uplink;
- important VLANs идут через indirect path;
- DHCP работает только в части VLANs;
- inter-VLAN routing работает, но traffic path выглядит странно;
- documentation не отражает real forwarding topology.

Это не всегда означает, что сеть "сломана".

Но это означает, что design еще не управляемый.

## Главный Вывод

VLANs дают segmentation.

Router-on-a-stick дает inter-VLAN routing.

DHCP scopes дают automatic addressing.

Но Layer 2 optimization отвечает на другой вопрос:

```text
Does the switching topology behave the way we intended?
```

После Fallout Shelter VLAN implementation сеть уже работала. Следующий профессиональный шаг - посмотреть на STP behavior, root bridge placement, blocked links и redundancy design.

Рабочая сеть - это baseline.

Предсказуемая сеть - это цель.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| STP | Spanning Tree Protocol. Layer 2 protocol that prevents loops by blocking redundant paths. |
| Root bridge | Switch that becomes the reference point for STP path calculation. |
| Blocked port | STP port state where the port does not forward user traffic to prevent a loop. |
| Forwarding port | STP port state where the port forwards frames. |
| Trunk | Switch link that carries traffic for multiple VLANs using VLAN tags. |
| Router-on-a-stick | Inter-VLAN routing design where one physical router interface uses multiple subinterfaces. |
| Design intent | The intended traffic path and failure behavior, not just whatever the protocol selected by default. |

## Questions

### 1. Why is a working VLAN deployment not automatically finished?

Answer:

Because connectivity proves that the basic configuration works, but it does not prove that Layer 2 paths, redundancy, STP root placement, and failure behavior match the intended design.

### 2. What problem does STP solve?

Answer:

STP prevents Layer 2 loops by placing some redundant paths into a non-forwarding state when needed.

### 3. What should you check after DHCP and pings start working?

Answer:

Check VLAN membership, trunk status, allowed VLANs, router subinterfaces, DHCP bindings, and then STP behavior: root bridge, forwarding ports, blocked ports, and whether traffic follows the expected path.

## What To Review Later

- STP root bridge selection.
- STP port roles and port states.
- Per-VLAN STP behavior.
- EtherChannel as a better way to use multiple physical links.
- How to document intended Layer 2 forwarding paths.
