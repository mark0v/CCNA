# Spanning Tree Implementation Checklist

Source: closed course page  
Date added: 2026-06-28  
Related plan item: Week 9 / Spanning Tree rollout checklist  
Tags: STP, Rapid PVST, root bridge, trunk, VLAN, PortFast, BPDU Guard, checklist
Language: English
Translation pair: articles/2026-06/week-09/10-spanning-tree-implementation-checklist.md

## Summary

A Spanning Tree rollout should not begin with random command entry.

If you enable STP features without a checklist, you can end up with a strange topology, the wrong root bridge, inconsistent trunks or even a Layer 2 loop.

Working order:

```text
1. Enable Rapid PVST+ everywhere.
2. Choose root and secondary root bridges.
3. Verify consistent VLANs and trunks.
4. Enable PortFast and BPDU Guard on access ports.
5. Verify, fix, and save.
```

This is not just a lab routine. It is production thinking: design first, configure second, verify third.

## Why A Checklist Matters

STP configuration touches the whole switching topology.

One missed command can look small, but the consequences can be large:

- one switch remains in classic STP mode;
- the root bridge is selected by lowest MAC address;
- a trunk does not carry the required VLAN;
- an access port without BPDU Guard accepts a loop;
- the configuration is not saved after successful verification.

STP must be consistent.

Especially when the network has multiple switches, multiple VLANs and redundant links.

## Step 1: Enable Rapid PVST+ Everywhere

On Cisco switches, classic STP can work, but it is slow.

For a modern Cisco environment, the expected baseline is often:

```text
spanning-tree mode rapid-pvst
```

Enable it on every switch.

Not only on the core.

Not only on the switch you are touching right now.

Check the Cafe switches, Fallout Shelter switches and any other switches in the same Layer 2 topology.

Verification:

```text
show spanning-tree summary
show running-config | include spanning-tree mode
```

If one switch remains in older behavior, convergence may be inconsistent and slow.

## Step 2: Choose The Root Bridge

The root bridge is the STP reference point.

Choose it from the topology, not from the MAC address.

Good questions:

- which switch is most central;
- where the uplinks concentrate;
- which switch is closest to the router or firewall;
- where the logical distribution point is;
- which switch should be the backup root.

For the Fallout Shelter example, Switch 1 is the root bridge because it is central and connected toward the routing side.

Primary root with explicit priority:

```text
spanning-tree vlan 1,10,20,30,40 priority 4096
```

Secondary root:

```text
spanning-tree vlan 1,10,20,30,40 priority 8192
```

Lower priority wins.

Cisco shortcut alternative:

```text
spanning-tree vlan 1,10,20,30,40 root primary
spanning-tree vlan 1,10,20,30,40 root secondary
```

Know both approaches.

Verification:

```text
show spanning-tree vlan 10
show spanning-tree vlan 20
show spanning-tree root
```

## Step 3: Verify VLANs And Trunks

This is a critical step.

Cisco PVST and Rapid PVST+ run a separate STP instance per VLAN.

If VLAN 1 looks good, that does not prove VLAN 10, 20, 30 and 40 are also good.

Trunk inconsistency can create strange STP behavior:

- one VLAN is missing on a trunk;
- a trunk is not enabled on one uplink;
- allowed VLAN lists do not match;
- STP topology for one VLAN differs from expected;
- two forwarding paths appear where you expected one blocked port.

Command:

```text
show interfaces trunk
```

Check:

- trunk mode;
- native VLAN;
- allowed VLANs;
- VLANs active in management domain;
- VLANs in spanning tree forwarding state and not pruned.

Also useful:

```text
show vlan brief
show running-config interface ...
```

Do not mark this step done until trunks are checked on both ends.

## Step 4: Enable PortFast And BPDU Guard On Access Ports

Access ports go to end devices:

- PCs;
- printers;
- POS terminals;
- cameras;
- phones;
- access points.

They usually need:

- PortFast for fast forwarding;
- BPDU Guard to protect against an accidental switch or loop.

Example for a range:

```text
interface range fa0/3-24
 switchport mode access
 spanning-tree portfast
 spanning-tree bpduguard enable
```

PortFast removes unnecessary listening and learning delay for end devices.

BPDU Guard moves a port into err-disabled state if an access port receives a BPDU.

This is the protection that helps against small unmanaged switches under desks.

Important: do not apply an access-port template to uplinks or trunks.

## Step 5: Verify And Save

After configuration, run a verification pass.

Minimum set:

```text
show spanning-tree
show spanning-tree vlan 10
show spanning-tree vlan 20
show spanning-tree summary
show interfaces trunk
show interfaces status
```

Check:

- the root bridge is the one expected;
- secondary root is configured;
- blocked ports make sense;
- root ports point toward the expected root;
- designated ports match the topology;
- trunks carry required VLANs;
- access ports have PortFast and BPDU Guard;
- there are no unexpected err-disabled ports.

If something looks strange, do not save blindly.

Fix it first.

After successful verification:

```text
copy running-config startup-config
```

Do this on every switch.

## Reading A Strange Topology

If STP output does not match expectations, use the familiar tiebreakers:

```text
1. Lowest cost to root.
2. Lowest bridge ID.
3. Lowest port number.
```

Example: if a link is running at 10 Mbps instead of 100 Mbps, the cost becomes worse. STP may block the port you expected to see forwarding.

So when the topology looks strange, check both STP and physical/interface details:

```text
show interfaces status
show interfaces counters errors
show running-config interface ...
```

## Rollout Checklist

Before changes:

- identify target switches;
- draw expected root and secondary root;
- define the VLAN list;
- identify trunk links;
- identify access port ranges;
- agree on a maintenance window if this is production.

During changes:

- enable Rapid PVST+ on all switches;
- configure root and secondary root;
- verify trunks and VLANs;
- apply PortFast and BPDU Guard on access ports;
- verify STP state.

After changes:

- save the config;
- update documentation;
- record actual blocked ports;
- check monitoring and logs;
- keep rollback notes.

## Main Takeaway

An STP rollout is not one command.

It is a sequence.

Remember:

```text
Mode first.
Root bridge second.
Trunks third.
Access protections fourth.
Verify and save last.
```

If you follow the checklist, the network gets loop prevention, fast convergence and predictable topology.

If you skip steps, STP will still choose something, but not necessarily what you wanted.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Rapid PVST+ | Cisco rapid per-VLAN STP mode. |
| Root bridge | STP reference switch that other switches calculate paths toward. |
| Secondary root | Planned backup root bridge if the primary root fails. |
| Trunk consistency | Matching trunk mode and allowed VLANs across both ends of a link. |
| PortFast | Feature that moves edge ports to forwarding quickly. |
| BPDU Guard | Protection that err-disables edge ports if they receive BPDUs. |
| Startup-config | Saved configuration that survives reload. |

## Questions

### 1. Why enable Rapid PVST+ on every switch?

Answer:

Because one switch left in classic STP behavior can still introduce slow convergence and inconsistent behavior in the Layer 2 topology.

### 2. Why verify trunks before trusting STP output?

Answer:

Because Rapid PVST+ runs per VLAN. A trunk that misses VLANs can make one VLAN look correct while another VLAN has broken or dangerous topology.

### 3. Why save after verification instead of immediately after typing commands?

Answer:

Because you should only preserve a configuration after confirming root bridge placement, trunk consistency, port roles, access protections and expected forwarding behavior.

## What To Review Later

- STP troubleshooting workflow.
- Root bridge tuning.
- Per-VLAN load balancing.
- Port cost and speed mismatches.
- Change-control checklist for Layer 2 rollouts.
