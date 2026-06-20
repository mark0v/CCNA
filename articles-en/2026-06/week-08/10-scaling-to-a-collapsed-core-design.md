# Scaling To A Collapsed Core Design

Source: closed course page  
Date added: 2026-06-20  
Related plan item: Week 8 / Scaling the lab topology  
Tags: collapsed core, access layer, distribution layer, STP, HSRP, redundancy, Packet Tracer
Language: English
Translation pair: articles/2026-06/week-08/10-scaling-to-a-collapsed-core-design.md

## Summary

A small cafe network is great for early labs. A few switches and a router are enough to understand VLANs, trunks and basic routing logic.

But for more serious topics, that network is too small. It does not force you to think about:

- redundancy;
- failure impact;
- access and distribution layers;
- STP behavior;
- gateway resilience;
- design trade-offs;
- network growth;
- downstream locations.

So the lab expands to the Fallout Shelter network - a larger environment where design choices start to have real consequences.

Main shift:

```text
Small network teaches features.
Larger network teaches consequences.
```

## Why The Small Network Is Not Enough Anymore

A SOHO network, meaning small office/home office, can be simple:

```text
Router
Two switches
Several clients
Basic VLANs
Basic routing
```

That is enough for the first lessons.

But when VLANs, redundancy, STP, HSRP and more serious switching design appear, a tiny topology hides why these technologies matter.

If the network has only one switch path and one router path, you do not feel:

- what happens when a switch fails;
- what happens when a router fails;
- why loop prevention matters;
- why redundant links can be blocked;
- why gateway failover matters to users;
- why a traffic path may be non-optimal.

A larger topology makes those questions visible.

## Fallout Shelter As A More Realistic Environment

The Fallout Shelter network supports around 50 people and many downstream locations.

This is no longer just "one small office."

If that site fails, the impact can affect:

- connected shops;
- services;
- business operations;
- users in several locations;
- communication paths;
- access to shared resources.

Here, network failure becomes a business problem.

So the design must account not only for user count, but also:

- physical layout;
- business criticality;
- growth;
- redundancy;
- operational support;
- future services.

## From "Connect Devices" To Architecture

In the cafe network, the focus was mostly on features.

In the Fallout Shelter network, it is time to think more like network architecture.

The design becomes more structured:

- access switches;
- distribution switches;
- redundant links;
- routers;
- future VLAN segmentation;
- future HSRP;
- STP behavior.

This is not necessarily a huge enterprise network, but it already looks like a real design rather than just a teaching set of devices.

## Collapsed Core Design

A collapsed core design combines core and distribution responsibilities into one layer.

In the classic three-tier model, there are:

```text
Access layer
Distribution layer
Core layer
```

In a collapsed core:

```text
Access layer
Collapsed core / distribution layer
```

There is no separate core layer. Distribution switches also perform core-like forwarding inside the site.

This design often fits:

- a single building;
- a medium office;
- a campus building;
- a smaller enterprise site;
- environments where a separate core layer would be overkill.

## Access Layer

The access layer is where endpoints connect.

Examples:

- PCs;
- laptops;
- printers;
- cameras;
- access points;
- phones;
- POS terminals;
- IoT devices.

Access switches are closest to users and devices.

This is where you commonly configure:

- access ports;
- VLAN assignment;
- port security;
- edge STP features;
- voice VLAN;
- endpoint-facing policies.

## Distribution Layer

The distribution layer aggregates access switches.

This is where more serious responsibilities appear:

- aggregating access switches;
- routing boundaries;
- policy enforcement;
- VLAN boundaries;
- uplinks toward routers/services;
- redundant paths;
- gateway services;
- traffic control.

In a collapsed core design, the distribution layer also acts as the local core for the site.

## Why The Design May Look "Too Big"

If the environment supports around 50 people, the topology may look larger than expected.

But user count is not the only factor.

Design is also driven by:

- how many downstream locations depend on the site;
- how important uptime is;
- where devices are physically located;
- what growth is expected;
- which services will be added later;
- what failure impact is acceptable.

A small site can deserve serious redundancy if its outage affects many stores or key services.

## Redundant Links

In the topology, access switches connect to both distribution switches.

Routers are also connected redundantly.

Goal:

```text
If one switch fails, another path remains.
If one router fails, another path can take over.
```

This is not overkill when the site matters to the business.

Redundancy is there so one failed element does not immediately become an outage for everyone.

## Future HSRP

HSRP means Hot Standby Router Protocol.

It lets two routers appear to clients as one default gateway.

Idea:

```text
Router A active
Router B standby
Clients use virtual gateway IP
If Router A fails, Router B takes over
```

Users do not manually change their gateway. Devices continue using the same virtual default gateway.

HSRP becomes useful precisely in a topology with redundant routers.

## When A Separate Core Layer Is Needed

A collapsed core can scale quite far.

Depending on hardware and layout, it can support:

- hundreds of users;
- sometimes low thousands;
- one building;
- multiple floors;
- a medium site.

A separate core layer usually appears when multiple buildings or major campus blocks must be connected.

Example:

```text
Building A: 500 users
Building B: 200 users
Building C: 300 users
```

Then the core layer becomes the high-speed backbone between distribution blocks in different buildings.

## Addressing For The Fallout Shelter

The Fallout Shelter already has an assigned subnet:

```text
10.0.16.0/23
```

This is the address range for this environment.

At this stage, the goal is not to fully configure every VLAN and routing feature. The goal is to create the physical and logical foundation.

Later, this foundation will carry:

- VLANs;
- trunks;
- STP;
- HSRP;
- routing;
- switch optimization.

## Packet Tracer And Topology

The topology was added in Packet Tracer under the cafe network.

That makes it easier to:

- compare small and larger implementations;
- see both designs;
- move between them quickly;
- avoid complicating the lab with physical views;
- focus on network behavior.

Sometimes it is better to keep a lab visually simple when the goal is to understand design and protocols.

## Red Links

Red links on router interfaces in Packet Tracer usually mean the interfaces are shut down.

Router interfaces are often administratively down by default.

This is fixed later with:

```text
no shutdown
```

So red state does not always mean a complex problem. Often the interface simply has not been enabled yet.

## Orange Links And STP

Orange links in a switching topology often hint that Spanning Tree Protocol is already working.

STP prevents Layer 2 loops.

If a switching network has redundant physical links, without STP you can get:

- broadcast storms;
- duplicate frames;
- MAC table instability;
- network meltdown.

STP may block some links so the network does not create a loop.

Important:

```text
More cables does not automatically mean more active bandwidth.
```

If STP blocks a link, that link provides standby redundancy, not active forwarding.

## Why Default STP Can Be Inefficient

STP protects against loops, but default path selection is not always optimal.

The network may work, but traffic may take an awkward path:

- through an extra switch;
- over a less ideal uplink;
- through a less desirable distribution switch;
- because root bridge placement is not intentional.

That is why later topics matter:

- STP tuning;
- intentional root bridge selection;
- EtherChannel;
- VLAN-aware design;
- topology planning.

## Why Build The "Mess" First

It would be possible to build the ideal topology immediately and hide the messy parts.

But real networking often works differently:

1. Build a baseline.
2. Observe behavior.
3. Notice blocked links and strange paths.
4. Understand why the protocol chose that path.
5. Optimize the design.

That makes the learning more realistic.

Seeing imperfect behavior first helps explain why STP tuning, HSRP and switch optimization matter later.

## Main Takeaway

This lesson moves the lab from a tiny network into a topology that can support deeper CCNA topics.

The cafe network was good for basics.

The Fallout Shelter network is needed for:

- VLAN design in a larger environment;
- redundant switching paths;
- STP behavior;
- future HSRP;
- gateway resilience;
- collapsed core architecture;
- real design trade-offs.

In short:

```text
Small topology shows commands.
Larger topology shows consequences.
```

Now there is an environment where VLANs, STP, HSRP and switching optimization can appear not as separate topics, but as parts of one living network.

