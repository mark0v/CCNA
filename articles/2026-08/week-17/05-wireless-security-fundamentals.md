# Wireless Security Fundamentals

Source: закрытая страница курса  
Date added: 2026-08-21  
Related plan item: Week 17 / Wireless security fundamentals  
Tags: wireless security, Wi-Fi, WEP, WPA, WPA2, WPA3, PSK, 802.1X, EAP, RADIUS, encryption, authentication
Language: Russian
Translation pair: articles-en/2026-08/week-17/05-wireless-security-fundamentals.md

## Кратко

- Wireless security важна, потому что сигнал выходит за пределы стен.
- В wired network злоумышленнику часто нужен физический доступ, а Wi-Fi можно атаковать из парковки рядом.
- Wireless security закрывает только один слой: передачу между client и access point.
- Нужны две вещи: encryption и authentication.
- `WEP` устарел и небезопасен.
- `WPA` был временным улучшением после `WEP`.
- `WPA2` стал зрелым стандартом и широко используется до сих пор.
- `WPA3` улучшает защиту и исправляет слабые места `WPA2`.
- `PSK` подходит для дома и маленьких сетей.
- `802.1X/EAP` лучше подходит для бизнеса, staff turnover и нескольких locations.

## Главное

- Wi-Fi нельзя считать безопасным только потому, что он "внутри здания".
- Радиосигнал не уважает стены, двери и границы офиса.
- Encryption защищает данные от чтения при перехвате.
- Authentication решает, кто имеет право подключиться.
- Shared password удобен, но плохо масштабируется.
- Identity-based access позволяет отключить одного пользователя, а не менять пароль всей сети.
- Wireless security не заменяет segmentation, firewalls, MFA, permissions и нормальную network policy.

## Заметки

Wireless security часто недооценивают.

В проводной сети атакующему обычно нужно получить доступ к чему-то физическому:

- кабелю;
- wall jack;
- switch port;
- зданию;
- комнате с оборудованием.

В Wi-Fi мы сами передаем доступ в воздух.

Даже если access points размещены аккуратно, сигнал может выходить:

- в коридор;
- на парковку;
- в соседний офис;
- на улицу;
- в соседнее помещение.

Поэтому wireless security - не формальность.

## Почему wireless более открыт

Сигнал не останавливается ровно на стене.

Можно настраивать power levels, правильно размещать AP и проектировать coverage, но полностью спрятать радиосигнал внутри здания обычно невозможно.

Практическая картина:

```text
Сотрудник сидит внутри.
Access point вещает внутри.
Сигнал уходит наружу.
Кто-то в машине рядом тоже может его услышать.
```

Это не значит, что Wi-Fi обязательно небезопасен. Это значит, что его нужно защищать осознанно.

## Беспроводная защита - только один слой

Wireless security не решает всю безопасность сети.

Она защищает конкретный участок:

```text
Client <-> Access Point
```

Но остаются другие слои:

- учетные записи;
- permissions;
- MFA;
- network segmentation;
- firewall policies;
- device posture;
- logging;
- monitoring;
- guest isolation;
- VLAN design.

Не думай о wireless security как о единственной защите. Это один слой в общей модели.

## Две главные идеи

В wireless security постоянно возвращаемся к двум словам:

- encryption;
- authentication.

## Шифрование

`Encryption` означает, что данные шифруются.

Если кто-то перехватывает traffic в воздухе, он не должен просто читать содержимое.

Упрощенно:

```text
Даже если ты услышал сигнал, ты не должен понять данные.
```

Без нормального encryption Wi-Fi превращается в удобную точку наблюдения для всех, кто рядом.

## Аутентификация

`Authentication` отвечает на другой вопрос:

```text
Имеешь ли ты право подключиться?
```

Это может быть:

- общий Wi-Fi password;
- username/password;
- certificate;
- учетная запись в identity system;
- проверка через RADIUS;
- другой EAP method.

Encryption защищает содержимое. Authentication контролирует вход.

Нужны оба.

## Открытые сети

Если Wi-Fi network не показывает lock icon и не требует пароль на wireless layer, это обычно open network.

Иногда после подключения появляется captive portal:

- hotel login page;
- airport portal;
- coffee shop terms page.

Но важно понимать:

```text
Captive portal не равен полноценной wireless encryption.
```

Он может контролировать доступ к internet, но сама wireless часть может оставаться открытой.

## Эволюция защиты

Wireless security развивалась по шагам:

```text
WEP -> WPA -> WPA2 -> WPA3
```

Каждый шаг закрывал проблемы предыдущего.

## Устаревший WEP

`WEP`, или `Wired Equivalent Privacy`, был ранней попыткой защитить Wi-Fi.

Название звучало уверенно: будто wireless станет примерно таким же безопасным, как кабель.

На практике `WEP` оказался слабым.

Его можно было взломать, и со временем это стало серьезной проблемой. Сегодня `WEP` не должен использоваться в нормальных сетях.

Практическое правило:

```text
Если видишь WEP - это security finding.
```

## Переходный WPA

`WPA`, или `Wi-Fi Protected Access`, появился как быстрый ответ на слабость `WEP`.

Это был шаг вперед.

Он улучшил защиту и позволил многим устройствам стать безопаснее без мгновенной замены всего оборудования.

Но `WPA` был скорее переходным решением, а не финальной точкой.

## Зрелый WPA2

`WPA2` стал большим шагом вперед.

Он принес более сильную защиту, особенно через `AES`.

`AES` - сильный алгоритм шифрования, который широко используется не только в Wi-Fi.

`WPA2` много лет был основной нормой и до сих пор встречается почти везде.

Важно:

```text
WPA2 не стал мусором только потому, что появился WPA3.
```

В реальных сетях `WPA2` все еще часто считается приемлемым и сильным вариантом, если настроен правильно.

## Современный WPA3

`WPA3` появился, чтобы улучшить защиту и закрыть слабые места `WPA2`.

Особенно важны улучшения вокруг процесса handshake и защиты от некоторых атак на слабые пароли.

`WPA3` - правильное направление для нового оборудования и новых deployments.

Но в реальности нужно учитывать compatibility:

- поддерживают ли clients WPA3;
- поддерживают ли AP WPA3;
- есть ли старые устройства;
- нужен ли mixed mode;
- как это влияет на onboarding.

## Общий ключ PSK

`PSK`, или `pre-shared key`, - это привычный Wi-Fi password.

Идея простая:

```text
Есть один общий secret.
Кто знает secret, тот может подключиться.
```

Для дома или маленького офиса это часто нормально.

Плюсы:

- легко настроить;
- понятно пользователям;
- не нужен RADIUS;
- не нужна сложная identity infrastructure.

Минусы появляются при масштабе.

## Проблема общего пароля

Shared password плохо масштабируется.

Представь:

- 50 сотрудников;
- tablets;
- printers;
- cameras;
- IoT devices;
- несколько locations;
- staff turnover.

Если один сотрудник ушел и пароль нужно менять, начнется боль:

- devices отпадают от Wi-Fi;
- printers перестают работать;
- tablets требуют повторной настройки;
- IoT devices ломаются;
- helpdesk получает волну обращений;
- все locations нужно обновить.

Один общий пароль удобен до тех пор, пока среда маленькая и стабильная.

## 802.1X и EAP

Для больших сред часто используют `802.1X` вместе с `EAP`.

`EAP`, или `Extensible Authentication Protocol`, - это framework для разных методов аутентификации.

Идея:

```text
Не один пароль для всех.
Каждый user или device проходит отдельную проверку.
```

Проверка может идти через:

- RADIUS server;
- Active Directory;
- Microsoft 365;
- certificate authority;
- identity provider;
- другую backend identity system.

Если сотрудник уходит, его account отключается. Не нужно менять пароль всей wireless network.

## Методы EAP

`EAP` - это не один конкретный способ.

Это framework, внутри которого есть разные методы:

- username/password;
- certificates;
- tunneled authentication;
- combinations of credentials and certificates.

Не нужно на этом этапе запоминать все варианты.

Важно понять принцип:

```text
802.1X/EAP дает индивидуальную проверку вместо одного общего пароля.
```

## Сценарий NetworkChuck Coffee

Если NetworkChuck Coffee - одна маленькая точка с несколькими trusted devices, сильный `WPA2-PSK` или `WPA3-PSK` может быть нормальным.

Но если бизнес растет:

- несколько shops;
- guest Wi-Fi;
- staff Wi-Fi;
- POS devices;
- printers;
- tablets;
- cameras;
- employees приходят и уходят;
- internal resources доступны из staff network.

Тогда shared password становится проблемой.

Лучше думать об identity-based access:

```text
Отключить одного user.
Не ломать всю wireless network.
```

Это особенно важно, когда staff turnover нормален, а количество devices растет.

## Гостевой Wi-Fi

Guest Wi-Fi должен быть отделен от внутренней сети.

Даже если гости получают internet access, они не должны видеть:

- cameras;
- printers;
- POS systems;
- staff laptops;
- management interfaces;
- internal servers.

Wireless security - это не только пароль. Это еще и segmentation.

Практическая идея:

```text
Guest traffic belongs in a separate network.
```

## Практический совет

Для дома или tiny office:

- используй `WPA2` или `WPA3`;
- ставь сильный PSK;
- не используй `WEP`;
- разделяй guest и private networks.

Для бизнеса:

- оцени `802.1X/EAP`;
- используй RADIUS или identity system;
- отделяй guest traffic;
- планируй staff turnover;
- документируй recovery;
- проверяй compatibility clients с `WPA3`.

## Главный вывод

Wireless security важна, потому что Wi-Fi передает доступ в воздух, а не по контролируемому кабелю.

Нужно защищать и вход в сеть, и данные в радиосреде. Authentication решает, кто может подключиться. Encryption защищает traffic от чтения.

`WEP` устарел. `WPA` был переходным шагом. `WPA2` стал зрелым и широко используемым стандартом. `WPA3` улучшает защиту для современных сетей.

Для маленьких сред подходит strong PSK. Для растущего бизнеса лучше смотреть в сторону `802.1X/EAP`, чтобы управлять доступом по пользователям и устройствам, а не одним общим паролем.

## Команды и термины

| Термин | Значение |
| --- | --- |
| wireless security | Защита беспроводного доступа и передачи данных. |
| encryption | Шифрование данных, чтобы их нельзя было прочитать при перехвате. |
| authentication | Проверка, имеет ли client право подключиться. |
| open network | Wi-Fi network без wireless password на уровне подключения. |
| captive portal | Web-страница авторизации после подключения к сети. |
| `WEP` | Wired Equivalent Privacy, устаревший и слабый метод защиты. |
| `WPA` | Wi-Fi Protected Access, переходный метод после `WEP`. |
| `WPA2` | Зрелый стандарт wireless security с сильным encryption. |
| `WPA3` | Более современный стандарт с улучшенной защитой. |
| `AES` | Алгоритм шифрования, используемый в сильных security designs. |
| `PSK` | Pre-shared key, общий пароль Wi-Fi. |
| `802.1X` | Стандарт port-based/network access authentication. |
| `EAP` | Extensible Authentication Protocol, framework методов аутентификации. |
| `RADIUS` | Серверный протокол для централизованной аутентификации. |

## Вопросы

### 1. Почему wireless security особенно важна?

Ответ: Потому что Wi-Fi-сигнал выходит за пределы физической границы здания и может быть доступен снаружи.

### 2. Чем encryption отличается от authentication?

Ответ: Encryption защищает данные от чтения, а authentication проверяет, кто имеет право подключиться.

### 3. Почему WEP нельзя использовать?

Ответ: `WEP` слабый и давно считается небезопасным.

### 4. Когда PSK подходит нормально?

Ответ: В home network или маленьком офисе, где мало trusted users и devices.

### 5. Почему 802.1X/EAP лучше для бизнеса?

Ответ: Он позволяет проверять каждого user или device отдельно и отключать доступ без смены общего Wi-Fi password.

## Что повторить позже

- Почему wireless более exposed, чем wired.
- Разницу между encryption и authentication.
- Эволюцию `WEP -> WPA -> WPA2 -> WPA3`.
- Где подходит `PSK`.
- Зачем нужны `802.1X`, `EAP` и `RADIUS`.
- Почему guest Wi-Fi должен быть отделен от internal network.
