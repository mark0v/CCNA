# Subnetting по Требуемому Количеству Hosts

Source: закрытая страница курса  
Date added: 2026-06-13  
Related plan item: Week 7 / Subnetting by host requirement  
Tags: subnetting, hosts, FLSM, prefix, subnet mask, capacity planning, headroom
Language: Russian
Translation pair: articles-en/2026-06/week-07/09-subnetting-by-host-requirement.md

## Кратко

Когда требование сформулировано как «нужна сеть минимум для 50 устройств», расчёт начинается с host capacity.

Нужно сохранить минимальное количество host bits `h`, при котором:

```text
2^h - 2 >= required hosts
```

После этого:

```text
New prefix = 32 - h
```

Пример для 50 hosts:

```text
2^5 - 2 = 30   insufficient
2^6 - 2 = 62   sufficient

Host bits:    6
Prefix:       /26
Mask:         255.255.255.192
Increment:    64
Usable hosts: 62
```

Главная идея:

```text
Сначала сохранить достаточно host bits,
затем использовать оставшиеся bits как network bits.
```

## Ключевые Идеи

- Требование может задавать число subnets или число hosts per subnet.
- При host-based subnetting сначала определяется необходимое количество host bits.
- Формула обычной IPv4 subnet: `2^h - 2`.
- Вычитание двух учитывает network и broadcast addresses.
- Выбирается самый длинный prefix, который всё ещё покрывает host requirement.
- Более длинный prefix означает меньшую subnet.
- Более короткий prefix означает большую subnet.
- После выбора prefix ranges строятся обычным методом increment.
- Parent block должен содержать хотя бы одну subnet выбранного размера.
- Из parent block может получиться несколько equal-size child subnets.
- В production к текущему числу endpoints добавляют разумный headroom.
- Infrastructure reservations также занимают addresses.

## Сначала Определите Тип Вопроса

### Вопрос По Subnets

```text
Сколько networks необходимо?
```

Нужно найти borrowed bits:

```text
2^n >= required subnets
```

### Вопрос По Hosts

```text
Сколько usable addresses требуется в каждой network?
```

Нужно сохранить host bits:

```text
2^h - 2 >= required hosts
```

Различие находится в первой части расчёта. После выбора mask increment, network, broadcast и usable ranges находятся одинаково.

## Почему Формула Использует `- 2`

В обычной IPv4 subnet:

- все host bits `0` обозначают network address;
- все host bits `1` обозначают broadcast address.

Например, 6 host bits создают:

```text
2^6 = 64 total combinations
```

Но usable hosts:

```text
64 - 2 = 62
```

Исключения:

- `/31` на point-to-point links по RFC 3021;
- `/32`, представляющий один address;
- специальные platform или protocol use cases.

Для стандартных учебных LAN calculations используйте `2^h - 2`.

## Почему Нельзя Просто Считать Bits Числа

Число `50` помещается в 6 binary bits, и `/26` действительно подходит. Но обобщённое правило «посчитать bits числа hosts» может дать ошибку на границе.

Пример для 63 hosts:

```text
63 decimal помещается в 6 bits.
```

Но:

```text
2^6 - 2 = 62
```

Недостаточно.

Нужны 7 host bits:

```text
2^7 - 2 = 126
```

Поэтому надёжная проверка:

```text
2^h - 2 >= requirement
```

## Таблица Host Capacity

| Host bits | Prefix | Total addresses | Traditional usable hosts |
| ---: | ---: | ---: | ---: |
| 2 | `/30` | 4 | 2 |
| 3 | `/29` | 8 | 6 |
| 4 | `/28` | 16 | 14 |
| 5 | `/27` | 32 | 30 |
| 6 | `/26` | 64 | 62 |
| 7 | `/25` | 128 | 126 |
| 8 | `/24` | 256 | 254 |
| 9 | `/23` | 512 | 510 |
| 10 | `/22` | 1024 | 1022 |
| 11 | `/21` | 2048 | 2046 |
| 12 | `/20` | 4096 | 4094 |
| 13 | `/19` | 8192 | 8190 |
| 14 | `/18` | 16384 | 16382 |

Эта таблица полезна для быстрой оценки, но её значения следуют из формулы.

## Практический Алгоритм

1. Записать parent network и parent prefix.
2. Записать required usable hosts per subnet.
3. Добавить infrastructure addresses и growth headroom, если это design task.
4. Найти минимальное `h`, где `2^h - 2` покрывает итог.
5. Вычислить `new prefix = 32 - h`.
6. Проверить, что new prefix не короче parent prefix.
7. Найти dotted-decimal mask.
8. Определить interesting octet.
9. Найти increment.
10. Перечислить child networks внутри parent block.
11. Найти network, broadcast и usable ranges.
12. Проверить число child subnets и host capacity.

## Проверка Parent Block

Child subnet должна находиться внутри parent allocation.

Если parent:

```text
192.168.10.0/24
```

и для hosts требуется:

```text
/23
```

задача невозможна внутри этого `/24`, потому что `/23` больше parent block.

```text
/23 is larger than /24
```

Нужно получить larger parent allocation или пересмотреть requirement.

## Пример 1: Минимум 50 Hosts

Дано:

```text
Parent network: 192.168.10.0/24
Required hosts: 50 per subnet
```

### Шаг 1. Найти Host Bits

```text
2^5 - 2 = 30   insufficient
2^6 - 2 = 62   sufficient
```

```text
Host bits = 6
```

### Шаг 2. Найти Prefix

```text
32 - 6 = 26
```

```text
New prefix = /26
```

Mask:

```text
255.255.255.192
```

Binary:

```text
11111111.11111111.11111111.11000000
```

### Шаг 3. Найти Increment

Interesting octet является четвёртым:

```text
256 - 192 = 64
```

```text
Increment = 64
```

### Шаг 4. Перечислить Child Subnets

```text
192.168.10.0/26
192.168.10.64/26
192.168.10.128/26
192.168.10.192/26
```

Из `/24` получено:

```text
2^(26 - 24) = 4 subnets
```

### Ranges

| Network | First host | Last host | Broadcast |
| --- | --- | --- | --- |
| `192.168.10.0/26` | `192.168.10.1` | `192.168.10.62` | `192.168.10.63` |
| `192.168.10.64/26` | `192.168.10.65` | `192.168.10.126` | `192.168.10.127` |
| `192.168.10.128/26` | `192.168.10.129` | `192.168.10.190` | `192.168.10.191` |
| `192.168.10.192/26` | `192.168.10.193` | `192.168.10.254` | `192.168.10.255` |

Каждая child subnet предоставляет:

```text
64 total addresses
62 usable hosts
```

## Если Исходный Address Не Является Parent Network

Фраза:

```text
172.16.10.0 requires 50 hosts
```

неполна без prefix.

С prefix `/24`:

```text
172.16.10.0/24
```

получатся четыре `/26`.

С prefix `/16`:

```text
172.16.0.0/16
```

можно получить 1024 `/26` subnets, включая `172.16.10.0/26`.

Address и prefix должны рассматриваться вместе.

## Пример 2: Минимум 500 Hosts

Дано:

```text
Parent network: 172.16.0.0/16
Required hosts: 500 per subnet
```

### Host Bits

```text
2^8 - 2 = 254   insufficient
2^9 - 2 = 510   sufficient
```

```text
Host bits = 9
```

### Prefix и Mask

```text
32 - 9 = 23
```

```text
Prefix: /23
Mask:   255.255.254.0
```

### Increment

```text
256 - 254 = 2 in the third octet
```

### Networks

```text
172.16.0.0/23
172.16.2.0/23
172.16.4.0/23
172.16.6.0/23
...
172.16.254.0/23
```

### Capacity

```text
Child subnets: 2^(23 - 16) = 128
Total/subnet:  2^9 = 512
Usable hosts:  510
```

Первый range:

```text
Network:    172.16.0.0
First host: 172.16.0.1
Last host:  172.16.1.254
Broadcast:  172.16.1.255
```

Второй:

```text
Network:    172.16.2.0
First host: 172.16.2.1
Last host:  172.16.3.254
Broadcast:  172.16.3.255
```

## Пример 3: Минимум 2000 Hosts

Дано:

```text
Parent network: 10.0.0.0/8
Required hosts: 2000 per subnet
```

### Host Bits

```text
2^10 - 2 = 1022   insufficient
2^11 - 2 = 2046   sufficient
```

```text
Host bits = 11
```

### Prefix и Mask

```text
32 - 11 = 21
```

```text
Prefix: /21
Mask:   255.255.248.0
```

### Increment

Interesting octet является третьим:

```text
256 - 248 = 8
```

### Networks

```text
10.0.0.0/21
10.0.8.0/21
10.0.16.0/21
10.0.24.0/21
...
10.255.248.0/21
```

### Первые Ranges

| Network | First host | Last host | Broadcast |
| --- | --- | --- | --- |
| `10.0.0.0/21` | `10.0.0.1` | `10.0.7.254` | `10.0.7.255` |
| `10.0.8.0/21` | `10.0.8.1` | `10.0.15.254` | `10.0.15.255` |
| `10.0.16.0/21` | `10.0.16.1` | `10.0.23.254` | `10.0.23.255` |

### Capacity

```text
Child subnets: 2^(21 - 8) = 8192
Total/subnet:  2^11 = 2048
Usable hosts:  2046
```

Математически `/21` покрывает 2000 hosts. Практически один broadcast domain такого размера требует отдельного обоснования.

## Headroom и Infrastructure Reservations

Требование «50 devices» редко означает, что достаточно ровно 50 addresses.

В subnet могут потребоваться:

- default gateway;
- redundant gateway;
- switches и access points;
- printers;
- cameras;
- controllers;
- monitoring;
- DHCP reservations;
- temporary devices;
- future growth.

Пример:

```text
Current user devices: 50
Infrastructure:        5
Expected growth:       20
Required capacity:     75
```

`/26` уже недостаточно:

```text
62 usable
```

Нужен `/25`:

```text
126 usable
```

Headroom выбирается по бизнес-плану, lifecycle оборудования и стоимости будущей renumbering, а не по универсальному проценту.

## Самый Маленький Практичный Prefix

Математическая цель:

```text
Найти самый длинный prefix, который покрывает requirement.
```

Практическая цель:

```text
Найти самый длинный prefix, который покрывает requirement,
infrastructure и разумный growth без ненужного waste.
```

Слишком маленькая subnet приводит к:

- раннему exhaustion;
- расширению DHCP scope через redesign;
- renumbering;
- добавлению secondary subnets;
- срочным изменениям VLAN design.

Слишком большая subnet приводит к:

- waste address space;
- большему broadcast domain;
- увеличенному fault scope;
- менее точной segmentation.

## Быстрые Граничные Значения

| Required usable hosts | Minimum host bits | Prefix | Capacity |
| ---: | ---: | ---: | ---: |
| 2 | 2 | `/30` | 2 |
| 3-6 | 3 | `/29` | 6 |
| 7-14 | 4 | `/28` | 14 |
| 15-30 | 5 | `/27` | 30 |
| 31-62 | 6 | `/26` | 62 |
| 63-126 | 7 | `/25` | 126 |
| 127-254 | 8 | `/24` | 254 |
| 255-510 | 9 | `/23` | 510 |
| 511-1022 | 10 | `/22` | 1022 |
| 1023-2046 | 11 | `/21` | 2046 |

Эта таблица быстро показывает важные переходы:

```text
62 hosts -> /26
63 hosts -> /25

254 hosts -> /24
255 hosts -> /23

510 hosts -> /23
511 hosts -> /22
```

## Host Requirement и Число Получаемых Subnets

После выбора child prefix количество equal-size subnets внутри parent:

```text
Number of child subnets = 2^(child prefix - parent prefix)
```

Пример:

```text
Parent: /16
Child:  /23
```

```text
2^(23 - 16) = 2^7 = 128 subnets
```

Host-based calculation определяет размер каждой subnet. Parent prefix определяет, сколько таких blocks доступно.

## Когда Требования Несовместимы

Дано:

```text
Parent:            192.168.10.0/24
Required subnets:  5
Required hosts:    50 per subnet
```

Для 50 hosts нужен `/26`.

Из `/24` можно получить:

```text
2^(26 - 24) = 4 subnets
```

Но требуется 5.

Значит, одного `/24` недостаточно.

Возможные решения:

- larger parent block, например `/23`;
- меньший host requirement;
- меньшее число networks;
- VLSM, если не все segments требуют 50 hosts;
- переработка design.

Всегда проверяйте оба ограничения, если они известны.

## FLSM и VLSM

Если всем segments требуется одинаковая capacity:

```text
FLSM
```

подходит хорошо.

Если требования различаются:

```text
Guest:       100 hosts
Employees:    50 hosts
POS:          12 hosts
Management:   10 hosts
WAN link:      2 hosts
```

одинаковая mask создаст waste. Здесь эффективнее VLSM:

```text
Guest:      /25
Employees:  /26
POS:        /28
Management: /28
WAN:        /30 or /31
```

Host-based sizing является основой VLSM.

## Практическое Задание

Для каждого scenario найдите:

- minimum host bits;
- child prefix;
- mask;
- increment;
- usable capacity;
- number of child subnets внутри parent;
- первые три network addresses.

### Задание 1

```text
Parent:         192.168.40.0/24
Required hosts: 25
```

### Задание 2

```text
Parent:         172.20.0.0/16
Required hosts: 700
```

### Задание 3

```text
Parent:         10.0.0.0/8
Required hosts: 4000
```

### Задание 4

```text
Parent:         192.0.2.0/24
Required hosts: 255
```

## Ответы

### Задание 1

```text
Host bits:    5
Prefix:       /27
Mask:         255.255.255.224
Increment:    32 in fourth octet
Capacity:     30 usable
Subnets:      8
Networks:     192.168.40.0, 192.168.40.32, 192.168.40.64
```

### Задание 2

```text
2^9 - 2 = 510    insufficient
2^10 - 2 = 1022  sufficient

Host bits:    10
Prefix:       /22
Mask:         255.255.252.0
Increment:    4 in third octet
Capacity:     1022 usable
Subnets:      64
Networks:     172.20.0.0, 172.20.4.0, 172.20.8.0
```

### Задание 3

```text
2^11 - 2 = 2046  insufficient
2^12 - 2 = 4094  sufficient

Host bits:    12
Prefix:       /20
Mask:         255.255.240.0
Increment:    16 in third octet
Capacity:     4094 usable
Subnets:      4096
Networks:     10.0.0.0, 10.0.16.0, 10.0.32.0
```

### Задание 4

Для 255 usable hosts требуется `/23`:

```text
2^8 - 2 = 254   insufficient
2^9 - 2 = 510   sufficient
```

Но `/23` больше parent `/24`. Поэтому requirement невозможно выполнить внутри указанного block.

## Проверка С Python `ipaddress`

```python
from ipaddress import ip_network

parent = ip_network("172.16.0.0/16")
children = list(parent.subnets(new_prefix=23))
first = children[0]

print(len(children))
print(first)
print(first.num_addresses)
print(first.network_address)
print(first.broadcast_address)
```

Ожидаемый результат:

```text
128
172.16.0.0/23
512
172.16.0.0
172.16.1.255
```

Traditional usable capacity:

```text
512 - 2 = 510
```

## Проверка На Cisco IOS

Назначение address из первой `/26`:

```text
Router(config)# interface gigabitEthernet 0/0
Router(config-if)# ip address 192.168.10.1 255.255.255.192
Router(config-if)# no shutdown
```

Проверка:

```text
Router# show ip interface brief
Router# show ip route connected
```

Connected route:

```text
192.168.10.0/26
```

IOS проверяет mask и address semantics, но не знает, какой growth запланирован бизнесом.

## Частые Ошибки

### Использовать `2^h >= hosts`

Для обычной subnet нужно учитывать два reserved addresses:

```text
2^h - 2 >= required hosts
```

### Выбрать `/26` Для 63 Hosts

`/26` предоставляет только 62 usable. Нужен `/25`.

### Забывать Gateway и Infrastructure

Требование по endpoints должно включать все interface addresses, а не только user devices.

### Выбирать Prefix Без Parent Network

Размер child subnet может не помещаться в parent allocation.

### Считать Address Достаточным Без Prefix

`172.16.10.0` не сообщает размер сети. Нужна запись вроде `172.16.10.0/24`.

### Брать Слишком Большой Запас Без Причины

Headroom полезен, но огромная subnet может ухудшить segmentation и расходовать allocation.

### Считать Increment Usable Capacity

Для `/26` increment и total addresses равны 64, но usable hosts равны 62.

### Не Проверять Второе Требование

Host capacity может выполняться, а необходимое число subnets нет.

## Контрольные Вопросы

### Вопрос 1

Какая формула определяет minimum host bits?

Ответ:

```text
2^h - 2 >= required usable hosts
```

### Вопрос 2

Какой prefix нужен для 50 hosts?

Ответ:

```text
/26, потому что он предоставляет 62 usable hosts.
```

### Вопрос 3

Какой prefix нужен для 63 hosts?

Ответ:

```text
/25. /26 предоставляет только 62 usable hosts.
```

### Вопрос 4

Каков increment `/23`?

Ответ:

```text
2 в третьем octet.
```

### Вопрос 5

Сколько `/26` subnets помещается в `/24`?

Ответ:

```text
2^(26 - 24) = 4.
```

### Вопрос 6

Почему 2000 hosts требуют `/21`?

Ответ:

```text
10 host bits дают 1022 usable, а 11 bits дают 2046.
32 - 11 = /21.
```

### Вопрос 7

Что делать, если required child prefix короче parent prefix?

Ответ:

```text
Child subnet не помещается в parent block.
Нужен larger allocation или изменение требований.
```

## Команды и Термины

| Термин | Значение |
| --- | --- |
| Host requirement | Требуемое число usable interface addresses в subnet. |
| Host bits | Bits справа от prefix boundary. |
| Headroom | Резерв capacity для роста и operations. |
| Infrastructure reservation | Addresses для gateway, AP, switches и services. |
| Child prefix | Prefix subnet, создаваемых внутри parent. |
| Parent prefix | Prefix исходного allocation. |
| Capacity | Число total или usable addresses в subnet. |
| FLSM | Equal-size subnet allocation. |
| VLSM | Allocation subnets разных размеров. |

## Что Повторить Позже

- Powers of two
- Prefix-to-mask conversion
- Interesting octet
- Network and broadcast ranges
- Subnetting by network requirement
- FLSM
- VLSM
- Capacity planning
- Address management and IPAM

