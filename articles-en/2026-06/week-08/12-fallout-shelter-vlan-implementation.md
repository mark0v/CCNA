# Fallout Shelter VLAN Implementation

Source: closed course page  
Date added: 2026-06-20  
Related plan item: Week 8 / Fallout Shelter VLAN implementation  
Tags: VLAN, subnetting, VTP, DTP, router-on-a-stick, DHCP, STP, segmentation
Language: English
Translation pair: articles/2026-06/week-08/12-fallout-shelter-vlan-implementation.md

## Summary

VLAN implementation is not a small switch config tweak.

When you deploy a VLAN architecture, you also change:

- logical network structure;
- IP addressing;
- subnets;
- default gateways;
- DHCP scopes;
- traffic paths;
- routing behavior;
- security boundaries;
- troubleshooting model.

For the Fallout Shelter network, the task came from the RFP, Request for Proposal. The business language did not say "create VLANs," but the requirements already defined the VLAN design.

Four isolated network segments were required:

- management traffic;
- internal communication;
- video surveillance;
- guest access.

That immediately becomes:

```text
Four segments
Four VLANs
Four subnets
Four gateways
Four DHCP scopes
```

## VLANs Are A Redesign

The phrase "implement VLANs" can sound like a small configuration change.

In reality, it is a redesign.

Why:

- every VLAN is a separate broadcast domain;
- every VLAN usually gets a separate IP subnet;
- every subnet needs a default gateway;
- DHCP must hand out addresses from the right pool;
- routing must know all networks;
- security policies must account for new boundaries;
- switch ports must be assigned to correct VLANs;
- trunk links must carry the required VLANs.

If only part of the work is done, the network may look configured but behave unreliably.

## Original Address Block

The Fallout Shelter had a larger assigned subnet:

```text
10.0.16.0/23
```

One `/23` provides a large address block, but the business requirement was not one flat network. It required four separated segments.

So the `/23` was split into four `/25` subnets.

Why `/25`?

A `/23` contains 512 total addresses.

Splitting it into four equal pieces gives:

```text
/23 -> four /25 networks
```

Each `/25` provides:

```text
128 total addresses
126 usable host addresses
```

For a shelter with around 50 people, that is enough room with plenty of reserve.

## VLAN And Subnet Mapping

Logical plan:

```text
VLAN 10 -> Management
VLAN 20 -> Internal users
VLAN 30 -> Video surveillance
VLAN 40 -> Guest access
```

Addressing idea:

```text
10.0.16.0/25    -> VLAN 10 Management
10.0.16.128/25  -> VLAN 20 Internal
10.0.17.0/25    -> VLAN 30 Video
10.0.17.128/25  -> VLAN 40 Guest
```

This keeps the shelter-wide `/23` inside the larger address plan while turning it into four useful networks.

Numbering VLANs by tens also helps:

```text
10, 20, 30, 40
```

If another related VLAN is needed later, there is room:

```text
11, 12, 21, 31
```

This is not a strict rule, just a useful operational habit.

## Management VLAN

A management VLAN is the network for administrative access to infrastructure devices.

Examples:

- SSH to switches;
- SSH to routers;
- web interfaces;
- monitoring;
- device management;
- controller communication.

Management traffic should be separated from normal user traffic.

If normal user devices can directly reach management interfaces on switches and routers, the attack surface becomes much larger.

Correct mindset:

```text
Being plugged into the building should not mean being able to manage infrastructure.
```

The management VLAN should be restricted and accessible only to administrators or trusted management systems.

## Segment By Risk, Not Only By Department

VLAN design is often explained through departments:

```text
Accounting VLAN
Sales VLAN
Engineering VLAN
```

But in production, it is useful to think more broadly: segment by risk.

Question:

```text
Which systems should never be casually reachable from normal user devices?
```

That question leads to better segmentation:

- management separated;
- guest separated;
- video surveillance separated;
- internal users separated;
- payment systems separated, if present;
- servers separated, if the design requires it.

## VTP In The Lab

This lesson used VTP, VLAN Trunking Protocol, to replicate VLAN information between switches.

Important:

```text
VTP does not create trunk links.
VTP shares VLAN database information over trunk links.
```

So trunk links must work first, and then VLAN database information can propagate through VTP.

Lab flow:

1. Create VLANs on one switch.
2. Configure switch-to-switch links as trunks.
3. Make sure VTP domain/mode allow propagation.
4. Verify that VLANs appear on other switches.

## DTP And Trunks

DTP, Dynamic Trunking Protocol, can help ports negotiate trunk mode.

In the lab, links were in dynamic auto.

If both sides are dynamic auto, the trunk does not form:

```text
auto + auto -> no trunk
```

When uplinks were changed to dynamic desirable, trunk links came up:

```text
desirable + auto -> trunk
```

This is useful for understanding DTP behavior.

But in production, it is usually better to configure trunks explicitly:

```text
switchport mode trunk
```

and avoid relying on negotiation without a reason.

## VTP Risk

VTP is convenient because the VLAN database can be created once and replicated to switches.

But the same mechanism can replicate a mistake.

If a VLAN is deleted on a VTP server, that deletion can propagate across the domain.

Consequences:

- VLAN disappears on other switches;
- access ports lose the expected VLAN;
- users/devices lose connectivity;
- troubleshooting becomes painful.

So modern best practice is often:

```text
Use VTP transparent
or avoid VTP unless intentionally designed
```

In the lab, VTP is useful as a teaching demonstration. In production, use it very carefully.

## Access Ports

After VLANs appeared on the switches, end-device ports were assigned to the right VLANs.

An access port belongs to one VLAN.

For example:

```text
PC in Management -> access VLAN 10
Internal user PC -> access VLAN 20
Camera device    -> access VLAN 30
Guest device     -> access VLAN 40
```

Example command:

```text
interface fastEthernet0/5
 switchport mode access
 switchport access vlan 20
```

That turns the design into real Layer 2 membership.

## Router-On-A-Stick

After segmentation, the next question is:

```text
How do these separate networks talk to each other?
```

Answer: inter-VLAN routing.

This implementation used router-on-a-stick.

One physical router interface connects to the switch through a trunk.

Router subinterfaces are created:

```text
G0/0.10 -> VLAN 10
G0/0.20 -> VLAN 20
G0/0.30 -> VLAN 30
G0/0.40 -> VLAN 40
```

Every subinterface receives:

- `encapsulation dot1Q <vlan-id>`;
- an IP address from the corresponding subnet;
- the default gateway role for its VLAN.

Example:

```text
interface g0/0.10
 encapsulation dot1Q 10
 ip address 10.0.16.1 255.255.255.128
```

## DHCP Scopes

Every VLAN needs its own DHCP scope.

Otherwise, devices will not receive the correct:

- IP address;
- subnet mask;
- default gateway;
- DNS server.

Example structure:

```text
DHCP pool MGMT   -> VLAN 10 subnet
DHCP pool USERS  -> VLAN 20 subnet
DHCP pool VIDEO  -> VLAN 30 subnet
DHCP pool GUEST  -> VLAN 40 subnet
```

Each pool must point to the default router for its VLAN.

## Router-Facing Switch Port Must Be Trunk

A common mistake: router subinterfaces are configured, DHCP pools exist, VLANs exist, but the switch port facing the router is not a trunk.

Then the router expects tagged VLAN traffic, but the switch does not send traffic that way.

Symptoms:

- DHCP does not work;
- clients may receive `169.254.x.x`;
- subinterfaces look configured, but traffic does not reach them.

Fix:

```text
interface gigabitEthernet0/1
 switchport mode trunk
```

After that, DHCP bindings appeared, clients received addresses from the correct subnets, and inter-VLAN communication worked.

## Verification

A working implementation must be proven with tests.

Verify:

- VLANs exist on switches;
- trunks are up;
- required VLANs are allowed on trunks;
- access ports are in the correct VLANs;
- router subinterfaces are up/up;
- DHCP bindings appear;
- clients receive correct IP/subnet/gateway;
- ping works where routing should allow traffic;
- ping fails where segmentation should block traffic;
- traceroute shows the expected router path.

Useful commands:

```text
show vlan
show interfaces trunk
show ip interface brief
show ip dhcp binding
show running-config interface ...
```

## STP Already Shows The Next Problem

By the end of the implementation, the segmented LAN worked.

But redundant links in the switching design began showing STP behavior.

STP, Spanning Tree Protocol, prevents Layer 2 loops by blocking extra paths.

That is good for safety.

But default STP choices are not always optimal.

The network can function correctly but not perfectly:

- some links are blocked;
- traffic paths may be awkward;
- redundancy exists but is not used as desired;
- root bridge placement may not be intentional.

That creates the next stage: Layer 2 optimization.

## What Was Built

By the end of the implementation:

- one `/23` was split into four `/25`s;
- four VLANs were created;
- the VLAN database replicated across the switching environment;
- ports were assigned as access ports for test endpoints;
- trunks were brought up between switches;
- router-on-a-stick provided inter-VLAN routing;
- DHCP scopes handed out addresses automatically;
- pings confirmed connectivity;
- STP showed that the topology works but needs optimization.

This is no longer "create a VLAN." It is a complete network redesign.

## Main Takeaway

VLANs are not a small change.

One new VLAN means:

- new broadcast domain;
- new subnet;
- new gateway;
- new DHCP scope;
- new routing consideration;
- new security boundary;
- new troubleshooting path.

In the Fallout Shelter, we built a working segmented LAN. The network is now more organized and secure, but the next question is already visible: how do we make Layer 2 redundancy not only safe, but intentional and efficient?

That leads into the next topics: STP behavior, STP tuning, EtherChannel and more mature switching design.

