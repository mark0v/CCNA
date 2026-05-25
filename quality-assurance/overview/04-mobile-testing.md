# 📱 04 — Mobile тестирование

> **Твой уровень:** 🔴 КРИТИЧЕСКИЙ ПРОБЕЛ (все подтемы Not Started в матрице)  
> **Приоритет:** ⭐⭐⭐ ВЫСОКИЙ

---

## 4.1 Типы мобильных приложений
**Твой уровень:** 🔴 ПРОБЕЛ

### Native Apps
- Написаны на нативном языке платформы: **Swift/Obj-C** (iOS), **Kotlin/Java** (Android)
- Установка через App Store / Google Play
- Лучший UX, полный доступ к API устройства
- **Что тестировать:** нативные UI элементы, жесты, нотификации, разрешения

### Hybrid Apps
- Веб-технологии (HTML/CSS/JS) внутри нативной оболочки (React Native, Ionic, Cordova)
- Одна кодовая база для iOS и Android
- **Что тестировать:** WebView поведение + нативные фичи

### Mobile Web Apps
- Веб-сайт, адаптированный под мобильный браузер
- Нет установки, работает через браузер
- **Что тестировать:** responsive дизайн, touch события, мобильный UX

### Ресурсы
- 🔗 [Native vs Hybrid vs Web Apps](https://www.mobiloud.com/blog/native-web-or-hybrid-apps)
- 🔗 [Types of Mobile Apps (ClevertTap)](https://clevertap.com/blog/types-of-mobile-apps/)

---

## 4.2 Специфика iOS
**Твой уровень:** 🔴 ПРОБЕЛ

### Файловая система iOS
- Sandboxing — каждое приложение изолировано в своей "песочнице"
- Папки: Documents, Library, Temp — что хранится где
- **Apple File System (APFS)** — современная файловая система Apple
- 🔗 [iOS File System (Apple)](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html)

### UI элементы iOS
- Navigation Bar, Tab Bar, Toolbar
- UITableView, UICollectionView
- UIAlertController, UIActionSheet
- Стандартные паттерны жестов: Swipe, Pinch, Tap, Long Press
- 🔗 [iOS Design Handbook](https://designcode.io/ios-design-handbook-ios-native-ui-elements)

### Версии iOS и устройства
- Покрытие версий OS при тестировании
- Матрица устройств (iPhone SE, iPhone 14, iPad и т.д.)
- 🔗 [App Store Distribution (Apple)](https://developer.apple.com/support/app-store/)

### Jailbreak
- Что такое jailbreak и зачем он нужен QA
- Риски тестирования на джейлбрейкнутых устройствах
- 🔗 [What is Jailbreaking (Kaspersky)](https://www.kaspersky.com/resource-center/definitions/what-is-jailbreaking)

### App Store Guidelines
- Что нельзя публиковать
- Требования к иконкам, скриншотам
- 🔗 [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)

---

## 4.3 Специфика Android
**Твой уровень:** 🔴 ПРОБЕЛ

### Файловая система Android
- Внутреннее хранилище vs SD карта
- Папки приложения: data/data/package_name/
- Shared Preferences, SQLite, Cache
- 🔗 [Android Data Storage](https://developer.android.com/training/data-storage)

### UI элементы Android
- ActionBar / Toolbar
- RecyclerView, ListView
- Material Design компоненты
- Navigation Drawer, Bottom Navigation
- 🔗 [Android UI Overview](https://developer.android.com/guide/topics/ui)
- 🔗 [Material Design (iOS compatible)](https://material.io/components?platform=ios)

### Версии Android и фрагментация
- Актуальные версии Android: 12, 13, 14, 15
- Фрагментация устройств — производители: Samsung, Xiaomi, Huawei, Google
- 🔗 [Android Versions (javatpoint)](https://www.javatpoint.com/android-versions)
- 🔗 [Android Dashboards](https://developer.android.com/about/dashboards)
- 🔗 [Top Manufacturers](https://www.appbrain.com/stats/top-manufacturers)

### Root права
- Что такое root доступ
- Зачем нужен QA (тестирование скрытых функций, логи)
- 🔗 [Root Android (AndroidCentral)](https://www.androidcentral.com/root)

---

## 4.4 Эмуляторы и симуляторы
**Твой уровень:** 🔴 ПРОБЕЛ

### Разница
| | Simulator | Emulator |
|--|-----------|----------|
| Что делает | Симулирует поведение | Эмулирует железо |
| Платформа | iOS Simulator (только macOS) | Android Emulator |
| Производительность | Быстрее | Медленнее |
| Аппаратные функции | Ограничены | Больше возможностей |

### Android Emulator (Android Studio)
- Создание AVD (Android Virtual Device)
- Developer Options на реальном устройстве
- ADB команды: `adb devices`, `adb logcat`, `adb install`

### iOS Simulator (Xcode)
- Симулятор встроен в Xcode (только macOS)
- Симуляция Push Notifications, Location, BiometricAuth

### Облачные устройства
- **BrowserStack** — реальные устройства в облаке
- **Sauce Labs** — облачная ферма устройств

### Ресурсы
- 🔗 [Emulator vs Simulator](https://perfectial.com/blog/emulator-vs-simulator/)
- 🔗 [Simulators vs Emulators (SauceLabs)](https://saucelabs.com/blog/simulators-vs-emulators-whats-the-difference-anyway)
- 🔗 [Android Developer Options](https://developer.android.com/studio/debug/dev-options)

---

## 4.5 Типы Mobile тестирования
**Твой уровень:** 🔴 ПРОБЕЛ

### Основные виды
- **Functional Testing** — проверка функций приложения
- **Usability Testing** — удобство использования
- **Performance Testing** — скорость загрузки, отклик, потребление памяти/батареи
- **Compatibility Testing** — разные устройства, OS версии, размеры экранов
- **Installation Testing** — установка, обновление, удаление
- **Interrupt Testing** — звонок, SMS, нотификации во время использования
- **Network Testing** — работа при смене сети (WiFi → 4G → offline)
- **Security Testing** — права доступа, хранение данных

### Ресурсы
- 🔗 [Mobile Testing Types (BrowserStack)](https://www.browserstack.com/guide/mobile-testing-types)
- 🔗 [Mobile Testing Checklist](http://www.testingdiaries.com/mobile-testing-checklist/)

---

## 4.6 Типы подключений
**Твой уровень:** 🔴 ПРОБЕЛ

### Тестирование сетевых условий
- **WiFi** — стабильное подключение
- **4G LTE / 3G / 2G** — разная скорость, задержки
- **Bluetooth** — для устройств (wearables, колонки, авто)
- **Airplane Mode** — полное отключение
- **Roaming** — поведение при роуминге
- **Переключение сети** — WiFi → 4G и обратно

### Имитация плохого соединения
- Android: Developer Options → Network throttling
- iOS: Settings → Developer → Network Link Conditioner
- Charles Proxy — Throttle bandwidth
- 🔗 [Simulate Slow Network (BrowserStack)](https://www.browserstack.com/guide/how-to-simulate-slow-network-conditions)
- 🔗 [BAM Tech: Poor Network](https://www.bam.tech/article/simulate-poor-network-test-mobile-apps-device)

---

## 4.7 Push Notifications
**Твой уровень:** 🔴 ПРОБЕЛ

### Что тестировать
- Доставка нотификации (foreground / background / killed state)
- Содержание: заголовок, текст, иконка, deep link
- Тапа по нотификации — куда переходит пользователь
- Группировка нотификаций
- Поведение при отключённых нотификациях
- Silent push (без визуального оповещения)

### Инструменты
- Firebase Cloud Messaging (FCM) — Android
- Apple Push Notification Service (APNs) — iOS
- Ручная отправка через Postman / Firebase console

### Ресурсы
- 🔗 [Mobile Push Notifications (GetVero)](https://www.getvero.com/resources/mobile-push-notifications/)
- 🔗 [Types of Push Notifications](https://www.moengage.com/blog/11-types-of-compelling-mobile-push-notifications-that-delight-users/)

---

## 4.8 In-App Purchases (Покупки)
**Твой уровень:** 🔴 ПРОБЕЛ

### Типы покупок
- **Consumable** — одноразовые (монеты, жизни в игре)
- **Non-Consumable** — постоянные (разблокировка фич)
- **Subscriptions** — регулярные платежи

### Тестовые среды
- **iOS Sandbox** — тестовые покупки без реальных денег
- **Android Test Purchases** — тестовый режим Google Play
- **TestFlight** — дистрибуция тестовых сборок iOS

### Ресурсы
- 🔗 [Testing In-App Purchases iOS](https://developer.apple.com/documentation/storekit/original_api_for_in-app_purchase/testing_in-app_purchases_with_sandbox)
- 🔗 [Google Play Billing Test](https://developer.android.com/google/play/billing/test)
- 🔗 [RevenueCat Google Play](https://docs.revenuecat.com/docs/google-play-store)

---

## 4.9 GPS и геолокация
**Твой уровень:** 🔴 ПРОБЕЛ

### Тестирование геолокации
- Разрешения: Always / While Using / Never
- Точность GPS (реальный GPS, WiFi triangulation, Cell)
- **Fake GPS** — тестирование с имитацией местоположения
- Geofencing — тест триггеров на вход/выход из зоны
- Beacons — Bluetooth маяки для точного Indoor positioning

### Ресурсы
- 🔗 [Fake GPS для тестирования](https://www.tenorshare.com/iphone-tips/poplular-fake-location-app.html)
- 🔗 [GPS, Beacons, Geofencing](https://www.apptricity.com/what-does-it-all-mean-beacon-technology-gps-and-geofencing/)

---

## 4.10 Чтение мобильных логов
**Твой уровень:** 🔴 ПРОБЕЛ (из IDP)

### Android логи (ADB Logcat)
```bash
# Просмотр всех логов
adb logcat

# Фильтр по тегу
adb logcat -s "MyApp"

# Фильтр по уровню (V/D/I/W/E)
adb logcat *:E  # только ошибки

# Сохранить в файл
adb logcat > logs.txt
```
- Уровни логов: **V**erbose, **D**ebug, **I**nfo, **W**arning, **E**rror
- Как найти крэш: искать `AndroidRuntime FATAL EXCEPTION`

### iOS логи (Xcode / Console)
- **Xcode** → Window → Devices and Simulators → просмотр логов
- **Console.app** — логи с подключённого устройства
- Crash репорты в Settings → Privacy → Analytics

### Ресурсы
- 🔗 [Getting iOS Crash Logs](https://training.qatestlab.com/blog/technical-articles/getting-ios-crash-logs/)
- 🔗 [Finding Android Logs (ADB)](https://documentation.meraki.com/SM/Other_Topics/Finding_Logs_for_Android_Troubleshooting)
- 🔗 [Xcode (Wikipedia)](https://en.wikipedia.org/wiki/Xcode)
- 🔗 [Android Studio (Wikipedia)](https://en.wikipedia.org/wiki/Android_Studio)

---

## 4.11 Настройка прокси на мобильных
**Твой уровень:** 🔴 ПРОБЕЛ

### Зачем нужен прокси на мобильном
- Перехватывать HTTP/HTTPS запросы от мобильного приложения
- Тестировать API mobile app
- Имитировать разные ответы сервера

### Настройка (Charles Proxy)
1. Запустить Charles на компьютере
2. В настройках WiFi на телефоне → Manual Proxy → IP компьютера: 8888
3. Установить сертификат Charles на телефон (для HTTPS)

- 🔗 [Proxy Setup Android](https://www.cactusvpn.com/tutorials/how-to-set-up-proxy-on-android-mobile-network/)
- 🔗 [Proxy Setup iPhone](https://smartproxy.com/configuration/how-to-setup-proxy-for-iphone)

---

## ✅ Чеклист по разделу

- [ ] Знаю разницу Native / Hybrid / Mobile Web
- [ ] Понимаю файловую систему iOS и Android
- [ ] Умею работать с Android Emulator (создать AVD, запустить, ADB)
- [ ] Знаю разницу Simulator (iOS) vs Emulator (Android)
- [ ] Умею читать ADB Logcat и находить ошибки
- [ ] Знаю типы мобильного тестирования (Interrupt, Network, Install, Performance)
- [ ] Умею тестировать Push Notifications
- [ ] Знаю как тестировать In-App Purchases в Sandbox
- [ ] Умею настроить прокси на мобильном для перехвата трафика
- [ ] Знаю что такое Fake GPS и как его применить при тестировании
