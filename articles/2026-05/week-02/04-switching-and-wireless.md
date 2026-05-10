# Switching & Wireless

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / LAN switching and wireless  
Tags: switch, wireless, access point, lan, wifi, ethernet, antennas, coverage, directional antenna

## Summary

LAN в NetworkChuck Coffee держится в основном на двух устройствах: `switch` и `wireless access point`. Switch соединяет проводные устройства внутри локальной сети, а access point расширяет эту же сеть в WiFi для телефонов, ноутбуков, планшетов и гостевых устройств.

Главная мысль: WiFi не живет отдельно от проводной сети. Обычно AP подключен кабелем обратно в switch, поэтому качество беспроводной сети зависит от проводной инфраструктуры под ней.

## Key Points

- Switch соединяет проводные устройства в LAN.
- Порты switch также называют interfaces.
- В бизнес-сети лучше использовать нормальные управляемые switches в network closet, а не случайные маленькие desk switches.
- Desk switches добавляют точки отказа и усложняют troubleshooting.
- Типичные офисные switches часто имеют 24 или 48 портов.
- Обычный Ethernet-кабель ограничен примерно 328 feet / 100 meters.
- Wireless access point расширяет проводную LAN в WiFi.
- AP обычно подключается к switch.
- Wireless clients попадают в LAN через AP.
- Antennas влияют на форму зоны покрытия.
- Omnidirectional antenna распространяет сигнал широко вокруг точки.
- Directional antenna фокусирует сигнал в одном направлении.
- Directional wireless иногда используют для связи между зданиями.

## Notes

### LAN Foundation

В кофейне к сети подключается много разных устройств:

- registers;
- printers;
- laptops;
- tablets;
- cameras;
- phones;
- wireless client devices;
- office systems.

Часть устройств подключается кабелем. Часть подключается по WiFi. Но чаще всего все они все равно сходятся в одну проводную основу.

```text
Switches + wireless access points
```

### Switch

Switch - это центральная точка для проводных устройств внутри LAN.

Обычно switches находятся в:

- network closet;
- rack;
- cabinet;
- MDF/IDF.

Каждый endpoint подключается в порт switch через Ethernet cable.

```text
Endpoint -> Ethernet cable -> Switch
```

### Почему не стоит ставить случайные mini-switches

Маленький unmanaged switch под столом кажется удобным решением, когда "не хватает портов". Но в бизнес-сети это быстро превращается в проблему.

Он добавляет:

- еще один блок питания;
- еще одну точку отказа;
- неизвестный участок топологии;
- лишнюю сложность при troubleshooting.

Лучше решать нехватку портов через нормальную кабельную инфраструктуру и управляемые switches.

### Wireless Access Point

AP берет проводную сеть и делает ее доступной по WiFi.

Важно: AP не создает магическую отдельную сеть сам по себе. Он обычно подключается обратно в switch.

```text
Wireless client -> AP -> Switch -> LAN resources
```

Если switch, кабель или uplink работают плохо, WiFi тоже будет страдать.

### Antennas and Coverage

Антенны формируют зону покрытия.

`Omnidirectional` антенна раздает сигнал широко вокруг AP. Это типичный вариант для покрытия помещения.

`Directional` антенна фокусирует сигнал в одном направлении. Такой подход может помочь, если нужно дострелить WiFi между зданиями или в конкретную удаленную зону.

## Commands / Terms

```text
LAN - Local Area Network
AP - Access Point
Interface - порт устройства
Omnidirectional antenna - широкая зона покрытия
Directional antenna - направленная зона покрытия
100 meters / 328 feet - типичный предел copper Ethernet run
```

## Questions

### Что делает switch?

Соединяет проводные устройства внутри LAN.

### Что делает wireless access point?

Подключается к проводной сети и дает wireless clients доступ к LAN по WiFi.

### Почему WiFi зависит от проводной сети?

Потому что AP обычно подключен кабелем в switch. Wireless часть является расширением проводной LAN.

### Почему random desk switches опасны в бизнес-сети?

Они создают дополнительные точки отказа и делают сеть менее понятной для поддержки.

## What To Review Later

- Difference between switch and hub.
- Managed vs unmanaged switch.
- AP placement and wireless coverage planning.
- VLANs for guest WiFi and internal devices.
- Directional wireless links between buildings.
