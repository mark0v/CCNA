# Subnetting по Требуемому Количеству Сетей

Source: закрытая страница курса  
Date added: 2026-06-13  
Related plan item: Week 7 / Subnetting by required subnets  
Tags: subnetting, FLSM, subnet mask, prefix, increment, network range, host bits
Language: Russian
Translation pair: articles-en/2026-06/week-07/07-subnetting-by-required-subnets.md

## Кратко

Subnetting начинается с обмена части host capacity на дополнительные networks.

Если исходная сеть имеет prefix `/24`, у неё 24 network bits и 8 host bits. Чтобы получить несколько меньших subnets одинакового размера, нужно занять несколько host bits и сделать их subnet bits.

Базовый процесс:

1. Определить требуемое количество subnets.
2. Найти минимальное число borrowed bits, для которого `2^n` покрывает требование.
3. Прибавить borrowed bits к исходному prefix.
4. Найти subnet increment.
5. Перечислить network ranges.
6. Проверить usable hosts в каждой новой subnet.

Пример:

```text
Исходная сеть:       192.168.10.0/24
Требуется subnets:   25
Borrowed bits:       5
Новый prefix:        /29
Новая mask:          255.255.255.248
Increment:           8
Subnets получено:    32
Usable hosts/subnet: 6
```

## Ключевые Идеи

- Network bits обозначаются единицами subnet mask.
- Host bits обозначаются нулями subnet mask.
- Borrowing превращает host bits в network bits.
- Заимствование `n` bits создаёт `2^n` equal-size subnets.
- Если остаётся `h` host bits, обычная subnet предоставляет `2^h - 2` usable host addresses.
- Новый prefix равен исходному prefix плюс borrowed bits.
- Increment показывает расстояние между соседними network addresses.
- Broadcast address находится непосредственно перед следующей network.
- Первый usable host идёт после network address.
- Последний usable host идёт перед broadcast address.
- Количество subnets округляется вверх до ближайшей степени двойки.
- FLSM создаёт subnets одинакового размера.
- Перед утверждением дизайна нужно проверить и число subnets, и host capacity.

## Что Именно Мы Меняем

Исходная сеть:

```text
192.168.10.0/24
```

Маска `/24` в binary:

```text
11111111.11111111.11111111.00000000
```

Обозначим роли bits:

```text
NNNNNNNN.NNNNNNNN.NNNNNNNN.HHHHHHHH
```

Здесь:

- `N` является network bit;
- `H` является host bit.

Если занять 5 host bits:

```text
NNNNNNNN.NNNNNNNN.NNNNNNNN.SSSSSHHH
```

где `S` является borrowed subnet bit.

Новая маска:

```text
11111111.11111111.11111111.11111000
```

В decimal:

```text
255.255.255.248
```

В CIDR:

```text
/29
```

## Главный Компромисс

Subnetting выполняет обмен:

```text
More network bits -> more subnets -> fewer hosts per subnet
```

Для исходного `/24`:

| Borrowed bits | New prefix | Subnets | Host bits left | Usable hosts/subnet |
| ---: | ---: | ---: | ---: | ---: |
| 0 | `/24` | 1 | 8 | 254 |
| 1 | `/25` | 2 | 7 | 126 |
| 2 | `/26` | 4 | 6 | 62 |
| 3 | `/27` | 8 | 5 | 30 |
| 4 | `/28` | 16 | 4 | 14 |
| 5 | `/29` | 32 | 3 | 6 |
| 6 | `/30` | 64 | 2 | 2 |

Для обычных LAN subnet calculations `/31` и `/32` требуют отдельного рассмотрения и не подчиняются стандартному ожиданию `2^h - 2` так же, как prefixes от `/30` и короче.

## Формулы

### Количество Subnets

```text
Number of subnets = 2^n
```

где `n` является числом borrowed bits.

### Total Addresses в Каждой Subnet

```text
Total addresses = 2^h
```

где `h` является числом оставшихся host bits.

### Usable Hosts в Обычной Subnet

```text
Usable hosts = 2^h - 2
```

Два addresses исключаются:

- network address;
- broadcast address.

### Новый Prefix

```text
New prefix = original prefix + borrowed bits
```

## Важное Уточнение О Subnet Zero

Современный расчёт включает все созданные subnets, в том числе:

- первую, у которой subnet bits равны всем нулям;
- последнюю, у которой subnet bits равны всем единицам.

Поэтому 5 borrowed bits дают:

```text
2^5 = 32 subnets
```

а не 30.

Старые материалы могут использовать правило `2^n - 2` для количества subnets. Оно связано с устаревшим исключением subnet zero и all-ones subnet. Для современного CCNA design и обычного Cisco configuration используется `2^n`.

## Трёхэтапная Модель

Исходный материал можно свести к трём крупным этапам:

1. Найти количество нужных subnet bits.
2. Построить mask и определить increment.
3. Использовать increment для перечисления ranges.

Практически полезно добавить четвёртый:

4. Проверить, хватает ли usable hosts в каждой subnet.

Без этой проверки можно выполнить требование по числу networks и получить subnets, в которые не помещаются устройства.

## Пример 1: Разделить `/24` На 25 Subnets

Дано:

```text
Parent network:    192.168.10.0/24
Required subnets:  25
```

### Шаг 1. Найти Borrowed Bits

Нужно найти минимальное `n`, при котором:

```text
2^n >= 25
```

Проверяем:

```text
2^4 = 16   insufficient
2^5 = 32   sufficient
```

Требуется:

```text
5 borrowed bits
```

Не нужно переводить само число `25` в binary для построения network ranges. Важно определить минимальную ширину binary field, которая предоставляет не менее 25 combinations.

### Шаг 2. Получить Новый Prefix

```text
Original prefix: /24
Borrowed bits:    5
New prefix:       /29
```

Binary mask:

```text
11111111.11111111.11111111.11111000
```

Decimal mask:

```text
255.255.255.248
```

### Шаг 3. Найти Increment

Есть два эквивалентных способа.

#### Способ A: Значение Последнего Network Bit

Последний network bit в интересующем octet имеет вес:

```text
8
```

Следовательно:

```text
Increment = 8
```

#### Способ B: Формула 256 Минус Mask Octet

```text
Increment = 256 - 248 = 8
```

Формула применяется к interesting octet, то есть к octet, где mask не равна ни `255`, ни `0`.

### Шаг 4. Перечислить Network Addresses

Прибавляем increment:

```text
192.168.10.0
192.168.10.8
192.168.10.16
192.168.10.24
192.168.10.32
192.168.10.40
...
192.168.10.248
```

Получено 32 networks:

```text
0, 8, 16, 24, ..., 248
```

### Шаг 5. Построить Ranges

Каждая subnet содержит 8 total addresses.

| Subnet | Network | First host | Last host | Broadcast |
| ---: | --- | --- | --- | --- |
| 1 | `192.168.10.0/29` | `192.168.10.1` | `192.168.10.6` | `192.168.10.7` |
| 2 | `192.168.10.8/29` | `192.168.10.9` | `192.168.10.14` | `192.168.10.15` |
| 3 | `192.168.10.16/29` | `192.168.10.17` | `192.168.10.22` | `192.168.10.23` |
| 4 | `192.168.10.24/29` | `192.168.10.25` | `192.168.10.30` | `192.168.10.31` |
| 5 | `192.168.10.32/29` | `192.168.10.33` | `192.168.10.38` | `192.168.10.39` |
| ... | ... | ... | ... | ... |
| 32 | `192.168.10.248/29` | `192.168.10.249` | `192.168.10.254` | `192.168.10.255` |

Правило:

```text
Broadcast = next network - 1
First host = network + 1
Last host = broadcast - 1
```

### Шаг 6. Проверить Host Capacity

После borrowing остаётся:

```text
8 original host bits - 5 borrowed bits = 3 host bits
```

Total addresses:

```text
2^3 = 8
```

Usable hosts:

```text
2^3 - 2 = 6
```

Результат:

```text
32 subnets
6 usable hosts per subnet
```

Требование 25 subnets выполнено. Но этот design пригоден только тогда, когда каждому segment достаточно максимум 6 обычных host addresses.

## Почему Получается 32, Хотя Нужно 25

Binary fields предоставляют combinations степенями двойки:

```text
1, 2, 4, 8, 16, 32, 64, ...
```

Невозможно занять «часть bit» и получить ровно 25 equal subnets.

Четырёх bits недостаточно:

```text
2^4 = 16
```

Пять bits дают:

```text
2^5 = 32
```

Семь оставшихся subnets можно:

- зарезервировать для роста;
- оставить нераспределёнными;
- использовать для новых sites;
- учитывать в IP address plan.

## Binary Представление Subnet ID

Пять borrowed bits образуют subnet ID от:

```text
00000
```

до:

```text
11111
```

Вместе с тремя host bits:

```text
SSSSSHHH
```

Примеры:

| Subnet bits | Host bits at network | Last octet decimal |
| --- | --- | ---: |
| `00000` | `000` | 0 |
| `00001` | `000` | 8 |
| `00010` | `000` | 16 |
| `00011` | `000` | 24 |
| `00100` | `000` | 32 |
| `11111` | `000` | 248 |

Increment `8` возникает потому, что три host bits формируют блок:

```text
2^3 = 8 addresses
```

## Network, Hosts и Broadcast В Binary

Вторая subnet:

```text
192.168.10.8/29
```

Последний octet network address:

```text
00001000
```

Пять subnet bits и три host bits:

```text
00001|000
```

Network address имеет все host bits равными нулю:

```text
00001|000 = 8
```

Первый host:

```text
00001|001 = 9
```

Последний host:

```text
00001|110 = 14
```

Broadcast имеет все host bits равными единице:

```text
00001|111 = 15
```

Это показывает, что network и broadcast не являются произвольными исключениями. Их роли следуют непосредственно из состояния host bits.

## Пример 2: Разделить `/24` На 60 Subnets

Дано:

```text
Parent network:    216.5.10.0/24
Required subnets:  60
```

### Найти Borrowed Bits

```text
2^5 = 32   insufficient
2^6 = 64   sufficient
```

Требуется:

```text
6 borrowed bits
```

### Найти Новый Prefix

```text
/24 + 6 = /30
```

Mask:

```text
255.255.255.252
```

Binary:

```text
11111111.11111111.11111111.11111100
```

### Найти Increment

```text
256 - 252 = 4
```

Network addresses:

```text
216.5.10.0
216.5.10.4
216.5.10.8
216.5.10.12
216.5.10.16
...
216.5.10.252
```

### Первые Ranges

| Subnet | Network | First host | Last host | Broadcast |
| ---: | --- | --- | --- | --- |
| 1 | `216.5.10.0/30` | `216.5.10.1` | `216.5.10.2` | `216.5.10.3` |
| 2 | `216.5.10.4/30` | `216.5.10.5` | `216.5.10.6` | `216.5.10.7` |
| 3 | `216.5.10.8/30` | `216.5.10.9` | `216.5.10.10` | `216.5.10.11` |
| 4 | `216.5.10.12/30` | `216.5.10.13` | `216.5.10.14` | `216.5.10.15` |
| ... | ... | ... | ... | ... |
| 64 | `216.5.10.252/30` | `216.5.10.253` | `216.5.10.254` | `216.5.10.255` |

### Проверить Host Capacity

Остаётся 2 host bits:

```text
2^2 = 4 total addresses
2^2 - 2 = 2 usable hosts
```

Результат:

```text
64 subnets
2 usable hosts per subnet
```

Такой `/30` подходит для traditional point-to-point links, но обычно не подходит для LAN с несколькими endpoints.

## Почему `/30` Полезен

Point-to-point link соединяет ровно два Layer 3 interfaces:

```text
Router A <--------> Router B
```

Для традиционного IPv4 design `/30` предоставляет:

- один network address;
- два usable interface addresses;
- один broadcast address.

Пример:

```text
10.0.0.0/30
```

```text
Network:    10.0.0.0
Router A:   10.0.0.1
Router B:   10.0.0.2
Broadcast:  10.0.0.3
```

Современные point-to-point links также могут использовать `/31` по RFC 3021, если это поддерживают устройства, provider design и operational tools. Но `/30` остаётся важным для обучения и совместимости.

## Increment и Block Size

В этом контексте термины часто используются как синонимы:

```text
Increment = block size
```

Для маски `/29`:

```text
Mask octet: 248
Block size:  256 - 248 = 8
```

Для `/30`:

```text
Mask octet: 252
Block size:  256 - 252 = 4
```

Также:

```text
Block size = 2^(host bits in interesting octet)
```

Для `/29` в последнем octet остаётся 3 host bits:

```text
2^3 = 8
```

## Таблица Increment Для Последнего Octet

| Prefix | Mask | Increment | Total addresses | Usable hosts |
| ---: | --- | ---: | ---: | ---: |
| `/25` | `255.255.255.128` | 128 | 128 | 126 |
| `/26` | `255.255.255.192` | 64 | 64 | 62 |
| `/27` | `255.255.255.224` | 32 | 32 | 30 |
| `/28` | `255.255.255.240` | 16 | 16 | 14 |
| `/29` | `255.255.255.248` | 8 | 8 | 6 |
| `/30` | `255.255.255.252` | 4 | 4 | 2 |

Эта таблица является следствием binary, а не набором случайных значений.

## Interesting Octet

Interesting octet является octet маски, в котором проходит граница между network и host bits.

Примеры:

```text
/26 = 255.255.255.192
Interesting octet: fourth
```

```text
/20 = 255.255.240.0
Interesting octet: third
```

Increment вычисляется именно в нём:

```text
/20 -> 256 - 240 = 16
```

Network addresses для `172.16.0.0/20` меняются в третьем octet:

```text
172.16.0.0
172.16.16.0
172.16.32.0
172.16.48.0
...
```

## Проверка Требований По Hosts

Предположим:

```text
Parent:            192.168.10.0/24
Required subnets:  25
Required hosts:    10 per subnet
```

Для 25 subnets требуется 5 borrowed bits:

```text
/24 -> /29
```

Но `/29` предоставляет только:

```text
6 usable hosts
```

Требования несовместимы внутри одного `/24`.

Нельзя получить одновременно 25 equal subnets по 10 usable hosts из 256 total addresses. Даже без учёта network и broadcast потребовалось бы:

```text
25 * 10 = 250 host addresses
```

а служебные addresses увеличивают потребность ещё сильнее.

Возможные решения:

- получить larger parent block;
- уменьшить число subnets;
- уменьшить host requirement;
- применить VLSM, если segments имеют разные размеры;
- изменить архитектуру.

## FLSM и VLSM

Текущая техника создаёт equal-size subnets:

```text
FLSM = Fixed Length Subnet Mask
```

Все child networks получают одинаковый prefix.

Пример:

```text
192.168.10.0/24 -> 32 x /29
```

Если одним segments нужно 60 hosts, другим 12, а links только 2, одинаковый размер может расходовать address space неэффективно.

Тогда используется:

```text
VLSM = Variable Length Subnet Mask
```

VLSM выделяет разные prefixes разным требованиям. Но сначала нужно уверенно понимать FLSM, increment и boundaries.

## Практический Алгоритм

### Входные Данные

Запишите:

```text
Parent network:
Parent prefix:
Required subnets:
Required hosts per subnet:
```

Если host requirement неизвестен, результат нельзя считать полностью подтверждённым design.

### Расчёт

1. Найти минимальное `n`, где `2^n >= required subnets`.
2. Вычислить `new prefix = original prefix + n`.
3. Найти новую dotted-decimal mask.
4. Определить interesting octet.
5. Вычислить `increment = 256 - mask octet`.
6. Перечислить network addresses с этим шагом.
7. Для каждой subnet найти broadcast как `next network - 1`.
8. Найти first и last usable hosts.
9. Вычислить оставшиеся host bits.
10. Проверить `2^h - 2` против host requirement.
11. Проверить, что все child subnets находятся внутри parent block.
12. Задокументировать allocation.

## Worked Exercise

Дано:

```text
Parent network:    10.40.8.0/24
Required subnets:  10
```

### Borrowed Bits

```text
2^3 = 8    insufficient
2^4 = 16   sufficient
```

```text
Borrowed bits = 4
```

### Новый Prefix

```text
/24 + 4 = /28
```

```text
Mask = 255.255.255.240
```

### Increment

```text
256 - 240 = 16
```

### Capacity

```text
Subnets:        2^4 = 16
Host bits:      4
Total/subnet:   2^4 = 16
Usable/subnet:  2^4 - 2 = 14
```

### Первые Networks

```text
10.40.8.0/28
10.40.8.16/28
10.40.8.32/28
10.40.8.48/28
10.40.8.64/28
...
```

### Первые Ranges

| Network | Usable range | Broadcast |
| --- | --- | --- |
| `10.40.8.0/28` | `10.40.8.1 - 10.40.8.14` | `10.40.8.15` |
| `10.40.8.16/28` | `10.40.8.17 - 10.40.8.30` | `10.40.8.31` |
| `10.40.8.32/28` | `10.40.8.33 - 10.40.8.46` | `10.40.8.47` |
| `10.40.8.48/28` | `10.40.8.49 - 10.40.8.62` | `10.40.8.63` |

## Практическое Задание

Для каждого примера найдите:

- borrowed bits;
- new prefix;
- dotted-decimal mask;
- increment;
- number of produced subnets;
- usable hosts per subnet;
- первые три network addresses.

### Задание 1

```text
172.16.50.0/24
Required subnets: 6
```

### Задание 2

```text
10.20.30.0/24
Required subnets: 12
```

### Задание 3

```text
192.0.2.0/24
Required subnets: 50
```

## Ответы

### Задание 1

```text
Borrowed bits: 3
New prefix:    /27
Mask:          255.255.255.224
Increment:     32
Subnets:       8
Usable hosts:  30
Networks:      172.16.50.0, 172.16.50.32, 172.16.50.64
```

### Задание 2

```text
Borrowed bits: 4
New prefix:    /28
Mask:          255.255.255.240
Increment:     16
Subnets:       16
Usable hosts:  14
Networks:      10.20.30.0, 10.20.30.16, 10.20.30.32
```

### Задание 3

```text
Borrowed bits: 6
New prefix:    /30
Mask:          255.255.255.252
Increment:     4
Subnets:       64
Usable hosts:  2
Networks:      192.0.2.0, 192.0.2.4, 192.0.2.8
```

## Проверка С Cisco IOS

После расчёта subnet можно назначить interface address:

```text
Router(config)# interface gigabitEthernet 0/0
Router(config-if)# ip address 192.168.10.1 255.255.255.248
Router(config-if)# no shutdown
```

Проверка:

```text
Router# show ip interface brief
Router# show ip route connected
```

Connected route должна отражать:

```text
192.168.10.0/29
```

Router не проверяет бизнес-требование по количеству hosts. Он только применяет корректную mask. Ответственность за sizing остаётся у инженера.

## Частые Ошибки

### Выбирать Степень Двойки Меньше Требования

Для 25 subnets:

```text
2^4 = 16
```

недостаточно. Нужно округлить вверх до 32.

### Прибавлять Число Subnets К Prefix

Неверно:

```text
/24 + 25
```

К prefix прибавляются borrowed bits, а не число networks:

```text
/24 + 5 = /29
```

### Использовать `2^n - 2` Для Современного Числа Subnets

Современный расчёт:

```text
2^n
```

### Забывать Проверить Hosts

25 subnets из `/24` дают `/29`, но только 6 usable hosts в каждой.

### Считать Increment Количеством Usable Hosts

Для `/29` increment равен 8, но usable hosts равны 6.

### Делать Broadcast Равным Следующей Network

Broadcast находится на один address раньше:

```text
Next network: 192.168.10.8
Broadcast:    192.168.10.7
```

### Назначать Network Или Broadcast Interface

В обычной `/29` нельзя назначать:

```text
192.168.10.0
192.168.10.7
```

### Выходить За Parent Block

Child subnets должны полностью находиться внутри исходной allocation.

### Полагаться На Classful Термины

`192.168.10.0/24` иногда неформально называют Class C network, но современный design использует CIDR prefix. Сам первый octet не определяет фактическую mask.

## Контрольные Вопросы

### Вопрос 1

Сколько bits нужно занять, чтобы получить минимум 25 subnets?

Ответ:

```text
5 bits, потому что 2^5 = 32.
```

### Вопрос 2

Какой prefix получится из `/24` после borrowing 5 bits?

Ответ:

```text
/29
```

### Вопрос 3

Какова mask для `/29`?

Ответ:

```text
255.255.255.248
```

### Вопрос 4

Каков increment `/29` в четвёртом octet?

Ответ:

```text
256 - 248 = 8
```

### Вопрос 5

Сколько usable hosts предоставляет обычная `/29`?

Ответ:

```text
2^3 - 2 = 6
```

### Вопрос 6

Как найти broadcast для `192.168.10.16/29`?

Ответ:

```text
Следующая network начинается с 192.168.10.24,
поэтому broadcast равен 192.168.10.23.
```

### Вопрос 7

Почему требование «25 subnets по 10 hosts» нельзя выполнить из одного `/24` с помощью FLSM?

Ответ:

```text
Для 25 subnets нужен `/29`, а он предоставляет только 6 usable hosts.
```

## Команды и Термины

| Термин | Значение |
| --- | --- |
| Parent network | Исходный block, который делится на child subnets. |
| Borrowed bit | Host bit, превращённый в network/subnet bit. |
| FLSM | Деление на equal-size subnets с одной mask. |
| VLSM | Выделение subnets разных размеров. |
| Prefix length | Количество network bits в mask. |
| Interesting octet | Octet, содержащий boundary network/host. |
| Increment | Расстояние между соседними network addresses. |
| Block size | Total addresses в одном aligned subnet block. |
| Network address | Первый address обычной subnet, все host bits равны 0. |
| Broadcast address | Последний address обычной subnet, все host bits равны 1. |
| Usable range | Addresses между network и broadcast. |

## Что Повторить Позже

- Binary subnet masks
- Powers of two
- Interesting octet
- Block size method
- Finding network and broadcast addresses
- FLSM
- VLSM
- `/31` point-to-point addressing
- Route summarization

