# EtherChannel Deployment Checklist

Source: закрытая страница курса  
Date added: 2026-07-03  
Related plan item: Week 10 / EtherChannel deployment checklist  
Tags: EtherChannel, LACP, port-channel, STP, trunk, VLAN, load balancing
Language: Russian
Translation pair: articles-en/2026-07/week-10/06-etherchannel-deployment-checklist.md

## Summary

- EtherChannel превращает redundant links из пассивного резерва в активную полезную bandwidth.
- Перед созданием bundle нужно проверить, что member interfaces полностью совпадают.
- В production лучше использовать LACP `active` на обеих сторонах.
- После настройки нужно проверить и EtherChannel, и STP, и load balancing behavior.

## Key Points

- STP блокирует лишние links не потому, что он сломан, а потому что защищает сеть от loops.
- EtherChannel работает с STP: он меняет несколько физических links на один logical Port-Channel.
- Member ports должны совпадать по speed, duplex, trunking и VLAN settings.
- Команда `channel-group 1 mode active` создает LACP-based bundle.
- `show etherchannel summary` и `show spanning-tree` подтверждают, что bundle работает и виден STP как один interface.

## Notes

Redundant links полезны, пока STP не блокирует один из них. Но STP делает это правильно: его задача - не максимальная bandwidth, а loop-free Layer 2 topology. Если два независимых links между одними switches будут forwarding одновременно, можно получить loop и broadcast storm.

EtherChannel решает эту практическую боль. Он объединяет несколько физических interfaces в один logical connection - Port-Channel. Для STP это уже не два конкурирующих пути, а один logical interface. Поэтому bundle может forwarding как единое целое, а physical member links остаются активными внутри него.

Главная идея:

> Один blocked link безопасен. Один bundled link безопасен и полезен.

Перед настройкой EtherChannel нельзя сразу вводить `channel-group`. Сначала нужно убедиться, что будущие member ports действительно одинаковые. Большинство проблем с EtherChannel начинаются не с LACP, а с того, что interfaces не являются "близнецами".

Проверить нужно:

- speed;
- duplex;
- trunk или access mode;
- allowed VLAN list;
- native VLAN;
- negotiation settings;
- отсутствие старых channel/protocol remnants;
- одинаковый Layer 2 purpose на обеих сторонах.

Особенно внимательно нужно смотреть на trunk behavior. Если один member port carries VLAN 10,20,30, а другой - только VLAN 10, bundle станет источником странного поведения. EtherChannel требует consistency.

Рабочий deployment flow:

1. Проверить interfaces на обеих сторонах.

```text
Switch# show interfaces trunk
Switch# show running-config interface fa0/1
Switch# show running-config interface fa0/2
```

2. Настроить member ports через interface range.

```text
Switch(config)# interface range fa0/1 - 2
Switch(config-if-range)# channel-group 1 mode active
```

3. Повторить matching configuration на другой стороне.

```text
Switch(config)# interface range fa0/1 - 2
Switch(config-if-range)# channel-group 1 mode active
```

4. Настраивать trunk и VLANs на Port-Channel interface.

```text
Switch(config)# interface port-channel 1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20,30
```

5. Проверить EtherChannel.

```text
Switch# show etherchannel summary
```

6. Проверить STP.

```text
Switch# show spanning-tree
```

До создания EtherChannel STP видел отдельные physical interfaces и мог блокировать один из них. После создания bundle STP должен видеть `Port-channel1` как один logical interface.

Если EtherChannel сначала показывает standalone state, это не всегда проблема. Часто это значит, что вторая сторона еще не настроена. Когда matching configuration появляется на другой стороне, LACP формирует bundle, и member ports становятся active participants.

После basic verification стоит проверить load balancing method:

```text
Switch# show etherchannel load-balance
```

Если switch использует, например, source MAC only, распределение может быть lopsided. Для сети, где много clients общаются с разными servers, вариант вроде source-destination MAC может дать более полезный hash:

```text
Switch(config)# port-channel load-balance src-dst-mac
```

Важно помнить: EtherChannel не делит один conversation packet-by-packet по всем links. Это привело бы к out-of-order packets. Вместо этого switch hashes flows: один conversation обычно держится одного member link, а множество conversations распределяются по bundle.

В NetworkChuck Coffee это полезно именно потому, что traffic разнообразный: POS systems, guest Wi-Fi, cameras, printers, office laptops, back-office systems. Чем больше разных source/destination pairs, тем больше шансов, что load balancing будет эффективным.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `channel-group 1 mode active` | Добавляет interfaces в group 1 и использует LACP active mode. |
| `interface port-channel 1` | Открывает logical interface, который представляет EtherChannel bundle. |
| `show etherchannel summary` | Проверяет group, protocol, Port-Channel state и active member ports. |
| `show spanning-tree` | Показывает, видит ли STP Port-Channel как один logical interface. |
| `show etherchannel load-balance` | Показывает текущий load balancing method. |
| `port-channel load-balance src-dst-mac` | Настраивает hashing по source и destination MAC addresses. |
| Standalone state | Состояние, когда Port-Channel еще не сформирован с другой стороной. |

## Questions

### 1. Почему EtherChannel не заменяет STP?

Answer: EtherChannel меняет несколько физических links на один logical interface, но STP все равно нужен для loop prevention в общей Layer 2 topology.

### 2. Что нужно проверить перед созданием EtherChannel?

Answer: Speed, duplex, trunk/access mode, allowed VLANs, native VLAN и negotiation settings на всех member interfaces и на обеих сторонах.

### 3. Почему лучше использовать LACP active?

Answer: LACP является стандартным negotiated protocol, а `active` явно пытается сформировать channel. `active` на обеих сторонах уменьшает количество лишних решений.

### 4. Что должно измениться в выводе STP после создания EtherChannel?

Answer: STP должен видеть Port-Channel как один logical interface вместо нескольких отдельных physical links.

### 5. Почему load balancing может быть неравномерным?

Answer: EtherChannel использует hash-based flow distribution. Если выбранные поля мало отличаются между flows, много traffic может попасть на один member link.

## What To Review Later

- Как читать `show etherchannel summary`.
- Почему trunk settings нужно держать на Port-Channel interface.
- Какие LACP states бывают при проблемах bundle.
- Как выбирать load balancing algorithm под traffic pattern.
