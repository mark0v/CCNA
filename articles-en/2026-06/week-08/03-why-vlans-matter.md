# Why VLANs Matter

Source: closed course page  
Date added: 2026-06-20  
Related plan item: Week 8 / VLAN foundations  
Tags: VLAN, switching, broadcast domain, segmentation, security, IP addressing
Language: English
Translation pair: articles/2026-06/week-08/03-why-vlans-matter.md

## Summary

A VLAN, or Virtual LAN, lets you divide one physical switching infrastructure into multiple logical networks.

In plain English: devices can be connected to the same switches but logically belong to different networks.

This is not just for tidy organization. VLANs give you:

- smaller broadcast domains;
- less unnecessary traffic noise;
- logical separation between device groups;
- security boundaries;
- a clearer IP addressing plan;
- the ability to apply routing and ACL policies between segments;
- network design that can scale.

Without VLANs, a network quickly becomes one large room where every device sits together and hears too much noise.

## Flat Network: One Big Room

Imagine a company with 100 people where every meeting must include every employee.

Sales discussion? Everyone joins.

Accounting question? Everyone joins.

A short update on a tiny project? All 100 people are back in the room.

That is absurd for people, but it is how a flat network feels.

A flat network is a network where different devices live in one large shared segment without logical separation.

At first, it feels simple:

```text
Everything is connected.
Everything gets an IP address.
Everything seems to work.
```

Then growth happens:

- more users;
- more devices;
- guest Wi-Fi;
- cameras;
- printers;
- POS terminals;
- office PCs;
- management devices;
- security requirements.

Suddenly the simple network becomes a source of noise, risk and painful troubleshooting.

## Does A Switch Not Already Separate Traffic?

A switch is definitely smarter than a hub.

A hub repeats the signal to every port. A switch builds a MAC address table and sends frames only where they need to go.

But that does not mean a switch automatically creates different broadcast domains.

If all ports are in the same VLAN, all devices remain in one Layer 2 broadcast domain.

Broadcast traffic still spreads inside that shared space.

Examples of broadcast or local discovery traffic include:

- ARP requests;
- DHCP discovery;
- some service discovery protocols;
- other Layer 2 announcements.

A switch reduces unnecessary unicast traffic compared with a hub, but VLANs are needed for real logical segmentation.

## What A VLAN Does

A VLAN divides a switch into logical groups.

One physical switch can look like this:

```text
Ports 1-8     -> VLAN 10 Users
Ports 9-12    -> VLAN 20 POS
Ports 13-16   -> VLAN 30 Cameras
Ports 17-20   -> VLAN 40 Guest Wi-Fi
Ports 21-24   -> VLAN 99 Management
```

Physically, it is one switch.

Logically, it is several separate networks.

Devices in different VLANs do not communicate directly at Layer 2. For traffic to pass between VLANs, a Layer 3 device is required:

- router;
- Layer 3 switch;
- firewall.

That is a good thing, because rules can be applied between VLANs.

## NetworkChuck Coffee Needs Boundaries

NetworkChuck Coffee may have many different device types on the network:

- barista tablets;
- point-of-sale terminals;
- office PCs;
- cameras;
- inventory systems;
- guest Wi-Fi clients;
- phones;
- network management devices.

If all of that is thrown into one segment, it becomes a risky mix.

Guest Wi-Fi users should not sit next to POS systems.

Cameras should not live with office laptops.

Management interfaces for switches and routers should not be available to ordinary users.

VLANs allow these boundaries without building a separate physical network for every group.

That is an important real-world idea: separation is achieved with good logical design, not by running a new cabling universe for every need.

## What VLANs Give You In Practice

### Smaller Communication Groups

Instead of one large everyone-talks-to-everyone space, the network is divided into manageable chunks.

That reduces broadcast scope and makes network behavior easier to understand.

### Security Boundaries

A VLAN by itself is not a complete security policy, but it creates boundaries where routing rules, ACLs or firewall policies can be applied.

For example:

```text
Guest VLAN has no access to POS VLAN.
Camera VLAN can send traffic only to the recording server.
Management VLAN is available only to administrators.
```

### IP Addressing Boundaries

Usually, every VLAN gets its own subnet.

For example:

```text
VLAN 10 Users:       10.0.10.0/24
VLAN 20 POS:         10.0.20.0/24
VLAN 30 Cameras:     10.0.30.0/24
VLAN 40 Guest Wi-Fi: 10.0.40.0/24
VLAN 99 Management:  10.0.99.0/24
```

That helps you:

- plan addresses;
- understand where a device belongs;
- troubleshoot faster;
- write clearer ACLs;
- document the network neatly.

### Better Control

When groups are separated, you can decide how they interact.

You can allow:

```text
Users -> Internet
Users -> Printer
POS -> Payment processor
Admin PC -> Management VLAN
```

And deny:

```text
Guest Wi-Fi -> Internal LAN
Cameras -> Office PCs
Users -> Switch management interfaces
```

The network starts behaving like a design instead of a random collection of connections.

## VLANs Are Not Only About Broadcast Noise

VLANs are often explained as a way to reduce broadcast traffic. That is true, but it is only part of the story.

The bigger idea is intent.

VLANs express how the business wants to separate its infrastructure:

- who is a guest;
- who is an employee;
- which systems are sensitive;
- which devices are infrastructure;
- where trust should stop.

That is why VLANs appear even in small environments. A small business still has different trust levels.

Guest Wi-Fi, printers, cameras, employee devices and payment systems should not live as one friendly flat network.

## How VLANs Connect To Routing

If devices are in the same VLAN and same subnet, they communicate directly through the switch.

If devices are in different VLANs, they need inter-VLAN routing.

That can be provided by:

- router-on-a-stick;
- Layer 3 switch;
- firewall interface or subinterface.

This is where previous topics begin to connect:

- subnetting provides address space for every VLAN;
- routing lets VLANs communicate with each other;
- ACLs control which traffic is allowed;
- NAT may be used for external access;
- DHCP can hand out addresses separately for each VLAN.

VLANs do not replace all these technologies. They create the structure those technologies rely on.

## Main Takeaway

VLANs let you break one large network into smaller, smarter and safer groups.

This matters not because VLANs look like an advanced topic. It matters because without segmentation, real networks become:

- noisy;
- hard to troubleshoot;
- insecure;
- difficult to scale;
- inconvenient to manage.

A VLAN is one of the first tools that moves switching from "we connected devices" to "we are building infrastructure."

Next, VLANs can be defined more precisely, ports can be assigned to VLANs, traffic from multiple VLANs can be carried between switches, and all of it can be tied back to IP addressing.

