# Configuring HSRP With Failover Testing

Source: закрытая страница курса  
Date added: 2026-07-18  
Related plan item: Week 12 / Configuring HSRP with failover testing  
Tags: HSRP, first hop redundancy, default gateway, NAT, OSPF, failover, preempt, interface tracking
Language: Russian
Translation pair: articles-en/2026-07/week-12/01-configuring-hsrp-with-failover-testing.md

## Summary

- HSRP дает хостам один стабильный default gateway, даже если физический router меняется.
- Сама команда `standby` не спасает сеть, если заранее не настроены routing, NAT, trunks и VLAN subinterfaces.
- В HSRP active router отвечает за virtual IP, standby router готов принять роль при отказе.
- Priority выбирает active router; preempt возвращает preferred router в active role после восстановления.
- Failover нужно проверять практически: pings, NAT translations, HSRP state и controlled link failure.
- Interface tracking нужен, чтобы router не оставался active, если потерял важный upstream link.

## Key Points

- HSRP is Cisco Hot Standby Router Protocol.
- First hop redundancy защищает первый Layer 3 hop для hosts, обычно default gateway.
- Physical router IP и gateway IP лучше разделять: real IP остаются на routers, virtual IP дают hosts.
- HSRPv2 включается командой `standby version 2`.
- Higher priority wins; default priority is 100.
- If priorities tie, higher interface IP wins.
- `preempt` позволяет preferred router вернуть active role после recovery.

## Notes

HSRP часто выглядит как маленькая настройка: несколько команд на interface, virtual IP, priority, preempt. Но настоящая работа начинается раньше. Нужно, чтобы второй router уже умел выйти в internet, видел VLANs, участвовал в routing и делал NAT.

Если этот фундамент сломан, HSRP только красиво прикроет плохую схему. Redundancy должна быть end-to-end, а не только в одном месте diagram.

## Before HSRP: Plumbing First

В lab второй internet connection был эмулирован через switch. Для Packet Tracer это удобно: можно показать два WAN handoff и проверить поведение routers.

В real world так проектировать нельзя бездумно. Если оба "резервных" канала приходят через один carrier, один ввод в здание или одну физическую трассу, backhoe может оборвать оба сразу. Второй circuit должен быть действительно независимым настолько, насколько это возможно по бюджету и доступности.

Перед HSRP нужно подготовить второй router:

- WAN-facing interface;
- default route toward ISP;
- router-on-a-stick subinterfaces for VLANs;
- trunk до switch;
- OSPF или другой routing exchange с остальной сетью;
- NAT for inside networks.

HSRP не заменяет routing и NAT. Он только дает end devices virtual default gateway, которому можно доверять.

## The Default Gateway Problem

Проблема простая: PC in VLAN 10 использует default gateway `10.0.16.1`. Если этот IP живет только на Router 1, то при отказе Router 1 PC продолжит отправлять traffic на мертвый gateway.

Host сам не решит перейти на Router 2. Для него default gateway - это конкретный IP address.

HSRP решает это через virtual IP:

- Router 1 имеет свой real interface IP;
- Router 2 имеет свой real interface IP;
- hosts используют общий virtual gateway IP;
- active router отвечает за этот virtual IP;
- standby router ждет и принимает роль при отказе.

Практичный шаблон адресов:

| Address role | Example |
| --- | --- |
| HSRP virtual IP | `10.0.16.1` |
| Router 1 real IP | `10.0.16.2` |
| Router 2 real IP | `10.0.16.3` |

Так clients сохраняют знакомый gateway address, но этот address больше не привязан к одному physical router.

## HSRPv2 Configuration Pattern

На каждом VLAN subinterface HSRP настраивается отдельно. Group number удобно делать равным VLAN number: это проще читать и troubleshoot.

Example for VLAN 10 on preferred router:

```text
interface g0/0.10
 encapsulation dot1Q 10
 ip address 10.0.16.2 255.255.255.0
 standby version 2
 standby 10 ip 10.0.16.1
 standby 10 priority 105
 standby 10 preempt
```

Example for VLAN 10 on standby router:

```text
interface g0/0.10
 encapsulation dot1Q 10
 ip address 10.0.16.3 255.255.255.0
 standby version 2
 standby 10 ip 10.0.16.1
 standby 10 preempt
```

Та же логика повторяется для других VLANs. У каждого subnet будет свой virtual gateway IP и свой HSRP group.

## Priority And Preempt

HSRP priority решает, кто станет active router.

| Rule | Meaning |
| --- | --- |
| Higher priority wins | Router with larger priority becomes active. |
| Default priority is 100 | If you do nothing, both routers start equal. |
| Tie uses higher IP | If priorities match, higher interface IP wins. |
| Preempt restores preference | Higher-priority router can take active role back. |

В lab Router 1 получил priority `105`, Router 2 остался на default `100`. Поэтому Router 1 стал active, а Router 2 - standby.

Без `preempt` failover может сработать, но failback будет не таким, как ожидается. Router 1 вернется после outage, но не обязательно снова станет active. Если design говорит, что Router 1 должен быть primary, включайте preempt осознанно.

## Virtual MAC And ARP

Для host все выглядит как один gateway. Он делает ARP for `10.0.16.1` и получает virtual MAC address, связанный с HSRP group.

Именно поэтому host не нужно перенастраивать при failover. IP gateway остается тем же, virtual MAC остается логической gateway identity, а routers между собой решают, кто сейчас отвечает.

Это важная troubleshooting detail. Если вы смотрите ARP cache или MAC address table и видите HSRP virtual MAC, это не ошибка. Это механизм, который делает gateway redundancy прозрачной для hosts.

## Testing Failover

Redundancy без теста - это предположение.

Минимальный test plan:

1. Запустить continuous ping с client к internet destination.
2. Проверить, что Router 1 active for HSRP.
3. Проверить NAT translations на Router 1.
4. Отключить path к Router 1 controlled way.
5. Убедиться, что Router 2 стал active.
6. Проверить, что NAT translations появились на Router 2.
7. Вернуть Router 1.
8. Убедиться, что preempt вернул Router 1 в active role.

Useful commands:

```text
show standby brief
show ip nat translations
show ip route
show ip ospf neighbor
```

В нормальном failover часть pings может потеряться. Главное, что traffic восстанавливается, standby router становится active, а возвращение primary router происходит controlled way.

## Interface Tracking

Есть неприятный сценарий: router остается живым со стороны LAN, но теряет internet-facing interface. Hosts все еще видят gateway, HSRP может считать router active, но traffic наружу не работает.

Interface tracking нужен именно для этого.

Идея простая: если critical upstream interface падает, router снижает свою HSRP priority. Тогда standby router с рабочим upstream становится active.

Conceptual example:

```text
track 1 interface g0/1 line-protocol

interface g0/0.10
 standby 10 track 1 decrement 20
```

Если tracked interface упадет, priority снизится. Router, который был preferred, перестанет быть лучшим выбором, и traffic перейдет на действительно healthy router.

## NetworkChuck Coffee Design View

Для NetworkChuck Coffee это не exam trick. Если edge router падает утром, POS systems, online orders, staff devices и payment traffic должны продолжить работать.

Users не волнует, какой router active. Им нужно, чтобы default gateway отвечал, internet работал, а business process не останавливался.

Главная мысль: HSRP is not really about routers. It is about hosts having a working default gateway during failure.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `standby version 2` | Enables HSRPv2 on the interface. |
| `standby 10 ip 10.0.16.1` | Sets HSRP group 10 virtual gateway IP. |
| `standby 10 priority 105` | Makes this router more preferred than default 100. |
| `standby 10 preempt` | Allows this router to retake active role after recovery. |
| `show standby brief` | Shows HSRP groups, states, active and standby routers. |
| `show ip nat translations` | Verifies which router is translating traffic. |
| Active router | Router currently forwarding for the virtual gateway. |
| Standby router | Router ready to take over the virtual gateway. |
| Virtual IP | Default gateway IP used by hosts. |
| Interface tracking | Lowers priority when a critical interface fails. |

## Questions

### 1. What problem does HSRP solve?

Answer: It gives hosts a resilient default gateway, so they do not depend on one physical router.

### 2. Why configure routing and NAT before HSRP?

Answer: HSRP only handles gateway redundancy. The backup router still needs working routing, trunks, VLAN subinterfaces and NAT.

### 3. Why use a virtual IP as the host default gateway?

Answer: The host can keep one gateway address while different physical routers take ownership behind the scenes.

### 4. What does `preempt` do?

Answer: It lets the higher-priority router take active role back after it recovers.

### 5. Why is interface tracking important?

Answer: It prevents a router with a failed upstream link from staying active just because its LAN interface is still up.

## What To Review Later

- HSRPv1 vs HSRPv2 differences.
- HSRP virtual MAC format.
- `show standby brief` output.
- NAT behavior during gateway failover.
- Interface tracking with priority decrement.
