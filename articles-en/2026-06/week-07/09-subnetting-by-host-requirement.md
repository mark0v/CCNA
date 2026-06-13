# Subnetting By Host Requirement

Source: closed course page  
Date added: 2026-06-13  
Related plan item: Week 7 / Subnetting by host requirement  
Tags: subnetting, hosts, FLSM, prefix, subnet mask, capacity planning, headroom
Language: English
Translation pair: articles/2026-06/week-07/09-subnetting-by-host-requirement.md

## Summary

When a requirement says "the network must support at least 50 devices," begin with host capacity.

Preserve the minimum number of host bits `h` for which:

```text
2^h - 2 >= required hosts
```

Then:

```text
New prefix = 32 - h
```

Example for 50 hosts:

```text
2^5 - 2 = 30   insufficient
2^6 - 2 = 62   sufficient

Host bits:    6
Prefix:       /26
Mask:         255.255.255.192
Increment:    64
Usable hosts: 62
```

The main idea is:

```text
Preserve enough host bits first,
then use the remaining bits for the network.
```

## Key Points

- A requirement can specify either a subnet count or hosts per subnet.
- Host-based subnetting determines the necessary host bits first.
- The ordinary IPv4 subnet formula is `2^h - 2`.
- Subtracting two accounts for the network and broadcast addresses.
- Choose the longest prefix that still satisfies the host requirement.
- A longer prefix means a smaller subnet.
- A shorter prefix means a larger subnet.
- After selecting the prefix, build ranges using the normal increment method.
- The parent block must contain at least one subnet of the selected size.
- A parent block can contain multiple equal-size child subnets.
- Production designs include reasonable growth headroom.
- Infrastructure reservations also consume addresses.

## Identify The Question Type First

### Subnet-Count Question

```text
How many networks are required?
```

Find borrowed bits:

```text
2^n >= required subnets
```

### Host-Count Question

```text
How many usable addresses are required in each network?
```

Preserve host bits:

```text
2^h - 2 >= required hosts
```

The distinction is at the beginning of the calculation. After choosing the mask, increment, network, broadcast and usable ranges are calculated in the same way.

## Why The Formula Uses `- 2`

In an ordinary IPv4 subnet:

- all host bits set to `0` identify the network address;
- all host bits set to `1` identify the broadcast address.

For example, six host bits produce:

```text
2^6 = 64 total combinations
```

Usable hosts:

```text
64 - 2 = 62
```

Exceptions include:

- `/31` on point-to-point links under RFC 3021;
- `/32`, representing one address;
- specialized platform or protocol use cases.

Use `2^h - 2` for normal instructional LAN calculations.

## Why Counting The Bits Of The Number Is Not Enough

Decimal `50` fits in six binary bits, and `/26` is indeed correct. However, the shortcut "count the bits needed to represent the host number" fails at boundaries.

For 63 hosts:

```text
Decimal 63 fits in six bits.
```

But:

```text
2^6 - 2 = 62
```

That is insufficient.

Seven host bits are required:

```text
2^7 - 2 = 126
```

The reliable test is:

```text
2^h - 2 >= requirement
```

## Host-Capacity Table

| Host bits | Prefix | Total addresses | Traditional usable hosts |
| ---: | ---: | ---: | ---: |
| 2 | `/30` | 4 | 2 |
| 3 | `/29` | 8 | 6 |
| 4 | `/28` | 16 | 14 |
| 5 | `/27` | 32 | 30 |
| 6 | `/26` | 64 | 62 |
| 7 | `/25` | 128 | 126 |
| 8 | `/24` | 256 | 254 |
| 9 | `/23` | 512 | 510 |
| 10 | `/22` | 1024 | 1022 |
| 11 | `/21` | 2048 | 2046 |
| 12 | `/20` | 4096 | 4094 |
| 13 | `/19` | 8192 | 8190 |
| 14 | `/18` | 16384 | 16382 |

This table is useful for quick sizing, but every value follows from the formula.

## Practical Algorithm

1. Record the parent network and parent prefix.
2. Record the required usable hosts per subnet.
3. Add infrastructure addresses and growth headroom for a design task.
4. Find the minimum `h` where `2^h - 2` covers the total.
5. Calculate `new prefix = 32 - h`.
6. Confirm that the new prefix is not shorter than the parent prefix.
7. Find the dotted-decimal mask.
8. Identify the interesting octet.
9. Find the increment.
10. List child networks inside the parent block.
11. Find network, broadcast and usable ranges.
12. Verify the child-subnet count and host capacity.

## Parent-Block Validation

A child subnet must fit inside the parent allocation.

If the parent is:

```text
192.168.10.0/24
```

and the host requirement needs:

```text
/23
```

the task is impossible inside that `/24`, because `/23` is larger than the parent block.

```text
/23 is larger than /24
```

Obtain a larger allocation or revise the requirement.

## Example 1: At Least 50 Hosts

Given:

```text
Parent network: 192.168.10.0/24
Required hosts: 50 per subnet
```

### Step 1: Find Host Bits

```text
2^5 - 2 = 30   insufficient
2^6 - 2 = 62   sufficient
```

```text
Host bits = 6
```

### Step 2: Find The Prefix

```text
32 - 6 = 26
```

```text
New prefix = /26
```

Mask:

```text
255.255.255.192
```

Binary:

```text
11111111.11111111.11111111.11000000
```

### Step 3: Find The Increment

The interesting octet is the fourth:

```text
256 - 192 = 64
```

```text
Increment = 64
```

### Step 4: List Child Subnets

```text
192.168.10.0/26
192.168.10.64/26
192.168.10.128/26
192.168.10.192/26
```

The `/24` produces:

```text
2^(26 - 24) = 4 subnets
```

### Ranges

| Network | First host | Last host | Broadcast |
| --- | --- | --- | --- |
| `192.168.10.0/26` | `192.168.10.1` | `192.168.10.62` | `192.168.10.63` |
| `192.168.10.64/26` | `192.168.10.65` | `192.168.10.126` | `192.168.10.127` |
| `192.168.10.128/26` | `192.168.10.129` | `192.168.10.190` | `192.168.10.191` |
| `192.168.10.192/26` | `192.168.10.193` | `192.168.10.254` | `192.168.10.255` |

Every child subnet provides:

```text
64 total addresses
62 usable hosts
```

## When The Original Address Is Not The Parent Network

This statement:

```text
172.16.10.0 requires 50 hosts
```

is incomplete without a prefix.

With `/24`:

```text
172.16.10.0/24
```

it produces four `/26` subnets.

With parent `/16`:

```text
172.16.0.0/16
```

it can produce 1,024 `/26` subnets, including `172.16.10.0/26`.

Always consider the address and prefix together.

## Example 2: At Least 500 Hosts

Given:

```text
Parent network: 172.16.0.0/16
Required hosts: 500 per subnet
```

### Host Bits

```text
2^8 - 2 = 254   insufficient
2^9 - 2 = 510   sufficient
```

```text
Host bits = 9
```

### Prefix And Mask

```text
32 - 9 = 23
```

```text
Prefix: /23
Mask:   255.255.254.0
```

### Increment

```text
256 - 254 = 2 in the third octet
```

### Networks

```text
172.16.0.0/23
172.16.2.0/23
172.16.4.0/23
172.16.6.0/23
...
172.16.254.0/23
```

### Capacity

```text
Child subnets: 2^(23 - 16) = 128
Total/subnet:  2^9 = 512
Usable hosts:  510
```

First range:

```text
Network:    172.16.0.0
First host: 172.16.0.1
Last host:  172.16.1.254
Broadcast:  172.16.1.255
```

Second:

```text
Network:    172.16.2.0
First host: 172.16.2.1
Last host:  172.16.3.254
Broadcast:  172.16.3.255
```

## Example 3: At Least 2,000 Hosts

Given:

```text
Parent network: 10.0.0.0/8
Required hosts: 2000 per subnet
```

### Host Bits

```text
2^10 - 2 = 1022   insufficient
2^11 - 2 = 2046   sufficient
```

```text
Host bits = 11
```

### Prefix And Mask

```text
32 - 11 = 21
```

```text
Prefix: /21
Mask:   255.255.248.0
```

### Increment

The interesting octet is the third:

```text
256 - 248 = 8
```

### Networks

```text
10.0.0.0/21
10.0.8.0/21
10.0.16.0/21
10.0.24.0/21
...
10.255.248.0/21
```

### First Ranges

| Network | First host | Last host | Broadcast |
| --- | --- | --- | --- |
| `10.0.0.0/21` | `10.0.0.1` | `10.0.7.254` | `10.0.7.255` |
| `10.0.8.0/21` | `10.0.8.1` | `10.0.15.254` | `10.0.15.255` |
| `10.0.16.0/21` | `10.0.16.1` | `10.0.23.254` | `10.0.23.255` |

### Capacity

```text
Child subnets: 2^(21 - 8) = 8192
Total/subnet:  2^11 = 2048
Usable hosts:  2046
```

Mathematically, `/21` covers 2,000 hosts. In practice, a broadcast domain of that size requires explicit justification.

## Headroom And Infrastructure Reservations

A requirement of "50 devices" rarely means exactly 50 addresses are enough.

A subnet can also need addresses for:

- default gateway;
- redundant gateway;
- switches and access points;
- printers;
- cameras;
- controllers;
- monitoring;
- DHCP reservations;
- temporary devices;
- future growth.

Example:

```text
Current user devices: 50
Infrastructure:        5
Expected growth:       20
Required capacity:     75
```

`/26` is no longer sufficient:

```text
62 usable
```

Use `/25`:

```text
126 usable
```

Choose headroom based on business plans, equipment lifecycle and the cost of future renumbering rather than one universal percentage.

## Smallest Practical Prefix

The mathematical goal is:

```text
Find the longest prefix that satisfies the requirement.
```

The practical goal is:

```text
Find the longest prefix that covers the requirement,
infrastructure and reasonable growth without excessive waste.
```

A subnet that is too small causes:

- early exhaustion;
- DHCP-scope redesign;
- renumbering;
- secondary subnets;
- urgent VLAN changes.

A subnet that is too large causes:

- wasted address space;
- a larger broadcast domain;
- a wider fault scope;
- less precise segmentation.

## Useful Boundary Values

| Required usable hosts | Minimum host bits | Prefix | Capacity |
| ---: | ---: | ---: | ---: |
| 2 | 2 | `/30` | 2 |
| 3-6 | 3 | `/29` | 6 |
| 7-14 | 4 | `/28` | 14 |
| 15-30 | 5 | `/27` | 30 |
| 31-62 | 6 | `/26` | 62 |
| 63-126 | 7 | `/25` | 126 |
| 127-254 | 8 | `/24` | 254 |
| 255-510 | 9 | `/23` | 510 |
| 511-1022 | 10 | `/22` | 1022 |
| 1023-2046 | 11 | `/21` | 2046 |

Important transitions:

```text
62 hosts -> /26
63 hosts -> /25

254 hosts -> /24
255 hosts -> /23

510 hosts -> /23
511 hosts -> /22
```

## Host Requirement And Produced Subnets

After selecting the child prefix, the number of equal-size subnets inside the parent is:

```text
Number of child subnets = 2^(child prefix - parent prefix)
```

Example:

```text
Parent: /16
Child:  /23
```

```text
2^(23 - 16) = 2^7 = 128 subnets
```

Host-based sizing determines each subnet's size. The parent prefix determines how many such blocks are available.

## When Requirements Conflict

Given:

```text
Parent:            192.168.10.0/24
Required subnets:  5
Required hosts:    50 per subnet
```

Fifty hosts require `/26`.

A `/24` contains:

```text
2^(26 - 24) = 4 subnets
```

Five are required, so one `/24` is insufficient.

Possible responses:

- obtain a larger parent block such as `/23`;
- reduce the host requirement;
- reduce the network count;
- use VLSM if not every segment needs 50 hosts;
- revise the design.

Always validate both constraints when both are known.

## FLSM And VLSM

If every segment needs the same capacity, FLSM works well.

If requirements differ:

```text
Guest:       100 hosts
Employees:    50 hosts
POS:          12 hosts
Management:   10 hosts
WAN link:      2 hosts
```

one mask wastes space. VLSM is more efficient:

```text
Guest:      /25
Employees:  /26
POS:        /28
Management: /28
WAN:        /30 or /31
```

Host-based sizing is the foundation of VLSM.

## Practice

For every scenario, find:

- minimum host bits;
- child prefix;
- mask;
- increment;
- usable capacity;
- number of child subnets inside the parent;
- first three network addresses.

### Exercise 1

```text
Parent:         192.168.40.0/24
Required hosts: 25
```

### Exercise 2

```text
Parent:         172.20.0.0/16
Required hosts: 700
```

### Exercise 3

```text
Parent:         10.0.0.0/8
Required hosts: 4000
```

### Exercise 4

```text
Parent:         192.0.2.0/24
Required hosts: 255
```

## Answers

### Exercise 1

```text
Host bits:    5
Prefix:       /27
Mask:         255.255.255.224
Increment:    32 in fourth octet
Capacity:     30 usable
Subnets:      8
Networks:     192.168.40.0, 192.168.40.32, 192.168.40.64
```

### Exercise 2

```text
2^9 - 2 = 510    insufficient
2^10 - 2 = 1022  sufficient

Host bits:    10
Prefix:       /22
Mask:         255.255.252.0
Increment:    4 in third octet
Capacity:     1022 usable
Subnets:      64
Networks:     172.20.0.0, 172.20.4.0, 172.20.8.0
```

### Exercise 3

```text
2^11 - 2 = 2046  insufficient
2^12 - 2 = 4094  sufficient

Host bits:    12
Prefix:       /20
Mask:         255.255.240.0
Increment:    16 in third octet
Capacity:     4094 usable
Subnets:      4096
Networks:     10.0.0.0, 10.0.16.0, 10.0.32.0
```

### Exercise 4

Two hundred and fifty-five usable hosts require `/23`:

```text
2^8 - 2 = 254   insufficient
2^9 - 2 = 510   sufficient
```

But `/23` is larger than the `/24` parent. The requirement cannot be met inside the stated block.

## Checking With Python `ipaddress`

```python
from ipaddress import ip_network

parent = ip_network("172.16.0.0/16")
children = list(parent.subnets(new_prefix=23))
first = children[0]

print(len(children))
print(first)
print(first.num_addresses)
print(first.network_address)
print(first.broadcast_address)
```

Expected output:

```text
128
172.16.0.0/23
512
172.16.0.0
172.16.1.255
```

Traditional usable capacity:

```text
512 - 2 = 510
```

## Cisco IOS Check

Assign an address from the first `/26`:

```text
Router(config)# interface gigabitEthernet 0/0
Router(config-if)# ip address 192.168.10.1 255.255.255.192
Router(config-if)# no shutdown
```

Verify:

```text
Router# show ip interface brief
Router# show ip route connected
```

Connected route:

```text
192.168.10.0/26
```

IOS validates address and mask semantics, but it does not know the business growth plan.

## Common Mistakes

### Using `2^h >= hosts`

An ordinary subnet needs two reserved addresses:

```text
2^h - 2 >= required hosts
```

### Selecting `/26` For 63 Hosts

`/26` provides only 62 usable addresses. Use `/25`.

### Forgetting Gateways And Infrastructure

The endpoint requirement must include every interface address, not only user devices.

### Choosing A Prefix Without Checking The Parent

The child subnet may not fit inside the parent allocation.

### Treating An Address As Complete Without A Prefix

`172.16.10.0` does not specify a network size. Use notation such as `172.16.10.0/24`.

### Taking Excessive Headroom Without A Reason

Headroom is useful, but an oversized subnet can weaken segmentation and consume the allocation.

### Treating Increment As Usable Capacity

For `/26`, the increment and total-address count are 64, but usable hosts are 62.

### Ignoring The Second Requirement

Host capacity can be sufficient while the available subnet count is not.

## Quick Self-Check

### Question 1

What formula determines the minimum host bits?

Answer:

```text
2^h - 2 >= required usable hosts
```

### Question 2

What prefix supports 50 hosts?

Answer:

```text
/26, which provides 62 usable hosts.
```

### Question 3

What prefix supports 63 hosts?

Answer:

```text
/25. A /26 provides only 62 usable hosts.
```

### Question 4

What is the `/23` increment?

Answer:

```text
2 in the third octet.
```

### Question 5

How many `/26` subnets fit inside a `/24`?

Answer:

```text
2^(26 - 24) = 4.
```

### Question 6

Why do 2,000 hosts require `/21`?

Answer:

```text
Ten host bits provide 1,022 usable addresses,
while eleven provide 2,046. 32 - 11 = /21.
```

### Question 7

What if the required child prefix is shorter than the parent prefix?

Answer:

```text
The child subnet cannot fit inside the parent block.
Obtain a larger allocation or revise the requirements.
```

## Commands And Terms

| Term | Meaning |
| --- | --- |
| Host requirement | Required usable interface addresses in a subnet. |
| Host bits | Bits to the right of the prefix boundary. |
| Headroom | Capacity reserved for growth and operations. |
| Infrastructure reservation | Addresses for gateways, APs, switches and services. |
| Child prefix | Prefix of subnets created inside a parent. |
| Parent prefix | Prefix of the original allocation. |
| Capacity | Total or usable addresses in a subnet. |
| FLSM | Equal-size subnet allocation. |
| VLSM | Allocation using different subnet sizes. |

## What To Review Later

- Powers of two
- Prefix-to-mask conversion
- Interesting octet
- Network and broadcast ranges
- Subnetting by network requirement
- FLSM
- VLSM
- Capacity planning
- Address management and IPAM

