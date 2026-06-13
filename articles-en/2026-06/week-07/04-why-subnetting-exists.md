# Why Subnetting Exists

Source: closed course page  
Date added: 2026-06-13  
Related plan item: Week 7 / Why subnetting exists  
Tags: subnetting, subnet mask, CIDR, classful addressing, VLAN, broadcast domain, IP planning
Language: English
Translation pair: articles/2026-06/week-07/04-why-subnetting-exists.md

## Summary

Subnetting divides IP address space into networks sized for their actual purpose. Instead of one large shared network or inflexible classful sizes, an engineer chooses prefix lengths based on endpoint count, segment function, growth and security requirements.

The practical meaning of subnetting is broader than binary arithmetic. It is a design tool: guest Wi-Fi, POS terminals, cameras, office devices, servers and voice systems can receive separate address ranges and broadcast domains.

## Key Points

- Subnetting creates logical IP networks of suitable sizes.
- A subnet mask or CIDR prefix separates network bits from host bits.
- A longer prefix creates more networks with fewer addresses in each.
- A shorter prefix creates fewer networks with more addresses in each.
- Old classful sizes do not fit flexible modern requirements.
- An oversized subnet expands the broadcast domain and administrative scope.
- An undersized subnet exhausts addresses quickly.
- VLANs and subnets are commonly designed together but are different concepts.
- A router or Layer 3 switch connects different subnets.
- Subnetting supports segmentation, route summarization and scaling.
- A good address plan reserves room for growth.
- The mathematics is a means, not the final goal.

## The Problem Subnetting Solves

Consider one network:

```text
192.168.10.0/24
```

containing:

- guest Wi-Fi;
- POS terminals;
- office laptops;
- cameras;
- inventory devices;
- printers;
- servers.

The devices can technically share one range, but this flat network causes problems:

- every endpoint shares one broadcast domain;
- security policies are harder to express;
- guest and business traffic mix;
- troubleshooting has an unnecessarily broad scope;
- growth in one device category affects the others;
- documentation and ownership become unclear.

Subnetting divides the space according to purpose.

## An Intentional Segmentation Example

Instead of one `/24`:

```text
192.168.10.0/24
```

the design can use:

```text
192.168.10.0/25    Guest Wi-Fi
192.168.10.128/27  POS
192.168.10.160/27  Cameras
192.168.10.192/27  Office
192.168.10.224/28  Infrastructure
192.168.10.240/28  Reserved
```

This is only a learning example. A real plan depends on host counts, growth, DHCP, redundancy, gateways and operational policy.

Each segment receives:

- its own network address;
- a host-address range;
- an IPv4 broadcast address;
- a default gateway;
- a separate policy boundary;
- a clear purpose.

## What A Subnet Mask Does

An IPv4 address contains 32 bits. The subnet mask determines which bits describe the network and which remain in the host portion.

Example:

```text
IP address:  192.168.10.25
Mask:        255.255.255.0
CIDR:        /24
```

The first 24 bits belong to the network portion:

```text
Network: 192.168.10.0/24
```

The last 8 bits are used inside that subnet.

Another example:

```text
192.168.10.25/27
```

The network portion is now 27 bits and the host portion only 5 bits. Network boundaries occur every 32 addresses.

## Prefix Length Controls Size

| Prefix | Total addresses | Traditional usable hosts |
| --- | ---: | ---: |
| `/24` | 256 | 254 |
| `/25` | 128 | 126 |
| `/26` | 64 | 62 |
| `/27` | 32 | 30 |
| `/28` | 16 | 14 |
| `/29` | 8 | 6 |
| `/30` | 4 | 2 |

Traditional usable-host counts exclude the network and broadcast addresses. `/31` point-to-point links follow the special rules in RFC 3021, so the universal `total - 2` shortcut has exceptions.

The central relationship is:

```text
Longer prefix -> more subnets, fewer addresses per subnet
Shorter prefix -> fewer subnets, more addresses per subnet
```

## Why The Old Classes Were Inflexible

Historical classful addressing divided unicast IPv4 space into fixed sizes:

| Class | Default prefix | Approximate scale |
| --- | --- | --- |
| A | `/8` | Very large network |
| B | `/16` | Large network |
| C | `/24` | Small network |

Organizations frequently did not fit these sizes. A network needing 500 hosts cannot fit in a `/24`, while assigning an entire `/16` creates enormous address waste.

Modern design uses CIDR and variable prefix lengths. Class A/B/C terminology still appears in education and legacy discussion, but routing should no longer be designed around classful boundaries.

## Subnetting And CIDR

CIDR notation:

```text
192.168.10.0/24
```

states the number of network bits directly.

This permits prefixes such as:

```text
/19
/22
/27
/30
```

without relying on old address classes.

Subnetting generally divides a larger allocation into smaller prefixes. Supernetting or route aggregation represents contiguous prefixes with a shorter summary.

## Subnetting And VLANs

Subnets and VLANs are closely related but not identical:

- A VLAN creates a Layer 2 broadcast domain.
- An IP subnet defines a Layer 3 address domain.

A common design uses:

```text
one VLAN <-> one IP subnet
```

Example:

| VLAN | Purpose | Subnet |
| ---: | --- | --- |
| 10 | Office | `10.10.10.0/24` |
| 20 | POS | `10.10.20.0/26` |
| 30 | Cameras | `10.10.30.0/25` |
| 40 | Guest Wi-Fi | `10.10.40.0/23` |

Different subnets require Layer 3 forwarding from a router, multilayer switch or firewall.

## Why Not Use One Enormous Network

A large subnet does not necessarily fail immediately, but it increases operational blast radius.

Possible consequences:

- more broadcast and unknown-unicast traffic;
- more ARP or neighbor state;
- harder incident isolation;
- more difficult policy between groups;
- greater accidental lateral connectivity;
- harder migrations;
- less obvious ownership of address ranges.

Broadcast-domain size should follow requirements, not a habit of using `/24` or one shared network for everything.

## Why Not Make A Network Too Small

If a subnet fits only the current endpoints, growth quickly exhausts available addresses.

Account for:

- current endpoints;
- near-term growth;
- gateway addresses;
- DHCP exclusions;
- static infrastructure;
- redundancy addresses;
- monitoring and management interfaces;
- temporary devices;
- reserved capacity.

Example:

```text
Current: 25 cameras
Growth:  up to 40 cameras
```

A `/27` provides 30 traditional usable hosts and is too small. A `/26` provides 62 and leaves reasonable headroom.

## Subnetting As Business Design

Requests rarely say:

```text
Create some subnets.
```

They sound like:

- create a VLAN for cameras;
- isolate guest Wi-Fi;
- open a branch office;
- add VoIP phones;
- separate servers from users;
- produce an address plan for a VPN;
- the current DHCP scope is nearly full;
- summarize routes between sites.

Each request requires decisions about subnet sizes and boundaries.

## NetworkChuck Coffee Example

Requirements:

| Segment | Current devices | Expected growth |
| --- | ---: | ---: |
| Guest Wi-Fi | 70 | 110 |
| Office | 12 | 20 |
| POS | 8 | 12 |
| Cameras | 24 | 40 |
| Infrastructure | 6 | 10 |

Possible initial sizing:

| Segment | Candidate prefix | Traditional usable hosts |
| --- | --- | ---: |
| Guest Wi-Fi | `/25` | 126 |
| Office | `/27` | 30 |
| POS | `/28` | 14 |
| Cameras | `/26` | 62 |
| Infrastructure | `/28` | 14 |

The plan still needs validation:

- do the prefixes fit the available parent block;
- do any ranges overlap;
- is reserved space available;
- is summarization convenient;
- can DHCP supply the required leases;
- do VLAN IDs and policies align;
- are addresses reserved for gateway redundancy.

## Fixed-Length And Variable-Length Subnetting

### FLSM

Fixed-Length Subnet Mask uses the same prefix for every subnet.

Advantages:

- simple calculation;
- uniform segment sizes;
- easy documentation.

Disadvantages:

- address waste when requirements differ;
- the largest segment determines every subnet size.

### VLSM

Variable-Length Subnet Mask uses different prefixes:

```text
Guest: /25
Cameras: /26
Office: /27
POS: /28
```

Advantages:

- fits real requirements better;
- uses address space more efficiently;
- supports flexible hierarchical design.

Disadvantages:

- requires careful planning;
- mistakes can create overlaps;
- documentation becomes especially important.

## What You Must Be Able To Calculate

For an IPv4 address and prefix, determine:

1. Subnet mask.
2. Network address.
3. Broadcast address.
4. First host address.
5. Last host address.
6. Total addresses.
7. Traditional usable hosts.
8. The next subnet boundary.

For a design problem:

1. Determine the required number of subnets.
2. Estimate host counts with headroom.
3. Select prefixes.
4. Place ranges without overlap.
5. Reserve growth space.
6. Prepare route summaries.

## The Binary Foundation

Subnetting uses binary because masks operate on bits.

The last octet of `/27` is:

```text
Mask:    224
Binary:  11100000
```

Three one bits extend the network portion, leaving five zero bits in the host portion.

Address count:

```text
2^5 = 32
```

That is why a `/27` block contains 32 addresses.

Binary is not an unrelated abstract exercise. It explains why boundaries occur at `.0`, `.32`, `.64`, `.96` and so on.

## Core Formulas

For an ordinary IPv4 subnet with prefix `/p`:

```text
Host bits = 32 - p
Total addresses = 2^(host bits)
Traditional usable hosts = 2^(host bits) - 2
```

When dividing parent prefix `/P` into child prefix `/p`:

```text
Borrowed bits = p - P
Number of equal-size subnets = 2^(borrowed bits)
```

Apply these formulas with awareness of `/31` and `/32` exceptions and the requirements of the platform and use case.

## Design Mistakes

### Using `/24` Everywhere

It is visually convenient but can waste addresses or create oversized segments.

### Sizing Only For Current Hosts

Growth and infrastructure requirements quickly make the plan too tight.

### Confusing VLANs And Subnets

They belong to different layers and should be aligned intentionally.

### Creating Overlapping Ranges

Overlap causes ambiguity, routing problems and difficult migrations.

### Ignoring Summarization

Random range placement enlarges routing tables and complicates policy.

### Failing To Document Allocations

A range that looks free may already be reserved for another site or service.

## Practical Exercise

Given:

```text
Parent network: 10.50.0.0/22
```

Requirements:

- Guest: 200 hosts.
- Cameras: 90 hosts.
- Office: 45 hosts.
- POS: 20 hosts.
- Infrastructure: 10 hosts.

Tasks:

1. Choose practical minimum prefixes with growth headroom.
2. Place the largest subnet first.
3. Avoid overlap.
4. Record network, usable range and broadcast.
5. Leave contiguous free space.

Initial candidates:

```text
Guest:          /24
Cameras:        /25
Office:         /26
POS:            /27
Infrastructure: /28
```

This is not yet a final production design; reserve and future expansion still require validation.

## Learning Path

Work in layers:

1. Understand network and host portions.
2. Learn the relationship between prefix and mask.
3. Learn powers of two.
4. Find block sizes.
5. Identify network boundaries.
6. Calculate host ranges.
7. Divide a parent network into equal subnets.
8. Move to VLSM.
9. Connect subnets to VLAN and routing design.
10. Verify results with tools without replacing understanding.

## Quick Self-Check

### Question 1

Why does subnetting exist?

Answer:

```text
To create IP networks of suitable size and purpose
inside the available address space.
```

### Question 2

What does a prefix length define?

Answer:

```text
The number of bits belonging to the network portion of an IPv4 address.
```

### Question 3

What happens when a prefix changes from `/24` to `/26`?

Answer:

```text
It creates more, smaller subnets; each `/26` contains 64 total addresses.
```

### Question 4

Why are a VLAN and a subnet not the same thing?

Answer:

```text
A VLAN defines a Layer 2 broadcast domain,
while a subnet defines a Layer 3 address domain.
```

### Question 5

What is the real subnetting skill?

Answer:

```text
Not merely arithmetic, but selecting address boundaries
that match scale, growth, segmentation and routing design.
```

## Commands / Terms

| Term | Purpose |
| --- | --- |
| Subnet | Logical IP network inside a larger address space. |
| Subnet mask | A 32-bit mask separating network and host portions. |
| CIDR prefix | Number of network bits, such as `/27`. |
| Network address | First address identifying a subnet. |
| Broadcast address | Last address in a traditional IPv4 subnet. |
| FLSM | Same prefix for all child subnets. |
| VLSM | Different prefixes for different requirements. |
| VLAN | Layer 2 broadcast domain. |
| Route summarization | Representing multiple prefixes with one summary. |
| Address plan | Documented allocation of address space. |

## What To Review Later

- Binary IPv4 representation
- Powers of two
- Prefix-to-mask conversion
- Block sizes
- Network and broadcast calculation
- FLSM
- VLSM
- Route summarization
- IPv6 prefix planning
