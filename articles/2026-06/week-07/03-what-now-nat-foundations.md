# Что дальше? Закрепляем основы NAT

Source: закрытая страница курса  
Date added: 2026-06-13  
Related plan item: Week 7 / NAT foundations checkpoint  
Tags: NAT, PAT, static NAT, dynamic NAT, Packet Tracer, troubleshooting, RFC 1918
Language: Russian
Translation pair: articles-en/2026-06/week-07/03-what-now-nat-foundations.md

## Кратко

Этот checkpoint объединяет изученные варианты Network Address Translation: static NAT, dynamic NAT и PAT/NAT overload. Главный результат блока состоит не в запоминании отдельных команд, а в понимании полного пути traffic через границу между private и public networks.

Теперь нужно закрепить материал самостоятельно: собрать topology в Packet Tracer, настроить маршрутизацию и NAT, проверить translations, намеренно внести ошибки и восстановить connectivity по последовательному плану.

## Ключевые идеи

- RFC 1918 addresses предназначены для private networks и не распространяются в глобальной Internet routing table.
- NAT меняет address representation при пересечении network boundary.
- Static NAT создаёт постоянное one-to-one mapping.
- Dynamic NAT временно выдаёт public address из пула.
- PAT позволяет множеству flows совместно использовать один или несколько public addresses.
- Outbound translation и inbound service publishing решают разные задачи.
- ACL в NAT configuration классифицирует source addresses.
- `ip nat inside` и `ip nat outside` определяют стороны translation.
- NAT не исправляет отсутствующие routes и не заменяет firewall.
- Upstream routing и filtering являются частью end-to-end path.
- Умение диагностировать сломанную конфигурацию важнее механического повторения команд.

## Что уже изучено

После блока NAT ты можешь объяснить и настроить:

- зачем private hosts требуется translation для обычного доступа в public Internet;
- разницу между inside local и inside global;
- роли inside и outside interfaces;
- static one-to-one translation;
- static port translation для публикации service;
- dynamic NAT с ACL и public pool;
- PAT с pool overload;
- PAT на address внешнего interface;
- проверку через `show ip nat translations`;
- диагностику через routing, ACL counters и NAT statistics.

## Private addresses и Internet

Private IPv4 ranges:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

не обладают специальным свойством, из-за которого packet физически не может покинуть LAN. Router способен переслать такой packet, если routing и policy это позволяют.

Проблема в другом:

- RFC 1918 prefixes не должны объявляться в global routing table;
- Internet routers не имеют нормального глобального return route к конкретной private network;
- providers и network operators обычно фильтруют spoofed или inappropriate source addresses;
- одинаковые private ranges одновременно используются миллионами независимых networks.

Поэтому packet с source `192.168.10.21` не может рассчитывать на нормальный end-to-end обмен через public Internet. NAT/PAT заменяет private source representation на routable public address, связанный с edge network.

## Три основных варианта NAT

### Static NAT

```text
192.168.10.50 <-> 216.0.5.20
```

Используется, когда внутреннему host требуется постоянная public identity.

Типичные задачи:

- публикация internal server;
- predictable inbound destination;
- устройство, которому нужен dedicated public source address;
- legacy integration.

Static NAT сам по себе не является firewall permission. Public routing и security policy всё равно должны разрешать нужный traffic.

### Dynamic NAT

```text
Inside networks -> ACL -> public address pool
```

Пример правила:

```cisco
ip nat inside source list 1 pool cafepublic
```

Router временно назначает каждому active inside host свободный address из пула. Каждая активная translation остаётся one-to-one, поэтому scalability ограничена количеством public addresses.

### PAT / NAT Overload

```text
many inside flows -> one or a few public addresses
```

Пример:

```cisco
ip nat inside source list 1 interface GigabitEthernet0/2 overload
```

PAT различает translations по protocol и transport port или identifier information. Это типичный вариант для общего internet access.

## Outbound access и inbound publishing

Эти направления нельзя смешивать в одну абстрактную задачу «настроить NAT».

### Outbound client access

Внутренние клиенты инициируют connections:

```text
Inside client -> edge router -> Internet service
```

Обычно применяется PAT:

```text
192.168.10.21:51001 -> 216.0.5.2:30001
```

### Inbound service publishing

Внешний client инициирует connection к заранее опубликованному адресу или порту:

```text
Internet client -> public IP/port -> internal server
```

Пример static PAT:

```cisco
ip nat inside source static tcp 192.168.10.50 443 216.0.5.20 443
```

Публикация требует особенно внимательной firewall policy, hardening, monitoring и часто отдельной DMZ.

## Самостоятельная лаборатория

Собери topology:

```text
Inside LAN
    |
Customer Edge Router
    |
ISP Router
    |
Outside Test Network / Loopback
```

Рекомендуемые элементы:

- минимум два inside clients;
- edge router с inside и outside interfaces;
- отдельный ISP router;
- outside server или loopback test address;
- private addressing внутри;
- documentation table с interfaces и prefixes.

### Пример addressing

| Устройство | Interface | Address | Роль |
| --- | --- | --- | --- |
| PC1 | NIC | `192.168.10.21/24` | Inside client |
| PC2 | NIC | `192.168.10.22/24` | Inside client |
| EDGE | Gi0/0 | `192.168.10.1/24` | NAT inside |
| EDGE | Gi0/2 | `216.0.5.2/24` | NAT outside |
| ISP | Gi0/0 | `216.0.5.1/24` | Upstream |
| ISP | Loopback0 | `203.0.113.10/32` | Test destination |

Адреса из documentation ranges используются здесь только для лаборатории.

## Этап 1. Проверить routing до NAT

До настройки translation:

1. Проверить local addressing.
2. Проверить default gateway clients.
3. Проверить interface status.
4. Проверить connected routes.
5. Настроить default route на edge router.
6. Проверить, что edge router достигает outside test address со своего outside address.

Пример:

```cisco
ip route 0.0.0.0 0.0.0.0 216.0.5.1
```

Важно отделять routing problem от NAT problem. Если edge router сам не достигает outside network, PAT не исправит путь.

## Этап 2. Настроить PAT

```cisco
interface GigabitEthernet0/0
 ip nat inside

interface GigabitEthernet0/2
 ip nat outside

access-list 1 permit 192.168.10.0 0.0.0.255

ip nat inside source list 1 interface GigabitEthernet0/2 overload
```

Сгенерировать traffic от обоих clients и проверить:

```cisco
show ip nat translations
show ip nat statistics
show access-lists 1
```

Ожидаемый результат: разные inside local addresses используют один inside global address с различающимися ports или identifiers.

## Этап 3. Добавить Static NAT или Static PAT

Добавь internal server:

```text
192.168.10.50
```

Вариант полного static NAT:

```cisco
ip nat inside source static 192.168.10.50 216.0.5.20
```

Вариант публикации только HTTPS:

```cisco
ip nat inside source static tcp 192.168.10.50 443 216.0.5.20 443
```

Проверь:

- достигается ли public address со стороны ISP;
- маршрутизируется ли `216.0.5.20` к edge router;
- запущен ли service на internal server;
- разрешён ли traffic security policy;
- возвращается ли reply через тот же edge.

## Моделирование ISP filtering

В реальных networks source validation может выполняться разными механизмами:

- infrastructure ACL;
- uRPF;
- anti-spoofing policy;
- provider edge filters;
- routing policy.

В Packet Tracer можно добавить ACL на ISP-facing interface, чтобы лабораторно показать отказ traffic с RFC 1918 source addresses. Но важно понимать: конкретная конфигурация провайдера не сводится к одной универсальной команде «block private addresses».

Цель lab:

1. Показать, что routing и policy могут переслать или отбросить packet.
2. Показать, что private source не имеет нормального global return path.
3. Убедиться, что после PAT outside network видит public source.

## Намеренно сломай конфигурацию

После рабочего baseline вноси по одной ошибке.

### Ошибка 1. Удалить `ip nat inside`

```cisco
interface GigabitEthernet0/0
 no ip nat inside
```

Наблюдение:

- ACL может совпадать;
- routing может существовать;
- translation не создаётся правильно, потому что NAT boundary не определена.

### Ошибка 2. Неверная wildcard mask

```cisco
access-list 1 permit 192.168.10.0 0.0.0.0
```

Такое правило совпадает только с точным address `192.168.10.0`, а не со всей `/24`.

### Ошибка 3. Неверный outside interface в overload rule

Проверить:

```cisco
show ip interface brief
show running-config | include ip nat
```

### Ошибка 4. Удалить default route

NAT entries не заменяют forwarding path.

### Ошибка 5. Изменить client default gateway

Packet может вообще не достичь NAT router.

### Ошибка 6. Заблокировать traffic на upstream

NAT может работать корректно, но policy дальше по path всё равно отбрасывает packet.

### Ошибка 7. Остановить published service

Успешная translation не доказывает, что application слушает нужный port.

## Системный порядок диагностики

Когда NAT не работает, не начинай со случайного повторного ввода команд.

1. Проверить source host IP, mask и gateway.
2. Проверить local interface state.
3. Проверить route lookup к destination.
4. Проверить return path.
5. Определить ingress и egress interfaces.
6. Проверить `ip nat inside` и `ip nat outside`.
7. Проверить соответствие source address ACL.
8. Проверить ACL hit counters.
9. Проверить NAT rule и наличие `overload`, pool или static mapping.
10. Проверить `show ip nat translations`.
11. Проверить `show ip nat statistics`.
12. Проверить reachability next hop и outside destination.
13. Проверить upstream filtering.
14. Проверить firewall policy.
15. Проверить DNS отдельно от IP connectivity.
16. Проверить application service и listening port.

## Основные команды проверки

```cisco
show ip interface brief
show ip route
show access-lists
show ip nat translations
show ip nat statistics
show running-config | include ip nat
show running-config | section interface
ping
traceroute
```

Для production troubleshooting также полезны logs, counters, packet captures и platform-specific commands. `debug ip nat` может создавать значительную нагрузку и объём output, поэтому его используют осторожно и ограниченно.

## Как читать результат

### ACL counters не растут

Вероятные причины:

- source address не входит в ACL;
- traffic не проходит через ожидаемый router;
- неверная wildcard mask;
- проверяется не тот flow.

### ACL counters растут, translations отсутствуют

Проверить:

- interface roles;
- NAT rule;
- pool/interface reference;
- platform errors;
- направление traffic.

### Translation есть, но ответа нет

Проверить:

- outside routing;
- provider filtering;
- destination reachability;
- return path;
- firewall;
- application.

### Ping по IP работает, имя не открывается

Вероятна DNS problem, а не NAT failure.

### Один client работает, другой нет

Проверить:

- ACL coverage;
- client gateway;
- VLAN/routing;
- pool exhaustion для dynamic NAT;
- platform/session limits для PAT.

## NAT не является security boundary сам по себе

Private addressing и PAT уменьшают прямую address visibility, но не заменяют:

- firewall;
- network segmentation;
- endpoint security;
- authentication;
- encryption;
- patch management;
- monitoring;
- least-privilege access.

Static mapping, публикующий service, увеличивает attack surface и должен сопровождаться explicit policy.

## Практический план закрепления

### Проход 1: точное повторение

- Воспроизвести working topology.
- Настроить routing.
- Настроить PAT.
- Проверить translations.
- Добавить static mapping.

### Проход 2: изменить адреса

- Использовать другие private subnets.
- Изменить outside subnet.
- Пересчитать wildcard masks.
- Обновить routes и ACL.

### Проход 3: добавить сегмент

- Guest Wi-Fi.
- Business LAN.
- Camera network.
- Отдельный server segment.

Определи, какие networks должны получать outbound NAT и какие не должны.

### Проход 4: диагностика

- Сломать один элемент.
- Предсказать симптом.
- Подтвердить его show commands.
- Исправить причину.
- Записать наблюдение.

### Проход 5: объяснение

Объясни без подсказки:

```text
Как packet меняется от inside client до outside server
и как reply возвращается правильному host.
```

Если объяснение точное и подтверждается output, тема перестаёт быть набором команд.

## NAT Foundations Checklist

- [ ] Понимаю, почему RFC 1918 addresses не используются для normal global routing.
- [ ] Отличаю routing от address translation.
- [ ] Различаю inside local, inside global, outside local и outside global.
- [ ] Могу назначить inside/outside interface roles.
- [ ] Могу настроить static NAT.
- [ ] Могу настроить static PAT.
- [ ] Могу настроить dynamic NAT pool.
- [ ] Могу настроить interface overload.
- [ ] Понимаю ACL как classifier.
- [ ] Умею вычислить wildcard mask.
- [ ] Проверяю translations и statistics.
- [ ] Всегда проверяю return path.
- [ ] Отличаю NAT issue от DNS, routing, firewall и application issue.
- [ ] Планирую изменения NAT как потенциально прерывающие.
- [ ] Документирую topology и rationale.

## Контрольные вопросы

### Вопрос 1

Почему RFC 1918 address не подходит как source для обычного public Internet exchange?

Ответ:

```text
Private prefixes не распространяются глобально, не имеют уникального
public return path и обычно фильтруются на network boundaries.
```

### Вопрос 2

Чем static NAT отличается от PAT?

Ответ:

```text
Static NAT создаёт постоянное address mapping,
а PAT позволяет множеству flows совместно использовать public address.
```

### Вопрос 3

Что проверить, если ACL counter растёт, но translation не появляется?

Ответ:

```text
Inside/outside roles, NAT rule, pool или interface reference
и направление прохождения traffic.
```

### Вопрос 4

Доказывает ли translation table, что application работает?

Ответ:

```text
Нет. NAT может быть исправен, а service, firewall или return path неисправны.
```

### Вопрос 5

Зачем намеренно ломать лабораторию?

Ответ:

```text
Чтобы связать конкретную ошибку с наблюдаемым симптомом
и научиться находить причину системно.
```

## Команды и термины

| Команда / термин | Назначение |
| --- | --- |
| RFC 1918 | Private IPv4 address ranges. |
| Static NAT | Постоянное one-to-one address mapping. |
| Dynamic NAT | Временная выдача address из pool. |
| PAT | Совместное использование public address по flows. |
| `ip nat inside` | Обозначает внутреннюю сторону NAT. |
| `ip nat outside` | Обозначает внешнюю сторону NAT. |
| `show ip nat translations` | Показывает active translations. |
| `show ip nat statistics` | Показывает NAT configuration и counters. |
| `show access-lists` | Показывает matches ACL. |
| Return path | Путь ответа к исходному host. |
| Upstream filtering | Policy на следующем network boundary. |

## Что повторить позже

- Extended ACLs
- Stateful firewall
- NAT order of operations
- Hairpin NAT
- Twice NAT
- IPv6 и отказ от IPv4 NAT
- Packet captures
- Production change planning
