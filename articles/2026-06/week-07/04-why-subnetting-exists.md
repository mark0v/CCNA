# Зачем существует Subnetting

Source: закрытая страница курса  
Date added: 2026-06-13  
Related plan item: Week 7 / Why subnetting exists  
Tags: subnetting, subnet mask, CIDR, classful addressing, VLAN, broadcast domain, IP planning
Language: Russian
Translation pair: articles-en/2026-06/week-07/04-why-subnetting-exists.md

## Кратко

Subnetting позволяет разделить IP address space на сети подходящего размера. Вместо одной большой общей сети или неудобных фиксированных classful размеров инженер выбирает prefix length под количество устройств, назначение сегмента, рост и требования безопасности.

Практический смысл subnetting не сводится к двоичной арифметике. Это инструмент проектирования: guest Wi-Fi, POS terminals, cameras, office devices, servers и voice systems могут получать отдельные address ranges и broadcast domains.

## Ключевые идеи

- Subnetting создаёт логические IP networks нужного размера.
- Subnet mask или CIDR prefix отделяет network bits от host bits.
- Увеличение prefix length создаёт больше сетей, но меньше addresses в каждой.
- Уменьшение prefix length создаёт меньше сетей, но больше addresses в каждой.
- Старое classful деление не соответствует гибким требованиям современных networks.
- Слишком большая subnet увеличивает broadcast domain и административный scope.
- Слишком маленькая subnet быстро исчерпывает addresses.
- VLAN и subnet обычно проектируются вместе, но это разные понятия.
- Router или Layer 3 switch соединяет разные subnets.
- Subnetting поддерживает segmentation, route summarization и масштабирование.
- Хороший адресный план оставляет место для роста.
- Математика является средством, а не конечной целью.

## Какую проблему решает Subnetting

Представим одну сеть:

```text
192.168.10.0/24
```

В неё помещены:

- guest Wi-Fi;
- POS terminals;
- office laptops;
- cameras;
- inventory devices;
- printers;
- servers.

Технически устройства могут использовать один address range, но такая flat network создаёт проблемы:

- все узлы находятся в одном broadcast domain;
- security policies сложнее выразить;
- guest и business traffic смешиваются;
- troubleshooting охватывает слишком большой scope;
- growth одного типа устройств влияет на остальных;
- документация и ownership становятся менее ясными.

Subnetting позволяет разделить исходное пространство по назначению.

## Пример осмысленного разделения

Вместо одной `/24`:

```text
192.168.10.0/24
```

можно спроектировать несколько сетей:

```text
192.168.10.0/25    Guest Wi-Fi
192.168.10.128/27  POS
192.168.10.160/27  Cameras
192.168.10.192/27  Office
192.168.10.224/28  Infrastructure
192.168.10.240/28  Reserved
```

Это только учебный пример. Реальный план зависит от числа hosts, growth, DHCP, redundancy, gateways и operational policy.

Каждый сегмент получает:

- собственный network address;
- диапазон host addresses;
- broadcast address в IPv4;
- default gateway;
- отдельную policy boundary;
- понятное назначение.

## Что делает Subnet Mask

IPv4 address содержит 32 bits. Subnet mask определяет, какие bits описывают network, а какие доступны host portion.

Пример:

```text
IP address:  192.168.10.25
Mask:        255.255.255.0
CIDR:        /24
```

Первые 24 bits относятся к network portion:

```text
Network: 192.168.10.0/24
```

Последние 8 bits используются внутри этой subnet.

Другой пример:

```text
192.168.10.25/27
```

Теперь network portion занимает 27 bits, а host portion только 5 bits. Network boundaries появляются через каждые 32 addresses.

## Prefix Length как регулятор размера

| Prefix | Total addresses | Traditional usable hosts |
| --- | ---: | ---: |
| `/24` | 256 | 254 |
| `/25` | 128 | 126 |
| `/26` | 64 | 62 |
| `/27` | 32 | 30 |
| `/28` | 16 | 14 |
| `/29` | 8 | 6 |
| `/30` | 4 | 2 |

Traditional usable hosts исключает network и broadcast addresses. Для `/31` на point-to-point links действуют специальные правила RFC 3021, поэтому универсальная формула `total - 2` имеет исключения.

Главная зависимость:

```text
Longer prefix -> more subnets, fewer addresses per subnet
Shorter prefix -> fewer subnets, more addresses per subnet
```

## Почему старые классы были неудобны

Историческое classful addressing делило unicast IPv4 space на фиксированные размеры:

| Class | Default prefix | Approximate scale |
| --- | --- | --- |
| A | `/8` | Очень большая network |
| B | `/16` | Большая network |
| C | `/24` | Небольшая network |

Организации часто не вписывались в эти размеры. Например, network с потребностью в 500 hosts не помещается в `/24`, но выделение целой `/16` создаёт огромный избыток addresses.

Современное проектирование использует CIDR и variable prefix lengths. Термины class A/B/C всё ещё встречаются в обучении и legacy discussions, но routing давно не должен строиться вокруг classful boundaries.

## Subnetting и CIDR

CIDR notation:

```text
192.168.10.0/24
```

показывает количество network bits напрямую.

Это позволяет использовать prefixes:

```text
/19
/22
/27
/30
```

без привязки к старым классам.

Subnetting обычно означает разделение более крупного allocation на меньшие prefixes. Supernetting или route aggregation объединяет contiguous prefixes в более короткое summary.

## Subnetting и VLAN

Subnet и VLAN тесно связаны, но не идентичны:

- VLAN создаёт Layer 2 broadcast domain.
- IP subnet определяет Layer 3 address domain.

Обычный design использует:

```text
one VLAN <-> one IP subnet
```

Например:

| VLAN | Purpose | Subnet |
| ---: | --- | --- |
| 10 | Office | `10.10.10.0/24` |
| 20 | POS | `10.10.20.0/26` |
| 30 | Cameras | `10.10.30.0/25` |
| 40 | Guest Wi-Fi | `10.10.40.0/23` |

Разные subnets требуют Layer 3 forwarding. Это может выполнять router, multilayer switch или firewall.

## Почему не стоит делать одну огромную сеть

Большая subnet не обязательно немедленно перестаёт работать, но увеличивает operational blast radius.

Возможные последствия:

- больше broadcast и unknown-unicast traffic;
- больше ARP/neighbor state;
- сложнее изолировать incident;
- сложнее применять policy между группами;
- больше риск ошибочной lateral connectivity;
- труднее проводить migrations;
- сложнее понимать ownership address ranges.

Размер broadcast domain должен определяться требованиями, а не привычкой использовать `/24` или одну общую сеть для всего.

## Почему не стоит делать сеть слишком маленькой

Если subnet рассчитана ровно на текущее число устройств, growth быстро исчерпает свободные addresses.

Нужно учитывать:

- current endpoints;
- ближайший growth;
- gateway addresses;
- DHCP exclusions;
- static infrastructure;
- redundancy addresses;
- monitoring и management interfaces;
- temporary devices;
- reserved capacity.

Пример:

```text
Сейчас: 25 cameras
Рост: до 40 cameras
```

`/27` даёт 30 traditional usable hosts и слишком мал. `/26` даёт 62 и оставляет разумный запас.

## Subnetting как business design

Запросы редко формулируются как:

```text
Раздели сеть на subnets.
```

Обычно задача звучит так:

- нужен новый VLAN для cameras;
- guest Wi-Fi нужно изолировать;
- открывается branch office;
- добавляются VoIP phones;
- нужно отделить servers от users;
- требуется адресный план для VPN;
- текущий DHCP scope заканчивается;
- необходимо summarization между sites.

Каждый такой запрос требует решений о subnet sizes и boundaries.

## Пример NetworkChuck Coffee

Требования:

| Segment | Current devices | Expected growth |
| --- | ---: | ---: |
| Guest Wi-Fi | 70 | 110 |
| Office | 12 | 20 |
| POS | 8 | 12 |
| Cameras | 24 | 40 |
| Infrastructure | 6 | 10 |

Возможный первый план:

| Segment | Candidate prefix | Traditional usable hosts |
| --- | --- | ---: |
| Guest Wi-Fi | `/25` | 126 |
| Office | `/27` | 30 |
| POS | `/28` | 14 |
| Cameras | `/26` | 62 |
| Infrastructure | `/28` | 14 |

Такой план нужно дополнительно проверить:

- помещаются ли prefixes в available parent block;
- не пересекаются ли ranges;
- остаётся ли reserved space;
- удобна ли summarization;
- поддерживает ли DHCP required leases;
- соответствуют ли VLAN IDs и policies;
- есть ли адреса для gateway redundancy.

## Fixed-Length и Variable-Length Subnetting

### FLSM

Fixed-Length Subnet Mask использует одинаковый prefix для всех subnets.

Преимущества:

- простой расчёт;
- одинаковый размер segments;
- легко документировать.

Недостатки:

- address waste, если requirements сильно различаются;
- размер определяется крупнейшим segment.

### VLSM

Variable-Length Subnet Mask использует разные prefixes:

```text
Guest: /25
Cameras: /26
Office: /27
POS: /28
```

Преимущества:

- лучше соответствует реальным потребностям;
- экономнее использует address space;
- гибче при hierarchical design.

Недостатки:

- требует аккуратного planning;
- выше риск overlap при ошибке;
- документация особенно важна.

## Что нужно уметь вычислять

Для заданного IPv4 address и prefix нужно находить:

1. Subnet mask.
2. Network address.
3. Broadcast address.
4. First host address.
5. Last host address.
6. Total addresses.
7. Traditional usable hosts.
8. Следующую subnet boundary.

Для проектной задачи также нужно:

1. Определить необходимое число subnets.
2. Оценить hosts с запасом.
3. Выбрать prefixes.
4. Расположить ranges без overlap.
5. Оставить growth space.
6. Подготовить summarization.

## Бинарная основа

Subnetting использует binary потому, что mask работает с bits.

Пример последнего октета `/27`:

```text
Mask:    224
Binary:  11100000
```

Три единичных bits добавлены к network portion, пять нулевых оставлены host portion.

Количество addresses:

```text
2^5 = 32
```

Именно поэтому block size `/27` равен 32.

Бинарная запись не является отдельной абстрактной задачей: она объясняет, почему boundaries находятся на `.0`, `.32`, `.64`, `.96` и далее.

## Основные формулы

Для обычной IPv4 subnet с prefix `/p`:

```text
Host bits = 32 - p
Total addresses = 2^(host bits)
Traditional usable hosts = 2^(host bits) - 2
```

Если из parent prefix `/P` создаётся child prefix `/p`:

```text
Borrowed bits = p - P
Number of equal-size subnets = 2^(borrowed bits)
```

Формулы нужно применять с пониманием исключений `/31` и `/32`, а также требований конкретной платформы и use case.

## Ошибки проектирования

### Использовать `/24` для всего

Это удобно визуально, но может тратить addresses или создавать слишком крупные segments.

### Рассчитывать только текущее число hosts

Growth и infrastructure requirements быстро делают план тесным.

### Путать VLAN и subnet

Они относятся к разным слоям и должны быть согласованы намеренно.

### Создавать overlapping ranges

Overlap приводит к ambiguity, routing problems и сложным migrations.

### Игнорировать summarization

Случайное размещение ranges увеличивает routing tables и усложняет policy.

### Не документировать allocations

Свободный на вид range может быть уже зарезервирован для другого site или service.

## Практическое упражнение

Дано:

```text
Parent network: 10.50.0.0/22
```

Требования:

- Guest: 200 hosts.
- Cameras: 90 hosts.
- Office: 45 hosts.
- POS: 20 hosts.
- Infrastructure: 10 hosts.

Задача:

1. Подобрать минимальные practical prefixes с growth reserve.
2. Разместить largest subnet first.
3. Не допустить overlap.
4. Записать network, usable range и broadcast.
5. Оставить свободное contiguous space.

Начальные кандидаты:

```text
Guest:          /24
Cameras:        /25
Office:         /26
POS:            /27
Infrastructure: /28
```

Это ещё не окончательный production design: нужно проверить reserve и future expansion.

## План изучения

Двигайся слоями:

1. Понять network и host portions.
2. Выучить связь prefix и mask.
3. Освоить powers of two.
4. Находить block size.
5. Определять network boundaries.
6. Считать host ranges.
7. Делить parent network на равные subnets.
8. Перейти к VLSM.
9. Связать subnets с VLANs и routing.
10. Проверять результаты инструментами, не заменяя ими понимание.

## Контрольные вопросы

### Вопрос 1

Зачем существует subnetting?

Ответ:

```text
Чтобы создавать IP networks подходящего размера и назначения
внутри доступного address space.
```

### Вопрос 2

Что определяет prefix length?

Ответ:

```text
Количество bits, относящихся к network portion IPv4 address.
```

### Вопрос 3

Что происходит при увеличении prefix с `/24` до `/26`?

Ответ:

```text
Создаётся больше меньших subnets; каждая `/26` содержит 64 total addresses.
```

### Вопрос 4

Почему VLAN и subnet не являются одним и тем же?

Ответ:

```text
VLAN определяет Layer 2 broadcast domain,
а subnet определяет Layer 3 address domain.
```

### Вопрос 5

В чём реальный навык subnetting?

Ответ:

```text
Не только в арифметике, а в выборе address boundaries,
соответствующих масштабу, росту, segmentation и routing design.
```

## Команды и термины

| Термин | Назначение |
| --- | --- |
| Subnet | Логическая IP network внутри большего address space. |
| Subnet mask | 32-bit mask, разделяющая network и host portions. |
| CIDR prefix | Количество network bits, например `/27`. |
| Network address | Первый address, идентифицирующий subnet. |
| Broadcast address | Последний address traditional IPv4 subnet. |
| FLSM | Одинаковый prefix для всех child subnets. |
| VLSM | Разные prefixes под разные requirements. |
| VLAN | Layer 2 broadcast domain. |
| Route summarization | Представление нескольких prefixes одним summary. |
| Address plan | Документированное распределение address space. |

## Что повторить позже

- Binary IPv4 representation
- Powers of two
- Prefix-to-mask conversion
- Block sizes
- Network and broadcast calculation
- FLSM
- VLSM
- Route summarization
- IPv6 prefix planning
