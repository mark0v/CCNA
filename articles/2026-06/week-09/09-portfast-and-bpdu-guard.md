# PortFast And BPDU Guard

Source: закрытая страница курса  
Date added: 2026-06-28  
Related plan item: Week 9 / PortFast and BPDU Guard on access ports  
Tags: STP, PortFast, BPDU Guard, err-disabled, access port, unmanaged switch, Cisco IOS
Language: Russian
Translation pair: articles-en/2026-06/week-09/09-portfast-and-bpdu-guard.md

## Кратко

Иногда сеть ломает не сложная атака и не ошибка firewall.

Иногда сеть ломает маленький unmanaged switch под столом.

Сценарий простой:

- кому-то нужен еще один network port;
- подключают дешевый unmanaged switch;
- позже кто-то случайно создает loop кабелем;
- broadcast traffic начинает ходить по кругу;
- сеть получает broadcast storm.

Проблема в том, что cheap unmanaged switches обычно не участвуют в STP. Они не помогают разорвать loop.

На Cisco switches для защиты access ports используются две важные функции:

```text
PortFast + BPDU Guard
```

PortFast ускоряет подключение end devices.

BPDU Guard защищает access port, если на нем внезапно появился switch.

## Почему Unmanaged Switch Опасен

Обычный access port должен вести к end device:

- PC;
- printer;
- IP phone;
- access point;
- camera;
- POS terminal.

End device не должен отправлять BPDUs.

BPDU, Bridge Protocol Data Unit, - это STP control message. Switches используют BPDUs, чтобы обнаруживать topology, выбирать root bridge и предотвращать loops.

Если access port получил BPDU, это подозрительно.

Это может означать:

- кто-то подключил switch;
- появился loop;
- порт используется не так, как был designed;
- unmanaged device начал создавать Layer 2 risk.

## BPDU Guard

BPDU Guard - это защита для ports, где не должно быть switches.

Логика:

```text
If this access port receives a BPDU,
shut it down before it can damage the network.
```

Когда BPDU Guard срабатывает, Cisco switch переводит port в err-disabled state.

Port перестает forwarding traffic.

Это может выглядеть жестко, но это лучше, чем позволить одному неправильному cable вызвать broadcast storm.

В logs можно увидеть message вроде:

```text
BPDU guard error detected
```

В interface status port может отображаться как:

```text
err-disabled
```

## Как Восстановить Err-Disabled Port

Базовое ручное восстановление:

```text
interface gigabitEthernet0/10
 shutdown
 no shutdown
```

Но перед recovery важно найти причину.

Не надо просто делать `shutdown` / `no shutdown`, если под столом все еще лежит loop или unmanaged switch подключен неправильно.

Проверь:

- что подключено в port;
- не воткнут ли лишний cable;
- нет ли маленького unmanaged switch;
- не должен ли этот port быть настоящим uplink;
- нет ли ошибки в documentation.

Err-disabled - это не только BPDU Guard. Такое состояние может появляться и из-за других защит, например port security violations.

Но навык clear через shutdown/no shutdown полезен в реальной работе.

## PortFast

PortFast решает другую проблему.

Classic STP может ждать:

```text
Listening 15s
Learning  15s
Forwarding
```

Для switch-to-switch links это осторожность.

Для обычного laptop или printer это лишняя задержка.

End device не создает switching topology. Он не должен становиться частью STP calculation как switch uplink.

PortFast говорит switch:

```text
This is an edge port.
Move to forwarding immediately.
```

Результат:

- PC быстрее получает network access;
- DHCP работает быстрее;
- user не ждет 30 seconds;
- access port ведет себя как edge port.

## Почему PortFast И BPDU Guard Используют Вместе

PortFast ускоряет port.

Но если кто-то подключит switch к PortFast-enabled port, появляется риск: port может быстро перейти в forwarding.

Именно поэтому PortFast и BPDU Guard обычно идут вместе.

Design logic:

```text
PortFast:
End devices should come online fast.

BPDU Guard:
If this edge port receives a BPDU, shut it down.
```

Один дает speed.

Другой дает safety.

## Настройка На Interface

Для конкретного access port:

```text
interface gigabitEthernet0/10
 switchport mode access
 spanning-tree portfast
 spanning-tree bpduguard enable
```

Используй это для ports, которые идут к end devices.

Не используй на switch uplinks без понимания design.

## Глобальная Настройка

Масштабируемый подход - включить PortFast для access ports и BPDU Guard для PortFast-enabled ports.

Команды:

```text
spanning-tree portfast default
spanning-tree portfast bpduguard default
```

После этого ports, которые должны быть uplinks/trunks, нужно настроить явно и не считать их edge ports.

Если нужно отключить BPDU Guard на конкретном uplink:

```text
interface gigabitEthernet0/1
 spanning-tree bpduguard disable
```

Но лучше сначала убедиться, что это действительно switch-to-switch link.

## Что Проверять

Полезные команды:

```text
show spanning-tree summary
show spanning-tree interface gigabitEthernet0/10 detail
show interfaces status err-disabled
show interfaces gigabitEthernet0/10
show logging
show running-config interface gigabitEthernet0/10
```

Проверяй:

- включен ли PortFast;
- включен ли BPDU Guard;
- не err-disabled ли port;
- есть ли BPDU Guard log message;
- правильный ли device подключен к port;
- не является ли port uplink.

## Практический Deployment Pattern

Для реальной сети хороший pattern такой:

1. Access ports получают PortFast.
2. Эти же edge ports получают BPDU Guard.
3. Uplinks/trunks документируются отдельно.
4. На switch-to-switch links PortFast не используется как обычный access edge feature.
5. После срабатывания BPDU Guard сначала ищется физическая причина, потом port возвращается.

Главная идея:

```text
Default edge ports should be fast and protected.
Uplinks should be intentional and documented.
```

## Главный Вывод

PortFast и BPDU Guard закрывают очень реальную human problem.

Люди подключают маленькие switches, перетыкают cables, забывают временные решения и создают loops.

PortFast делает access ports быстрыми для end devices.

BPDU Guard выключает edge port, если он внезапно начинает получать STP BPDUs.

Запомни:

```text
PortFast for speed.
BPDU Guard for protection.
Use them together on edge ports.
```

Это маленькая настройка, которая может спасти всю Layer 2 network от очень глупого outage.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| PortFast | Cisco STP feature that lets edge ports move to forwarding immediately. |
| BPDU Guard | Feature that err-disables a port if it receives a BPDU where it should not. |
| BPDU | Bridge Protocol Data Unit, STP control message sent between switches. |
| Err-disabled | Cisco port state where the switch disables an interface because of a protection event. |
| Edge port | Port intended for an end device, not another switch. |
| Unmanaged switch | Simple switch with no managed STP controls or enterprise safeguards. |

## Questions

### 1. Why should PortFast be used on end-device ports?

Answer:

Because end-device ports do not need the normal STP listening and learning delay. PortFast lets them reach forwarding quickly.

### 2. What does BPDU Guard do when an access port receives a BPDU?

Answer:

It places the port into an err-disabled state to prevent a possible Layer 2 loop or unauthorized switch connection.

### 3. Why are PortFast and BPDU Guard commonly deployed together?

Answer:

PortFast gives fast forwarding on edge ports, while BPDU Guard shuts the port down if that edge port starts behaving like a switch-facing link.

## What To Review Later

- PortFast edge behavior.
- BPDU Guard recovery.
- Err-disabled causes.
- Port security.
- Storm control.
- Proper access layer documentation.
