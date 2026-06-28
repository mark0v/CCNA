# Spanning Tree Vocabulary

Source: closed course page  
Date added: 2026-06-28  
Related plan item: Week 9 / Spanning Tree vocabulary and decision terms  
Tags: STP, root bridge, bridge ID, BPDU, port cost, root port, designated port, blocked port
Language: English
Translation pair: articles/2026-06/week-09/05-spanning-tree-vocabulary.md

## Summary

Spanning Tree Protocol solves a simple problem: keep redundancy and prevent broadcast storms.

The complexity is not the main idea. The complexity is how switches independently decide which link should forward traffic and which link should block.

STP uses a vocabulary for that decision process:

- root bridge;
- bridge ID;
- priority;
- MAC address;
- BPDU;
- port cost;
- root port;
- designated port;
- blocked port.

Once those words make sense, STP stops looking like magic. It becomes a sequence of decisions.

## Why Switches Need Rules

A person can look at a diagram and quickly say:

```text
There is the loop.
Block that link.
```

A switch does not think that way. It has no visual diagram and no human context.

Switches need formal rules:

- who the reference point is;
- which path is best;
- which port should forward;
- which port should block;
- what to do after a failure.

The first major STP question is:

```text
Who is the root bridge?
```

The answer controls the rest of the topology.

## Root Bridge

The root bridge is the switch STP chooses as the center of the Layer 2 topology.

Every other switch calculates its path to the root bridge and builds forwarding decisions around it.

Important: the root bridge is not a router and not a default gateway.

It is the STP reference point.

If the root bridge is chosen poorly, the forwarding topology can also be poor.

For example, if an old access switch accidentally becomes the root bridge, traffic may flow through inefficient links instead of through the core or distribution switch where you expected the central role.

A better design is usually:

```text
Core or distribution switch should be root bridge.
Random access switch should not be root bridge.
```

## Bridge ID

The root bridge is elected using the Bridge ID.

Bridge ID has two parts:

```text
Bridge ID = priority + MAC address
```

The lowest Bridge ID wins.

That means STP does not pick the newest switch, the fastest switch or the one with the best name.

It chooses the switch with the lowest Bridge ID.

## Priority

Priority is the first part of the Bridge ID.

The default priority is usually:

```text
32768
```

If all switches have the same priority, the election moves to the tiebreaker: MAC address.

To control root bridge election, an engineer changes the priority.

The rule is simple:

```text
Lower priority wins.
```

If the core switch should become the root bridge, set its priority lower than the other switches.

This is one of the most important STP design controls.

## Why The Default Root Can Be Strange

If all switches keep the default priority `32768`, the switch with the lowest MAC address wins.

A lower MAC address often means an older device.

That can feel strange: why might an older switch become root?

The reason is stability.

If every new switch automatically won the election, adding any new switch could suddenly rebuild the STP topology.

But that does not mean production networks should be left to chance.

Good practice:

```text
Do not let MAC address choose your root bridge.
Set the priority intentionally.
```

## BPDU

BPDU means Bridge Protocol Data Unit.

It is the STP control message switches exchange with each other.

With BPDUs, switches advertise:

- their Bridge ID;
- the root bridge they currently believe is best;
- their path cost to the root bridge;
- STP timing information;
- topology changes.

You can think of a BPDU as an STP heartbeat and control message.

If a switch stops receiving expected BPDUs through a link, STP knows the topology changed and can recalculate forwarding paths.

## Port Cost

After the root bridge is elected, every non-root switch must answer:

```text
What is my best path to the root bridge?
```

STP uses port cost for that.

Port cost is a number related to link speed.

General rule:

```text
Faster link = lower cost.
Slower link = higher cost.
Lower total cost wins.
```

For CCNA, memorize two classic values:

| Link speed | STP cost |
| --- | --- |
| 100 Mbps | 19 |
| 1 Gbps | 4 |

If a switch has multiple paths to the root bridge, it chooses the path with the lowest total cost.

## Root Port

A root port is the port a non-root switch uses to reach the root bridge.

Each non-root switch has exactly one root port.

The root bridge itself does not have a root port because it is already root.

Simple formula:

```text
Root port = best port toward the root bridge.
```

If an access switch has two uplinks to the distribution layer, STP compares path cost and selects one as the root port.

## Designated Port

A designated port is the port that forwards traffic for a segment.

Each Layer 2 segment needs a designated port so traffic can pass without creating a loop.

On the root bridge, active ports are usually designated ports because the root bridge is the best reference point for the topology.

Simple formula:

```text
Designated port = forwarding port for that segment.
```

## Blocked Port

A blocked port is a port STP does not use for forwarding user traffic because forwarding through it would create a loop.

Blocked port is often confused with broken port.

They are different.

```text
Blocked by STP does not mean failed.
Blocked means protecting the network.
```

On a redundant connection, one side may be forwarding and the other side may be blocked.

Both switches can be correct. One port is needed for the active path, and the other is held in standby so it does not create a loop.

## STP Decision Order

At a basic level, read STP in this order:

```text
1. Elect the root bridge.
2. Choose root ports on non-root switches.
3. Choose designated ports on each segment.
4. Block remaining loop-causing ports.
```

This is not every STP detail, but it is a strong foundation.

When you read `show spanning-tree`, look for those answers:

- who the root bridge is;
- what the local switch Bridge ID is;
- which port is the root port;
- which ports are designated;
- which ports are blocked;
- what the path cost is.

## Why The Terms Matter In A Real Network

Without the vocabulary, STP output looks like a strange set of lines.

With the vocabulary, `show spanning-tree` becomes a map of decisions.

You can see:

- why this switch is not root;
- why traffic uses this uplink;
- why the fast link is blocked;
- why an old switch became the center of the topology;
- what will change after priority tuning;
- which link opens after a failure.

This matters in real networks, where STP can choose a loop-free topology without choosing the optimal topology.

Loop-free does not always mean well-designed.

## Main Takeaway

STP vocabulary is not just a word list for an exam.

It is the language switches use to explain their decisions.

Remember the foundation:

```text
Lowest Bridge ID wins root bridge election.
Lowest path cost wins the best path.
Root ports point toward the root.
Designated ports forward for a segment.
Blocked ports prevent loops.
```

If those rules make sense, the next step is to take a real topology and manually determine which ports will forward and which ports will block.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Root bridge | Switch elected as the STP reference point for the topology. |
| Bridge ID | STP identifier made from bridge priority and MAC address. |
| Priority | Configurable value used first in root bridge election. Lower wins. |
| BPDU | Bridge Protocol Data Unit, the STP control message exchanged by switches. |
| Port cost | STP value based mainly on link speed. Lower cost is preferred. |
| Root port | Best port on a non-root switch toward the root bridge. |
| Designated port | Forwarding port selected for a Layer 2 segment. |
| Blocked port | Port that does not forward user traffic because it would create a loop. |

## Questions

### 1. What decides the root bridge?

Answer:

The lowest Bridge ID wins. Bridge ID is made from priority and MAC address.

### 2. Why should production networks not leave root bridge election to chance?

Answer:

Because default priority can let the lowest MAC address win, which may place the root bridge on an old or poorly located switch.

### 3. What is the difference between a root port and a blocked port?

Answer:

A root port is the best forwarding path from a non-root switch to the root bridge. A blocked port is held out of forwarding to prevent a Layer 2 loop.

## What To Review Later

- STP election order.
- Root bridge priority tuning.
- Path cost calculation.
- Reading `show spanning-tree`.
- Per-VLAN STP behavior.
- Root bridge primary and secondary design.
