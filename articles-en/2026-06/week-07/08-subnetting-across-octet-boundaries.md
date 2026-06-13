# Subnetting Across Octet Boundaries

Source: closed course page  
Date added: 2026-06-13  
Related plan item: Week 7 / Subnetting across octet boundaries  
Tags: subnetting, FLSM, CIDR, octet boundary, rollover, class A, class B, increment
Language: English
Translation pair: articles/2026-06/week-07/08-subnetting-across-octet-boundaries.md

## Summary

The subnetting algorithm does not change for larger parent networks. A `/16` or `/8` follows the same steps as a `/24`:

1. Find the minimum number of borrowed bits.
2. Determine the new prefix and mask.
3. Identify the interesting octet and increment.
4. List the network ranges.
5. Verify usable-host capacity.

The main challenge is not a new formula. It is remembering that:

- the increment can occur in the second, third or fourth octet;
- when an octet reaches `256`, it resets to zero and increments the octet to its left.

Example:

```text
172.16.0.0/16
Required subnets: 100

Borrowed bits: 7
New prefix:    /23
Mask:          255.255.254.0
Increment:     2 in the third octet
Subnets:       128
Usable hosts:  510 per subnet
```

## Key Points

- The CIDR prefix, not the historical address class, defines the actual network boundary.
- For FLSM, the subnet count is `2^n`, where `n` is the number of borrowed bits.
- The new prefix is the original prefix plus the borrowed bits.
- The interesting octet contains the network-to-host transition.
- Calculate the increment as `256 - mask value` in the interesting octet.
- An octet can contain only values from `0` through `255`.
- Reaching `256` while adding the increment causes rollover into the octet on the left.
- An address ending in `.0` or `.255` is not automatically a network or broadcast address.
- Address roles depend on the prefix and the boundaries of the specific subnet.
- A broadcast address is immediately before the next network.
- A mathematically valid large host count is not automatically a good LAN design.

## Classful Terms And Modern CIDR

Historically, IPv4 unicast addresses were divided into classes:

| Class | First octet | Default mask | Default prefix |
| --- | --- | --- | ---: |
| A | 1-126 | `255.0.0.0` | `/8` |
| B | 128-191 | `255.255.0.0` | `/16` |
| C | 192-223 | `255.255.255.0` | `/24` |

In older exercises, "subnet a Class B network" usually means:

```text
Start with a /16 parent prefix.
```

"Class A" usually means:

```text
Start with a /8 parent prefix.
```

Modern networks use classless routing and CIDR. Therefore:

```text
172.16.0.0/20
```

must not be treated as `/16` merely because `172` historically belonged to Class B. The explicitly stated `/20` is the parent prefix.

This article retains classful terms for continuity with the source lesson, but every calculation uses the actual prefix.

## One Algorithm For Every Parent Prefix

Record the inputs:

```text
Parent network:
Parent prefix:
Required subnets:
Required hosts per subnet:
```

Then:

1. Find the minimum `n` where `2^n >= required subnets`.
2. Calculate `new prefix = parent prefix + n`.
3. Convert the prefix to a dotted-decimal mask.
4. Identify the interesting octet.
5. Calculate the increment in that octet.
6. List the network addresses.
7. Find broadcast as the address before the next network.
8. Find the usable range.
9. Calculate the remaining host bits.
10. Validate host capacity and the parent boundary.

## Finding The Interesting Octet

| Prefix range | Interesting octet |
| --- | --- |
| `/1` - `/8` | First |
| `/9` - `/16` | Second |
| `/17` - `/24` | Third |
| `/25` - `/30` | Fourth |

Examples:

```text
/18 = 255.255.192.0
Interesting octet: third
Increment: 256 - 192 = 64
```

```text
/23 = 255.255.254.0
Interesting octet: third
Increment: 256 - 254 = 2
```

```text
/25 = 255.255.255.128
Interesting octet: fourth
Increment: 256 - 128 = 128
```

## Octet Rollover

An octet cannot contain `256`.

If subnet progression produces:

```text
172.20.0.128 + 128
```

the intermediate result is:

```text
172.20.0.256
```

That notation is invalid. Carry the `256` into the octet on the left:

```text
172.20.1.0
```

Similarly:

```text
10.0.192.0 + 64 in the third octet
```

becomes:

```text
10.0.256.0 -> 10.1.0.0
```

This is normal positional addition, not a special subnetting exception.

## Example 1: Divide A `/16` Into 100 Subnets

Given:

```text
Parent network:    172.16.0.0/16
Required subnets:  100
```

### Step 1: Find Borrowed Bits

```text
2^6 = 64    insufficient
2^7 = 128   sufficient
```

```text
Borrowed bits = 7
```

### Step 2: Find The New Prefix

```text
/16 + 7 = /23
```

Binary mask:

```text
11111111.11111111.11111110.00000000
```

Decimal mask:

```text
255.255.254.0
```

### Step 3: Find The Increment

The interesting octet is the third:

```text
256 - 254 = 2
```

```text
Increment = 2 in the third octet
```

### Step 4: List Networks

```text
172.16.0.0/23
172.16.2.0/23
172.16.4.0/23
172.16.6.0/23
...
172.16.254.0/23
```

Total:

```text
2^7 = 128 subnets
```

### Step 5: Find The First Range

First network:

```text
172.16.0.0/23
```

Next network:

```text
172.16.2.0/23
```

Therefore:

```text
Network:    172.16.0.0
First host: 172.16.0.1
Last host:  172.16.1.254
Broadcast:  172.16.1.255
```

The subnet spans two third-octet values:

```text
172.16.0.x
172.16.1.x
```

### Second Range

```text
Network:    172.16.2.0
First host: 172.16.2.1
Last host:  172.16.3.254
Broadcast:  172.16.3.255
```

### Final Range

```text
Network:    172.16.254.0
First host: 172.16.254.1
Last host:  172.16.255.254
Broadcast:  172.16.255.255
```

### Step 6: Verify Hosts

After `/23`, the remaining host bits are:

```text
32 - 23 = 9 host bits
```

```text
Total addresses: 2^9 = 512
Usable hosts:    2^9 - 2 = 510
```

Result:

```text
128 subnets
510 usable hosts per subnet
```

## Why `.0` And `.255` Can Be Usable

Consider:

```text
172.16.0.0/23
```

Its range is:

```text
172.16.0.0 - 172.16.1.255
```

Only the first address of the entire `/23` is the network:

```text
172.16.0.0
```

Only the final address is the broadcast:

```text
172.16.1.255
```

These addresses are therefore inside the usable range:

```text
172.16.0.255
172.16.1.0
```

Full check:

```text
First usable: 172.16.0.1
Last usable:  172.16.1.254
```

An ending of `.0` or `.255` proves nothing by itself. You must know the prefix and subnet boundaries.

## Boundary Rule

For an ordinary IPv4 subnet:

```text
First address of subnet = network
Last address of subnet  = broadcast
Everything between      = usable host range
```

This is sometimes called the Oreo rule: the two outside addresses are not assigned to hosts, while the middle is usable.

A more precise binary interpretation is:

- the network has all host bits set to `0`;
- the broadcast has all host bits set to `1`;
- intermediate combinations are host addresses.

## Example 2: Divide A `/16` Into 500 Subnets

Given:

```text
Parent network:    172.20.0.0/16
Required subnets:  500
```

### Borrowed Bits

```text
2^8 = 256   insufficient
2^9 = 512   sufficient
```

```text
Borrowed bits = 9
```

### New Prefix

```text
/16 + 9 = /25
```

Mask:

```text
255.255.255.128
```

Binary role:

```text
NNNNNNNN.NNNNNNNN.SSSSSSSS.SHHHHHHH
```

All eight bits of the third octet and one bit of the fourth become subnet bits.

### Increment

The interesting octet is now the fourth:

```text
256 - 128 = 128
```

```text
Increment = 128 in the fourth octet
```

### Network Progression

```text
172.20.0.0/25
172.20.0.128/25
172.20.1.0/25
172.20.1.128/25
172.20.2.0/25
172.20.2.128/25
...
172.20.255.128/25
```

The rollover:

```text
172.20.0.128 + 128
= 172.20.0.256
= 172.20.1.0
```

### First Ranges

| Network | First host | Last host | Broadcast |
| --- | --- | --- | --- |
| `172.20.0.0/25` | `172.20.0.1` | `172.20.0.126` | `172.20.0.127` |
| `172.20.0.128/25` | `172.20.0.129` | `172.20.0.254` | `172.20.0.255` |
| `172.20.1.0/25` | `172.20.1.1` | `172.20.1.126` | `172.20.1.127` |
| `172.20.1.128/25` | `172.20.1.129` | `172.20.1.254` | `172.20.1.255` |

### Capacity

```text
Subnets:       2^9 = 512
Host bits:     32 - 25 = 7
Total/subnet:  2^7 = 128
Usable hosts:  2^7 - 2 = 126
```

The requirement for 500 subnets is satisfied, leaving 12 spare subnets.

## Example 3: Divide A `/8` Into 1000 Subnets

Given:

```text
Parent network:    10.0.0.0/8
Required subnets:  1000
```

### Borrowed Bits

```text
2^9 = 512     insufficient
2^10 = 1024   sufficient
```

```text
Borrowed bits = 10
```

### New Prefix

```text
/8 + 10 = /18
```

Mask:

```text
255.255.192.0
```

Binary:

```text
11111111.11111111.11000000.00000000
```

Borrowing covers:

- all eight bits of the second octet;
- the first two bits of the third octet.

### Increment

The interesting octet is the third:

```text
256 - 192 = 64
```

```text
Increment = 64 in the third octet
```

### Network Progression

```text
10.0.0.0/18
10.0.64.0/18
10.0.128.0/18
10.0.192.0/18
10.1.0.0/18
10.1.64.0/18
10.1.128.0/18
10.1.192.0/18
10.2.0.0/18
...
10.255.192.0/18
```

After four `/18` blocks, the third octet rolls over:

```text
10.0.192.0 + 64
= 10.0.256.0
= 10.1.0.0
```

### First Ranges

| Network | First host | Last host | Broadcast |
| --- | --- | --- | --- |
| `10.0.0.0/18` | `10.0.0.1` | `10.0.63.254` | `10.0.63.255` |
| `10.0.64.0/18` | `10.0.64.1` | `10.0.127.254` | `10.0.127.255` |
| `10.0.128.0/18` | `10.0.128.1` | `10.0.191.254` | `10.0.191.255` |
| `10.0.192.0/18` | `10.0.192.1` | `10.0.255.254` | `10.0.255.255` |
| `10.1.0.0/18` | `10.1.0.1` | `10.1.63.254` | `10.1.63.255` |

### Capacity

```text
Subnets:       2^10 = 1024
Host bits:     32 - 18 = 14
Total/subnet:  2^14 = 16384
Usable hosts:  2^14 - 2 = 16382
```

The subnet count requirement is satisfied, but 16,382 hosts in one broadcast domain is generally excessive for a practical user LAN.

## Mathematically Correct Is Not Automatically Well Designed

A design must also consider:

- actual endpoint count;
- broadcast-domain size;
- fault domain;
- security boundaries;
- DHCP scope;
- wireless density;
- ARP and neighbor scale;
- growth;
- route summarization;
- operational complexity.

A `/18` can be reasonable for:

- a large address pool behind a firewall or NAT;
- container or virtual infrastructure;
- a specialized routed service network;
- a parent block intended for further VLSM allocation.

It should not automatically become one VLAN containing thousands of clients.

## Reading Ranges Reliably

For every subnet:

1. Write the current network.
2. Write the next network.
3. Subtract one address from the next network to find broadcast.
4. Add one to the current network for the first host.
5. Subtract one from broadcast for the last host.

Example:

```text
Current network: 172.16.2.0/23
Next network:    172.16.4.0/23
```

```text
Broadcast:  172.16.3.255
First host: 172.16.2.1
Last host:  172.16.3.254
```

Do not guess the broadcast from the visual appearance of the address.

## Address-Membership Check

Question:

```text
Is 172.16.3.0 usable in 172.16.2.0/23?
```

Range:

```text
Network:    172.16.2.0
Broadcast:  172.16.3.255
Usable:     172.16.2.1 - 172.16.3.254
```

Answer:

```text
Yes. 172.16.3.0 is inside the usable range.
```

Question:

```text
Is 172.16.3.255 usable?
```

Answer:

```text
No. It is the broadcast address of this /23.
```

## Example Comparison

| Parent | Requirement | Borrowed | New prefix | Increment | Subnets | Usable hosts |
| --- | ---: | ---: | ---: | --- | ---: | ---: |
| `192.168.10.0/24` | 25 | 5 | `/29` | 8 in fourth | 32 | 6 |
| `172.16.0.0/16` | 100 | 7 | `/23` | 2 in third | 128 | 510 |
| `172.20.0.0/16` | 500 | 9 | `/25` | 128 in fourth | 512 | 126 |
| `10.0.0.0/8` | 1000 | 10 | `/18` | 64 in third | 1024 | 16382 |

## Practice

For every scenario, find:

- borrowed bits;
- new prefix;
- mask;
- interesting octet;
- increment;
- number of subnets;
- usable hosts per subnet;
- first five network addresses.

### Exercise 1

```text
Parent:            172.30.0.0/16
Required subnets:  50
```

### Exercise 2

```text
Parent:            172.31.0.0/16
Required subnets:  300
```

### Exercise 3

```text
Parent:            10.0.0.0/8
Required subnets:  200
```

## Answers

### Exercise 1

```text
Borrowed bits: 6
New prefix:    /22
Mask:          255.255.252.0
Interesting:   third octet
Increment:     4
Subnets:       64
Usable hosts:  1022
Networks:
172.30.0.0
172.30.4.0
172.30.8.0
172.30.12.0
172.30.16.0
```

### Exercise 2

```text
Borrowed bits: 9
New prefix:    /25
Mask:          255.255.255.128
Interesting:   fourth octet
Increment:     128
Subnets:       512
Usable hosts:  126
Networks:
172.31.0.0
172.31.0.128
172.31.1.0
172.31.1.128
172.31.2.0
```

### Exercise 3

```text
Borrowed bits: 8
New prefix:    /16
Mask:          255.255.0.0
Interesting:   second octet
Increment:     1
Subnets:       256
Usable hosts:  65534
Networks:
10.0.0.0
10.1.0.0
10.2.0.0
10.3.0.0
10.4.0.0
```

For `/16`, the second mask octet is `255`. The increment can be understood as the next complete second-octet value, which is `1`. The formula `256 - mask octet` also yields `1`.

## Checking With Python `ipaddress`

Use Python's standard module to verify a lab calculation:

```python
from ipaddress import ip_network

parent = ip_network("172.16.0.0/16")
subnets = list(parent.subnets(new_prefix=23))

print(len(subnets))
print(subnets[0])
print(subnets[1])
print(subnets[-1])
```

Expected output:

```text
128
172.16.0.0/23
172.16.2.0/23
172.16.254.0/23
```

The tool is useful for verification, but perform the calculation manually first.

## Common Mistakes

### Starting From A Default Class Mask Instead Of The Stated Prefix

If the input is `172.16.0.0/20`, the parent prefix is `/20`, not `/16`.

### Counting The Increment In The Wrong Octet

For `/23`, the increment is `2` in the third octet, not the fourth.

### Continuing Beyond 255 Without Rollover

Incorrect:

```text
10.0.256.0
```

Correct:

```text
10.1.0.0
```

### Treating Every `.0` As A Network Address

`172.16.1.0` is usable inside `172.16.0.0/23`.

### Treating Every `.255` As A Broadcast

`172.16.0.255` is usable inside `172.16.0.0/23`.

### Forgetting Octets To The Right Of The Interesting Octet

A network address sets every host bit on the right to `0`. A broadcast sets them to `1`.

### Failing To Validate Host Capacity

One thousand subnets from a `/8` produce `/18`, but each subnet may be far too large for the intended technology and broadcast domain.

### Confusing Total And Usable Addresses

A `/23` contains 512 total addresses but 510 traditional usable hosts.

## Quick Self-Check

### Question 1

What prefix results from borrowing 7 bits from a `/16`?

Answer:

```text
/23
```

### Question 2

What is the increment for `/23`?

Answer:

```text
2 in the third octet.
```

### Question 3

What is the broadcast for `172.16.2.0/23`?

Answer:

```text
The next network is 172.16.4.0,
so the broadcast is 172.16.3.255.
```

### Question 4

Can `172.16.3.0` be assigned to a host in `172.16.2.0/23`?

Answer:

```text
Yes. The usable range is 172.16.2.1 through 172.16.3.254.
```

### Question 5

What follows `172.20.0.128/25`?

Answer:

```text
172.20.1.0/25
```

### Question 6

How many usable hosts are in a `/18`?

Answer:

```text
2^(32 - 18) - 2 = 2^14 - 2 = 16382.
```

### Question 7

Why should the first address octet not automatically determine the parent mask?

Answer:

```text
Modern routing is classless; the CIDR prefix defines the actual boundary.
```

## Commands And Terms

| Term | Meaning |
| --- | --- |
| Octet boundary | Transition between 8-bit groups in an IPv4 address. |
| Rollover | Carry operation when an octet reaches 256. |
| Interesting octet | Octet containing the network/host boundary. |
| Increment | Step between network addresses in the interesting octet. |
| Borrowed bits | Host bits converted into subnet bits. |
| Classful addressing | Historical default `/8`, `/16` and `/24` scheme. |
| CIDR | Classless addressing using an explicit prefix length. |
| FLSM | Equal-size child subnets using the same mask. |
| Usable host | Address between network and broadcast in an ordinary subnet. |

## What To Review Later

- CIDR prefixes
- Interesting octet
- Increment and block size
- Binary rollover
- Network and broadcast calculations
- Subnetting by host requirement
- FLSM and VLSM
- Route summarization

