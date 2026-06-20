# Native VLAN And Management Traffic

Source: закрытая страница курса  
Date added: 2026-06-20  
Related plan item: Week 8 / Native VLAN and trunk behavior  
Tags: native VLAN, VLAN, trunking, 802.1Q, management VLAN, untagged traffic, VLAN mismatch
Language: Russian
Translation pair: articles-en/2026-06/week-08/09-native-vlan-and-management-traffic.md

## Кратко

Native VLAN отвечает на один конкретный вопрос:

```text
Если traffic пришел на trunk port без VLAN tag, в какую VLAN его поместить?
```

Trunk port переносит traffic нескольких VLANs. Обычно frames на trunk имеют 802.1Q tag, чтобы receiving switch понимал, к какой VLAN они относятся.

Но если frame приходит untagged, switch все равно должен куда-то его отнести. Native VLAN и есть этот default bucket для untagged traffic на trunk.

Главные идеи:

- native VLAN используется для untagged traffic на trunk;
- исторически это помогало работать с устройствами, которые не умели tagging;
- в современных сетях native VLAN часто связана с management traffic;
- native VLAN не должна оставаться случайной или default;
- обе стороны trunk должны иметь одинаковую native VLAN;
- native VLAN mismatch может создать traffic leak и серьезные troubleshooting problems.

## Зачем Вообще Нужна Native VLAN

802.1Q trunk обычно переносит tagged traffic.

Tagged frame содержит VLAN information:

```text
Frame + VLAN tag -> switch knows the VLAN
```

Но возможна ситуация, когда frame пришел на trunk без tag:

```text
Frame without VLAN tag -> ?
```

Switch не может просто игнорировать саму идею VLAN. Ему нужно решить, куда положить этот frame.

Ответ:

```text
Untagged traffic on trunk -> native VLAN
```

По умолчанию на Cisco часто native VLAN - VLAN 1, но в нормальном design лучше выбирать ее осознанно.

## Историческая Причина

Исторически native VLAN была полезна в средах, где не все устройства умели tagging.

Например, hubs.

Hub - это простое устройство, которое не понимает:

- MAC address table;
- VLANs;
- tagging;
- switching logic.

Он просто повторяет electrical signal out every port.

Если такой legacy device находился рядом с trunk connection и отправлял untagged traffic, switch должен был понять, к какой VLAN этот traffic относится.

Native VLAN давала этот answer.

Сегодня hubs почти не встречаются в нормальных designs, но сама концепция native VLAN осталась.

## Почему Native VLAN Все Еще Важна

Native VLAN не исчезла, потому что modern infrastructure все еще иногда работает с untagged traffic.

Типичные examples:

- hypervisor host с trunk link к switch;
- wireless access point, который несет несколько SSIDs/VLANs;
- infrastructure device, которому нужен management access;
- некоторые appliances, где production traffic tagged, а management traffic untagged.

То есть native VLAN часто используется как management path.

## Пример С Virtualization Host

Представь physical server, на котором работает virtualization.

На нем могут быть virtual machines в разных VLANs:

```text
Accounting VM -> VLAN 10
Dev VM        -> VLAN 20
Security VM   -> VLAN 30
```

Switch port к server может быть trunk, чтобы все эти VLANs проходили по одному physical link.

Но сам physical host тоже нужно manage:

- login to hypervisor;
- monitoring;
- updates;
- troubleshooting;
- backup agent;
- management API.

Management traffic для самого host может идти через native VLAN, если он отправляется untagged.

## Пример С Wireless Access Point

Wireless AP может транслировать несколько SSIDs:

```text
Staff Wi-Fi -> VLAN 10
Guest Wi-Fi -> VLAN 20
IoT Wi-Fi   -> VLAN 30
```

Switch port к AP часто работает как trunk.

Но сам AP тоже нужно manage:

- зайти в controller;
- получить config;
- отправить logs;
- скачать firmware;
- отвечать на monitoring.

Management network для AP может быть native VLAN.

Так AP переносит tagged client traffic для SSIDs, но сам management path может быть untagged/native.

## Management VLAN

Management VLAN - это VLAN, которая используется для административного доступа к infrastructure devices.

В нее могут входить:

- switches;
- routers;
- access points;
- hypervisors;
- firewalls;
- controllers;
- monitoring appliances.

Management VLAN не должна быть доступна всем users.

Если attacker получает доступ к management VLAN, он может оказаться не просто "в сети", а рядом с control plane устройств, которые эту сеть обслуживают.

Поэтому management VLAN должна быть:

- deliberate;
- documented;
- restricted;
- monitored;
- protected ACLs/firewall rules;
- не default VLAN 1 без причины.

## VLAN И Subnet

В practical design обычно используют mental model:

```text
One VLAN = one IP subnet
```

Технически бывают более сложные designs, но для CCNA-level и нормальной operational clarity это лучший baseline.

Если native VLAN используется для management, она обычно имеет свою management subnet.

Например:

```text
VLAN 99 Management: 10.0.99.0/24
Gateway:            10.0.99.1
```

## Native VLAN Mismatch

Самая опасная ошибка с native VLAN - mismatch между сторонами trunk.

Пример:

```text
Switch A trunk native VLAN: 99
Switch B trunk native VLAN: 1
```

Теперь untagged traffic интерпретируется по-разному на разных концах link.

Это может привести к:

- traffic leaking between VLANs;
- странным broadcast problems;
- security issues;
- connectivity issues;
- очень неприятному troubleshooting.

На Cisco switches можно увидеть warnings о native VLAN mismatch, но если не смотреть logs или работать слишком быстро, предупреждение легко пропустить.

## Почему Mismatch Опасен

Представь, что Switch A считает untagged traffic частью VLAN 99.

Switch B считает untagged traffic частью VLAN 1.

Тогда один и тот же untagged traffic может попасть в разные logical networks на разных сторонах trunk.

Это ломает идею clean boundaries.

Если guest network, management network или user network начинают пересекаться не там, где нужно, сеть становится непредсказуемой.

## Практические Правила

### Не Оставляй Native VLAN На Default Без Причины

VLAN 1 часто используется по умолчанию. Это не значит, что ее стоит использовать как management/native VLAN в production.

Лучше выбрать отдельную VLAN:

```text
VLAN 99 Management
```

И задокументировать ее.

### Match Native VLAN На Обеих Сторонах Trunk

На обоих ends trunk native VLAN должна совпадать.

Например:

```text
Switch A: native VLAN 99
Switch B: native VLAN 99
```

### Ограничь Доступ К Management VLAN

Management VLAN должна быть доступна только administrators и нужным systems.

Используй:

- ACLs;
- firewall policies;
- jump hosts;
- monitoring allowlists;
- secure management protocols;
- strong authentication.

### Проверяй Trunk State

Полезная команда:

```text
show interfaces trunk
```

Она помогает увидеть native VLAN и allowed VLANs на trunk.

Также смотри logs, особенно если switch сообщает о native VLAN mismatch.

## Что Нужно Запомнить

Три главных пункта:

1. Native VLAN - это VLAN, куда попадает untagged traffic на trunk port.
2. В modern networks native VLAN часто используется для management traffic.
3. Native VLAN должна совпадать на обеих сторонах trunk.

Если native VLAN настроена небрежно, могут появиться traffic leaks, management exposure и очень странные сетевые симптомы.

## Главный Вывод

Native VLAN может казаться маленькой исторической деталью, но последствия ее неправильной настройки большие.

Она отвечает за untagged traffic на trunk.

Она часто связана с management access.

Она должна быть deliberate, documented и одинаковой на обеих сторонах trunk.

Короткая памятка:

```text
Native VLAN = default VLAN for untagged traffic on a trunk
Management VLAN = controlled admin path for infrastructure devices
Native VLAN mismatch = trouble
```

Если настроить это аккуратно, VLAN design остается clean, predictable и secure.

