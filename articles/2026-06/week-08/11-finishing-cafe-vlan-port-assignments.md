# Finishing Cafe VLAN Port Assignments

Source: закрытая страница курса  
Date added: 2026-06-20  
Related plan item: Week 8 / Completing cafe VLAN implementation  
Tags: VLAN, access port, trunk port, WAP, dead VLAN, switch hardening, VLAN 1
Language: Russian
Translation pair: articles-en/2026-06/week-08/11-finishing-cafe-vlan-port-assignments.md

## Кратко

VLAN design не закончен, пока каждый switch port не получил правильную роль.

Можно создать VLANs, настроить router-on-a-stick, добавить DHCP pools и subinterfaces, но сеть все равно будет broken, если ports остались в default VLAN или работают в неправильном mode.

Полная VLAN implementation включает:

- trunks между switches;
- trunks к устройствам, которые несут multiple VLANs;
- access ports для endpoints;
- правильное VLAN membership для каждого live device;
- disabled unused ports;
- dead VLAN для неиспользуемых ports;
- отключение trunk negotiation там, где оно не нужно.

Главная идея:

```text
VLAN exists as design only when switch ports enforce it.
```

## VLAN Не Заканчивается На Создании VLAN

Создать VLAN:

```text
vlan 10
name ADMIN
```

это только начало.

Настроить subinterface на router:

```text
interface g0/0.10
encapsulation dot1Q 10
ip address ...
```

это тоже только часть.

Чтобы device реально оказался в нужной VLAN, port, куда он подключен, должен быть назначен в эту VLAN.

Если device остается plugged into port в VLAN 1, он не становится частью VLAN 10 только потому, что IP address выглядит похожим на admin subnet.

Layer 2 membership и Layer 3 addressing должны совпадать.

## Access Ports И Trunk Ports

В этом rollout нужно решить, какие ports являются access, а какие trunk.

Access port:

```text
Carries one VLAN
Usually connects to endpoint
```

Trunk port:

```text
Carries multiple VLANs
Usually connects to infrastructure or multi-VLAN device
```

Примеры access ports:

- PC;
- printer;
- server with one VLAN;
- camera;
- POS terminal.

Примеры trunk ports:

- switch-to-switch link;
- switch-to-router link for ROAS;
- switch-to-firewall link with multiple VLANs;
- wireless access point with multiple SSIDs;
- virtualization host carrying multiple VLANs.

## WAP Может Быть Trunk

WAP означает Wireless Access Point.

Он похож на switch for the air: wireless clients подключаются к нему без кабеля, но AP все равно переносит network traffic.

Если WAP обслуживает один SSID и одну VLAN, access port может быть enough.

Но если WAP будет обслуживать несколько SSIDs:

```text
Admin Wi-Fi  -> VLAN 10
Patron Wi-Fi -> VLAN 20
```

то switch port к WAP должен переносить traffic нескольких VLANs.

Это trunk.

AP будет tagging traffic, чтобы switch понимал:

```text
This wireless client traffic belongs to VLAN 10.
This wireless client traffic belongs to VLAN 20.
```

Правило:

```text
One VLAN -> access
Multiple VLANs -> trunk
```

## Plex Server И Layer 2/Layer 3 Mismatch

Хороший troubleshooting example - Plex server.

У него был IP address из admin network, но он все равно не мог communicate.

Причина: switch port, куда он был подключен, оставался в VLAN 1.

Это классическая ошибка:

```text
IP address looks correct
But switchport VLAN membership is wrong
```

Layer 3 говорит:

```text
This host belongs to admin subnet.
```

Layer 2 говорит:

```text
This port belongs to VLAN 1.
```

И сеть не сходится.

После назначения port как access port в VLAN 10 connectivity вернулась:

```text
switchport mode access
switchport access vlan 10
```

## Почему VLAN 1 "Потемнела"

Ранее IP address был removed с physical router interface, а routing перенесен на subinterfaces.

Это означает, что default VLAN 1 больше не имела normal router path, если для нее не была создана отдельная subinterface/gateway.

Устройства, которые остались в VLAN 1, оказались stranded.

Коротко:

```text
No router interface for VLAN 1
No default gateway path
Devices left in VLAN 1 lose connectivity
```

Поэтому важно не оставлять live devices случайно в VLAN 1.

## Subnet Mask Тоже Должна Совпадать

В уроке также была исправлена subnet mask на server.

Это важный остаточный эффект изменений.

Если сеть была split на smaller subnets, device может сохранить старую mask.

Например:

```text
Old design: /26
New VLAN subnet: /27
```

Если host остался с old mask, он может неправильно считать, какие addresses local, а какие remote.

После изменения infrastructure всегда проверяй:

- IP address;
- subnet mask;
- default gateway;
- VLAN membership;
- DHCP/static source;
- DNS;
- reachability.

## Unused Ports Не Безопасны По Умолчанию

Неиспользуемый switch port - это не просто пустой port.

Это potential access point.

Если кто-то может подключить device к открытому port и сразу получить network access, это security risk.

Best practice для unused ports:

1. Set as access ports.
2. Place into unused/dead VLAN.
3. Shut them down.

Пример:

```text
vlan 999
name DEAD_UNUSED

interface range fa0/16 - 24
switchport mode access
switchport access vlan 999
shutdown
```

## Почему Access Mode Даже Для Unused Ports

Unused port тоже лучше явно сделать access port.

Причина: если port остается dynamic, он может попытаться negotiate trunk через DTP.

Если кто-то подключит switch или устройство, которое умеет negotiated trunk, может появиться unwanted trunk.

Поэтому:

```text
switchport mode access
switchport access vlan 999
shutdown
```

Так port:

- не работает физически из-за shutdown;
- если его случайно включат, он попадет в dead VLAN;
- не будет negotiated trunk;
- не даст access к production VLANs.

## Convenience Vs Security

В real networks не везде unused ports жестко отключены.

Например, в campus environments или офисах, где users постоянно двигают desks, phones и docking stations, admins иногда оставляют ports активными ради удобства.

Но в regulated или sensitive environments auditors могут спросить:

```text
Why are unused ports active?
```

Поэтому design зависит от environment.

Если security важнее convenience, unused ports должны быть locked down.

## Что Значит "VLAN Rollout Done"

К концу rollout cafe switch должен иметь intentional behavior на каждом interface.

Пример результата:

```text
Switch-to-switch links -> trunks
Switch-to-router link  -> trunk
WAP uplinks            -> trunks
PC/server ports        -> access ports in correct VLANs
Unused ports           -> access ports in dead VLAN, shutdown
```

Это и есть complete VLAN implementation.

Не просто:

```text
VLANs exist.
```

А:

```text
Every port has a purpose.
Every live device belongs somewhere.
Every unused opening is treated as risk.
```

## Checklist

Перед тем как считать VLAN configuration законченной, проверь:

- VLANs созданы и названы;
- access ports назначены в правильные VLANs;
- trunk ports настроены там, где нужно;
- WAP/multi-SSID links работают как trunks;
- router/firewall links работают как trunks, если используют subinterfaces;
- devices получили correct IP/subnet/gateway;
- hosts не остались случайно в VLAN 1;
- unused ports находятся в dead VLAN;
- unused ports shutdown;
- dynamic trunk negotiation отключен там, где не нужен;
- `show vlan` и `show interfaces trunk` подтверждают design.

## Главный Вывод

Cafe VLAN rollout показывает разницу между design и implementation.

Design говорит:

```text
Admin devices belong to VLAN 10.
Patron devices belong to VLAN 20.
```

Implementation доказывает это на каждом switch port.

Если port не назначен правильно, design остается только картинкой.

Сеть начинает вести себя правильно только тогда, когда:

- Layer 2 VLAN membership;
- Layer 3 addressing;
- default gateway;
- trunk/access roles;
- security posture

согласованы между собой.

Теперь cafe network стала clean proving ground, а те же идеи можно переносить в более крупную Fallout Shelter topology.

