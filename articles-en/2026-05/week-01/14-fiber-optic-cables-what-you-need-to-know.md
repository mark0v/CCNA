# Fiber Optic Cables (What you NEED to know)

Source: private course page  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 01 Lesson 02  
Tags: fiber, fiber optic, single mode, multimode, sfp, lc, copper, poe

## Summary

Fiber optic cable sends data using light instead of electricity. It is fast, supports long distances and is resistant to electromagnetic interference, which makes it ideal for uplinks, building links, backbone connections and ISP handoffs.

Main idea: fiber is not exotic magic. It is a normal part of modern networking when copper reaches its limits.

## Key Points

- Fiber uses light pulses.
- Copper uses electrical signals.
- Fiber resists EMI.
- Fiber can go much farther than copper.
- Fiber supports very high bandwidth.
- A fiber cable has a core and cladding.
- Single mode is used for longer distances.
- Multimode is common for shorter runs.
- LC connectors are common.
- Duplex fiber often uses one strand to send and one to receive.
- SFP modules let switches accept fiber or copper modules.
- Fiber does not provide PoE like copper.
- Real networks often use fiber for uplinks and copper for endpoints.

## Notes

### Why Use Fiber?

Fiber is useful for:

- switch uplinks;
- data center connections;
- building-to-building links;
- high-speed server links;
- ISP circuits;
- long-distance runs.

### Single Mode vs Multimode

```text
Multimode   = shorter distance, often inside buildings
Single mode = longer distance and higher performance
```

### SFP Modules

Many switches do not have fixed fiber ports. Instead they have SFP slots:

```text
Switch -> SFP module -> Fiber cable
```

The module must match the fiber type, connector, speed and distance.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Fiber | Cable that carries light pulses. |
| Single mode | Fiber type for long distances. |
| Multimode | Fiber type for shorter distances. |
| SFP | Small Form-factor Pluggable module. |
| LC | Common fiber connector. |

## Questions

### Why does fiber ignore many EMI problems?

It uses light instead of electrical signals.

### Why does copper still matter?

It is cheaper, common and supports PoE for endpoints.

## What To Review Later

- Fiber connector types.
- SFP vs SFP+.
- Duplex vs simplex fiber.
- Fiber cleaning and handling.
