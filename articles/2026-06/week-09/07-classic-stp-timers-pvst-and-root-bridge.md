# Classic STP Timers, PVST, And Root Bridge Control

Source: закрытая страница курса  
Date added: 2026-06-28  
Related plan item: Week 9 / Classic STP timers, PVST, and root bridge configuration  
Tags: STP, PVST, RSTP, timers, port states, root bridge, priority, Cisco IOS
Language: Russian
Translation pair: articles-en/2026-06/week-09/07-classic-stp-timers-pvst-and-root-bridge.md

## Кратко

Classic Spanning Tree Protocol безопасный, но медленный.

Когда port поднимается, он не начинает forwarding сразу. Classic STP сначала проводит его через states, чтобы не создать Layer 2 loop.

Минимально это может занять 30 seconds:

```text
Listening: 15 seconds
Learning: 15 seconds
Forwarding: traffic starts
```

В failover scenario восстановление может занять до 50 seconds, если учитывать blocking/max age behavior.

Для старых сетей это было acceptable. Для современных networks это очень долго. Поэтому в production обычно используют Rapid Spanning Tree Protocol, RSTP, но понимать classic STP states все равно важно: RSTP ускоряет тот же базовый процесс.

## Почему Classic STP Медленный

STP не создан для скорости.

Он создан для safety.

Когда interface появляется в topology, switch не может просто начать пересылать traffic. Сначала нужно убедиться, что этот port не создаст loop.

Если начать forwarding слишком рано, один неправильный redundant link может вызвать broadcast storm.

Поэтому classic STP ждет, слушает BPDUs, строит MAC table и только потом forwards frames.

Это выглядит медленно, потому что это действительно медленно.

## Четыре Port States

Classic STP часто объясняют через port states.

### Blocking

Blocking state используется, когда STP считает, что forwarding через этот port может создать loop.

Port:

- не forwards user traffic;
- не learns MAC addresses;
- still receives BPDUs;
- может оставаться standby path.

В convergence scenario ожидание может быть до 20 seconds, связанное с max age.

Blocking - это не обязательно failure. Часто это normal STP protection.

### Listening

Listening длится 15 seconds.

В этом состоянии switch активно участвует в STP calculation:

- принимает и отправляет BPDUs;
- выясняет root bridge;
- определяет port roles;
- не forwards user traffic;
- не builds MAC address table для user frames.

Port уже участвует в STP logic, но еще не обслуживает обычный traffic.

### Learning

Learning тоже длится 15 seconds.

Теперь switch начинает building MAC address table.

Port:

- learns source MAC addresses;
- still does not forward user traffic;
- готовится к безопасному forwarding.

Это снижает вероятность лишнего flooding, когда port наконец перейдет в forwarding.

### Forwarding

Forwarding - рабочее состояние.

Port:

- forwards user traffic;
- learns MAC addresses;
- sends and receives BPDUs;
- участвует в normal switching.

Именно до этого состояния users обычно ждут после подключения link.

## 30 И 50 Seconds

Для freshly activated port в classic STP минимум часто выглядит так:

```text
Listening 15s
Learning  15s
Total     30s
```

В некоторых failover cases добавляется ожидание blocking/max age:

```text
Blocking / max age 20s
Listening          15s
Learning           15s
Total              50s
```

Это не glitch.

Это design classic STP.

Но для modern network 30-50 seconds downtime может быть unacceptable.

## Почему RSTP Важен

Rapid Spanning Tree Protocol, RSTP, появился именно потому, что classic STP convergence слишком медленный для современных ожиданий.

RSTP сохраняет цель STP:

```text
Prevent Layer 2 loops.
Preserve redundancy.
Recover after failure.
```

Но делает convergence намного быстрее.

Пока важно понять classic process. Тогда RSTP будет выглядеть не как новая магия, а как faster version of the same idea.

## PVST: Один STP Instance На VLAN

На Cisco switch команда:

```text
show spanning-tree
```

часто показывает не один STP instance, а отдельный instance per VLAN.

Это PVST, Per-VLAN Spanning Tree.

Идея:

```text
Each VLAN can have its own STP topology.
```

Например:

- VLAN 10 может иметь один root bridge;
- VLAN 20 может иметь другой root bridge;
- VLAN 30 может использовать другой forwarding path.

Это помогает load balancing.

Link, который blocked для VLAN 10, может forwarding для VLAN 20.

Так сеть не обязана держать один и тот же active path для всех VLANs.

## Почему Priority Выглядит Странно

В Cisco PVST можно увидеть priority вроде:

```text
32769
32778
```

Это не случайные числа.

Default bridge priority обычно `32768`, но Cisco добавляет VLAN ID в extended system ID.

Примеры:

| VLAN | Displayed priority |
| --- | --- |
| VLAN 1 | 32769 |
| VLAN 10 | 32778 |
| VLAN 20 | 32788 |

Логика:

```text
32768 + VLAN ID
```

Именно поэтому для ручной настройки priority используются increments of 4096. Часть field используется для VLAN information.

## Почему Root Bridge Нельзя Оставлять Случаю

Если root bridge не настроить, STP выберет его по lowest Bridge ID.

Если priority у всех switches одинаковая, победит lowest MAC address.

Это может поставить root bridge на random access switch в wiring closet.

Последствия:

- traffic идет не через лучший switch;
- fast uplink может оказаться blocked;
- topology выглядит странно;
- troubleshooting становится сложнее;
- failure recovery может идти не так, как ожидалось.

Root bridge должен быть design decision.

Обычно root выбирают на core или distribution switch.

## Настройка Root Bridge Вручную

Вариант 1 - задать priority явно:

```text
spanning-tree vlan 1 priority 4096
```

Lower priority wins.

Главное - выбрать значение ниже, чем у остальных switches.

Для нескольких VLANs можно настраивать отдельно, чтобы управлять per-VLAN topology.

## Root Primary И Root Secondary

Cisco также дает shortcut commands:

```text
spanning-tree vlan 1 root primary
spanning-tree vlan 1 root secondary
```

`root primary` смотрит на текущие priorities и пытается поставить switch ниже остальных, чтобы он стал root.

`root secondary` задает priority так, чтобы switch стал backup root. Если primary root bridge упадет, secondary должен выиграть election вместо случайного closet switch.

Можно указать несколько VLANs:

```text
spanning-tree vlan 1,10,20 root primary
```

или в IOS-style range/list syntax, если platform это поддерживает.

## Практическая Проверка

После настройки STP не верь config blindly.

Проверяй:

```text
show spanning-tree
show spanning-tree vlan 1
show spanning-tree vlan 10
show running-config | include spanning-tree
```

Смотри:

- кто root bridge для каждой VLAN;
- local switch является root или нет;
- какая priority отображается;
- какие ports root/designated/blocked;
- совпадает ли forwarding path с design.

## Главный Вывод

Classic STP надежный, но медленный.

Port может ждать 30 seconds перед forwarding, а failover может занимать до 50 seconds.

PVST добавляет важную Cisco-особенность: отдельный STP instance для каждой VLAN, что позволяет управлять paths и load balancing per VLAN.

Root bridge election нельзя оставлять на default MAC address tiebreaker.

Запомни:

```text
Classic STP is cautious.
PVST is per VLAN.
Root bridge should be intentional.
RSTP is the faster next step.
```

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Blocking | STP state where a port does not forward user traffic to prevent loops. |
| Listening | STP state where a port participates in BPDU exchange but does not forward traffic. |
| Learning | STP state where a port learns MAC addresses but still does not forward user traffic. |
| Forwarding | STP state where a port forwards traffic and learns MAC addresses. |
| PVST | Per-VLAN Spanning Tree, Cisco STP mode with one STP instance per VLAN. |
| RSTP | Rapid Spanning Tree Protocol, faster STP evolution. |
| Root primary | Cisco shortcut to make a switch the intended STP root for selected VLANs. |
| Root secondary | Cisco shortcut to make a switch the backup STP root for selected VLANs. |

## Questions

### 1. Why can classic STP take 30 seconds before forwarding?

Answer:

Because a port normally spends 15 seconds in listening and 15 seconds in learning before forwarding traffic.

### 2. Why does Cisco show priorities like 32769 for VLAN 1?

Answer:

Because Cisco PVST uses extended system ID: default priority 32768 plus the VLAN ID.

### 3. Why configure root primary and root secondary?

Answer:

To make the intended core or distribution switch the root bridge and keep a planned backup root ready if the primary fails.

## What To Review Later

- Rapid Spanning Tree Protocol.
- STP timers and convergence.
- PVST and per-VLAN load balancing.
- Root bridge priority design.
- PortFast and BPDU Guard for edge ports.
