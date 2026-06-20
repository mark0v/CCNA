# Configuring VLAN Trunks

Source: closed course page  
Date added: 2026-06-20  
Related plan item: Week 8 / Configuring VLAN trunks  
Tags: VLAN, trunk port, 802.1Q, subnetting, allowed VLANs, show interfaces trunk
Language: English
Translation pair: articles/2026-06/week-08/06-configuring-vlan-trunks.md

## Summary

Creating a VLAN on one switch is not enough. If a VLAN must exist on multiple switches, its traffic has to be carried between them. That is what trunk ports are for.

A trunk port is a switch port that can carry traffic for multiple VLANs at the same time.

Key ideas:

- an access port belongs to one VLAN;
- a trunk port carries multiple VLANs;
- trunk links usually connect switches to each other;
- 802.1Q tagging identifies which VLAN a frame belongs to;
- a VLAN usually maps to a separate IP subnet;
- devices in the same VLAN and same subnet should communicate through a trunk;
- devices in different VLANs should not communicate without routing.

A trunk turns a VLAN from a local object on one switch into a logical network that can span multiple switches.

## A VLAN Is Not Just A Name

A VLAN is not just a label on ports.

A VLAN is a separate broadcast domain. In most practical designs, that broadcast domain maps to a separate IP subnet.

For example:

```text
VLAN 10 Admin:   10.0.18.0/27
VLAN 20 Patron:  10.0.18.32/27
```

If the store previously used one `/26`, and now two VLANs are required, that `/26` can be split into two `/27`s.

That preserves the larger addressing plan while creating two separate networks inside one site allocation.

Example:

```text
Original store subnet: 10.0.18.0/26

Split into:
10.0.18.0/27   -> Admin VLAN
10.0.18.32/27  -> Patron VLAN
```

The store remains inside its original block, but now it has logical separation.

## Why Subnetting Comes Back

VLANs and subnetting almost always go together.

If you create two VLANs, you usually need two IP subnets.

Otherwise, the design becomes strange: at Layer 2 you separated devices, but at Layer 3 you did not give them separate address spaces.

A good rule:

```text
One VLAN = one broadcast domain = one IP subnet
```

This is not just a phrase to memorize. It is a practical design habit.

A VLAN without the right subnet behind it is like a new room without walls. The name exists, but the separation is not real.

## What A Trunk Does

An access port is used for an endpoint device and belongs to one VLAN.

For example:

```text
PC port -> VLAN 10 only
Camera port -> VLAN 30 only
Printer port -> VLAN 20 only
```

A trunk port is used for infrastructure links.

For example:

```text
Switch 1 <-> Switch 2
Switch <-> Router
Switch <-> Firewall
Switch <-> Layer 3 switch
```

A trunk carries traffic for multiple VLANs:

```text
Trunk link carries VLAN 10, VLAN 20, VLAN 30, VLAN 99
```

That allows devices in the same VLAN to remain in the same logical network even when they connect to different switches.

## Configuring A Trunk Port

Basic command:

```text
Switch(config-if)# switchport mode trunk
```

This command puts the port into trunk mode.

If the trunk is configured between two switches, both sides of the link must be configured correctly.

Until the settings match on both sides, the link may briefly flap. In a lab, that is normal. In production, it can cause an outage, so changes like this should be planned.

## 802.1Q Tagging

When traffic crosses a trunk, the switch must know which VLAN each frame belongs to.

That is done with an 802.1Q tag.

Simple flow:

```text
Frame from VLAN 10 enters trunk
Switch adds 802.1Q VLAN tag
Frame crosses trunk
Next switch reads tag
Frame is placed back into VLAN 10
```

802.1Q is the industry standard for VLAN tagging.

The old Cisco proprietary option was called ISL. In modern normal networks, 802.1Q is the main standard.

## How To Prove The Trunk Works

It is important not only to configure the trunk, but to verify behavior.

Practical test:

1. Put a PC on Switch 1 into VLAN 10.
2. Put another PC on Switch 2 into VLAN 10.
3. Give both IP addresses from the same subnet.
4. Ping between them.

If the ping works, VLAN 10 traffic is crossing the trunk correctly.

Example:

```text
PC-A on Switch 1 -> VLAN 10 -> 10.0.18.10/27
PC-B on Switch 2 -> VLAN 10 -> 10.0.18.11/27

Ping should work.
```

This proves that VLAN 10 is not trapped on one switch. It is stretched across switches through the trunk.

## Verifying Separation

After that, verify the opposite behavior.

Move one PC into another VLAN, such as VLAN 20, and give it an address from another subnet.

```text
PC-A on Switch 1 -> VLAN 10 -> 10.0.18.10/27
PC-B on Switch 2 -> VLAN 20 -> 10.0.18.40/27

Ping should fail without routing.
```

If the ping stops working, that is good.

It means:

- VLAN separation works;
- devices are in different broadcast domains;
- traffic between VLANs does not pass without Layer 3 routing.

That is not a failure. That is the design.

## show interfaces trunk

After configuring a trunk, verify trunk state.

Command:

```text
Switch# show interfaces trunk
```

It helps you see:

- which ports are operating as trunks;
- which encapsulation is used;
- which VLANs are allowed on the trunk;
- which VLANs are active;
- which VLANs are forwarding.

This is one of the main commands for VLAN and trunk troubleshooting.

## Allowed VLAN List: The Command That Can Break Your Day

A trunk can carry many VLANs, but sometimes the allowed VLAN list should be limited.

That is useful:

- to avoid carrying unnecessary traffic;
- to reduce broadcast noise;
- to keep VLANs away from places where they are not needed;
- to improve security posture.

But there is a dangerous detail.

A command like:

```text
switchport trunk allowed vlan 10
```

does not add VLAN 10 to the list.

It replaces the allowed list and leaves only VLAN 10.

If VLAN 20, 30, 99, the management VLAN or the voice VLAN were crossing that trunk before, they can be cut off with one command.

To add, use `add`:

```text
switchport trunk allowed vlan add 10
```

To remove:

```text
switchport trunk allowed vlan remove 10
```

After any change, always verify:

```text
show interfaces trunk
```

This is one of those commands where a small syntax difference can become a large outage.

## Why VLAN Pruning Is Useful

In large networks, not every switch needs to see every VLAN.

For example, dorm VLAN traffic or guest VLAN traffic should not cross links where that VLAN has no devices.

Limiting allowed VLANs on trunks helps:

- reduce unnecessary broadcast traffic;
- limit VLAN reach;
- make the topology clearer;
- reduce the impact of a possible issue;
- improve security boundaries.

But pruning must be deliberate, documented and verified.

## What Was Proven In The Lesson

By the end of this lesson, two things were proven.

First: trunk links carry VLAN traffic between switches.

Second: devices in the same VLAN and same subnet can communicate across different switches when the trunk is configured correctly.

The opposite was also proven: devices in different VLANs do not communicate without inter-VLAN routing.

That is the desired behavior:

```text
Same VLAN + same subnet + trunk works -> communication works
Different VLANs + no routing -> communication fails
```

## What Comes Next

Trunks allow VLANs to span multiple switches.

But trunks do not let devices in different VLANs communicate with each other.

Communication between VLAN 10 and VLAN 20 requires Layer 3:

- router;
- Layer 3 switch;
- firewall.

This is called inter-VLAN routing.

We built the walls. Next, we carefully add the doors.

