# Routers Connect Networks

Source: закрытая страница курса  
Date added: 2026-06-01  
Related plan item: Week 5 / Router purpose and route types  
Tags: router, routing table, default gateway, static route, default route, dynamic routing, broadcast domain, LAN, WAN
Language: Russian
Translation pair: articles-en/2026-05/week-05/12-routers-connect-networks.md

## Summary

Этот урок закрепляет главную роль routers: они существуют, чтобы соединять разные networks. Switch помогает устройствам общаться внутри одной LAN, но когда traffic должен попасть в другую subnet, на другой site или в internet, нужен router.

Главная мысль: every router interface is a network. Если у router один interface смотрит в cafe LAN, а второй - в WAN, то router стоит между двумя разными networks и принимает решения, куда отправлять packets дальше.

## Key Points

- Routers connect different IP networks.
- Each router interface usually belongs to a separate network.
- Switches use MAC addresses to forward frames locally.
- Routers use IP addresses and routing tables to forward packets between networks.
- Hosts send non-local traffic to their default gateway.
- Routers stop broadcasts from crossing into other networks.
- Connected routes appear when router interfaces are configured and up.
- Static routes are manually configured paths.
- Default routes are catch-all routes for unknown destinations.
- More specific routes win over less specific routes.
- Dynamic routing protocols let routers share routing information automatically.
- Always check both forward and return paths during troubleshooting.

## Notes

### Why Routers Exist

A network diagram can make everything look connected already:

```text
devices -> switches -> more devices
```

But physical connection is not the same as routing.

Inside NetworkChuck Coffee, local devices can communicate through switches. That works because they are inside the same local network or switching environment.

The moment one cafe device needs to reach a server in another network, the problem changes.

Now we need a device that can say:

```text
This destination is not local.
I know which direction to send this packet.
```

That device is the router.

### Every Router Interface Is A Network

This is one of the most important CCNA ideas:

```text
Every router interface is a network.
```

If a router has:

- one interface connected to the cafe LAN;
- one interface connected to a WAN link;
- one interface connected to a server network;

then the router is connected to three different networks.

Each interface needs its own correct IP address and subnet mask for the network it belongs to.

That is why router addressing must be planned carefully.

### MAC Addresses Still Matter

MAC addresses do not disappear when routing begins.

They still matter on each local segment.

But their role is local.

Switches use MAC addresses to forward frames inside the LAN.

Routers use IP addresses to decide where packets should go between networks.

A useful way to think about it:

```text
MAC address = next local delivery step.
IP address = final network destination.
```

The packet keeps its source and destination IP addresses as it moves across networks, but the local Layer 2 frame changes from hop to hop.

### Local Or Remote Destination

When a host wants to send traffic, it checks the destination IP address.

If the destination is in the same subnet, the host can send directly on the local network.

If the destination is not in the same subnet, the host sends the traffic to its default gateway.

Pattern:

```text
If destination is local -> send directly.
If destination is remote -> send to default gateway.
```

The default gateway is usually the router interface in the host's local network.

### Example: Cafe To Remote Server

Imagine a cafe terminal sending a report to a server in a remote data center.

The terminal checks the server IP address and realizes:

```text
That server is not in my subnet.
```

So the terminal does not try to reach the remote server directly at Layer 2.

Instead, it sends the packet to its default gateway:

```text
Cafe terminal -> Switch -> Router local interface
```

From there, the router uses its routing table to decide the next step.

### Routers Stop Broadcasts

Routers also contain broadcasts.

Broadcasts are local messages such as:

```text
Who has this address?
Everybody listen to this local request.
```

Inside a LAN, broadcasts are normal.

But broadcasts should not spread everywhere.

If routers forwarded all broadcasts into every connected network, networks would become noisy and unstable very quickly.

So the router acts as a boundary:

```text
Broadcast stops here.
Routed packet forwarding starts here.
```

This is one reason routers create separate broadcast domains.

### Routing Table

Once the router receives a packet, it checks its routing table.

A routing table is the router's list of known networks and how to reach them.

Routes can come from different sources:

- directly connected interfaces;
- static routes;
- default routes;
- dynamic routing protocols.

The router compares the destination IP address against the routing table and chooses the best matching route.

### Connected Routes

A connected route appears when a router interface is:

- configured with an IP address and subnet mask;
- administratively enabled;
- physically/protocol up.

For example, if a router interface is configured in `192.168.10.0/24`, the router knows that network is directly connected.

This is the simplest kind of route because the router is attached to that network.

### Static Routes

A static route is a route manually configured by an administrator.

It tells the router:

```text
To reach this network, send traffic to this next hop.
```

Static routes are useful for:

- small networks;
- simple branch links;
- lab environments;
- one-off paths;
- backup or controlled paths.

But they can become hard to manage as the network grows.

If you add many sites and many networks, every missing or incorrect static route becomes a possible outage.

### The Return Path Problem

A classic routing issue is one-way communication.

Traffic may reach the remote network, but the reply cannot return.

Example:

```text
Cafe router knows how to reach the server network.
Remote router does not know how to reach the cafe network.
```

Result:

```text
Request goes out.
Reply gets lost.
```

Troubleshooting rule:

```text
Do not only ask "Can traffic get there?"
Also ask "Can traffic get back?"
```

Routing must work in both directions for most communication to succeed.

### Default Routes

A default route is the router's catch-all route.

It says:

```text
If no more specific route matches, send traffic this way.
```

For internet access, the default route often points toward the ISP or upstream firewall/router.

Common notation:

```text
0.0.0.0/0
```

That means "all IPv4 destinations" as a fallback.

### Rule Of Specificity

Routers prefer the most specific matching route.

Example:

```text
Route A: 192.168.3.0/24
Route B: 0.0.0.0/0
```

If traffic is going to `192.168.3.50`, the router uses `192.168.3.0/24`, because it is more specific.

The default route does not override better routes.

It only catches traffic when no more specific match exists.

### Dynamic Routing

Static routing is fine until the network becomes large or changes often.

Dynamic routing protocols let routers share routing information with each other automatically.

Examples:

- OSPF;
- EIGRP;
- BGP;
- RIP.

With dynamic routing, routers exchange what they know:

```text
I am connected to these networks.
I learned these other networks from neighbors.
Here is the best path I know.
```

Administrators still configure the protocol, but they do not manually type every route on every router.

That becomes very important as networks grow.

### Putting It Together

Routers exist to:

- connect different networks;
- stop broadcasts from spreading everywhere;
- make forwarding decisions with a routing table;
- use connected, static, default and dynamic routes;
- provide a path from local networks to remote networks.

Once you understand what the router sees in its routing table, routing becomes much easier to troubleshoot.

## Packet Flow Example

Remote destination:

```text
PC checks destination IP
Destination is not local
PC sends packet to default gateway
Router checks routing table
Router forwards packet toward next hop
Remote network receives traffic
Return traffic must also have a valid path back
```

## Practical Checklist

When troubleshooting routing, check:

- source IP and subnet mask;
- destination IP;
- source host default gateway;
- router interface status;
- connected routes;
- static routes;
- default route;
- route specificity;
- return path;
- whether broadcasts are expected to stay local;
- whether dynamic routing is exchanging routes correctly.

## Quick Self-Check

### Question 1

What does "every router interface is a network" mean?

Answer:

```text
Each routed interface usually connects to a separate IP network and needs an address from that network.
```

### Question 2

When does a host send traffic to its default gateway?

Answer:

```text
When the destination IP address is outside the host's local subnet.
```

### Question 3

Why do routers stop broadcasts?

Answer:

```text
To keep broadcast traffic contained inside the local network and prevent unnecessary noise across other networks.
```

### Question 4

What is a static route?

Answer:

```text
A manually configured route that tells a router how to reach a specific network.
```

### Question 5

What is a default route?

Answer:

```text
A catch-all route used when no more specific route matches the destination.
```

### Question 6

What should you always check in routing troubleshooting?

Answer:

```text
Both the forward path and the return path.
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Router interface | Routed connection point that belongs to an IP network. |
| Default gateway | Router interface used by hosts to reach remote networks. |
| Routing table | List of known routes and next hops. |
| Connected route | Route learned from an active configured interface. |
| Static route | Manually configured route. |
| Default route | Fallback route, commonly `0.0.0.0/0`. |
| Dynamic routing | Automatic route exchange between routers. |
| OSPF | Link-state dynamic routing protocol. |
| EIGRP | Cisco-developed advanced distance-vector routing protocol. |
| BGP | Path-vector protocol used heavily on the internet. |
| RIP | Older distance-vector routing protocol. |
| Broadcast domain | Network area where broadcasts remain contained. |
| Specificity | Routing rule where the longest/most specific matching prefix wins. |

## What To Review Later

- `show ip route`
- Longest prefix match
- Static route syntax
- Default route syntax
- Administrative distance
- Routing metrics
- OSPF basics
- BGP basics
- Return path troubleshooting
