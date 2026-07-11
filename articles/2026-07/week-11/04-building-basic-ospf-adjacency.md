# Building Basic OSPF Adjacency

Source: закрытая страница курса  
Date added: 2026-07-11  
Related plan item: Week 11 / Building basic OSPF adjacency  
Tags: OSPF, adjacency, WAN, Area 0, network command, passive interface, LSDB, troubleshooting
Language: Russian
Translation pair: articles-en/2026-07/week-11/04-building-basic-ospf-adjacency.md

## Summary

- После теории dynamic routing нужно собрать первый рабочий OSPF adjacency.
- В lab topology cafe router и fallout shelter router соединяются point-to-point WAN link.
- Для WAN link удобно использовать `/30`, потому что нужны только два usable IP addresses.
- OSPF `network` command включает protocol на matching interfaces и advertising connected networks.
- Первый troubleshooting lesson: если adjacency не формируется, проверяй interface IP, network statements и OSPF hellos.

## Key Points

- OSPF позволяет routers learn routes automatically instead of relying on static routes.
- Area 0 - backbone area и правильный starting point для simple OSPF design.
- Targeted `network <interface-ip> 0.0.0.0 area 0` снижает риск accidental interface matching.
- Passive interface полезен для VLANs, которые нужно advertise, но где не нужны OSPF neighbors.
- `show ip ospf neighbor`, `show ip route ospf` и debug output помогают быстро найти mistakes.

## Notes

Теория dynamic routing становится полезной только тогда, когда routers действительно начинают обмениваться routes. В этой статье цель простая: соединить две routed части Castle Rysen/NetworkChuck Coffee environment и поднять первый OSPF neighbor relationship.

Топология:

- cafe router;
- fallout shelter router;
- WAN link между ними;
- cafe admin VLAN;
- cafe patron VLAN;
- fallout shelter VLANs.

Design choice: advertising только нужные сети. Cafe admin VLAN должна быть reachable с других sites, потому что там живут management systems, servers и важная инфраструктура. Patron VLAN - это guest/BYOD traffic, и fallout shelter не обязан знать о ней напрямую.

## WAN Link

Для point-to-point WAN link используется subnet `172.16.0.0/30`.

`/30` удобен для router-to-router links:

| Address | Role |
| --- | --- |
| `172.16.0.0` | Network address. |
| `172.16.0.1` | Cafe router WAN IP. |
| `172.16.0.2` | Fallout shelter router WAN IP. |
| `172.16.0.3` | Broadcast address. |

Это ровно два usable addresses - по одному для каждого router. Для point-to-point link больше обычно не нужно.

Практический совет: WAN links удобно держать в отдельном address range, например `172.16.0.0/16`, а LAN/VLAN networks - в `10.0.0.0/8`. Тогда при чтении routing table адрес `172.x` сразу выглядит как transit/WAN segment.

## Basic OSPF Enablement

OSPF включается через process ID:

```text
router ospf 1
```

Process ID локален для router. Он не обязан совпадать между neighbors, но в labs его часто держат одинаковым для ясности.

Дальше нужно выбрать interfaces, где будет работать OSPF. Targeted style использует exact interface IP с wildcard `0.0.0.0`:

```text
router ospf 1
 network 172.16.0.1 0.0.0.0 area 0
 network 10.0.18.1 0.0.0.0 area 0
```

Такой подход говорит: match exactly interface with this IP. Он помогает избежать случайного включения OSPF на лишних interfaces.

На другой стороне WAN link:

```text
router ospf 1
 network 172.16.0.2 0.0.0.0 area 0
```

Когда оба routers включают OSPF на WAN interfaces в same area, они начинают отправлять hello packets. Если параметры совместимы, формируется OSPF neighbor adjacency.

## Area 0

OSPF использует areas. Area - это logical chunk OSPF topology, где routers share same link-state database.

Area 0 - backbone area. В simple design и в первой lab logical choice - положить оба routers в Area 0:

```text
network 172.16.0.1 0.0.0.0 area 0
```

Multi-area OSPF нужен позже, когда topology растет и LSDB становится слишком большой. На старте Area 0 достаточно.

Ментальная модель:

> OSPF area - это neighborhood map. Routers внутри area имеют одинаковую карту, но каждый считает свой best path от собственной точки старта.

## Passive Interfaces

Cafe admin VLAN нужно advertise, но на ней не нужен OSPF neighbor. Поэтому interface можно сделать passive:

```text
router ospf 1
 passive-interface g0/0.18
```

Это остановит OSPF hello packets на admin VLAN, но connected network продолжит advertising в OSPF.

Для user-facing или server-facing VLANs это нормальный pattern:

- advertise subnet;
- do not form neighbors;
- reduce noise;
- reduce attack surface.

## Troubleshooting First Adjacency

Если neighbor не появляется, не угадывай. Проверяй:

```text
show ip ospf neighbor
show ip interface brief
show running-config | section router ospf
show ip protocols
show ip route ospf
```

Типичные причины:

- OSPF network statement matched wrong interface IP;
- interfaces находятся в different OSPF areas;
- WAN interface down/down или administratively down;
- IP addresses не находятся в одной subnet;
- hello/dead timers mismatch;
- passive-interface accidentally applied to WAN interface;
- authentication mismatch, если она настроена.

Debug может показать live protocol activity:

```text
debug ip ospf events
```

Но в production debug нужно использовать осторожно. Он может быть noisy и влиять на router CPU.

Главный lesson: troubleshooting - это не отдельная часть networking. Это и есть networking. Скопировать команды мало. Нужно уметь смотреть outputs, найти mismatch и исправить config.

## What Was Accomplished

После правильной настройки:

- cafe router и fallout shelter router становятся OSPF neighbors;
- routers dynamically exchange routing information;
- fallout shelter видит cafe admin VLAN как OSPF-learned route;
- routing table получает routes не через static config, а через protocol;
- появляется foundation для дальнейшего OSPF tuning.

На fallout shelter side можно advertising несколько VLANs broad network statement, но это требует discipline. Just because you can advertise everything does not mean you should. Позже design нужно refine через route control, summarization и более точные statements.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `router ospf 1` | Starts OSPF process 1 on the local router. |
| `network 172.16.0.1 0.0.0.0 area 0` | Enables OSPF on exact interface IP and places it in Area 0. |
| `passive-interface g0/0.18` | Stops hellos on that interface while still advertising its connected network. |
| `show ip ospf neighbor` | Verifies OSPF neighbor relationships. |
| `show ip route ospf` | Shows OSPF-learned routes in the routing table. |
| Area 0 | OSPF backbone area. |
| LSDB | Link-state database, OSPF topology information inside an area. |

## Questions

### 1. Почему `/30` хорошо подходит для point-to-point WAN link?

Answer: Потому что он дает ровно два usable IP addresses, по одному для каждого router endpoint.

### 2. Почему targeted `network <ip> 0.0.0.0 area 0` удобен?

Answer: Он matches exact interface IP, снижая риск accidentally включить OSPF на лишнем interface.

### 3. Зачем делать admin VLAN passive?

Answer: Чтобы advertising subnet в OSPF, но не отправлять hello packets и не формировать neighbors на user/server-facing segment.

### 4. Что означает OSPF adjacency?

Answer: Это neighbor relationship между routers, которые обмениваются OSPF information и участвуют в одной routing domain.

### 5. Что проверять первым, если adjacency не формируется?

Answer: Interface status, IP addressing, OSPF network statements, area ID, passive-interface и `show ip ospf neighbor`.

## What To Review Later

- OSPF neighbor states.
- OSPF hello/dead timers.
- Area 0 and multi-area design.
- Route summarization in OSPF.
- Safer troubleshooting with `show` commands before debug.
