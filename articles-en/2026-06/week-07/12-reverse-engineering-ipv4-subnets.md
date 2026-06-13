# Reverse Engineering IPv4 Subnets

Source: closed course page  
Date added: 2026-06-13  
Related plan item: Week 7 / Reverse engineering IPv4 subnets  
Tags: subnetting, troubleshooting, reverse engineering, network address, broadcast, gateway, binary AND
Language: English
Translation pair: articles/2026-06/week-07/12-reverse-engineering-ipv4-subnets.md

## Summary

Troubleshooting more often requires decoding an existing subnet than designing a new one.

Given:

```text
Host address: 192.168.5.22
Mask:         255.255.255.240
```

Determine:

- prefix;
- network address;
- broadcast address;
- usable host range;
- whether other devices share the subnet;
- whether the default gateway is valid.

For this example:

```text
Prefix:      /28
Increment:   16
Network:     192.168.5.16
First host:  192.168.5.17
Last host:   192.168.5.30
Broadcast:   192.168.5.31
```

## Key Points

- An IP address without a mask or prefix does not define a subnet.
- The mask determines block size and boundaries.
- Calculate the increment in the interesting octet.
- A host belongs to the block between adjacent network boundaries.
- The network is the first address in the block.
- The broadcast is the final address in the block.
- A default gateway normally must be a usable address in the host's subnet.
- Devices on one physical switch can belong to different IP subnets.
- A syntactically valid address can still be wrong for a segment.
- Binary AND directly produces the network address.

## When Reverse Subnetting Is Useful

Common situations include:

- checking static IP configuration;
- diagnosing an unreachable default gateway;
- comparing client and server addresses;
- validating a DHCP scope;
- finding an incorrect subnet mask;
- analyzing a routing table;
- inheriting an undocumented network;
- checking firewall objects;
- investigating duplicate or overlapping ranges;
- determining whether an address is network or broadcast.

## Required Inputs

At minimum:

```text
IPv4 address
Subnet mask or prefix
```

Also useful:

```text
Default gateway
DNS servers
VLAN
Interface
DHCP or static source
```

Without a prefix:

```text
192.168.5.22
```

does not tell you whether the host belongs to a `/24`, `/28`, `/30` or another subnet.

## Increment Method

1. Convert the mask to a prefix if necessary.
2. Find the interesting octet.
3. Calculate `increment = 256 - mask octet`.
4. List multiples of the increment.
5. Find the interval containing the host value.
6. The lower boundary is the network.
7. The next boundary minus one is the broadcast.
8. Addresses between them form the usable range.

## Example 1: `192.168.5.22/28`

Mask:

```text
255.255.255.240
```

Binary:

```text
11111111.11111111.11111111.11110000
```

Prefix:

```text
/28
```

Interesting octet:

```text
Fourth octet
```

Increment:

```text
256 - 240 = 16
```

Boundaries:

```text
0, 16, 32, 48, 64, 80, 96, 112,
128, 144, 160, 176, 192, 208, 224, 240
```

Value `22` is in:

```text
16 <= 22 < 32
```

Therefore:

```text
Network:    192.168.5.16
First host: 192.168.5.17
Host:       192.168.5.22
Last host:  192.168.5.30
Broadcast:  192.168.5.31
```

## Fast Boundary Formula

For interesting-octet value `v` and block size `b`:

```text
Network value = floor(v / b) * b
Broadcast value = network value + b - 1
```

For `22` and block size `16`:

```text
floor(22 / 16) = 1
1 * 16 = 16
Broadcast = 16 + 16 - 1 = 31
```

## Binary AND Verification

The network address is:

```text
IP address AND subnet mask
```

Final octet:

```text
22  = 00010110
240 = 11110000
AND = 00010000
```

```text
00010000 = 16
```

Network:

```text
192.168.5.16
```

Find broadcast by setting every host bit to `1`:

```text
Network:   00010000
Host bits:     1111
Broadcast: 00011111 = 31
```

## Default-Gateway Validation

Host:

```text
192.168.5.22/28
```

Usable range:

```text
192.168.5.17 - 192.168.5.30
```

Possible gateway addresses include:

```text
192.168.5.17
192.168.5.30
```

or another assigned router address in the usable range.

Invalid choices:

```text
192.168.5.16   network
192.168.5.31   broadcast
192.168.5.33   different subnet
```

A host normally must consider its gateway directly connected and resolve its Layer 2 address through ARP. Some platforms support special on-link or point-to-point configurations, but normal LAN design requires the gateway to share the subnet.

## Comparing Multiple Devices

Every device uses `/28`:

| Device | Address |
| --- | --- |
| PC | `192.168.5.10/28` |
| Server A | `192.168.5.17/28` |
| Server B | `192.168.5.19/28` |
| Router | `192.168.5.33/28` |

### PC

`10` belongs to block `0-15`:

```text
Network:   192.168.5.0/28
Usable:    192.168.5.1 - 192.168.5.14
Broadcast: 192.168.5.15
```

### Servers

`17` and `19` belong to block `16-31`:

```text
Network:   192.168.5.16/28
Usable:    192.168.5.17 - 192.168.5.30
Broadcast: 192.168.5.31
```

### Router

`33` belongs to block `32-47`:

```text
Network:   192.168.5.32/28
Usable:    192.168.5.33 - 192.168.5.46
Broadcast: 192.168.5.47
```

Result:

```text
PC subnet:      192.168.5.0/28
Server subnet:  192.168.5.16/28
Router subnet:  192.168.5.32/28
```

One switch does not make these addresses one IP subnet.

## Physical Segment And Logical Subnet

A Layer 2 switch forwards Ethernet frames inside a VLAN. An IP host decides whether a destination is local by applying its own address and mask.

For a local destination:

```text
Host performs ARP for destination.
```

For a remote destination:

```text
Host sends packet to default gateway.
```

Two devices can therefore share a physical switch while considering each other remote because of their addresses and masks.

Communication between IP subnets requires Layer 3 forwarding and a correctly reachable gateway for each subnet.

## Why An Off-Subnet Gateway Breaks A Normal LAN

Host:

```text
192.168.5.10/28
```

Gateway:

```text
192.168.5.33
```

The host calculates:

```text
Local network:   192.168.5.0/28
Gateway network: 192.168.5.32/28
```

The gateway is not on-link for the host. A normal configuration cannot use a remote gateway as its next hop without an additional mechanism.

A valid gateway for the PC must be in:

```text
192.168.5.1 - 192.168.5.14
```

## Example 2: Boundary In The Third Octet

Given:

```text
Host: 172.16.35.200/20
Mask: 255.255.240.0
```

Interesting octet:

```text
Third
```

Increment:

```text
256 - 240 = 16
```

Third-octet boundaries:

```text
0, 16, 32, 48, 64, ...
```

`35` is between `32` and `48`.

```text
Network:    172.16.32.0
First host: 172.16.32.1
Last host:  172.16.47.254
Broadcast:  172.16.47.255
```

`172.16.35.200` is usable.

## Example 3: `/23` And Unusual Endings

Given:

```text
Host: 172.20.11.0/23
Mask: 255.255.254.0
```

Third-octet increment:

```text
256 - 254 = 2
```

`11` belongs to block `10-11`.

```text
Network:    172.20.10.0
First host: 172.20.10.1
Last host:  172.20.11.254
Broadcast:  172.20.11.255
```

`172.20.11.0` is a usable host even though it ends in `.0`.

## Example 4: Detecting Broadcast

Given:

```text
Address: 10.4.7.255/21
Mask:    255.255.248.0
```

Third-octet increment:

```text
8
```

Third-octet value `7` belongs to block `0-7`.

```text
Network:   10.4.0.0
Broadcast: 10.4.7.255
```

The given address is the broadcast and must not be assigned to an ordinary host interface.

## Universal Checklist

```text
Given:
  IP address
  Mask/prefix
  Gateway, if available

Derive:
  Prefix
  Interesting octet
  Increment
  Lower boundary
  Next boundary
  Network
  Broadcast
  First host
  Last host

Validate:
  Host is usable
  Gateway is usable
  Host and gateway share subnet
  Peer devices share subnet when expected
  DHCP scope matches
  No overlap exists
```

## Troubleshooting Workflow

1. Obtain the actual device configuration.
2. Do not trust documentation without verification.
3. Record IP, mask and gateway.
4. Determine the host subnet.
5. Confirm the host address is not network or broadcast.
6. Determine the gateway subnet.
7. Confirm the same-subnet relationship.
8. Check ARP or neighbor resolution.
9. Check VLAN and switch port.
10. Check router interface and routing.
11. Compare with DHCP scope or IPAM.
12. Change configuration only after confirming the root cause.

## Windows Commands

```powershell
ipconfig /all
route print
arp -a
ping <gateway>
tracert <destination>
```

Check:

- IPv4 Address;
- Subnet Mask;
- Default Gateway;
- DHCP Enabled;
- lease source;
- route to the local subnet.

## Linux Commands

```bash
ip address
ip route
ip neigh
ping -c 4 <gateway>
tracepath <destination>
```

## Cisco IOS Commands

```text
show ip interface brief
show running-config interface <interface>
show ip route
show arp
show interfaces switchport
show vlan brief
```

## Comparing Two Addresses

The most reliable way to determine whether two addresses share a subnet is:

```text
Network A = Address A AND Mask
Network B = Address B AND Mask
```

If:

```text
Network A == Network B
```

they share a subnet when using the same mask.

If the masks differ, each host can classify the relationship differently. This asymmetric mask mismatch can cause one-way or unstable connectivity.

## Mask Mismatch

Host A:

```text
192.168.5.10/24
```

Host B:

```text
192.168.5.200/28
```

Host A considers Host B local because both are inside `192.168.5.0/24`.

Host B belongs to:

```text
192.168.5.192/28
```

and considers `192.168.5.10` remote.

The result can depend on the gateway, proxy ARP and platform behavior. Even if some packets pass, the configuration is logically inconsistent and should be corrected.

## DHCP-Scope Validation

For:

```text
192.168.5.16/28
```

a valid pool could be:

```text
192.168.5.18 - 192.168.5.30
```

when:

```text
192.168.5.17 = gateway
```

Do not include:

```text
192.168.5.16   network
192.168.5.31   broadcast
192.168.5.32   next subnet
```

## Practice

For each address, find network, usable range and broadcast.

### Exercise 1

```text
192.168.100.77/27
```

### Exercise 2

```text
172.31.73.14/21
```

### Exercise 3

```text
10.10.200.255/18
```

### Exercise 4

```text
203.0.113.191/26
```

Also determine whether the address itself is usable.

## Answers

### Exercise 1

`/27`:

```text
Mask:      255.255.255.224
Increment: 32 in fourth octet
```

`77` belongs to block `64-95`.

```text
Network:    192.168.100.64
First host: 192.168.100.65
Last host:  192.168.100.94
Broadcast:  192.168.100.95
Address:    usable
```

### Exercise 2

`/21`:

```text
Mask:      255.255.248.0
Increment: 8 in third octet
```

`73` belongs to block `72-79`.

```text
Network:    172.31.72.0
First host: 172.31.72.1
Last host:  172.31.79.254
Broadcast:  172.31.79.255
Address:    usable
```

### Exercise 3

`/18`:

```text
Mask:      255.255.192.0
Increment: 64 in third octet
```

`200` belongs to block `192-255`.

```text
Network:    10.10.192.0
First host: 10.10.192.1
Last host:  10.10.255.254
Broadcast:  10.10.255.255
Address:    10.10.200.255 is usable
```

The `.255` ending does not make it broadcast because the broadcast of the entire `/18` is `10.10.255.255`.

### Exercise 4

`/26`:

```text
Mask:      255.255.255.192
Increment: 64 in fourth octet
```

`191` is the end of block `128-191`.

```text
Network:    203.0.113.128
First host: 203.0.113.129
Last host:  203.0.113.190
Broadcast:  203.0.113.191
Address:    broadcast, not usable
```

## Python Verification

```python
from ipaddress import ip_interface

interface = ip_interface("192.168.5.22/28")
network = interface.network

print(network.network_address)
print(network.broadcast_address)
print(network.num_addresses)
print(interface.ip in network)
```

Expected output:

```text
192.168.5.16
192.168.5.31
16
True
```

## Common Mistakes

### Analyzing An IP Without Its Mask

The address alone does not define boundaries.

### Treating Every `.0` As Network

Its role depends on the host bits of the specific prefix.

### Treating Every `.255` As Broadcast

In a subnet larger than `/24`, such an address can be usable.

### Applying Increment In The Wrong Octet

For `/20`, apply the increment in the third octet.

### Making The Next Network The Broadcast

Broadcast is:

```text
next network - 1
```

### Checking Gateway Syntax Only

The gateway must be usable and on-link for a normal LAN host.

### Treating One Switch As One IP Subnet

The switching domain and IP subnet are related by design convention but are not the same concept.

### Ignoring A Mask Mismatch

Two hosts can make different local-versus-remote decisions.

### Relying Only On Ping

Ping failure does not prove a subnet error, and successful ping through proxy ARP does not prove the design is correct.

## Quick Self-Check

### Question 1

What is the increment for `255.255.255.240`?

Answer:

```text
256 - 240 = 16.
```

### Question 2

Which subnet contains `192.168.5.22/28`?

Answer:

```text
192.168.5.16/28.
```

### Question 3

What is the broadcast of that subnet?

Answer:

```text
192.168.5.31.
```

### Question 4

Can `172.20.11.0` be a host address?

Answer:

```text
Yes, for example inside 172.20.10.0/23.
```

### Question 5

Why must a gateway normally share the subnet?

Answer:

```text
The host must reach the next hop directly at Layer 2 and resolve its MAC address.
```

### Question 6

How can you confirm the network without the increment method?

Answer:

```text
Perform a bitwise AND between the IP address and subnet mask.
```

## Commands And Terms

| Term | Meaning |
| --- | --- |
| Reverse subnetting | Deriving boundaries from an existing IP and mask. |
| Interesting octet | Octet containing the network/host boundary. |
| Increment | Step between network boundaries. |
| On-link | Address the host considers directly connected. |
| Binary AND | Operation deriving network address from IP and mask. |
| Mask mismatch | Different masks on devices in one intended segment. |
| Network boundary | First address of an aligned subnet block. |
| Broadcast | Final address of an ordinary IPv4 subnet. |

## What To Review Later

- Binary AND
- Interesting octet
- Block alignment
- Default-gateway behavior
- ARP
- VLAN versus subnet
- DHCP-scope validation
- Proxy ARP
- Troubleshooting workflow

