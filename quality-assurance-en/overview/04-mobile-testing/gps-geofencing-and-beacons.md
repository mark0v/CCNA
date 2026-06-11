# GPS, Geofencing, And Beacons For Mobile QA

Source: user-provided article, corrected and expanded with official Android and Apple documentation  
Date added: 2026-06-11  
Related plan item: Mobile Testing  
Tags: QA, mobile testing, GPS, GNSS, geofencing, BLE, beacons, location  
Language: English  
Translation pair: quality-assurance/overview/04-mobile-testing/gps-geofencing-and-beacons.md

## Summary

Location-aware mobile products use several distinct technologies:

- **GPS/GNSS** helps calculate device coordinates from satellite signals;
- **platform location services** combine GNSS, Wi-Fi, cellular, and sensor data;
- **geofencing** defines a virtual region and generates enter, exit, or dwell events;
- a **BLE beacon** broadcasts a short radio identifier that a nearby device uses to estimate proximity;
- **RFID** identifies tags through a compatible reader and is commonly used for assets and inventory.

QA engineers should not treat these terms as interchangeable. A geofence is a logical rule, while GPS, Wi-Fi, BLE, or RFID can provide proximity or location data.

## Key Points

- Mobile location normally combines several signals rather than GPS alone.
- Indoor environments, tunnels, urban canyons, and radio interference reduce accuracy.
- A geofence is normally defined by center coordinates and a radius.
- Primary transitions are `ENTER`, `EXIT`, and `DWELL`.
- A geofence event can be delayed, particularly while the app is in the background.
- Android geofencing requires precise location and normally background location permission for background monitoring.
- A beacon normally broadcasts a BLE advertisement; the mobile device scans and interprets it.
- RSSI provides approximate proximity, not an exact distance.
- Emulators and mock location improve repeatability, but final validation needs a real route and physical beacons.
- Location data is sensitive personal data.

## Notes

## GPS, GNSS, And Location Services

GPS is the United States Global Positioning System. **GNSS** is the broader term covering GPS and other satellite navigation systems.

A phone can calculate location from:

- GNSS satellites;
- nearby Wi-Fi access points;
- cellular towers;
- Bluetooth signals;
- accelerometer, gyroscope, and compass;
- previously known location;
- platform fused-location algorithms.

The statement "GPS fails because it is cloudy" is too simplistic. Stronger factors include:

- missing clear sky view;
- buildings and reflected radio signals;
- tunnels and underground parking;
- indoor environments;
- device antenna;
- power-saving mode;
- disabled precise location;
- stale cached location;
- manufacturer background restrictions.

A location object usually contains latitude, longitude, accuracy, and timestamp, and can also contain altitude, speed, and bearing.

## What Is Geofencing?

A geofence is a virtual geographic region.

A circular geofence is defined by:

```text
latitude + longitude + radius
```

The system can report:

| Event | Meaning |
| --- | --- |
| Enter | Device moves inside the region |
| Exit | Device leaves the region |
| Dwell | Device remains inside for a configured duration |
| Initial trigger | App is already inside or outside during registration |
| Expiration | Region monitoring ends after a configured time |

Examples:

- notify a store that a customer is approaching;
- remind a user about pickup;
- activate home automation;
- record employee arrival;
- display location-based content;
- detect an asset leaving an allowed area.

A transition does not necessarily happen exactly on the drawn boundary or in the same second.

## Region Size And Accuracy

A radius that is too small causes:

- missed transitions;
- frequent enter/exit events near the boundary;
- dependence on random location error;
- increased battery use.

Android documentation suggests considering a minimum radius around 100 meters as a practical starting point under typical Wi-Fi location conditions.

QA should know:

- configured radius;
- current reported accuracy;
- expected transition delay;
- dwell duration;
- expiration;
- maximum number of active regions;
- fallback behavior when accuracy is insufficient.

If reported accuracy is 150 m, a 20 m geofence boundary cannot be verified confidently.

## Permissions

### Android

Test:

- approximate location;
- precise location;
- allow while using the app;
- allow only this time;
- deny;
- background location;
- permission downgrade in Settings;
- disabled location services;
- battery optimization and manufacturer restrictions.

Android geofencing requires `ACCESS_FINE_LOCATION`. Background geofence monitoring on Android 10+ normally also requires `ACCESS_BACKGROUND_LOCATION`.

The permission request should explain value in feature context instead of demanding maximum access on first launch.

### iOS

Test:

- Allow Once;
- Allow While Using App;
- Allow Always when background monitoring is truly required;
- Don't Allow;
- Precise Location on/off;
- permission changes in Settings;
- Background App Refresh;
- globally disabled location services.

Permission prompt behavior depends on current authorization state and OS version. Cover clean installation and upgrade separately.

## Geofence Test Matrix

### Registration

- valid coordinates and radius;
- invalid coordinates;
- zero, negative, or very large radius;
- duplicate region ID;
- maximum region count;
- expiration;
- application update;
- device reboot;
- logout and another user login.

### Transitions

- outside to inside;
- inside to outside;
- initial state inside;
- initial state outside;
- quick boundary crossing;
- dwell;
- repeated crossing;
- movement parallel to the boundary;
- location jump;
- low-accuracy update;
- transition after a long offline period.

### Application State

- foreground;
- background;
- terminated;
- device locked;
- device rebooted;
- low-power mode;
- network unavailable;
- changed location permission;
- denied notification permission.

A geofence can trigger correctly while the user sees no notification because notification permission or a channel is disabled.

## Typical Geofencing Defects

- `ENTER` fires several times for one visit.
- `EXIT` is missed after a quick crossing.
- Initial trigger creates an incorrect duplicate event.
- A region uses incorrect coordinates.
- Radius is passed in the wrong units.
- Dwell timer is not reset after exit.
- Old regions remain after logout.
- A different account receives the previous user's event.
- The app treats mock location as a trusted production event.
- A notification contains an expired offer.
- A background restriction delays the event while UI presents it as real-time.
- Analytics count one physical visit several times.

## What Is A BLE Beacon?

A beacon is a small Bluetooth Low Energy transmitter that periodically broadcasts an advertisement packet.

A beacon normally:

- does not know who is nearby;
- does not connect to the internet by itself;
- does not determine GPS coordinates;
- broadcasts an identifier and calibration data;
- uses a battery or continuous power source.

A mobile app or gateway scans BLE advertisements and estimates proximity from received signal strength, or RSSI.

Typical flow:

```text
Beacon broadcasts ID -> phone scans BLE -> app recognizes ID
-> business rule runs -> UI, analytics, or notification action
```

iBeacon is an Apple protocol/profile for proximity use cases. Other beacon formats also exist.

## RSSI And Proximity

RSSI depends on:

- distance;
- calibrated transmit power;
- walls, shelves, and people;
- device orientation;
- phone model and antenna;
- other radio traffic;
- beacon battery;
- scan interval.

Categories such as `immediate`, `near`, and `far` are therefore approximate. RSSI is not a precise measuring tape.

Collect several measurements and validate business thresholds rather than one instant value.

## Beacon Test Matrix

- Bluetooth on/off;
- required Bluetooth/location permissions;
- foreground/background app;
- beacon in range/out of range;
- near/far threshold;
- several nearby beacons;
- accidentally duplicated identifier;
- weak battery;
- blocked signal;
- phone in a pocket or bag;
- different phone models;
- rapid movement;
- stationary dwell;
- device reboot;
- application reinstall;
- beacon replacement;
- offline device;
- delayed server synchronization.

A physical test area should document beacon placement, identifiers, transmit power, and expected ranges.

## Geofence Versus Beacon

| Characteristic | Geofence | BLE Beacon |
| --- | --- | --- |
| Best environment | Outdoor or large regions | Indoor or small proximity zones |
| Main input | Platform location | BLE advertisement |
| Typical scale | Tens or hundreds of meters and more | Near-room or near-object proximity |
| Infrastructure | Usually no local hardware | Physical beacon installation |
| Accuracy | Depends on location accuracy | Depends on RSSI and radio environment |
| Background limits | Location and OS restrictions | Bluetooth scanning and OS restrictions |
| Common use | Arrival, departure, regional trigger | In-store zone, exhibit, nearby asset |

A product can use a coarse geofence to detect arrival near a building and a beacon to identify a specific indoor zone.

## RFID Versus Beacon

| Characteristic | RFID | BLE Beacon |
| --- | --- | --- |
| Object | RFID tag | Active BLE transmitter |
| Reader | Dedicated reader or compatible NFC device | BLE-capable phone or gateway |
| Power | Passive tags can work without a battery | A beacon normally requires power |
| Typical use | Inventory, access, asset identification | Proximity and indoor engagement |
| Mobile support | Depends on RFID type | BLE is widely supported by phones |

RFID geofencing often means a business rule around reader locations rather than a GPS-style circular region.

## Mock Location And Simulation

Use:

- Android mock location applications;
- Android Emulator location controls;
- GPX routes in iOS Simulator or Xcode;
- scripted coordinates;
- test backend events;
- a shielded or controlled beacon test area.

Test:

- static point;
- realistic route;
- different speeds;
- teleport or jump;
- pause on the boundary;
- inaccurate point;
- stale timestamp;
- impossible speed;
- mocked-location policy where applicable.

Simulation accelerates regression but does not reproduce antennas, buildings, background scheduling, and real movement completely.

## Battery And Performance

Location and BLE scanning can consume battery.

Verify:

- scan frequency;
- location update interval;
- background duration;
- CPU wakeups;
- network synchronization frequency;
- duplicate registration;
- behavior in low-power mode;
- device temperature;
- battery use over a representative session.

A feature should not request continuous high-accuracy updates when a geofence transition or low-frequency location is sufficient.

## Security And Privacy

- Request only the location access that is necessary.
- Explain the purpose before the system prompt.
- Do not retain raw location longer than needed.
- Do not log precise coordinates with user identity without protection.
- Test deletion, consent withdrawal, and logout.
- Do not use proximity as the only authorization factor.
- The server must validate high-risk operations independently of client location.
- A beacon identifier is not secret and can be copied or replayed.

Location and movement history can reveal a user's home, work, health, and habits.

## Diagnostics

For a defect, collect:

- device model and OS;
- app build;
- coordinates and accuracy;
- timestamp and timezone;
- permission state;
- precise or approximate mode;
- foreground/background state;
- location services state;
- battery mode;
- geofence ID, center, radius, and transition;
- beacon identifier, RSSI, and transmit power;
- Bluetooth state;
- expected and actual delay;
- screen recording, logs, and route.

Android diagnostics:

```bash
adb logcat
adb shell dumpsys location
adb shell dumpsys bluetooth_manager
```

Do not share raw location logs without a privacy review.

## QA Checklist

- [ ] Technology is identified: location geofence, BLE beacon, or RFID.
- [ ] Permission states are covered.
- [ ] Precise and approximate location are tested.
- [ ] Enter, exit, dwell, and initial trigger are tested.
- [ ] Boundary and low-accuracy scenarios are covered.
- [ ] Foreground, background, and terminated states are tested.
- [ ] Reboot, update, logout, and account switch are covered.
- [ ] A mock route is supplemented with a real-world route.
- [ ] Beacon tests run on several physical devices.
- [ ] Battery use and delayed events are measured.
- [ ] Notifications and analytics are not duplicated.
- [ ] Location data passes privacy review.

## Interview Focus

1. How does GPS/GNSS differ from a platform location service?
2. What is a geofence and which transitions does it support?
3. Why can a geofence event be delayed?
4. How does a beacon differ from a GPS geofence?
5. Why is RSSI not an exact distance?
6. Which location permission states should be tested?
7. Why does mock location not replace a real route?
8. Which privacy risks are associated with location history?

## Sources

- User-provided article: "What Does It All Mean: Beacon Technology, GPS and Geofencing"
- [Android: Create and monitor geofences](https://developer.android.com/develop/sensors-and-location/location/geofencing)
- [Android: Request location permissions](https://developer.android.com/develop/sensors-and-location/location/permissions)
- [Apple Core Location](https://developer.apple.com/documentation/corelocation)
- [Apple iBeacon](https://developer.apple.com/ibeacon/)

