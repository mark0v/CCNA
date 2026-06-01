# Subnet Mask Defines the Network

Source: closed course page  
Date added: 2026-06-01  
Related plan item: Week 5 / Subnet mask and network boundaries  
Tags: subnet mask, ipv4, network portion, host portion, classful addressing, subnetting, default gateway
Language: English
Translation pair: articles/2026-05/week-05/01-subnet-mask-defines-the-network.md

## Summary

An IP address by itself does not tell a device where its local network ends and where the outside world begins. The subnet mask defines that boundary. It tells the device which part of the IPv4 address is the network portion and which part is the host portion.

Main idea: the subnet mask answers the question "is this destination in my network, or do I need a router?"

## Key Points

- An IP address without a subnet mask is incomplete.
- The subnet mask defines the network portion and host portion.
- The network portion identifies the network.
- The host portion identifies a specific device inside that network.
- If the destination is local, the host can send traffic directly inside the LAN.
- If the destination is remote, the host sends traffic to the default gateway.
- `255` in a simple mask means network part.
- `0` in a simple mask means host part.
- Default classful masks: Class A `/8`, Class B `/16`, Class C `/24`.
- Huge default networks are not practical for real operations.
- Subnetting divides a larger network into smaller manageable networks.
- `/24` commonly provides 254 usable host addresses.

## Notes

### Why The Subnet Mask Matters

When we assign an IP address to a device, it may feel like the important part is done.

But that is only half the story.

The device still needs to know:

```text
Who is on my local network?
Who requires a router?
```

That is the job of the subnet mask.

The IP address says:

```text
Here is my address.
```

The subnet mask says:

```text
This part of the address describes the network.
This part of the address describes the host.
```

Without that boundary, the device cannot make a correct routing decision.

### Network Portion And Host Portion

An IPv4 address has two logical parts:

- network portion;
- host portion.

The network portion describes the "neighborhood", or the network.

The host portion describes the "house number" inside that neighborhood, or the specific device.

Useful analogy:

```text
Network portion = neighborhood
Host portion = house number inside that neighborhood
```

The subnet mask shows where the line between those parts is.

### Simple 255 And 0 Rule

Before going deep into binary, use this simple model:

```text
255 = this part of the IP address belongs to the network
0   = this part of the IP address belongs to the host
```

This is not the whole subnetting theory, but it is perfect for the first mental model.

Example:

```text
IP address:   10.5.90.110
Subnet mask:  255.0.0.0
```

Here:

```text
Network portion: 10
Host portion:    5.90.110
```

The device treats anything starting with `10` as local.

Another example:

```text
IP address:   172.21.160.5
Subnet mask:  255.255.0.0
```

Here:

```text
Network portion: 172.21
Host portion:    160.5
```

The device treats anything starting with `172.21` as local.

### Local Or Remote

The practical job of the subnet mask:

```text
Decide whether the destination is local or remote.
```

If the destination is local:

- the host tries to deliver the frame directly inside the local network;
- for IPv4, it can use ARP to find the destination MAC address;
- no router is needed.

If the destination is remote:

- the host realizes the destination is outside the local network;
- the host sends the frame to the default gateway MAC address;
- the packet inside the frame still contains the final destination IP.

The subnet mask is the line in the sand:

```text
This side = my network.
That side = I need a router.
```

### Default Gateway Can Be Missing, Mask Cannot

A host can live without a default gateway if it only needs to communicate inside the local network.

Example:

```text
IP address:   192.168.1.10
Subnet mask:  255.255.255.0
Gateway:      not configured
```

This device can still talk to other hosts in `192.168.1.0/24` if Layer 2 connectivity works.

But without a subnet mask, the operating system does not know which network is local.

That is why an IP address without a mask is incomplete configuration.

### A Quick Word About Octets

An IPv4 address has four octets.

Example:

```text
192.168.10.25
```

Here:

- `192` = first octet;
- `168` = second octet;
- `10` = third octet;
- `25` = fourth octet.

Each octet ranges from `0` to `255`.

The word `octet` matters because subnet masks are also written as four octets:

```text
255.255.255.0
```

### Classful Defaults

Historically, IPv4 addresses were grouped into classes:

| Class | First octet range | Default mask | Prefix |
| --- | --- | --- | --- |
| Class A | 1-126 | 255.0.0.0 | /8 |
| Class B | 128-191 | 255.255.0.0 | /16 |
| Class C | 192-223 | 255.255.255.0 | /24 |

This is called classful addressing.

Modern networks should not be designed only with classful thinking because we use CIDR and subnetting. But the default masks help explain where the familiar boundaries came from.

### Why Default Networks Are Too Big

A Class A network like:

```text
10.0.0.0
255.0.0.0
```

has a very large address space.

Usable host addresses:

```text
16,777,214
```

That is too many for one normal local network.

Problems with giant flat networks:

- too much broadcast traffic;
- harder troubleshooting;
- weaker security boundaries;
- harder separation of departments/locations;
- harder growth control;
- less predictable network behavior.

In real life, we need smaller networks.

### What Subnetting Does

Subnetting is the process of taking a large network and dividing it into smaller networks.

We do this by changing the subnet mask.

Simple idea:

```text
Move the boundary between the network portion and host portion.
```

The more bits are given to the network portion, the more subnets you can create.

The fewer bits remain for the host portion, the fewer hosts fit in each subnet.

This is the trade-off:

```text
more networks = fewer hosts per network
fewer networks = more hosts per network
```

### NetworkChuck Coffee Example

Imagine NetworkChuck Coffee.

We have a large private range:

```text
10.0.0.0
```

If we keep the default Class A mask:

```text
255.0.0.0
```

we get one enormous network.

But the business has multiple coffee shops, and each location is easier to manage with its own subnet.

Example:

```text
10.0.1.0/24  = Coffee House 1
10.0.2.0/24  = Coffee House 2
10.0.3.0/24  = Coffee House 3
10.0.4.0/24  = Coffee House 4
```

`/24` means:

```text
255.255.255.0
```

In this subnet, you usually get:

```text
254 usable host addresses
```

That is usually enough for:

- registers;
- laptops;
- printers;
- tablets;
- cameras;
- phones;
- access points;
- office devices.

Now every coffee shop has its own clear and manageable network.

### Why Smaller Subnets Are Useful

Smaller subnets help:

- reduce the broadcast domain;
- simplify troubleshooting;
- separate locations;
- apply security rules;
- plan addressing;
- control growth;
- make routing easier to understand.

This is not only an exam topic.

It is a real operational skill.

### Important Memory Hook

Remember:

```text
IP address identifies the host.
Subnet mask defines the network boundary.
Default gateway connects you to other networks.
```

Even shorter:

```text
IP = who I am
Mask = who is local
Gateway = where I go for remote
```

### Why Binary Comes Next

The `255 = network` and `0 = host` rule is good for simple masks:

```text
255.0.0.0
255.255.0.0
255.255.255.0
```

But subnetting becomes more interesting when the mask looks like:

```text
255.255.255.128
255.255.255.192
255.255.255.224
```

To understand those, we need binary.

Binary explains why a mask can cut a network not only between octets, but also inside an octet.

## Examples

### Example 1

```text
IP address:   10.5.90.110
Subnet mask:  255.0.0.0
```

Result:

```text
Network: 10.0.0.0
Host:    5.90.110
```

Simple reading:

```text
Anything starting with 10 is local.
```

### Example 2

```text
IP address:   172.21.160.5
Subnet mask:  255.255.0.0
```

Result:

```text
Network: 172.21.0.0
Host:    160.5
```

Simple reading:

```text
Anything starting with 172.21 is local.
```

### Example 3

```text
IP address:   10.0.3.50
Subnet mask:  255.255.255.0
```

Result:

```text
Network: 10.0.3.0
Host:    50
```

Simple reading:

```text
Anything starting with 10.0.3 is local.
```

## Quick Self-Check

### Question 1

What does subnet mask define?

Answer:

```text
The boundary between network portion and host portion.
```

### Question 2

Can a host communicate locally without a default gateway?

Answer:

```text
Yes, if it has a valid IP address, subnet mask and Layer 2 connectivity.
```

### Question 3

What does `/24` mean in decimal subnet mask form?

Answer:

```text
255.255.255.0
```

### Question 4

Why are huge flat networks bad?

Answer:

```text
They create too much broadcast traffic and are harder to secure, troubleshoot and manage.
```

### Question 5

What does subnetting do?

Answer:

```text
It divides a larger network into smaller networks by changing the subnet mask.
```

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Subnet mask | Value that defines which part of IPv4 address is network and which part is host. |
| Network portion | Part of IP address that identifies the network. |
| Host portion | Part of IP address that identifies a device inside the network. |
| Octet | One of four decimal numbers in IPv4 address. |
| Classful addressing | Old IPv4 model with Class A/B/C default masks. |
| `/24` | Prefix length equivalent to `255.255.255.0`. |
| Subnetting | Dividing a larger network into smaller networks. |
| Default gateway | Router address used to reach remote networks. |
| Broadcast domain | Area where broadcast traffic is heard. |

## What To Review Later

- IPv4 address structure
- Private vs public IP addresses
- Binary subnet masks
- CIDR notation
- Default gateway
- ARP
- Broadcast domains
- Routing between subnets

