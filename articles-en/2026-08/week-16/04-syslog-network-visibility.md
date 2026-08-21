# Syslog Network Visibility

Source: closed course page  
Date added: 2026-08-21  
Related plan item: Week 16 / Syslog network visibility  
Tags: syslog, logging, monitoring, centralized logging, troubleshooting, severity, UDP 514
Language: English
Translation pair: articles/2026-08/week-16/04-syslog-network-visibility.md

## Summary

- `SNMP` shows metrics, while `syslog` shows events.
- `syslog` is the message stream from network devices about what is happening.
- A message usually includes a category, severity level, and event text.
- Severity levels run from `0` to `7`: emergency through debug.
- Local logs are useful, but not enough.
- Centralized `syslog` preserves history and helps correlate events across devices.
- Basic Cisco configuration is simple: point the device at a server with `logging`.

## Key Points

- `syslog` provides context that metrics alone cannot provide.
- Cisco `syslog` messages often appear directly in the console during configuration.
- A local log buffer can be lost after a reboot.
- Checking logs one device at a time does not scale.
- A `syslog` server collects messages in one place where they can be searched, stored, and correlated.
- By default, `syslog` uses `UDP 514`.
- The best test is to create a real event, such as an interface state change.

## Notes

After configuring `SNMP`, it may feel like visibility is complete.

It is not.

`SNMP` and `syslog` answer different questions.

`SNMP` says:

```text
How is the device doing?
```

`syslog` says:

```text
What just happened?
```

That distinction matters. Metrics show state. Logs show events.

## What Syslog Shows

`syslog` is how a device speaks out loud.

Example messages:

- an interface went down;
- an interface came up;
- a user logged in;
- authentication failed;
- configuration changed;
- a device reloaded;
- a routing neighbor disappeared;
- a hardware error occurred.

If you have ever configured a Cisco device and seen a message suddenly appear in the console while typing, that was `syslog`.

It was already in front of you. Now it has a name and a clear role.

## What A Message Contains

A `syslog` message usually provides several important pieces:

- source or category;
- severity level;
- timestamp;
- device hostname;
- message text.

The category helps identify which part of the device generated the message.

The severity helps you quickly judge urgency.

The text explains what happened.

## Severity Levels

`syslog` has eight severity levels.

| Level | Name | Meaning |
| --- | --- | --- |
| `0` | Emergency | System is unusable. |
| `1` | Alert | Immediate action is needed. |
| `2` | Critical | Critical condition. |
| `3` | Error | Error condition. |
| `4` | Warning | Warning condition. |
| `5` | Notice | Significant but not emergency event. |
| `6` | Informational | Informational message. |
| `7` | Debug | Detailed troubleshooting output. |

The lower the number, the more serious the event.

If you see level `3`, that is an error. If you see level `7`, it may be detailed diagnostic noise.

## SNMP And Syslog Together

`SNMP` and `syslog` do not replace each other.

They complete the picture:

| Tool | What It Provides |
| --- | --- |
| `SNMP` | Metrics, state, graphs, thresholds. |
| `syslog` | Events, causes, sequence of actions. |

Example:

1. `SNMP` shows that an interface became unavailable.
2. `syslog` shows an interface state change message.
3. Timestamps show when it began.
4. Nearby authentication, reload, or configuration messages may provide context.

`SNMP` shows the pulse. `syslog` tells the story.

## Why Local Logs Are Not Enough

On a Cisco device, logs can be viewed locally.

Useful commands:

```text
show logging
show log
```

That is helpful for quick troubleshooting.

But there are problems:

- local logs are often stored in memory;
- after a reboot, some history may disappear;
- the buffer size is limited;
- manually checking dozens of devices is inefficient;
- correlating events across routers, switches, and servers is difficult.

For one lab device, local logs may be enough. For a real network, they are not.

## Centralized Syslog

The better approach is to send logs to a separate server.

This is called off-box logging: messages leave the device and are stored somewhere else.

The server could be:

- a Synology with Log Center;
- a Windows Server with suitable software;
- a Linux server;
- Splunk;
- Graylog;
- another logging platform.

The main idea:

```text
All devices send messages to one place.
```

There, messages can be searched, filtered, stored, archived, and correlated.

## Basic Cisco Configuration

On the Cisco side, the basic configuration is simple.

In global configuration mode, define the server address:

```text
logging <syslog-server-ip>
```

By default, `syslog` uses `UDP 514`.

Then verify the state:

```text
show logging
```

Real devices provide additional options:

- which severity level to send;
- which facility to use;
- where to send messages;
- how to handle timestamps;
- whether secure transport is needed;
- which messages should appear on the console.

But the core idea remains simple: define the server and send logs to it.

## How To Verify

The best verification is to create a real event.

For example, bring up an unused interface:

```text
interface g0/1
no shutdown
```

Or change the state of a test interface.

After that, the `syslog` server should receive an event with:

- time;
- device hostname;
- severity level;
- message text;
- interface state change.

That confirms not only the router configuration, but the whole delivery path.

## NetworkChuck Coffee Scenario

At NetworkChuck Coffee, guest Wi-Fi fails during the morning rush.

Without centralized logs, you have to log into each device:

- access point;
- access switch;
- router;
- firewall;
- servers.

That is slow.

With centralized `syslog`, you can open one place and see:

- the access point rebooted;
- the switch interface started flapping;
- authentication failures occurred;
- the router sent a warning;
- someone changed configuration.

One log entry can be interesting. A chain of entries from different systems tells the truth.

## Practical Tip

Do not wait for an outage to enable centralized logging.

If a device reboots, fails, or is compromised, local logs may disappear with it.

A `syslog` server preserves history.

History matters for:

- unstable interfaces;
- rare problems that appear once a week;
- login investigations;
- configuration change analysis;
- reload investigations;
- security event investigations.

## Main Takeaway

`syslog` is the standard way devices report what is happening.

`SNMP` gives metrics and state. `syslog` gives events and context.

Local logs are useful, but a centralized log server changes everything: history, search, correlation, and visibility across the whole network.

## Commands And Terms

| Term | Meaning |
| --- | --- |
| `syslog` | Standard for sending event messages from devices. |
| `logging <ip>` | Cisco command used to send logs to a server. |
| `show logging` | Command used to check local and remote logging state. |
| `UDP 514` | Default transport and port for `syslog`. |
| severity | Message importance level. |
| facility | Message category or source. |
| off-box logging | Storing logs outside the device itself. |
| centralized logging | Collecting logs in one central location. |
| buffer | Memory area where a device temporarily stores logs. |
| timestamp | Time marker in a message. |

## Questions

### 1. How is syslog different from SNMP?

Answer: `SNMP` shows metrics and state, while `syslog` shows events and device messages.

### 2. Why are local logs not enough?

Answer: They can disappear after a reboot, have limited size, and are inefficient for analyzing a large network.

### 3. What port does syslog usually use?

Answer: `UDP 514`.

### 4. Which command points a Cisco device to a syslog server?

Answer: `logging <syslog-server-ip>`.

### 5. Why is centralized syslog useful during investigations?

Answer: It stores events from different devices in one place and helps correlate them by time.

## Review Later

- The difference between `SNMP` and `syslog`.
- `syslog` severity levels.
- The `logging <ip>` command.
- Why local logs are unreliable as the only source.
- Why a centralized log server matters.
- Why timestamps matter for event correlation.
