# OSPF Network Command And Passive Interface

Source: closed course page  
Date added: 2026-07-11  
Related plan item: Week 11 / OSPF network command and passive interface  
Tags: OSPF, network command, wildcard mask, passive interface, hello packets, routing protocols
Language: English
Translation pair: articles/2026-07/week-11/03-ospf-network-command-and-passive-interface.md

## Summary

- The OSPF `network` command does two things at the same time.
- It selects interfaces where OSPF should run and advertises the connected networks on those interfaces.
- If an interface should be advertised but should not discover neighbors, use `passive-interface`.
- A wildcard mask is the inverse of a subnet mask and is used to match interfaces.
- The key point: the `network` command mainly matches interfaces; it does not manually define the exact route advertisement.

## Key Points

- The OSPF `network` command starts OSPF on matching interfaces.
- A matching interface starts sending OSPF hello packets.
- The connected network on that interface is advertised to other OSPF routers.
- `passive-interface` stops hello packets but still advertises the connected network.
- A wildcard mask is calculated as `255.255.255.255 - subnet mask`.

## Notes

The `network` command looks simple, but it often causes confusion in OSPF. It can look like it simply tells the router to "advertise this network." In reality, it does more.

In OSPF, the `network` command performs two related tasks:

1. It finds interfaces that should participate in OSPF.
2. It advertises the connected networks on those interfaces into the OSPF routing domain.

That means after the `network` command, OSPF does not only tell other routers about the connected subnet. It also starts OSPF behavior on the matching interface: sending hello packets and trying to discover neighbors.

## The Real Meaning Of Network

Imagine a NetworkChuck Coffee router with two VLANs:

- an admin VLAN for servers, management, and backups;
- a patron VLAN for guest devices and BYOD traffic.

If OSPF is enabled for the admin subnet, the router advertises that network to other sites. That is useful: the Fallout Shelter or another branch can learn how to reach admin systems.

But there is a second effect. OSPF starts sending hello packets on the interface matched by the `network` command. Hello packets are used to discover and maintain OSPF neighbor relationships.

The problem: there may be no other router on the admin VLAN that should become an OSPF neighbor. In that case, hello packets are unnecessary there.

Mental model:

> The `network` command does not only say "advertise this." It also says "run OSPF on the matching interface."

## Passive Interface

If a subnet should be advertised but OSPF neighbors should not form on that segment, use `passive-interface`.

Passive interface does something important:

- stops OSPF hello packets on the interface;
- prevents neighbor relationships on that interface;
- still advertises the connected network into OSPF.

This is especially useful for user-facing or server-facing segments. For example, the admin VLAN should be advertised so other sites know the route. But OSPF neighbors are not needed on that VLAN.

Example:

```text
router ospf 1
 network 10.0.18.0 0.0.0.31 area 0
 passive-interface g0/0.18
```

In production, a common approach is "passive by default":

```text
router ospf 1
 passive-interface default
 no passive-interface g0/1
```

The idea is simple: all interfaces are passive except the ones where an OSPF neighbor should actually form. This reduces noise, lowers the attack surface, and makes the configuration more predictable.

The security angle matters too. If OSPF is enabled on a user-facing segment and the interface is not passive, a rogue device could try to become an OSPF neighbor. That is a risk: the device could receive routing information or attempt to influence the topology.

## Wildcard Mask

The classic Cisco OSPF `network` command uses a wildcard mask. This is the inverse of the subnet mask.

Formula:

```text
255.255.255.255 - subnet mask = wildcard mask
```

Example:

| Subnet mask | Prefix | Wildcard mask |
| --- | --- | --- |
| `255.255.255.0` | `/24` | `0.0.0.255` |
| `255.255.255.224` | `/27` | `0.0.0.31` |
| `255.255.255.252` | `/30` | `0.0.0.3` |
| `255.255.255.255` | `/32` | `0.0.0.0` |

For a `/27`, the subnet mask is `255.255.255.224`. The last wildcard octet is `255 - 224 = 31`, so the wildcard is `0.0.0.31`.

## Matching Interface, Not Defining Route

The most important detail: the `network` command does not tell OSPF to "advertise exactly this IP and wildcard as a route." It is used to match interfaces.

When OSPF finds a matching interface, it looks at that interface's real IP configuration and advertises the actual connected network.

That means you can match an exact interface IP with wildcard `0.0.0.0`:

```text
router ospf 1
 network 10.0.18.1 0.0.0.0 area 0
```

If the interface has IP `10.0.18.1/27`, OSPF matches that exact interface. Then it advertises the actual connected subnet, such as `10.0.18.0/27`, not only the host route `10.0.18.1/32`.

This explains why the `network` command is better understood as "I choose this interface." After the interface is selected, two effects happen:

- OSPF runs on that interface;
- the connected network is advertised.

## Practical Checklist

Before enabling OSPF through the `network` command:

- identify which interfaces should form OSPF neighbors;
- identify which connected networks should be advertised;
- make user-facing/server-facing interfaces passive;
- verify the wildcard mask;
- after configuration, verify neighbors and routes.

Useful checks:

```text
show ip ospf neighbor
show ip protocols
show ip route ospf
show running-config | section router ospf
```

Main takeaway: the OSPF `network` command is not just an advertising command. It is an interface selection command with a route advertisement side effect. Once that is clear, OSPF configuration becomes much more logical.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `network 10.0.18.0 0.0.0.31 area 0` | Matches interfaces in that range and enables OSPF in area 0. |
| `network 10.0.18.1 0.0.0.0 area 0` | Matches one exact interface IP. |
| `passive-interface g0/0.18` | Stops OSPF hellos on that interface while still advertising the connected network. |
| `passive-interface default` | Makes all OSPF interfaces passive by default. |
| `no passive-interface g0/1` | Allows OSPF neighbor formation on a specific interface. |
| Wildcard mask | Inverse subnet mask used by Cisco matching logic. |
| Hello packet | OSPF packet used to discover and maintain neighbors. |

## Questions

### 1. What two things does the OSPF `network` command do?

Answer: It selects interfaces where OSPF will run and advertises the connected networks on those interfaces.

### 2. Why use `passive-interface`?

Answer: To advertise the connected network without sending OSPF hello packets or forming neighbors on that interface.

### 3. Why are passive interfaces useful for security?

Answer: They prevent a user-facing segment from becoming a place where a rogue device can try to form an OSPF neighbor relationship.

### 4. How do you calculate the wildcard mask for `/27`?

Answer: `/27` is `255.255.255.224`; `255 - 224 = 31`, so the wildcard is `0.0.0.31`.

### 5. Why does `network 10.0.18.1 0.0.0.0 area 0` not advertise only a host route?

Answer: Because the command matches the exact interface IP. After the match, OSPF advertises the actual connected network on that interface.

## What To Review Later

- OSPF hello packets and neighbor formation.
- Difference between interface matching and route advertisement.
- Common wildcard masks.
- `passive-interface default` production pattern.
- OSPF `show` commands for verification.
