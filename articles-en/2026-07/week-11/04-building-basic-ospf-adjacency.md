# Building Basic OSPF Adjacency

Source: closed course page  
Date added: 2026-07-11  
Related plan item: Week 11 / Building basic OSPF adjacency  
Tags: OSPF, adjacency, WAN, Area 0, network command, passive interface, LSDB, troubleshooting
Language: English
Translation pair: articles/2026-07/week-11/04-building-basic-ospf-adjacency.md

## Summary

- After dynamic routing theory, the next step is building the first working OSPF adjacency.
- In the lab topology, the cafe router and fallout shelter router are connected through a point-to-point WAN link.
- A `/30` is convenient for a WAN link because only two usable IP addresses are needed.
- The OSPF `network` command enables the protocol on matching interfaces and advertises connected networks.
- First troubleshooting lesson: if adjacency does not form, check interface IPs, network statements, and OSPF hellos.

## Key Points

- OSPF lets routers learn routes automatically instead of relying on static routes.
- Area 0 is the backbone area and the right starting point for a simple OSPF design.
- Targeted `network <interface-ip> 0.0.0.0 area 0` reduces accidental interface matching.
- Passive interface is useful for VLANs that should be advertised but should not form OSPF neighbors.
- `show ip ospf neighbor`, `show ip route ospf`, and debug output help find mistakes quickly.

## Notes

Dynamic routing theory becomes useful only when routers actually start exchanging routes. The goal here is simple: connect two routed parts of the Castle Rysen/NetworkChuck Coffee environment and bring up the first OSPF neighbor relationship.

Topology:

- cafe router;
- fallout shelter router;
- WAN link between them;
- cafe admin VLAN;
- cafe patron VLAN;
- fallout shelter VLANs.

Design choice: advertise only the networks that need to be known. The cafe admin VLAN should be reachable from other sites because it contains management systems, servers, and important infrastructure. The patron VLAN is guest/BYOD traffic, and the fallout shelter does not need direct awareness of it.

## WAN Link

The point-to-point WAN link uses subnet `172.16.0.0/30`.

`/30` works well for router-to-router links:

| Address | Role |
| --- | --- |
| `172.16.0.0` | Network address. |
| `172.16.0.1` | Cafe router WAN IP. |
| `172.16.0.2` | Fallout shelter router WAN IP. |
| `172.16.0.3` | Broadcast address. |

That gives exactly two usable addresses: one for each router. A point-to-point link usually does not need more.

Practical tip: keep WAN links in a separate address range, such as `172.16.0.0/16`, while LAN/VLAN networks live in `10.0.0.0/8`. Then when reading a routing table, a `172.x` address immediately looks like a transit/WAN segment.

## Basic OSPF Enablement

OSPF starts with a process ID:

```text
router ospf 1
```

The process ID is local to the router. It does not need to match between neighbors, but labs often keep it the same for clarity.

Next, choose the interfaces where OSPF should run. The targeted style uses an exact interface IP with wildcard `0.0.0.0`:

```text
router ospf 1
 network 172.16.0.1 0.0.0.0 area 0
 network 10.0.18.1 0.0.0.0 area 0
```

This approach says: match exactly the interface with this IP. It helps avoid accidentally enabling OSPF on extra interfaces.

On the other side of the WAN link:

```text
router ospf 1
 network 172.16.0.2 0.0.0.0 area 0
```

When both routers enable OSPF on their WAN interfaces in the same area, they begin sending hello packets. If parameters are compatible, an OSPF neighbor adjacency forms.

## Area 0

OSPF uses areas. An area is a logical chunk of OSPF topology where routers share the same link-state database.

Area 0 is the backbone area. In a simple design and first lab, the logical choice is to place both routers in Area 0:

```text
network 172.16.0.1 0.0.0.0 area 0
```

Multi-area OSPF comes later, when the topology grows and the LSDB becomes too large. At the start, Area 0 is enough.

Mental model:

> An OSPF area is a neighborhood map. Routers inside the area have the same map, but each calculates its best path from its own starting point.

## Passive Interfaces

The cafe admin VLAN should be advertised, but it does not need an OSPF neighbor. The interface can be made passive:

```text
router ospf 1
 passive-interface g0/0.18
```

This stops OSPF hello packets on the admin VLAN, but the connected network is still advertised into OSPF.

For user-facing or server-facing VLANs, this is a normal pattern:

- advertise the subnet;
- do not form neighbors;
- reduce noise;
- reduce attack surface.

## Troubleshooting First Adjacency

If the neighbor does not appear, do not guess. Check:

```text
show ip ospf neighbor
show ip interface brief
show running-config | section router ospf
show ip protocols
show ip route ospf
```

Common causes:

- OSPF network statement matched the wrong interface IP;
- interfaces are in different OSPF areas;
- WAN interface is down/down or administratively down;
- IP addresses are not in the same subnet;
- hello/dead timers mismatch;
- passive-interface accidentally applied to the WAN interface;
- authentication mismatch, if configured.

Debug can show live protocol activity:

```text
debug ip ospf events
```

Use debug carefully in production. It can be noisy and affect router CPU.

Main lesson: troubleshooting is not a separate part of networking. It is networking. Copying commands is not enough. You need to read output, find the mismatch, and correct the configuration.

## What Was Accomplished

After correct configuration:

- cafe router and fallout shelter router become OSPF neighbors;
- routers dynamically exchange routing information;
- fallout shelter sees the cafe admin VLAN as an OSPF-learned route;
- the routing table receives routes through the protocol, not static config;
- there is now a foundation for further OSPF tuning.

On the fallout shelter side, a broad network statement can advertise several VLANs at once, but this requires discipline. Just because you can advertise everything does not mean you should. Later, the design should be refined with route control, summarization, and more precise statements.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `router ospf 1` | Starts OSPF process 1 on the local router. |
| `network 172.16.0.1 0.0.0.0 area 0` | Enables OSPF on exact interface IP and places it in Area 0. |
| `passive-interface g0/0.18` | Stops hellos on that interface while still advertising its connected network. |
| `show ip ospf neighbor` | Verifies OSPF neighbor relationships. |
| `show ip route ospf` | Shows OSPF-learned routes in the routing table. |
| Area 0 | OSPF backbone area. |
| LSDB | Link-state database, OSPF topology information inside an area. |

## Questions

### 1. Why is `/30` useful for a point-to-point WAN link?

Answer: It provides exactly two usable IP addresses, one for each router endpoint.

### 2. Why is targeted `network <ip> 0.0.0.0 area 0` useful?

Answer: It matches the exact interface IP, reducing the risk of accidentally enabling OSPF on the wrong interface.

### 3. Why make the admin VLAN passive?

Answer: To advertise the subnet into OSPF without sending hello packets or forming neighbors on a user/server-facing segment.

### 4. What is an OSPF adjacency?

Answer: It is a neighbor relationship between routers that exchange OSPF information and participate in the same routing domain.

### 5. What should you check first if adjacency does not form?

Answer: Interface status, IP addressing, OSPF network statements, area ID, passive-interface, and `show ip ospf neighbor`.

## What To Review Later

- OSPF neighbor states.
- OSPF hello/dead timers.
- Area 0 and multi-area design.
- Route summarization in OSPF.
- Safer troubleshooting with `show` commands before debug.
