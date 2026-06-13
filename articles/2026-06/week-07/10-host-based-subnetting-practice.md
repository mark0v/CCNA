# Практика Subnetting по Количеству Hosts

Source: закрытая страница курса  
Date added: 2026-06-13  
Related plan item: Week 7 / Host-based subnetting practice  
Tags: subnetting, practice, hosts, FLSM, subnet mask, network range, self-check
Language: Russian
Translation pair: articles-en/2026-06/week-07/10-host-based-subnetting-practice.md

## Кратко

Subnetting становится навыком только после самостоятельной практики. Наблюдение за готовым решением создаёт узнавание, но не гарантирует, что вы сможете выполнить расчёт с чистого листа.

Правильный порядок работы:

1. Решить задачу самостоятельно.
2. Записать каждый промежуточный шаг.
3. Проверить ответ.
4. Найти точное место ошибки.
5. Повторить расчёт без подсказки.

Эта статья содержит четыре задачи по host-based subnetting. Сначала выполните раздел **Задания**, не переходя к **Answer Key**.

## Что Нужно Найти

Для каждой задачи определите:

1. Minimum host bits.
2. Child prefix.
3. Dotted-decimal mask.
4. Interesting octet.
5. Increment.
6. Total addresses per subnet.
7. Usable hosts per subnet.
8. Number of child subnets в parent block.
9. Первые три network addresses.
10. Network, first host, last host и broadcast первой child subnet.
11. Выполнимо ли требование внутри указанного parent block.

## Рабочий Алгоритм

```text
1. Find h: 2^h - 2 >= required hosts
2. Child prefix = 32 - h
3. Confirm child prefix >= parent prefix
4. Convert prefix to subnet mask
5. Find interesting octet
6. Increment = 256 - mask value in interesting octet
7. List child networks
8. Broadcast = next network - 1
9. First host = network + 1
10. Last host = broadcast - 1
11. Child subnets = 2^(child prefix - parent prefix)
```

Для обычных LAN calculations формула usable hosts:

```text
2^h - 2
```

## Правила Практики

- Не открывайте answer key до завершения попытки.
- Не угадывайте mask по памяти, если не можете объяснить её через bits.
- Записывайте parent prefix.
- Проверяйте, помещается ли child subnet в parent.
- Не считайте `.0` и `.255` автоматически reserved без анализа prefix.
- После расчёта выполните обратную проверку capacity.
- Используйте calculator только после ручной попытки.

## Шаблон Ответа

Скопируйте этот шаблон для каждой задачи:

```text
Parent:
Required usable hosts:

Host bits:
Capacity check:
Child prefix:
Mask:
Interesting octet:
Increment:
Total addresses:
Usable hosts:
Child subnet count:

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

## Задание 1: Cafe Floor

NetworkChuck Coffee выделил:

```text
Parent network: 192.168.50.0/24
Required hosts: 45 per subnet
```

Найдите все значения из рабочего шаблона.

Дополнительный вопрос:

```text
Хватит ли выбранной subnet, если позднее потребуется 65 usable addresses?
```

---

## Задание 2: Office Building

Дано:

```text
Parent network: 172.22.0.0/16
Required hosts: 300 per subnet
```

Найдите все значения из рабочего шаблона.

Дополнительный вопрос:

```text
Является ли 172.22.1.0 usable address в первой child subnet?
```

---

## Задание 3: Distribution Center

Дано:

```text
Parent network: 10.0.0.0/8
Required hosts: 1500 per subnet
```

Найдите все значения из рабочего шаблона.

Дополнительный вопрос:

```text
Какой network address следует после 10.0.248.0?
```

---

## Задание 4: Невозможное Требование

Дано:

```text
Parent network: 198.51.100.0/24
Required hosts: 300 per subnet
```

Найдите необходимый child prefix и определите, можно ли создать такую subnet внутри parent block.

Дополнительный вопрос:

```text
Какой минимальный aligned parent block мог бы содержать одну такую subnet,
если allocation начинается с 198.51.100.0?
```

---

## Остановитесь Перед Проверкой

Перед переходом к ответам убедитесь, что для всех четырёх задач записаны:

- проверка двух соседних powers of two;
- prefix и mask;
- increment;
- хотя бы первые три networks;
- полный первый range;
- вывод о выполнимости.

Familiarity не равна mastery. Цель упражнения заключается не в узнавании правильного ответа, а в самостоятельном воспроизведении процесса.

---

## Answer Key

## Решение 1: Cafe Floor

Дано:

```text
Parent:         192.168.50.0/24
Required hosts: 45
```

### Host Bits

```text
2^5 - 2 = 30   insufficient
2^6 - 2 = 62   sufficient
```

```text
Host bits = 6
```

### Prefix и Mask

```text
Child prefix = 32 - 6 = /26
Mask         = 255.255.255.192
```

### Increment

Interesting octet является четвёртым:

```text
256 - 192 = 64
```

### Capacity

```text
Total addresses: 2^6 = 64
Usable hosts:    64 - 2 = 62
Child subnets:   2^(26 - 24) = 4
```

### Networks

```text
192.168.50.0/26
192.168.50.64/26
192.168.50.128/26
192.168.50.192/26
```

### Первый Range

```text
Network:    192.168.50.0
First host: 192.168.50.1
Last host:  192.168.50.62
Broadcast:  192.168.50.63
```

### Дополнительный Вопрос

Для 65 usable addresses `/26` недостаточно:

```text
/26 = 62 usable
/25 = 126 usable
```

Потребуется `/25`.

### Итог

```text
Requirement feasible: yes
Reason: /24 contains four /26 subnets, each with 62 usable hosts.
```

## Решение 2: Office Building

Дано:

```text
Parent:         172.22.0.0/16
Required hosts: 300
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
Child prefix = 32 - 9 = /23
Mask         = 255.255.254.0
```

### Increment

Interesting octet является третьим:

```text
256 - 254 = 2
```

### Capacity

```text
Total addresses: 2^9 = 512
Usable hosts:    510
Child subnets:   2^(23 - 16) = 128
```

### Первые Networks

```text
172.22.0.0/23
172.22.2.0/23
172.22.4.0/23
```

### Первый Range

```text
Network:    172.22.0.0
First host: 172.22.0.1
Last host:  172.22.1.254
Broadcast:  172.22.1.255
```

### Дополнительный Вопрос

```text
172.22.1.0
```

находится между first и last host, поэтому является usable address.

Окончание `.0` не делает address network автоматически. Для этой `/23` network address равен `172.22.0.0`.

### Итог

```text
Requirement feasible: yes
Reason: /16 contains 128 /23 subnets with 510 usable hosts each.
```

## Решение 3: Distribution Center

Дано:

```text
Parent:         10.0.0.0/8
Required hosts: 1500
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
Child prefix = 32 - 11 = /21
Mask         = 255.255.248.0
```

### Increment

Interesting octet является третьим:

```text
256 - 248 = 8
```

### Capacity

```text
Total addresses: 2^11 = 2048
Usable hosts:    2046
Child subnets:   2^(21 - 8) = 8192
```

### Первые Networks

```text
10.0.0.0/21
10.0.8.0/21
10.0.16.0/21
```

### Первый Range

```text
Network:    10.0.0.0
First host: 10.0.0.1
Last host:  10.0.7.254
Broadcast:  10.0.7.255
```

### Дополнительный Вопрос

После:

```text
10.0.248.0/21
```

прибавление `8` даёт `256` в третьем octet:

```text
10.0.256.0 -> 10.1.0.0
```

Следующая network:

```text
10.1.0.0/21
```

### Итог

```text
Requirement feasible: yes
Reason: /8 contains 8192 /21 subnets with 2046 usable hosts each.
```

Практический design должен отдельно обосновать broadcast domain такого размера.

## Решение 4: Невозможное Требование

Дано:

```text
Parent:         198.51.100.0/24
Required hosts: 300
```

### Host Bits

```text
2^8 - 2 = 254   insufficient
2^9 - 2 = 510   sufficient
```

```text
Host bits = 9
```

### Требуемый Prefix

```text
Child prefix = 32 - 9 = /23
Mask         = 255.255.254.0
```

Но:

```text
Required child: /23
Available parent: /24
```

`/23` является более крупным block, чем `/24`, поэтому он не помещается внутри parent.

### Alignment

Network boundaries `/23` в третьем octet идут с increment `2`.

Address `198.51.100.0` находится на корректной `/23` boundary, потому что `100` является чётным.

Минимальный parent block:

```text
198.51.100.0/23
```

Range:

```text
Network:    198.51.100.0
First host: 198.51.100.1
Last host:  198.51.101.254
Broadcast:  198.51.101.255
```

### Итог

```text
Requirement feasible in stated parent: no
Required allocation: 198.51.100.0/23 or another aligned /23
```

## Сводная Таблица

| Task | Parent | Hosts | Child prefix | Usable | Child subnets | Feasible |
| ---: | --- | ---: | ---: | ---: | ---: | --- |
| 1 | `192.168.50.0/24` | 45 | `/26` | 62 | 4 | Yes |
| 2 | `172.22.0.0/16` | 300 | `/23` | 510 | 128 | Yes |
| 3 | `10.0.0.0/8` | 1500 | `/21` | 2046 | 8192 | Yes |
| 4 | `198.51.100.0/24` | 300 | `/23` | 510 | Does not fit | No |

## Как Разбирать Ошибку

Не ограничивайтесь отметкой «неверно». Классифицируйте ошибку.

| Тип ошибки | Пример | Что повторить |
| --- | --- | --- |
| Requirement | Решалась задача по subnets вместо hosts | Определение типа задачи |
| Capacity | Использовано `2^h`, забыто `- 2` | Network и broadcast |
| Prefix | Вычислено `h`, но неверно найден `32 - h` | CIDR structure |
| Mask | Prefix неверно переведён в decimal | Binary mask values |
| Increment | Использован не тот octet | Interesting octet |
| Range | Broadcast приравнен следующей network | `next network - 1` |
| Rollover | Получен octet `256` | Octet carry |
| Parent | Child subnet крупнее allocation | Parent/child validation |
| Usability | Любой `.0` объявлен network | Prefix-aware boundaries |

## Журнал Повторной Попытки

Для каждой ошибки запишите:

```text
Task:
My incorrect result:
Correct result:
First incorrect step:
Why it was incorrect:
Rule to apply next time:
Second attempt result:
```

Такой журнал превращает случайную ошибку в конкретное правило.

## Проверка Инструментом

После ручного решения можно проверить ranges с Python:

```python
from ipaddress import ip_network

parent = ip_network("192.168.50.0/24")
children = list(parent.subnets(new_prefix=26))

for subnet in children:
    print(
        subnet,
        subnet.network_address,
        subnet.broadcast_address,
        subnet.num_addresses - 2,
    )
```

Инструмент должен подтверждать решение, а не заменять первую попытку.

## Дополнительный Раунд

После успешного решения измените только requirement:

| Parent | Original hosts | New hosts |
| --- | ---: | ---: |
| `192.168.50.0/24` | 45 | 63 |
| `172.22.0.0/16` | 300 | 511 |
| `10.0.0.0/8` | 1500 | 2047 |
| `198.51.100.0/24` | 300 | 120 |

Обратите внимание, как переход через capacity boundary изменяет prefix:

```text
62 -> 63     changes /26 to /25
510 -> 511   changes /23 to /22
2046 -> 2047 changes /21 to /20
```

## Критерий Готовности

Материал можно считать усвоенным, если вы без answer key можете:

- правильно определить тип requirement;
- выбрать host bits через две соседние powers of two;
- получить prefix и mask;
- найти interesting octet и increment;
- перечислить network ranges;
- определить first host, last host и broadcast;
- заметить невозможное требование;
- объяснить каждый шаг словами;
- повторить расчёт с новым числом hosts.

Скорость появляется после стабильной точности. Сначала формируется повторяемый процесс.

## Контрольные Вопросы

### Вопрос 1

Почему простого просмотра решений недостаточно?

Ответ:

```text
Узнавание шагов не гарантирует способность самостоятельно воспроизвести их.
```

### Вопрос 2

Когда следует открывать answer key?

Ответ:

```text
После завершённой самостоятельной попытки с записанными шагами.
```

### Вопрос 3

Что полезнее отметки «неверно»?

Ответ:

```text
Найти первый ошибочный шаг и связать его с конкретным правилом.
```

### Вопрос 4

Какой prefix нужен для 300 usable hosts?

Ответ:

```text
/23, потому что /24 даёт 254, а /23 даёт 510 usable hosts.
```

### Вопрос 5

Почему `/23` нельзя создать внутри `/24`?

Ответ:

```text
/23 является более крупным address block, чем /24.
```

## Что Повторить Позже

- Host-capacity boundaries
- Prefix-to-mask conversion
- Interesting octet
- Increment and rollover
- Parent/child prefix validation
- FLSM
- VLSM
- Timed subnetting drills

