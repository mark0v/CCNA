# Reverse Engineering IPv4 Subnets

Source: закрытая страница курса  
Date added: 2026-06-13  
Related plan item: Week 7 / Reverse engineering IPv4 subnets  
Tags: subnetting, troubleshooting, reverse engineering, network address, broadcast, gateway, binary AND
Language: Russian
Translation pair: articles-en/2026-06/week-07/12-reverse-engineering-ipv4-subnets.md

## Кратко

При troubleshooting чаще приходится не проектировать новую subnet, а расшифровывать существующую конфигурацию.

Даны:

```text
Host address: 192.168.5.22
Mask:         255.255.255.240
```

Нужно определить:

- prefix;
- network address;
- broadcast address;
- usable host range;
- принадлежность других devices к той же subnet;
- допустимость default gateway.

Для примера:

```text
Prefix:      /28
Increment:   16
Network:     192.168.5.16
First host:  192.168.5.17
Last host:   192.168.5.30
Broadcast:   192.168.5.31
```

## Ключевые Идеи

- IP address без mask или prefix не определяет subnet.
- Mask определяет размер block и его boundaries.
- Increment вычисляется в interesting octet.
- Host принадлежит block между соседними network boundaries.
- Network является первым address block.
- Broadcast является последним address block.
- Default gateway обычно должен быть usable address в той же subnet, что и host.
- Устройства на одном physical switch могут находиться в разных IP subnets.
- Синтаксически допустимый address не обязательно подходит для конкретного segment.
- Binary AND даёт network address напрямую.

## Когда Нужен Reverse Subnetting

Типичные ситуации:

- проверка static IP configuration;
- диагностика недоступного default gateway;
- сравнение client и server addresses;
- проверка DHCP scope;
- поиск неправильной subnet mask;
- анализ routing table;
- миграция undocumented network;
- проверка firewall objects;
- расследование duplicate или overlapping ranges;
- проверка, является ли address network или broadcast.

## Входные Данные

Минимально нужны:

```text
IPv4 address
Subnet mask or prefix
```

Полезно также получить:

```text
Default gateway
DNS servers
VLAN
Interface
DHCP or static source
```

Без prefix запись:

```text
192.168.5.22
```

не сообщает, находится ли host в `/24`, `/28`, `/30` или другой subnet.

## Метод Increment

1. Перевести mask в prefix при необходимости.
2. Найти interesting octet.
3. Вычислить `increment = 256 - mask octet`.
4. Выписать multiples increment.
5. Найти interval, содержащий host value.
6. Нижняя boundary является network.
7. Следующая boundary минус один является broadcast.
8. Addresses между ними являются usable range.

## Пример 1: `192.168.5.22/28`

Mask:

```text
255.255.255.240
```

Binary:

```text
11111111.11111111.11111111.11110000
```

Prefix:

```text
/28
```

Interesting octet:

```text
Fourth octet
```

Increment:

```text
256 - 240 = 16
```

Boundaries:

```text
0, 16, 32, 48, 64, 80, 96, 112,
128, 144, 160, 176, 192, 208, 224, 240
```

Значение `22` находится здесь:

```text
16 <= 22 < 32
```

Следовательно:

```text
Network:    192.168.5.16
First host: 192.168.5.17
Host:       192.168.5.22
Last host:  192.168.5.30
Broadcast:  192.168.5.31
```

## Быстрая Формула Boundary

Для interesting-octet value `v` и increment `b`:

```text
Network value = floor(v / b) * b
Broadcast value = network value + b - 1
```

Для `22` и block size `16`:

```text
floor(22 / 16) = 1
1 * 16 = 16
Broadcast = 16 + 16 - 1 = 31
```

## Проверка Через Binary AND

Network address получается побитовой операцией:

```text
IP address AND subnet mask
```

Последний octet:

```text
22  = 00010110
240 = 11110000
AND = 00010000
```

```text
00010000 = 16
```

Network:

```text
192.168.5.16
```

Broadcast можно получить, установив все host bits в `1`:

```text
Network:   00010000
Host bits:     1111
Broadcast: 00011111 = 31
```

## Проверка Default Gateway

Host:

```text
192.168.5.22/28
```

Usable range:

```text
192.168.5.17 - 192.168.5.30
```

Подходящие gateway candidates:

```text
192.168.5.17
192.168.5.30
```

или любой другой назначенный router address внутри usable range.

Неподходящие:

```text
192.168.5.16   network
192.168.5.31   broadcast
192.168.5.33   different subnet
```

Обычно host должен считать gateway directly connected и разрешить его Layer 2 address через ARP. Некоторые platforms допускают специальные on-link или point-to-point configurations, но обычный LAN design требует gateway в той же subnet.

## Сравнение Нескольких Devices

Все устройства используют `/28`:

| Device | Address |
| --- | --- |
| PC | `192.168.5.10/28` |
| Server A | `192.168.5.17/28` |
| Server B | `192.168.5.19/28` |
| Router | `192.168.5.33/28` |

### PC

`10` находится в block `0-15`:

```text
Network:   192.168.5.0/28
Usable:    192.168.5.1 - 192.168.5.14
Broadcast: 192.168.5.15
```

### Servers

`17` и `19` находятся в block `16-31`:

```text
Network:   192.168.5.16/28
Usable:    192.168.5.17 - 192.168.5.30
Broadcast: 192.168.5.31
```

### Router

`33` находится в block `32-47`:

```text
Network:   192.168.5.32/28
Usable:    192.168.5.33 - 192.168.5.46
Broadcast: 192.168.5.47
```

Итог:

```text
PC subnet:      192.168.5.0/28
Server subnet:  192.168.5.16/28
Router subnet:  192.168.5.32/28
```

Один switch не превращает эти addresses в одну IP subnet.

## Physical Segment и Logical Subnet

Layer 2 switch пересылает Ethernet frames внутри VLAN. IP host решает, является ли destination local, используя собственный address и mask.

Если destination local:

```text
Host performs ARP for destination.
```

Если destination remote:

```text
Host sends packet to default gateway.
```

Поэтому два devices могут быть физически подключены к одному switch, но считать друг друга remote из-за masks и addresses.

Для связи разных IP subnets нужен Layer 3 forwarding и корректно доступный gateway для каждой subnet.

## Почему Gateway В Другой Subnet Ломает Обычный LAN

Host:

```text
192.168.5.10/28
```

Gateway:

```text
192.168.5.33
```

Host рассчитывает:

```text
Local network: 192.168.5.0/28
Gateway network: 192.168.5.32/28
```

Gateway не является on-link address для host. Обычная configuration не может использовать remote gateway как next hop без дополнительного механизма.

Корректный gateway для PC должен находиться в:

```text
192.168.5.1 - 192.168.5.14
```

## Пример 2: Boundary В Третьем Octet

Дано:

```text
Host: 172.16.35.200/20
Mask: 255.255.240.0
```

Interesting octet:

```text
Third
```

Increment:

```text
256 - 240 = 16
```

Third-octet boundaries:

```text
0, 16, 32, 48, 64, ...
```

`35` находится между `32` и `48`.

```text
Network:    172.16.32.0
First host: 172.16.32.1
Last host:  172.16.47.254
Broadcast:  172.16.47.255
```

Address `172.16.35.200` является usable.

## Пример 3: `/23` и Необычные Окончания

Дано:

```text
Host: 172.20.11.0/23
Mask: 255.255.254.0
```

Increment в третьем octet:

```text
256 - 254 = 2
```

`11` входит в block `10-11`.

```text
Network:    172.20.10.0
First host: 172.20.10.1
Last host:  172.20.11.254
Broadcast:  172.20.11.255
```

`172.20.11.0` является usable host, хотя заканчивается `.0`.

## Пример 4: Обнаружение Broadcast

Дано:

```text
Address: 10.4.7.255/21
Mask:    255.255.248.0
```

Increment в третьем octet:

```text
8
```

Third-octet value `7` находится в block `0-7`.

```text
Network:   10.4.0.0
Broadcast: 10.4.7.255
```

Данный address является broadcast и не должен назначаться обычному host interface.

## Универсальный Checklist

```text
Given:
  IP address
  Mask/prefix
  Gateway, if available

Derive:
  Prefix
  Interesting octet
  Increment
  Lower boundary
  Next boundary
  Network
  Broadcast
  First host
  Last host

Validate:
  Host is usable
  Gateway is usable
  Host and gateway share subnet
  Peer devices share subnet when expected
  DHCP scope matches
  No overlap exists
```

## Troubleshooting Workflow

1. Получить actual configuration с устройства.
2. Не доверять документации без проверки.
3. Записать IP, mask и gateway.
4. Определить host subnet.
5. Проверить, что host address не network/broadcast.
6. Определить gateway subnet.
7. Проверить same-subnet relationship.
8. Проверить ARP/neighbor resolution.
9. Проверить VLAN и switch port.
10. Проверить router interface и routing.
11. Сравнить с DHCP scope или IPAM.
12. Исправить только после подтверждения root cause.

## Команды Windows

```powershell
ipconfig /all
route print
arp -a
ping <gateway>
tracert <destination>
```

Полезно проверить:

- IPv4 Address;
- Subnet Mask;
- Default Gateway;
- DHCP Enabled;
- lease source;
- route к local subnet.

## Команды Linux

```bash
ip address
ip route
ip neigh
ping -c 4 <gateway>
tracepath <destination>
```

## Команды Cisco IOS

```text
show ip interface brief
show running-config interface <interface>
show ip route
show arp
show interfaces switchport
show vlan brief
```

## Проверка Двух Addresses

Самый надёжный способ определить, находятся ли два addresses в одной subnet:

```text
Network A = Address A AND Mask
Network B = Address B AND Mask
```

Если:

```text
Network A == Network B
```

они находятся в одной subnet при одинаковой mask.

Если masks различаются, каждый host может воспринимать relationship по-разному. Это называется asymmetric subnet-mask mismatch и способно создавать одностороннюю или нестабильную connectivity.

## Mask Mismatch

Host A:

```text
192.168.5.10/24
```

Host B:

```text
192.168.5.200/28
```

Host A считает Host B local, потому что оба находятся в `192.168.5.0/24`.

Host B находится в:

```text
192.168.5.192/28
```

и считает `192.168.5.10` remote.

Результат может зависеть от gateway, proxy ARP и platform behavior. Даже если отдельные packets проходят, configuration логически несогласованна и должна быть исправлена.

## DHCP Scope Validation

Для subnet:

```text
192.168.5.16/28
```

допустимый pool может быть:

```text
192.168.5.18 - 192.168.5.30
```

если:

```text
192.168.5.17 = gateway
```

Нельзя включать:

```text
192.168.5.16   network
192.168.5.31   broadcast
192.168.5.32   next subnet
```

## Практическое Задание

Для каждого address найдите network, usable range и broadcast.

### Задание 1

```text
192.168.100.77/27
```

### Задание 2

```text
172.31.73.14/21
```

### Задание 3

```text
10.10.200.255/18
```

### Задание 4

```text
203.0.113.191/26
```

Также определите, является ли сам address usable.

## Ответы

### Задание 1

`/27`:

```text
Mask:      255.255.255.224
Increment: 32 in fourth octet
```

`77` входит в block `64-95`.

```text
Network:    192.168.100.64
First host: 192.168.100.65
Last host:  192.168.100.94
Broadcast:  192.168.100.95
Address:    usable
```

### Задание 2

`/21`:

```text
Mask:      255.255.248.0
Increment: 8 in third octet
```

`73` входит в block `72-79`.

```text
Network:    172.31.72.0
First host: 172.31.72.1
Last host:  172.31.79.254
Broadcast:  172.31.79.255
Address:    usable
```

### Задание 3

`/18`:

```text
Mask:      255.255.192.0
Increment: 64 in third octet
```

`200` входит в block `192-255`.

```text
Network:    10.10.192.0
First host: 10.10.192.1
Last host:  10.10.255.254
Broadcast:  10.10.255.255
Address:    10.10.200.255 is usable
```

Окончание `.255` не делает его broadcast, потому что broadcast всей `/18` равен `10.10.255.255`.

### Задание 4

`/26`:

```text
Mask:      255.255.255.192
Increment: 64 in fourth octet
```

`191` является концом block `128-191`.

```text
Network:    203.0.113.128
First host: 203.0.113.129
Last host:  203.0.113.190
Broadcast:  203.0.113.191
Address:    broadcast, not usable
```

## Проверка С Python

```python
from ipaddress import ip_interface

interface = ip_interface("192.168.5.22/28")
network = interface.network

print(network.network_address)
print(network.broadcast_address)
print(network.num_addresses)
print(interface.ip in network)
```

Ожидаемый результат:

```text
192.168.5.16
192.168.5.31
16
True
```

## Частые Ошибки

### Анализировать IP Без Mask

Address сам по себе не определяет boundaries.

### Считать Любой `.0` Network

Роль зависит от host bits конкретного prefix.

### Считать Любой `.255` Broadcast

В larger-than-`/24` subnet такой address может быть usable.

### Использовать Increment В Неправильном Octet

Для `/20` increment применяется в третьем octet.

### Приравнять Следующую Network К Broadcast

Broadcast равен:

```text
next network - 1
```

### Проверять Gateway Только На Синтаксис

Gateway должен быть usable и on-link для обычного LAN host.

### Считать Один Switch Одной IP Subnet

Switching domain и IP subnet связаны design convention, но не являются одним и тем же понятием.

### Игнорировать Mask Mismatch

Два hosts могут принимать разные решения о local/remote destination.

### Полагаться Только На Ping

Ping failure не доказывает subnet error, а успешный ping при proxy ARP не доказывает корректность design.

## Контрольные Вопросы

### Вопрос 1

Какой increment у `255.255.255.240`?

Ответ:

```text
256 - 240 = 16.
```

### Вопрос 2

В какой subnet находится `192.168.5.22/28`?

Ответ:

```text
192.168.5.16/28.
```

### Вопрос 3

Каков broadcast этой subnet?

Ответ:

```text
192.168.5.31.
```

### Вопрос 4

Может ли `172.20.11.0` быть host address?

Ответ:

```text
Да, например внутри 172.20.10.0/23.
```

### Вопрос 5

Почему gateway обычно должен быть в той же subnet?

Ответ:

```text
Host должен достигнуть next hop напрямую на Layer 2 и разрешить его MAC address.
```

### Вопрос 6

Как подтвердить network без increment method?

Ответ:

```text
Выполнить побитовый AND между IP address и subnet mask.
```

## Команды и Термины

| Термин | Значение |
| --- | --- |
| Reverse subnetting | Определение boundaries по существующим IP и mask. |
| Interesting octet | Octet, содержащий network/host boundary. |
| Increment | Размер шага между network boundaries. |
| On-link | Address, который host считает directly connected. |
| Binary AND | Операция получения network address из IP и mask. |
| Mask mismatch | Разные masks на devices одного предполагаемого segment. |
| Network boundary | Первый address aligned subnet block. |
| Broadcast | Последний address обычной IPv4 subnet. |

## Что Повторить Позже

- Binary AND
- Interesting octet
- Block alignment
- Default gateway behavior
- ARP
- VLAN versus subnet
- DHCP scope validation
- Proxy ARP
- Troubleshooting workflow

