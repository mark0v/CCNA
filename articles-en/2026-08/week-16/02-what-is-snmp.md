# What Is SNMP

Source: closed course page  
Date added: 2026-08-21  
Related plan item: Week 16 / What is SNMP  
Tags: SNMP, OID, MIB, NMS, monitoring, SNMPv2c, SNMPv3, traps
Language: English
Translation pair: articles/2026-08/week-16/02-what-is-snmp.md

## Summary

- `SNMP` is a way to ask network devices questions and get values back.
- An `OID` is one specific measurable object on a device.
- A `MIB` is the catalog of `OID`s a device supports.
- An `NMS` polls devices, stores history, builds graphs, and sends alerts.
- `GET` reads data, `SET` can change values, and `TRAP` sends an event from a device to a server.
- `SNMPv2c` is common and simple, but its community string is sent in clear text.
- `SNMPv3` adds authentication and encryption.

## Key Points

- `SNMP` is not the magic in a pretty dashboard. It is a simple value-query mechanism.
- Many monitoring tools rely on `SNMP` to collect metrics from switches, routers, and access points.
- One `OID` is one data point: CPU, memory, interface utilization, uptime, temperature.
- A `MIB` tells a monitoring system what a device can report.
- Historical values are more useful than a single snapshot because they show trends and recurring problems.
- In real networks, `SNMP` should usually be read-only.
- If a device supports `SNMPv3`, it is usually the preferred option.

## Notes

`SNMP`, or `Simple Network Management Protocol`, can be explained very simply:

```text
Give me the value of this parameter.
```

Everything else - graphs, dashboards, reports, alerts, and monitoring screens - is built on top of that idea.

Monitoring looks complex when you see a finished tool like PRTG, Nagios, Zabbix, or SolarWinds. Under the hood, the basic pattern is often the same: a server asks a device for a value, the device answers, and the system stores the result.

## SNMP As A Question-And-Answer Engine

Imagine NetworkChuck Coffee.

There is a switch in the back office. During the morning rush, the network starts slowing down. Without monitoring, you have to guess:

- is the switch overloaded?
- is an uplink saturated?
- did an access point reboot?
- is CPU usage climbing?
- are there interface errors?

`SNMP` lets the monitoring system ask the device directly:

```text
What is your CPU usage right now?
How much traffic is crossing this interface?
How long have you been up since the last reboot?
Are there errors on this port?
```

The answers turn mystery into data.

## What An OID Is

An `OID`, or `Object Identifier`, is one specific value you can query on a device.

Examples of `OID`s:

- CPU usage;
- memory utilization;
- device uptime;
- interface status;
- interface speed;
- inbound traffic counter;
- outbound traffic counter;
- temperature;
- power status.

An `OID` is not all information about a device. It is one specific data point.

Simplified:

```text
OID = one measurable parameter.
```

## What A MIB Is

A `MIB`, or `Management Information Base`, is the catalog of values a device supports.

If an `OID` is one sensor, a `MIB` is the list of sensors available on the device.

A vendor may publish a `MIB` for its devices so monitoring software can understand:

- which values can be queried;
- what those values are called;
- what type of data will be returned;
- where vendor-specific values live.

This is especially useful for extended metrics: temperature, power supplies, fans, modules, and wireless-specific values.

## Why Monitoring Systems Exist

Technically, you can query `OID`s manually from a command line. But that stops making sense very quickly.

Manual querying has problems:

- there are many `OID`s;
- there are many devices;
- values must be checked regularly;
- history matters;
- thresholds and alerts matter;
- raw identifiers are hard for humans to read.

That is why we use an `NMS`, or `Network Management System`.

An `NMS` does the repetitive work:

- polls devices on a schedule;
- stores values;
- builds graphs;
- shows trends;
- compares values to thresholds;
- sends alerts;
- helps identify when a problem began.

History changes troubleshooting.

If NetworkChuck Coffee slows down every day at 7:15 a.m., a single check at 10:30 may show nothing. A week-long graph can reveal a recurring spike on one specific interface.

## GET, SET, And TRAP

`SNMP` has several operation types.

### GET

`GET` is the most common and safest option.

The monitoring system asks:

```text
Give me the value of this OID.
```

The device returns the value.

This is read access. For normal monitoring, it is usually enough.

### SET

`SET` can change a value on the device.

That is a different level of trust. If `GET` says "show me what is happening," `SET` says "let me change the device."

In real networks, `SNMP` is often configured as read-only because unnecessary write capability adds risk.

### TRAP

`TRAP` works differently.

The device sends a message to the monitoring server when an important event happens.

Examples:

- an interface goes down;
- a device reboots;
- a power supply fails;
- temperature crosses a threshold;
- a routing adjacency changes.

Polling and `TRAP`s complement each other. Polling gives regular metrics, while `TRAP`s help the system learn about events faster.

## SNMP Versions

The versions you will most often see in study and production are `SNMPv2c` and `SNMPv3`.

### SNMPv2c

`SNMPv2c` is popular because it is simple.

It uses a `community string`, which is the shared access string known by the device and the monitoring system.

The security problem is that the `community string` is sent in clear text. If someone captures that traffic, they may gain access to `SNMP` data.

Conceptually, it is like older insecure protocols: simple to use, but weakly protected.

### SNMPv3

`SNMPv3` adds what `SNMPv2c` lacks:

- authentication;
- encryption;
- better access control.

If `SNMPv2c` is closer to Telnet in its trust model, `SNMPv3` is closer to SSH: a little more work to configure, but much better for a modern environment.

If a device supports `SNMPv3`, use it when possible.

### SNMPv1

You may still find `SNMPv1` on old or very small devices.

It is not the best option, but real networks often include legacy equipment. If everything looks correct and monitoring still does not work, check which `SNMP` version the device supports.

## Why Read-Only Matters

For most monitoring tasks, read-only access is enough.

It reduces the risk of:

- accidental changes;
- bad automation;
- credential misuse;
- larger damage if credentials are compromised.

Monitoring should provide visibility. It should not receive permission to change infrastructure unless there is a clear reason.

Practical rule:

```text
If you only need visibility, use read-only.
```

## NetworkChuck Coffee Scenario

Guest Wi-Fi at NetworkChuck Coffee starts struggling when the line reaches the door.

Without `SNMP`, the complaint sounds like this:

```text
Wi-Fi is bad.
```

With `SNMP`, you can check:

- whether the access point is overloaded;
- whether the uplink is saturated;
- whether there are interface errors;
- whether a device rebooted;
- whether CPU usage is climbing;
- whether the problem repeats at the same time every day.

That is no longer an argument about opinions. It is work with data.

## Practical Tip

Do not treat `SNMP` as a fancy extra.

In real networks, it is one of the fastest ways to move from reactive panic to normal support. Start with basic values:

- uptime;
- CPU;
- memory;
- uplink status;
- interface utilization;
- interface errors;
- availability of critical devices.

Even that minimum makes a huge difference.

## Main Takeaway

`SNMP` is a way to ask devices for specific values.

An `OID` is one parameter. A `MIB` is the catalog of available parameters. An `NMS` regularly collects those values, stores history, builds graphs, and sends alerts.

The main value of `SNMP` is not the pretty dashboard. The value is that an engineer stops guessing and starts seeing facts.

## Commands And Terms

| Term | Meaning |
| --- | --- |
| `SNMP` | Simple Network Management Protocol, a protocol for querying data from network devices. |
| `OID` | Object Identifier, one specific measurable parameter. |
| `MIB` | Management Information Base, the catalog of available `OID`s. |
| `NMS` | Network Management System, a system for network management and monitoring. |
| `GET` | Operation that reads a value. |
| `SET` | Operation that changes a value. |
| `TRAP` | Message sent by a device to the monitoring server when an event occurs. |
| `community string` | Shared access string used in `SNMPv2c`. |
| `SNMPv2c` | Simple and common version, but without encrypted community strings. |
| `SNMPv3` | Version with authentication and encryption. |
| read-only | Access that permits reading but not changing values. |

## Questions

### 1. What does SNMP do?

Answer: It lets a system query a device for specific values such as CPU, uptime, or interface utilization.

### 2. What is an OID?

Answer: One specific measurable parameter on a device.

### 3. What is a MIB?

Answer: A catalog of `OID`s supported by a device.

### 4. How is GET different from SET?

Answer: `GET` reads a value, while `SET` can change a value on the device.

### 5. Why is SNMPv3 better than SNMPv2c?

Answer: `SNMPv3` supports authentication and encryption, while `SNMPv2c` sends the community string in clear text.

## Review Later

- The role of `SNMP` in monitoring.
- The difference between `OID` and `MIB`.
- The purpose of an `NMS`.
- `GET`, `SET`, and `TRAP` operations.
- Differences between `SNMPv2c` and `SNMPv3`.
- Why read-only access is safer for monitoring.
