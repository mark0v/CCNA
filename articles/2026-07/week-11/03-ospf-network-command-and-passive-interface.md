# OSPF Network Command And Passive Interface

Source: закрытая страница курса  
Date added: 2026-07-11  
Related plan item: Week 11 / OSPF network command and passive interface  
Tags: OSPF, network command, wildcard mask, passive interface, hello packets, routing protocols
Language: Russian
Translation pair: articles-en/2026-07/week-11/03-ospf-network-command-and-passive-interface.md

## Summary

- Команда `network` в OSPF делает две вещи одновременно.
- Она выбирает interfaces, где должен работать OSPF, и advertising connected networks с этих interfaces.
- Если interface нужно advertising, но не нужно neighbor discovery, используется `passive-interface`.
- Wildcard mask - это inverse subnet mask, который помогает match interfaces.
- Важно помнить: `network` command mainly matches interfaces, а не вручную описывает точную route advertisement.

## Key Points

- OSPF `network` command запускает OSPF на matching interface.
- Matching interface начинает отправлять OSPF hello packets.
- Connected network этого interface advertising другим OSPF routers.
- `passive-interface` выключает hello packets, но не выключает advertisement connected network.
- Wildcard mask считается как `255.255.255.255 - subnet mask`.

## Notes

Команда `network` выглядит простой, но именно она часто ломает понимание OSPF. Кажется, что она просто говорит router-у: "advertise this network". На самом деле она делает больше.

В OSPF команда `network` выполняет две связанные задачи:

1. Находит interfaces, которые должны участвовать в OSPF.
2. Advertising connected networks с этих interfaces в OSPF routing domain.

Это значит, что после `network` command OSPF не только сообщает другим routers о connected subnet. Он еще и запускает OSPF behavior на matching interface: отправляет hello packets и пытается найти neighbors.

## The Real Meaning Of Network

Представим router NetworkChuck Coffee с двумя VLAN:

- admin VLAN для servers, management и backups;
- patron VLAN для guest devices и BYOD traffic.

Если включить OSPF для admin subnet, router начнет advertising эту network другим sites. Это полезно: Fallout Shelter или другой branch сможет узнать, как reach admin systems.

Но есть второй эффект. OSPF начнет отправлять hello packets на interface, который matched by `network` command. Hello packets нужны, чтобы искать и поддерживать OSPF neighbor relationships.

Проблема: на admin VLAN может не быть другого router, с которым нужно стать OSPF neighbor. Тогда hello packets там лишние.

Ментальная модель:

> `network` command не только говорит "advertise this". Она еще говорит "run OSPF on the matching interface".

## Passive Interface

Если нужно advertising subnet, но не нужно формировать OSPF neighbors на этом segment, используется `passive-interface`.

Passive interface делает важную вещь:

- stopping OSPF hello packets на interface;
- preventing neighbor relationships на этом interface;
- still advertising connected network в OSPF.

Это особенно полезно для user-facing или server-facing segments. Например, admin VLAN нужно advertising, чтобы другие sites знали route. Но OSPF neighbors на этом VLAN не нужны.

Пример:

```text
router ospf 1
 network 10.0.18.0 0.0.0.31 area 0
 passive-interface g0/0.18
```

В production часто используют подход "passive by default":

```text
router ospf 1
 passive-interface default
 no passive-interface g0/1
```

Идея простая: все interfaces passive, кроме тех, где действительно должен быть OSPF neighbor. Это уменьшает noise, снижает attack surface и делает configuration более предсказуемой.

Security angle тоже важен. Если OSPF включен на user-facing segment и interface не passive, rogue device может попытаться стать OSPF neighbor. Это уже risk: device может получить routing information или попытаться повлиять на topology.

## Wildcard Mask

OSPF `network` command в классическом Cisco syntax использует wildcard mask. Это inverse subnet mask.

Формула:

```text
255.255.255.255 - subnet mask = wildcard mask
```

Пример:

| Subnet mask | Prefix | Wildcard mask |
| --- | --- | --- |
| `255.255.255.0` | `/24` | `0.0.0.255` |
| `255.255.255.224` | `/27` | `0.0.0.31` |
| `255.255.255.252` | `/30` | `0.0.0.3` |
| `255.255.255.255` | `/32` | `0.0.0.0` |

Для `/27` subnet mask `255.255.255.224`. Последний octet wildcard: `255 - 224 = 31`, значит wildcard `0.0.0.31`.

## Matching Interface, Not Defining Route

Самая важная деталь: `network` command не говорит OSPF "advertise exactly this IP and wildcard as route". Она используется для matching interfaces.

Когда OSPF находит matching interface, он смотрит на real IP configuration этого interface и advertising actual connected network.

Поэтому можно match exact interface IP через wildcard `0.0.0.0`:

```text
router ospf 1
 network 10.0.18.1 0.0.0.0 area 0
```

Если interface имеет IP `10.0.18.1/27`, OSPF match this exact interface. После этого он advertising actual connected subnet, например `10.0.18.0/27`, а не только host route `10.0.18.1/32`.

Это объясняет, почему `network` command лучше воспринимать как "I choose this interface". После выбора interface происходят два эффекта:

- OSPF runs on that interface;
- connected network is advertised.

## Practical Checklist

Перед включением OSPF через `network` command:

- определить, какие interfaces должны form OSPF neighbors;
- определить, какие connected networks нужно advertise;
- сделать user-facing/server-facing interfaces passive;
- проверить wildcard mask;
- после настройки проверить neighbors and routes.

Полезные проверки:

```text
show ip ospf neighbor
show ip protocols
show ip route ospf
show running-config | section router ospf
```

Главный takeaway: `network` command в OSPF не просто advertising command. Это interface selection command with route advertisement side effect. Если понять это, OSPF configuration становится намного логичнее.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `network 10.0.18.0 0.0.0.31 area 0` | Matches interfaces in that range and enables OSPF in area 0. |
| `network 10.0.18.1 0.0.0.0 area 0` | Matches one exact interface IP. |
| `passive-interface g0/0.18` | Stops OSPF hellos on that interface while still advertising the connected network. |
| `passive-interface default` | Makes all OSPF interfaces passive by default. |
| `no passive-interface g0/1` | Allows OSPF neighbor formation on a specific interface. |
| Wildcard mask | Inverse subnet mask used by Cisco matching logic. |
| Hello packet | OSPF packet used to discover and maintain neighbors. |

## Questions

### 1. Какие две вещи делает OSPF `network` command?

Answer: Она выбирает interfaces, где будет работать OSPF, и advertising connected networks с этих interfaces.

### 2. Зачем нужен `passive-interface`?

Answer: Чтобы advertising connected network, но не отправлять OSPF hello packets и не формировать neighbors на этом interface.

### 3. Почему passive interfaces полезны для security?

Answer: Они не позволяют user-facing segment стать местом, где rogue device может попытаться сформировать OSPF neighbor relationship.

### 4. Как посчитать wildcard mask для `/27`?

Answer: `/27` это `255.255.255.224`; `255 - 224 = 31`, значит wildcard `0.0.0.31`.

### 5. Почему `network 10.0.18.1 0.0.0.0 area 0` не advertising только host route?

Answer: Потому что command matches exact interface IP. После match OSPF advertising actual connected network этого interface.

## What To Review Later

- OSPF hello packets and neighbor formation.
- Difference between interface matching and route advertisement.
- Common wildcard masks.
- `passive-interface default` production pattern.
- OSPF `show` commands for verification.
