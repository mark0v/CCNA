# What Now? NAT Foundations

Source: closed course page  
Date added: 2026-06-13  
Related plan item: Week 7 / NAT foundations checkpoint  
Tags: NAT, PAT, static NAT, dynamic NAT, Packet Tracer, troubleshooting, RFC 1918
Language: English
Translation pair: articles/2026-06/week-07/03-what-now-nat-foundations.md

## Summary

This checkpoint combines the Network Address Translation forms covered so far: static NAT, dynamic NAT and PAT/NAT overload. The main result is not memorizing isolated commands, but understanding the complete traffic path across the boundary between private and public networks.

The next step is independent practice: build the topology in Packet Tracer, configure routing and NAT, inspect translations, introduce faults intentionally and restore connectivity with a systematic process.

## Key Points

- RFC 1918 addresses are intended for private networks and are not propagated through the global Internet routing table.
- NAT changes address representation across a network boundary.
- Static NAT creates a permanent one-to-one mapping.
- Dynamic NAT temporarily assigns a public address from a pool.
- PAT allows many flows to share one or more public addresses.
- Outbound translation and inbound service publishing solve different problems.
- An ACL in a NAT configuration classifies source addresses.
- `ip nat inside` and `ip nat outside` define the translation sides.
- NAT does not repair missing routes or replace a firewall.
- Upstream routing and filtering are part of the end-to-end path.
- Diagnosing a broken configuration is more valuable than mechanically repeating commands.

## What You Can Do Now

After this NAT block, you can explain and configure:

- why private hosts require translation for ordinary public Internet access;
- inside local and inside global terminology;
- inside and outside interface roles;
- static one-to-one translation;
- static port translation for publishing a service;
- dynamic NAT with an ACL and public pool;
- PAT with pool overload;
- PAT using an outside interface address;
- verification with `show ip nat translations`;
- troubleshooting with routing, ACL counters and NAT statistics.

## Private Addresses And The Internet

Private IPv4 ranges:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

do not have a special property that physically prevents a packet from leaving a LAN. A router can forward such a packet if routing and policy permit it.

The real issues are:

- RFC 1918 prefixes must not be advertised into the global routing table;
- Internet routers have no normal global return route to a specific private network;
- providers and network operators commonly filter spoofed or inappropriate source addresses;
- millions of independent networks reuse the same private ranges.

A packet sourced from `192.168.10.21` therefore cannot rely on ordinary end-to-end exchange across the public Internet. NAT or PAT replaces the private source representation with a routable public address associated with the edge network.

## The Three Main NAT Forms

### Static NAT

```text
192.168.10.50 <-> 216.0.5.20
```

Use it when an internal host requires a permanent public identity.

Typical uses:

- publishing an internal server;
- a predictable inbound destination;
- a device requiring a dedicated public source address;
- legacy integration.

Static NAT is not firewall permission. Public routing and security policy must still allow the required traffic.

### Dynamic NAT

```text
Inside networks -> ACL -> public address pool
```

Example:

```cisco
ip nat inside source list 1 pool cafepublic
```

The router temporarily assigns an available pool address to each active inside host. Every active translation remains one-to-one, limiting scalability to the number of public addresses.

### PAT / NAT Overload

```text
many inside flows -> one or a few public addresses
```

Example:

```cisco
ip nat inside source list 1 interface GigabitEthernet0/2 overload
```

PAT distinguishes translations using protocol and transport port or identifier information. It is the common choice for general Internet access.

## Outbound Access And Inbound Publishing

Do not merge these into one vague task called "configure NAT."

### Outbound Client Access

Inside clients initiate connections:

```text
Inside client -> edge router -> Internet service
```

PAT is the common solution:

```text
192.168.10.21:51001 -> 216.0.5.2:30001
```

### Inbound Service Publishing

An outside client initiates a connection to a published address or port:

```text
Internet client -> public IP/port -> internal server
```

Static PAT example:

```cisco
ip nat inside source static tcp 192.168.10.50 443 216.0.5.20 443
```

Publishing requires especially careful firewall policy, hardening, monitoring and often a separate DMZ.

## Independent Lab

Build this topology:

```text
Inside LAN
    |
Customer Edge Router
    |
ISP Router
    |
Outside Test Network / Loopback
```

Recommended components:

- at least two inside clients;
- an edge router with inside and outside interfaces;
- a separate ISP router;
- an outside server or loopback test address;
- private addressing internally;
- a documentation table for interfaces and prefixes.

### Example Addressing

| Device | Interface | Address | Role |
| --- | --- | --- | --- |
| PC1 | NIC | `192.168.10.21/24` | Inside client |
| PC2 | NIC | `192.168.10.22/24` | Inside client |
| EDGE | Gi0/0 | `192.168.10.1/24` | NAT inside |
| EDGE | Gi0/2 | `216.0.5.2/24` | NAT outside |
| ISP | Gi0/0 | `216.0.5.1/24` | Upstream |
| ISP | Loopback0 | `203.0.113.10/32` | Test destination |

Documentation ranges are used here only for the lab.

## Stage 1: Verify Routing Before NAT

Before configuring translation:

1. Verify local addressing.
2. Verify client default gateways.
3. Verify interface status.
4. Verify connected routes.
5. Configure a default route on the edge.
6. Confirm that the edge can reach the outside test address using its outside address.

Example:

```cisco
ip route 0.0.0.0 0.0.0.0 216.0.5.1
```

Separate routing problems from NAT problems. If the edge router cannot reach the outside network itself, PAT cannot repair the path.

## Stage 2: Configure PAT

```cisco
interface GigabitEthernet0/0
 ip nat inside

interface GigabitEthernet0/2
 ip nat outside

access-list 1 permit 192.168.10.0 0.0.0.255

ip nat inside source list 1 interface GigabitEthernet0/2 overload
```

Generate traffic from both clients and inspect:

```cisco
show ip nat translations
show ip nat statistics
show access-lists 1
```

Expected result: different inside local addresses use the same inside global address with distinct ports or identifiers.

## Stage 3: Add Static NAT Or Static PAT

Add an internal server:

```text
192.168.10.50
```

Full static NAT:

```cisco
ip nat inside source static 192.168.10.50 216.0.5.20
```

Publish HTTPS only:

```cisco
ip nat inside source static tcp 192.168.10.50 443 216.0.5.20 443
```

Verify:

- the public address is reachable from the ISP side;
- `216.0.5.20` is routed toward the edge;
- the internal service is running;
- security policy permits the traffic;
- the reply returns through the same edge.

## Simulating ISP Filtering

Real networks can perform source validation with:

- infrastructure ACLs;
- uRPF;
- anti-spoofing policy;
- provider edge filters;
- routing policy.

Packet Tracer can use an ACL on an ISP-facing interface to demonstrate rejection of traffic with RFC 1918 source addresses. However, a provider design is not reducible to one universal "block private addresses" command.

The lab should demonstrate:

1. Routing and policy can forward or discard a packet.
2. A private source has no normal global return path.
3. After PAT, the outside network sees a public source.

## Break The Configuration Intentionally

After establishing a working baseline, introduce one fault at a time.

### Fault 1: Remove `ip nat inside`

```cisco
interface GigabitEthernet0/0
 no ip nat inside
```

Observation:

- the ACL can match;
- routing can exist;
- translation fails because the NAT boundary is incomplete.

### Fault 2: Use The Wrong Wildcard Mask

```cisco
access-list 1 permit 192.168.10.0 0.0.0.0
```

This matches only exact address `192.168.10.0`, not the entire `/24`.

### Fault 3: Reference The Wrong Outside Interface

Check:

```cisco
show ip interface brief
show running-config | include ip nat
```

### Fault 4: Remove The Default Route

NAT entries do not replace a forwarding path.

### Fault 5: Change The Client Default Gateway

The packet may never reach the NAT router.

### Fault 6: Block Traffic Upstream

NAT can operate correctly while a later policy discards the packet.

### Fault 7: Stop The Published Service

A valid translation does not prove that the application listens on the required port.

## Systematic Troubleshooting Order

When NAT fails, do not start by randomly retyping commands.

1. Verify the source host IP, mask and gateway.
2. Verify the local interface state.
3. Verify the route lookup to the destination.
4. Verify the return path.
5. Identify ingress and egress interfaces.
6. Check `ip nat inside` and `ip nat outside`.
7. Confirm that the source address matches the ACL.
8. Check ACL hit counters.
9. Verify the NAT rule and its overload, pool or static mapping.
10. Inspect `show ip nat translations`.
11. Inspect `show ip nat statistics`.
12. Verify next-hop and outside-destination reachability.
13. Check upstream filtering.
14. Check firewall policy.
15. Test DNS separately from IP connectivity.
16. Verify the application service and listening port.

## Core Verification Commands

```cisco
show ip interface brief
show ip route
show access-lists
show ip nat translations
show ip nat statistics
show running-config | include ip nat
show running-config | section interface
ping
traceroute
```

Production troubleshooting can also use logs, counters, packet captures and platform-specific commands. `debug ip nat` can generate substantial load and output, so use it carefully and selectively.

## Reading The Symptoms

### ACL Counters Do Not Increase

Possible causes:

- the source is outside the ACL;
- traffic does not cross the expected router;
- the wildcard mask is wrong;
- the wrong flow is being tested.

### ACL Counters Increase But No Translation Appears

Check:

- interface roles;
- the NAT rule;
- pool or interface reference;
- platform errors;
- traffic direction.

### A Translation Exists But No Reply Returns

Check:

- outside routing;
- provider filtering;
- destination reachability;
- return path;
- firewall;
- application.

### IP Connectivity Works But Names Fail

This is likely a DNS problem rather than a NAT failure.

### One Client Works And Another Does Not

Check:

- ACL coverage;
- client gateway;
- VLAN and routing;
- pool exhaustion with dynamic NAT;
- platform or session limits with PAT.

## NAT Is Not A Security Boundary By Itself

Private addressing and PAT reduce direct address visibility, but do not replace:

- a firewall;
- network segmentation;
- endpoint security;
- authentication;
- encryption;
- patch management;
- monitoring;
- least-privilege access.

A static mapping that publishes a service increases attack surface and requires explicit policy.

## Practice Plan

### Pass 1: Exact Reproduction

- Recreate the working topology.
- Configure routing.
- Configure PAT.
- Verify translations.
- Add a static mapping.

### Pass 2: Change The Addresses

- Use different private subnets.
- Change the outside subnet.
- Recalculate wildcard masks.
- Update routes and ACLs.

### Pass 3: Add A Segment

- Guest Wi-Fi.
- Business LAN.
- Camera network.
- Separate server segment.

Decide which networks should receive outbound NAT and which should not.

### Pass 4: Troubleshoot

- Break one element.
- Predict the symptom.
- Confirm it with show commands.
- Fix the cause.
- Record the observation.

### Pass 5: Explain

Without notes, explain:

```text
How a packet changes from an inside client to an outside server
and how the reply returns to the correct host.
```

When the explanation is precise and supported by output, the topic is no longer merely a command list.

## NAT Foundations Checklist

- [ ] I understand why RFC 1918 addresses are not used for normal global routing.
- [ ] I distinguish routing from address translation.
- [ ] I distinguish inside local, inside global, outside local and outside global.
- [ ] I can assign inside and outside interface roles.
- [ ] I can configure static NAT.
- [ ] I can configure static PAT.
- [ ] I can configure a dynamic NAT pool.
- [ ] I can configure interface overload.
- [ ] I understand an ACL as a classifier.
- [ ] I can calculate a wildcard mask.
- [ ] I inspect translations and statistics.
- [ ] I always check the return path.
- [ ] I distinguish NAT issues from DNS, routing, firewall and application issues.
- [ ] I plan NAT changes as potentially disruptive.
- [ ] I document the topology and rationale.

## Quick Self-Check

### Question 1

Why is an RFC 1918 address unsuitable as the source of ordinary public Internet exchange?

Answer:

```text
Private prefixes are not propagated globally, lack a unique public return path
and are commonly filtered at network boundaries.
```

### Question 2

How does static NAT differ from PAT?

Answer:

```text
Static NAT creates a permanent address mapping,
while PAT allows many flows to share a public address.
```

### Question 3

What should you check if the ACL counter increases but no translation appears?

Answer:

```text
Inside and outside roles, the NAT rule, its pool or interface reference,
and the traffic direction.
```

### Question 4

Does a translation table entry prove that an application works?

Answer:

```text
No. NAT can be correct while the service, firewall or return path fails.
```

### Question 5

Why break a lab intentionally?

Answer:

```text
To connect a specific fault with an observable symptom
and learn to identify the cause systematically.
```

## Commands / Terms

| Command / Term | Purpose |
| --- | --- |
| RFC 1918 | Private IPv4 address ranges. |
| Static NAT | Permanent one-to-one address mapping. |
| Dynamic NAT | Temporary assignment from a pool. |
| PAT | Public-address sharing between flows. |
| `ip nat inside` | Marks the internal NAT side. |
| `ip nat outside` | Marks the external NAT side. |
| `show ip nat translations` | Displays active translations. |
| `show ip nat statistics` | Displays NAT configuration and counters. |
| `show access-lists` | Displays ACL matches. |
| Return path | Reply path toward the original host. |
| Upstream filtering | Policy at the next network boundary. |

## What To Review Later

- Extended ACLs
- Stateful firewalls
- NAT order of operations
- Hairpin NAT
- Twice NAT
- IPv6 and avoiding IPv4 NAT
- Packet captures
- Production change planning
