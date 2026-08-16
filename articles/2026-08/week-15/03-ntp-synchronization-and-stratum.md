# NTP Synchronization And Stratum

Source: закрытая страница курса  
Date added: 2026-08-16  
Related plan item: Week 15 / NTP synchronization and stratum  
Tags: NTP, stratum, ntp master, ntp server, loopback, time synchronization, Cisco IOS
Language: Russian
Translation pair: articles-en/2026-08/week-15/03-ntp-synchronization-and-stratum.md

## Кратко

- Ручная настройка clock лучше, чем неправильное время, но она не масштабируется.
- `NTP` синхронизирует время между network devices автоматически.
- В `NTP` есть server, который предоставляет время, и clients, которые синхронизируются с ним.
- `stratum` показывает, насколько близко устройство к исходному источнику времени.
- Чем ниже `stratum`, тем более авторитетным считается источник.
- Cisco router можно сделать локальным источником времени командой `ntp master`.
- На client device используется команда `ntp server <ip-address>`.
- Если синхронизация не работает, сначала проверь IP connectivity и time zone.

## Главное

- Цель `NTP` - не один раз выставить правильное время, а удерживать устройства согласованными.
- Accurate timestamps нужны для logs, certificates, VPN, authentication и troubleshooting.
- `stratum 1` ближе всего к исходному точному источнику времени.
- `stratum 16` означает, что источник не считается доверенным.
- В lab router может быть `ntp master` со стандартным `stratum 8`.
- В production обычно лучше использовать несколько внутренних NTP-серверов, которые синхронизируются с upstream sources.
- Loopback interface удобен как стабильный NTP identity.

## Заметки

Ручная настройка времени на Cisco device полезна как быстрый fix. Это лучше, чем оставить router или switch с default-дотой из прошлого.

Но как только устройств становится больше одного, ручной clock превращается в проблему:

- clocks drift;
- время задают разные люди;
- часть devices забывают;
- после reboot поведение может отличаться;
- logs снова перестают совпадать.

Главная цель:

```text
Все устройства должны автоматически соглашаться, который сейчас час.
```

Для этого нужен `NTP`.

## Что делает NTP

`NTP`, или `Network Time Protocol`, дает устройствам единый источник времени.

Модель простая:

| Роль | Что делает |
| --- | --- |
| NTP server | Предоставляет время. |
| NTP client | Запрашивает время и синхронизируется. |

NTP server может быть:

- Linux server;
- Windows server;
- public NTP server;
- router;
- firewall;
- выделенный time source.

Для небольшой lab-сети можно сделать router локальным master. Для production лучше строить контролируемую схему: несколько внутренних устройств синхронизируются с надежными upstream sources, а остальные devices используют внутренние источники.

## Почему это важно

В NetworkChuck Coffee неправильное время быстро ломает troubleshooting.

Представь:

- switch пишет, что interface упал в 09:01;
- router пишет routing event в 08:54;
- firewall показывает deny позже, но с другим time zone;
- POS system пишет сбой еще в другое время.

Теперь непонятно, что было первым. А если порядок событий непонятен, расследование становится медленным и ненадежным.

Consistent time делает сеть похожей на одну систему, а не на набор отдельных коробок с разными часами.

## Уровень Stratum

`stratum` - это число, которое показывает, насколько близко устройство к исходному источнику точного времени.

Упрощенно:

| Stratum | Значение |
| --- | --- |
| `stratum 1` | Источник напрямую связан с очень точным time source. |
| `stratum 2` | Получает время от stratum 1. |
| `stratum 3` | Получает время от stratum 2. |
| `stratum 16` | Не считается надежным источником. |

Чем ниже stratum, тем авторитетнее источник.

Это нужно, чтобы сеть не строила бесконечную цепочку времени. Если устройства будут бесконечно синхронизироваться друг от друга без контроля, clock drift постепенно превратит точное время в мусор.

## Роутер как NTP Master

В lab можно сначала вручную выставить clock на router, а потом сделать его локальным NTP source.

Пример:

```text
show clock
clock set 11:22:30 12 Sep 2024

configure terminal
ntp master
end

show ntp status
```

Команда `ntp master` говорит router работать как NTP server для других устройств.

На Cisco по умолчанию такой master часто показывает `stratum 8`. Это нормально для lab: router говорит "я источник времени", но не притворяется atomic clock.

Если router синхронизирован сам с собой как master, вывод может выглядеть непривычно, но логика понятная: в этой маленькой сети он является authority.

## Клиентская сторона

На switch или другом client device нужно указать NTP server.

Пример:

```text
configure terminal
ntp server 10.1.0.1
end

show ntp status
show clock detail
```

Команда:

```text
ntp server <ip-address>
```

говорит устройству получать время от указанного server.

Важно: `NTP` не магия. Если switch не может ping router, синхронизация не заработает. Сначала connectivity, потом service.

Проверить стоит:

- IP address на client;
- default gateway или route;
- VLAN/interface state;
- ACL;
- reachability до NTP server;
- time zone.

## Синхронизация не всегда мгновенная

После настройки `NTP` нужно подождать.

Иногда `show ntp status` сначала показывает unsynchronized. Это не всегда ошибка. NTP может занять минуту или больше, прежде чем device выберет server и начнет уверенно синхронизироваться.

Порядок проверки:

1. Есть IP connectivity до server.
2. `ntp server` указан правильно.
3. `show ntp status` меняет состояние на synchronized.
4. `show clock detail` показывает, что source - NTP.
5. Display time выглядит правильно после учета time zone.

## Стабильный адрес через Loopback

Если router имеет несколько physical interfaces, возникает вопрос: какой IP использовать как NTP server address?

Практичный ответ - loopback interface.

Loopback - виртуальный interface, который не зависит от состояния одного physical port. Если routing до loopback настроен правильно, devices могут использовать один стабильный адрес.

Пример идеи:

```text
interface loopback0
 ip address 10.1.0.1 255.255.255.255
```

Затем clients используют:

```text
ntp server 10.1.0.1
```

На реальном gear можно дополнительно управлять source interface для NTP. В отдельных simulator такая команда может быть ограничена, но сама идея важна: стабильный identity лучше случайного physical interface.

## Часовой пояс

NTP обычно синхронизирует время относительно UTC-подхода, а local device отображает его с учетом time zone.

Если display time выглядит неправильным, это не всегда проблема NTP.

Проверь по порядку:

1. Синхронизирован ли NTP.
2. Какой time source показывает `show clock detail`.
3. Какой time zone настроен.
4. Нет ли daylight saving mismatch.

Сначала verify synchronization, потом разбирай display offset.

## Дизайн для production

В production редко стоит отправлять сотни devices напрямую на public NTP server.

Более чистый дизайн:

- один или несколько внутренних NTP servers синхронизируются с upstream sources;
- network devices используют внутренние NTP servers;
- используется redundancy;
- при необходимости включается authentication;
- source interfaces и ACL задаются осознанно.

Плюсы:

- меньше зависимости от internet;
- проще control;
- единая policy;
- меньше внешнего трафика;
- понятнее troubleshooting.

## Сценарий NetworkChuck Coffee

NetworkChuck Coffee растет.

Один router можно сделать внутренним NTP master в lab или маленьком окружении. Switches и access points синхронизируются с ним.

Результат:

- logs совпадают по времени;
- troubleshooting становится нормальным;
- security events можно сравнивать;
- POS и back office systems выглядят согласованнее;
- при outage легче построить timeline.

Это не самая эффектная настройка, но без нее сеть быстро начинает рассказывать противоречивые истории.

## Проверка

Команды:

```text
show clock
show clock detail
show ntp status
show ntp associations
ntp master
ntp server 10.1.0.1
clock timezone AZ -7
```

Что проверить:

- правильный clock на master;
- включен ли `ntp master`;
- какой `stratum` показывает device;
- есть ли connectivity от client к server;
- синхронизировался ли client;
- показывает ли `show clock detail` NTP как source;
- правильно ли настроен time zone.

## Главный вывод

Ручная настройка clock - полезная временная мера, но она не решает проблему согласованного времени в сети.

`NTP` решает именно это: дает network devices общий источник времени и удерживает их синхронизированными. `stratum` помогает понять авторитетность источника, `ntp master` позволяет сделать локальный source, а `ntp server` подключает clients к нему.

Сначала добейся connectivity, потом настрой NTP, подожди синхронизации и только затем доверяй timestamps.

## Команды и термины

| Термин | Значение |
| --- | --- |
| `NTP` | Network Time Protocol, протокол синхронизации времени. |
| `ntp master` | Делает Cisco device локальным NTP source. |
| `ntp server` | Указывает NTP server для client device. |
| `show ntp status` | Показывает состояние NTP-синхронизации. |
| `show ntp associations` | Показывает NTP associations. |
| `stratum` | Уровень близости к исходному источнику времени. |
| `stratum 16` | Недоверенное или несинхронизированное состояние. |
| loopback interface | Виртуальный interface со стабильным IP. |
| clock drift | Постепенное расхождение времени. |
| UTC | Базовый мировой стандарт времени. |

## Вопросы

### 1. Почему ручная настройка clock является ловушкой?

Ответ: Она помогает одному device, но не удерживает множество устройств синхронизированными со временем.

### 2. Что делает NTP?

Ответ: Синхронизирует время devices с общим источником.

### 3. Что означает stratum?

Ответ: Насколько близко NTP source находится к исходному точному источнику времени.

### 4. Какая команда делает router локальным NTP source?

Ответ: `ntp master`.

### 5. Что проверить, если NTP не синхронизируется?

Ответ: IP connectivity, правильный `ntp server`, routes, ACL, состояние интерфейсов и time zone.

## Что повторить позже

- `ntp master`.
- `ntp server <ip-address>`.
- `show ntp status`.
- `show ntp associations`.
- Значение `stratum`.
- Использование loopback как стабильного NTP address.
- Разницу между synchronization и local time display.
