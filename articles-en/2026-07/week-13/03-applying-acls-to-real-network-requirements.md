# Applying ACLs To Real Network Requirements

Source: closed course page  
Date added: 2026-07-29  
Related plan item: Week 13 / Applying ACLs to real network requirements  
Tags: ACL, extended ACL, standard ACL, VTY, access-class, Plex, VLAN security, SSH, Telnet, logging
Language: English
Translation pair: articles/2026-07/week-13/03-applying-acls-to-real-network-requirements.md

## Summary

- ACLs become real when they enforce business requirements, not just lab syntax.
- Extended ACLs can allow specific application ports while denying broader subnet access.
- Order matters: specific permits must come before broader denies.
- A final `permit ip any any` may be needed to preserve normal traffic after targeted restrictions.
- Extended ACLs usually go close to the source.
- Standard ACLs are a clean fit for limiting VTY management access by source subnet.

## Key Points

- Plan ACL logic before typing commands.
- Routers normally route traffic unless policy stops it; ACLs flip the mindset to explicit matching.
- Application reachability and ping reachability are different tests.
- Plex-style access may need several TCP/UDP permit lines.
- `log` can turn ACL entries into useful troubleshooting visibility.
- Device management access should be restricted to approved admin or management networks.

## Notes

Knowing ACL syntax is not the same as deploying ACLs safely.

The real skill is translating requirements into traffic logic:

- who is sending traffic;
- where it is going;
- which ports or protocols are allowed;
- what must be blocked;
- where the policy should be enforced;
- how to test without breaking the business.

That planning step is what prevents an ACL from becoming an outage.

## Draw First, Configure Second

Before configuring an ACL, write the policy in plain language.

For Castle Rysen / NetworkChuck Coffee, the requirement looked like this:

1. Cafe patron devices should not freely access administrative devices.
2. Patron devices still need limited Plex access.
3. Cameras, network gear, and management resources should remain protected.
4. SSH and Telnet access to network devices should come only from approved management networks.

That becomes two ACL jobs:

| Requirement | Best ACL type |
| --- | --- |
| Allow specific Plex ports and deny other patron-to-admin traffic | Extended ACL |
| Allow only management subnets to SSH/Telnet to devices | Standard ACL on VTY lines |

## Extended ACL For Patron Filtering

The cafe patron VLAN should reach only specific services in the admin subnet.

ACL logic:

1. Permit required Plex TCP/UDP ports from patron subnet to Plex/admin subnet.
2. Deny all other IP traffic from patron subnet to admin subnet.
3. Permit everything else so internet and unrelated traffic still works.

Conceptual example:

```text
ip access-list extended cafe_filter
 remark Allow patron VLAN to reach Plex service ports
 permit tcp 10.0.18.0 0.0.0.255 10.0.10.0 0.0.0.255 eq 32400
 permit udp 10.0.18.0 0.0.0.255 10.0.10.0 0.0.0.255 eq 32400
 remark Block other patron access to admin VLAN
 deny ip 10.0.18.0 0.0.0.255 10.0.10.0 0.0.0.255
 remark Preserve normal traffic elsewhere
 permit ip any any
```

The exact ports and subnets depend on the environment. The pattern is the key.

## Why Order Matters

This works:

```text
permit required Plex traffic
deny all other patron-to-admin traffic
permit all other IP traffic
```

This breaks the intended access:

```text
deny all patron-to-admin traffic
permit required Plex traffic
permit all other IP traffic
```

The second version denies the traffic before the router reaches the specific permit lines.

ACLs process top-down. First match wins.

## Destination Ports

For application access, the service port is usually on the destination side.

If a patron device reaches Plex, HTTPS, or SSH, the client source port is usually a temporary high-numbered port. The destination service listens on the well-known or application port.

Read the line as a sentence:

```text
permit tcp from patron subnet to Plex subnet on destination port 32400
```

If the port is attached to the source side accidentally, the ACL may be syntactically valid but logically wrong.

## Applying The Extended ACL

Extended ACLs are usually applied close to the source.

For patron traffic, that means applying the ACL inbound on the patron VLAN subinterface.

Concept:

```text
interface g0/0.18
 ip access-group cafe_filter in
```

Think like the router:

- patron packets enter Layer 3 through the patron subinterface;
- the ACL inspects them as they enter;
- unwanted traffic is stopped early.

This avoids letting traffic travel across the network only to be denied later.

## Testing The Policy

Test both allowed and denied behavior.

Useful tests:

| Test | Expected result |
| --- | --- |
| Ping from patron device to Plex server | May fail if ICMP is not permitted. |
| App connection to Plex port | Should succeed if the right port is permitted. |
| Patron access to admin device management page | Should fail. |
| Patron internet access | Should still work because of final permit. |
| Admin access to devices | Should work from approved networks. |
| Non-management SSH/Telnet to device | Should fail. |

Ping is not the same as application reachability. If ICMP is not permitted, ping can fail while the application port still works.

Quick port test:

```text
telnet 10.0.10.20 32400
```

This is not a full application test, but it can show whether the TCP port is reachable.

## ACL Logging

ACL entries can include `log` for visibility.

Concept:

```text
permit tcp 10.0.18.0 0.0.0.255 host 10.0.10.20 eq 32400 log
deny ip 10.0.18.0 0.0.0.255 10.0.10.0 0.0.0.255 log
```

This helps identify which hosts are matching which lines.

Use logging carefully in production. Busy ACL entries can generate a lot of logs.

## Locking Down Device Management

Device management is a different problem.

Instead of filtering routed traffic between VLANs, the goal is to restrict who can start remote management sessions to the device itself.

VTY lines are used for remote access such as SSH and Telnet.

For this use case, a standard ACL is often clean because source subnet is the main question:

```text
ip access-list standard MGMT_ONLY
 permit 10.0.10.0 0.0.0.255
 permit 10.0.40.0 0.0.0.255
```

Apply it to VTY lines:

```text
line vty 0 15
 access-class MGMT_ONLY in
```

Now management login attempts are checked by source IP before access is allowed.

## Standard ACL vs Extended ACL In This Design

Use the ACL type that matches the problem.

| Problem | ACL choice | Reason |
| --- | --- | --- |
| Patron VLAN needs only specific Plex ports | Extended ACL | Need source, destination, and ports. |
| Only management subnets can SSH/Telnet to devices | Standard ACL | Source subnet is enough on VTY lines. |

Avoid overcomplicating the config. Precision is useful, but only where the requirement needs it.

## NetworkChuck Coffee Design View

At NetworkChuck Coffee, ACLs protect business functions while preserving customer experience.

Patron devices should not browse cameras, network gear, or admin systems. But customers may still need specific media or service access. Staff and network admins need management access, but only from trusted networks.

Good ACL design keeps the business running:

- customers keep useful access;
- administrative resources stay protected;
- management access is controlled;
- troubleshooting has clear tests;
- policies are documented and readable.

## Main Takeaway

ACLs are about thinking through traffic, not memorizing syntax.

Ask:

```text
Who is talking?
Where are they going?
Which protocols and ports are allowed?
What should be denied?
Where should the policy be enforced?
How will I prove it works?
```

That mindset turns ACLs from command memorization into network design.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `ip access-list extended cafe_filter` | Creates or edits a named extended ACL. |
| `permit tcp ... eq PORT` | Permits TCP traffic to a specific port. |
| `deny ip SOURCE DESTINATION` | Denies all IP traffic matching source and destination. |
| `permit ip any any` | Allows all remaining IP traffic that reaches the line. |
| `ip access-group NAME in` | Applies ACL inbound on an interface. |
| `access-class NAME in` | Applies ACL to inbound VTY management access. |
| VTY | Virtual terminal lines for SSH/Telnet access. |
| `log` | Adds logging for ACL matches. |

## Questions

### 1. Why plan ACL logic before configuring?

Answer: Because ACL order, implicit deny, and placement can break traffic immediately if the policy is not clear.

### 2. Why permit Plex ports before denying patron-to-admin traffic?

Answer: ACLs process top-down, so the specific allowed traffic must match before the broader deny.

### 3. Why can ping fail even when Plex access works?

Answer: Ping uses ICMP, and ICMP may not be permitted even though Plex TCP/UDP ports are allowed.

### 4. Why apply the extended ACL near the patron VLAN?

Answer: Extended ACLs are specific, so unwanted traffic should be stopped close to the source.

### 5. Why use `access-class` on VTY lines?

Answer: It limits SSH/Telnet management access based on source IP before a remote session is allowed.

## What To Review Later

- Extended ACL order.
- Application port requirements.
- Source vs destination port placement.
- ACL logging impact.
- VTY `access-class`.
- Testing allowed and denied traffic.
