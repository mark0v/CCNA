# What Now? IP Addressing Foundations

Source: closed course page  
Date added: 2026-06-01  
Related plan item: Week 5 / IP addressing checkpoint before routers  
Tags: ip addressing, cidr, subnet mask, block size, switch management, router, troubleshooting
Language: English
Translation pair: articles/2026-05/week-05/04-what-now-ip-addressing-foundations.md

## Summary

This lesson is a checkpoint after the first IP addressing topics. We now understand why IP addresses exist, how a subnet mask defines the network boundary, how private IPs differ from public IPs, and how an initial addressing plan comes from business requirements.

Main idea: IP addressing stops looking like a pile of numbers and starts looking like a system you can work with.

## Key Points

- IP addressing fundamentals are practical, not just theory.
- CIDR notation helps describe network size.
- Block size patterns prepare you for subnetting.
- Subnet mask helps decide what is local and what is remote.
- Private IPs and NAT explain how internal devices reach the internet.
- Addressing plan should reflect business requirements.
- A switch may not need an IP for Layer 2 forwarding, but it needs an IP for management.
- Routers use IP addressing to connect different networks.
- Troubleshooting often starts with checking IP address, subnet mask and gateway.
- The next big step is router configuration.

## Notes

### This Is Real Networking

When learning basics, it is easy to think:

```text
When do we get to real networking?
```

Answer:

```text
This is real networking.
```

IP addressing, masks, CIDR, private ranges and gateways are not just a warm-up.

They are the foundation for:

- router configuration;
- subnetting;
- VLAN design;
- inter-VLAN routing;
- routing tables;
- firewall rules;
- troubleshooting;
- network documentation.

If the IP foundation is weak, every next topic feels chaotic.

If the foundation is solid, router topics start to make sense.

### You Know More Than You Think

At this point, you can already:

- understand IPv4 address structure;
- see network and host portions;
- read simple subnet masks;
- understand `/24`;
- recognize private IPv4 ranges;
- explain why NAT is needed;
- understand why large flat networks are bad;
- see why separate network segments are useful;
- create a simple addressing pattern for sites.

That is already a working set of skills.

Subnetting has not been fully explored yet, but the pattern is starting to appear.

### CIDR Is Shorthand For Network Size

CIDR notation looks like this:

```text
192.168.10.0/24
```

`/24` says how many bits belong to the network portion.

In familiar decimal mask form:

```text
/24 = 255.255.255.0
```

CIDR helps quickly describe network size and boundary.

Later, CIDR becomes even more important when calculating:

- block sizes;
- number of subnets;
- usable host addresses;
- summary routes.

### Block Size Pattern

In initial addressing design, we already used a pattern:

```text
Shop 1 = 192.168.0.0/24 - 192.168.3.0/24
Shop 2 = 192.168.4.0/24 - 192.168.7.0/24
Shop 3 = 192.168.8.0/24 - 192.168.11.0/24
```

That means:

```text
Four /24 networks per shop.
```

This is not random.

The pattern helps:

- reveal structure;
- leave growth room;
- simplify documentation;
- prepare for summarization;
- think in subnetting blocks.

Subnetting becomes easier when you first see the rhythm of address blocks.

### What This Lets You Do Right Now

With these skills, you can already start basic device addressing.

For example:

- assign an IP address to a PC;
- verify subnet mask;
- understand local vs remote destination;
- configure default gateway;
- assign management IP to a switch;
- build a simple addressing plan for a small site;
- notice obvious addressing mistakes.

This is a practical skill.

Not just an exam definition.

### Switches And Management IPs

A switch operates at Layer 2 and forwards frames by MAC addresses.

For basic switching, it does not need an IP address.

But in a real network, a switch often gets a management IP.

Why:

- remote login;
- SSH management;
- monitoring;
- SNMP;
- configuration;
- troubleshooting;
- firmware/software tasks.

Memory hook:

```text
Switching traffic does not require switch IP.
Managing the switch over the network does.
```

Example:

```text
Switch management IP: 192.168.10.2/24
Default gateway:      192.168.10.1
```

Now an admin can reach the switch remotely if routing and access rules allow it.

### Routers Are The Next Step

So far, we have talked about devices inside networks.

Routers connect networks.

A router uses IP addressing more actively:

- decides where traffic should go;
- has interfaces in different networks;
- acts as default gateway;
- forwards packets between subnets;
- uses routing table;
- separates broadcast domains.

If a host wants to talk outside the local network, it sends traffic to the default gateway.

That gateway is usually a router interface IP.

Example:

```text
PC IP:        192.168.10.50
Mask:         255.255.255.0
Gateway:      192.168.10.1
Router int:   192.168.10.1
```

The router becomes the doorway to other networks.

### Troubleshooting Fuel

On the job, confidence often starts with simple questions:

```text
Is the IP address correct?
Is the subnet mask correct?
Is the default gateway correct?
Is this destination local or remote?
Is this IP private or public?
Is there an overlap?
```

Bad addressing breaks everything quickly.

If a device cannot connect, IP settings are one of the first places to check.

Typical issues:

- wrong subnet mask;
- missing default gateway;
- wrong gateway;
- duplicate IP address;
- address from wrong subnet;
- private/public misunderstanding;
- overlapping subnets across VPN/sites.

### This Is A Launchpad

We are not done with subnetting.

We have only started seeing:

- masks;
- CIDR;
- blocks;
- private ranges;
- network boundaries.

Later, we will return and go deeper into the mechanics.

But for now, it is important to notice: you have crossed an important line.

You are not just hearing terms.

You are starting to use them.

### What Comes Next

Next step:

```text
Router configuration.
```

Why routers are next:

- they connect networks;
- they need IP addresses on interfaces;
- they use masks to understand connected networks;
- they become default gateways;
- they move packets between subnets.

Everything we learned about IP addressing becomes immediately useful on routers.

## Practical Checklist

Before moving into router configuration, make sure you can explain:

- what an IP address identifies;
- what a subnet mask defines;
- what `/24` means;
- what a default gateway does;
- what private IP ranges are;
- what NAT does;
- why switches may need management IPs;
- why routers stop broadcasts;
- why network segments exist;
- why clean addressing plans matter.

## Quick Self-Check

### Question 1

Does a Layer 2 switch need an IP address to forward frames?

Answer:

```text
No. It forwards frames using MAC addresses.
```

### Question 2

Why give a switch an IP address?

Answer:

```text
For management, monitoring, remote access and troubleshooting.
```

### Question 3

What is the next major device type after basic IP addressing?

Answer:

```text
Routers, because they connect different networks.
```

### Question 4

Why is CIDR notation useful?

Answer:

```text
It gives a compact way to describe network size and boundary.
```

### Question 5

Why does bad addressing cause outages quickly?

Answer:

```text
Because devices may think destinations are local/remote incorrectly or may not know where to send traffic.
```

## Commands / Terms

| Term | Meaning |
| --- | --- |
| CIDR | Classless Inter-Domain Routing, prefix notation like `/24`. |
| Block size | Addressing pattern/increment used when dividing networks. |
| Management IP | IP address used to manage a network device remotely. |
| Default gateway | Router address a host uses to reach remote networks. |
| Router | Device that forwards packets between networks. |
| Local destination | Destination inside the same subnet. |
| Remote destination | Destination outside the local subnet. |
| Troubleshooting | Structured process of finding and fixing problems. |

## What To Review Later

- Router interface configuration
- Default gateway
- Static routes
- Connected routes
- VLAN management interfaces
- Subnetting block sizes
- CIDR notation
- IP troubleshooting commands

