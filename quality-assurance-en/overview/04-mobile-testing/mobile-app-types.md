# Mobile App Types For QA

Source: pasted article comparing web, native, cross-platform, hybrid, and wrapper apps  
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

## What To Review Later

- Android and iOS application lifecycle.
- WebView testing.
- PWA manifest and service workers.
- Mobile permissions.
- Device and OS coverage matrix.
- Installation and update testing.
