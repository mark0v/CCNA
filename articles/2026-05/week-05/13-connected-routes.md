# Connected Routes

Source: закрытая страница курса  
Date added: 2026-06-01  
Related plan item: Week 5 / Connected routes and routing table basics  
Tags: connected route, router, routing table, show ip route, show ip interface brief, WAN, interface status, Packet Tracer
Language: Russian
Translation pair: articles-en/2026-05/week-05/13-connected-routes.md

## Summary

Connected route появляется автоматически, когда router interface получает IP address, включен и находится в рабочем состоянии. Это первое routing knowledge, которое router получает без static routes и без dynamic routing protocols.

Главная мысль: router знает только те connected networks, к которым он действительно подключен активными interfaces. Если interface down, connected route исчезает из routing table. Если remote network находится за другим router, ее нужно добавить отдельным routing способом.

## Key Points

- Routing starts when a router interface has an IP address and is up.
- Connected routes are learned automatically from active router interfaces.
- A connected route is marked with `C` in `show ip route`.
- A local route is marked with `L` and points to the router's exact interface IP.
- If an interface goes down, its connected route disappears.
- If the interface comes back up, the connected route returns.
- `show ip interface brief` shows interface/IP/status quickly.
- `show ip route` shows what networks the router currently knows.
- A WAN link between routers becomes a connected network for both routers.
- Each router knows only its own connected networks by default.
- Remote LANs behind another router require more routing knowledge.
- Physical layer issues can look like configuration issues if you skip hardware checks.

## Notes

### Routing Starts Earlier Than It Looks

It is easy to think routing begins only when we configure:

- a static route;
- OSPF;
- EIGRP;
- BGP;
- RIP.

But a router starts learning as soon as you configure and activate an interface.

If the interface has:

- an IP address;
- a subnet mask;
- `no shutdown`;
- working physical/protocol status;

then the router automatically adds that directly attached network to its routing table.

That route is called a connected route.

### Connected Route Definition

A connected route is a network the router knows because one of its own interfaces is part of that network.

No manual route is needed.

No routing protocol is needed.

The router is physically and logically attached, so it knows:

```text
I can reach this network directly through my own interface.
```

In `show ip route`, connected routes are usually marked with:

```text
C
```

### NetworkChuck Coffee Scenario

In the lab scenario, the cafe network grows from one local site into two connected locations:

- main coffee shop;
- fallout shelter site;
- private WAN between them.

The private WAN is a wide area network connection between locations. A service provider usually handles the physical transport, while we configure the routers on each end.

This creates a more realistic topology:

```text
Coffee shop LAN -> Coffee shop router -> WAN -> Shelter router -> Shelter LAN
```

Each router needs interfaces configured for the networks it touches.

### Physical Layer Matters

The lab also shows an important real-world lesson: not every problem is an IP configuration problem.

Sometimes the issue is:

- wrong module;
- wrong port type;
- missing SFP;
- wrong cable;
- unmatched transceiver;
- interface administratively down;
- physical link not connected.

If a link will not come up, start with the physical layer.

Before changing routing commands, check:

```text
Is the correct interface module installed?
Is the cable type correct?
Are both ends compatible?
Is the interface enabled?
Does Packet Tracer or the real device show link lights/status?
```

This saves time because a router cannot form a connected route for a network on a down interface.

### Building The WAN Link

After the correct modules and links are in place, each side of the WAN gets an IP address.

Example idea:

```text
Coffee router WAN interface: 10.0.0.1/30
Shelter router WAN interface: 10.0.0.2/30
```

Both router interfaces are in the same WAN subnet.

When both sides are up, each router sees the WAN network as connected.

Then basic tests become possible:

```text
ping 10.0.0.2
telnet 10.0.0.2
```

Ping checks reachability.

Telnet, in a lab, can confirm that one router can actually reach the other router's CLI service.

### The Router Learns What It Touches

Once the WAN interface is configured and up, the router adds the WAN subnet as a connected route.

Once the LAN interface is configured and up, the router adds the LAN subnet as a connected route.

Example:

```text
Coffee router knows:
- coffee shop LAN
- WAN link

Shelter router knows:
- shelter LAN
- WAN link
```

This happens automatically because those networks are directly attached.

### `show ip route`

`show ip route` lets you see the router's routing table.

This is one of the most important verification commands in routing.

You use it to answer:

```text
What networks does this router know?
How did it learn them?
Where will it send traffic?
```

Connected routes appear with `C`.

Local host routes appear with `L`.

### Local Routes

Local routes are usually marked with:

```text
L
```

A local route points to the router's exact interface IP address.

For example, if the router interface is:

```text
192.168.1.1/24
```

you may see:

```text
C 192.168.1.0/24
L 192.168.1.1/32
```

The `C` route represents the whole connected network.

The `L` route represents the router's own exact interface address.

For now, the biggest idea is not to get lost in `L` routes. Know they exist, but focus on connected networks first.

### Shut The Interface, Lose The Route

Connected routes depend on interface state.

If you shut down an interface:

```text
interface g0/0
 shutdown
```

the route for that connected network disappears from the routing table.

Why?

Because the router no longer considers that network reachable through itself.

If you bring the interface back:

```text
interface g0/0
 no shutdown
```

and the link becomes operational again, the connected route returns.

This relationship is extremely useful in troubleshooting.

### Use Two Commands Together

Two commands work well together:

```text
show ip interface brief
show ip route
```

`show ip interface brief` answers:

```text
Which interfaces exist?
What IP addresses do they have?
Are they up/down?
Are they administratively down?
```

`show ip route` answers:

```text
Which networks does the router know right now?
Are connected routes present?
Are remote routes missing?
```

When you compare both outputs, you can connect interface state to routing table state.

### What The Router Still Does Not Know

Connected routes are useful, but incomplete.

Each router knows only the networks it is directly connected to.

Example:

```text
Coffee router knows:
- 192.168.1.0/24 coffee LAN
- WAN network

Shelter router knows:
- 192.168.3.0/24 shelter LAN
- WAN network
```

But the coffee router does not automatically know how to reach the shelter LAN.

And the shelter router does not automatically know how to reach the coffee LAN.

Those are remote networks.

Remote networks require additional routing knowledge, such as:

- static routes;
- default routes;
- dynamic routing protocols.

### Why Ping Between Routers Is Not Enough

If the routers can ping each other across the WAN, that proves the WAN subnet works.

But it does not prove that LAN-to-LAN routing works.

This can be misleading.

The WAN interfaces are directly connected, so pings between WAN IPs can succeed.

But a host in the coffee LAN still may not reach a host in the shelter LAN until both routers know routes to the remote LANs.

Always distinguish:

```text
Router-to-router WAN reachability
LAN-to-LAN reachability
```

They are related, but they are not the same test.

### Troubleshooting Pattern

If a subnet is unreachable, ask:

1. Is the related interface up?
2. Does the interface have the correct IP address and subnet mask?
3. Does `show ip route` include the connected route?
4. Is the destination network directly connected or remote?
5. If remote, does a route exist?
6. Does the return path exist?

This keeps troubleshooting structured.

### The Core Lesson

Connected routes prove that routers are not passive boxes.

They react to interface configuration and link state.

Basic sequence:

1. Configure an interface.
2. Bring it up.
3. Router adds the directly attached network as connected.
4. Shut the interface down.
5. Router removes the connected route.
6. Bring it back up.
7. Route returns.

That is the foundation before static and dynamic routing.

## Example Topology

```text
Coffee LAN 192.168.1.0/24
        |
Cafe01-RTR01
        |
Private WAN
        |
Shelter-RTR01
        |
Shelter LAN 192.168.3.0/24
```

What each router learns automatically:

```text
Cafe01-RTR01:
- 192.168.1.0/24 connected
- WAN subnet connected

Shelter-RTR01:
- 192.168.3.0/24 connected
- WAN subnet connected
```

What they do not learn automatically:

```text
Cafe01-RTR01 does not automatically know 192.168.3.0/24.
Shelter-RTR01 does not automatically know 192.168.1.0/24.
```

## Practical Checklist

When validating connected routes:

- check physical cabling/module/interface type;
- verify the interface is not administratively down;
- assign the correct IP address and mask;
- use `show ip interface brief`;
- use `show ip route`;
- look for `C` connected routes;
- note `L` local routes without over-focusing on them;
- shut/no shut only when appropriate in a lab or approved maintenance window;
- test router-to-router WAN reachability;
- test LAN-to-LAN reachability separately;
- identify which remote routes are still missing.

## Quick Self-Check

### Question 1

What is a connected route?

Answer:

```text
A route to a network directly attached to an active router interface.
```

### Question 2

How does a router learn a connected route?

Answer:

```text
Automatically, when an interface has an IP address and is up/up.
```

### Question 3

What happens to a connected route when its interface goes down?

Answer:

```text
The route disappears from the routing table.
```

### Question 4

Which command shows the routing table?

Answer:

```text
show ip route
```

### Question 5

Which command quickly shows interface IP addresses and status?

Answer:

```text
show ip interface brief
```

### Question 6

Why are connected routes incomplete by themselves?

Answer:

```text
They only cover directly attached networks, not remote networks behind another router.
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Connected route | Automatically learned route for a directly attached network. |
| `C` | Routing table code for connected route. |
| Local route | Host-specific route to the router's own interface IP. |
| `L` | Routing table code for local route. |
| `show ip route` | Displays the router's routing table. |
| `show ip interface brief` | Displays interface IP/status summary. |
| `shutdown` | Administratively disables an interface. |
| `no shutdown` | Enables an interface. |
| WAN | Wide area network connecting separate locations. |
| Remote network | Network not directly connected to the local router. |
| Static route | Manually configured route to a remote network. |
| Dynamic routing | Automatic route learning through routing protocols. |

## What To Review Later

- Static routes
- Default routes
- Dynamic routing protocols
- `show ip route` codes
- Longest prefix match
- Return path troubleshooting
- WAN link troubleshooting
- Interface module/cable compatibility
