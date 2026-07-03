# EtherChannel Deployment Checklist

Source: closed course page  
Date added: 2026-07-03  
Related plan item: Week 10 / EtherChannel deployment checklist  
Tags: EtherChannel, LACP, port-channel, STP, trunk, VLAN, load balancing
Language: English
Translation pair: articles/2026-07/week-10/06-etherchannel-deployment-checklist.md

## Summary

- EtherChannel turns redundant links from passive backup paths into active usable bandwidth.
- Before building the bundle, verify that member interfaces match completely.
- In production, LACP `active` on both sides is usually the clean choice.
- After configuration, verify EtherChannel, STP, and load balancing behavior.

## Key Points

- STP blocks extra links because it protects the network from loops, not because it is broken.
- EtherChannel works with STP by turning several physical links into one logical Port-Channel.
- Member ports must match speed, duplex, trunking, and VLAN settings.
- `channel-group 1 mode active` creates an LACP-based bundle.
- `show etherchannel summary` and `show spanning-tree` confirm that the bundle works and appears to STP as one interface.

## Notes

Redundant links are useful until STP blocks one of them. But STP is doing the right thing: its job is not maximum bandwidth, it is a loop-free Layer 2 topology. If two independent links between the same switches forward at the same time, they can create a loop and a broadcast storm.

EtherChannel solves that practical problem. It combines several physical interfaces into one logical connection: a Port-Channel. To STP, this is no longer two competing paths. It is one logical interface. The bundle can forward as a single unit, while the physical member links remain active inside it.

Main idea:

> One blocked link is safe. One bundled link is safe and useful.

Do not jump straight to `channel-group` before configuring EtherChannel. First, make sure the future member ports really match. Most EtherChannel problems do not start with LACP itself. They start because the interfaces are not actually twins.

Check:

- speed;
- duplex;
- trunk or access mode;
- allowed VLAN list;
- native VLAN;
- negotiation settings;
- old channel/protocol remnants;
- the same Layer 2 purpose on both sides.

Pay special attention to trunk behavior. If one member port carries VLAN 10,20,30 and another carries only VLAN 10, the bundle can become a source of strange behavior. EtherChannel requires consistency.

Working deployment flow:

1. Verify interfaces on both sides.

```text
Switch# show interfaces trunk
Switch# show running-config interface fa0/1
Switch# show running-config interface fa0/2
```

2. Configure member ports with an interface range.

```text
Switch(config)# interface range fa0/1 - 2
Switch(config-if-range)# channel-group 1 mode active
```

3. Repeat the matching configuration on the other side.

```text
Switch(config)# interface range fa0/1 - 2
Switch(config-if-range)# channel-group 1 mode active
```

4. Configure trunking and VLANs on the Port-Channel interface.

```text
Switch(config)# interface port-channel 1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20,30
```

5. Verify EtherChannel.

```text
Switch# show etherchannel summary
```

6. Verify STP.

```text
Switch# show spanning-tree
```

Before EtherChannel, STP saw separate physical interfaces and could block one of them. After the bundle is created, STP should see `Port-channel1` as one logical interface.

If the EtherChannel initially shows a standalone state, that is not always a problem. Often it means the other side is not configured yet. When the matching configuration appears on the other side, LACP forms the bundle and the member ports become active participants.

After basic verification, check the load balancing method:

```text
Switch# show etherchannel load-balance
```

If the switch uses source MAC only, distribution can be lopsided. In a network where many clients talk to different servers, an option like source-destination MAC may produce a more useful hash:

```text
Switch(config)# port-channel load-balance src-dst-mac
```

Remember: EtherChannel does not split one conversation packet by packet across all links. That would create out-of-order packets. Instead, the switch hashes flows: one conversation usually stays on one member link, while many conversations are distributed across the bundle.

At NetworkChuck Coffee, this matters because traffic is varied: POS systems, guest Wi-Fi, cameras, printers, office laptops, and back-office systems. The more different source/destination pairs exist, the better chance load balancing has to be effective.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `channel-group 1 mode active` | Adds interfaces to group 1 using LACP active mode. |
| `interface port-channel 1` | Opens the logical interface that represents the EtherChannel bundle. |
| `show etherchannel summary` | Checks the group, protocol, Port-Channel state, and active member ports. |
| `show spanning-tree` | Shows whether STP sees the Port-Channel as one logical interface. |
| `show etherchannel load-balance` | Shows the current load balancing method. |
| `port-channel load-balance src-dst-mac` | Configures hashing based on source and destination MAC addresses. |
| Standalone state | A state where the Port-Channel has not formed with the other side yet. |

## Questions

### 1. Why does EtherChannel not replace STP?

Answer: EtherChannel turns several physical links into one logical interface, but STP is still needed for loop prevention across the overall Layer 2 topology.

### 2. What should be checked before creating EtherChannel?

Answer: Speed, duplex, trunk/access mode, allowed VLANs, native VLAN, and negotiation settings on all member interfaces and on both sides.

### 3. Why use LACP active?

Answer: LACP is a standards-based negotiated protocol, and `active` explicitly attempts to form the channel. Using `active` on both sides reduces extra decision points.

### 4. What should change in STP output after EtherChannel is created?

Answer: STP should see the Port-Channel as one logical interface instead of several separate physical links.

### 5. Why can load balancing be uneven?

Answer: EtherChannel uses hash-based flow distribution. If the selected fields do not vary much between flows, a lot of traffic can land on one member link.

## What To Review Later

- How to read `show etherchannel summary`.
- Why trunk settings should be maintained on the Port-Channel interface.
- Which LACP states appear when a bundle has problems.
- How to choose a load balancing algorithm for a traffic pattern.
