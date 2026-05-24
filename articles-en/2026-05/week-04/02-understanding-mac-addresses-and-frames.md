# Understanding MAC Addresses and Frames

Source: closed course page  
Date added: 2026-05-24  
Related plan item: Week 4 / MAC addresses and Ethernet frames  
Tags: switching, mac address, frame, ethernet, layer 2, data link, oui, fcs, crc
Language: English
Translation pair: articles/2026-05/week-04/02-understanding-mac-addresses-and-frames.md

## Summary

To understand switching, you need to start with the language a switch speaks: MAC addresses and frames. A switch operates at Layer 2, the Data Link layer, and makes decisions primarily from MAC addresses, not IP addresses. A MAC address is the local hardware identity of a network interface, and a frame is the Layer 2 wrapper that carries the source MAC, destination MAC and checking information such as FCS.

Main idea: if you understand MAC addresses and Ethernet frames, later topics like the MAC address table, forwarding and device tracing become much easier.

## Key Points

- Switches operate primarily at Layer 2, the Data Link layer.
- Layer 2 uses MAC addresses.
- A MAC address identifies a network interface on the local network.
- MAC stands for Media Access Control.
- MAC addresses are often called physical addresses.
- A MAC address has 12 hexadecimal characters.
- Hexadecimal uses 0-9 and A-F.
- The first half of a MAC address is the OUI.
- OUI stands for Organizationally Unique Identifier.
- The OUI identifies the hardware vendor.
- The second half helps make the address unique for that device/interface.
- Switches forward frames based on source and destination MAC addresses.
- A frame is the Layer 2 wrapper around data.
- Frames include source MAC, destination MAC and FCS.
- FCS/CRC helps detect whether a frame was corrupted in transit.
- IP is end-to-end addressing; MAC is local/hop-to-hop delivery.

## Notes

### Why Start with MAC Addresses?

Before routers, VLANs, firewalls and internet access, a local network must move data between local devices.

At NetworkChuck Coffee, many problems start inside the LAN:

- printer cannot connect;
- desktop cannot reach server;
- access point acts strangely;
- POS terminal drops offline;
- unknown device appears on the network.

The first useful place to look is often the switch.

To understand what the switch sees, you need to understand:

- MAC addresses;
- Ethernet frames;
- Layer 2 behavior.

### MAC Address

MAC means:

```text
Media Access Control
```

A MAC address is the hardware-style address associated with a network interface.

Examples of interfaces:

- laptop Ethernet port;
- Wi-Fi adapter;
- printer NIC;
- IP camera network port;
- access point Ethernet port;
- POS terminal network interface.

People also call it:

```text
Physical address
```

For learning, think of it as the device interface identity on the local network.

### Burned-In Address and Spoofing

Traditionally, MAC address is described as burned into the network card.

That is a good learning model.

In real life, MAC addresses can sometimes be changed or spoofed in software.

But the core idea remains:

```text
MAC address = local Layer 2 identity of a network interface
```

### How to View a MAC Address

On Windows:

```text
ipconfig /all
```

On macOS or Linux:

```text
ifconfig
```

or newer Linux tools:

```text
ip link
```

The MAC address may appear as:

- Physical Address;
- ether;
- hardware address;
- MAC address.

### MAC Address Format

A MAC address has:

```text
12 hexadecimal characters
```

Hexadecimal uses:

```text
0 1 2 3 4 5 6 7 8 9 A B C D E F
```

The same MAC can be written in different formats:

```text
AA-BB-CC-11-22-33
AA:BB:CC:11:22:33
AABB.CC11.2233
```

The separators differ, but the value is the same.

### OUI

The first six hexadecimal characters identify the vendor.

This part is called:

```text
OUI - Organizationally Unique Identifier
```

OUI can often tell you who made the network hardware.

Examples:

- Intel;
- Apple;
- Cisco;
- Ubiquiti;
- Roku;
- HP.

This is useful during device hunting.

### Device-Specific Half

The second half of the MAC address helps identify the specific interface/device from that vendor.

Simplified structure:

```text
First 6 hex characters  = vendor OUI
Last 6 hex characters   = device/interface-specific value
```

This makes MAC addresses useful for identifying and tracing devices.

### MAC Address as a Troubleshooting Clue

If you find an unknown MAC address on a switch, you can look up the OUI.

That may not tell you the exact model, but it can narrow the search.

Example:

```text
OUI says Roku
```

Now you can ask why a streaming device is on a business LAN.

Example:

```text
OUI says Ubiquiti
```

Maybe it is an access point or camera.

This turns MAC address from exam trivia into operational evidence.

### OSI Layer 2

Switches primarily operate at:

```text
Layer 2 - Data Link layer
```

Layer 2 uses MAC addresses and frames.

Layer 1 below it is Physical layer:

- copper electrical signals;
- fiber light pulses;
- Wi-Fi radio waves;
- bits moving across a medium.

Layer 2 organizes those bits into frames that a switch can understand.

### Switches Do Not Start with Apps

A switch does not care about:

- browser tabs;
- banking apps;
- video streams;
- user files;
- website content.

At Layer 2, the switch cares about the frame.

Most importantly:

- source MAC address;
- destination MAC address;
- port where the frame arrived.

### Frame

A frame is the Layer 2 unit of data.

It wraps data with Layer 2 information.

Simplified Ethernet frame idea:

```text
Destination MAC
Source MAC
Type/Length
Payload
FCS
```

The exact Ethernet frame has more details, but for this stage, focus on:

- destination MAC;
- source MAC;
- FCS.

### Encapsulation

Encapsulation means each layer adds its own information as data moves down the stack.

Simplified path:

```text
Application data
Transport segment
IP packet
Ethernet frame
Bits on the wire
```

At Layer 2, the packet is placed inside a frame.

That frame is what the switch reads and forwards.

### Source MAC and Destination MAC

Source MAC:

```text
The sender's local hardware address
```

Destination MAC:

```text
The local next-hop Layer 2 address
```

If the destination is inside the same LAN, destination MAC is usually the final local device.

If the traffic is going outside the LAN, destination MAC is usually the default gateway/router interface.

### IP vs MAC

IP and MAC solve different addressing problems.

| Address | Scope | Layer | Purpose |
| --- | --- | --- | --- |
| IP address | End-to-end | Layer 3 | Logical address from source to final destination |
| MAC address | Local/hop-to-hop | Layer 2 | Local delivery to next device on the LAN |

Simple memory:

```text
IP tells the overall destination.
MAC gets the frame to the next local hop.
```

### FCS and CRC

FCS means:

```text
Frame Check Sequence
```

CRC means:

```text
Cyclic Redundancy Check
```

For this lesson, they are connected ideas: a mathematical check used to detect corruption in the frame.

The receiving device can use FCS to decide whether the frame appears intact.

If the frame is corrupted, it can be discarded.

### NetworkChuck Coffee Example

When a POS terminal sends traffic, it does not simply throw random bits onto the cable.

It builds a frame.

That frame includes:

- source MAC of the POS terminal;
- destination MAC of the next local device;
- payload;
- FCS.

The switch reads the frame and decides where to send it next.

This is the beginning of switching.

### Main Takeaway

Switching starts with MAC addresses and frames.

Before learning how a switch builds a MAC address table or forwards intelligently, understand what the switch is looking at:

```text
Source MAC
Destination MAC
Incoming port
Frame integrity
```

Once that clicks, switching becomes much less mysterious.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| MAC address | Layer 2 address associated with a network interface. |
| Media Access Control | Full meaning of MAC. |
| Physical address | Common name for MAC address. |
| Hexadecimal | Number system using 0-9 and A-F. |
| OUI | Organizationally Unique Identifier; vendor portion of a MAC address. |
| NIC | Network Interface Card or network adapter. |
| Layer 2 | Data Link layer of the OSI model. |
| Frame | Layer 2 unit of data used by Ethernet switching. |
| Source MAC | MAC address of the sending interface. |
| Destination MAC | MAC address of the local next-hop receiving interface. |
| FCS | Frame Check Sequence used to detect frame corruption. |
| CRC | Cyclic Redundancy Check; mathematical error-checking method. |
| Encapsulation | Process where each layer wraps data with its own information. |
| Default gateway | Router used to reach destinations outside the local network. |
| `ipconfig /all` | Windows command that shows interface details including MAC address. |
| `ifconfig` | macOS/Linux command that can show interface details including MAC address. |

## Questions

### 1. Why start switching with MAC addresses?

Because switches make Layer 2 forwarding decisions using MAC addresses.

### 2. What does MAC stand for?

Media Access Control.

### 3. What is a MAC address?

A Layer 2 hardware-style address associated with a network interface.

### 4. How many hexadecimal characters are in a MAC address?

12.

### 5. What does hexadecimal use?

The characters 0-9 and A-F.

### 6. What is an OUI?

Organizationally Unique Identifier; the vendor-identifying first half of a MAC address.

### 7. Which OSI layer do switches primarily use for forwarding?

Layer 2, the Data Link layer.

### 8. What is a frame?

The Layer 2 wrapper/unit of data that includes MAC addressing and control information.

### 9. What does source MAC identify?

The sending local network interface.

### 10. What does destination MAC identify?

The local next-hop interface that should receive the frame.

### 11. How is IP different from MAC?

IP is end-to-end logical addressing; MAC is local Layer 2 delivery.

### 12. What does FCS help detect?

Whether a frame was corrupted during transmission.

## What To Review Later

- MAC address format.
- OUI lookup.
- Layer 2 and Data Link layer.
- Ethernet frame basics.
- Source MAC vs destination MAC.
- IP vs MAC addressing.
- FCS and CRC.
- Encapsulation.
- How switches use MAC addresses.
