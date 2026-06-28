# Rapid Spanning Tree And MST

Source: closed course page  
Date added: 2026-06-28  
Related plan item: Week 9 / Rapid Spanning Tree and MST  
Tags: RSTP, Rapid PVST, MST, STP, convergence, alternate port, Cisco IOS, Layer 2
Language: English
Translation pair: articles/2026-06/week-09/08-rapid-spanning-tree-and-mst.md

## Summary

Classic STP protects the network from Layer 2 loops, but convergence can be too slow.

In classic STP, failover can take many seconds. For a modern network, that is no longer a normal pause. It is a visible outage.

Rapid Spanning Tree Protocol, RSTP, solves the same problem as classic STP:

```text
Prevent loops.
Keep redundancy.
Recover after failure.
```

But it does it faster.

Main idea:

```text
RSTP is not a new switching idea.
It is a faster STP process.
```

Root bridge election, path cost and port blocking logic remain familiar. What changes is reaction speed and how the switch understands backup paths in advance.

## The Problem With Classic STP

Classic STP is cautious.

When the topology changes, it may move through:

- blocking;
- listening;
- learning;
- forwarding.

In worst-case scenarios, that can mean around 50 seconds before traffic recovers.

The reason is timers and the fact that classic STP often waits before deciding that a path is truly lost.

BPDUs, Bridge Protocol Data Units, are usually sent every 2 seconds. If expected BPDUs disappear, STP eventually understands that the topology changed and begins convergence.

For older networks, that was acceptable.

For a network carrying payments, voice, cameras, cloud apps and business operations, it is too slow.

## What RSTP Improves

RSTP speeds up convergence in two practical ways.

### 1. Faster Failure Detection

RSTP does not have to wait as long as classic STP.

In practice, RSTP can react after losing a few hello intervals. This is often described as three missed BPDUs, or roughly 6 seconds with the default 2-second hello time.

If the physical link actually drops to a down state, the switch can react even faster because the port status changed directly.

That is much better than waiting through the classic STP timer path.

### 2. Remembered Backup Paths

In classic STP, a blocked port is often treated simply as blocked.

RSTP adds more useful roles.

One important role is the alternate port.

An alternate port is a backup path to the root bridge. The switch already knows this port can replace the root port if the primary path fails.

So after a failure, a long relearning process is not always required.

Simplified:

```text
Classic STP:
Something failed.
Wait, recalculate, transition.

RSTP:
Primary path failed.
Use known alternate path.
```

In ideal conditions, failover can be sub-second or close to it, especially when the physical failure is detected immediately.

## RSTP Does Not Replace The Fundamentals

RSTP does not remove the need to understand classic STP.

You still need:

- root bridge;
- Bridge ID;
- path cost;
- root port;
- designated port;
- blocked or discarding behavior;
- BPDU exchange;
- topology changes.

If classic STP makes sense, RSTP is logical.

It does not change the goal. It improves and accelerates the mechanism.

## Enabling Rapid PVST+ On Cisco

On Cisco switches, the common mode is Rapid PVST+, Rapid Per-VLAN Spanning Tree.

Command:

```text
Switch(config)# spanning-tree mode rapid-pvst
```

Apply the setting consistently across switches in the environment.

Rapid PVST+ means:

- rapid convergence behavior;
- a separate STP instance per VLAN;
- different possible root bridges per VLAN;
- per-VLAN load balancing through intentional root placement.

After enabling it, verify:

```text
show spanning-tree
show spanning-tree summary
show running-config | include spanning-tree mode
```

## Why Cisco Rapid PVST+ Is Not Just "One RSTP"

In a Cisco environment, there is usually not one shared STP instance for the whole network.

The PVST model means:

```text
VLAN 10 has its STP logic.
VLAN 20 has its STP logic.
VLAN 30 has its STP logic.
```

Rapid PVST+ adds RSTP speed to that per-VLAN model.

That is useful because you can make:

- switch A root primary for VLAN 10;
- switch B root primary for VLAN 20;
- different forwarding paths for different VLANs;
- better use of redundant links.

The tradeoff is that many VLANs mean many STP instances.

## When PVST+ Becomes Heavy

For a few VLANs, Rapid PVST+ is convenient.

But if a network has dozens or hundreds of VLANs, one instance per VLAN begins to cost resources.

Each VLAN instance requires:

- BPDU processing;
- separate STP state;
- topology calculation;
- CPU and memory attention;
- operational visibility.

In a small lab, this is not noticeable.

In a large campus network, it becomes a design concern.

## MST: Multiple Spanning Tree

MST, Multiple Spanning Tree, solves the scale problem.

Instead of a separate STP instance for every VLAN, MST lets you group VLANs into instances.

Example:

```text
Instance 1: VLANs 10-50
Instance 2: VLANs 51-100
Instance 3: VLANs 101-150
```

The network gets multiple STP topologies, but not one topology per VLAN.

Idea:

```text
PVST+: one instance per VLAN.
MST: one instance per VLAN group.
```

This reduces overhead while keeping flexibility for large environments.

## Three Flavors To Keep Separate

### Classic STP

Original behavior.

Pros:

- simple concept;
- loop prevention;
- still exists in old networks.

Cons:

- slow convergence;
- 30-50 second delays can hurt;
- not ideal for modern production.

### Rapid PVST+

Cisco-friendly modern default for many environments.

Pros:

- fast convergence;
- per-VLAN flexibility;
- familiar Cisco operations;
- good fit for many campus networks.

Cons:

- one instance per VLAN;
- overhead grows with VLAN count.

### MST

Scale-oriented approach.

Pros:

- groups VLANs into fewer STP instances;
- reduces overhead;
- works better for large VLAN counts;
- still allows multiple forwarding topologies.

Cons:

- requires more careful planning;
- region and configuration consistency matter;
- troubleshooting can be less beginner-friendly.

## Practical Recommendation

If you inherit a Cisco switching network, check the STP mode.

Commands:

```text
show spanning-tree summary
show running-config | include spanning-tree mode
```

If the network still runs classic 802.1D behavior, it is worth discussing as a modernization target.

For a typical Cisco campus or lab environment, you often expect:

```text
spanning-tree mode rapid-pvst
```

For a large enterprise with many VLANs, MST may be appropriate.

But do not change STP mode blindly. First check:

- current root bridge placement;
- VLAN count;
- switch platform support;
- topology design;
- maintenance window;
- rollback plan;
- documentation.

## Main Takeaway

RSTP makes STP faster, but it does not remove the STP fundamentals.

Rapid PVST+ is the Cisco approach: fast convergence plus per-VLAN STP.

MST is the scale approach: group VLANs into fewer STP instances.

Remember:

```text
Classic STP: original and slow.
Rapid PVST+: fast Cisco per-VLAN model.
MST: scalable grouped-instance model.
```

If you understand classic STP decisions, Rapid STP becomes understandable: it reacts faster, remembers backup paths and fits modern networks better.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| RSTP | Rapid Spanning Tree Protocol, faster STP evolution. |
| Rapid PVST+ | Cisco rapid per-VLAN STP mode. |
| Alternate port | RSTP backup path that can replace the root port if the primary path fails. |
| MST | Multiple Spanning Tree, grouping VLANs into shared STP instances. |
| Convergence | Process of recalculating and restoring a loop-free topology after a change. |
| BPDU | STP control message exchanged between switches. |
| 802.1D | Original classic STP standard behavior. |

## Questions

### 1. What is the main advantage of RSTP over classic STP?

Answer:

RSTP converges much faster by reacting more quickly to failures and by using roles such as alternate ports for known backup paths.

### 2. What Cisco command enables Rapid PVST+?

Answer:

`spanning-tree mode rapid-pvst`

### 3. Why use MST in a large network?

Answer:

MST reduces overhead by grouping many VLANs into fewer spanning tree instances instead of running a separate instance for every VLAN.

## What To Review Later

- RSTP port roles.
- RSTP proposal/agreement behavior.
- Rapid PVST+ verification.
- MST regions and VLAN-to-instance mapping.
- STP migration planning.
