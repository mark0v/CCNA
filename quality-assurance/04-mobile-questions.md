# Mobile Testing Questions

Source: Interview Prep  
Date added: 2026-05-25  
Related plan item: QA interview preparation  
Tags: QA, mobile testing, iOS, Android, PWA, hybrid, cross-platform  
Language: Russian  

## Summary

Материал покрывает mobile QA: типы мобильных приложений, iOS/Android testing, device coverage, app lifecycle, network changes, push notifications, permissions, reconnects, performance и mobile-specific bug reporting.

Для вакансии важно связывать ответы с real-time poker behavior: нестабильная сеть, background/foreground, session continuity, reconnect и синхронизация игрового состояния.

## Key Points

- Native, web, PWA, hybrid и cross-platform приложения отличаются архитектурой, доступом к OS features, производительностью и QA-рисками.
- Даже при общей кодовой базе iOS и Android нужно тестировать отдельно: platform-specific баги остаются.
- Для mobile QA особенно важны реальные устройства, версии OS, permissions, push, background/foreground, network switch и performance.
- PWA и WebView требуют отдельного внимания к cache, service worker, storage, keyboard, scrolling и ограничениям браузера.
- Для real-time mobile продукта критичны reconnect, session continuity и корректное состояние после плохой сети.

## Notes

## 1. Виды мобильных приложений: native, web, hybrid/cross-platform

Мобильные приложения обычно делят на несколько типов:

- **Native apps / нативные приложения**
- **Web apps / мобильные веб-приложения**
- **PWA / Progressive Web Apps**
- **Hybrid apps / гибридные приложения**
- **Cross-platform apps / кроссплатформенные приложения**

Иногда hybrid и cross-platform называют "смешанным" подходом, но технически между ними есть разница.

### Native apps

**Native app** - приложение, разработанное специально под конкретную платформу.

Для iOS обычно используют:

- Swift
- Objective-C

Для Android:

- Kotlin
- Java

Приложение устанавливается из App Store или Google Play и имеет прямой доступ к возможностям устройства.

Преимущества:

- лучшая производительность;
- лучший доступ к hardware и OS features: camera, GPS, push notifications, biometrics, Bluetooth, background modes;
- нативный UI/UX для платформы;
- лучше подходит для сложных, real-time и performance-sensitive приложений;
- стабильнее работа с lifecycle: background, foreground, permissions, notifications.

Недостатки:

- нужно разрабатывать отдельно для iOS и Android;
- выше стоимость разработки и поддержки;
- логика может расходиться между платформами;
- релизы зависят от App Store/Google Play review;
- баг может быть только на одной платформе.

QA-фокус:

- проверять отдельно iOS и Android;
- учитывать версии OS;
- тестировать реальные устройства, не только эмуляторы;
- проверять permissions, push, background/foreground, network switch, performance, battery usage.

Пример: для poker platform native app хорошо подходит, потому что нужна стабильная работа real-time table, быстрый UI, push, reconnect и корректное поведение при нестабильной сети.

### Web apps

**Web app** - это сайт или веб-приложение, которое открывается в мобильном браузере.

Пользователь не устанавливает приложение из store, а открывает его через Safari, Chrome или другой браузер.

Преимущества:

- одна кодовая база для разных платформ;
- быстрее релизы, не нужен review в App Store/Google Play;
- проще обновлять;
- доступно по ссылке;
- дешевле разработка и поддержка.

Недостатки:

- ограниченный доступ к возможностям устройства;
- производительность может быть ниже, чем у native;
- поведение зависит от браузера;
- хуже offline/background возможности;
- push notifications и permissions имеют ограничения, особенно на iOS;
- UX может быть менее нативным.

QA-фокус:

- проверять разные mobile browsers;
- responsive layout;
- touch interactions;
- orientation;
- browser cache;
- network throttling;
- ограничения Safari/Chrome;
- поведение при обновлении страницы или закрытии вкладки.

Пример: web app может быть удобен для lobby, профиля или просмотра истории, но для live poker table с real-time действиями web может требовать особенно тщательной проверки WebSocket, latency и reconnect.

### PWA

**PWA / Progressive Web App** - это web app с дополнительными возможностями, похожими на приложение: установка на home screen, service worker, cache, offline или частично offline режим, push notifications в некоторых случаях.

Преимущества:

- работает как web, но ощущается ближе к app;
- можно установить на home screen;
- можно кешировать ресурсы;
- обновляется без store review;
- одна кодовая база.

Недостатки:

- ограничения зависят от платформы и браузера;
- не все native features доступны;
- push/background возможности ограничены;
- service worker/cache могут создавать баги со старой версией приложения;
- на iOS PWA обычно имеет больше ограничений, чем на Android.

QA-фокус:

- установка/удаление PWA;
- service worker;
- cache invalidation;
- offline/online transitions;
- обновление версии;
- push, если поддерживается;
- поведение после очистки storage/cache.

### Hybrid apps

**Hybrid app** - мобильное приложение, которое устанавливается как обычное app, но внутри часто использует WebView для отображения web-контента.

Примеры технологий:

- Ionic
- Cordova
- Capacitor

Преимущества:

- одна web-based кодовая база;
- можно распространять через stores;
- есть доступ к части native capabilities через plugins;
- дешевле и быстрее, чем два полностью native приложения;
- удобно, если команда сильнее в web.

Недостатки:

- производительность часто ниже, чем у native;
- WebView может вести себя по-разному на iOS и Android;
- зависимость от plugins;
- сложнее debugging между native wrapper и web content;
- UX может быть менее нативным;
- возможны проблемы с keyboard, scrolling, gestures, WebView cache.

QA-фокус:

- проверять WebView-specific баги;
- keyboard overlap;
- scrolling;
- permissions через plugins;
- file upload;
- deep links;
- push notifications;
- cache/storage внутри WebView;
- отличия iOS/Android WebView.

### Cross-platform apps

**Cross-platform app** - приложение с одной основной кодовой базой, которое собирается под iOS и Android, но рендерит UI ближе к native или использует общий runtime.

Примеры технологий:

- React Native
- Flutter
- Xamarin / .NET MAUI

Преимущества:

- одна основная кодовая база для iOS и Android;
- быстрее разработка, чем два отдельных native apps;
- производительность обычно лучше, чем у классического hybrid/WebView;
- доступ к native modules;
- проще держать одинаковую бизнес-логику на обеих платформах.

Недостатки:

- все равно могут быть platform-specific bugs;
- иногда нужны native developers для сложных модулей;
- зависимость от framework и packages;
- обновления framework могут ломать поведение;
- performance может уступать полностью native в сложных сценариях.

QA-фокус:

- проверять обе платформы, даже если код общий;
- искать platform-specific issues;
- тестировать native modules: push, permissions, biometrics, deep links;
- проверять UI differences;
- performance на слабых устройствах;
- app lifecycle и reconnect.

### Короткое сравнение

| Тип приложения | Как работает | Плюсы | Минусы |
|---|---|---|---|
| Native | Отдельное приложение под iOS/Android | Лучшая производительность, полный доступ к OS features | Дороже, две кодовые базы |
| Web app | Открывается в мобильном браузере | Быстрые релизы, одна кодовая база | Ограничения браузера, меньше native features |
| PWA | Web app с установкой/cache/service worker | Похоже на app, без store review | Ограничения платформ, cache/service worker issues |
| Hybrid | App wrapper + WebView | Быстрее разработка, доступ к plugins | WebView bugs, ниже performance |
| Cross-platform | Одна кодовая база, сборка под iOS/Android | Баланс скорости и качества, ближе к native | Platform-specific bugs, зависимость от framework |

Хороший ответ на интервью:

"Основные виды мобильных приложений - native, web/PWA, hybrid и cross-platform. Native пишется отдельно под iOS и Android, дает лучшую производительность и доступ к возможностям устройства, но дороже в поддержке. Web app работает в браузере, проще обновляется и имеет одну кодовую базу, но ограничен браузером. Hybrid app устанавливается как приложение, но часто использует WebView, поэтому быстрее в разработке, но может иметь проблемы с performance и WebView. Cross-platform, например React Native или Flutter, дает одну основную кодовую базу и UI ближе к native, но все равно требует тестирования обеих платформ."

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Native app | Приложение, разработанное отдельно под iOS или Android. |
| Web app | Приложение, которое открывается в мобильном браузере. |
| PWA | Web app с установкой на home screen, service worker и cache-возможностями. |
| Hybrid app | Установленное приложение, которое часто отображает web-контент внутри WebView. |
| Cross-platform app | Приложение с общей кодовой базой для iOS и Android, например React Native или Flutter. |
| WebView | Встроенный браузерный компонент внутри mobile app. |
| App lifecycle | Состояния приложения: foreground, background, killed, restored. |
| Device coverage | Набор устройств, OS versions и экранов, которые нужно покрыть тестами. |

## What To Review Later

- Отличия native, web, PWA, hybrid и cross-platform apps.
- Какие проверки нужны отдельно для iOS и Android.
- Риски WebView, service worker и mobile browser cache.
- Background/foreground и reconnect scenarios.
- Как выбирать device coverage для QA.
