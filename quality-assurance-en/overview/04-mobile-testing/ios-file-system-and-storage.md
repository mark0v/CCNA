# iOS File System And Storage For QA

Source: Apple File System Programming Guide material  
Date added: 2026-06-11  
Related plan item: Mobile Testing  
Tags: QA, mobile testing, iOS, APFS, sandbox, storage, iCloud  
Language: English  
Translation pair: quality-assurance/overview/04-mobile-testing/ios-file-system-and-storage.md

## Summary

iOS uses APFS and isolates each application in a sandbox. An application cannot freely read the device file system or other application containers. Its files are distributed between the bundle, Documents, Library, Caches, and temporary directories according to their purpose, persistence, and backup requirements.

For QA, the important goal is not testing physical paths, which may change, but verifying the expected data lifecycle:

- whether user documents persist;
- whether temporary data is cleaned;
- whether cache can be rebuilt;
- whether settings survive an update;
- whether data is removed after uninstall;
- whether unnecessary files enter iCloud backup;
- whether protected files are available after device locking.

## Key Points

- APFS is the primary file system on modern Apple platforms.
- An iOS application runs inside a sandbox.
- The application bundle is signed and read-only.
- `Documents` stores user-generated content.
- `Library/Application Support` stores persistent internal data.
- `Library/Caches` stores re-creatable cache files.
- `tmp` stores temporary files and may be purged.
- Documents and Application Support are normally included in backup.
- Cache and temporary data are not guaranteed to persist.
- Sensitive files may use iOS Data Protection.

## Notes

## APFS

**APFS** (Apple File System) is used in modern iOS, macOS, watchOS, and tvOS versions.

Observable properties relevant to mobile QA include:

- application data persists on storage;
- files have permissions and protection;
- the system can remove reclaimable data when storage is low;
- application containers are isolated;
- data may participate in backup and restore.

QA normally tests product behavior on top of the file system rather than APFS internals.

## iOS Sandbox

During installation, iOS creates application-specific containers.

Main containers:

- **bundle container** - executable and packaged resources;
- **data container** - user and application data;
- additional containers such as iCloud or App Groups when enabled by entitlements.

An application normally cannot access other application containers. Photos, Contacts, Files, and other protected data are accessed through system APIs and permissions.

QA checks:

- application does not expose another user's data;
- denied permission is handled correctly;
- imported files are copied or opened according to requirements;
- extensions and related apps share data only through approved containers;
- sensitive files do not become publicly accessible.

## App Bundle

The bundle contains:

- executable;
- resources;
- images;
- localized strings;
- configuration packaged with the build.

It is signed and read-only during normal operation. Runtime data should not be saved inside it.

QA risks:

- missing resource in a release build;
- incorrect localized file;
- configuration from another environment;
- resource filename case mismatch;
- application attempts to modify a bundled file;
- corrupted or incorrectly signed package.

## Data Container

The data container contains directories with different lifecycles.

| Directory | Purpose | Backup | May be purged |
| --- | --- | --- | --- |
| `Documents/` | User-created or user-visible files | Usually yes | Normally no |
| `Library/Application Support/` | Persistent internal app data | Usually yes | Normally no |
| `Library/Caches/` | Re-creatable cached data | No | Yes |
| `Library/Preferences/` | App preferences through system APIs | Usually yes | Normally no |
| `tmp/` | Short-lived temporary files | No | Yes |

Exact behavior depends on implementation and current platform rules.

## Documents

`Documents/` is used for files that a user creates, imports, edits, or explicitly manages.

Examples:

- exported report;
- drawing;
- downloaded document intended for offline use;
- user project;
- editable text file.

QA checks:

- create, rename, edit, and delete;
- duplicate filename;
- unsupported format;
- large file;
- low storage;
- application restart;
- device restart;
- backup and restore;
- Files app visibility when supported;
- correct behavior after account logout.

## Documents/Inbox

Inbox is used for files passed to the application by an external source.

The application can read and move an imported file, but should not treat it as a normal editable working document in place.

QA scenarios:

- Open in/Share to application;
- duplicate import;
- invalid extension;
- content does not match extension;
- long or Unicode filename;
- import while application is closed;
- import without enough storage;
- source file is removed after transfer.

## Library/Application Support

Application Support stores persistent files required by the application but not directly managed by the user.

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

Cache improves performance, but the application must work without it.

Examples:

- downloaded thumbnails;
- API response cache;
- temporary media;
- derived database indexes.

The system may remove cached files when storage is low.

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

> Deleting cache may temporarily slow the application, but should not destroy user data or permanently break functionality.

## Temporary Directory

`tmp/` stores short-lived data.

Examples:

- intermediate export file;
- temporary upload;
- image processing result;
- downloaded file before validation.

The application must not rely on temporary data persisting between launches and should remove it when no longer needed.

QA checks:

- interrupted upload/export;
- application termination during a temporary operation;
- repeated operations do not fill storage;
- cleanup after success and failure;
- relaunch after the system removes temporary files.

## Preferences

Preferences should be stored through platform APIs such as `UserDefaults`, not by manually creating files in the Preferences directory.

Suitable data:

- selected theme;
- onboarding flag;
- simple user settings;
- last selected option.

Unsuitable data:

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
- correct default values after fresh installation.

## Backup And Restore

Persistent user data may be included in iCloud or device backup. Re-downloadable cache and large media should not unnecessarily increase backup size.

QA should verify:

- critical data restores correctly;
- cache is not treated as irreplaceable data;
- restored application handles newer server state;
- no duplicate data appears after restore;
- account authentication is handled safely;
- application does not back up prohibited or excessive files.

Backup behavior should be confirmed against current product and Apple requirements.

## iCloud Containers

iCloud containers synchronize documents or application data across user devices.

Possible risks:

- sync conflict;
- delayed upload;
- same file changed on two devices;
- deleted file reappears;
- duplicate document;
- user signs out of iCloud;
- storage quota exceeded;
- offline changes merge incorrectly.

QA scenario:

1. Create a document on device A.
2. Wait for sync and open it on device B.
3. Edit it on both devices.
4. Check conflict handling.
5. Delete it on one device.
6. Reconnect an offline device and inspect the final state.

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

Do not assume the extension alone proves that file content is valid.

## Data Protection And Encryption

iOS supports file protection classes that control when encrypted files are accessible.

Depending on configuration, a file may be unavailable while the device is locked. This matters for background tasks.

QA scenarios:

- lock device during upload or processing;
- background execution with protected data;
- unlock and retry;
- reboot before first unlock;
- notification triggers background work;
- verify no sensitive content appears in logs or temporary files.

Sensitive values such as credentials and tokens usually belong in Keychain rather than ordinary files or preferences.

## Installation, Update, And Uninstall

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

The application container is generally removed with the app, while external or synchronized data may remain according to platform and product behavior.

Check:

- reinstall state;
- Keychain persistence according to requirements;
- iCloud documents;
- shared containers;
- server-side account data;
- downloaded files exported outside the sandbox.

## Low Storage Testing

Insufficient storage can break download, database, camera, update, and export flows.

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

Available approaches depend on build, device, and permissions:

- Xcode Devices and Simulators;
- simulator container;
- application logs;
- exported diagnostics;
- development/debug tools;
- Files app for explicitly shared documents.

On a normal non-jailbroken device, QA should not expect unrestricted access to the whole file system.

Never publish production personal data, tokens, or secrets in screenshots and logs.

## Common Defects

- user document is saved to cache and later disappears;
- cache deletion logs the user out unexpectedly;
- application cannot launch when a temporary file is missing;
- update corrupts the local database;
- downloaded media is included in backup unnecessarily;
- imported file cannot be edited because it remains in Inbox;
- stale cache displays deleted server data;
- logout leaves another user's local files;
- application writes a sensitive token to preferences;
- locked device causes a background task to corrupt a file;
- low storage leaves an unusable partial download;
- reinstall unexpectedly restores or loses data.

## Bug Report Tips

Include:

- build version;
- device and iOS version;
- installation state: fresh, updated, or restored;
- account;
- available storage;
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

### 1. Why should an application not store runtime data in its bundle?

Answer: The bundle is signed, read-only, and intended for packaged application resources.

### 2. Where should a user-generated document be stored?

Answer: Usually in Documents or an appropriate user-visible document container.

### 3. Can an application rely on cache persistence?

Answer: No. The system may delete cache, so the application must be able to rebuild it.

### 4. How does Application Support differ from Caches?

Answer: Application Support stores persistent internal data, while Caches stores re-creatable data that may be deleted.

### 5. What is important after an update?

Answer: Documents, preferences, database migration, cache compatibility, and recovery after interruption.

### 6. Why does device lock state matter?

Answer: Protected encrypted files may be inaccessible while the device is locked, especially during background tasks.

## What To Review Later

- iOS sandbox and containers.
- Keychain and secure storage.
- iCloud sync conflict testing.
- Installation, update, and migration testing.
- Low-storage scenarios.
- Android application storage for comparison.
