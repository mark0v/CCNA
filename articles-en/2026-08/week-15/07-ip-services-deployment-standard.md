# IP Services Deployment Standard

Source: closed course page  
Date added: 2026-08-16  
Related plan item: Week 15 / IP services deployment standard  
Tags: IP services, DNS, NTP, DHCP, loopback, OSPF, Packet Tracer, deployment standard, documentation
Language: English
Translation pair: articles/2026-08/week-15/07-ip-services-deployment-standard.md

## Summary

- Real requirements often arrive as vague statements, not step-by-step instructions.
- The engineer's job is turning those requirements into a documented and repeatable deployment standard.
- This article ties together DNS, NTP, DHCP, loopback interfaces, and verification.
- DNS should provide clear internal names and forward unknown queries when needed.
- NTP should provide stable time synchronization for all sites.
- DHCP should provide correct options for the right VLANs.
- Packet Tracer is useful for learning, but its limitations should not be confused with real Cisco behavior.

## Key Points

- A repeatable standard matters more than a one-time working configuration.
- If Castle Rysen opens a new cafe, deployment should not start from scratch.
- A loopback interface gives a stable IP address for services such as DNS and NTP.
- If a loopback is used as a service address, it must be advertised by the routing protocol.
- Split DNS lets one name return different answers for internal and external clients.
- DHCP option 42 can provide the NTP server address to clients.
- Verification is part of the job, not a decorative final step.

## Notes

Deploying IP services "should be simple." In practice, simplicity ends where real topology, simulator limitations, and vague business requirements begin.

An RFP rarely says:

```text
Enter these ten commands in this exact order.
```

Instead, it says something like:

```text
Provide DNS, NTP, DHCP, and basic network services for the sites.
```

The engineer must translate that into a clear standard: what to configure, where to configure it, which addresses to use, how to verify, what to document, and how to repeat it at the next site.

## Requirement Becomes Standard

For Castle Rysen, the goal is not bringing the Fallout Shelter online once.

The goal:

```text
Make deployment repeatable so the next cafe can be built from the same template.
```

That requires:

- naming standard;
- DNS records;
- NTP hierarchy;
- DHCP scopes;
- stable service addresses;
- routing for service addresses;
- verification commands;
- notes about simulator limitations;
- documented exceptions.

Without a standard, every new location becomes a separate experiment. With one, deployment becomes repeatable.

## DNS As Clarity

DNS translates names into IP addresses. In a deployment standard, it also reduces troubleshooting chaos.

If you can use a name instead of an address:

```text
cafe1.castlerysen.local
```

the topology becomes clearer.

Example local mappings:

```text
ip host cafe1.castlerysen.local 203.0.113.11
ip host cafe2.castlerysen.local 203.0.113.12
```

Idea:

- internal resources get readable names;
- routers can resolve internal names;
- unknown public names go to upstream DNS;
- documentation matches naming.

For a small network, a router can be a simple DNS helper. For a large network, redundant DNS infrastructure is better.

## Split DNS

Split DNS means the same name can resolve to different IP addresses depending on where the query comes from.

Example:

| Client location | Name | Answer |
| --- | --- | --- |
| Inside network | `bob.castlerysen.com` | Private IP |
| Internet | `bob.castlerysen.com` | Public IP |

This is useful because users keep one name while the path is chosen correctly.

Internal users should not go out to the internet and loop back in just to reach a local resource.

Split DNS keeps the name consistent while making the routing path smarter.

## Loopback As Service Address

A loopback interface is a virtual interface that does not depend on one physical port.

That matters for services.

If NTP or DNS points to a physical interface, a cable change, shutdown, or redesign can break clients.

If services use a loopback:

```text
interface loopback0
 ip address 10.255.0.1 255.255.255.255
```

clients get a stable target.

But there is one condition: the network must know a route to the loopback.

If OSPF is used, the loopback should be advertised:

```text
router ospf 1
 network 10.255.0.1 0.0.0.0 area 0
```

Otherwise, the address is clean but unreachable.

## NTP Design

NTP synchronizes time.

For Castle Rysen:

- Fallout Shelter routers act as NTP masters;
- district shop routers become NTP clients;
- clients use loopback addresses as stable targets;
- routing provides reachability;
- clocks are verified with show commands.

Example:

```text
ntp master 1
ntp server 10.255.0.1
```

In production, stratum should be treated carefully. A lab can use a local master, but a real network should use reliable upstream sources and redundancy.

The main requirement: logs on routers, switches, and security devices should build one timeline.

## DHCP Design

DHCP provides IP settings to clients.

Each VLAN needs the right scope:

- patron VLAN;
- admin VLAN;
- management VLAN;
- voice VLAN, if phones exist;
- special-purpose VLANs when needed.

DHCP should provide:

- IP address;
- subnet mask;
- default gateway;
- DNS server;
- domain name;
- lease time;
- sometimes NTP server through option 42.

Option 42:

```text
DHCP option 42 = NTP server address
```

Not every simulator supports this correctly, but in real architecture it is a useful part of the standard.

## Packet Tracer And Real Devices

Packet Tracer is useful. It helps with learning, topology building, and logic.

But it is not a full replacement for real Cisco gear.

Limitations may appear in:

- DNS server behavior;
- multiple name-server support;
- `ip dns server`;
- NTP display;
- time zones;
- DHCP options;
- rare command limitations.

Takeaway:

```text
Do not memorize the simulator glitch. Understand the architecture.
```

If the lab behaves strangely, check documentation, compare with real device behavior, and record the limitation separately.

## Verification Is The Job

Deployment is not finished when commands are entered.

Verify:

```text
show hosts
show running-config | include ip name-server
ping cafe1.castlerysen.local
show ntp status
show ntp associations
show clock detail
show ip dhcp pool
show ip dhcp binding
show ip route 10.255.0.1
show ip ospf neighbor
```

Verification questions:

- do names resolve correctly?
- is the loopback reachable?
- did OSPF keep adjacency?
- is NTP synchronized?
- do DHCP scopes match VLANs?
- do clients receive correct DNS/NTP options?
- is a simulator limitation being mistaken for a design error?

## Castle Rysen Scenario

For Castle Rysen, the standard can look like this:

1. Create a loopback on Fallout Shelter routers.
2. Advertise the loopback with OSPF.
3. Configure local DNS records for cafe routers.
4. Configure upstream DNS forwarding.
5. Make Fallout Shelter routers NTP masters or clients of an internal time source.
6. Configure district routers as NTP clients.
7. Verify DHCP scopes by VLAN.
8. Add NTP option through DHCP where the platform supports it.
9. Verify everything with show commands.
10. Document the standard for the next cafe.

That turns a vague requirement into a repeatable deployment.

## Main Takeaway

IP services deployment is not just entering commands.

The real work is building a standard: stable addresses, clear DNS names, synchronized time, correct DHCP scopes, routing to service addresses, and mandatory verification.

When that is documented, a new site is no longer a new mystery. It becomes a repeatable rollout.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| IP services | Services such as DNS, NTP, and DHCP that support network operation. |
| deployment standard | Documented repeatable deployment process. |
| DNS | Name resolution service. |
| Split DNS | Different DNS answers for internal and external clients. |
| NTP | Time synchronization service. |
| DHCP | Automatic IP configuration service. |
| loopback interface | Virtual interface with a stable IP address. |
| OSPF | Routing protocol that can advertise a loopback. |
| DHCP option 42 | DHCP option for NTP server address. |
| verification | Checking that the design actually works after configuration. |

## Questions

### 1. Why turn a vague requirement into a deployment standard?

Answer: So the next site can be configured repeatedly without improvisation and hidden differences.

### 2. Why is a loopback useful for DNS and NTP?

Answer: It provides a stable service address that does not depend on one physical interface.

### 3. Why advertise the loopback with OSPF?

Answer: So other devices know the route to the service address.

### 4. What is Split DNS?

Answer: A design where the same name can return different IP addresses for internal and external clients.

### 5. Why is verification part of the job?

Answer: Commands alone do not prove that a service is reachable, synchronized, or providing correct parameters.

## What To Review Later

- DNS local mappings.
- Split DNS concept.
- Loopback interface as a service address.
- OSPF advertisement for loopback.
- NTP master/client design.
- DHCP scopes and option 42.
- Difference between simulator limitation and real design.
