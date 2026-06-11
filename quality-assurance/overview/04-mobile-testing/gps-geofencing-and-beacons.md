# GPS, Geofencing и Beacons для Mobile QA

Source: user-provided article, corrected and expanded with official Android and Apple documentation  
Date added: 2026-06-11  
Related plan item: Mobile Testing  
Tags: QA, mobile testing, GPS, GNSS, geofencing, BLE, beacons, location  
Language: Russian  
Translation pair: quality-assurance-en/overview/04-mobile-testing/gps-geofencing-and-beacons.md

## Summary

Location-aware mobile products используют несколько разных технологий:

- **GPS/GNSS** помогает определить coordinates устройства по спутниковым сигналам;
- **platform location services** объединяют GNSS, Wi-Fi, cellular network и sensors;
- **geofencing** создаёт virtual region и генерирует события enter, exit или dwell;
- **BLE beacon** передаёт короткий radio identifier, по которому nearby device оценивает proximity;
- **RFID** идентифицирует tags через совместимый reader и чаще применяется для assets и inventory.

Для QA важно не смешивать эти понятия. Geofence — логическое правило, а GPS, Wi-Fi, BLE или RFID — возможные источники proximity/location data.

## Key Points

- Mobile location обычно является результатом нескольких signals, а не только GPS.
- Indoor accuracy, tunnels, urban canyons и radio interference ухудшают результат.
- Geofence обычно задаётся center coordinates и radius.
- Основные transitions: `ENTER`, `EXIT` и `DWELL`.
- Geofence event может приходить с задержкой, особенно когда app находится в background.
- Для Android geofencing требуется precise location, а для background monitoring обычно также background location permission.
- Beacon обычно только broadcasts BLE advertisement; mobile device scans and interprets it.
- RSSI даёт приблизительную proximity, но не точное расстояние.
- Emulator и mock location полезны для repeatability, но финальная проверка требует real route и physical beacons.
- Location data является sensitive personal data.

## Notes

## GPS, GNSS и Location Services

GPS — американская Global Positioning System. Более общий термин **GNSS** включает GPS и другие satellite navigation systems.

Телефон может определять location с помощью:

- GNSS satellites;
- nearby Wi-Fi access points;
- cellular towers;
- Bluetooth signals;
- accelerometer, gyroscope и compass;
- previously known location;
- platform fused-location algorithms.

Поэтому утверждение «GPS не работает из-за облачности» слишком простое. На качество сильнее влияют:

- отсутствие clear sky view;
- здания и отражение radio signals;
- tunnel или underground parking;
- indoor environment;
- device antenna;
- power-saving mode;
- disabled precise location;
- stale cached location;
- manufacturer-specific background restrictions.

Location object обычно содержит не только latitude и longitude, но также accuracy, timestamp, а иногда altitude, speed и bearing.

## Что такое Geofencing

Geofence — virtual geographic region.

Круглая geofence задаётся:

```text
latitude + longitude + radius
```

Система может сообщать:

| Event | Meaning |
| --- | --- |
| Enter | Device оказался внутри region |
| Exit | Device покинул region |
| Dwell | Device оставался внутри достаточно долго |
| Initial trigger | App уже находится внутри или снаружи при регистрации |
| Expiration | Region больше не отслеживается после заданного времени |

Примеры:

- уведомить магазин, что customer приближается;
- напомнить о pickup;
- включить home automation;
- отметить прибытие сотрудника;
- показать location-based content;
- зарегистрировать выход asset из разрешённой зоны.

Geofence transition не обязательно происходит точно на нарисованной линии и в ту же секунду.

## Размер Region и Accuracy

Слишком маленький radius приводит к:

- пропущенным transitions;
- частому enter/exit около boundary;
- зависимости от случайной погрешности;
- повышенному battery usage.

Android documentation рекомендует для типичных Wi-Fi location conditions рассматривать minimum radius около 100 meters как practical starting point.

QA должен знать:

- configured radius;
- current reported accuracy;
- expected transition delay;
- dwell duration;
- expiration;
- maximum number of active regions;
- fallback behavior при недостаточной accuracy.

Если reported accuracy равна 150 m, нельзя уверенно проверять boundary geofence с radius 20 m.

## Permissions

### Android

Проверяйте:

- approximate location;
- precise location;
- allow while using app;
- allow only this time;
- deny;
- background location;
- permission downgrade через Settings;
- location services выключены;
- battery optimization и manufacturer restrictions.

Для Android geofencing требуется `ACCESS_FINE_LOCATION`. Для background geofence monitoring на Android 10+ обычно требуется `ACCESS_BACKGROUND_LOCATION`.

Permission request должен объяснять пользу и появляться в контексте feature, а не автоматически требовать максимальный доступ при первом launch.

### iOS

Проверяйте:

- Allow Once;
- Allow While Using App;
- Allow Always, когда feature действительно требует background monitoring;
- Don't Allow;
- Precise Location on/off;
- изменение permission в Settings;
- Background App Refresh;
- location services disabled globally.

Поведение permission prompts зависит от current authorization state и OS version. Тестируйте clean install и upgrade separately.

## Geofence Test Matrix

### Registration

- valid coordinates and radius;
- invalid coordinates;
- zero/negative/very large radius;
- duplicate region ID;
- maximum number of regions;
- expiration;
- app update;
- device reboot;
- logout и login другого user.

### Transitions

- outside -> inside;
- inside -> outside;
- initial state inside;
- initial state outside;
- quick boundary crossing;
- dwell;
- repeated crossing;
- movement parallel to boundary;
- location jump;
- low-accuracy update;
- transition after long offline period.

### Application State

- foreground;
- background;
- terminated;
- device locked;
- device rebooted;
- low-power mode;
- network unavailable;
- app permission changed;
- notification permission denied.

Geofence может сработать корректно, но пользователь не увидит notification из-за отдельного notification permission или disabled channel.

## Типичные Geofencing Defects

- `ENTER` вызывается несколько раз для одного visit.
- `EXIT` не приходит после быстрого пересечения.
- Initial trigger создаёт ложное повторное событие.
- Region регистрируется для неправильных coordinates.
- Radius передан в неверных units.
- Dwell timer не сбрасывается после exit.
- Старые regions остаются после logout.
- Другой account получает событие предыдущего пользователя.
- App считает mock location реальным production event.
- Notification содержит устаревший offer.
- Background restriction задерживает event, а UI показывает его как real-time.
- Analytics считает один physical visit несколько раз.

## Что такое BLE Beacon

Beacon — небольшой Bluetooth Low Energy transmitter, который периодически broadcasts advertisement packet.

Обычно beacon:

- не знает, кто находится рядом;
- не подключается к интернету самостоятельно;
- не определяет GPS coordinates;
- передаёт identifier и calibration data;
- питается от battery или постоянного power source.

Mobile app или gateway scans BLE advertisements и оценивает proximity по received signal strength, или RSSI.

Типичный flow:

```text
Beacon broadcasts ID -> phone scans BLE -> app recognizes ID
-> business rule runs -> UI, analytics or notification action
```

iBeacon — Apple protocol/profile for proximity use cases. Существуют и другие beacon formats.

## RSSI и Proximity

RSSI зависит от:

- расстояния;
- calibrated transmit power;
- walls, shelves и people;
- device orientation;
- phone model и antenna;
- other radio traffic;
- beacon battery;
- scan interval.

Поэтому категории `immediate`, `near` и `far` являются приблизительными. RSSI нельзя считать точной линейкой.

При тестировании собирайте несколько measurements и проверяйте business thresholds, а не одно мгновенное значение.

## Beacon Test Matrix

- Bluetooth on/off;
- required Bluetooth/location permissions;
- app foreground/background;
- beacon in range/out of range;
- near/far threshold;
- несколько beacons рядом;
- одинаковый identifier по ошибке;
- weak battery;
- blocked signal;
- phone в pocket или bag;
- different phone models;
- rapid movement;
- stationary dwell;
- device reboot;
- app reinstall;
- beacon replacement;
- offline device;
- delayed server sync.

Physical test area должна иметь documented beacon placement, identifiers, transmit power и expected ranges.

## Geofence Vs Beacon

| Characteristic | Geofence | BLE Beacon |
| --- | --- | --- |
| Best environment | Outdoor/large regions | Indoor/small proximity zones |
| Main input | Platform location | BLE advertisement |
| Typical scale | Tens/hundreds of meters and more | Near-room or near-object proximity |
| Infrastructure | Usually no local hardware | Physical beacon installation |
| Accuracy | Depends on location accuracy | Depends on RSSI and radio environment |
| Background limits | Location/OS restrictions | Bluetooth scanning/OS restrictions |
| Common use | Arrival, departure, regional trigger | In-store zone, exhibit, nearby asset |

Продукт может использовать coarse geofence, чтобы определить arrival near a building, а beacon — чтобы определить конкретную indoor zone.

## RFID Vs Beacon

| Characteristic | RFID | BLE Beacon |
| --- | --- | --- |
| Object | RFID tag | Active BLE transmitter |
| Reader | Dedicated reader or compatible NFC device | BLE-capable phone/gateway |
| Power | Passive tags могут быть без battery | Beacon обычно требует power |
| Typical use | Inventory, access, asset identification | Proximity and indoor engagement |
| Mobile support | Зависит от RFID type | BLE широко поддерживается phones |

RFID geofencing часто означает business rule вокруг reader locations, а не GPS-style circular region.

## Mock Location и Simulation

Используйте:

- Android mock location app;
- Android Emulator location controls;
- GPX routes в iOS Simulator/Xcode;
- scripted coordinates;
- test backend events;
- shielded or controlled beacon test area.

Проверяйте:

- static point;
- realistic route;
- different speed;
- teleport/jump;
- pause on boundary;
- inaccurate point;
- stale timestamp;
- impossible speed;
- mocked-location policy, если она существует.

Simulation ускоряет regression, но не воспроизводит полностью antenna, buildings, background scheduling и real movement.

## Battery и Performance

Location и BLE scanning могут расходовать battery.

Проверяйте:

- scan frequency;
- location update interval;
- background duration;
- CPU wakeups;
- network sync frequency;
- duplicate registration;
- app behavior in low-power mode;
- device temperature;
- battery usage over a representative session.

Feature не должна запрашивать continuous high-accuracy updates, если достаточно geofence transition или low-frequency location.

## Security And Privacy

- Запрашивайте только необходимый location access.
- Объясняйте purpose до system prompt.
- Не храните raw location дольше необходимого.
- Не логируйте precise coordinates вместе с user identity без защиты.
- Проверяйте deletion, consent withdrawal и account logout.
- Не используйте proximity как единственный фактор authorization.
- Server должен валидировать high-risk operations независимо от client location.
- Beacon identifier не является секретом и может быть copied or replayed.

Location и movement history могут раскрывать дом, работу, здоровье и привычки пользователя.

## Diagnostics

Для defect собирайте:

- device model и OS;
- app build;
- coordinates и accuracy;
- timestamp/timezone;
- permission state;
- precise/approximate mode;
- foreground/background state;
- location services state;
- battery mode;
- geofence ID, center, radius и transition;
- beacon identifier, RSSI и transmit power;
- Bluetooth state;
- expected и actual delay;
- screen recording, logs и route.

Android logs:

```bash
adb logcat
adb shell dumpsys location
adb shell dumpsys bluetooth_manager
```

Не отправляйте raw location logs без privacy review.

## QA Checklist

- [ ] Технология определена: location geofence, BLE beacon или RFID.
- [ ] Permission states покрыты.
- [ ] Precise и approximate location проверены.
- [ ] Enter, exit, dwell и initial trigger проверены.
- [ ] Boundary и low-accuracy scenarios покрыты.
- [ ] Foreground, background и terminated states проверены.
- [ ] Reboot, update, logout и account switch покрыты.
- [ ] Mock route дополнен real-world route.
- [ ] Beacon tests выполнены на нескольких physical devices.
- [ ] Battery и delayed events измерены.
- [ ] Notifications и analytics не дублируются.
- [ ] Location data проходит privacy review.

## Interview Focus

1. Чем GPS/GNSS отличается от platform location service?
2. Что такое geofence и какие transitions она поддерживает?
3. Почему geofence event может прийти с задержкой?
4. Чем beacon отличается от GPS geofence?
5. Почему RSSI не является точным расстоянием?
6. Какие location permissions нужно проверить?
7. Почему mock location не заменяет real route?
8. Какие privacy risks связаны с location history?

## Sources

- User-provided article: "What Does It All Mean: Beacon Technology, GPS and Geofencing"
- [Android: Create and monitor geofences](https://developer.android.com/develop/sensors-and-location/location/geofencing)
- [Android: Request location permissions](https://developer.android.com/develop/sensors-and-location/location/permissions)
- [Apple Core Location](https://developer.apple.com/documentation/corelocation)
- [Apple iBeacon](https://developer.apple.com/ibeacon/)

