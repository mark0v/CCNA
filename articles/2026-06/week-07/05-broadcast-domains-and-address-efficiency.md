# Broadcast Domains и эффективность адресного пространства

Source: закрытая страница курса  
Date added: 2026-06-13  
Related plan item: Week 7 / Broadcast domains and address efficiency  
Tags: subnetting, broadcast domain, ARP, DHCP, point-to-point, address efficiency, subnet sizing
Language: Russian
Translation pair: articles-en/2026-06/week-07/05-broadcast-domains-and-address-efficiency.md

## Кратко

Subnetting решает две фундаментальные задачи:

1. Делит слишком большие broadcast domains на управляемые сегменты.
2. Выделяет каждому сегменту столько IP addresses, сколько ему действительно нужно.

Большая flat network заставляет множество устройств принимать локальные broadcasts и расширяет область воздействия ошибок. Слишком крупная subnet на маленьком link, напротив, тратит address space. Хороший design выбирает размер сети по назначению, количеству endpoints и ожидаемому росту.

## Ключевые идеи

- IPv4 broadcast остаётся внутри Layer 2 broadcast domain.
- ARP и начальные этапы DHCP используют broadcast.
- Router не пересылает Layer 2 broadcasts между обычными routed interfaces.
- Разделение на VLANs и subnets ограничивает область broadcast traffic.
- Меньший broadcast domain упрощает policy, troubleshooting и fault isolation.
- Размер subnet должен соответствовать реальному числу endpoints.
- `/24` предоставляет 256 total addresses и традиционно 254 usable host addresses.
- `/30` предоставляет 4 total addresses и традиционно 2 usable addresses.
- `/31` может использовать оба addresses на IPv4 point-to-point link согласно RFC 3021.
- Public IPv4 space особенно важно не расходовать без необходимости.
- Самая маленькая возможная subnet не всегда является лучшим operational choice.

## Причина 1. Контроль Broadcast Domain

Broadcast предназначен для всех устройств в локальном broadcast domain.

Примеры IPv4 и Ethernet mechanisms, связанных с broadcast:

- ARP request для поиска MAC address известного IPv4 host;
- DHCP Discover, когда client ещё не знает DHCP server;
- DHCP Request в некоторых стадиях lease process;
- некоторые discovery и legacy protocols;
- unknown destination behavior на Layer 2 до изучения MAC address.

Каждый broadcast не обязательно создаёт серьёзную нагрузку. Проблема появляется, когда один domain становится слишком большим, содержит много активных endpoints или включает noisy/defective devices.

## ARP как пример

Host `192.168.10.21/24` хочет отправить packet соседу `192.168.10.50`.

Он должен узнать destination MAC:

```text
Who has 192.168.10.50?
Tell 192.168.10.21.
```

ARP request отправляется как Ethernet broadcast:

```text
ff:ff:ff:ff:ff:ff
```

Все устройства этого Layer 2 segment получают frame, хотя ответить должен только владелец адреса.

Если destination находится в другой subnet, host ищет MAC своего default gateway, а router затем пересылает Layer 3 packet в другую network. Исходный ARP broadcast не проходит через router как обычный broadcast.

## DHCP как пример

Новый client до получения адреса не знает:

- собственного IPv4 address;
- DHCP server address;
- default gateway;
- subnet mask.

Поэтому начальный DHCP Discover использует broadcast.

```text
Client -> DHCP Discover -> local broadcast domain
```

Если DHCP server находится в другой subnet, router или Layer 3 switch может использовать DHCP relay, например `ip helper-address`. Relay преобразует локальный client request в routable exchange к server.

Subnet boundary ограничивает исходный broadcast, но не мешает централизованному DHCP при корректной relay configuration.

## Почему одна гигантская сеть неудобна

Допустим, организация использует:

```text
10.0.0.0/8
```

как одну flat subnet.

Теоретически это огромное число addresses. Практически один такой broadcast domain был бы крайне плохим design:

- broadcasts достигают огромного числа endpoints;
- ARP tables и Layer 2 state становятся крупнее;
- spanning-tree и switching incidents имеют большой blast radius;
- guest, office, cameras и payment devices находятся слишком близко;
- применение security policy требует дополнительных механизмов внутри общего segment;
- troubleshooting становится менее локализованным;
- duplicate IP или loop может затронуть слишком много users.

Наличие большого allocation не означает, что его нужно использовать как одну subnet.

## Subnet и Broadcast Domain

В типичном enterprise design:

```text
One VLAN = one Layer 2 broadcast domain
One VLAN = one primary IP subnet
```

Пример:

| VLAN | Назначение | Subnet |
| ---: | --- | --- |
| 10 | Office | `10.20.10.0/24` |
| 20 | POS | `10.20.20.0/27` |
| 30 | Cameras | `10.20.30.0/26` |
| 40 | Guest | `10.20.40.0/23` |

Router, multilayer switch или firewall выполняет forwarding между этими networks и становится точкой применения policy.

Subnetting само по себе не создаёт security: если inter-VLAN routing разрешает всё, segments всё ещё могут общаться. Но subnet boundaries дают места, где policy можно выразить и контролировать.

## Не все Broadcasts одинаковы

Важно не превращать правило «broadcasts плохие» в догму.

Нормальные broadcasts являются частью работы IPv4 LAN. Современная switched network обычно справляется с разумным их количеством.

Размер segment выбирают с учётом:

- числа endpoints;
- broadcast и multicast behavior applications;
- wireless client density;
- ARP/neighbor scale;
- fault isolation;
- security zones;
- device capabilities;
- operational simplicity.

Цель не в полном устранении broadcast, а в контроле его scope.

## Причина 2. Эффективное использование адресов

Каждый subnet allocation занимает целый aligned block.

Если link соединяет только два router interfaces, использование `/24` означает:

```text
Total addresses: 256
Traditional usable: 254
Required endpoints: 2
```

Большая часть блока не используется.

Для private addresses это может казаться неважным, но плохое планирование:

- фрагментирует allocation;
- мешает summarization;
- создаёт inconsistency;
- усложняет growth;
- формирует плохие привычки перед работой с public space.

Для public IPv4 waste имеет прямую стоимость и ограничивает доступный ресурс.

## `/30` для Point-to-Point Link

Традиционный IPv4 point-to-point subnet:

```text
192.0.2.0/30
```

Содержит:

| Address | Роль |
| --- | --- |
| `192.0.2.0` | Network address |
| `192.0.2.1` | Router A |
| `192.0.2.2` | Router B |
| `192.0.2.3` | Broadcast address |

Результат:

```text
4 total addresses
2 traditional usable addresses
```

Это хорошо соответствует link с двумя IPv4 endpoints и широко поддерживается.

## `/31` и RFC 3021

Современные point-to-point links часто используют `/31`:

```text
192.0.2.0/31
```

Addresses:

```text
192.0.2.0
192.0.2.1
```

RFC 3021 позволяет использовать оба address как interface addresses, потому что на point-to-point link нет необходимости в традиционных network и broadcast semantics.

Преимущества:

- два addresses вместо четырёх;
- отсутствие двух потерянных addresses на каждый link;
- особенно заметная экономия при большом числе WAN links.

Перед использованием нужно проверить:

- поддержку обоими устройствами;
- требования провайдера;
- monitoring и management tools;
- routing protocol behavior;
- operational standards организации.

Для beginner labs `/30` часто проще, но важно знать, что `/31` является нормальным современным вариантом.

## Сравнение размеров

| Prefix | Total addresses | Traditional usable hosts | Типичный пример |
| --- | ---: | ---: | --- |
| `/24` | 256 | 254 | User LAN |
| `/26` | 64 | 62 | Cameras |
| `/27` | 32 | 30 | POS |
| `/28` | 16 | 14 | Infrastructure |
| `/30` | 4 | 2 | Traditional point-to-point |
| `/31` | 2 | 2 on point-to-point | Efficient point-to-point |
| `/32` | 1 | Single host route | Loopback or host route |

Таблица не является автоматическим design guide. Назначение prefix зависит от требований.

## Custom Fit вместо привычки

Неправильный подход:

```text
Мы всегда используем /24.
```

Более зрелый подход:

```text
Сколько endpoints требуется?
Каков growth?
Какой traffic pattern?
Какая policy boundary нужна?
Как этот range вписывается в parent allocation?
Можно ли summarise routes?
```

После этого выбирается prefix.

## Пример NetworkChuck Coffee

Требования:

| Segment | Endpoints | Growth target |
| --- | ---: | ---: |
| Guest Wi-Fi | 80 | 120 |
| Employees | 18 | 28 |
| POS | 8 | 12 |
| Cameras | 24 | 40 |
| Router link | 2 | 2 |

Кандидаты:

| Segment | Prefix | Capacity rationale |
| --- | --- | --- |
| Guest Wi-Fi | `/25` | 126 traditional usable |
| Employees | `/27` | 30 traditional usable |
| POS | `/28` | 14 traditional usable |
| Cameras | `/26` | 62 traditional usable |
| Router link | `/30` or `/31` | Two endpoints |

Prefix выбирается не только по текущему числу hosts. Guest Wi-Fi может требовать более крупный DHCP pool из-за высокой сменяемости clients, а infrastructure subnet может резервировать addresses для redundancy.

## Broadcast Reduction не равно уменьшению Internet Traffic

Разделение subnet не уменьшает автоматически application traffic, который должен идти между networks или в Internet.

Оно:

- ограничивает Layer 2 broadcasts;
- заставляет inter-subnet traffic проходить через Layer 3 device;
- создаёт policy and observation points;
- локализует failures.

Если applications постоянно общаются между segments, routed traffic останется. Поэтому segmentation должна учитывать communication flows.

## Цена слишком мелкого деления

Чрезмерное количество tiny subnets тоже создаёт overhead:

- больше VLANs и SVIs;
- больше DHCP scopes;
- больше routes;
- больше ACL/firewall rules;
- больше documentation;
- сложнее migrations и troubleshooting;
- выше риск исчерпания маленького segment.

Subnetting оптимизирует design, а не требует сделать каждую возможную network минимальной.

## Network и Broadcast Addresses

В традиционной IPv4 subnet:

- первый address идентифицирует network;
- последний address является directed broadcast address;
- промежуточные addresses назначаются interfaces.

Для:

```text
192.168.50.0/24
```

получаем:

```text
Network:    192.168.50.0
First host: 192.168.50.1
Last host:  192.168.50.254
Broadcast:  192.168.50.255
```

Исключения:

- `/31` на point-to-point по RFC 3021;
- `/32`, представляющий один address;
- platform-specific или protocol-specific use cases.

## Практическое упражнение

Дано:

```text
Parent block: 10.60.0.0/23
```

Нужно разместить:

- Guest Wi-Fi: 100 endpoints.
- Cameras: 45 endpoints.
- POS: 12 endpoints.
- Management: 10 endpoints.
- Два point-to-point links.

Задача:

1. Выбрать prefixes с разумным запасом.
2. Решить, использовать `/30` или `/31` для links.
3. Разместить blocks от largest к smallest.
4. Записать network и broadcast для обычных subnets.
5. Убедиться в отсутствии overlap.
6. Оставить contiguous free space.

Возможные размеры:

```text
Guest:      /25
Cameras:    /26
POS:        /28
Management: /28
Links:      /30 or /31
```

## Порядок проверки дизайна

1. Подтвердить endpoint requirements.
2. Добавить growth reserve.
3. Выбрать smallest practical prefix.
4. Проверить alignment network boundary.
5. Проверить отсутствие overlap.
6. Проверить gateway и infrastructure reservations.
7. Проверить DHCP capacity.
8. Проверить broadcast-domain intent.
9. Проверить route summarization.
10. Задокументировать allocation.

## Частые ошибки

### Считать любую большую сеть broadcast storm

Большой domain увеличивает риск и scope, но фактическая нагрузка зависит от devices и traffic.

### Считать subnetting полноценной security policy

Segmentation создаёт boundary, но доступ определяется routing и firewall/ACL rules.

### Всегда выбирать минимальный prefix

Нужен запас для growth и operations.

### Всегда использовать `/30` на point-to-point

`/30` корректен, но `/31` может быть эффективнее при поддержке.

### Использовать `/31` без проверки

Standards, tools или provider design могут требовать `/30`.

### Игнорировать parent allocation

Даже правильно рассчитанные child subnets должны помещаться в выделенный block.

## Контрольные вопросы

### Вопрос 1

Какие две основные задачи решает subnetting?

Ответ:

```text
Ограничивает broadcast domains и распределяет address space
в соответствии с потребностями segments.
```

### Вопрос 2

Почему ARP request получает весь local segment?

Ответ:

```text
Потому что неизвестный destination MAC ищется с помощью
Ethernet broadcast внутри Layer 2 domain.
```

### Вопрос 3

Почему `/24` не подходит для link с двумя endpoints?

Ответ:

```text
Он выделяет 256 addresses для задачи, которой нужны только два.
```

### Вопрос 4

Чем `/31` отличается от традиционного `/30`?

Ответ:

```text
На поддерживаемом point-to-point link оба address `/31`
используются endpoints без отдельных network и broadcast addresses.
```

### Вопрос 5

Уменьшает ли subnetting весь network traffic?

Ответ:

```text
Нет. Оно ограничивает Layer 2 broadcast scope,
но необходимый routed application traffic сохраняется.
```

## Команды и термины

| Термин | Назначение |
| --- | --- |
| Broadcast domain | Layer 2 scope, получающий broadcast frames. |
| ARP | Сопоставляет IPv4 address с MAC address в local segment. |
| DHCP relay | Пересылает DHCP exchange между subnets. |
| Point-to-point | Link ровно между двумя Layer 3 endpoints. |
| `/30` | Traditional point-to-point subnet с двумя usable hosts. |
| `/31` | RFC 3021 point-to-point subnet с двумя usable addresses. |
| Network address | Идентификатор traditional subnet. |
| Broadcast address | Последний address traditional IPv4 subnet. |
| Address efficiency | Соответствие размера allocation реальной потребности. |
| Blast radius | Область воздействия failure или incident. |

## Что повторить позже

- ARP process
- DHCP DORA
- DHCP relay
- Ethernet broadcasts
- VLAN boundaries
- `/30`, `/31` и `/32`
- VLSM allocation
- Route summarization
