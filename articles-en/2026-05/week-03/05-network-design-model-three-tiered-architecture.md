# Network Design Model - Three Tiered Architecture

Source: closed course page  
Date added: 2026-05-16  
Related plan item: Week 3 / Network design models  
Tags: network design, three-tier architecture, access layer, distribution layer, core layer, collapsed core, spine leaf, soho
Language: English
Translation pair: articles/2026-05/week-03/05-network-design-model-three-tiered-architecture.md

## Summary

A network design model helps you build a network intentionally instead of just plugging devices together until ports run out. Three-tier architecture divides a campus network into the access layer, distribution layer and core layer. This gives the network structure, redundancy and scalability.

For a tiny network, the SOHO model can be fine: a router, a switch and a few devices. But once the network becomes important to the business, random daisy-chained switches become risky. One or two buildings often use a two-tier or collapsed core design. Three or more buildings usually need a separate core layer.

## Key Points

- Bad network design often starts as devices randomly plugged together.
- SOHO model can work for a very small office or home network.
- A growing business quickly outgrows unmanaged daisy-chained switches.
- Three-tier architecture is a classic Cisco network design model.
- Access layer is where end devices connect.
- Distribution layer aggregates access switches and provides redundancy.
- Core layer connects buildings or major network blocks at scale.
- Access switches should connect upward, not randomly to each other.
- Redundant links to two distribution switches reduce single points of failure.
- Two-tier design is also called collapsed core.
- Collapsed core combines distribution and core functions.
- One or two buildings often use two-tier design.
- Three or more buildings usually need a core layer.
- Spine-leaf is another architecture, mostly used in data centers.
- Good design prevents fragile, hard-to-troubleshoot networks.

## Notes

### Why Design Matters

The most painful network outages often come from a lack of design, not from advanced technology.

A bad pattern:

```text
Plug in a router.
Add a switch.
Run out of ports.
Add another switch.
Daisy-chain more switches.
Hope nothing breaks.
```

At first, this works. Later, the network becomes part of the business, and the random layout becomes a problem.

### SOHO Model

SOHO means:

```text
Small Office, Home Office
```

A typical SOHO network:

- router;
- one switch;
- maybe a wireless access point;
- a few end devices.

For a tiny coffee shop, home office or temporary network, this can be fine.

The problem starts when the network grows:

- more computers;
- IP phones;
- printers;
- cameras;
- access points;
- servers;
- payment systems;
- coffee roasting equipment.

If you keep adding switches one after another, you create a fragile daisy-chain.

### Daisy-Chain Risk

A daisy-chain looks something like this:

```text
Router -> Switch 1 -> Switch 2 -> Switch 3 -> Switch 4
```

Problems:

- one failed switch can cut off everything downstream;
- one unplugged cable can stop a whole business area;
- the traffic path becomes unclear;
- troubleshooting gets harder;
- redundancy is almost nonexistent.

For a home network, this may be tolerable. For a business, it is risky.

### Three-Tier Architecture

Three-tier architecture divides the network into three layers:

1. Access layer.
2. Distribution layer.
3. Core layer.

Each layer has a role. That makes the network easier to understand, scale and protect.

### Access Layer

The access layer is where devices access the network.

Devices here include:

- user computers;
- printers;
- IP phones;
- wireless access points;
- cameras;
- point-of-sale terminals;
- other end devices.

Simple idea:

```text
End devices plug into the access layer.
```

This is the layer closest to users.

### Distribution Layer

The distribution layer is the consolidation point for access switches.

Access switches should not randomly connect to each other. They connect upward to the distribution layer.

The distribution layer often handles:

- aggregation of access switches;
- policy boundaries;
- routing between VLANs;
- redundancy;
- connection to shared services;
- summarization or control points in larger designs.

In the study example, important shared services can live here:

- DNS;
- DHCP;
- internal servers.

### Redundancy at Distribution

A strong three-tier or two-tier design idea:

```text
Each access switch connects to both distribution switches.
```

That provides redundancy.

If one distribution switch fails, the access layer still has a path through the second distribution switch.

That is much better than a single chain of switches.

### Core Layer

The core layer matters when the network becomes campus-scale.

Imagine several buildings:

- Building A;
- Building B;
- Building C;
- Building D.

If every building connects directly to every other building, you get a full-mesh nightmare.

Bad growth example:

```text
A connects to B, C, D
B connects to A, C, D
C connects to A, B, D
D connects to A, B, C
```

The more buildings you add, the more complex the topology becomes.

The core layer solves this:

```text
All buildings connect to the core.
Core carries traffic between buildings.
```

The core should be fast, reliable and simple. Its job is transport between major network blocks.

### Two-Tier / Collapsed Core

Not every network needs a separate core.

For one or two buildings, two-tier design is often enough:

```text
Access layer + Distribution layer
```

This is also called:

```text
Collapsed core
```

Core functions are collapsed into distribution.

This design is simpler, cheaper and appropriate for smaller campus environments.

### When to Use Three Tiers

Simple rule:

| Environment | Recommended Design |
| --- | --- |
| Home or tiny office | SOHO |
| One or two buildings | Two-tier / collapsed core |
| Three or more buildings | Three-tier architecture |
| Data center with many servers | Spine-leaf |

This is not an absolute law, but it is a useful mental model.

### Spine and Leaf

Spine-leaf is another architecture, usually used in the data center.

Data centers have lots of:

- servers;
- racks;
- east-west traffic;
- redundant paths;
- high bandwidth needs.

Leaf switches connect to servers and spine switches. Spine switches connect the leaf layer together.

The idea is similar to collapsed core in some ways, but optimized for massive compute environments.

NetworkChuck Coffee is not there yet, but it is useful to know this architecture exists.

### NetworkChuck Coffee Example

At first, Harvey may start with SOHO:

```text
Router -> Switch -> AP and devices
```

When roasters, IP phones, staff computers, POS terminals and servers appear, the network needs more structure.

A better design:

```text
End devices -> Access switches -> Distribution switches -> Core if needed
```

This makes it easier to:

- scale;
- add new devices;
- troubleshoot outages;
- document the topology;
- avoid single points of failure;
- connect new buildings.

### Main Takeaway

Do not just plug devices together until the network "sort of works."

Better mindset:

```text
Design first.
Then connect.
Then configure.
Then troubleshoot from a known structure.
```

Three-tier architecture gives you a framework for building network infrastructure intentionally.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Network design model | Framework for structuring a network before devices are connected. |
| SOHO | Small Office, Home Office; simple small-network model. |
| Daisy-chain | Connecting switches one after another in a chain, often creating fragile paths. |
| Three-tier architecture | Design model with access, distribution and core layers. |
| Access layer | Layer where end devices connect to the network. |
| Distribution layer | Aggregation layer for access switches; often provides policy, routing and redundancy. |
| Core layer | High-speed layer connecting major network blocks or buildings. |
| Redundancy | Extra path or device that keeps service working if one component fails. |
| Collapsed core | Two-tier design where core functions are combined with distribution. |
| Campus network | Network connecting multiple areas or buildings in one organization/location. |
| Full mesh | Topology where every node connects directly to every other node. |
| Spine-leaf | Data center architecture with leaf switches connected to spine switches. |
| Single point of failure | Component whose failure can break a larger part of the network. |

## Questions

### 1. Why does randomly connecting switches become a problem?

Because the network becomes fragile, poorly documented and hard to troubleshoot.

### 2. What is the SOHO model?

Small Office, Home Office model: a simple network with a router, switch, maybe an AP and a small number of devices.

### 3. When does the SOHO model stop being enough?

When the business depends on the network and many devices, services, payment systems or multiple switches appear.

### 4. Which three layers exist in three-tier architecture?

Access, Distribution and Core.

### 5. What connects to the access layer?

End devices: computers, printers, IP phones, APs, cameras and POS terminals.

### 6. What role does the distribution layer perform?

It aggregates access switches and provides redundancy, policy/routing boundaries and connection to shared services.

### 7. Why connect an access switch to two distribution switches?

To provide redundancy: if one distribution switch fails, a second path remains.

### 8. Why is the core layer needed?

To cleanly and scalably connect multiple buildings or major network blocks.

### 9. What is collapsed core?

A two-tier design where core functions are combined with the distribution layer.

### 10. When is two-tier design usually used?

For one or two buildings where a separate core is not needed yet.

### 11. When should you move toward three-tier design?

When the network connects three or more buildings or becomes campus-scale.

### 12. Where is spine-leaf architecture usually used?

In data centers with many servers, racks, redundant paths and high bandwidth needs.

## What To Review Later

- SOHO vs business network design.
- Access layer role.
- Distribution layer role.
- Core layer role.
- Redundancy between access and distribution.
- Two-tier / collapsed core.
- Three-tier campus design.
- Full mesh problem between buildings.
- Spine-leaf basics.
