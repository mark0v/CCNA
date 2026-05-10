# Staging the Network Equipment

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Network equipment staging  
Tags: staging, switch, router, access point, server, lan, wan, mdf, redundancy, auto-mdix

## Summary

Staging network equipment - это подготовка и проверка сетевого оборудования до установки на реальной площадке. Вместо того чтобы приехать в NetworkChuck Coffee, открыть коробки и надеяться, что все заработает, оборудование лучше заранее включить, соединить, промаркировать и проверить в спокойной среде.

Главная мысль: сначала staging, потом installation. Switch связывает wired LAN, access point расширяет сеть в Wi-Fi, router соединяет LAN с WAN/internet, а staging помогает поймать ошибки до того, как они станут проблемами на рабочей площадке.

## Key Points

- Staging означает предварительную сборку и проверку сетевого оборудования.
- Staging можно делать дома, в офисе или на workbench.
- Цель - проверить питание, cables, ports и базовый design до выезда на site.
- Switch - центр локальной проводной LAN.
- Registers, servers, office PCs, cameras и APs обычно подключаются к switch.
- 24-port Cisco switch в статье - просто пример.
- Multiple switches дают гибкость и могут помочь с redundancy.
- Redundancy означает запасной вариант или устойчивость при отказе.
- Two switches могут снизить риск одного failure point, но добавляют design decisions.
- Switches соединяются между собой, чтобы обмениваться traffic.
- Современные switches обычно поддерживают Auto-MDIX.
- Servers предоставляют services.
- Clients потребляют services.
- Wireless access point расширяет wired network в Wi-Fi.
- Цвета кабелей нужны для организации, но сами по себе технического смысла не имеют.
- Router соединяет local LAN с outside WAN/internet.
- ISP означает Internet Service Provider.
- Router/firewall часто контролирует allowed/blocked traffic.
- Labels на cables и ports уменьшают количество ошибок.
- MDF означает Main Distribution Facility - центральное место для network gear.

## Notes

### Build it before you need it

Staging - это привычка собрать сеть до реальной установки.

Плохой подход:

```text
Open boxes -> guess -> plug things in -> hope it works
```

Хороший подход:

```text
Unbox -> power on -> connect -> label -> test -> install
```

Staging превращает неприятные сюрпризы в маленькие задачи, а не в emergency во время работы кофейни.

### Почему staging важен

На реальной площадке ошибки стоят дороже.

Возможные проблемы:

- access point не включается;
- switch port неисправен;
- router настроен не так, как ожидалось;
- не хватает правильного cable;
- забыли power adapter;
- firmware/settings не готовы;
- labels отсутствуют;
- physical layout непонятен.

В staging это раздражает, но не ломает бизнес. В работающей кофейне с клиентами это уже давление.

### Switch как центр LAN

Switch обычно является центральным устройством для local wired network.

LAN означает Local Area Network.

К switch могут подключаться:

- registers/POS terminals;
- wireless access points;
- cameras;
- servers;
- office PCs;
- printers;
- network storage;
- other switches.

Модель:

```text
LAN devices -> switch
```

Switch связывает внутреннюю сеть.

### Port count

В статье используется 24-port Cisco switch.

Модель не главное. Главное:

```text
Switch дает Ethernet ports для подключения устройств к LAN.
```

При планировании нужно учитывать:

- current devices;
- spare ports;
- future growth;
- uplinks;
- APs and cameras;
- PoE requirements.

### Один switch или несколько

Иногда одного большого switch достаточно. Иногда лучше несколько.

Причины использовать multiple switches:

- больше гибкости;
- больше портов;
- физическая планировка;
- redundancy;
- separation между зонами;
- future growth.

Tradeoff:

```text
Больше устройств может дать resilience,
но также добавляет устройства, которые нужно управлять и которые тоже могут ломаться.
```

### Redundancy

Redundancy означает backup/resilience при отказе.

Ментальная модель:

```text
Two is one, one is none.
```

Если единственный switch умирает, сеть может остановиться. Несколько switches могут снизить риск, если design сделан грамотно.

### Connecting switches

Если используются two switches, их нужно соединить между собой.

```text
Switch A <-> Switch B
```

Раньше для switch-to-switch links иногда приходилось думать о crossover cables. Современное оборудование обычно поддерживает Auto-MDIX.

### Auto-MDIX

Auto-MDIX упрощает cabling.

Plain-English:

```text
Switch сам понимает, как общаться по cable.
```

Это снижает необходимость вручную выбирать straight-through или crossover cable в большинстве современных setup.

### Servers and clients

Server предоставляет services.

Примеры services:

- file storage;
- media;
- internal apps;
- databases;
- authentication;
- backups.

Client потребляет эти services:

- laptops;
- tablets;
- register terminals;
- office PCs;
- phones.

Модель:

```text
Client -> requests service -> server
```

### Wireless access point

Wireless access point расширяет wired network в air.

AP обычно подключается к switch через Ethernet.

```text
Wireless clients -> AP -> switch -> LAN/WAN
```

AP дает Wi-Fi для phones, laptops, tablets, handheld business devices и customer devices.

### Cable colors

Цвет кабеля сам по себе не меняет Ethernet behavior.

Blue cable не становится "server cable" только потому, что он blue.

Цвета полезны как local convention:

| Color use | Possible meaning |
| --- | --- |
| Blue | General data |
| Yellow | APs |
| Red | WAN/uplink |
| Green | Cameras |

Важно документировать свои conventions.

### Router connects to the internet

Switch, AP и server могут создать рабочую LAN, но LAN сама по себе не дает internet access.

Router соединяет local network с outside world.

```text
LAN -> router -> WAN/internet
```

### WAN and ISP

WAN означает Wide Area Network.

В этом уроке WAN - это internet connection.

ISP означает Internet Service Provider.

ISP может дать подключение через:

- cable;
- fiber;
- DSL;
- wireless handoff;
- provider circuit.

### Router and security

Router часто делает больше, чем просто routing.

Он может выполнять:

- firewall rules;
- filtering;
- allowed traffic decisions;
- blocked traffic decisions;
- NAT;
- basic edge protection.

Главная точка:

```text
Router/edge device - место, где local network встречает outside world.
```

### Label before installation

Labeling кажется мелочью, но очень помогает.

Маркируй:

- cables;
- switch ports;
- router ports;
- AP locations;
- patch panel ports;
- power adapters;
- uplinks.

На site labels уменьшают количество глупых ошибок.

### MDF

MDF означает Main Distribution Facility.

Plain-English:

```text
Центральное место, где находится network gear.
```

В реальной кофейне кабели могут идти через walls и ceilings назад в MDF. Во время staging вся эта реальность сжимается до tabletop version.

### Staging vs final install

Staging помогает проверить:

- devices power on;
- cabling works;
- switches connect;
- AP connects;
- router path is understood;
- labels make sense;
- topology is practical.

Final installation добавляет:

- ceilings;
- walls;
- long cable runs;
- ladders;
- physical mounting;
- customer pressure;
- business downtime.

### Physical picture

Модель из статьи:

```text
Clients/servers/APs/cameras -> switch -> router -> internet
```

Расширенно:

```text
Wireless clients -> AP -> switch
Wired clients -> switch
Server -> switch
Switch -> router -> ISP/internet
```

Эта картинка дает будущим темам место в голове.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Staging | Предварительная сборка и проверка оборудования до установки на site. |
| Switch | Центральное LAN-устройство для проводных network devices. |
| LAN | Local Area Network. |
| WAN | Wide Area Network. |
| Router | Устройство, которое соединяет local network с другими сетями, например internet. |
| ISP | Internet Service Provider. |
| AP | Access Point; устройство для Wi-Fi. |
| Auto-MDIX | Функция, которая автоматически обрабатывает transmit/receive cabling behavior. |
| Server | Устройство/система, которая предоставляет services. |
| Client | Устройство/приложение, которое потребляет services. |
| Redundancy | Backup/resilience при отказе. |
| MDF | Main Distribution Facility; центральное место для network equipment. |
| Uplink | Соединение между network devices, например switch-to-switch или switch-to-router. |
| Firewall rules | Правила, которые allow или block traffic. |

## Questions

### 1. Что означает staging network equipment?

Это предварительная сборка и проверка сетевого оборудования до установки на реальной площадке.

### 2. Почему staging лучше делать до installation?

Так можно безопасно найти проблемы до того, как они станут дорогими on-site issues.

### 3. Что обычно является центром local wired network?

Switch.

### 4. Что предоставляет switch?

Ethernet ports и связь между wired LAN devices.

### 5. Почему можно использовать больше одного switch?

Для flexibility, большего числа портов, физической планировки, future growth или redundancy.

### 6. Что означает redundancy?

Backup или resilience при отказе.

### 7. Что делает Auto-MDIX?

Автоматически подстраивает transmit/receive behavior, чтобы современные devices могли общаться по обычным cables.

### 8. Что делает server?

Server предоставляет services другим устройствам.

### 9. Что делает client?

Client потребляет services от server.

### 10. Что делает wireless access point?

Расширяет wired network в Wi-Fi, чтобы wireless devices могли подключаться.

### 11. Имеют ли cable colors встроенный технический смысл?

Нет. Цвета помогают организовать кабели, но сами по себе не меняют работу cable.

### 12. Какое устройство соединяет LAN с internet?

Router.

### 13. Что означает ISP?

Internet Service Provider.

### 14. Что такое WAN в этом уроке?

Outside network / internet connection.

### 15. Какие security-функции могут жить рядом с router?

Firewall rules, filtering и решения о том, какой traffic разрешить или заблокировать.

### 16. Почему важно маркировать cables и ports?

Это уменьшает ошибки при installation и troubleshooting.

### 17. Что означает MDF?

Main Distribution Facility.

### 18. Какая главная physical picture из урока?

Devices подключаются к switches, AP расширяет LAN в Wi-Fi, router соединяет local network с internet.

## What To Review Later

- Staging first, installing second.
- Switch as the center of the wired LAN.
- Why multiple switches can help with redundancy.
- Auto-MDIX for switch-to-switch cabling.
- Server vs client.
- Access point role.
- Router connects LAN to WAN/internet.
- ISP meaning.
- Cable colors as organization, not technical truth.
- MDF as central network equipment location.
