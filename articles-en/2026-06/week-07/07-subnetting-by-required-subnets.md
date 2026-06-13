# Subnetting By Required Number Of Networks

Source: closed course page  
Date added: 2026-06-13  
Related plan item: Week 7 / Subnetting by required subnets  
Tags: subnetting, FLSM, subnet mask, prefix, increment, network range, host bits
Language: English
Translation pair: articles/2026-06/week-07/07-subnetting-by-required-subnets.md

## Summary

Subnetting exchanges some host capacity for additional networks.

An original `/24` network has 24 network bits and 8 host bits. To produce several smaller equal-size subnets, borrow host bits and turn them into subnet bits.

The basic process is:

1. Determine the required number of subnets.
2. Find the minimum number of borrowed bits for which `2^n` satisfies the requirement.
3. Add the borrowed bits to the original prefix.
4. Find the subnet increment.
5. List the network ranges.
6. Verify the usable hosts in every new subnet.

Example:

```text
Original network:    192.168.10.0/24
Required subnets:    25
Borrowed bits:       5
New prefix:          /29
New mask:            255.255.255.248
Increment:           8
Subnets produced:    32
Usable hosts/subnet: 6
```

## Key Points

- Ones in a subnet mask identify network bits.
- Zeros identify host bits.
- Borrowing converts host bits into network bits.
- Borrowing `n` bits creates `2^n` equal-size subnets.
- Leaving `h` host bits provides `2^h - 2` usable addresses in an ordinary subnet.
- The new prefix equals the original prefix plus the borrowed bits.
- The increment is the distance between adjacent network addresses.
- A broadcast address is immediately before the next network.
- The first usable host follows the network address.
- The last usable host precedes the broadcast address.
- Round the subnet requirement up to the next power of two.
- FLSM creates equal-size subnets.
- Validate both subnet count and host capacity before approving a design.

## What Changes During Subnetting

Original network:

```text
192.168.10.0/24
```

Binary `/24` mask:

```text
11111111.11111111.11111111.00000000
```

Bit roles:

```text
NNNNNNNN.NNNNNNNN.NNNNNNNN.HHHHHHHH
```

Here:

- `N` is a network bit;
- `H` is a host bit.

Borrow five host bits:

```text
NNNNNNNN.NNNNNNNN.NNNNNNNN.SSSSSHHH
```

where `S` is a borrowed subnet bit.

New mask:

```text
11111111.11111111.11111111.11111000
```

Decimal:

```text
255.255.255.248
```

CIDR:

```text
/29
```

## The Main Tradeoff

Subnetting makes this exchange:

```text
More network bits -> more subnets -> fewer hosts per subnet
```

For an original `/24`:

| Borrowed bits | New prefix | Subnets | Host bits left | Usable hosts/subnet |
| ---: | ---: | ---: | ---: | ---: |
| 0 | `/24` | 1 | 8 | 254 |
| 1 | `/25` | 2 | 7 | 126 |
| 2 | `/26` | 4 | 6 | 62 |
| 3 | `/27` | 8 | 5 | 30 |
| 4 | `/28` | 16 | 4 | 14 |
| 5 | `/29` | 32 | 3 | 6 |
| 6 | `/30` | 64 | 2 | 2 |

For ordinary LAN calculations, `/31` and `/32` require special handling and do not follow the standard `2^h - 2` expectation in the same way as `/30` and shorter prefixes.

## Formulas

### Number Of Subnets

```text
Number of subnets = 2^n
```

where `n` is the number of borrowed bits.

### Total Addresses Per Subnet

```text
Total addresses = 2^h
```

where `h` is the number of host bits remaining.

### Usable Hosts In An Ordinary Subnet

```text
Usable hosts = 2^h - 2
```

The excluded addresses are:

- network address;
- broadcast address.

### New Prefix

```text
New prefix = original prefix + borrowed bits
```

## Important Note About Subnet Zero

Modern calculations include every created subnet, including:

- the first subnet whose subnet bits are all zero;
- the final subnet whose subnet bits are all one.

Five borrowed bits therefore produce:

```text
2^5 = 32 subnets
```

not 30.

Older materials can show `2^n - 2` for the number of subnets. That rule came from excluding subnet zero and the all-ones subnet. Modern CCNA design and normal Cisco configurations use `2^n`.

## Three-Stage Model

The source lesson can be summarized in three broad stages:

1. Find the required number of subnet bits.
2. Build the mask and determine the increment.
3. Use the increment to list ranges.

In practice, add a fourth:

4. Verify the usable-host capacity of each subnet.

Without that validation, a calculation can satisfy the network count but produce subnets too small for the business requirement.

## Example 1: Divide A `/24` Into 25 Subnets

Given:

```text
Parent network:    192.168.10.0/24
Required subnets:  25
```

### Step 1: Find The Borrowed Bits

Find the smallest `n` for which:

```text
2^n >= 25
```

Check:

```text
2^4 = 16   insufficient
2^5 = 32   sufficient
```

Required:

```text
5 borrowed bits
```

You do not need the exact binary representation of decimal 25 to build the ranges. The important result is the minimum binary field width capable of representing at least 25 combinations.

### Step 2: Find The New Prefix

```text
Original prefix: /24
Borrowed bits:    5
New prefix:       /29
```

Binary mask:

```text
11111111.11111111.11111111.11111000
```

Decimal mask:

```text
255.255.255.248
```

### Step 3: Find The Increment

There are two equivalent methods.

#### Method A: Lowest Network-Bit Value

The final network bit in the interesting octet has weight:

```text
8
```

Therefore:

```text
Increment = 8
```

#### Method B: 256 Minus The Mask Octet

```text
Increment = 256 - 248 = 8
```

Apply this formula to the interesting octet, where the mask is neither `255` nor `0`.

### Step 4: List Network Addresses

Add the increment repeatedly:

```text
192.168.10.0
192.168.10.8
192.168.10.16
192.168.10.24
192.168.10.32
192.168.10.40
...
192.168.10.248
```

This produces 32 networks:

```text
0, 8, 16, 24, ..., 248
```

### Step 5: Build The Ranges

Each subnet contains 8 total addresses.

| Subnet | Network | First host | Last host | Broadcast |
| ---: | --- | --- | --- | --- |
| 1 | `192.168.10.0/29` | `192.168.10.1` | `192.168.10.6` | `192.168.10.7` |
| 2 | `192.168.10.8/29` | `192.168.10.9` | `192.168.10.14` | `192.168.10.15` |
| 3 | `192.168.10.16/29` | `192.168.10.17` | `192.168.10.22` | `192.168.10.23` |
| 4 | `192.168.10.24/29` | `192.168.10.25` | `192.168.10.30` | `192.168.10.31` |
| 5 | `192.168.10.32/29` | `192.168.10.33` | `192.168.10.38` | `192.168.10.39` |
| ... | ... | ... | ... | ... |
| 32 | `192.168.10.248/29` | `192.168.10.249` | `192.168.10.254` | `192.168.10.255` |

Rules:

```text
Broadcast = next network - 1
First host = network + 1
Last host = broadcast - 1
```

### Step 6: Verify Host Capacity

The host bits remaining are:

```text
8 original host bits - 5 borrowed bits = 3 host bits
```

Total addresses:

```text
2^3 = 8
```

Usable hosts:

```text
2^3 - 2 = 6
```

Result:

```text
32 subnets
6 usable hosts per subnet
```

The requirement for 25 subnets is satisfied, but the design is useful only if every segment needs no more than 6 ordinary host addresses.

## Why 25 Becomes 32

Binary fields provide combinations in powers of two:

```text
1, 2, 4, 8, 16, 32, 64, ...
```

You cannot borrow part of a bit to produce exactly 25 equal subnets.

Four bits are insufficient:

```text
2^4 = 16
```

Five bits provide:

```text
2^5 = 32
```

The remaining seven subnets can be:

- reserved for growth;
- left unallocated;
- assigned to new sites;
- recorded in the IP address plan.

## Binary Subnet IDs

Five borrowed bits form subnet IDs from:

```text
00000
```

through:

```text
11111
```

Together with three host bits:

```text
SSSSSHHH
```

Examples:

| Subnet bits | Host bits at network | Last octet decimal |
| --- | --- | ---: |
| `00000` | `000` | 0 |
| `00001` | `000` | 8 |
| `00010` | `000` | 16 |
| `00011` | `000` | 24 |
| `00100` | `000` | 32 |
| `11111` | `000` | 248 |

The increment is `8` because the three host bits form a block of:

```text
2^3 = 8 addresses
```

## Network, Hosts And Broadcast In Binary

Consider the second subnet:

```text
192.168.10.8/29
```

The last octet of its network address is:

```text
00001000
```

Five subnet bits and three host bits:

```text
00001|000
```

The network address has every host bit set to zero:

```text
00001|000 = 8
```

First host:

```text
00001|001 = 9
```

Last host:

```text
00001|110 = 14
```

The broadcast address has every host bit set to one:

```text
00001|111 = 15
```

Network and broadcast addresses are not arbitrary exclusions. Their roles follow directly from the host-bit values.

## Example 2: Divide A `/24` Into 60 Subnets

Given:

```text
Parent network:    216.5.10.0/24
Required subnets:  60
```

### Find Borrowed Bits

```text
2^5 = 32   insufficient
2^6 = 64   sufficient
```

Required:

```text
6 borrowed bits
```

### Find The New Prefix

```text
/24 + 6 = /30
```

Mask:

```text
255.255.255.252
```

Binary:

```text
11111111.11111111.11111111.11111100
```

### Find The Increment

```text
256 - 252 = 4
```

Network addresses:

```text
216.5.10.0
216.5.10.4
216.5.10.8
216.5.10.12
216.5.10.16
...
216.5.10.252
```

### First Ranges

| Subnet | Network | First host | Last host | Broadcast |
| ---: | --- | --- | --- | --- |
| 1 | `216.5.10.0/30` | `216.5.10.1` | `216.5.10.2` | `216.5.10.3` |
| 2 | `216.5.10.4/30` | `216.5.10.5` | `216.5.10.6` | `216.5.10.7` |
| 3 | `216.5.10.8/30` | `216.5.10.9` | `216.5.10.10` | `216.5.10.11` |
| 4 | `216.5.10.12/30` | `216.5.10.13` | `216.5.10.14` | `216.5.10.15` |
| ... | ... | ... | ... | ... |
| 64 | `216.5.10.252/30` | `216.5.10.253` | `216.5.10.254` | `216.5.10.255` |

### Verify Host Capacity

Two host bits remain:

```text
2^2 = 4 total addresses
2^2 - 2 = 2 usable hosts
```

Result:

```text
64 subnets
2 usable hosts per subnet
```

This `/30` fits traditional point-to-point links but normally does not fit a LAN containing several endpoints.

## Why `/30` Is Useful

A point-to-point link joins exactly two Layer 3 interfaces:

```text
Router A <--------> Router B
```

A traditional IPv4 `/30` provides:

- one network address;
- two usable interface addresses;
- one broadcast address.

Example:

```text
10.0.0.0/30
```

```text
Network:    10.0.0.0
Router A:   10.0.0.1
Router B:   10.0.0.2
Broadcast:  10.0.0.3
```

Modern point-to-point links can also use `/31` under RFC 3021 when supported by the devices, provider design and operational tools. `/30` remains important for learning and compatibility.

## Increment And Block Size

These terms are often interchangeable in this context:

```text
Increment = block size
```

For `/29`:

```text
Mask octet: 248
Block size:  256 - 248 = 8
```

For `/30`:

```text
Mask octet: 252
Block size:  256 - 252 = 4
```

Also:

```text
Block size = 2^(host bits in interesting octet)
```

With `/29`, three host bits remain in the final octet:

```text
2^3 = 8
```

## Last-Octet Increment Table

| Prefix | Mask | Increment | Total addresses | Usable hosts |
| ---: | --- | ---: | ---: | ---: |
| `/25` | `255.255.255.128` | 128 | 128 | 126 |
| `/26` | `255.255.255.192` | 64 | 64 | 62 |
| `/27` | `255.255.255.224` | 32 | 32 | 30 |
| `/28` | `255.255.255.240` | 16 | 16 | 14 |
| `/29` | `255.255.255.248` | 8 | 8 | 6 |
| `/30` | `255.255.255.252` | 4 | 4 | 2 |

This table follows from binary; it is not a collection of arbitrary values.

## Interesting Octet

The interesting octet contains the boundary between network and host bits.

Examples:

```text
/26 = 255.255.255.192
Interesting octet: fourth
```

```text
/20 = 255.255.240.0
Interesting octet: third
```

Calculate the increment in that octet:

```text
/20 -> 256 - 240 = 16
```

Network addresses for `172.16.0.0/20` change in the third octet:

```text
172.16.0.0
172.16.16.0
172.16.32.0
172.16.48.0
...
```

## Validating Host Requirements

Suppose:

```text
Parent:            192.168.10.0/24
Required subnets:  25
Required hosts:    10 per subnet
```

Twenty-five subnets require five borrowed bits:

```text
/24 -> /29
```

But `/29` provides only:

```text
6 usable hosts
```

The requirements are incompatible inside one `/24`.

It is impossible to obtain 25 equal subnets containing 10 usable hosts each from only 256 total addresses. Even before network and broadcast overhead:

```text
25 * 10 = 250 host addresses
```

Possible responses:

- obtain a larger parent block;
- reduce the subnet count;
- reduce the host requirement;
- use VLSM when segments have different sizes;
- revise the architecture.

## FLSM And VLSM

The current technique creates equal-size subnets:

```text
FLSM = Fixed Length Subnet Mask
```

Every child network receives the same prefix:

```text
192.168.10.0/24 -> 32 x /29
```

If some segments need 60 hosts, others need 12 and links need only 2, an equal size can waste address space.

Then use:

```text
VLSM = Variable Length Subnet Mask
```

VLSM assigns different prefixes to different requirements. First become comfortable with FLSM, increments and boundaries.

## Practical Algorithm

### Inputs

Write down:

```text
Parent network:
Parent prefix:
Required subnets:
Required hosts per subnet:
```

If the host requirement is unknown, the result is not a fully validated design.

### Calculation

1. Find the minimum `n` where `2^n >= required subnets`.
2. Calculate `new prefix = original prefix + n`.
3. Find the new dotted-decimal mask.
4. Identify the interesting octet.
5. Calculate `increment = 256 - mask octet`.
6. List network addresses using that increment.
7. Find each broadcast as `next network - 1`.
8. Find first and last usable hosts.
9. Calculate remaining host bits.
10. Compare `2^h - 2` with the host requirement.
11. Confirm every child subnet remains inside the parent block.
12. Document the allocation.

## Worked Exercise

Given:

```text
Parent network:    10.40.8.0/24
Required subnets:  10
```

### Borrowed Bits

```text
2^3 = 8    insufficient
2^4 = 16   sufficient
```

```text
Borrowed bits = 4
```

### New Prefix

```text
/24 + 4 = /28
```

```text
Mask = 255.255.255.240
```

### Increment

```text
256 - 240 = 16
```

### Capacity

```text
Subnets:        2^4 = 16
Host bits:      4
Total/subnet:   2^4 = 16
Usable/subnet:  2^4 - 2 = 14
```

### First Networks

```text
10.40.8.0/28
10.40.8.16/28
10.40.8.32/28
10.40.8.48/28
10.40.8.64/28
...
```

### First Ranges

| Network | Usable range | Broadcast |
| --- | --- | --- |
| `10.40.8.0/28` | `10.40.8.1 - 10.40.8.14` | `10.40.8.15` |
| `10.40.8.16/28` | `10.40.8.17 - 10.40.8.30` | `10.40.8.31` |
| `10.40.8.32/28` | `10.40.8.33 - 10.40.8.46` | `10.40.8.47` |
| `10.40.8.48/28` | `10.40.8.49 - 10.40.8.62` | `10.40.8.63` |

## Practice

For each example, find:

- borrowed bits;
- new prefix;
- dotted-decimal mask;
- increment;
- number of produced subnets;
- usable hosts per subnet;
- first three network addresses.

### Exercise 1

```text
172.16.50.0/24
Required subnets: 6
```

### Exercise 2

```text
10.20.30.0/24
Required subnets: 12
```

### Exercise 3

```text
192.0.2.0/24
Required subnets: 50
```

## Answers

### Exercise 1

```text
Borrowed bits: 3
New prefix:    /27
Mask:          255.255.255.224
Increment:     32
Subnets:       8
Usable hosts:  30
Networks:      172.16.50.0, 172.16.50.32, 172.16.50.64
```

### Exercise 2

```text
Borrowed bits: 4
New prefix:    /28
Mask:          255.255.255.240
Increment:     16
Subnets:       16
Usable hosts:  14
Networks:      10.20.30.0, 10.20.30.16, 10.20.30.32
```

### Exercise 3

```text
Borrowed bits: 6
New prefix:    /30
Mask:          255.255.255.252
Increment:     4
Subnets:       64
Usable hosts:  2
Networks:      192.0.2.0, 192.0.2.4, 192.0.2.8
```

## Cisco IOS Check

After calculating a subnet, assign an interface address:

```text
Router(config)# interface gigabitEthernet 0/0
Router(config-if)# ip address 192.168.10.1 255.255.255.248
Router(config-if)# no shutdown
```

Verify:

```text
Router# show ip interface brief
Router# show ip route connected
```

The connected route should include:

```text
192.168.10.0/29
```

The router does not validate the business host requirement. It only applies a syntactically valid mask. Sizing remains the engineer's responsibility.

## Common Mistakes

### Choosing A Power Of Two Below The Requirement

For 25 subnets:

```text
2^4 = 16
```

is insufficient. Round up to 32.

### Adding The Subnet Count To The Prefix

Incorrect:

```text
/24 + 25
```

Add borrowed bits, not networks:

```text
/24 + 5 = /29
```

### Using `2^n - 2` For Modern Subnet Counts

Use:

```text
2^n
```

### Forgetting To Validate Hosts

Twenty-five subnets from a `/24` produce `/29`, but only 6 usable hosts per subnet.

### Treating Increment As Usable Hosts

The `/29` increment is 8, while its usable-host count is 6.

### Making Broadcast Equal To The Next Network

Broadcast is one address earlier:

```text
Next network: 192.168.10.8
Broadcast:    192.168.10.7
```

### Assigning Network Or Broadcast To An Interface

In an ordinary `/29`, do not assign:

```text
192.168.10.0
192.168.10.7
```

### Leaving The Parent Block

Every child subnet must remain entirely within the original allocation.

### Relying On Classful Terms

`192.168.10.0/24` is sometimes informally called a Class C network, but modern design uses the CIDR prefix. The first octet alone does not determine the actual mask.

## Quick Self-Check

### Question 1

How many bits must be borrowed to produce at least 25 subnets?

Answer:

```text
5 bits, because 2^5 = 32.
```

### Question 2

What prefix results from borrowing 5 bits from a `/24`?

Answer:

```text
/29
```

### Question 3

What is the `/29` mask?

Answer:

```text
255.255.255.248
```

### Question 4

What is the `/29` increment in the fourth octet?

Answer:

```text
256 - 248 = 8
```

### Question 5

How many usable hosts does an ordinary `/29` provide?

Answer:

```text
2^3 - 2 = 6
```

### Question 6

How do you find the broadcast for `192.168.10.16/29`?

Answer:

```text
The next network begins at 192.168.10.24,
so the broadcast is 192.168.10.23.
```

### Question 7

Why can one `/24` not provide 25 FLSM subnets with 10 usable hosts each?

Answer:

```text
Twenty-five subnets require `/29`, which provides only 6 usable hosts.
```

## Commands And Terms

| Term | Meaning |
| --- | --- |
| Parent network | Original block divided into child subnets. |
| Borrowed bit | Host bit converted into a network/subnet bit. |
| FLSM | Equal-size subnetting with one mask. |
| VLSM | Allocating subnets of different sizes. |
| Prefix length | Number of network bits in a mask. |
| Interesting octet | Octet containing the network/host boundary. |
| Increment | Distance between adjacent network addresses. |
| Block size | Total addresses in one aligned subnet block. |
| Network address | First address of an ordinary subnet, with all host bits zero. |
| Broadcast address | Final address of an ordinary subnet, with all host bits one. |
| Usable range | Addresses between network and broadcast. |

## What To Review Later

- Binary subnet masks
- Powers of two
- Interesting octet
- Block-size method
- Finding network and broadcast addresses
- FLSM
- VLSM
- `/31` point-to-point addressing
- Route summarization

