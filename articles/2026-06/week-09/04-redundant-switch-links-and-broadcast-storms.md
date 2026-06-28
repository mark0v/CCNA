# Redundant Switch Links And Broadcast Storms

Source: закрытая страница курса  
Date added: 2026-06-28  
Related plan item: Week 9 / Redundant switch links and broadcast storms  
Tags: STP, redundancy, broadcast storm, Layer 2, switching loop, TTL, BPDU
Language: Russian
Translation pair: articles-en/2026-06/week-09/04-redundant-switch-links-and-broadcast-storms.md

## Кратко

Redundancy звучит как очевидно хорошая идея: если один cable между switches упадет, второй cable спасет connectivity.

Но в Layer 2 network второй cable может не спасти сеть, а положить ее.

Причина - switching loop.

Когда два switches соединены двумя обычными Layer 2 links, broadcast frame может начать ходить по кругу. Switch получает broadcast, flood-ит его через остальные ports, второй switch делает то же самое, и frame возвращается обратно.

Так появляется broadcast storm.

Главная мысль:

```text
Redundant physical links are useful.
Uncontrolled Layer 2 loops are catastrophic.
STP is the control mechanism between those two facts.
```

## Почему Второй Cable Не Всегда Решение

Представь простую схему:

```text
SW1 ----- SW2
```

Один cable соединяет два switches.

Если этот cable упадет, devices на разных switches потеряют связь. Поэтому логичная мысль - добавить второй cable:

```text
SW1 ===== SW2
```

На физическом уровне это выглядит как better reliability.

Но на Layer 2 это уже loop.

Теперь frame может пройти из SW1 в SW2 по одному link и вернуться обратно по другому. Для unicast traffic это уже плохо, но для broadcast это особенно опасно.

## Как Broadcast Превращается В Storm

Broadcast frame отправляется всем devices в одной VLAN.

Типичный пример - DHCP request:

```text
Who can give me an IP address?
```

Switch получает такой frame и делает нормальную Layer 2 работу:

- принимает frame на одном port;
- отправляет его out all other ports in the VLAN;
- не отправляет обратно только на тот port, откуда frame пришел.

Если topology без loops, это нормально.

Если между switches есть loop, начинается проблема:

1. PC отправляет broadcast на SW1.
2. SW1 flood-ит broadcast на SW2.
3. SW2 flood-ит broadcast обратно на SW1 через другой link.
4. SW1 снова flood-ит его.
5. Процесс повторяется без нормального конца.

Сеть не "немного замедляется".

Она может быстро стать непригодной для работы.

## Почему Layer 3 Ведет Себя Иначе

Хороший вопрос: почему routing loops не ведут себя так же бесконечно?

На Layer 3 у IP packet есть TTL, Time To Live.

Обычно packet стартует с TTL вроде `255`. Каждый router на пути уменьшает TTL на `1`. Когда TTL становится `0`, packet drop-ится.

Это не делает routing loops хорошими, но ограничивает ущерб.

```text
Layer 3 packet:
TTL decreases at every router hop.
Eventually TTL reaches 0.
Packet is dropped.
```

Switching работает иначе.

Switches в классическом Layer 2 forwarding смотрят на MAC addresses, а не на IP TTL. Ethernet frame не имеет такого же hop countdown.

```text
Layer 2 frame:
No TTL.
No automatic hop countdown.
Loop can continue until topology changes or network fails.
```

Поэтому Layer 2 loop особенно опасен.

## Что Видит Пользователь

Broadcast storm может выглядеть как странный и резкий outage.

Симптомы:

- сеть внезапно становится медленной;
- DHCP перестает выдавать addresses;
- pings теряются;
- phones, cameras, POS terminals или workstations отваливаются;
- switch CPU растет;
- MAC address table начинает flapping;
- links физически up, но traffic почти не проходит.

Для пользователя это выглядит просто:

```text
The network is down.
```

Для engineer это повод искать Layer 2 loop, лишний cable, неверный trunk, отключенный STP или неправильную STP topology.

## Как STP Решает Проблему

Spanning Tree Protocol, STP, не запрещает redundancy.

Он делает redundancy controlled.

STP смотрит на topology, обнаруживает redundant paths и блокирует те links или ports, которые сейчас не нужны для loop-free forwarding.

Важно:

```text
Blocked does not mean removed.
Blocked means standby.
```

Cable физически остается подключенным.

Если active path упадет, STP может пересчитать topology и открыть backup path.

Так сеть получает два свойства одновременно:

- protection from Layer 2 loops;
- redundancy for link failure.

## Почему STP Нужно Понимать Глубже

Если STP просто блокирует лишний link, почему нужна целая серия уроков?

Потому что real networks редко выглядят как два switches и два cables.

В enterprise environment может быть:

- 10 switches;
- 50 switches;
- 100 switches;
- access layer;
- distribution or collapsed core;
- multiple VLANs;
- multiple trunks;
- mixed link speeds;
- redundant uplinks;
- old and new switches in one topology.

STP должен выбрать loop-free path во всей этой topology.

И technical truth такой: STP может выбрать безопасный path, но не самый лучший path.

Например, он может оставить active старый медленный link и заблокировать более быстрый uplink, если bridge priorities и path costs оставлены на defaults.

С точки зрения STP это может быть valid loop-free topology.

С точки зрения performance это плохой design.

## Что Значит Управлять STP

Понимать STP - значит не просто знать, что он blocks loops.

Нужно понимать:

- как выбирается root bridge;
- почему один port становится root port;
- почему другой port становится designated;
- почему третий port блокируется;
- как path cost влияет на выбор;
- как bridge priority меняет root placement;
- как topology реагирует на failure.

Это не обязательно сразу конфигурация.

Сначала это mental model.

Ты смотришь на topology и можешь сказать:

```text
This switch should be root.
This uplink should forward.
This backup link should block.
If the active link fails, this path should open.
```

Вот это уже engineer-level understanding.

## Real World Tip

Broadcast storm может появиться даже от короткой ошибки.

Например, кто-то случайно подключил лишний patch cable между двумя switches или завел два wall ports в один unmanaged switch под столом.

Если STP включен и правильно работает, он должен защитить сеть.

Но convergence не всегда мгновенная, а misconfiguration может снизить защиту.

Перед добавлением новых switch connections в production полезно проверить:

- STP enabled;
- root bridge placement;
- port roles;
- trunk status;
- BPDU Guard/PortFast на edge ports;
- expected blocked links;
- documentation vs real cabling.

Не добавляй redundant cable "на удачу".

Сначала пойми, что сделает STP.

## Команды Для Проверки

Начальный набор:

```text
show spanning-tree
show spanning-tree vlan 10
show spanning-tree summary
show interfaces trunk
show mac address-table dynamic
```

Что искать:

- кто root bridge;
- какие ports forwarding;
- какие ports blocking;
- есть ли frequent topology changes;
- совпадает ли forwarding path с design;
- не flapping ли MAC addresses между ports.

Если MAC address быстро появляется то на одном port, то на другом, это может быть серьезным признаком Layer 2 loop или неправильной topology.

## Главный Вывод

Redundancy сама по себе не делает switch network надежной.

Без loop prevention она может уничтожить сеть.

STP нужен, чтобы второй cable был backup path, а не источником broadcast storm.

Запомни коротко:

```text
Redundant switch links create loops.
Loops create broadcast storms.
STP blocks redundant paths to keep the network alive.
```

Дальше важно понять не только что STP блокирует, но и почему он выбирает именно этот port, этот path и этот root bridge.

Именно это превращает STP из "магии, которая сделала link оранжевым" в инструмент, которым можно управлять.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Switching loop | Layer 2 loop where frames can circulate endlessly between switches. |
| Broadcast storm | Overload caused by broadcast frames looping and multiplying through the network. |
| TTL | Time To Live. Layer 3 packet field decremented by routers to limit routing loops. |
| STP | Spanning Tree Protocol. Protocol that blocks redundant Layer 2 paths to prevent loops. |
| Blocked port | STP state where a port does not forward user traffic because forwarding would create a loop. |
| Convergence | Process of STP recalculating a loop-free topology after a change. |
| Root bridge | Reference switch used by STP to calculate the best forwarding paths. |

## Questions

### 1. Why can adding a second cable between switches break the network?

Answer:

Because two Layer 2 links between the same switching paths can create a loop. Broadcast frames can circulate endlessly and cause a broadcast storm.

### 2. Why does TTL not protect a Layer 2 switching loop?

Answer:

TTL is an IP Layer 3 field handled by routers. Layer 2 switches forward Ethernet frames based on MAC addresses and do not decrement IP TTL during normal switching.

### 3. What does STP do with redundant links?

Answer:

STP blocks redundant paths that would create loops, while keeping them available as standby paths if the active link fails.

## What To Review Later

- Root bridge election.
- STP port roles.
- STP port states.
- Path cost and bridge priority.
- PortFast and BPDU Guard.
- EtherChannel for using multiple physical links without STP blocking each one separately.
