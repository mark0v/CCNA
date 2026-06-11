# Эмуляторы, симуляторы и реальные устройства

Source: user-provided comparisons supplemented with official Android and Apple documentation  
Date added: 2026-06-11  
Related plan item: Mobile Testing  
Tags: QA, mobile testing, emulator, simulator, real devices, Android, iOS  
Language: Russian  
Translation pair: quality-assurance-en/overview/04-mobile-testing/emulators-simulators-real-devices.md

## Summary

Emulator, simulator и physical device — это разные test environments.

- **Simulator** воспроизводит software environment и поведение platform, не пытаясь полностью повторить hardware.
- **Emulator** создаёт virtual device и моделирует больше hardware and OS characteristics.
- **Real device** выполняет application на настоящем processor, sensors, battery, display and radio hardware.

Ни один вариант не является универсально лучшим. Virtual devices дают speed, repeatability and scale, а physical devices показывают реальное пользовательское поведение.

## Key Points

- iOS Simulator запускается через Xcode на macOS.
- Android Emulator использует Android Virtual Devices, или AVD.
- Hardware acceleration может значительно ускорять emulator.
- Emulator умеет моделировать location, rotation, battery and network conditions, но это не эквивалент реального hardware.
- Simulator удобен для UI, navigation and application logic.
- Real devices обязательны для confidence в performance, battery, camera, sensors, calls, Bluetooth and store builds.
- CI обычно использует virtual devices, а меньший набор physical devices применяется для smoke and release testing.

## Notes

## Термины

В индустрии термины иногда используются непоследовательно. Для mobile QA удобно придерживаться такого различия:

| Environment | Meaning |
| --- | --- |
| Simulator | Моделирует platform behavior без полной hardware emulation |
| Emulator | Запускает virtual device и воспроизводит OS вместе с частью hardware configuration |
| Real device | Настоящий phone or tablet |

Не следует выбирать environment только по названию. Важнее знать его capabilities and limitations.

## Что общего у Simulator и Emulator

Оба являются software-defined test environments и помогают:

- запускать tests без отдельного physical device;
- быстро менять OS version and device profile;
- сбрасывать environment в известное состояние;
- создавать repeatable test data and conditions;
- запускать tests параллельно;
- расширять coverage в CI;
- собирать screenshots, logs and diagnostics.

Их главное преимущество — controllability. QA может воспроизвести одну и ту же configuration много раз, что сложнее обеспечить на постоянно используемом physical device.

При этом virtual environment может отличаться от реального устройства не только hardware, но и:

- installed applications;
- user accounts;
- background processes;
- carrier configuration;
- manufacturer services;
- accumulated storage and cache;
- long-term device state.

## iOS Simulator

iOS Simulator входит в Xcode и работает на macOS.

Он удобен для:

- UI layout;
- navigation;
- application logic;
- localization;
- accessibility inspection;
- different screen sizes;
- light/dark appearance;
- location scenarios;
- screenshots;
- быстрых developer and QA checks.

Simulator не является настоящим iPhone or iPad. Он использует resources host Mac и не повторяет полностью:

- processor performance;
- memory pressure;
- battery behavior;
- camera quality;
- cellular radio;
- Bluetooth hardware;
- thermal throttling;
- display characteristics;
- all security and hardware features.

## Android Emulator

Android Emulator запускает virtual Android device на development machine.

Configuration AVD может включать:

- Android version/API level;
- device profile;
- screen size and density;
- memory;
- storage;
- orientation;
- cameras;
- location;
- battery state;
- network conditions.

Он удобен для:

- testing many Android versions;
- UI and functional regression;
- API-level compatibility;
- clean installations;
- snapshots;
- repeatable state;
- automated tests in CI;
- debugging with ADB.

Некоторые hardware capabilities simulated or mapped to host hardware, поэтому результат всё равно нужно подтвердить на physical device.

## Как работает Android Emulator

Способ выполнения зависит от host and system image.

Возможны:

- hardware-assisted virtualization;
- native execution for compatible architecture;
- translation between CPU architectures;
- software rendering or hardware-accelerated graphics.

Поэтому утверждение, что любой emulator всегда использует binary translation и обязательно работает медленно, неверно.

Performance зависит от:

- host CPU;
- virtualization support;
- available RAM;
- graphics acceleration;
- system image architecture;
- number of parallel virtual devices;
- AVD configuration.

## Real Devices

Physical device показывает application в реальном environment:

- actual CPU and memory;
- real battery;
- manufacturer firmware;
- real display;
- camera and microphone;
- sensors;
- Wi-Fi and cellular modem;
- Bluetooth and NFC;
- thermal behavior;
- device storage;
- interruptions.

Real devices особенно важны для Android из-за fragmentation:

- manufacturers;
- screen sizes;
- chipsets;
- custom Android skins;
- background restrictions;
- permission behavior;
- battery optimization.

## Comparison

| Area | Simulator | Emulator | Real device |
| --- | --- | --- | --- |
| Startup and reset | Fast | Usually fast | Slower/manual |
| Repeatability | High | High | Medium |
| OS versions | Multiple virtual runtimes | Many API levels | Limited to available devices |
| UI testing | Strong | Strong | Required for final validation |
| Hardware fidelity | Low | Partial | Full |
| Performance results | Not representative | Limited | Most representative |
| Battery testing | Not reliable | Simulated state | Required |
| Camera/sensors | Limited or simulated | Simulated/mapped | Required |
| Network realism | Controlled simulation | Controlled simulation | Real conditions |
| CI automation | Excellent | Excellent | Possible through device farms |
| Cost | Development hardware | Development hardware | Device purchase or cloud farm |

## What To Test In Simulator

Good candidates:

- screen transitions;
- validation;
- forms;
- orientation;
- text size;
- localization;
- basic accessibility;
- common application logic;
- error messages;
- mocked network responses;
- different iPhone/iPad layouts.

Do not rely only on Simulator for:

- performance;
- memory;
- battery;
- camera;
- Bluetooth/NFC;
- push delivery under real conditions;
- production signing;
- App Store build behavior.

Simulator особенно удобен, если test focus находится на interaction между application screens, mocked services or other software-controlled behavior, а hardware fidelity не влияет на expected result.

## What To Test In Emulator

Good candidates:

- Android API compatibility;
- clean install and app data reset;
- UI regression;
- permissions;
- deep links;
- different screen density;
- location simulation;
- basic network throttling;
- ADB logs;
- automated suites;
- negative system states.

Emulator-specific checks may include:

```bash
adb devices
adb install app.apk
adb shell pm clear com.example.app
adb logcat
```

Do not treat emulator benchmark results as equivalent to physical-device performance.

Emulator подходит для controlled hardware-like configurations, но не гарантирует точное воспроизведение конкретного chipset, driver, firmware or manufacturer customization.

Например, изменение virtual RAM полезно для поиска memory-sensitive defects, но не доказывает, что application одинаково поведёт себя на physical phones с тем же заявленным объёмом памяти.

## Как выбрать среду для конкретного теста

| Test goal | Preferred starting environment | Final confirmation |
| --- | --- | --- |
| UI layout and validation | Simulator or emulator | Priority real screens |
| Business logic | Simulator/emulator with controlled data | Real-device smoke |
| OS/API compatibility | Emulator or simulator runtime | Representative devices |
| Hardware integration | Emulator for early checks | Real device |
| Performance and battery | Virtual device for obvious regressions | Real device required |
| Network error handling | Controlled virtual profile | Real network transitions |
| Store installation and signing | Limited virtual checks | Store-distributed real device |
| Broad automated regression | Virtual devices in CI | Physical device farm subset |

Environment should be chosen per risk, not once for the entire project.

## What Requires Real Devices

Prioritize physical devices for:

- startup and scrolling performance;
- memory pressure;
- battery drain;
- thermal throttling;
- camera quality and focus;
- microphone and audio routing;
- biometric authentication;
- Bluetooth and NFC;
- GPS accuracy;
- calls and SMS interruptions;
- cellular switching and roaming;
- manufacturer-specific Android behavior;
- real push notifications;
- store-distributed builds;
- accessibility with real assistive technologies;
- color, brightness and touch response.

## Network Testing

Virtual tools can simulate:

- bandwidth;
- latency;
- packet loss;
- offline state;
- network type.

Real devices are still needed for:

- Wi-Fi to cellular handover;
- weak radio signal;
- captive portals;
- roaming;
- VPN behavior;
- moving between access points;
- Bluetooth interference;
- modem and carrier-specific issues.

Use both controlled and real conditions:

1. Virtual network profile for repeatable regression.
2. Physical device for realistic transitions.

## Interrupt Testing

Test interruptions such as:

- incoming call;
- SMS;
- push notification;
- alarm;
- low-battery alert;
- permission dialog;
- another application opening;
- screen lock;
- background and foreground transition.

Some states can be triggered virtually, but final behavior should be confirmed on a real device.

Verify:

- entered data remains;
- media resumes correctly;
- no duplicate operation;
- session remains valid;
- sensitive content is hidden when required;
- application returns to the correct screen.

## Performance And Battery

Simulator and emulator are useful for finding obvious regressions, but host machine resources distort measurements.

Use real devices for:

- launch time;
- frame drops;
- CPU and memory;
- battery consumption;
- network usage;
- heating;
- background activity;
- long-running tests.

Compare results only under documented conditions:

- same build;
- same device;
- same OS;
- same network;
- same battery state;
- same scenario.

## CI And Device Farms

Virtual devices are well suited for CI because they are:

- reproducible;
- resettable;
- parallelizable;
- scriptable;
- cheaper at scale.

A practical pipeline:

1. Unit and API tests.
2. UI smoke on simulator/emulator.
3. Regression across selected virtual OS versions.
4. Smoke on physical device farm.
5. Release candidate testing on priority real devices.

Real-device testing should not always wait until the final day before release. Hardware-critical and high-risk flows should run on representative devices earlier so that platform-specific defects are not discovered too late.

A balanced strategy:

- virtual devices on every change or pull request;
- physical-device smoke on regular builds;
- broader device-farm regression before release;
- exploratory testing on locally held devices for real-world behavior.

Cloud device farms provide access to real devices, but QA should still understand:

- session limits;
- network location;
- device cleanliness;
- logs and video;
- shared-device privacy;
- differences from a locally held device.

## Device Matrix

Choose devices by product data and risk.

Consider:

- supported OS versions;
- active-user distribution;
- manufacturers;
- screen size and density;
- low-end and high-end hardware;
- tablet support;
- chipset;
- special hardware features;
- market and region.

Minimum useful matrix often includes:

- one older supported device;
- one common mid-range device;
- one current flagship;
- relevant tablet;
- priority iPhone sizes;
- oldest and newest supported OS.

This is a starting point, not a universal rule.

## Common Defects

- layout passes in Simulator but clips on real device;
- emulator test passes but manufacturer firmware kills background task;
- real camera returns different orientation or metadata;
- application overheats during long media use;
- UI animation is smooth virtually but drops frames on low-end phone;
- Bluetooth permission flow differs by OS version;
- virtual network profile does not reproduce cellular handover failure;
- notification works on emulator but fails with production signing;
- simulator does not reveal safe-area or keyboard behavior seen on device;
- test suite depends on state left in an AVD snapshot.
- issue reproduces only in an unrealistically clean virtual environment and misses migration from long-used devices;
- physical-device defect is discovered late because all earlier coverage was virtual.

## Bug Report Tips

Always identify the environment:

- simulator, emulator or real device;
- tool and version;
- virtual device profile;
- system image/API level;
- host OS;
- physical device model;
- OS and manufacturer build;
- app build and installation source;
- network;
- relevant simulated controls.

Do not report “Android device” when the issue occurred only on one AVD.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Simulator | Software model of a platform environment |
| Emulator | Virtual device that reproduces OS and part of hardware behavior |
| AVD | Android Virtual Device configuration |
| System image | Android OS image used by an emulator |
| Hardware acceleration | Use of host virtualization/GPU to improve virtual-device performance |
| Device farm | Remote collection of virtual or physical test devices |
| Fragmentation | Variation across OS versions, hardware and manufacturers |
| Snapshot | Saved state of a virtual device |
| Thermal throttling | Hardware performance reduction caused by heat |

## Questions

### 1. Может ли emulator полностью заменить real device?

Answer: Нет. Он полезен для repeatable functional testing, но не воспроизводит полностью hardware, performance, battery and network behavior.

### 2. Для чего особенно полезен iOS Simulator?

Answer: Для быстрых UI, layout, navigation and logic checks на разных simulated Apple devices.

### 3. Почему Android Emulator подходит для CI?

Answer: Его можно автоматически создавать, сбрасывать, конфигурировать и запускать параллельно.

### 4. Где нужно измерять performance?

Answer: Финальные performance conclusions следует делать на representative physical devices.

### 5. Как выбрать реальные устройства?

Answer: По supported OS, analytics, manufacturers, hardware tiers, screen sizes and product risks.

### 6. В чём общее преимущество emulator and simulator?

Answer: Они дают controlled, repeatable and scalable environments, которые удобно сбрасывать и запускать в automation.

### 7. Нужно ли откладывать real-device testing до конца release cycle?

Answer: Нет. Critical hardware and platform scenarios следует проверять на physical devices регулярно, а не только перед release.

## What To Review Later

- Android Virtual Device configuration.
- Xcode Simulator controls.
- Real-device logging.
- Mobile performance profiling.
- Device farms.
- Mobile device coverage matrix.

## Sources

- [Android Emulator documentation](https://developer.android.com/studio/run/emulator)
- [Configure Android Virtual Devices](https://developer.android.com/studio/run/managing-avds)
- [Apple Simulator documentation](https://developer.apple.com/documentation/xcode/running-your-app-in-simulator-or-on-a-device)
