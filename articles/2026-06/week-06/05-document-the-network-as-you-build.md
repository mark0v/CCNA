# Document the Network as You Build

Source: закрытая страница курса  
Date added: 2026-06-09  
Related plan item: Week 6 / Network documentation and IPAM foundations  
Tags: network documentation, IPAM, inventory, show version, show ip interface brief, lifecycle, troubleshooting
Language: Russian
Translation pair: articles-en/2026-06/week-06/05-document-the-network-as-you-build.md

## Summary

Network documentation нужно вести во время построения сети, а не откладывать до завершения проекта. Даже простая spreadsheet с devices, interfaces и IP addresses значительно ускоряет troubleshooting, поддержку и замену оборудования.

Главная мысль: полезная документация, которую легко обновлять, лучше идеальной системы, которая так и не была создана. Начни с одной таблицы и расширяй ее вместе с network.

## Key Points

- Документировать нужно сразу после configuration changes.
- Не следует полагаться на память или обещание вернуться к документации позже.
- Начать можно с Excel или Google Sheets.
- Базовые поля: device name, model, serial, interface, MAC и IP address.
- Полезно хранить firmware, purchase date, in-service date и warranty.
- `show version` дает model, serial и software information.
- `show ip interface brief` быстро показывает interfaces, IP и status.
- `show interface` помогает найти interface MAC address и operational data.
- Значения следует получать с devices, а не восстанавливать по памяти.
- Единый формат данных делает таблицу удобной для поиска и сравнения.
- Такая inventory является первым шагом к IPAM и lifecycle management.
- Документация должна обновляться через тот же change process, что и сеть.

## Notes

### Documentation Is Not Closeout Work

Формально documentation часто оказывается в конце project plan.

На практике к этому моменту:

- команда устала;
- сроки уже закончились;
- детали забыты;
- engineers переключились на следующий проект;
- temporary решения стали permanent;
- никто не хочет восстанавливать topology по памяти.

Поэтому правильный момент для записи изменения:

```text
Immediately after the change is configured and verified.
```

### Why It Matters During An Incident

Когда network ломается, documentation отвечает на первые вопросы:

```text
Как называется device?
Где он находится?
Какая у него management IP?
Какой interface подключен?
Какой сосед находится с другой стороны?
Какая версия software установлена?
Есть ли warranty?
Когда configuration менялась?
```

Без этих данных troubleshooting начинается с повторного исследования самой сети.

### Start With One Useful Sheet

Необязательно сразу внедрять enterprise documentation platform.

Создай sheet:

```text
Devices and IP Addresses
```

Минимальные columns:

| Column | Purpose |
| --- | --- |
| Device Name | Уникальное hostname |
| Role | Router, switch, firewall, AP, server |
| Site / Location | Физическое расположение |
| Vendor / Model | Точная hardware platform |
| Serial Number | Support и asset tracking |
| Interface | Конкретный physical/logical port |
| Interface Description | Назначение link |
| MAC Address | Layer 2 identity |
| IP Address / Prefix | Layer 3 assignment |
| Default Gateway | Для management endpoints |
| Firmware / OS | Software version |
| Purchase Date | Начало lifecycle |
| In-Service Date | Когда device введен в эксплуатацию |
| Warranty End | Планирование replacement/support |
| Owner | Ответственная команда или человек |
| Notes | Особые детали |

### Keep The Structure Practical

Таблица должна быть:

- понятной без отдельной инструкции;
- удобной для filtering;
- последовательно отформатированной;
- простой для обновления;
- доступной нужным engineers;
- защищенной от случайных изменений.

Полезные улучшения:

- bold headers;
- frozen header row;
- filters;
- consistent date format;
- fixed IP/CIDR format;
- conditional highlighting для expired warranty;
- отдельные dropdown values для role и status.

### Collect Data From Devices

Не вводи inventory по памяти.

На Cisco IOS используй:

```cisco
show version
show ip interface brief
show interfaces
show inventory
show cdp neighbors detail
show lldp neighbors detail
```

Команды дают разные части картины.

### `show version`

Обычно помогает определить:

- Cisco IOS version;
- uptime;
- hardware model;
- memory;
- system image;
- serial or processor board ID;
- configuration register.

Пример:

```cisco
show version
```

Software version важно фиксировать точно, включая release и build.

### `show inventory`

На поддерживаемых devices:

```cisco
show inventory
```

Команда может показать:

- chassis PID;
- serial number;
- installed modules;
- power supplies;
- transceivers.

Она часто удобнее `show version` для hardware inventory.

### `show ip interface brief`

```cisco
show ip interface brief
```

Быстро показывает:

- interface name;
- assigned IP;
- assignment method;
- administrative status;
- line protocol status.

Это хороший источник для первичного interface/IP mapping.

### `show interfaces`

Для конкретного interface:

```cisco
show interface GigabitEthernet0/1
```

Можно получить:

- hardware/MAC address;
- description;
- status;
- speed and duplex;
- counters and errors;
- MTU;
- traffic rates.

В inventory обычно переносится стабильная identity information, а не временные counters.

### Neighbor Discovery

Чтобы документировать connections:

```cisco
show cdp neighbors detail
show lldp neighbors detail
```

Они помогают связать:

- local interface;
- remote device;
- remote port;
- management address;
- platform.

Но discovery output нужно сверять с фактической cabling и design.

### Standardize The Data

Выбери единые formats.

Примеры:

```text
Hostname:       CAFE01-RTR01
Interface:      GigabitEthernet0/1
IPv4:           192.168.2.1/24
MAC:            00:1A:2B:3C:4D:5E
Date:           2026-06-09
Software:       Cisco IOS 15.2(4)M
```

Не смешивай без причины:

- `Gi0/1` и `GigabitEthernet0/1`;
- CIDR и отдельные masks;
- разные MAC separators;
- локальные и ISO date formats;
- marketing и exact product names.

Consistency улучшает search, sorting и automation.

### Why Model And Serial Matter

Точные model и serial number нужны для:

- vendor support case;
- warranty verification;
- replacement/RMA;
- spare planning;
- security advisory checks;
- asset ownership;
- audit.

Запись вроде `Cisco switch` недостаточна.

Нужна точная platform, например:

```text
Cisco Catalyst C9200L-24P-4G
```

### Why Firmware Matters

Разные software versions могут означать:

- разное поведение protocols;
- известные bugs;
- security vulnerabilities;
- несовместимость commands;
- разные default settings;
- невозможность получить vendor support.

Firmware inventory помогает быстро найти devices, требующие patch или upgrade.

### Lifecycle And Warranty

Purchase и in-service dates позволяют оценить возраст equipment.

Warranty end и end-of-support dates помогают планировать:

- budget;
- replacement;
- maintenance windows;
- spare stock;
- migrations.

Не стоит узнавать, что device давно unsupported, во время outage.

### This Is The Beginning Of IPAM

IPAM означает:

```text
IP Address Management
```

IPAM систематизирует:

- address spaces;
- subnets;
- assigned и available IPs;
- DHCP scopes;
- DNS records;
- VLANs;
- sites;
- owners;
- reservations;
- conflicts.

Начальная spreadsheet еще не полноценная IPAM platform, но формирует нужную дисциплину.

### Grow Documentation Gradually

После базового inventory можно добавить sheets:

- Subnets and VLANs;
- Routing;
- WAN Circuits;
- Cabling;
- Rack Layout;
- Wireless;
- Firewall Rules;
- Support Contracts;
- Change Log;
- Backup and Recovery.

Добавляй structure по мере реальной необходимости.

### Make Updates Part Of Change Management

Для каждого network change:

1. Запланировать configuration.
2. Обновить или подготовить documentation.
3. Выполнить change.
4. Проверить результат.
5. Зафиксировать фактические values.
6. Добавить дату и автора.

Change не считается полностью завершенным, пока documentation не соответствует фактическому state.

### Protect Sensitive Information

Documentation не должна хранить plaintext passwords, private keys или reusable secrets в обычной spreadsheet.

Можно документировать:

- тип authentication;
- имя vault entry;
- owner;
- rotation date;
- recovery procedure location.

Сами secrets должны находиться в approved password manager или secrets vault.

## Example Inventory Row

| Device | Role | Site | Model | Serial | Interface | IP/Prefix | MAC | Software | Warranty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CAFE01-RTR01 | Edge Router | Cafe 01 | ISR 4331 | FDOXXXXXXX | Gi0/0/0 | 192.168.1.1/24 | 00:1A:2B:3C:4D:5E | IOS XE 17.x | 2028-06-30 |

## Practical Checklist

- Создать central inventory.
- Добавить понятные columns.
- Собрать данные непосредственно с devices.
- Нормализовать names, dates, MAC и IP formats.
- Записать site и role.
- Записать model, serial и software.
- Добавить lifecycle и warranty details.
- Документировать interface descriptions и neighbors.
- Не хранить secrets в открытом виде.
- Обновлять documentation при каждом change.
- Периодически сверять таблицу с реальной сетью.

## Quick Self-Check

### Question 1

Когда лучше документировать network change?

Answer:

```text
Во время выполнения change, сразу после configuration и verification.
```

### Question 2

Какие команды быстро дают device и IP information?

Answer:

```text
show version, show inventory и show ip interface brief.
```

### Question 3

Почему firmware version важна?

Answer:

```text
Она влияет на behavior, bugs, security, compatibility и support.
```

### Question 4

Что такое IPAM?

Answer:

```text
Практика управления IP address spaces, subnets и assignments.
```

### Question 5

Нужно ли хранить passwords в inventory spreadsheet?

Answer:

```text
Нет. Secrets должны находиться в защищенном password manager или vault.
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Network inventory | Реестр devices, interfaces и operational details. |
| IPAM | IP Address Management. |
| `show version` | Device model/software и system information. |
| `show inventory` | Hardware modules, PID и serial numbers. |
| `show ip interface brief` | Краткий список interface IP/status. |
| `show interface` | Подробные данные конкретного interface. |
| CDP / LLDP | Neighbor discovery protocols. |
| Lifecycle | Период от покупки до вывода equipment из эксплуатации. |
| RMA | Процесс vendor replacement неисправного hardware. |
| Source of truth | Авторитетное место хранения актуальных данных. |

## What To Review Later

- IPAM platforms
- Network diagrams
- Configuration backups
- Change management
- Asset lifecycle
- NetBox
- Automated discovery
- Documentation audits
