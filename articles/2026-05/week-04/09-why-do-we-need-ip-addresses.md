# Why Do We Need IP Addresses?

Source: закрытая страница курса  
Date added: 2026-05-24  
Related plan item: Week 4 / Why IP addressing exists  
Tags: ip addressing, mac address, default gateway, router, arp, broadcast, subnet mask, routing
Language: Russian
Translation pair: articles-en/2026-05/week-04/09-why-do-we-need-ip-addresses.md

## Summary

MAC addresses хороши для local delivery внутри одного network segment, но они не масштабируются на мир из множества сетей. Если бы устройства искали друг друга только через broadcasts по MAC, сеть быстро утонула бы в шуме. IP addresses дают hierarchy, structure and network boundaries, а routers соединяют эти networks и не пропускают broadcasts дальше.

Главная мысль: MAC addresses доставляют frame до next local hop, а IP addresses описывают final destination across networks.

## Key Points

- MAC addresses are local Layer 2 addresses.
- MAC addresses alone do not scale across many networks.
- Broadcasts are acceptable in a local network but dangerous at large scale.
- IP addresses create structure and separate networks.
- Routers connect networks.
- Routers stop broadcasts from crossing network boundaries.
- ARP broadcasts stay inside the local network.
- A host does not ARP directly for a remote destination.
- For remote destinations, the host sends the frame to the default gateway MAC.
- The packet still contains the final destination IP address.
- The default gateway is the router's local IP address.
- IP addresses help devices decide what is local and what is remote.
- Subnet mask tells which part of the IP address is network and which part is host.
- Routing tables help routers move packets between networks.

## Notes

### Why MAC Addresses Are Not Enough

Every network interface has a MAC address.

So it is natural to ask:

```text
Why do we need IP addresses too?
```

The short answer:

```text
MAC addresses are local.
IP addresses scale across networks.
```

MAC addresses work well inside one LAN.

But a large network, company, city or internet cannot operate as one giant MAC-based broadcast space.

### The Broadcast Problem

If devices used only MAC addresses to find each other, they would need to ask everyone:

```text
Where is this MAC address?
```

That is a broadcast-style problem.

Inside a small LAN, broadcast is manageable.

Across many buildings, cities and networks, it would be disaster:

- too much noise;
- too much unnecessary traffic;
- poor scalability;
- every device hearing too many requests;
- network performance collapse.

IP addressing helps avoid that by creating network boundaries.

### IP Addresses Add Structure

IP addresses do not replace MAC addresses.

They add structure to where MAC addresses matter.

Useful memory:

```text
MAC = local delivery
IP = logical structure across networks
```

IP addressing lets us divide the world into separate networks.

Each network can handle its own local broadcasts without forcing every other network to listen.

### Router's Two Big Jobs

Routers have two important roles:

1. Connect networks.
2. Stop broadcasts.

This is huge.

Routers forward traffic between networks based on IP addresses.

But they do not forward normal Layer 2 broadcasts like ARP requests into every other network.

### ARP Stays Local

ARP asks:

```text
Who has this IP address?
```

ARP request is a broadcast.

Inside NetworkChuck Coffee LAN:

```text
Laptop broadcasts ARP request.
Local devices hear it.
Router hears it.
Router does not forward it to other networks.
```

This keeps local discovery local.

### Local Destination

If a laptop wants to reach a server in the same network:

```text
Destination IP: local server
Destination MAC: local server MAC
```

The host can ARP for the server's MAC because the server is local.

The switch forwards the frame inside the LAN.

No router is needed for same-subnet communication.

### Remote Destination

If a laptop wants to reach a server in another network, it cannot ARP directly for that remote server's MAC.

ARP does not cross routers.

Instead, the laptop sends traffic to:

```text
Default gateway
```

The default gateway is the router's local IP address on the laptop's network.

### Default Gateway

Default gateway is the door out of the local network.

When the destination is remote, the host uses:

```text
Destination IP: final remote server
Destination MAC: local router/default gateway MAC
```

The local switch only needs to deliver the frame to the router.

The router then looks at the IP destination and forwards the packet toward the next network.

### Two Address Layers Working Together

For remote traffic:

```text
IP destination = where the packet ultimately needs to go
MAC destination = where this local frame should go next
```

This is why both address types are needed.

One describes the final logical destination.

The other handles the next local hop.

### Router Rewrites Layer 2

When a router forwards a packet:

- it removes the old Layer 2 frame;
- keeps the Layer 3 destination IP;
- chooses next hop;
- builds a new Layer 2 frame for the next segment.

Simple memory:

```text
IP is end-to-end.
MAC is hop-to-hop.
```

### Subnet Mask Preview

Subnet mask tells a device which part of the IP address identifies:

- the network;
- the host.

Slash notation example:

```text
/24
```

`/24` is shorthand for a subnet mask such as:

```text
255.255.255.0
```

You do not need full subnet mastery yet, but the purpose matters:

```text
Subnet mask helps decide local vs remote.
```

### IP Addresses Create the Map

IP addressing defines network neighborhoods.

Devices use IP address + subnet mask to decide:

```text
Is the destination local?
Or do I need my default gateway?
```

Routers use routing tables to decide:

```text
Where should I send this packet next?
```

The internet is essentially many IP networks connected by routers.

### NetworkChuck Coffee Example

In NetworkChuck Coffee:

- POS terminal talks to local printer;
- back-office laptop talks to local server;
- guest device accesses internet;
- shop router connects to another location;
- payment traffic leaves the local network.

Local traffic can stay inside the LAN.

Remote traffic goes to the default gateway.

IP addressing makes those decisions possible.

### Troubleshooting Basics

When a device cannot reach the internet, check basics first:

- IP address;
- subnet mask;
- default gateway.

If one of those is wrong, higher-level troubleshooting may waste time.

Example problems:

- wrong IP network;
- wrong mask;
- missing gateway;
- gateway unreachable;
- duplicate IP address.

### Main Takeaway

Remember three ideas:

```text
MAC addresses handle local delivery.
IP addresses identify final destinations across networks.
Routers connect networks and stop broadcasts.
```

When this clicks, networking becomes more like a system and less like random parts.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| MAC address | Layer 2 local address used for hop-to-hop delivery. |
| IP address | Layer 3 logical address used for network structure and end-to-end destination. |
| Broadcast | Frame sent to all devices in the local broadcast domain. |
| ARP | Address Resolution Protocol; resolves local IP addresses to MAC addresses. |
| Router | Device that connects networks and forwards packets based on IP. |
| Default gateway | Local router IP used to reach remote networks. |
| Subnet mask | Value that identifies network and host portions of an IP address. |
| `/24` | CIDR prefix notation commonly equivalent to 255.255.255.0. |
| Routing table | Router's map for where to send packets next. |
| Local network | Same IP network/subnet as the source device. |
| Remote network | Different IP network/subnet reached through a router. |
| Hop-to-hop | Local delivery from one device to the next. |
| End-to-end | Communication from original source to final destination. |

## Questions

### 1. Why are MAC addresses alone not enough?

Because MAC addresses are local and do not scale well across many networks.

### 2. What problem would happen if broadcasts traveled everywhere?

The network would be overwhelmed with unnecessary traffic and become unscalable.

### 3. What do IP addresses add?

Hierarchy, logical structure and network boundaries.

### 4. What are two major router jobs?

Connect networks and stop broadcasts.

### 5. Does ARP cross routers?

No. ARP broadcasts stay local.

### 6. What is the default gateway?

The local router IP address a device uses to reach remote networks.

### 7. If a destination is remote, whose MAC address does the host use?

The MAC address of the default gateway/router interface.

### 8. What does the destination IP identify in remote communication?

The final remote destination.

### 9. What changes hop by hop?

MAC addresses and Layer 2 frames.

### 10. What stays focused on the final destination?

The destination IP address.

### 11. What does a subnet mask help a device decide?

Whether a destination is local or remote.

### 12. What should you check first when a device cannot reach the internet?

IP address, subnet mask and default gateway.

## What To Review Later

- MAC address local scope.
- Broadcast boundaries.
- Router stops broadcasts.
- ARP stays local.
- Default gateway.
- Local vs remote destination.
- IP as final destination.
- MAC as next-hop delivery.
- Subnet mask purpose.
- Routing table basics.
