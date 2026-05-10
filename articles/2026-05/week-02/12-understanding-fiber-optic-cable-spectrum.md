# Understanding Fiber Optic Cable Spectrum

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Fiber cabling basics  
Tags: fiber, single mode, multimode, sfp, transceiver, bandwidth, distance, copper, poe, uplink

## Summary

Fiber optic cable - это отдельный мир по сравнению с copper. Copper передает electrical signals и обычно ограничен 100 meters. Fiber передает light, поэтому выигрывает на distance, bandwidth и long-haul connections.

Главная мысль: copper отлично подходит для nearby endpoints, а fiber нужен там, где сеть должна пройти далеко или передать много данных.

## Key Points

- Fiber uses light instead of electricity.
- Copper Ethernet over UTP обычно ограничен около 100 meters.
- Fiber can go much farther than copper.
- Fiber используют для buildings, campuses, cities, data centers and backbone links.
- Single mode fiber обычно лучше для long distance and high bandwidth.
- Multimode fiber обычно используют для shorter runs inside buildings or campuses.
- Single mode historically cost more, but price gap may be smaller now.
- Fiber connects to switches through SFP/SFP+ modules or similar transceivers.
- SFP means Small Form-factor Pluggable.
- Нужно match switch, module, fiber type, connector type, speed and distance.
- Fiber can support 25G, 40G, 100G and beyond depending on equipment.
- Fiber does not carry PoE like copper.
- Copper remains important for phones, APs, cameras and endpoints that need power.
- Real networks usually use both copper and fiber.

## Notes

### Why Fiber Exists

Copper is familiar and practical, but it has limits:

- distance;
- electrical interference;
- high-speed scaling;
- long campus or city links.

Fiber solves many of those problems because it carries light through glass or plastic core.

### Single Mode vs Multimode

Simple comparison:

```text
Single mode -> longer distance, higher bandwidth, smaller core
Multimode   -> shorter distance, common inside buildings/campuses
```

Для NetworkChuck Coffee:

- closet to closet in same building: multimode may be fine;
- building to building or serious growth: single mode may be better;
- ISP or long-haul connection: often single mode.

### SFP and Transceivers

Fiber cable обычно не подключается напрямую в обычный RJ45 port.

Switch имеет SFP slot:

```text
Switch SFP slot -> SFP module -> Fiber cable
```

SFP module задает, какой type connection будет у порта.

Нужно проверить:

- speed;
- fiber type;
- connector;
- distance rating;
- compatibility with switch;
- single mode or multimode.

### Fiber Limitation: No PoE

Fiber не питает endpoint devices как copper with PoE.

Поэтому:

- backbone/uplink/long run -> fiber;
- phones/APs/cameras/endpoints needing power -> copper with PoE.

Это не fiber vs copper. Это правильный инструмент для правильной задачи.

## Commands / Terms

```text
Fiber - cable that carries data as light
Single mode - long-distance fiber type
Multimode - shorter-distance fiber type
SFP - Small Form-factor Pluggable
Transceiver - module that sends/receives optical/electrical signal
PoE - Power over Ethernet
```

## Questions

### Почему fiber лучше для distance?

Потому что он передает light и не страдает от тех же electrical limits, что copper.

### Когда использовать single mode?

Для long distance, high bandwidth и links с запасом на рост.

### Когда multimode может быть нормальным выбором?

Для shorter runs внутри здания или campus.

### Почему fiber не заменяет copper везде?

Потому что fiber не дает PoE, а copper дешевле и удобнее для endpoints.

## What To Review Later

- LC connectors.
- SFP vs SFP+ vs QSFP.
- Fiber wavelengths.
- Duplex fiber.
- Optical budgets.
