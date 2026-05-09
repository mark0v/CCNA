# Understanding Fiber Optic Cable Spectrum

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Fiber cabling  
Tags: fiber, single mode, multimode, sfp, transceiver, bandwidth, distance, poe, backbone

## Summary

Fiber optic cabling is a different world from copper. Copper is familiar and common for nearby endpoint devices, but fiber solves the problems copper cannot handle well: long distance, high bandwidth and large-scale infrastructure links.

Main idea: fiber is not a replacement for copper everywhere. Fiber is usually the right choice for backbone, uplink, building-to-building, campus, data center and long-distance links, while copper remains strong for endpoint access and PoE-powered devices.

## Key Points

- Fiber optic cable carries data using light.
- Copper Ethernet carries data using electrical signals.
- Copper UTP Ethernet is generally limited to around 100 meters per run.
- Fiber can support much longer distances than copper.
- Fiber is used for buildings, campuses, cities, data centers and long-haul infrastructure.
- Single mode and multimode are the two major fiber types discussed.
- Single mode is built for longer distance and higher bandwidth.
- Multimode is typically used for shorter runs, often inside buildings or local campus environments.
- Single mode may cost more, but the price gap is often smaller than it used to be.
- Choosing fiber type is both a technical and business decision.
- SFP means Small Form-factor Pluggable.
- SFP modules let switches connect to fiber or sometimes copper.
- Fiber planning requires matching switch, module, fiber type, connector type, distance and speed.
- Fiber supports very high speeds such as 25 Gbps, 40 Gbps, 100 Gbps and beyond, depending on equipment.
- Fiber does not carry PoE to endpoint devices like copper can.
- Real networks often use both fiber and copper.

## Notes

### Fiber Is Its Own World

Fiber is not just another cable that happens to look different.

It introduces different choices:

- cable types;
- connectors;
- transceivers;
- distances;
- speeds;
- installation methods;
- splicing and cleaning concerns;
- different design tradeoffs than copper.

You do not need to become a fiber specialist for CCNA, but you do need the big picture.

### Why Fiber Exists

Fiber exists because copper has limits.

Copper is excellent for short, practical endpoint connections, but it is not ideal for:

- very long distances;
- city-scale links;
- building-to-building runs;
- high-speed backbone links;
- data center interconnects;
- very high-capacity switch uplinks.

Fiber uses light, which lets it go much farther and carry much more data at scale.

### Distance Is the Killer Feature

Copper Ethernet over UTP generally tops out around:

```text
100 meters per run
```

Fiber can go far beyond that. Depending on fiber type, optics and infrastructure, fiber can support:

- building-to-building links;
- campus links;
- city links;
- data center links;
- long-haul provider links;
- undersea infrastructure links.

The article's main contrast:

```text
Copper is for nearby devices.
Fiber is for serious distance and serious data.
```

### Fiber Uses Light

The physical signal difference:

| Medium | Signal |
| --- | --- |
| Copper | Electrical pulses |
| Fiber | Pulses of light |

Because fiber uses light, it behaves differently from copper and supports very different design possibilities.

### NetworkChuck Coffee Example

At NetworkChuck Coffee, copper might connect local endpoints inside one shop.

Fiber becomes more important when the business grows and needs to connect:

- central office;
- roasting facility;
- warehouse;
- multiple buildings;
- data center;
- distant network closets;
- high-speed switch uplinks.

Fiber becomes the backbone that lets the network stretch beyond one room or one building.

### Regeneration and Long-Haul Links

The article mentions fiber being extended over massive distances.

Important nuance:

```text
Fiber is not literally unlimited.
It can be regenerated and extended over very long distances.
```

Long-haul networks use fiber because the signal can be repeated/regenerated and carried much farther than copper.

### Single Mode vs Multimode

Two major fiber types:

- single mode;
- multimode.

Comparison:

| Feature | Single mode | Multimode |
| --- | --- | --- |
| Typical distance | Longer | Shorter |
| Typical bandwidth | Higher | Lower than single mode at scale |
| Typical use | Long links, building-to-building, provider/data center links | Inside buildings, closets, shorter campus links |
| Cost | Often more expensive, but gap has narrowed | Historically cheaper |
| Planning mindset | Better for growth and long-term reach | Fine for many short local runs |

### Single Mode Fiber

Single mode fiber is built for long-distance, high-bandwidth communication.

Good fit for:

- long runs;
- building-to-building links;
- provider circuits;
- data center connectivity;
- serious growth planning;
- high-performance network backbones.

Single mode often becomes attractive when replacing fiber later would be expensive or painful.

### Multimode Fiber

Multimode fiber is typically used for shorter distances.

Good fit for:

- server room to nearby closet;
- inside-building links;
- short campus runs;
- local switch uplinks;
- environments where distance is only a few hundred meters or less.

Multimode is not useless. It can still be the correct answer when the use case fits.

### Fiber Choice Is a Business Decision

Do not choose fiber only by cheapest upfront cost.

Think about:

- current distance needs;
- future bandwidth needs;
- business growth;
- cost of replacing installed fiber later;
- downtime risk;
- labor cost;
- redesign cost.

If the business may grow, spending more upfront on the right fiber may be cheaper than replacing it later.

### How Fiber Connects to a Switch

Fiber usually does not plug directly into a normal RJ45 Ethernet port.

Many switches use:

```text
SFP ports
```

SFP means Small Form-factor Pluggable.

An SFP port is a module slot. You insert a module that matches the connection you need.

Examples:

| Module | Result |
| --- | --- |
| Fiber SFP | Switch can connect to fiber |
| Copper SFP | Switch can connect to copper Ethernet |

### SFP Matching

Fiber planning is really parts matching.

You need to match:

- switch support;
- SFP/SFP+ module type;
- fiber type;
- connector type;
- speed requirement;
- distance requirement;
- single mode vs multimode;
- transceiver compatibility.

This can feel intimidating, but the logic is straightforward once you know what to check.

### Bandwidth

Fiber supports very high speeds when paired with the right equipment.

Examples mentioned:

- 25 Gbps;
- 40 Gbps;
- 100 Gbps;
- beyond 100 Gbps in larger infrastructure.

This is why fiber is common for:

- switch uplinks;
- storage networks;
- high-performance servers;
- data center interconnects;
- backbone links.

### Fiber Does Not Provide PoE

Fiber's big practical limitation:

```text
Fiber does not carry electrical power to endpoint devices like copper PoE.
```

PoE means Power over Ethernet.

Devices that commonly rely on PoE:

- wireless access points;
- VoIP phones;
- security cameras;
- small endpoint devices.

For those devices, copper often remains the better practical choice.

### Fiber and Copper Work Together

This is not fiber vs copper.

A realistic network uses both:

| Use case | Common media |
| --- | --- |
| Desktop endpoints | Copper |
| Phones | Copper |
| Access points | Copper with PoE |
| Cameras | Copper with PoE |
| Switch uplinks | Fiber or copper depending on distance/speed |
| Building-to-building links | Fiber |
| Backbone links | Fiber |
| Data center/high-performance links | Fiber |

The design goal is to use each medium where it fits.

### Connectors

Fiber connectors can feel confusing because there are multiple connector styles.

The article mentions LC connectors and other connector types.

The connector is only one part of the match.

You must make sure:

- connector fits the transceiver;
- transceiver fits the switch;
- fiber type fits the transceiver;
- speed and distance requirements match the optics.

### Main Takeaway

Fiber exists because networks outgrow copper.

Fiber gives:

- more distance;
- more bandwidth;
- more capacity;
- better fit for backbones and long links.

Copper still gives:

- simple endpoint access;
- broad compatibility;
- lower cost for short runs;
- PoE for devices that need power.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Fiber optic cable | Cable that carries data as light. |
| Copper Ethernet | Cable that carries data as electrical pulses. |
| UTP | Unshielded Twisted Pair copper Ethernet cabling. |
| Single mode fiber | Fiber type built for long-distance/high-bandwidth links. |
| Multimode fiber | Fiber type often used for shorter local links. |
| SFP | Small Form-factor Pluggable module/slot. |
| Transceiver | Module that sends and receives signals for a link. |
| Connector | Physical end of a cable, such as LC. |
| Backbone | High-capacity network path connecting major network areas. |
| Uplink | Connection from one network device toward another higher-level device. |
| PoE | Power over Ethernet, carried by copper Ethernet, not fiber. |
| Bandwidth | Amount of data a link can carry over time. |
| Long-haul | Network connection over very long distance. |

## Questions

### 1. What signal does fiber use to carry data?

Fiber uses pulses of light.

### 2. What signal does copper use to carry data?

Copper uses electrical pulses.

### 3. What is the typical copper UTP Ethernet distance limit?

Around 100 meters per run.

### 4. What is fiber's biggest advantage over copper in this lesson?

Distance.

### 5. Where is fiber commonly used?

Backbones, uplinks, building-to-building links, campus links, city links, data centers and long-haul infrastructure.

### 6. What are the two main fiber types discussed?

Single mode and multimode.

### 7. Which fiber type usually goes farther?

Single mode.

### 8. Which fiber type is typically used for shorter runs?

Multimode.

### 9. Why might someone choose single mode even if it costs more?

Because it supports longer distances, higher bandwidth and may avoid expensive replacement later as the business grows.

### 10. What does SFP stand for?

Small Form-factor Pluggable.

### 11. What does an SFP module do?

It gives a switch port the correct interface for a specific connection type, such as fiber or copper.

### 12. What must be matched when planning a fiber connection?

Switch, module, fiber type, connector type, speed requirement and distance requirement.

### 13. What speeds can fiber support with the right equipment?

Examples include 25 Gbps, 40 Gbps, 100 Gbps and beyond.

### 14. What important job can copper do that fiber usually cannot?

Copper can carry PoE to endpoint devices.

### 15. Why is this not simply fiber vs copper?

Because real networks use both: fiber for long/high-speed links and copper for endpoint access and PoE.

## What To Review Later

- Fiber uses light; copper uses electricity.
- Copper UTP limit around 100 meters.
- Why fiber wins for distance.
- Single mode vs multimode.
- SFP modules and transceivers.
- Matching switch, module, connector, fiber type, speed and distance.
- Fiber bandwidth use cases.
- Why fiber does not replace copper for PoE endpoints.
