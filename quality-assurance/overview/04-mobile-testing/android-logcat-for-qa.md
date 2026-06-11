# Android Logcat для QA

Source: user-provided Android Developers material  
Date added: 2026-06-11  
Related plan item: Mobile Testing  
Tags: QA, mobile testing, Android, Logcat, ADB, logs, crash analysis  
Language: Russian  
Translation pair: quality-assurance-en/overview/04-mobile-testing/android-logcat-for-qa.md

## Summary

Logcat показывает сообщения приложений, Android system services и самого устройства в реальном времени. Когда приложение падает, в логе обычно появляются exception, причина ошибки и stack trace.

Для QA Logcat помогает:

- подтвердить crash или ANR техническими данными;
- найти HTTP, database, permission и lifecycle errors;
- сопоставить пользовательское действие с точным timestamp;
- отличить UI-дефект от backend или device problem;
- приложить к bug report воспроизводимый фрагмент диагностики.

Logcat содержит много фонового шума. Главный навык тестировщика — не читать всё подряд, а ограничивать вывод package, process, tag, level и временем воспроизведения.

## Key Points

- Logcat доступен в Android Studio и через команду `adb logcat`.
- Запись содержит timestamp, process ID, thread ID, tag, package, priority и message.
- Основные уровни: `VERBOSE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, `ASSERT`.
- Фильтр `level:ERROR` в Android Studio показывает этот и более серьёзные уровни.
- `is:crash` ищет application crashes, а `is:stacktrace` — Java-like stack traces.
- После перезапуска process его PID меняется, поэтому фильтр только по PID может потерять новые сообщения.
- Логи могут содержать tokens, personal data и внутреннюю информацию. Перед отправкой их необходимо проверить.

## Notes

## Что содержит строка Logcat

Пример:

```text
2026-06-11 14:25:10.412 18420-18471 NetworkClient com.example.app E Request failed
```

| Field | Meaning |
| --- | --- |
| Date and time | Когда записано сообщение |
| PID | ID процесса |
| TID | ID потока |
| Tag | Источник или категория сообщения |
| Package | Приложение, создавшее запись |
| Priority | Severity сообщения |
| Message | Текст события или ошибки |

Для анализа дефекта особенно важны timestamp, package, tag, exception type, первая строка причины и блок `Caused by`.

## Уровни логирования

| Level | Letter | Typical meaning |
| --- | --- | --- |
| Verbose | `V` | Максимально подробная диагностика |
| Debug | `D` | Информация для разработки и отладки |
| Info | `I` | Нормальные значимые события |
| Warn | `W` | Подозрительное состояние без немедленного failure |
| Error | `E` | Ошибка операции или компонента |
| Assert | `A` | Критическое условие; часто отображается как fatal |

Severity не гарантирует наличие дефекта. Некоторые приложения пишут ожидаемые ситуации как `ERROR`, а важная причина может находиться в предыдущих строках `INFO` или `WARN`.

## Logcat в Android Studio

1. Запустите приложение на physical device или emulator.
2. Откройте `View > Tool Windows > Logcat`.
3. Выберите правильное устройство.
4. Выберите process или задайте query.
5. Очистите текущий вывод при необходимости.
6. Воспроизведите дефект.
7. Поставьте поток на pause и изучите сообщения вокруг timestamp.

Toolbar позволяет:

- перейти к последней строке;
- очистить отображаемый output;
- поставить поток на pause;
- перезапустить Logcat;
- изменить формат;
- создать несколько tabs или split panels.

Несколько панелей удобны, чтобы одновременно видеть логи приложения и отдельный фильтр по network, database или errors.

## Query Language в Android Studio

Основные ключи:

| Key | Filters by |
| --- | --- |
| `package` | Package name |
| `process` | Process name |
| `tag` | Log tag |
| `message` | Message text |
| `level` | Выбранный и более высокий severity |
| `age` | Возраст записи |
| `is` | Специальный тип события |

Полезные примеры:

```text
package:mine
package:com.example.app level:WARN
package:com.example.app age:5m
is:crash
is:stacktrace
tag:OkHttp
message:"permission denied"
-tag:NoiseTag
tag~:Network.*
```

`package:mine` соответствует packages открытого Android Studio project.

### Логические операторы

```text
(tag:Network | tag:OkHttp) & package:com.example.app
(is:crash | level:ERROR) & age:10m
package:com.example.app & -tag:Analytics
```

- `&` означает AND;
- `|` означает OR;
- parentheses задают порядок;
- `-` перед key исключает совпадения;
- `~` после key включает regular expression.

Используйте parentheses в сложных запросах: без них operator precedence может дать неожиданный результат.

### Фильтр по времени

```text
age:30s
age:5m
age:3h
age:1d
```

`age` сравнивается со временем host computer. Неправильные часы устройства или компьютера затрудняют сопоставление событий, поэтому фиксируйте timezone и проверяйте time synchronization.

## Logcat через ADB

### Базовые команды

```bash
# Поток логов в реальном времени
adb logcat

# Очистить log buffers
adb logcat -c

# Вывести накопленные сообщения и завершить команду
adb logcat -d

# Показать справку доступной версии Platform Tools
adb logcat --help
```

Если подключено несколько устройств, укажите serial:

```bash
adb devices
adb -s DEVICE_SERIAL logcat
```

### Сохранение лога

PowerShell:

```powershell
adb logcat -c
adb logcat -v threadtime > android-logcat.txt
```

Остановите запись с помощью `Ctrl+C` сразу после воспроизведения.

Для короткого накопленного снимка:

```powershell
adb logcat -d -v threadtime > android-logcat.txt
```

Формат `threadtime` сохраняет date/time, PID, TID, priority, tag и message, поэтому удобен для bug report.

### Фильтрация

```bash
# Только Error и выше для всех tags
adb logcat "*:E"

# Конкретный tag от Debug, остальные сообщения скрыты
adb logcat MyAppTag:D "*:S"

# Логи определённого PID, если опция поддерживается Platform Tools
adb logcat --pid=18420
```

В PowerShell filter expressions со `*` лучше заключать в quotes.

PID-фильтр полезен только пока process жив. После crash или restart найдите новый PID либо используйте package-aware Android Studio filter.

## Практический workflow для дефекта

1. Запишите device model, Android version и application build.
2. Синхронизируйте часы или отметьте разницу времени.
3. Подключите устройство и проверьте `adb devices`.
4. Очистите буфер командой `adb logcat -c`.
5. Начните запись в файл.
6. Воспроизведите дефект минимальным числом шагов.
7. Отметьте точное время последнего действия.
8. Остановите запись сразу после результата.
9. Найдите package, crash, exception, `Caused by`, `ANR`, `FATAL EXCEPTION` или relevant tag.
10. Удалите лишний шум и проверьте файл на sensitive data.
11. Приложите лог вместе со steps, video и test environment.

Короткий лог вокруг одного воспроизведения обычно полезнее, чем огромный файл за весь рабочий день.

## Как анализировать crash

Ищите:

```text
FATAL EXCEPTION
AndroidRuntime
Caused by:
Process: com.example.app
```

Порядок анализа:

1. Найдите начало crash block.
2. Проверьте package и process.
3. Прочитайте exception type и message.
4. Найдите первую строку stack trace из application package.
5. Просмотрите предыдущие события: network response, permission denial, database operation или lifecycle transition.
6. Сопоставьте timestamp с действиями пользователя.

Первая строка с `Error` не всегда является root cause. Причина часто находится ниже после `Caused by` или выше, перед stack trace.

## Типичные сценарии QA

### Приложение закрывается

- Используйте `is:crash` или ищите `FATAL EXCEPTION`.
- Проверьте, был ли restart process.
- Сохраните полный stack trace, не только одну красную строку.

### Кнопка ничего не делает

- Фильтруйте package и время последнего нажатия.
- Ищите permission errors, invalid state, failed request и navigation exceptions.
- Отсутствие логов само по себе не доказывает, что handler не вызван.

### Данные не загружаются

- Ищите network/client tags, status codes, timeout, DNS, TLS и parsing errors.
- Не публикуйте authorization headers или response bodies с пользовательскими данными.
- Сопоставьте client timestamp с server logs, если они доступны.

### Проблема после background/rotation

- Ищите process restart, Activity/Fragment lifecycle, state restoration и database errors.
- Помните, что rotation, process death и обычный background — разные события.

## Ограничения

- Release build может удалять или ограничивать debug logs.
- Android restricts access к сообщениям других applications.
- Circular buffers перезаписывают старые записи.
- High-volume logging быстро создаёт шум и большие файлы.
- Лог может описывать симптом, но не доказывать root cause.
- OEM firmware добавляет собственные services и tags.
- Очистка Logcat не очищает application data и не перезапускает process.

## Безопасность логов

Перед отправкой проверьте наличие:

- access и refresh tokens;
- passwords, PIN и one-time codes;
- email, phone, address и account IDs;
- precise location;
- request/response bodies;
- cookies и authorization headers;
- device identifiers;
- internal URLs и infrastructure details.

Если sensitive data регулярно попадает в production logs, это отдельный security/privacy defect.

Не редактируйте строки так, чтобы потерялись timestamp, tag, exception hierarchy или важная последовательность событий. Лучше удалить нерелевантные блоки и отметить, что файл был sanitized.

## Что приложить к bug report

- короткий Logcat fragment или полный файл воспроизведения;
- точный timestamp и timezone;
- package name и app build;
- device model и Android version;
- debug или release build type;
- steps to reproduce;
- expected и actual result;
- screenshot или screen recording;
- используемый query/filter;
- сведения о нестандартных Developer options.

## Interview Focus

1. Что такое Logcat и какие сообщения он показывает?
2. Какие поля содержит log entry?
3. Чем `ERROR` отличается от `FATAL EXCEPTION`?
4. Как отфильтровать логи по package, level и времени?
5. Зачем очищать буфер перед воспроизведением?
6. Почему PID-фильтр может перестать работать после crash?
7. Какие sensitive data нельзя без проверки отправлять в логах?

## Sources

- [View logs with Logcat](https://developer.android.com/studio/debug/logcat)
- [Logcat command-line tool](https://developer.android.com/tools/logcat)

