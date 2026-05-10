# Using Straight-through, Crossover, and MDI-X

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Ethernet cable types  
Tags: ethernet, straight-through, crossover, auto-mdix, tx, rx, 802.3, cabling, switch

## Summary

Straight-through, crossover и Auto MDI-X объясняют, как transmit and receive pairs должны совпадать между устройствами. В старых сетях cable type был важен: unlike devices обычно соединяли straight-through cable, like devices - crossover cable. Современный Auto MDI-X чаще всего решает это автоматически.

Главная мысль: сейчас ты часто просто подключаешь обычный patch cable и все работает, но understanding TX/RX помогает при troubleshooting.

## Key Points

- Ethernet работает по standards family IEEE 802.3.
- Standards дают interoperability между vendors.
- TX means transmit.
- RX means receive.
- Старые 10/100 Mbps Ethernet использовали только часть pins.
- PC/end device typically transmitted on pins 1 and 2.
- PC/end device typically received on pins 3 and 6.
- Switch был wired opposite way.
- Straight-through cable connects pin 1 to pin 1, pin 2 to pin 2, etc.
- Straight-through cable worked for unlike devices, like PC to switch.
- Crossover cable swaps transmit and receive pairs.
- Crossover cable was used for like devices, like switch to switch or PC to PC.
- Auto MDI-X автоматически определяет, нужно ли поменять TX/RX behavior.
- Modern devices usually support Auto MDI-X.
- Older gear and some embedded devices may still require attention to cable type.

## Notes

### Why Standards Matter

Ethernet cabling and communication are standards-based.

Это позволяет соединять devices разных vendors и ожидать predictable behavior.

```text
Dell switch + Apple laptop + Cisco router = works because standards
```

### Straight-through Cable

Straight-through means:

```text
Pin 1 -> Pin 1
Pin 2 -> Pin 2
Pin 3 -> Pin 3
...
```

Он исторически использовался для unlike devices:

- PC to switch;
- router to switch;
- endpoint to switch.

Идея: одна сторона sends там, где другая receives.

### Crossover Cable

Если соединить два like devices, у них могут совпасть TX and RX pins. Тогда оба пытаются говорить или слушать на одинаковых парах.

Crossover cable исправляет это:

```text
TX pair <-> RX pair
```

Исторически used for:

- switch to switch;
- PC to PC;
- router to router in some cases.

### Auto MDI-X

Auto MDI-X позволяет устройству автоматически определить, как использовать pairs.

Это значит, что modern switches and NICs обычно могут работать и со straight-through, и с crossover cable.

Но при troubleshooting старого оборудования нельзя слепо рассчитывать на Auto MDI-X.

## Commands / Terms

```text
TX - transmit
RX - receive
Straight-through - pins match end-to-end
Crossover - TX/RX pairs are crossed
Auto MDI-X - automatic pair role detection
802.3 - Ethernet standards family
```

## Questions

### Когда historically использовали straight-through cable?

Для unlike devices, например PC to switch.

### Когда historically использовали crossover cable?

Для like devices, например switch to switch или PC to PC.

### Что делает Auto MDI-X?

Автоматически определяет и меняет TX/RX behavior, чтобы link поднялся с обычным cable.

### Почему это все еще важно знать?

Потому что old gear, unusual devices and troubleshooting иногда требуют понимания старой логики.

## What To Review Later

- T568A/T568B crossover pinout.
- Auto-negotiation.
- Link lights.
- Full duplex and half duplex.
- Legacy Ethernet behavior.
