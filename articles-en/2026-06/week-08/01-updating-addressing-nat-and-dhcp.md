# Updating Addressing, NAT, And DHCP

Source: closed course page  
Date added: 2026-06-20  
Related plan item: Week 8 / Applying the new subnet plan  
Tags: IPv4, subnetting, NAT, wildcard mask, DHCP, router configuration, Packet Tracer
Language: English
Translation pair: articles/2026-06/week-08/01-updating-addressing-nat-and-dhcp.md

## Summary

When a subnet plan is ready on paper, it still has to be applied to a real configuration. In this lesson, the new `10.0.18.0/26` subnet for a district shop is mapped onto the router interface, NAT and DHCP.

The main idea is simple: IP addressing does not live by itself. When a subnet changes, you also need to check:

- gateway address;
- subnet mask;
- old interfaces and loopbacks;
- NAT access list;
- wildcard mask;
- DHCP excluded addresses;
- DHCP pool;
- DNS server;
- default router for clients;
- actual DHCP bindings.

Otherwise, the network may look mostly correct but still fail because stale configuration is left behind.

## New Gateway For The LAN

The LAN-facing router interface was assigned:

```text
10.0.18.1 255.255.255.192
```

`255.255.255.192` is the dotted decimal form of `/26`.

You need to be comfortable translating both ways:

```text
/26 = 255.255.255.192
255.255.255.192 = /26
```

Different commands and platforms may ask for different formats. Slash notation and dotted decimal masks represent the same concept, just written differently.

For subnet `10.0.18.0/26`, the range is:

```text
Network address:    10.0.18.0
Usable range:       10.0.18.1 - 10.0.18.62
Broadcast address:  10.0.18.63
Subnet mask:        255.255.255.192
```

Assigning the first usable address to the router interface makes sense because it becomes the default gateway for devices in that LAN.

## Remove Stale Configuration

When the addressing plan changes, adding the new IP address is not enough. You also need to remove configuration that no longer matches the design.

In the lesson, this included:

- old loopback interfaces;
- an old WAN link;
- stale configuration from the previous design.

This is an important habit. Problems often appear not because the new configuration is wrong, but because old configuration is still present. The router may still have extra routes, NAT rules, interfaces or ACL entries, which makes troubleshooting unclear.

A good approach is:

1. Understand what should remain in the new design.
2. Remove what is no longer used.
3. Configure the new parameters.
4. Verify that the running config no longer contains the old design.

## NAT Must Be Updated Too

NAT means Network Address Translation. It allows internal private IP addresses to reach external networks such as the internet.

If the subnet changes, the NAT rule must change too. The old NAT access list may still reference the previous subnet. In that case, new clients may not be translated, or NAT may match the wrong address range.

New subnet:

```text
10.0.18.0/26
```

Subnet mask:

```text
255.255.255.192
```

Wildcard mask for the ACL:

```text
0.0.0.63
```

A wildcard mask is the inverse form of the subnet mask.

```text
255.255.255.192
0.0.0.63
```

You can verify the last octet like this:

```text
255 - 192 = 63
```

So for `10.0.18.0/26`, the NAT ACL should match the range `10.0.18.0 - 10.0.18.63` with wildcard `0.0.0.63`.

It feels strange at first. Later it becomes normal: the subnet mask tells you what is fixed, and the wildcard mask tells you what is allowed to vary.

## DHCP: Let The Router Hand Out Addresses

DHCP means Dynamic Host Configuration Protocol. It automatically gives clients IP configuration:

- IP address;
- subnet mask;
- default gateway;
- DNS server;
- sometimes additional options.

Without DHCP, every PC would need to be configured manually. That is slow, uncomfortable and very likely to create mistakes as the number of devices grows.

In this lesson, the router was configured as the DHCP server for the district shop subnet.

## Excluded Addresses

First, exclude addresses that DHCP must not hand out to clients.

Common exclusions include:

- gateway address;
- addresses for network devices;
- static infrastructure addresses;
- addresses reserved for future servers, printers or other fixed devices.

For example, if the router interface uses `10.0.18.1`, DHCP must not give that address to a PC. Otherwise, you get an IP conflict.

## DHCP Pool

After exclusions, you create the DHCP pool. It defines:

- network;
- subnet mask;
- default router;
- DNS server.

For this design, the important values are:

```text
Network:         10.0.18.0
Mask:            255.255.255.192
Default router:  10.0.18.1
```

The default router is the gateway clients use to leave their local network.

## Client Verification

After DHCP was configured, the PCs were switched from static addressing to DHCP.

They received:

```text
10.0.18.11
10.0.18.12
```

That is a good sign: the clients received addresses from the correct subnet, and the router showed DHCP bindings mapped to client MAC addresses.

A DHCP binding shows this relationship:

```text
Client MAC address -> Assigned IP address
```

This is why lab practice is useful: you can see the path from design, to configuration, to proof.

## What This Lesson Proved

This was not just a lesson about changing IP addresses in Packet Tracer. It showed that a subnetting plan must be operational.

That means you need to be able to:

- read `/26` and understand the range;
- translate `/26` to `255.255.255.192`;
- choose the gateway address;
- remove stale configuration;
- update NAT for the new subnet;
- calculate the wildcard mask;
- configure the DHCP pool;
- verify that clients actually received correct addresses.

A subnet plan is useful only when you can apply it to routers, switches, wireless gear and end devices.

## Practical Takeaway

When a subnet changes, do not think only about the interface IP.

Check the whole dependency chain:

```text
Interface IP
Subnet mask
Routing
NAT ACL
DHCP pool
Excluded addresses
Client configuration
Verification commands
```

A network is stable not because one command is correct. It is stable when all related parts of the design agree with each other.

