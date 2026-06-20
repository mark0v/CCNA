# Finishing Cafe VLAN Port Assignments

Source: closed course page  
Date added: 2026-06-20  
Related plan item: Week 8 / Completing cafe VLAN implementation  
Tags: VLAN, access port, trunk port, WAP, dead VLAN, switch hardening, VLAN 1
Language: English
Translation pair: articles/2026-06/week-08/11-finishing-cafe-vlan-port-assignments.md

## Summary

A VLAN design is not finished until every switch port has the correct role.

You can create VLANs, configure router-on-a-stick, add DHCP pools and subinterfaces, and still have a broken network if ports remain in the default VLAN or operate in the wrong mode.

A complete VLAN implementation includes:

- trunks between switches;
- trunks to devices that carry multiple VLANs;
- access ports for endpoints;
- correct VLAN membership for every live device;
- disabled unused ports;
- a dead VLAN for unused ports;
- disabled trunk negotiation where it is not needed.

Main idea:

```text
VLAN exists as design only when switch ports enforce it.
```

## VLAN Does Not End With Creating The VLAN

Creating a VLAN:

```text
vlan 10
name ADMIN
```

is only the beginning.

Configuring a router subinterface:

```text
interface g0/0.10
encapsulation dot1Q 10
ip address ...
```

is also only part of the work.

For a device to actually belong to the right VLAN, the port it connects to must be assigned to that VLAN.

If a device is still plugged into a port in VLAN 1, it does not become part of VLAN 10 just because its IP address looks like the admin subnet.

Layer 2 membership and Layer 3 addressing must match.

## Access Ports And Trunk Ports

In this rollout, each port needs a role: access or trunk.

Access port:

```text
Carries one VLAN
Usually connects to endpoint
```

Trunk port:

```text
Carries multiple VLANs
Usually connects to infrastructure or multi-VLAN device
```

Examples of access ports:

- PC;
- printer;
- server with one VLAN;
- camera;
- POS terminal.

Examples of trunk ports:

- switch-to-switch link;
- switch-to-router link for ROAS;
- switch-to-firewall link with multiple VLANs;
- wireless access point with multiple SSIDs;
- virtualization host carrying multiple VLANs.

## A WAP Can Be A Trunk

WAP means Wireless Access Point.

It is similar to a switch for the air: wireless clients connect to it without a cable, but the AP still carries network traffic.

If a WAP serves one SSID and one VLAN, an access port may be enough.

But if the WAP will serve multiple SSIDs:

```text
Admin Wi-Fi  -> VLAN 10
Patron Wi-Fi -> VLAN 20
```

then the switch port to the WAP must carry traffic for multiple VLANs.

That is a trunk.

The AP tags traffic so the switch understands:

```text
This wireless client traffic belongs to VLAN 10.
This wireless client traffic belongs to VLAN 20.
```

Rule:

```text
One VLAN -> access
Multiple VLANs -> trunk
```

## Plex Server And Layer 2/Layer 3 Mismatch

A useful troubleshooting example is the Plex server.

It had an IP address from the admin network, but it still could not communicate.

Reason: the switch port it was connected to was still in VLAN 1.

This is a classic mistake:

```text
IP address looks correct
But switchport VLAN membership is wrong
```

Layer 3 says:

```text
This host belongs to admin subnet.
```

Layer 2 says:

```text
This port belongs to VLAN 1.
```

And the network does not line up.

After assigning the port as an access port in VLAN 10, connectivity returned:

```text
switchport mode access
switchport access vlan 10
```

## Why VLAN 1 Went Dark

Earlier, the IP address was removed from the physical router interface, and routing moved to subinterfaces.

That means default VLAN 1 no longer had a normal router path unless a separate subinterface/gateway was created for it.

Devices left in VLAN 1 became stranded.

In short:

```text
No router interface for VLAN 1
No default gateway path
Devices left in VLAN 1 lose connectivity
```

So live devices should not be left accidentally in VLAN 1.

## Subnet Mask Must Match Too

The server subnet mask also had to be corrected.

This is a common leftover after changes.

If a network was split into smaller subnets, a device may still hold the old mask.

For example:

```text
Old design: /26
New VLAN subnet: /27
```

If the host keeps the old mask, it may calculate local and remote addresses incorrectly.

After infrastructure changes, always verify:

- IP address;
- subnet mask;
- default gateway;
- VLAN membership;
- DHCP/static source;
- DNS;
- reachability.

## Unused Ports Are Not Safe By Default

An unused switch port is not just an empty port.

It is a potential access point.

If someone can plug a device into an open port and immediately get network access, that is a security risk.

Best practice for unused ports:

1. Set them as access ports.
2. Place them into an unused/dead VLAN.
3. Shut them down.

Example:

```text
vlan 999
name DEAD_UNUSED

interface range fa0/16 - 24
switchport mode access
switchport access vlan 999
shutdown
```

## Why Access Mode Even For Unused Ports

Even unused ports should be explicitly set as access ports.

Reason: if a port remains dynamic, it may try to negotiate a trunk through DTP.

If someone connects a switch or device that can negotiate a trunk, an unwanted trunk may appear.

So:

```text
switchport mode access
switchport access vlan 999
shutdown
```

That means the port:

- is physically down because of shutdown;
- goes to a dead VLAN if accidentally enabled;
- will not negotiate a trunk;
- will not provide access to production VLANs.

## Convenience Vs Security

In real networks, unused ports are not always locked down everywhere.

For example, in campus environments or offices where users constantly move desks, phones and docking stations, admins may leave ports active for convenience.

But in regulated or sensitive environments, auditors may ask:

```text
Why are unused ports active?
```

So the design depends on the environment.

If security matters more than convenience, unused ports should be locked down.

## What "VLAN Rollout Done" Means

By the end of the rollout, the cafe switch should have intentional behavior on every interface.

Example result:

```text
Switch-to-switch links -> trunks
Switch-to-router link  -> trunk
WAP uplinks            -> trunks
PC/server ports        -> access ports in correct VLANs
Unused ports           -> access ports in dead VLAN, shutdown
```

That is a complete VLAN implementation.

Not merely:

```text
VLANs exist.
```

But:

```text
Every port has a purpose.
Every live device belongs somewhere.
Every unused opening is treated as risk.
```

## Checklist

Before calling VLAN configuration complete, verify:

- VLANs are created and named;
- access ports are assigned to correct VLANs;
- trunk ports are configured where needed;
- WAP/multi-SSID links operate as trunks;
- router/firewall links operate as trunks if subinterfaces are used;
- devices received correct IP/subnet/gateway;
- hosts were not left accidentally in VLAN 1;
- unused ports are in a dead VLAN;
- unused ports are shut down;
- dynamic trunk negotiation is disabled where unnecessary;
- `show vlan` and `show interfaces trunk` confirm the design.

## Main Takeaway

The cafe VLAN rollout shows the difference between design and implementation.

Design says:

```text
Admin devices belong to VLAN 10.
Patron devices belong to VLAN 20.
```

Implementation proves it on every switch port.

If a port is not assigned correctly, the design remains only a diagram.

The network behaves correctly only when:

- Layer 2 VLAN membership;
- Layer 3 addressing;
- default gateway;
- trunk/access roles;
- security posture

agree with each other.

Now the cafe network is a clean proving ground, and the same ideas can be carried into the larger Fallout Shelter topology.

