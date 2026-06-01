# Private IP Addresses and NAT

Source: closed course page  
Date added: 2026-06-01  
Related plan item: Week 5 / Private IPv4 ranges and NAT  
Tags: private ip, public ip, rfc 1918, nat, pat, ipv4, subnetting, default gateway
Language: English
Translation pair: articles/2026-05/week-05/02-private-ip-addresses-and-nat.md

## Summary

Private IP addresses are IPv4 addresses designed for use inside private networks and not routed across the public internet. Because of that, the same private ranges can be reused in millions of homes, offices, and businesses at the same time.

Main idea: private IPs work inside the network, and NAT allows private devices to reach the internet through a public IP address.

## Key Points

- IPv4 address space is limited to about 4.3 billion addresses.
- Private IPv4 ranges help conserve public addresses.
- Private addresses should not be routed on the public internet.
- Private ranges are defined in RFC 1918.
- There are three private IPv4 ranges: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`.
- The same private address can exist in different isolated networks.
- NAT translates private addresses to an external public address.
- PAT/NAT overload allows many internal devices to share one public IP through ports.
- In troubleshooting, first identify whether an address is private or public.
- If two connected networks use the same private addressing, routing conflicts can happen.

## Notes

### Why Private IP Addresses Exist

IPv4 provides about:

```text
4,294,967,296 addresses
```

At first, that sounds like a lot.

But in the real world, addresses disappear quickly:

- phones;
- laptops;
- servers;
- cameras;
- printers;
- TVs;
- IoT devices;
- cars;
- cloud systems;
- business networks.

If every device needed a unique public IPv4 address, IPv4 would have been exhausted much faster.

The solution:

```text
Reserve special ranges for private networks.
```

These addresses can be used inside local networks, but internet routers should not route them as public destinations.

### The Three Private IPv4 Ranges

Private IPv4 ranges:

| Range | Prefix | Common Use |
| --- | --- | --- |
| `10.0.0.0` - `10.255.255.255` | `10.0.0.0/8` | Large organizations, multi-site networks, labs. |
| `172.16.0.0` - `172.31.255.255` | `172.16.0.0/12` | Medium/large networks, enterprise segments. |
| `192.168.0.0` - `192.168.255.255` | `192.168.0.0/16` | Home networks, small offices, simple LANs. |

You should recognize them instantly.

Memory hook:

```text
10 anything = private
172.16 through 172.31 = private
192.168 anything = private
```

The most common mistake is thinking all of `172.x.x.x` is private.

That is wrong.

Only this range is private:

```text
172.16.0.0 - 172.31.255.255
```

Examples:

```text
172.20.5.10 = private
172.40.5.10 = not private RFC 1918
```

### RFC 1918

Private address ranges are defined in RFC 1918.

The idea of RFC 1918:

```text
Use these ranges inside private networks.
The public internet will not route them globally.
```

So:

- my home can use `192.168.1.10`;
- your home can also use `192.168.1.10`;
- an office can use `10.0.1.50`;
- a lab can use `10.0.1.50`.

As long as those networks are isolated, there is no conflict.

### Private IPs Are Reusable

Private IP addresses are reusable because they are not globally unique.

They only need to be unique inside a specific private network.

Example:

```text
Home A laptop: 192.168.1.20
Home B laptop: 192.168.1.20
```

Both can exist at the same time because they sit behind different routers and NAT boundaries.

For the public internet, those internal private addresses are not visible as destination addresses.

### Private IPs Do Not Work On The Public Internet

If a packet with a private destination address reaches the public internet, routers should drop/ignore it because RFC 1918 ranges are not meant for public routing.

That means:

```text
192.168.1.20
```

is not a reachable global internet destination.

If you are troubleshooting and see a private IP, do not try to "trace it across the internet".

Your next logical stop is usually:

- local router;
- firewall;
- NAT device;
- VPN boundary;
- internal routing.

### Why Classes Still Help

Classful networking is old school, but historical classes help explain the size of private ranges.

| Private range | Classful feeling | Default historical size |
| --- | --- | --- |
| `10.0.0.0/8` | Class A | Huge |
| `172.16.0.0/12` | Part of Class B space | Medium/large |
| `192.168.0.0/16` | Class C world | Small/home-friendly |

In modern networks, we use CIDR and subnetting, not pure classes.

But the pattern is useful:

- `192.168.x.x` is common at home and in small offices;
- `10.x.x.x` is common in enterprises and labs;
- `172.16-31.x.x` is often forgotten, but it is also private.

### What NAT Does

NAT stands for:

```text
Network Address Translation
```

NAT translates addresses between the internal private network and the external public network.

Home example:

```text
Laptop: 192.168.1.20
Phone:  192.168.1.30
TV:     192.168.1.40
Router public IP: 203.0.113.50
```

Private devices cannot go to the internet directly with their private addresses.

The router performs translation:

```text
192.168.1.20 -> 203.0.113.50
192.168.1.30 -> 203.0.113.50
192.168.1.40 -> 203.0.113.50
```

From the outside, traffic appears to come from the router public IP.

### How One Public IP Can Serve Many Devices

Question:

```text
How can one public IP represent many devices at the same time?
```

Answer: ports.

More specifically, this is usually PAT:

```text
Port Address Translation
```

It is also often called:

```text
NAT overload
```

The router tracks conversations using source ports.

Example:

```text
192.168.1.20:50001 -> 203.0.113.50:50001
192.168.1.30:50002 -> 203.0.113.50:50002
192.168.1.40:50003 -> 203.0.113.50:50003
```

When replies return, the router looks at the port and knows which internal device should receive the traffic.

This allows many devices to share one public IPv4 address.

### NAT Is Useful, But Not Magic

NAT helped IPv4 survive longer, but it is not a perfect solution.

Pros:

- conserves public IPv4 addresses;
- allows reuse of private ranges;
- hides internal addressing from the internet;
- convenient for homes and businesses.

Cons:

- complicates troubleshooting;
- breaks end-to-end transparency;
- requires state tracking;
- can complicate inbound connections;
- sometimes interferes with protocols/apps that need direct connections.

NAT does not replace a firewall, although it often runs on the same edge device.

### Private Addressing At NetworkChuck Coffee

For NetworkChuck Coffee, it makes no sense to assign a public IP to every device:

- registers;
- tablets;
- cameras;
- printers;
- smart devices;
- employee laptops;
- guest Wi-Fi clients.

It is much more practical to use private addressing internally.

Small shop example:

```text
192.168.10.0/24
```

Another shop:

```text
192.168.20.0/24
```

Larger multi-location design:

```text
10.0.0.0/8
```

Example:

```text
10.0.1.0/24  = Coffee House 1
10.0.2.0/24  = Coffee House 2
10.0.3.0/24  = Coffee House 3
```

The edge router/firewall performs NAT to the outside.

### Duplicate Private IPs Can Become A Problem

Duplicate private IPs are safe while networks are isolated.

But if two networks with the same ranges are connected, problems can start.

Example:

```text
Site A: 192.168.1.0/24
Site B: 192.168.1.0/24
```

If a VPN connects them, the router may not know where to send traffic for `192.168.1.50`, because that network exists on both sides.

This is called overlapping address space.

Solutions:

- plan addressing in advance;
- use different subnets per site;
- redesign addressing;
- use NAT between overlapping networks if redesign is impossible.

### Troubleshooting Tip

Before troubleshooting, always ask:

```text
Is this IP address private or public?
```

If private:

- do not look for it in the public internet;
- check local subnet;
- check default gateway;
- check NAT/firewall;
- check internal routing;
- check VPN boundaries.

If public:

- check internet routing;
- DNS;
- firewall rules;
- provider/ISP;
- public service availability.

This saves a lot of time.

## Examples

### Example 1 - Home NAT

```text
Laptop private IP: 192.168.1.20
Router public IP:  203.0.113.50
```

Laptop opens a website.

Router translates:

```text
192.168.1.20 -> 203.0.113.50
```

The website sees source:

```text
203.0.113.50
```

not:

```text
192.168.1.20
```

### Example 2 - Private Range Recognition

```text
10.44.12.8       = private
172.16.5.100     = private
172.31.255.10    = private
172.32.1.1       = not RFC 1918 private
192.168.88.25    = private
8.8.8.8          = public
```

### Example 3 - Coffee Shops

```text
Coffee House 1: 10.0.1.0/24
Coffee House 2: 10.0.2.0/24
Coffee House 3: 10.0.3.0/24
```

Each shop has its own subnet.

All shops can use private IPs internally.

Each shop can use NAT at the edge to reach the internet.

## Quick Self-Check

### Question 1

What are the three private IPv4 ranges?

Answer:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

### Question 2

Is `172.32.10.5` private?

Answer:

```text
No. The private 172 range is only 172.16.0.0 through 172.31.255.255.
```

### Question 3

Can private IP addresses be routed across the public internet?

Answer:

```text
No. RFC 1918 private addresses are not meant for public internet routing.
```

### Question 4

What does NAT do?

Answer:

```text
It translates private internal addresses to public external addresses.
```

### Question 5

How can many private devices share one public IP?

Answer:

```text
Through PAT/NAT overload, which tracks conversations using port numbers.
```

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Private IP address | IPv4 address used inside private networks and not routed publicly. |
| Public IP address | Globally routable IP address on the internet. |
| RFC 1918 | Standard that defines private IPv4 address ranges. |
| NAT | Network Address Translation. |
| PAT | Port Address Translation, many private hosts sharing one public IP using ports. |
| NAT overload | Cisco/common term for PAT. |
| Overlapping address space | Two connected networks using the same IP range. |
| Edge router | Router/firewall at the boundary between internal network and outside network. |
| ISP | Internet Service Provider. |

## What To Review Later

- Subnet masks
- CIDR notation
- Default gateway
- NAT/PAT configuration
- Public vs private routing
- VPN overlapping subnets
- IPv6 addressing
- Firewall basics

