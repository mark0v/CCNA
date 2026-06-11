# Mobile Push Notification Testing

Source: user-provided article, updated with official Android, Apple, and Firebase documentation  
Date added: 2026-06-11  
Related plan item: Mobile Testing  
Tags: QA, mobile testing, push notifications, APNs, FCM, deep links, permissions  
Language: English  
Translation pair: quality-assurance/overview/04-mobile-testing/mobile-push-notifications-testing.md

## Summary

A push notification is a message delivered to a device through a platform push provider. It can inform the user, open specific content, trigger an action, or prompt the application to refresh data.

For QA, push testing covers more than text and an icon. The entire chain matters:

```text
Backend -> APNs/FCM -> device OS -> application -> target screen/action
```

A defect at any stage can look like "the notification did not arrive." Testers should distinguish sending, provider acceptance, device delivery, display, and tap handling.

## Key Points

- Apple Push Notification service, or APNs, delivers remote notifications to Apple devices.
- Firebase Cloud Messaging, or FCM, is commonly used for Android and cross-platform delivery.
- A device or registration token identifies an application installation and can change.
- On iOS, the application requests permission for alerts, sounds, and badges.
- On Android 13+, new installations require the `POST_NOTIFICATIONS` runtime permission for most notifications.
- Android notification channels let users disable individual categories.
- Foreground, background, terminated, and force-stopped states need separate coverage.
- Push delivery is not guaranteed to be immediate, so a critical operation must not depend on a notification alone.
- Payloads must not contain secrets or unnecessary personal data.

## Notes

## Remote Push Flow

A typical flow:

1. The application requests notification permission where required.
2. The OS or messaging SDK issues an installation token.
3. The application sends the token and user/device context to the backend.
4. The backend creates a notification request.
5. A provider such as APNs or FCM accepts the request.
6. The provider attempts delivery to the device.
7. The OS displays the notification or passes the payload to the app.
8. The user taps the notification or an action.
9. The application opens target content and records analytics.

A successful provider response means the request was accepted. It does not always prove that the user saw it.

## Terms

| Term | Meaning |
| --- | --- |
| APNs | Apple Push Notification service |
| FCM | Firebase Cloud Messaging |
| Device/registration token | Identifier for an application installation |
| Payload | Notification data |
| Notification message | Message whose display is often handled by the SDK or OS |
| Data message | Data handled by application code |
| Deep link | Link to a specific screen or content |
| Topic | Group subscribed to a category |
| Collapse key | Rule for replacing stale messages with a newer one |
| TTL | How long a provider can attempt delivery |

Do not confuse a remote push with a local notification. A local notification is scheduled by the app on the device and does not require a remote push provider.

## Permissions

### iOS

Test:

- the first system prompt;
- `Allow`;
- `Don't Allow`;
- provisional or quiet delivery when used;
- permission changes in Settings;
- alerts, sounds, and badges separately;
- returning to the app after denial;
- navigation to system settings.

The app should not repeatedly trigger the system prompt after denial. It can explain the value and direct the user to Settings.

### Android

On Android 13 (API 33) and higher, most new installations must request `POST_NOTIFICATIONS`. Notifications are normally off until the user grants permission.

Test:

- `Allow`;
- `Don't allow`;
- dismissing the dialog without choosing;
- a later request according to product logic;
- device upgrade from Android 12L or lower;
- application restore on a new device;
- disabling all app notifications in Settings;
- disabling one notification channel;
- channel importance, sound, vibration, and badge.

Behavior also depends on target SDK and exemptions. Do not generalize one Android version across the full matrix.

Reset Android 13+ permission state with:

```bash
adb shell pm revoke PACKAGE_NAME android.permission.POST_NOTIFICATIONS
adb shell pm clear-permission-flags PACKAGE_NAME \
  android.permission.POST_NOTIFICATIONS user-set
adb shell pm clear-permission-flags PACKAGE_NAME \
  android.permission.POST_NOTIFICATIONS user-fixed
```

## Application States

| State | What to verify |
| --- | --- |
| Foreground | No duplicate UI and correct in-app presentation |
| Background | Notification displays and opens the correct screen |
| Terminated | Cold start handles payload and navigation |
| Device locked | Sensitive data follows privacy settings |
| User logged out | Previous account data is not displayed |
| Force-stopped Android app | Platform-specific recovery after manual launch |
| Offline | Message arrives after reconnection within its TTL |

Test each state separately because the same payload can follow different code paths.

## Notification Content

Verify:

- title and body;
- application name;
- icon or image;
- timestamp;
- sound and vibration;
- badge count;
- localization;
- text truncation;
- emoji and special characters;
- plural forms;
- right-to-left text;
- sensitive content on the lock screen;
- grouping and ordering;
- duplicate messages;
- expired content.

A notification should make sense without opening the app while revealing no more data than privacy requirements allow.

## Taps, Deep Links, And Actions

Test:

- tap on the body;
- action buttons;
- dismissal;
- opening from the lock screen;
- authenticated and unauthenticated users;
- existing target content;
- deleted or unavailable target content;
- app already open on another screen;
- cold start;
- back navigation after a deep link;
- universal/app-link fallback;
- repeated taps.

A deep link should open relevant content instead of always opening the home screen. Stale content must produce a controlled state rather than a crash or blank page.

## Notification Types

| Type | Example | Main QA focus |
| --- | --- | --- |
| Transactional | Payment, order, account activity | Accuracy, timeliness, privacy |
| Reminder | Appointment, task, abandoned flow | Schedule, timezone, deduplication |
| Promotional | Offer or campaign | Consent, frequency, localization |
| Re-engagement | Return to unfinished activity | Correct segmentation and target |
| Geolocation | Entry into a region | Permission, accuracy, battery |
| Social/message | New message or mention | Ordering, badge, read state |
| System/service | Maintenance or status | Priority, stale information |
| Survey/rating | Feedback request | Eligibility and frequency |

Marketing and operational notifications can have different consent and frequency requirements.

## Payload Testing

Verify:

- required fields;
- optional fields;
- missing title or body;
- unknown fields;
- invalid data types;
- maximum supported size;
- Unicode;
- malformed deep link;
- expired TTL;
- collapse behavior;
- priority;
- target token, topic, or segment;
- development, staging, and production environments.

Example conceptual payload:

```json
{
  "type": "order_status",
  "orderId": "A-1042",
  "status": "ready",
  "deepLink": "example://orders/A-1042"
}
```

The client must not treat a payload as authorization. After opening, it should retrieve current data from the backend and verify access.

## Token Lifecycle

Test:

- first registration;
- logout and login as another user;
- token refresh;
- reinstall;
- restore from backup;
- several devices for one user;
- several accounts on one device;
- invalid or expired token;
- backend token removal;
- opt-out and account deletion.

A common security defect is a device continuing to receive the previous user's notifications after logout.

## Delivery And Reliability

Test:

- online delivery;
- temporary offline state;
- airplane mode;
- Wi-Fi/cellular switch;
- low-power modes;
- delayed delivery;
- out-of-order messages;
- duplicate send;
- collapse of stale updates;
- expired TTL;
- provider rejection;
- invalid-token cleanup;
- large campaign load.

For sequential states such as `created -> shipped -> delivered`, an older status must not appear after the newer one.

Push is a signal, not the only source of truth. The app should synchronize current state with the backend after opening.

## Localization, Time, And Segmentation

Verify:

- device language;
- account language;
- locale and region;
- timezone and daylight saving time;
- campaign schedule;
- user segment;
- age, subscription, and consent restrictions;
- quiet hours;
- frequency caps;
- exclusion lists.

Do not infer a user's local time only from the current IP address. The user may travel, use a VPN, or have a different timezone in the profile.

## Security And Privacy

- Do not put passwords, tokens, or confidential data in a payload.
- Consider lock-screen previews and connected wearables.
- Verify cross-account token binding.
- A deep link must not bypass authentication or authorization.
- APNs/FCM server credentials must not exist in the mobile client.
- Logs and analytics must not expose full sensitive payloads.
- The backend must stop sending after account deletion or opt-out.

Push payloads pass through external infrastructure and the device OS. Send only the minimum necessary information.

## Diagnostics

Collect:

- message or campaign ID;
- provider response;
- send timestamp;
- token hash or safe target identifier;
- device receipt timestamp;
- display timestamp;
- tap/action timestamp;
- application state;
- device model and OS;
- app build;
- permission and channel state;
- network state;
- relevant client logs.

Android:

```bash
adb logcat
adb shell dumpsys notification
```

For iOS, use Xcode device logs, application logs, and the provider-side APNs response. A screenshot alone cannot diagnose production delivery.

## Metrics

| Metric | Question |
| --- | --- |
| Opt-in rate | Do users grant notification permission? |
| Provider acceptance | Did the provider accept requests? |
| Delivery/display rate | Did messages arrive and display? |
| Open rate | Did the user open the notification? |
| Conversion | Did the user complete the target action? |
| Opt-out rate | Did users disable notifications? |
| Uninstall rate | Did users remove the app under messaging pressure? |
| Latency | How long did delivery take? |

Do not confuse an open with a conversion. A notification can be opened without completing the intended action.

## Core Test Matrix

- [ ] Supported iOS and Android versions.
- [ ] Physical devices and production-like signing.
- [ ] Permission allow, deny, dismiss, and settings changes.
- [ ] Foreground, background, terminated, and locked states.
- [ ] Wi-Fi, cellular, offline, and network switch.
- [ ] Correct text, icon, sound, badge, and grouping.
- [ ] Deep links and action buttons.
- [ ] Logged-in, logged-out, and switched-account states.
- [ ] Token refresh, reinstall, and multiple devices.
- [ ] Localization, timezone, and quiet hours.
- [ ] Duplicate, delayed, expired, and out-of-order messages.
- [ ] Security, privacy, and lock-screen previews.
- [ ] Analytics events without double counting.

## Typical Defects

- Android 13 permission is not requested, so notifications remain invisible.
- A channel is disabled while the global app permission is enabled.
- A push appears twice because both the SDK and custom handler display it.
- A tap opens home instead of the target screen.
- Cold start loses the deep link.
- Badge count does not decrease after reading.
- The previous account receives a notification after logout.
- Private text appears on the lock screen.
- An incorrect timezone shifts a reminder.
- An older status arrives after a newer one.
- A staging build is registered in the production push environment or vice versa.
- The provider accepts a request, but the backend incorrectly reports it as delivered.

## Interview Focus

1. How does remote push differ from a local notification?
2. What is the delivery chain through APNs or FCM?
3. Which permission scenarios belong in iOS and Android 13+ coverage?
4. Why do foreground and terminated states require separate tests?
5. What happens to a token after reinstall or refresh?
6. How do you test a deep link from a notification?
7. Why does provider success not equal actual delivery?
8. Which data must never be placed in a payload?

## Sources

- User-provided article: "Mobile Push Notifications: Everything you need to know"
- [Android notification runtime permission](https://developer.android.com/develop/ui/views/notifications/notification-permission)
- [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging)
- [Apple User Notifications](https://developer.apple.com/documentation/usernotifications)

