# Variable Length Subnet Masking

Source: закрытая страница курса  
Date added: 2026-06-13  
Related plan item: Week 7 / Variable Length Subnet Masking  
Tags: VLSM, subnetting, IPv4, address planning, host requirements, point-to-point
Language: Russian
Translation pair: articles-en/2026-06/week-07/13-variable-length-subnet-masking.md

## Кратко

VLSM, или Variable Length Subnet Masking, позволяет использовать разные prefixes внутри одного parent address block.

Вместо одинаковой mask для всех segments:

```text
Every subnet = /26
```

каждому segment выделяется подходящий размер:

```text
Large LAN:  /26
Small LAN:  /27
WAN link:   /30
```

Сам алгоритм subnetting не меняется. Для каждого требования:

1. Определить требуемое число usable hosts.
2. Найти smallest practical prefix.
3. Расположить allocations от largest к smallest.
4. Проверить alignment, overlap и remaining space.

## Ключевые Идеи

- FLSM использует одну mask для всех child subnets.
- VLSM использует masks разной длины.
- Каждая VLSM allocation остаётся обычной CIDR subnet.
- Requirements сортируются от largest к smallest.
- Крупные blocks размещаются первыми.
- Каждая network должна начинаться на boundary своего prefix.
- Child subnets не должны пересекаться.
- Все allocations должны находиться внутри parent block.
- Network и broadcast addresses учитываются для каждой subnet отдельно.
- Свободное пространство желательно сохранять contiguous.
- Routing protocols должны поддерживать classless prefixes.

## FLSM и VLSM

### FLSM

```text
Fixed Length Subnet Mask
```

Все child networks имеют одинаковый prefix.

Преимущества:

- простой расчёт;
- одинаковая capacity;
- предсказуемые increments.

Недостаток:

- address waste, если segments сильно различаются по размеру.

### VLSM

```text
Variable Length Subnet Mask
```

Разные child networks получают разные prefixes.

Преимущества:

- allocation ближе к реальным требованиям;
- меньше waste;
- удобно для LAN, infrastructure и WAN links в одном plan.

Цена:

- нужно внимательнее следить за alignment и overlap;
- документация становится важнее;
- summarization требует планирования.

## Почему Нужно Начинать С Largest

Большая subnet требует крупный contiguous aligned block.

Маленькие blocks легче разместить в оставшемся пространстве. Если сначала распределить `/30` и `/28` без общего плана, они могут разбить address space и помешать размещению `/25` или `/26`.

Практическое правило:

```text
Sort requirements from largest to smallest.
Allocate in that order.
```

## Рабочий Алгоритм

1. Подтвердить parent network и prefix.
2. Собрать host requirements для всех segments.
3. Добавить gateways, infrastructure и growth headroom.
4. Для каждого segment найти prefix через `2^h - 2`.
5. Отсортировать allocations по total block size, от largest к smallest.
6. Начать с первой свободной aligned boundary.
7. Записать network, usable range и broadcast.
8. Перейти к первому address после allocation.
9. Проверить alignment следующего block.
10. Повторить для всех requirements.
11. Проверить отсутствие overlap.
12. Записать remaining free ranges.

## Пример NetworkChuck Coffee

Parent block:

```text
192.168.10.0/24
```

Requirements:

| Segment | Required usable hosts |
| --- | ---: |
| Main Cafe | 50 |
| Office | 50 |
| Kiosk A | 20 |
| Kiosk B | 20 |
| WAN Link 1 | 2 |
| WAN Link 2 | 2 |

## Шаг 1. Выбрать Prefix Для Каждого Segment

### 50 Hosts

```text
2^5 - 2 = 30   insufficient
2^6 - 2 = 62   sufficient
```

```text
Prefix: /26
Block:  64 addresses
```

Нужно две `/26`.

### 20 Hosts

```text
2^4 - 2 = 14   insufficient
2^5 - 2 = 30   sufficient
```

```text
Prefix: /27
Block:  32 addresses
```

Нужно две `/27`.

### 2 Hosts

Traditional point-to-point:

```text
2^2 - 2 = 2
```

```text
Prefix: /30
Block:  4 addresses
```

Нужно две `/30`.

## Шаг 2. Отсортировать Requirements

```text
/26
/26
/27
/27
/30
/30
```

Total addresses:

```text
64 + 64 + 32 + 32 + 4 + 4 = 200
```

Parent `/24` содержит 256 addresses, поэтому preliminary capacity check проходит.

Это ещё не доказывает корректность plan: blocks должны быть aligned и не пересекаться.

## Шаг 3. Выполнить Allocation

### Main Cafe

```text
Network:    192.168.10.0/26
First host: 192.168.10.1
Last host:  192.168.10.62
Broadcast:  192.168.10.63
```

### Office

Следующая `/26` boundary:

```text
192.168.10.64
```

```text
Network:    192.168.10.64/26
First host: 192.168.10.65
Last host:  192.168.10.126
Broadcast:  192.168.10.127
```

### Kiosk A

Следующая свободная `/27` boundary:

```text
192.168.10.128
```

```text
Network:    192.168.10.128/27
First host: 192.168.10.129
Last host:  192.168.10.158
Broadcast:  192.168.10.159
```

### Kiosk B

```text
Network:    192.168.10.160/27
First host: 192.168.10.161
Last host:  192.168.10.190
Broadcast:  192.168.10.191
```

### WAN Link 1

```text
Network:    192.168.10.192/30
Router A:   192.168.10.193
Router B:   192.168.10.194
Broadcast:  192.168.10.195
```

### WAN Link 2

```text
Network:    192.168.10.196/30
Router A:   192.168.10.197
Router B:   192.168.10.198
Broadcast:  192.168.10.199
```

## Итоговая Таблица

| Segment | Network | Mask | Usable range | Broadcast |
| --- | --- | --- | --- | --- |
| Main Cafe | `192.168.10.0/26` | `255.255.255.192` | `.1 - .62` | `.63` |
| Office | `192.168.10.64/26` | `255.255.255.192` | `.65 - .126` | `.127` |
| Kiosk A | `192.168.10.128/27` | `255.255.255.224` | `.129 - .158` | `.159` |
| Kiosk B | `192.168.10.160/27` | `255.255.255.224` | `.161 - .190` | `.191` |
| WAN Link 1 | `192.168.10.192/30` | `255.255.255.252` | `.193 - .194` | `.195` |
| WAN Link 2 | `192.168.10.196/30` | `255.255.255.252` | `.197 - .198` | `.199` |

## Remaining Address Space

Использовано:

```text
192.168.10.0 - 192.168.10.199
```

Свободно:

```text
192.168.10.200 - 192.168.10.255
```

Это 56 addresses, но range не является одним aligned CIDR block.

Его можно представить, например, как:

```text
192.168.10.200/29   8 addresses
192.168.10.208/28  16 addresses
192.168.10.224/27  32 addresses
```

Планирование свободного пространства тоже важно. Если ожидается новая `/27`, удобно сохранить aligned block `192.168.10.224/27`.

## Почему Нельзя Просто Взять Первую Свободную Цифру

После allocation address может быть свободным, но не находиться на boundary нужного prefix.

Пример:

```text
Next free address: 192.168.10.200
Need: /27
```

`/27` boundaries в четвёртом octet:

```text
0, 32, 64, 96, 128, 160, 192, 224
```

`200` не является `/27` boundary.

Block `192.168.10.192/27` уже частично занят WAN links, поэтому следующая свободная целая `/27` начинается с:

```text
192.168.10.224/27
```

## Alignment Rules

| Prefix | Block size | Valid fourth-octet starts |
| ---: | ---: | --- |
| `/25` | 128 | 0, 128 |
| `/26` | 64 | 0, 64, 128, 192 |
| `/27` | 32 | 0, 32, 64, 96, 128, 160, 192, 224 |
| `/28` | 16 | multiples of 16 |
| `/29` | 8 | multiples of 8 |
| `/30` | 4 | multiples of 4 |

Для boundaries в другом octet применяется тот же принцип.

## Проверка Overlap

Две subnets пересекаются, если имеют хотя бы один общий address.

Неверный plan:

```text
192.168.10.128/26   covers .128 - .191
192.168.10.160/27   covers .160 - .191
```

Вторая полностью находится внутри первой.

Правильный plan должен использовать sibling blocks, а не overlapping parent/child allocations.

## `/30` Или `/31` Для WAN

Traditional design использует `/30`.

При поддержке RFC 3021 point-to-point link может использовать `/31`:

```text
192.168.10.192/31
192.168.10.194/31
```

Это экономит addresses, но перед использованием нужно проверить:

- поддержку обоими devices;
- provider requirements;
- monitoring tools;
- организационные standards.

Для базовых CCNA labs `/30` остаётся понятным вариантом.

## VLSM и Routing Protocols

VLSM требует передачи prefix length вместе с route.

Classless protocols поддерживают VLSM, например:

- RIPv2;
- OSPF;
- EIGRP;
- IS-IS;
- BGP.

Старый classful RIPv1 не передаёт mask в route updates и не подходит для современного VLSM design.

Static routes также явно содержат mask или prefix.

## Route Summarization

VLSM не отменяет summarization, но allocations нужно планировать иерархически.

Например:

```text
192.168.10.0/26
192.168.10.64/26
```

являются contiguous и вместе образуют:

```text
192.168.10.0/25
```

Это может быть useful summary, если topology и routing policy позволяют.

А две `/27`:

```text
192.168.10.128/27
192.168.10.160/27
```

суммируются как:

```text
192.168.10.128/26
```

Summary не должен включать destinations, которые находятся через другой path.

## Проверка Capacity До Allocation

Полезно выполнить два уровня проверки.

### Raw Address Count

```text
Sum of block sizes <= parent addresses
```

### Placement Check

- каждый block aligned;
- blocks не пересекаются;
- blocks находятся в parent;
- remaining space подходит ожидаемому growth.

Raw sum может помещаться математически, но плохой порядок allocation способен оставить только fragmented space.

## Документирование VLSM Plan

Для каждой allocation запишите:

| Field | Example |
| --- | --- |
| Purpose | Main Cafe |
| VLAN | 10 |
| Network | `192.168.10.0/26` |
| Gateway | `192.168.10.1` |
| DHCP pool | `.10 - .62` |
| Reservations | `.2 - .9` |
| Broadcast | `.63` |
| Site | HQ |
| Status | Assigned |

Используйте IPAM, spreadsheet или version-controlled source of truth.

## Практическое Задание

Parent:

```text
10.50.0.0/23
```

Requirements:

| Segment | Usable hosts |
| --- | ---: |
| Guest | 120 |
| Employees | 60 |
| Cameras | 28 |
| POS | 12 |
| Management | 10 |
| WAN 1 | 2 |
| WAN 2 | 2 |

Задачи:

1. Выбрать prefix для каждого segment.
2. Отсортировать allocations.
3. Разместить их от начала parent block.
4. Записать ranges.
5. Найти remaining free space.

## Возможное Решение

Prefixes:

```text
Guest:      /25
Employees:  /26
Cameras:    /27
POS:        /28
Management: /28
WAN 1:      /30
WAN 2:      /30
```

Allocation:

| Segment | Network | Usable range | Broadcast |
| --- | --- | --- | --- |
| Guest | `10.50.0.0/25` | `10.50.0.1 - 10.50.0.126` | `10.50.0.127` |
| Employees | `10.50.0.128/26` | `10.50.0.129 - 10.50.0.190` | `10.50.0.191` |
| Cameras | `10.50.0.192/27` | `10.50.0.193 - 10.50.0.222` | `10.50.0.223` |
| POS | `10.50.0.224/28` | `10.50.0.225 - 10.50.0.238` | `10.50.0.239` |
| Management | `10.50.0.240/28` | `10.50.0.241 - 10.50.0.254` | `10.50.0.255` |
| WAN 1 | `10.50.1.0/30` | `10.50.1.1 - 10.50.1.2` | `10.50.1.3` |
| WAN 2 | `10.50.1.4/30` | `10.50.1.5 - 10.50.1.6` | `10.50.1.7` |

Remaining:

```text
10.50.1.8 - 10.50.1.255
```

Его можно сохранить крупными aligned blocks для growth.

## Проверочный Checklist

- [ ] Parent network корректно aligned.
- [ ] Все requirements включают infrastructure и headroom.
- [ ] Prefix каждого segment покрывает usable hosts.
- [ ] Allocations отсортированы largest-first.
- [ ] Каждая network начинается на valid boundary.
- [ ] Network и broadcast не назначены hosts.
- [ ] Subnets не пересекаются.
- [ ] Все subnets находятся внутри parent.
- [ ] Remaining ranges задокументированы.
- [ ] Summaries не скрывают неправильные paths.
- [ ] Routing поддерживает classless prefixes.

## Частые Ошибки

### Allocating Smallest First

Может фрагментировать пространство и заблокировать крупный block.

### Использовать Одну Mask Для Всех

Это FLSM, а не VLSM, и часто создаёт waste.

### Игнорировать Alignment

Первый свободный address не всегда является valid network boundary.

### Забывать Network и Broadcast

Host requirement переводится в prefix через `2^h - 2`.

### Создавать Overlap

Каждая allocation должна быть disjoint.

### Не Учитывать Growth

Минимально возможный prefix может слишком быстро исчерпаться.

### Считать Free Range Одной Subnet

Произвольный contiguous range не обязательно является одним aligned CIDR block.

### Использовать Classful Routing

Route updates без mask не могут корректно описать VLSM prefixes.

## Контрольные Вопросы

### Вопрос 1

Что означает VLSM?

Ответ:

```text
Использование subnets с разными prefix lengths внутри одного address plan.
```

### Вопрос 2

Почему allocations размещают largest-first?

Ответ:

```text
Крупным networks нужны большие contiguous aligned blocks,
которые сложнее разместить после fragmentation.
```

### Вопрос 3

Какой prefix нужен для 50 usable hosts?

Ответ:

```text
/26, предоставляющий 62 usable hosts.
```

### Вопрос 4

Какой prefix нужен для 20 hosts?

Ответ:

```text
/27, предоставляющий 30 usable hosts.
```

### Вопрос 5

Может ли `192.168.10.200/27` быть network address?

Ответ:

```text
Нет. /27 boundaries являются multiples of 32.
Address 200 находится внутри 192.168.10.192/27.
```

### Вопрос 6

Почему raw address sum недостаточна?

Ответ:

```text
Blocks также должны быть aligned, non-overlapping и помещаться в parent.
```

## Команды и Термины

| Термин | Значение |
| --- | --- |
| VLSM | Разные prefix lengths в одном address plan. |
| FLSM | Одинаковый prefix для всех child subnets. |
| Largest-first | Allocation от крупнейшего block к меньшему. |
| Alignment | Начало subnet на boundary её block size. |
| Fragmentation | Свободное пространство, разбитое на неудобные ranges. |
| Overlap | Общие addresses у двух allocations. |
| Address plan | Документированное распределение IP space. |
| Classless routing | Передача routes вместе с prefix length. |

## Что Повторить Позже

- Host-based subnet sizing
- Block alignment
- CIDR notation
- `/30` and `/31`
- Route summarization
- Classless routing protocols
- IPAM
- VLSM practice

