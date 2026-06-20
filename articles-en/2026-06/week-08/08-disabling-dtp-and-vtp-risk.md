# Disabling DTP And VTP Risk

Source: closed course page  
Date added: 2026-06-20  
Related plan item: Week 8 / VLAN-related Cisco protocols and hardening  
Tags: DTP, VTP, VLAN, trunking, Cisco, switch hardening, VLAN hopping
Language: English
Translation pair: articles/2026-06/week-08/08-disabling-dtp-and-vtp-risk.md

## Summary

Some Cisco features were created for convenience, but in modern production networks they are often disabled.

Two important examples:

- DTP - Dynamic Trunking Protocol;
- VTP - VLAN Trunking Protocol.

Both protocols are Cisco proprietary. Both were designed as automation. Both can create unnecessary risk if left uncontrolled.

Practical takeaway:

```text
Access ports should be access ports.
Trunk ports should be trunk ports.
VLAN databases should not magically change across the network.
```

The less guessing and hidden automation there is, the easier troubleshooting becomes and the smaller the attack surface is.

## DTP: Negotiating Trunk Mode

DTP means Dynamic Trunking Protocol.

It lets switch ports negotiate whether they should become a trunk link.

A trunk link carries traffic for multiple VLANs. An access port belongs to one VLAN.

The DTP idea sounds convenient:

```text
Switch ports negotiate automatically.
If trunk is needed, trunk forms.
```

But in a real network, that is often not the behavior you want.

If an engineer wants a trunk, the engineer can configure a trunk explicitly:

```text
switchport mode trunk
```

If an engineer wants an access port, the engineer can configure access explicitly:

```text
switchport mode access
```

The network is easier to understand when port behavior is intentional.

## DTP Modes

DTP uses negotiation modes.

Main ideas:

```text
dynamic auto       -> I can become trunk if the other side asks
dynamic desirable  -> I want to become trunk
trunk              -> I am trunk
access             -> I am access
```

Behavior examples:

```text
desirable + auto       -> trunk forms
desirable + desirable  -> trunk forms
auto + auto            -> trunk does not form
```

For the exam, these combinations matter.

For real work, it is usually simpler to remove negotiation and configure the port mode manually.

## Why DTP Can Be Dangerous

If DTP is enabled on a user-facing port, a rogue device may try to negotiate a trunk.

That matters because a trunk can carry traffic for multiple VLANs.

Scenario:

1. An attacker connects a device to an open wall jack.
2. The port is left in dynamic mode.
3. The device attempts to negotiate a trunk.
4. If a trunk forms, the attacker may try to access VLANs they should never touch.

This is related to VLAN hopping risk.

VLAN hopping is a situation where a device tries to reach VLANs it should not access.

## switchport nonegotiate

The command that disables DTP negotiation on an interface is:

```text
switchport nonegotiate
```

After this, the port does not try to negotiate trunk mode.

Typical approach for an access port:

```text
interface FastEthernet0/10
 switchport mode access
 switchport access vlan 20
 switchport nonegotiate
```

For a trunk port:

```text
interface GigabitEthernet0/1
 switchport mode trunk
 switchport nonegotiate
```

Important: if negotiation is disabled, both sides of a trunk must be configured explicitly.

## Practical Rule For DTP

On production switches, hard-code port behavior:

```text
User-facing ports -> access
Infrastructure links -> trunk
Unused ports -> shutdown
```

The idea is simple: a port should do what you configured it to do, not discuss it with an unknown device.

This helps:

- reduce ambiguity;
- make troubleshooting faster;
- reduce accidental trunk risk;
- reduce attack surface;
- make configuration easier to read.

## VTP: The Name Is Misleading

VTP means VLAN Trunking Protocol.

The name can be confusing: VTP is not the trunking method.

The trunking method for VLAN traffic is 802.1Q tagging.

VTP does something else: it propagates the VLAN database between switches.

For example:

```text
Create VLAN 10 on one switch
VTP advertises VLAN 10
Other switches learn/create VLAN 10
```

The idea was convenient: create once, replicate everywhere.

The problem is that VTP can propagate not only creation, but also deletion.

## Why VTP Can Be Risky

In a large network, automatic VLAN database propagation can be dangerous.

One wrong switch or one wrong VLAN deletion can affect many switches.

Common unpleasant scenarios:

- someone deletes a VLAN on a switch participating in VTP as a server;
- the deletion propagates through the VTP domain;
- the VLAN disappears on other switches;
- ports lose their logical networks;
- users, phones, servers or management connectivity break.

Another scenario:

- an old lab switch is connected to production;
- it still has a different VLAN database;
- it participates in VTP;
- the network receives unexpected VLAN updates.

Automation is convenient until it automates a mistake.

## VTP Modes

Traditionally, VTP has three main modes.

### Server

The switch can:

- create VLANs;
- delete VLANs;
- modify the VLAN database;
- advertise those changes to other switches.

On many older switches, server was the default mode, which is part of why VTP caused so much pain.

### Client

The switch:

- receives VTP updates;
- applies the VLAN database from servers;
- cannot create or delete VLANs locally.

This sounds safer, but the switch still depends on updates.

### Transparent

The switch:

- manages its VLAN database locally;
- does not apply received VTP updates to its own VLAN database;
- does not advertise its VLAN changes like a server.

Transparent mode is often preferred in modern networks.

Command:

```text
vtp mode transparent
```

## VTP Domain

A VTP domain is a name that defines which switches should exchange VTP information.

Important: the domain name is case-sensitive.

For example:

```text
COOKIE
cookie
```

These are different domains.

But even a domain boundary does not remove the main operational risk: if you do not want automatic VLAN database propagation, do not rely on VTP.

## What To Usually Do In Production

Practical approach:

```text
DTP:
  Manually set access/trunk mode
  Disable negotiation where appropriate

VTP:
  Use transparent mode unless there is a deliberate reason not to
```

Examples:

```text
switchport mode access
switchport nonegotiate
```

```text
switchport mode trunk
switchport nonegotiate
```

```text
vtp mode transparent
```

The goal is not to disable everything blindly. The goal is to remove automation that is not controlled and not needed for the design.

## Exam Vs Real World

For the exam, know:

- what DTP is;
- what VTP is;
- DTP modes and when a trunk forms;
- VTP modes;
- what `switchport nonegotiate` does;
- what `vtp mode transparent` does;
- that 802.1Q handles tagging, not VTP.

For the real world, you also need judgment:

```text
Just because a feature exists does not mean it should be enabled.
```

Sometimes professional design is boring design:

- explicit port modes;
- no unnecessary negotiation;
- predictable VLAN database;
- documented trunks;
- checked allowed VLANs;
- fewer surprises.

## Main Takeaway

DTP and VTP were created for convenience, but convenience can become risk.

DTP can accidentally or unexpectedly turn a port into a trunk.

VTP can propagate VLAN changes where you did not intend them to go.

So the practical baseline is:

```text
Hard-code access ports.
Hard-code trunk ports.
Disable DTP negotiation where appropriate.
Use VTP transparent unless VTP is intentionally designed and controlled.
```

A good network is often boring in the best way: it does exactly what the config says and does not try to be smarter than the engineer.

