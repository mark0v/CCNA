# Rolling Out IPv6 As An Overlay

Source: closed course page  
Date added: 2026-07-18  
Related plan item: Week 12 / Rolling out IPv6 as an overlay  
Tags: IPv6, dual stack, overlay, /48, /64, hextet, VLAN, Cisco, ipv6 unicast-routing, link-local
Language: English
Translation pair: articles/2026-07/week-12/06-rolling-out-ipv6-as-an-overlay.md

## Summary

- IPv6 rollout often starts not by replacing IPv4, but by overlaying IPv6 beside the existing IPv4 network.
- In IPv6, subnetting is usually more about organization than conservation.
- Common design: an ISP gives a `/48`, and the site creates many `/64` LAN subnets.
- The fourth hextet is a clean place to encode internal subnet or VLAN structure.
- A Cisco router needs `ipv6 unicast-routing`; otherwise it can have IPv6 addresses but not route IPv6 traffic.
- `show ipv6 interface brief` will show assigned IPv6 addresses plus automatically generated link-local `fe80::` addresses.

## Key Points

- Overlay means IPv6 runs alongside IPv4 during transition.
- IPv4 is not disappearing overnight, and many environments stay dual stack for a long time.
- A `/48` can provide 65,536 `/64` subnets.
- A `/64` is the normal IPv6 LAN prefix size.
- `2001:db8::/32` is reserved for documentation examples.
- Link-local addresses are normal and appear automatically on IPv6-enabled interfaces.

## Notes

A practical IPv6 rollout does not have to start with a massive theory dump or a full replacement of IPv4.

Most real networks do not rip out IPv4 overnight. They add IPv6 alongside it, validate behavior, extend support where needed, and slowly grow operational comfort.

That model is called dual stack or overlay-style deployment: IPv4 keeps working, IPv6 starts working too.

## Why Overlay Makes Sense

IPv4 is still everywhere:

- internal addressing;
- NAT designs;
- legacy devices;
- older applications;
- small business networks;
- equipment that only partially supports IPv6.

Because of that, IPv6 usually arrives beside IPv4, not instead of IPv4.

Useful mindset:

| Old assumption | Better rollout mindset |
| --- | --- |
| Replace IPv4 immediately | Add IPv6 where it makes sense. |
| Perfect every concept first | Build a clean pattern and learn by operating it. |
| Treat IPv6 as separate world | Run it alongside the existing network. |
| Subnet to conserve addresses | Subnet to organize the design. |

## IPv6 Subnetting Mindset

IPv4 subnetting often feels like address rationing. You count hosts, calculate increments, preserve addresses, and avoid waste.

IPv6 changes that pressure.

With IPv6, the address space is huge enough that design focuses more on:

- clean structure;
- readable subnets;
- repeatable patterns;
- easy troubleshooting;
- long-term growth.

The line to remember:

```text
In IPv4, we subnet to conserve. In IPv6, we subnet to organize.
```

That does not mean IPv6 design can be sloppy. It means the goal changes from squeezing addresses to building a logical structure.

## /48 To /64 Planning

A common provider allocation for an organization or site might be a `/48`.

An IPv6 address has eight hextets:

```text
2001:db8:0001:0000:0000:0000:0000:0000
```

Each hextet is 16 bits.

If the prefix is `/48`, the first three hextets are the assigned network space:

```text
2001:db8:1::/48
```

That leaves the fourth hextet as a convenient subnet field.

Examples:

| VLAN / subnet | IPv6 subnet |
| --- | --- |
| VLAN 10 | `2001:db8:1:1::/64` |
| VLAN 20 | `2001:db8:1:2::/64` |
| VLAN 30 | `2001:db8:1:3::/64` |

Using a `/48` this way gives 65,536 possible `/64` networks because the fourth hextet is 16 bits.

## VLAN Numbers And Hex

Be careful when trying to match VLAN IDs directly to IPv6 hextets.

IPv6 hextets are hexadecimal. Decimal and hexadecimal are not always visually identical.

Examples:

| Decimal VLAN | Hex value |
| --- | --- |
| 10 | `a` |
| 20 | `14` |
| 30 | `1e` |

You do not have to build a clever conversion-based scheme. In many real environments, a simple pattern that your team understands is better than a technically elegant pattern nobody remembers.

The goal is supportability.

## Cisco Router Configuration

Before a Cisco router can route IPv6 traffic, enable IPv6 routing globally:

```text
ipv6 unicast-routing
```

This command matters. Without it, you may still be able to assign IPv6 addresses to interfaces, but the router will not forward IPv6 between networks.

Example subinterface configuration:

```text
interface g0/0.10
 encapsulation dot1Q 10
 ipv6 address 2001:db8:1:1::1/64

interface g0/0.20
 encapsulation dot1Q 20
 ipv6 address 2001:db8:1:2::1/64
```

This is familiar if you already understand router-on-a-stick for IPv4. The shape is the same: one physical interface, multiple VLAN subinterfaces, each with its own gateway address.

## Verification

Useful command:

```text
show ipv6 interface brief
```

This shows IPv6-enabled interfaces and their addresses.

You should expect to see:

- manually assigned global unicast addresses, such as `2001:db8:1:1::1`;
- automatically generated link-local addresses, usually starting with `fe80::`.

That `fe80::` address is not a mistake. IPv6 interfaces use link-local addresses for local-link communication, and they appear automatically when IPv6 is enabled on an interface.

The link-local topic matters enough to deserve its own lesson.

## NetworkChuck Coffee Design View

For Castle Rysen Cafe or NetworkChuck Coffee, IPv6 rollout should not break what already works.

A practical approach:

1. Keep the IPv4 network stable.
2. Pick a clean IPv6 prefix plan.
3. Assign `/64` per VLAN.
4. Enable IPv6 routing.
5. Add IPv6 addresses to router subinterfaces.
6. Verify interface state.
7. Expand gradually.

This is how real transitions usually happen: controlled, layered, and reversible enough that the business is not betting everything on one big cutover.

## Main Takeaway

IPv6 rollout becomes less intimidating when you treat it as an overlay first.

You do not have to destroy IPv4 to learn IPv6. Put IPv6 beside it, use a clean `/48` to `/64` pattern, enable `ipv6 unicast-routing`, and verify the addresses that appear.

The network starts becoming dual stack, and the IPv6 concepts become easier because they are now attached to a working topology.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `ipv6 unicast-routing` | Enables IPv6 routing globally on a Cisco router. |
| `ipv6 address .../64` | Assigns an IPv6 address and prefix to an interface. |
| `show ipv6 interface brief` | Shows IPv6 addresses and interface status. |
| Overlay | IPv6 running alongside existing IPv4. |
| Dual stack | IPv4 and IPv6 enabled at the same time. |
| `/48` | Common provider/site allocation size. |
| `/64` | Common IPv6 LAN subnet size. |
| Hextet | 16-bit hexadecimal IPv6 address group. |
| Link-local | IPv6 address scoped to one local link, commonly `fe80::/10`. |

## Questions

### 1. What does IPv6 overlay mean?

Answer: IPv6 runs alongside the existing IPv4 network instead of replacing it immediately.

### 2. Why does IPv6 subnetting feel different from IPv4?

Answer: IPv6 has huge address space, so subnetting focuses more on organization than conservation.

### 3. How many `/64` subnets can a `/48` provide?

Answer: 65,536 `/64` subnets.

### 4. What Cisco command enables IPv6 routing globally?

Answer: `ipv6 unicast-routing`.

### 5. Why does an `fe80::` address appear automatically?

Answer: It is a link-local address generated for local IPv6 communication on that interface.

## What To Review Later

- IPv6 global unicast addresses.
- Link-local addresses and `fe80::/10`.
- Router advertisements.
- SLAAC and DHCPv6.
- IPv6 routing verification.
- Dual-stack troubleshooting.
