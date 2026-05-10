# What is a Router?

Source: private course page  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 00 Lesson 02  
Tags: router, routing, wan, gateway, internet, networks

## Summary

A router connects different networks and decides where traffic should go next. Inside a coffee shop, switches handle local communication. When traffic needs to leave the local network and reach another network or the internet, the router becomes the key device.

Main idea: a router is the device that helps networks talk to other networks.

## Key Points

- A router connects different networks.
- A switch connects devices inside one network.
- The router often acts as the default gateway for local devices.
- WAN traffic usually leaves the LAN through a router.
- The internet is made of many interconnected networks and routers.
- Routers make forwarding decisions based on destination networks.
- Home routers often combine routing, switching, wireless and firewall features.

## Notes

### Router vs Switch

Simple model:

```text
Switch = local communication
Router = communication between networks
```

If two devices are in the same LAN, the switch can help them talk. If traffic needs to reach another network, it goes to the router.

### Default Gateway

For many endpoints, the router is configured as the default gateway. That means:

```text
If I do not know where this destination is, send it to the router.
```

### Internet Edge

In a small business, the router often sits at the edge between the internal network and the ISP connection.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Router | Connects different networks. |
| WAN | Wide Area Network. |
| Default gateway | The next-hop device used to reach other networks. |
| Routing | Choosing a path for traffic. |

## Questions

### What does a router do?

It forwards traffic between different networks.

### Why do endpoints need a default gateway?

So they know where to send traffic that is not local.

## What To Review Later

- Routing tables.
- Default routes.
- NAT.
- LAN vs WAN.
