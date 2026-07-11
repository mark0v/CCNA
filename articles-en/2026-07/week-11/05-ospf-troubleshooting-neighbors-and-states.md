# OSPF Troubleshooting: Neighbors And States

Source: closed course page  
Date added: 2026-07-11  
Related plan item: Week 11 / OSPF troubleshooting neighbors and states  
Tags: OSPF, troubleshooting, neighbor states, DR, BDR, LSDB, LSA, router ID
Language: English
Translation pair: articles/2026-07/week-11/05-ospf-troubleshooting-neighbors-and-states.md

## Summary

- OSPF troubleshooting starts with neighbors, not routes.
- If routers do not become neighbors, they do not exchange routing information.
- Neighbor states show where the OSPF process stopped.
- `Two-Way` is not always a problem; on broadcast networks it can be normal for non-DR/BDR peers.
- Good troubleshooting means reading protocol behavior, not randomly changing configuration.

## Key Points

- First command: `show ip ospf neighbor`.
- OSPF compatibility requires the same subnet, same area, same timers, matching authentication, and matching network type.
- States `Down`, `Init`, `Two-Way`, `Exstart`, `Exchange`, `Loading`, and `Full` help narrow down failure.
- DR/BDR election exists on broadcast networks to avoid update chaos.
- Router ID must be unique; duplicate router IDs break OSPF behavior.

## Notes

Memorizing commands only helps until the first real troubleshooting situation. With OSPF, it is important to understand protocol behavior, not just commands. If a route is missing, the first question should not be "why is the route missing?" It should be "do I have an OSPF neighbor?"

OSPF lives and dies by neighbors. Without a neighbor relationship, routers do not exchange link-state information, do not build a consistent LSDB, and do not install learned routes into the routing table.

Main sequence:

1. Check neighbors.
2. Look at neighbor state.
3. Understand where the process stopped.
4. Check the requirements for that stage.
5. Fix the specific mismatch.

## Neighbor Requirements

For OSPF routers to become neighbors, key parameters must match:

| Requirement | Why it matters |
| --- | --- |
| Same subnet | Routers must be Layer 3 neighbors on a shared segment. |
| Same area | The interface must be in the same OSPF area. |
| Same hello/dead timers | Routers must expect hellos with the same logic. |
| Matching authentication | If authentication is enabled, settings must match. |
| Matching network type | Point-to-point, broadcast, and other types affect adjacency behavior. |
| Unique router ID | Router ID is the router's identity in the OSPF domain. |

If one of these parameters does not match, adjacency may not form or may get stuck in a state.

## Neighbor States

OSPF neighbor relationships move through states:

| State | Meaning | Troubleshooting focus |
| --- | --- | --- |
| Down | No hellos received. | Interface, IP, OSPF enabled, physical/link status. |
| Init | Hello received, but the router does not see itself in the neighbor hello. | One-way communication, timers, ACLs, multicast reachability. |
| Two-Way | Routers see each other. | Normal on broadcast for non-DR/BDR; otherwise check next states. |
| Exstart | Routers choose master/slave for database exchange. | MTU mismatch often appears here. |
| Exchange | Routers exchange DBD summaries. | Database exchange problems. |
| Loading | Routers request missing LSAs. | LSR/LSU exchange, LSDB completion. |
| Full | LSDB synchronized. | Healthy full adjacency. |

These states are not trivia. They are a troubleshooting roadmap. If a neighbor is stuck in `Init`, the problem is usually before database exchange. If it is stuck in `Exstart`, think about MTU or negotiation problems. If `Two-Way` appears on a broadcast network with a non-DR/BDR peer, that can be normal.

## Two-Way Is Not Always Bad

On point-to-point links, you usually want to see `Full`. But on broadcast networks, OSPF elects a DR and BDR:

- DR: designated router;
- BDR: backup designated router.

The purpose of DR/BDR is to avoid making every router form a full adjacency with every other router. Otherwise, a shared segment would create too many update relationships.

So a router can be `Two-Way` with non-DR/BDR peers and `Full` with the DR/BDR. That is healthy behavior.

If you only memorize "Full is good," you can mistakenly treat normal `Two-Way` behavior as a problem.

## OSPF Packet Flow

Once routers are compatible, they exchange packets:

| Packet | Role |
| --- | --- |
| Hello | Discover and maintain neighbors. |
| DBD | Database Description, summary of LSDB contents. |
| LSR | Link-State Request, request for missing details. |
| LSU | Link-State Update, carries LSAs and changes. |
| LSAck | Acknowledges received LSAs. |

The DBD packet is a summary, not the entire LSDB. A router checks what it is missing, requests details through LSR, receives them through LSU, and acknowledges through LSAck.

Once this is clear, debug output stops being chaotic noise. You can see which phase the protocol is in: hello exchange, summary exchange, loading missing LSAs, or full synchronization.

## Commands To Use First

Start with the neighbor table:

```text
show ip ospf neighbor
```

Then check the process and interfaces:

```text
show ip protocols
show ip ospf interface brief
show ip ospf database
show running-config | section router ospf
show ip route ospf
```

`show ip protocols` shows active routing protocols, advertised networks, and useful process details.

`show ip ospf interface brief` shows which interfaces participate in OSPF, which area they are in, and what role they have.

`show ip ospf database` shows the LSDB. It is useful, but usually not the first command because output can be large.

## Clear OSPF Process

Command:

```text
clear ip ospf process
```

This restarts the OSPF process. It is useful in labs, for example after changing the router ID. But in production it is disruptive: neighbors drop, routes are relearned, and traffic can be affected briefly. Use it only with a clear understanding of impact.

## Router ID And DR/BDR

Router ID is the router's OSPF identity. If it is not manually configured, a Cisco router chooses:

1. Highest IP on a loopback interface.
2. If no loopback exists, highest IP on an active physical/logical interface.

Router IDs must be unique. A duplicate router ID can cause strange adjacency and LSDB behavior.

On broadcast networks, router ID participates in DR/BDR election along with OSPF priority. On point-to-point links, DR/BDR is not needed because there are only two routers on the segment.

## Troubleshooting Method

Correct pattern:

1. Do not change config immediately.
2. Check `show ip ospf neighbor`.
3. Identify the state.
4. Check requirements for that state.
5. Confirm interface participation.
6. Check router ID, area, timers, authentication, and network type.
7. Only then change configuration.

Troubleshooting is where book knowledge becomes real skill. Avoid panic-editing. Read the output calmly and make minimal precise changes.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `show ip ospf neighbor` | Shows OSPF neighbors and their states. |
| `show ip protocols` | Shows running routing protocols and advertised networks. |
| `show ip ospf interface brief` | Shows OSPF-enabled interfaces, areas, and roles. |
| `show ip ospf database` | Shows LSDB contents. |
| `clear ip ospf process` | Restarts OSPF process; disruptive in production. |
| DR | Designated router on broadcast segment. |
| BDR | Backup designated router. |
| Router ID | Unique OSPF identity for a router. |

## Questions

### 1. Why does OSPF troubleshooting start with neighbors?

Answer: Without a neighbor relationship, routers do not exchange OSPF information and cannot learn routes from each other.

### 2. Which parameters must match for OSPF adjacency?

Answer: Same subnet, same area, hello/dead timers, authentication, network type, and unique router IDs.

### 3. Why is `Two-Way` not always a bad state?

Answer: On broadcast networks, non-DR/BDR routers may remain Two-Way with each other while forming Full adjacency only with the DR/BDR.

### 4. What can being stuck in `Exstart` indicate?

Answer: It often points to an MTU mismatch or a database exchange negotiation problem.

### 5. Why is `clear ip ospf process` risky in production?

Answer: It resets the OSPF process, neighbors drop, routes are relearned, and this can cause a temporary outage.

## What To Review Later

- OSPF neighbor state machine.
- DR/BDR election rules.
- OSPF packet types: Hello, DBD, LSR, LSU, LSAck.
- Router ID selection.
- Safe OSPF troubleshooting workflow.
