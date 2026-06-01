# Initial IP Addressing Design

Source: closed course page  
Date added: 2026-06-01  
Related plan item: Week 5 / Initial addressing design for Castle Rysen  
Tags: ip addressing, network design, subnetting, cidr, broadcast domain, vlan, summarization, rfp
Language: English
Translation pair: articles/2026-05/week-05/03-initial-ip-addressing-design.md

## Summary

Initial IP addressing design starts not with random IP ranges, but with business requirements. You need to understand how many sites the organization has, which traffic types must be separated, where growth room is needed, and how the addressing plan will scale.

Main idea: a good addressing plan translates business requirements into predictable technical structure.

## Key Points

- Network design starts with requirements, not with random IPs.
- RFP helps reveal scale, sites, and segmentation needs.
- Network segment is a logical part of a network, usually a separate broadcast domain.
- Router stops broadcasts between network segments.
- District shop may need multiple segments: internal, voice, guest.
- VLANs are often used for logical separation inside one switching environment.
- `/24` means subnet mask `255.255.255.0`.
- For a shop, it is useful to allocate blocks of four `/24` networks: three active + one spare.
- Spare network leaves room for growth.
- Clean grouped addressing helps future route summarization.
- Predictable addressing simplifies troubleshooting, routing, and expansion.

## Notes

### Start With The Business

When the task is "address the network", do not just open a table and start typing IP ranges.

First, understand the business:

- how many locations;
- what types of sites;
- how sites relate to each other;
- how many users/devices;
- which traffic types must be separated;
- where growth is expected;
- which future services may appear.

For Castle Rysen, those answers come from the RFP.

RFP tells us:

- there is a central office;
- central office supports fallout shelters;
- fallout shelters support district shops;
- each district shop needs separate network segments.

This is already not a flat network.

This is a structured design problem.

### Translate Business Language Into Network Design

Business requirement:

```text
Separate internal communication, voice traffic and guest access.
```

Network designer hears:

```text
We need multiple network segments.
```

That translation step is important.

Business usually does not say:

```text
Create VLAN 10, VLAN 20 and VLAN 30 with separate subnets.
```

Business says:

```text
Employees, phones and guests should be separated.
```

Your job as a network person is to turn that into:

- segments;
- subnets;
- VLANs later;
- routing boundaries;
- security policy;
- addressing plan.

### What Is A Network Segment

A network segment is a separate logical part of a network where devices live in the same local network space.

Related term:

```text
broadcast domain
```

Broadcast domain answers the question:

```text
How far does a broadcast travel?
```

For example, an ARP request is a broadcast.

If broadcast stays inside one segment, that is good.

If broadcast starts going everywhere, the network becomes noisy quickly.

### Routers Stop Broadcasts

A router does not forward normal Layer 2 broadcasts between networks.

That is one of the key router jobs:

```text
Stop broadcasts at the network boundary.
```

When we create a routed boundary, we effectively create a separate network segment.

So if a district shop requires three segments, we think:

```text
Internal users = one segment
Voice devices  = one segment
Guest access   = one segment
```

Each segment should have its own IP network.

### VLAN Sidebar

In a real shop network, we usually do not build three physically separate networks.

We often use VLANs.

VLAN means:

```text
Virtual LAN
```

A VLAN lets one physical switching environment be split into multiple logical networks.

Example:

```text
VLAN 10 = Internal
VLAN 20 = Voice
VLAN 30 = Guest
```

We are not going deep into VLANs yet, but it is important to see that the RFP is already hinting at the future design direction.

### Why Use /24 For The First Design

At this stage, `/24` networks are easy to use.

`/24` means:

```text
255.255.255.0
```

It usually gives:

```text
254 usable host addresses
```

For a small district shop, this is enough for:

- registers;
- laptops;
- phones;
- printers;
- guest Wi-Fi clients;
- cameras;
- tablets;
- access points.

`/24` is also easy to read and easy to teach.

Later, we can make subnetting more efficient, but initial high-level design should stay understandable.

### Shop Addressing Pattern

For the first shop, allocate four `/24` networks:

```text
192.168.0.0/24  = Shop 1 Internal
192.168.1.0/24  = Shop 1 Voice
192.168.2.0/24  = Shop 1 Guest
192.168.3.0/24  = Shop 1 Spare
```

Why four?

Because we need three active segments now, but the spare leaves room for growth.

Future use cases:

- cameras;
- IoT devices;
- dedicated management network;
- security systems;
- separate payment devices;
- new business service.

Spare space helps avoid redesigning the addressing plan at the first change.

### Blocks Of Four

The next shop receives the next block of four:

```text
192.168.4.0/24  = Shop 2 Internal
192.168.5.0/24  = Shop 2 Voice
192.168.6.0/24  = Shop 2 Guest
192.168.7.0/24  = Shop 2 Spare
```

Third shop:

```text
192.168.8.0/24   = Shop 3 Internal
192.168.9.0/24   = Shop 3 Voice
192.168.10.0/24  = Shop 3 Guest
192.168.11.0/24  = Shop 3 Spare
```

Pattern:

```text
Shop 1 = 0-3
Shop 2 = 4-7
Shop 3 = 8-11
```

This is clean, predictable, and expandable.

### Why Grouping Matters

Grouping networks in clean blocks helps later with:

- troubleshooting;
- documentation;
- site identification;
- route summarization;
- avoiding overlap;
- faster mental parsing.

Route summarization means we can represent multiple related networks with one larger route.

You do not need to know all the mechanics yet, but the idea is important:

```text
Clean blocks today can mean cleaner routing tomorrow.
```

If addressing is random, future routing tables and troubleshooting become painful.

### Thinking Beyond One Shop

If designing the enterprise from day one, it may be logical to use a larger private range:

```text
10.0.0.0/8
```

Why?

Castle Rysen may have:

- central office;
- many fallout shelters;
- many district shops;
- regions;
- guest networks;
- voice networks;
- internal networks;
- future services.

A large range gives room.

But for learning, it is better to focus first on one district shop.

If we solve the entire global design before understanding one shop, there are too many moving parts.

### Fallout Shelters And Address Space Planning

For fallout shelters, we can start from another end of the range or allocate separate blocks to avoid overlap with shop allocations.

That is not random.

Good design:

- leaves space for shops;
- leaves space for shelters;
- leaves space for central office;
- avoids overlap;
- uses predictable patterns.

Predictable addressing looks boring.

That is good.

In large networks, boring and predictable is powerful.

### CIDR Term

CIDR stands for:

```text
Classless Inter-Domain Routing
```

CIDR notation uses prefix length:

```text
192.168.0.0/24
```

`/24` tells us how many bits belong to the network portion.

Equivalent decimal mask:

```text
255.255.255.0
```

CIDR lets us move beyond old classful boundaries and design networks flexibly.

### Design Process

Useful process:

1. Read requirements.
2. Identify sites.
3. Identify traffic groups.
4. Decide required segments.
5. Pick private address space.
6. Assign predictable blocks.
7. Leave spare networks.
8. Document everything.
9. Check for overlap.
10. Think about future routing and summarization.

Do not start with IPs.

Start with the structure.

### Real World Tip

When building an addressing plan:

```text
Do not solve only today's problem.
```

Leave room for:

- growth;
- new sites;
- new services;
- security separation;
- route summarization;
- future troubleshooting.

Future-you will be very happy when expansion does not require renumbering every device.

## Example Addressing Plan

### Shop 1

| Segment | Network | Purpose |
| --- | --- | --- |
| Internal | `192.168.0.0/24` | Employee devices and internal systems. |
| Voice | `192.168.1.0/24` | IP phones and voice devices. |
| Guest | `192.168.2.0/24` | Guest Wi-Fi clients. |
| Spare | `192.168.3.0/24` | Future growth. |

### Shop 2

| Segment | Network | Purpose |
| --- | --- | --- |
| Internal | `192.168.4.0/24` | Employee devices and internal systems. |
| Voice | `192.168.5.0/24` | IP phones and voice devices. |
| Guest | `192.168.6.0/24` | Guest Wi-Fi clients. |
| Spare | `192.168.7.0/24` | Future growth. |

### Shop 3

| Segment | Network | Purpose |
| --- | --- | --- |
| Internal | `192.168.8.0/24` | Employee devices and internal systems. |
| Voice | `192.168.9.0/24` | IP phones and voice devices. |
| Guest | `192.168.10.0/24` | Guest Wi-Fi clients. |
| Spare | `192.168.11.0/24` | Future growth. |

## Practice Exercise

Use `172.16.0.0` private range.

Address three cafes.

Each cafe needs:

- internal segment;
- voice segment;
- guest segment;
- one spare network.

Use `/24` networks.

One possible answer:

```text
Cafe 1 Internal = 172.16.0.0/24
Cafe 1 Voice    = 172.16.1.0/24
Cafe 1 Guest    = 172.16.2.0/24
Cafe 1 Spare    = 172.16.3.0/24

Cafe 2 Internal = 172.16.4.0/24
Cafe 2 Voice    = 172.16.5.0/24
Cafe 2 Guest    = 172.16.6.0/24
Cafe 2 Spare    = 172.16.7.0/24

Cafe 3 Internal = 172.16.8.0/24
Cafe 3 Voice    = 172.16.9.0/24
Cafe 3 Guest    = 172.16.10.0/24
Cafe 3 Spare    = 172.16.11.0/24
```

The pattern is the point.

## Quick Self-Check

### Question 1

What should network design start with?

Answer:

```text
Business requirements.
```

### Question 2

What is a broadcast domain?

Answer:

```text
The area where a broadcast message can travel before a router or boundary stops it.
```

### Question 3

Why use one spare `/24` per shop?

Answer:

```text
To leave room for future growth without redesigning the addressing plan.
```

### Question 4

What does `/24` mean?

Answer:

```text
A 24-bit network prefix, equivalent to subnet mask 255.255.255.0.
```

### Question 5

Why group networks in clean blocks?

Answer:

```text
It helps documentation, troubleshooting, growth and future route summarization.
```

## Commands / Terms

| Term | Meaning |
| --- | --- |
| RFP | Request for proposal, document with business/project requirements. |
| Network segment | Separate logical part of a network. |
| Broadcast domain | Area where broadcast traffic is heard. |
| VLAN | Virtual LAN, logical Layer 2 separation inside switching infrastructure. |
| CIDR | Classless Inter-Domain Routing. |
| `/24` | Prefix length equivalent to `255.255.255.0`. |
| Route summarization | Representing multiple related networks with one larger route. |
| Spare network | Reserved network for future use. |
| Addressing plan | Structured assignment of IP ranges to sites and segments. |

## What To Review Later

- Subnet masks
- Private IP addresses
- VLANs
- Broadcast domains
- CIDR notation
- Route summarization
- Inter-VLAN routing
- Network documentation

