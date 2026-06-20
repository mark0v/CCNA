# Creating VLANs And Access Ports

Source: closed course page  
Date added: 2026-06-20  
Related plan item: Week 8 / Creating VLANs and assigning access ports  
Tags: VLAN, access port, Cisco switch, SVI, switchport, VLAN 1, DTP
Language: English
Translation pair: articles/2026-06/week-08/05-creating-vlans-and-access-ports.md

## Summary

A VLAN becomes real not when you understand the idea, but when you create the VLAN on a switch, give it a name and assign ports to it.

This lesson introduces the practical foundation:

- VLAN 1 already exists on a Cisco switch by default;
- new VLANs are created in global configuration mode;
- VLANs should be given clear names;
- `show vlan` displays created VLANs and assigned ports;
- an access port belongs to one VLAN;
- `switchport mode access` fixes a port as an access port;
- `switchport access vlan <id>` assigns a port to a specific VLAN;
- dynamic switchport mode should not be left on user-facing ports.

The main idea: a VLAN without assigned ports is only an empty logical room. Separation appears when switchports are actually placed into different VLANs.

## Business Requirements Do Not Always Say "Make A VLAN"

In real work, you will rarely be told:

```text
Configure VLANs.
```

More often, the business request sounds like this:

```text
Separate guest devices from administrative devices.
Create a security boundary between customer traffic and internal systems.
Keep cameras, servers, network gear and guest users apart.
```

An engineer has to translate that into network design.

For NetworkChuck Coffee, that means:

- patron devices should not live with admin systems;
- the guest side should not have open access to infrastructure;
- cameras, servers and network gear should be separated from normal users;
- the same physical switch can serve different logical groups.

The Layer 2 tool for that separation is a VLAN.

## VLAN 1 Already Exists

On a Cisco switch, VLANs exist out of the box.

By default, all normal switchports are in VLAN 1.

That explains the basic behavior:

```text
All ports in VLAN 1
All devices in same default broadcast domain
Switch management SVI often tied to VLAN 1
```

SVI means Switch Virtual Interface.

It is a virtual interface tied to a VLAN that lets the switch have an IP address for management.

For example, if the switch has a management IP on VLAN 1, and devices are connected to ports in VLAN 1, those devices can reach the switch management address if the IP settings match.

Important: an SVI is not a physical port. It is a logical interface that belongs to a VLAN.

## Creating A VLAN

To create a VLAN on a Cisco switch, use global configuration mode.

Example:

```text
Switch(config)# vlan 10
Switch(config-vlan)# name ADMIN_DEVICES
```

Another VLAN:

```text
Switch(config)# vlan 20
Switch(config-vlan)# name PATRON_DEVICES
```

The `vlan 10` command creates VLAN 10 or enters its configuration mode if it already exists.

The `name` command gives it a human-readable name.

Technically, a VLAN can exist only as a number, but names help a lot in real work.

Compare:

```text
VLAN 10
VLAN 20
```

with:

```text
VLAN 10 ADMIN_DEVICES
VLAN 20 PATRON_DEVICES
```

The second version is easier to read, easier to document and easier to troubleshoot.

## Verifying With show vlan

After creating VLANs, verify that the switch sees them.

Command:

```text
Switch# show vlan
```

It displays:

- VLAN ID;
- VLAN name;
- status;
- ports assigned to the VLAN.

Important point: right after creation, a VLAN may be empty.

It exists and has a name, but no ports have been assigned to it yet.

That is like building rooms but moving nobody into them.

## Assigning Ports To A VLAN

Separation starts working when switchports are assigned to VLANs.

For one port:

```text
Switch(config)# interface fastEthernet 0/10
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 20
```

For multiple ports, use an interface range:

```text
Switch(config)# interface range fastEthernet 0/10 - 15
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 20
```

What these commands do:

```text
switchport mode access
```

This fixes the port as an access port. The port belongs to one VLAN.

```text
switchport access vlan 20
```

This assigns the access port to VLAN 20.

After that, ports `Fa0/10 - Fa0/15` are no longer part of default VLAN 1. They belong to VLAN 20.

If a client connects to one of these ports, it lives in VLAN 20.

## Access Port

An access port is a switchport intended for an endpoint device.

Common access-port devices include:

- PC;
- laptop;
- printer;
- IP phone;
- camera;
- access point in simple mode;
- POS terminal.

An access port carries traffic for one VLAN.

The client device usually does not know about VLAN tagging. To the client, the port looks like a normal Ethernet connection.

Inside the switch, the switch understands:

```text
This frame came from access port in VLAN 20.
Therefore this traffic belongs to VLAN 20.
```

## Why Dynamic Mode Should Not Be Left Alone

On many Cisco switches, ports may use a dynamic mode by default.

This is related to DTP, Dynamic Trunking Protocol.

The idea of dynamic mode is that a port can negotiate whether it should act as an access port or a trunk port.

That sounds convenient, but it is a bad habit for user-facing ports.

Why:

- port behavior becomes less predictable;
- another switch may try to negotiate a trunk;
- a trunk carries traffic for multiple VLANs;
- VLAN hopping or another unwanted access path becomes a risk;
- the security boundary becomes weaker.

It is better to state intent explicitly:

```text
User-facing port -> switchport mode access
Switch-to-switch link -> switchport mode trunk
```

No guessing.

## VLAN Hopping In General Terms

VLAN hopping is an attack or unwanted situation where a device tries to access VLANs it should not reach.

One risk is related to a port becoming a trunk when dynamic negotiation is allowed.

If an attacker connects a device that can pretend to be a switch, the port may negotiate trunk mode. Then traffic for multiple VLANs can cross that link.

That is why user access ports should be fixed:

```text
switchport mode access
```

And assigned only to the required VLAN:

```text
switchport access vlan 20
```

## What Was Done In The Lesson

This lesson performed three main actions.

First: confirmed that VLANs already exist on the switch through default VLAN 1.

Second: created and named new VLANs:

```text
VLAN 10 ADMIN_DEVICES
VLAN 20 PATRON_DEVICES
```

Third: assigned a range of ports to the patron VLAN as access ports:

```text
interface range fastEthernet 0/10 - 15
switchport mode access
switchport access vlan 20
```

After that, devices connected to those ports are in VLAN 20, not VLAN 1.

## Why You Should Not Move Everything Yet

If VLANs are created only on one switch and trunk links between switches are not configured yet, connectivity can be broken accidentally.

For example:

```text
Device A in VLAN 20 on Switch 1
Device B in VLAN 20 on Switch 2
```

If there is no trunk between the switches, VLAN 20 traffic cannot properly cross between them.

That creates separation without the required connectivity.

So order matters:

1. Create VLANs.
2. Assign access ports.
3. Configure trunk links between switches.
4. Verify VLAN propagation and traffic.
5. Only then move production devices in bulk.

## Main Takeaway

Creating a VLAN is only the first step.

Real separation appears when:

- the VLAN is created;
- the VLAN is named;
- ports are configured as access;
- access ports are placed into the correct VLAN;
- dynamic behavior is disabled where it is not needed;
- trunk links are ready to carry VLANs between switches.

Short reminder:

```text
vlan 20
name PATRON_DEVICES

interface range fa0/10 - 15
switchport mode access
switchport access vlan 20

show vlan
```

This is the minimum practical foundation for VLAN configuration.

Next, trunk links must be configured so VLANs can span multiple switches.

