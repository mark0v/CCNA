# Типы мобильных приложений для QA

Source: pasted articles comparing mobile application types and technologies  
Date added: 2026-06-11  
Related plan item: Mobile Testing  
Tags: QA, mobile testing, native, hybrid, cross-platform, PWA, mobile web  
Language: Russian  
Translation pair: quality-assurance-en/overview/04-mobile-testing/mobile-app-types.md

## Summary

Мобильный продукт может быть реализован как mobile web app, Progressive Web App, native app, cross-platform app или hybrid app. Эти варианты отличаются способом запуска, technology stack, доступом к device features, distribution и типичными рисками.

Для QA тип приложения определяет:

- где и как устанавливать build;
- какие platforms and browsers покрывать;
- нужны ли App Store and Google Play checks;
- как тестировать permissions, hardware and background behavior;
- где искать проблемы: в web layer, native layer или integration bridge.

Главная мысль:

> Название технологии менее важно, чем понимание реальной architecture приложения и границ между его слоями.

## Key Points

- Mobile web app работает в browser и не устанавливается как обычное приложение.
- PWA является web app с manifest, service worker и дополнительными platform capabilities.
- Native app создаётся отдельно для конкретной platform.
- Cross-platform frameworks позволяют разделять code между iOS and Android, но приложение использует native runtime or compiled output.
- Hybrid app запускает web content внутри native container, обычно через WebView.
- React Native и Flutter корректнее относить к cross-platform development, а не к классическим WebView hybrid apps.
- Один и тот же product может иметь web, PWA and mobile app versions одновременно.

## Notes

## Mobile Web App

Mobile web app открывается по URL в mobile browser.

Обычно используется:

- HTML;
- CSS;
- JavaScript;
- responsive design;
- web frameworks.

Преимущества:

- не требует установки;
- обновляется на server;
- одна версия доступна на разных devices;
- легко распространяется ссылкой.

Ограничения:

- зависит от browser;
- ограниченный или неодинаковый доступ к device APIs;
- browser UI влияет на experience;
- offline support обычно ограничен;
- нет обычного store distribution.

QA focus:

- responsive layout;
- mobile browsers and rendering engines;
- touch interactions;
- viewport and orientation;
- virtual keyboard;
- browser permissions;
- slow and unstable networks;
- cookies and storage;
- deep links and URL navigation.

## Progressive Web App

PWA — web application, использующее современные browser capabilities для app-like experience.

Основные элементы:

- Web App Manifest;
- service worker;
- HTTPS;
- responsive UI;
- cache and offline strategy;
- installability where supported.

Возможности зависят от OS and browser. Нельзя считать, что PWA одинаково работает на Android and iOS.

QA checks:

- install prompt or Add to Home Screen;
- app icon and launch behavior;
- manifest fields;
- offline and cached content;
- update of service worker;
- stale cache;
- push notifications where supported;
- fallback when capability is unavailable.

## Native App

Native app создаётся для конкретной operating system.

Typical stacks:

- iOS: Swift or Objective-C;
- Android: Kotlin or Java.

Преимущества:

- полный доступ к platform APIs;
- native UI and behavior;
- высокая производительность;
- глубокая integration с device hardware;
- сильная offline support.

Риски:

- отдельные implementations могут вести себя по-разному;
- release cycles iOS and Android могут расходиться;
- platform-specific bugs;
- больше combinations of OS and devices.

QA focus:

- platform guidelines;
- permissions;
- lifecycle and background states;
- gestures;
- notifications;
- biometrics;
- camera, GPS and sensors;
- installation, update and uninstall;
- store builds and signing.

## Cross-Platform App

Cross-platform frameworks позволяют использовать значительную часть общей codebase для iOS and Android.

Examples:

- React Native;
- Flutter;
- Kotlin Multiplatform;
- .NET MAUI.

Frameworks работают по-разному:

- Flutter рисует UI своим rendering engine;
- React Native связывает application logic с native components;
- Kotlin Multiplatform позволяет разделять business logic при platform-specific UI.

Cross-platform не означает identical behavior.

QA focus:

- feature parity;
- platform-specific navigation;
- native components;
- bridge/plugin failures;
- performance;
- animations;
- platform permissions;
- shared defect versus platform-only defect;
- framework and plugin updates.

## Hybrid App

Hybrid app сочетает native container и web technologies. Web content обычно отображается внутри `WebView`.

Common technologies:

- Ionic;
- Apache Cordova;
- Capacitor.

Native plugins дают web code доступ к:

- camera;
- geolocation;
- files;
- notifications;
- device information.

QA должен проверять оба слоя:

1. Web content and API behavior.
2. Native shell, plugins and lifecycle.

Typical risks:

- blank WebView;
- broken back navigation;
- web and native session mismatch;
- external link opens incorrectly;
- permission granted in OS but unavailable to plugin;
- keyboard overlaps web form;
- content does not respect safe areas;
- old cached web bundle remains after update.

## Wrapper App

Wrapper app — частный вариант hybrid architecture, где существующий website or web app загружается внутри native shell.

Wrapper может добавлять:

- push notifications;
- native navigation;
- deep links;
- authentication integration;
- analytics;
- store distribution.

QA focus:

- remote content availability;
- behavior when website is unavailable;
- domain allowlist;
- external browser transitions;
- cookies and session;
- native-to-web communication;
- app review compliance;
- difference between website release and store build.

## Comparison

| Type | Runs in | Installed | Main UI | Device access | Main QA risk |
| --- | --- | --- | --- | --- | --- |
| Mobile web | Browser | No | Web | Limited/browser-dependent | Browser and responsive compatibility |
| PWA | Browser/standalone web mode | Optional | Web | Expanded but platform-dependent | Cache, installability and capability gaps |
| Native | OS runtime | Yes | Native | Full | Platform and device fragmentation |
| Cross-platform | Native/compiled framework runtime | Yes | Framework/native | Broad via framework/plugins | Shared code with platform-specific differences |
| Hybrid | Native shell + WebView | Yes | Web inside native container | Via plugins | Web/native integration |
| Wrapper | Native shell + existing web content | Yes | Mostly existing web UI | Via added native layer | Remote content and shell integration |

## Distribution, Updates And Storage

Тип приложения влияет не только на development, но и на delivery process.

| Type | Distribution | Updates | Device storage |
| --- | --- | --- | --- |
| Mobile web | URL/browser | Immediately on server deployment | Browser cache and site data |
| PWA | Browser/home-screen installation | Web deployment plus service worker update cycle | Cache, storage and offline assets |
| Native | App Store, Google Play or enterprise distribution | New build, review and user/device rollout | Installed application and local data |
| Cross-platform | Same as native | New platform builds, sometimes shared release | Installed application and local data |
| Hybrid/wrapper | Stores or enterprise distribution | Native shell update and/or remote web update | Native package, WebView cache and local data |

QA должен уточнить:

- требует ли change нового store build;
- может ли web content измениться без обновления app;
- как выполняется forced or phased update;
- сохраняются ли data and sessions после update;
- как service worker or WebView cache получает новую version;
- что происходит при rollback.

## Как выбрать подход

Technology choice зависит от product requirements, а не только от стоимости или скорости разработки.

| Requirement | Usually consider |
| --- | --- |
| Быстрый public access без установки | Mobile web |
| Installable web experience with limited offline support | PWA |
| Максимальный доступ к hardware and platform APIs | Native |
| Shared code with rich mobile UI | Cross-platform |
| Existing web team and WebView-based product | Hybrid |
| Existing website reused inside a store app | Wrapper |

Дополнительные вопросы:

- Насколько критична performance?
- Какие device capabilities нужны?
- Должно ли приложение работать offline?
- Нужны ли App Store and Google Play?
- Как часто выпускаются updates?
- Какой minimum OS поддерживается?
- Есть ли existing web codebase?
- Нужна ли одинаковая feature set на обеих platforms?

Ни один ответ не гарантирует единственный правильный architecture. Один product может комбинировать approaches, например native shell с отдельными WebView screens.

## Классификация по назначению

Technology type описывает способ реализации. Дополнительно приложения классифицируют по business functionality.

| Category | Typical QA focus |
| --- | --- |
| Social and messaging | Notifications, feeds, privacy, media upload, realtime delivery |
| Entertainment and streaming | Playback, DRM, bandwidth, background mode, downloads |
| Utility | Permissions, widgets, background tasks, device integration |
| Gaming | Performance, graphics, state saving, purchases, multiplayer |
| E-commerce | Catalog, cart, payment, delivery, deep links |
| Health and fitness | Sensors, permissions, sensitive data, background tracking |
| Education | Progress sync, downloads, quizzes, media and accessibility |
| Finance | Authentication, security, transactions, audit and masking |
| Travel and navigation | Location, maps, offline data, time zones and roaming |
| Business/productivity | Roles, synchronization, files, collaboration and enterprise policies |

Эта классификация влияет на risk-based testing. Например, для finance app security and transaction integrity важнее animations, а для streaming app критичны playback and network transitions.

## Классификация по аудитории

### B2C

Consumer applications обычно требуют:

- intuitive onboarding;
- broad device coverage;
- accessibility;
- analytics;
- store ratings and reviews;
- localization;
- peak-load readiness.

### B2B

Business applications чаще требуют:

- complex roles;
- enterprise integrations;
- data export;
- security policies;
- managed devices;
- audit logs;
- backward compatibility.

### Internal Apps

Внутренние applications могут распространяться через enterprise tools вместо public stores.

QA focus:

- SSO;
- VPN and corporate network;
- MDM policies;
- device enrollment;
- restricted distribution;
- company-specific workflows;
- remote wipe and access revocation.

## How To Identify The App Type

Ask the team:

- Which frameworks and languages are used?
- Is UI rendered by browser/WebView or native components?
- Is the same codebase used for both platforms?
- Is content bundled in the app or loaded remotely?
- Which native plugins are used?
- Which features differ by platform?
- How are updates delivered?

Do not identify architecture only by appearance. A polished WebView may look native, and a native app can display web content on individual screens.

## Test Strategy By Type

### Mobile Web

- browser matrix;
- responsive layout;
- web storage;
- browser navigation;
- links and downloads;
- network throttling.

### PWA

- all mobile web checks;
- install and uninstall;
- service worker updates;
- offline mode;
- cached data;
- standalone display.

### Native

- OS and device matrix;
- lifecycle;
- hardware;
- permissions;
- store installation;
- upgrade and migration.

### Cross-Platform

- all important flows on both platforms;
- platform differences;
- plugin behavior;
- shared regression;
- performance on weaker devices.

### Hybrid Or Wrapper

- WebView behavior;
- web/native bridge;
- remote and bundled content;
- session and cookies;
- native navigation;
- network loss while loading content.

## Common Defects

- feature exists on Android but is missing on iOS;
- PWA displays outdated cached content;
- WebView shows a blank screen after returning from background;
- native back button closes app instead of navigating web history;
- Flutter screen clips text with large accessibility font;
- React Native plugin works on one OS version only;
- mobile web layout breaks when keyboard opens;
- wrapper app opens internal links in external browser;
- app update removes local user data;
- service worker keeps an old PWA version after deployment;
- remote web release breaks a wrapper without changing its store build;
- permission denial causes endless loading.

## Bug Report Tips

Include:

- app type and framework if known;
- build version;
- OS and device;
- installation source;
- app state: foreground, background or killed;
- network;
- orientation;
- permissions;
- exact screen or URL;
- logs and video;
- whether the issue reproduces on the other platform.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Mobile web app | Web application optimized for mobile browsers. |
| PWA | Web app with installability and enhanced browser capabilities. |
| Native app | Application built for a specific operating system. |
| Cross-platform | Approach that shares code across multiple platforms. |
| Hybrid app | Native container that runs web UI, usually in a WebView. |
| Wrapper app | Hybrid shell around an existing website or web app. |
| WebView | Embedded browser component inside a native application. |
| Bridge | Communication layer between web/framework code and native APIs. |
| Service worker | Browser worker used for cache, offline behavior and background tasks. |
| Feature parity | Equivalent functionality across supported platforms. |
| MDM | Mobile Device Management used to control enterprise devices and apps. |
| Phased rollout | Gradual release of an application update to part of the audience. |
| Forced update | Application blocks or limits use until a required version is installed. |

## Questions

### 1. Чем mobile web app отличается от native app?

Answer: Mobile web app работает в browser и не устанавливается как обычный store app. Native app работает в OS runtime и имеет прямой доступ к platform APIs.

### 2. Является ли React Native классическим hybrid framework?

Answer: Нет. Его обычно относят к cross-platform frameworks, потому что UI использует native components, а не просто web page внутри WebView.

### 3. Что особенно важно тестировать в PWA?

Answer: Manifest, installation, service worker updates, cache, offline behavior and platform capability differences.

### 4. Где чаще всего возникают defects в hybrid app?

Answer: На границе WebView, native shell and plugins.

### 5. Почему cross-platform app всё равно нужно тестировать на обеих platforms?

Answer: OS behavior, native components, permissions, plugins and lifecycle remain platform-specific.

### 6. Почему способ обновления важен для QA?

Answer: Web, PWA and store apps получают changes по-разному, поэтому отличаются risks cache, compatibility, migration and rollback.

### 7. Влияет ли business category на testing strategy?

Answer: Да. Finance, gaming, health, streaming and business apps имеют разные critical workflows and risks.

## What To Review Later

- Android and iOS application lifecycle.
- WebView testing.
- PWA manifest and service workers.
- Mobile permissions.
- Device and OS coverage matrix.
- Installation and update testing.
- Store, enterprise and phased distribution.
- B2C, B2B and internal mobile applications.
