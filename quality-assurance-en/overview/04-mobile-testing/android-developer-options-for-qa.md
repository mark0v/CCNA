# Android Developer Options For QA

Source: user-provided material based on Android Developers documentation  
Date added: 2026-06-11  
Related plan item: Mobile Testing  
Tags: QA, mobile testing, Android, Developer options, USB debugging, ADB  
Language: English  
Translation pair: quality-assurance/overview/04-mobile-testing/android-developer-options-for-qa.md

## Summary

`Developer options` is a hidden Android settings section for debugging, diagnostics, and controlled testing conditions.

QA engineers can use it to:

- connect a physical device through `adb`;
- collect logs and bug reports;
- display touches in a screen recording;
- inspect layout bounds and RTL behavior;
- select a mock location application;
- investigate rendering, memory, and background lifecycle issues;
- reproduce selected Bluetooth, USB, and network scenarios.

These settings change device behavior. Record every non-default value before testing and restore the default state after the experiment.

## Key Points

- On Android 4.2 and higher, the section is normally enabled by tapping `Build number` seven times.
- Names and locations vary by Android version and device manufacturer.
- `USB debugging` lets Android Debug Bridge communicate with and control the device.
- The user must approve the workstation RSA key on the first USB connection.
- Pairing-based wireless debugging is supported on phones running Android 11 and higher.
- `Show taps` and `Pointer location` can improve defect evidence.
- `Don't keep activities` and `Background process limit` are stress tools, not normal device conditions.
- Developer options should not remain enabled permanently on personal or production devices.

## Notes

## Enabling Developer Options

1. Open `Settings`.
2. Find `Build number`.
3. Tap it seven times.
4. Confirm the device PIN, pattern, or password if requested.
5. Go back and open `Developer options`.

Common paths:

| Device | Path |
| --- | --- |
| Google Pixel | `Settings > About phone > Build number` |
| Samsung Galaxy | `Settings > About phone > Software information > Build number` |
| Many other devices | `Settings > System > About phone > Build number` |

Manufacturers can rename or move the section. Use Settings search when the documented path does not match the device.

## Connecting A Device To ADB

### USB Debugging

1. Enable `Developer options`.
2. Turn on `USB debugging`.
3. Connect the device with a data-capable USB cable.
4. Unlock the screen.
5. Approve the workstation RSA fingerprint.
6. Verify the connection:

```bash
adb devices
```

Expected states:

| State | Meaning |
| --- | --- |
| `device` | Connected and authorized |
| `unauthorized` | The RSA confirmation has not been approved |
| `offline` | A connection exists, but the device is not responding |
| Device missing | Check the cable, USB mode, driver, and ADB server |

If the device is missing, verify that:

- the cable supports data transfer;
- a suitable `Default USB configuration` is selected;
- the OEM USB driver is installed on Windows;
- the screen is unlocked;
- the RSA prompt was not rejected.

Use `Revoke USB debugging authorizations` to remove trusted workstations and authorize the connection again.

### Wireless Debugging

Phones running Android 11 and higher can pair with `adb` over Wi-Fi using a QR code or pairing code.

The device and workstation must be on the same network. Corporate Wi-Fi can block peer-to-peer traffic or mDNS discovery.

After pairing, verify the connection:

```bash
adb devices
```

Wireless debugging is useful when:

- the USB port is needed for another accessory;
- charging or accessory behavior must be tested;
- a poor cable causes unstable connections;
- several devices connect to one workstation.

It does not simulate a mobile network because commands still travel through the Wi-Fi infrastructure.

## Useful Options For QA

### Evidence And UI

| Option | QA use |
| --- | --- |
| `Show taps` | Displays touch points in a screen recording |
| `Pointer location` | Displays gesture coordinates and paths |
| `Show layout bounds` | Shows view bounds, margins, and clipping |
| `Force RTL layout direction` | Provides a quick right-to-left UI check |
| `Simulate secondary displays` | Exercises additional-display scenarios |
| `System UI demo mode` | Produces clean screenshots without random notifications |

`Pointer location` adds a large diagnostics overlay and can cover the UI. `Show taps` is usually sufficient for a normal defect video.

### Debugging And Test Data

| Option | QA use |
| --- | --- |
| `Take bug report` | Collects system logs and diagnostic information |
| `Select debug app` | Selects a debuggable application |
| `Wait for debugger` | Pauses the selected app until a debugger attaches |
| `Select mock location app` | Replaces the reported GPS location |
| `Bluetooth HCI snoop log` | Records Bluetooth traffic for analysis |
| `Stay awake` | Keeps the screen on while the device is plugged in |

Mock location is useful for geofencing, maps, delivery, and regional scenarios. Also test denied location permission, disabled location services, and a real route.

### Rendering And Accessibility

| Option | QA use |
| --- | --- |
| `Profile GPU rendering` | Helps identify slow frames and UI jank |
| `Debug GPU overdraw` | Visualizes pixels drawn multiple times |
| `Show GPU view updates` | Highlights GPU-rendered regions as they update |
| `Simulate color space` | Provides a quick visual color-perception check |
| Animation scales | Exercises transitions at different speeds |

Do not measure production performance with forced rendering, GPU overlays, or non-default animation scales enabled. Reproduce the issue on the default configuration first.

### Lifecycle And Background Behavior

| Option | QA use | Risk |
| --- | --- | --- |
| `Don't keep activities` | Quickly exposes state restoration defects | Artificially destroys every Activity after the user leaves it |
| `Background process limit` | Exercises behavior under process pressure | Changes normal Android process management |
| Memory information | Shows overall and per-app memory usage | Does not replace profiling or long-running tests |

`Don't keep activities` is not an exact simulation of a low-memory process kill. Use it as a stress tool, then reproduce the defect in a realistic lifecycle scenario.

## Basic ADB Commands For Testers

```bash
# List connected devices
adb devices

# Stream device logs
adb logcat

# Stop an application
adb shell am force-stop com.example.app

# Clear application data
adb shell pm clear com.example.app

# Generate a complete bug report
adb bugreport

# Record the screen
adb shell screenrecord /sdcard/test.mp4

# Copy the recording to the workstation
adb pull /sdcard/test.mp4
```

`pm clear` removes local application data. It is similar to a clean app-data state, but the installed version, permissions, external files, and server-side account state can still differ from a fresh installation.

## QA Scenarios

### UI And Gestures

- Record a defect with `Show taps` enabled.
- Test swipe, long press, multi-touch, and edge gestures.
- Enable `Show layout bounds` to find clipping and incorrect touch targets.
- Enable `Force RTL` and inspect navigation, icons, alignment, and mixed-direction text.
- Restore the settings and repeat the critical flow in the default state.

### Lifecycle

- Open a form containing unsent data.
- Move the app to the background.
- Create memory pressure or temporarily enable `Don't keep activities`.
- Return to the app.
- Verify the screen, navigation stack, draft, and scroll position.

### Location

- Select an approved mock location application.
- Test different countries, time zones, and coordinates.
- Test a sudden location jump and missing signal.
- Repeat the critical scenario with real GPS.

### Connectivity And Accessories

- Test supported USB modes such as charging and MTP.
- Capture Bluetooth HCI logs only when needed and handle them securely.
- Test Wi-Fi handover under real network conditions.
- Do not treat developer network toggles as a complete replacement for a poor real network.

## What To Include In A Bug Report

In addition to steps and expected/actual results, provide:

- device model;
- Android version and build number;
- application build;
- USB or Wi-Fi connection type;
- enabled Developer options;
- animation scale;
- background process limit;
- whether mock location was used;
- root, custom firmware, or work profile status;
- timestamps for matching the event with `logcat`;
- bug report, logs, screenshot, or screen recording.

Without this context, a non-default setting can create a defect that the team cannot reproduce.

## Security And Cleanup

- Approve an RSA fingerprint only on a trusted workstation.
- Disable USB and wireless debugging when they are not needed.
- Remove old paired workstations.
- Review a bug report before sharing it because it can contain accounts, identifiers, network details, and user data.
- Disable mock location, visual overlays, and lifecycle stress options after testing.
- When unsure, turn off the main Developer options switch or restore each changed value manually.

## Interview Focus

1. How do you enable Developer options on Android?
2. How does `USB debugging` differ from normal USB file transfer?
3. What does `unauthorized` mean in `adb devices`?
4. How can QA use `Show taps`, `Show layout bounds`, and `Force RTL`?
5. Why is `Don't keep activities` not a normal user environment?
6. What information belongs in an Android bug report?
7. What risks come with leaving ADB enabled?

## Sources

- [Configure on-device developer options](https://developer.android.com/studio/debug/dev-options)
- [Android Debug Bridge](https://developer.android.com/tools/adb)

