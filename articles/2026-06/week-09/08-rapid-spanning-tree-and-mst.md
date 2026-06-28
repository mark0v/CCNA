# Rapid Spanning Tree And MST

Source: закрытая страница курса  
Date added: 2026-06-28  
Related plan item: Week 9 / Rapid Spanning Tree and MST  
Tags: RSTP, Rapid PVST, MST, STP, convergence, alternate port, Cisco IOS, Layer 2
Language: Russian
Translation pair: articles-en/2026-06/week-09/08-rapid-spanning-tree-and-mst.md

## Кратко

Classic STP защищает сеть от Layer 2 loops, но convergence может быть слишком медленной.

В classic STP failover может занимать десятки seconds. Для modern network это уже не "нормальная пауза", а заметный outage.

Rapid Spanning Tree Protocol, RSTP, решает ту же задачу, что и classic STP:

```text
Prevent loops.
Keep redundancy.
Recover after failure.
```

Но делает это быстрее.

Главная мысль:

```text
RSTP is not a new switching idea.
It is a faster STP process.
```

Root bridge election, path cost и port blocking logic остаются знакомыми. Меняется скорость реакции и то, как switch заранее понимает роль backup paths.

## Проблема Classic STP

Classic STP работает осторожно.

Когда topology меняется, он может проходить через:

- blocking;
- listening;
- learning;
- forwarding.

В худших сценариях это может дать около 50 seconds before traffic recovers.

Причина в timers и в том, что classic STP часто ждет, прежде чем решить, что path действительно потерян.

BPDUs, Bridge Protocol Data Units, обычно отправляются каждые 2 seconds. Если expected BPDUs пропадают, STP eventually понимает, что topology изменилась, и начинает convergence.

Для старых networks это было acceptable.

Для сети, где работают payments, voice, cameras, cloud apps и business operations, это слишком долго.

## Что Улучшает RSTP

RSTP ускоряет convergence двумя практическими способами.

### 1. Быстрее Обнаруживает Failure

RSTP не обязан ждать так долго, как classic STP.

На практике RSTP может реагировать после потери нескольких hello intervals. Часто это описывают как three missed BPDUs, то есть примерно 6 seconds при default hello time 2 seconds.

Если physical link реально падает в состояние down, switch может реагировать еще быстрее, потому что port status изменился напрямую.

Это уже гораздо лучше, чем ждать classic STP timer path.

### 2. Помнит Backup Paths

В classic STP blocked port часто воспринимается просто как blocked.

RSTP добавляет более полезные roles.

Важная роль - alternate port.

Alternate port - это backup path к root bridge. Switch уже знает, что этот port может стать заменой root port, если primary path упадет.

Поэтому при failure не всегда нужно заново проходить длинный learning process.

Упрощенно:

```text
Classic STP:
Something failed.
Wait, recalculate, transition.

RSTP:
Primary path failed.
Use known alternate path.
```

В идеальных условиях failover может быть sub-second или близко к этому, особенно когда physical failure detected immediately.

## RSTP Не Отменяет Основы

RSTP не освобождает от понимания classic STP.

Все еще важно знать:

- root bridge;
- Bridge ID;
- path cost;
- root port;
- designated port;
- blocked/discarding behavior;
- BPDU exchange;
- topology changes.

Если ты понимаешь classic STP, RSTP выглядит логично.

Он не меняет цель. Он ускоряет и уточняет mechanism.

## Как Включить Rapid PVST+ На Cisco

На Cisco switches часто используется Rapid PVST+, то есть Rapid Per-VLAN Spanning Tree.

Команда:

```text
Switch(config)# spanning-tree mode rapid-pvst
```

Эту настройку нужно применять последовательно на switches в environment.

Rapid PVST+ означает:

- rapid convergence behavior;
- отдельный STP instance per VLAN;
- возможность разных root bridges для разных VLANs;
- per-VLAN load balancing через intentional root placement.

После включения проверяй:

```text
show spanning-tree
show spanning-tree summary
show running-config | include spanning-tree mode
```

## Почему Cisco Rapid PVST+ Не То Же Самое, Что "Один RSTP"

В Cisco environment обычно не один общий STP instance для всей сети.

PVST-подход означает:

```text
VLAN 10 has its STP logic.
VLAN 20 has its STP logic.
VLAN 30 has its STP logic.
```

Rapid PVST+ добавляет скорость RSTP к этому per-VLAN model.

Это удобно, потому что можно сделать:

- switch A root primary для VLAN 10;
- switch B root primary для VLAN 20;
- разные forwarding paths для разных VLANs;
- better use of redundant links.

Но есть tradeoff: много VLANs означает много STP instances.

## Когда PVST+ Становится Тяжелым

Для нескольких VLANs Rapid PVST+ удобен.

Но если network имеет десятки или сотни VLANs, per-VLAN instance начинает стоить ресурсов.

Каждый VLAN instance требует:

- BPDU processing;
- separate STP state;
- topology calculation;
- CPU and memory attention;
- operational visibility.

В маленькой lab это незаметно.

В large campus network это становится design concern.

## MST: Multiple Spanning Tree

MST, Multiple Spanning Tree, решает scale problem.

Вместо отдельного STP instance для каждой VLAN, MST позволяет сгруппировать VLANs в instances.

Пример:

```text
Instance 1: VLANs 10-50
Instance 2: VLANs 51-100
Instance 3: VLANs 101-150
```

Так network получает несколько STP topologies, но не отдельную topology на каждый VLAN.

Идея:

```text
PVST+: one instance per VLAN.
MST: one instance per VLAN group.
```

Это снижает overhead и сохраняет flexibility для large environments.

## Три Варианта, Которые Нужно Различать

### Classic STP

Original behavior.

Плюсы:

- простая идея;
- loop prevention;
- still exists in old networks.

Минусы:

- slow convergence;
- 30-50 second delays can be painful;
- not ideal for modern production.

### Rapid PVST+

Cisco-friendly modern default для многих environments.

Плюсы:

- fast convergence;
- per-VLAN flexibility;
- familiar Cisco operations;
- good fit for many campus networks.

Минусы:

- one instance per VLAN;
- overhead grows with VLAN count.

### MST

Scale-oriented approach.

Плюсы:

- groups VLANs into fewer STP instances;
- reduces overhead;
- works better for large VLAN counts;
- still allows multiple forwarding topologies.

Минусы:

- requires more careful planning;
- region/config consistency matters;
- troubleshooting can be less beginner-friendly.

## Практическая Рекомендация

Если ты наследуешь Cisco switching network, проверь STP mode.

Команды:

```text
show spanning-tree summary
show running-config | include spanning-tree mode
```

Если network still runs classic 802.1D behavior, это стоит обсудить как modernization target.

Для обычной Cisco campus/lab среды чаще всего ожидаешь:

```text
spanning-tree mode rapid-pvst
```

Для large enterprise с большим количеством VLANs может быть уместен MST.

Но не меняй STP mode вслепую. Сначала проверь:

- current root bridge placement;
- VLAN count;
- switch platform support;
- topology design;
- maintenance window;
- rollback plan;
- documentation.

## Главный Вывод

RSTP делает STP быстрее, но не отменяет STP fundamentals.

Rapid PVST+ - это Cisco-подход: fast convergence plus per-VLAN STP.

MST - это scale-подход: group VLANs into fewer STP instances.

Запомни:

```text
Classic STP: original and slow.
Rapid PVST+: fast Cisco per-VLAN model.
MST: scalable grouped-instance model.
```

Если ты понимаешь classic STP decisions, Rapid STP становится понятным: он быстрее реагирует, заранее знает backup paths и лучше подходит для modern networks.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| RSTP | Rapid Spanning Tree Protocol, faster STP evolution. |
| Rapid PVST+ | Cisco rapid per-VLAN STP mode. |
| Alternate port | RSTP backup path that can replace the root port if the primary path fails. |
| MST | Multiple Spanning Tree, grouping VLANs into shared STP instances. |
| Convergence | Process of recalculating and restoring a loop-free topology after a change. |
| BPDU | STP control message exchanged between switches. |
| 802.1D | Original classic STP standard behavior. |

## Questions

### 1. What is the main advantage of RSTP over classic STP?

Answer:

RSTP converges much faster by reacting more quickly to failures and by using roles such as alternate ports for known backup paths.

### 2. What Cisco command enables Rapid PVST+?

Answer:

`spanning-tree mode rapid-pvst`

### 3. Why use MST in a large network?

Answer:

MST reduces overhead by grouping many VLANs into fewer spanning tree instances instead of running a separate instance for every VLAN.

## What To Review Later

- RSTP port roles.
- RSTP proposal/agreement behavior.
- Rapid PVST+ verification.
- MST regions and VLAN-to-instance mapping.
- STP migration planning.
