# Redundant Switch Links And Broadcast Storms

Source: closed course page  
Date added: 2026-06-28  
Related plan item: Week 9 / Redundant switch links and broadcast storms  
Tags: STP, redundancy, broadcast storm, Layer 2, switching loop, TTL, BPDU
Language: English
Translation pair: articles/2026-06/week-09/04-redundant-switch-links-and-broadcast-storms.md

## Summary

Redundancy sounds like an obvious win: if one cable between switches fails, a second cable preserves connectivity.

But in a Layer 2 network, the second cable can take the network down instead of saving it.

The reason is a switching loop.

When two switches are connected by two ordinary Layer 2 links, a broadcast frame can begin circulating. One switch receives the broadcast and floods it through other ports, the second switch does the same, and the frame returns to the first switch.

That creates a broadcast storm.

Main idea:

```text
Redundant physical links are useful.
Uncontrolled Layer 2 loops are catastrophic.
STP is the control mechanism between those two facts.
```

## Why The Second Cable Is Not Always The Fix

Imagine a simple topology:

```text
SW1 ----- SW2
```

One cable connects two switches.

If that cable fails, devices on different switches lose connectivity. So the obvious thought is to add a second cable:

```text
SW1 ===== SW2
```

At the physical layer, this looks like better reliability.

At Layer 2, it is now a loop.

A frame can leave SW1 for SW2 on one link and return on the other. That is bad for unicast traffic, and especially dangerous for broadcast traffic.

## How Broadcast Becomes A Storm

A broadcast frame is sent to every device in one VLAN.

A common example is a DHCP request:

```text
Who can give me an IP address?
```

A switch receives that frame and performs normal Layer 2 behavior:

- receives the frame on one port;
- sends it out all other ports in the VLAN;
- does not send it back only on the port where it arrived.

If the topology has no loops, that is fine.

If there is a loop between switches, the problem begins:

1. A PC sends a broadcast to SW1.
2. SW1 floods the broadcast to SW2.
3. SW2 floods the broadcast back to SW1 through another link.
4. SW1 floods it again.
5. The process repeats without a normal ending.

The network does not merely become a little slower.

It can become unusable very quickly.

## Why Layer 3 Behaves Differently

A good question is: why do routing loops not behave endlessly the same way?

At Layer 3, an IP packet has TTL, Time To Live.

A packet often starts with a TTL such as `255`. Each router along the path decreases the TTL by `1`. When TTL reaches `0`, the packet is dropped.

That does not make routing loops good, but it limits the damage.

```text
Layer 3 packet:
TTL decreases at every router hop.
Eventually TTL reaches 0.
Packet is dropped.
```

Switching is different.

In classic Layer 2 forwarding, switches look at MAC addresses, not IP TTL. An Ethernet frame does not have that same hop countdown.

```text
Layer 2 frame:
No TTL.
No automatic hop countdown.
Loop can continue until topology changes or network fails.
```

That is why a Layer 2 loop is especially dangerous.

## What The User Sees

A broadcast storm can look like a sudden, strange outage.

Symptoms:

- the network suddenly becomes slow;
- DHCP stops handing out addresses reliably;
- pings drop;
- phones, cameras, POS terminals or workstations disconnect;
- switch CPU rises;
- MAC address tables start flapping;
- links are physically up, but traffic barely passes.

For a user, it simply looks like:

```text
The network is down.
```

For an engineer, it is a reason to look for a Layer 2 loop, extra cable, wrong trunk, disabled STP or incorrect STP topology.

## How STP Solves The Problem

Spanning Tree Protocol, STP, does not forbid redundancy.

It makes redundancy controlled.

STP looks at the topology, detects redundant paths and blocks the links or ports that are not currently needed for loop-free forwarding.

Important:

```text
Blocked does not mean removed.
Blocked means standby.
```

The cable remains physically connected.

If the active path fails, STP can recalculate the topology and open the backup path.

This gives the network two properties at the same time:

- protection from Layer 2 loops;
- redundancy for link failure.

## Why STP Needs Deeper Study

If STP simply blocks the extra link, why are there several lessons on it?

Because real networks rarely look like two switches and two cables.

An enterprise environment may have:

- 10 switches;
- 50 switches;
- 100 switches;
- access layer;
- distribution or collapsed core;
- multiple VLANs;
- multiple trunks;
- mixed link speeds;
- redundant uplinks;
- old and new switches in one topology.

STP must choose a loop-free path across that whole topology.

The technical truth is this: STP can choose a safe path without choosing the best path.

For example, it may leave an old slow link active and block a faster uplink if bridge priorities and path costs are left at defaults.

From STP's perspective, that may be a valid loop-free topology.

From a performance perspective, it is a poor design.

## What It Means To Manage STP

Understanding STP means more than knowing that it blocks loops.

You need to understand:

- how the root bridge is selected;
- why one port becomes a root port;
- why another port becomes designated;
- why a third port blocks;
- how path cost influences selection;
- how bridge priority changes root placement;
- how the topology reacts to failure.

That is not necessarily configuration yet.

First, it is a mental model.

You look at the topology and can say:

```text
This switch should be root.
This uplink should forward.
This backup link should block.
If the active link fails, this path should open.
```

That is engineer-level understanding.

## Real World Tip

A broadcast storm can happen from a brief mistake.

For example, someone accidentally plugs in an extra patch cable between two switches or connects two wall ports into one unmanaged switch under a desk.

If STP is enabled and working correctly, it should protect the network.

But convergence is not always instant, and misconfiguration can weaken protection.

Before adding new switch connections in production, verify:

- STP enabled;
- root bridge placement;
- port roles;
- trunk status;
- BPDU Guard and PortFast on edge ports;
- expected blocked links;
- documentation versus real cabling.

Do not add a redundant cable by guessing.

Understand what STP will do first.

## Verification Commands

Starter set:

```text
show spanning-tree
show spanning-tree vlan 10
show spanning-tree summary
show interfaces trunk
show mac address-table dynamic
```

Look for:

- who the root bridge is;
- which ports are forwarding;
- which ports are blocking;
- whether topology changes are frequent;
- whether the forwarding path matches the design;
- whether MAC addresses are flapping between ports.

If a MAC address rapidly appears on one port and then another, that can be a serious sign of a Layer 2 loop or incorrect topology.

## Main Takeaway

Redundancy alone does not make a switched network reliable.

Without loop prevention, it can destroy the network.

STP is needed so the second cable becomes a backup path instead of the source of a broadcast storm.

Short version:

```text
Redundant switch links create loops.
Loops create broadcast storms.
STP blocks redundant paths to keep the network alive.
```

Next, it is important to understand not only what STP blocks, but why it chooses that port, that path and that root bridge.

That turns STP from "magic that made the link orange" into a tool you can manage.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Switching loop | Layer 2 loop where frames can circulate endlessly between switches. |
| Broadcast storm | Overload caused by broadcast frames looping and multiplying through the network. |
| TTL | Time To Live. Layer 3 packet field decremented by routers to limit routing loops. |
| STP | Spanning Tree Protocol. Protocol that blocks redundant Layer 2 paths to prevent loops. |
| Blocked port | STP state where a port does not forward user traffic because forwarding would create a loop. |
| Convergence | Process of STP recalculating a loop-free topology after a change. |
| Root bridge | Reference switch used by STP to calculate the best forwarding paths. |

## Questions

### 1. Why can adding a second cable between switches break the network?

Answer:

Because two Layer 2 links between the same switching paths can create a loop. Broadcast frames can circulate endlessly and cause a broadcast storm.

### 2. Why does TTL not protect a Layer 2 switching loop?

Answer:

TTL is an IP Layer 3 field handled by routers. Layer 2 switches forward Ethernet frames based on MAC addresses and do not decrement IP TTL during normal switching.

### 3. What does STP do with redundant links?

Answer:

STP blocks redundant paths that would create loops, while keeping them available as standby paths if the active link fails.

## What To Review Later

- Root bridge election.
- STP port roles.
- STP port states.
- Path cost and bridge priority.
- PortFast and BPDU Guard.
- EtherChannel for using multiple physical links without STP blocking each one separately.
