# Dynamic ARP Inspection With DHCP Snooping

Source: closed course page  
Date added: 2026-08-02  
Related plan item: Week 14 / Dynamic ARP Inspection with DHCP Snooping  
Tags: Dynamic ARP Inspection, DAI, DHCP Snooping, ARP spoofing, man-in-the-middle, switch security, Layer 2 security
Language: English
Translation pair: articles/2026-08/week-14/03-dynamic-arp-inspection-with-dhcp-snooping.md

## Summary

- Dynamic ARP Inspection protects against forged ARP replies.
- ARP is trusting by default: a device asks who owns an IP address and believes the answer.
- An attacker can use ARP spoofing to claim their MAC address belongs to a server or gateway IP.
- DAI inspects ARP messages on untrusted ports.
- DAI usually relies on the binding table created by DHCP Snooping.
- Uplinks, trunks, and ports with static-IP devices need careful planning.
- A careless DAI rollout can break valid ARP traffic.

## Key Points

- DAI does not work in isolation; it needs a trusted IP-to-MAC reference.
- DHCP Snooping builds the trust base, and DAI uses it to validate ARP.
- User-facing access ports usually remain untrusted.
- Infrastructure ports and uplinks often need to be trusted or accounted for.
- Static-IP devices may not appear in the DHCP Snooping binding table.
- ARP rate limiting can apply on untrusted ports.
- Before production rollout, identify trunks, uplinks, static-IP devices, and special edge ports.

## Notes

ARP looks harmless. A device asks, "Who has this IP address?" Another device answers with its MAC address. The client then sends frames to that MAC address.

The problem is that ARP does not verify truth by itself. If a malicious device answers faster than the real server or gateway, the client may believe it.

That is ARP spoofing: an attacker claims, "This IP belongs to me," even though it does not. Traffic can then pass through the attacker's device. That is a classic man-in-the-middle scenario.

Dynamic ARP Inspection, or DAI, adds validation. The switch inspects ARP messages and compares device claims against trusted information it already knows.

## The Problem DAI Solves

Imagine NetworkChuck Coffee.

A register terminal wants to reach a back-office server. It sends an ARP request:

```text
Who owns this IP address?
```

The real server should answer with its MAC address. But a rogue laptop in the same network can answer first:

```text
That IP is mine. Send traffic to me.
```

If the client believes it, sensitive traffic can go to the wrong device.

DAI stops that impersonation. It validates ARP replies and drops ones where the IP and MAC do not match the known binding.

## Relationship With DHCP Snooping

DAI relies on DHCP Snooping.

When a client receives an address through DHCP, the switch sees:

- the client's MAC address;
- the assigned IP address;
- the VLAN;
- the interface.

That information goes into the binding table.

Simplified:

```text
MAC address + IP address + VLAN + interface
```

After that, DAI can validate ARP:

```text
If a device claims to own this IP, its MAC address must match the binding table.
```

If there is no match, the ARP message is dropped.

## Basic Configuration

First, DHCP Snooping must be enabled:

```text
ip dhcp snooping
ip dhcp snooping vlan 10,20
```

Then ARP inspection is enabled for the target VLANs:

```text
ip arp inspection vlan 10,20
```

Then trust is configured on the correct interfaces:

```text
interface gi0/1
 ip arp inspection trust
```

Breakdown:

| Command | Meaning |
| --- | --- |
| `ip arp inspection vlan 10,20` | Enables DAI for VLAN 10 and VLAN 20. |
| `ip arp inspection trust` | Marks the interface as trusted for ARP inspection. |
| `ip dhcp snooping` | Creates the basis for the binding table. |

By default, ports are treated as untrusted, and ARP messages on them are inspected.

## What Needs Trust

Before enabling DAI, walk the topology.

Pay special attention to:

- switch uplinks;
- trunk ports;
- router ports;
- firewall ports;
- servers with static IP addresses;
- wireless access points with many clients;
- controllers and other infrastructure devices.

This matters because not every device receives an address through DHCP. If a device uses a static IP address, it may not be present in the DHCP Snooping binding table. DAI can then see a valid ARP reply and treat it as a spoof.

There are two common approaches:

- make the infrastructure interface trusted;
- add a correct static binding if the platform and design support it.

The main rule is simple: do not enable DAI blindly.

## ARP Validation

DAI can perform additional checks.

Common validation checks include:

- source MAC;
- destination MAC;
- IP address.

The idea is that the switch compares what the ARP packet claims with what should be true.

Source MAC and IP address checks are especially useful against the classic spoofing attempt where an attacker claims, "I own this IP," but their MAC address does not match the known binding.

Destination MAC validation can add another layer, but it requires care. Gratuitous ARP is sometimes legitimate, including in first-hop redundancy scenarios. The stricter the validation, the more important it is to understand real edge cases.

## ARP Rate Limit

DAI can limit ARP packets per second on untrusted ports.

For a normal user PC, that is useful. A flood of ARP packets can indicate an attack or a mistake.

But one port does not always mean one device. A wireless access point or downstream segment may carry ARP traffic for many clients. In that case, the default rate limit should be reviewed before rollout.

Otherwise, the protection can look like random connectivity issues.

## Verification

Useful commands:

```text
show ip arp inspection
show ip arp inspection vlan 10
show ip arp inspection interfaces
show ip dhcp snooping binding
show running-config | include arp inspection
```

Check:

- whether DAI is enabled on the correct VLANs;
- which interfaces are trusted;
- which interfaces are untrusted;
- whether the binding table exists;
- whether ARP rate limits are appropriate;
- whether static devices are missing from the table.

## NetworkChuck Coffee Scenario

At NetworkChuck Coffee, DHCP Snooping already protects against rogue DHCP servers and builds the binding table.

The next step is enabling DAI to:

- inspect ARP replies on access ports;
- block attempts to claim someone else's IP address;
- reduce man-in-the-middle risk;
- use the data DHCP Snooping already collected.

Before that, trusted uplinks, trunks, and infrastructure ports must be identified. Otherwise, the network can be protected so aggressively that valid traffic stops working.

## Main Takeaway

DAI makes ARP replies prove they are telling the truth.

If a device claims to own an IP address, the switch checks that claim against the DHCP Snooping binding table. If the IP and MAC do not match, the ARP message is dropped.

This is powerful Layer 2 protection, but it requires planning. Build the trusted DHCP base first, enable inspection next, configure trusted interfaces carefully, and then verify network behavior.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Dynamic ARP Inspection | Switch feature that validates ARP messages. |
| DAI | Abbreviation for Dynamic ARP Inspection. |
| ARP spoofing | Forging ARP replies to impersonate another IP address. |
| DHCP Snooping binding table | Table of MAC, IP, VLAN, and interface mappings. |
| trusted interface | Interface whose ARP traffic is trusted. |
| untrusted interface | Interface where ARP traffic is inspected. |
| gratuitous ARP | ARP message sent without a prior request. |
| man-in-the-middle | Scenario where an attacker positions a device between communicating endpoints. |
| ARP rate limit | Limit on ARP packets on an untrusted port. |

## Questions

### 1. What attack does DAI protect against?

Answer: ARP spoofing that can lead to a man-in-the-middle attack.

### 2. Why does DAI depend on DHCP Snooping?

Answer: DHCP Snooping builds the binding table that DAI uses to validate IP-to-MAC mappings.

### 3. Why do static-IP devices need attention?

Answer: They may not appear in the DHCP Snooping binding table, so DAI may block their ARP traffic.

### 4. Which ports should be reviewed before enabling DAI?

Answer: Uplinks, trunks, router/firewall ports, static-IP servers, and wireless access points.

### 5. What should be verified after enabling DAI?

Answer: VLANs with ARP inspection, trusted and untrusted interfaces, the binding table, and ARP rate limits.

## What To Review Later

- `ip arp inspection vlan` configuration.
- Role of the DHCP Snooping binding table.
- Difference between trusted and untrusted interfaces.
- Static-IP device risks.
- `show ip arp inspection` verification.
- ARP rate limits on untrusted ports.
