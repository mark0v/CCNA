# Creating VLANs And Access Ports

Source: закрытая страница курса  
Date added: 2026-06-20  
Related plan item: Week 8 / Creating VLANs and assigning access ports  
Tags: VLAN, access port, Cisco switch, SVI, switchport, VLAN 1, DTP
Language: Russian
Translation pair: articles-en/2026-06/week-08/05-creating-vlans-and-access-ports.md

## Кратко

VLAN становится реальной не тогда, когда ты понял идею, а когда ты создал VLAN на switch, дал ей имя и назначил в нее ports.

В этой части появляется практическая база:

- VLAN 1 уже существует на Cisco switch по умолчанию;
- новые VLANs создаются в global configuration mode;
- VLAN стоит называть понятным именем;
- `show vlan` показывает созданные VLANs и assigned ports;
- access port принадлежит одной VLAN;
- `switchport mode access` фиксирует port как access;
- `switchport access vlan <id>` назначает port в конкретную VLAN;
- dynamic switchport mode лучше не оставлять на user-facing ports.

Главная идея: VLAN без assigned ports - это только пустая logical room. Separation появляется, когда switchports реально помещены в разные VLANs.

## Business Requirement Не Всегда Говорит "Сделай VLAN"

В реальной задаче тебе редко скажут:

```text
Configure VLANs.
```

Чаще business request звучит иначе:

```text
Separate guest devices from administrative devices.
Create a security boundary between customer traffic and internal systems.
Keep cameras, servers, network gear and guest users apart.
```

Инженер должен перевести это на язык network design.

Для NetworkChuck Coffee это означает:

- patron devices не должны жить вместе с admin systems;
- guest side не должен иметь свободный доступ к infrastructure;
- cameras, servers и network gear лучше отделять от обычных users;
- same physical switch может обслуживать разные logical groups.

Инструмент для такой separation на Layer 2 - VLAN.

## VLAN 1 Уже Есть

На Cisco switch VLANs существуют сразу из коробки.

По умолчанию все обычные switchports находятся в VLAN 1.

Это объясняет базовое поведение:

```text
All ports in VLAN 1
All devices in same default broadcast domain
Switch management SVI often tied to VLAN 1
```

SVI означает Switch Virtual Interface.

Это virtual interface, связанный с VLAN, который позволяет switch иметь IP address для management.

Например, если switch имеет management IP на VLAN 1, а devices подключены к ports в VLAN 1, эти devices могут reach switch management address, если IP settings совпадают.

Важно: SVI - не physical port. Это logical interface, принадлежащий VLAN.

## Создание VLAN

Чтобы создать VLAN на Cisco switch, используется global configuration mode.

Пример:

```text
Switch(config)# vlan 10
Switch(config-vlan)# name ADMIN_DEVICES
```

Еще одна VLAN:

```text
Switch(config)# vlan 20
Switch(config-vlan)# name PATRON_DEVICES
```

Команда `vlan 10` создает VLAN 10 или переходит в ее configuration mode, если она уже существует.

Команда `name` задает human-readable name.

Технически VLAN может жить только как number, но в реальной работе имена сильно помогают.

Сравни:

```text
VLAN 10
VLAN 20
```

и:

```text
VLAN 10 ADMIN_DEVICES
VLAN 20 PATRON_DEVICES
```

Второй вариант проще читать, проще документировать и проще troubleshooting.

## Проверка Через show vlan

После создания VLANs нужно проверить, что switch их видит.

Команда:

```text
Switch# show vlan
```

Она показывает:

- VLAN ID;
- VLAN name;
- status;
- ports, которые assigned в VLAN.

Важный момент: сразу после создания VLAN может быть пустой.

Она существует, имеет имя, но ports в нее еще не назначены.

Это как построить комнаты, но никого туда не переселить.

## Назначение Ports В VLAN

Separation начинает работать, когда switchports назначаются в VLANs.

Для одного port:

```text
Switch(config)# interface fastEthernet 0/10
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 20
```

Для нескольких ports удобнее использовать interface range:

```text
Switch(config)# interface range fastEthernet 0/10 - 15
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 20
```

Что делают эти команды:

```text
switchport mode access
```

Фиксирует port как access port. То есть port будет принадлежать одной VLAN.

```text
switchport access vlan 20
```

Назначает этот access port в VLAN 20.

После этого ports `Fa0/10 - Fa0/15` больше не находятся в default VLAN 1. Они относятся к VLAN 20.

Если подключить client к одному из этих ports, он будет жить в VLAN 20.

## Access Port

Access port - это switchport, предназначенный для endpoint device.

Обычно к access ports подключают:

- PC;
- laptop;
- printer;
- IP phone;
- camera;
- access point в simple mode;
- POS terminal.

Access port передает traffic одной VLAN.

Client device обычно не знает о VLAN tagging. Для него port выглядит как обычное Ethernet подключение.

Switch внутри себя понимает:

```text
This frame came from access port in VLAN 20.
Therefore this traffic belongs to VLAN 20.
```

## Почему Dynamic Mode Лучше Не Оставлять

На многих Cisco switches ports по умолчанию могут находиться в dynamic mode.

Это связано с DTP, Dynamic Trunking Protocol.

Идея dynamic mode: port может договариваться, быть ли ему access port или trunk port.

Звучит удобно, но для user-facing ports это плохая привычка.

Почему:

- port behavior становится менее predictable;
- чужой switch может попытаться negotiated trunk;
- trunk переносит traffic нескольких VLANs;
- появляется риск VLAN hopping или другой нежелательной access path;
- security boundary становится слабее.

Поэтому лучше явно задавать intent:

```text
User-facing port -> switchport mode access
Switch-to-switch link -> switchport mode trunk
```

Никакого guessing.

## Что Такое VLAN Hopping В Общем Смысле

VLAN hopping - это атака или нежелательная ситуация, где устройство пытается получить доступ к VLANs, к которым оно не должно иметь отношения.

Один из рисков связан с тем, что port может стать trunk, если dynamic negotiation разрешен.

Если attacker подключит устройство, которое умеет притворяться switch, port может договориться о trunk mode. Тогда через этот link может пойти traffic нескольких VLANs.

Именно поэтому access ports для users лучше фиксировать:

```text
switchport mode access
```

И назначать только нужную VLAN:

```text
switchport access vlan 20
```

## Что Было Сделано В Уроке

В этой части были выполнены три основных действия.

Первое: подтверждено, что VLANs уже существуют на switch через default VLAN 1.

Второе: созданы и названы новые VLANs:

```text
VLAN 10 ADMIN_DEVICES
VLAN 20 PATRON_DEVICES
```

Третье: range ports был назначен в patron VLAN как access ports:

```text
interface range fastEthernet 0/10 - 15
switchport mode access
switchport access vlan 20
```

После этого devices, подключенные к этим ports, находятся в VLAN 20, а не в VLAN 1.

## Почему Пока Нельзя Просто Перенести Все Devices

Если VLANs созданы только на одном switch, а trunk links между switches еще не настроены, можно случайно сломать connectivity.

Например:

```text
Device A in VLAN 20 on Switch 1
Device B in VLAN 20 on Switch 2
```

Если между switches нет trunk, VLAN 20 traffic не сможет правильно перейти между ними.

Получится separation без нужной connectivity.

Поэтому порядок важен:

1. Создать VLANs.
2. Назначить access ports.
3. Настроить trunk links между switches.
4. Проверить VLAN propagation и traffic.
5. Только потом массово переносить production devices.

## Главный Вывод

Создать VLAN - это только первый шаг.

Реальная separation появляется, когда:

- VLAN создана;
- VLAN названа;
- ports назначены как access;
- access ports помещены в правильную VLAN;
- dynamic behavior отключен там, где он не нужен;
- trunk links готовы переносить VLANs между switches.

Короткая памятка:

```text
vlan 20
name PATRON_DEVICES

interface range fa0/10 - 15
switchport mode access
switchport access vlan 20

show vlan
```

Это минимальный practical foundation для VLAN configuration.

Дальше нужно настроить trunk links, чтобы VLANs могли span multiple switches.

