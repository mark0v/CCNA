# Fiber Optic Cables (What you NEED to know)

Source: закрытая страница курса  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 00 Lesson 13  
Tags: fiber, multimode, single mode, lc, sfp, duplex, emi, copper

## Summary

Fiber optic cable передает data с помощью pulses of light, а не electrical signals. Поэтому fiber отлично подходит для high bandwidth, long distance links и environments с electromagnetic interference. В реальных networks fiber часто используют для uplinks, backbone connections, building-to-building links, ISP handoffs и data center/campus connections.

Главная мысль статьи: fiber не заменяет copper везде. Fiber и copper решают разные задачи, и хороший network design использует оба media там, где они подходят лучше всего.

## Key Points

- Fiber optic cable передает data using light.
- Fiber дает high bandwidth, long distance и resistance to EMI.
- Copper Ethernet still matters because it is cheaper, easier and supports PoE.
- Fiber cable has core and cladding.
- Core carries light.
- Cladding keeps light inside the core.
- Fiber is delicate: it should not be kinked, crushed or bent too sharply.
- Two major fiber types: multimode and single mode.
- Multimode usually fits shorter distances and inside-building use cases.
- Single mode fits longer distances and high-performance links.
- Fiber commonly uses connectors like LC.
- Duplex fiber often uses one strand for transmit and one for receive.
- SFP means Small Form-factor Pluggable.
- SFP modules let a switch port support fiber or copper depending on module type.
- Before ordering fiber, check connector type, fiber type, distance and device/module support.

## Notes

### Fiber Uses Light

Fiber optic cable sends data using pulses of light.

Copper Ethernet uses electrical signals. Fiber uses light traveling through a tiny strand.

This difference gives fiber several advantages:

- faster speeds;
- longer distances;
- resistance to electrical interference;
- strong fit for backbones and uplinks;
- useful for ISP and data center connectivity.

### Why We Use Fiber

Fiber solves problems that copper cannot solve as well.

Main advantages:

| Advantage | Why it matters |
| --- | --- |
| Speed | Supports very high bandwidth links |
| Distance | Can go much farther than copper |
| EMI resistance | Light is not affected like copper electrical signals |
| Backbone use | Good for core, campus and data center links |

For NetworkChuck Coffee, fiber might appear in:

- core switch connections;
- building-to-building links;
- first-floor to third-floor closet uplinks;
- ISP high-speed internet handoff;
- data center/corporate links;
- switch uplinks.

### EMI

EMI means Electromagnetic Interference.

Copper can be affected by electrical noise because it carries electrical signals.

Fiber uses light, so it avoids many EMI problems.

This makes fiber useful in places with:

- heavy electrical equipment;
- long cable runs;
- industrial environments;
- high-density network closets;
- backbone paths where reliability matters.

### How Light Stays Inside Fiber

Fiber cable has two key internal parts:

| Part | Role |
| --- | --- |
| Core | Tiny center where light travels |
| Cladding | Surrounding layer that keeps light inside |

The light reflects in a controlled way inside the cable, staying within the core instead of escaping.

You do not need deep physics for CCNA, but you do need the basic model:

```text
Fiber guides light through a tiny path.
```

### Fiber Is Delicate

Fiber needs more care than copper patch cables.

Avoid:

- kinking;
- crushing;
- sharp bends;
- pulling too hard;
- dirty connectors;
- careless handling.

If fiber is damaged, it is usually not as easy to fix in the field as copper with a simple crimping tool.

### Fiber Ordering Checklist

Before ordering or installing fiber, check:

- connector type;
- fiber type;
- required distance;
- switch/transceiver support;
- single mode vs multimode;
- duplex vs other options;
- speed requirement;
- correct SFP/SFP+ module;
- patch panel/termination type.

Fiber mistakes are annoying because they often require a new cable or module, not a quick re-crimp.

### Single Mode vs Multimode

Two major fiber types:

- multimode;
- single mode.

Comparison:

| Feature | Multimode | Single mode |
| --- | --- | --- |
| Core size | Larger | Smaller |
| Light path | More bouncing/modes | More direct path |
| Typical distance | Shorter | Longer |
| Typical use | Inside building, racks, closets | Building-to-building, ISP, long-haul |
| Cost | Often cheaper overall for short runs | Often more expensive |
| Strength | Practical short high-speed links | Long distance and high performance |

### Multimode Fiber

Multimode has a larger core. Light has more room to bounce around as it travels.

Good fit for:

- short runs;
- inside-building cabling;
- switch-to-switch links in closet;
- rack-level high-speed connections;
- short data center connections.

Multimode is often exactly right for many real-world local jobs.

### Single Mode Fiber

Single mode has a much smaller core. Light travels more directly, with lower signal loss.

Good fit for:

- long distance runs;
- building-to-building links;
- ISP-scale connections;
- campus links;
- high-performance long links.

Single mode wins on distance, but that does not mean it is always the best choice for every job.

### Connectors

Fiber uses different connector types than copper Ethernet.

The article mentions LC connectors, which are very common in modern fiber deployments.

Fiber connector details matter because a cable with the wrong connector may not fit your transceiver, patch panel or device.

Common planning question:

```text
What connector does my SFP/transceiver require?
```

### Duplex Fiber

Many fiber cables come in pairs.

Duplex means two-way communication using two separate paths.

Simple model:

```text
One strand transmits.
One strand receives.
```

This is different from a single copper Ethernet cable where transmit/receive behavior is handled through pairs inside the cable.

### SFP

SFP means Small Form-factor Pluggable.

An SFP port is a slot where you insert a module. The module determines what type of connection the port supports.

Examples:

| Module type | Result |
| --- | --- |
| Fiber SFP | Port connects to fiber |
| Copper SFP | Port connects to copper Ethernet |

This makes switch hardware more flexible.

At NetworkChuck Coffee, an SFP module might be used for:

- fiber uplink to core switch;
- fiber link to another closet;
- copper uplink if needed;
- ISP handoff;
- data center connection.

### Fiber vs Copper

Fiber is powerful, but copper is not going away.

Comparison:

| Feature | Fiber | Copper Ethernet |
| --- | --- | --- |
| Signal | Light | Electricity |
| Distance | Longer | Shorter |
| Bandwidth | Very high | High, but usually less for long runs |
| EMI resistance | Excellent | More affected by EMI |
| Cost/ease | More planning/care | Cheaper and easier |
| PoE | No typical endpoint PoE role | Supports PoE |
| Common use | Uplinks, backbone, long runs | Endpoints, access layer |

### Why Copper Still Matters

Copper is still common because it is:

- cheaper;
- easier to work with;
- supported by almost everything;
- great for endpoints;
- capable of PoE.

Typical copper devices:

- desktops;
- printers;
- phones;
- access points;
- cameras;
- office devices.

PoE is one of the biggest reasons copper remains important at the access layer.

### Where Fiber Usually Fits

Fiber often fits:

- switch uplinks;
- backbone connections;
- core/distribution links;
- building-to-building runs;
- long runs;
- high-speed paths;
- data center links;
- ISP connections.

Copper often fits:

- endpoint access;
- phones;
- APs;
- cameras;
- desktops;
- printers;
- PoE devices.

### Main Takeaway

Fiber uses light, not electricity. This gives it major advantages in speed, distance and interference resistance.

But network engineers still choose the right tool:

```text
Fiber for uplinks/backbones/long high-speed links.
Copper for endpoints/access layer/PoE.
```

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Fiber optic cable | Cable that transmits data using light. |
| Copper Ethernet | Cable that transmits data using electrical signals. |
| EMI | Electromagnetic Interference. |
| Core | Center of fiber where light travels. |
| Cladding | Layer around fiber core that keeps light inside. |
| Multimode fiber | Fiber with larger core, usually for shorter runs. |
| Single mode fiber | Fiber with smaller core, used for longer distance/high performance links. |
| LC connector | Common fiber connector type. |
| Duplex | Two-way communication using two paths/strands. |
| SFP | Small Form-factor Pluggable module/slot. |
| Transceiver | Module that sends/receives signals, such as SFP. |
| Uplink | Connection from one network device upward/toward core/distribution. |
| Backbone | High-capacity network path tying major network areas together. |
| PoE | Power over Ethernet, supported by copper Ethernet, not typical fiber endpoint cabling. |

## Questions

### 1. What does fiber optic cable use to transmit data?

Fiber uses pulses of light.

### 2. Why is fiber resistant to EMI?

Because fiber uses light instead of electrical signals, so electromagnetic interference affects it much less than copper.

### 3. What are the two main internal parts of fiber mentioned in the article?

Core and cladding.

### 4. What does the core do?

The core is the tiny center where light travels.

### 5. What does the cladding do?

The cladding helps keep light inside the core.

### 6. What is multimode fiber usually used for?

Multimode is usually used for shorter distances, often inside buildings, closets, racks and short data center links.

### 7. What is single mode fiber usually used for?

Single mode is used for longer distance runs, building-to-building links, ISP-scale links and high-performance long connections.

### 8. What does duplex fiber mean?

Duplex means two-way communication using two separate paths, often one strand to transmit and one to receive.

### 9. What does SFP stand for?

SFP stands for Small Form-factor Pluggable.

### 10. Why are SFP modules useful?

They let the same switch slot support different connection types, such as fiber or copper, depending on the module.

### 11. Why is copper still common if fiber is so powerful?

Copper is cheaper, easier to work with, widely supported and can deliver PoE to endpoint devices.

### 12. Where would you expect to see fiber in a business network?

Uplinks, backbone links, switch-to-switch links, building-to-building links, ISP handoffs and data center connections.

### 13. What should you check before ordering fiber?

Connector type, fiber type, distance, device/transceiver support, speed requirement and whether the link needs single mode or multimode.

### 14. Why should fiber not be kinked or bent sharply?

Because fiber is delicate; sharp bends or damage can break it or degrade signal performance.

## What To Review Later

- Fiber uses light, copper uses electricity.
- Core and cladding.
- EMI resistance.
- Multimode vs single mode.
- LC connector and duplex fiber.
- SFP modules and transceivers.
- Fiber vs copper use cases.
- Why copper remains important for PoE and endpoint access.
