# NAT Types and Port Translation

Source: закрытая страница курса  
Date added: 2026-06-09  
Related plan item: Week 6 / NAT types and PAT  
Tags: NAT, static NAT, dynamic NAT, PAT, NAT overload, RFC 1918, ports, translation table
Language: Russian
Translation pair: articles-en/2026-06/week-06/08-nat-types-and-port-translation.md

## Summary

NAT появился как практический способ связать private IPv4 networks с public internet при ограниченном количестве public addresses. Он преобразует addresses на edge device и позволяет внутренним hosts использовать public connectivity.

Три основные формы: static NAT создает постоянное one-to-one mapping, dynamic NAT временно назначает address из public pool, а NAT overload/PAT позволяет множеству hosts разделять один public IP за счет TCP/UDP port numbers.

## Key Points

- NAT является практическим ответом на дефицит public IPv4 addresses.
- RFC 1918 определяет private IPv4 address ranges.
- Providers и internet routers обычно фильтруют private source/destination prefixes.
- Static NAT использует постоянное one-to-one mapping.
- Dynamic NAT выделяет временный public address из pool.
- NAT overload использует many-to-one translation.
- PAT различает simultaneous sessions по transport ports.
- Router хранит active mappings в NAT translation table.
- NAT чаще всего выполняется на internet edge router или firewall.
- Для troubleshooting нужно проверять routes, NAT, DNS и security policy отдельно.

## Notes

### Why NAT Exists

IPv4 address space ограничен.

Если бы каждому device требовался уникальный public IPv4 address, доступных addresses было бы недостаточно.

NAT позволил:

- использовать повторяющиеся private ranges внутри организаций;
- выдавать public identity только на network edge;
- разделять один public address между множеством hosts;
- продлить практический срок жизни IPv4.

NAT полезен, но является механизмом совместимости, а не идеальной заменой глобальному address space.

### RFC 1918 Private Ranges

Private IPv4 ranges:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

Они предназначены для internal use и могут повторяться в разных networks.

Важно сформулировать точно: эти addresses технически являются обычными IPv4 addresses, но public internet не должен принимать или рекламировать RFC 1918 prefixes.

### NAT At The Edge

NetworkChuck Coffee использует private addresses внутри:

- user devices;
- POS terminals;
- printers;
- cameras;
- internal servers.

На границе:

```text
Private LAN -> Edge router/firewall -> Public internet
```

Edge device переводит address representation и отслеживает sessions.

## Static NAT

Static NAT создает постоянное one-to-one mapping:

```text
192.168.1.50 <-> 216.0.5.10
```

Публичный address всегда соответствует одному internal host.

Типичные use cases:

- internal web server;
- mail gateway;
- externally reachable service;
- device, которому нужен predictable public address;
- legacy application с фиксированными allowlists.

### Advantages

- predictable mapping;
- удобен для inbound connections;
- легко документировать;
- translation существует постоянно.

### Limitations

- каждому mapping нужен public address;
- не экономит addresses так эффективно, как PAT;
- inbound service все равно требует firewall policy;
- exposed service требует patching и monitoring.

## Dynamic NAT

Dynamic NAT создает временное one-to-one mapping из public pool.

Пример pool:

```text
216.0.5.10 - 216.0.5.14
```

Internal host получает свободный public address на время translation.

### Advantages

- mappings создаются автоматически;
- public addresses можно переиспользовать;
- не нужно закреплять address за каждым host постоянно.

### Limitations

- количество simultaneous translated hosts ограничено размером pool;
- если pool исчерпан, новые translations не создаются;
- public identity host может меняться;
- требуется несколько public addresses.

## NAT Overload / PAT

NAT overload - наиболее распространенный вариант для small office и home networks.

Также называется:

```text
PAT - Port Address Translation
```

Множество private hosts разделяют один public IP.

Router различает flows по комбинации:

- protocol;
- inside local IP;
- inside local port;
- translated IP;
- translated port;
- outside destination.

### Example

```text
192.168.1.10:51000 -> 216.0.5.2:30001
192.168.1.20:51000 -> 216.0.5.2:30002
```

Оба hosts используют public address `216.0.5.2`, но разные translated ports.

### Why Ports Matter

TCP и UDP используют source и destination port numbers для идентификации application sessions.

PAT может изменять source port, чтобы каждое active flow оставалось уникальным.

Когда reply приходит на:

```text
216.0.5.2:30001
```

router смотрит translation table и направляет его:

```text
192.168.1.10:51000
```

### Benefits

- один public IPv4 обслуживает много hosts;
- подходит для outbound internet access;
- экономит public address space;
- используется почти во всех small network edge deployments.

### Constraints

- translation table имеет конечный размер;
- port exhaustion возможен при огромном количестве sessions;
- inbound access требует explicit mapping/port forwarding;
- некоторые protocols сложнее проходят через NAT;
- logging должен позволять сопоставлять public port с internal session.

## Translation Table

NAT device хранит active mappings.

На Cisco IOS проверка:

```cisco
show ip nat translations
```

Можно увидеть columns:

```text
Pro
Inside global
Inside local
Outside local
Outside global
```

Также полезно:

```cisco
show ip nat statistics
```

Команда показывает:

- inside/outside interfaces;
- количество active translations;
- hits and misses;
- pools;
- configuration references.

## Choosing The NAT Type

| Requirement | Suitable Type |
| --- | --- |
| Постоянный public address для одного internal server | Static NAT |
| Временные one-to-one mappings из набора addresses | Dynamic NAT |
| Internet access для множества users через один address | PAT / overload |

В одной network могут использоваться несколько типов одновременно.

## NAT Is Not The Whole Internet Path

Для working connectivity также нужны:

- correct host IP and mask;
- default gateway;
- route к ISP;
- reachable ISP next hop;
- firewall/ACL permission;
- DNS, если используются names;
- return path;
- working application.

Если translation отсутствует, это NAT issue. Если translation есть, но replies не приходят, нужно исследовать routing, ISP и security.

## Troubleshooting Checklist

1. Проверить inside host addressing.
2. Проверить default route.
3. Проверить inside/outside interface roles.
4. Проверить NAT traffic-selection rule.
5. Проверить public pool или overload interface.
6. Выполнить `show ip nat translations`.
7. Выполнить `show ip nat statistics`.
8. Проверить firewall/ACL.
9. Проверить DNS отдельно.
10. Очистить stale translations только при необходимости и понимании impact.

## Quick Self-Check

### Question 1

Какие три основные формы NAT?

Answer:

```text
Static NAT, dynamic NAT и NAT overload/PAT.
```

### Question 2

Как работает static NAT?

Answer:

```text
Создает постоянное one-to-one mapping между private и public addresses.
```

### Question 3

Что ограничивает dynamic NAT?

Answer:

```text
Количество available public addresses в pool.
```

### Question 4

Как PAT различает hosts, использующих один public IP?

Answer:

```text
С помощью protocol и translated TCP/UDP port numbers.
```

### Question 5

Какой командой посмотреть active Cisco NAT mappings?

Answer:

```text
show ip nat translations
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Static NAT | Permanent one-to-one translation. |
| Dynamic NAT | Temporary one-to-one translation from a pool. |
| PAT | Port Address Translation. |
| NAT overload | Cisco term for many-to-one PAT. |
| Public pool | Набор public addresses для dynamic NAT. |
| Translation table | Active NAT session mappings. |
| Source port | Transport port выбранный initiating host. |
| Port exhaustion | Нехватка available translated port combinations. |
| `show ip nat translations` | Показывает active mappings. |
| `show ip nat statistics` | Показывает NAT configuration и counters. |

## What To Review Later

- Cisco NAT terminology
- Static NAT configuration
- Dynamic NAT pools
- PAT configuration
- NAT ACLs
- Port forwarding
- NAT logging
- NAT troubleshooting
