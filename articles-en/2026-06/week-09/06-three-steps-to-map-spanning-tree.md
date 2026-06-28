# Three Steps To Map Spanning Tree

Source: closed course page  
Date added: 2026-06-28  
Related plan item: Week 9 / Three-step STP topology mapping  
Tags: STP, root port, designated port, blocked port, root bridge, port cost, bridge ID, topology
Language: English
Translation pair: articles/2026-06/week-09/06-three-steps-to-map-spanning-tree.md

## Summary

Many people know that Spanning Tree Protocol blocks redundant ports.

Fewer people understand why STP blocks the exact ports it blocks.

That difference matters. In a real network, you are not staring at a definition. You are staring at a topology, `show spanning-tree` output and the question: why is this link not forwarding?

To manually analyze an STP topology, use the same order every time:

```text
1. Identify root ports.
2. Identify designated ports.
3. Block everything else.
```

Plus three tiebreakers:

```text
1. Lowest cost to root bridge.
2. Lowest bridge ID.
3. Lowest port number.
```

If you work systematically, STP stops being guesswork.

## The Topology To Imagine

Picture the Cisco three-tier hierarchy:

- access layer at the bottom, where end devices connect;
- distribution layer in the middle, where networks consolidate;
- core layer at the top, the backbone of the network.

That design often has many redundant paths.

That is good for uptime.

But at Layer 2, it also creates potential loops.

STP must preserve full connectivity while removing loops. It does that by selecting an active forwarding tree and blocking extra paths.

## Before The Three Steps: Root Bridge

Before choosing ports, STP first elects the root bridge.

The root bridge is the reference point for the whole STP topology.

Root bridge election uses the lowest Bridge ID:

```text
Bridge ID = priority + MAC address
```

Lowest wins.

In this article, we are not configuring priority yet. Assume the root bridge has already been selected.

After that, each switch asks the main question:

```text
How do I reach the root bridge?
```

## Step 1: Identify Root Ports

A root port is the best port on a non-root switch toward the root bridge.

Every non-root switch must have exactly one root port.

A root port is always forwarding.

How does a switch choose the best port?

It compares paths to the root bridge using three tiebreakers.

### Tiebreaker 1: Lowest Cost To Root

Cost is related to link speed.

For CCNA, keep these values in mind:

| Link speed | STP cost |
| --- | --- |
| 100 Mbps | 19 |
| 1 Gbps | 4 |

A switch adds the costs along each path to the root bridge.

Lowest total cost wins.

Example:

```text
Path A: 4 + 4 = 8
Path B: 19 + 4 = 23
Path A wins
```

### Tiebreaker 2: Lowest Bridge ID

If the cost is the same, the switch compares the neighbor Bridge ID.

The path through the neighbor with the lowest Bridge ID wins.

That gives STP a deterministic path even when speeds are equal.

### Tiebreaker 3: Lowest Port Number

If cost and Bridge ID are also tied, STP compares port numbers.

Lowest port number wins.

This is the final tiebreaker when the earlier values do not separate the paths.

## Step 2: Identify Designated Ports

After root ports, STP looks at each Layer 2 segment.

Each segment must have one designated port.

A designated port is the port that forwards traffic for that segment.

First rule:

```text
All active ports on the root bridge are designated ports.
```

That is the reward for becoming root bridge. The root bridge is the best reference point, so its ports on connected segments forward.

For other segments, the switches on each end of the link compete.

They use the same criteria:

```text
1. Lowest cost to root bridge.
2. Lowest bridge ID.
3. Lowest port number.
```

Whoever wins gets the designated port.

The designated port forwards.

## Step 3: Block The Leftovers

Now the rule is simple:

```text
If a port is not a root port
and not a designated port,
it becomes blocked.
```

A blocked port does not forward user traffic.

But it is not "dead." It is still physically up and can still receive BPDUs.

Its job is to prevent a Layer 2 loop from becoming a broadcast storm.

In a fully redundant design, STP may block many links.

That is not a bug.

That is STP doing its job.

## How To See This On A Diagram

A useful trick: after choosing blocked ports, mentally erase the blocked links from the diagram.

The remaining active topology should look like a tree:

- all switches connected;
- every switch has a path to the root bridge;
- no loops remain;
- redundant links are in standby.

If an active link fails, STP can recalculate the topology and open some blocked ports.

That is how the network gets redundancy without loops.

## Paper Workflow

When you see an STP diagram, do not guess.

Use this checklist:

### 1. Mark The Root Bridge

Find the switch with the lowest Bridge ID.

If priority is configured intentionally, the root is usually a core or distribution switch.

### 2. Mark Root Ports

On every non-root switch, find the best path to root:

- lowest total cost;
- then lowest neighbor Bridge ID;
- then lowest neighbor port number.

### 3. Mark Designated Ports

On every segment, choose the forwarding side:

- root bridge ports win automatically;
- otherwise compare lowest cost to root;
- then Bridge ID;
- then port number.

### 4. Block The Rest

Every port that is neither root nor designated becomes blocked.

## Why This Matters In A Real Network

In production, you are not always drawing STP on paper.

But this mental model matters when:

- a fast uplink is blocked;
- traffic flows through an unexpected switch;
- an access switch becomes root;
- after a failure, the wrong path opens;
- the topology converges, but performance is poor;
- `show spanning-tree` shows roles that do not match the diagram.

If you understand the three steps, you can explain the STP decision.

If you do not, blocked links look random.

## Main Takeaway

STP can be analyzed by hand.

The order is always:

```text
1. Root ports.
2. Designated ports.
3. Blocked leftovers.
```

The tiebreakers are also ordered:

```text
1. Lowest cost to root.
2. Lowest bridge ID.
3. Lowest port number.
```

Practice on messy switch diagrams. Draw redundant links, choose the root bridge and walk through the steps.

That is more valuable than memorizing the phrase "STP blocks redundant links."

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Root port | Best port on a non-root switch toward the root bridge. |
| Designated port | Forwarding port selected for a Layer 2 segment. |
| Blocked port | Port that does not forward user traffic because it would create a loop. |
| Path cost | Total STP cost from a switch toward the root bridge. |
| Bridge ID | Identifier made from priority and MAC address. Lowest wins elections. |
| Tiebreaker | Rule used when the earlier STP comparison produces a tie. |
| Segment | Layer 2 link or shared medium where STP chooses a designated port. |

## Questions

### 1. What are the three manual STP mapping steps?

Answer:

Identify root ports, identify designated ports, then block every remaining port that is neither root nor designated.

### 2. What are the three main STP tiebreakers?

Answer:

Lowest cost to the root bridge, lowest bridge ID, and lowest port number.

### 3. Why are blocked ports not a failure?

Answer:

They are standby ports that prevent Layer 2 loops. They can become useful if the active path fails and STP recalculates the topology.

## What To Review Later

- Root bridge priority configuration.
- Reading `show spanning-tree`.
- Root port selection examples.
- Designated port selection examples.
- STP convergence after link failure.
- EtherChannel and why it changes the redundant-link problem.
