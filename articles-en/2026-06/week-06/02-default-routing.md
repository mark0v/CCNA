# Default Routing

Source: closed course page  
Date added: 2026-06-09  
Related plan item: Week 6 / Default routing  
Tags: default route, gateway of last resort, ISP, static route, routing table, longest prefix match, Cisco IOS
Language: English
Translation pair: articles/2026-06/week-06/02-default-routing.md

## Summary

A router does not need to know a route to every network on the internet. Instead, an edge router can use a default route: a fallback path selected when the routing table has no more specific route.

Main idea: a default route does not make the router all-knowing. It only identifies where the router should send a packet next when it does not know the destination network itself.

## Key Points

- A default route is used only when no more specific route exists.
- In IPv4 it is represented as `0.0.0.0 0.0.0.0`.
- A default route often points to the ISP next-hop router.
- The gateway of last resort is the next hop for unknown destinations.
- More specific routes take priority over the default route.
- The ISP-facing interface must be configured and `up/up` first.
- The ISP provides the public IP, subnet mask and next-hop information.
- A `/30` is often used for point-to-point links between routers.
- In `show ip route`, a default static route is commonly marked `S*`.
- A default route provides outbound direction but does not replace NAT or return routing.

## Notes

### Do We Need Every Internet Route?

The internet contains an enormous number of networks.

It would make no sense for a small business router to manually store a route for every one of them.

Instead, the router needs one instruction:

```text
If I do not have a more precise route, send the traffic to the upstream provider.
```

That instruction is the default route.

### Gateway Of Last Resort

The gateway of last resort is the router that receives traffic when no better route exists.

Example:

```text
The cafe router knows the local LAN.
The cafe router knows the WAN to the shelter.
The cafe router does not know the destination website.
The cafe router uses its gateway of last resort.
```

The default route is the last choice, not the first.

### Routing Knowledge Builds In Layers

A router learns routes in stages:

1. Connected routes appear from active interfaces.
2. Static routes add specific remote networks.
3. A default route covers all remaining unknown destinations.
4. Dynamic routing protocols can exchange routes automatically.

Each layer extends the previous one.

### What The ISP Provides

An ISP usually provides:

- a public IP address for the customer router;
- a subnet mask or prefix length;
- the ISP next-hop IP;
- DNS information;
- sometimes VLAN, encapsulation or authentication settings.

These values should not be guessed. Obtain and document them from the provider.

Example:

```text
Cafe router public IP: 216.0.5.2/30
ISP router IP:         216.0.5.1/30
```

### Why `/30` Is Common

A `/30` prefix corresponds to:

```text
255.255.255.252
```

A traditional `/30` subnet contains four addresses:

- network address;
- two usable host addresses;
- broadcast address.

This works well for an IPv4 point-to-point link that needs an address at each router end.

Modern networks can also use `/31`, but `/30` remains common in labs and legacy designs.

### Configure The ISP Interface First

Before adding the default route, establish the ISP link.

Example:

```cisco
enable
configure terminal
interface GigabitEthernet0/2
 description Link to ISP
 ip address 216.0.5.2 255.255.255.252
 no shutdown
end
```

Verification:

```cisco
show ip interface brief
ping 216.0.5.1
```

If the ISP next hop is unreachable, the default route cannot provide internet connectivity.

### Default Route Command

Basic Cisco IOS command:

```cisco
ip route 0.0.0.0 0.0.0.0 216.0.5.1
```

| Part | Meaning |
| --- | --- |
| `0.0.0.0` | Any destination network |
| `0.0.0.0` | Mask that matches any IPv4 address |
| `216.0.5.1` | ISP router next hop |

In plain English:

```text
If no more specific route is found, send the packet to 216.0.5.1.
```

### Why `0.0.0.0/0` Matches Everything

CIDR notation:

```text
0.0.0.0/0
```

A `/0` prefix fixes no network bits, so every IPv4 destination matches it.

However, the routing table may contain more specific matches.

### Longest Prefix Match

A router selects the most specific matching route, meaning the route with the longest prefix.

Example:

```text
192.168.3.0/24 via 192.168.2.2
0.0.0.0/0 via 216.0.5.1
```

A packet for `192.168.3.10` matches both routes, but `/24` is more specific than `/0`.

It is therefore sent toward the shelter router, not the ISP.

A packet for an unknown internet address such as `8.8.8.8` does not match the known specific routes and uses `/0`.

### Verify The Default Route

Use:

```cisco
show ip route
```

An expected entry can look like:

```text
S* 0.0.0.0/0 [1/0] via 216.0.5.1
```

Where:

- `S` means static route;
- `*` means candidate default;
- `0.0.0.0/0` is the default destination;
- `216.0.5.1` is the next hop.

The output may also show:

```text
Gateway of last resort is 216.0.5.1 to network 0.0.0.0
```

### NetworkChuck Coffee Packet Flow

A cafe user opens a website:

1. The PC determines that the destination is outside its local subnet.
2. The PC sends the frame to its default gateway.
3. The cafe router receives the packet.
4. The router searches the routing table.
5. No more specific route exists.
6. The router selects the default route.
7. The packet is forwarded to the ISP router.
8. The provider and internet routing infrastructure continue forwarding it.

```text
Cafe PC
  -> Cafe switch
  -> Cafe router
  -> default route
  -> ISP router
  -> Internet
```

### What Happens Without A Default Route

Internal networks can still work without a default route:

- hosts communicate inside the LAN;
- the cafe reaches the shelter through a static route;
- routers ping connected interfaces.

Unknown internet destinations have no matching route.

The router drops those packets:

```text
No matching route -> packet dropped
```

### Default Route Does Not Solve Everything

A default route provides outbound direction, but internet access can also require:

- valid public addressing;
- NAT/PAT for private hosts;
- an ISP return route;
- DNS;
- firewall or ACL policy;
- a working physical link;
- correct client default gateways.

The default route can send a private host's packet toward the ISP, but without NAT the private source address normally cannot be routed across the public internet.

### BGP And Internet-Scale Routing

Large providers and networks exchange internet routes with BGP.

BGP stands for Border Gateway Protocol.

It allows autonomous systems to advertise the prefixes they can reach.

A small cafe router does not need a full internet routing table. It sends unknown traffic to its provider, which has broader routing knowledge.

### Troubleshooting Order

If default routing does not work:

1. Check the ISP interface status.
2. Check the public IP address and mask.
3. Ping the ISP next hop.
4. Check `show ip route`.
5. Confirm the `0.0.0.0/0` route.
6. Check for a next-hop typo.
7. Check NAT for private clients.
8. Check ACL and firewall rules.
9. Test DNS separately from IP reachability.
10. Confirm that the ISP has a return path.

### Save The Configuration

After verification:

```cisco
copy running-config startup-config
```

Otherwise, the default route will disappear after a reload.

## Configuration Example

```cisco
enable
configure terminal

interface GigabitEthernet0/2
 description Internet uplink
 ip address 216.0.5.2 255.255.255.252
 no shutdown

ip route 0.0.0.0 0.0.0.0 216.0.5.1

end
show ip interface brief
show ip route
ping 216.0.5.1
```

## Practical Checklist

- Obtain addressing information from the ISP.
- Configure the ISP-facing interface.
- Verify the `up/up` state.
- Verify ISP next-hop reachability.
- Configure `0.0.0.0/0`.
- Look for `S*` in the routing table.
- Confirm specific static routes still take priority.
- Check NAT for private networks.
- Test DNS after IP connectivity.
- Save the configuration.

## Quick Self-Check

### Question 1

When is a default route used?

Answer:

```text
When the routing table has no more specific route to the destination.
```

### Question 2

What is the IPv4 default route?

Answer:

```text
0.0.0.0/0
```

### Question 3

What is the gateway of last resort?

Answer:

```text
The next hop used for traffic whose destination has no more specific route.
```

### Question 4

Which route wins for `192.168.3.10`: `192.168.3.0/24` or `0.0.0.0/0`?

Answer:

```text
192.168.3.0/24 because it is the more specific prefix.
```

### Question 5

How is a default static route marked in a Cisco routing table?

Answer:

```text
S*
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Default route | Fallback route for unknown destinations. |
| `0.0.0.0/0` | IPv4 prefix that matches every destination. |
| Gateway of last resort | Next hop for traffic without a more specific route. |
| `ip route 0.0.0.0 0.0.0.0 <next-hop>` | Cisco default static route command. |
| `S*` | Static candidate default route in a Cisco routing table. |
| ISP | Internet service provider. |
| Public IP | Address routable on the public internet. |
| Longest prefix match | Selection of the most specific matching route. |
| `/30` | Small IPv4 subnet with two traditionally usable addresses. |
| BGP | Internet-scale routing protocol between autonomous systems. |

## What To Review Later

- NAT and PAT
- Longest prefix match
- Floating default routes
- BGP basics
- IPv4 subnetting
- ISP edge design
- Default route troubleshooting
