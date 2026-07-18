# ACLs Are A Tool, Not A Thing

Source: closed course page  
Date added: 2026-07-18  
Related plan item: Week 12 / ACLs are a tool, not a thing  
Tags: ACL, access control list, standard ACL, extended ACL, implicit deny, NAT, QoS, route filtering, VTY
Language: English
Translation pair: articles/2026-07/week-12/10-acls-are-a-tool-not-a-thing.md

## Summary

- An ACL by itself does nothing until it is applied to an interface or used by another feature.
- Standard ACLs match only source IP address.
- Extended ACLs can match source, destination, protocol, and port.
- ACLs process top-down and stop at the first match.
- Every ACL has an implicit deny at the end.
- `permit` and `deny` mean different things depending on where the ACL is used.

## Key Points

- An ACL is a list of matching rules.
- The feature using the ACL defines the actual result.
- For traffic filtering, `permit` means allow through.
- For NAT, `permit` means allow translation.
- For QoS, `permit` may mean allow traffic into a priority class.
- ACLs can also support route filtering and management-plane security.

## Notes

The most important ACL idea: an access list is a tool, not a complete feature by itself.

You can write a perfect ACL with clear permit and deny statements, but the router will not act on it until that ACL is connected to something.

Better mental model:

```text
ACL = rules that match traffic
Applied feature = action taken on matched traffic
```

The same ACL logic can produce very different results depending on whether it is used for filtering, NAT, QoS, route control, or device access.

## What An ACL Contains

At the simplest level, an ACL contains permit and deny statements.

Those statements are evaluated in order.

Two major ACL categories:

| ACL type | What it matches | Practical feel |
| --- | --- | --- |
| Standard ACL | Source IP address only | Simple, blunt, useful for broad matching. |
| Extended ACL | Source, destination, protocol, port | More precise, common for traffic filtering. |

Standard ACL example concept:

```text
Match traffic from this source network.
```

Extended ACL example concept:

```text
Match this source going to this destination using this protocol and port.
```

Extended ACLs are usually more useful when you need detailed control over traffic filtering.

## Top-Down Processing

ACLs are processed from top to bottom.

The router checks line 1, then line 2, then line 3, and so on. When traffic matches a line, processing stops.

This means order is critical.

Example logic:

```text
permit host 10.0.10.50
deny 10.0.10.0 0.0.0.255
```

This allows one specific host first, then denies the rest of the subnet.

If you reverse the order:

```text
deny 10.0.10.0 0.0.0.255
permit host 10.0.10.50
```

the specific host is denied with the rest of the subnet because the first match wins. The router never reaches the later permit line.

## Implicit Deny

Every ACL has an invisible deny at the bottom.

Conceptually:

```text
deny any
```

You do not type it, but it is always there.

If traffic does not match any permit statement, it is denied by default.

Troubleshooting habit:

1. Check line order.
2. Check whether the traffic matches anything.
3. Remember the implicit deny.

Many ACL problems are caused by a correct-looking permit statement that never gets reached, or by traffic falling through to implicit deny.

## Five Common ACL Purposes

ACLs appear across many router and firewall features.

Common purposes:

| Purpose | What the ACL does |
| --- | --- |
| Traffic filtering | Identifies traffic to allow or drop on an interface. |
| NAT | Identifies traffic eligible for address translation. |
| Route filtering | Identifies routes to advertise, block, or accept. |
| QoS | Identifies traffic that should receive special handling. |
| Security functions | Limits management access or supports security services. |

The ACL syntax may look similar, but the meaning changes with the feature using it.

## Traffic Filtering

Traffic filtering is the use case most people think of first.

An ACL is applied to an interface inbound or outbound. The router uses the ACL to decide whether traffic is allowed through or dropped.

This is where ACLs feel firewall-like.

Example NetworkChuck Coffee use:

- allow POS systems to reach payment services;
- block guest Wi-Fi from internal back office systems;
- allow management subnet to reach infrastructure devices;
- block unnecessary traffic between sensitive VLANs.

For this type of work, extended ACLs are often preferred because they can match source, destination, protocol, and ports.

## NAT

When ACLs are used with NAT, `permit` and `deny` do not mean "allow or block traffic through the router."

They mean whether traffic is selected for translation.

Example meaning:

```text
permit = this traffic should be translated
deny = this traffic should not be translated by this NAT rule
```

If traffic is not matched by the NAT ACL, it may fail to reach the public internet because it was not translated, not because a security filter explicitly blocked it.

That distinction matters during troubleshooting.

## Route Filtering

Route filtering uses ACL-like logic to control routing information.

The goal is not usually to block user packets directly. The goal is to decide which routes are allowed into or out of a routing process.

NetworkChuck Coffee examples:

- advertise only specific site networks to a partner;
- prevent internal-only networks from being shared;
- control which branch routes appear in another location;
- keep routing tables cleaner and safer.

This is ACL thinking applied to control-plane information.

## QoS

QoS, Quality of Service, prioritizes traffic.

An ACL can classify traffic so the network knows what deserves special handling.

Example:

- voice traffic gets priority;
- video traffic receives better treatment;
- bulk backup traffic does not get priority;
- business-critical application traffic is identified.

In QoS, `permit` might effectively mean "this traffic belongs in the class that gets special treatment." Other traffic is not necessarily blocked; it just does not get that priority.

## Device Security

ACLs are also used to protect the network devices themselves.

Example: restrict who can remotely manage a router through VTY lines.

VTY lines are virtual terminal lines used for remote access such as SSH or Telnet.

Concept:

```text
Only the management subnet can SSH into this router.
```

This is not about forwarding traffic through the router. It is about controlling access to the router's management plane.

That is a major real-world use case.

## NetworkChuck Coffee Design View

For NetworkChuck Coffee, the same ACL skill appears in multiple places:

| Business need | ACL role |
| --- | --- |
| Guest Wi-Fi isolation | Filter guest traffic away from internal resources. |
| POS internet access | Select POS subnet for NAT. |
| Site-to-site VPN | Identify traffic that should enter the tunnel. |
| Voice priority | Match voice traffic for QoS. |
| Router management security | Allow SSH only from trusted admin networks. |

The ACL is the traffic selector. The surrounding feature gives it meaning.

## Main Takeaway

An ACL is a list of matching rules, and the feature you attach it to defines what `permit` and `deny` actually mean.

For filtering, `permit` means pass. For NAT, `permit` means translate. For QoS, `permit` may mean prioritize. For management security, `permit` means allow access to the device.

Same tool, different job.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Standard ACL | ACL that matches source IP only. |
| Extended ACL | ACL that can match source, destination, protocol, and port. |
| Top-down processing | ACL lines are checked in order from first to last. |
| First match wins | ACL processing stops at the first matching statement. |
| Implicit deny | Invisible deny at the end of every ACL. |
| NAT ACL | ACL used to select traffic for translation. |
| QoS ACL | ACL used to classify traffic for priority treatment. |
| VTY | Virtual terminal lines used for remote device access. |

## Questions

### 1. Does an ACL act by itself?

Answer: No. It must be applied to an interface or used by another feature.

### 2. What does a standard ACL match?

Answer: Source IP address only.

### 3. What does an extended ACL match?

Answer: Source, destination, protocol, and often port numbers.

### 4. Why does ACL order matter?

Answer: ACLs process top-down and stop at the first match.

### 5. What is the implicit deny?

Answer: The invisible deny at the end of every ACL that denies traffic that matched no earlier permit.

## What To Review Later

- Standard ACL syntax.
- Extended ACL syntax.
- Wildcard masks.
- ACL placement: inbound vs outbound.
- NAT ACL behavior.
- VTY access-class configuration.
