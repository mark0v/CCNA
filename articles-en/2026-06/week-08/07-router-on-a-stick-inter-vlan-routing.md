# Router-On-A-Stick Inter-VLAN Routing

Source: closed course page  
Date added: 2026-06-20  
Related plan item: Week 8 / Inter-VLAN routing with router-on-a-stick  
Tags: VLAN, inter-VLAN routing, router-on-a-stick, subinterface, 802.1Q, DHCP, default gateway
Language: English
Translation pair: articles/2026-06/week-08/07-router-on-a-stick-inter-vlan-routing.md

## Summary

VLANs are created for separation. But sooner or later, devices in different VLANs need to reach something: a server, the internet, a shared service or another business system.

The problem is simple:

```text
VLAN 10 = separate network
VLAN 20 = separate network
Different networks need routing
```

Inter-VLAN routing is routing between VLANs.

One classic way to do it in a small network is router-on-a-stick, or ROAS.

Main ideas:

- every VLAN is a separate IP network;
- devices in different VLANs do not communicate directly at Layer 2;
- a router or Layer 3 device is required for traffic between VLANs;
- router-on-a-stick uses one physical router interface;
- subinterfaces are created on the router;
- every subinterface is tied to a VLAN with `encapsulation dot1Q`;
- the subinterface IP address becomes the default gateway for that VLAN;
- the switch port facing the router must be a trunk.

## Why VLANs Cannot Talk To Each Other

A VLAN is a separate broadcast domain and usually a separate subnet.

For example:

```text
VLAN 10 Admin:   10.0.18.0/27
VLAN 20 Patron:  10.0.18.32/27
```

A device in VLAN 10 sees its network as local.

A device in VLAN 20 sees its network as local.

But there is a Layer 3 boundary between them.

If a host wants to send traffic to another subnet, it sends that traffic to its default gateway. Without a router or Layer 3 switch, communication between VLANs will not happen.

That is not a failure. That is the point of VLAN segmentation.

## Two Ways To Route Between VLANs

There are two basic approaches.

### One Physical Interface Per VLAN

The old brute-force method:

```text
Router interface 1 -> VLAN 10
Router interface 2 -> VLAN 20
Router interface 3 -> VLAN 30
```

Each router interface connects to its VLAN and gets an IP address in that subnet.

It works, but it becomes inconvenient quickly:

- many physical router interfaces are required;
- switch ports are consumed;
- cabling becomes messy;
- adding a VLAN requires another physical connection;
- scalability is poor.

This approach is useful for understanding the concept, but rarely convenient as a practical design.

### Router-On-A-Stick

Router-on-a-stick uses one physical router interface and a trunk link to the switch.

Logical subinterfaces are created on the router:

```text
GigabitEthernet0/0.10 -> VLAN 10
GigabitEthernet0/0.20 -> VLAN 20
```

Every subinterface:

- receives a VLAN tag with `encapsulation dot1Q`;
- gets an IP address from the corresponding subnet;
- becomes the default gateway for devices in that VLAN.

One physical interface can serve multiple VLANs.

## Why The IP Is Removed From The Physical Interface

With ROAS, the IP address is usually not assigned to the main physical interface.

Not like this:

```text
interface GigabitEthernet0/0
 ip address 10.0.18.1 255.255.255.192
```

Instead, IP addresses are assigned to subinterfaces:

```text
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 10.0.18.1 255.255.255.224

interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 10.0.18.33 255.255.255.224
```

The physical interface becomes the carrier for trunk traffic.

The subinterfaces become the logical endpoints for VLANs.

## Subinterface Number

The number after the dot technically does not have to match the VLAN ID.

This is possible:

```text
GigabitEthernet0/0.123
encapsulation dot1Q 10
```

But it is bad for readability.

It is better to do this:

```text
GigabitEthernet0/0.10 -> VLAN 10
GigabitEthernet0/0.20 -> VLAN 20
```

This is not magic. It is operational sanity. A month later, the mapping is obvious.

## encapsulation dot1Q

The `encapsulation dot1Q` command tells the router which VLAN traffic should land on a subinterface.

Example:

```text
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
```

This means:

```text
Tagged frames for VLAN 10 -> handled by Gi0/0.10
```

For VLAN 20:

```text
interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
```

Without this command, the router does not know how to connect tagged VLAN traffic to its subinterfaces.

## Default Gateway For Every VLAN

The subinterface IP address becomes the default gateway for clients in that VLAN.

Example:

```text
VLAN 10 Admin subnet:   10.0.18.0/27
Gateway:                10.0.18.1

VLAN 20 Patron subnet:  10.0.18.32/27
Gateway:                10.0.18.33
```

Clients in VLAN 10 use `10.0.18.1`.

Clients in VLAN 20 use `10.0.18.33`.

If a host wants to leave its subnet, it sends traffic to its default gateway.

## DHCP Pools For Different VLANs

If the router also provides DHCP, every VLAN needs its own pool.

Example:

```text
ip dhcp pool ADMIN
 network 10.0.18.0 255.255.255.224
 default-router 10.0.18.1
 dns-server 8.8.8.8

ip dhcp pool PATRON
 network 10.0.18.32 255.255.255.224
 default-router 10.0.18.33
 dns-server 8.8.8.8
```

Clients receive:

- an address from the correct subnet;
- the correct default gateway;
- DNS server information;
- configuration that matches their VLAN.

## A Very Useful Failure: 169.254.x.x

If a client receives an address like:

```text
169.254.x.x
```

that usually means DHCP failed.

The client tried to get an address through DHCP but did not receive a response. It then assigned itself an automatic self-assigned address.

This is an important troubleshooting clue.

Check:

- whether the client port is in the correct VLAN;
- whether the VLAN exists on the switch;
- whether the trunk between switch and router is configured;
- whether the VLAN is allowed on the trunk;
- whether the router subinterface exists;
- whether `encapsulation dot1Q` is configured;
- whether the DHCP pool is correct;
- whether the DHCP server is reachable from that VLAN.

In the lesson, the trunk to the router was the missing piece.

## The Switch Port To The Router Must Be A Trunk

For router-on-a-stick, the switch port connected to the router must be a trunk.

Why?

Because traffic for multiple VLANs must cross one physical link.

On the switch:

```text
interface GigabitEthernet0/1
 switchport mode trunk
```

If this port remains an access port, the router will not see tagged VLAN 10 and VLAN 20 traffic as expected.

The situation becomes unpleasant:

```text
VLANs exist
Router subinterfaces exist
DHCP pools exist
But traffic does not reach the right subinterface
```

The config looks almost correct, but the system does not work.

## Verifying Inter-VLAN Routing

After fixing the trunk, clients started receiving correct DHCP leases:

```text
VLAN 10 client -> address from VLAN 10 subnet
VLAN 20 client -> address from VLAN 20 subnet
```

Then ping can be tested between VLANs.

If routing is allowed and default gateways are configured correctly, the ping works.

Traceroute is useful for understanding the path:

```text
Client in VLAN 10
 -> Gateway subinterface for VLAN 10
 -> Router routes traffic
 -> Destination in VLAN 20
```

Traceroute shows that traffic goes to the router first. That is inter-VLAN routing in action.

## What To Remember

The four main points:

1. Every VLAN is a separate network. Communication between VLANs requires a router or Layer 3 device.
2. Router-on-a-stick lets one physical router interface route between multiple VLANs.
3. `encapsulation dot1Q` ties a router subinterface to a specific VLAN.
4. The switch port facing the router must be a trunk, or tagged VLAN traffic will not go where it should.

## Main Takeaway

This lesson pulls together several topics:

- VLANs;
- subnetting;
- trunks;
- 802.1Q;
- router subinterfaces;
- default gateways;
- DHCP pools;
- troubleshooting.

That is a good sign. Networking starts to look less like isolated facts and more like a system.

Traffic from one VLAN goes to its default gateway, the router receives it on the matching subinterface, makes a routing decision and sends it onward.

In short:

```text
VLAN separates
Trunk carries
Subinterface receives
Router routes
Policy controls
```

Next, native VLAN and trunk behavior matter, because there are a few details there that are easy to miss.

