# Staging the Network Equipment

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Network equipment staging  
Tags: staging, switch, router, access point, server, lan, wan, mdf, redundancy, auto-mdix

## Summary

Staging network equipment means building and testing the network setup before installing it on site. Instead of opening boxes at NetworkChuck Coffee and hoping everything works, you power on the gear, connect the pieces, label cables and verify the basic design in a safe environment first.

Main idea: stage first, install second. The switch ties the local wired network together, the access point extends it over WiFi, the router connects the LAN to the WAN/internet, and staging helps catch mistakes before they become expensive on-site problems.

## Key Points

- Staging means setting up network equipment before the real installation.
- Staging can happen at home, in an office or on a workbench.
- The goal is to confirm power, cables, ports and basic design before going on site.
- A switch is the center of the local wired LAN.
- Devices like registers, servers, office PCs, cameras and APs often plug into the switch.
- A 24-port switch is only an example; the key idea is having enough Ethernet ports for devices.
- Multiple switches can provide flexibility and redundancy.
- Redundancy means backup/resilience if something fails.
- Two switches can help avoid one single failure point, but also add design choices.
- Switches are connected together so they can share traffic.
- Modern switches usually support Auto-MDIX for easier switch-to-switch cabling.
- Servers provide services to clients on the network.
- Clients consume services from servers.
- Wireless access points extend the wired network into the air.
- Cable colors are for organization; color has no inherent technical meaning.
- The router connects the local LAN to the outside WAN/internet.
- ISP means Internet Service Provider.
- Router/firewall functions often control what traffic is allowed or blocked.
- Labeling cables and ports before installation prevents mistakes.
- MDF means Main Distribution Facility, the central place where network gear lives.

## Notes

### Build It Before You Need It

Staging is the habit of building the network before the real installation.

Instead of doing this first on site:

```text
Open boxes -> guess -> plug things in -> hope it works
```

Do this first in a safe place:

```text
Unbox -> power on -> connect -> label -> test -> install
```

Staging turns surprises into small problems instead of live-site emergencies.

### Why Staging Matters

On site, mistakes are expensive.

Possible problems:

- access point does not power up;
- switch port is bad;
- router is not configured as expected;
- wrong cables are packed;
- power adapter is missing;
- device firmware or settings are not ready;
- labels are missing;
- physical layout is unclear.

In staging, these are annoying but manageable. In a coffee shop with customers waiting, they become pressure.

### The Switch Is the Center of the LAN

The switch is usually the central device for the local wired network.

LAN means Local Area Network.

Devices that may plug into the switch:

- registers/POS terminals;
- wireless access points;
- cameras;
- servers;
- office PCs;
- printers;
- network storage;
- other switches.

Simple model:

```text
LAN devices -> switch
```

The switch ties the internal network together.

### Port Count

The article uses a 24-port Cisco switch as an example.

The exact model is not the point.

The important idea:

```text
A switch gives devices Ethernet ports to connect to the LAN.
```

When planning, think about:

- number of current devices;
- spare ports;
- future growth;
- uplinks;
- APs and cameras;
- whether PoE is required.

### One Switch vs Multiple Switches

Sometimes one larger switch is enough. Sometimes more than one switch makes sense.

Reasons to use multiple switches:

- more flexibility;
- more available ports;
- physical layout;
- redundancy;
- separation between areas;
- future growth.

Tradeoff:

```text
More devices can add resilience,
but also add more devices that can fail and must be managed.
```

### Redundancy

Redundancy means having backup/resilience if something fails.

The lesson's mindset:

```text
Two is one, one is none.
```

If one switch is the only central point and it dies, the network may be down.

Multiple switches can reduce that risk when designed properly.

### Connecting Switches

If you use two switches, they need to connect to each other so traffic can pass between devices on both switches.

Simple model:

```text
Switch A <-> Switch B
```

Older environments sometimes required thinking about crossover cables for switch-to-switch links.

Modern gear usually supports Auto-MDIX, which detects and adjusts the transmit/receive behavior automatically.

### Auto-MDIX

Auto-MDIX makes modern cabling easier.

Plain-English meaning:

```text
The switch figures out how to communicate over the cable automatically.
```

This reduces the need to manually worry about straight-through vs crossover cables in most modern setups.

### Servers and Clients

A server provides services to the network.

Examples of services:

- file storage;
- media;
- internal apps;
- databases;
- authentication;
- backups.

A client consumes those services.

Examples of clients:

- laptops;
- tablets;
- register terminals;
- office PCs;
- phones.

Simple model:

```text
Client -> requests service -> server
```

### Wireless Access Point

A wireless access point extends the wired network into the air.

The AP usually connects to the switch with Ethernet.

Simple model:

```text
Wireless clients -> AP -> switch -> LAN/WAN
```

The AP gives WiFi access to:

- phones;
- laptops;
- tablets;
- handheld business devices;
- customer devices.

The network may feel wireless to users, but the AP normally depends on the wired LAN.

### Cable Colors

Cable colors do not inherently change how Ethernet works.

A blue cable is not technically different from a yellow cable just because of color.

Colors are useful for organization.

Examples:

| Color use | Possible meaning |
| --- | --- |
| Blue | General data |
| Yellow | APs |
| Red | WAN/uplink |
| Green | Cameras |

These meanings are local conventions. The cable color itself does not define the network role.

### The Router Connects to the Internet

The switch, AP and server can create a working LAN.

But a LAN alone does not automatically provide internet access.

The router connects the local network to the outside world.

Simple model:

```text
LAN -> router -> WAN/internet
```

### WAN and ISP

WAN means Wide Area Network.

In this lesson, the WAN is the internet connection.

ISP means Internet Service Provider.

Examples of ISP handoff/connection types:

- cable;
- fiber;
- DSL;
- wireless handoff;
- other provider circuits.

The ISP delivers connectivity into the building.

### Router and Security

The router often does more than forward traffic.

It may also handle:

- firewall rules;
- filtering;
- allowed traffic;
- blocked traffic;
- NAT;
- basic edge protection.

The article does not go deep here yet. The important point is location:

```text
The router/edge device is where the local network meets the outside world.
```

### Label Before Installation

Labeling is a small habit with huge payoff.

Label:

- cables;
- switch ports;
- router ports;
- AP locations;
- patch panel ports;
- power adapters;
- uplinks.

On site, especially under pressure, labels reduce dumb mistakes.

### MDF

MDF means Main Distribution Facility.

Plain-English meaning:

```text
The central location where network gear lives.
```

In a real coffee shop, cable runs may go through walls and ceilings back to the MDF.

During staging, the same design is compressed onto a desk or workbench so you can test it before dealing with real physical distances.

### Staging vs Final Install

Staging is a tabletop version of the real install.

It helps verify:

- devices power on;
- basic cabling works;
- switches connect;
- AP connects;
- router path is understood;
- labels make sense;
- planned topology is practical.

Final installation adds real-world complexity:

- ceilings;
- walls;
- long cable runs;
- ladders;
- physical mounting;
- customer pressure;
- business downtime.

### Physical Picture

The article's physical model:

```text
Clients/servers/APs/cameras -> switch -> router -> internet
```

Expanded:

```text
Wireless clients -> AP -> switch
Wired clients -> switch
Server -> switch
Switch -> router -> ISP/internet
```

This picture gives deeper networking concepts somewhere to live.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Staging | Building/testing equipment before installing it on site. |
| Switch | Central LAN device that connects wired network devices. |
| LAN | Local Area Network. |
| WAN | Wide Area Network. |
| Router | Device that connects the local network to other networks, such as the internet. |
| ISP | Internet Service Provider. |
| AP | Access Point; device that provides WiFi. |
| Auto-MDIX | Feature that automatically handles transmit/receive cabling behavior. |
| Server | Device/system that provides services to clients. |
| Client | Device/application that consumes services. |
| Redundancy | Backup/resilience if something fails. |
| MDF | Main Distribution Facility; central network equipment location. |
| Uplink | Connection between network devices, often switch-to-switch or switch-to-router. |
| Firewall rules | Rules that allow or block traffic. |

## Questions

### 1. What does staging network equipment mean?

It means setting up and testing the network gear before installing it on site.

### 2. Why should you stage equipment before installation?

Because it helps catch problems safely before they become expensive on-site issues.

### 3. What is usually the center of the local wired network?

The switch.

### 4. What does a switch provide?

It provides Ethernet ports and connects wired LAN devices together.

### 5. Why might you use more than one switch?

For flexibility, more ports, physical layout, future growth or redundancy.

### 6. What does redundancy mean?

Redundancy means backup or resilience if something fails.

### 7. What does Auto-MDIX do?

It automatically adjusts transmit/receive behavior so modern devices can usually communicate over normal cables.

### 8. What does a server do?

A server provides services to other devices on the network.

### 9. What does a client do?

A client consumes services from a server.

### 10. What does a wireless access point do?

It extends the wired network into the air so wireless devices can connect over WiFi.

### 11. Do Ethernet cable colors have inherent technical meaning?

No. Cable colors are useful for organization, but the color itself does not change how the cable works.

### 12. What device connects the LAN to the internet?

The router.

### 13. What does ISP stand for?

Internet Service Provider.

### 14. What is the WAN in this lesson?

The outside network/internet connection.

### 15. What security-related functions may live near the router?

Firewall rules, filtering and decisions about what traffic is allowed or blocked.

### 16. Why is labeling cables and ports important?

It reduces mistakes during installation and troubleshooting, especially under pressure.

### 17. What does MDF stand for?

Main Distribution Facility.

### 18. What is the main physical picture from this lesson?

Devices connect to switches, access points extend the LAN over WiFi, and the router connects the local network to the internet.

## What To Review Later

- Staging first, installing second.
- Switch as the center of the wired LAN.
- Why multiple switches can help with redundancy.
- Auto-MDIX for switch-to-switch cabling.
- Server vs client.
- Access point role.
- Router connects LAN to WAN/internet.
- ISP meaning.
- Cable colors as organization, not technical truth.
- MDF as central network equipment location.
