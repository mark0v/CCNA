# Host-Based Subnetting Practice

Source: closed course page  
Date added: 2026-06-13  
Related plan item: Week 7 / Host-based subnetting practice  
Tags: subnetting, practice, hosts, FLSM, subnet mask, network range, self-check
Language: English
Translation pair: articles/2026-06/week-07/10-host-based-subnetting-practice.md

## Summary

Subnetting becomes a skill only through independent practice. Watching a completed solution creates familiarity, but it does not guarantee that you can reproduce the calculation from a blank page.

Use this learning sequence:

1. Solve the problem independently.
2. Write every intermediate step.
3. Check the answer.
4. Locate the first incorrect step.
5. Repeat the calculation without help.

This article contains four host-based subnetting exercises. Complete the **Exercises** section before opening the **Answer Key**.

## Required Outputs

For every exercise, find:

1. Minimum host bits.
2. Child prefix.
3. Dotted-decimal mask.
4. Interesting octet.
5. Increment.
6. Total addresses per subnet.
7. Usable hosts per subnet.
8. Number of child subnets in the parent block.
9. First three network addresses.
10. Network, first host, last host and broadcast of the first child subnet.
11. Whether the requirement fits inside the stated parent block.

## Working Algorithm

```text
1. Find h: 2^h - 2 >= required hosts
2. Child prefix = 32 - h
3. Confirm child prefix >= parent prefix
4. Convert prefix to subnet mask
5. Find interesting octet
6. Increment = 256 - mask value in interesting octet
7. List child networks
8. Broadcast = next network - 1
9. First host = network + 1
10. Last host = broadcast - 1
11. Child subnets = 2^(child prefix - parent prefix)
```

For normal LAN calculations:

```text
Usable hosts = 2^h - 2
```

## Practice Rules

- Do not open the answer key before completing an attempt.
- Do not guess a mask from memory unless you can explain it through bits.
- Always write the parent prefix.
- Confirm that the child subnet fits in the parent.
- Do not mark every `.0` or `.255` as reserved without checking the prefix.
- Verify capacity after calculating the range.
- Use a calculator only after a manual attempt.

## Answer Template

Use this template for each problem:

```text
Parent:
Required usable hosts:

Host bits:
Capacity check:
Child prefix:
Mask:
Interesting octet:
Increment:
Total addresses:
Usable hosts:
Child subnet count:

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

## Exercise 1: Cafe Floor

NetworkChuck Coffee has:

```text
Parent network: 192.168.50.0/24
Required hosts: 45 per subnet
```

Find every value in the answer template.

Additional question:

```text
Will the selected subnet still work if the later requirement becomes
65 usable addresses?
```

---

## Exercise 2: Office Building

Given:

```text
Parent network: 172.22.0.0/16
Required hosts: 300 per subnet
```

Find every value in the answer template.

Additional question:

```text
Is 172.22.1.0 a usable address in the first child subnet?
```

---

## Exercise 3: Distribution Center

Given:

```text
Parent network: 10.0.0.0/8
Required hosts: 1500 per subnet
```

Find every value in the answer template.

Additional question:

```text
Which network follows 10.0.248.0?
```

---

## Exercise 4: Impossible Requirement

Given:

```text
Parent network: 198.51.100.0/24
Required hosts: 300 per subnet
```

Find the required child prefix and determine whether it can be created inside the parent block.

Additional question:

```text
What is the smallest aligned parent block that could contain one such subnet
if the allocation begins at 198.51.100.0?
```

---

## Stop Before Checking

Before continuing, make sure all four attempts contain:

- checks of two adjacent powers of two;
- prefix and mask;
- increment;
- at least three networks;
- the complete first range;
- a feasibility conclusion.

Familiarity is not mastery. The goal is not to recognize the correct answer but to reproduce the process independently.

---

## Answer Key

## Solution 1: Cafe Floor

Given:

```text
Parent:         192.168.50.0/24
Required hosts: 45
```

### Host Bits

```text
2^5 - 2 = 30   insufficient
2^6 - 2 = 62   sufficient
```

```text
Host bits = 6
```

### Prefix And Mask

```text
Child prefix = 32 - 6 = /26
Mask         = 255.255.255.192
```

### Increment

The interesting octet is the fourth:

```text
256 - 192 = 64
```

### Capacity

```text
Total addresses: 2^6 = 64
Usable hosts:    64 - 2 = 62
Child subnets:   2^(26 - 24) = 4
```

### Networks

```text
192.168.50.0/26
192.168.50.64/26
192.168.50.128/26
192.168.50.192/26
```

### First Range

```text
Network:    192.168.50.0
First host: 192.168.50.1
Last host:  192.168.50.62
Broadcast:  192.168.50.63
```

### Additional Question

For 65 usable addresses, `/26` is insufficient:

```text
/26 = 62 usable
/25 = 126 usable
```

Use `/25`.

### Result

```text
Requirement feasible: yes
Reason: /24 contains four /26 subnets, each with 62 usable hosts.
```

## Solution 2: Office Building

Given:

```text
Parent:         172.22.0.0/16
Required hosts: 300
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
Child prefix = 32 - 9 = /23
Mask         = 255.255.254.0
```

### Increment

The interesting octet is the third:

```text
256 - 254 = 2
```

### Capacity

```text
Total addresses: 2^9 = 512
Usable hosts:    510
Child subnets:   2^(23 - 16) = 128
```

### First Networks

```text
172.22.0.0/23
172.22.2.0/23
172.22.4.0/23
```

### First Range

```text
Network:    172.22.0.0
First host: 172.22.0.1
Last host:  172.22.1.254
Broadcast:  172.22.1.255
```

### Additional Question

`172.22.1.0` lies between the first and last hosts and is therefore usable.

The `.0` ending does not automatically make it a network address. The network address of this `/23` is `172.22.0.0`.

### Result

```text
Requirement feasible: yes
Reason: /16 contains 128 /23 subnets with 510 usable hosts each.
```

## Solution 3: Distribution Center

Given:

```text
Parent:         10.0.0.0/8
Required hosts: 1500
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
Child prefix = 32 - 11 = /21
Mask         = 255.255.248.0
```

### Increment

The interesting octet is the third:

```text
256 - 248 = 8
```

### Capacity

```text
Total addresses: 2^11 = 2048
Usable hosts:    2046
Child subnets:   2^(21 - 8) = 8192
```

### First Networks

```text
10.0.0.0/21
10.0.8.0/21
10.0.16.0/21
```

### First Range

```text
Network:    10.0.0.0
First host: 10.0.0.1
Last host:  10.0.7.254
Broadcast:  10.0.7.255
```

### Additional Question

After:

```text
10.0.248.0/21
```

adding `8` produces `256` in the third octet:

```text
10.0.256.0 -> 10.1.0.0
```

The next network is:

```text
10.1.0.0/21
```

### Result

```text
Requirement feasible: yes
Reason: /8 contains 8192 /21 subnets with 2046 usable hosts each.
```

A practical design must separately justify a broadcast domain of this size.

## Solution 4: Impossible Requirement

Given:

```text
Parent:         198.51.100.0/24
Required hosts: 300
```

### Host Bits

```text
2^8 - 2 = 254   insufficient
2^9 - 2 = 510   sufficient
```

```text
Host bits = 9
```

### Required Prefix

```text
Child prefix = 32 - 9 = /23
Mask         = 255.255.254.0
```

But:

```text
Required child: /23
Available parent: /24
```

A `/23` is larger than a `/24`, so it cannot fit inside the parent.

### Alignment

`/23` network boundaries advance by `2` in the third octet.

Address `198.51.100.0` is correctly aligned for `/23` because `100` is even.

The smallest parent block is:

```text
198.51.100.0/23
```

Range:

```text
Network:    198.51.100.0
First host: 198.51.100.1
Last host:  198.51.101.254
Broadcast:  198.51.101.255
```

### Result

```text
Requirement feasible in stated parent: no
Required allocation: 198.51.100.0/23 or another aligned /23
```

## Summary Table

| Task | Parent | Hosts | Child prefix | Usable | Child subnets | Feasible |
| ---: | --- | ---: | ---: | ---: | ---: | --- |
| 1 | `192.168.50.0/24` | 45 | `/26` | 62 | 4 | Yes |
| 2 | `172.22.0.0/16` | 300 | `/23` | 510 | 128 | Yes |
| 3 | `10.0.0.0/8` | 1500 | `/21` | 2046 | 8192 | Yes |
| 4 | `198.51.100.0/24` | 300 | `/23` | 510 | Does not fit | No |

## Analyzing A Mistake

Do not stop at "incorrect." Classify the error.

| Error type | Example | Review |
| --- | --- | --- |
| Requirement | Solved for subnets instead of hosts | Identifying question type |
| Capacity | Used `2^h` and forgot `- 2` | Network and broadcast |
| Prefix | Found `h` but calculated `32 - h` incorrectly | CIDR structure |
| Mask | Converted the prefix incorrectly | Binary mask values |
| Increment | Used the wrong octet | Interesting octet |
| Range | Made broadcast equal to the next network | `next network - 1` |
| Rollover | Produced octet `256` | Octet carry |
| Parent | Child subnet is larger than allocation | Parent/child validation |
| Usability | Marked every `.0` as network | Prefix-aware boundaries |

## Retry Log

For each mistake, record:

```text
Task:
My incorrect result:
Correct result:
First incorrect step:
Why it was incorrect:
Rule to apply next time:
Second attempt result:
```

This turns a random error into a specific reusable rule.

## Tool Verification

After solving manually, verify ranges with Python:

```python
from ipaddress import ip_network

parent = ip_network("192.168.50.0/24")
children = list(parent.subnets(new_prefix=26))

for subnet in children:
    print(
        subnet,
        subnet.network_address,
        subnet.broadcast_address,
        subnet.num_addresses - 2,
    )
```

The tool should confirm your solution, not replace the first attempt.

## Additional Round

After solving the original exercises, change only the requirement:

| Parent | Original hosts | New hosts |
| --- | ---: | ---: |
| `192.168.50.0/24` | 45 | 63 |
| `172.22.0.0/16` | 300 | 511 |
| `10.0.0.0/8` | 1500 | 2047 |
| `198.51.100.0/24` | 300 | 120 |

Notice how crossing a capacity boundary changes the prefix:

```text
62 -> 63     changes /26 to /25
510 -> 511   changes /23 to /22
2046 -> 2047 changes /21 to /20
```

## Readiness Criteria

You understand the material when, without the answer key, you can:

- identify the requirement type;
- select host bits using two adjacent powers of two;
- calculate prefix and mask;
- find the interesting octet and increment;
- list network ranges;
- identify first host, last host and broadcast;
- detect an impossible requirement;
- explain each step;
- repeat the calculation with a new host count.

Speed follows stable accuracy. Build a repeatable process first.

## Quick Self-Check

### Question 1

Why is watching solutions insufficient?

Answer:

```text
Recognizing the steps does not guarantee that you can reproduce them independently.
```

### Question 2

When should you open the answer key?

Answer:

```text
After completing an independent attempt with written steps.
```

### Question 3

What is more useful than marking an answer "wrong"?

Answer:

```text
Find the first incorrect step and connect it to a specific rule.
```

### Question 4

What prefix supports 300 usable hosts?

Answer:

```text
/23, because /24 provides 254 and /23 provides 510 usable hosts.
```

### Question 5

Why can a `/23` not be created inside a `/24`?

Answer:

```text
A /23 is a larger address block than a /24.
```

## What To Review Later

- Host-capacity boundaries
- Prefix-to-mask conversion
- Interesting octet
- Increment and rollover
- Parent/child prefix validation
- FLSM
- VLSM
- Timed subnetting drills

