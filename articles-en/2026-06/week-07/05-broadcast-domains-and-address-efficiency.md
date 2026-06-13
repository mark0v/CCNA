# Broadcast Domains And Address Efficiency

Source: closed course page  
Date added: 2026-06-13  
Related plan item: Week 7 / Broadcast domains and address efficiency  
Tags: subnetting, broadcast domain, ARP, DHCP, point-to-point, address efficiency, subnet sizing
Language: English
Translation pair: articles/2026-06/week-07/05-broadcast-domains-and-address-efficiency.md

## Summary

Subnetting solves two fundamental problems:

1. It divides oversized broadcast domains into manageable segments.
2. It allocates only the IP address space a segment reasonably needs.

A large flat network makes many devices receive local broadcasts and expands the impact of faults. An oversized subnet on a tiny link wastes address space. Good design sizes a network according to its purpose, endpoint count and expected growth.

## Key Points

- IPv4 broadcasts remain inside a Layer 2 broadcast domain.
- ARP and the initial stages of DHCP use broadcast.
- A router does not forward Layer 2 broadcasts between ordinary routed interfaces.
- VLAN and subnet boundaries limit broadcast scope.
- Smaller broadcast domains simplify policy, troubleshooting and fault isolation.
- Subnet size should match actual endpoint requirements.
- A `/24` provides 256 total addresses and traditionally 254 usable host addresses.
- A `/30` provides 4 total addresses and traditionally 2 usable addresses.
- A `/31` can use both addresses on an IPv4 point-to-point link under RFC 3021.
- Public IPv4 space is especially important to allocate efficiently.
- The smallest possible subnet is not always the best operational choice.

## Reason 1: Controlling The Broadcast Domain

A broadcast is intended for every device in the local broadcast domain.

IPv4 and Ethernet mechanisms involving broadcast include:

- an ARP request seeking the MAC address for a known IPv4 host;
- DHCP Discover before a client knows the DHCP server;
- DHCP Request during some lease stages;
- some discovery and legacy protocols;
- Layer 2 unknown-destination behavior before a switch learns a MAC address.

An individual broadcast is not necessarily a serious load. Problems arise when a domain becomes excessively large, contains many active endpoints or includes noisy and faulty devices.

## ARP Example

Host `192.168.10.21/24` wants to send a packet to neighbor `192.168.10.50`.

It must learn the destination MAC:

```text
Who has 192.168.10.50?
Tell 192.168.10.21.
```

The ARP request uses the Ethernet broadcast address:

```text
ff:ff:ff:ff:ff:ff
```

Every device in the Layer 2 segment receives the frame, though only the address owner should answer.

If the destination is in another subnet, the host resolves the MAC of its default gateway. The router then forwards the Layer 3 packet into another network. The original ARP broadcast does not pass through the router as an ordinary broadcast.

## DHCP Example

Before receiving an address, a new client does not know:

- its own IPv4 address;
- the DHCP server address;
- the default gateway;
- the subnet mask.

The initial DHCP Discover therefore uses broadcast:

```text
Client -> DHCP Discover -> local broadcast domain
```

If the DHCP server is in another subnet, a router or Layer 3 switch can provide DHCP relay, for example with `ip helper-address`. The relay converts the local client request into a routable exchange with the server.

The subnet boundary limits the original broadcast without preventing centralized DHCP when relay is configured correctly.

## Why One Giant Network Is Difficult

Suppose an organization uses:

```text
10.0.0.0/8
```

as one flat subnet.

It provides enormous address capacity, but creates a poor broadcast-domain design:

- broadcasts reach an enormous endpoint population;
- ARP tables and Layer 2 state grow;
- spanning-tree and switching incidents have a large blast radius;
- guests, office devices, cameras and payment systems are too close;
- security policy requires extra controls within one shared segment;
- troubleshooting is less localized;
- duplicate addresses or loops can affect too many users.

Owning a large allocation does not mean it should be one subnet.

## Subnets And Broadcast Domains

A common enterprise design uses:

```text
One VLAN = one Layer 2 broadcast domain
One VLAN = one primary IP subnet
```

Example:

| VLAN | Purpose | Subnet |
| ---: | --- | --- |
| 10 | Office | `10.20.10.0/24` |
| 20 | POS | `10.20.20.0/27` |
| 30 | Cameras | `10.20.30.0/26` |
| 40 | Guest | `10.20.40.0/23` |

A router, multilayer switch or firewall forwards traffic between these networks and provides a policy enforcement point.

Subnetting alone does not create security. If inter-VLAN routing permits everything, the segments can still communicate. Subnet boundaries provide locations where policy can be expressed and controlled.

## Not All Broadcasts Are Bad

Do not turn "broadcasts are bad" into an absolute rule.

Normal broadcasts are part of IPv4 LAN operation, and a modern switched network typically handles a reasonable volume.

Choose segment size based on:

- endpoint count;
- application broadcast and multicast behavior;
- wireless-client density;
- ARP and neighbor scale;
- fault isolation;
- security zones;
- device capability;
- operational simplicity.

The goal is to control broadcast scope, not eliminate broadcasts entirely.

## Reason 2: Efficient Address Allocation

Every subnet allocation consumes an aligned block.

If a link connects only two router interfaces, using a `/24` means:

```text
Total addresses: 256
Traditional usable: 254
Required endpoints: 2
```

Most of the block remains unused.

With private addressing, this can look harmless, but poor planning:

- fragments the allocation;
- harms summarization;
- creates inconsistency;
- complicates growth;
- establishes bad habits before public-space design.

With public IPv4, waste has a direct cost and consumes a scarce resource.

## `/30` For A Point-To-Point Link

A traditional IPv4 point-to-point subnet:

```text
192.0.2.0/30
```

contains:

| Address | Role |
| --- | --- |
| `192.0.2.0` | Network address |
| `192.0.2.1` | Router A |
| `192.0.2.2` | Router B |
| `192.0.2.3` | Broadcast address |

Result:

```text
4 total addresses
2 traditional usable addresses
```

It fits a two-endpoint link well and has broad support.

## `/31` And RFC 3021

Modern point-to-point links often use `/31`:

```text
192.0.2.0/31
```

Addresses:

```text
192.0.2.0
192.0.2.1
```

RFC 3021 permits both addresses as interface addresses because a point-to-point link does not require traditional network and broadcast semantics.

Benefits:

- two addresses instead of four;
- no two-address loss on each link;
- significant savings across many WAN links.

Before using it, verify:

- support on both devices;
- provider requirements;
- monitoring and management tools;
- routing protocol behavior;
- organizational standards.

`/30` is often simpler in beginner labs, but `/31` is a normal modern design.

## Size Comparison

| Prefix | Total addresses | Traditional usable hosts | Common example |
| --- | ---: | ---: | --- |
| `/24` | 256 | 254 | User LAN |
| `/26` | 64 | 62 | Cameras |
| `/27` | 32 | 30 | POS |
| `/28` | 16 | 14 | Infrastructure |
| `/30` | 4 | 2 | Traditional point-to-point |
| `/31` | 2 | 2 on point-to-point | Efficient point-to-point |
| `/32` | 1 | Single host route | Loopback or host route |

This is not an automatic design guide. Prefix selection depends on requirements.

## Custom Fit Instead Of Habit

Weak approach:

```text
We always use /24.
```

Better approach:

```text
How many endpoints are required?
What growth is expected?
What is the traffic pattern?
What policy boundary is needed?
How does the range fit the parent allocation?
Can the routes be summarized?
```

Choose the prefix after answering these questions.

## NetworkChuck Coffee Example

Requirements:

| Segment | Endpoints | Growth target |
| --- | ---: | ---: |
| Guest Wi-Fi | 80 | 120 |
| Employees | 18 | 28 |
| POS | 8 | 12 |
| Cameras | 24 | 40 |
| Router link | 2 | 2 |

Candidates:

| Segment | Prefix | Capacity rationale |
| --- | --- | --- |
| Guest Wi-Fi | `/25` | 126 traditional usable |
| Employees | `/27` | 30 traditional usable |
| POS | `/28` | 14 traditional usable |
| Cameras | `/26` | 62 traditional usable |
| Router link | `/30` or `/31` | Two endpoints |

Prefix selection is not based only on current hosts. Guest Wi-Fi might require a larger DHCP pool because of client churn, while an infrastructure subnet can reserve addresses for redundancy.

## Broadcast Reduction Does Not Mean Less Internet Traffic

Subnetting does not automatically reduce application traffic that must cross networks or reach the Internet.

It:

- limits Layer 2 broadcast scope;
- forces inter-subnet traffic through a Layer 3 device;
- creates policy and observation points;
- localizes failures.

If applications communicate frequently across segments, routed traffic remains. Segmentation should account for communication flows.

## The Cost Of Excessive Segmentation

Too many tiny subnets also create overhead:

- more VLANs and SVIs;
- more DHCP scopes;
- more routes;
- more ACL and firewall rules;
- more documentation;
- harder migrations and troubleshooting;
- greater risk of exhausting a small segment.

Subnetting optimizes a design; it does not require every network to be as small as mathematically possible.

## Network And Broadcast Addresses

In a traditional IPv4 subnet:

- the first address identifies the network;
- the last is the directed broadcast address;
- addresses between them are assigned to interfaces.

For:

```text
192.168.50.0/24
```

the values are:

```text
Network:    192.168.50.0
First host: 192.168.50.1
Last host:  192.168.50.254
Broadcast:  192.168.50.255
```

Exceptions include:

- `/31` point-to-point under RFC 3021;
- `/32`, representing one address;
- platform-specific or protocol-specific use cases.

## Practical Exercise

Given:

```text
Parent block: 10.60.0.0/23
```

Place:

- Guest Wi-Fi: 100 endpoints.
- Cameras: 45 endpoints.
- POS: 12 endpoints.
- Management: 10 endpoints.
- Two point-to-point links.

Tasks:

1. Select prefixes with reasonable headroom.
2. Decide between `/30` and `/31` for the links.
3. Allocate blocks from largest to smallest.
4. Record network and broadcast for ordinary subnets.
5. Avoid overlap.
6. Leave contiguous free space.

Possible sizes:

```text
Guest:      /25
Cameras:    /26
POS:        /28
Management: /28
Links:      /30 or /31
```

## Design Validation Order

1. Confirm endpoint requirements.
2. Add growth headroom.
3. Choose the smallest practical prefix.
4. Verify network-boundary alignment.
5. Check for overlap.
6. Check gateway and infrastructure reservations.
7. Check DHCP capacity.
8. Confirm broadcast-domain intent.
9. Check route summarization.
10. Document the allocation.

## Common Mistakes

### Treating Every Large Network As A Broadcast Storm

A larger domain increases risk and scope, but actual load depends on devices and traffic.

### Treating Subnetting As A Complete Security Policy

Segmentation creates a boundary; routing and firewall or ACL rules control access.

### Always Choosing The Minimum Prefix

Operations and growth require headroom.

### Always Using `/30` On Point-To-Point Links

`/30` is valid, but `/31` can be more efficient when supported.

### Using `/31` Without Validation

Standards, tools or provider designs can require `/30`.

### Ignoring The Parent Allocation

Correctly sized child subnets must still fit the assigned block.

## Quick Self-Check

### Question 1

Which two main problems does subnetting solve?

Answer:

```text
It limits broadcast domains and allocates address space
according to segment requirements.
```

### Question 2

Why does every local device receive an ARP request?

Answer:

```text
The sender uses an Ethernet broadcast to discover
the unknown destination MAC address.
```

### Question 3

Why is a `/24` a poor fit for a two-endpoint link?

Answer:

```text
It allocates 256 addresses to a task requiring only two.
```

### Question 4

How does `/31` differ from traditional `/30`?

Answer:

```text
On a supported point-to-point link, both `/31` addresses
are used by the endpoints without separate network and broadcast addresses.
```

### Question 5

Does subnetting reduce all network traffic?

Answer:

```text
No. It limits Layer 2 broadcast scope,
while required routed application traffic remains.
```

## Commands / Terms

| Term | Purpose |
| --- | --- |
| Broadcast domain | Layer 2 scope receiving broadcast frames. |
| ARP | Maps an IPv4 address to a MAC address in a local segment. |
| DHCP relay | Forwards DHCP exchanges between subnets. |
| Point-to-point | Link between exactly two Layer 3 endpoints. |
| `/30` | Traditional point-to-point subnet with two usable hosts. |
| `/31` | RFC 3021 point-to-point subnet with two usable addresses. |
| Network address | Identifier of a traditional subnet. |
| Broadcast address | Last address in a traditional IPv4 subnet. |
| Address efficiency | Matching allocation size to actual need. |
| Blast radius | Scope affected by a failure or incident. |

## What To Review Later

- ARP process
- DHCP DORA
- DHCP relay
- Ethernet broadcasts
- VLAN boundaries
- `/30`, `/31` and `/32`
- VLSM allocation
- Route summarization
