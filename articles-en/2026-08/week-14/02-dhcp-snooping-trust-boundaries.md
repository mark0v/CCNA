# DHCP Snooping Trust Boundaries

Source: closed course page  
Date added: 2026-08-02  
Related plan item: Week 14 / DHCP Snooping trust boundaries  
Tags: DHCP Snooping, rogue DHCP, switch security, access layer, trust boundary, binding table, Layer 2 security
Language: English
Translation pair: articles/2026-08/week-14/02-dhcp-snooping-trust-boundaries.md

## Summary

- DHCP Snooping protects the network from rogue DHCP servers.
- DHCP is trusting by default: a client can accept an answer from whichever server responds.
- A switch with DHCP Snooping only allows DHCP offers from trusted ports.
- User-facing access ports usually remain untrusted.
- Trusted ports are uplinks or ports toward the legitimate DHCP server.
- If you miss a trusted port in the return path, clients may stop receiving addresses.
- The DHCP Snooping binding table is later used by other Layer 2 security features.

## Key Points

- The question is not where the client is; the question is where the legitimate DHCP offer comes from.
- Do not trust a port just because the attached user needs DHCP.
- The trust boundary must match the real path of DHCP replies.
- In a multi-switch network, trusted uplinks must be configured on every hop that receives legitimate offers.
- If you trust every port, the feature loses its purpose.
- DHCP Snooping is not an isolated checkbox; it is a foundation for later IP-to-MAC validation.

## Notes

DHCP Snooping has an odd name, but the feature is practical. DHCP works quietly until it breaks. A client boots, sends a broadcast request, the server responds, the client receives an IP address, gateway, DNS settings, and starts working.

The problem is that DHCP does not verify which server is real. If another device starts answering DHCP requests, clients may accept that response.

Sometimes this is accidental. Someone brings in a home router, connects it to the office network, and DHCP is still enabled. Clients receive bad addresses or a bad gateway and lose connectivity.

Sometimes it is an attack. A rogue DHCP server can hand out addresses from the correct subnet but set itself as the default gateway. The user may still reach the network, but traffic now passes through an attacker-controlled device. That is a man-in-the-middle scenario.

## The Rogue DHCP Problem

Imagine NetworkChuck Coffee.

There is a legitimate DHCP server handing out addresses for the cafe, admin network, and other VLANs. Everything works.

Then someone connects another device that also starts offering DHCP:

- a home router;
- a small lab server;
- a rogue access point;
- a misconfigured laptop;
- an attacker's device.

The client does not ask whether this is the real DHCP server. It waits for an answer.

If the rogue DHCP server responds first, the client may receive:

- the wrong IP address;
- the wrong default gateway;
- the wrong DNS server;
- a path through the attacker;
- settings that break access to the network.

This is dangerous because it can look like a normal DHCP outage instead of an attack.

## What DHCP Snooping Does

DHCP Snooping tells the switch:

```text
DHCP offers are only allowed from ports I explicitly trust.
```

After the feature is enabled, all ports are untrusted until you configure trust.

The logic:

| Port type | Behavior |
| --- | --- |
| `trusted` | Allowed to receive DHCP server replies. |
| `untrusted` | DHCP server replies are blocked. |

Client DHCP requests from access ports still pass. That is normal. The server replies must return through an approved path.

The key configuration question:

```text
Through which interface does this switch receive the legitimate DHCP offer?
```

That interface is usually the one that should be trusted.

## Basic Configuration

Example:

```text
ip dhcp snooping
ip dhcp snooping vlan 10,20

interface gi0/1
 ip dhcp snooping trust
```

Breakdown:

| Command | Meaning |
| --- | --- |
| `ip dhcp snooping` | Enables the feature globally. |
| `ip dhcp snooping vlan 10,20` | Enables protection for VLAN 10 and VLAN 20. |
| `ip dhcp snooping trust` | Marks the interface as trusted for DHCP replies. |

Every other port remains untrusted unless explicitly configured otherwise.

## Where To Put Trust

The most common mistake is trusting a user port because the user needs a DHCP address.

That is backward.

Trust the direction where DHCP offers come from, not the client.

Examples:

| Scenario | How to think |
| --- | --- |
| DHCP server directly connected to the switch | Trust the port toward the DHCP server. |
| DHCP server behind a router | Trust the uplink toward the router. |
| DHCP server behind another switch | Trust the trunk/uplink toward the DHCP server. |
| User-facing access port | Usually untrusted. |

In a multi-switch network, verify the whole path. If the DHCP offer passes through three switches, each switch must trust the correct uplink where that offer arrives.

One missed `ip dhcp snooping trust` can stop clients behind that point from receiving addresses.

## Packet Tracer And Real Devices

In labs, Packet Tracer can behave strangely with DHCP Snooping, especially with VLANs. It is not the best source for production conclusions.

On real gear, the logic is cleaner:

- enable DHCP Snooping;
- specify the VLANs;
- trust only ports that receive legitimate DHCP replies;
- do not trust user access ports;
- verify with show commands.

If a simulator requires you to trust extra interfaces just to make a demo work, do not carry that habit into a real network. Trusting every port defeats the security goal.

## Binding Table

One important benefit of DHCP Snooping is the binding table.

The switch records which MAC address received which IP address, in which VLAN, and on which interface.

Simplified:

```text
MAC address + IP address + VLAN + interface
```

This is useful beyond DHCP. Other Layer 2 security features can use this table to detect whether a device is pretending to own another IP address.

That is why DHCP Snooping often comes before stronger mechanisms such as Dynamic ARP Inspection.

## Verification

Useful commands:

```text
show ip dhcp snooping
show ip dhcp snooping binding
show interfaces trunk
show running-config | include dhcp snooping
```

Check:

- whether DHCP Snooping is enabled globally;
- whether it is enabled for the correct VLANs;
- which ports are trusted;
- whether unnecessary access ports are trusted;
- whether the binding table is populated;
- whether the trunk/VLAN path matches the real DHCP path.

If clients are not receiving addresses, check the trust boundary before assuming the DHCP server is down. Very often, the server is fine and one uplink is missing trust.

## NetworkChuck Coffee Scenario

At NetworkChuck Coffee, customers and staff should receive addresses from the legitimate DHCP server.

We want to:

- allow DHCP requests from clients;
- allow DHCP replies only from the real infrastructure side;
- block rogue DHCP servers on access ports;
- keep a binding table for future protections.

The result is simple: a random box plugged into a wall jack cannot start handing out network settings to the cafe.

## Main Takeaway

DHCP Snooping is about trust boundaries.

You explicitly tell the switch which interfaces are allowed to bring in DHCP replies. Every other port is treated as suspicious for server-side DHCP traffic.

The feature is small, but the effect is large: less rogue DHCP risk, less chance of man-in-the-middle through a fake gateway, and better data for later Layer 2 security.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| DHCP Snooping | Switch feature that filters DHCP replies based on trusted and untrusted ports. |
| rogue DHCP server | Unauthorized DHCP server in the network. |
| `trusted port` | Port allowed to receive DHCP server replies. |
| `untrusted port` | Port where DHCP server replies are blocked. |
| DHCP offer | DHCP server response offering network settings. |
| binding table | Table of MAC, IP, VLAN, and interface mappings learned through DHCP. |
| trust boundary | Point where the switch explicitly trusts infrastructure DHCP traffic. |
| man-in-the-middle | Scenario where an attacker passes traffic through their own device. |

## Questions

### 1. What does DHCP Snooping block?

Answer: DHCP replies from unauthorized ports.

### 2. Why should a user access port usually remain untrusted?

Answer: A user port should send DHCP requests, but it should not bring in DHCP replies as a server.

### 3. What happens if you miss a trusted uplink in the DHCP offer path?

Answer: Clients behind that point may stop receiving IP addresses.

### 4. Why is the binding table useful?

Answer: It records MAC, IP, VLAN, and interface mappings and can be used by other security features.

### 5. Why not just trust every port?

Answer: A rogue DHCP server would also be allowed to send DHCP replies, defeating the protection.

## What To Review Later

- DHCP Snooping enablement commands.
- Difference between trusted and untrusted ports.
- How to trace the DHCP offer path.
- `show ip dhcp snooping` verification.
- The DHCP Snooping binding table.
- Relationship between DHCP Snooping and Dynamic ARP Inspection.
