# Subnetting Через Границы Octets

Source: закрытая страница курса  
Date added: 2026-06-13  
Related plan item: Week 7 / Subnetting across octet boundaries  
Tags: subnetting, FLSM, CIDR, octet boundary, rollover, class A, class B, increment
Language: Russian
Translation pair: articles-en/2026-06/week-07/08-subnetting-across-octet-boundaries.md

## Кратко

Алгоритм subnetting не меняется для крупных parent networks. Сеть `/16` или `/8` рассчитывается теми же шагами, что и `/24`:

1. Найти минимальное количество borrowed bits.
2. Получить новый prefix и mask.
3. Определить interesting octet и increment.
4. Перечислить network ranges.
5. Проверить usable hosts.

Основная сложность заключается не в новой формуле, а в двух деталях:

- increment может находиться во втором, третьем или четвёртом octet;
- после достижения `256` значение octet обнуляется, а octet слева увеличивается на единицу.

Пример:

```text
172.16.0.0/16
Required subnets: 100

Borrowed bits: 7
New prefix:    /23
Mask:          255.255.254.0
Increment:     2 in the third octet
Subnets:       128
Usable hosts:  510 per subnet
```

## Ключевые Идеи

- CIDR prefix, а не исторический address class, определяет фактическую network boundary.
- Для FLSM число subnets равно `2^n`, где `n` является числом borrowed bits.
- Новый prefix равен исходному prefix плюс borrowed bits.
- Interesting octet содержит переход от network bits к host bits.
- Increment вычисляется как `256 - mask value` в interesting octet.
- Octet принимает значения только от `0` до `255`.
- При прибавлении increment и достижении `256` выполняется rollover в octet слева.
- Адрес с окончанием `.0` или `.255` не обязательно является network или broadcast.
- Роль address определяется prefix и границами конкретной subnet.
- Broadcast всегда находится непосредственно перед следующей network.
- Большое количество математически корректных hosts не означает хороший LAN design.

## Classful Термины и Современный CIDR

Исторически IPv4 unicast addresses делились на classes:

| Class | Первый octet | Default mask | Default prefix |
| --- | --- | --- | ---: |
| A | 1-126 | `255.0.0.0` | `/8` |
| B | 128-191 | `255.255.0.0` | `/16` |
| C | 192-223 | `255.255.255.0` | `/24` |

В старых учебных задачах выражение «subnet a Class B network» обычно означает:

```text
Начать с parent prefix /16.
```

«Class A» обычно означает:

```text
Начать с parent prefix /8.
```

Современные сети используют classless routing и CIDR. Поэтому:

```text
172.16.0.0/20
```

не следует рассчитывать как `/16` только потому, что `172` исторически попадал в Class B. Исходным является явно указанный `/20`.

В этой статье classful terms используются для связи с исходным курсом, а все реальные вычисления основаны на prefix.

## Один Алгоритм Для Любого Parent Prefix

Запишите входные данные:

```text
Parent network:
Parent prefix:
Required subnets:
Required hosts per subnet:
```

Затем:

1. Найдите минимальное `n`, где `2^n >= required subnets`.
2. Вычислите `new prefix = parent prefix + n`.
3. Преобразуйте prefix в dotted-decimal mask.
4. Найдите interesting octet.
5. Вычислите increment в этом octet.
6. Перечислите network addresses.
7. Найдите broadcast как address перед следующей network.
8. Найдите usable range.
9. Вычислите оставшиеся host bits.
10. Проверьте host capacity и parent boundary.

## Как Найти Interesting Octet

| Prefix range | Interesting octet |
| --- | --- |
| `/1` - `/8` | First |
| `/9` - `/16` | Second |
| `/17` - `/24` | Third |
| `/25` - `/30` | Fourth |

Примеры:

```text
/18 = 255.255.192.0
Interesting octet: third
Increment: 256 - 192 = 64
```

```text
/23 = 255.255.254.0
Interesting octet: third
Increment: 256 - 254 = 2
```

```text
/25 = 255.255.255.128
Interesting octet: fourth
Increment: 256 - 128 = 128
```

## Octet Rollover

Octet не может содержать `256`.

Если subnet progression приводит к:

```text
172.20.0.128 + 128
```

получается:

```text
172.20.0.256
```

Эта запись недопустима. `256` переносится в octet слева:

```text
172.20.1.0
```

Аналогично:

```text
10.0.192.0 + 64 in third octet
```

даёт:

```text
10.0.256.0 -> 10.1.0.0
```

Это обычное позиционное сложение, а не специальное исключение subnetting.

## Пример 1: `/16` На 100 Subnets

Дано:

```text
Parent network:    172.16.0.0/16
Required subnets:  100
```

### Шаг 1. Найти Borrowed Bits

```text
2^6 = 64    insufficient
2^7 = 128   sufficient
```

```text
Borrowed bits = 7
```

### Шаг 2. Получить Новый Prefix

```text
/16 + 7 = /23
```

Binary mask:

```text
11111111.11111111.11111110.00000000
```

Decimal mask:

```text
255.255.254.0
```

### Шаг 3. Найти Increment

Interesting octet является третьим:

```text
256 - 254 = 2
```

```text
Increment = 2 in the third octet
```

### Шаг 4. Перечислить Networks

```text
172.16.0.0/23
172.16.2.0/23
172.16.4.0/23
172.16.6.0/23
...
172.16.254.0/23
```

Всего:

```text
2^7 = 128 subnets
```

### Шаг 5. Найти Первый Range

Первая network:

```text
172.16.0.0/23
```

Следующая network:

```text
172.16.2.0/23
```

Следовательно:

```text
Network:    172.16.0.0
First host: 172.16.0.1
Last host:  172.16.1.254
Broadcast:  172.16.1.255
```

Обратите внимание: subnet охватывает два значения третьего octet:

```text
172.16.0.x
172.16.1.x
```

### Второй Range

```text
Network:    172.16.2.0
First host: 172.16.2.1
Last host:  172.16.3.254
Broadcast:  172.16.3.255
```

### Последний Range

```text
Network:    172.16.254.0
First host: 172.16.254.1
Last host:  172.16.255.254
Broadcast:  172.16.255.255
```

### Шаг 6. Проверить Hosts

После `/23` остаётся:

```text
32 - 23 = 9 host bits
```

```text
Total addresses: 2^9 = 512
Usable hosts:    2^9 - 2 = 510
```

Итог:

```text
128 subnets
510 usable hosts per subnet
```

## Почему `.0` и `.255` Могут Быть Usable

Рассмотрим:

```text
172.16.0.0/23
```

Его range:

```text
172.16.0.0 - 172.16.1.255
```

Только первый address всей `/23` является network:

```text
172.16.0.0
```

Только последний является broadcast:

```text
172.16.1.255
```

Поэтому эти addresses находятся внутри usable range:

```text
172.16.0.255
172.16.1.0
```

Полная проверка:

```text
First usable: 172.16.0.1
Last usable:  172.16.1.254
```

Окончание `.0` или `.255` само по себе ничего не доказывает. Нужно знать prefix и границы subnet.

## Правило Границ

Для обычной IPv4 subnet:

```text
First address of subnet = network
Last address of subnet  = broadcast
Everything between      = usable host range
```

Это правило иногда называют «Oreo rule»: два крайних addresses не назначаются hosts, а середина используется.

Полезнее воспринимать его не как мнемонику, а как binary:

- network имеет все host bits равными `0`;
- broadcast имеет все host bits равными `1`;
- промежуточные combinations являются host addresses.

## Пример 2: `/16` На 500 Subnets

Дано:

```text
Parent network:    172.20.0.0/16
Required subnets:  500
```

### Borrowed Bits

```text
2^8 = 256   insufficient
2^9 = 512   sufficient
```

```text
Borrowed bits = 9
```

### Новый Prefix

```text
/16 + 9 = /25
```

Mask:

```text
255.255.255.128
```

Binary role:

```text
NNNNNNNN.NNNNNNNN.SSSSSSSS.SHHHHHHH
```

Все 8 bits третьего octet и 1 bit четвёртого стали subnet bits.

### Increment

Interesting octet теперь четвёртый:

```text
256 - 128 = 128
```

```text
Increment = 128 in the fourth octet
```

### Network Progression

```text
172.20.0.0/25
172.20.0.128/25
172.20.1.0/25
172.20.1.128/25
172.20.2.0/25
172.20.2.128/25
...
172.20.255.128/25
```

Переход:

```text
172.20.0.128 + 128
= 172.20.0.256
= 172.20.1.0
```

### Первые Ranges

| Network | First host | Last host | Broadcast |
| --- | --- | --- | --- |
| `172.20.0.0/25` | `172.20.0.1` | `172.20.0.126` | `172.20.0.127` |
| `172.20.0.128/25` | `172.20.0.129` | `172.20.0.254` | `172.20.0.255` |
| `172.20.1.0/25` | `172.20.1.1` | `172.20.1.126` | `172.20.1.127` |
| `172.20.1.128/25` | `172.20.1.129` | `172.20.1.254` | `172.20.1.255` |

### Capacity

```text
Subnets:       2^9 = 512
Host bits:     32 - 25 = 7
Total/subnet:  2^7 = 128
Usable hosts:  2^7 - 2 = 126
```

Требование 500 subnets выполнено, остаётся 12 spare subnets.

## Пример 3: `/8` На 1000 Subnets

Дано:

```text
Parent network:    10.0.0.0/8
Required subnets:  1000
```

### Borrowed Bits

```text
2^9 = 512     insufficient
2^10 = 1024   sufficient
```

```text
Borrowed bits = 10
```

### Новый Prefix

```text
/8 + 10 = /18
```

Mask:

```text
255.255.192.0
```

Binary:

```text
11111111.11111111.11000000.00000000
```

Borrowing охватывает:

- все 8 bits второго octet;
- первые 2 bits третьего octet.

### Increment

Interesting octet является третьим:

```text
256 - 192 = 64
```

```text
Increment = 64 in the third octet
```

### Network Progression

```text
10.0.0.0/18
10.0.64.0/18
10.0.128.0/18
10.0.192.0/18
10.1.0.0/18
10.1.64.0/18
10.1.128.0/18
10.1.192.0/18
10.2.0.0/18
...
10.255.192.0/18
```

После четырёх `/18` blocks третьего octet происходит rollover:

```text
10.0.192.0 + 64
= 10.0.256.0
= 10.1.0.0
```

### Первые Ranges

| Network | First host | Last host | Broadcast |
| --- | --- | --- | --- |
| `10.0.0.0/18` | `10.0.0.1` | `10.0.63.254` | `10.0.63.255` |
| `10.0.64.0/18` | `10.0.64.1` | `10.0.127.254` | `10.0.127.255` |
| `10.0.128.0/18` | `10.0.128.1` | `10.0.191.254` | `10.0.191.255` |
| `10.0.192.0/18` | `10.0.192.1` | `10.0.255.254` | `10.0.255.255` |
| `10.1.0.0/18` | `10.1.0.1` | `10.1.63.254` | `10.1.63.255` |

### Capacity

```text
Subnets:       2^10 = 1024
Host bits:     32 - 18 = 14
Total/subnet:  2^14 = 16384
Usable hosts:  2^14 - 2 = 16382
```

Математика удовлетворяет требованию по subnets, но 16 382 hosts в одном broadcast domain обычно слишком много для практического user LAN.

## Математически Верно Не Значит Хорошо Спроектировано

Для design необходимо проверить:

- сколько endpoints действительно будет в segment;
- размер broadcast domain;
- fault domain;
- security boundaries;
- DHCP scope;
- wireless density;
- ARP и neighbor scale;
- growth;
- route summarization;
- operational complexity.

Пример `/18` может быть разумным для:

- large address pool за firewall/NAT;
- container или virtual infrastructure;
- специальной routed service network;
- дальнейшего VLSM allocation.

Но он не должен автоматически становиться одной VLAN с тысячами clients.

## Как Читать Ranges Без Ошибок

Для каждой subnet:

1. Запишите текущую network.
2. Запишите следующую network.
3. Вычтите один address из следующей network, чтобы получить broadcast.
4. Прибавьте один к текущей network для first host.
5. Вычтите один из broadcast для last host.

Пример:

```text
Current network: 172.16.2.0/23
Next network:    172.16.4.0/23
```

```text
Broadcast:  172.16.3.255
First host: 172.16.2.1
Last host:  172.16.3.254
```

Не угадывайте broadcast по внешнему виду address.

## Проверка Принадлежности Address

Вопрос:

```text
Является ли 172.16.3.0 usable address в 172.16.2.0/23?
```

Range:

```text
Network:    172.16.2.0
Broadcast:  172.16.3.255
Usable:     172.16.2.1 - 172.16.3.254
```

Ответ:

```text
Да, 172.16.3.0 находится внутри usable range.
```

Вопрос:

```text
Является ли 172.16.3.255 usable?
```

Ответ:

```text
Нет, это broadcast данной /23.
```

## Таблица Примеров

| Parent | Requirement | Borrowed | New prefix | Increment | Subnets | Usable hosts |
| --- | ---: | ---: | ---: | --- | ---: | ---: |
| `192.168.10.0/24` | 25 | 5 | `/29` | 8 in fourth | 32 | 6 |
| `172.16.0.0/16` | 100 | 7 | `/23` | 2 in third | 128 | 510 |
| `172.20.0.0/16` | 500 | 9 | `/25` | 128 in fourth | 512 | 126 |
| `10.0.0.0/8` | 1000 | 10 | `/18` | 64 in third | 1024 | 16382 |

## Практическое Задание

Для каждого scenario найдите:

- borrowed bits;
- new prefix;
- mask;
- interesting octet;
- increment;
- number of subnets;
- usable hosts per subnet;
- первые пять network addresses.

### Задание 1

```text
Parent:            172.30.0.0/16
Required subnets:  50
```

### Задание 2

```text
Parent:            172.31.0.0/16
Required subnets:  300
```

### Задание 3

```text
Parent:            10.0.0.0/8
Required subnets:  200
```

## Ответы

### Задание 1

```text
Borrowed bits: 6
New prefix:    /22
Mask:          255.255.252.0
Interesting:   third octet
Increment:     4
Subnets:       64
Usable hosts:  1022
Networks:
172.30.0.0
172.30.4.0
172.30.8.0
172.30.12.0
172.30.16.0
```

### Задание 2

```text
Borrowed bits: 9
New prefix:    /25
Mask:          255.255.255.128
Interesting:   fourth octet
Increment:     128
Subnets:       512
Usable hosts:  126
Networks:
172.31.0.0
172.31.0.128
172.31.1.0
172.31.1.128
172.31.2.0
```

### Задание 3

```text
Borrowed bits: 8
New prefix:    /16
Mask:          255.255.0.0
Interesting:   second octet
Increment:     1
Subnets:       256
Usable hosts:  65534
Networks:
10.0.0.0
10.1.0.0
10.2.0.0
10.3.0.0
10.4.0.0
```

Для `/16` маска второго octet равна `255`. Increment можно понимать как следующий полный second-octet value, то есть `1`. Формула `256 - mask octet` также даёт `1`.

## Проверка С Python `ipaddress`

Для лабораторной проверки можно использовать стандартный модуль Python:

```python
from ipaddress import ip_network

parent = ip_network("172.16.0.0/16")
subnets = list(parent.subnets(new_prefix=23))

print(len(subnets))
print(subnets[0])
print(subnets[1])
print(subnets[-1])
```

Ожидаемый результат:

```text
128
172.16.0.0/23
172.16.2.0/23
172.16.254.0/23
```

Инструмент полезен для проверки, но сначала выполните расчёт вручную.

## Частые Ошибки

### Начинать С Default Class Mask Вместо Указанного Prefix

Если дано `172.16.0.0/20`, parent prefix равен `/20`, а не `/16`.

### Считать Increment Не В Том Octet

Для `/23` increment равен `2` в третьем octet, а не `2` в четвёртом.

### Продолжать Считать После 255 Без Rollover

Неверно:

```text
10.0.256.0
```

Правильно:

```text
10.1.0.0
```

### Считать Любой `.0` Network Address

`172.16.1.0` является usable внутри `172.16.0.0/23`.

### Считать Любой `.255` Broadcast

`172.16.0.255` является usable внутри `172.16.0.0/23`.

### Забывать Octets Справа От Interesting Octet

Network address устанавливает все host bits справа в `0`. Broadcast устанавливает их в `1`.

### Не Проверять Host Capacity

1000 subnets из `/8` дают `/18`, но размер каждой subnet может быть чрезмерным для выбранной технологии и broadcast domain.

### Путать Total и Usable

`/23` содержит 512 total addresses, но 510 traditional usable hosts.

## Контрольные Вопросы

### Вопрос 1

Какой prefix получится, если из `/16` занять 7 bits?

Ответ:

```text
/23
```

### Вопрос 2

Каков increment для `/23`?

Ответ:

```text
2 в третьем octet.
```

### Вопрос 3

Каков broadcast для `172.16.2.0/23`?

Ответ:

```text
Следующая network равна 172.16.4.0,
поэтому broadcast равен 172.16.3.255.
```

### Вопрос 4

Можно ли назначить `172.16.3.0` host в `172.16.2.0/23`?

Ответ:

```text
Да. Usable range равен 172.16.2.1 - 172.16.3.254.
```

### Вопрос 5

Что идёт после `172.20.0.128/25`?

Ответ:

```text
172.20.1.0/25
```

### Вопрос 6

Сколько usable hosts в `/18`?

Ответ:

```text
2^(32 - 18) - 2 = 2^14 - 2 = 16382.
```

### Вопрос 7

Почему первый octet address не должен автоматически определять parent mask?

Ответ:

```text
Современная маршрутизация classless; фактическую boundary задаёт CIDR prefix.
```

## Команды и Термины

| Термин | Значение |
| --- | --- |
| Octet boundary | Переход между 8-bit группами IPv4 address. |
| Rollover | Перенос при достижении значения 256 в octet. |
| Interesting octet | Octet, в котором проходит network/host boundary. |
| Increment | Шаг между network addresses в interesting octet. |
| Borrowed bits | Host bits, превращённые в subnet bits. |
| Classful addressing | Историческая схема default `/8`, `/16` и `/24`. |
| CIDR | Classless addressing с явной prefix length. |
| FLSM | Equal-size child subnets с одинаковой mask. |
| Usable host | Address между network и broadcast обычной subnet. |

## Что Повторить Позже

- CIDR prefixes
- Interesting octet
- Increment and block size
- Binary rollover
- Network and broadcast calculation
- Subnetting by host requirement
- FLSM and VLSM
- Route summarization

