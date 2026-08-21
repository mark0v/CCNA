# Network Automation Planes And SDN

Source: closed course page  
Date added: 2026-08-21  
Related plan item: Week 17 / Network automation planes and SDN  
Tags: network automation, SDN, management plane, control plane, data plane, Python, CAPWAP, OpenFlow, NETCONF, APIs  
Language: English  
Translation pair: articles/2026-08/week-17/08-network-automation-planes-and-sdn.md

## Summary

- Network automation does not kill the command line, but it removes repetitive manual work.
- If the same task repeats across many devices, it can often be scripted, templated, or centrally managed.
- The management plane is how administrators manage a device: SSH, web UI, SNMP, API.
- The control plane is where decisions are made: routing, topology, forwarding logic.
- The data plane is where packets are forwarded, often using ASICs.
- Basic automation often works with the management plane.
- `SDN` goes further and centralizes the control plane through a controller.
- A Wireless LAN Controller with lightweight APs is a practical example of centralized control.

## Key Points

- Automation is the cure for repetition, not magic.
- One shop can be managed manually. Many locations need repeatability.
- A Python script that connects to multiple devices and changes a password is a simple automation example.
- Three planes explain modern networking: management, control, and data.
- `SDN` is not just automating login work. It moves network intelligence into a controller.
- The data plane still matters because devices must forward packets quickly.
- The full SDN vision needs standards and open protocols, not only vendor-specific controllers.

## Notes

When people hear network automation, they sometimes get the wrong idea:

```text
The command line is dead.
I no longer need to understand switches.
```

No.

Automation does not remove networking. It removes repetitive work that people do over and over.

If a task is the same on 10, 100, or 500 devices, it should not always require manual typing on each device.

## Automation As A Cure For Repetition

Network automation is practical:

```text
If an action repeats, it can often be standardized and automated.
```

Approaches vary:

- script;
- template;
- playbook;
- controller;
- API;
- central management system.

The point is the same: do not turn the engineer into someone manually entering the same thing hundreds of times.

## NetworkChuck Coffee Scenario

One coffee shop is simple.

You can manually configure:

- router;
- several switches;
- wireless access points;
- VLANs;
- passwords;
- SSH settings;
- NTP;
- syslog.

Then NetworkChuck Coffee grows.

Now there are:

- multiple locations;
- matching VLANs;
- matching security settings;
- matching wireless policies;
- matching passwords or secrets;
- matching monitoring settings.

Manual configuration becomes risky.

One device is updated. Another is missed. A third gets a typo. A fourth is missing a command.

Automation makes rollout repeatable.

## Python Example

`Python` is a popular programming language for automation.

A simple network automation example:

```text
Script connects to several devices.
It logs in.
It sends the same commands.
It checks the result.
It saves output.
```

For example, it can update a password on several lab devices or collect interface status.

Start safely.

Do not make your first automation task a production change across hundreds of switches. Begin with read-only tasks or a lab environment.

## Three Network Device Planes

To understand automation and `SDN`, divide a device into three logical planes:

- management plane;
- control plane;
- data plane.

These are not three physical boxes. They are three roles inside a network device.

## Management Plane

The `management plane` is how an administrator interacts with the device.

Examples:

- SSH;
- web interface;
- SNMP;
- API calls;
- console;
- NETCONF;
- RESTCONF.

If a script connects to a router over SSH and sends commands, it is working through the management plane.

Basic network automation often starts here.

## Control Plane

The `control plane` is the part of the device that makes decisions.

Examples:

- routing protocols;
- topology decisions;
- neighbor relationships;
- STP decisions;
- path selection;
- control traffic exchange.

The control plane is not physically forwarding every packet. It understands:

```text
Where should traffic go?
Which path is correct?
What topology is current?
```

## Data Plane

The `data plane` forwards packets.

Simplified:

```text
Packet enters.
Device checks forwarding information.
Packet exits the right interface.
```

The data plane must be fast.

That is why devices often use `ASICs`, specialized chips built for high-speed traffic forwarding.

Short model:

```text
Management plane = administration.
Control plane = decisions.
Data plane = forwarding.
```

## Where SDN Fits

`SDN`, or `Software Defined Networking`, goes beyond normal automation.

Basic automation:

```text
I still manage separate devices.
I just do it faster with scripts or tools.
```

SDN:

```text
Network intelligence moves into a controller.
Devices become simpler and more focused on forwarding.
```

In other words, `SDN` centralizes not only management, but part of the control plane.

## Controller

A `controller` is the central system that makes decisions and manages devices.

It can:

- store policies;
- deliver configuration;
- manage topology;
- collect telemetry;
- program forwarding behavior;
- coordinate changes.

Ideally, the engineer works with the controller, and the controller manages the devices.

## Wireless Controller Example

A Wireless LAN Controller is an easy example.

A lightweight AP often does not operate as a fully independent device.

It:

- connects to the network;
- finds the WLC;
- receives configuration;
- broadcasts the right SSIDs;
- maps traffic to VLANs;
- may tunnel traffic through the controller;
- gives part of the intelligence to the controller.

That is a practical example of SDN-like thinking: centralized management and control instead of manually configuring every AP.

In Cisco environments, AP-to-controller communication often uses `CAPWAP`.

## Why Universal SDN Is Hard

The full `SDN` dream looks like this:

```text
Any device.
Any vendor.
One controller.
Unified management.
```

Reality is harder.

If a Cisco controller only controls Cisco, and another vendor controls only its own devices, that is useful but not the full ideal.

Real progress needs:

- open standards;
- common protocols;
- predictable APIs;
- consistent data models;
- interoperability between vendors.

## Protocols And Tools

Automation and SDN discussions include protocols such as:

- `OpenFlow`;
- `NETCONF`;
- `RESTCONF`;
- `OpFlex`;
- SSH;
- SNMP;
- APIs.

You do not need to memorize every detail immediately.

The main idea:

```text
Networks are becoming programmable.
Devices can be queried, configured, and coordinated through standard or vendor APIs.
```

## Beyond Classic Networking

This idea exists outside routers and switches too.

Similar patterns appear in:

- home automation;
- camera systems;
- cloud platforms;
- infrastructure tools;
- wireless controllers;
- firewall managers;
- monitoring platforms.

The expectation is becoming normal:

```text
Plug in.
Adopt.
Centrally manage.
Automate.
```

## Practical Tip

If you are starting automation, do not try to replace the entire workflow immediately.

Start safely:

- backup configs;
- collect interface status;
- collect inventory;
- verify NTP;
- verify syslog;
- change lab passwords;
- compare baseline.

First build trust in scripts. Then expand.

## Main Takeaway

Network automation removes repetitive manual tasks, especially through the management plane.

`SDN` goes further: it centralizes the control plane and moves intelligence into a controller. But the data plane remains critical because devices must still forward packets quickly.

Three ideas to remember:

1. Automation reduces repetition.
2. SDN centralizes control.
3. The data plane keeps traffic moving.

## Commands And Terms

| Term | Meaning |
| --- | --- |
| network automation | Automating repetitive network management tasks. |
| `Python` | Programming language often used for automation. |
| management plane | Device administration: SSH, API, SNMP, web UI. |
| control plane | Decision-making: routing, topology, path selection. |
| data plane | Packet forwarding. |
| `ASIC` | Specialized chip for fast traffic forwarding. |
| `SDN` | Software Defined Networking, centralized control approach. |
| controller | Central management and control system. |
| `WLC` | Wireless LAN Controller. |
| `CAPWAP` | Protocol used between lightweight APs and controllers. |
| `OpenFlow` | Protocol associated with programmable forwarding. |
| `NETCONF` | Protocol for programmatic management of network devices. |
| API | Programmable interface for system interaction. |
| orchestration | Coordinated automation across systems. |

## Questions

### 1. What does automation not remove?

Answer: It does not remove the need to understand networking or the command line. It removes repetitive manual work.

### 2. What is the management plane?

Answer: The way administrators manage a device, such as SSH, web UI, SNMP, and APIs.

### 3. How is the control plane different from the data plane?

Answer: The control plane makes decisions about paths and topology, while the data plane forwards packets.

### 4. How is SDN different from basic automation?

Answer: Basic automation often manages devices through the management plane, while SDN centralizes the control plane through a controller.

### 5. Why does the data plane still matter?

Answer: Even with a smart controller, devices must still forward traffic quickly.

## Review Later

- The three planes: management, control, data.
- Why automation starts with repetitive tasks.
- How SDN differs from normal scripting.
- The role of a controller.
- Why a WLC is a practical SDN-like example.
- Why open protocols and APIs matter.
