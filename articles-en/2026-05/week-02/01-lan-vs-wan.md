# LAN vs. WAN

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Network fundamentals  
Tags: lan, wan, network, switch, access point, wifi, network closet, local network

## Summary

A network is any system that lets devices communicate with each other. LAN and WAN are two basic ways to describe the scope of that communication: LAN is the local network inside a contained place like a coffee shop, office or home; WAN is the wider network used to reach outside that local space, usually the internet or another remote location.

Main idea: LAN is inside, WAN is outside. The LAN is built around local infrastructure such as switches, cabling and access points. The WAN is the path that lets the local network reach the rest of the world.

## Key Points

- A network lets devices communicate and share data.
- Local data means data stored on and accessed from one device.
- Connecting two devices together creates a network, even if it is tiny.
- In IT, network is a generic term for connected things that can communicate.
- A coffee shop network includes more than visible WiFi.
- Wireless clients usually depend on a wired network behind the scenes.
- The network closet is the hidden room where key infrastructure lives.
- A switch connects wired devices in the local network.
- A wireless access point provides WiFi, but usually connects back to a switch.
- LAN means Local Area Network.
- A LAN covers a limited local area, such as one shop, building, office suite or home.
- LAN traffic stays inside that local environment.
- WAN means Wide Area Network.
- A WAN connects across larger distances.
- In everyday conversation, WAN often means the internet connection.
- WAN can also connect one business location to another.
- Troubleshooting starts by asking whether the problem is inside the building or outside the building.

## Notes

### What Is a Network?

A network is a way for devices to communicate with each other.

That communication can happen through:

- copper cable;
- fiber;
- WiFi;
- other connection methods.

The simplest possible idea:

```text
Device A can talk to Device B.
That is a network.
```

The network may be small, ugly or not scalable, but if devices can communicate, the core idea is there.

### Local Data

Local means something is on that device and accessible from that device.

Examples:

- local files;
- local folders;
- local apps;
- local stored data.

Before devices are connected, each device is its own little island. After they are connected, they can share data and communicate.

### Network as a Generic Word

Network is not only an IT word.

Examples:

- network of roads;
- network of people;
- network of coffee shops;
- computer network.

The shared idea is:

```text
Connected things that can interact or communicate.
```

In IT, those connected things are usually devices and services.

### NetworkChuck Coffee Example

Customers see the polished side of the coffee shop:

- WiFi;
- registers;
- tablets;
- seating area;
- streaming devices.

What they do not see is the network infrastructure behind the wall.

The coffee shop may have:

- network closet;
- switches;
- patch panels;
- cabling;
- wireless access points;
- router/firewall;
- WAN connection;
- power and UPS equipment.

The visible wireless experience depends on physical infrastructure.

### Wireless Still Needs Wires

Wireless does not mean the whole network has no wires.

It usually means:

```text
The client device does not need a cable.
The access point still connects back to the wired network.
```

This is a critical mental model. WiFi is usually an extension of the wired LAN, not a replacement for the entire LAN.

### The Network Closet

The network closet is the hidden room where important network infrastructure lives.

It may connect:

- register/POS devices;
- office computers;
- cameras;
- access points;
- printers;
- local servers;
- smart TVs or media devices;
- internet/WAN equipment.

For customers, the network closet is invisible. For the business, it is the heart of connectivity.

### Why We Use a Switch

Connecting every device directly to every other device does not scale.

Bad model:

```text
Computer A -> Computer B -> Computer C -> Computer D
```

If something in the middle fails, devices downstream may lose connectivity.

Better model:

```text
Devices -> Switch
```

A switch is the central device where wired LAN devices connect.

The switch lets devices communicate without needing messy direct connections between every pair of devices.

### Wireless Access Point

A wireless access point is often shortened to:

```text
AP
```

An AP provides WiFi so wireless devices can connect, such as:

- phones;
- laptops;
- tablets;
- handheld devices.

But the AP usually plugs into the switch.

Simple model:

```text
Phone -> WiFi -> Access Point -> Switch -> LAN/WAN
```

### LAN

LAN means Local Area Network.

A LAN is a network inside a limited local area.

Examples:

- one coffee shop;
- one home;
- one office;
- one office suite;
- one building;
- one local business location.

At NetworkChuck Coffee, LAN devices might include:

- register/POS system;
- back office PC;
- smart TV;
- printer;
- WiFi clients;
- cameras;
- local server;
- access points;
- switches.

### LAN Traffic

LAN traffic stays inside the local environment.

Examples:

- POS terminal talks to a local device in the shop;
- laptop prints to a printer in the same office;
- customer streams from a local media server in the building;
- office PC accesses a local shared folder;
- phone talks to an internal server.

LAN does not mean tiny. A LAN can include many switches, access points, printers, cameras and clients.

The important part is the scope:

```text
Local and contained.
```

### WAN

WAN means Wide Area Network.

A WAN connects across large distances or beyond the local environment.

In everyday use, WAN often means:

```text
The internet connection.
```

But technically, a WAN can also connect:

- one branch to another branch;
- a coffee shop to headquarters;
- a local office to a data center;
- locations across town;
- locations across the country.

### WAN Traffic

WAN traffic leaves the local environment.

Examples:

- register reaches a cloud payment processor;
- laptop opens Netflix;
- manager checks inventory from another city;
- branch office connects to headquarters;
- local network reaches cloud apps.

Simple model:

```text
LAN -> WAN -> outside network/internet/remote site
```

### LAN vs WAN Troubleshooting

Good troubleshooting starts with scope.

Ask:

```text
Is the problem inside the building,
or does it happen only when traffic leaves the building?
```

If the problem stays local, think LAN:

- switch;
- cabling;
- WiFi;
- access point;
- local addressing;
- local device issue.

If the problem happens when leaving the local network, think WAN:

- internet circuit;
- ISP issue;
- router/firewall;
- WAN connection;
- remote service;
- routing outside the site.

### Mental Model

The core distinction:

| Type | Scope | Example |
| --- | --- | --- |
| LAN | Inside local space | Coffee shop devices talking internally |
| WAN | Outside local space | Coffee shop reaching internet or remote site |

Short version:

```text
LAN is inside.
WAN is outside.
```

### Main Takeaway

A network lets devices communicate.

Inside the local location, that communication is the LAN.

When communication leaves that local space, it uses the WAN.

Behind the scenes, the LAN usually depends on switches, cabling and access points, while the WAN provides the path to the internet or remote locations.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Network | Connected devices that can communicate. |
| Local | Stored on or accessible from the current device/location. |
| LAN | Local Area Network; a network inside a limited local area. |
| WAN | Wide Area Network; a network spanning wider distance or outside the local site. |
| Switch | Central wired device that connects LAN devices. |
| AP | Access Point; device that provides WiFi and usually connects back to the wired LAN. |
| WiFi | Wireless access method for client devices. |
| Network closet | Room or area where network infrastructure is installed. |
| LAN traffic | Traffic that stays inside the local network. |
| WAN traffic | Traffic that leaves the local network for internet or remote locations. |
| ISP | Internet Service Provider. |

## Questions

### 1. What is a network?

A network is a way for devices to communicate with each other.

### 2. What does local mean in this lesson?

Local means data or resources are stored on and accessible from that device or local environment.

### 3. What happens when two standalone computers are connected together?

They form a network because they can now communicate and share data.

### 4. Why does a coffee shop need a network closet?

Because the hidden infrastructure for WiFi, registers, cameras, office devices and WAN connectivity usually lives there.

### 5. Why is wireless not truly wire-free from a design perspective?

Because wireless clients usually connect through an access point that plugs back into the wired network.

### 6. What does a switch do?

A switch connects wired devices in the local network and helps them communicate.

### 7. What does AP stand for?

AP stands for Access Point.

### 8. What does an access point do?

It provides WiFi so wireless devices can connect to the network.

### 9. What does LAN stand for?

LAN stands for Local Area Network.

### 10. What is a LAN?

A LAN is a network inside a limited local area, such as a home, office, shop or building.

### 11. What does WAN stand for?

WAN stands for Wide Area Network.

### 12. What is a WAN?

A WAN connects networks across larger distances or outside the local environment.

### 13. In everyday conversation, what does WAN often mean?

It often means the internet connection.

### 14. Can WAN mean something other than internet?

Yes. A WAN can connect one business location to another remote location.

### 15. What is the simple LAN vs WAN mental model?

LAN is inside; WAN is outside.

### 16. What question should you ask first when troubleshooting?

Ask whether the problem stays inside the building or only happens when traffic leaves the building.

### 17. If a printer inside the shop cannot be reached, is that more likely LAN or WAN?

LAN, because the communication is local.

### 18. If the register cannot reach a cloud payment processor, is that more likely LAN or WAN?

WAN or internet-path related, because the communication leaves the local network.

## What To Review Later

- Network means connected devices that can communicate.
- Wireless usually rides on wired infrastructure.
- Switch role in the LAN.
- AP role for WiFi.
- LAN = local/inside.
- WAN = wide/outside.
- Internet as common WAN example.
- WAN can also connect business sites.
- Troubleshooting starts by scoping LAN vs WAN.
