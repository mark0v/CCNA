# Wireless Access Points And Client Discovery

Source: закрытая страница курса  
Date added: 2026-08-21  
Related plan item: Week 17 / Wireless access points and client discovery  
Tags: Wi-Fi, WAP, access point, autonomous AP, lightweight AP, cloud-managed AP, WLC, CAPWAP, beacon, probe, association
Language: Russian
Translation pair: articles-en/2026-08/week-17/04-wireless-access-points-and-client-discovery.md

## Кратко

- Выбор access point зависит от среды, а не только от скорости на коробке.
- Indoor, outdoor, omnidirectional и directional варианты решают разные задачи.
- Wireless - двусторонняя связь: client должен не только слышать AP, но и отвечать ему.
- Autonomous AP управляется отдельно.
- Lightweight AP зависит от wireless LAN controller.
- Cloud-managed AP управляется через vendor cloud и часто зависит от подписки.
- Clients находят сети через passive discovery с beacon frames и active discovery с probe requests.
- После discovery client выбирает AP, проходит association и начинает обмен.
- 802.11 использует Layer 2 acknowledgements, потому что wireless среда менее надежна, чем кабель.

## Главное

- Нельзя проектировать Wi-Fi только по принципу "сделаем сигнал мощнее".
- Directional antenna помогает сфокусировать передачу, но не делает телефон дальнобойным устройством.
- Для одной маленькой точки может хватить autonomous AP.
- Для сети с несколькими locations лучше centralized management.
- У lightweight и cloud-managed моделей есть зависимость: controller, internet, license, vendor platform.
- При выборе модели нужно заранее понимать, что произойдет при отказе controller или истечении лицензии.
- Некоторое количество retransmissions и dropped frames в Wi-Fi нормально.

## Заметки

Выбор wireless access point кажется простой задачей:

```text
Купить WAP.
Закрепить.
Получить Wi-Fi.
```

В реальном deployment это быстро усложняется.

В NetworkChuck Coffee разные зоны требуют разных решений:

- front lobby;
- patio;
- pickup area;
- back office;
- кассовая зона;
- outdoor seating.

Одна и та же business network, но разные physical requirements.

## Типы точек доступа по среде

Access points могут быть рассчитаны на разные условия.

Примеры:

- indoor AP;
- outdoor AP;
- AP для high-density среды;
- AP с built-in antennas;
- AP с external antennas;
- AP для специальных условий.

Outdoor AP должен выдерживать погоду, температуру, влагу и физическую среду. Indoor AP обычно не рассчитан на это.

High-density AP важен там, где много клиентов одновременно: кафе, аудитории, офисы, конференц-залы.

## Антенны

Антенна определяет, как распространяется сигнал.

`Omnidirectional antenna` распространяет сигнал широко вокруг точки доступа.

Это полезно для обычных помещений, где клиенты находятся в разных направлениях.

`Directional antenna` фокусирует сигнал в одном направлении.

Это полезно, когда нужно покрыть конкретную область:

- patio;
- warehouse aisle;
- длинный коридор;
- parking pickup line;
- outdoor zone.

Но directional antenna не решает все.

## Двусторонняя связь

Главная ошибка:

```text
AP может докричаться до клиента, значит связь будет работать.
```

Не обязательно.

Wireless communication - двусторонняя.

Access point может иметь мощную антенну и хорошо передавать сигнал далеко. Но телефон, tablet или laptop может не иметь мощности и антенны, чтобы надежно ответить обратно.

Правильная мысль:

```text
Если client слышит AP, это еще не значит, что AP хорошо слышит client.
```

Поэтому range - это не только "как далеко вещает AP". Это способность двух сторон вести нормальный разговор.

## Пример с pickup line

Представь school pickup line или parking pickup area у NetworkChuck Coffee.

На схеме может казаться, что один AP с directional antenna покроет всю линию машин.

Client devices видят SSID. Сигнал вроде есть.

Но connection нестабильный, потому что tablets и phones не могут надежно отправлять ответный сигнал назад.

Это типичная ловушка wireless design: смотреть только на сторону AP и забывать про сторону client.

## Модели управления WAP

В реальных сетях обычно встречаются три practical модели:

- autonomous WAP;
- lightweight WAP;
- cloud-managed WAP.

Названия у vendor могут отличаться, но идея примерно такая.

## Автономные WAP

`Autonomous WAP` управляется отдельно.

Один AP:

- свой интерфейс управления;
- своя конфигурация;
- свои настройки SSID;
- свои security settings;
- свои channels и power settings.

Это удобно для маленькой среды.

Примеры:

- home network;
- маленький офис;
- одна точка с одним-двумя AP;
- простой all-in-one router с Wi-Fi.

Минус очевиден: если AP много, управлять каждым отдельно становится неудобно и рискованно.

## Легковесные WAP

`Lightweight WAP` зависит от `wireless LAN controller`, или `WLC`.

Идея:

```text
AP подключается к сети.
Находит controller.
Получает configuration.
Начинает работать.
```

В Cisco-среде для этого часто используется `CAPWAP`.

`CAPWAP` помогает AP найти controller, получить настройки и в некоторых designs туннелировать traffic обратно к controller.

Плюсы:

- centralized management;
- единые SSID и policies;
- проще управлять многими AP;
- удобнее менять настройки;
- лучше для campus и multi-site deployments.

Минус:

```text
Если controller недоступен, AP может потерять способность нормально работать.
```

Это зависит от модели и настроек, но dependency нужно учитывать заранее.

## Облачное управление WAP

`Cloud-managed WAP` тоже управляется централизованно, но controller находится в облаке vendor.

Обычно администратор входит в dashboard и управляет AP через интернет.

Плюсы:

- удобная панель;
- управление несколькими locations;
- быстрый rollout;
- vendor-hosted control plane;
- меньше локальной инфраструктуры.

Минусы:

- зависимость от subscription;
- зависимость от vendor cloud;
- возможные ограничения при потере internet;
- риск изменения licensing model;
- нужно понимать, что продолжит работать без cloud connectivity.

Cloud management удобен, но удобство всегда имеет цену.

## Вопросы перед выбором модели

При выборе между autonomous, lightweight и cloud-managed AP не смотри только на features.

Спроси:

- что будет, если controller died;
- что будет, если internet down;
- что будет, если license expired;
- можно ли продолжать обслуживать clients;
- где хранится configuration;
- как быстро заменить AP;
- есть ли vendor lock-in;
- как это масштабируется на несколько locations.

Это design questions, а не только purchasing questions.

## Сценарий NetworkChuck Coffee

Для одной маленькой кофейни autonomous AP может быть приемлемым.

Но если NetworkChuck Coffee растет:

- несколько stores;
- guest Wi-Fi;
- staff Wi-Fi;
- POS tablets;
- outdoor seating;
- pickup area;
- камеры;
- единые security policies;
- одинаковые SSID.

Тогда centralized management становится намного привлекательнее.

Никто не хочет заходить на 12 AP по отдельности, чтобы изменить один SSID или password.

## Как client находит Wi-Fi

Client device не знает магически все сети вокруг.

Есть два основных способа discovery:

- passive discovery;
- active discovery.

## Пассивное обнаружение

При passive discovery access point периодически отправляет beacon frame.

Beacon говорит примерно:

```text
Я здесь.
Вот SSID, который я предлагаю.
Вот мои параметры.
```

Client слышит beacon и добавляет network в список доступных Wi-Fi networks.

Именно поэтому иногда Wi-Fi list уже заполнен сетями, когда ты его открываешь.

## Активное обнаружение

При active discovery client сам отправляет probe request.

Идея:

```text
Какие networks есть рядом?
```

Nearby AP отвечают probe response и сообщают, какие SSID они предлагают.

Именно поэтому иногда после открытия Wi-Fi list новые networks появляются через секунду.

Client не просто ждет. Он ищет.

## Подключение association

После discovery client выбирает AP и начинает association.

Упрощенный flow:

```text
Hear beacons.
Send probes.
Choose network.
Associate.
Authenticate.
Communicate.
```

Под капотом больше деталей, особенно с security, но high-level идея такая: client нашел сеть, выбрал AP, согласовал подключение и начал обмен.

## Почему Wi-Fi не такой чистый, как Ethernet

Ethernet через кабель намного более контролируемый.

Wi-Fi работает в messy среде:

- interference;
- signal loss;
- retries;
- dropped frames;
- reflection;
- clients moving;
- changing signal quality.

Поэтому 802.11 включает acknowledgements на Layer 2.

Устройство фактически делает быстрые проверки:

```text
Получил?
Да.

Не получил?
Отправь снова.
```

Это происходит быстро и постоянно.

## Повторные передачи не всегда авария

Если при troubleshooting Wi-Fi ты видишь retransmissions или dropped frames, не нужно сразу паниковать.

Некоторое количество проблем в wireless среде ожидаемо.

Цель не в идеальном Wi-Fi без единой потери. Это фантазия.

Цель:

```text
Wireless должен быть достаточно хорошо спроектирован, чтобы reliably support business need.
```

Для NetworkChuck Coffee это значит:

- guest Wi-Fi работает;
- staff tablets не теряют связь;
- POS devices стабильны;
- outdoor или pickup зона покрыта разумно;
- design учитывает двухстороннюю связь;
- AP management не становится single point of surprise.

## Практический совет

При выборе WAP не спрашивай только:

```text
Как далеко он бьет?
```

Спроси:

- кто clients;
- смогут ли clients отвечать обратно;
- нужна ли outdoor модель;
- нужна ли directional antenna;
- сколько AP будет в сети;
- кто управляет configuration;
- что происходит при отказе controller;
- что происходит без internet;
- нужна ли subscription;
- как сеть масштабируется.

Это реальные вопросы deployment, а не маркетинговые характеристики.

## Главный вывод

Wireless access point - это не просто коробка с Wi-Fi.

Нужно выбрать тип AP, тип антенны, модель управления и понять, как clients будут обнаруживать сеть и подключаться к ней.

Autonomous проще, но хуже масштабируется. Lightweight хорошо подходит для enterprise, но зависит от controller. Cloud-managed удобно, но привязано к vendor cloud и subscription.

А сам Wi-Fi остается messy средой: client discovery, association, acknowledgements, retries и signal quality важны так же, как выбор hardware.

## Команды и термины

| Термин | Значение |
| --- | --- |
| `WAP` | Wireless Access Point, точка беспроводного доступа. |
| access point | Устройство, предоставляющее Wi-Fi. |
| omnidirectional antenna | Антенна с широким распространением сигнала вокруг AP. |
| directional antenna | Антенна, фокусирующая сигнал в выбранном направлении. |
| autonomous AP | AP, который управляется отдельно. |
| lightweight AP | AP, который получает управление от `WLC`. |
| cloud-managed AP | AP, управляемый через облачную платформу vendor. |
| `WLC` | Wireless LAN Controller, централизованный controller для AP. |
| `CAPWAP` | Протокол для связи AP с controller в Cisco-среде. |
| beacon | Периодическое объявление сети от AP. |
| probe request | Запрос client о доступных wireless networks. |
| association | Процесс подключения client к AP. |
| acknowledgement | Подтверждение получения frame на Layer 2. |
| retransmission | Повторная отправка frame. |

## Вопросы

### 1. Почему дальность AP не гарантирует хорошее подключение?

Ответ: Client должен не только слышать AP, но и иметь возможность надежно отправить ответный сигнал обратно.

### 2. Чем autonomous AP отличается от lightweight AP?

Ответ: Autonomous AP управляется отдельно, а lightweight AP получает configuration от controller.

### 3. Что делает CAPWAP?

Ответ: Помогает lightweight AP найти controller, получить настройки и в некоторых designs туннелировать traffic.

### 4. Чем passive discovery отличается от active discovery?

Ответ: При passive discovery client слушает beacons от AP, а при active discovery сам отправляет probe requests.

### 5. Почему retransmissions в Wi-Fi не всегда означают катастрофу?

Ответ: Wireless среда менее надежна, поэтому 802.11 ожидает некоторые retries и acknowledgements на Layer 2.

## Что повторить позже

- Indoor и outdoor AP.
- Directional и omnidirectional antennas.
- Разницу между autonomous, lightweight и cloud-managed AP.
- Роль `WLC` и `CAPWAP`.
- Passive и active discovery.
- Association process.
- Почему wireless требует acknowledgements и retransmissions.
