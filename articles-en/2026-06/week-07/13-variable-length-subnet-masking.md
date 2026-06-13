# Variable Length Subnet Masking

Source: closed course page  
Date added: 2026-06-13  
Related plan item: Week 7 / Variable Length Subnet Masking  
Tags: VLSM, subnetting, IPv4, address planning, host requirements, point-to-point
Language: English
Translation pair: articles/2026-06/week-07/13-variable-length-subnet-masking.md

## Summary

VLSM, or Variable Length Subnet Masking, uses different prefixes inside one parent address block.

Instead of assigning the same mask everywhere:

```text
Every subnet = /26
```

size each segment for its actual need:

```text
Large LAN:  /26
Small LAN:  /27
WAN link:   /30
```

The subnetting algorithm does not change. For every requirement:

1. Determine the required usable hosts.
2. Find the smallest practical prefix.
3. Allocate from largest to smallest.
4. Validate alignment, overlap and remaining space.

## Key Points

- FLSM uses one mask for every child subnet.
- VLSM uses masks of different lengths.
- Every VLSM allocation is still a normal CIDR subnet.
- Sort requirements from largest to smallest.
- Allocate large blocks first.
- Every network must begin on a boundary valid for its prefix.
- Child subnets must not overlap.
- Every allocation must stay inside the parent block.
- Account for network and broadcast in every ordinary subnet.
- Preserve contiguous free space when practical.
- Routing protocols must support classless prefixes.

## FLSM And VLSM

### FLSM

```text
Fixed Length Subnet Mask
```

Every child network uses the same prefix.

Advantages:

- simple calculation;
- equal capacity;
- predictable increments.

Disadvantage:

- address waste when segment sizes differ significantly.

### VLSM

```text
Variable Length Subnet Mask
```

Different child networks use different prefixes.

Advantages:

- allocation matches actual requirements;
- less waste;
- LANs, infrastructure and WAN links can share one plan efficiently.

Cost:

- alignment and overlap require more care;
- documentation becomes more important;
- summarization requires planning.

## Why Largest Comes First

A large subnet requires a large contiguous aligned block.

Small blocks are easier to fit into remaining space. Allocating `/30` and `/28` blocks first without a complete plan can fragment space needed by a later `/25` or `/26`.

Practical rule:

```text
Sort requirements from largest to smallest.
Allocate in that order.
```

## Working Algorithm

1. Confirm the parent network and prefix.
2. Gather host requirements for every segment.
3. Add gateways, infrastructure and growth headroom.
4. Find each prefix using `2^h - 2`.
5. Sort allocations by total block size, largest first.
6. Begin at the first free aligned boundary.
7. Record network, usable range and broadcast.
8. Move to the first address after the allocation.
9. Verify alignment for the next block.
10. Repeat for every requirement.
11. Check for overlap.
12. Record remaining free ranges.

## NetworkChuck Coffee Example

Parent block:

```text
192.168.10.0/24
```

Requirements:

| Segment | Required usable hosts |
| --- | ---: |
| Main Cafe | 50 |
| Office | 50 |
| Kiosk A | 20 |
| Kiosk B | 20 |
| WAN Link 1 | 2 |
| WAN Link 2 | 2 |

## Step 1: Select Each Prefix

### 50 Hosts

```text
2^5 - 2 = 30   insufficient
2^6 - 2 = 62   sufficient
```

```text
Prefix: /26
Block:  64 addresses
```

Two `/26` blocks are required.

### 20 Hosts

```text
2^4 - 2 = 14   insufficient
2^5 - 2 = 30   sufficient
```

```text
Prefix: /27
Block:  32 addresses
```

Two `/27` blocks are required.

### 2 Hosts

Traditional point-to-point:

```text
2^2 - 2 = 2
```

```text
Prefix: /30
Block:  4 addresses
```

Two `/30` blocks are required.

## Step 2: Sort Requirements

```text
/26
/26
/27
/27
/30
/30
```

Total addresses:

```text
64 + 64 + 32 + 32 + 4 + 4 = 200
```

A `/24` contains 256 addresses, so the preliminary capacity check passes.

This does not yet prove the plan is valid. Blocks must also be aligned and non-overlapping.

## Step 3: Allocate

### Main Cafe

```text
Network:    192.168.10.0/26
First host: 192.168.10.1
Last host:  192.168.10.62
Broadcast:  192.168.10.63
```

### Office

Next `/26` boundary:

```text
192.168.10.64
```

```text
Network:    192.168.10.64/26
First host: 192.168.10.65
Last host:  192.168.10.126
Broadcast:  192.168.10.127
```

### Kiosk A

Next free `/27` boundary:

```text
192.168.10.128
```

```text
Network:    192.168.10.128/27
First host: 192.168.10.129
Last host:  192.168.10.158
Broadcast:  192.168.10.159
```

### Kiosk B

```text
Network:    192.168.10.160/27
First host: 192.168.10.161
Last host:  192.168.10.190
Broadcast:  192.168.10.191
```

### WAN Link 1

```text
Network:    192.168.10.192/30
Router A:   192.168.10.193
Router B:   192.168.10.194
Broadcast:  192.168.10.195
```

### WAN Link 2

```text
Network:    192.168.10.196/30
Router A:   192.168.10.197
Router B:   192.168.10.198
Broadcast:  192.168.10.199
```

## Final Table

| Segment | Network | Mask | Usable range | Broadcast |
| --- | --- | --- | --- | --- |
| Main Cafe | `192.168.10.0/26` | `255.255.255.192` | `.1 - .62` | `.63` |
| Office | `192.168.10.64/26` | `255.255.255.192` | `.65 - .126` | `.127` |
| Kiosk A | `192.168.10.128/27` | `255.255.255.224` | `.129 - .158` | `.159` |
| Kiosk B | `192.168.10.160/27` | `255.255.255.224` | `.161 - .190` | `.191` |
| WAN Link 1 | `192.168.10.192/30` | `255.255.255.252` | `.193 - .194` | `.195` |
| WAN Link 2 | `192.168.10.196/30` | `255.255.255.252` | `.197 - .198` | `.199` |

## Remaining Address Space

Used:

```text
192.168.10.0 - 192.168.10.199
```

Free:

```text
192.168.10.200 - 192.168.10.255
```

This is 56 addresses, but the range is not one aligned CIDR block.

It can be represented as:

```text
192.168.10.200/29   8 addresses
192.168.10.208/28  16 addresses
192.168.10.224/27  32 addresses
```

Free-space planning matters too. If a new `/27` is expected, preserving `192.168.10.224/27` is useful.

## Why The First Free Number Is Not Always A Network

An address can be unused without being a boundary for the required prefix.

Example:

```text
Next free address: 192.168.10.200
Need: /27
```

`/27` boundaries in the fourth octet are:

```text
0, 32, 64, 96, 128, 160, 192, 224
```

`200` is not a `/27` boundary.

Block `192.168.10.192/27` is already partially occupied by WAN links, so the next complete free `/27` is:

```text
192.168.10.224/27
```

## Alignment Rules

| Prefix | Block size | Valid fourth-octet starts |
| ---: | ---: | --- |
| `/25` | 128 | 0, 128 |
| `/26` | 64 | 0, 64, 128, 192 |
| `/27` | 32 | 0, 32, 64, 96, 128, 160, 192, 224 |
| `/28` | 16 | multiples of 16 |
| `/29` | 8 | multiples of 8 |
| `/30` | 4 | multiples of 4 |

The same principle applies when the boundary occurs in another octet.

## Overlap Check

Two subnets overlap if they share at least one address.

Invalid plan:

```text
192.168.10.128/26   covers .128 - .191
192.168.10.160/27   covers .160 - .191
```

The second network lies entirely inside the first.

A valid plan uses sibling blocks, not overlapping parent and child allocations.

## `/30` Or `/31` For WAN

Traditional design uses `/30`.

When RFC 3021 is supported, a point-to-point link can use `/31`:

```text
192.168.10.192/31
192.168.10.194/31
```

This saves addresses, but verify:

- support on both devices;
- provider requirements;
- monitoring tools;
- organizational standards.

For basic CCNA labs, `/30` remains an understandable choice.

## VLSM And Routing Protocols

VLSM requires routes to carry prefix length.

Classless protocols supporting VLSM include:

- RIPv2;
- OSPF;
- EIGRP;
- IS-IS;
- BGP.

Old classful RIPv1 does not include the mask in route updates and is unsuitable for modern VLSM designs.

Static routes also specify a mask or prefix explicitly.

## Route Summarization

VLSM does not prevent summarization, but allocations should be planned hierarchically.

For example:

```text
192.168.10.0/26
192.168.10.64/26
```

are contiguous and combine into:

```text
192.168.10.0/25
```

This can be a useful summary when topology and routing policy allow it.

The two `/27` blocks:

```text
192.168.10.128/27
192.168.10.160/27
```

combine into:

```text
192.168.10.128/26
```

A summary must not include destinations reachable through another path.

## Capacity Checks Before Allocation

Use two levels of validation.

### Raw Address Count

```text
Sum of block sizes <= parent addresses
```

### Placement Check

- every block is aligned;
- blocks do not overlap;
- blocks remain inside the parent;
- remaining space supports expected growth.

The raw sum can fit mathematically while a poor allocation order leaves only fragmented space.

## Documenting A VLSM Plan

For every allocation, record:

| Field | Example |
| --- | --- |
| Purpose | Main Cafe |
| VLAN | 10 |
| Network | `192.168.10.0/26` |
| Gateway | `192.168.10.1` |
| DHCP pool | `.10 - .62` |
| Reservations | `.2 - .9` |
| Broadcast | `.63` |
| Site | HQ |
| Status | Assigned |

Use IPAM, a spreadsheet or a version-controlled source of truth.

## Practice

Parent:

```text
10.50.0.0/23
```

Requirements:

| Segment | Usable hosts |
| --- | ---: |
| Guest | 120 |
| Employees | 60 |
| Cameras | 28 |
| POS | 12 |
| Management | 10 |
| WAN 1 | 2 |
| WAN 2 | 2 |

Tasks:

1. Select each prefix.
2. Sort the allocations.
3. Allocate from the beginning of the parent block.
4. Record ranges.
5. Find the remaining free space.

## Possible Solution

Prefixes:

```text
Guest:      /25
Employees:  /26
Cameras:    /27
POS:        /28
Management: /28
WAN 1:      /30
WAN 2:      /30
```

Allocation:

| Segment | Network | Usable range | Broadcast |
| --- | --- | --- | --- |
| Guest | `10.50.0.0/25` | `10.50.0.1 - 10.50.0.126` | `10.50.0.127` |
| Employees | `10.50.0.128/26` | `10.50.0.129 - 10.50.0.190` | `10.50.0.191` |
| Cameras | `10.50.0.192/27` | `10.50.0.193 - 10.50.0.222` | `10.50.0.223` |
| POS | `10.50.0.224/28` | `10.50.0.225 - 10.50.0.238` | `10.50.0.239` |
| Management | `10.50.0.240/28` | `10.50.0.241 - 10.50.0.254` | `10.50.0.255` |
| WAN 1 | `10.50.1.0/30` | `10.50.1.1 - 10.50.1.2` | `10.50.1.3` |
| WAN 2 | `10.50.1.4/30` | `10.50.1.5 - 10.50.1.6` | `10.50.1.7` |

Remaining:

```text
10.50.1.8 - 10.50.1.255
```

Preserve it as large aligned blocks for growth where possible.

## Validation Checklist

- [ ] Parent network is correctly aligned.
- [ ] Requirements include infrastructure and headroom.
- [ ] Every prefix covers the usable-host requirement.
- [ ] Allocations are sorted largest first.
- [ ] Every network begins on a valid boundary.
- [ ] Network and broadcast are not assigned to hosts.
- [ ] Subnets do not overlap.
- [ ] Every subnet remains inside the parent.
- [ ] Remaining ranges are documented.
- [ ] Summaries do not hide incorrect paths.
- [ ] Routing supports classless prefixes.

## Common Mistakes

### Allocating Smallest First

This can fragment space and block a larger allocation.

### Using One Mask Everywhere

That is FLSM rather than VLSM and often wastes space.

### Ignoring Alignment

The first unused address is not always a valid network boundary.

### Forgetting Network And Broadcast

Convert host requirements through `2^h - 2`.

### Creating Overlap

Every allocation must be disjoint.

### Ignoring Growth

The mathematically smallest prefix can be exhausted too quickly.

### Treating A Free Range As One Subnet

An arbitrary contiguous range is not necessarily one aligned CIDR block.

### Using Classful Routing

Route updates without masks cannot correctly describe VLSM prefixes.

## Quick Self-Check

### Question 1

What does VLSM mean?

Answer:

```text
Using subnets with different prefix lengths inside one address plan.
```

### Question 2

Why allocate largest first?

Answer:

```text
Large networks require large contiguous aligned blocks
that become difficult to place after fragmentation.
```

### Question 3

Which prefix supports 50 usable hosts?

Answer:

```text
/26, providing 62 usable hosts.
```

### Question 4

Which prefix supports 20 hosts?

Answer:

```text
/27, providing 30 usable hosts.
```

### Question 5

Can `192.168.10.200/27` be a network address?

Answer:

```text
No. /27 boundaries are multiples of 32.
Address 200 belongs to 192.168.10.192/27.
```

### Question 6

Why is raw address count insufficient?

Answer:

```text
Blocks must also be aligned, non-overlapping and inside the parent.
```

## Commands And Terms

| Term | Meaning |
| --- | --- |
| VLSM | Different prefix lengths in one address plan. |
| FLSM | The same prefix for every child subnet. |
| Largest-first | Allocation from the largest block to smaller blocks. |
| Alignment | Starting a subnet on a boundary valid for its block size. |
| Fragmentation | Free space divided into inconvenient ranges. |
| Overlap | Two allocations sharing addresses. |
| Address plan | Documented distribution of IP space. |
| Classless routing | Advertising routes together with prefix length. |

## What To Review Later

- Host-based subnet sizing
- Block alignment
- CIDR notation
- `/30` and `/31`
- Route summarization
- Classless routing protocols
- IPAM
- VLSM practice

