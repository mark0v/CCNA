# VLANs, Broadcast Domains, And Trunks

Source: closed course page  
Date added: 2026-06-20  
Related plan item: Week 8 / VLAN broadcast domains and trunking  
Tags: VLAN, broadcast domain, trunk port, 802.1Q, router-on-a-stick, segmentation
Language: English
Translation pair: articles/2026-06/week-08/04-vlans-broadcast-domains-and-trunks.md

## Summary

VLANs do not exist as a fancy feature. They solve real network growth problems.

When a company adds more devices, such as IP phones, cameras, guest Wi-Fi and business systems, one flat network quickly becomes hard to manage. Addresses run out, broadcast noise grows, sensitive systems become harder to protect, and it gets harder to understand where everything belongs.

A VLAN, or Virtual LAN, lets you take one physical switch and divide it into several logical networks.

The key idea:

```text
One VLAN = one broadcast domain
One broadcast domain = usually one IP subnet
More VLANs = more separation and flexibility
```

VLANs provide two main benefits:

- scalability;
- security through segmentation.

## Why VLANs Show Up

Imagine adding a large Voice over IP rollout to an existing network.

Before that, the network had laptops, PCs, printers and normal user devices. Now almost every user also gets an IP phone.

The number of endpoints grows quickly.

That creates questions:

- will there be enough IP addresses;
- will the broadcast domain become too large;
- should phones be separated from normal data devices;
- how can separate policies be applied to voice traffic;
- how can troubleshooting stay clear.

If everything remains in one flat network, the network may work, but it becomes less manageable over time.

VLANs solve this through logical separation.

## Broadcast Domain

A broadcast domain is the area of a network where broadcast traffic can travel.

If a device sends a broadcast, such as an ARP request, the switch floods that frame inside the broadcast domain.

On a normal switch without VLAN segmentation, all ports are usually in one default VLAN.

That means:

```text
One switch
One default VLAN
One broadcast domain
```

If one device sends a broadcast, that broadcast can be sent out all relevant ports inside that VLAN.

## VLAN As A Virtual Broadcast Domain

A VLAN lets you split a switch into multiple broadcast domains.

For example:

```text
Ports 1-4  -> VLAN 10 Green
Ports 5-8  -> VLAN 20 Red
```

Devices in VLAN 10 are in one broadcast domain.

Devices in VLAN 20 are in another broadcast domain.

A broadcast from VLAN 10 does not enter VLAN 20. A broadcast from VLAN 20 does not enter VLAN 10.

Logically, this is like two separate switches inside one physical switch:

```text
Green talks to Green
Red talks to Red
Green does not directly talk to Red
```

If Green and Red need to communicate, routing is required.

## VLANs Scale Across Switches

A VLAN does not have to live on only one switch.

In a real network, devices in the same VLAN may connect to different switches.

For example:

```text
Switch 1, port 1 -> VLAN 10
Switch 2, port 7 -> VLAN 10
```

Physically, the devices connect to different switches, but logically they can be in the same VLAN and the same broadcast domain.

To do that, switches must carry VLAN traffic between each other.

That is where trunk ports appear.

## Trunk Port

A trunk port is a port that carries traffic for multiple VLANs.

A normal access port usually belongs to one VLAN:

```text
Access port -> VLAN 10 only
```

A trunk port can carry several VLANs:

```text
Trunk port -> VLAN 10, VLAN 20, VLAN 30, VLAN 99
```

This is needed when switches connect to each other or when a switch connects to a router, firewall or Layer 3 device that must see several VLANs.

## 802.1Q Tagging

When a frame crosses a trunk, the switch must know which VLAN the frame belongs to.

That is done with a VLAN tag.

The standard is called `802.1Q`.

The simple idea is:

```text
Frame crosses trunk -> switch adds VLAN information
Next switch reads tag -> sends frame into the correct VLAN
```

`802.1Q` matters because it is an industry standard. It is not only a Cisco-specific mechanism. Different vendors can support trunking through this standard.

Without tagging, the receiving switch would not know where to place traffic arriving on a trunk link.

## The Two Main Reasons To Use VLANs

### Scalability

Every VLAN usually maps to its own IP subnet.

When a new device group appears, you can create a separate VLAN and subnet for it.

For example:

```text
VLAN 10 Data:   10.0.10.0/24
VLAN 20 Voice:  10.0.20.0/24
VLAN 30 Guest:  10.0.30.0/24
```

That allows you to add IP phones without pushing them into the same address space where user laptops already live.

This helps you:

- avoid exhausting one subnet too quickly;
- plan growth;
- separate device types;
- document the network more easily.

### Security

VLANs provide segmentation.

This is not a magic security button, but it is an important boundary.

If phones live in one VLAN, laptops in another and guest Wi-Fi in a third, those groups are not in the same shared Layer 2 space.

Then policy can be applied:

```text
Guest VLAN -> Internet only
Voice VLAN -> Call servers
Data VLAN -> Internal services
Management VLAN -> Admin access only
```

Segmentation reduces exposure and helps contain problems inside a specific zone.

## But How Do VLANs Communicate?

VLANs separate traffic. That is good.

But sometimes devices in different VLANs must communicate:

- users need to print to printers;
- phones need to reach a call server;
- guest networks need internet access;
- admin workstations need to manage switches.

That requires routing.

VLANs operate at Layer 2, while communication between IP subnets requires Layer 3.

Possible options include:

- router;
- Layer 3 switch;
- firewall.

## Router-On-A-Stick

One common option in smaller environments is router-on-a-stick.

The idea:

```text
Switch connects to router using one trunk link
Router creates subinterfaces
Each subinterface belongs to one VLAN
Each subinterface gets gateway IP for that VLAN
```

For example:

```text
Router subinterface for VLAN 10 -> 10.0.10.1
Router subinterface for VLAN 20 -> 10.0.20.1
Router subinterface for VLAN 30 -> 10.0.30.1
```

For clients, these addresses become default gateways.

Traffic from VLAN 10 goes to the router. The router decides whether it may be sent to VLAN 20, VLAN 30 or the internet.

This is where policy lives:

- allow;
- deny;
- inspect;
- translate through NAT;
- route onward.

## How This Connects Previous Topics

VLANs connect to almost everything already covered:

- switching - ports are placed into VLANs;
- subnetting - every VLAN gets its own IP subnet;
- routing - traffic between VLANs crosses Layer 3;
- ACLs - policies control access between VLANs;
- DHCP - every VLAN can have its own pool;
- NAT - selected VLANs can reach the internet;
- troubleshooting - you need to know where the Layer 2 boundary is and where the Layer 3 boundary is.

So VLANs may feel complex not because the core idea is difficult, but because they touch many parts of networking at once.

## Main Takeaway

A VLAN lets you carve a physical network into multiple logical networks.

One switch can become several logical broadcast domains.

Several switches can carry those VLANs through trunk links.

`802.1Q` tagging helps switches understand which VLAN traffic belongs to on a trunk.

Routing is required when traffic must move between VLANs.

In short:

```text
VLAN = logical separation
Trunk = carry multiple VLANs between devices
802.1Q = VLAN tag on trunk links
Router/L3 device = communication between VLANs
```

VLANs give the network room to grow and room to protect what matters.

