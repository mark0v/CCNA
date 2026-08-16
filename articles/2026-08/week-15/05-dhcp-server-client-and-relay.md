# DHCP Server Client And Relay

Source: закрытая страница курса  
Date added: 2026-08-16  
Related plan item: Week 15 / DHCP server client and relay  
Tags: DHCP, DORA, DHCP server, DHCP client, DHCP relay, ip helper-address, Cisco IOS, troubleshooting
Language: Russian
Translation pair: articles-en/2026-08/week-15/05-dhcp-server-client-and-relay.md

## Кратко

- `DHCP` кажется автоматическим, пока устройства не перестают получать IP-адреса.
- На Cisco devices DHCP встречается в трех ролях: server, client и relay agent.
- DHCP server выдает IP-настройки из pool.
- DHCP client запрашивает адрес и параметры сети.
- DHCP relay agent пересылает запросы к DHCP server в другой subnet.
- Основной процесс DHCP называется `DORA`: Discover, Offer, Request, Acknowledge.
- На Cisco relay обычно настраивается командой `ip helper-address`.

## Главное

- DHCP выдает не только IP address, но и default gateway, DNS servers, lease time и другие options.
- Перед настройкой DHCP pool стоит настроить excluded addresses.
- Router в small и midsize network часто удобно использовать как DHCP server.
- Switch management interface может быть DHCP client, особенно в lab или staging.
- В production infrastructure devices часто получают static management IP для предсказуемости.
- DHCP broadcast не проходит через router сам по себе.
- Если DHCP server находится в другой subnet, нужен relay.

## Заметки

`DHCP`, или `Dynamic Host Configuration Protocol`, работает настолько удобно, что его легко недооценить. Device подключается, получает адрес, gateway, DNS и начинает работать.

А потом однажды адрес не приходит.

С этого момента DHCP перестает быть "фоновой мелочью" и становится критичным сервисом. В NetworkChuck Coffee это сразу заметно: barista tablets, office PCs, POS terminals и management interfaces без адресов не могут нормально участвовать в сети.

Главная мысль:

```text
DHCP невидим, пока работает. Когда он ломается, сеть быстро выглядит сломанной.
```

## Роли DHCP

В этой теме важно держать в голове три роли.

| Роль | Что делает |
| --- | --- |
| DHCP server | Выдает IP-настройки клиентам. |
| DHCP client | Запрашивает настройки. |
| DHCP relay agent | Пересылает DHCP-запросы между subnet. |

На Cisco router можно увидеть все эти идеи:

- router может раздавать адреса как DHCP server;
- switch или router interface может получать адрес как DHCP client;
- router interface может пересылать DHCP-запросы через `ip helper-address`.

## Cisco Router как DHCP-сервер

В small и midsize сетях router часто является удобным DHCP server.

Он уже:

- знает local subnets;
- routing находится на нем;
- обычно является default gateway;
- всегда нужен для работы site.

Базовая логика настройки:

1. Исключить static addresses.
2. Создать DHCP pool.
3. Указать network.
4. Указать default router.
5. Указать DNS server.
6. При необходимости указать domain name и другие options.

Пример:

```text
ip dhcp excluded-address 192.168.10.1 192.168.10.20

ip dhcp pool CAFE-VLAN10
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 192.168.10.53
 domain-name cafe.local
```

`excluded-address` стоит делать до pool. Эти адреса router не должен выдавать клиентам, потому что они зарезервированы для gateway, servers, printers или других static devices.

Технически router не должен выдать собственный address, но явные исключения остаются хорошей практикой. Они делают схему понятной для будущего администратора.

## Процесс DORA

`DORA` - это базовый DHCP-разговор.

| Шаг | Что происходит |
| --- | --- |
| Discover | Client broadcast: "Мне нужен IP address". |
| Offer | Server предлагает address и options. |
| Request | Client выбирает предложение и запрашивает его. |
| Acknowledge | Server подтверждает lease и настройки. |

Упрощенно:

```text
Discover -> Offer -> Request -> Acknowledge
```

Если есть несколько DHCP servers, client может получить несколько offers. Обычно выбирается первый ответ.

Важно понимать: DHCP не просто выдает IP. Он сообщает устройству, где оно находится в сети и как ему общаться дальше.

Обычно client получает:

- IP address;
- subnet mask;
- default gateway;
- DNS server;
- lease time;
- дополнительные options.

## DHCP-клиент на сетевом устройстве

DHCP client - это не только laptop или desktop.

Cisco switch может использовать DHCP для management interface, например через SVI.

Пример идеи:

```text
interface vlan 10
 ip address dhcp
 no shutdown
```

Это удобно:

- в lab;
- при staging;
- во временных сетях;
- при быстром deployment.

Но для production management часто лучше static IP.

Почему:

- проще documentation;
- проще monitoring;
- проще remote access;
- меньше неожиданностей после lease changes;
- предсказуемее troubleshooting.

Правило: знать DHCP client mode нужно обязательно, но использовать его для infrastructure management нужно осознанно.

## Когда Server в другой subnet

DHCP начинается с broadcast.

Проблема:

```text
Routers не пересылают broadcasts по умолчанию.
```

Если client в VLAN 10 отправляет DHCP Discover, а DHCP server находится в VLAN 50, запрос сам туда не попадет.

Для этого нужен DHCP relay agent.

На Cisco обычно используется команда:

```text
interface vlan 10
 ip helper-address 192.168.50.10
```

Она говорит router или Layer 3 switch:

```text
Когда ты услышишь DHCP-запрос в этой VLAN, перешли его к удаленному DHCP server.
```

## Как Relay помогает Server выбрать Pool

Relay не просто пересылает packet вслепую.

Он добавляет информацию о том, откуда пришел запрос. Благодаря этому centralized DHCP server понимает, какой scope использовать.

Пример:

- request пришел с interface VLAN 10;
- server видит, что request относится к subnet VLAN 10;
- server выбирает DHCP pool для VLAN 10;
- offer возвращается через relay.

Без этой информации server не знал бы, из какого address pool выдавать IP.

В large network это критично. Не нужно ставить отдельный DHCP server в каждую VLAN. Можно держать centralized DHCP infrastructure и использовать relay на gateway interfaces.

## Диагностика DHCP

Правильные вопросы важнее случайных команд.

Спроси:

1. Client отправляет Discover?
2. Server отвечает Offer?
3. Client получает правильный subnet?
4. DHCP pool настроен верно?
5. Excluded addresses не перекрывают весь pool?
6. Default gateway и DNS options правильные?
7. Если server remote, есть ли `ip helper-address`?
8. Есть ли route между relay и DHCP server?
9. Не блокирует ли ACL DHCP traffic?
10. Нет ли rogue DHCP server?

Если понимать `DORA`, troubleshooting становится разговором: на каком шаге диалог оборвался?

## Сценарий NetworkChuck Coffee

В NetworkChuck Coffee DHCP нужен для:

- tablets;
- POS terminals;
- office PCs;
- guest devices;
- printers;
- switch management в lab;
- new site deployment.

Для маленькой площадки router может быть DHCP server:

```text
ip dhcp pool CAFE
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 192.168.10.53
```

Если позже появляется centralized server в back office или data center, gateway interfaces на VLAN получают `ip helper-address`.

Так DHCP остается централизованным, но обслуживает много VLAN.

## Проверка

Полезные команды:

```text
show ip dhcp pool
show ip dhcp binding
show ip dhcp conflict
show running-config | section dhcp
show running-config interface vlan 10
debug ip dhcp server packet
ip dhcp excluded-address 192.168.10.1 192.168.10.20
ip dhcp pool CAFE-VLAN10
ip helper-address 192.168.50.10
```

Что проверить:

- pool существует;
- network и mask правильные;
- default-router указан верно;
- DNS server указан верно;
- excluded range не слишком большой;
- bindings появляются;
- conflicts отсутствуют или объяснимы;
- helper address настроен на нужном interface;
- client реально находится в правильной VLAN.

## Главный вывод

DHCP кажется простым, потому что большую часть времени работает сам.

Но за этой простотой три важные роли: server, client и relay agent. Server раздает настройки, client их запрашивает, relay переносит запросы через router boundary.

Если знаешь `DORA` и понимаешь `ip helper-address`, ты можешь не просто настроить DHCP, а быстро понять, где именно сломался процесс выдачи адреса.

## Команды и термины

| Термин | Значение |
| --- | --- |
| `DHCP` | Dynamic Host Configuration Protocol, автоматическая выдача IP-настроек. |
| `DORA` | Discover, Offer, Request, Acknowledge. |
| DHCP server | Устройство, выдающее IP-настройки. |
| DHCP client | Устройство, запрашивающее IP-настройки. |
| DHCP relay agent | Устройство, пересылающее DHCP-запросы к server в другой subnet. |
| `ip dhcp pool` | Создает DHCP pool на Cisco device. |
| `ip dhcp excluded-address` | Исключает адреса из выдачи DHCP. |
| `default-router` | DHCP option для default gateway. |
| `dns-server` | DHCP option для DNS server. |
| `ip helper-address` | Cisco command для DHCP relay. |
| lease | Временная выдача IP-настроек клиенту. |
| scope | Address pool на DHCP server для конкретной subnet. |

## Вопросы

### 1. Какие три роли DHCP нужно знать на Cisco devices?

Ответ: DHCP server, DHCP client и DHCP relay agent.

### 2. Что означает DORA?

Ответ: Discover, Offer, Request, Acknowledge.

### 3. Почему excluded addresses нужно настраивать заранее?

Ответ: Чтобы DHCP server не выдал адреса, зарезервированные для gateway, servers, printers или других static devices.

### 4. Зачем нужен `ip helper-address`?

Ответ: Чтобы пересылать DHCP-запросы из одной subnet к DHCP server в другой subnet.

### 5. Почему DHCP client на switch management interface не всегда лучший production design?

Ответ: Static management IP обычно проще документировать, мониторить и использовать для remote access.

## Что повторить позже

- Процесс `DORA`.
- Настройку `ip dhcp excluded-address`.
- Настройку `ip dhcp pool`.
- DHCP options `default-router` и `dns-server`.
- DHCP client на SVI.
- DHCP relay через `ip helper-address`.
- Проверку `show ip dhcp binding`.
