# Reading the Routing Table

Source: closed course page  
Date added: 2026-06-09  
Related plan item: Week 6 / Reading and interpreting routing tables  
Tags: routing table, administrative distance, metric, longest prefix match, next hop, EIGRP, static route
Language: English
Translation pair: articles/2026-06/week-06/04-reading-the-routing-table.md

## Summary

The routing table is the primary source of information about where a router will send a packet. Each route entry can identify the destination network, route source, administrative distance, metric, next hop, age and exit interface.

Main idea: a router first selects the most specific prefix. If the same prefix is learned from different sources, it compares administrative distance. If multiple routes remain from the same protocol, it compares their metrics.

## Key Points

- `show ip route` displays installed routes.
- The route code identifies how the router learned a route.
- `C` means connected, `L` local, `S` static and `D` EIGRP.
- The destination prefix identifies the target network and its size.
- In `[AD/metric]`, the first value is administrative distance and the second is metric.
- Lower administrative distance is preferred.
- A metric compares paths learned through one routing protocol.
- Longest prefix match happens before AD and metric comparison.
- The next hop identifies the next router.
- The exit interface identifies where the packet leaves.
- The routing table installs the winner, while a protocol database can retain alternatives.

## Notes

### The Router's Decision Map

The routing table is the router's forwarding decision map.

For each packet, the router:

1. Reads the destination IP address.
2. Finds matching prefixes.
3. Selects the longest matching prefix.
4. Uses the best installed route.
5. Determines the next hop and exit interface.
6. Forwards or drops the packet if no route exists.

Primary command:

```cisco
show ip route
```

### Where Routes Come From

| Code | Source |
| --- | --- |
| `C` | Directly connected network |
| `L` | Exact local interface address |
| `S` | Manually configured static route |
| `D` | Route learned through EIGRP |
| `O` | Route learned through OSPF |
| `R` | Route learned through RIP |
| `B` | Route learned through BGP |

The code at the beginning explains why the route exists.

### Connected And Local Routes

When an interface is configured and `up/up`, the router commonly adds:

```text
C 192.168.1.0/24 is directly connected, GigabitEthernet0/0
L 192.168.1.1/32 is directly connected, GigabitEthernet0/0
```

`C` represents the entire connected subnet.

`L` represents the router's exact interface address as a `/32` host route.

### Reading A Dynamic Route Entry

Example EIGRP route:

```text
D 192.168.3.0/24 [90/3072] via 192.168.2.2, 00:04:18, GigabitEthernet0/1
```

| Part | Meaning |
| --- | --- |
| `D` | Learned through EIGRP |
| `192.168.3.0/24` | Destination prefix |
| `90` | Administrative distance |
| `3072` | EIGRP metric |
| `192.168.2.2` | Next-hop router |
| `00:04:18` | Route age |
| `GigabitEthernet0/1` | Exit interface |

Read it as:

```text
The 192.168.3.0/24 network was learned through EIGRP.
Use next hop 192.168.2.2 and exit GigabitEthernet0/1.
```

### Variably Subnetted

The output can include:

```text
192.168.1.0/24 is variably subnetted, 2 subnets, 2 masks
```

This is informational. It means the router lists prefixes of different lengths within a common address block.

Common examples are:

- a connected `/24`;
- a local `/32` host route.

It is not an error.

### Administrative Distance

Administrative distance represents trust in a route source.

Lower is preferred.

| Route source | Default AD |
| --- | ---: |
| Connected | 0 |
| Static | 1 |
| EIGRP summary | 5 |
| External BGP | 20 |
| Internal EIGRP | 90 |
| OSPF | 110 |
| RIP | 120 |
| External EIGRP | 170 |
| Internal BGP | 200 |

If an identical prefix is learned through a static route and EIGRP:

```text
Static AD: 1
EIGRP AD: 90
```

The static route is normally installed.

EIGRP may still be functioning; its route simply lost to a more preferred source.

### Metric

A metric evaluates paths within one routing protocol.

If EIGRP knows two paths to the same prefix, it compares EIGRP metrics.

The lower metric is normally preferred.

Remember:

```text
AD compares route sources.
Metric compares paths within a route source/protocol.
```

Do not directly compare an EIGRP metric with an OSPF metric. The protocols calculate metrics differently; administrative distance is used between the protocols first.

### Longest Prefix Match Comes First

The core forwarding rule is:

```text
The most specific matching prefix wins.
```

Example:

```text
192.168.3.0/24 via 192.168.2.2
192.168.0.0/16 via 10.0.0.2
0.0.0.0/0 via 216.0.5.1
```

For destination `192.168.3.10`, all three routes match.

The `/24` wins because it contains the most matching network bits.

Even a highly preferred default route does not replace a more specific prefix.

### Route Selection Order

Simplified order:

1. Find the most specific destination prefix.
2. For an identical prefix, compare administrative distance across route sources.
3. For routes from one protocol, compare metric.
4. Install the winner in the routing table.
5. If supported, install multiple equal-cost paths.

AD does not compare a `/24` with a `/0`; longest prefix match happens first.

### Static Route Replacing EIGRP

Suppose EIGRP has learned:

```text
D 192.168.3.0/24 [90/3072] via 192.168.2.2
```

An administrator adds:

```cisco
ip route 192.168.3.0 255.255.255.0 192.168.2.2
```

The identical `/24` now has two sources:

- static AD `1`;
- EIGRP AD `90`.

The static route is installed:

```text
S 192.168.3.0/24 [1/0] via 192.168.2.2
```

After the static route is removed, EIGRP can become the winner again:

```cisco
no ip route 192.168.3.0 255.255.255.0 192.168.2.2
```

### Next Hop And Exit Interface

The next hop is the neighboring router receiving the packet.

The exit interface is the local interface through which the packet leaves.

A route can be read backward:

```text
Exit through this interface,
send to this next hop,
to reach this destination network.
```

The router must resolve the next hop through a connected or otherwise usable route. This is recursive lookup.

### Route Age

A dynamic route often includes a timer:

```text
00:04:18
```

It indicates time since the latest route update.

This can help identify:

- a newly learned route;
- a flapping adjacency;
- a stable update;
- a route repeatedly being reinstalled.

### Troubleshooting Questions

Do not ask only:

```text
Is the route present?
```

Also ask:

```text
Which prefix is installed?
How was it learned?
Why did this source win?
What is its AD?
What is its metric?
What is the next hop?
What is the exit interface?
Is the next hop reachable?
Is there a more specific route?
Does a return path exist?
```

### Useful Verification Commands

```cisco
show ip route
show ip route 192.168.3.0
show ip route static
show ip route eigrp
show ip protocols
show ip eigrp topology
show ip interface brief
traceroute 192.168.3.10
```

A protocol-specific database can retain routes that are not installed as the current winner.

## Worked Examples

### Example 1: Specific Route Versus Default

```text
S 192.168.3.0/24 via 192.168.2.2
S* 0.0.0.0/0 via 216.0.5.1
```

Destination `192.168.3.20` uses `/24`.

Destination `8.8.8.8` uses `/0`.

### Example 2: Static Versus EIGRP

Both routes describe `192.168.3.0/24`.

```text
Static AD 1
EIGRP AD 90
```

The static route is installed.

### Example 3: Two EIGRP Paths

If EIGRP learns an identical prefix through two neighbors, it compares its composite metric.

The lower-metric path becomes the successor. Equal-cost routes can be installed together depending on configuration.

## Practical Checklist

- Find the route code.
- Read the destination prefix.
- Identify the prefix length.
- Separate `[AD/metric]`.
- Find the next hop.
- Find the exit interface.
- Check the route age.
- Check for more specific prefixes.
- Explain why the route won.
- Verify the return path.

## Quick Self-Check

### Question 1

What does `[90/3072]` mean in an EIGRP route?

Answer:

```text
90 is administrative distance; 3072 is the EIGRP metric.
```

### Question 2

What does administrative distance compare?

Answer:

```text
The preference of different route sources for the same prefix.
```

### Question 3

What does a metric compare?

Answer:

```text
Path quality within one routing protocol.
```

### Question 4

Which is considered first: lower AD or longest prefix?

Answer:

```text
Longest prefix match is considered first.
```

### Question 5

Why can a static route hide an EIGRP route?

Answer:

```text
For the same prefix, a static route has a lower default administrative distance.
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Routing table | Table of best routes used for forwarding. |
| Route code | Source from which a route was learned. |
| Administrative distance | Preference of a route source; lower is better. |
| Metric | Path evaluation inside a routing protocol. |
| Longest prefix match | Selection of the most specific matching prefix. |
| Next hop | Next router in the path. |
| Exit interface | Local interface used to send the packet. |
| Route age | Time since the last protocol update. |
| `show ip route` | Displays the routing table. |
| Recursive lookup | Resolution of how to reach a next-hop address. |

## What To Review Later

- Administrative distance values
- EIGRP metrics
- OSPF cost
- Equal-cost multipath
- Floating static routes
- Recursive route lookup
- Route redistribution
