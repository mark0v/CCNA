# Spanning Tree Implementation Checklist

Source: закрытая страница курса  
Date added: 2026-06-28  
Related plan item: Week 9 / Spanning Tree rollout checklist  
Tags: STP, Rapid PVST, root bridge, trunk, VLAN, PortFast, BPDU Guard, checklist
Language: Russian
Translation pair: articles-en/2026-06/week-09/10-spanning-tree-implementation-checklist.md

## Кратко

Spanning Tree rollout нельзя начинать с хаотичного ввода команд.

Если включать STP features без checklist, легко получить странную topology, неправильный root bridge, inconsistent trunks или даже Layer 2 loop.

Рабочий порядок:

```text
1. Enable Rapid PVST+ everywhere.
2. Choose root and secondary root bridges.
3. Verify consistent VLANs and trunks.
4. Enable PortFast and BPDU Guard on access ports.
5. Verify, fix, and save.
```

Это не просто lab routine. Это production mindset: сначала design, потом configuration, потом verification.

## Почему Нужен Checklist

STP configuration touches the whole switching topology.

Одна пропущенная команда может выглядеть мелочью, но последствия будут большими:

- один switch остался в classic STP mode;
- root bridge выбрался по lowest MAC address;
- trunk не carries нужную VLAN;
- access port без BPDU Guard принял loop;
- config не сохранили после successful verification.

STP должен быть consistent.

Особенно если сеть содержит несколько switches, несколько VLANs и redundant links.

## Step 1: Enable Rapid PVST+ Everywhere

На Cisco switches classic STP может работать, но он slow.

Для modern Cisco environment ожидаемый baseline часто:

```text
spanning-tree mode rapid-pvst
```

Включать нужно на каждом switch.

Не только на core.

Не только на том switch, который прямо сейчас трогаешь.

Проверь Cafe switches, Fallout Shelter switches и любые остальные switches в той же Layer 2 topology.

Verification:

```text
show spanning-tree summary
show running-config | include spanning-tree mode
```

Если один switch остался в старом behavior, convergence может быть inconsistent и slow.

## Step 2: Choose The Root Bridge

Root bridge - это STP reference point.

Выбирать его нужно по topology, а не по MAC address.

Хорошие вопросы:

- какой switch самый central;
- где больше uplinks;
- какой switch ближе к router/firewall;
- где logical distribution point;
- какой switch должен быть backup root.

Для Fallout Shelter example root bridge - Switch 1, потому что он central и связан с routing side.

Настройка primary root через priority:

```text
spanning-tree vlan 1,10,20,30,40 priority 4096
```

Secondary root:

```text
spanning-tree vlan 1,10,20,30,40 priority 8192
```

Lower priority wins.

Альтернатива Cisco shortcut:

```text
spanning-tree vlan 1,10,20,30,40 root primary
spanning-tree vlan 1,10,20,30,40 root secondary
```

Оба подхода нужно понимать.

Verification:

```text
show spanning-tree vlan 10
show spanning-tree vlan 20
show spanning-tree root
```

## Step 3: Verify VLANs And Trunks

Это critical step.

Cisco PVST/Rapid PVST+ runs separate STP instance per VLAN.

Если VLAN 1 выглядит good, это не значит, что VLAN 10, 20, 30 и 40 тоже good.

Trunk inconsistency может создать странную STP behavior:

- одна VLAN missing на trunk;
- trunk не включен на одном uplink;
- allowed VLAN list не совпадает;
- STP topology для одной VLAN отличается от expected;
- где ожидался blocked port, появились два forwarding paths.

Команда:

```text
show interfaces trunk
```

Проверяй:

- trunk mode;
- native VLAN;
- allowed VLANs;
- VLANs active in management domain;
- VLANs in spanning tree forwarding state and not pruned.

Также полезно:

```text
show vlan brief
show running-config interface ...
```

Не отмечай этот пункт как done, пока trunks не проверены на обоих ends.

## Step 4: Enable PortFast And BPDU Guard On Access Ports

Access ports идут к end devices:

- PCs;
- printers;
- POS terminals;
- cameras;
- phones;
- access points.

На них обычно нужны:

- PortFast для быстрого forwarding;
- BPDU Guard для защиты от случайного switch или loop.

Пример для range:

```text
interface range fa0/3-24
 switchport mode access
 spanning-tree portfast
 spanning-tree bpduguard enable
```

PortFast убирает unnecessary listening/learning delay для end devices.

BPDU Guard переводит port в err-disabled, если access port получает BPDU.

Это именно та защита, которая помогает против маленьких unmanaged switches под столом.

Важно: не применяй access-port template к uplinks/trunks.

## Step 5: Verify And Save

После configuration нужен verification pass.

Минимальный набор:

```text
show spanning-tree
show spanning-tree vlan 10
show spanning-tree vlan 20
show spanning-tree summary
show interfaces trunk
show interfaces status
```

Проверь:

- root bridge тот, который ожидался;
- secondary root configured;
- blocked ports make sense;
- root ports point toward expected root;
- designated ports match topology;
- trunks carry required VLANs;
- access ports have PortFast/BPDU Guard;
- нет unexpected err-disabled ports.

Если что-то выглядит странно, не сохраняй blindly.

Сначала исправь.

После successful verification:

```text
copy running-config startup-config
```

И сделай это на каждом switch.

## Как Читать Странную Topology

Если STP output не совпадает с ожиданиями, используй уже знакомые tiebreakers:

```text
1. Lowest cost to root.
2. Lowest bridge ID.
3. Lowest port number.
```

Пример: если link работает на 10 Mbps вместо 100 Mbps, cost становится worse. STP может заблокировать port, который ты ожидал увидеть forwarding.

Поэтому при странной topology проверяй не только STP, но и physical/interface details:

```text
show interfaces status
show interfaces counters errors
show running-config interface ...
```

## Rollout Checklist

Перед изменениями:

- определить target switches;
- нарисовать expected root/secondary root;
- определить VLAN list;
- определить trunk links;
- определить access port ranges;
- согласовать maintenance window, если production.

Во время изменений:

- включить Rapid PVST+ на всех switches;
- настроить root/secondary root;
- проверить trunks and VLANs;
- применить PortFast/BPDU Guard на access ports;
- проверить STP state.

После изменений:

- сохранить config;
- обновить documentation;
- записать actual blocked ports;
- проверить monitoring/logs;
- оставить rollback notes.

## Главный Вывод

STP rollout - это не одна команда.

Это sequence.

Запомни:

```text
Mode first.
Root bridge second.
Trunks third.
Access protections fourth.
Verify and save last.
```

Если пройти checklist, сеть получает loop prevention, fast convergence и предсказуемую topology.

Если пропустить шаги, STP все равно что-то выберет, но не обязательно то, что ты хотел.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Rapid PVST+ | Cisco rapid per-VLAN STP mode. |
| Root bridge | STP reference switch that other switches calculate paths toward. |
| Secondary root | Planned backup root bridge if the primary root fails. |
| Trunk consistency | Matching trunk mode and allowed VLANs across both ends of a link. |
| PortFast | Feature that moves edge ports to forwarding quickly. |
| BPDU Guard | Protection that err-disables edge ports if they receive BPDUs. |
| Startup-config | Saved configuration that survives reload. |

## Questions

### 1. Why enable Rapid PVST+ on every switch?

Answer:

Because one switch left in classic STP behavior can still introduce slow convergence and inconsistent behavior in the Layer 2 topology.

### 2. Why verify trunks before trusting STP output?

Answer:

Because Rapid PVST+ runs per VLAN. A trunk that misses VLANs can make one VLAN look correct while another VLAN has broken or dangerous topology.

### 3. Why save after verification instead of immediately after typing commands?

Answer:

Because you should only preserve a configuration after confirming root bridge placement, trunk consistency, port roles, access protections and expected forwarding behavior.

## What To Review Later

- STP troubleshooting workflow.
- Root bridge tuning.
- Per-VLAN load balancing.
- Port cost and speed mismatches.
- Change-control checklist for Layer 2 rollouts.
