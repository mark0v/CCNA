# Why Spanning Tree Protocol Exists

Source: closed course page  
Date added: 2026-06-28  
Related plan item: Week 9 / Spanning Tree Protocol foundations  
Tags: STP, Spanning Tree Protocol, switching, redundancy, Layer 2, broadcast storm, CCNA
Language: English
Translation pair: articles/2026-06/week-09/02-why-spanning-tree-protocol-exists.md

## Summary

Spanning Tree Protocol, STP, exists because of a simple problem: in a Layer 2 network, redundant links can create a loop.

A loop in a switched network is not just "one packet went the wrong way." It can become a broadcast storm, where broadcast frames keep circulating, multiplying and overwhelming the network.

That is why STP does two things:

- finds dangerous redundant paths;
- blocks enough of those paths to keep the topology loop-free.

The blocked link does not disappear forever. It stays available as a standby path. If the primary link fails, STP can recalculate the topology and restore connectivity through the backup path.

Main idea:

```text
Redundancy is good.
Layer 2 loops are dangerous.
STP keeps redundancy from destroying the network.
```

## Why STP Intimidates Students

STP often sits next to subnetting on the list of CCNA topics that make students lose confidence.

The reason is not that the idea is impossible.

The reason is that STP quickly gets detailed:

- bridge ID;
- root bridge election;
- root ports;
- designated ports;
- blocked ports;
- timers;
- port states;
- convergence;
- per-VLAN behavior.

If you start with those details, the topic looks like a pile of strange rules.

It is better to start with why.

STP was not created for an exam. It exists because real switched networks need redundancy, but Layer 2 Ethernet by itself does not safely handle loops.

## What Happens Without STP

Imagine two switches with two physical links between them.

On a diagram, that looks good:

```text
SW1 ===== SW2
```

One link can be primary, and the other can be backup.

But Ethernet frames do not have a TTL like IP packets. If a Layer 2 frame enters a loop, it does not disappear just because it crossed too many hops.

Broadcast frames are especially dangerous.

A broadcast must be sent out all ports in the VLAN except the port it came from. If there is a loop between switches, each switch can keep forwarding the same broadcast again and again.

Result:

- broadcast frames circulate endlessly;
- copies multiply;
- switch CPU and bandwidth are exhausted;
- MAC address tables start flapping;
- normal traffic stops passing;
- users see "the network is down" even though the physical links are still lit.

That is a broadcast storm.

## Broadcast Storm In Practice

A broadcast storm rarely looks clean.

Common symptoms:

- the network suddenly becomes very slow;
- pings start dropping;
- DHCP stops answering reliably;
- phones, registers, cameras or workstations disconnect;
- switches show high utilization;
- logs fill with MAC flapping or topology changes;
- unplugging one cable unexpectedly "fixes" the issue.

In a small lab, this may only be annoying.

In a business network, it is an outage.

If it is a coffee shop, orders stop processing. If it is a warehouse, scanners may stop. If it is an office, users lose access to services.

STP exists so a redundant link does not become that kind of incident.

## What STP Does

STP looks at the switching topology and builds a loop-free tree.

The word "tree" matters.

In networking, a tree is a topology without loops. There is a path between points, but there is no endless circle.

STP decides which ports will forward and which ports must be blocked.

Simplified:

```text
Forwarding ports carry traffic.
Blocked ports protect the network from loops.
```

If the active path fails, STP can recalculate the topology and open a previously blocked path.

So STP does not destroy redundancy. It turns some redundancy into standby capacity.

## Why This Is Not Just "Turn Off The Extra Link"

You might ask: if a redundant link is dangerous, why not just unplug it?

Because redundancy is useful.

Without backup links, one failed cable, failed port or failed switch path can cut off part of the network.

STP lets you keep physical redundancy connected, but controlled.

Difference:

```text
No redundancy:
one failure can break connectivity.

Uncontrolled redundancy:
one loop can break the whole Layer 2 network.

STP-controlled redundancy:
backup path exists, but loops are prevented.
```

That is why STP is a foundational enterprise switching technology.

## What STP Watches

At a basic level, STP exchanges control messages between switches. These messages are called BPDUs, Bridge Protocol Data Units.

With BPDUs, switches understand:

- which switches exist in the topology;
- which switch should become the root bridge;
- which ports provide the best path to the root bridge;
- which ports should forward traffic;
- which ports must block to prevent a loop.

You do not need to memorize every election rule yet.

The important point for now is:

```text
STP is not guessing.
Switches exchange information and calculate a safe forwarding topology.
```

Later lessons can break down exactly how STP makes those decisions.

## How This Connects To Our Network

In the NetworkChuck Coffee and Fallout Shelter scenarios, the switch infrastructure is becoming more realistic.

When the network is tiny and every link is single-homed, STP can feel secondary.

But the moment a second uplink, redundant switch path or collapsed core topology appears, STP becomes mandatory knowledge.

Without STP:

- one extra cable can create a loop;
- one misconfigured port can take down a VLAN;
- one "backup link" can become the outage cause;
- troubleshooting turns into guessing.

With STP:

- the topology stays loop-free;
- a redundant path can wait as backup;
- a blocked port does not automatically mean failure;
- an engineer can explain why traffic flows the way it does.

## Do Not Casually Disable STP

In a lab, it can be tempting to disable STP so a link "turns green" or traffic "moves faster."

That is a dangerous habit.

If STP blocks a port, understand why first.

Check:

- whether there is a redundant path;
- which switch is the root bridge;
- which port is root, designated or blocked;
- whether there is an unexpected cable;
- whether an access port accidentally became part of a loop;
- whether the topology matches the diagram.

An STP block is not always a problem.

Sometimes it is proof that network protection is working.

## First Commands To Observe

At the CCNA level, start by observing rather than tuning.

Useful commands:

```text
show spanning-tree
show spanning-tree vlan 10
show spanning-tree summary
show interfaces status
show mac address-table
```

Look for:

- root bridge;
- local bridge ID;
- port roles;
- port states;
- forwarding ports;
- blocking ports;
- topology changes;
- MAC address movement.

For now, the goal is simple: see that STP is actually working, not just memorize a definition.

## Main Takeaway

STP does not exist because Cisco wanted to make the CCNA harder.

STP exists because uncontrolled Layer 2 redundancy can destroy a network.

It prevents switching loops and broadcast storms by blocking redundant paths where needed.

But a blocked path is not a wasted link. It is standby protection that can preserve connectivity during a failure.

Short version:

```text
STP is the safety system that lets switched networks have redundancy without loops.
```

Understanding STP is the difference between someone who only sees blinking lights and an engineer who understands why the network behaves the way it does.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| STP | Spanning Tree Protocol. Protocol that prevents Layer 2 loops in switched networks. |
| Broadcast storm | Network failure where broadcast frames loop and multiply until the network is overloaded. |
| Redundant link | Extra physical path used for backup or resiliency. |
| Loop-free topology | Layer 2 topology where frames cannot circulate endlessly. |
| BPDU | Bridge Protocol Data Unit. STP message exchanged between switches. |
| Root bridge | Central reference switch used by STP to calculate paths. |
| Blocking port | Port that STP prevents from forwarding traffic to avoid a loop. |
| Forwarding port | Port that actively forwards traffic. |

## Questions

### 1. Why does STP exist?

Answer:

STP exists to prevent Layer 2 loops when switched networks have redundant links.

### 2. Why are Layer 2 loops dangerous?

Answer:

Ethernet frames do not have a TTL like IP packets. A broadcast frame can loop repeatedly, multiply, overload the network and cause a broadcast storm.

### 3. Does a blocked STP port always mean something is broken?

Answer:

No. A blocked port may mean STP is correctly preventing a loop while keeping the link available as a standby path.

## What To Review Later

- Root bridge election.
- Root ports and designated ports.
- STP port states.
- STP timers and convergence.
- Rapid Spanning Tree Protocol.
- EtherChannel as an alternative to letting STP block parallel links.
