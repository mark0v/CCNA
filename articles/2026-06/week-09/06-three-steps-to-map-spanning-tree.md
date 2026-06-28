# Three Steps To Map Spanning Tree

Source: закрытая страница курса  
Date added: 2026-06-28  
Related plan item: Week 9 / Three-step STP topology mapping  
Tags: STP, root port, designated port, blocked port, root bridge, port cost, bridge ID, topology
Language: Russian
Translation pair: articles-en/2026-06/week-09/06-three-steps-to-map-spanning-tree.md

## Кратко

Многие знают, что Spanning Tree Protocol блокирует redundant ports.

Меньше людей понимают, почему STP блокирует именно эти ports.

Это важная разница. В реальной сети ты смотришь не на определение, а на topology, `show spanning-tree` output и странный вопрос: почему этот link не forwarding?

Чтобы вручную разобрать STP topology, используй один и тот же порядок:

```text
1. Identify root ports.
2. Identify designated ports.
3. Block everything else.
```

Плюс три tiebreakers:

```text
1. Lowest cost to root bridge.
2. Lowest bridge ID.
3. Lowest port number.
```

Если идти системно, STP перестает быть угадыванием.

## Топология, О Которой Думаем

Представь Cisco three-tier hierarchy:

- access layer внизу, где подключаются end devices;
- distribution layer в середине, где networks consolidate;
- core layer наверху, backbone для всей сети.

Такая design часто имеет много redundant paths.

Это хорошо для uptime.

Но для Layer 2 это также потенциальные loops.

STP должен оставить full connectivity, но убрать loops. Для этого он выбирает active forwarding tree и блокирует лишние paths.

## Перед Тремя Шагами: Root Bridge

Перед тем как выбирать ports, STP сначала выбирает root bridge.

Root bridge - это reference point для всей STP topology.

Root bridge выбирается по lowest Bridge ID:

```text
Bridge ID = priority + MAC address
```

Lowest wins.

В этой статье мы не настраиваем priority. Просто считаем, что root bridge уже выбран.

После этого каждый switch задает главный вопрос:

```text
How do I reach the root bridge?
```

## Шаг 1: Найти Root Ports

Root port - это лучший port на non-root switch в сторону root bridge.

У каждого non-root switch должен быть ровно один root port.

Root port всегда forwarding.

Как switch выбирает root port?

Он сравнивает paths к root bridge по трем tiebreakers.

### Tiebreaker 1: Lowest Cost To Root

Cost связан со speed link.

Для CCNA нужно держать в голове:

| Link speed | STP cost |
| --- | --- |
| 100 Mbps | 19 |
| 1 Gbps | 4 |

Switch складывает costs вдоль path к root bridge.

Lowest total cost wins.

Пример:

```text
Path A: 4 + 4 = 8
Path B: 19 + 4 = 23
Path A wins
```

### Tiebreaker 2: Lowest Bridge ID

Если cost одинаковый, switch смотрит на neighbor Bridge ID.

Path через neighbor с lowest Bridge ID wins.

Это помогает выбрать deterministic path, даже если speeds одинаковые.

### Tiebreaker 3: Lowest Port Number

Если cost одинаковый и Bridge ID одинаковый, STP смотрит на port number.

Lowest port number wins.

Это последний tiebreaker, когда остальные параметры не различают paths.

## Шаг 2: Найти Designated Ports

После root ports STP смотрит на каждый Layer 2 segment.

Каждый segment должен иметь один designated port.

Designated port - это port, который forwards traffic для этого segment.

Первое правило:

```text
All active ports on the root bridge are designated ports.
```

Это "награда" за то, что switch стал root bridge. Root bridge является лучшим reference point, поэтому его ports на connected segments forwarding.

Для остальных segments switches на двух концах link соревнуются.

Они используют те же критерии:

```text
1. Lowest cost to root bridge.
2. Lowest bridge ID.
3. Lowest port number.
```

Кто выигрывает, получает designated port.

Designated port forwarding.

## Шаг 3: Заблокировать Остальные Ports

Теперь простое правило:

```text
If a port is not a root port
and not a designated port,
it becomes blocked.
```

Blocked port не forwarding user traffic.

Но он не "мертвый". Он все еще физически up и может получать BPDUs.

Его задача - не дать Layer 2 loop стать broadcast storm.

В fully redundant design может оказаться, что STP блокирует много links.

Это не bug.

Это STP выполняет свою работу.

## Как Это Видеть На Diagram

Полезный прием: после выбора blocked ports мысленно сотри blocked links с diagram.

Оставшаяся active topology должна выглядеть как tree:

- все switches connected;
- path к root bridge есть;
- loops нет;
- redundant links находятся в standby.

Если active link fails, STP может пересчитать topology и открыть часть blocked ports.

Именно так сеть получает redundancy без loop.

## Мини-Workflow Для Бумаги

Когда видишь STP diagram, не пытайся угадывать.

Иди по checklist:

### 1. Отметь Root Bridge

Найди switch с lowest Bridge ID.

Если priority настроена вручную, обычно root будет core или distribution switch.

### 2. Отметь Root Ports

На каждом non-root switch найди best path to root:

- lowest total cost;
- then lowest neighbor Bridge ID;
- then lowest neighbor port number.

### 3. Отметь Designated Ports

На каждом segment выбери forwarding side:

- root bridge ports win automatically;
- otherwise compare lowest cost to root;
- then Bridge ID;
- then port number.

### 4. Заблокируй Остальное

Все ports, которые не root и не designated, становятся blocked.

## Почему Это Важно В Реальной Сети

В production ты не всегда рисуешь STP на бумаге.

Но этот mental model нужен, когда:

- быстрый uplink оказался blocked;
- traffic идет через unexpected switch;
- access switch стал root;
- после failure открылся не тот path;
- topology converged, но performance плохой;
- `show spanning-tree` показывает роли, которые не совпадают с diagram.

Если ты понимаешь три шага, ты можешь объяснить STP decision.

Если не понимаешь, blocked links выглядят случайными.

## Главный Вывод

STP можно разбирать вручную.

Порядок всегда один:

```text
1. Root ports.
2. Designated ports.
3. Blocked leftovers.
```

Tiebreakers тоже идут в порядке:

```text
1. Lowest cost to root.
2. Lowest bridge ID.
3. Lowest port number.
```

Практикуйся на messy switch diagrams. Рисуй redundant links, выбирай root bridge и проходи эти steps.

Это даст больше, чем простое запоминание фразы "STP blocks redundant links".

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Root port | Best port on a non-root switch toward the root bridge. |
| Designated port | Forwarding port selected for a Layer 2 segment. |
| Blocked port | Port that does not forward user traffic because it would create a loop. |
| Path cost | Total STP cost from a switch toward the root bridge. |
| Bridge ID | Identifier made from priority and MAC address. Lowest wins elections. |
| Tiebreaker | Rule used when the earlier STP comparison produces a tie. |
| Segment | Layer 2 link or shared medium where STP chooses a designated port. |

## Questions

### 1. What are the three manual STP mapping steps?

Answer:

Identify root ports, identify designated ports, then block every remaining port that is neither root nor designated.

### 2. What are the three main STP tiebreakers?

Answer:

Lowest cost to the root bridge, lowest bridge ID, and lowest port number.

### 3. Why are blocked ports not a failure?

Answer:

They are standby ports that prevent Layer 2 loops. They can become useful if the active path fails and STP recalculates the topology.

## What To Review Later

- Root bridge priority configuration.
- Reading `show spanning-tree`.
- Root port selection examples.
- Designated port selection examples.
- STP convergence after link failure.
- EtherChannel and why it changes the redundant-link problem.
