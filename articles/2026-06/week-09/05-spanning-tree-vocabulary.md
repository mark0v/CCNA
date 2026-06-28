# Spanning Tree Vocabulary

Source: закрытая страница курса  
Date added: 2026-06-28  
Related plan item: Week 9 / Spanning Tree vocabulary and decision terms  
Tags: STP, root bridge, bridge ID, BPDU, port cost, root port, designated port, blocked port
Language: Russian
Translation pair: articles-en/2026-06/week-09/05-spanning-tree-vocabulary.md

## Кратко

Spanning Tree Protocol решает простую задачу: сохранить redundancy и не допустить broadcast storm.

Сложность начинается не в самой идее, а в том, как switches самостоятельно договариваются, какой link должен forward traffic, а какой должен block.

Для этого STP использует набор терминов:

- root bridge;
- bridge ID;
- priority;
- MAC address;
- BPDU;
- port cost;
- root port;
- designated port;
- blocked port.

Если эти слова понятны, дальше STP перестает выглядеть как магия. Это становится последовательным алгоритмом.

## Почему Switches Нужны Правила

Человек может посмотреть на diagram и быстро сказать:

```text
Вот loop.
Этот link можно заблокировать.
```

Switch так не думает. У него нет визуального diagram и человеческого context.

Switches нужны формальные правила:

- кто главный reference point;
- какой path считается лучшим;
- какой port должен forward;
- какой port должен block;
- что делать при failure.

Первый большой вопрос STP:

```text
Who is the root bridge?
```

От ответа зависит вся остальная topology.

## Root Bridge

Root bridge - это switch, который STP выбирает как центр Layer 2 topology.

Все остальные switches считают path до root bridge и строят forwarding decisions вокруг него.

Важно понимать: root bridge - это не router и не default gateway.

Это reference point для STP.

Если root bridge выбран плохо, forwarding topology тоже может быть плохой.

Например, если старый access switch случайно стал root bridge, traffic может идти через неудачные links, а не через core или distribution switch, где ты ожидал центральную роль.

Правильный design обычно такой:

```text
Core or distribution switch should be root bridge.
Random access switch should not be root bridge.
```

## Bridge ID

Root bridge выбирается через Bridge ID.

Bridge ID состоит из двух частей:

```text
Bridge ID = priority + MAC address
```

Побеждает lowest Bridge ID.

То есть STP ищет не самый новый switch, не самый быстрый switch и не самый "главный" по названию.

Он выбирает switch с самым низким Bridge ID.

## Priority

Priority - первая часть Bridge ID.

Default priority обычно:

```text
32768
```

Если все switches имеют одинаковую priority, election переходит к tiebreaker - MAC address.

Чтобы управлять root bridge election, engineer меняет priority.

Правило простое:

```text
Lower priority wins.
```

Если нужно, чтобы core switch стал root bridge, ему задают priority ниже, чем у остальных switches.

Это один из самых важных STP design controls.

## Почему Default Root Может Быть Странным

Если все switches оставлены с default priority `32768`, побеждает switch с lowest MAC address.

Часто lower MAC address означает более старое устройство.

Это может казаться странным: почему старый switch получает шанс стать root?

Причина - stability.

Если бы новый switch автоматически выигрывал election, то подключение любого нового switch могло бы внезапно перестроить STP topology.

Но это не значит, что нужно оставлять production network на удачу.

Правильная практика:

```text
Do not let MAC address choose your root bridge.
Set the priority intentionally.
```

## BPDU

BPDU означает Bridge Protocol Data Unit.

Это служебное STP message, которым switches обмениваются между собой.

Через BPDU switches сообщают:

- свой Bridge ID;
- root bridge, который они считают лучшим;
- path cost до root bridge;
- STP timing information;
- topology changes.

BPDU можно воспринимать как heartbeat и control message STP.

Если switch перестает получать ожидаемые BPDUs через link, STP понимает, что topology изменилась, и может пересчитать forwarding paths.

## Port Cost

После выбора root bridge каждый non-root switch должен понять:

```text
What is my best path to the root bridge?
```

Для этого STP использует port cost.

Port cost - это число, связанное со speed link.

Общее правило:

```text
Faster link = lower cost.
Slower link = higher cost.
Lower total cost wins.
```

Для CCNA полезно запомнить два классических значения:

| Link speed | STP cost |
| --- | --- |
| 100 Mbps | 19 |
| 1 Gbps | 4 |

Если switch имеет несколько paths к root bridge, он выбирает path с lowest total cost.

## Root Port

Root port - это port, через который non-root switch идет к root bridge.

У каждого non-root switch есть ровно один root port.

Root bridge сам root port не имеет, потому что он уже root.

Простая формула:

```text
Root port = best port toward the root bridge.
```

Если на access switch есть два uplinks к distribution layer, STP сравнит path cost и выберет один из них как root port.

## Designated Port

Designated port - это port, который forwards traffic для segment.

На каждом Layer 2 segment должен быть designated port, чтобы traffic мог проходить без loop.

На root bridge все active ports обычно являются designated ports, потому что root bridge является лучшим reference point для topology.

Простая формула:

```text
Designated port = forwarding port for that segment.
```

## Blocked Port

Blocked port - это port, который STP не использует для forwarding user traffic, потому что forwarding через него создал бы loop.

Blocked port часто путают с broken port.

Это разные вещи.

```text
Blocked by STP does not mean failed.
Blocked means protecting the network.
```

Обычно на redundant connection один side может быть forwarding, а другой side blocked.

Оба switches при этом "правы". Один port нужен для active path, второй удерживается в standby, чтобы не создать loop.

## Порядок Мышления STP

На базовом уровне STP можно читать в таком порядке:

```text
1. Elect the root bridge.
2. Choose root ports on non-root switches.
3. Choose designated ports on each segment.
4. Block remaining loop-causing ports.
```

Это не все детали STP, но это сильная основа.

Когда ты читаешь `show spanning-tree`, ищи именно эти ответы:

- кто root bridge;
- какой Bridge ID у local switch;
- какой port является root port;
- какие ports designated;
- какие ports blocked;
- какой cost у path.

## Почему Термины Важны В Реальной Сети

Если не понимать vocabulary, STP output выглядит как странный набор строк.

Если понимать vocabulary, `show spanning-tree` превращается в карту decisions.

Ты можешь увидеть:

- почему этот switch не root;
- почему traffic идет через этот uplink;
- почему быстрый link оказался blocked;
- почему старый switch стал центром topology;
- что изменится после настройки priority;
- какой link откроется при failure.

Это особенно важно в real networks, где STP может выбрать loop-free topology, но не обязательно optimal topology.

Loop-free не всегда значит хорошо спроектировано.

## Главный Вывод

STP vocabulary - это не набор слов для exam.

Это язык, на котором switches объясняют свои decisions.

Запомни основу:

```text
Lowest Bridge ID wins root bridge election.
Lowest path cost wins the best path.
Root ports point toward the root.
Designated ports forward for a segment.
Blocked ports prevent loops.
```

Если эти правила понятны, следующий шаг - взять real topology и вручную определить, какие ports будут forwarding, а какие будут blocked.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Root bridge | Switch elected as the STP reference point for the topology. |
| Bridge ID | STP identifier made from bridge priority and MAC address. |
| Priority | Configurable value used first in root bridge election. Lower wins. |
| BPDU | Bridge Protocol Data Unit, the STP control message exchanged by switches. |
| Port cost | STP value based mainly on link speed. Lower cost is preferred. |
| Root port | Best port on a non-root switch toward the root bridge. |
| Designated port | Forwarding port selected for a Layer 2 segment. |
| Blocked port | Port that does not forward user traffic because it would create a loop. |

## Questions

### 1. What decides the root bridge?

Answer:

The lowest Bridge ID wins. Bridge ID is made from priority and MAC address.

### 2. Why should production networks not leave root bridge election to chance?

Answer:

Because default priority can let the lowest MAC address win, which may place the root bridge on an old or poorly located switch.

### 3. What is the difference between a root port and a blocked port?

Answer:

A root port is the best forwarding path from a non-root switch to the root bridge. A blocked port is held out of forwarding to prevent a Layer 2 loop.

## What To Review Later

- STP election order.
- Root bridge priority tuning.
- Path cost calculation.
- Reading `show spanning-tree`.
- Per-VLAN STP behavior.
- Root bridge primary and secondary design.
