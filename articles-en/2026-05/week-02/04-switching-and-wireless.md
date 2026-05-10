# Switching & Wireless

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / LAN switching and wireless  
Tags: switch, wireless, access point, lan, wifi, ethernet, antennas, coverage, directional antenna

## Summary

The LAN of NetworkChuck Coffee is built mainly on two device types: switches and wireless access points. Switches provide the wired foundation for local devices, while access points extend that same LAN into the air for phones, laptops, tablets and guest devices.

Main idea: WiFi is not magic and not separate from the wired network. Wireless access points usually plug back into switches, so the visible wireless experience depends on the wired LAN underneath.

## Key Points

- The LAN inside NetworkChuck Coffee depends heavily on switches and wireless access points.
- A switch connects wired devices together on the LAN.
- Switch ports are also called interfaces.
- Business networks should use proper switches in a network closet instead of random unmanaged desk switches.
- Small unmanaged desk switches create extra failure points and troubleshooting confusion.
- Common business switches often have 24 or 48 ports.
- Standard Ethernet cable runs are limited to about 328 feet / 100 meters.
- A wireless access point extends the wired LAN into WiFi.
- An AP usually plugs back into the switch.
- Wireless clients join the LAN through the AP.
- WiFi convenience depends on wired infrastructure.
- Antennas shape wireless coverage.
- Omnidirectional antennas spread signal broadly around the AP.
- Directional antennas focus signal in a tighter direction.
- Directional wireless can sometimes connect buildings when running cable is impractical.
- Switches are the foundation; APs are the wireless extension.

## Notes

### The LAN Foundation

Inside a coffee shop, many devices need network access:

- registers;
- printers;
- laptops;
- tablets;
- cameras;
- phones;
- wireless client devices;
- office systems.

Some devices connect with cables. Some connect over WiFi. But both usually tie back to the same wired foundation.

The two key device types:

```text
Switches + wireless access points
```

### The Switch

A switch connects wired devices together on the LAN.

LAN means Local Area Network.

Switches usually live in:

- network closets;
- racks;
- cabinets;
- MDF/IDF areas.

Devices connect to switch ports with Ethernet cables.

Switch ports may also be called:

```text
interfaces
```

### Why Switches Matter

A switch gives wired devices a place to communicate.

Examples:

```text
Register -> switch
Printer -> switch
Camera -> switch
Access point -> switch
Office PC -> switch
```

The switch is usually not flashy, but it is doing the heavy lifting for the LAN all day.

### Avoid Random Desk Switches

Small unmanaged switches under desks may seem convenient, but they create problems in business networks.

Risks:

- extra point of failure;
- extra power brick;
- cable clutter;
- undocumented topology;
- device can be kicked loose;
- harder troubleshooting;
- unknown loops or performance problems;
- cheap hardware failure during busy hours.

Better approach:

```text
Solve port needs intentionally with proper cabling and managed switch design.
```

### Business Switches

In a real business setup, use proper switches in the network closet.

Common port counts:

| Switch size | Typical use |
| --- | --- |
| 24 ports | Small/medium network closet |
| 48 ports | Larger closets or more dense endpoint areas |

Do not obsess over the exact model yet. The important concept is structured, intentional switching.

### Ethernet Distance Limit

Standard Ethernet cable runs are limited to about:

```text
328 feet / 100 meters
```

Beyond that, the signal needs help.

Possible solutions:

- place another switch;
- redesign the cable path;
- use fiber;
- use another appropriate media type.

You cannot run copper Ethernet forever and expect reliable results.

### Wireless Access Point

Wireless access point is usually shortened to:

```text
AP
```

An AP takes the wired network and broadcasts it through the air.

Wireless devices can then connect:

- phones;
- laptops;
- tablets;
- handheld business devices;
- customer devices.

### WiFi Is Not Magic

WiFi can feel separate, but it is usually an extension of the wired LAN.

Simple path:

```text
Wireless client -> AP -> switch -> LAN
```

The AP does not create a separate universe. It connects back into the same network infrastructure.

### Switch and AP Relationship

The switch provides the wired foundation.

The AP extends that foundation wirelessly.

Simple model:

```text
Wired devices -> switch
Wireless devices -> AP -> switch
```

This is why bad switch/cabling design can still break WiFi experiences.

### Antennas and Coverage

Wireless coverage depends partly on antenna behavior.

Antennas shape how signal travels.

Two broad types from the lesson:

| Antenna type | Signal behavior |
| --- | --- |
| Omnidirectional | Broad coverage around the device |
| Directional | Focused signal in a tighter direction |

### Omnidirectional Antennas

Omnidirectional antennas spread signal broadly.

Mental picture:

```text
Bubble/circle of coverage around the AP
```

Good fit for:

- cafe seating area;
- office spaces;
- general room coverage;
- areas where clients are spread around the AP.

### Directional Antennas

Directional antennas focus the signal.

The hose analogy:

```text
Put your thumb over a hose -> water shoots farther.
Focus wireless signal -> signal can reach farther in one direction.
```

Good fit for:

- point-to-point wireless links;
- connecting nearby buildings;
- targeting coverage down a hallway;
- outdoor links across a lot;
- cases where running cable is expensive or impractical.

### Wireless Building Bridges

Wireless can sometimes connect buildings without trenching cable.

Example:

```text
Building A AP/antenna -> wireless bridge -> Building B AP/antenna
```

This can help when NetworkChuck Coffee needs connectivity between nearby buildings and running cable through the ground would be too expensive.

### How the Pieces Fit Together

Physical model:

```text
Internet -> network equipment -> switch -> wired devices
                                      -> AP -> wireless devices
```

More detailed:

```text
ISP/internet enters the shop.
Network equipment distributes connectivity internally.
The switch connects wired LAN devices.
The AP plugs into the switch.
Wireless devices join the LAN through the AP.
```

### Main Takeaway

Switches and wireless access points build the coffee shop LAN.

Short version:

```text
Switch = local wired foundation.
AP = wireless extension of that foundation.
```

If you understand those roles, the rest of the network design has a clear place to attach.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| LAN | Local Area Network. |
| Switch | Device that connects wired LAN devices. |
| Port/interface | Physical/logical switch connection where a cable plugs in. |
| Access point | Device that extends the wired LAN into WiFi. |
| AP | Short for access point. |
| WiFi | Wireless network access for client devices. |
| Ethernet | Wired network technology commonly used to connect LAN devices. |
| Unmanaged switch | Simple switch with little/no configuration, risky when used randomly in business environments. |
| Managed switch | Switch with management/configuration features. |
| Omnidirectional antenna | Antenna that spreads signal broadly around the device. |
| Directional antenna | Antenna that focuses signal in a specific direction. |
| Wireless bridge | Wireless link used to connect two network areas or buildings. |

## Questions

### 1. What two device types build much of the coffee shop LAN?

Switches and wireless access points.

### 2. What does a switch do?

It connects wired devices together on the LAN.

### 3. What are switch ports sometimes called?

Interfaces.

### 4. Why are random unmanaged desk switches risky in a business network?

They add failure points, power bricks, undocumented connections and troubleshooting confusion.

### 5. Where should proper business switches usually live?

In a network closet, rack or structured network area.

### 6. What common port counts were mentioned for business switches?

24 ports and 48 ports.

### 7. What is the standard Ethernet copper run limit mentioned?

About 328 feet or 100 meters.

### 8. What does an access point do?

It takes the wired network and broadcasts it wirelessly so WiFi devices can connect.

### 9. Does an AP usually connect back to a switch?

Yes. The AP usually plugs into the switch.

### 10. Why is WiFi not magic?

Because wireless clients usually depend on an AP that is connected to the wired LAN underneath.

### 11. What is an omnidirectional antenna?

An antenna that spreads signal broadly around the device.

### 12. What is a directional antenna?

An antenna that focuses signal in a tighter direction.

### 13. How can directional antennas help between buildings?

They can focus wireless signal far enough to create a point-to-point link when running cable is impractical.

### 14. What is the simple relationship between a switch and an AP?

The switch is the wired foundation, and the AP extends that foundation into WiFi.

### 15. What should you avoid when users need more ports?

Avoid tossing random cheap switches under desks; solve it intentionally with proper cabling and switch design.

## What To Review Later

- Switch role in the LAN.
- Port/interface terminology.
- Why random unmanaged desk switches are bad in business networks.
- Ethernet 100-meter / 328-foot limit.
- AP as wired LAN extension into WiFi.
- WiFi depends on wired infrastructure.
- Omnidirectional vs directional antennas.
- Wireless building bridge concept.
- Switch = foundation, AP = extension.
