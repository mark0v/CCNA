# Baseline Switch Security Controls

Source: closed course page  
Date added: 2026-07-29  
Related plan item: Week 13 / Baseline switch security controls  
Tags: network security, switch security, port security, DHCP snooping, Dynamic ARP Inspection, access layer, baseline hardening
Language: English
Translation pair: articles/2026-07/week-13/11-baseline-switch-security-controls.md

## Summary

- Cybersecurity is not only for dedicated security teams; baseline security belongs in everyday networking.
- Access-layer switches need protections because users and devices plug in there.
- Three baseline controls to know: Port Security, DHCP Snooping, and Dynamic ARP Inspection.
- Port Security controls which MAC addresses can use a switch port.
- DHCP Snooping blocks unauthorized DHCP server behavior.
- Dynamic ARP Inspection helps stop forged ARP messages and man-in-the-middle attacks.
- These features are preventive controls, not emergency-only tools.

## Key Points

- Good network design includes security from the start.
- A network engineer does not need to become a full-time security specialist to care about security.
- Guest devices, POS systems, staff devices, and cameras all create trust boundaries.
- Rogue DHCP and ARP spoofing can break connectivity or silently redirect traffic.
- Many practical security controls are already built into enterprise switches.
- The next lessons should turn these concepts into hands-on configuration.

## Notes

Security can sound like a separate discipline, but networking and security overlap constantly.

Switches decide who connects. Routers decide where traffic goes. Wireless networks decide how users join. If those parts are left wide open because "security is someone else's job," the design is already weak.

At CCNA level, the goal is not to become a penetration tester. The goal is to build networks that do not collapse or expose internal systems the moment someone plugs in the wrong device.

## Security Is Part Of Networking

Cybersecurity is not one separate island.

In real environments, network engineers touch security when they configure:

- VLANs;
- ACLs;
- switch ports;
- DHCP behavior;
- management access;
- wireless authentication;
- routing boundaries;
- device hardening;
- logging and monitoring.

Some security controls are advanced. Some are optional depending on the environment. But some are basic good practice.

For access-layer switching, three controls are especially important:

1. Port Security.
2. DHCP Snooping.
3. Dynamic ARP Inspection.

## Why Access Layer Security Matters

The access layer is where endpoints connect.

That includes:

- employee laptops;
- POS terminals;
- printers;
- cameras;
- guest devices;
- phones;
- tablets;
- unknown devices someone plugs into a wall jack.

If an attacker or careless user can connect a rogue device, they may be able to:

- consume DHCP leases;
- hand out fake DHCP information;
- impersonate devices;
- poison ARP traffic;
- intercept traffic;
- disrupt business systems.

This is why switch security matters before an incident.

## Port Security

Port Security controls which MAC addresses are allowed on a switch port.

Plain idea:

```text
This switch port should only accept expected devices.
```

Possible behavior:

- allow only one MAC address;
- learn a MAC address dynamically;
- restrict or shut down the port when a violation happens;
- prevent random devices from using an access port.

NetworkChuck Coffee example:

If a POS terminal should be the only device on a port, Port Security can help enforce that expectation. If someone unplugs it and connects an unknown device, the switch can react.

Port Security is not a complete identity solution, but it is useful baseline hardening for access ports.

## DHCP Snooping

DHCP gives clients IP addresses and network settings.

That convenience creates risk. A rogue DHCP server can hand out bad information:

- wrong default gateway;
- wrong DNS server;
- wrong IP settings;
- attacker-controlled path.

DHCP Snooping lets the switch classify ports as trusted or untrusted.

Concept:

| Port type | Meaning |
| --- | --- |
| Trusted | Allowed to send DHCP server replies. |
| Untrusted | Client-facing; DHCP server replies are blocked. |

Uplink ports toward the real DHCP server are trusted. User access ports are untrusted.

If a random device on an access port tries to act like a DHCP server, the switch drops those responses.

## Dynamic ARP Inspection

ARP helps devices map IP addresses to MAC addresses on a local network.

Problem: ARP is easy to lie to if the network does not check it.

An attacker can send forged ARP messages and convince devices that the attacker's MAC address belongs to the default gateway or another important host.

That can enable man-in-the-middle attacks.

Dynamic ARP Inspection, or DAI, checks ARP messages and blocks suspicious ones.

DAI commonly uses information learned by DHCP Snooping to validate whether an IP-to-MAC binding makes sense.

That is why these features often belong together:

```text
DHCP Snooping builds trusted binding information.
DAI uses that information to inspect ARP.
```

## NetworkChuck Coffee Scenario

Imagine someone plugs a cheap device into an unused network jack at NetworkChuck Coffee.

Possible bad behavior:

- it starts acting as a DHCP server;
- it tells clients to use it as the gateway;
- it poisons ARP entries;
- it intercepts traffic;
- it breaks POS or staff connectivity;
- it creates a noisy outage or a quiet compromise.

Baseline switch security helps stop this earlier:

| Problem | Control |
| --- | --- |
| Unexpected device on port | Port Security |
| Fake DHCP server | DHCP Snooping |
| Forged ARP messages | Dynamic ARP Inspection |

This is not theoretical. These controls protect normal business operations.

## Exam And Real-World Alignment

Some certification topics feel abstract until later.

These features are different.

Port Security, DHCP Snooping, and DAI are useful both for the exam and real networks. They map directly to common access-layer risks:

- unauthorized devices;
- rogue DHCP;
- ARP spoofing;
- man-in-the-middle;
- user-caused outages.

That makes them worth learning as practical tools, not just vocabulary.

## Deployment Mindset

Do not deploy these blindly.

Good rollout habits:

- understand the topology;
- know where DHCP servers live;
- identify trunk/uplink ports;
- identify access ports;
- test in a small area first;
- document trusted ports;
- monitor for violations;
- use maintenance windows when needed;
- have rollback steps.

Baseline security is good. Accidental lockout is still bad.

## What Comes Next

The next practical sequence should be:

1. Port Security: what it does and how to deploy it.
2. DHCP Snooping: trusted ports, VLAN scope, and verification.
3. Dynamic ARP Inspection: ARP validation and DHCP Snooping bindings.

Together, these controls make the access layer much harder to abuse.

## Main Takeaway

Some security belongs everywhere.

If you build or support switches where users and devices connect, baseline protections should be part of the design.

You do not need to become a full-time cybersecurity analyst to configure responsible network defenses. Port Security, DHCP Snooping, and Dynamic ARP Inspection are part of building networks that keep working when someone plugs in something they should not.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Port Security | Switch feature that limits allowed MAC addresses on a port. |
| DHCP Snooping | Switch feature that blocks unauthorized DHCP server replies. |
| Dynamic ARP Inspection | Switch feature that validates ARP messages. |
| DAI | Abbreviation for Dynamic ARP Inspection. |
| Access layer | Network layer where end devices connect. |
| Trusted port | Port allowed to send specific infrastructure traffic such as DHCP replies. |
| Untrusted port | Client-facing port where infrastructure replies should be blocked. |
| Rogue DHCP server | Unauthorized device handing out DHCP settings. |
| ARP spoofing | Sending false ARP information to redirect traffic. |
| Man-in-the-middle | Attack where traffic is intercepted between communicating systems. |

## Questions

### 1. Why does cybersecurity belong in networking?

Answer: Network devices control how users and systems connect, communicate, and trust each other.

### 2. What does Port Security protect against?

Answer: Unexpected or unauthorized MAC addresses on switch ports.

### 3. What does DHCP Snooping protect against?

Answer: Unauthorized DHCP servers sending fake DHCP replies.

### 4. What does Dynamic ARP Inspection protect against?

Answer: Forged ARP messages that can support man-in-the-middle attacks.

### 5. Why should these controls be deployed before an incident?

Answer: They are baseline hardening features designed to prevent common access-layer attacks and outages.

## What To Review Later

- Port Security configuration and violation modes.
- DHCP Snooping trusted ports.
- DHCP Snooping binding table.
- Dynamic ARP Inspection validation.
- Access-layer hardening checklist.
- Safe rollout and rollback planning.
