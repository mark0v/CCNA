# What Now? Routing Foundations

Source: closed course page  
Date added: 2026-06-09  
Related plan item: Week 6 / Routing foundations checkpoint  
Tags: routing, static route, default route, EIGRP, routing table, NAT, documentation, WAN
Language: English
Translation pair: articles/2026-06/week-06/06-what-now-routing-foundations.md

## Summary

This checkpoint combines the foundational routing skills: connected, static, default and dynamic routes, routing-table interpretation, WAN construction and documentation. Routing is now a path-selection process for every packet rather than a collection of isolated commands.

The next major step is NAT. A default route gives traffic a direction toward the ISP, but private IPv4 addresses do not automatically become publicly routable.

## Key Points

- A basic routed network can now connect multiple LANs.
- Connected routes appear automatically from active interfaces.
- Static routes manually describe paths to remote networks.
- A default route handles destinations without a more specific match.
- EIGRP demonstrated automatic route exchange.
- `show ip route` displays the current winners installed for forwarding.
- A router can know alternative paths without showing them as active routes.
- Private addressing is useful internally but requires NAT for internet access.
- The simple current addressing scheme will improve after subnetting.
- Documentation is part of the engineering workflow.
- The next section connects routing with NAT and functional internet access.

## Notes

### What You Can Do Now

After this section, you can:

- assign IP addresses to router interfaces;
- enable interfaces with `no shutdown`;
- verify status with `show ip interface brief`;
- recognize connected and local routes;
- connect two locations through a WAN;
- add a static route to a remote LAN;
- configure the return path;
- add a default route toward an ISP;
- start basic EIGRP;
- verify neighbor adjacency;
- interpret a route entry;
- explain AD, metric and longest prefix match;
- document devices and IP assignments.

This is a practical routed-networking foundation.

### From A Diagram To A Real Flow

A topology is no longer an abstract picture.

You can trace a packet:

```text
Source host
-> local switch
-> default gateway
-> routing table lookup
-> next hop
-> remote router
-> destination network
```

The reply requires its own routing decision in the opposite direction.

### Temporary Addressing Is Fine For Learning

The lab uses a familiar scheme:

```text
192.168.1.0/24
192.168.2.0/24
192.168.3.0/24
```

It is easy to read and keeps attention on routing.

A real design must also consider:

- number of hosts;
- growth;
- route summarization;
- VLAN structure;
- address waste;
- security boundaries;
- site hierarchy;
- DHCP scopes.

Subnetting will make the addressing plan more efficient.

### Static Routing Recap

A static route explicitly tells a router:

```text
To reach this network, use this next hop.
```

Example:

```cisco
ip route 192.168.3.0 255.255.255.0 192.168.2.2
```

Static routing:

- is simple;
- is predictable;
- suits small or stub networks;
- requires manual maintenance;
- needs return routes.

### Default Routing Recap

Default route:

```cisco
ip route 0.0.0.0 0.0.0.0 216.0.5.1
```

It means:

```text
If no more specific route exists, send the packet to the ISP next hop.
```

A default route does not replace:

- specific routes;
- NAT;
- DNS;
- firewall policy;
- ISP return routing.

### Dynamic Routing Recap

EIGRP demonstrated dynamic routing:

```text
Routers discover neighbors.
Routers advertise connected networks.
Routers exchange route information.
Routers install preferred paths.
```

Basic configuration:

```cisco
router eigrp 1
 network 192.168.1.0 0.0.0.255
 network 192.168.2.0 0.0.0.255
```

Dynamic routing becomes useful as topology and prefix counts grow.

### Reading `show ip route`

`show ip route` displays the current forwarding decision.

Important codes:

| Code | Meaning |
| --- | --- |
| `C` | Connected |
| `L` | Local interface address |
| `S` | Static |
| `S*` | Static candidate default |
| `D` | EIGRP |

Route selection:

1. Longest prefix match.
2. Lower administrative distance for the same prefix.
3. Lower protocol metric among paths from one source.

### The Routing Table Shows Winners

A router can receive multiple routes to a destination.

`show ip route` normally displays the best route or equal-cost winners installed for forwarding.

Alternative routes can remain in:

- the EIGRP topology table;
- the OSPF LSDB;
- the BGP table;
- configuration as a floating static route.

The absence of a route from the main table does not always mean that a protocol never learned it.

### Why Internet Still Does Not Work Fully

A default route sends a packet toward the ISP.

Internal hosts use private ranges:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

These ranges are not routed on the public internet.

If a cafe PC at `192.168.1.10` sends traffic outward:

1. The PC sends the packet to its default gateway.
2. The router selects the default route.
3. The packet can leave toward the ISP.
4. The private source address is unsuitable for normal public return routing.

Address translation is required.

### NAT Is The Next Step

NAT means:

```text
Network Address Translation
```

NAT changes address information at a network boundary.

Small-business internet access commonly uses PAT:

```text
Port Address Translation
```

Many private hosts can share one public IP through different transport-layer ports.

Simplified example:

```text
192.168.1.10:50000
-> translated to
216.0.5.2:30001
```

The router tracks the translation and sends the reply to the correct internal host.

### Routing And NAT Solve Different Problems

Routing answers:

```text
Where should the packet go?
```

NAT answers:

```text
Which address representation should cross this boundary?
```

Internet access requires both:

- a route toward the ISP;
- address translation for private hosts.

### Documentation Is A Core Skill

Documentation is not a side task after a successful ping.

Record:

- hostname;
- site;
- interface purpose;
- IP/prefix;
- next hop;
- route purpose;
- WAN circuit;
- software version;
- configuration rationale;
- date and author.

Record not only what was configured, but why.

Months later, this prevents reverse engineering your own decisions under pressure.

### A Suggested Routing Record

| Device | Destination | Prefix | Route Type | Next Hop | Exit Interface | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| CAFE01-RTR01 | Shelter LAN | 192.168.3.0/24 | EIGRP | 192.168.2.2 | Gi0/1 | Site connectivity |
| CAFE01-RTR01 | Default | 0.0.0.0/0 | Static | 216.0.5.1 | Gi0/2 | Internet upstream |

### Troubleshooting Mindset

A vague issue:

```text
The remote server is unreachable.
```

can now be decomposed:

1. Local host addressing.
2. Default gateway.
3. Local interface state.
4. Connected route.
5. Remote route.
6. Next-hop reachability.
7. Routing protocol neighbor.
8. Return route.
9. NAT when crossing a public boundary.
10. ACL or firewall policy.

This is the transition from command memorization to systematic troubleshooting.

## Routing Foundations Checklist

- [ ] I can explain a connected route.
- [ ] I can configure a static route.
- [ ] I always check the return path.
- [ ] I can configure a default route.
- [ ] I understand the gateway of last resort.
- [ ] I understand basic dynamic routing.
- [ ] I can verify an EIGRP neighbor.
- [ ] I can read `[AD/metric]`.
- [ ] I apply longest prefix match.
- [ ] I understand why NAT is required.
- [ ] I document the network while building.

## Quick Self-Check

### Question 1

What does `show ip route` display?

Answer:

```text
The best routes installed by the router for forwarding.
```

### Question 2

Why is a default route insufficient for private-host internet access?

Answer:

```text
Private source addresses require NAT/PAT for normal communication with the public internet.
```

### Question 3

What is considered first during route lookup?

Answer:

```text
The longest matching prefix.
```

### Question 4

What problem does dynamic routing solve?

Answer:

```text
It automates route exchange and reduces manual maintenance in a growing network.
```

### Question 5

When should documentation be updated?

Answer:

```text
During every change, while the configuration and rationale are still fresh.
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `show ip route` | Displays installed routes. |
| Static route | Manually defined path. |
| Default route | Fallback path for unknown destinations. |
| Dynamic routing | Automatic route exchange. |
| EIGRP | Dynamic routing protocol used in the lesson. |
| NAT | Network Address Translation. |
| PAT | Translation of many private sessions through a public IP. |
| Private IPv4 | Addresses not routed on the public internet. |
| Return path | Route used by the reply toward the source. |
| Documentation | Current record of topology and design decisions. |

## What To Review Later

- NAT terminology
- Static NAT
- Dynamic NAT
- PAT / overload
- Inside local and inside global
- Subnetting
- ACLs and firewall policy
- Route troubleshooting
