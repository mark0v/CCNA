# Classic STP Timers, PVST, And Root Bridge Control

Source: closed course page  
Date added: 2026-06-28  
Related plan item: Week 9 / Classic STP timers, PVST, and root bridge configuration  
Tags: STP, PVST, RSTP, timers, port states, root bridge, priority, Cisco IOS
Language: English
Translation pair: articles/2026-06/week-09/07-classic-stp-timers-pvst-and-root-bridge.md

## Summary

Classic Spanning Tree Protocol is safe, but slow.

When a port comes up, it does not immediately begin forwarding. Classic STP first moves it through states so it does not create a Layer 2 loop.

At minimum, that can take 30 seconds:

```text
Listening: 15 seconds
Learning: 15 seconds
Forwarding: traffic starts
```

In a failover scenario, recovery can take up to 50 seconds when blocking and max age behavior are involved.

That was acceptable for older networks. In modern networks, it is a long outage. That is why production networks usually use Rapid Spanning Tree Protocol, RSTP, but classic STP states still matter: RSTP accelerates the same basic process.

## Why Classic STP Is Slow

STP was not designed for speed.

It was designed for safety.

When an interface appears in the topology, a switch cannot simply begin forwarding traffic. It must first make sure that the port will not create a loop.

If forwarding starts too early, one wrong redundant link can cause a broadcast storm.

So classic STP waits, listens for BPDUs, builds the MAC table and only then forwards frames.

It feels slow because it is slow.

## The Four Port States

Classic STP is often explained through port states.

### Blocking

Blocking state is used when STP believes forwarding through the port may create a loop.

The port:

- does not forward user traffic;
- does not learn MAC addresses;
- still receives BPDUs;
- may remain a standby path.

In a convergence scenario, waiting can be up to 20 seconds due to max age.

Blocking is not automatically a failure. It is often normal STP protection.

### Listening

Listening lasts 15 seconds.

In this state, the switch actively participates in STP calculation:

- receives and sends BPDUs;
- identifies the root bridge;
- determines port roles;
- does not forward user traffic;
- does not build the MAC address table for user frames.

The port is participating in STP logic, but it is not serving ordinary traffic yet.

### Learning

Learning also lasts 15 seconds.

Now the switch begins building the MAC address table.

The port:

- learns source MAC addresses;
- still does not forward user traffic;
- prepares for safe forwarding.

This reduces unnecessary flooding when the port finally transitions to forwarding.

### Forwarding

Forwarding is the working state.

The port:

- forwards user traffic;
- learns MAC addresses;
- sends and receives BPDUs;
- participates in normal switching.

This is the state users are usually waiting for after a link comes up.

## 30 And 50 Seconds

For a freshly activated port in classic STP, the minimum often looks like this:

```text
Listening 15s
Learning  15s
Total     30s
```

In some failover cases, blocking and max age waiting are added:

```text
Blocking / max age 20s
Listening          15s
Learning           15s
Total              50s
```

This is not a glitch.

It is classic STP design.

But for a modern network, 30-50 seconds of downtime can be unacceptable.

## Why RSTP Matters

Rapid Spanning Tree Protocol, RSTP, exists because classic STP convergence is too slow for modern expectations.

RSTP keeps the STP goal:

```text
Prevent Layer 2 loops.
Preserve redundancy.
Recover after failure.
```

But it converges much faster.

For now, understand the classic process. Then RSTP will look less like new magic and more like a faster version of the same idea.

## PVST: One STP Instance Per VLAN

On a Cisco switch, this command:

```text
show spanning-tree
```

often shows not one STP instance, but a separate instance per VLAN.

That is PVST, Per-VLAN Spanning Tree.

The idea:

```text
Each VLAN can have its own STP topology.
```

For example:

- VLAN 10 can have one root bridge;
- VLAN 20 can have another root bridge;
- VLAN 30 can use a different forwarding path.

This helps with load balancing.

A link that is blocked for VLAN 10 can still forward VLAN 20 traffic.

The network does not have to use the same active path for every VLAN.

## Why Priority Looks Strange

In Cisco PVST, you may see priorities such as:

```text
32769
32778
```

Those are not random numbers.

The default bridge priority is usually `32768`, but Cisco adds the VLAN ID through the extended system ID.

Examples:

| VLAN | Displayed priority |
| --- | --- |
| VLAN 1 | 32769 |
| VLAN 10 | 32778 |
| VLAN 20 | 32788 |

Logic:

```text
32768 + VLAN ID
```

That is also why manual priority values use increments of 4096. Part of the field is used for VLAN information.

## Why Root Bridge Should Not Be Random

If you do not configure the root bridge, STP elects it by lowest Bridge ID.

If every switch has the same priority, the lowest MAC address wins.

That can place the root bridge on a random access switch in a wiring closet.

Consequences:

- traffic does not flow through the best switch;
- a fast uplink may be blocked;
- the topology looks strange;
- troubleshooting becomes harder;
- failure recovery may not behave as expected.

Root bridge placement should be a design decision.

Usually, the root should be a core or distribution switch.

## Manual Root Bridge Configuration

Option 1 is to set priority explicitly:

```text
spanning-tree vlan 1 priority 4096
```

Lower priority wins.

The key is to choose a value lower than the other switches.

For multiple VLANs, you can tune this separately to control per-VLAN topology.

## Root Primary And Root Secondary

Cisco also provides shortcut commands:

```text
spanning-tree vlan 1 root primary
spanning-tree vlan 1 root secondary
```

`root primary` checks current priorities and tries to set the switch lower than the others so it becomes root.

`root secondary` sets priority so the switch becomes the backup root. If the primary root bridge fails, the secondary should win the election instead of a random closet switch.

You can specify multiple VLANs:

```text
spanning-tree vlan 1,10,20 root primary
```

or an IOS-style range/list syntax if the platform supports it.

## Practical Verification

After configuring STP, do not trust the config blindly.

Verify:

```text
show spanning-tree
show spanning-tree vlan 1
show spanning-tree vlan 10
show running-config | include spanning-tree
```

Look for:

- who the root bridge is for each VLAN;
- whether the local switch is root;
- what priority is displayed;
- which ports are root, designated or blocked;
- whether the forwarding path matches the design.

## Main Takeaway

Classic STP is reliable, but slow.

A port may wait 30 seconds before forwarding, and failover can take up to 50 seconds.

PVST adds an important Cisco behavior: a separate STP instance for each VLAN, which allows per-VLAN path control and load balancing.

Root bridge election should not be left to the default MAC address tiebreaker.

Remember:

```text
Classic STP is cautious.
PVST is per VLAN.
Root bridge should be intentional.
RSTP is the faster next step.
```

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Blocking | STP state where a port does not forward user traffic to prevent loops. |
| Listening | STP state where a port participates in BPDU exchange but does not forward traffic. |
| Learning | STP state where a port learns MAC addresses but still does not forward user traffic. |
| Forwarding | STP state where a port forwards traffic and learns MAC addresses. |
| PVST | Per-VLAN Spanning Tree, Cisco STP mode with one STP instance per VLAN. |
| RSTP | Rapid Spanning Tree Protocol, faster STP evolution. |
| Root primary | Cisco shortcut to make a switch the intended STP root for selected VLANs. |
| Root secondary | Cisco shortcut to make a switch the backup STP root for selected VLANs. |

## Questions

### 1. Why can classic STP take 30 seconds before forwarding?

Answer:

Because a port normally spends 15 seconds in listening and 15 seconds in learning before forwarding traffic.

### 2. Why does Cisco show priorities like 32769 for VLAN 1?

Answer:

Because Cisco PVST uses extended system ID: default priority 32768 plus the VLAN ID.

### 3. Why configure root primary and root secondary?

Answer:

To make the intended core or distribution switch the root bridge and keep a planned backup root ready if the primary fails.

## What To Review Later

- Rapid Spanning Tree Protocol.
- STP timers and convergence.
- PVST and per-VLAN load balancing.
- Root bridge priority design.
- PortFast and BPDU Guard for edge ports.
