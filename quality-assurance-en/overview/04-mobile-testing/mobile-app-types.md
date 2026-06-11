# Mobile App Types For QA

Source: pasted articles comparing mobile application types and technologies  
Date added: 2026-06-11  
Related plan item: Mobile Testing  
Tags: QA, mobile testing, native, hybrid, cross-platform, PWA, mobile web  
Language: English  
Translation pair: quality-assurance/overview/04-mobile-testing/mobile-app-types.md

## Summary

A mobile product can be implemented as a mobile web app, Progressive Web App, native app, cross-platform app, or hybrid app. These approaches differ in runtime, technology stack, device access, distribution, and typical risks.

For QA, the application type determines:

- where and how a build is installed;
- which platforms and browsers require coverage;
- whether App Store and Google Play checks are needed;
- how permissions, hardware, and background behavior are tested;
- whether defects belong to the web layer, native layer, or integration bridge.

Main idea:

> The technology label matters less than understanding the actual architecture and boundaries between application layers.

## Key Points

- A mobile web app runs in a browser and is not installed as a regular application.
- A PWA is a web app with a manifest, service worker, and additional platform capabilities.
- A native app is developed specifically for one platform.
- Cross-platform frameworks share code between iOS and Android while using a native runtime or compiled output.
- A hybrid app runs web content inside a native container, usually through a WebView.
- React Native and Flutter are better classified as cross-platform rather than classic WebView hybrid apps.
- One product may provide web, PWA, and mobile app versions at the same time.

## Notes

## Mobile Web App

A mobile web app is opened through a URL in a mobile browser.

It commonly uses:

- HTML;
- CSS;
- JavaScript;
- responsive design;
- web frameworks.

Advantages:

- no installation;
- server-side updates;
- one version across devices;
- easy link-based distribution.

Limitations:

- browser dependency;
- limited or inconsistent device API access;
- browser UI affects the experience;
- offline support is usually limited;
- no regular store distribution.

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

A PWA is a web application that uses modern browser capabilities to provide an app-like experience.

Core elements:

- Web App Manifest;
- service worker;
- HTTPS;
- responsive UI;
- cache and offline strategy;
- installability where supported.

Capabilities vary by OS and browser. QA should not assume identical PWA behavior on Android and iOS.

QA checks:

- install prompt or Add to Home Screen;
- app icon and launch behavior;
- manifest fields;
- offline and cached content;
- service worker updates;
- stale cache;
- push notifications where supported;
- fallback when a capability is unavailable.

## Native App

A native app is built for a specific operating system.

Typical stacks:

- iOS: Swift or Objective-C;
- Android: Kotlin or Java.

Advantages:

- full platform API access;
- native UI and behavior;
- high performance;
- deep device hardware integration;
- strong offline support.

Risks:

- separate implementations may behave differently;
- iOS and Android release cycles may diverge;
- platform-specific defects;
- more OS and device combinations.

QA focus:

- platform guidelines;
- permissions;
- lifecycle and background states;
- gestures;
- notifications;
- biometrics;
- camera, GPS, and sensors;
- installation, update, and uninstall;
- store builds and signing.

## Cross-Platform App

Cross-platform frameworks allow a significant part of the codebase to be shared between iOS and Android.

Examples:

- React Native;
- Flutter;
- Kotlin Multiplatform;
- .NET MAUI.

Frameworks use different models:

- Flutter renders UI through its own engine;
- React Native connects application logic to native components;
- Kotlin Multiplatform can share business logic while keeping platform-specific UI.

Cross-platform does not mean identical behavior.

QA focus:

- feature parity;
- platform-specific navigation;
- native components;
- bridge/plugin failures;
- performance;
- animations;
- platform permissions;
- shared versus platform-only defects;
- framework and plugin updates.

## Hybrid App

A hybrid app combines a native container with web technologies. Web content is usually displayed inside a `WebView`.

Common technologies:

- Ionic;
- Apache Cordova;
- Capacitor.

Native plugins allow web code to access:

- camera;
- geolocation;
- files;
- notifications;
- device information.

QA should test both layers:

1. Web content and API behavior.
2. Native shell, plugins, and lifecycle.

Typical risks:

- blank WebView;
- broken back navigation;
- web and native session mismatch;
- external links open incorrectly;
- permission is granted in the OS but unavailable to the plugin;
- keyboard overlaps a web form;
- content ignores safe areas;
- old cached web bundle remains after an update.

## Wrapper App

A wrapper app is a specific hybrid architecture where an existing website or web app is loaded inside a native shell.

A wrapper may add:

- push notifications;
- native navigation;
- deep links;
- authentication integration;
- analytics;
- store distribution.

QA focus:

- remote content availability;
- behavior when the website is unavailable;
- domain allowlist;
- external browser transitions;
- cookies and session;
- native-to-web communication;
- app review compliance;
- difference between website releases and store builds.

## Comparison

| Type | Runs in | Installed | Main UI | Device access | Main QA risk |
| --- | --- | --- | --- | --- | --- |
| Mobile web | Browser | No | Web | Limited/browser-dependent | Browser and responsive compatibility |
| PWA | Browser/standalone web mode | Optional | Web | Expanded but platform-dependent | Cache, installability, and capability gaps |
| Native | OS runtime | Yes | Native | Full | Platform and device fragmentation |
| Cross-platform | Native/compiled framework runtime | Yes | Framework/native | Broad through framework/plugins | Shared code with platform-specific differences |
| Hybrid | Native shell + WebView | Yes | Web inside native container | Through plugins | Web/native integration |
| Wrapper | Native shell + existing web content | Yes | Mostly existing web UI | Through added native layer | Remote content and shell integration |

## Distribution, Updates, And Storage

The application type affects not only development but also the delivery process.

| Type | Distribution | Updates | Device storage |
| --- | --- | --- | --- |
| Mobile web | URL/browser | Immediately on server deployment | Browser cache and site data |
| PWA | Browser/home-screen installation | Web deployment plus service worker update cycle | Cache, storage, and offline assets |
| Native | App Store, Google Play, or enterprise distribution | New build, review, and user/device rollout | Installed application and local data |
| Cross-platform | Same as native | New platform builds, sometimes a shared release | Installed application and local data |
| Hybrid/wrapper | Stores or enterprise distribution | Native shell update and/or remote web update | Native package, WebView cache, and local data |

QA should determine:

- whether a change requires a new store build;
- whether web content can change without an app update;
- how forced or phased updates work;
- whether data and sessions survive an update;
- how a service worker or WebView cache receives a new version;
- what happens during rollback.

## How To Choose An Approach

Technology choice depends on product requirements, not only cost or development speed.

| Requirement | Usually consider |
| --- | --- |
| Fast public access without installation | Mobile web |
| Installable web experience with limited offline support | PWA |
| Maximum hardware and platform API access | Native |
| Shared code with rich mobile UI | Cross-platform |
| Existing web team and WebView-based product | Hybrid |
| Existing website reused inside a store app | Wrapper |

Additional questions:

- How critical is performance?
- Which device capabilities are required?
- Must the application work offline?
- Are App Store and Google Play distribution required?
- How frequently are updates released?
- Which minimum OS versions are supported?
- Is there an existing web codebase?
- Is identical feature coverage required on both platforms?

No answer guarantees one correct architecture. A product can combine approaches, such as a native shell with individual WebView screens.

## Classification By Function

Technology type describes implementation. Applications can also be classified by business functionality.

| Category | Typical QA focus |
| --- | --- |
| Social and messaging | Notifications, feeds, privacy, media upload, realtime delivery |
| Entertainment and streaming | Playback, DRM, bandwidth, background mode, downloads |
| Utility | Permissions, widgets, background tasks, device integration |
| Gaming | Performance, graphics, state saving, purchases, multiplayer |
| E-commerce | Catalog, cart, payment, delivery, deep links |
| Health and fitness | Sensors, permissions, sensitive data, background tracking |
| Education | Progress sync, downloads, quizzes, media, and accessibility |
| Finance | Authentication, security, transactions, audit, and masking |
| Travel and navigation | Location, maps, offline data, time zones, and roaming |
| Business/productivity | Roles, synchronization, files, collaboration, and enterprise policies |

This classification affects risk-based testing. For example, security and transaction integrity matter more than animation quality in a finance app, while playback and network transitions are critical in a streaming app.

## Classification By Audience

### B2C

Consumer applications commonly require:

- intuitive onboarding;
- broad device coverage;
- accessibility;
- analytics;
- store ratings and reviews;
- localization;
- peak-load readiness.

### B2B

Business applications commonly require:

- complex roles;
- enterprise integrations;
- data export;
- security policies;
- managed devices;
- audit logs;
- backward compatibility.

### Internal Apps

Internal applications may be distributed through enterprise tools instead of public stores.

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
- Is UI rendered by a browser/WebView or native components?
- Is the same codebase used for both platforms?
- Is content bundled in the app or loaded remotely?
- Which native plugins are used?
- Which features differ by platform?
- How are updates delivered?

Do not identify architecture only by appearance. A polished WebView may look native, while a native app can display web content on individual screens.

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
- installation and removal;
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
- native back button closes the app instead of navigating web history;
- Flutter screen clips text with a large accessibility font;
- React Native plugin works on only one OS version;
- mobile web layout breaks when the keyboard opens;
- wrapper app opens internal links in an external browser;
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
- app state: foreground, background, or killed;
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
| Service worker | Browser worker used for cache, offline behavior, and background tasks. |
| Feature parity | Equivalent functionality across supported platforms. |
| MDM | Mobile Device Management used to control enterprise devices and apps. |
| Phased rollout | Gradual release of an application update to part of the audience. |
| Forced update | Application blocks or limits use until a required version is installed. |

## Questions

### 1. How does a mobile web app differ from a native app?

Answer: A mobile web app runs in a browser and is not installed as a regular store application. A native app runs in the OS runtime and directly accesses platform APIs.

### 2. Is React Native a classic hybrid framework?

Answer: No. It is commonly classified as cross-platform because its UI uses native components rather than only a web page inside a WebView.

### 3. What is especially important when testing a PWA?

Answer: Manifest, installation, service worker updates, cache, offline behavior, and platform capability differences.

### 4. Where do defects commonly occur in a hybrid app?

Answer: At the boundary between the WebView, native shell, and plugins.

### 5. Why must a cross-platform app still be tested on both platforms?

Answer: OS behavior, native components, permissions, plugins, and lifecycle remain platform-specific.

### 6. Why does the update mechanism matter to QA?

Answer: Web, PWA, and store applications receive changes differently, creating different cache, compatibility, migration, and rollback risks.

### 7. Does the business category affect the testing strategy?

Answer: Yes. Finance, gaming, health, streaming, and business applications have different critical workflows and risks.

## What To Review Later

- Android and iOS application lifecycle.
- WebView testing.
- PWA manifest and service workers.
- Mobile permissions.
- Device and OS coverage matrix.
- Installation and update testing.
- Store, enterprise, and phased distribution.
- B2C, B2B, and internal mobile applications.
