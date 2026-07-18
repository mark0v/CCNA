# Building IPv6 Between Sites With Static Routes

Source: закрытая страница курса  
Date added: 2026-07-18  
Related plan item: Week 12 / Building IPv6 between sites with static routes  
Tags: IPv6, global unicast, unique local, link-local, EUI-64, static routing, WAN, dual stack, Castle Rysen
Language: Russian
Translation pair: articles-en/2026-07/week-12/07-building-ipv6-between-sites-with-static-routes.md

## Summary

- IPv6 становится понятнее, когда его реально настраиваешь на topology, а не только читаешь address theory.
- Global unicast addresses are globally unique and routable, similar in role to public IPv4 addresses.
- Unique local addresses use `fd00::/8` for internal-only IPv6 addressing.
- Link-local addresses use `fe80::/10` and appear automatically for local-link communication.
- EUI-64 can generate the host portion of an IPv6 address from the interface MAC address.
- IPv6 static routing uses the same idea as IPv4 static routing: `ipv6 route` points remote prefixes toward a next hop.

## Key Points

- IPv6 is not harder than IPv4; it is less familiar.
- IPv6 interfaces often have multiple addresses at the same time.
- Global unicast can be used directly on internal VLAN interfaces when the organization has a routed prefix.
- Unique local addressing exists, but many deployments prefer global unicast plus firewall policy.
- WAN links can use manually assigned IPv6 addresses to keep next hops easy to read.
- Addressing plus routing is what turns isolated IPv6 interfaces into a working IPv6 network.

## Notes

IPv6 starts feeling real when it leaves one interface and becomes a routed network.

At Castle Rysen, IPv6 was already working on the cafe side. The next step was to extend it to the fallout shelter, assign addressing to VLANs, create a WAN link between the sites and add static routes so both sides could reach each other.

That is the difference between "I configured IPv6 addresses" and "I built an IPv6 network."

## The Big IPv6 Shift

IPv4 taught us to conserve public addresses. The usual model:

- ISP gives a small number of public IPv4 addresses;
- internal networks use private IPv4;
- NAT hides many inside devices behind fewer public addresses.

IPv6 changes that model.

An ISP can give a large routed IPv6 prefix, and the organization can number internal networks with global unicast addresses. That does not mean "no security." It means address uniqueness and routing are separate from access control. Firewalls still decide what is allowed.

This is a mindset change:

| IPv4 habit | IPv6 mindset |
| --- | --- |
| Conserve public addresses | Organize large address space cleanly. |
| NAT is expected | Routing plus firewall policy is expected. |
| Private inside, public outside | Global unicast may exist inside too. |
| Address scarcity drives design | Structure and supportability drive design. |

## Global Unicast Addresses

Global unicast addresses are IPv6 addresses intended to be globally unique and routable.

In practical terms, this is the IPv6 category you usually think of when assigning normal routed addresses to VLAN interfaces, WAN interfaces or hosts that need regular network communication.

Example documentation prefix:

```text
2001:db8:1::/48
```

Example VLAN subnets:

```text
2001:db8:1:1::/64
2001:db8:1:2::/64
2001:db8:1:3::/64
```

The exact production prefix should come from your provider or internal IPv6 plan, but the design idea is the same: carve predictable `/64` networks for each VLAN or segment.

## Unique Local Addresses

IPv6 does have private-style addressing. The practical range to remember:

```text
fd00::/8
```

These are called unique local addresses, or ULAs. They are intended for internal communication and should not be routed on the public internet.

There is also `fc00::/8`, but for practical CCNA-level work and most real conversations, `fd00::/8` is the one to recognize.

Use cases:

- internal-only networks;
- labs;
- environments without provider-assigned IPv6;
- designs where internal addressing should not depend on ISP prefix changes.

But many real IPv6 designs use global unicast internally and rely on firewall policy for security. Do not assume "globally unique" means "open to the internet."

## Link-Local Addresses

IPv6 interfaces commonly have a link-local address automatically.

Range:

```text
fe80::/10
```

Link-local addresses are used only on the local network segment. They are not routed across the internet or across normal routed boundaries.

They matter for:

- neighbor discovery;
- router discovery;
- local next-hop communication;
- routing protocol adjacencies;
- basic IPv6 interface behavior.

If you run:

```text
show ipv6 interface brief
```

and see an `fe80::` address, that is normal. You did not necessarily configure it manually. IPv6 created it because the interface needs local communication.

## EUI-64

EUI-64 is a method for generating the interface identifier, the host portion of an IPv6 address, from a MAC address.

The general idea:

1. Start with the interface MAC address.
2. Split it into two halves.
3. Insert `fffe` in the middle.
4. Flip the universal/local bit.
5. Use the result as the 64-bit interface identifier.

On Cisco, you may see configuration like:

```text
ipv6 address 2001:db8:1:10::/64 eui-64
```

That means the router uses the prefix you provided and generates the host portion automatically.

EUI-64 is useful to understand, especially for labs and protocol behavior. In production, many engineers prefer manually planned addresses for routers because they are easier to read, document and use as next hops.

## WAN Link And Static Routes

For the WAN link between the cafe and fallout shelter, manually assigned IPv6 addresses can make troubleshooting cleaner.

Example:

```text
Cafe WAN router:    2001:db8:1:100::1/64
Shelter WAN router: 2001:db8:1:100::2/64
```

Now the static routes are easy to read.

On the cafe router, routes to shelter networks point to the shelter WAN address:

```text
ipv6 route 2001:db8:1:20::/64 2001:db8:1:100::2
ipv6 route 2001:db8:1:30::/64 2001:db8:1:100::2
```

On the shelter router, routes to cafe networks point back to the cafe WAN address:

```text
ipv6 route 2001:db8:1:1::/64 2001:db8:1:100::1
ipv6 route 2001:db8:1:2::/64 2001:db8:1:100::1
```

The concept is the same as IPv4:

```text
To reach that remote network, send packets to this next hop.
```

The command is just `ipv6 route` instead of `ip route`.

## Verification

Useful checks:

```text
show ipv6 interface brief
show ipv6 route
ping 2001:db8:1:20::1
traceroute 2001:db8:1:20::1
```

What to confirm:

- interfaces have expected global unicast addresses;
- link-local addresses exist;
- WAN link has reachable next-hop addresses;
- static routes appear in the IPv6 routing table;
- ping across the WAN works;
- return routes exist.

Return routing matters. If cafe can send traffic to shelter but shelter has no route back, the test still fails.

## NetworkChuck Coffee Design View

For Castle Rysen and NetworkChuck Coffee, this is the point where IPv6 becomes more than address formatting.

The environment now has:

- IPv6 on cafe VLANs;
- IPv6 on fallout shelter VLANs;
- IPv6 on the WAN link;
- static routes in both directions;
- working cross-site connectivity.

That is a real IPv6 overlay. IPv4 still exists, but IPv6 can now route across the environment too.

## Main Takeaway

IPv6 is not alien technology. It has bigger addresses and new address types, but the networking logic is familiar.

You still need:

- interface addresses;
- subnets;
- WAN links;
- routing;
- next hops;
- verification.

The more you use it, the more normal it becomes.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Global unicast | Globally unique, routable IPv6 address type. |
| Unique local | Internal-only IPv6 address type, commonly `fd00::/8`. |
| Link-local | Local-link IPv6 address, commonly `fe80::/10`. |
| EUI-64 | Method to generate IPv6 interface ID from MAC address. |
| `ipv6 route` | Cisco command for static IPv6 routes. |
| `show ipv6 route` | Displays IPv6 routing table. |
| `show ipv6 interface brief` | Shows IPv6 interface addresses and status. |

## Questions

### 1. What is a global unicast IPv6 address?

Answer: A globally unique IPv6 address intended to be routable.

### 2. What IPv6 range is used for unique local addresses?

Answer: `fd00::/8`.

### 3. What IPv6 range is used for link-local addresses?

Answer: `fe80::/10`.

### 4. Why manually address WAN links?

Answer: Manual addresses make next hops easier to read, document and troubleshoot.

### 5. What command creates a static IPv6 route on Cisco IOS?

Answer: `ipv6 route`.

## What To Review Later

- Global unicast vs unique local vs link-local.
- EUI-64 generation steps.
- IPv6 static route syntax.
- IPv6 return path troubleshooting.
- Neighbor Discovery Protocol.
- IPv6 routing protocol behavior.
