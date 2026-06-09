# Static Routing Basics

Source: closed course page  
Date added: 2026-06-09  
Related plan item: Week 6 / Static routing  
Tags: static route, routing table, next hop, return path, WAN, Cisco IOS, ip route
Language: English
Translation pair: articles/2026-06/week-06/01-static-routing-basics.md

## Summary

A static route is a manually configured path to a remote network that a router does not already know. Routers automatically add connected networks, but networks behind another router do not appear in the routing table by themselves.

Main idea: a router can forward packets only to destinations for which it has a route. Complete communication requires both a forward path and a return path.

## Key Points

- Routers automatically know only directly connected networks.
- A remote network must be present in the routing table.
- A static route is configured manually with `ip route`.
- A route identifies the destination network, subnet mask and next hop.
- The next hop must be reachable through an already known network.
- A route on only one router creates incomplete or one-way connectivity.
- The responding router must know the path back to the source network.
- A successful ping from a router does not always prove end-host connectivity.
- `show ip route` reveals what the router currently knows.
- Verification must cover both directions.

## Notes

### What Static Routing Solves

The NetworkChuck Coffee topology uses three networks:

```text
Cafe LAN:       192.168.1.0/24
Private WAN:    192.168.2.0/24
Shelter LAN:    192.168.3.0/24
```

The cafe router is directly connected to:

- `192.168.1.0/24`;
- `192.168.2.0/24`.

The shelter router is directly connected to:

- `192.168.2.0/24`;
- `192.168.3.0/24`.

These connected routes appear automatically when the interfaces are configured and `up/up`.

However, the cafe router does not know `192.168.3.0/24`, and the shelter router does not know `192.168.1.0/24`.

Static routes fill this knowledge gap.

### Routers Do Not Guess

A person can look at the topology and see the path:

```text
Cafe LAN -> Cafe router -> WAN -> Shelter router -> Shelter LAN
```

A router does not infer paths from a diagram.

For every packet, it compares the destination IP address against its routing table. If no matching route exists, the router drops the packet.

Rule:

```text
No route, no trip.
```

### Prove What Already Works

Before adding a static route, verify the foundation:

1. Hosts can reach their own default gateways.
2. Router interfaces are `up/up`.
3. Routers can reach each other across the WAN.
4. Connected routes appear in `show ip route`.

This separates a routing problem from Layer 1, Layer 2 or local IP configuration problems.

If a PC cannot reach its own default gateway, adding a remote static route will not solve the issue.

### Static Route Syntax

Basic Cisco IOS syntax:

```text
ip route <destination-network> <subnet-mask> <next-hop-ip>
```

In plain English:

```text
To reach this destination network with this subnet mask,
send the packet to this next-hop router.
```

The route from the cafe router to the shelter LAN is:

```cisco
ip route 192.168.3.0 255.255.255.0 192.168.2.2
```

| Part | Meaning |
| --- | --- |
| `192.168.3.0` | Destination network |
| `255.255.255.0` | Destination subnet mask |
| `192.168.2.2` | Shelter router next-hop address |

The router uses its known WAN network to deliver the packet to the neighboring router.

### Why Next Hop Is Common

A static route can also reference an exit interface:

```cisco
ip route 192.168.3.0 255.255.255.0 GigabitEthernet0/1
```

In many Ethernet scenarios, a next-hop IP is clearer:

```cisco
ip route 192.168.3.0 255.255.255.0 192.168.2.2
```

It explicitly identifies the neighboring router that should receive the traffic next.

The best syntax depends on the link type and design, but the next-hop form is easy to understand for this lab.

### First Route: Forward Path

After adding the route, the cafe router knows:

```text
To reach 192.168.3.0/24, send traffic to 192.168.2.2.
```

The forward path to the shelter LAN now exists.

Verify it with:

```cisco
show ip route
ping 192.168.3.10
```

A static route is normally marked with:

```text
S
```

However, one successful test from the router does not necessarily prove that every cafe host has complete connectivity to the remote server.

### One-Way Communication Is Not Success

Normal communication needs traffic to flow in both directions:

```text
Request: Cafe LAN -> Shelter LAN
Reply:   Shelter LAN -> Cafe LAN
```

If the cafe router knows the path to `192.168.3.0/24`, but the shelter router does not know the path to `192.168.1.0/24`, the request may arrive while the reply is lost.

This is a classic missing return route.

During troubleshooting, always ask:

```text
Can traffic get there?
Can the reply get back?
```

### Second Route: Return Path

The shelter router needs the reverse route:

```cisco
ip route 192.168.1.0 255.255.255.0 192.168.2.1
```

| Part | Meaning |
| --- | --- |
| `192.168.1.0` | Cafe destination network |
| `255.255.255.0` | Cafe subnet mask |
| `192.168.2.1` | Cafe router next-hop address |

Now both routers know the remote LAN:

```text
Cafe router:
192.168.3.0/24 via 192.168.2.2

Shelter router:
192.168.1.0/24 via 192.168.2.1
```

Both forward and return paths exist.

### Why Router Ping Can Be Misleading

The ping source matters.

If the cafe router pings the remote server, the source address may be its WAN interface. The shelter router already knows the WAN as a connected network, so the reply can return.

If a cafe PC sends the ping, its source belongs to `192.168.1.0/24`. Without the reverse route, the shelter router does not know how to return the reply.

Therefore, test:

- router to router;
- router to host;
- host to host;
- both directions.

### Verify The Routing Table

After configuration, use:

```cisco
show ip route
```

Confirm:

- an `S` route appears;
- the destination network is correct;
- the mask is correct;
- the next hop is correct;
- the next hop is reachable;
- the reverse route exists on the other router.

You can also inspect the running configuration:

```cisco
show running-config | include ip route
```

### Save The Configuration

After successful verification, save the configuration:

```cisco
copy running-config startup-config
```

Or:

```cisco
write memory
```

Otherwise, the routes can disappear after a reload.

### When Static Routes Are Useful

Static routes work well for:

- small networks;
- simple branch links;
- stable paths;
- labs;
- stub networks;
- default routes;
- backup routes;
- tightly controlled forwarding.

As the number of routers and networks grows, manual route management becomes difficult. Dynamic routing protocols then become more practical.

## Configuration Example

### Cafe Router

```cisco
enable
configure terminal
ip route 192.168.3.0 255.255.255.0 192.168.2.2
end
show ip route
```

### Shelter Router

```cisco
enable
configure terminal
ip route 192.168.1.0 255.255.255.0 192.168.2.1
end
show ip route
```

### Verification

```cisco
ping 192.168.2.2
ping 192.168.3.10
traceroute 192.168.3.10
show ip route
show ip interface brief
```

## Troubleshooting Checklist

If static routing does not work:

1. Check the source host IP address and subnet mask.
2. Check the source host default gateway.
3. Check interface states with `show ip interface brief`.
4. Check connected routes.
5. Check the static route destination and mask.
6. Check the next-hop address.
7. Confirm that the next hop is reachable.
8. Check the static route on the remote router.
9. Check the return path.
10. Check host firewalls and ACLs only after routing.
11. Test each hop separately.

## Quick Self-Check

### Question 1

What is a static route?

Answer:

```text
A manually configured route to a network the router does not learn automatically.
```

### Question 2

What are the three main parts of an `ip route` command?

Answer:

```text
Destination network, subnet mask and next-hop IP or exit interface.
```

### Question 3

Why is a route on only one router insufficient?

Answer:

```text
Reply traffic also needs a route back to the source network.
```

### Question 4

Which command displays the routing table?

Answer:

```text
show ip route
```

### Question 5

Which code identifies a static route in a Cisco routing table?

Answer:

```text
S
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Static route | Route manually configured by an administrator. |
| `ip route` | Cisco IOS command that adds an IPv4 static route. |
| Destination network | Remote network that must be reached. |
| Next hop | Next router on the path to the destination. |
| Forward path | Path taken by the request toward the destination. |
| Return path | Path taken by the reply back to the source. |
| `show ip route` | Displays the routing table. |
| `S` | Cisco routing table code for a static route. |
| Connected route | Automatic route to a directly attached network. |
| Remote network | Network not directly connected to the current router. |

## What To Review Later

- Default routes
- Floating static routes
- Administrative distance
- Recursive route lookup
- Longest prefix match
- Dynamic routing protocols
- Route troubleshooting
