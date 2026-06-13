# Настройка PAT (NAT Overload)

Source: закрытая страница курса  
Date added: 2026-06-13  
Related plan item: Week 7 / PAT and NAT overload configuration  
Tags: PAT, NAT overload, interface overload, NAT pool, ACL, source port, Cisco IOS
Language: Russian
Translation pair: articles-en/2026-06/week-07/02-configuring-pat-nat-overload.md

## Кратко

PAT, или NAT overload, позволяет множеству внутренних устройств одновременно использовать один публичный IPv4-адрес или небольшой публичный пул. Маршрутизатор различает потоки не только по IP-адресам, но и по transport-layer ports; для ICMP используются identifiers.

Это наиболее распространённый вариант NAT для исходящего доступа пользователей в интернет. Домашние маршрутизаторы, небольшие офисы и многие корпоративные edge devices применяют именно PAT, потому что отдельный публичный адрес для каждого внутреннего клиента не требуется.

PAT можно настроить двумя основными способами:

```text
ACL -> public NAT pool -> overload
ACL -> outside interface address -> overload
```

Метод с interface особенно удобен, когда провайдер выдаёт публичный адрес динамически.

## Ключевые идеи

- Dynamic NAT создаёт активные соответствия one-to-one.
- PAT создаёт many-to-one или many-to-few translations.
- Ключевое слово `overload` разрешает совместное использование public address.
- Router различает TCP/UDP sessions по protocol и port numbers.
- Один inside host может одновременно создавать множество translations.
- ACL определяет внутренние source addresses, но не является здесь firewall rule.
- PAT может использовать NAT pool или IP-адрес outside interface.
- Interface overload автоматически использует текущий адрес интерфейса.
- Изменение NAT при активном трафике может прервать соединения.
- Перед удалением старого dynamic NAT rule может потребоваться очистить translations.
- Количество доступных sessions не следует считать просто равным 65 535 на адрес.
- NAT не заменяет routing, firewall и security policy.

## Dynamic NAT и PAT

Dynamic NAT:

```text
192.168.10.21 <-> 216.0.5.50
192.168.10.22 <-> 216.0.5.51
192.168.10.23 <-> 216.0.5.52
```

Каждый одновременно активный inside host занимает отдельный public address.

PAT:

```text
192.168.10.21:51001 -> 216.0.5.2:30001
192.168.10.22:51001 -> 216.0.5.2:30002
192.168.10.23:62000 -> 216.0.5.2:30003
```

Все клиенты представлены одним inside global address, а translations остаются уникальными благодаря protocol и port/identifier information.

| Свойство | Dynamic NAT | PAT / NAT overload |
| --- | --- | --- |
| Связь адресов | One-to-one | Many-to-one или many-to-few |
| Public resources | Один адрес на активный host | Один адрес для множества flows |
| Различение | По IP addresses | По IP, protocol и port/identifier |
| Типичное применение | Временные отдельные public identities | Общий internet access |
| Масштабируемость | Размер public pool | Port/translation capacity устройства |

## Как PAT различает соединения

Для TCP и UDP flow обычно определяется комбинацией:

```text
protocol
inside local IP and port
inside global IP and translated port
outside IP and port
```

Если два клиента используют одинаковый исходный port, router может изменить один из translated source ports:

```text
192.168.10.21:50000 -> 216.0.5.2:50000
192.168.10.22:50000 -> 216.0.5.2:50001
```

Для ICMP в translation table может использоваться query identifier, а не TCP/UDP port.

Поэтому название Port Address Translation удобно, но не следует считать, что механизм работает исключительно с TCP и UDP.

## Предварительные элементы

Как и другие варианты inside source NAT, PAT требует:

1. Рабочей IP addressing.
2. Маршрутов к внутренним и внешним сетям.
3. `ip nat inside` на внутренних интерфейсах.
4. `ip nat outside` на внешнем интерфейсе.
5. ACL, сопоставляющего eligible inside source addresses.
6. Правила NAT с ключевым словом `overload`.

Пример ролей:

```cisco
interface GigabitEthernet0/0
 description Cafe LAN
 ip nat inside

interface GigabitEthernet0/1
 description Fallout Shelter LAN
 ip nat inside

interface GigabitEthernet0/2
 description ISP uplink
 ip nat outside
```

Пример ACL:

```cisco
access-list 1 permit 192.168.10.0 0.0.0.255
access-list 1 permit 192.168.20.0 0.0.0.255
```

## Вариант 1. PAT с публичным пулом

Пусть уже существует pool:

```cisco
ip nat pool cafepublic 216.0.5.50 216.0.5.100 netmask 255.255.255.0
```

Обычный dynamic NAT использует:

```cisco
ip nat inside source list 1 pool cafepublic
```

Чтобы разрешить overload:

```cisco
ip nat inside source list 1 pool cafepublic overload
```

Ключевое слово `overload` меняет поведение. Public addresses теперь могут обслуживать множество одновременных translations вместо одного active inside host на адрес.

### Когда полезен pool overload

- Организация имеет несколько выделенных публичных адресов.
- Одного адреса недостаточно по session capacity.
- Требуется распределить translations по нескольким public identities.
- Политика или масштаб среды требует public pool.

Router обычно начинает использовать адреса пула по мере необходимости. Конкретное распределение зависит от платформы и IOS behavior, поэтому capacity нужно проверять по документации и измерениям.

## Вариант 2. PAT на outside interface

Для небольших сред чаще используется адрес самого внешнего интерфейса:

```cisco
ip nat inside source list 1 interface GigabitEthernet0/2 overload
```

Чтение команды:

```text
Для inside source addresses, совпавших с ACL 1,
использовать текущий IP address интерфейса GigabitEthernet0/2
и разрешить overload.
```

Полная конфигурация:

```cisco
enable
configure terminal

interface GigabitEthernet0/0
 description Cafe LAN
 ip nat inside

interface GigabitEthernet0/1
 description Fallout Shelter LAN
 ip nat inside

interface GigabitEthernet0/2
 description ISP uplink
 ip nat outside

access-list 1 permit 192.168.10.0 0.0.0.255
access-list 1 permit 192.168.20.0 0.0.0.255

ip nat inside source list 1 interface GigabitEthernet0/2 overload

end
```

## Почему interface overload удобен

Если ISP назначает outside address через DHCP, адрес может измениться:

```text
Yesterday: 198.51.100.20
Today:     198.51.100.47
```

Правило с interface reference не содержит жёстко заданного public IP:

```cisco
ip nat inside source list 1 interface GigabitEthernet0/2 overload
```

Router использует адрес, который сейчас настроен на `GigabitEthernet0/2`. После DHCP renewal NAT rule продолжает ссылаться на тот же interface.

Это не гарантирует отсутствие краткого разрыва при смене WAN address: существующие translations, связанные со старым адресом, больше не могут продолжаться как прежде. Но конфигурацию NAT не требуется вручную переписывать под новый IP.

## Переход с Dynamic NAT на PAT

Исходное правило:

```cisco
ip nat inside source list 1 pool cafepublic
```

Целевое правило с pool overload:

```cisco
ip nat inside source list 1 pool cafepublic overload
```

Или с interface overload:

```cisco
ip nat inside source list 1 interface GigabitEthernet0/2 overload
```

### Почему старое правило может не удалиться

При активных translations IOS может отказаться изменить или удалить используемую NAT configuration. Даже после очистки таблицы фоновые устройства способны немедленно создать записи заново:

- cameras;
- POS terminals;
- phones;
- monitoring agents;
- cloud applications;
- update services.

В production изменение NAT следует считать потенциально прерывающей операцией.

## Безопасная последовательность изменения

Конкретный порядок зависит от topology, redundancy и платформы, но общий план такой:

1. Сохранить и просмотреть текущую конфигурацию.
2. Зафиксировать active translations и statistics.
3. Подготовить точные команды rollback.
4. Сообщить пользователям и согласовать maintenance window.
5. Остановить или перенаправить новый traffic, если архитектура это позволяет.
6. При необходимости временно shutdown затронутый inside или outside interface.
7. Очистить dynamic translations.
8. Удалить старое NAT rule.
9. Добавить overload rule.
10. Вернуть interfaces в рабочее состояние.
11. Проверить routing, NAT и application connectivity.
12. Наблюдать counters, logs и translation usage.

Лабораторный пример:

```cisco
clear ip nat translation *
configure terminal
no ip nat inside source list 1 pool cafepublic
ip nat inside source list 1 interface GigabitEthernet0/2 overload
end
```

Если translations немедленно возвращаются, временное отключение трафика может быть необходимо. Нельзя бездумно выполнять `shutdown` на production router: это запланированный outage с известным impact.

## Проверка PAT

Сгенерировать traffic от нескольких inside hosts, затем выполнить:

```cisco
show ip nat translations
```

Пример:

```text
Pro  Inside global       Inside local         Outside local       Outside global
tcp  216.0.5.2:30001     192.168.10.21:51001  203.0.113.10:443    203.0.113.10:443
tcp  216.0.5.2:30002     192.168.10.22:51001  203.0.113.10:443    203.0.113.10:443
udp  216.0.5.2:31001     192.168.20.15:53000  198.51.100.53:53    198.51.100.53:53
```

Признаки PAT:

- разные inside local addresses;
- одинаковый inside global address;
- разные translated ports или identifiers.

Дополнительные команды:

```cisco
show ip nat statistics
show access-lists 1
show running-config | include ip nat
show ip interface brief
show ip route
```

После теста следует проверить не только ping, но и реальные TCP/UDP applications.

## Сколько соединений помещается в один public IP

IPv4 transport port field содержит 16 bits, но утверждение «один адрес всегда поддерживает ровно 65 535 sessions» слишком упрощено.

Фактическая capacity зависит от:

- protocol;
- зарезервированных и доступных port ranges;
- destination tuple reuse;
- IOS allocation algorithm;
- hardware и software platform limits;
- memory;
- translation timeouts;
- traffic pattern;
- количества sessions одного host;
- security и policy limits.

Одно устройство может создавать сотни или тысячи flows. Поэтому PAT capacity планируют по реальным concurrent translations и connection rates, а не только по теоретическому количеству port values.

Если одного public address недостаточно, варианты включают:

- pool overload;
- дополнительные public addresses;
- более мощную edge platform;
- сокращение ненужных session timeouts только после анализа;
- IPv6 adoption;
- архитектурное разделение traffic.

## PAT не является firewall

PAT обычно не создаёт произвольное inbound mapping для незапрошенного трафика, потому что отсутствует соответствующая translation. Однако это не делает PAT полноценной security policy.

Требуются отдельные controls:

- stateful firewall;
- ACL;
- segmentation;
- secure management plane;
- logging и monitoring;
- IDS/IPS при необходимости;
- patching endpoints;
- explicit static mappings только для нужных services.

NAT отвечает за address translation, а firewall определяет разрешённый traffic.

## Порядок диагностики

Если PAT не работает:

1. Проверить IP, mask и default gateway клиента.
2. Проверить routing к outside destination.
3. Проверить `ip nat inside` на ingress interface.
4. Проверить `ip nat outside` на egress interface.
5. Проверить соответствие source address ACL.
6. Проверить ACL counters.
7. Проверить наличие `overload` в NAT rule.
8. Для interface PAT проверить address и status outside interface.
9. Для pool PAT проверить pool и provider routing.
10. Проверить translation table и statistics.
11. Проверить firewall/ACL policy.
12. Проверить DNS отдельно от IP connectivity.
13. Проверить platform translation/session limits.

## Частые ошибки

### Пропущено слово overload

```cisco
ip nat inside source list 1 pool cafepublic
```

Это dynamic NAT, а не PAT.

### Указан неверный outside interface

Interface overload использует адрес именно указанного interface. Нужно сверить topology и `show ip interface brief`.

### ACL не включает все внутренние сети

Наличие `ip nat inside` не добавляет сеть в ACL автоматически.

### Старые translations мешают изменению

Очистка таблицы прерывает sessions и требует maintenance planning.

### PAT воспринимается как бесконечный ресурс

Translations, ports, memory и platform capacity конечны.

### NAT принимается за firewall

Translation и traffic authorization являются разными функциями.

## Контрольные вопросы

### Вопрос 1

Что делает ключевое слово `overload`?

Ответ:

```text
Разрешает нескольким inside translations совместно использовать
public address, различая flows по protocol и port/identifier information.
```

### Вопрос 2

Чем interface overload удобен при DHCP от ISP?

Ответ:

```text
NAT rule использует текущий address интерфейса,
поэтому public IP не нужно жёстко задавать в конфигурации.
```

### Вопрос 3

Можно ли использовать PAT с пулом?

Ответ:

```text
Да: ip nat inside source list 1 pool cafepublic overload.
```

### Вопрос 4

Почему перед изменением NAT очищают translations?

Ответ:

```text
Активные entries могут удерживать старое правило,
а их удаление завершает связанные sessions.
```

### Вопрос 5

Как узнать, что работает именно PAT?

Ответ:

```text
В translation table несколько inside local addresses используют
одинаковый inside global address с разными ports или identifiers.
```

## Команды и термины

| Команда / термин | Назначение |
| --- | --- |
| PAT | Port Address Translation. |
| NAT overload | Cisco term для совместного использования public addresses. |
| `overload` | Включает many-to-one/many-to-few translation. |
| `ip nat inside source list 1 pool cafepublic overload` | PAT с публичным пулом. |
| `ip nat inside source list 1 interface GigabitEthernet0/2 overload` | PAT на address внешнего interface. |
| `show ip nat translations` | Показывает addresses, protocols и ports. |
| `show ip nat statistics` | Показывает NAT roles, counters и capacity data. |
| `clear ip nat translation *` | Удаляет dynamic translations и прерывает sessions. |
| Inside local | Внутренний address до translation. |
| Inside global | Address, представляющий внутренний host снаружи. |

## Что повторить позже

- PAT translation table
- TCP/UDP port allocation
- ICMP identifiers
- NAT timeouts
- NAT order of operations
- Hairpin NAT
- Stateful firewall behavior
- PAT capacity planning
