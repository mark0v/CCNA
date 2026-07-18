# Configuring HSRP With Failover Testing

Source: closed course page  
Date added: 2026-07-18  
Related plan item: Week 12 / Configuring HSRP with failover testing  
Tags: HSRP, first hop redundancy, default gateway, NAT, OSPF, failover, preempt, interface tracking
Language: English
Translation pair: articles/2026-07/week-12/01-configuring-hsrp-with-failover-testing.md

## Summary

- HSRP gives hosts one stable default gateway, even when the physical router changes.
- The `standby` commands cannot save a design if routing, NAT, trunks, and VLAN subinterfaces are not already correct.
- In HSRP, the active router answers for the virtual IP, and the standby router is ready to take over.
- Priority chooses the active router; preempt lets the preferred router take the active role back after recovery.
- Failover should be tested in practice with pings, NAT translations, HSRP state, and a controlled link failure.
- Interface tracking is needed so a router does not stay active after losing a critical upstream link.

## Key Points

- HSRP is Cisco Hot Standby Router Protocol.
- First hop redundancy protects the first Layer 3 hop for hosts, usually their default gateway.
- Separate the physical router IPs from the gateway IP: routers keep real IPs, hosts use a virtual IP.
- HSRPv2 is enabled with `standby version 2`.
- Higher priority wins; default priority is 100.
- If priorities tie, the higher interface IP wins.
- `preempt` lets the preferred router retake the active role after recovery.

## Notes

HSRP often looks like a small configuration: a few commands on an interface, a virtual IP, priority, and preempt. The real work starts before that. The second router must already have internet reachability, VLAN visibility, routing participation, and NAT.

If that foundation is broken, HSRP only makes a bad design look cleaner. Redundancy has to work end to end, not just in one part of the diagram.

## Before HSRP: Plumbing First

In the lab, the second internet connection was emulated with a switch. For Packet Tracer, that is convenient: it lets you show two WAN handoffs and test router behavior.

In the real world, do not treat that as a finished design. If both "redundant" circuits arrive through the same carrier, the same building entrance, or the same physical path, one construction accident can take both down. A second circuit should be as independent as the budget and location allow.

Before HSRP, prepare the second router:

- WAN-facing interface;
- default route toward the ISP;
- router-on-a-stick subinterfaces for VLANs;
- trunk to the switch;
- OSPF or another routing exchange with the rest of the network;
- NAT for inside networks.

HSRP does not replace routing or NAT. It only gives end devices a virtual default gateway they can trust.

## The Default Gateway Problem

The problem is simple: a PC in VLAN 10 uses default gateway `10.0.16.1`. If that IP lives only on Router 1, then when Router 1 fails, the PC keeps sending traffic to a dead gateway.

The host will not decide to use Router 2 by itself. To the host, the default gateway is a specific IP address.

HSRP solves this with a virtual IP:

- Router 1 has its own real interface IP;
- Router 2 has its own real interface IP;
- hosts use one shared virtual gateway IP;
- the active router answers for that virtual IP;
- the standby router waits and takes over during failure.

Practical addressing pattern:

| Address role | Example |
| --- | --- |
| HSRP virtual IP | `10.0.16.1` |
| Router 1 real IP | `10.0.16.2` |
| Router 2 real IP | `10.0.16.3` |

Clients keep the gateway address they expect, but that address is no longer tied to one physical router.

## HSRPv2 Configuration Pattern

HSRP is configured separately on each VLAN subinterface. A simple convention is to make the HSRP group number match the VLAN number.

Example for VLAN 10 on the preferred router:

```text
interface g0/0.10
 encapsulation dot1Q 10
 ip address 10.0.16.2 255.255.255.0
 standby version 2
 standby 10 ip 10.0.16.1
 standby 10 priority 105
 standby 10 preempt
```

Example for VLAN 10 on the standby router:

```text
interface g0/0.10
 encapsulation dot1Q 10
 ip address 10.0.16.3 255.255.255.0
 standby version 2
 standby 10 ip 10.0.16.1
 standby 10 preempt
```

The same logic repeats for the other VLANs. Each subnet gets its own virtual gateway IP and its own HSRP group.

## Priority And Preempt

HSRP priority decides which router becomes active.

| Rule | Meaning |
| --- | --- |
| Higher priority wins | Router with larger priority becomes active. |
| Default priority is 100 | If you do nothing, both routers start equal. |
| Tie uses higher IP | If priorities match, higher interface IP wins. |
| Preempt restores preference | Higher-priority router can take active role back. |

In the lab, Router 1 received priority `105`, while Router 2 stayed at the default `100`. Router 1 became active, and Router 2 became standby.

Without `preempt`, failover may work, but failback may not match the design. Router 1 can return after an outage and still not become active again. If the design says Router 1 should be primary, enable preempt intentionally.

## Virtual MAC And ARP

To the host, everything looks like one gateway. It sends ARP for `10.0.16.1` and receives a virtual MAC address tied to the HSRP group.

That is why the host does not need to be reconfigured during failover. The gateway IP stays the same, the virtual MAC represents the logical gateway identity, and the routers decide which one currently answers.

This is an important troubleshooting detail. If you inspect an ARP cache or MAC address table and see an HSRP virtual MAC, that is not an error. It is the mechanism that makes gateway redundancy transparent to hosts.

## Testing Failover

Redundancy without testing is an assumption.

Minimum test plan:

1. Start a continuous ping from a client to an internet destination.
2. Verify that Router 1 is active for HSRP.
3. Verify NAT translations on Router 1.
4. Disable the path to Router 1 in a controlled way.
5. Confirm that Router 2 becomes active.
6. Confirm that NAT translations appear on Router 2.
7. Restore Router 1.
8. Confirm that preempt returns Router 1 to the active role.

Useful commands:

```text
show standby brief
show ip nat translations
show ip route
show ip ospf neighbor
```

During a normal failover, a few pings may drop. The important result is that traffic recovers, the standby router becomes active, and the primary router returns in a controlled way.

## Interface Tracking

There is a dangerous scenario: a router remains alive on the LAN side but loses its internet-facing interface. Hosts can still see the gateway, HSRP may still consider the router active, but outbound traffic does not work.

Interface tracking exists for this case.

The idea is simple: if a critical upstream interface goes down, the router lowers its HSRP priority. Then the standby router with a working upstream path becomes active.

Conceptual example:

```text
track 1 interface g0/1 line-protocol

interface g0/0.10
 standby 10 track 1 decrement 20
```

If the tracked interface goes down, priority drops. The router that was preferred stops being the best choice, and traffic moves to the router that is actually healthy.

## NetworkChuck Coffee Design View

For NetworkChuck Coffee, this is not an exam trick. If the edge router fails during the morning rush, POS systems, online orders, staff devices, and payment traffic should keep working.

Users do not care which router is active. They need the default gateway to answer, the internet to work, and the business process to keep moving.

Main idea: HSRP is not really about routers. It is about hosts having a working default gateway during failure.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `standby version 2` | Enables HSRPv2 on the interface. |
| `standby 10 ip 10.0.16.1` | Sets HSRP group 10 virtual gateway IP. |
| `standby 10 priority 105` | Makes this router more preferred than default 100. |
| `standby 10 preempt` | Allows this router to retake active role after recovery. |
| `show standby brief` | Shows HSRP groups, states, active and standby routers. |
| `show ip nat translations` | Verifies which router is translating traffic. |
| Active router | Router currently forwarding for the virtual gateway. |
| Standby router | Router ready to take over the virtual gateway. |
| Virtual IP | Default gateway IP used by hosts. |
| Interface tracking | Lowers priority when a critical interface fails. |

## Questions

### 1. What problem does HSRP solve?

Answer: It gives hosts a resilient default gateway, so they do not depend on one physical router.

### 2. Why configure routing and NAT before HSRP?

Answer: HSRP only handles gateway redundancy. The backup router still needs working routing, trunks, VLAN subinterfaces, and NAT.

### 3. Why use a virtual IP as the host default gateway?

Answer: The host can keep one gateway address while different physical routers take ownership behind the scenes.

### 4. What does `preempt` do?

Answer: It lets the higher-priority router take the active role back after it recovers.

### 5. Why is interface tracking important?

Answer: It prevents a router with a failed upstream link from staying active just because its LAN interface is still up.

## What To Review Later

- HSRPv1 vs HSRPv2 differences.
- HSRP virtual MAC format.
- `show standby brief` output.
- NAT behavior during gateway failover.
- Interface tracking with priority decrement.
