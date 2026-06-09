# Cisco NAT Terminology

Source: closed course page  
Date added: 2026-06-09  
Related plan item: Week 6 / Cisco NAT address terminology  
Tags: NAT, inside local, inside global, outside local, outside global, Cisco IOS, address translation
Language: English
Translation pair: articles/2026-06/week-06/10-cisco-nat-terminology.md

## Summary

Cisco describes NAT addresses with two pairs of terms: `inside/outside` and `local/global`. Inside or outside identifies the side to which a host belongs. Local or global describes how the address is represented from the relevant perspective.

In a typical outbound PAT scenario, the inside local address is often private, the inside global address is public, and the outside global address is the public internet-server address. However, local does not always literally mean private and global does not always literally mean public; these are translation roles.

## Key Points

- Inside refers to hosts on the internal side of NAT.
- Outside refers to hosts on the external side.
- Inside local is the inside host address as seen on the inside.
- Inside global represents the inside host on the outside.
- Outside global is the real outside-host address on the outside.
- Outside local represents the outside host on the inside.
- In simple internet NAT, inside local is commonly private and inside global public.
- Outside local and outside global commonly match when the outside address is not translated.
- NAT terminology is based on perspective and representation.
- Understanding the terms makes `show ip nat translations` easier to read.

## Notes

### Why The Terms Matter

NAT configuration and verification use Cisco terminology.

Without it, these columns look arbitrary:

```text
Inside global
Inside local
Outside local
Outside global
```

They answer two questions:

1. Does this host belong to the inside or outside?
2. How is its address represented locally or globally?

### Inside And Outside

`Inside` normally means the network managed by the organization whose addresses are being translated.

NetworkChuck Coffee examples:

- cafe laptop;
- POS terminal;
- internal server;
- guest client;
- inside side of the edge router.

`Outside` refers to the external network and its hosts:

- internet server;
- cloud API;
- public DNS server;
- ISP side.

Inside and outside describe side and ownership context, not address type.

### Local And Global

More precisely:

- `local` is the address used or visible in the local address domain;
- `global` is the address used or visible in the global/external address domain.

A beginner shortcut is:

```text
local often looks private
global often looks public
```

But this is not universal.

An organization can use public space internally, and an outside local address does not have to be private. Think in terms of representation rather than RFC 1918 versus public.

## Inside Local

The inside local address is the inside host's address in the internal network.

Example:

```text
192.168.1.50
```

It is configured on the POS terminal or laptop.

In typical IPv4 NAT it is private, but the definition does not require that.

```text
Inside local = how the inside host is addressed on the inside.
```

## Inside Global

The inside global address represents the inside host in the external/global network.

Example:

```text
216.0.5.2
```

With PAT, many inside local addresses can share one inside global address through different port numbers.

```text
192.168.1.50:51000 -> 216.0.5.2:30001
192.168.1.60:52000 -> 216.0.5.2:30002
```

```text
Inside global = how the inside host appears outside.
```

## Outside Global

The outside global address is the real address of the outside host in the external network.

If a cafe PC contacts:

```text
8.8.8.8
```

then `8.8.8.8` is normally the outside global address.

```text
Outside global = how the outside host is addressed on the outside.
```

## Outside Local

The outside local address represents the outside host in the internal/local network.

In most simple internet PAT scenarios, the outside address is not translated:

```text
Outside local  = 8.8.8.8
Outside global = 8.8.8.8
```

They are equal.

Outside local differs when NAT changes how the outside host is represented to the inside network.

Uses include:

- overlapping address spaces after a merger;
- a legacy device expecting a destination in a particular range;
- policy-driven bidirectional NAT;
- network integration during migration.

### Outside Local Example

Actual outside server:

```text
Outside global: 203.0.113.50
```

Inside users contact an alias:

```text
Outside local: 10.200.0.50
```

The NAT device translates:

```text
10.200.0.50 <-> 203.0.113.50
```

The inside host sees a local-style destination even though the real host is outside.

## Typical PAT Conversation

Cafe PC:

```text
Inside local: 192.168.1.50
```

Cafe edge public address:

```text
Inside global: 216.0.5.2
```

Internet server:

```text
Outside local: 8.8.8.8
Outside global: 8.8.8.8
```

Translation:

```text
Inside local 192.168.1.50:51000
-> Inside global 216.0.5.2:30001
-> Outside global 8.8.8.8:53
```

| Term | Typical Meaning | Example |
| --- | --- | --- |
| Inside local | Inside address before translation | `192.168.1.50` |
| Inside global | Address representing the inside host outside | `216.0.5.2` |
| Outside global | Real external-host address | `8.8.8.8` |
| Outside local | External-host address as seen inside | `8.8.8.8` or translated alias |

## Reading Cisco NAT Output

Command:

```cisco
show ip nat translations
```

Example:

```text
Pro  Inside global       Inside local        Outside local       Outside global
icmp 216.0.5.2:1         192.168.1.50:1      1.1.1.1:1           1.1.1.1:1
```

Interpretation:

- the private inside host is `192.168.1.50`;
- it appears outside as `216.0.5.2`;
- the outside host is `1.1.1.1`;
- the outside address is not translated, so its local/global values match.

## A Better Memory Method

Do not memorize four disconnected definitions.

For each address, ask:

```text
Whose host is it?
How is that host represented from this perspective?
```

Then:

```text
Inside local   = our host, inside representation
Inside global  = our host, outside representation
Outside global = their host, outside representation
Outside local  = their host, inside representation
```

## Overlapping Networks

NAT can help when two organizations use the same prefix:

```text
Company A: 10.10.0.0/16
Company B: 10.10.0.0/16
```

During temporary integration, one side can be represented as:

```text
10.200.0.0/16
```

This supports coexistence while long-term renumbering or redesign occurs.

Such NAT complicates:

- troubleshooting;
- logging;
- application dependencies;
- DNS;
- security policy;
- documentation.

It is useful as a migration tool, not always as an ideal permanent architecture.

## Common Mistakes

### Mistake 1: Local Always Means Private

Often, but not necessarily.

Local describes perspective or address domain.

### Mistake 2: Global Means The ISP Owns It

Inside global represents the inside host outside. The address can be provider-assigned, organization-owned or obtained another way.

### Mistake 3: Outside Local Is Always Different

In ordinary PAT, outside local and outside global commonly match.

### Mistake 4: Inside Means The Router Interface

Inside terminology describes hosts and addresses on the inside side. The separate `ip nat inside` command marks an interface role.

## Practical Exercise

Draw:

```text
PC -> NAT Router -> Internet Server
```

Assign:

```text
PC: 192.168.1.50
Router public: 216.0.5.2
Server: 1.1.1.1
```

Label:

- inside local;
- inside global;
- outside local;
- outside global.

Then repeat with an outside alias so outside local differs from outside global.

## Quick Self-Check

### Question 1

What is inside local?

Answer:

```text
The inside host address used in the internal network before translation.
```

### Question 2

What is inside global?

Answer:

```text
The address representing the inside host in the external/global network.
```

### Question 3

Why do outside local and outside global often match?

Answer:

```text
Ordinary outbound NAT does not translate the outside destination address.
```

### Question 4

Does local always mean private?

Answer:

```text
No. That is a common-case shortcut; the term describes representation and perspective.
```

### Question 5

When can outside local differ?

Answer:

```text
When an outside host is represented to the inside network through a translated alias, such as with overlapping networks.
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Inside local | Inside host address in the inside network. |
| Inside global | Address representing the inside host outside. |
| Outside global | Actual outside-host address in the outside network. |
| Outside local | Address representing the outside host inside. |
| `ip nat inside` | Marks an interface as the NAT inside side. |
| `ip nat outside` | Marks an interface as the NAT outside side. |
| `show ip nat translations` | Displays translations using Cisco terminology. |
| Address domain | Context in which an address representation is used. |
| Overlapping network | Networks using conflicting address space. |

## What To Review Later

- Static NAT syntax
- Dynamic NAT syntax
- PAT syntax
- Inside/outside interface roles
- NAT order of operations
- Overlapping-network translation
- NAT troubleshooting
