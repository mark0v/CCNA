# Практика Subnetting по Количеству Networks

Source: закрытая страница курса  
Date added: 2026-06-13  
Related plan item: Week 7 / Network-based subnetting practice  
Tags: subnetting, practice, networks, FLSM, borrowed bits, increment, self-check
Language: Russian
Translation pair: articles-en/2026-06/week-07/11-network-based-subnetting-practice.md

## Кратко

В network-based subnetting исходное требование определяет минимальное количество child networks.

Основная формула:

```text
2^n >= required subnets
```

где `n` является числом host bits, которые нужно занять и превратить в subnet bits.

После этого:

```text
Child prefix = parent prefix + n
```

Но расчёт не заканчивается выбором mask. Нужно проверить, сколько host bits осталось и достаточно ли usable addresses в каждой получившейся subnet.

Эта статья является самостоятельным практикумом. Сначала решите четыре задачи, затем переходите к answer key.

## Что Нужно Найти

Для каждой задачи определите:

1. Minimum borrowed bits.
2. Child prefix.
3. Dotted-decimal mask.
4. Interesting octet.
5. Increment.
6. Actual number of child subnets.
7. Remaining host bits.
8. Total и usable addresses per child subnet.
9. Первые три network addresses.
10. Network, first host, last host и broadcast первой child subnet.
11. Выполнимо ли требование внутри parent block.
12. Хватает ли host capacity, если она указана.

## Рабочий Алгоритм

```text
1. Find n: 2^n >= required subnets
2. Child prefix = parent prefix + n
3. Confirm child prefix <= 30 for ordinary LAN subnets
4. Convert prefix to subnet mask
5. Find interesting octet
6. Increment = 256 - mask value in interesting octet
7. Actual child subnets = 2^n
8. Remaining host bits = 32 - child prefix
9. Usable hosts = 2^h - 2
10. List child networks
11. Broadcast = next network - 1
12. Validate every stated requirement
```

## Правила Практики

- Не открывайте answer key до завершения всех задач.
- Всегда округляйте required subnets вверх до степени двойки.
- К parent prefix прибавляются borrowed bits, а не число networks.
- Используйте современную формулу `2^n`, включая subnet zero.
- Считайте increment в interesting octet.
- Выполняйте rollover при достижении `256`.
- Проверяйте оставшуюся host capacity.
- Сохраняйте каждый child block внутри parent allocation.

## Шаблон Ответа

```text
Parent:
Required subnets:
Required hosts per subnet, if given:

Borrowed bits:
Subnet-count check:
Child prefix:
Mask:
Interesting octet:
Increment:
Actual child subnets:
Remaining host bits:
Total addresses/subnet:
Usable hosts/subnet:

Network 1:
Network 2:
Network 3:

First subnet:
  Network:
  First host:
  Last host:
  Broadcast:

Requirement feasible: yes/no
Reason:
```

---

## Задание 1: Branch Offices

Дано:

```text
Parent network:   192.168.80.0/24
Required subnets: 6
```

Дополнительный вопрос:

```text
Сможет ли каждая child subnet поддержать 25 usable hosts?
```

---

## Задание 2: Regional Sites

Дано:

```text
Parent network:   172.24.0.0/16
Required subnets: 100
```

Дополнительный вопрос:

```text
Является ли 172.24.1.255 broadcast первой child subnet?
```

---

## Задание 3: Enterprise Expansion

Дано:

```text
Parent network:   10.0.0.0/8
Required subnets: 700
```

Дополнительный вопрос:

```text
Какая network следует после 10.0.224.0?
```

---

## Задание 4: Конфликт Требований

Дано:

```text
Parent network:            192.0.2.0/24
Required subnets:          20
Required usable hosts:     20 per subnet
```

Сначала выберите prefix по числу networks, затем проверьте host capacity.

Дополнительный вопрос:

```text
Какой минимальный larger parent prefix позволит получить
не менее 20 equal subnets по 20 usable hosts?
```

---

## Остановитесь Перед Проверкой

Для каждой задачи должны быть записаны:

- две соседние powers of two;
- borrowed bits;
- child prefix и mask;
- increment;
- host capacity;
- первые три networks;
- первый полный range;
- итоговый вывод.

Узнавание чужого решения не заменяет самостоятельный расчёт.

---

## Answer Key

## Решение 1: Branch Offices

Дано:

```text
Parent:            192.168.80.0/24
Required subnets:  6
```

### Borrowed Bits

```text
2^2 = 4   insufficient
2^3 = 8   sufficient
```

```text
Borrowed bits = 3
```

### Prefix и Mask

```text
Child prefix = /24 + 3 = /27
Mask         = 255.255.255.224
```

### Increment

```text
256 - 224 = 32 in the fourth octet
```

### Capacity

```text
Actual subnets:       2^3 = 8
Remaining host bits:  32 - 27 = 5
Total addresses:      2^5 = 32
Usable hosts:         2^5 - 2 = 30
```

### Первые Networks

```text
192.168.80.0/27
192.168.80.32/27
192.168.80.64/27
```

### Первый Range

```text
Network:    192.168.80.0
First host: 192.168.80.1
Last host:  192.168.80.30
Broadcast:  192.168.80.31
```

### Дополнительный Вопрос

Каждая `/27` предоставляет 30 usable hosts, поэтому требование 25 hosts выполняется.

### Итог

```text
Requirement feasible: yes
Produced: 8 subnets, each with 30 usable hosts
```

## Решение 2: Regional Sites

Дано:

```text
Parent:            172.24.0.0/16
Required subnets:  100
```

### Borrowed Bits

```text
2^6 = 64    insufficient
2^7 = 128   sufficient
```

```text
Borrowed bits = 7
```

### Prefix и Mask

```text
Child prefix = /16 + 7 = /23
Mask         = 255.255.254.0
```

### Increment

```text
256 - 254 = 2 in the third octet
```

### Capacity

```text
Actual subnets:       128
Remaining host bits:  9
Total addresses:      512
Usable hosts:         510
```

### Первые Networks

```text
172.24.0.0/23
172.24.2.0/23
172.24.4.0/23
```

### Первый Range

```text
Network:    172.24.0.0
First host: 172.24.0.1
Last host:  172.24.1.254
Broadcast:  172.24.1.255
```

### Дополнительный Вопрос

Да:

```text
172.24.1.255
```

является broadcast первой `/23`, потому что следующая network начинается с `172.24.2.0`.

### Итог

```text
Requirement feasible: yes
Produced: 128 subnets, each with 510 usable hosts
```

## Решение 3: Enterprise Expansion

Дано:

```text
Parent:            10.0.0.0/8
Required subnets:  700
```

### Borrowed Bits

```text
2^9 = 512     insufficient
2^10 = 1024   sufficient
```

```text
Borrowed bits = 10
```

### Prefix и Mask

```text
Child prefix = /8 + 10 = /18
Mask         = 255.255.192.0
```

### Increment

```text
256 - 192 = 64 in the third octet
```

### Capacity

```text
Actual subnets:       1024
Remaining host bits:  14
Total addresses:      16384
Usable hosts:         16382
```

### Первые Networks

```text
10.0.0.0/18
10.0.64.0/18
10.0.128.0/18
```

Четвёртая:

```text
10.0.192.0/18
```

Пятая после rollover:

```text
10.1.0.0/18
```

### Первый Range

```text
Network:    10.0.0.0
First host: 10.0.0.1
Last host:  10.0.63.254
Broadcast:  10.0.63.255
```

### Дополнительный Вопрос

`10.0.224.0` не является boundary `/18`, потому что `/18` networks в третьем octet начинаются только с:

```text
0, 64, 128, 192
```

Address `10.0.224.0` находится внутри:

```text
10.0.192.0/18
```

Следующая network после этого block:

```text
10.1.0.0/18
```

Это дополнительная проверка alignment: прибавлять increment следует к network boundary, а не к произвольному address.

### Итог

```text
Requirement feasible: yes
Produced: 1024 subnets, each with 16382 usable hosts
```

Практический design должен отдельно оценить чрезмерный размер broadcast domain.

## Решение 4: Конфликт Требований

Дано:

```text
Parent:            192.0.2.0/24
Required subnets:  20
Required hosts:    20 per subnet
```

### Prefix По Числу Networks

```text
2^4 = 16   insufficient
2^5 = 32   sufficient
```

```text
Borrowed bits = 5
Child prefix  = /24 + 5 = /29
```

Mask:

```text
255.255.255.248
```

Increment:

```text
8
```

### Host Capacity

```text
Remaining host bits: 3
Total addresses:     8
Usable hosts:        6
```

Требуется 20 usable hosts, поэтому `/29` не подходит.

### Prefix По Числу Hosts

```text
2^4 - 2 = 14   insufficient
2^5 - 2 = 30   sufficient
```

Для hosts нужен:

```text
/27
```

Но `/24` содержит только:

```text
2^(27 - 24) = 8 subnets
```

а нужно 20.

### Минимальный Larger Parent

Каждая child subnet должна быть `/27`. Для 20 networks нужно минимум 32 equal blocks:

```text
2^5 = 32
```

Parent prefix:

```text
/27 - 5 borrowed levels = /22
```

Минимальный parent size:

```text
/22
```

Однако `192.0.2.0` не является `/22` network boundary. `/22` boundaries в третьем octet идут с шагом `4`.

Значение `2` входит в block:

```text
192.0.0.0/22
```

который охватывает:

```text
192.0.0.0 - 192.0.3.255
```

Если allocation должна начинаться именно с `192.0.2.0`, единый aligned `/22` с такой network address невозможен. Нужен другой aligned block или несколько allocations.

### Итог

```text
Requirement feasible in /24: no
Minimum equal-size parent prefix: /22
Required child size: /27
```

## Сводная Таблица

| Task | Parent | Required networks | Child prefix | Produced | Usable hosts | Feasible |
| ---: | --- | ---: | ---: | ---: | ---: | --- |
| 1 | `192.168.80.0/24` | 6 | `/27` | 8 | 30 | Yes |
| 2 | `172.24.0.0/16` | 100 | `/23` | 128 | 510 | Yes |
| 3 | `10.0.0.0/8` | 700 | `/18` | 1024 | 16382 | Yes |
| 4 | `192.0.2.0/24` | 20 | `/29` by network count | 32 | 6 | No, needs 20 hosts |

## Как Разбирать Ошибки

| Тип ошибки | Пример | Что повторить |
| --- | --- | --- |
| Requirement | Решалась задача по hosts вместо networks | Типы subnetting questions |
| Rounding | Для 100 выбрано 6 bits | Следующая power of two |
| Prefix | К `/16` прибавлено 100 | Borrowed bits |
| Formula | Использовано `2^n - 2` для subnets | Modern subnet-zero rule |
| Octet | Increment `/23` применён в четвёртом octet | Interesting octet |
| Rollover | Записан address с octet `256` | Positional carry |
| Alignment | Произвольный address принят за network | Block boundaries |
| Hosts | Проверено число networks, но не capacity | Remaining host bits |
| Parent | Child blocks вышли за allocation | Parent containment |

## Журнал Повторной Попытки

```text
Task:
My borrowed bits:
My child prefix:
My first three networks:
First incorrect step:
Correct rule:
Second attempt:
```

Повторите задачу без просмотра готового решения после того, как нашли первое ошибочное действие.

## Проверка С Python

После ручного расчёта:

```python
from ipaddress import ip_network

parent = ip_network("172.24.0.0/16")
children = list(parent.subnets(new_prefix=23))

print(len(children))
print(children[:3])
print(children[0].broadcast_address)
print(children[0].num_addresses - 2)
```

Ожидаемый результат:

```text
128
[IPv4Network('172.24.0.0/23'),
 IPv4Network('172.24.2.0/23'),
 IPv4Network('172.24.4.0/23')]
172.24.1.255
510
```

## Дополнительный Раунд

Измените только required subnets:

| Parent | Original | New requirement |
| --- | ---: | ---: |
| `192.168.80.0/24` | 6 | 9 |
| `172.24.0.0/16` | 100 | 129 |
| `10.0.0.0/8` | 700 | 1025 |

Проверьте переходы:

```text
8 -> 9       requires one more borrowed bit
128 -> 129   requires one more borrowed bit
1024 -> 1025 requires one more borrowed bit
```

Каждый дополнительный borrowed bit:

- удваивает число child subnets;
- вдвое уменьшает total addresses в каждой subnet.

## Критерий Готовности

Вы готовы двигаться дальше, если можете:

- отличить network-based requirement от host-based;
- найти borrowed bits через powers of two;
- получить child prefix из любого parent prefix;
- определить interesting octet;
- выполнить increment и rollover;
- найти network и broadcast;
- вычислить оставшуюся host capacity;
- заметить конфликт требований;
- объяснить alignment;
- повторить задачу без answer key.

## Контрольные Вопросы

### Вопрос 1

Сколько bits нужно занять для минимум 100 subnets?

Ответ:

```text
7, потому что 2^6 = 64, а 2^7 = 128.
```

### Вопрос 2

Какой prefix получится из `/16` после borrowing 7 bits?

Ответ:

```text
/23
```

### Вопрос 3

Сколько usable hosts останется в `/23`?

Ответ:

```text
2^9 - 2 = 510.
```

### Вопрос 4

Почему требование 20 subnets по 20 hosts нельзя выполнить из `/24`?

Ответ:

```text
Для 20 subnets нужен /29, но он даёт только 6 usable hosts.
Для 20 hosts нужен /27, но /24 содержит только восемь /27.
```

### Вопрос 5

Что важнее скорости на первом этапе?

Ответ:

```text
Повторяемый процесс и точная проверка каждого ограничения.
```

## Что Повторить Позже

- Powers of two
- Borrowed bits
- Prefix-to-mask conversion
- Interesting octet
- Increment and rollover
- Alignment
- Host-capacity validation
- FLSM and VLSM
- Timed subnetting drills

