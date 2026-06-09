# Configuring Static NAT

Source: closed course page  
Date added: 2026-06-09  
Related plan item: Week 6 / Static NAT configuration  
Tags: static NAT, ip nat inside, ip nat outside, port forwarding, translation table, Cisco IOS
Language: English
Translation pair: articles/2026-06/week-06/11-configuring-static-nat.md

## Summary

Static NAT creates a permanent bidirectional one-to-one mapping between an inside local and an inside global address. It suits an internal server or another host that requires a predictable public identity.

The translation command alone is insufficient. The router must also know which interface is NAT inside and which is NAT outside. Verification includes `show ip nat translations`, routing checks and end-to-end tests.

## Key Points

- Static NAT permanently maps one internal address to one external address.
- The mapping supports outbound and inbound traffic.
- The primary command is `ip nat inside source static`.
- The internal interface receives `ip nat inside`.
- The internet-facing interface receives `ip nat outside`.
- A static mapping appears in the NAT table without active traffic.
- Static NAT does not provide general internet access for every host.
- Routing and return paths must work independently of NAT.
- Port-level static NAT publishes a service instead of a whole address.
- Published services require firewall policy and security hardening.

## Notes

### Static NAT Use Case

NetworkChuck Coffee hosts an internal server:

```text
Inside local:  192.168.1.50
Inside global: 216.0.5.20
```

Customers contact `216.0.5.20`, and the edge router translates the traffic to `192.168.1.50`.

Outbound traffic from the server is also represented as `216.0.5.20`.

### One-To-One And Bidirectional

Static NAT means:

```text
One inside local address <-> one inside global address
```

```text
192.168.1.50 <-> 216.0.5.20
```

The mapping is:

- permanent;
- predictable;
- present before sessions exist;
- usable for inbound connections when routing and security permit.

### Configure The Static Mapping

In global configuration mode:

```cisco
ip nat inside source static 192.168.1.50 216.0.5.20
```

Read it as:

```text
Represent inside source 192.168.1.50
as global address 216.0.5.20.
```

Contextual help is normal:

```cisco
ip nat ?
ip nat inside ?
ip nat inside source ?
```

### Mark The Inside Interface

On the interface toward the internal server:

```cisco
interface GigabitEthernet0/0
 description Cafe LAN
 ip nat inside
```

### Mark The Outside Interface

On the interface toward the ISP:

```cisco
interface GigabitEthernet0/2
 description ISP uplink
 ip nat outside
```

Without these roles, the router has a mapping but does not know where to apply it.

### Complete Example

```cisco
enable
configure terminal

interface GigabitEthernet0/0
 description Cafe LAN
 ip nat inside

interface GigabitEthernet0/2
 description ISP uplink
 ip nat outside

ip nat inside source static 192.168.1.50 216.0.5.20

end
```

Adapt interface names and addresses to the topology.

### Public Address Routing

The ISP side must know that `216.0.5.20` is reachable through the cafe edge.

This can be provided by:

- a connected public subnet;
- a provider static route;
- a routed public block;
- proxy ARP in a supported design.

If the outside network cannot deliver traffic to the inside global address, the NAT mapping cannot help.

### Verify The Mapping

```cisco
show ip nat translations
```

A static entry can look like:

```text
Pro  Inside global  Inside local    Outside local  Outside global
---  216.0.5.20     192.168.1.50    ---            ---
```

Protocol-specific entries appear as traffic is generated.

Also use:

```cisco
show ip nat statistics
show running-config | include ip nat
show ip interface brief
show ip route
```

### Troubleshooting Order

If static NAT fails:

1. Check the static mapping.
2. Check `ip nat inside`.
3. Check `ip nat outside`.
4. Check the internal host IP, mask and gateway.
5. Check the route to the outside destination.
6. Check ISP next-hop reachability.
7. Check routing of the public inside-global address to the edge.
8. Check ACL or firewall policy.
9. Check the service on the internal host.
10. Check NAT translations and counters.

### Static NAT Is Host-Specific

If the only mapping is for:

```text
192.168.1.50
```

another host such as `192.168.1.60` receives no automatic translation.

Static NAT does not replace PAT for general user internet access.

A common design uses:

- static NAT or static PAT for published services;
- PAT overload for outbound client traffic.

### Port-Level Static Translation

Publish only a specific TCP or UDP service.

HTTPS example:

```cisco
ip nat inside source static tcp 192.168.1.50 443 216.0.5.20 443
```

Meaning:

```text
TCP 216.0.5.20:443 -> 192.168.1.50:443
```

The external port can differ:

```cisco
ip nat inside source static tcp 192.168.1.50 443 216.0.5.20 8443
```

Then:

```text
TCP 216.0.5.20:8443 -> 192.168.1.50:443
```

### Publishing Multiple Services

One public IP can direct different ports to different hosts:

```text
216.0.5.20:443 -> 192.168.1.50:443
216.0.5.20:25  -> 192.168.1.60:25
```

Each protocol/address/port combination must be unique.

### Security Considerations

Static NAT is not firewall permission.

Before publishing:

- allow only required ports;
- use a stateful firewall;
- patch the internal server;
- disable unnecessary services;
- enable logging and monitoring;
- protect authentication;
- use TLS;
- consider a DMZ instead of a user LAN;
- assess vulnerability exposure.

The ability to publish a service does not make doing so safe without controls.

### Clearing Translations

In a lab:

```cisco
clear ip nat translation *
```

In production, this interrupts active translated sessions. Use it only after evaluating impact.

## Configuration Checklist

- Identify the inside local address.
- Allocate a routable inside global address.
- Verify provider routing.
- Configure the static mapping.
- Mark the NAT inside interface.
- Mark the NAT outside interface.
- Verify routing.
- Verify firewall or ACL policy.
- Inspect the translation table.
- Test inbound and outbound directions.
- Save the configuration.
- Update documentation.

## Quick Self-Check

### Question 1

What does static NAT create?

Answer:

```text
A permanent one-to-one mapping between inside local and inside global addresses.
```

### Question 2

Which interface commands are required?

Answer:

```text
ip nat inside and ip nat outside.
```

### Question 3

Why can a mapping exist while traffic still fails?

Answer:

```text
Interface roles, routing, firewall permission or the target service can still be missing.
```

### Question 4

Does static NAT provide internet access for every internal host?

Answer:

```text
No. It translates only the explicitly configured host or service.
```

### Question 5

What does static PAT do?

Answer:

```text
It maps a specific public protocol and port to a specific internal service.
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Static NAT | Permanent one-to-one address mapping. |
| Static PAT | Permanent protocol and port mapping. |
| `ip nat inside source static` | Creates a static translation. |
| `ip nat inside` | Marks the internal interface role. |
| `ip nat outside` | Marks the external interface role. |
| Inside local | Internal host address before translation. |
| Inside global | Address representing the host outside. |
| `show ip nat translations` | Displays the translation table. |
| `show ip nat statistics` | Displays NAT roles and counters. |
| Port forwarding | Publishing an internal service through a public port. |

## What To Review Later

- Dynamic NAT configuration
- PAT overload configuration
- NAT order of operations
- Public block routing
- Proxy ARP
- DMZ design
- NAT troubleshooting
