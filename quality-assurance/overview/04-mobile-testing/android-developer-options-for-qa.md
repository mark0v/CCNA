# Android Developer Options для QA

Source: user-provided material based on Android Developers documentation  
Date added: 2026-06-11  
Related plan item: Mobile Testing  
Tags: QA, mobile testing, Android, Developer options, USB debugging, ADB  
Language: Russian  
Translation pair: quality-assurance-en/overview/04-mobile-testing/android-developer-options-for-qa.md

## Summary

`Developer options` — скрытый раздел настроек Android для отладки, диагностики и моделирования нестандартных условий.

Для QA он полезен, чтобы:

- подключить реальное устройство через `adb`;
- собирать логи и bug report;
- показывать касания во время записи видео;
- проверять RTL-интерфейс и границы layout;
- выбирать mock location application;
- исследовать проблемы с rendering, memory и background lifecycle;
- воспроизводить отдельные Bluetooth, USB и network scenarios.

Эти настройки изменяют поведение устройства. Перед тестированием важно записать все нестандартные значения, а после эксперимента вернуть их к default state.

## Key Points

- На Android 4.2 и выше раздел обычно включается семью нажатиями на `Build number`.
- Названия и расположение настроек отличаются в зависимости от Android version и производителя.
- `USB debugging` разрешает компьютеру управлять устройством через Android Debug Bridge.
- При первом USB-подключении пользователь должен подтвердить RSA key доверенного компьютера.
- Wireless debugging с pairing поддерживается на телефонах с Android 11 и выше.
- `Show taps` и `Pointer location` улучшают evidence при записи дефекта.
- `Don't keep activities` и `Background process limit` подходят для stress testing, но не отражают обычное состояние телефона.
- Developer options не должны постоянно оставаться включёнными на личном или production device.

## Notes

## Как включить Developer Options

1. Откройте `Settings`.
2. Найдите `Build number`.
3. Нажмите на него семь раз.
4. При необходимости подтвердите PIN, pattern или password.
5. Вернитесь назад и откройте `Developer options`.

Типичные пути:

| Device | Path |
| --- | --- |
| Google Pixel | `Settings > About phone > Build number` |
| Samsung Galaxy | `Settings > About phone > Software information > Build number` |
| Многие другие устройства | `Settings > System > About phone > Build number` |

Производитель может изменить название или расположение раздела. Если путь не совпадает, используйте поиск внутри Settings.

## Подключение устройства к ADB

### USB Debugging

1. Включите `Developer options`.
2. Активируйте `USB debugging`.
3. Подключите устройство data-capable USB cable.
4. Разблокируйте экран.
5. Подтвердите RSA fingerprint компьютера.
6. Проверьте подключение:

```bash
adb devices
```

Ожидаемые состояния:

| State | Meaning |
| --- | --- |
| `device` | Устройство подключено и авторизовано |
| `unauthorized` | RSA confirmation не подтверждён |
| `offline` | Соединение установлено, но устройство не отвечает |
| Устройство отсутствует | Проблема с кабелем, USB mode, driver или ADB server |

Если устройство не обнаружено, проверьте:

- поддерживает ли кабель передачу данных;
- выбран ли подходящий `Default USB configuration`;
- установлен ли OEM USB driver на Windows;
- разблокирован ли экран;
- не был ли отклонён RSA prompt.

Для сброса доверенных компьютеров используйте `Revoke USB debugging authorizations`, затем подключитесь снова.

### Wireless Debugging

Телефоны с Android 11 и выше могут подключаться к `adb` через Wi-Fi с помощью QR code или pairing code.

Устройство и workstation должны находиться в одной сети. Corporate Wi-Fi может блокировать peer-to-peer traffic или mDNS discovery.

После pairing проверьте соединение:

```bash
adb devices
```

Wireless debugging удобно, когда:

- USB port нужен для другого оборудования;
- требуется тестировать charging or accessory scenarios;
- плохой кабель вызывает нестабильное соединение;
- несколько устройств подключаются к одной workstation.

Это не тест мобильной сети: команды всё ещё идут через Wi-Fi infrastructure.

## Полезные настройки для QA

### Evidence и UI

| Option | QA use |
| --- | --- |
| `Show taps` | Показывает точки касания в screen recording |
| `Pointer location` | Показывает coordinates и траекторию жеста |
| `Show layout bounds` | Отображает границы views, margins и clipping |
| `Force RTL layout direction` | Быстрая проверка интерфейса справа налево |
| `Simulate secondary displays` | Проверка additional display scenarios |
| `System UI demo mode` | Чистые screenshots без случайных notifications |

`Pointer location` добавляет много служебной информации и может закрывать UI. Для обычного bug video чаще достаточно `Show taps`.

### Debugging и test data

| Option | QA use |
| --- | --- |
| `Take bug report` | Сохраняет system logs и diagnostic information |
| `Select debug app` | Выбирает debuggable application |
| `Wait for debugger` | Останавливает запуск выбранного app до подключения debugger |
| `Select mock location app` | Позволяет подменить GPS location |
| `Bluetooth HCI snoop log` | Записывает Bluetooth traffic для анализа |
| `Stay awake` | Не выключает экран, пока устройство подключено к питанию |

Mock location полезен для geofencing, maps, delivery и regional scenarios. Проверяйте также поведение без location permission, с выключенной геолокацией и на реальном маршруте.

### Rendering и accessibility

| Option | QA use |
| --- | --- |
| `Profile GPU rendering` | Помогает заметить медленные frames и UI jank |
| `Debug GPU overdraw` | Показывает повторную отрисовку одних pixels |
| `Show GPU view updates` | Подсвечивает обновляемые GPU regions |
| `Simulate color space` | Быстрая визуальная проверка восприятия цветов |
| Animation scales | Проверка transitions на разных скоростях |

Не оценивайте production performance после включения forced rendering, GPU overlays или нестандартных animation scales. Сначала воспроизведите проблему на default configuration.

### Lifecycle и background behavior

| Option | QA use | Risk |
| --- | --- | --- |
| `Don't keep activities` | Быстро выявляет ошибки восстановления state | Искусственно уничтожает каждую Activity после ухода с неё |
| `Background process limit` | Проверяет работу при ограниченной памяти | Меняет обычное управление процессами Android |
| Memory information | Показывает общее и per-app memory usage | Не заменяет profiling и long-running tests |

`Don't keep activities` не является точной симуляцией low-memory kill. Используйте его как stress tool, а найденный дефект перепроверьте в реалистичном lifecycle scenario.

## Базовые ADB-команды для тестировщика

```bash
# Список подключённых устройств
adb devices

# Логи устройства
adb logcat

# Остановить приложение
adb shell am force-stop com.example.app

# Очистить данные приложения
adb shell pm clear com.example.app

# Создать полный bug report
adb bugreport

# Записать экран
adb shell screenrecord /sdcard/test.mp4

# Скопировать запись на компьютер
adb pull /sdcard/test.mp4
```

`pm clear` удаляет локальные данные приложения и эквивалентен чистому состоянию после установки только с точки зрения app data. Версия приложения, permissions, внешние файлы и server-side account state могут сохраниться или отличаться.

## QA-сценарии

### UI и gestures

- Запишите defect с включённым `Show taps`.
- Проверьте swipe, long press, multi-touch и edge gestures.
- Включите `Show layout bounds` и найдите clipping или неправильные touch targets.
- Включите `Force RTL` и проверьте navigation, icons, alignment и mixed-direction text.
- Верните настройки и повторите critical flow в default state.

### Lifecycle

- Откройте форму с введёнными, но не отправленными данными.
- Переведите app в background.
- Создайте memory pressure или временно включите `Don't keep activities`.
- Вернитесь в app.
- Проверьте восстановление screen, navigation stack, draft и scroll position.

### Location

- Выберите approved mock location app.
- Проверьте разные countries, time zones и coordinates.
- Проверьте резкий location jump и отсутствие сигнала.
- Повторите critical scenario с real GPS.

### Connectivity и accessories

- Проверьте USB modes: charging, MTP и другие поддерживаемые варианты.
- Соберите Bluetooth HCI log только при необходимости и безопасно обработайте данные.
- Проверьте Wi-Fi handover отдельно в реальных network conditions.
- Не считайте developer network toggles полной заменой реальной плохой сети.

## Что указать в bug report

Помимо стандартных шагов и expected/actual result, добавьте:

- device model;
- Android version и build number;
- application build;
- connection type: USB или Wi-Fi;
- включённые Developer options;
- animation scale;
- background process limit;
- использовалась ли mock location;
- наличие root, custom firmware или work profile;
- timestamps для сопоставления с `logcat`;
- bug report, logs, screenshot или screen recording.

Без этой информации нестандартная настройка может создать дефект, который команда не сможет воспроизвести.

## Безопасность и восстановление

- Подтверждайте RSA fingerprint только на доверенном компьютере.
- Не оставляйте USB or wireless debugging включённым без необходимости.
- Удаляйте старые paired workstations.
- Не публикуйте bug report без проверки: он может содержать accounts, device identifiers, network details и пользовательские данные.
- После теста выключите mock location, visual overlays и lifecycle stress options.
- При сомнении выключите общий переключатель Developer options или восстановите изменённые значения вручную.

## Interview Focus

1. Как включить Developer options на Android?
2. Чем `USB debugging` отличается от обычного USB file transfer?
3. Что означает состояние `unauthorized` в `adb devices`?
4. Для чего QA использует `Show taps`, `Show layout bounds` и `Force RTL`?
5. Почему `Don't keep activities` нельзя считать обычным пользовательским окружением?
6. Какие данные нужно приложить к Android bug report?
7. Какие риски создаёт постоянно включённый ADB?

## Sources

- [Configure on-device developer options](https://developer.android.com/studio/debug/dev-options)
- [Android Debug Bridge](https://developer.android.com/tools/adb)

