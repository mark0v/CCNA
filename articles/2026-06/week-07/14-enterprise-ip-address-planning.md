# Enterprise IP Address Planning: Castle Rysen Coffee

Source: закрытая страница курса  
Date added: 2026-06-13  
Related plan item: Week 7 / Enterprise IP address planning  
Tags: IPv4, VLSM, address planning, enterprise design, route summarization, RFC 1918, growth
Language: Russian
Translation pair: articles-en/2026-06/week-07/14-enterprise-ip-address-planning.md

## Кратко

Реальный IP address plan строится не только по текущему числу сотрудников. Он учитывает:

- пользовательские и корпоративные devices;
- servers и virtual infrastructure;
- Wi-Fi, cameras и access control;
- management networks;
- growth;
- географию и организационную структуру;
- route summarization;
- operational simplicity.

Для Castle Rysen Coffee используется private block `10.0.0.0/8` и иерархия:

```text
Central Office:       10.0.0.0/20
Regional Group 1:     10.0.16.0/20
Regional Group 2:     10.0.32.0/20
...
```

Каждый regional `/20` содержит:

- один shelter `/23`;
- до 50 district shops `/26`;
- резерв для infrastructure, links и growth.

## Ключевые Идеи

- Headcount не равен числу IP addresses.
- Business requirements сначала переводятся в device и service requirements.
- Site blocks полезно делать крупнее отдельных текущих VLANs.
- Иерархический plan отражает geography и ownership.
- Contiguous allocations облегчают route summarization.
- Reserved space является частью design, а не обязательно waste.
- Каждый summary block должен быть aligned.
- Детальные subnets внутри site block могут меняться без изменения global plan.
- IPAM и документация обязательны для долгоживущей схемы.

## От Headcount К Device Count

Один человек может использовать:

- laptop;
- phone;
- tablet;
- wearable;
- virtual desktop;
- wired и wireless interfaces.

Кроме пользователей, addresses нужны:

- access points;
- switches;
- routers;
- firewalls;
- printers;
- cameras;
- badge readers;
- door controllers;
- POS terminals;
- servers;
- hypervisors;
- management interfaces;
- load balancers;
- monitoring;
- temporary и guest devices.

Поэтому:

```text
200 people != 200 IP addresses
```

## Discovery Перед Расчётом

Перед выбором prefixes соберите:

1. Site types и количество sites.
2. Current endpoints по категориям.
3. Growth forecast.
4. Infrastructure и redundancy.
5. VLAN и security-zone requirements.
6. WAN topology.
7. Cloud, VPN и partner ranges.
8. Existing overlaps.
9. Summarization boundaries.
10. Operational ownership.

Неизвестные assumptions нужно явно записывать.

## Выбор Private Space

RFC 1918 определяет:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

Для крупной и растущей организации `10.0.0.0/8` предоставляет удобное пространство для иерархического планирования.

Это не означает, что весь `/8` следует использовать как одну subnet. Он является parent allocation для множества smaller prefixes.

Следует проверить overlap с:

- mergers и acquisitions;
- VPN partners;
- cloud VNets/VPCs;
- remote workers;
- lab environments.

## Требования Castle Rysen Coffee

Пример assumptions:

| Site type | Count | Planning capacity |
| --- | ---: | ---: |
| Central Office | 1 | около 4,000 addresses |
| Fallout Shelter | 30 | около 500 addresses каждый |
| District Shop per Shelter | до 50 | около 50 addresses каждый |

Planning capacity не обязана означать одну broadcast domain. Это site allocation, который позже делится на VLANs с помощью VLSM.

## Central Office

Для примерно 4,000 addresses:

```text
2^11 = 2048   insufficient
2^12 = 4096   sufficient
```

Site block:

```text
10.0.0.0/20
```

Range:

```text
Network:   10.0.0.0
Last:      10.0.15.255
Addresses: 4096
```

Этот `/20` не должен автоматически становиться одной VLAN. Его можно разделить, например, на:

- employee VLANs;
- voice;
- wireless;
- servers;
- management;
- cameras;
- guest;
- infrastructure.

## Размер Regional Group

Один regional group содержит:

```text
1 shelter
50 district shops
```

### Shelter

Для около 500 addresses:

```text
/23 = 512 total, 510 traditional usable
```

### District Shop

Для около 50 addresses:

```text
/26 = 64 total, 62 traditional usable
```

### Raw Capacity

```text
Shelter:       1 * 512 = 512
District shops: 50 * 64 = 3200
Total used:              3712
```

Следующая power-of-two block:

```text
4096 addresses = /20
```

Поэтому каждому shelter и его shops выделяется один regional `/20`.

## Почему `/20` Лучше Точного Уплотнения

Regional `/20` предоставляет:

```text
4096 addresses
```

Текущий plan использует:

```text
3712 addresses
```

Резерв:

```text
4096 - 3712 = 384 addresses
```

Он может использоваться для:

- WAN/transit links;
- management;
- regional services;
- additional shops;
- growth;
- migration overlap;
- future VLANs.

Главное преимущество:

```text
Один regional group = один clean /20 summary
```

## Regional Group 1

Summary:

```text
10.0.16.0/20
```

Range:

```text
10.0.16.0 - 10.0.31.255
```

### Shelter 1

```text
10.0.16.0/23
```

Range:

```text
10.0.16.0 - 10.0.17.255
```

### Shops 1-50

Первый shop:

```text
10.0.18.0/26
```

Каждый следующий `/26` увеличивается на 64 addresses.

| Shop | Network |
| ---: | --- |
| 1 | `10.0.18.0/26` |
| 2 | `10.0.18.64/26` |
| 3 | `10.0.18.128/26` |
| 4 | `10.0.18.192/26` |
| 5 | `10.0.19.0/26` |
| ... | ... |
| 49 | `10.0.30.0/26` |
| 50 | `10.0.30.64/26` |

Последний shop занимает:

```text
10.0.30.64 - 10.0.30.127
```

### Reserved Space

Свободно внутри regional `/20`:

```text
10.0.30.128 - 10.0.31.255
```

CIDR decomposition:

```text
10.0.30.128/25
10.0.31.0/24
```

Этот резерв и позволяет следующему regional group начаться на clean boundary:

```text
10.0.32.0/20
```

## Regional Pattern

`/20` increment в третьем octet равен:

```text
16
```

Первые groups:

| Group | Summary |
| ---: | --- |
| Central Office | `10.0.0.0/20` |
| Regional 1 | `10.0.16.0/20` |
| Regional 2 | `10.0.32.0/20` |
| Regional 3 | `10.0.48.0/20` |
| Regional 4 | `10.0.64.0/20` |
| ... | ... |
| Regional 15 | `10.0.240.0/20` |
| Regional 16 | `10.1.0.0/20` |

После `10.0.240.0/20` происходит rollover во второй octet.

Для 30 regional groups последний:

```text
Regional 30 = 10.1.224.0/20
```

## Общий Parent Для Первой Фазы

Central `/20` плюс 30 regional `/20` blocks:

```text
31 * 4096 = 126,976 addresses
```

Aligned parent:

```text
10.0.0.0/15
```

Range:

```text
10.0.0.0 - 10.1.255.255
```

После allocation до `10.1.239.255` остаётся:

```text
10.1.240.0/20
```

внутри `/15`.

Это не означает, что enterprise обязан рекламировать `/15` везде. Summary зависит от topology и failure domains.

## Hierarchical Addressing

Хорошая схема кодирует структуру:

```text
Enterprise
  -> Region
    -> Site
      -> VLAN / function
```

Преимущества:

- проще читать routes;
- легче делегировать ownership;
- удобнее агрегировать prefixes;
- проще расследовать incidents;
- expansion следует повторяемому pattern;
- site redesign не ломает глобальную иерархию.

## Внутреннее Деление Site Blocks

Site allocation является container, а не одной subnet.

Пример Central Office `/20`:

| Function | Example prefix |
| --- | --- |
| Employees | `/22` |
| Guest | `/22` |
| Servers | `/23` |
| Voice | `/23` |
| Cameras | `/24` |
| Management | `/24` |
| Infrastructure | `/25` |
| Reserve | remaining aligned blocks |

Фактические размеры определяются discovery, а не этой примерной таблицей.

## Route Summarization

Regional group 1 может включать много routes:

```text
10.0.16.0/23
10.0.18.0/26
10.0.18.64/26
...
10.0.30.64/26
```

На boundary region они могут суммироваться как:

```text
10.0.16.0/20
```

Только если:

- все covered routes находятся за этим region;
- нет более specific route через другой path;
- summary не создаёт black hole без корректной discard route/policy;
- failure behavior понятен.

## Re-addressing Как Проект

Переадресация затрагивает:

- DHCP scopes;
- static devices;
- router interfaces;
- firewall rules и objects;
- ACLs;
- NAT;
- DNS;
- monitoring;
- certificates и allowlists;
- VPN selectors;
- routing;
- documentation;
- application dependencies.

Это migration program, а не только subnet calculation.

## Migration Phases

### 1. Discovery

- inventory addresses;
- identify owners;
- find static assignments;
- map VLANs и routes;
- detect overlaps;
- baseline traffic.

### 2. Design

- approve hierarchy;
- size site containers;
- assign VLAN prefixes;
- plan summaries;
- define naming и IPAM fields.

### 3. Validation

- model in lab;
- validate routing;
- test DHCP, DNS, NAT и security policy;
- confirm rollback.

### 4. Pilot

- migrate low-risk site;
- measure outages;
- update runbook;
- resolve hidden dependencies.

### 5. Rollout

- migrate by region/site;
- maintain change windows;
- verify after each stage;
- retire old routes deliberately.

### 6. Closeout

- remove temporary config;
- reconcile IPAM;
- update diagrams;
- capture lessons learned.

## Cutover Checklist

- [ ] New VLANs and SVIs configured.
- [ ] DHCP scopes created and excluded ranges correct.
- [ ] Routing and summaries staged.
- [ ] Firewall/ACL/NAT updated.
- [ ] DNS changes prepared.
- [ ] Static devices mapped.
- [ ] Monitoring accepts new ranges.
- [ ] Remote access path preserved.
- [ ] Rollback commands tested.
- [ ] Old and new networks coexistence understood.
- [ ] Post-change tests assigned.

## Проверка Address Plan

Для каждого allocation:

- correct network boundary;
- sufficient capacity;
- no overlap;
- contained in parent;
- gateway reserved;
- DHCP range documented;
- growth reserve;
- summary relationship;
- owner и purpose;
- lifecycle status.

## Автоматическая Проверка

Python может проверить regional pattern:

```python
from ipaddress import ip_network

enterprise = ip_network("10.0.0.0/15")
groups = list(enterprise.subnets(new_prefix=20))

central = groups[0]
regions = groups[1:31]

print(central)
print(regions[0])
print(regions[-1])
```

Ожидается:

```text
10.0.0.0/20
10.0.16.0/20
10.1.224.0/20
```

## Практическое Задание

Для нового region требуется:

- 1 hub на 900 addresses;
- 20 branches по 100 addresses;
- 40 kiosks по 25 addresses;
- 20 WAN links по 2 addresses;
- минимум 20% адресного резерва.

Задачи:

1. Выбрать prefixes.
2. Рассчитать raw total.
3. Выбрать aligned regional container.
4. Предложить largest-first allocation.
5. Определить summary.

### Возможный Ответ

```text
Hub:      /22 = 1024 addresses
Branches: /25 = 128 each -> 2560
Kiosks:   /27 = 32 each  -> 1280
WAN:      /30 = 4 each   -> 80
Raw total: 4944
```

С 20% reserve:

```text
4944 * 1.2 = 5932.8
```

Следующий power-of-two container:

```text
8192 addresses = /19
```

Конкретное размещение должно начинаться на `/19` boundary и проверяться на fragmentation.

## Частые Ошибки

### Считать Людей Вместо Devices

Headcount является входом для discovery, но не окончательной capacity.

### Делать Site Allocation Одной VLAN

Container prefix предназначен для дальнейшего subnetting.

### Уплотнять Без Резерва

Это осложняет рост и summarization.

### Резервировать Без Обоснования

Headroom должен соответствовать forecast и architecture.

### Игнорировать Alignment

Красивое число не обязательно является valid network boundary.

### Обещать Summary Без Topology

Aggregation должна отражать реальные paths.

### Забывать External Overlap

Private ranges могут конфликтовать через VPN, cloud или acquisition.

### Рассматривать Renumbering Только Как Routing Change

Зависимости существуют в security, DNS, applications и operations.

## Контрольные Вопросы

### Вопрос 1

Почему 200 сотрудников не означают 200 addresses?

Ответ:

```text
У пользователей несколько devices, а инфраструктура и services
также потребляют addresses.
```

### Вопрос 2

Какой block предоставляет около 4,000 addresses?

Ответ:

```text
/20, содержащий 4096 total addresses.
```

### Вопрос 3

Почему shelter и 50 shops удобно помещать в `/20`?

Ответ:

```text
Их raw blocks используют 3712 addresses, а /20 предоставляет 4096,
оставляя reserve и clean summary boundary.
```

### Вопрос 4

Где заканчивается shop 50 при начале shops с `10.0.18.0/26`?

Ответ:

```text
Shop 50 равен 10.0.30.64/26 и заканчивается 10.0.30.127.
```

### Вопрос 5

Что позволяет следующему group начаться с `10.0.32.0/20`?

Ответ:

```text
Сознательный reserve 10.0.30.128 - 10.0.31.255
внутри первого regional /20.
```

## Команды и Термины

| Термин | Значение |
| --- | --- |
| Site container | Parent prefix для внутренних VLANs site. |
| Regional block | Contiguous allocation для region и его sites. |
| Headroom | Обоснованный резерв для роста. |
| Hierarchical addressing | Схема, отражающая enterprise structure. |
| Summary route | Aggregate route для contiguous child prefixes. |
| Re-addressing | Migration существующих systems на новую IP scheme. |
| IPAM | Source of truth для address allocations. |
| RFP | Документ с business и technical requirements. |

## Что Повторить Позже

- VLSM
- Route summarization
- RFC 1918
- IPAM
- DHCP migration
- Routing design
- Renumbering runbooks
- IPv6 address planning

