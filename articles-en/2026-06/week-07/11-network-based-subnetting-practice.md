# Network-Based Subnetting Practice

Source: closed course page  
Date added: 2026-06-13  
Related plan item: Week 7 / Network-based subnetting practice  
Tags: subnetting, practice, networks, FLSM, borrowed bits, increment, self-check
Language: English
Translation pair: articles/2026-06/week-07/11-network-based-subnetting-practice.md

## Summary

In network-based subnetting, the initial requirement defines the minimum number of child networks.

The main formula is:

```text
2^n >= required subnets
```

where `n` is the number of host bits borrowed and converted into subnet bits.

Then:

```text
Child prefix = parent prefix + n
```

The calculation does not end after selecting the mask. You must verify the remaining host bits and usable capacity in every resulting subnet.

This article is an independent practice worksheet. Complete all four exercises before opening the answer key.

## Required Outputs

For every exercise, find:

1. Minimum borrowed bits.
2. Child prefix.
3. Dotted-decimal mask.
4. Interesting octet.
5. Increment.
6. Actual number of child subnets.
7. Remaining host bits.
8. Total and usable addresses per child subnet.
9. First three network addresses.
10. Network, first host, last host and broadcast of the first child subnet.
11. Whether the requirement fits inside the parent block.
12. Whether host capacity is sufficient when specified.

## Working Algorithm

```text
1. Find n: 2^n >= required subnets
2. Child prefix = parent prefix + n
3. Confirm child prefix <= 30 for ordinary LAN subnets
4. Convert prefix to subnet mask
5. Find interesting octet
6. Increment = 256 - mask value in interesting octet
7. Actual child subnets = 2^n
8. Remaining host bits = 32 - child prefix
9. Usable hosts = 2^h - 2
10. List child networks
11. Broadcast = next network - 1
12. Validate every stated requirement
```

## Practice Rules

- Do not open the answer key before finishing every exercise.
- Round the subnet requirement up to a power of two.
- Add borrowed bits to the parent prefix, not the number of networks.
- Use the modern `2^n` formula, including subnet zero.
- Apply the increment in the interesting octet.
- Perform rollover when an octet reaches `256`.
- Verify remaining host capacity.
- Keep every child block inside the parent allocation.

## Answer Template

```text
Parent:
Required subnets:
Required hosts per subnet, if given:

Borrowed bits:
Subnet-count check:
Child prefix:
Mask:
Interesting octet:
Increment:
Actual child subnets:
Remaining host bits:
Total addresses/subnet:
Usable hosts/subnet:

Network 1:
Network 2:
Network 3:

First subnet:
  Network:
  First host:
  Last host:
  Broadcast:

Requirement feasible: yes/no
Reason:
```

---

## Exercise 1: Branch Offices

Given:

```text
Parent network:   192.168.80.0/24
Required subnets: 6
```

Additional question:

```text
Can each child subnet support 25 usable hosts?
```

---

## Exercise 2: Regional Sites

Given:

```text
Parent network:   172.24.0.0/16
Required subnets: 100
```

Additional question:

```text
Is 172.24.1.255 the broadcast address of the first child subnet?
```

---

## Exercise 3: Enterprise Expansion

Given:

```text
Parent network:   10.0.0.0/8
Required subnets: 700
```

Additional question:

```text
Which network follows 10.0.224.0?
```

---

## Exercise 4: Conflicting Requirements

Given:

```text
Parent network:        192.0.2.0/24
Required subnets:      20
Required usable hosts: 20 per subnet
```

Select a prefix by subnet count first, then verify host capacity.

Additional question:

```text
What is the smallest larger parent prefix that can provide
at least 20 equal subnets with 20 usable hosts each?
```

---

## Stop Before Checking

Every attempt should include:

- two adjacent powers of two;
- borrowed bits;
- child prefix and mask;
- increment;
- host capacity;
- first three networks;
- the complete first range;
- a final conclusion.

Recognizing someone else's solution does not replace doing the calculation.

---

## Answer Key

## Solution 1: Branch Offices

Given:

```text
Parent:            192.168.80.0/24
Required subnets:  6
```

### Borrowed Bits

```text
2^2 = 4   insufficient
2^3 = 8   sufficient
```

```text
Borrowed bits = 3
```

### Prefix And Mask

```text
Child prefix = /24 + 3 = /27
Mask         = 255.255.255.224
```

### Increment

```text
256 - 224 = 32 in the fourth octet
```

### Capacity

```text
Actual subnets:       2^3 = 8
Remaining host bits:  32 - 27 = 5
Total addresses:      2^5 = 32
Usable hosts:         2^5 - 2 = 30
```

### First Networks

```text
192.168.80.0/27
192.168.80.32/27
192.168.80.64/27
```

### First Range

```text
Network:    192.168.80.0
First host: 192.168.80.1
Last host:  192.168.80.30
Broadcast:  192.168.80.31
```

### Additional Question

Every `/27` provides 30 usable hosts, so the 25-host requirement is satisfied.

### Result

```text
Requirement feasible: yes
Produced: 8 subnets, each with 30 usable hosts
```

## Solution 2: Regional Sites

Given:

```text
Parent:            172.24.0.0/16
Required subnets:  100
```

### Borrowed Bits

```text
2^6 = 64    insufficient
2^7 = 128   sufficient
```

```text
Borrowed bits = 7
```

### Prefix And Mask

```text
Child prefix = /16 + 7 = /23
Mask         = 255.255.254.0
```

### Increment

```text
256 - 254 = 2 in the third octet
```

### Capacity

```text
Actual subnets:       128
Remaining host bits:  9
Total addresses:      512
Usable hosts:         510
```

### First Networks

```text
172.24.0.0/23
172.24.2.0/23
172.24.4.0/23
```

### First Range

```text
Network:    172.24.0.0
First host: 172.24.0.1
Last host:  172.24.1.254
Broadcast:  172.24.1.255
```

### Additional Question

Yes, `172.24.1.255` is the broadcast of the first `/23`, because the next network begins at `172.24.2.0`.

### Result

```text
Requirement feasible: yes
Produced: 128 subnets, each with 510 usable hosts
```

## Solution 3: Enterprise Expansion

Given:

```text
Parent:            10.0.0.0/8
Required subnets:  700
```

### Borrowed Bits

```text
2^9 = 512     insufficient
2^10 = 1024   sufficient
```

```text
Borrowed bits = 10
```

### Prefix And Mask

```text
Child prefix = /8 + 10 = /18
Mask         = 255.255.192.0
```

### Increment

```text
256 - 192 = 64 in the third octet
```

### Capacity

```text
Actual subnets:       1024
Remaining host bits:  14
Total addresses:      16384
Usable hosts:         16382
```

### First Networks

```text
10.0.0.0/18
10.0.64.0/18
10.0.128.0/18
```

Fourth:

```text
10.0.192.0/18
```

Fifth after rollover:

```text
10.1.0.0/18
```

### First Range

```text
Network:    10.0.0.0
First host: 10.0.0.1
Last host:  10.0.63.254
Broadcast:  10.0.63.255
```

### Additional Question

`10.0.224.0` is not a `/18` boundary. `/18` networks in the third octet start only at:

```text
0, 64, 128, 192
```

`10.0.224.0` is inside `10.0.192.0/18`. The next network after that block is:

```text
10.1.0.0/18
```

This checks alignment: add the increment to a network boundary, not an arbitrary address.

### Result

```text
Requirement feasible: yes
Produced: 1024 subnets, each with 16382 usable hosts
```

A practical design should separately evaluate the excessive broadcast-domain size.

## Solution 4: Conflicting Requirements

Given:

```text
Parent:            192.0.2.0/24
Required subnets:  20
Required hosts:    20 per subnet
```

### Prefix By Network Count

```text
2^4 = 16   insufficient
2^5 = 32   sufficient
```

```text
Borrowed bits = 5
Child prefix  = /24 + 5 = /29
```

Mask:

```text
255.255.255.248
```

Increment:

```text
8
```

### Host Capacity

```text
Remaining host bits: 3
Total addresses:     8
Usable hosts:        6
```

Twenty usable hosts are required, so `/29` is insufficient.

### Prefix By Host Count

```text
2^4 - 2 = 14   insufficient
2^5 - 2 = 30   sufficient
```

Hosts require:

```text
/27
```

But a `/24` contains only:

```text
2^(27 - 24) = 8 subnets
```

while 20 are required.

### Minimum Larger Parent

Every child subnet must be `/27`. At least 20 networks require 32 equal blocks:

```text
2^5 = 32
```

Parent prefix:

```text
/27 - 5 levels = /22
```

The minimum parent size is:

```text
/22
```

However, `192.0.2.0` is not a `/22` network boundary. `/22` boundaries advance by `4` in the third octet.

The value `2` belongs to:

```text
192.0.0.0/22
```

covering:

```text
192.0.0.0 - 192.0.3.255
```

If the allocation must begin exactly at `192.0.2.0`, a single aligned `/22` cannot use that network address. Use another aligned block or multiple allocations.

### Result

```text
Requirement feasible in /24: no
Minimum equal-size parent prefix: /22
Required child size: /27
```

## Summary Table

| Task | Parent | Required networks | Child prefix | Produced | Usable hosts | Feasible |
| ---: | --- | ---: | ---: | ---: | ---: | --- |
| 1 | `192.168.80.0/24` | 6 | `/27` | 8 | 30 | Yes |
| 2 | `172.24.0.0/16` | 100 | `/23` | 128 | 510 | Yes |
| 3 | `10.0.0.0/8` | 700 | `/18` | 1024 | 16382 | Yes |
| 4 | `192.0.2.0/24` | 20 | `/29` by network count | 32 | 6 | No, needs 20 hosts |

## Analyzing Mistakes

| Error type | Example | Review |
| --- | --- | --- |
| Requirement | Solved for hosts instead of networks | Subnetting question types |
| Rounding | Selected 6 bits for 100 networks | Next power of two |
| Prefix | Added 100 to `/16` | Borrowed bits |
| Formula | Used `2^n - 2` for subnet count | Modern subnet-zero rule |
| Octet | Applied `/23` increment in the fourth octet | Interesting octet |
| Rollover | Wrote an octet containing `256` | Positional carry |
| Alignment | Treated an arbitrary address as a network | Block boundaries |
| Hosts | Checked network count but not capacity | Remaining host bits |
| Parent | Child blocks exceeded the allocation | Parent containment |

## Retry Log

```text
Task:
My borrowed bits:
My child prefix:
My first three networks:
First incorrect step:
Correct rule:
Second attempt:
```

Repeat the problem without viewing the solution after identifying the first incorrect action.

## Python Verification

After calculating manually:

```python
from ipaddress import ip_network

parent = ip_network("172.24.0.0/16")
children = list(parent.subnets(new_prefix=23))

print(len(children))
print(children[:3])
print(children[0].broadcast_address)
print(children[0].num_addresses - 2)
```

Expected output:

```text
128
[IPv4Network('172.24.0.0/23'),
 IPv4Network('172.24.2.0/23'),
 IPv4Network('172.24.4.0/23')]
172.24.1.255
510
```

## Additional Round

Change only the subnet requirement:

| Parent | Original | New requirement |
| --- | ---: | ---: |
| `192.168.80.0/24` | 6 | 9 |
| `172.24.0.0/16` | 100 | 129 |
| `10.0.0.0/8` | 700 | 1025 |

Check these transitions:

```text
8 -> 9       requires one more borrowed bit
128 -> 129   requires one more borrowed bit
1024 -> 1025 requires one more borrowed bit
```

Every additional borrowed bit:

- doubles the number of child subnets;
- halves the total addresses in each subnet.

## Readiness Criteria

You are ready to continue when you can:

- distinguish network-based from host-based requirements;
- find borrowed bits using powers of two;
- derive a child prefix from any parent prefix;
- identify the interesting octet;
- apply increment and rollover;
- find network and broadcast;
- calculate remaining host capacity;
- detect conflicting requirements;
- explain alignment;
- repeat the exercise without the answer key.

## Quick Self-Check

### Question 1

How many bits are required for at least 100 subnets?

Answer:

```text
7, because 2^6 = 64 and 2^7 = 128.
```

### Question 2

What prefix results from borrowing 7 bits from `/16`?

Answer:

```text
/23
```

### Question 3

How many usable hosts remain in `/23`?

Answer:

```text
2^9 - 2 = 510.
```

### Question 4

Why can `/24` not provide 20 subnets with 20 hosts each?

Answer:

```text
Twenty subnets require /29, but /29 provides only 6 usable hosts.
Twenty hosts require /27, but /24 contains only eight /27 subnets.
```

### Question 5

What matters more than speed at first?

Answer:

```text
A repeatable process and accurate validation of every constraint.
```

## What To Review Later

- Powers of two
- Borrowed bits
- Prefix-to-mask conversion
- Interesting octet
- Increment and rollover
- Alignment
- Host-capacity validation
- FLSM and VLSM
- Timed subnetting drills

