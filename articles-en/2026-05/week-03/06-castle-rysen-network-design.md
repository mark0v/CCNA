# Castle Rysen Network Design

Source: closed course page  
Date added: 2026-05-16  
Related plan item: Week 3 / Applying network design models  
Tags: network design, soho, two-tier, three-tier, mdf, idf, fiber, redundancy, ethernet distance
Language: English
Translation pair: articles/2026-05/week-03/06-castle-rysen-network-design.md

## Summary

Network design models become useful when you apply them to a real building. A small café and a large multi-zone building use similar principles, but scale creates different decisions. In a small SOHO network, the goal is to prevent chaotic switch growth and keep spare capacity. In a larger building, you need structure: an MDF as the central point, IDFs in separate zones, redundant uplinks and fiber where Ethernet distance limits become a problem.

Main idea: a model is not exam theory. It is a decision tool for a real project.

## Key Points

- Small café networks can become messy quickly if switches are added organically.
- SOHO does not mean "ignore design."
- Around the third switch, it is time to become intentional.
- Keep switch capacity available instead of maxing out every port.
- Leaving 20-30% spare ports helps during failures and growth.
- Separating roles across switches makes failures easier to recover from.
- Larger buildings often need MDF and IDF planning.
- MDF is the main network distribution point.
- IDFs serve local building zones and connect back to the MDF.
- Redundant uplinks reduce single points of failure.
- Fiber is often used between MDF and IDFs.
- Ethernet copper runs are commonly limited to about 100 meters.
- Attenuation means signal weakens over distance.
- Three-tier thinking helps organize large, multi-area buildings.
- Design models help translate theory into real cable and equipment placement.

## Notes

### From Model to Real Building

Two-tier, three-tier and spine-leaf sound abstract until you stand in a real building and decide:

- where to place switches;
- where cables should run;
- where the network core belongs;
- how to survive a switch or cable failure;
- which distances are acceptable.

The model helps turn the building into a network plan.

### Scenario 1 - Small Café

Imagine NetworkChuck Coffee or Castle Rysen Coffee as a small café with around 15 people.

This looks like SOHO:

```text
Small Office, Home Office
```

It may include:

- Plex server;
- wireless access points;
- POS terminals;
- staff computers;
- printers;
- phones;
- guest Wi-Fi.

At this size, the network often grows organically:

```text
Need more ports -> add a switch
Need more ports again -> add another switch
Now nobody knows what connects where
```

That is the trap.

### When Three Switches Appear

Real-world practical rule:

```text
When you hit switch number three, start designing intentionally.
```

This is not a strict exam rule, but it is a useful habit.

Do not just add a switch and hope. Stop and think:

- which devices connect where;
- which roles the switches have;
- what breaks if one switch fails;
- whether spare ports exist;
- how quickly service can be restored.

### Cleaner Small Café Design

Suppose you have three 24-port switches:

- Switch A;
- Switch B;
- Switch C.

Instead of chaos, assign roles:

```text
Switch A: wireless access points
Switch B: most wired devices
Switch C: additional wired devices / spare capacity
```

If Switch A is dedicated to WAPs and fails, you lose Wi-Fi, but not the whole network.

You can temporarily move AP cables to Switch B or Switch C if spare ports are available.

### Leave Breathing Room

Do not max out switch ports.

Good practice:

```text
Keep 20-30% of ports free.
```

Why it matters:

- easier failed-switch recovery;
- easier growth;
- easier temporary cable moves;
- less emergency work;
- less risk during troubleshooting.

If every port is used, every failure becomes a crisis.

### Two-Tier-ish Thinking

A small café does not need a full campus design.

But it helps to think loosely in a two-tier way:

```text
Access devices -> organized switching -> router/internet/services
```

Even a loose two-tier design is better than random sprawl.

The goal:

- simplicity;
- readable layout;
- recoverability;
- room for growth.

### Scenario 2 - Larger Building

Now imagine the Fallout Shelter or a large multi-area building.

It has zones:

- eatery;
- sleeping quarters;
- administration wing;
- network core;
- other building areas.

SOHO thinking no longer works here.

You need structure.

### MDF

MDF means:

```text
Main Distribution Facility
```

This is the main network room or central distribution point.

The MDF usually contains:

- distribution/core switches;
- router connections;
- internet handoff;
- firewall or edge devices;
- major uplinks;
- central patching.

In a large building, the MDF is the heart of the network.

### IDF

IDF means:

```text
Intermediate Distribution Facility
```

IDFs are placed closer to building zones.

Examples:

- IDF for eatery;
- IDF for sleeping quarters;
- IDF for administration;
- IDF for another floor or wing.

An IDF acts like the local access layer for that area.

Cables from the IDF serve devices in that zone.

### MDF to IDF Connections

IDFs connect back to the MDF.

Common media:

- fiber optic cable;
- sometimes Ethernet copper, if distance allows.

Important: you usually run multiple links for redundancy, not just one uplink.

Bad option:

```text
IDF -> one cable -> MDF
```

Better:

```text
IDF -> redundant uplinks -> MDF
```

One cable is a single point of failure.

### Ethernet Distance Limit

Copper Ethernet is commonly limited to about:

```text
100 meters
```

If the run is too long, signal quality degrades.

This is related to attenuation:

```text
Attenuation = signal loss over distance
```

In a large building, you cannot always run every cable directly back to the MDF. The distance may simply be too great.

### Why IDFs Exist

IDFs help you work with physics instead of fighting it.

Instead of pulling every endpoint cable back to the central core:

```text
Device -> local IDF -> fiber/uplink -> MDF
```

The large building becomes manageable:

- local cable runs are shorter;
- uplinks are planned;
- zones are clear;
- troubleshooting is easier;
- redundancy can be designed.

### Three-Tier Thinking in Practice

For a large building:

```text
End devices -> IDF/access layer -> MDF/distribution or core -> outside networks/services
```

In a campus environment, this can expand to:

```text
Access in each area -> Distribution per building -> Core between buildings
```

The model helps you identify access, distribution and when core is needed.

### Café vs Fallout Shelter

| Environment | Design Thought |
| --- | --- |
| Small café | Keep it simple, organized and recoverable. |
| Three switches in café | Stop growing randomly; assign roles and leave spare ports. |
| Large multi-zone building | Use MDF and IDFs. |
| Long cable distances | Use fiber or strategically placed IDFs. |
| Critical links | Add redundancy. |

### Main Takeaway

Models are decision tools.

They help when you stand in a real building and decide:

- a café can use a simple two-tier-ish design;
- a big multi-zone building needs MDF/IDF planning;
- copper distance limits matter;
- redundancy must be intentional;
- switch capacity must leave room for failure and growth.

Theory is the map. The real building is the territory.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| SOHO | Small Office, Home Office; simple small-network environment. |
| Organic growth | Network growth by adding devices as needed without a planned design. |
| Two-tier model | Design with access and distribution/collapsed core functions. |
| Three-tier model | Design with access, distribution and core layers. |
| MDF | Main Distribution Facility; main network distribution point or network room. |
| IDF | Intermediate Distribution Facility; local distribution point for a building area or floor. |
| WAP | Wireless Access Point. |
| Redundancy | Extra path, device or link that keeps service available during failure. |
| Single point of failure | One component whose failure can break a larger service or area. |
| Uplink | Connection from a lower-layer switch or IDF back toward distribution/core. |
| Fiber optic cable | Cable using light, often used for longer distances and uplinks. |
| Ethernet distance limit | Copper Ethernet runs are commonly limited to about 100 meters. |
| Attenuation | Signal weakening over distance. |
| Spare capacity | Unused ports or resources reserved for growth and recovery. |

## Questions

### 1. Why can a small café network become messy quickly?

Because switches are often added organically as ports run out, without documenting roles or paths.

### 2. What practical warning appears around the third switch?

It is time to stop adding switches randomly and start designing intentionally.

### 3. Why should you avoid maxing out switch ports?

Spare ports make growth and failure recovery much easier.

### 4. How much spare switch capacity is a good practical target?

About 20-30% free ports when possible.

### 5. Why might one switch be dedicated to wireless access points?

It creates a clean role boundary, so if that switch fails, the failure is easier to understand and recover from.

### 6. What is an MDF?

Main Distribution Facility; the main network distribution room or central point for core/distribution equipment.

### 7. What is an IDF?

Intermediate Distribution Facility; a local network distribution point serving a specific area, floor or wing.

### 8. Why use IDFs in a large building?

They shorten local cable runs, organize zones and connect back to the MDF through planned uplinks.

### 9. Why are redundant uplinks important?

They reduce the risk that one failed cable or link disconnects an entire area.

### 10. What is the common copper Ethernet distance limit?

About 100 meters.

### 11. What is attenuation?

Signal weakening over distance.

### 12. When does fiber make sense between MDF and IDF?

When distance, bandwidth or uplink reliability needs exceed what copper Ethernet can comfortably provide.

## What To Review Later

- SOHO growth trap.
- Switch role planning.
- Leaving 20-30% spare ports.
- Two-tier-ish café design.
- MDF and IDF roles.
- Redundant uplinks.
- Ethernet 100-meter distance limit.
- Attenuation.
- Fiber between distribution points.
