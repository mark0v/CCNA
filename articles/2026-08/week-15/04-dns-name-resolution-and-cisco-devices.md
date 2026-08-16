# DNS Name Resolution And Cisco Devices

Source: закрытая страница курса  
Date added: 2026-08-16  
Related plan item: Week 15 / DNS name resolution and Cisco devices  
Tags: DNS, name resolution, UDP 53, TCP 53, DNS records, ip name-server, ip host, troubleshooting
Language: Russian
Translation pair: articles-en/2026-08/week-15/04-dns-name-resolution-and-cisco-devices.md

## Кратко

- `DNS` переводит понятные имена в IP-адреса.
- Если `DNS` ломается, сеть часто выглядит сломанной даже при исправных links и routing.
- Большинство обычных DNS-запросов использует `UDP 53`.
- `TCP 53` используется для zone transfer, репликации и крупных ответов.
- Важные записи: `A`, `CNAME`, `MX`, `NS`, `TXT`.
- Cisco device может использовать DNS через `ip name-server`.
- На поддерживаемых платформах Cisco device может отвечать на простые DNS-запросы с локальными `ip host` mappings.

## Главное

- DNS - не просто "сайты в адреса"; это центральная часть работы приложений, почты, cloud-сервисов и security.
- DNS-проблемы часто выглядят как медленная сеть.
- Медленный resolver может заставить здоровую сеть казаться больной.
- Caching ускоряет DNS, но из-за него изменения не всегда видны сразу.
- Для small office можно использовать простую локальную DNS-логику на router.
- Для большой сети нужен redundant и highly available DNS design.
- При жалобе "internet slow" стоит проверить DNS рано, а не после долгой проверки bandwidth.

## Заметки

`DNS`, или `Domain Name System`, делает одну базовую вещь:

```text
Имя превращается в IP-адрес.
```

Людям удобно помнить имена вроде `amazon.com`, internal apps или server aliases. Устройства же отправляют traffic к IP-адресам. `DNS` связывает эти два мира.

Когда `DNS` работает, его почти не замечают. Когда он ломается, почти все начинает выглядеть странно: часть сервисов доступна, часть нет, IP работает, имя нет, пользователи говорят "сеть упала", хотя физически сеть может быть полностью alive.

## Как работает DNS

Обычный клиентский DNS lookup чаще всего идет через `UDP 53`.

Это может звучать странно, потому что UDP не гарантирует доставку. Но DNS работает по модели request-response: если client не получил answer, он может повторить запрос.

Есть и `TCP 53`. Он нужен в сценариях, где UDP не подходит:

- zone transfer;
- server replication;
- большие ответы;
- некоторые security и reliability-сценарии.

На уровне CCNA важно запомнить:

```text
DNS обычно использует UDP 53, но TCP 53 тоже существует и нужен.
```

## Типы записей

DNS хранит разные record types.

| Record | Для чего нужен |
| --- | --- |
| `A` | Имя в IPv4 address. |
| `AAAA` | Имя в IPv6 address. |
| `CNAME` | Alias на другое DNS name. |
| `MX` | Mail exchanger для почты домена. |
| `NS` | Authoritative name server для зоны. |
| `TXT` | Текстовые данные для verification, email security и других задач. |

`TXT` records часто недооценивают. В реальности на них завязано много email security и domain verification. DNS помогает не только найти адрес, но и подтвердить, кому можно доверять.

## Почему DNS ломает все так сильно

Почти никто не работает с raw IP-адресами.

Пользователи открывают:

- websites;
- cloud apps;
- email;
- Teams;
- Outlook;
- internal portals;
- APIs;
- business applications.

Все это зависит от name resolution.

Если `DNS` не отвечает, names ничего не значат. Если `DNS` отвечает медленно, сеть кажется медленной.

Современная web-page может грузить:

- HTML с одного host;
- images с другого;
- scripts с третьего;
- CSS с четвертого;
- analytics с пятого;
- ads или integrations еще откуда-то.

Каждый элемент может требовать DNS lookup. Если каждый lookup задерживается на секунды, пользователь видит "медленный internet", хотя bandwidth может быть нормальным.

## Проверяй DNS рано

Когда пользователь говорит "internet slow", не начинай только с bandwidth graphs и duplex.

Быстрые проверки:

```text
nslookup example.com
nslookup example.com 8.8.8.8
ping 8.8.8.8
ping example.com
```

Идея:

- если IP reachable, но name не работает, смотри DNS;
- если другой resolver отвечает быстрее, проблема может быть в текущем DNS server;
- если DNS периодически timeout, сеть будет казаться нестабильной.

DNS часто не первая мысль, но должен быть среди первых проверок.

## Кэширование

DNS активно использует cache.

Плюсы:

- быстрее повторные queries;
- меньше нагрузки на upstream servers;
- меньше external traffic;
- выше устойчивость при кратких проблемах upstream.

Минусы:

- изменения record не везде видны сразу;
- old answer может жить в cache до истечения TTL;
- troubleshooting иногда путается из-за разных answers у разных resolvers.

Поэтому фраза "я уже поправил DNS" не всегда означает "все клиенты уже видят новую запись".

## Cisco-устройство как DNS-клиент

Cisco router или switch может сам использовать DNS, чтобы разрешать names.

Команда:

```text
ip name-server 10.1.0.53
```

После этого device может выполнять команды по имени, например:

```text
ping server.example.local
```

Это удобно для администрирования. Не нужно помнить каждый IP address, особенно если в сети есть management names.

Часто также настраивают domain lookup behavior и default domain, но базовая идея проста: `ip name-server` указывает, к какому DNS server обращаться.

## Cisco-устройство как простой DNS-сервер

В некоторых небольших сетях Cisco device может быть легким DNS helper.

Идея:

- включить DNS service, если платформа поддерживает;
- создать локальные name mappings;
- выдать этот DNS address клиентам через DHCP.

Пример локальной записи:

```text
ip host pos-server 10.10.10.50
ip host inventory 10.10.10.60
```

Теперь router может знать простые локальные имена.

Это не замена полноценной enterprise DNS-инфраструктуре, но для маленького site может быть достаточно. Особенно если router уже является центральным устройством, а отдельный server добавил бы лишнюю сложность.

## Рабочий процесс для маленькой сети

Простой порядок:

1. Указать upstream DNS через `ip name-server`.
2. При необходимости включить DNS service на поддерживаемой платформе.
3. Создать local mappings через `ip host`.
4. Настроить DHCP так, чтобы clients получали нужный DNS server.
5. Проверить lookup с Cisco device и client devices.

Главная цель - сделать names удобными и предсказуемыми без лишней инфраструктуры.

## Дизайн для роста

Для маленького cafe одна простая DNS-точка может быть нормальной.

Для крупной сети один lonely router как единственный DNS source - плохой design.

При росте нужны:

- минимум два DNS servers;
- redundancy;
- monitoring;
- controlled forwarding;
- documented zones;
- backup и change process;
- понятный TTL strategy;
- security для records и updates.

DNS становится критичной инфраструктурой, потому что от него зависят users, apps, mail, authentication и cloud services.

## Сценарий NetworkChuck Coffee

В NetworkChuck Coffee нужно, чтобы POS, office computers, media server и internal tools находили друг друга по именам.

Для маленькой площадки можно сделать просто:

- router знает upstream DNS;
- router хранит несколько local `ip host` entries;
- DHCP выдает клиентам DNS address;
- staff использует names, а не IP addresses.

Если сеть вырастает, DNS нужно переносить в более надежную схему: redundant internal DNS servers, monitoring и нормальная зона.

Less complexity может быть преимуществом, пока она соответствует размеру сети.

## Проверка

Команды и инструменты:

```text
nslookup example.com
nslookup example.com 8.8.8.8
show hosts
show running-config | include ip name-server
ping hostname
ip name-server 10.1.0.53
ip host pos-server 10.10.10.50
```

Что проверить:

- какой DNS server использует device;
- отвечает ли resolver;
- работает ли lookup по имени;
- отличается ли ответ от другого resolver;
- нет ли старого cache;
- корректно ли DHCP выдает DNS server;
- не является ли DNS single point of failure.

## Главный вывод

`DNS` делает сеть удобной для людей и приложений.

Он переводит names в addresses, но его роль шире: mail, verification, security, internal apps и cloud services тоже зависят от DNS. Когда DNS медленный или сломан, здоровая сеть может выглядеть неисправной.

На Cisco devices важно понимать две роли: device может использовать DNS через `ip name-server`, а в маленькой сети иногда может помогать с local mappings через `ip host`.

## Команды и термины

| Термин | Значение |
| --- | --- |
| `DNS` | Domain Name System, система перевода names в IP addresses. |
| resolver | DNS server, который отвечает на client queries. |
| `UDP 53` | Основной транспорт для обычных DNS queries. |
| `TCP 53` | Используется для zone transfer, больших ответов и отдельных сценариев. |
| `A record` | DNS-запись name-to-IPv4. |
| `CNAME` | Alias на другое DNS name. |
| `MX` | Запись для mail routing. |
| `NS` | Authoritative name server для DNS zone. |
| `TXT` | Текстовая DNS-запись для verification и security. |
| `ip name-server` | Cisco command для указания DNS server. |
| `ip host` | Cisco command для локального name-to-IP mapping. |
| `TTL` | Время жизни DNS answer в cache. |

## Вопросы

### 1. Что делает DNS?

Ответ: Переводит понятные names в IP addresses.

### 2. Почему DNS-проблемы часто выглядят как медленная сеть?

Ответ: Современные приложения и сайты делают много lookups, и задержки resolver замедляют весь опыт.

### 3. Какой port чаще всего использует обычный DNS query?

Ответ: `UDP 53`.

### 4. Для чего нужен `ip name-server`?

Ответ: Чтобы Cisco device знал, к какому DNS server обращаться для name resolution.

### 5. Почему DNS нужно делать redundant при росте сети?

Ответ: Потому что DNS быстро становится критичным single point of failure для users, apps и security.

## Что повторить позже

- `UDP 53` и `TCP 53`.
- Record types: `A`, `AAAA`, `CNAME`, `MX`, `NS`, `TXT`.
- `ip name-server`.
- `ip host`.
- DNS troubleshooting через `nslookup`.
- Влияние caching и `TTL`.
