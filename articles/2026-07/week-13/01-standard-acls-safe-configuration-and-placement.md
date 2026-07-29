# Standard ACLs: Safe Configuration And Placement

Source: закрытая страница курса  
Date added: 2026-07-29  
Related plan item: Week 13 / Standard ACLs safe configuration and placement  
Tags: ACL, standard ACL, access list, implicit deny, named ACL, wildcard mask, sequence number, ip access-group
Language: Russian
Translation pair: articles-en/2026-07/week-13/01-standard-acls-safe-configuration-and-placement.md

## Summary

- Standard ACLs простые, потому что match только source IP address.
- Простота опасна: standard ACL легко блокирует больше traffic, чем планировалось.
- Перед удалением или изменением ACL нужно сначала проверить, где она applied.
- ACL with only deny statements блокирует остальной traffic через implicit deny.
- Named ACLs удобнее numbered ACLs because names explain intent.
- Standard ACL best practice: place it as close to the destination as possible.

## Key Points

- An ACL can be applied to interfaces, VTY lines or other features.
- Remove ACL references before deleting or rewriting the ACL itself.
- A single-host match can use `host 10.0.0.10` or wildcard `10.0.0.10 0.0.0.0`.
- Add `permit any` when the goal is to block one source but allow everyone else.
- Named ACL configuration mode supports sequence numbers and line edits.
- Direction is from the router's point of view: inbound means traffic entering the router interface.

## Notes

Standard ACLs feel easy because there is not much to match. They only look at source IP address.

That simplicity is useful, but it also makes standard ACLs blunt. If you apply one in the wrong place, you might block a host from reaching much more than the one destination you meant to protect.

The safe habit is to think about two questions before touching the config:

1. What does this ACL match?
2. Where is this ACL applied right now?

## Cleanup Before Changes

Before deleting or rewriting an ACL, check where it is referenced.

Places to check:

- router interfaces;
- subinterfaces;
- VTY lines;
- NAT rules;
- VPN or QoS features;
- any other feature that can call an ACL.

Why this matters: an ACL can be applied somewhere even if it currently has no entries. Later, if someone creates a new ACL with the same name or number, it can take effect immediately at the old attachment point.

That creates a delayed outage: everything looks fine during cleanup, then traffic breaks later when a new statement appears.

Safe order:

1. Find where the ACL is applied.
2. Remove the ACL from the interface, line or feature.
3. Then delete or rebuild the ACL.
4. Reapply only after the new list is complete and reviewed.

## Building A Named Standard ACL

Named ACLs are easier to maintain than numbered ACLs because the name explains the purpose.

Example:

```text
ip access-list standard PC1-FILTER
 deny host 10.0.10.50
 permit any
```

This says:

- deny traffic sourced from `10.0.10.50`;
- permit everything else.

The `permit any` matters. Without it, the implicit deny at the bottom blocks all other traffic too.

## Host Match And Wildcard Mask

These two statements match the same single host:

```text
deny host 10.0.10.50
deny 10.0.10.50 0.0.0.0
```

The wildcard mask `0.0.0.0` means every bit must match exactly.

Cisco may display the cleaner `host` form automatically because it is easier to read.

For standard ACLs, remember: even when you match a single host, you are still matching only source address. You are not matching destination, protocol or port.

## Implicit Deny

Every ACL has an invisible deny at the bottom.

Conceptually:

```text
deny any
```

If your ACL only says:

```text
ip access-list standard PC1-FILTER
 deny host 10.0.10.50
```

then the result is:

```text
deny host 10.0.10.50
deny any
```

That blocks the host and everyone else.

To block one source but allow the rest, add:

```text
permit any
```

An ACL with only deny statements is usually a production warning sign unless the feature using it has a very specific purpose.

## Editing With Sequence Numbers

Named ACL mode supports sequence numbers. This makes it easier to edit ACLs without deleting and rebuilding the whole list.

Example display:

```text
10 deny host 10.0.10.50
20 permit any
```

You can remove a specific line:

```text
ip access-list standard PC1-FILTER
 no 10
```

You can also insert a new line between existing entries by choosing a sequence number that fits.

This matters because real ACLs can become long. Surgical edits are safer than large rewrites.

## Remarks

Remarks are comments inside an ACL.

Example:

```text
ip access-list standard PC1-FILTER
 remark Block PC1 during access-list lab
 deny host 10.0.10.50
 permit any
```

A good remark explains why the rule exists.

Six months later, that context can prevent someone from deleting a rule that was protecting a real business need.

## Applying The ACL

Creating the ACL does nothing until it is applied.

For interface filtering, use `ip access-group`:

```text
interface g0/0.10
 ip access-group PC1-FILTER in
```

Direction is from the router's point of view.

| Direction | Meaning |
| --- | --- |
| `in` | Traffic enters this router interface. |
| `out` | Traffic exits this router interface. |

Useful mental model: be the router. Ask whether the packet is coming into the interface or leaving through it.

If PC1 is in the subnet connected to `g0/0.10`, and PC1 sends traffic toward the router, that traffic is inbound on `g0/0.10`.

## Removing The ACL From An Interface

To stop applying the ACL:

```text
interface g0/0.10
 no ip access-group PC1-FILTER in
```

This removes the attachment. It does not necessarily delete the ACL from the configuration.

That distinction matters:

- removing application stops the ACL from filtering at that interface;
- deleting the ACL removes the list itself;
- doing changes in the wrong order can create surprises later.

## Standard ACL Placement

Standard ACLs only match source IP address.

They cannot match:

- destination address;
- protocol;
- TCP/UDP port;
- application type.

Because of that, standard ACLs should usually be placed as close to the destination as possible.

Why?

If you place a standard ACL close to the source, you may block the source from reaching everything, not just the one destination you intended.

If you place it near the destination, the source can still reach other networks, and only gets blocked when trying to reach the protected destination area.

## NetworkChuck Coffee Design View

For NetworkChuck Coffee, imagine one PC should not reach a particular internal resource, but should still reach the internet, printers or other allowed services.

A standard ACL near the source may block too broadly.

A better design places the standard ACL close to the destination network being protected.

That limitation is also why extended ACLs are often preferred for precise filtering. Extended ACLs can match source and destination, so they give more control.

## Main Takeaway

Standard ACLs are easy because they only match source IP. They are dangerous for the same reason.

Use safe habits:

- check where the ACL is applied;
- remove old references before rewriting;
- remember implicit deny;
- use named ACLs;
- add `permit any` when needed;
- use sequence numbers and remarks;
- place standard ACLs close to the destination.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `ip access-list standard NAME` | Creates or edits a named standard ACL. |
| `deny host A.B.C.D` | Denies traffic sourced from one host. |
| `permit any` | Permits all other sources. |
| `ip access-group NAME in` | Applies an ACL inbound on an interface. |
| `no ip access-group NAME in` | Removes inbound ACL application from an interface. |
| Sequence number | Line number used to edit ACL entries. |
| Remark | Comment explaining an ACL entry or list. |
| Implicit deny | Invisible deny at the end of every ACL. |

## Questions

### 1. What does a standard ACL match?

Answer: Source IP address only.

### 2. Why is an ACL with only deny statements dangerous?

Answer: Because the implicit deny blocks everything else that is not explicitly permitted.

### 3. Why use named ACLs?

Answer: Names describe intent and make the configuration easier to maintain.

### 4. What does `ip access-group` do?

Answer: It applies an ACL to an interface in a specific direction.

### 5. Where should standard ACLs usually be placed?

Answer: As close to the destination as possible.

## What To Review Later

- Numbered vs named ACLs.
- Standard ACL syntax.
- Wildcard masks.
- Sequence numbers and remarks.
- Inbound vs outbound direction.
- Extended ACL placement rules.
