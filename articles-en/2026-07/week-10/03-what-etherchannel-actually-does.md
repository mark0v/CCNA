# What EtherChannel Actually Does

Source: closed course page  
Date added: 2026-07-03  
Related plan item: Week 10 / What EtherChannel actually does  
Tags: EtherChannel, LACP, PAgP, LAG, STP, link aggregation, load balancing
Language: English
Translation pair: articles/2026-07/week-10/03-what-etherchannel-actually-does.md

## Summary

- EtherChannel combines multiple physical links between the same devices into one logical channel.
- To STP, that bundle looks like one path, so individual member links are not blocked as separate redundant links.
- EtherChannel increases aggregate throughput, but it usually does not make one single flow faster than one member link.
- A channel can be built statically, with PAgP, or with LACP; real networks usually prefer LACP.

## Key Points

- EtherChannel is Cisco's name for link aggregation.
- In broader industry language, the common term is LAG, or Link Aggregation Group.
- A bundle can only combine links between the same pair of devices.
- One conversation usually stays on one physical link, while different conversations are distributed across member links.
- Speed, duplex, VLAN settings, and trunk/access mode must match on all member interfaces.

## Notes

Spanning Tree solves Layer 2 loops, but it does that in a blunt way: it sees multiple independent paths between switches and blocks the extras. Safe? Yes. Efficient? Not always. If two working uplinks exist between two switches, we want to use both, not stare at one blocked port.

EtherChannel solves that problem. It takes multiple physical interfaces between the same pair of devices and combines them into one logical link. To the switches, this is no longer a set of separate loop candidates. It is one channel. To STP, it is one logical path.

Separate the terms clearly:

- EtherChannel is the Cisco term;
- LAG, Link Aggregation Group, is the broader industry term;
- port-channel is the logical interface created by the bundle.

The main rule is that member links must connect the same pair of devices. You cannot take one port to Switch B and another port to Switch C and make a normal EtherChannel from them. The bundle works because both ends understand the same logical relationship.

If two 1 Gbps ports are bundled into an EtherChannel, the channel can provide 2 Gbps of aggregate bandwidth. If eight 10 Gbps ports are bundled, the total capacity becomes 80 Gbps. But there is an important catch: one single flow does not automatically become faster than one member link.

EtherChannel usually distributes traffic across member links with a load balancing algorithm. The algorithm may look at source/destination MAC addresses, source/destination IP addresses, TCP/UDP ports, or a combination of those fields depending on the platform and configuration. A conversation between Host A and Host B may use one physical link, while a conversation between Host C and Host D uses another.

Practical result:

- one large file transfer may still be limited to 1 Gbps on a bundle made of two 1 Gbps links;
- many simultaneous flows can be spread across multiple links;
- aggregate network throughput increases, even if each individual flow is not "merged" across cables.

This is not packet-level bonding. EtherChannel does not split one packet stream into fragments and reassemble it on the other side. It distributes conversations across links so the bundle as a whole can carry more traffic.

Common use cases include:

- switch-to-switch uplinks;
- server connections;
- wireless access point uplinks;
- storage or video systems where one interface can become a bottleneck;
- distribution/access designs that need both bandwidth and resilience.

At NetworkChuck Coffee, this could be the link between an access switch and a distribution switch. The access switch serves POS, Wi-Fi, cameras, and back office systems. One uplink can become a bottleneck, while multiple independent uplinks would be partially blocked by STP. EtherChannel allows those cables to operate as one logical uplink.

There are three ways to build EtherChannel:

| Method | Meaning |
| --- | --- |
| Static | Ports are manually forced into a bundle with no negotiation. |
| PAgP | Cisco-proprietary negotiation protocol for EtherChannel. |
| LACP | Industry-standard negotiation protocol for link aggregation. |

Static mode can look simple, but it carries more risk: if one side is misconfigured, negotiation will not stop the mistake. In production, LACP is usually preferred. It lets both sides agree on the bundle and prevents the channel from forming correctly when key settings do not match.

Consistency matters a lot with EtherChannel. Member interfaces should match on:

- speed;
- duplex;
- trunk or access mode;
- allowed VLAN list;
- native VLAN;
- negotiation mode;
- general Layer 2 parameters.

If one port differs, the bundle may fail to form, enter a suspended state, or behave unpredictably.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| EtherChannel | Cisco feature that combines multiple physical links into one logical channel. |
| LAG | Link Aggregation Group; the general term for link aggregation. |
| Port-channel | The logical interface that represents the EtherChannel bundle. |
| Member link | A physical interface that belongs to the EtherChannel. |
| LACP | Standards-based negotiation protocol for link aggregation. |
| PAgP | Cisco-proprietary negotiation protocol for EtherChannel. |
| Aggregate throughput | Total bundle capacity across many flows. |

## Questions

### 1. Why does EtherChannel help STP?

Answer: It turns multiple physical links into one logical link. STP sees one path instead of several separate redundant paths that need to be blocked.

### 2. Can you bundle ports that connect to different switches?

Answer: No, in a normal EtherChannel the member links must connect the same pair of devices. Otherwise, it is not one logical channel between two endpoints.

### 3. Will a two-link 1 Gbps EtherChannel give one file transfer 2 Gbps?

Answer: Usually no. One flow normally stays on one member link. EtherChannel increases aggregate throughput for many simultaneous flows.

### 4. Why is LACP usually better than static EtherChannel?

Answer: LACP negotiates and helps prevent a bundle from forming when settings do not match. Static mode does not verify agreement between the two sides as reliably.

## What To Review Later

- Which load balancing algorithms are available on a specific Cisco platform.
- The difference between `channel-group` and `interface port-channel`.
- LACP modes: active and passive.
- PAgP modes: desirable and auto.
