# Categories Of Routing Protocols

Source: closed course page  
Date added: 2026-07-11  
Related plan item: Week 11 / Categories of routing protocols  
Tags: routing protocols, IGP, EGP, distance vector, link state, path vector, OSPF, BGP
Language: English
Translation pair: articles/2026-07/week-11/01-categories-of-routing-protocols.md

## Summary

- Routing protocol categories matter for more than the exam; they explain network behavior during failures.
- The first major split is IGP for routing inside an organization and EGP for routing between organizations.
- Distance vector protocols learn through neighbors and do not keep a complete network map.
- Link state protocols build broader topology knowledge and usually converge faster.
- Path vector is the category for BGP, where path information and policy matter more than just "the shortest road."

## Key Points

- IGP operates inside one administrative domain.
- EGP operates between administrative domains; the main example is BGP.
- Distance vector is simpler and lighter, but can react to changes more slowly or with less complete visibility.
- Link state uses more CPU and memory, but gives routers more topology awareness.
- BGP is used where scale, route control, and policy matter.

## Notes

Routing protocol categories can look like dry certification trivia. In practice, they explain how a protocol behaves under load, during failure, and while troubleshooting.

The commands that enable a routing protocol are useful only until the first outage. When the network stops working, the architecture matters more: how the protocol learns routes, how it chooses the best path, how quickly it converges, and how much of the network it can see.

At NetworkChuck Coffee, this quickly becomes practical. When multiple locations, partner networks, ISP handoffs, and cloud connections appear, routing is no longer "just a route table." Card payments, online orders, inventory systems, and inter-store communication depend on it.

## IGP vs EGP

The first level of classification:

| Category | Meaning | Example |
| --- | --- | --- |
| IGP | Interior Gateway Protocol, works inside an organization. | OSPF, EIGRP, RIP, IS-IS |
| EGP | Exterior Gateway Protocol, works between organizations. | BGP |

IGP is used inside your own network. For example, NetworkChuck Coffee routing between back office, POS systems, security cameras, warehouse networks, and branch cafes is internal routing. The routers need to exchange routes inside one controlled environment.

EGP is used between organizations or administrative domains. The main EGP is BGP, Border Gateway Protocol. It is the routing protocol of the internet, but it is useful beyond internet providers. If NetworkChuck Coffee connects to a partner network and should exchange only approved routes, BGP provides that control.

Main idea: IGP handles the company's internal roads; EGP handles controlled route exchange beyond the company.

## Distance Vector: Routing By Rumor

Distance vector protocols can be described as routing by rumor. The router does not build a complete map of the entire network. It listens to neighbors and learns: "to reach that destination, send traffic through me."

The advantage is simplicity and lower resource cost. The router does not need to store the whole topology or perform complex calculations. That can be useful in small or constrained environments.

The downside is limited visibility. If a router sees the network only through neighbor updates, changes may spread gradually. During failures, that can produce delayed convergence or strange routing behavior until all routers receive current information.

Classic examples:

- RIP;
- EIGRP.

For troubleshooting, do not only ask whether the route exists. Ask how it was learned. If the route came from a distance vector protocol, look at neighbor relationships, update timing, and the possibility of incomplete information.

## Link State: Routing By Map

Link state protocols work differently. The router receives more topology information and builds a broader picture of the network. Instead of "my neighbor said go that way," the router understands the layout and calculates the best path itself.

The main CCNA example is OSPF, Open Shortest Path First. IS-IS also exists and is common in some large provider or enterprise environments, but CCNA usually focuses on OSPF.

Benefits of link state:

- routers see more of the network topology;
- changes are usually handled faster;
- convergence is often better;
- path calculation is more informed.

Cost:

- more CPU usage;
- more memory usage;
- more complexity.

This is not magic; it is a tradeoff. Link state provides better visibility and faster decisions, but it needs more resources and careful design.

## Path Vector: BGP And Policy

BGP sits in the path vector category. It does not build a complete map of the internet like a link state protocol because the internet is too large. Instead, BGP works with path information and policy.

In BGP, the question is not only "which way is shorter." Often the more important questions are:

- which routes should be accepted;
- which routes should be advertised outward;
- which external paths should be trusted;
- which provider should be preferred;
- which networks should not enter the environment.

That is why BGP fits internet routing, partner connections, multi-homing, and controlled route exchange between organizations. It scales not by mapping the whole world, but through path attributes and policy.

## Fast Recap

| Concept | Practical meaning |
| --- | --- |
| IGP | Internal routing inside your organization. |
| EGP | External routing between organizations. |
| Distance vector | Lighter and simpler, learns through neighbor updates. |
| Link state | Sees more topology, often faster convergence, costs more resources. |
| Path vector | BGP-style routing with path and policy control. |

Main takeaway: category labels are not for memorization. They explain behavior. Once the architecture is clear, configuration stops feeling random and troubleshooting becomes logical.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| IGP | Interior Gateway Protocol, routing inside one organization. |
| EGP | Exterior Gateway Protocol, routing between organizations. |
| Distance vector | Protocol type where routers learn routes through neighbor updates. |
| Link state | Protocol type where routers build topology knowledge and calculate best paths. |
| Path vector | Protocol type where decisions are based on path information and policy. |
| OSPF | Link-state IGP, widely used in enterprise networks. |
| BGP | Path-vector EGP, routing protocol of the internet. |
| Convergence | The process where routers reach an updated understanding of topology after a change. |

## Questions

### 1. What is the difference between IGP and EGP?

Answer: IGP is used for routing inside one organization, while EGP is used for routing between organizations or administrative domains.

### 2. Why is distance vector called routing by rumor?

Answer: A router learns routes from neighbors and does not keep a complete topology map. It trusts neighbor updates and builds forwarding decisions from them.

### 3. How is link state different from distance vector?

Answer: Link state protocols give routers a broader topology map, so they can calculate best paths themselves and often react to changes faster.

### 4. Why is BGP considered path vector?

Answer: BGP makes decisions based on path information and policy, not just a complete topology map or neighbor rumors.

### 5. Why does this classification matter for troubleshooting?

Answer: The category explains how the route was learned, how the protocol reacts to failure, and where to look for problems: neighbors, topology database, policy, or external advertisements.

## What To Review Later

- Which routing protocols are IGPs.
- Why BGP is the main EGP.
- The difference between distance vector and link state convergence.
- Main use cases for OSPF and BGP.
