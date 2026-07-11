# From Routing Resiliency To Gateway Resiliency

Source: closed course page  
Date added: 2026-07-11  
Related plan item: Week 11 / From routing resiliency to gateway resiliency  
Tags: dynamic routing, OSPF, first hop redundancy, default gateway, FHRP, resiliency, routing protocols
Language: English
Translation pair: articles/2026-07/week-11/07-from-routing-resiliency-to-gateway-resiliency.md

## Summary

- Dynamic routing protocols let routers learn, share, and recover routes automatically.
- The OSPF deployment in NetworkChuck Coffee now shows real routing resiliency.
- But hosts do not participate in OSPF and usually know only one default gateway.
- If a host's default gateway fails, the routed core may be resilient while the endpoint still loses connectivity.
- The next step is first hop redundancy protocols, which make the default gateway highly available.

## Key Points

- Dynamic routing matters because it helps the network grow and recover, not because protocol names are interesting.
- OSPF lets routers adapt to changes without manual static route updates.
- Routing resiliency between routers does not solve gateway failure for clients.
- Hosts usually do not build a full routing table; they send off-subnet traffic to the default gateway.
- FHRP is needed so hosts have a resilient first hop.

## Notes

After a dynamic routing section, it is easy to think the network is now fully resilient. Routers have learned routes, OSPF is running, areas are configured, and a default route can be distributed dynamically. But that is only part of the story.

Routing protocols solve router-to-router reachability. They help routers:

- discover networks;
- share route information;
- recalculate paths after failure;
- use alternate routes;
- reduce manual static route maintenance.

That is already a major step. Static routes work in small environments, but when NetworkChuck Coffee grows into multiple cafes, offices, warehouse networks, and shared services, manual route management quickly becomes an operational burden.

The OSPF deployment this week was a sample deployment, not the final form. It showed a pattern that can scale:

- cafe and fallout shelter routes are exchanged dynamically;
- the WAN link participates in OSPF;
- routes appear through the protocol instead of static config;
- multi-area design and summarization prepare the network for growth;
- a default route can be injected centrally.

That makes routers smarter and more resilient.

## What Routers Can Do Now

After dynamic routing, routers can:

- learn where remote networks are;
- choose paths based on protocol metrics;
- react when topology changes;
- remove failed paths;
- install alternate routes;
- recover when links return.

In a real network, that matters. Links fail, devices reboot, interfaces flap, and configs change. Dynamic routing keeps the routing domain from depending on one engineer manually editing routes during every failure.

Main practical design question:

> Does this work today, and what happens when a link fails, a site is added, or traffic patterns change?

Dynamic routing earns its keep in the second half of that question.

## The Host Problem

Hosts are a different story.

Laptops, phones, printers, POS terminals, cameras, and workstations usually do not run OSPF. They do not form neighbor relationships, build an LSDB, recalculate best paths, or learn alternate routes from routers.

A host usually knows:

- its IP address;
- subnet mask;
- default gateway;
- DNS servers.

The default gateway is the first router or Layer 3 interface the host uses for destinations outside its local subnet.

If that gateway disappears, the host does not become a routing expert. It simply loses the way out.

This is a subtle design gap:

- routed infrastructure between routers can be redundant;
- OSPF can have alternate paths;
- WAN design can be resilient;
- but the host still depends on one configured default gateway.

If the gateway fails, the user experience breaks.

## Why Routing Resiliency Is Not Enough

Imagine NetworkChuck Coffee:

- POS terminals use default gateway `10.10.10.1`;
- Wi-Fi clients use gateway `10.10.20.1`;
- office laptops use gateway `10.10.30.1`.

OSPF may work perfectly behind those gateways. But if the router or SVI serving `10.10.10.1` fails, POS terminals do not care that OSPF elsewhere is healthy. Their first hop is gone.

That means:

> Routers can be resilient while hosts are still stranded.

To make the full design resilient, the gap between the host and first router must be closed.

## First Hop Redundancy

The next topic is first hop redundancy protocols, or FHRP.

FHRP exists to:

- give hosts a stable default gateway;
- allow multiple routers/L3 devices to share gateway responsibility;
- move the gateway function to a backup device if the primary fails;
- keep clients using the same configured gateway address;
- reduce outage impact when the first-hop device fails.

In plain English: endpoints get a backup plan.

Routing protocols made the routers smart. FHRP makes the endpoint experience resilient.

Common FHRP protocols:

| Protocol | Notes |
| --- | --- |
| HSRP | Cisco first hop redundancy protocol. |
| VRRP | Standards-based first hop redundancy protocol. |
| GLBP | Cisco protocol with gateway redundancy and load balancing behavior. |

We are not abandoning OSPF. We are building the next layer of resiliency on top of it. First, routers learned how to handle network changes. Now hosts need a reliable first hop.

## Section Recap

What has already been covered:

- why dynamic routing protocols matter;
- protocol families: OSPF, RIP, EIGRP, BGP;
- path selection with metrics, costs, and administrative distance;
- OSPF `network` command and passive interfaces;
- basic OSPF adjacency;
- OSPF troubleshooting;
- multi-area OSPF, ABR, ASBR, summarization, and default route injection.

What remains unresolved:

- client devices still depend on one default gateway;
- hosts do not participate in routing protocols;
- gateway failure can break users even if the routing core remains healthy.

That is why the next logical step is first hop redundancy.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Dynamic routing | Routers automatically learn and share route information. |
| OSPF | Link-state IGP used for scalable internal routing. |
| Default gateway | First-hop router address used by hosts for off-subnet traffic. |
| First hop | First Layer 3 device a host uses to reach remote networks. |
| FHRP | First Hop Redundancy Protocol, makes default gateway highly available. |
| HSRP | Cisco FHRP. |
| VRRP | Standards-based FHRP. |
| GLBP | Cisco FHRP with load sharing behavior. |

## Questions

### 1. What has dynamic routing already solved?

Answer: It lets routers automatically learn routes, share information, and recover from topology changes without manual static route edits.

### 2. Why is that not enough for hosts?

Answer: Hosts usually do not run routing protocols. They know a default gateway, and if it fails, the host loses its path outside the local subnet.

### 3. What is a default gateway?

Answer: It is the first-hop Layer 3 address a host sends traffic to for destinations outside its local subnet.

### 4. Why do we need FHRP?

Answer: To make the default gateway resilient by allowing a backup router or Layer 3 device to take over the gateway role if the primary fails.

### 5. How is FHRP related to OSPF?

Answer: OSPF handles routing between routers. FHRP handles gateway availability for hosts. They solve different parts of resiliency design.

## What To Review Later

- Difference between routing resiliency and first-hop resiliency.
- How hosts use default gateways.
- HSRP, VRRP, and GLBP roles.
- Why OSPF health does not guarantee client connectivity.
