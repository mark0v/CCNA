# Dynamic Routing With EIGRP

Source: closed course page  
Date added: 2026-06-09  
Related plan item: Week 6 / Dynamic routing introduction  
Tags: dynamic routing, EIGRP, adjacency, neighbor, routing table, Cisco IOS, network statement
Language: English
Translation pair: articles/2026-06/week-06/03-dynamic-routing-with-eigrp.md

## Summary

Dynamic routing allows routers to exchange information about reachable networks automatically. Unlike static routing, an administrator does not enter every remote route manually: routers form neighbor relationships and add learned routes to their routing tables.

This lesson uses classic EIGRP. After the static routes are removed, connectivity to remote LANs fails. EIGRP is then enabled on the intended interfaces, the routers become neighbors and exchange routes automatically.

## Key Points

- Dynamic routing automates route exchange between routers.
- Static routes remain useful but scale poorly as a network grows.
- EIGRP means Enhanced Interior Gateway Routing Protocol.
- `router eigrp 1` starts a classic EIGRP process with AS number `1`.
- Routers need a compatible EIGRP autonomous system number.
- A `network` statement selects participating interfaces and advertised connected networks.
- Routers discover one another with hello packets.
- After forming an adjacency, they exchange routing information.
- An EIGRP route is marked `D` in a Cisco routing table.
- Dynamic routing should run only on intended links.
- An internet-facing interface should not participate without an explicit design reason.
- Verification must cover neighbors, learned routes and end-to-end connectivity.

## Notes

### Break The Network To Understand It

A useful lab workflow is:

1. Remove the existing static routes.
2. Confirm remote connectivity fails.
3. Inspect the routing table.
4. Configure dynamic routing.
5. Observe neighbors and learned routes appearing.
6. Test connectivity again.

This makes the value of a routing protocol visible.

Remove a static route:

```cisco
no ip route 192.168.3.0 255.255.255.0 192.168.2.2
```

On the other router:

```cisco
no ip route 192.168.1.0 255.255.255.0 192.168.2.1
```

Connected routes remain, but remote LAN routes disappear.

### What Dynamic Routing Means

A dynamic routing protocol lets routers communicate:

```text
Which networks they know.
Which paths reach those networks.
When a route appears, changes or disappears.
```

Each router processes updates according to the protocol and installs its best routes in the routing table.

This is automated information exchange, not magic.

### Static Versus Dynamic Routing

Static routing:

- is configured manually;
- is predictable;
- is simple in small topologies;
- generates no routing protocol traffic;
- requires manual changes when the topology changes.

Dynamic routing:

- exchanges routes automatically;
- scales better;
- adapts to topology changes;
- requires protocol configuration;
- consumes CPU, memory and network traffic;
- requires controlled boundaries and neighbor relationships.

Both methods can coexist in one network.

### Why EIGRP

EIGRP is a dynamic interior gateway protocol traditionally associated with Cisco environments.

Its full name is:

```text
Enhanced Interior Gateway Routing Protocol
```

This introductory lesson focuses on the workflow rather than every EIGRP mechanism:

```text
Enable process
Select interfaces/networks
Discover neighbors
Exchange routes
Install learned routes
```

### Autonomous System Number

Classic EIGRP starts with:

```cisco
router eigrp 1
```

The number `1` is the EIGRP process autonomous system number.

To form a classic EIGRP adjacency, neighboring routers must use the same AS number and compatible parameters.

Example on both routers:

```cisco
router eigrp 1
```

Here, the AS number identifies the routing domain; it is not a public BGP autonomous system assignment.

### The `network` Statement

In classic EIGRP, the `network` command does two important things:

1. Selects local interfaces on which EIGRP should operate.
2. Advertises the connected networks of those interfaces to EIGRP neighbors.

Simple lab form:

```cisco
router eigrp 1
 network 192.168.1.0
 network 192.168.2.0
```

More precise form with wildcard masks:

```cisco
router eigrp 1
 network 192.168.1.0 0.0.0.255
 network 192.168.2.0 0.0.0.255
```

The wildcard `0.0.0.255` corresponds to `/24`.

Precise statements reduce the chance of enabling the protocol on unintended interfaces.

### Hello Packets And Neighbors

EIGRP sends hello packets on participating interfaces.

They discover and maintain neighbors.

If only one router is configured, it sends hello messages but forms no adjacency.

When the second router is configured on the shared WAN network, the routers discover each other and become EIGRP neighbors.

A console message often reports the new adjacency.

### Neighbor Adjacency

An adjacency means the routers:

- discovered each other;
- have compatible protocol parameters;
- are ready to exchange routing information;
- monitor neighbor availability.

Verification:

```cisco
show ip eigrp neighbors
```

Without a neighbor, routes cannot be learned through it.

### Learned Routes

After adjacency forms, routers exchange known networks.

The cafe router can learn:

```text
192.168.3.0/24
```

The shelter router can learn:

```text
192.168.1.0/24
```

Check:

```cisco
show ip route
```

An EIGRP-learned route is marked:

```text
D
```

The letter `E` was already used by the older EGP protocol, so Cisco uses `D`, historically associated with the DUAL algorithm.

Example:

```text
D 192.168.3.0/24 [90/...] via 192.168.2.2
```

### Do Not Enable It Everywhere

Dynamic routing should operate only where the design requires it.

Do not enable EIGRP carelessly:

- on an internet-facing interface;
- in a user access LAN where no neighbor is expected;
- on untrusted networks;
- on interfaces whose networks should not be advertised.

Accidental participation can:

- expose internal prefixes;
- create unwanted neighbors;
- install incorrect routes;
- complicate troubleshooting;
- increase the attack surface.

### Internet-Facing Interface

The NetworkChuck Coffee router has a link to its ISP.

That interface is not included in EIGRP because:

- the ISP is not an internal EIGRP neighbor;
- internal routes should not be advertised toward it;
- internet access can use a default route;
- routing boundaries should be intentional.

Distinguish:

```text
Internal dynamic routing domain
External ISP connection
```

### Passive Interfaces

If a connected LAN should be advertised but no EIGRP neighbor should form on it, use a passive interface.

Example:

```cisco
router eigrp 1
 passive-interface GigabitEthernet0/0
```

The network can remain advertised, but EIGRP hello packets are not sent through that interface.

A defensive pattern is:

```cisco
router eigrp 1
 passive-interface default
 no passive-interface GigabitEthernet0/1
```

All interfaces are passive except the explicitly permitted router-to-router link.

### Verification Commands

Core commands:

```cisco
show ip protocols
show ip eigrp neighbors
show ip eigrp topology
show ip route
show ip route eigrp
show ip interface brief
```

| Command | Verifies |
| --- | --- |
| `show ip protocols` | Protocol process, networks and passive interfaces |
| `show ip eigrp neighbors` | Formed EIGRP neighbors |
| `show ip eigrp topology` | EIGRP topology information |
| `show ip route eigrp` | Routes installed through EIGRP |
| `show ip interface brief` | Interface addressing and state |

### End-To-End Testing

After `D` routes appear, test:

```cisco
ping 192.168.3.10
traceroute 192.168.3.10
```

Test from end hosts as well as routers.

Useful sequence:

1. A PC reaches its default gateway.
2. Routers reach each other across the WAN.
3. The EIGRP adjacency exists.
4. Remote routes are installed.
5. The remote gateway is reachable.
6. The remote host is reachable.
7. Return traffic works.

### Why Dynamic Routing Scales Better

For two routers, static routing may look simpler.

A growing network can contain:

- multiple coffee shops;
- guest Wi-Fi networks;
- point-of-sale VLANs;
- voice networks;
- security cameras;
- inventory systems;
- redundant WAN links;
- data centers.

With every new prefix, manually updating all routers becomes expensive and error-prone.

Dynamic routing reduces manual route configuration and can react automatically to topology changes.

### Save The Configuration

After verification:

```cisco
copy running-config startup-config
```

## Configuration Example

### Cafe Router

```cisco
enable
configure terminal

router eigrp 1
 network 192.168.1.0 0.0.0.255
 network 192.168.2.0 0.0.0.255
 passive-interface GigabitEthernet0/0

end
```

### Shelter Router

```cisco
enable
configure terminal

router eigrp 1
 network 192.168.2.0 0.0.0.255
 network 192.168.3.0 0.0.0.255
 passive-interface GigabitEthernet0/0

end
```

Adapt interface names to the actual topology.

### Verification

```cisco
show ip protocols
show ip eigrp neighbors
show ip route eigrp
ping 192.168.3.10
```

## Troubleshooting Checklist

If EIGRP routes do not appear:

1. Check interface state and IP addressing.
2. Confirm the routers share the same WAN subnet.
3. Check the EIGRP AS number.
4. Check `network` statements.
5. Check wildcard masks.
6. Ensure the router-to-router interface is not passive.
7. Check `show ip eigrp neighbors`.
8. Check ACLs or filtering.
9. Confirm the required connected network exists.
10. Check the routing table and return path.

## Quick Self-Check

### Question 1

What is dynamic routing?

Answer:

```text
Automatic exchange of routing information between routers through a routing protocol.
```

### Question 2

What does EIGRP stand for?

Answer:

```text
Enhanced Interior Gateway Routing Protocol.
```

### Question 3

What is the EIGRP AS number used for?

Answer:

```text
It identifies the classic EIGRP routing process; neighbors must use a compatible, normally matching number.
```

### Question 4

What does an EIGRP `network` statement do?

Answer:

```text
It selects participating interfaces and advertises their connected networks.
```

### Question 5

Which routing table code identifies an EIGRP route?

Answer:

```text
D
```

### Question 6

Why should EIGRP not be enabled on the ISP interface?

Answer:

```text
It is outside the internal routing domain, and internal routes should not be advertised outward accidentally.
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Dynamic routing | Automatic route exchange between routers. |
| EIGRP | Enhanced Interior Gateway Routing Protocol. |
| `router eigrp 1` | Starts classic EIGRP process with AS number `1`. |
| `network` | Selects interfaces/networks for EIGRP participation. |
| Hello packet | Message used to discover and maintain neighbors. |
| Adjacency | Working neighbor relationship between routers. |
| `D` | Cisco routing table code for an EIGRP route. |
| Passive interface | Interface that sends no hellos while its network can still be advertised. |
| `show ip eigrp neighbors` | Displays EIGRP neighbors. |
| `show ip protocols` | Displays active routing protocol configuration. |

## What To Review Later

- EIGRP DUAL algorithm
- Feasible distance and reported distance
- EIGRP metrics
- Passive interfaces
- Route summarization
- OSPF
- Administrative distance
- Routing protocol authentication
