# Forcing My Kids to Make Ethernet Cables

Source: закрытая страница курса  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 00 Lesson 11  
Tags: ethernet, cabling, cat5e, utp, stp, rj45, t568b, crossover, auto-mdix

## Summary

Эта статья объясняет, зачем IT-специалисту понимать Ethernet cable construction, даже если большинство patch cables проще купить готовыми. Создание кабеля вручную помогает понять twisted pairs, pinouts, RJ45 connectors, T568B, straight-through и crossover cables, а также важность тестирования.

Главная мысль статьи: Ethernet cable - это не просто “провод”. Это carefully engineered system из copper wires, twisted pairs, standards и termination rules, от которых зависит стабильность network.

## Key Points

- Ethernet cables можно купить готовыми, но полезно хотя бы раз сделать cable самому.
- Custom cable может понадобиться для exact length, structured cabling, damaged run или office/shop wiring.
- Basic tools: Ethernet cable, RJ45 connector, crimping tool and cable tester.
- Cat5e UTP часто используется для basic Ethernet cabling.
- UTP means Unshielded Twisted Pair.
- STP means Shielded Twisted Pair.
- Twisted pairs уменьшают EMI and crosstalk.
- Older Ethernet standards могли использовать only two pairs.
- 1000BASE-T uses all four pairs and supports simultaneous send/receive.
- Straight-through cable используется для different device types, например PC to switch.
- Crossover cable historically used for similar devices, например PC to PC or switch to switch.
- Auto-MDIX позволяет modern devices automatically adjust transmit/receive pairs.
- T568B pinout нужно знать и уметь собрать.
- Cable tester confirms whether pins 1-8 are wired correctly.
- Standard copper Ethernet run max length is 100 meters.

## Notes

### Why Make Ethernet Cables?

Готовые Ethernet cables обычно лучше покупать, особенно patch cables. Они надежнее, аккуратнее и экономят время.

Но умение terminate cable полезно, когда нужно:

- сделать custom length;
- заменить damaged cable run;
- проложить cable через walls/ceilings;
- подключить new office/back office;
- wire a POS terminal;
- troubleshoot physical layer issues;
- understand Ethernet beyond theory.

Практическая идея:

```text
Once you terminate and test a cable yourself, Ethernet becomes less mysterious.
```

### Tools and Materials

Basic set:

| Item | Purpose |
| --- | --- |
| Ethernet cable | Copper cable with twisted pairs |
| RJ45 connector | Connector terminated on cable end |
| Crimping tool | Tool that attaches connector to cable |
| Cable tester | Verifies correct pin continuity/order |
| Cable stripper/cutter | Removes outer jacket and trims wires |

Cable tester is especially important because bad termination can create painful troubleshooting later.

### Stripping the Cable

First step is removing the outer sheath/jacket.

Important warning:

```text
Do not nick or damage the copper wires inside.
```

If a wire is damaged during stripping, the cable might fail immediately or create intermittent problems later. Intermittent physical layer problems are especially frustrating.

### What's Inside the Cable

Inside Ethernet cable are:

- 4 twisted pairs;
- 8 copper wires total.

The twists are not decorative. They reduce electrical problems:

- EMI;
- crosstalk.

### EMI and Crosstalk

| Term | Meaning |
| --- | --- |
| EMI | Electromagnetic Interference; outside electrical noise affecting signal. |
| Crosstalk | Interference between signals in nearby wires/pairs. |

Twisted pair design helps preserve signal quality by reducing these effects.

### UTP vs STP

UTP means Unshielded Twisted Pair.

Characteristics:

- no extra metallic shielding;
- common in office/home networks;
- relies on twists to reduce interference.

STP means Shielded Twisted Pair.

Characteristics:

- includes shielding;
- better for electrically noisy environments;
- useful in factories or places with strong interference.

### Ethernet Standards and Pair Usage

Older Ethernet standards did not always use all four pairs.

| Standard | Pair usage idea |
| --- | --- |
| 10BASE-T | Uses two pairs |
| 100BASE-TX | Uses two pairs |
| 1000BASE-T | Uses all four pairs |

1000BASE-T is gigabit Ethernet over Cat5e. It uses all four pairs and can send/receive at the same time.

### Straight-Through Cable

Straight-through cable has the same pinout on both ends.

Common use:

```text
PC -> Switch
```

Historically, this worked because PCs and switches used complementary transmit/receive pins.

### Crossover Cable

Crossover cable swaps transmit and receive pairs.

Historical use:

```text
PC -> PC
Switch -> Switch
```

Reason: similar devices could be transmitting and receiving on the same pins, so crossover corrected the conversation.

### Auto-MDIX

Auto-MDIX allows modern devices to automatically detect and adjust transmit/receive pairs.

Because of Auto-MDIX:

- crossover cables are less common in daily work;
- straight-through cables often work in more situations;
- the concept still matters for exam knowledge and Ethernet history.

Auto-MDIX does not make the old concept useless. It explains why modern cabling feels easier than older cabling.

### T568B Pinout

The lesson uses T568B for a straight-through cable.

T568B wire order:

| Pin | Wire color |
| --- | --- |
| 1 | White orange |
| 2 | Orange |
| 3 | White green |
| 4 | Blue |
| 5 | White blue |
| 6 | Green |
| 7 | White brown |
| 8 | Brown |

Memory target:

```text
White orange, orange,
white green, blue,
white blue, green,
white brown, brown
```

The order matters. One wire in the wrong place can make the cable fail or behave unpredictably.

### Building the Cable

Basic process:

1. Strip back the outer jacket.
2. Untwist the pairs.
3. Straighten the wires.
4. Arrange wires in T568B order.
5. Trim wires evenly.
6. Insert wires into RJ45 connector with clip facing down.
7. Confirm all wires reach the end of the connector.
8. Crimp the connector.
9. Repeat the same pinout on the other end for straight-through cable.
10. Test the cable.

For straight-through T568B:

```text
End A = T568B
End B = T568B
```

### Testing the Cable

Cable tester verifies whether pins are connected correctly.

Good result:

```text
1 -> 1
2 -> 2
3 -> 3
4 -> 4
5 -> 5
6 -> 6
7 -> 7
8 -> 8
```

Bad signs:

- missing light;
- lights out of order;
- intermittent connection;
- split pair;
- wrong pin mapping.

If termination is bad, the practical fix is often to cut off the connector and terminate again.

### Maximum Copper Ethernet Length

Standard copper Ethernet run max length:

```text
100 meters
```

Going beyond 100 meters can cause signal degradation and strange network behavior.

If NetworkChuck Coffee needs to connect something farther than copper supports, the next option is usually fiber.

### Main Takeaway

Ethernet cabling combines:

- voltage signals;
- copper pairs;
- pinouts;
- twists;
- connectors;
- standards;
- testing.

Making one cable by hand helps connect the abstract networking model to the physical layer.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Ethernet cable | Copper network cable used to connect devices. |
| Cat5e | Common Ethernet cable category capable of gigabit Ethernet. |
| UTP | Unshielded Twisted Pair. |
| STP | Shielded Twisted Pair. |
| RJ45 | Common Ethernet connector. |
| Crimping tool | Tool used to attach RJ45 connector to cable. |
| Cable tester | Tool used to verify cable pinout/continuity. |
| EMI | Electromagnetic Interference. |
| Crosstalk | Interference between signals in nearby wires. |
| 10BASE-T | Older Ethernet standard using two pairs. |
| 100BASE-TX | Fast Ethernet standard using two pairs. |
| 1000BASE-T | Gigabit Ethernet over copper, uses all four pairs. |
| Straight-through cable | Cable with same pinout on both ends. |
| Crossover cable | Cable that swaps transmit/receive pairs. |
| Auto-MDIX | Feature that automatically adjusts transmit/receive pairs. |
| T568B | Common Ethernet wiring standard/pinout. |
| Sheath / jacket | Outer covering of the cable. |
| Twisted pair | Pair of copper wires twisted together to reduce interference. |

## Questions

### 1. Почему полезно уметь делать Ethernet cable, если можно купить готовый?

Потому что это помогает понять physical layer, termination, pinouts, testing and troubleshooting. Также это нужно для custom runs and structured cabling.

### 2. Какие tools нужны для basic Ethernet cable termination?

Ethernet cable, RJ45 connectors, crimping tool and cable tester.

### 3. Что означает UTP?

UTP means Unshielded Twisted Pair.

### 4. Что означает STP?

STP means Shielded Twisted Pair.

### 5. Зачем wires inside Ethernet cable twisted?

Twists help reduce EMI and crosstalk.

### 6. Сколько copper wires внутри standard Ethernet cable?

Внутри 8 copper wires, arranged as 4 twisted pairs.

### 7. Какие pair usage differences между 100BASE-TX и 1000BASE-T?

100BASE-TX uses two pairs, while 1000BASE-T uses all four pairs.

### 8. Что такое straight-through cable?

Straight-through cable has the same pinout on both ends and historically connects different device types like PC to switch.

### 9. Что такое crossover cable?

Crossover cable swaps transmit and receive pairs and historically connects similar devices like PC to PC or switch to switch.

### 10. Что делает Auto-MDIX?

Auto-MDIX automatically detects and adjusts transmit/receive pairs, making crossover cables less necessary with modern devices.

### 11. Какой T568B wire order?

White orange, orange, white green, blue, white blue, green, white brown, brown.

### 12. Что должен показать cable tester для good straight-through cable?

Pins should light in order 1 through 8 on both ends: 1->1, 2->2, 3->3 and so on.

### 13. Какова максимальная длина standard copper Ethernet run?

100 meters.

### 14. Что делать, если нужно подключение дальше 100 meters?

Рассматривать fiber or another appropriate network design instead of pushing copper beyond spec.

## What To Review Later

- UTP vs STP.
- EMI and crosstalk.
- T568B pinout.
- Straight-through vs crossover.
- Auto-MDIX.
- 10BASE-T, 100BASE-TX, 1000BASE-T pair usage.
- Cable testing and common termination failures.
- 100 meter copper Ethernet limit.
