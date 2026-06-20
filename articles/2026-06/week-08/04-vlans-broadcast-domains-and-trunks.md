# VLANs, Broadcast Domains, And Trunks

Source: закрытая страница курса  
Date added: 2026-06-20  
Related plan item: Week 8 / VLAN broadcast domains and trunking  
Tags: VLAN, broadcast domain, trunk port, 802.1Q, router-on-a-stick, segmentation
Language: Russian
Translation pair: articles-en/2026-06/week-08/04-vlans-broadcast-domains-and-trunks.md

## Кратко

VLAN существует не как fancy feature, а как ответ на реальные проблемы роста сети.

Когда в компании появляется больше devices, например IP phones, cameras, guest Wi-Fi и business systems, одна flat network быстро перестает быть удобной. Не хватает адресов, растет broadcast noise, сложнее защищать sensitive systems, сложнее понимать, где что находится.

VLAN, или Virtual LAN, позволяет взять один physical switch и разделить его на несколько logical networks.

Ключевая идея:

```text
Одна VLAN = один broadcast domain
Один broadcast domain = обычно одна IP subnet
Больше VLANs = больше separation и flexibility
```

VLAN дает две главные выгоды:

- scalability;
- security through segmentation.

## Почему VLANs Вообще Появляются

Представь, что в уже работающую сеть нужно добавить большой Voice over IP rollout.

До этого в сети были laptops, PCs, printers и обычные user devices. Теперь почти у каждого user появляется еще и IP phone.

Количество endpoints резко растет.

Это создает вопросы:

- хватит ли IP addresses;
- не станет ли broadcast domain слишком большим;
- нужно ли phones отделять от обычных data devices;
- как применить отдельные policies к voice traffic;
- как troubleshooting делать без хаоса.

Если оставить все в одной flat network, сеть может работать, но будет все менее управляемой.

VLANs решают это через logical separation.

## Broadcast Domain

Broadcast domain - это область сети, внутри которой broadcast traffic может распространяться.

Если device отправляет broadcast, например ARP request, switch floods этот frame внутри broadcast domain.

На обычном switch без VLAN segmentation все ports обычно находятся в одной default VLAN.

Это означает:

```text
Один switch
Одна default VLAN
Один broadcast domain
```

Если одно устройство отправляет broadcast, этот broadcast может уйти ко всем relevant ports внутри этой VLAN.

## VLAN Как Virtual Broadcast Domain

VLAN позволяет разделить switch на несколько broadcast domains.

Например:

```text
Ports 1-4  -> VLAN 10 Green
Ports 5-8  -> VLAN 20 Red
```

Теперь devices в VLAN 10 находятся в одном broadcast domain.

Devices в VLAN 20 находятся в другом broadcast domain.

Broadcast из VLAN 10 не уходит в VLAN 20. Broadcast из VLAN 20 не уходит в VLAN 10.

Логически это похоже на два отдельных switches внутри одного physical switch:

```text
Green talks to Green
Red talks to Red
Green does not directly talk to Red
```

Если нужно, чтобы Green и Red общались, понадобится routing.

## VLANs Масштабируются Между Switches

VLAN не обязана жить только на одном switch.

В реальной сети devices одной VLAN могут быть подключены к разным switches.

Например:

```text
Switch 1, port 1 -> VLAN 10
Switch 2, port 7 -> VLAN 10
```

Физически devices подключены к разным switches, но логически они могут быть в одной VLAN и одном broadcast domain.

Для этого switches должны передавать VLAN traffic между собой.

Здесь появляется trunk port.

## Trunk Port

Trunk port - это port, который переносит traffic нескольких VLANs.

Обычный access port обычно принадлежит одной VLAN:

```text
Access port -> VLAN 10 only
```

Trunk port может нести несколько VLANs:

```text
Trunk port -> VLAN 10, VLAN 20, VLAN 30, VLAN 99
```

Это нужно, когда switches соединяются между собой или когда switch подключается к router/firewall/Layer 3 device, который должен видеть несколько VLANs.

## 802.1Q Tagging

Когда frame идет через trunk, switch должен понимать, к какой VLAN этот frame относится.

Для этого используется VLAN tag.

Стандарт называется `802.1Q`.

Простая идея такая:

```text
Frame crosses trunk -> switch adds VLAN information
Next switch reads tag -> sends frame into the correct VLAN
```

`802.1Q` важен потому, что это industry standard. Это не только Cisco-specific механизм. Разные vendors могут поддерживать trunking через этот стандарт.

Без tagging receiving switch не знал бы, куда отнести traffic на trunk link.

## Две Главные Причины Использовать VLANs

### Scalability

Каждая VLAN обычно соответствует отдельной IP subnet.

Если появляется новая группа devices, можно создать для нее отдельную VLAN и subnet.

Например:

```text
VLAN 10 Data:   10.0.10.0/24
VLAN 20 Voice:  10.0.20.0/24
VLAN 30 Guest:  10.0.30.0/24
```

Так можно добавить IP phones, не запихивая их в тот же address space, где уже живут user laptops.

Это помогает:

- не исчерпать один subnet слишком быстро;
- планировать growth;
- разделять device types;
- легче документировать сеть.

### Security

VLANs дают segmentation.

Это не магическая security button, но это важная boundary.

Если phones живут в одной VLAN, laptops в другой, guest Wi-Fi в третьей, то эти groups не находятся в одном shared Layer 2 space.

Дальше можно применить policy:

```text
Guest VLAN -> Internet only
Voice VLAN -> Call servers
Data VLAN -> Internal services
Management VLAN -> Admin access only
```

Segmentation уменьшает exposure и помогает удерживать проблему внутри конкретной зоны.

## Но Как VLANs Общаются Между Собой?

VLANs разделяют traffic. Это хорошо.

Но иногда devices из разных VLANs должны общаться:

- users должны печатать на printers;
- phones должны добраться до call server;
- guest network должна выйти в internet;
- admin workstation должна управлять switches.

Для этого нужен routing.

VLANs работают на Layer 2, а communication между IP subnets требует Layer 3.

Варианты:

- router;
- Layer 3 switch;
- firewall.

## Router-On-A-Stick

Один распространенный вариант в небольших environments - router-on-a-stick.

Идея:

```text
Switch connects to router using one trunk link
Router creates subinterfaces
Each subinterface belongs to one VLAN
Each subinterface gets gateway IP for that VLAN
```

Например:

```text
Router subinterface for VLAN 10 -> 10.0.10.1
Router subinterface for VLAN 20 -> 10.0.20.1
Router subinterface for VLAN 30 -> 10.0.30.1
```

Для clients эти addresses становятся default gateways.

Traffic из VLAN 10 идет к router. Router решает, можно ли отправить его в VLAN 20, VLAN 30 или в internet.

Именно здесь появляется policy:

- allow;
- deny;
- inspect;
- translate through NAT;
- route onward.

## Как Это Связывает Предыдущие Темы

VLANs соединяются почти со всем, что уже было изучено:

- switching - ports помещаются в VLANs;
- subnetting - каждая VLAN получает свою IP subnet;
- routing - traffic между VLANs проходит через Layer 3;
- ACLs - policies контролируют доступ между VLANs;
- DHCP - каждая VLAN может иметь свой pool;
- NAT - selected VLANs могут выходить в internet;
- troubleshooting - нужно понимать, где Layer 2 boundary, а где Layer 3 boundary.

Поэтому VLANs могут ощущаться сложными не из-за самой идеи, а потому что они касаются сразу многих частей networking.

## Главный Вывод

VLAN позволяет carve physical network into multiple logical networks.

Один switch может стать несколькими logical broadcast domains.

Несколько switches могут переносить эти VLANs через trunk links.

`802.1Q` tagging помогает switches понимать, к какой VLAN относится traffic на trunk.

Routing нужен, когда traffic должен пройти между VLANs.

Если коротко:

```text
VLAN = logical separation
Trunk = carry multiple VLANs between devices
802.1Q = VLAN tag on trunk links
Router/L3 device = communication between VLANs
```

VLANs дают сети room to grow и room to protect what matters.

