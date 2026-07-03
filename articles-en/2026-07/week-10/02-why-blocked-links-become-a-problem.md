# Why Blocked Links Become A Problem

Source: closed course page  
Date added: 2026-07-03  
Related plan item: Week 10 / Why blocked links become a problem  
Tags: STP, EtherChannel, redundancy, bandwidth, link aggregation, switch links
Language: English
Translation pair: articles/2026-07/week-10/02-why-blocked-links-become-a-problem.md

## Summary

- STP blocks extra Layer 2 paths so the network does not create a loop and a broadcast storm.
- That behavior is correct, but it turns some physical links into passive backup links.
- If two switches are connected with four cables, STP may leave only one active.
- EtherChannel is not a replacement for STP. It is a way to use redundant links safely.

## Key Points

- Uncontrolled redundancy creates Layer 2 loops.
- STP protects the network, but it does not try to use every available physical connection.
- A blocked link is useful for failover, but it does not help normal traffic until a failure happens.
- In real networks, this is especially visible on uplinks between access and distribution switches.
- EtherChannel turns several physical ports into one logical channel that STP sees as one path.

## Notes

STP is easy to appreciate because it protects the network from loops. When multiple independent Layer 2 paths exist between switches, the protocol chooses a safe topology and blocks the extra ports. That prevents a broadcast storm, where broadcast frames keep circulating until the segment is overwhelmed.

That solution has a cost. The physical cables are installed, the switch ports are used, and the hardware has been paid for, but some links do not carry normal user traffic. They exist as backup paths, but they do not help with everyday throughput.

Imagine two switches at NetworkChuck Coffee. They are connected with four links because we want redundancy and more capacity. From a human point of view, that makes sense. From STP's point of view, those are four potential paths that can create a loop. So STP leaves one forwarding path and blocks the others.

The network becomes safe, but inefficient:

- one active link carries POS traffic, cameras, Wi-Fi, voice, and back office systems;
- three other links wait for a failure;
- the available physical bandwidth is not fully used.

The wrong conclusion would be to blame STP. STP is not bad and it is not getting in the way. It is solving its job: removing Layer 2 loops. The limitation is that plain redundancy gives us backup capacity, but not always usable working bandwidth.

What we want sounds almost contradictory: multiple physical links between the same switches should behave like one logical link. Then the network gets both resilience and extra capacity, while STP does not see four separate redundant paths.

That is why EtherChannel exists. It combines several physical interfaces into one logical bundle. To STP, that bundle looks like one interface, so the protocol no longer blocks individual cables as separate duplicate paths.

The practical result:

- more usable bandwidth between switches;
- connectivity remains if one physical link in the bundle fails;
- the STP topology stays cleaner;
- less wasted bandwidth on important uplinks.

In production networks, EtherChannel is especially useful between access and distribution switches. For example, if an access switch serves wireless access points, POS terminals, and cameras, a single uplink can become a bottleneck. Multiple uplinks without EtherChannel will often be partially blocked by STP. Multiple uplinks with EtherChannel can work as one logical channel.

There is one important warning: EtherChannel requires matching settings on both sides. Speed, duplex, trunk/access mode, allowed VLANs, native VLAN, and negotiation mode must match. If one side is different, the bundle may fail to form or behave unpredictably.

At this stage, the main point is not the commands. The main point is the motivation. STP blocks redundant links for safety. EtherChannel lets us reclaim that bandwidth without bringing back the Layer 2 loop.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Blocked port | An STP port that does not forward user traffic because forwarding could create a loop. |
| Forwarding path | The active Layer 2 path that actually carries traffic. |
| Redundant link | An additional physical connection built for resiliency. |
| Logical link | A link that appears as one connection to the switch, even if multiple physical ports are inside it. |
| EtherChannel bundle | A group of physical interfaces combined into one logical channel. |
| Wasted bandwidth | Capacity that physically exists but is not used for normal traffic. |

## Questions

### 1. Why does STP block some redundant links?

Answer: Multiple independent Layer 2 paths between the same switches can create a loop. STP blocks the extra paths to prevent a broadcast storm.

### 2. Why is a blocked STP link still useful?

Answer: It remains available as a backup. If the active link fails, STP can reconverge and use the alternate path.

### 3. What is the practical problem with blocked links?

Answer: They do not carry normal user traffic. That means some of the installed physical bandwidth sits unused.

### 4. How does EtherChannel solve this problem?

Answer: EtherChannel combines multiple physical links into one logical bundle. STP sees the bundle as one link, while traffic can use the capacity of multiple physical connections.

## What To Review Later

- Why Layer 2 loops are more dangerous than just "an extra route".
- How STP chooses blocked and forwarding ports.
- Which settings must match on both sides of an EtherChannel.
- How EtherChannel differs from a normal set of redundant links.
