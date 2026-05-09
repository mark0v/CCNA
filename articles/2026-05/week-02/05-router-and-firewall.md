# Router & Firewall

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Router and firewall roles  
Tags: router, firewall, lan, wan, edge, all-in-one, security, routing, network design

## Summary

Routers and firewalls have different core jobs, but in real networks their functions often overlap. A router's main job is to move traffic between networks, especially between the LAN and the WAN/internet. A firewall's main job is to inspect traffic and enforce security rules.

Main idea: do not judge a device only by the label on the box. Ask what function it is performing in the network. In small networks, one all-in-one device may route, firewall, switch and provide wireless. As the business grows, separating those roles can improve performance, security and control.

## Key Points

- A router routes traffic between networks.
- A firewall secures traffic by allowing or blocking it based on rules.
- Real devices often blur router/firewall/switch/wireless functions.
- Small business all-in-one devices can combine routing, switching, wireless and security.
- Separating functions helps you understand what each part is doing.
- The switch and AP handle local LAN communication.
- The router handles traffic leaving or entering the local network.
- LAN means Local Area Network.
- WAN means Wide Area Network.
- The router sits at the edge, with one side toward the LAN and one side toward the WAN/internet.
- Routers often have fewer ports than switches because they are not primarily endpoint aggregation devices.
- Many modern routers include switch ports or wireless access point functions.
- A router's core function is moving traffic between networks.
- A firewall's core function is inspecting and controlling traffic for security.
- A router can have firewall features.
- A firewall can route traffic.
- Dedicated firewalls are usually better for serious security inspection under load.
- Small offices may be fine with an all-in-one router/firewall.
- Growing environments often benefit from dedicated switching, wireless, routing and firewall roles.

## Notes

### Router or Firewall?

The simple version:

```text
Router = moves traffic between networks.
Firewall = secures traffic with rules.
```

The real-world version is messier because devices often combine functions.

One physical box may include:

- router;
- firewall;
- switch;
- wireless access point;
- VPN features;
- filtering;
- NAT;
- management portal.

This is convenient, but it can make learning harder if every function is hidden inside one mystery box.

### Why Separate the Concepts

All-in-one devices are not bad.

But for learning, it helps to separate:

- switching;
- wireless;
- routing;
- firewalling.

This makes each function visible.

If everything is introduced as one device that "makes internet happen," the mental model stays fuzzy.

### LAN Side

LAN means Local Area Network.

At NetworkChuck Coffee, the LAN includes local devices inside the building:

- laptops;
- POS systems;
- printers;
- cameras;
- phones;
- tablets;
- servers;
- access points;
- switches.

The switch and wireless access point mostly handle local communication.

### WAN Side

WAN means Wide Area Network.

In this lesson, the WAN usually means the internet connection.

WAN traffic includes:

- browser traffic to websites;
- cloud payment requests;
- cloud apps;
- traffic to remote business locations;
- communication leaving the local network.

### What the Router Actually Does

The router handles traffic that leaves or enters the local network.

Simple model:

```text
LAN -> router -> WAN/internet
WAN/internet -> router -> LAN
```

The router helps decide:

```text
Does this traffic stay local,
or should it leave the local network?
```

This is why the router is often at the edge of the network.

### Router as Border Crossing

Mental model:

```text
Switch/AP = local conversations.
Router = border crossing.
```

The router has one foot in the local coffee shop network and one foot toward the outside world.

It connects different networks together.

### Why Routers Often Have Fewer Ports

Switches often have many ports:

- 24 ports;
- 48 ports;
- more in larger environments.

Why?

```text
Switches connect many local devices.
```

Routers often need fewer ports because their job is different:

```text
One side to LAN.
One side to WAN.
```

This is a general pattern, not a strict rule.

### Why It Gets Messy

Modern devices combine roles.

Examples:

- router with built-in switch ports;
- wireless router with built-in AP;
- firewall that also routes;
- router with security filtering;
- small office appliance that does everything.

So you cannot always identify the role of a device just by looking at the physical box.

Better question:

```text
What function is this device performing in this network?
```

### All-in-One Devices

For a small NetworkChuck Coffee location, an all-in-one device may be practical.

Benefits:

- lower cost;
- less space;
- fewer devices;
- simpler deployment;
- easier basic management;
- faster setup.

Possible combined roles:

- router;
- firewall;
- switch;
- wireless AP.

This can be enough for a tiny or simple environment.

### When All-in-One Starts to Strain

As the business grows, all-in-one designs may become limiting.

Growth adds:

- more users;
- guest WiFi;
- payment systems;
- cameras;
- VPNs;
- multiple locations;
- stricter security;
- higher performance requirements;
- more troubleshooting needs.

At that point, separating roles can make more sense.

### What the Firewall Does

A firewall focuses on security.

It decides what traffic should be:

- allowed;
- blocked;
- inspected;
- filtered;
- logged.

Core firewall function:

```text
Inspect traffic and enforce security rules.
```

### Router vs Firewall Core Functions

Comparison:

| Device role | Core function |
| --- | --- |
| Router | Move traffic between networks |
| Firewall | Inspect/control traffic for security |

Overlap exists:

| Overlap | Example |
| --- | --- |
| Router with firewall features | Home/small office router blocking inbound traffic |
| Firewall with routing features | Dedicated firewall routing between LAN, WAN and VLANs |

The difference is the primary purpose and specialization.

### Dedicated Firewall

A dedicated firewall is built to do security inspection well.

It may provide:

- better policy control;
- stronger traffic inspection;
- VPN features;
- logging;
- filtering;
- segmentation;
- higher security performance;
- better visibility.

When security and load matter, dedicated gear can be worth it.

### Small Business Design

For the early NetworkChuck Coffee network, a single device may be fine.

One box might handle:

```text
routing + firewalling + switching + wireless
```

That can be practical if:

- the shop is small;
- budget is limited;
- traffic is light;
- security needs are basic;
- management should stay simple.

Do not overbuild a tiny environment just because enterprise designs exist.

### Growing Network Design

As the network grows, ask better questions:

- Should guest WiFi be separated from payment systems?
- Do we need stronger inspection between stores and the internet?
- Is one box overloaded?
- Do we need better wireless coverage?
- Do we need managed switches?
- Do we need VPNs between sites?
- Do we need better logs and visibility?

This is how real networks evolve.

They grow in layers, not in one giant leap.

### Functional Thinking

Do not focus only on hardware labels.

Focus on roles:

| Role | Function |
| --- | --- |
| Switch | Connect local wired devices |
| AP | Extend local network wirelessly |
| Router | Connect networks / reach outside world |
| Firewall | Protect and control traffic at boundaries |

The same physical box can perform more than one role.

### Main Takeaway

Fast version:

- router moves traffic between networks;
- firewall decides what traffic is allowed or blocked;
- one device can do both jobs in small networks;
- larger environments often separate roles for control, performance and security.

Most important question:

```text
What function is this device performing in the network?
```

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Router | Device/function that moves traffic between networks. |
| Firewall | Device/function that inspects and controls traffic for security. |
| LAN | Local Area Network; devices inside the local site. |
| WAN | Wide Area Network; outside/remote network, often the internet. |
| Edge | Boundary between local network and outside network. |
| All-in-one device | Device that combines routing, firewalling, switching and/or wireless. |
| Firewall rule | Security rule that allows or blocks traffic. |
| Filtering | Process of allowing/denying traffic based on policy. |
| VPN | Virtual Private Network; secure connection across untrusted networks. |
| Guest WiFi | Wireless network for guests, often separated from business systems. |
| Segmentation | Separating networks or traffic types for control/security. |
| Security inspection | Firewall process of examining traffic before allowing it. |

## Questions

### 1. What is a router's core job?

To move traffic between networks.

### 2. What is a firewall's core job?

To inspect traffic and enforce security rules.

### 3. Why can router vs firewall feel confusing in real life?

Because many devices combine routing, firewalling, switching and wireless functions in one box.

### 4. What does LAN stand for?

Local Area Network.

### 5. What does WAN stand for?

Wide Area Network.

### 6. In this lesson, what does WAN usually mean?

The internet connection or outside network.

### 7. What local devices might live on the LAN at NetworkChuck Coffee?

Laptops, POS systems, printers, cameras, phones, tablets, servers, switches and APs.

### 8. What does the router decide at a basic level?

Whether traffic stays local or should be sent out to another network.

### 9. Why do routers often have fewer ports than switches?

Because routers connect networks, while switches connect many local devices.

### 10. Is port count a perfect way to identify device role?

No. Modern devices often combine roles, so port count is only a general clue.

### 11. Can a router have firewall features?

Yes.

### 12. Can a firewall route traffic?

Yes.

### 13. Why might a dedicated firewall be useful?

It is built for stronger security inspection, policy control, logging and performance under load.

### 14. When might an all-in-one router/firewall be enough?

In a small office or single coffee shop with basic requirements.

### 15. Why might a growing business separate router and firewall roles?

For better security, performance, control, visibility and scalability.

### 16. What is the better question than "What is written on the box?"

What function is this device performing in the network?

### 17. What protects the boundary of the network?

The firewall function, often located at or near the edge.

## What To Review Later

- Router core function: move traffic between networks.
- Firewall core function: inspect/control traffic.
- LAN side vs WAN side.
- Router as network border crossing.
- All-in-one devices and why they are common.
- Why physical boxes can blur roles.
- Dedicated firewall benefits.
- Small business vs growing network design.
- Think in functions, not labels.
