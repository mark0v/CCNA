# Why VLANs Matter

Source: закрытая страница курса  
Date added: 2026-06-20  
Related plan item: Week 8 / VLAN foundations  
Tags: VLAN, switching, broadcast domain, segmentation, security, IP addressing
Language: Russian
Translation pair: articles-en/2026-06/week-08/03-why-vlans-matter.md

## Кратко

VLAN, или Virtual LAN, позволяет разделить одну physical switching infrastructure на несколько logical networks.

Проще говоря: устройства могут быть подключены к тем же switches, но логически находиться в разных сетях.

Это нужно не ради красоты. VLANs дают:

- меньшие broadcast domains;
- меньше лишнего traffic noise;
- logical separation между группами устройств;
- security boundaries;
- более понятный IP addressing plan;
- возможность применять routing и ACL policies между сегментами;
- network design, который можно масштабировать.

Без VLAN сеть быстро превращается в одну большую комнату, где все устройства находятся рядом и слышат слишком много лишнего.

## Flat Network: Одна Большая Комната

Представь компанию на 100 человек, где каждое совещание обязано включать всех сотрудников.

Sales discussion? Все участвуют.

Accounting question? Все участвуют.

Короткое обновление по маленькому project? Снова все 100 человек в одной комнате.

Это абсурдно для людей, но именно так ощущается flat network.

Flat network - это сеть, где разные устройства живут в одном большом shared segment без логического разделения.

Сначала это кажется простым:

```text
Все подключено.
Все получает IP.
Все вроде работает.
```

Потом начинается рост:

- больше users;
- больше devices;
- guest Wi-Fi;
- cameras;
- printers;
- POS terminals;
- office PCs;
- management devices;
- security requirements.

И внезапно простая сеть становится источником шума, риска и неудобного troubleshooting.

## Разве Switch Уже Не Разделяет Traffic?

Switch действительно умнее hub.

Hub просто повторяет signal всем ports. Switch строит MAC address table и отправляет frames только туда, куда нужно.

Но это не означает, что switch автоматически создает разные broadcast domains.

Если все ports находятся в одной VLAN, то все devices остаются в одном Layer 2 broadcast domain.

Broadcast traffic все еще распространяется внутри этого общего пространства.

Примеры broadcast или local discovery traffic:

- ARP requests;
- DHCP discovery;
- некоторые service discovery protocols;
- другие Layer 2 announcements.

Switch уменьшает лишний unicast traffic по сравнению с hub, но VLANs нужны для настоящей logical segmentation.

## Что Делает VLAN

VLAN делит switch на logical groups.

Один physical switch может выглядеть так:

```text
Ports 1-8     -> VLAN 10 Users
Ports 9-12    -> VLAN 20 POS
Ports 13-16   -> VLAN 30 Cameras
Ports 17-20   -> VLAN 40 Guest Wi-Fi
Ports 21-24   -> VLAN 99 Management
```

Физически это один switch.

Логически это несколько отдельных networks.

Устройства в разных VLAN не общаются напрямую на Layer 2. Чтобы traffic прошел между VLANs, нужен Layer 3 device:

- router;
- Layer 3 switch;
- firewall.

И это хорошо, потому что между VLANs можно применить rules.

## NetworkChuck Coffee Нужны Границы

Для NetworkChuck Coffee в одной сети могут оказаться разные типы устройств:

- barista tablets;
- point-of-sale terminals;
- office PCs;
- cameras;
- inventory systems;
- guest Wi-Fi clients;
- phones;
- network management devices.

Если бросить все это в один segment, получится опасная смесь.

Guest Wi-Fi users не должны находиться рядом с POS systems.

Cameras не должны жить вместе с office laptops.

Management interfaces switches и routers не должны быть доступны обычным users.

VLANs позволяют построить boundaries без отдельной физической сети для каждой группы.

Это важная real-world идея: разделение достигается не дополнительными километрами кабеля, а правильной logical design.

## Что VLANs Дают На Практике

### Меньшие Communication Groups

Вместо одного большого everyone-talks-to-everyone пространства сеть делится на manageable chunks.

Это уменьшает broadcast scope и делает поведение сети понятнее.

### Security Boundaries

VLAN сама по себе не является полноценной security policy, но она создает границы, на которые потом можно навесить routing rules, ACLs или firewall policies.

Например:

```text
Guest VLAN не имеет доступа к POS VLAN.
Camera VLAN может отправлять traffic только к recording server.
Management VLAN доступна только administrators.
```

### IP Addressing Boundaries

Обычно каждая VLAN получает свою subnet.

Например:

```text
VLAN 10 Users:       10.0.10.0/24
VLAN 20 POS:         10.0.20.0/24
VLAN 30 Cameras:     10.0.30.0/24
VLAN 40 Guest Wi-Fi: 10.0.40.0/24
VLAN 99 Management:  10.0.99.0/24
```

Это помогает:

- планировать addresses;
- понимать, где находится device;
- troubleshooting делать быстрее;
- писать ACLs понятнее;
- документировать сеть аккуратнее.

### Better Control

Когда groups separated, можно решать, как они взаимодействуют.

Можно разрешить:

```text
Users -> Internet
Users -> Printer
POS -> Payment processor
Admin PC -> Management VLAN
```

И запретить:

```text
Guest Wi-Fi -> Internal LAN
Cameras -> Office PCs
Users -> Switch management interfaces
```

Так сеть начинает вести себя как design, а не как случайный набор подключений.

## VLANs Не Только Про Broadcast Noise

VLANs часто объясняют как способ уменьшить broadcast traffic. Это правда, но это только часть картины.

Более важная идея: VLANs выражают intent.

Они показывают, как business хочет разделить свою инфраструктуру:

- кто является guest;
- кто является employee;
- какие systems sensitive;
- какие devices infrastructure;
- где должен останавливаться trust.

Именно поэтому VLANs появляются даже в небольших environments. Маленький бизнес тоже имеет разные trust levels.

Guest Wi-Fi, printers, cameras, employee devices и payment systems не должны жить как одна дружная плоская сеть.

## Как VLANs Связаны С Routing

Если devices находятся в одной VLAN и одной subnet, они общаются напрямую через switch.

Если devices находятся в разных VLANs, им нужен inter-VLAN routing.

Это может быть:

- router-on-a-stick;
- Layer 3 switch;
- firewall interface или subinterface.

Именно здесь прошлые темы начинают соединяться:

- subnetting помогает выделить address space для каждой VLAN;
- routing позволяет VLANs общаться между собой;
- ACLs контролируют, какой traffic разрешен;
- NAT может применяться для выхода во внешние сети;
- DHCP может выдавать addresses отдельно для каждой VLAN.

VLANs не заменяют все эти технологии. Они создают structure, на которую эти технологии опираются.

## Главный Вывод

VLANs позволяют разбить одну большую сеть на smaller, smarter, safer groups.

Это важно не потому, что VLANs выглядят как advanced topic. Это важно потому, что без segmentation real networks становятся:

- шумными;
- сложными для troubleshooting;
- небезопасными;
- плохо масштабируемыми;
- неудобными для управления.

VLAN - это один из первых инструментов, который переводит switching из режима "просто подключили devices" в режим "мы строим infrastructure".

Дальше можно разбирать, как VLANs создаются, как ports назначаются в VLANs, как traffic нескольких VLANs проходит между switches и как все это связывается с IP addressing.

