# Copper Cabling Standards and Characteristics

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Copper cabling  
Tags: copper, ethernet, utp, rj45, t568b, cat5e, cat6, cat6a, cat8, distance, cabling

## Summary

Copper Ethernet никуда не исчезает. Он дешевый, надежный, удобный для endpoints и до сих пор используется повсюду: POS terminals, office computers, phones, access points, printers, cameras and wall jacks.

Главная мысль: copper cabling передает data как electrical pulses по twisted pairs, обычно ограничен 100 meters, использует RJ45 connectors и требует правильной wiring standard вроде T568B.

## Key Points

- Copper Ethernet остается стандартным выбором для огромного числа устройств.
- Внутри cable находятся 8 copper wires.
- Эти wires организованы в 4 twisted pairs.
- Twists помогают снижать interference and crosstalk.
- UTP means Unshielded Twisted Pair.
- Copper передает data как electrical signals.
- Fiber передает data как light.
- Типичный limit для twisted-pair Ethernet - 100 meters.
- Если нужно дальше, используют switch для regeneration или переходят на fiber.
- RJ45 - привычный connector для Ethernet ports.
- RJ11 похож, но меньше и используется для phone systems.
- T568B задает порядок wires в connector.
- Нельзя freestyle wiring order, потому что pairs and twists важны для signal integrity.
- Cat5e supports 1 Gbps at 100 meters.
- Cat6 can support 10 Gbps up to about 55 meters.
- Cat6a supports 10 Gbps at 100 meters.
- Cat8 supports 40 Gbps up to about 30 meters.

## Notes

### What's Inside

Copper Ethernet cable обычно содержит:

```text
8 wires = 4 twisted pairs
```

Twisted pairs помогают бороться с:

- electromagnetic interference;
- crosstalk;
- signal degradation.

`UTP` означает, что пары скручены, но дополнительного metallic shielding нет.

### Distance Limit

Ключевое число:

```text
100 meters / 328 feet
```

Это practical design limit для обычного twisted-pair Ethernet run.

Не стоит проектировать кабельный run прямо впритык к 100 meters. Patch panels, wall jacks, bends и неточные измерения быстро съедают запас.

### RJ45 and T568B

RJ45 - connector, который большинство людей узнают как "Ethernet plug".

T568B - common wiring standard.

Order:

```text
White orange
Orange
White green
Blue
White blue
Green
White brown
Brown
```

Порядок важен, потому что Ethernet relies on specific pairs.

### Cable Categories

Практическая таблица:

```text
Cat5e  -> 1 Gbps / 100 m
Cat6   -> 10 Gbps / ~55 m
Cat6a  -> 10 Gbps / 100 m
Cat8   -> 40 Gbps / ~30 m
```

Cat5e до сих пор очень часто встречается. Для новых building runs с запасом на будущее Cat6a часто выглядит сильнее. Для high-speed backbone иногда логичнее использовать fiber.

## Commands / Terms

```text
UTP - Unshielded Twisted Pair
RJ45 - Ethernet connector
RJ11 - smaller phone connector
T568B - wiring pinout standard
Cat5e/Cat6/Cat6a/Cat8 - copper cable categories
```

## Questions

### Почему pairs twisted?

Чтобы снижать interference and crosstalk.

### Какой типичный limit copper Ethernet?

Около 100 meters.

### Почему нельзя просто придумать свой порядок wires?

Потому что wiring standard сохраняет правильные pairs и signal integrity.

### Когда стоит подумать о fiber вместо copper?

Когда нужны long distance, very high bandwidth или backbone/uplink connections.

## What To Review Later

- T568A vs T568B.
- Shielded vs unshielded cable.
- Patch panels and structured cabling.
- Cat6 vs Cat6a deployment.
- Fiber uplinks.
