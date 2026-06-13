# Configuring PAT (NAT Overload)

Source: closed course page  
Date added: 2026-06-13  
Related plan item: Week 7 / PAT and NAT overload configuration  
Tags: PAT, NAT overload, interface overload, NAT pool, ACL, source port, Cisco IOS
Language: English
Translation pair: articles/2026-06/week-07/02-configuring-pat-nat-overload.md

## Summary

PAT, or NAT overload, allows many internal devices to share one public IPv4 address or a small public pool. The router distinguishes flows with more than IP addresses: it tracks transport-layer ports and uses identifiers for protocols such as ICMP.

This is the most common NAT form for outbound user internet access. Home routers, small offices and many enterprise edge devices use PAT because each inside client does not require a separate public address.

PAT has two common configurations:

```text
ACL -> public NAT pool -> overload
ACL -> outside interface address -> overload
```

The interface method is especially useful when an ISP assigns the public address dynamically.

## Key Points

- Dynamic NAT creates active one-to-one mappings.
- PAT creates many-to-one or many-to-few translations.
- The `overload` keyword permits public-address sharing.
- The router distinguishes TCP and UDP sessions by protocol and port numbers.
- One inside host can create many translations simultaneously.
- The ACL identifies inside source addresses; it is not a firewall rule here.
- PAT can use a NAT pool or the outside interface address.
- Interface overload automatically uses the interface's current address.
- Changing NAT with active traffic can interrupt connections.
- Existing translations may need to be cleared before removing the old dynamic NAT rule.
- Session capacity is not simply and universally 65,535 per address.
- NAT does not replace routing, firewalls or security policy.

## Dynamic NAT Versus PAT

Dynamic NAT:

```text
192.168.10.21 <-> 216.0.5.50
192.168.10.22 <-> 216.0.5.51
192.168.10.23 <-> 216.0.5.52
```

Every active inside host occupies a separate public address.

PAT:

```text
192.168.10.21:51001 -> 216.0.5.2:30001
192.168.10.22:51001 -> 216.0.5.2:30002
192.168.10.23:62000 -> 216.0.5.2:30003
```

All clients use the same inside global address, while protocol and port or identifier information keeps translations unique.

| Property | Dynamic NAT | PAT / NAT overload |
| --- | --- | --- |
| Address relationship | One-to-one | Many-to-one or many-to-few |
| Public resources | One address per active host | One address for many flows |
| Distinction | IP addresses | IP, protocol and port/identifier |
| Common use | Temporary separate public identities | General internet access |
| Scalability | Public pool size | Device port/translation capacity |

## How PAT Distinguishes Connections

For TCP and UDP, a flow normally includes:

```text
protocol
inside local IP and port
inside global IP and translated port
outside IP and port
```

If two clients use the same source port, the router can change one translated source port:

```text
192.168.10.21:50000 -> 216.0.5.2:50000
192.168.10.22:50000 -> 216.0.5.2:50001
```

For ICMP, the translation table can use a query identifier instead of a TCP or UDP port.

Port Address Translation is therefore a useful name, but the mechanism should not be considered TCP/UDP-only.

## Prerequisites

Like other forms of inside source NAT, PAT requires:

1. Working IP addressing.
2. Routes to inside and outside networks.
3. `ip nat inside` on internal interfaces.
4. `ip nat outside` on the external interface.
5. An ACL matching eligible inside source addresses.
6. A NAT rule containing `overload`.

Interface roles:

```cisco
interface GigabitEthernet0/0
 description Cafe LAN
 ip nat inside

interface GigabitEthernet0/1
 description Fallout Shelter LAN
 ip nat inside

interface GigabitEthernet0/2
 description ISP uplink
 ip nat outside
```

ACL:

```cisco
access-list 1 permit 192.168.10.0 0.0.0.255
access-list 1 permit 192.168.20.0 0.0.0.255
```

## Option 1: PAT With A Public Pool

Suppose this pool exists:

```cisco
ip nat pool cafepublic 216.0.5.50 216.0.5.100 netmask 255.255.255.0
```

Ordinary dynamic NAT uses:

```cisco
ip nat inside source list 1 pool cafepublic
```

Enable overload:

```cisco
ip nat inside source list 1 pool cafepublic overload
```

The `overload` keyword changes the behavior. Public addresses can now support many concurrent translations instead of one active inside host per address.

### When Pool Overload Is Useful

- The organization owns several public addresses.
- One address does not provide sufficient session capacity.
- Translations should be distributed across multiple public identities.
- Policy or scale requires a public pool.

The router generally uses pool addresses as needed. Exact allocation behavior depends on the platform and IOS release, so capacity should be validated through documentation and measurement.

## Option 2: PAT On The Outside Interface

Smaller environments commonly use the external interface address:

```cisco
ip nat inside source list 1 interface GigabitEthernet0/2 overload
```

Read it as:

```text
For inside source addresses matched by ACL 1,
use the current IP address of GigabitEthernet0/2
and permit overload.
```

Complete configuration:

```cisco
enable
configure terminal

interface GigabitEthernet0/0
 description Cafe LAN
 ip nat inside

interface GigabitEthernet0/1
 description Fallout Shelter LAN
 ip nat inside

interface GigabitEthernet0/2
 description ISP uplink
 ip nat outside

access-list 1 permit 192.168.10.0 0.0.0.255
access-list 1 permit 192.168.20.0 0.0.0.255

ip nat inside source list 1 interface GigabitEthernet0/2 overload

end
```

## Why Interface Overload Is Useful

If the ISP assigns the outside address through DHCP, it can change:

```text
Yesterday: 198.51.100.20
Today:     198.51.100.47
```

The interface rule does not contain a hard-coded public IP:

```cisco
ip nat inside source list 1 interface GigabitEthernet0/2 overload
```

The router uses whichever address is currently configured on `GigabitEthernet0/2`. After DHCP renewal, the NAT rule still references the same interface.

This does not guarantee that an address change causes no brief disruption. Existing translations associated with the old address cannot continue unchanged. It does mean that the NAT configuration does not need to be rewritten manually for the new IP.

## Migrating From Dynamic NAT To PAT

Existing rule:

```cisco
ip nat inside source list 1 pool cafepublic
```

Target pool-overload rule:

```cisco
ip nat inside source list 1 pool cafepublic overload
```

Or interface overload:

```cisco
ip nat inside source list 1 interface GigabitEthernet0/2 overload
```

### Why The Old Rule Can Resist Removal

IOS can reject removal or modification of NAT configuration while translations are active. Even after clearing the table, background devices can recreate entries immediately:

- cameras;
- POS terminals;
- phones;
- monitoring agents;
- cloud applications;
- update services.

Treat a production NAT change as a potentially disruptive operation.

## A Safer Change Sequence

The exact procedure depends on topology, redundancy and platform, but a general plan is:

1. Save and review the current configuration.
2. Record active translations and statistics.
3. Prepare exact rollback commands.
4. Notify users and schedule a maintenance window.
5. Stop or redirect new traffic where the design permits.
6. Temporarily shut an affected inside or outside interface if necessary.
7. Clear dynamic translations.
8. Remove the old NAT rule.
9. Add the overload rule.
10. Restore interface operation.
11. Verify routing, NAT and application connectivity.
12. Monitor counters, logs and translation use.

Lab example:

```cisco
clear ip nat translation *
configure terminal
no ip nat inside source list 1 pool cafepublic
ip nat inside source list 1 interface GigabitEthernet0/2 overload
end
```

If translations return immediately, temporarily stopping traffic may be necessary. Do not casually issue `shutdown` on a production router; this is a planned outage with understood impact.

## Verifying PAT

Generate traffic from multiple inside hosts, then run:

```cisco
show ip nat translations
```

Example:

```text
Pro  Inside global       Inside local         Outside local       Outside global
tcp  216.0.5.2:30001     192.168.10.21:51001  203.0.113.10:443    203.0.113.10:443
tcp  216.0.5.2:30002     192.168.10.22:51001  203.0.113.10:443    203.0.113.10:443
udp  216.0.5.2:31001     192.168.20.15:53000  198.51.100.53:53    198.51.100.53:53
```

PAT indicators:

- different inside local addresses;
- the same inside global address;
- different translated ports or identifiers.

Additional commands:

```cisco
show ip nat statistics
show access-lists 1
show running-config | include ip nat
show ip interface brief
show ip route
```

Test real TCP and UDP applications in addition to ping.

## How Many Connections Fit Behind One Public IP

The transport port field is 16 bits, but saying that one public address always supports exactly 65,535 sessions is too simplistic.

Actual capacity depends on:

- protocol;
- reserved and usable port ranges;
- destination tuple reuse;
- the IOS allocation algorithm;
- hardware and software platform limits;
- memory;
- translation timeouts;
- traffic patterns;
- sessions per host;
- security and policy limits.

One endpoint can create hundreds or thousands of flows. Plan PAT capacity using measured concurrent translations and connection rates, not only the theoretical number of port values.

If one public address is insufficient, options include:

- pool overload;
- additional public addresses;
- a more capable edge platform;
- carefully tuned timeouts after analysis;
- IPv6 adoption;
- architectural traffic separation.

## PAT Is Not A Firewall

PAT normally lacks a translation for unsolicited inbound traffic, but this does not make it a complete security policy.

Separate controls are still required:

- stateful firewall;
- ACLs;
- segmentation;
- secure management plane;
- logging and monitoring;
- IDS/IPS where appropriate;
- endpoint patching;
- explicit static mappings only for required services.

NAT translates addresses; a firewall decides which traffic is allowed.

## Troubleshooting Order

If PAT does not work:

1. Verify the client IP, mask and default gateway.
2. Verify routing to the outside destination.
3. Check `ip nat inside` on the ingress interface.
4. Check `ip nat outside` on the egress interface.
5. Confirm that the source address matches the ACL.
6. Check ACL counters.
7. Confirm that the NAT rule contains `overload`.
8. For interface PAT, verify the outside interface address and state.
9. For pool PAT, verify the pool and provider routing.
10. Check the translation table and statistics.
11. Check firewall or ACL policy.
12. Test DNS separately from IP connectivity.
13. Check platform translation and session limits.

## Common Mistakes

### Omitting The Overload Keyword

```cisco
ip nat inside source list 1 pool cafepublic
```

This is dynamic NAT, not PAT.

### Referencing The Wrong Outside Interface

Interface overload uses the address of the specified interface. Verify the topology and `show ip interface brief`.

### Leaving Inside Networks Out Of The ACL

`ip nat inside` does not add a network to the ACL automatically.

### Active Translations Blocking The Change

Clearing the table interrupts sessions and requires maintenance planning.

### Treating PAT As Infinite

Translations, ports, memory and platform capacity are finite.

### Treating NAT As A Firewall

Translation and traffic authorization are separate functions.

## Quick Self-Check

### Question 1

What does `overload` do?

Answer:

```text
It allows multiple inside translations to share a public address
by distinguishing flows with protocol and port or identifier information.
```

### Question 2

Why is interface overload useful with ISP DHCP?

Answer:

```text
The NAT rule uses the interface's current address,
so a public IP is not hard-coded in the configuration.
```

### Question 3

Can PAT use a pool?

Answer:

```text
Yes: ip nat inside source list 1 pool cafepublic overload.
```

### Question 4

Why clear translations before changing NAT?

Answer:

```text
Active entries can retain the old rule,
and removing them terminates the associated sessions.
```

### Question 5

How can the translation table prove that PAT is active?

Answer:

```text
Multiple inside local addresses use the same inside global address
with different translated ports or identifiers.
```

## Commands / Terms

| Command / Term | Purpose |
| --- | --- |
| PAT | Port Address Translation. |
| NAT overload | Cisco term for sharing public addresses. |
| `overload` | Enables many-to-one or many-to-few translation. |
| `ip nat inside source list 1 pool cafepublic overload` | PAT with a public pool. |
| `ip nat inside source list 1 interface GigabitEthernet0/2 overload` | PAT using the outside interface address. |
| `show ip nat translations` | Displays addresses, protocols and ports. |
| `show ip nat statistics` | Displays NAT roles, counters and capacity data. |
| `clear ip nat translation *` | Removes dynamic translations and interrupts sessions. |
| Inside local | Internal address before translation. |
| Inside global | Address representing the inside host externally. |

## What To Review Later

- PAT translation tables
- TCP and UDP port allocation
- ICMP identifiers
- NAT timeouts
- NAT order of operations
- Hairpin NAT
- Stateful firewall behavior
- PAT capacity planning
