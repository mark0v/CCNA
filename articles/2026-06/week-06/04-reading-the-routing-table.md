# Reading the Routing Table

Source: закрытая страница курса  
Date added: 2026-06-09  
Related plan item: Week 6 / Reading and interpreting routing tables  
Tags: routing table, administrative distance, metric, longest prefix match, next hop, EIGRP, static route
Language: Russian
Translation pair: articles-en/2026-06/week-06/04-reading-the-routing-table.md

## Summary

Routing table - основной источник информации о том, куда router отправит packet. Каждая route entry показывает destination network, источник маршрута, administrative distance, metric, next hop, возраст и exit interface.

Главная мысль: router сначала выбирает самый specific prefix. Если одинаковый prefix изучен из разных источников, сравнивается administrative distance. Если остаются несколько routes одного protocol, сравнивается metric.

## Key Points

- `show ip route` показывает установленные маршруты.
- Route code объясняет, откуда router узнал маршрут.
- `C` означает connected, `L` - local, `S` - static, `D` - EIGRP.
- Destination prefix показывает сеть назначения и ее размер.
- В `[AD/metric]` первое число - administrative distance, второе - metric.
- Меньшее значение administrative distance предпочтительнее.
- Metric сравнивает пути, изученные одним routing protocol.
- Longest prefix match выполняется раньше сравнения AD и metric.
- Next hop указывает следующего router.
- Exit interface показывает, через какой interface уйдет packet.
- Routing table устанавливает лучший route, но protocol database может помнить альтернативы.

## Notes

### The Router's Decision Map

Routing table можно представить как карту решений router.

Для каждого packet router:

1. Читает destination IP.
2. Ищет matching prefixes.
3. Выбирает самый длинный matching prefix.
4. Использует лучший установленный route.
5. Определяет next hop и exit interface.
6. Пересылает packet или отбрасывает его, если route отсутствует.

Основная команда:

```cisco
show ip route
```

### Where Routes Come From

Router может узнать route несколькими способами.

| Code | Source |
| --- | --- |
| `C` | Directly connected network |
| `L` | Exact local interface address |
| `S` | Manually configured static route |
| `D` | Route learned through EIGRP |
| `O` | Route learned through OSPF |
| `R` | Route learned through RIP |
| `B` | Route learned through BGP |

Code в начале entry сразу подсказывает, почему маршрут присутствует.

### Connected And Local Routes

Если interface настроен и `up/up`, router обычно добавляет:

```text
C 192.168.1.0/24 is directly connected, GigabitEthernet0/0
L 192.168.1.1/32 is directly connected, GigabitEthernet0/0
```

`C` описывает всю directly connected subnet.

`L` описывает точный IP address самого router как host route `/32`.

### Reading A Dynamic Route Entry

Пример EIGRP route:

```text
D 192.168.3.0/24 [90/3072] via 192.168.2.2, 00:04:18, GigabitEthernet0/1
```

Разбор:

| Part | Meaning |
| --- | --- |
| `D` | Route learned through EIGRP |
| `192.168.3.0/24` | Destination prefix |
| `90` | Administrative distance |
| `3072` | EIGRP metric |
| `192.168.2.2` | Next-hop router |
| `00:04:18` | Route age |
| `GigabitEthernet0/1` | Exit interface |

Эту строку можно прочитать так:

```text
Сеть 192.168.3.0/24 изучена через EIGRP.
Для нее используется next hop 192.168.2.2,
packet выйдет через GigabitEthernet0/1.
```

### Variably Subnetted

В output может появиться:

```text
192.168.1.0/24 is variably subnetted, 2 subnets, 2 masks
```

Это информационная строка. Она означает, что router показывает prefixes разной длины внутри общего address block.

Часто рядом находятся:

- connected subnet `/24`;
- local host route `/32`.

Это не ошибка.

### Administrative Distance

Administrative distance оценивает доверие к источнику route.

Меньше - предпочтительнее.

Типичные значения:

| Route source | Default AD |
| --- | ---: |
| Connected | 0 |
| Static | 1 |
| EIGRP summary | 5 |
| External BGP | 20 |
| Internal EIGRP | 90 |
| OSPF | 110 |
| RIP | 120 |
| External EIGRP | 170 |
| Internal BGP | 200 |

Если одинаковый destination prefix получен через static route и EIGRP:

```text
Static AD: 1
EIGRP AD: 90
```

В routing table обычно устанавливается static route.

EIGRP не обязательно перестал работать. Его route просто проиграл более предпочтительному источнику.

### Metric

Metric оценивает качество paths внутри одного routing protocol.

Например, если EIGRP знает два пути к одному prefix, он сравнивает EIGRP metrics.

Меньшая metric обычно предпочтительнее.

Важно:

```text
AD compares route sources.
Metric compares paths within a route source/protocol.
```

Нельзя напрямую считать EIGRP metric лучше OSPF metric только потому, что число меньше. Эти protocols рассчитывают metrics по-разному. Сначала между protocols применяется AD.

### Longest Prefix Match Comes First

Самое важное правило forwarding:

```text
The most specific matching prefix wins.
```

Пример routing table:

```text
192.168.3.0/24 via 192.168.2.2
192.168.0.0/16 via 10.0.0.2
0.0.0.0/0 via 216.0.5.1
```

Для destination `192.168.3.10` совпадают все три routes:

- `/24`;
- `/16`;
- `/0`.

Побеждает `/24`, потому что он содержит больше matching network bits.

Даже default route с низким AD не заменяет более specific prefix.

### Route Selection Order

Упрощенный порядок:

1. Найти самый specific destination prefix.
2. Для одинакового prefix сравнить administrative distance разных route sources.
3. Для routes одного protocol сравнить metric.
4. Установить winner в routing table.
5. При поддержке equal-cost paths router может установить несколько routes.

AD не используется для сравнения `/24` с `/0`; сначала всегда longest prefix match.

### Static Route Replacing EIGRP

Предположим, EIGRP уже изучил:

```text
D 192.168.3.0/24 [90/3072] via 192.168.2.2
```

Administrator добавляет:

```cisco
ip route 192.168.3.0 255.255.255.0 192.168.2.2
```

Теперь для одинакового `/24` есть два sources:

- static AD `1`;
- EIGRP AD `90`.

В `show ip route` будет установлен static route:

```text
S 192.168.3.0/24 [1/0] via 192.168.2.2
```

После удаления static route EIGRP route может снова стать winner:

```cisco
no ip route 192.168.3.0 255.255.255.0 192.168.2.2
```

### Next Hop And Exit Interface

Next hop - IP соседнего router, которому передается packet.

Exit interface - local interface, через который packet покидает router.

Можно читать entry в обратном направлении:

```text
Выйти через этот interface,
передать этому next hop,
чтобы достичь этой destination network.
```

Router должен уметь разрешить next hop через connected или другой подходящий route. Этот процесс называют recursive lookup.

### Route Age

Dynamic route часто показывает timer:

```text
00:04:18
```

Он указывает, сколько времени прошло с последнего обновления route.

Для troubleshooting это помогает понять:

- route недавно появился;
- adjacency могла flapping;
- update давно стабилен;
- route постоянно переустанавливается.

### Troubleshooting Questions

Не ограничивайся вопросом:

```text
Is the route present?
```

Спрашивай:

```text
Какой prefix установлен?
Откуда он изучен?
Почему этот source победил?
Какой AD?
Какая metric?
Какой next hop?
Какой exit interface?
Достижим ли next hop?
Есть ли более specific route?
Существует ли return path?
```

### Useful Verification Commands

```cisco
show ip route
show ip route 192.168.3.0
show ip route static
show ip route eigrp
show ip protocols
show ip eigrp topology
show ip interface brief
traceroute 192.168.3.10
```

`show ip route <network>` помогает сфокусироваться на конкретном destination.

Protocol-specific database может содержать routes, которые не были установлены как текущий winner.

## Worked Examples

### Example 1: Specific Route Versus Default

```text
S 192.168.3.0/24 via 192.168.2.2
S* 0.0.0.0/0 via 216.0.5.1
```

Destination `192.168.3.20` использует `/24`.

Destination `8.8.8.8` использует `/0`.

### Example 2: Static Versus EIGRP

Оба routes относятся к `192.168.3.0/24`.

```text
Static AD 1
EIGRP AD 90
```

Static route устанавливается как winner.

### Example 3: Two EIGRP Paths

Если EIGRP изучает одинаковый prefix через двух neighbors, protocol сравнивает composite metric.

Путь с меньшей metric становится successor. Equal-cost paths могут быть установлены одновременно в зависимости от configuration.

## Practical Checklist

- Найти route code.
- Прочитать destination prefix.
- Определить prefix length.
- Разделить `[AD/metric]`.
- Найти next hop.
- Найти exit interface.
- Проверить route age.
- Проверить более specific prefixes.
- Объяснить, почему route победил.
- Проверить обратный путь.

## Quick Self-Check

### Question 1

Что означает `[90/3072]` в EIGRP route?

Answer:

```text
90 - administrative distance, 3072 - EIGRP metric.
```

### Question 2

Что сравнивает administrative distance?

Answer:

```text
Доверие к разным источникам route для одинакового prefix.
```

### Question 3

Что сравнивает metric?

Answer:

```text
Качество путей, изученных одним routing protocol.
```

### Question 4

Что выбирается раньше: lower AD или longest prefix?

Answer:

```text
Сначала longest prefix match.
```

### Question 5

Почему static route может скрыть EIGRP route?

Answer:

```text
Для одинакового prefix static route имеет более низкий default AD.
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Routing table | Таблица лучших routes, используемых для forwarding. |
| Route code | Источник, из которого route был изучен. |
| Administrative distance | Предпочтительность route source; lower is better. |
| Metric | Оценка пути внутри routing protocol. |
| Longest prefix match | Выбор самого specific matching prefix. |
| Next hop | Следующий router на пути. |
| Exit interface | Local interface для отправки packet. |
| Route age | Время с последнего protocol update. |
| `show ip route` | Показывает routing table. |
| Recursive lookup | Поиск способа достичь next-hop address. |

## What To Review Later

- Administrative distance values
- EIGRP metrics
- OSPF cost
- Equal-cost multipath
- Floating static routes
- Recursive route lookup
- Route redistribution
