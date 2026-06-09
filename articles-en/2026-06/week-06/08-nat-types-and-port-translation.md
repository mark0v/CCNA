# NAT Types and Port Translation

Source: closed course page  
Date added: 2026-06-09  
Related plan item: Week 6 / NAT types and PAT  
Tags: NAT, static NAT, dynamic NAT, PAT, NAT overload, RFC 1918, ports, translation table
Language: English
Translation pair: articles/2026-06/week-06/08-nat-types-and-port-translation.md

## Summary

NAT became a practical way to connect private IPv4 networks to the public internet despite limited public address space. An edge device translates addresses and allows internal hosts to use public connectivity.

The three main forms are static NAT, which creates a permanent one-to-one mapping; dynamic NAT, which temporarily assigns an address from a public pool; and NAT overload/PAT, which lets many hosts share one public IP by using TCP or UDP port numbers.

## Key Points

- NAT is a practical response to public IPv4 address scarcity.
- RFC 1918 defines private IPv4 address ranges.
- Providers and internet routers normally filter private prefixes.
- Static NAT uses a permanent one-to-one mapping.
- Dynamic NAT allocates a temporary public address from a pool.
- NAT overload uses many-to-one translation.
- PAT distinguishes simultaneous sessions with transport ports.
- The router stores active mappings in a NAT translation table.
- NAT normally runs on an internet edge router or firewall.
- Troubleshooting should separate routes, NAT, DNS and security policy.

## Notes

### Why NAT Exists

IPv4 address space is limited.

If every device required a unique public IPv4 address, the available space would be insufficient.

NAT enabled organizations to:

- reuse private ranges internally;
- expose a public identity only at the edge;
- share one public address among many hosts;
- extend the practical life of IPv4.

NAT is useful, but it is a compatibility mechanism rather than a perfect replacement for global address space.

### RFC 1918 Private Ranges

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

These ranges are intended for internal use and can appear in many independent networks.

Private addresses are technically valid IPv4 addresses, but the public internet should not accept or advertise RFC 1918 prefixes.

### NAT At The Edge

NetworkChuck Coffee uses private addresses for:

- user devices;
- POS terminals;
- printers;
- cameras;
- internal servers.

At the boundary:

```text
Private LAN -> Edge router/firewall -> Public internet
```

The edge device translates address information and tracks sessions.

## Static NAT

Static NAT creates a permanent one-to-one mapping:

```text
192.168.1.50 <-> 216.0.5.10
```

Typical uses:

- an internal web server;
- a mail gateway;
- an externally reachable service;
- a device requiring a predictable public address;
- a legacy application using fixed allowlists.

### Advantages

- predictable mapping;
- supports inbound connections;
- easy to document;
- translation is always present.

### Limitations

- every mapping consumes a public address;
- less address-efficient than PAT;
- inbound service still requires firewall policy;
- exposed services require patching and monitoring.

## Dynamic NAT

Dynamic NAT creates temporary one-to-one mappings from a public pool.

Example:

```text
216.0.5.10 - 216.0.5.14
```

An internal host receives an available public address for the lifetime of its translation.

### Advantages

- automatic mappings;
- public addresses can be reused;
- no permanent assignment for every host.

### Limitations

- simultaneous translated hosts are limited by pool size;
- new translations fail when the pool is exhausted;
- a host's public identity can change;
- multiple public addresses are still required.

## NAT Overload / PAT

NAT overload is the common small-office and home-network form.

It is also called:

```text
PAT - Port Address Translation
```

Many private hosts share one public IP.

The router distinguishes flows using:

- protocol;
- inside local IP;
- inside local port;
- translated IP;
- translated port;
- outside destination.

### Example

```text
192.168.1.10:51000 -> 216.0.5.2:30001
192.168.1.20:51000 -> 216.0.5.2:30002
```

Both hosts use `216.0.5.2`, but with different translated ports.

### Why Ports Matter

TCP and UDP port numbers identify application sessions.

PAT can modify the source port so every active flow remains unique.

When a reply arrives at:

```text
216.0.5.2:30001
```

the router checks the translation table and forwards it to:

```text
192.168.1.10:51000
```

### Benefits

- one public IPv4 address supports many hosts;
- ideal for outbound internet access;
- conserves public address space;
- common at small-network edges.

### Constraints

- translation tables are finite;
- port exhaustion can occur at very large scale;
- inbound access requires explicit mapping or port forwarding;
- some protocols interact poorly with NAT;
- logs must map public ports back to internal sessions.

## Translation Table

A NAT device stores active mappings.

On Cisco IOS:

```cisco
show ip nat translations
```

Common columns include:

```text
Pro
Inside global
Inside local
Outside local
Outside global
```

Another useful command:

```cisco
show ip nat statistics
```

It can display:

- inside and outside interfaces;
- active translation counts;
- hits and misses;
- pools;
- configuration references.

## Choosing The NAT Type

| Requirement | Suitable Type |
| --- | --- |
| Fixed public address for one internal server | Static NAT |
| Temporary one-to-one mappings from several addresses | Dynamic NAT |
| Internet access for many users through one address | PAT / overload |

One network can use several NAT forms at the same time.

## NAT Is Not The Whole Internet Path

Working connectivity also requires:

- correct host IP and mask;
- a default gateway;
- a route to the ISP;
- a reachable ISP next hop;
- firewall or ACL permission;
- DNS when names are used;
- a return path;
- a working application.

If no translation appears, investigate NAT selection. If a translation exists but no reply arrives, investigate routing, the ISP and security policy.

## Troubleshooting Checklist

1. Verify inside-host addressing.
2. Verify the default route.
3. Verify inside and outside interface roles.
4. Verify the NAT traffic-selection rule.
5. Verify the public pool or overload interface.
6. Run `show ip nat translations`.
7. Run `show ip nat statistics`.
8. Check firewall or ACL policy.
9. Test DNS separately.
10. Clear stale translations only when necessary and with impact understood.

## Quick Self-Check

### Question 1

What are the three primary NAT forms?

Answer:

```text
Static NAT, dynamic NAT and NAT overload/PAT.
```

### Question 2

How does static NAT work?

Answer:

```text
It creates a permanent one-to-one mapping between private and public addresses.
```

### Question 3

What limits dynamic NAT?

Answer:

```text
The number of available public addresses in its pool.
```

### Question 4

How does PAT distinguish hosts sharing one public IP?

Answer:

```text
By using the protocol and translated TCP or UDP port numbers.
```

### Question 5

Which command displays active Cisco NAT mappings?

Answer:

```text
show ip nat translations
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Static NAT | Permanent one-to-one translation. |
| Dynamic NAT | Temporary one-to-one translation from a pool. |
| PAT | Port Address Translation. |
| NAT overload | Cisco term for many-to-one PAT. |
| Public pool | Set of public addresses used by dynamic NAT. |
| Translation table | Active NAT session mappings. |
| Source port | Transport port selected by the initiating host. |
| Port exhaustion | Lack of available translated port combinations. |
| `show ip nat translations` | Displays active mappings. |
| `show ip nat statistics` | Displays NAT configuration and counters. |

## What To Review Later

- Cisco NAT terminology
- Static NAT configuration
- Dynamic NAT pools
- PAT configuration
- NAT ACLs
- Port forwarding
- NAT logging
- NAT troubleshooting
