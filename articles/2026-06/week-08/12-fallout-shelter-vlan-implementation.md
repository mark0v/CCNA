# Fallout Shelter VLAN Implementation

Source: закрытая страница курса  
Date added: 2026-06-20  
Related plan item: Week 8 / Fallout Shelter VLAN implementation  
Tags: VLAN, subnetting, VTP, DTP, router-on-a-stick, DHCP, STP, segmentation
Language: Russian
Translation pair: articles-en/2026-06/week-08/12-fallout-shelter-vlan-implementation.md

## Кратко

VLAN implementation - это не маленькая правка switch config.

Когда ты внедряешь VLAN architecture, ты одновременно меняешь:

- logical network structure;
- IP addressing;
- subnets;
- default gateways;
- DHCP scopes;
- traffic paths;
- routing behavior;
- security boundaries;
- troubleshooting model.

Для Fallout Shelter network задача пришла из RFP, Request for Proposal. Business language не говорил "создай VLANs", но требования уже задавали VLAN design.

Нужно было четыре isolated network segments:

- management traffic;
- internal communication;
- video surveillance;
- guest access.

Это сразу превращается в:

```text
Four segments
Four VLANs
Four subnets
Four gateways
Four DHCP scopes
```

## VLANs - Это Redesign

Фраза "implement VLANs" может звучать как небольшая настройка.

На самом деле это redesign.

Почему:

- каждая VLAN является отдельным broadcast domain;
- каждая VLAN обычно получает отдельную IP subnet;
- для каждой subnet нужен default gateway;
- DHCP должен выдавать addresses из правильного pool;
- routing должен понимать все networks;
- security policies должны учитывать новые boundaries;
- switch ports должны быть назначены в правильные VLANs;
- trunk links должны переносить нужные VLANs.

Если сделать только часть работы, сеть будет выглядеть настроенной, но работать нестабильно.

## Исходный Address Block

Для Fallout Shelter был выделен larger subnet:

```text
10.0.16.0/23
```

Один `/23` дает большой address block, но business requirement требовал не одну flat network, а четыре separated segments.

Поэтому `/23` был split into four `/25` subnets.

Почему `/25`?

`/23` содержит 512 total addresses.

Если разделить его на четыре равные части, получится:

```text
/23 -> four /25 networks
```

Каждый `/25` дает:

```text
128 total addresses
126 usable host addresses
```

Для shelter с примерно 50 people этого достаточно с запасом.

## VLAN And Subnet Mapping

Логическая схема:

```text
VLAN 10 -> Management
VLAN 20 -> Internal users
VLAN 30 -> Video surveillance
VLAN 40 -> Guest access
```

Адресная идея:

```text
10.0.16.0/25    -> VLAN 10 Management
10.0.16.128/25  -> VLAN 20 Internal
10.0.17.0/25    -> VLAN 30 Video
10.0.17.128/25  -> VLAN 40 Guest
```

Так один shelter-wide `/23` остается внутри larger address plan, но превращается в четыре useful networks.

VLAN numbering через десятки тоже помогает:

```text
10, 20, 30, 40
```

Если позже понадобится новая related VLAN, можно вставить:

```text
11, 12, 21, 31
```

Это не жесткое правило, а удобная operational habit.

## Management VLAN

Management VLAN - это сеть для administrative access к infrastructure devices.

Например:

- SSH на switches;
- SSH на routers;
- web interfaces;
- monitoring;
- device management;
- controller communication.

Management traffic важно отделять от обычного user traffic.

Если обычные user devices могут напрямую обращаться к management interfaces switches и routers, attack surface становится гораздо шире.

Правильная идея:

```text
Being plugged into the building should not mean being able to manage infrastructure.
```

Management VLAN должна быть restricted и accessible only для administrators или trusted management systems.

## Segment By Risk, Not Only By Department

VLAN design часто объясняют через departments:

```text
Accounting VLAN
Sales VLAN
Engineering VLAN
```

Но в production полезно думать шире: segment by risk.

Вопрос:

```text
Какие systems не должны быть casually reachable с обычных user devices?
```

Этот вопрос приводит к хорошей segmentation:

- management отдельно;
- guest отдельно;
- video surveillance отдельно;
- internal users отдельно;
- payment systems отдельно, если они есть;
- servers отдельно, если design этого требует.

## VTP В Lab

В этом уроке использовался VTP, VLAN Trunking Protocol, чтобы replicate VLAN information между switches.

Важно:

```text
VTP does not create trunk links.
VTP shares VLAN database information over trunk links.
```

То есть сначала trunk links должны работать, а уже потом VLAN database может распространяться через VTP.

Lab flow:

1. Создать VLANs на одном switch.
2. Настроить switch-to-switch links как trunks.
3. Убедиться, что VTP domain/mode позволяют propagation.
4. Проверить, что VLANs появились на других switches.

## DTP И Trunks

DTP, Dynamic Trunking Protocol, может помочь ports negotiated trunk mode.

В lab links были в dynamic auto.

Если обе стороны dynamic auto, trunk не formed:

```text
auto + auto -> no trunk
```

Когда uplinks были переведены в dynamic desirable, trunk links came up:

```text
desirable + auto -> trunk
```

Это полезно для понимания DTP behavior.

Но в production обычно лучше явно настраивать trunks:

```text
switchport mode trunk
```

и не полагаться на negotiation без причины.

## VTP Risk

VTP удобен, потому что VLAN database можно создать один раз и распространить на switches.

Но тот же механизм может распространить ошибку.

Если удалить VLAN на VTP server, deletion может propagate across domain.

Последствия:

- VLAN disappears на other switches;
- access ports теряют expected VLAN;
- users/devices lose connectivity;
- troubleshooting становится болезненным.

Поэтому modern best practice часто:

```text
Use VTP transparent
or avoid VTP unless intentionally designed
```

В lab VTP полезен как учебная демонстрация. В production его нужно использовать очень осторожно.

## Access Ports

Когда VLANs появились на switches, end-device ports были назначены в нужные VLANs.

Access port принадлежит одной VLAN.

Например:

```text
PC in Management -> access VLAN 10
Internal user PC -> access VLAN 20
Camera device    -> access VLAN 30
Guest device     -> access VLAN 40
```

Пример команды:

```text
interface fastEthernet0/5
 switchport mode access
 switchport access vlan 20
```

Это превращает design в реальное Layer 2 membership.

## Router-On-A-Stick

После segmentation возникает вопрос:

```text
How do these separate networks talk to each other?
```

Ответ: inter-VLAN routing.

В этом implementation использовался router-on-a-stick.

Один physical router interface подключается к switch через trunk.

На router создаются subinterfaces:

```text
G0/0.10 -> VLAN 10
G0/0.20 -> VLAN 20
G0/0.30 -> VLAN 30
G0/0.40 -> VLAN 40
```

Каждая subinterface получает:

- `encapsulation dot1Q <vlan-id>`;
- IP address из соответствующей subnet;
- роль default gateway для своей VLAN.

Пример:

```text
interface g0/0.10
 encapsulation dot1Q 10
 ip address 10.0.16.1 255.255.255.128
```

## DHCP Scopes

Для каждой VLAN нужен свой DHCP scope.

Иначе devices не получат правильные:

- IP address;
- subnet mask;
- default gateway;
- DNS server.

Пример structure:

```text
DHCP pool MGMT   -> VLAN 10 subnet
DHCP pool USERS  -> VLAN 20 subnet
DHCP pool VIDEO  -> VLAN 30 subnet
DHCP pool GUEST  -> VLAN 40 subnet
```

Каждый pool должен указывать default router своей VLAN.

## Router-Facing Switch Port Must Be Trunk

Одна из типичных ошибок: router subinterfaces настроены, DHCP pools созданы, VLANs существуют, но switch port к router не trunk.

Тогда router ожидает tagged VLAN traffic, а switch не отправляет его как trunk traffic.

Симптом:

- DHCP не работает;
- clients могут получить `169.254.x.x`;
- subinterfaces выглядят настроенными, но traffic до них не доходит.

Fix:

```text
interface gigabitEthernet0/1
 switchport mode trunk
```

После этого DHCP bindings начали появляться, clients получили addresses из правильных subnets, и inter-VLAN communication заработала.

## Проверка

Рабочую реализацию нужно подтверждать тестами.

Проверяй:

- VLANs существуют на switches;
- trunks подняты;
- нужные VLANs allowed on trunks;
- access ports в правильных VLANs;
- router subinterfaces up/up;
- DHCP bindings появляются;
- clients получают correct IP/subnet/gateway;
- ping работает там, где routing должен разрешать traffic;
- ping не работает там, где segmentation должна запрещать traffic;
- traceroute показывает expected router path.

Полезные команды:

```text
show vlan
show interfaces trunk
show ip interface brief
show ip dhcp binding
show running-config interface ...
```

## STP Уже Показывает Следующую Проблему

К концу implementation segmented LAN заработала.

Но redundant links в switching design начали показывать STP behavior.

STP, Spanning Tree Protocol, предотвращает Layer 2 loops, блокируя лишние paths.

Это хорошо для safety.

Но default STP choices не всегда optimal.

Network может function correctly, но не идеально:

- некоторые links blocked;
- traffic path может быть awkward;
- redundancy есть, но используется не так, как хотелось бы;
- root bridge placement может быть не intentional.

Это создает следующий этап: Layer 2 optimization.

## Что Было Построено

В результате implementation:

- один `/23` был разделен на четыре `/25`;
- создано четыре VLANs;
- VLAN database replicated across switching environment;
- ports назначены как access для test endpoints;
- trunks подняты между switches;
- router-on-a-stick обеспечил inter-VLAN routing;
- DHCP scopes начали выдавать addresses автоматически;
- pings подтвердили connectivity;
- STP показал, что topology работает, но требует optimization.

Это уже не "создать VLAN". Это полноценный network redesign.

## Главный Вывод

VLANs are not a small change.

Одна новая VLAN означает:

- new broadcast domain;
- new subnet;
- new gateway;
- new DHCP scope;
- new routing consideration;
- new security boundary;
- new troubleshooting path.

В Fallout Shelter мы построили working segmented LAN. Теперь сеть стала более organized и secure, но следующий вопрос уже виден: как сделать Layer 2 redundancy не просто safe, а intentional и efficient.

Именно туда ведут следующие темы: STP behavior, STP tuning, EtherChannel и более mature switching design.

