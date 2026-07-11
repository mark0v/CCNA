# FHRP Virtual IP And Virtual MAC

Source: закрытая страница курса  
Date added: 2026-07-11  
Related plan item: Week 11 / FHRP virtual IP and virtual MAC  
Tags: FHRP, HSRP, VRRP, GLBP, virtual IP, virtual MAC, default gateway, ARP
Language: Russian
Translation pair: articles-en/2026-07/week-11/09-fhrp-virtual-ip-and-virtual-mac.md

## Summary

- Dynamic routing делает routers resilient, но hosts все равно обычно знают только один default gateway.
- Если gateway disappears, host не выбирает другой router автоматически.
- FHRP решает first-hop problem через virtual IP и virtual MAC.
- HSRP, VRRP и GLBP - основные protocols в этой family.
- Virtual MAC так же важен, как virtual IP, потому что hosts forward traffic на Layer 2 через ARP.

## Key Points

- Router redundancy and host gateway redundancy are different problems.
- FHRP lets two or more routers act like one gateway for hosts.
- Hosts keep using the same default gateway IP during failover.
- Standby router takes over virtual IP and virtual MAC when active router fails.
- HSRP is Cisco active/standby, VRRP is standards-based, GLBP adds load balancing.

## Notes

Dynamic routing protocols решают route resiliency between routers. OSPF, EIGRP or RIP могут помочь routers find alternate paths when links fail. Но это не значит, что end devices automatically protected.

Host usually gets one default gateway. Laptop, printer, POS terminal or server does not run OSPF. It does not learn alternate paths. It knows: "if destination is outside my subnet, send it to this gateway."

Если every host points to Router 1 and Router 1 fails, backup Router 2 can still be perfectly healthy. Но hosts won't magically switch to it. Backup path exists, but endpoints cannot use it.

Главная мысль:

> Router redundancy and host gateway redundancy are not the same thing.

## What FHRP Solves

First hop - это first Layer 3 device, к которому host отправляет off-subnet traffic. Обычно это default gateway.

FHRP, First Hop Redundancy Protocol, делает first hop resilient:

- hosts configure one gateway IP;
- routers share that gateway identity;
- one router is active;
- another router is standby;
- if active fails, standby takes over;
- hosts keep using same gateway.

Это failover at gateway level, без manual changes on every host and without waiting for DHCP renewals.

## Virtual IP

Вместо того чтобы использовать physical IP одного router-а как default gateway, FHRP создает virtual IP.

Example:

| Device | Physical IP | Role |
| --- | --- | --- |
| Router 1 | `10.10.10.2` | Active |
| Router 2 | `10.10.10.3` | Standby |
| FHRP virtual gateway | `10.10.10.1` | Default gateway for hosts |

Hosts use `10.10.10.1` as default gateway. They do not care which physical router is active right now.

If Router 1 fails, Router 2 takes over the same virtual IP. Host configuration does not change.

## Virtual MAC

Virtual IP is only half the solution.

On a LAN, hosts do not forward frames directly to an IP. They use ARP to resolve gateway IP to MAC address:

```text
Who has 10.10.10.1?
```

If active router answered with its physical MAC and then failed, hosts might continue sending frames to old physical MAC until ARP cache expires. That would delay failover and cause outage.

FHRP solves this by using virtual MAC.

The active router answers ARP for the virtual IP with virtual MAC. When standby becomes active, it starts using that same virtual MAC identity.

Result:

- host keeps gateway IP;
- host keeps gateway MAC;
- standby router takes over behind the scenes;
- traffic continues without waiting for every host to relearn ARP.

This is why FHRP works as a real production failover mechanism, not just a nice diagram.

## HSRP, VRRP, GLBP

Three names to know:

| Protocol | Meaning | Practical model |
| --- | --- | --- |
| HSRP | Hot Standby Router Protocol | Cisco active/standby gateway failover. |
| VRRP | Virtual Router Redundancy Protocol | Standards-based active/standby style redundancy. |
| GLBP | Gateway Load Balancing Protocol | Cisco gateway redundancy with load balancing behavior. |

HSRP is Cisco's original first-hop redundancy protocol. One router is active and one is standby.

VRRP is standards-based and more common in mixed-vendor environments.

GLBP adds load balancing. It can distribute hosts across multiple routers while keeping gateway redundancy.

For now, do not overcomplicate it. The base concept is the same: make the host's default gateway survive a router failure.

## Hello Messages And Failover

FHRP routers check each other with hello messages. Standby router listens for active router.

If standby stops hearing expected hellos:

1. It assumes active router failed.
2. It takes over virtual gateway role.
3. It starts answering for virtual IP.
4. It uses virtual MAC.
5. Hosts continue sending traffic to same gateway identity.

This is what makes failover mostly invisible to users. They do not know the physical router changed.

## Why This Matters In Production

At NetworkChuck Coffee, imagine morning rush:

- POS systems process payments;
- mobile orders flow in;
- inventory sync runs;
- guest Wi-Fi is full;
- office systems use cloud services.

If primary gateway dies and every device points to that gateway's physical IP, the store feels offline. A second router sitting in the rack does not help unless hosts have a way to use it.

FHRP closes that gap.

It also changes troubleshooting thinking. Do not only ask:

```text
Can the router reach the internet?
```

Ask:

```text
What does the endpoint believe its gateway is?
Who owns that gateway right now?
Is the virtual MAC reachable?
Did failover actually happen?
```

## Commands / Terms

| Term | Meaning |
| --- | --- |
| FHRP | First Hop Redundancy Protocol, provides resilient default gateway. |
| First hop | First Layer 3 device host uses for off-subnet traffic. |
| Virtual IP | Shared gateway IP configured on hosts. |
| Virtual MAC | Shared MAC address used by current active gateway. |
| HSRP | Cisco first-hop redundancy protocol. |
| VRRP | Standards-based first-hop redundancy protocol. |
| GLBP | Cisco protocol that adds gateway load balancing. |
| ARP | Address Resolution Protocol, maps IP address to MAC address on LAN. |

## Questions

### 1. Why is dynamic routing not enough for hosts?

Answer: Hosts usually do not run routing protocols. They know one default gateway and keep using it unless something changes their configuration or FHRP handles failover.

### 2. What problem does virtual IP solve?

Answer: It gives hosts one stable gateway IP that can move between routers during failover.

### 3. Why does FHRP need virtual MAC?

Answer: Hosts send frames to a MAC address after ARP resolution. Virtual MAC lets standby router take over without hosts waiting for ARP cache expiration.

### 4. What is the difference between HSRP and VRRP?

Answer: HSRP is Cisco's protocol, while VRRP is standards-based and useful in mixed-vendor environments.

### 5. What makes GLBP different?

Answer: GLBP adds gateway load balancing behavior instead of only active/standby failover.

## What To Review Later

- HSRP active and standby states.
- How ARP works with default gateways.
- Virtual MAC formats for HSRP and VRRP.
- Failover testing for first-hop redundancy.
