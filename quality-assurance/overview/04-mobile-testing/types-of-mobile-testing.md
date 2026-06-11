# Типы мобильного тестирования

Source: user-provided BrowserStack material, adapted for the QA study guide  
Date added: 2026-06-11  
Related plan item: Mobile Testing  
Tags: QA, mobile testing, functional, interruption, compatibility, performance, security  
Language: Russian  
Translation pair: quality-assurance-en/overview/04-mobile-testing/types-of-mobile-testing.md

## Summary

Мобильное тестирование проверяет продукт не только как набор функций, но и как приложение, работающее на разных устройствах, версиях OS, экранах, сетях и в условиях постоянных системных прерываний.

Основные направления:

- functional testing;
- interruption and lifecycle testing;
- compatibility testing;
- usability and accessibility testing;
- localization testing;
- performance testing;
- security testing;
- installation and update testing;
- network testing;
- API and integration testing.

Эти типы не изолированы. Один сценарий покупки может одновременно проверять UI, API, сеть, безопасность, производительность и восстановление после interruption.

## Key Points

- Mobile testing учитывает hardware, OS, permissions, network и application lifecycle.
- Functional testing подтверждает business requirements и user flows.
- Compatibility testing требует осмысленной device matrix, а не случайного набора телефонов.
- Interruption testing проверяет calls, notifications, charging, network loss и background transitions.
- Speed, memory, battery и stability входят в более широкое performance testing.
- Security testing охватывает данные на устройстве, transport, authentication, sessions и APIs.
- Virtual devices удобны для широкого покрытия, но critical flows следует проверять на real devices.
- Test strategy должна быть risk-based: не каждый build требует полного набора всех видов тестирования.

## Notes

## Почему мобильному продукту нужны отдельные проверки

По сравнению с desktop или обычным web-продуктом мобильное приложение сильнее зависит от:

- manufacturer и device model;
- Android/iOS version;
- screen size, density, notch и foldable state;
- CPU, RAM, storage и battery;
- camera, GPS, Bluetooth, NFC и biometrics;
- permissions;
- Wi-Fi, cellular network и offline mode;
- incoming calls, messages и notifications;
- background execution rules;
- App Store или Google Play distribution.

Поэтому успешный happy path на одном устройстве не доказывает качество mobile application.

## Карта видов тестирования

| Direction | Main question | Typical risks |
| --- | --- | --- |
| Functional | Работают ли функции по требованиям? | Неверный результат, сломанный flow |
| Interruption and lifecycle | Восстанавливается ли app после системных событий? | Потеря state, crash, duplicate action |
| Compatibility | Работает ли app в поддерживаемой matrix? | Layout, OS, hardware и browser differences |
| Usability and accessibility | Может ли пользователь удобно выполнить задачу? | Плохая navigation, touch targets, barriers |
| Localization | Корректен ли продукт для locale и region? | Truncation, formats, RTL, cultural errors |
| Performance | Достаточно ли app быстро и стабильно? | Slow launch, jank, memory leak, battery drain |
| Security | Защищены ли данные и операции? | Data leak, broken auth, insecure storage |
| Installation and update | Корректен ли lifecycle build? | Failed install, data loss, migration errors |
| Network | Переживает ли app реальные условия связи? | Timeout, duplicate request, stale data |
| API and integration | Правильно ли mobile client взаимодействует с services? | Contract, parsing, error handling |

## 1. Functional Testing

Functional testing подтверждает, что features и business rules работают согласно требованиям.

Примеры:

- app устанавливается и запускается;
- registration, login и logout работают;
- buttons, fields, menus и gestures выполняют ожидаемые действия;
- push notifications открывают правильный экран;
- search, filters и sorting возвращают правильные данные;
- purchase или payment завершается один раз;
- validation и error messages соответствуют ситуации;
- permissions запрашиваются в нужный момент;
- deep links ведут к правильному content.

Проверяйте:

- positive и negative scenarios;
- boundary values;
- разные user roles;
- сохранение данных;
- повторные действия и idempotency;
- поведение после relaunch.

## 2. Interruption And Lifecycle Testing

Mobile application регулярно теряет focus, уходит в background, приостанавливается или уничтожается OS.

Типичные interruptions:

- incoming call;
- SMS или notification;
- alarm;
- screen lock;
- переход в другое app;
- подключение или отключение charger;
- low battery;
- потеря и восстановление network;
- изменение orientation;
- permission dialog;
- OS update или device restart.

Проверяйте:

- сохраняется ли введённый state;
- продолжается, отменяется или безопасно повторяется операция;
- не отправляется ли payment/request дважды;
- корректно ли восстанавливаются media, timer и navigation;
- скрывается ли sensitive content в app switcher;
- правильно ли обновляются данные после возвращения.

`Don't keep activities` может помочь найти lifecycle defects, но не заменяет реальные background и process-death scenarios.

## 3. Compatibility Testing

Compatibility testing проверяет application в поддерживаемых combinations.

### Device compatibility

- manufacturers и models;
- low-end и high-end hardware;
- screen sizes и densities;
- phones, tablets и foldables;
- camera, GPS, Bluetooth, NFC и biometrics.

### OS compatibility

- minimum supported version;
- наиболее популярные versions;
- latest supported version;
- manufacturer skins и system restrictions.

### Browser compatibility

Для mobile web и PWA:

- Chrome;
- Safari;
- Firefox;
- Samsung Internet;
- WebView versions.

### Network compatibility

- Wi-Fi;
- cellular networks;
- roaming;
- VPN или proxy;
- offline mode;
- high latency и packet loss.

Device matrix формируется по analytics, target audience, market share, business risk и technical requirements.

## 4. Usability And Accessibility Testing

Usability testing оценивает, насколько легко пользователь понимает interface и выполняет задачу.

Проверяйте:

- понятную navigation;
- достаточный размер touch targets;
- удобство one-handed use;
- readable text;
- keyboard behavior;
- отсутствие лишних steps;
- feedback после actions;
- понятные errors и recovery;
- consistency между screens.

Accessibility дополняет usability:

- screen reader labels;
- logical focus order;
- dynamic text scaling;
- color contrast;
- управление без сложных gestures;
- landscape и zoom;
- отсутствие зависимости только от цвета.

Оценка «мне удобно» недостаточна. Используйте requirements, platform guidelines и реальные user scenarios.

## 5. Localization Testing

Localization testing проверяет адаптацию к language, locale и region.

Покрытие:

- translation и terminology;
- text expansion и truncation;
- date, time и timezone;
- decimal и thousand separators;
- currency;
- names, addresses и phone formats;
- plural forms;
- right-to-left layout;
- local content и legal requirements.

Меняйте не только язык, но и system region, timezone, calendar и keyboard. Язык интерфейса и регион устройства могут отличаться.

## 6. Performance Testing

Performance testing мобильного приложения включает несколько подвидов.

### Speed and responsiveness

- cold, warm и hot start;
- screen load time;
- response на tap;
- scrolling smoothness;
- animation jank;
- API response и rendering time.

### Memory

- рост memory во время long session;
- освобождение resources после закрытия screen;
- повторное открытие тяжёлых flows;
- поведение на low-memory device;
- background и foreground cycles.

Постоянный рост memory может указывать на leak, но вывод требует profiling и повторяемых измерений.

### Battery and resources

- battery consumption;
- CPU usage;
- background work;
- GPS и sensor usage;
- network activity;
- device heating;
- storage growth.

### Stability and recovery

- длительная работа;
- многократное повторение operation;
- server overload;
- timeout;
- process restart;
- восстановление после temporary failure.

Измеряйте на real devices с зафиксированными build, OS, network и начальным состоянием.

## 7. Security Testing

Security testing проверяет защиту данных, identity и privileged operations.

Основные области:

- authentication и authorization;
- session expiration и logout;
- secure local storage;
- encryption in transit;
- certificate validation;
- permissions;
- logs и screenshots;
- clipboard;
- deep links;
- WebView;
- API access control;
- protection от tampering и reverse engineering согласно risk model.

Примеры:

- пользователь не видит данные другого account;
- token удаляется после logout;
- password не попадает в Logcat;
- sensitive screen защищён в background preview;
- app безопасно обрабатывает modified deep link;
- server не доверяет только client-side checks.

Security testing требует отдельной methodology и не сводится к запуску vulnerability scanner.

## 8. Installation, Update And Uninstallation Testing

Проверяйте:

- clean installation;
- first launch;
- недостаток storage;
- unsupported OS;
- update с предыдущих supported versions;
- database and preferences migration;
- interrupted update;
- сохранение login и user data;
- rollback, если он поддерживается;
- uninstall и cleanup;
- reinstall после uninstall.

Критический сценарий — обновление production user с реальными накопленными данными, а не только установка свежего build.

## 9. Network Testing

Mobile network непостоянна, поэтому важно проверять:

- offline launch;
- медленную сеть;
- high latency;
- packet loss;
- timeout;
- переключение Wi-Fi на cellular и обратно;
- краткий disconnect;
- duplicate и reordered actions;
- retry;
- cached и stale data;
- upload/download interruption.

После восстановления связи приложение не должно незаметно дублировать payment, order, message или file upload.

Network throttling tools полезны для повторяемости, но critical behavior также проверяется в реальных условиях.

## 10. API And Integration Testing

Mobile client зависит от backend, push providers, maps, analytics, payments и других services.

Проверяйте:

- request method, headers и body;
- status codes и response schema;
- authentication и refresh token;
- pagination;
- timeout и retry;
- backward compatibility;
- invalid и partial data;
- duplicate requests;
- third-party service failure;
- client behavior при новой или неизвестной response field.

API testing помогает локализовать defect: проблема находится в client UI, network layer, backend contract или external service.

## Дополнительные направления

В зависимости от продукта strategy может включать:

- accessibility testing;
- privacy testing;
- compliance testing;
- push notification testing;
- payment testing;
- sensor and hardware testing;
- data migration testing;
- exploratory testing;
- store submission testing;
- analytics validation;
- recovery and resilience testing.

Это не конкурирующие классификации. Один test case может относиться сразу к нескольким направлениям.

## Real Devices, Emulators And Simulators

Используйте environments совместно:

| Environment | Best suited for |
| --- | --- |
| Emulator/simulator | Быстрый functional regression, OS profiles, automation |
| Real device | Sensors, battery, performance, calls, camera, Bluetooth, real UX |
| Device cloud | Широкая device matrix и parallel execution |

Не каждый test обязан выполняться на real device, но release confidence без проверки critical flows на physical hardware будет ограничен.

## Как выбрать проверки для build

### Smoke build

- install and launch;
- login;
- основной business flow;
- critical API;
- crash check;
- один representative device на platform.

### Feature build

- functional and negative tests;
- relevant permissions;
- interruptions;
- affected API integrations;
- targeted compatibility;
- regression around changed modules.

### Release candidate

- full critical regression;
- supported OS/device matrix;
- installation and update;
- performance sanity;
- security and privacy checks;
- localization;
- real network and real device coverage;
- store requirements.

## QA Checklist

- [ ] Определён тип приложения и supported platforms.
- [ ] Составлена risk-based device matrix.
- [ ] Проверены critical functional flows.
- [ ] Покрыты background, interruption и recovery.
- [ ] Проверены permissions и hardware integrations.
- [ ] Есть offline и unstable-network scenarios.
- [ ] Выполнены localization и accessibility checks.
- [ ] Измерены launch, memory, battery и stability.
- [ ] Проверены authentication, storage и sensitive data.
- [ ] Протестировано обновление с предыдущей версии.
- [ ] Critical flows повторены на real devices.
- [ ] Environment details приложены к defects.

## Interview Focus

1. Какие основные типы mobile testing вы знаете?
2. Чем interruption testing отличается от обычного functional testing?
3. Как сформировать device matrix?
4. Какие проверки входят в mobile performance testing?
5. Почему emulator не заменяет real device?
6. Как тестировать переход между Wi-Fi и cellular network?
7. Какие риски нужно проверить при обновлении приложения?

## Sources

- User-provided BrowserStack article: "Types of Mobile Testing"
- [Types of Mobile Testing](https://www.browserstack.com/guide/types-of-mobile-testing)

