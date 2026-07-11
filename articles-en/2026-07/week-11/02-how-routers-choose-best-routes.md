# How Routers Choose Best Routes

Source: closed course page  
Date added: 2026-07-11  
Related plan item: Week 11 / How routers choose best routes  
Tags: routing table, administrative distance, metric, static routes, OSPF, RIP, floating static
Language: English
Translation pair: articles/2026-07/week-11/02-how-routers-choose-best-routes.md

## Summary

- The routing table does not show everything a router knows; it shows the winning routes.
- A router chooses a route through three main checks: specificity, administrative distance, and metric.
- The default route is used only when no more specific route exists.
- Administrative distance shows how much the router trusts the source of the route.
- Metric is used as the tie-breaker inside one routing protocol.

## Key Points

- A more specific route always beats a less specific route.
- A directly connected route has AD 0, a static route has AD 1, OSPF has AD 110, and RIP has AD 120.
- A floating static route is a static route with a higher administrative distance for backup scenarios.
- If routes come from the same protocol, the router chooses by metric.
- RIP uses hop count, OSPF uses cost, and EIGRP uses a composite metric.

## Notes

A router does not simply "know the best path." It receives routing information from different sources, compares the options, and installs only the winners in the routing table. That means the routing table is not the router's entire brain; it is the current final answer.

The router may know backup paths, alternate paths, and routes from different protocols, but the active routing table contains only the routes that won the selection process. If the current winner disappears, another route can take its place.

Main idea:

> The routing table is not everything the router knows. It is the list of routes that won the argument.

## Step 1: Specificity

The first decision point is specificity. The longer the prefix, the more specific the route. More specific wins.

Example:

| Route | Meaning |
| --- | --- |
| `10.10.10.0/24` | Less specific route. |
| `10.10.10.128/25` | More specific route. |
| `0.0.0.0/0` | Default route, least specific. |

If a packet is going to `10.10.10.140`, the `/25` route beats the `/24` route because it describes the destination more precisely. The default route is used only if nothing more specific matches.

This explains why the default route does not take all traffic. It is not the "main" route. It is the final fallback option: "if nothing else matches, send it here."

## Step 2: Administrative Distance

If specificity is equal, the router checks administrative distance. This is the trust level of the route source. Lower AD wins.

Important values:

| Source | Administrative Distance |
| --- | --- |
| Directly connected | 0 |
| Static route | 1 |
| OSPF | 110 |
| RIP | 120 |

If a router learns the same prefix from OSPF and RIP, it chooses OSPF because 110 is better than 120. If a static route exists for that same prefix, the static route beats OSPF because 1 is better than 110.

That makes static routes powerful and dangerous. The router heavily trusts manual configuration. If a static route is wrong, it can silently override a good dynamic route and send traffic the wrong way.

## Floating Static Routes

A floating static route is a static route with an intentionally worse administrative distance. It is used as a backup path.

For example, the main route comes from OSPF with AD 110. We want a static backup through LTE/5G, but only if the OSPF route disappears. The static route receives an AD higher than 110:

```text
ip route 10.50.0.0 255.255.0.0 192.0.2.2 121
```

Now the static route does not compete with OSPF while the OSPF route is available. But if the OSPF route disappears, the floating static route can enter the routing table.

A practical NetworkChuck Coffee use case: the main WAN link carries traffic between sites, while cellular backup should activate only during failure. A floating static keeps the backup route in reserve without constantly using the expensive link.

## Step 3: Metric

If specificity and administrative distance are tied, the router checks metric. Metric works inside one protocol.

For example, two OSPF routes to the same prefix have the same specificity and the same AD 110. OSPF then chooses the route with the lower cost.

Different protocols calculate metric differently:

| Protocol | Metric |
| --- | --- |
| RIP | Hop count. |
| OSPF | Cost, usually based on bandwidth. |
| EIGRP | Composite metric, including bandwidth and other factors. |

RIP looks at the number of routers to the destination. It does not understand link quality as flexibly as more modern protocols. OSPF uses cost: faster links usually receive lower cost, and lower cost wins. EIGRP uses a composite metric where multiple factors become one value.

Main rule: inside a protocol, lower metric usually wins.

## Full Selection Order

A router chooses a route like this:

1. More specific prefix wins.
2. If equal, lower administrative distance wins.
3. If equal, lower metric wins.

Once this is clear, `show ip route` stops being mysterious. You can look at competing routes and explain why one route was installed.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Routing table | Active list of best routes installed by the router. |
| Specificity | How precisely a route describes the destination network; longer prefix wins. |
| Default route | Least specific route, `0.0.0.0/0`, used only when no better match exists. |
| Administrative distance | Trust value for route source; lower is better. |
| Metric | Protocol-specific path quality value; lower usually wins. |
| Floating static | Static route with increased AD used as backup. |
| `show ip route` | Command that displays installed routes. |

## Questions

### 1. Why does the routing table not show every possible route?

Answer: The routing table contains installed winners. The router may know alternate routes, but it shows only active best routes.

### 2. Why does a default route not beat a specific route?

Answer: The default route `0.0.0.0/0` is the least specific route. Any more precise route to the destination wins.

### 3. What does administrative distance mean?

Answer: It is the trust value of the route source. A lower value means the router trusts that source more.

### 4. Why use a floating static route?

Answer: To use a static route as a backup. It receives a higher AD so it does not beat the primary dynamic route while that route is available.

### 5. When is metric used?

Answer: When competing routes have the same specificity and administrative distance, usually because they came from the same protocol.

## What To Review Later

- Administrative distance values for common route sources.
- How OSPF calculates cost.
- Why static routes can override dynamic routes.
- How to read competing routes in `show ip route`.
