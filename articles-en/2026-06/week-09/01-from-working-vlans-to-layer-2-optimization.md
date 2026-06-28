# From Working VLANs To Layer 2 Optimization

Source: closed course page  
Date added: 2026-06-28  
Related plan item: Week 9 / Layer 2 optimization after VLAN deployment  
Tags: VLAN, STP, Layer 2, redundancy, trunk, router-on-a-stick, verification
Language: English
Translation pair: articles/2026-06/week-09/01-from-working-vlans-to-layer-2-optimization.md

## Summary

Working VLAN segmentation is not the end of the design.

It is the point where the network starts showing whether the Layer 2 topology was built intentionally or simply left to default behavior.

In the Fallout Shelter network, the implementation already had:

- four VLANs;
- four subnets;
- default gateways for the VLANs;
- DHCP scopes;
- access ports for endpoints;
- trunks between switches;
- router-on-a-stick for inter-VLAN routing.

After that, clients received addresses, DHCP bindings appeared, pings worked, and the network became a working segmented LAN.

But that immediately created the next question:

```text
The network works.
But is the Layer 2 design optimal?
```

That is a normal next stage. First you prove connectivity. Then you verify how that connectivity moves through the switching topology.

## Why Working Does Not Mean Finished

When VLANs begin working, it is easy to think the task is done.

But VLAN implementation changes more than switch config. It changes:

- broadcast domains;
- IP subnets;
- gateway placement;
- DHCP boundaries;
- trunk requirements;
- routing paths;
- security boundaries;
- troubleshooting model.

If all of that works, it proves the baseline design is viable.

It does not prove that:

- redundancy is being used correctly;
- traffic is taking the expected path;
- STP selected the best root bridge;
- blocked ports are where you wanted them;
- uplinks are used efficiently;
- failure behavior is understood in advance.

For a production mindset, that difference matters.

A lab can be "green" from a ping perspective while the design still needs work.

## Where STP Appears

STP, Spanning Tree Protocol, protects a Layer 2 network from loops.

If switches have redundant links, STP must keep the topology loop-free. To do that, it may block one of the paths.

That is correct from a safety perspective.

But a default STP decision does not always match your design intent.

For example:

- the root bridge may be the wrong switch;
- the main uplink may be blocked;
- traffic may use an awkward path;
- a backup link may become active somewhere unexpected;
- different VLANs may not use the forwarding paths you planned.

The network can still work.

That is why a simple `ping` test does not answer the Layer 2 optimization question.

`ping` says: "a route exists."

STP analysis asks: "is the network using the right Layer 2 path, or did it merely find any safe path?"

## What To Check After VLAN Deployment

After VLANs, trunks, DHCP, and router-on-a-stick are working, verify Layer 2 behavior as a separate stage.

Minimum checklist:

```text
1. Which switches participate in the VLAN path?
2. Which links are trunks?
3. Which VLANs are allowed on each trunk?
4. Where is the STP root bridge for each VLAN?
5. Which ports are forwarding?
6. Which ports are blocking?
7. Does the forwarding path match the design?
8. What happens when the active uplink fails?
```

This is no longer one command.

It is a check that the topology behaves predictably.

## Why Redundancy Can Mislead You

Redundancy often looks good on a diagram.

Two uplinks are better than one. Multiple paths are better than one path. Multiple switches are better than a single point of failure.

But at Layer 2, redundant links are dangerous without loop prevention.

That is why STP blocks part of the topology.

The problem is not that STP blocks a link. That is its job.

The problem appears when the blocked link is not the one you expected.

The right way to think about it:

```text
I built redundancy.
STP made it safe.
Now I must make it intentional.
```

Do not only celebrate that a loop did not happen. Understand which switch controls the tree, which links are active, which links are standby, and how quickly the network recovers from failure.

## Connection To VLAN Design

VLAN design and STP design are connected.

Each VLAN is a separate broadcast domain. If the topology uses multiple switches and trunks, each VLAN needs a clear Layer 2 path.

In a small lab topology, that may look obvious.

In a real network, questions appear quickly:

- Should the management VLAN use the same uplink as the guest VLAN?
- Should video traffic prefer a different path?
- Should the guest VLAN only reach the firewall or router?
- Where should the root bridge be for critical VLANs?
- Should load be distributed between links for different VLANs?

When the network is small, these questions are easy to ignore.

But a small lab is exactly where you can learn to see them without production pressure.

## Practical Verification Flow

After VLAN deployment, do not stop at IP checks.

Verify the layers in order.

### 1. VLAN Database

Confirm that the VLANs exist where they should exist.

```text
show vlan brief
```

Check:

- VLAN IDs;
- VLAN names;
- access port membership.

### 2. Trunks

Confirm that switch-to-switch links and the router-facing link are actually trunks.

```text
show interfaces trunk
```

Check:

- trunk status;
- native VLAN;
- allowed VLANs;
- VLANs active in the management domain.

### 3. Router-On-A-Stick

Confirm that router subinterfaces match the VLAN tags.

```text
show ip interface brief
show running-config interface ...
```

Look for:

- correct encapsulation dot1Q;
- correct gateway IP;
- interface up/up;
- no missing trunk on the switch side.

### 4. DHCP

Confirm that clients receive addresses from the correct scopes.

```text
show ip dhcp binding
```

For each client, verify:

- IP address;
- subnet mask;
- default gateway;
- DNS, if required in the lab;
- VLAN membership on the switch port.

### 5. STP

Now move into Layer 2 optimization.

```text
show spanning-tree
show spanning-tree vlan 10
show spanning-tree vlan 20
show spanning-tree vlan 30
show spanning-tree vlan 40
```

Check:

- root bridge;
- root port;
- designated ports;
- blocked ports;
- bridge priority;
- port cost;
- whether the path matches the design.

## Red Flags

After VLAN implementation, watch for these signs:

- STP root bridge was selected accidentally;
- an access switch became root bridge for no reason;
- a trunk is blocked where you expected the main uplink;
- important VLANs use an indirect path;
- DHCP only works in some VLANs;
- inter-VLAN routing works, but the traffic path looks strange;
- documentation does not reflect the real forwarding topology.

This does not always mean the network is broken.

It means the design is not fully controlled yet.

## Main Takeaway

VLANs provide segmentation.

Router-on-a-stick provides inter-VLAN routing.

DHCP scopes provide automatic addressing.

But Layer 2 optimization answers a different question:

```text
Does the switching topology behave the way we intended?
```

After the Fallout Shelter VLAN implementation, the network worked. The next professional step is to inspect STP behavior, root bridge placement, blocked links, and redundancy design.

A working network is the baseline.

A predictable network is the goal.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| STP | Spanning Tree Protocol. Layer 2 protocol that prevents loops by blocking redundant paths. |
| Root bridge | Switch that becomes the reference point for STP path calculation. |
| Blocked port | STP port state where the port does not forward user traffic to prevent a loop. |
| Forwarding port | STP port state where the port forwards frames. |
| Trunk | Switch link that carries traffic for multiple VLANs using VLAN tags. |
| Router-on-a-stick | Inter-VLAN routing design where one physical router interface uses multiple subinterfaces. |
| Design intent | The intended traffic path and failure behavior, not just whatever the protocol selected by default. |

## Questions

### 1. Why is a working VLAN deployment not automatically finished?

Answer:

Because connectivity proves that the basic configuration works, but it does not prove that Layer 2 paths, redundancy, STP root placement, and failure behavior match the intended design.

### 2. What problem does STP solve?

Answer:

STP prevents Layer 2 loops by placing some redundant paths into a non-forwarding state when needed.

### 3. What should you check after DHCP and pings start working?

Answer:

Check VLAN membership, trunk status, allowed VLANs, router subinterfaces, DHCP bindings, and then STP behavior: root bridge, forwarding ports, blocked ports, and whether traffic follows the expected path.

## What To Review Later

- STP root bridge selection.
- STP port roles and port states.
- Per-VLAN STP behavior.
- EtherChannel as a better way to use multiple physical links.
- How to document intended Layer 2 forwarding paths.
