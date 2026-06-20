# Router-On-A-Stick Inter-VLAN Routing

Source: закрытая страница курса  
Date added: 2026-06-20  
Related plan item: Week 8 / Inter-VLAN routing with router-on-a-stick  
Tags: VLAN, inter-VLAN routing, router-on-a-stick, subinterface, 802.1Q, DHCP, default gateway
Language: Russian
Translation pair: articles-en/2026-06/week-08/07-router-on-a-stick-inter-vlan-routing.md

## Кратко

VLANs создаются для separation. Но рано или поздно devices из разных VLANs должны куда-то ходить: к server, в internet, к shared service или к другой business system.

Проблема простая:

```text
VLAN 10 = отдельная network
VLAN 20 = отдельная network
Different networks need routing
```

Inter-VLAN routing - это routing между VLANs.

Один из классических способов сделать это в небольшой сети - router-on-a-stick, или ROAS.

Главные идеи:

- каждая VLAN является отдельной IP network;
- devices в разных VLANs не общаются напрямую на Layer 2;
- router или Layer 3 device нужен для traffic между VLANs;
- router-on-a-stick использует один physical router interface;
- на router создаются subinterfaces;
- каждая subinterface привязана к VLAN через `encapsulation dot1Q`;
- IP address subinterface становится default gateway для этой VLAN;
- switch port к router должен быть trunk.

## Почему VLANs Не Говорят Друг С Другом

VLAN - это отдельный broadcast domain и обычно отдельная subnet.

Например:

```text
VLAN 10 Admin:   10.0.18.0/27
VLAN 20 Patron:  10.0.18.32/27
```

Device из VLAN 10 видит свою network как local.

Device из VLAN 20 видит свою network как local.

Но между ними находится Layer 3 boundary.

Если host хочет отправить traffic в другую subnet, он отправляет его на default gateway. Поэтому без router или Layer 3 switch communication между VLANs не будет.

Это не поломка. Это смысл VLAN segmentation.

## Два Способа Route Между VLANs

Есть два базовых подхода.

### One Physical Interface Per VLAN

Старый и грубый способ:

```text
Router interface 1 -> VLAN 10
Router interface 2 -> VLAN 20
Router interface 3 -> VLAN 30
```

Каждый router interface подключается к своей VLAN и получает IP address из этой subnet.

Это работает, но быстро становится неудобно:

- нужно много physical interfaces на router;
- тратятся switch ports;
- cabling становится messy;
- добавление VLAN требует нового physical connection;
- scalability плохая.

Такой вариант полезен для понимания концепции, но редко удобен как practical design.

### Router-On-A-Stick

Router-on-a-stick использует один physical router interface и trunk link к switch.

На router создаются logical subinterfaces:

```text
GigabitEthernet0/0.10 -> VLAN 10
GigabitEthernet0/0.20 -> VLAN 20
```

Каждая subinterface:

- получает VLAN tag через `encapsulation dot1Q`;
- получает IP address из соответствующей subnet;
- становится default gateway для devices этой VLAN.

Один physical interface начинает обслуживать несколько VLANs.

## Почему IP Убирают С Physical Interface

При ROAS IP address обычно не назначают на main physical interface.

Например, не так:

```text
interface GigabitEthernet0/0
 ip address 10.0.18.1 255.255.255.192
```

Вместо этого IP addresses назначаются на subinterfaces:

```text
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 10.0.18.1 255.255.255.224

interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 10.0.18.33 255.255.255.224
```

Physical interface становится carrier для trunk traffic.

Subinterfaces становятся logical endpoints для VLANs.

## Subinterface Number

Число после точки технически не обязано совпадать с VLAN ID.

Можно сделать:

```text
GigabitEthernet0/0.123
encapsulation dot1Q 10
```

Но это плохая идея для читаемости.

Лучше делать так:

```text
GigabitEthernet0/0.10 -> VLAN 10
GigabitEthernet0/0.20 -> VLAN 20
```

Это не магия, а operational sanity. Через месяц ты откроешь config и сразу поймешь mapping.

## encapsulation dot1Q

Команда `encapsulation dot1Q` говорит router, traffic какой VLAN должен попадать на subinterface.

Пример:

```text
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
```

Это означает:

```text
Tagged frames for VLAN 10 -> handled by Gi0/0.10
```

Для VLAN 20:

```text
interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
```

Без этой команды router не знает, как связать tagged VLAN traffic с subinterfaces.

## Default Gateway Для Каждой VLAN

IP address subinterface становится default gateway для clients в этой VLAN.

Пример:

```text
VLAN 10 Admin subnet:   10.0.18.0/27
Gateway:                10.0.18.1

VLAN 20 Patron subnet:  10.0.18.32/27
Gateway:                10.0.18.33
```

Clients в VLAN 10 используют `10.0.18.1`.

Clients в VLAN 20 используют `10.0.18.33`.

Если host хочет выйти из своей subnet, он отправляет traffic на свой default gateway.

## DHCP Pools Для Разных VLANs

Если router также раздает DHCP, для каждой VLAN нужен свой pool.

Пример:

```text
ip dhcp pool ADMIN
 network 10.0.18.0 255.255.255.224
 default-router 10.0.18.1
 dns-server 8.8.8.8

ip dhcp pool PATRON
 network 10.0.18.32 255.255.255.224
 default-router 10.0.18.33
 dns-server 8.8.8.8
```

Так clients получают:

- address из правильной subnet;
- правильный default gateway;
- DNS server;
- config, соответствующий их VLAN.

## Очень Полезная Ошибка: 169.254.x.x

Если client получает address вида:

```text
169.254.x.x
```

это обычно означает, что DHCP failed.

Client пытался получить address через DHCP, но не получил response. Тогда он назначил себе automatic self-assigned address.

Это важный troubleshooting clue.

Проверь:

- находится ли client port в правильной VLAN;
- существует ли VLAN на switch;
- настроен ли trunk между switch и router;
- разрешена ли VLAN на trunk;
- есть ли subinterface на router;
- есть ли `encapsulation dot1Q`;
- правильно ли настроен DHCP pool;
- reachable ли DHCP server из этой VLAN.

В уроке именно trunk к router оказался missing piece.

## Switch Port К Router Должен Быть Trunk

Для router-on-a-stick switch port, который подключен к router, должен быть trunk.

Почему?

Потому что через один physical link должны пройти traffic нескольких VLANs.

На switch:

```text
interface GigabitEthernet0/1
 switchport mode trunk
```

Если этот port останется access port, router не увидит tagged traffic VLAN 10 и VLAN 20 как ожидается.

Ситуация получится неприятная:

```text
VLANs exist
Router subinterfaces exist
DHCP pools exist
But traffic does not reach the right subinterface
```

Config выглядит почти правильно, но system не работает.

## Проверка Inter-VLAN Routing

После исправления trunk clients начали получать correct DHCP leases:

```text
VLAN 10 client -> address from VLAN 10 subnet
VLAN 20 client -> address from VLAN 20 subnet
```

Затем можно проверить ping между VLANs.

Если routing разрешен и default gateways настроены правильно, ping проходит.

Для понимания path полезен traceroute:

```text
Client in VLAN 10
 -> Gateway subinterface for VLAN 10
 -> Router routes traffic
 -> Destination in VLAN 20
```

Traceroute показывает, что traffic сначала идет на router. Это и есть inter-VLAN routing в действии.

## Что Нужно Запомнить

Главные четыре пункта:

1. Каждая VLAN - отдельная network. Для communication между VLANs нужен router или Layer 3 device.
2. Router-on-a-stick позволяет route между несколькими VLANs через один physical router interface.
3. `encapsulation dot1Q` связывает router subinterface с конкретной VLAN.
4. Switch port к router должен быть trunk, иначе tagged VLAN traffic не попадет туда, куда нужно.

## Главный Вывод

В этом уроке сошлось сразу несколько тем:

- VLANs;
- subnetting;
- trunks;
- 802.1Q;
- router subinterfaces;
- default gateways;
- DHCP pools;
- troubleshooting.

Это хороший знак. Networking начинает выглядеть не как набор отдельных фактов, а как система.

Traffic из одной VLAN идет к своему default gateway, router принимает его на соответствующей subinterface, принимает routing decision и отправляет дальше.

Коротко:

```text
VLAN separates
Trunk carries
Subinterface receives
Router routes
Policy controls
```

Дальше важно разобраться с native VLAN и trunk behavior, потому что там есть несколько нюансов, которые легко пропустить.

