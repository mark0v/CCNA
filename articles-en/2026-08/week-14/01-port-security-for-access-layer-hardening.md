# Port Security For Access Layer Hardening

Source: closed course page  
Date added: 2026-08-02  
Related plan item: Week 14 / Port Security for access layer hardening  
Tags: Port Security, switch security, access layer, MAC address, sticky MAC, violation mode, err-disabled
Language: English
Translation pair: articles/2026-08/week-14/01-port-security-for-access-layer-hardening.md

## Summary

- Port Security limits which MAC addresses can use a switch port.
- A default access port is too trusting: connect a device and it usually works.
- For many access ports, "one port, one expected MAC address" is a useful baseline.
- Sticky MAC lets the switch learn the first MAC address and keep it as an allowed secure address.
- Port Security violation modes are protect, restrict, and shutdown.
- Shutdown puts the port into err-disabled, which is visible but requires recovery.
- Port Security is not a replacement for 802.1X or NAC, but it is useful access-layer hardening.

## Key Points

- The access layer is where users, printers, POS terminals, cameras, and unknown devices enter the network.
- If a port accepts any MAC address, the switch is trusting whatever gets connected.
- Port Security adds guardrails to normal MAC address learning.
- The maximum allowed MAC count must match the real device pattern on the port.
- An IP phone with a PC behind it may need a maximum of 2, not 1.
- Restrict is often a practical middle ground: unauthorized traffic is dropped, but the port stays up.
- Shutdown is appropriate where a violation should immediately take the port down.

## Notes

Port Security sounds boring at first. It is not encryption, a firewall, or a full identity system. But simple switch features often prevent very normal operational mistakes.

At NetworkChuck Coffee, the access layer connects admin PCs, POS terminals, access points, printers, and service devices. If someone finds an unused wall jack and connects a small unmanaged switch or a rogue access point, a default switch may simply accept it.

That is the problem. A switch is built to connect devices and learn MAC addresses. Port Security does not change that core behavior; it adds a rule around it: this port should only see expected MAC addresses in expected quantities.

## What Port Security Does

The plain idea:

```text
This access port should only serve an allowed number of devices.
```

For example, port E0/3 in the office should connect only one admin PC. If another MAC address appears, it might mean:

- the user replaced the endpoint;
- someone connected a small switch;
- an unknown laptop appeared;
- someone connected a rogue access point;
- the port now has an unexpected device chain.

Not every case is an attack, but the network should not silently accept every change.

Port Security lets you define:

- how many MAC addresses are allowed;
- which MAC addresses are allowed;
- whether the switch should learn the address automatically;
- what should happen when the rule is violated.

## Basic Configuration

Typical example for one access port:

```text
interface fa0/1
 switchport mode access
 switchport port-security
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation shutdown
```

Command breakdown:

| Command | Meaning |
| --- | --- |
| `switchport mode access` | Forces the port to operate as an access port. |
| `switchport port-security` | Enables Port Security on the interface. |
| `maximum 1` | Allows only one MAC address. |
| `mac-address sticky` | Learns the first seen MAC address as a secure MAC. |
| `violation shutdown` | Moves the port to err-disabled when a violation occurs. |

Port Security is usually applied to access ports. It is generally not appropriate on trunks or uplinks because those links are expected to carry traffic for many devices and VLANs.

## Sticky MAC

Sticky MAC is useful because you do not have to manually type every endpoint MAC address.

The switch sees the first connected device, learns its MAC address, and adds it to the running configuration as a secure MAC. After you save the configuration, that address survives a reboot.

This works well for predictable devices:

- POS terminals;
- printers;
- cameras;
- administrator workstations;
- kiosks;
- lab endpoints.

There is an operational side too. If a device is replaced, an employee moves desks, or the port changes purpose, an old sticky MAC can become stale. Those changes need documentation and cleanup.

## Violation Modes

Port Security has three main violation modes.

| Mode | Behavior |
| --- | --- |
| `protect` | Drops traffic from the extra MAC address with minimal visibility. |
| `restrict` | Drops unauthorized traffic and records the violation in counters/logs. |
| `shutdown` | Logs the violation and moves the port to err-disabled. |

Shutdown is the default. It is the most aggressive and the most visible. If an unauthorized MAC address appears, the interface is logically disabled. Even if the original approved device is reconnected, the port will not recover by itself.

Manual recovery usually looks like this:

```text
interface fa0/1
 shutdown
 no shutdown
```

That is worth remembering: err-disabled is not unique to Port Security. A port can also land there because of BPDU Guard or other protective features.

## What To Use In Practice

If the port is sensitive and a violation should immediately stop connectivity, use shutdown.

If you want visibility without immediately taking down a legitimate attached device, restrict is often useful.

If you only want to silently drop extra traffic, protect exists, but it is less helpful operationally because it gives you fewer diagnostic signals.

A good rollout starts small. Test on predictable, low-risk ports, watch the logs, and then expand. Otherwise it is easy to cause your own outage with a maximum that is too low or a sticky MAC learned at the wrong time.

## Verification

Useful commands:

```text
show port-security
show port-security interface fa0/1
show running-config interface fa0/1
show interfaces status err-disabled
```

Check:

- whether Port Security is enabled;
- how many MAC addresses are allowed;
- which violation mode is configured;
- which MAC address is learned as secure;
- whether violations have occurred;
- whether the port is err-disabled.

## NetworkChuck Coffee Scenario

A POS port should serve only the POS terminal. If someone disconnects it and connects a personal laptop or a small switch, the network should not treat that as normal.

With Port Security, you can:

- allow one MAC address;
- learn it with sticky MAC;
- use restrict or shutdown when another MAC address appears;
- see the violation with show commands and logs.

This is not perfect security. MAC addresses can be spoofed. But it is still much better than a completely open access port.

## Limitations

Port Security does not replace:

- 802.1X;
- NAC;
- centralized authentication;
- monitoring;
- physical security;
- regular port audits.

It is local switch-port protection. Its job is to reduce risk from casual connections, unauthorized devices, and simple mistakes.

## Main Takeaway

Port Security gives access ports boundaries.

The switch still learns MAC addresses, but now it learns them under rules: how many devices are allowed, which addresses are trusted, and what to do when the rule is broken.

For CCNA, know the commands and modes. For real work, understand the operational tradeoff: Port Security protects overly trusting ports, but it must be deployed carefully around phones, workstations, hardware replacements, and remote sites.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Port Security | Cisco switch feature that limits MAC addresses on a port. |
| MAC address | Layer 2 hardware address of a network interface. |
| secure MAC address | MAC address allowed by the Port Security policy. |
| sticky MAC | Dynamically learned MAC address added to the configuration. |
| violation mode | The response used when an unauthorized MAC address appears. |
| protect | Silently drops violating traffic. |
| restrict | Drops violating traffic and provides violation visibility. |
| shutdown | Moves the port to err-disabled. |
| err-disabled | State where the switch has logically disabled a port because of an error or protection feature. |
| access port | Port used by an endpoint in one VLAN. |

## Questions

### 1. What does Port Security limit?

Answer: The number and set of MAC addresses allowed to use a switch port.

### 2. Why is `maximum 1` not always correct?

Answer: One port may legitimately see two MAC addresses, such as an IP phone and a PC behind it.

### 3. How is `restrict` different from `protect`?

Answer: Both drop violating traffic, but restrict provides visibility through counters and violation messages.

### 4. What does `shutdown` mode do?

Answer: It moves the port to err-disabled when a violation occurs, requiring administrator recovery.

### 5. Why is Port Security not a complete identity system?

Answer: It relies on MAC addresses, and MAC addresses can be spoofed; stronger identity enforcement needs mechanisms such as 802.1X.

## What To Review Later

- Basic Port Security configuration.
- Difference between protect, restrict, and shutdown.
- Err-disabled behavior.
- Sticky MAC configuration.
- `show port-security` verification.
- Scenarios where the maximum MAC count should be increased.
