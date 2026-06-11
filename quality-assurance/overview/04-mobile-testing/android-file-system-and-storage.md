# Файловая система и хранение данных в Android

Source: Android Developers "Data and file storage overview"  
Date added: 2026-06-11  
Related plan item: Mobile Testing  
Tags: QA, mobile testing, Android, storage, scoped storage, MediaStore, Room  
Language: Russian  
Translation pair: quality-assurance-en/overview/04-mobile-testing/android-file-system-and-storage.md

## Summary

Android предлагает несколько способов хранить данные:

- app-specific files во внутреннем или внешнем storage;
- shared media and documents;
- key-value preferences;
- local databases.

Правильный вариант зависит от privacy, persistence, size, sharing and availability requirements. Для QA важно понимать не конкретный hard-coded path, а data lifecycle, permissions, Android version and target SDK behavior.

Главная мысль:

> Private application data, shared user files, cache and structured records имеют разный lifecycle и должны тестироваться по-разному.

## Key Points

- Internal app-specific storage приватно для application и всегда доступно.
- External storage не обязательно означает removable SD card.
- App-specific files обычно удаляются при uninstall.
- Shared media and documents могут оставаться после uninstall.
- Scoped storage ограничивает доступ applications к shared storage.
- `MediaStore` используется для shared images, video and audio.
- Storage Access Framework предоставляет user-controlled access к documents.
- Preferences подходят для небольших key-value settings.
- Room/SQLite используются для structured local data.
- Storage permissions зависят от OS version and target SDK.

## Notes

## Storage Categories

| Category | Typical use | Shared with other apps | Removed on uninstall |
| --- | --- | --- | --- |
| Internal app-specific files | Private persistent app files | No | Yes |
| Internal cache | Re-creatable temporary data | No | Yes or earlier |
| External app-specific files | Larger app-only files | Normally no | Yes |
| Shared media | Photos, video and audio | Yes, under platform rules | No |
| Shared documents | User-selected documents and downloads | Through system picker | No |
| Preferences | Small private key-value data | No | Yes |
| Database | Structured private data | No by default | Yes |

Application behavior and backup configuration can introduce exceptions, so verify product requirements.

## Internal Storage

Internal storage contains directories private to application.

Typical APIs:

- `filesDir` / `getFilesDir()`;
- `cacheDir` / `getCacheDir()`.

Advantages:

- always available;
- no storage permission required;
- isolated from other regular applications;
- suitable for sensitive app-specific data.

QA checks:

- data persists after application restart;
- account switching does not leak files;
- logout removes required private data;
- update preserves or migrates files;
- uninstall removes app-specific data as expected;
- no sensitive content appears in logs or exported files.

## Internal Persistent Files

Use internal files for data that application needs reliably and that should not be shared directly.

Examples:

- internal configuration;
- downloaded private content;
- serialized application state;
- supporting data not represented in database.

QA scenarios:

- missing file;
- corrupted file;
- old file format after update;
- partial write;
- process killed during save;
- low storage;
- duplicate account data;
- backup and restore.

## Internal Cache

Cache contains re-creatable data. Android may remove it when storage is low, and application should also manage its own cache.

Examples:

- thumbnails;
- API response cache;
- temporary media;
- intermediate processing output.

QA principle:

> Removing cache may affect speed or offline convenience, but must not destroy irreplaceable user data.

Test:

- clear cache through system settings;
- delete individual cache files;
- relaunch application;
- stale cache after server changes;
- corrupted cache;
- cache growth;
- low-storage eviction;
- cleanup after failed operation.

## External Storage

Android terminology can be confusing:

- **internal storage** is private application storage on the device;
- **external storage** is a shared or separately managed storage volume and may be built-in or removable.

Do not assume `/sdcard` is a physical SD card, and do not rely on hard-coded paths.

External storage can become unavailable or read-only. App-critical files should not depend on removable storage.

QA scenarios:

- volume mounted and unmounted;
- read-only state;
- SD card removal where supported;
- multiple external volumes;
- insufficient free space;
- file disappears while application runs;
- retry after storage becomes available.

## External App-Specific Storage

Application can use dedicated external directories through APIs such as:

- `getExternalFilesDir()`;
- `getExternalCacheDir()`.

On supported Android versions these app-specific directories do not require broad storage permission. Their files are removed on uninstall.

Good for:

- large app-only downloads;
- replaceable media used inside application;
- external cache.

Risks:

- storage unavailable;
- user or system removes files;
- application assumes a fixed path;
- data is incorrectly treated as shared;
- critical startup data is placed on removable volume.

## Shared Storage

Shared storage is intended for user content that should remain accessible outside application.

Examples:

- photos;
- videos;
- music;
- exported reports;
- documents;
- downloaded files.

Shared files often remain after uninstall because they belong to user rather than application.

QA checks:

- file visible to expected applications;
- filename and metadata;
- duplicate export;
- overwrite behavior;
- uninstall does not remove user-owned content unexpectedly;
- delete permission and confirmation;
- access after permission changes;
- privacy of files not intended for sharing.

## MediaStore

`MediaStore` is the Android API for shared media collections.

Typical types:

- images;
- video;
- audio;
- downloads.

QA scenarios:

- create and read media;
- correct album/location;
- metadata and MIME type;
- duplicate filename;
- edit or delete media created by application;
- access media created by another application;
- user revokes media access;
- selected photos only;
- item removed outside application;
- gallery refresh.

For modern Android versions, privacy-preserving Photo Picker is often preferable when application only needs user-selected images or videos.

## Storage Access Framework

Storage Access Framework (SAF) uses system UI to let user choose a document or directory.

Common actions:

- open document;
- create document;
- select directory;
- persist access to selected URI when supported.

Advantages:

- user controls which files application can access;
- no broad filesystem permission for normal use cases;
- works with local and cloud document providers.

QA scenarios:

- cancel picker;
- choose unsupported file;
- choose cloud file while offline;
- provider unavailable;
- selected file renamed or deleted;
- persisted access after restart;
- access revoked;
- duplicate save;
- read-only document;
- large document;
- unusual provider.

## Preferences

Preferences store small primitive or simple key-value data.

Examples:

- theme;
- onboarding state;
- selected language;
- basic feature settings.

Do not treat normal preferences as secure storage for:

- passwords;
- tokens;
- payment data;
- large or relational datasets.

QA checks:

- default values;
- persistence after restart;
- reset settings;
- update compatibility;
- separate state per account;
- no secret exposure;
- restore behavior.

## Databases

Android applications commonly use SQLite through Room for structured local data.

Examples:

- offline records;
- message history;
- product catalog;
- queued operations;
- relational application state.

QA scenarios:

- schema migration;
- downgrade if supported;
- corrupted database;
- transaction rollback;
- duplicate rows;
- concurrency;
- large dataset;
- account logout cleanup;
- offline-to-online synchronization;
- interrupted migration;
- backup and restore.

## Scoped Storage

Scoped storage limits direct access to shared storage and other applications' files.

Application generally works with:

- its own app-specific directories;
- media through `MediaStore`;
- user-selected documents through SAF;
- special broad access only for approved core use cases.

QA should test combinations of:

- Android OS version;
- application target SDK;
- fresh install versus upgrade;
- permission state;
- files created before and after migration;
- legacy application data.

## Storage Permissions

Storage permission behavior changed across Android releases.

### Legacy Android

Older versions used:

- `READ_EXTERNAL_STORAGE`;
- `WRITE_EXTERNAL_STORAGE`.

These permissions should not be assumed to provide the same access on modern Android.

### Modern Media Permissions

For access to media created by other applications, modern Android versions may use granular permissions:

- `READ_MEDIA_IMAGES`;
- `READ_MEDIA_VIDEO`;
- `READ_MEDIA_AUDIO`.

Application may instead use Photo Picker for user-selected visual media.

QA scenarios:

- allow full access;
- allow selected photos/videos where supported;
- deny;
- revoke in settings;
- add newly selected media;
- application update from legacy permission model;
- repeated permission request;
- feature fallback without permission.

### All Files Access

`MANAGE_EXTERNAL_STORAGE` provides broad access intended only for limited core use cases such as file managers, backup applications and similar tools.

It is subject to platform and Google Play restrictions.

QA should verify:

- feature truly requires broad access;
- behavior without access;
- settings flow;
- policy-compliant user explanation;
- no access beyond business need;
- app remains usable with privacy-friendly alternatives where possible.

## Permission Test Matrix

| State | Expected checks |
| --- | --- |
| Not requested | Feature explains why access is needed at the right time |
| Allowed | Only required data becomes available |
| Denied | Clear fallback; no crash or endless loader |
| Denied repeatedly | Application respects platform behavior and offers settings when appropriate |
| Revoked in settings | Application detects loss of access |
| Partial media access | Only selected items are visible |
| OS upgrade | Existing grants and behavior migrate safely |
| App target SDK update | Storage behavior remains compatible |

## Installation, Update And Uninstall

### Fresh Install

- app-specific directories start clean;
- defaults are correct;
- no another-user data;
- permission is requested only when feature needs it.

### Update

- database and files migrate;
- legacy external paths remain accessible or migrate;
- scoped storage changes do not lose data;
- cached files can be recreated;
- permissions are re-evaluated correctly.

### Uninstall

- app-specific internal and external files are removed;
- shared user files remain when expected;
- server-side data follows account requirements;
- reinstall starts with expected state;
- auto-backup restore is considered.

## Low Storage Testing

Test:

- download with little free space;
- database write failure;
- camera/media save;
- export to shared storage;
- partial file cleanup;
- cache eviction;
- retry after freeing space;
- application launch at storage limit;
- clear and actionable error message.

No operation should silently corrupt persistent user data.

## Inspecting Files

Tools:

- Android Studio Device Explorer;
- Device File Explorer;
- `adb shell`;
- `run-as` for debuggable applications where allowed;
- application logs;
- system file picker;
- emulator snapshots and test data.

Access differs between debug/release builds and rooted/non-rooted devices.

Useful commands:

```bash
adb shell df -h
adb shell pm clear com.example.app
adb shell appops get com.example.app
```

Do not expose production personal data or secrets while collecting evidence.

## Common Defects

- private file saved in shared storage;
- cache contains irreplaceable user data;
- logout leaves previous account database;
- application crashes after cache is cleared;
- hard-coded `/sdcard` path fails on another device;
- SD card removal causes endless loading;
- exported file disappears on uninstall unexpectedly;
- shared file is deleted without user confirmation;
- scoped storage migration loses downloads;
- denied media permission causes blank screen;
- application sees all photos when only selected access was granted;
- update cannot read legacy files;
- low storage leaves corrupted database or partial media;
- `MANAGE_EXTERNAL_STORAGE` requested without justified functionality.

## Bug Report Tips

Include:

- build and package name;
- Android version and API level;
- target SDK if known;
- device and manufacturer;
- storage type and available space;
- file type and size;
- permission state;
- fresh install or upgrade;
- URI/path category without sensitive data;
- app state and account;
- logs and screenshots;
- expected persistence after uninstall/update.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Internal storage | Private and reliably available application storage. |
| External storage | Storage volume that may be shared, emulated or removable. |
| App-specific storage | Directories intended only for one application. |
| Shared storage | User content accessible through platform sharing APIs. |
| Scoped storage | Privacy model limiting direct access to shared files. |
| MediaStore | Android API for shared media collections. |
| SAF | Storage Access Framework for user-selected documents. |
| Preferences | Small key-value application settings. |
| Room | Jetpack persistence layer over SQLite. |
| URI | Identifier used to access content through Android providers. |

## Questions

### 1. Где хранить sensitive app-specific data?

Answer: Обычно во внутреннем app-specific storage или другом подходящем private secure storage.

### 2. Удаляются ли shared files при uninstall?

Answer: Обычно нет, поскольку они считаются user-owned content.

### 3. Может ли application полагаться на cache?

Answer: Нет. Cache может быть очищен system or user и должен восстанавливаться.

### 4. Что такое scoped storage?

Answer: Privacy model, ограничивающая прямой доступ application к shared storage and files других apps.

### 5. Когда используется Storage Access Framework?

Answer: Когда user должен выбрать document or directory через system picker без broad filesystem access.

### 6. Почему storage testing требует version matrix?

Answer: Permissions and storage behavior зависят от Android version, target SDK and migration path.

## What To Review Later

- Android scoped storage.
- MediaStore and Photo Picker.
- Storage Access Framework.
- Room database migrations.
- Android permissions by API level.
- Backup, restore and uninstall behavior.

## Sources

- [Android data and file storage overview](https://developer.android.com/training/data-storage)
- [App-specific storage](https://developer.android.com/training/data-storage/app-specific)
- [Shared media storage](https://developer.android.com/training/data-storage/shared/media)
- [All files access](https://developer.android.com/training/data-storage/manage-all-files)
