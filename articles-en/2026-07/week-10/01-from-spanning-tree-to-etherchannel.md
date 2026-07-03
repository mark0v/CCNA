# From Spanning Tree To EtherChannel

Source: closed course page  
Date added: 2026-07-03  
Related plan item: Week 10 / From Spanning Tree to EtherChannel  
Tags: STP, Rapid STP, VLAN, trunk, EtherChannel, link aggregation, redundancy
Language: English
Translation pair: articles/2026-07/week-10/01-from-spanning-tree-to-etherchannel.md

## Summary

- Spanning Tree protects the network from loops, but that protection has a cost: redundant links are often blocked.
- In a real network, STP must be implemented consistently across every switch.
- Cheap unmanaged switches are dangerous because they often do not participate in STP and cannot stop a Layer 2 loop.
- The next topic is EtherChannel: a way to combine multiple physical links into one logical connection.

## Key Points

- STP prevents broadcast storms, but it does not increase the usable bandwidth of redundant links.
- Rapid PVST+ should be enabled consistently on all Cisco switches in the same switching domain.
- Root bridge placement, trunk VLAN lists, native VLANs, and port modes must be verified during an STP rollout.
- An unmanaged switch without STP can create a loop with one badly placed cable.
- EtherChannel keeps redundancy while allowing multiple physical links to carry traffic as one logical connection.

## Notes

The Spanning Tree section covered a lot of Layer 2 ground: base configuration, Rapid STP, VLANs, trunks, and a live troubleshooting scenario where missing trunks and VLAN mismatches broke the expected topology. The main lesson is simple: it is not enough to understand STP. You must deploy it consistently.

If the core switches are running Rapid PVST+ but an edge switch is still using classic STP, the network may still pass traffic. The problem shows up during failure or troubleshooting: different timers, slower convergence, unexpected port states, and more confusion when you need clarity.

A practical STP rollout should be boring and repeatable:

- choose the STP mode;
- enable it on every switch;
- explicitly configure primary and secondary root bridges;
- verify trunk ports and allowed VLAN lists;
- enable PortFast and BPDU Guard on access ports;
- document the result.

One practical reason to buy enterprise-grade switches is STP support. A cheap unmanaged switch may seem like an easy way to add a few ports under a desk, but it does not understand BPDUs and cannot protect the network from a loop. One cable in the wrong place can create a broadcast storm and take down the segment.

If a network audit finds switches without active STP, document the risk immediately. Even if nothing has failed yet, the loop risk already exists. In production environments, that risk needs to be visible and written down.

STP still leaves one problem unsolved. Its basic logic is to block a redundant path so the Layer 2 topology stays loop-free. That is good for reliability, but it is inefficient. The physical cable exists, the port exists, and the bandwidth exists, but user traffic does not use that blocked link.

This is where EtherChannel comes in. EtherChannel takes multiple physical connections between switches and presents them as one logical link. STP sees the bundle as a single link, so it does not block individual cables inside the bundle as separate redundant paths.

The result is more usable bandwidth, retained redundancy, and a cleaner Layer 2 topology.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| STP | A protocol that prevents Layer 2 loops by blocking redundant paths. |
| Rapid PVST+ | Cisco's Rapid Spanning Tree implementation with a separate STP instance per VLAN. |
| Broadcast storm | A condition where broadcast frames loop endlessly and overwhelm the network. |
| Unmanaged switch | A switch without full management features, often missing STP and safety controls. |
| EtherChannel | A feature that combines multiple physical links into one logical channel. |
| Link aggregation | The general approach of making several physical connections operate as one logical link. |

## Questions

### 1. Why should STP be configured consistently across all switches?

Answer: Mixing STP modes and settings makes convergence and troubleshooting harder. The network may work normally, but failure behavior becomes less predictable.

### 2. Why is a cheap unmanaged switch risky in an enterprise network?

Answer: It may not support STP or process BPDUs. If it creates a Layer 2 loop, it cannot stop the resulting broadcast storm.

### 3. What problem does STP leave unsolved?

Answer: STP preserves a redundant link for failover, but often blocks it for normal traffic. That means part of the physical bandwidth sits unused.

### 4. What does EtherChannel change?

Answer: EtherChannel combines multiple physical links into one logical channel. STP sees the bundle as one link, while the network gets both redundancy and additional usable bandwidth.

## What To Review Later

- The difference between STP, RSTP, PVST+, and Rapid PVST+.
- How to verify trunk VLAN lists before making STP changes.
- Why BPDU Guard and PortFast are enabled together on access ports.
- Which port settings must match before configuring EtherChannel.
