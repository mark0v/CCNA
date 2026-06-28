# PortFast And BPDU Guard

Source: closed course page  
Date added: 2026-06-28  
Related plan item: Week 9 / PortFast and BPDU Guard on access ports  
Tags: STP, PortFast, BPDU Guard, err-disabled, access port, unmanaged switch, Cisco IOS
Language: English
Translation pair: articles/2026-06/week-09/09-portfast-and-bpdu-guard.md

## Summary

Sometimes the network is not broken by a complex attack or a firewall mistake.

Sometimes it is broken by a small unmanaged switch under a desk.

The scenario is simple:

- someone needs one more network port;
- a cheap unmanaged switch is connected;
- later, someone accidentally creates a loop with a cable;
- broadcast traffic begins circulating;
- the network gets a broadcast storm.

The problem is that cheap unmanaged switches usually do not participate in STP. They do not help break the loop.

On Cisco switches, two important features protect access ports:

```text
PortFast + BPDU Guard
```

PortFast makes end-device ports come up quickly.

BPDU Guard protects an access port if a switch suddenly appears there.

## Why An Unmanaged Switch Is Dangerous

A normal access port should connect to an end device:

- PC;
- printer;
- IP phone;
- access point;
- camera;
- POS terminal.

An end device should not send BPDUs.

BPDU, Bridge Protocol Data Unit, is an STP control message. Switches use BPDUs to discover topology, elect the root bridge and prevent loops.

If an access port receives a BPDU, that is suspicious.

It may mean:

- someone connected a switch;
- a loop appeared;
- the port is being used differently than designed;
- an unmanaged device is creating Layer 2 risk.

## BPDU Guard

BPDU Guard protects ports where switches should not exist.

Logic:

```text
If this access port receives a BPDU,
shut it down before it can damage the network.
```

When BPDU Guard triggers, the Cisco switch places the port into err-disabled state.

The port stops forwarding traffic.

That can feel aggressive, but it is better than letting one wrong cable cause a broadcast storm.

The logs may show a message such as:

```text
BPDU guard error detected
```

In interface status, the port may appear as:

```text
err-disabled
```

## Recovering An Err-Disabled Port

Basic manual recovery:

```text
interface gigabitEthernet0/10
 shutdown
 no shutdown
```

But find the cause before recovery.

Do not simply run `shutdown` / `no shutdown` if the loop is still under the desk or the unmanaged switch is still connected incorrectly.

Check:

- what is connected to the port;
- whether an extra cable is plugged in;
- whether there is a small unmanaged switch;
- whether the port should actually be an uplink;
- whether documentation is wrong.

Err-disabled is not only caused by BPDU Guard. It can also appear because of other protections, such as port security violations.

But knowing how to clear it with shutdown/no shutdown is useful real-world knowledge.

## PortFast

PortFast solves a different problem.

Classic STP may wait:

```text
Listening 15s
Learning  15s
Forwarding
```

For switch-to-switch links, that caution makes sense.

For an ordinary laptop or printer, it is unnecessary delay.

An end device does not create a switching topology. It should not become part of STP calculation like a switch uplink.

PortFast tells the switch:

```text
This is an edge port.
Move to forwarding immediately.
```

Result:

- the PC receives network access faster;
- DHCP works sooner;
- the user does not wait 30 seconds;
- the access port behaves like an edge port.

## Why PortFast And BPDU Guard Work Together

PortFast speeds up the port.

But if someone connects a switch to a PortFast-enabled port, there is risk: the port can move to forwarding quickly.

That is why PortFast and BPDU Guard are commonly paired.

Design logic:

```text
PortFast:
End devices should come online fast.

BPDU Guard:
If this edge port receives a BPDU, shut it down.
```

One provides speed.

The other provides safety.

## Interface Configuration

For a specific access port:

```text
interface gigabitEthernet0/10
 switchport mode access
 spanning-tree portfast
 spanning-tree bpduguard enable
```

Use this on ports connected to end devices.

Do not use it on switch uplinks unless you understand the design.

## Global Configuration

A scalable approach is to enable PortFast for access ports and BPDU Guard for PortFast-enabled ports.

Commands:

```text
spanning-tree portfast default
spanning-tree portfast bpduguard default
```

After that, ports that should be uplinks or trunks must be configured intentionally and not treated as edge ports.

If BPDU Guard must be disabled on a specific uplink:

```text
interface gigabitEthernet0/1
 spanning-tree bpduguard disable
```

But first confirm that it really is a switch-to-switch link.

## What To Verify

Useful commands:

```text
show spanning-tree summary
show spanning-tree interface gigabitEthernet0/10 detail
show interfaces status err-disabled
show interfaces gigabitEthernet0/10
show logging
show running-config interface gigabitEthernet0/10
```

Check:

- whether PortFast is enabled;
- whether BPDU Guard is enabled;
- whether the port is err-disabled;
- whether there is a BPDU Guard log message;
- whether the correct device is connected;
- whether the port is actually an uplink.

## Practical Deployment Pattern

For a real network, a good pattern is:

1. Access ports get PortFast.
2. Those same edge ports get BPDU Guard.
3. Uplinks and trunks are documented separately.
4. Switch-to-switch links do not use PortFast as an ordinary access edge feature.
5. After BPDU Guard triggers, find the physical cause first, then restore the port.

Main idea:

```text
Default edge ports should be fast and protected.
Uplinks should be intentional and documented.
```

## Main Takeaway

PortFast and BPDU Guard solve a very real human problem.

People connect small switches, move cables, forget temporary fixes and create loops.

PortFast makes access ports fast for end devices.

BPDU Guard shuts down an edge port if it suddenly receives STP BPDUs.

Remember:

```text
PortFast for speed.
BPDU Guard for protection.
Use them together on edge ports.
```

This is a small configuration that can save the whole Layer 2 network from a very preventable outage.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| PortFast | Cisco STP feature that lets edge ports move to forwarding immediately. |
| BPDU Guard | Feature that err-disables a port if it receives a BPDU where it should not. |
| BPDU | Bridge Protocol Data Unit, STP control message sent between switches. |
| Err-disabled | Cisco port state where the switch disables an interface because of a protection event. |
| Edge port | Port intended for an end device, not another switch. |
| Unmanaged switch | Simple switch with no managed STP controls or enterprise safeguards. |

## Questions

### 1. Why should PortFast be used on end-device ports?

Answer:

Because end-device ports do not need the normal STP listening and learning delay. PortFast lets them reach forwarding quickly.

### 2. What does BPDU Guard do when an access port receives a BPDU?

Answer:

It places the port into an err-disabled state to prevent a possible Layer 2 loop or unauthorized switch connection.

### 3. Why are PortFast and BPDU Guard commonly deployed together?

Answer:

PortFast gives fast forwarding on edge ports, while BPDU Guard shuts the port down if that edge port starts behaving like a switch-facing link.

## What To Review Later

- PortFast edge behavior.
- BPDU Guard recovery.
- Err-disabled causes.
- Port security.
- Storm control.
- Proper access layer documentation.
