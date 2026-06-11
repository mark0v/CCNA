# Тестирование мобильных Push Notifications

Source: user-provided article, updated with official Android, Apple, and Firebase documentation  
Date added: 2026-06-11  
Related plan item: Mobile Testing  
Tags: QA, mobile testing, push notifications, APNs, FCM, deep links, permissions  
Language: Russian  
Translation pair: quality-assurance-en/overview/04-mobile-testing/mobile-push-notifications-testing.md

## Summary

Push notification — сообщение, которое remote service доставляет на устройство через platform push provider. Оно может информировать пользователя, открывать определённый экран, запускать action или обновлять данные приложения.

Для QA проверка push — это не только текст и иконка. Нужно покрыть всю цепочку:

```text
Backend -> APNs/FCM -> device OS -> application -> target screen/action
```

Дефект на любом этапе может выглядеть одинаково: «уведомление не пришло». Поэтому тестировщик должен разделять отправку, доставку, отображение и обработку нажатия.

## Key Points

- Apple Push Notification service, или APNs, доставляет remote notifications на Apple devices.
- Firebase Cloud Messaging, или FCM, часто используется для Android и может участвовать в cross-platform delivery.
- Device token или registration token идентифицирует конкретную app installation и может измениться.
- На iOS приложение запрашивает разрешение пользователя на alerts, sounds и badges.
- На Android 13+ новые установки требуют runtime-разрешение `POST_NOTIFICATIONS` для большинства notifications.
- Android notification channels позволяют пользователю отключать отдельные категории.
- Foreground, background, terminated и force-stopped states необходимо тестировать отдельно.
- Push delivery не гарантируется как мгновенная, поэтому critical business operation не должна зависеть только от notification.
- Payload не должен содержать secrets или лишние personal data.

## Notes

## Как работает Remote Push

Типичный flow:

1. Application запрашивает notification permission, если это требуется.
2. OS или messaging SDK выдаёт app installation token.
3. Application отправляет token на backend вместе с user/device context.
4. Backend создаёт notification request.
5. Provider, например APNs или FCM, принимает request.
6. Provider пытается доставить message на device.
7. OS показывает notification или передаёт payload приложению.
8. Пользователь нажимает notification или action.
9. Application открывает target content и отправляет analytics event.

Успешный ответ provider означает, что request принят, но не всегда доказывает фактическое отображение пользователю.

## Термины

| Term | Meaning |
| --- | --- |
| APNs | Apple Push Notification service |
| FCM | Firebase Cloud Messaging |
| Device/registration token | Идентификатор конкретной установки приложения |
| Payload | Данные notification |
| Notification message | Сообщение, отображением которого часто управляет SDK/OS |
| Data message | Данные, обработку которых контролирует application |
| Deep link | Ссылка на конкретный screen или content |
| Topic | Группа подписчиков на определённую категорию |
| Collapse key | Правило замены устаревших сообщений новым |
| TTL | Срок, в течение которого provider может пытаться доставить message |

Не путайте push notification с local notification. Local notification планируется самим приложением на устройстве и не требует remote push provider.

## Permissions

### iOS

Проверяйте:

- первый system prompt;
- `Allow`;
- `Don't Allow`;
- provisional или quiet delivery, если используется;
- изменение разрешений в Settings;
- alerts, sounds и badges по отдельности;
- повторный вход в app после denial;
- корректную ссылку на system settings.

Приложение не должно бесконечно показывать системный prompt после отказа. Оно может объяснить ценность уведомлений и направить пользователя в Settings.

### Android

На Android 13 (API 33) и выше большинство новых установок должны запросить `POST_NOTIFICATIONS`. До выдачи разрешения notifications для нового app обычно выключены.

Проверяйте:

- `Allow`;
- `Don't allow`;
- dismiss системного dialog без выбора;
- повторный запрос согласно product logic;
- обновление устройства с Android 12L или ниже;
- restore приложения на новом устройстве;
- отключение всех app notifications в Settings;
- отключение отдельного notification channel;
- channel importance, sound, vibration и badge.

Поведение зависит также от target SDK и exemptions. Не переносите результат одного Android version на всю matrix.

Для сброса состояния Android 13+:

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
| Foreground | Не создаётся ли duplicate UI; корректна ли in-app presentation |
| Background | Notification отображается и открывает правильный screen |
| Terminated | Cold start корректно обрабатывает payload и navigation |
| Device locked | Sensitive data не раскрывается вопреки privacy settings |
| User logged out | Не показываются данные предыдущего account |
| Force-stopped Android app | Проверяется platform-specific recovery после ручного запуска |
| Offline | Message доставляется после восстановления сети в пределах TTL |

Тестируйте states отдельно. Один и тот же payload может обрабатываться разными code paths.

## Notification Content

Проверяйте:

- title и body;
- app name;
- icon или image;
- timestamp;
- sound и vibration;
- badge count;
- localization;
- text truncation;
- emoji и special characters;
- plural forms;
- right-to-left text;
- sensitive content на lock screen;
- grouping и ordering;
- duplicate messages;
- expired content.

Notification должна оставаться понятной без открытия app, но не раскрывать больше данных, чем разрешают privacy requirements.

## Tap, Deep Links And Actions

Проверьте:

- tap по body;
- action buttons;
- dismiss;
- открытие из lock screen;
- authenticated и unauthenticated user;
- target object существует;
- target object удалён или недоступен;
- app уже открыт на другом screen;
- cold start;
- back navigation после deep link;
- universal/app link fallback;
- repeated tap.

Deep link должен открывать конкретный relevant screen, а не всегда home page. Если content устарел, приложение должно показать контролируемое состояние, а не crash или пустой экран.

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

Marketing и operational notifications часто имеют разные consent и frequency requirements.

## Payload Testing

Проверяйте:

- required fields;
- optional fields;
- missing title/body;
- unknown fields;
- invalid data types;
- maximum supported size;
- Unicode;
- malformed deep link;
- expired TTL;
- collapse behavior;
- priority;
- target token, topic или segment;
- environment: development/staging/production.

Пример условного payload:

```json
{
  "type": "order_status",
  "orderId": "A-1042",
  "status": "ready",
  "deepLink": "example://orders/A-1042"
}
```

Client не должен доверять payload как источнику authorization. После открытия он должен получить актуальные данные с backend и проверить access.

## Token Lifecycle

Тестируйте:

- first registration;
- logout и login другого user;
- token refresh;
- reinstall;
- restore from backup;
- несколько devices одного user;
- несколько accounts на одном device;
- invalid или expired token;
- удаление token на backend;
- opt-out и account deletion.

Распространённый security defect: после logout устройство продолжает получать notifications предыдущего пользователя.

## Delivery And Reliability

Проверяйте:

- online delivery;
- temporary offline;
- airplane mode;
- Wi-Fi/cellular switch;
- low-power modes;
- delayed delivery;
- out-of-order messages;
- duplicate send;
- collapse of outdated updates;
- expired TTL;
- provider rejection;
- invalid token cleanup;
- large campaign load.

Для последовательных статусов вроде `created -> shipped -> delivered` пользователь не должен увидеть устаревший статус после более нового.

Push — сигнал, а не единственное хранилище истины. После открытия app должна синхронизировать актуальное состояние с backend.

## Localization, Time And Segmentation

Проверяйте:

- device language;
- account language;
- locale и region;
- timezone и daylight saving time;
- campaign schedule;
- user segment;
- age, subscription и consent restrictions;
- quiet hours;
- frequency caps;
- exclusion lists.

Нельзя определять локальное время пользователя только по текущему IP: пользователь может путешествовать, использовать VPN или иметь другой timezone в profile.

## Security And Privacy

- Не помещайте passwords, tokens или confidential data в payload.
- Учитывайте preview на lock screen и connected wearable.
- Проверяйте cross-account token binding.
- Deep link не должен обходить authentication/authorization.
- Server credentials для APNs/FCM не должны находиться в mobile client.
- Logs и analytics не должны раскрывать полный sensitive payload.
- После account deletion или opt-out backend должен прекратить отправку.

Push payload проходит через external infrastructure и device OS. Передавайте минимально необходимую информацию.

## Diagnostics

Собирайте:

- message/campaign ID;
- provider response;
- send timestamp;
- target token hash или безопасный identifier;
- device receipt timestamp;
- display timestamp;
- tap/action timestamp;
- app state;
- device model и OS;
- app build;
- permission/channel state;
- network state;
- relevant client logs.

Android:

```bash
adb logcat
adb shell dumpsys notification
```

На iOS полезны Xcode device logs, application logs и provider-side APNs response. Production delivery нельзя диагностировать только по screenshot.

## Metrics

| Metric | Question |
| --- | --- |
| Opt-in rate | Пользователи разрешают notifications? |
| Provider acceptance | Provider принял requests? |
| Delivery/display rate | Messages дошли и были показаны? |
| Open rate | Пользователь открыл notification? |
| Conversion | Выполнил целевое действие? |
| Opt-out rate | Отключил notifications? |
| Uninstall rate | Удалил app после messaging pressure? |
| Latency | Сколько заняла доставка? |

Не путайте open и conversion. Notification может быть открыта, но target action не завершён.

## Core Test Matrix

- [ ] iOS и Android supported versions.
- [ ] Physical devices и production-like signing.
- [ ] Permission allow, deny, dismiss и settings changes.
- [ ] Foreground, background, terminated и locked states.
- [ ] Wi-Fi, cellular, offline и network switch.
- [ ] Correct text, icon, sound, badge и grouping.
- [ ] Deep link и action buttons.
- [ ] Logged-in, logged-out и switched-account states.
- [ ] Token refresh, reinstall и multiple devices.
- [ ] Localization, timezone и quiet hours.
- [ ] Duplicate, delayed, expired и out-of-order messages.
- [ ] Security, privacy и lock-screen previews.
- [ ] Analytics events без double counting.

## Typical Defects

- Android 13 permission не запрашивается, поэтому notifications не видны.
- Channel отключён, хотя global app permission включён.
- Push приходит дважды: от SDK и custom handler.
- Tap открывает home вместо target screen.
- Cold start теряет deep link.
- Badge не уменьшается после прочтения.
- Старый account получает notification после logout.
- Notification показывает private text на lock screen.
- Неверная timezone сдвигает reminder.
- Более старый status приходит после нового.
- Staging build зарегистрирован в production push environment или наоборот.
- Provider принял request, но backend ошибочно считает его доставленным.

## Interview Focus

1. Чем remote push отличается от local notification?
2. Как выглядит delivery chain через APNs или FCM?
3. Какие permission scenarios нужно проверить на iOS и Android 13+?
4. Почему foreground и terminated states тестируются отдельно?
5. Что происходит с token после reinstall или refresh?
6. Как проверить deep link из notification?
7. Почему provider success не равен фактической delivery?
8. Какие данные нельзя помещать в payload?

## Sources

- User-provided article: "Mobile Push Notifications: Everything you need to know"
- [Android notification runtime permission](https://developer.android.com/develop/ui/views/notifications/notification-permission)
- [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging)
- [Apple User Notifications](https://developer.apple.com/documentation/usernotifications)

