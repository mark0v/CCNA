# Emulators, Simulators, And Real Devices

Source: user-provided comparisons supplemented with official Android and Apple documentation  
Date added: 2026-06-11  
Related plan item: Mobile Testing  
Tags: QA, mobile testing, emulator, simulator, real devices, Android, iOS  
Language: English  
Translation pair: quality-assurance/overview/04-mobile-testing/emulators-simulators-real-devices.md

## Summary

An emulator, simulator, and physical device are different test environments.

- A **simulator** reproduces software environment and platform behavior without attempting complete hardware emulation.
- An **emulator** creates a virtual device and models more hardware and operating-system characteristics.
- A **real device** runs the application on actual processor, sensors, battery, display, and radio hardware.

No option is universally best. Virtual devices provide speed, repeatability, and scale, while physical devices reveal actual user behavior.

## Key Points

- iOS Simulator runs through Xcode on macOS.
- Android Emulator uses Android Virtual Devices, or AVDs.
- Hardware acceleration can significantly improve emulator speed.
- An emulator can simulate location, rotation, battery, and network conditions, but this is not equal to real hardware.
- A simulator is useful for UI, navigation, and application logic.
- Real devices are required for confidence in performance, battery, camera, sensors, calls, Bluetooth, and store builds.
- CI commonly uses virtual devices, with a smaller physical-device set for smoke and release testing.

## Notes

## Terms

The industry sometimes uses these terms inconsistently. For mobile QA, this distinction is useful:

| Environment | Meaning |
| --- | --- |
| Simulator | Models platform behavior without complete hardware emulation |
| Emulator | Runs a virtual device and reproduces the OS with part of its hardware configuration |
| Real device | Actual phone or tablet |

Do not choose an environment only by its name. Understand its capabilities and limitations.

## What Simulator And Emulator Have In Common

Both are software-defined test environments that help teams:

- run tests without a dedicated physical device;
- quickly change OS versions and device profiles;
- reset an environment to a known state;
- create repeatable test data and conditions;
- run tests in parallel;
- expand CI coverage;
- collect screenshots, logs, and diagnostics.

Their main advantage is controllability. QA can reproduce the same configuration many times, which is harder on a physical device that is used continuously.

A virtual environment may differ from a real device not only in hardware, but also in:

- installed applications;
- user accounts;
- background processes;
- carrier configuration;
- manufacturer services;
- accumulated storage and cache;
- long-term device state.

## iOS Simulator

iOS Simulator is included with Xcode and runs on macOS.

It is useful for:

- UI layout;
- navigation;
- application logic;
- localization;
- accessibility inspection;
- different screen sizes;
- light/dark appearance;
- location scenarios;
- screenshots;
- fast developer and QA checks.

Simulator is not a real iPhone or iPad. It uses host Mac resources and does not completely reproduce:

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

Android Emulator runs a virtual Android device on a development machine.

An AVD configuration can include:

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

It is useful for:

- testing many Android versions;
- UI and functional regression;
- API-level compatibility;
- clean installations;
- snapshots;
- repeatable state;
- automated tests in CI;
- debugging with ADB.

Some hardware capabilities are simulated or mapped to host hardware, so results still require physical-device confirmation.

## How Android Emulator Works

Execution depends on the host and system image.

Possible techniques include:

- hardware-assisted virtualization;
- native execution for a compatible architecture;
- translation between CPU architectures;
- software rendering or hardware-accelerated graphics.

Therefore, it is incorrect to say that every emulator always uses binary translation and must be slow.

Performance depends on:

- host CPU;
- virtualization support;
- available RAM;
- graphics acceleration;
- system image architecture;
- number of parallel virtual devices;
- AVD configuration.

## Real Devices

A physical device exposes the application to:

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

Real devices are especially important for Android fragmentation:

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

Simulator is especially useful when the test focus is interaction between application screens, mocked services, or other software-controlled behavior where hardware fidelity does not affect the expected result.

## What To Test In Emulator

Good candidates:

- Android API compatibility;
- clean install and application data reset;
- UI regression;
- permissions;
- deep links;
- different screen density;
- location simulation;
- basic network throttling;
- ADB logs;
- automated suites;
- negative system states.

Useful commands:

```bash
adb devices
adb install app.apk
adb shell pm clear com.example.app
adb logcat
```

Do not treat emulator benchmark results as equivalent to physical-device performance.

An emulator is useful for controlled hardware-like configurations, but it does not guarantee exact reproduction of a specific chipset, driver, firmware, or manufacturer customization.

For example, changing virtual RAM can help identify memory-sensitive defects, but it does not prove identical behavior on physical phones with the same advertised memory.

## Choosing An Environment For A Test

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

Choose the environment per risk rather than once for the entire project.

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
- color, brightness, and touch response.

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
4. Smoke on a physical device farm.
5. Release candidate testing on priority real devices.

Real-device testing should not always wait until the final day before release. Hardware-critical and high-risk flows should run on representative devices earlier so platform-specific defects are not discovered too late.

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

Choose devices based on product data and risk.

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

A minimum useful matrix often includes:

- one older supported device;
- one common mid-range device;
- one current flagship;
- relevant tablet;
- priority iPhone sizes;
- oldest and newest supported OS.

This is a starting point, not a universal rule.

## Common Defects

- layout passes in Simulator but clips on a real device;
- emulator test passes but manufacturer firmware kills a background task;
- real camera returns different orientation or metadata;
- application overheats during long media use;
- UI animation is smooth virtually but drops frames on a low-end phone;
- Bluetooth permission flow differs by OS version;
- virtual network profile does not reproduce cellular handover failure;
- notification works on emulator but fails with production signing;
- simulator does not reveal safe-area or keyboard behavior seen on device;
- test suite depends on state left in an AVD snapshot.
- issue reproduces only in an unrealistically clean virtual environment and misses migration from long-used devices;
- physical-device defect is discovered late because all earlier coverage was virtual.

## Bug Report Tips

Always identify the environment:

- simulator, emulator, or real device;
- tool and version;
- virtual device profile;
- system image/API level;
- host OS;
- physical device model;
- OS and manufacturer build;
- application build and installation source;
- network;
- relevant simulated controls.

Do not report "Android device" when the issue occurred only on one AVD.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Simulator | Software model of a platform environment |
| Emulator | Virtual device that reproduces OS and part of hardware behavior |
| AVD | Android Virtual Device configuration |
| System image | Android OS image used by an emulator |
| Hardware acceleration | Use of host virtualization/GPU to improve virtual-device performance |
| Device farm | Remote collection of virtual or physical test devices |
| Fragmentation | Variation across OS versions, hardware, and manufacturers |
| Snapshot | Saved state of a virtual device |
| Thermal throttling | Hardware performance reduction caused by heat |

## Questions

### 1. Can an emulator completely replace a real device?

Answer: No. It is useful for repeatable functional testing, but it does not fully reproduce hardware, performance, battery, and network behavior.

### 2. What is iOS Simulator especially useful for?

Answer: Fast UI, layout, navigation, and logic checks across simulated Apple devices.

### 3. Why is Android Emulator suitable for CI?

Answer: It can be created, reset, configured, and run in parallel through automation.

### 4. Where should performance be measured?

Answer: Final performance conclusions should be based on representative physical devices.

### 5. How should real devices be selected?

Answer: Based on supported OS versions, analytics, manufacturers, hardware tiers, screen sizes, and product risks.

### 6. What common advantage do emulators and simulators provide?

Answer: They provide controlled, repeatable, and scalable environments that are easy to reset and automate.

### 7. Should real-device testing wait until the end of the release cycle?

Answer: No. Critical hardware and platform scenarios should run regularly on physical devices, not only before release.

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
