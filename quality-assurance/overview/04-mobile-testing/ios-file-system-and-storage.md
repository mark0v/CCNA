# Файловая система и хранение данных в iOS

Source: Apple File System Programming Guide material  
Date added: 2026-06-11  
Related plan item: Mobile Testing  
Tags: QA, mobile testing, iOS, APFS, sandbox, storage, iCloud  
Language: Russian  
Translation pair: quality-assurance-en/overview/04-mobile-testing/ios-file-system-and-storage.md

## Summary

iOS использует APFS и изолирует каждое приложение в sandbox. Приложение не может свободно читать файловую систему устройства или containers других приложений. Его files распределяются между bundle, Documents, Library, Caches and temporary directories в зависимости от назначения и требований к persistence and backup.

Для QA важно проверять не физические paths, которые могут меняться, а ожидаемое lifecycle данных:

- сохраняются ли user documents;
- очищается ли temporary data;
- восстанавливается ли cache;
- переживают ли settings update;
- удаляются ли данные после uninstall;
- не попадают ли лишние files в iCloud backup;
- доступны ли protected files после блокировки устройства.

## Key Points

- APFS является основной файловой системой современных Apple platforms.
- iOS application работает внутри sandbox.
- App bundle подписан и доступен приложению только для чтения.
- `Documents` предназначен для user-generated content.
- `Library/Application Support` хранит внутренние persistent data.
- `Library/Caches` содержит восстанавливаемые cache files.
- `tmp` предназначен для временных files и может очищаться системой.
- Documents and Application Support обычно включаются в backup.
- Cache and temporary data нельзя считать гарантированно persistent.
- Sensitive files могут использовать iOS Data Protection.

## Notes

## APFS

**APFS** (Apple File System) используется в современных версиях iOS, macOS, watchOS and tvOS.

Для mobile QA важны его observable properties:

- application data сохраняется на storage;
- files имеют permissions and protection;
- system может очищать reclaimable data при нехватке места;
- app containers изолированы;
- data может участвовать в backup and restore.

QA обычно не тестирует internals APFS напрямую. Проверяется поведение product поверх filesystem.

## iOS Sandbox

При установке iOS создаёт для application собственные containers.

Основные:

- **bundle container** — executable and packaged resources;
- **data container** — user and application data;
- дополнительные containers, например iCloud or App Group, если предусмотрены entitlements.

Application обычно не имеет доступа к containers других apps. Доступ к Photos, Contacts, Files and other protected data происходит через system APIs and permissions.

QA checks:

- приложение не показывает чужие данные;
- denied permission обрабатывается корректно;
- imported file копируется или открывается согласно requirements;
- data sharing между extensions/apps работает только через разрешённый container;
- sensitive files не становятся публично доступными.

## App Bundle

Bundle содержит:

- executable;
- resources;
- images;
- localized strings;
- configuration packaged with the build.

Bundle подписан и read-only во время normal operation. Application не должно сохранять runtime data внутрь bundle.

QA risks:

- missing resource in release build;
- wrong localized file;
- configuration from another environment;
- resource filename case mismatch;
- application expects to modify bundled file;
- corrupted or incorrectly signed package.

## Data Container

Data container содержит directories с разным lifecycle.

| Directory | Purpose | Backup | May be purged |
| --- | --- | --- | --- |
| `Documents/` | User-created or user-visible files | Usually yes | Normally no |
| `Library/Application Support/` | Persistent internal app data | Usually yes | Normally no |
| `Library/Caches/` | Re-creatable cached data | No | Yes |
| `Library/Preferences/` | App preferences through system APIs | Usually yes | Normally no |
| `tmp/` | Short-lived temporary files | No | Yes |

Точное поведение зависит от implementation and platform rules.

## Documents

`Documents/` используется для files, которые создаёт, импортирует, редактирует или явно управляет user.

Examples:

- exported report;
- drawing;
- downloaded document intended for offline use;
- user project;
- editable text file.

QA checks:

- create, rename, edit and delete;
- duplicate filename;
- unsupported format;
- large file;
- low storage;
- app restart;
- device restart;
- backup and restore;
- Files app visibility, если она заявлена;
- correct behavior after account logout.

## Documents/Inbox

Inbox используется для files, переданных приложению внешним source.

Application может читать and move imported file, но не должно редактировать его на месте как обычный working document.

QA scenarios:

- Open in/Share to application;
- duplicate import;
- invalid extension;
- content does not match extension;
- file with long or Unicode name;
- import while app is closed;
- import without enough storage;
- source file is removed after transfer.

## Library/Application Support

Application Support предназначен для persistent files, необходимых application, но не предназначенных для прямого управления user.

Examples:

- local database;
- downloaded templates;
- internal configuration;
- persistent indexes;
- app-managed content.

QA checks:

- migration after update;
- corrupted local database;
- missing file recovery;
- logout cleanup;
- account switching;
- restore from backup;
- consistency with server;
- no user-facing files are hidden there incorrectly.

## Library/Caches

Cache повышает performance, но application должно работать и без него.

Examples:

- downloaded thumbnails;
- API response cache;
- temporary media;
- derived database indexes.

System может удалить cached files при нехватке storage.

QA scenarios:

- clear cache;
- launch after cache removal;
- stale cache after server update;
- offline behavior;
- corrupted cache;
- repeated download;
- cache size growth;
- low disk space.

Expected principle:

> Deleting cache may make the app slower temporarily, but should not destroy user data or permanently break functionality.

## Temporary Directory

`tmp/` используется для short-lived data.

Examples:

- intermediate export file;
- temporary upload;
- image processing result;
- downloaded file before validation.

Application не должно полагаться на сохранность tmp between launches. Оно также должно удалять files, когда они больше не нужны.

QA checks:

- interrupted upload/export;
- app termination during temporary operation;
- repeated operations do not fill storage;
- cleanup after success and failure;
- relaunch after system removes temporary files.

## Preferences

Preferences должны храниться через platform APIs such as `UserDefaults`, а не через вручную созданные files в Preferences directory.

Подходят для:

- selected theme;
- onboarding flag;
- simple user settings;
- last selected option.

Не подходят для:

- passwords;
- access tokens;
- large datasets;
- critical database records.

QA checks:

- persistence after restart;
- behavior after update;
- reset settings;
- separate values for different accounts;
- secure storage for secrets;
- correct default values after fresh install.

## Backup And Restore

Persistent user data обычно может попадать в iCloud/device backup. Re-downloadable cache and large media should not unnecessarily increase backup size.

QA should verify:

- critical data restores correctly;
- cache is not treated as irreplaceable data;
- restored application handles newer server state;
- no duplicate data after restore;
- account authentication is handled safely;
- application does not back up prohibited or excessive files.

Backup behavior should be confirmed against current product and Apple requirements.

## iCloud Containers

iCloud containers позволяют synchronise documents or application data across user devices.

Possible risks:

- sync conflict;
- delayed upload;
- same file changed on two devices;
- deleted file reappears;
- duplicate document;
- user signs out of iCloud;
- storage quota exceeded;
- offline changes merge incorrectly.

QA scenarios:

1. Create document on device A.
2. Wait for sync and open on device B.
3. Edit on both devices.
4. Check conflict handling.
5. Delete on one device.
6. Reconnect an offline device and inspect final state.

## File Types

Apple platforms identify content through file extensions and system type identifiers.

QA should test:

- supported and unsupported types;
- uppercase/lowercase extension;
- wrong extension with different content;
- missing extension;
- multiple dots in filename;
- Unicode filename;
- file association;
- preview and share behavior.

Do not assume extension alone proves that file content is valid.

## Data Protection And Encryption

iOS supports file protection classes that control when encrypted files are accessible.

Depending on configuration, a file may be unavailable while device is locked. This matters for background tasks.

QA scenarios:

- lock device during upload or processing;
- background execution with protected data;
- unlock and retry;
- reboot before first unlock;
- notification triggers background work;
- verify no sensitive content appears in logs or temporary files.

Sensitive values such as credentials and tokens usually belong in Keychain rather than ordinary files or preferences.

## Installation, Update And Uninstall

### Fresh Install

Check:

- default files and settings;
- no stale data from another account;
- initial storage footprint;
- directories are created when needed.

### Update

Check:

- documents remain available;
- database migration succeeds;
- cache schema changes safely;
- preferences remain compatible;
- interrupted migration can recover;
- storage footprint does not unexpectedly grow.

### Uninstall

App container is generally removed with the application, while external or synchronised data may remain according to platform and product behavior.

Check:

- reinstall state;
- Keychain persistence according to requirements;
- iCloud documents;
- shared containers;
- server-side account data;
- downloaded files exported outside app sandbox.

## Low Storage Testing

Insufficient storage can break download, database, camera, update and export flows.

Test:

- operation close to storage limit;
- partial file;
- clear error message;
- cleanup after failure;
- retry after freeing space;
- no corrupted user data;
- cache eviction;
- application launch with little free space.

## Inspecting Application Data

Available approaches depend on build, device and permissions:

- Xcode Devices and Simulators;
- simulator container;
- application logs;
- exported diagnostics;
- development/debug tools;
- Files app for explicitly shared documents.

On a normal non-jailbroken device, QA should not expect unrestricted access to the whole filesystem.

Never publish production personal data, tokens or secrets in screenshots and logs.

## Common Defects

- user document saved to cache and later disappears;
- cache deletion logs user out unexpectedly;
- application cannot launch when tmp file is missing;
- update corrupts local database;
- downloaded media is included in backup unnecessarily;
- imported file cannot be edited because it remains in Inbox;
- stale cache displays deleted server data;
- logout leaves another user's local files;
- app writes sensitive token to preferences;
- locked device causes background task to corrupt a file;
- low storage leaves an unusable partial download;
- reinstall unexpectedly restores or loses data.

## Bug Report Tips

Include:

- build version;
- device and iOS version;
- installation state: fresh, updated or restored;
- account;
- storage availability;
- file type and size;
- directory/lifecycle category if known;
- network and iCloud state;
- device lock state;
- steps and expected persistence;
- logs without sensitive data.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| APFS | Apple File System used by modern Apple platforms. |
| Sandbox | Isolated environment limiting application file access. |
| Bundle | Signed read-only package containing application code and resources. |
| Data container | Application-specific location for runtime data. |
| Documents | Persistent user-created or user-visible files. |
| Application Support | Persistent internal application data. |
| Caches | Re-creatable data that the system may purge. |
| tmp | Temporary data that must not be treated as persistent. |
| Data Protection | iOS encryption and accessibility rules for files. |
| Keychain | Secure storage intended for credentials and secrets. |

## Questions

### 1. Почему приложение не должно хранить runtime data в bundle?

Answer: Bundle подписан, read-only и предназначен для packaged application resources.

### 2. Где хранить user-generated document?

Answer: Обычно в Documents или в соответствующем user-visible document container.

### 3. Может ли приложение полагаться на сохранность cache?

Answer: Нет. System может удалить cache, поэтому application должно восстановить его.

### 4. Чем Application Support отличается от Caches?

Answer: Application Support хранит persistent internal data, а Caches — re-creatable data, которое может быть удалено.

### 5. Что важно проверить после update?

Answer: Documents, preferences, database migration, cache compatibility and recovery after interruption.

### 6. Почему lock state важен для file testing?

Answer: Protected encrypted files могут быть недоступны, пока device locked, особенно для background tasks.

## What To Review Later

- iOS sandbox and containers.
- Keychain and secure storage.
- iCloud sync conflict testing.
- Installation, update and migration testing.
- Low-storage scenarios.
- Android application storage for comparison.
