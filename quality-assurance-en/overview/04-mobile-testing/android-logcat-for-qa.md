# Android Logcat For QA

Source: user-provided Android Developers material  
Date added: 2026-06-11  
Related plan item: Mobile Testing  
Tags: QA, mobile testing, Android, Logcat, ADB, logs, crash analysis  
Language: English  
Translation pair: quality-assurance/overview/04-mobile-testing/android-logcat-for-qa.md

## Summary

Logcat displays real-time messages from applications, Android system services, and the device. When an application crashes, the log normally includes the exception, an error reason, and a stack trace.

QA engineers use Logcat to:

- support a crash or ANR report with technical evidence;
- find HTTP, database, permission, and lifecycle errors;
- match a user action to an exact timestamp;
- distinguish UI defects from backend or device problems;
- attach a reproducible diagnostic fragment to a bug report.

Logcat contains a large amount of background noise. The essential skill is narrowing the output by package, process, tag, level, and reproduction time.

## Key Points

- Logcat is available in Android Studio and through `adb logcat`.
- An entry contains a timestamp, process ID, thread ID, tag, package, priority, and message.
- Common levels are `VERBOSE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, and `ASSERT`.
- `level:ERROR` in Android Studio matches that and higher-severity levels.
- `is:crash` finds application crashes and `is:stacktrace` finds Java-like stack traces.
- A process receives a new PID after restart, so a PID-only filter can miss subsequent messages.
- Logs can contain tokens, personal data, and internal information and must be reviewed before sharing.

## Notes

## Anatomy Of A Logcat Entry

Example:

```text
2026-06-11 14:25:10.412 18420-18471 NetworkClient com.example.app E Request failed
```

| Field | Meaning |
| --- | --- |
| Date and time | When the message was recorded |
| PID | Process ID |
| TID | Thread ID |
| Tag | Message source or category |
| Package | Application that produced the entry |
| Priority | Message severity |
| Message | Event or error text |

For defect analysis, pay particular attention to the timestamp, package, tag, exception type, first reason line, and `Caused by` blocks.

## Log Levels

| Level | Letter | Typical meaning |
| --- | --- | --- |
| Verbose | `V` | Most detailed diagnostics |
| Debug | `D` | Development and debugging information |
| Info | `I` | Normal significant events |
| Warn | `W` | Suspicious state without immediate failure |
| Error | `E` | Failed operation or component |
| Assert | `A` | Critical condition, often displayed as fatal |

Severity does not prove that a defect exists. Some applications log expected conditions as `ERROR`, while an important cause may appear in earlier `INFO` or `WARN` entries.

## Logcat In Android Studio

1. Run the application on a physical device or emulator.
2. Open `View > Tool Windows > Logcat`.
3. Select the correct device.
4. Select the process or enter a query.
5. Clear the current output if needed.
6. Reproduce the defect.
7. Pause the stream and inspect messages around the timestamp.

The toolbar can:

- scroll to the latest entry;
- clear displayed output;
- pause the stream;
- restart Logcat;
- change formatting;
- create multiple tabs or split panels.

Multiple panels are useful for viewing application logs alongside a separate network, database, or error filter.

## Android Studio Query Language

Primary keys:

| Key | Filters by |
| --- | --- |
| `package` | Package name |
| `process` | Process name |
| `tag` | Log tag |
| `message` | Message text |
| `level` | Selected and higher severity |
| `age` | Entry age |
| `is` | Special event type |

Useful examples:

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

`package:mine` matches packages in the open Android Studio project.

### Logical Operators

```text
(tag:Network | tag:OkHttp) & package:com.example.app
(is:crash | level:ERROR) & age:10m
package:com.example.app & -tag:Analytics
```

- `&` means AND;
- `|` means OR;
- parentheses control evaluation order;
- `-` before a key excludes matches;
- `~` after a key enables regular-expression matching.

Use parentheses in complex queries because operator precedence can otherwise produce an unexpected result.

### Time Filtering

```text
age:30s
age:5m
age:3h
age:1d
```

`age` is compared with the host computer timestamp. Incorrect device or host clocks can make correlation difficult, so record the timezone and verify time synchronization.

## Logcat Through ADB

### Basic Commands

```bash
# Stream logs in real time
adb logcat

# Clear log buffers
adb logcat -c

# Dump accumulated messages and exit
adb logcat -d

# Show help for the installed Platform Tools version
adb logcat --help
```

When several devices are connected, specify the serial:

```bash
adb devices
adb -s DEVICE_SERIAL logcat
```

### Saving A Log

PowerShell:

```powershell
adb logcat -c
adb logcat -v threadtime > android-logcat.txt
```

Stop recording with `Ctrl+C` immediately after reproducing the issue.

For a short accumulated snapshot:

```powershell
adb logcat -d -v threadtime > android-logcat.txt
```

The `threadtime` format preserves date/time, PID, TID, priority, tag, and message, making it useful for bug reports.

### Filtering

```bash
# Error and higher for all tags
adb logcat "*:E"

# One tag from Debug, suppress all other tags
adb logcat MyAppTag:D "*:S"

# One PID when supported by the installed Platform Tools
adb logcat --pid=18420
```

In PowerShell, quote filter expressions containing `*`.

A PID filter is useful only while the process remains alive. After a crash or restart, find the new PID or use a package-aware Android Studio filter.

## Practical Defect Workflow

1. Record the device model, Android version, and application build.
2. Synchronize clocks or note the time difference.
3. Connect the device and verify it with `adb devices`.
4. Clear the buffer with `adb logcat -c`.
5. Start recording to a file.
6. Reproduce the defect with the minimum number of steps.
7. Note the exact time of the final action.
8. Stop recording immediately after the result.
9. Search for the package, crash, exception, `Caused by`, `ANR`, `FATAL EXCEPTION`, or relevant tag.
10. Remove irrelevant noise and inspect the file for sensitive data.
11. Attach the log with steps, video, and test environment details.

A short log around one reproduction is usually more useful than a huge file covering an entire workday.

## Analyzing A Crash

Search for:

```text
FATAL EXCEPTION
AndroidRuntime
Caused by:
Process: com.example.app
```

Analysis order:

1. Find the start of the crash block.
2. Verify the package and process.
3. Read the exception type and message.
4. Find the first stack frame from the application package.
5. Inspect preceding events such as a network response, permission denial, database operation, or lifecycle transition.
6. Match the timestamp with the user action.

The first `Error` entry is not necessarily the root cause. The cause may appear later under `Caused by` or earlier before the stack trace.

## Common QA Scenarios

### Application Closes

- Use `is:crash` or search for `FATAL EXCEPTION`.
- Check whether the process restarted.
- Save the complete stack trace, not a single red line.

### A Button Does Nothing

- Filter by package and the time of the last tap.
- Search for permission errors, invalid state, failed requests, and navigation exceptions.
- Missing logs do not prove that the event handler was not called.

### Data Does Not Load

- Search network/client tags, status codes, timeouts, DNS, TLS, and parsing errors.
- Do not publish authorization headers or response bodies containing user data.
- Correlate the client timestamp with server logs when available.

### Failure After Background Or Rotation

- Search for process restart, Activity/Fragment lifecycle, state restoration, and database errors.
- Rotation, process death, and normal backgrounding are different events.

## Limitations

- A release build can remove or limit debug logs.
- Android restricts access to messages from other applications.
- Circular buffers overwrite old entries.
- High-volume logging creates noise and large files.
- A log can describe a symptom without proving the root cause.
- OEM firmware adds manufacturer-specific services and tags.
- Clearing Logcat does not clear application data or restart the process.

## Log Security

Before sharing, check for:

- access and refresh tokens;
- passwords, PINs, and one-time codes;
- email, phone, address, and account IDs;
- precise location;
- request and response bodies;
- cookies and authorization headers;
- device identifiers;
- internal URLs and infrastructure details.

Sensitive data in production logs is a separate security or privacy defect.

Do not edit entries in a way that removes timestamps, tags, exception hierarchy, or event order. Prefer deleting irrelevant blocks and note that the file was sanitized.

## What To Attach To A Bug Report

- a short Logcat fragment or the complete reproduction file;
- exact timestamp and timezone;
- package name and app build;
- device model and Android version;
- debug or release build type;
- steps to reproduce;
- expected and actual result;
- screenshot or screen recording;
- query or filter used;
- non-default Developer options.

## Interview Focus

1. What is Logcat and which messages does it display?
2. Which fields does a log entry contain?
3. How does an `ERROR` differ from a `FATAL EXCEPTION`?
4. How do you filter by package, level, and time?
5. Why clear the buffer before reproduction?
6. Why can a PID filter stop working after a crash?
7. Which sensitive data must be reviewed before sharing logs?

## Sources

- [View logs with Logcat](https://developer.android.com/studio/debug/logcat)
- [Logcat command-line tool](https://developer.android.com/tools/logcat)

