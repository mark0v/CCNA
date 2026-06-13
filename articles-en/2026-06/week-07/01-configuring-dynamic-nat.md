# Configuring Dynamic NAT

Source: closed course page  
Date added: 2026-06-13  
Related plan item: Week 7 / Dynamic NAT configuration  
Tags: dynamic NAT, NAT pool, standard ACL, wildcard mask, inside local, inside global, Cisco IOS
Language: English
Translation pair: articles/2026-06/week-07/01-configuring-dynamic-nat.md

## Summary

Dynamic NAT allows a group of internal hosts to borrow addresses temporarily from a pool of public IPv4 addresses. Unlike static NAT, the administrator does not create a permanent mapping for every client in advance. The router selects an available pool address when traffic appears and creates a dynamic translation.

The configuration requires four elements:

1. Interfaces marked with `ip nat inside` and `ip nat outside`.
2. An ACL identifying the internal addresses eligible for translation.
3. A pool of available inside global addresses.
4. A command linking the ACL to the NAT pool.

Dynamic NAT is more flexible than static NAT, but it does not solve public-address scarcity. Every concurrently active internal host still needs a separate pool address. PAT, or NAT overload, is more common for general client internet access.

## Key Points

- Static NAT creates a permanent one-to-one mapping.
- Dynamic NAT assigns inside hosts available addresses from a public pool.
- Every active dynamic translation remains one-to-one.
- A standard ACL identifies the source addresses to translate.
- An ACL does nothing by itself until a feature or interface uses it.
- Wildcard mask `0.0.0.255` matches a `/24` network.
- A NAT pool defines its first address, last address and network mask.
- `ip nat inside source list ... pool ...` links the inside group to the public pool.
- Multiple routed inside segments can use the same outside interface.
- New clients cannot obtain translations after the pool is exhausted.
- The provider must route the public range toward the NAT router.
- PAT is usually more practical for large client populations.

## From Static NAT To Dynamic NAT

Static NAT looks like:

```text
192.168.10.10 <-> 216.0.5.50
192.168.10.11 <-> 216.0.5.51
192.168.10.12 <-> 216.0.5.52
```

Each mapping is configured manually and exists permanently. This works well for servers requiring predictable public addresses, but poorly for a DHCP client network.

Dynamic NAT describes two groups:

```text
Inside group: 192.168.10.0/24
Public pool:  216.0.5.50-216.0.5.100
```

When outbound traffic appears, the router temporarily associates an internal address with an available pool address:

```text
192.168.10.21 <-> 216.0.5.50
192.168.10.38 <-> 216.0.5.51
192.168.10.74 <-> 216.0.5.52
```

The administrator does not decide in advance which client receives which public address.

## Why Dynamic NAT Is Called Many-To-Many

Dynamic NAT connects many possible internal addresses to many public addresses. Each active entry, however, remains an individual one-to-one mapping:

```text
one active inside local <-> one inside global
```

Ordinary dynamic NAT cannot assign the same public address to multiple inside clients simultaneously. Address sharing is provided by PAT.

## Step 1: Mark The Interfaces

The router must know which side contains the internal addresses and which side leads outside.

Interface toward the cafe LAN:

```cisco
interface GigabitEthernet0/0
 description Cafe LAN
 ip nat inside
```

Interface toward the ISP:

```cisco
interface GigabitEthernet0/2
 description ISP uplink
 ip nat outside
```

Another routed internal segment can also participate:

```cisco
interface GigabitEthernet0/1
 description Fallout Shelter LAN
 ip nat inside
```

Marking an interface as inside is not sufficient by itself. Its network must also match the ACL used by the NAT rule.

## Step 2: Identify Inside Addresses With An ACL

For the cafe network:

```text
192.168.10.0/24
```

create a standard numbered ACL:

```cisco
access-list 1 permit 192.168.10.0 0.0.0.255
```

This entry means:

```text
Match source addresses from 192.168.10.0 through 192.168.10.255.
```

In the NAT context, `permit` means that a matching source address is eligible for translation. It does not automatically grant firewall permission.

### The ACL As A Classifier

ACLs are commonly associated with security, but their basic purpose is to match traffic against conditions.

An ACL can support:

- interface packet filtering;
- NAT;
- policy-based routing;
- QoS;
- route filtering;
- other IOS features.

Until a feature references the list, it only stores match conditions.

## Wildcard Masks

A wildcard mask indicates which address bits must match.

The rule is:

```text
0 = the corresponding bit must match
1 = the corresponding bit can be ignored
```

For `/24`:

```text
Subnet mask:   255.255.255.0
Wildcard mask:   0.0.0.255
```

Therefore:

```cisco
access-list 1 permit 192.168.10.0 0.0.0.255
```

fixes the first three octets and permits any value in the last octet.

A practical calculation is:

```text
255.255.255.255
- subnet mask
= wildcard mask
```

### Adding A Second Inside Network

If another segment is:

```text
192.168.20.0/24
```

add it to the same ACL:

```cisco
access-list 1 permit 192.168.20.0 0.0.0.255
```

Verify it with:

```cisco
show access-lists 1
```

Modern IOS displays sequence numbers even when the older numbered syntax created the ACL.

## Step 3: Create The Public NAT Pool

The lab uses:

```text
216.0.5.50-216.0.5.100
```

Create the pool:

```cisco
ip nat pool cafepublic 216.0.5.50 216.0.5.100 netmask 255.255.255.0
```

Read it as:

```text
Create a NAT pool named cafepublic,
starting at 216.0.5.50,
ending at 216.0.5.100,
with mask 255.255.255.0.
```

The name `cafepublic` has local significance only in the router configuration.

### Pool Size

The range is inclusive:

```text
100 - 50 + 1 = 51
```

The pool therefore contains 51 inside global addresses.

An arbitrary range cannot be treated as public space. The provider must allocate it to the organization and route it toward the NAT router.

## Step 4: Link The ACL To The Pool

The dynamic NAT command is:

```cisco
ip nat inside source list 1 pool cafepublic
```

Read it as a sentence:

```text
For inside source addresses matched by ACL 1,
use addresses from the pool named cafepublic.
```

The rule now has:

- a classification of inside source addresses;
- a range of available inside global addresses;
- a NAT direction defined by the interface roles.

## Complete Configuration

```cisco
enable
configure terminal

interface GigabitEthernet0/0
 description Cafe LAN
 ip nat inside

interface GigabitEthernet0/1
 description Fallout Shelter LAN
 ip nat inside

interface GigabitEthernet0/2
 description ISP uplink
 ip nat outside

access-list 1 permit 192.168.10.0 0.0.0.255
access-list 1 permit 192.168.20.0 0.0.0.255

ip nat pool cafepublic 216.0.5.50 216.0.5.100 netmask 255.255.255.0
ip nat inside source list 1 pool cafepublic

end
```

Adapt interface names, internal networks and the public range to the actual topology.

## What Happens To A Packet

Suppose this client:

```text
192.168.10.21
```

sends internet traffic.

The router:

1. Receives the packet on an `ip nat inside` interface.
2. Matches the source address against ACL 1.
3. Finds an available address in `cafepublic`.
4. Creates a translation such as:

```text
192.168.10.21 <-> 216.0.5.50
```

5. Forwards the translated packet through an `ip nat outside` interface.
6. Uses the entry for return traffic.

The next inside client receives another available pool address.

## Verification

Display NAT entries:

```cisco
show ip nat translations
```

Example:

```text
Pro  Inside global  Inside local     Outside local  Outside global
---  216.0.5.50     192.168.10.21    ---            ---
---  216.0.5.51     192.168.20.15    ---            ---
```

Display NAT parameters and counters:

```cisco
show ip nat statistics
```

Check the ACL:

```cisco
show access-lists 1
```

Inspect the configuration:

```cisco
show running-config | include ip nat
show running-config | include access-list
show ip interface brief
show ip route
```

Generate traffic from an eligible internal client to a reachable outside host to create translations.

## The Main Limit: Pool Exhaustion

A pool of 51 addresses supports no more than 51 concurrent one-to-one translations.

When every address is occupied:

```text
Client 1  -> public address 1
Client 2  -> public address 2
...
Client 51 -> public address 51
Client 52 -> no available public address
```

The ACL can match, routing can work and interface roles can be correct, but client 52 cannot obtain a translation until an address becomes available.

This limitation is why dynamic NAT is not the usual final solution for a large client population.

## Dynamic NAT Versus PAT

| Property | Dynamic NAT | PAT / NAT overload |
| --- | --- | --- |
| Public addresses | Address pool | One or more addresses |
| Active mapping | One public IP per inside host | One public IP for many sessions |
| Separation | By IP address | By protocol and port/identifier |
| Scalability | Limited by pool size | Much higher |
| Common use | Specialized pool requirements | General internet access |

Dynamic NAT is useful when:

- the organization truly owns a public pool;
- each active host requires a separate public source address;
- the association can be temporary;
- concurrent hosts do not exceed the pool size.

PAT is more practical when many clients must share one or a few public addresses.

## Routing The Public Pool

NAT does not create routes throughout the outside network.

The provider must deliver traffic for:

```text
216.0.5.50-216.0.5.100
```

to the edge router. A connected subnet, provider route or routed public block can provide this.

The router also needs:

- a route to outside destinations;
- routes to the inside networks;
- correct client default gateways;
- a valid return path.

## Clearing Dynamic Entries

In a lab:

```cisco
clear ip nat translation *
```

This removes current dynamic translations. In production it can interrupt active connections and should be used only after evaluating the impact.

Removing the configuration is separate:

```cisco
no ip nat inside source list 1 pool cafepublic
no ip nat pool cafepublic
no access-list 1
```

Remove the rule referencing the pool and ACL first.

## Troubleshooting Order

If dynamic NAT does not work:

1. Verify the client IP address, mask and default gateway.
2. Verify routing without assuming NAT repairs routes.
3. Check `ip nat inside` on the ingress interface.
4. Check `ip nat outside` on the external interface.
5. Confirm that the source address matches the ACL.
6. Check ACL hit counters with `show access-lists`.
7. Verify the NAT pool name and range.
8. Verify the command linking the ACL and pool.
9. Check for available pool addresses.
10. Verify provider routing for the public pool.
11. Check ACL or firewall policy.
12. Inspect `show ip nat translations` and `show ip nat statistics`.

## Common Mistakes

### Creating An ACL Without Applying It

The list performs no action by itself. NAT must reference it:

```cisco
ip nat inside source list 1 pool cafepublic
```

### Confusing The Wildcard And Subnet Masks

A `/24` ACL uses:

```text
0.0.0.255
```

not subnet mask `255.255.255.0`.

### Marking An Additional Inside Interface Without Updating The ACL

The interface role identifies the NAT side but does not automatically include its source network.

### Excluding The Last Pool Address

The boundaries are inclusive. `.50-.100` contains 51 addresses.

### Expecting One Address To Be Shared

Ordinary dynamic NAT does not overload an address. PAT is required for sharing.

### Using An Arbitrary Public Range

Inside global addresses must be allocated and routed to the organization.

## Quick Self-Check

### Question 1

How does dynamic NAT differ from static NAT?

Answer:

```text
Dynamic NAT temporarily selects an available inside global address from a pool,
while static NAT uses a preconfigured permanent mapping.
```

### Question 2

What does the ACL do in this configuration?

Answer:

```text
It identifies source addresses to which dynamic NAT applies.
```

### Question 3

How many addresses are in the `.50-.100` range?

Answer:

```text
51 addresses: 100 - 50 + 1.
```

### Question 4

What happens to the 52nd concurrently active client?

Answer:

```text
It cannot receive a translation until a public pool address becomes available.
```

### Question 5

Why is PAT more common for general internet access?

Answer:

```text
PAT allows many clients to share one or a few public addresses
by distinguishing sessions with transport information.
```

## Commands / Terms

| Command / Term | Purpose |
| --- | --- |
| Dynamic NAT | Temporary assignment from a public address pool. |
| NAT pool | Range of inside global addresses. |
| Standard ACL | Matches source IPv4 addresses. |
| Wildcard mask | Identifies significant and ignored address bits. |
| `ip nat inside` | Marks the internal NAT side. |
| `ip nat outside` | Marks the external NAT side. |
| `access-list 1 permit ...` | Identifies inside source addresses. |
| `ip nat pool ...` | Creates an address pool. |
| `ip nat inside source list 1 pool cafepublic` | Links the ACL and pool. |
| `show ip nat translations` | Displays active mappings. |
| `show ip nat statistics` | Displays NAT configuration and counters. |
| `show access-lists` | Displays ACL entries and match counters. |

## What To Review Later

- Named standard ACLs
- Wildcard masks for different prefix lengths
- Dynamic NAT timeouts
- PAT / NAT overload
- NAT order of operations
- Public pool routing
- NAT troubleshooting
