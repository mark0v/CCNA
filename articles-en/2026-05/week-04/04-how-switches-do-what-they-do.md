# How Switches Do What They Do

Source: closed course page  
Date added: 2026-05-24  
Related plan item: Week 4 / Switch learning and forwarding  
Tags: switching, cam table, mac address, arp, broadcast, unicast, frame forwarding, default gateway
Language: English
Translation pair: articles/2026-05/week-04/04-how-switches-do-what-they-do.md

## Summary

A switch becomes "smart" by learning source MAC addresses from incoming frames and saving the MAC address to port relationship in its CAM/MAC address table. When the destination MAC is known, the switch forwards the frame only to the correct port. When the destination MAC is unknown or the frame is a broadcast, the switch floods it out all ports except the incoming port.

Main idea: switching begins with three ideas: source MAC learning, CAM table forwarding and ARP, which connects an IP address to a MAC address inside the local network.

## Key Points

- Switches learn from the source MAC address of incoming frames.
- The CAM table maps MAC addresses to switch ports.
- CAM means Content Addressable Memory.
- If the destination MAC is known, the switch forwards the frame only to the correct port.
- If the destination MAC is unknown, the switch may flood the frame.
- Broadcast frames are sent out all ports except the port they came in on.
- ARP resolves an IP address to a MAC address on the local network.
- ARP request is a broadcast.
- ARP reply is usually unicast.
- The first ping often requires ARP before ICMP traffic can be sent.
- Switches operate with Layer 2 frames and MAC addresses.
- IP identifies the final logical destination.
- MAC identifies the next local hop.
- For destinations outside the LAN, the host uses the MAC address of the default gateway.
- Routers rewrite Layer 2 headers at each hop while the IP destination remains focused on the final target.

## Notes

### The Core of Switching

A switch becomes useful because it learns.

Basic process:

```text
Frame arrives on a port.
Switch reads the source MAC address.
Switch records source MAC -> incoming port.
Switch uses CAM table to make future forwarding decisions.
```

Without learning, the switch would behave more like an old hub and send too much traffic everywhere.

### NetworkChuck Coffee Example

At NetworkChuck Coffee, many devices are connected to switches:

- registers;
- laptops;
- printers;
- access points;
- cameras;
- back-office systems.

The switch needs to forward traffic intelligently.

It should not blast every frame everywhere forever.

Learning MAC addresses allows the switch to send frames only where they need to go.

### CAM Table

CAM means:

```text
Content Addressable Memory
```

In switching, the CAM table stores learned MAC address entries.

Concept:

```text
MAC address -> switch port
```

Example:

```text
AAAA.AAAA.AAAA -> Fa0/1
BBBB.BBBB.BBBB -> Fa0/2
```

Modern Cisco output often calls this the MAC address table.

### First Conversation Starts with an Empty Table

Imagine a network just powered on.

The switch has no learned MAC addresses yet.

Two hosts:

```text
Host A
IP: 192.168.1.50/24
MAC: 1111.1111.1111

Host B
IP: 192.168.1.51/24
MAC: 2222.2222.2222
```

At first, the switch does not know where either MAC lives.

### /24 Review

`/24` means subnet mask:

```text
255.255.255.0
```

For this example:

```text
Network part: 192.168.1
Host part: last octet
```

So `192.168.1.50` and `192.168.1.51` are in the same local network.

### ARP

ARP means:

```text
Address Resolution Protocol
```

ARP answers this question:

```text
I know the IP address. What MAC address should I use locally?
```

Before Host A can send traffic directly to Host B on the same LAN, Host A needs Host B's MAC address.

### ARP Request

If Host A does not know Host B's MAC address, it sends an ARP request.

Question:

```text
Who has 192.168.1.51? Tell 192.168.1.50.
```

ARP request is a broadcast.

Broadcast destination MAC:

```text
FFFF.FFFF.FFFF
```

This means every device on the local broadcast domain should receive it.

### What the Switch Learns from ARP Request

When the ARP request enters the switch, the switch reads the source MAC.

Example:

```text
Source MAC: 1111.1111.1111
Incoming port: Fa0/1
```

The switch learns:

```text
1111.1111.1111 -> Fa0/1
```

Then it sees the destination MAC:

```text
FFFF.FFFF.FFFF
```

Because this is broadcast, the switch floods it.

### Flooding

Flooding means sending a frame out multiple ports.

Important rule:

```text
Flood out all ports except the port the frame came in on.
```

The switch does not send the broadcast back to the incoming port because that would be useless and can contribute to problems.

### Devices Receive the Broadcast

Every local device receives the ARP request.

Devices that are not `192.168.1.51` ignore it.

Host B sees:

```text
That IP is mine.
```

Then Host B sends an ARP reply.

### ARP Reply

ARP reply is usually unicast.

Example:

```text
Source MAC: 2222.2222.2222
Destination MAC: 1111.1111.1111
```

When the reply enters the switch, the switch learns:

```text
2222.2222.2222 -> Fa0/2
```

Now the switch knows both hosts:

```text
1111.1111.1111 -> Fa0/1
2222.2222.2222 -> Fa0/2
```

Future frames between them can be forwarded directly.

### Ping Happens After ARP

When you type:

```text
ping 192.168.1.51
```

the device may need ARP first.

It cannot build the proper Layer 2 frame until it knows the destination MAC.

Order:

```text
ARP request
ARP reply
Build frame for ping
Send ICMP traffic
```

This is why the first ping can sometimes take longer than later pings.

### Broadcast vs Unicast

Broadcast:

```text
One sender -> everyone in the local broadcast domain
Destination MAC: FFFF.FFFF.FFFF
```

Unicast:

```text
One sender -> one specific destination
Destination MAC: specific device MAC
```

Switches flood broadcasts.

Switches forward known unicasts only to the learned destination port.

### Why IP and MAC Both Exist

At first, IP plus MAC can feel like duplicate addressing.

They solve different problems.

| Address | Purpose |
| --- | --- |
| IP address | Logical end-to-end destination |
| MAC address | Local next-hop delivery |

Inside the LAN, switches use MAC addresses.

Across networks, routers use IP addresses to move packets toward the final destination.

### Local Destination

If Host A sends to Host B in the same LAN:

```text
Destination IP: Host B IP
Destination MAC: Host B MAC
```

The switch forwards based on Host B's MAC address.

### Destination Outside the LAN

If Host A sends to Google or another internet destination, Google is not local.

Host A does not ARP for Google's MAC address.

Instead, Host A ARPs for:

```text
Default gateway MAC address
```

The packet:

```text
Destination IP: Google IP
Destination MAC: local router/default gateway MAC
```

The IP says where the packet ultimately needs to go.

The MAC says where this local frame should go next.

### Routers Rewrite Layer 2

When a router forwards a packet to the next network, it removes the old Layer 2 frame and creates a new one.

The IP destination remains focused on the final destination.

The MAC addresses change hop by hop.

Simple memory:

```text
IP stays end-to-end.
MAC changes hop-to-hop.
```

### Troubleshooting Value

When something cannot connect, do not immediately blame the app.

Ask:

- can the host ARP for the target;
- can it ARP for the default gateway;
- is the switch learning MAC addresses;
- are MAC addresses on expected ports;
- is cabling correct;
- is traffic landing on the wrong port.

Many "mystery" outages are basic Layer 2 or ARP problems.

### Main Takeaway

A switch does what it does by:

1. Watching incoming frames.
2. Learning source MAC addresses.
3. Building a CAM/MAC address table.
4. Flooding broadcasts and unknowns when needed.
5. Forwarding known unicast frames efficiently.

ARP connects the IP world to the MAC world on the local network.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| CAM table | Table mapping learned MAC addresses to switch ports. |
| MAC address table | Cisco output/table showing learned MAC addresses and interfaces. |
| Source MAC | MAC address of the sender in a frame. |
| Destination MAC | MAC address of the intended local receiver or broadcast. |
| ARP | Address Resolution Protocol; maps local IP addresses to MAC addresses. |
| ARP request | Broadcast asking who owns a specific IP address. |
| ARP reply | Usually unicast response containing the requested MAC address. |
| Broadcast | Frame sent to all devices in the local broadcast domain. |
| Unicast | Frame sent to one specific destination. |
| Flooding | Sending a frame out multiple ports except the incoming port. |
| Default gateway | Local router used to reach destinations outside the LAN. |
| ICMP | Protocol used by ping. |
| `/24` | Prefix length equivalent to subnet mask 255.255.255.0. |
| Hop-to-hop | Local delivery from one network device to the next. |
| End-to-end | Communication from original source to final destination. |

## Questions

### 1. How does a switch learn where devices are?

It reads the source MAC address of incoming frames and records the incoming port.

### 2. What does the CAM table store?

MAC addresses and the switch ports where they were learned.

### 3. What happens when a switch receives a broadcast frame?

It floods the frame out all ports except the port it came in on.

### 4. What is the broadcast MAC address?

`FFFF.FFFF.FFFF`.

### 5. What does ARP do?

It resolves an IP address to a MAC address on the local network.

### 6. Is an ARP request broadcast or unicast?

Broadcast.

### 7. Is an ARP reply usually broadcast or unicast?

Unicast.

### 8. Why may ARP happen before ping?

The sender needs the destination MAC address before it can build the Layer 2 frame for the ping.

### 9. What does IP addressing provide?

Logical end-to-end destination information.

### 10. What does MAC addressing provide?

Local next-hop Layer 2 delivery.

### 11. If the destination is outside the LAN, which MAC address does the host use?

The MAC address of the default gateway/router interface.

### 12. What changes hop by hop: IP or MAC?

MAC addresses change hop by hop; IP stays focused on the end-to-end destination.

## What To Review Later

- Source MAC learning.
- CAM/MAC address table.
- Broadcast MAC address.
- ARP request and ARP reply.
- Broadcast vs unicast.
- Flooding behavior.
- First ping and ARP.
- IP vs MAC addressing.
- Default gateway MAC for off-LAN traffic.
- Hop-to-hop vs end-to-end.
