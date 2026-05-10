# Why This Skill is Important

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Physical and logical connection types  
Tags: cabling, connections, copper, fiber, wireless, standards, capacity, distance, network design

## Summary

Перед настройкой IP addresses, VLANs или routing нужно сделать более базовую вещь: правильно соединить устройства. Connection type - это design choice. Разные media имеют разные speed, distance, capacity и tradeoffs.

Главная мысль: сеть не появляется сама. Нужно знать, что подключать, чем подключать и почему этот выбор подходит задаче.

## Key Points

- Networks require physical or wireless connections.
- Before configuration, devices must be connected correctly.
- Cable type is not just a minor detail.
- Wrong cabling can create performance and reliability problems.
- Copper, fiber and wireless solve different problems.
- Category 3 cabling is too old for modern Ethernet demands.
- Capacity means how much data a connection can carry.
- Distance limit matters when planning physical layout.
- Copper is common for endpoints and short building runs.
- Fiber is useful for distance and high bandwidth.
- Wireless is flexible, but has tradeoffs in coverage, interference and reliability.
- Real design asks not only "will it work today?", but "will it still work after growth?".

## Notes

### Why Connections Matter

NetworkChuck Coffee depends on connectivity for:

- POS systems;
- guest WiFi;
- office systems;
- security cameras;
- VoIP phones;
- wireless access points;
- servers;
- future locations.

Если connection выбран плохо, сеть может сначала "как-то работать", а потом развалиться под нагрузкой.

### Cable Is Not Just Cable

Разные connection types имеют разные характеристики:

- speed;
- distance;
- cost;
- reliability;
- power support;
- installation complexity;
- future capacity.

Например, old Category 3 cabling не подходит для современных требований. Если не понимать cabling categories, можно попытаться построить новую сеть на старой физической базе и получить bottleneck.

### Think Like a Builder

Нужно видеть connection как часть дизайна:

```text
Endpoint nearby -> often copper
Long distance / high speed -> often fiber
Mobility / convenience -> wireless
Power over cable needed -> copper with PoE
```

Это не cable trivia. Это практическое проектирование.

## Commands / Terms

```text
Capacity - сколько данных connection может передать
Medium / media - физическая или беспроводная среда передачи
Copper - медный Ethernet cable
Fiber - fiber optic cabling
Wireless - передача по radio
PoE - Power over Ethernet
```

## Questions

### Почему нельзя думать "cable is cable"?

Потому что разные cables поддерживают разные speeds, distances и use cases.

### Что нужно оценивать при выборе connection?

Type, capacity, distance, tradeoffs и future growth.

### Почему это важно для NetworkChuck Coffee?

Потому что POS, WiFi, cameras and phones зависят от надежной физической и беспроводной инфраструктуры.

## What To Review Later

- Copper cabling categories.
- Fiber single mode vs multimode.
- Wireless standards.
- PoE requirements.
- Structured cabling design.
