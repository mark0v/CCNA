# Layer 2 Security Policy Rollout

Source: closed course page  
Date added: 2026-08-02  
Related plan item: Week 14 / Layer 2 security policy rollout  
Tags: Layer 2 security, Port Security, DHCP Snooping, Dynamic ARP Inspection, switch security, trust boundary, rollout policy
Language: English
Translation pair: articles/2026-08/week-14/04-layer-2-security-policy-rollout.md

## Summary

- Layer 2 security should be deployed as a policy, not as a random set of commands.
- A vague request to "secure the network" must become specific rules for ports, VLANs, and trust boundaries.
- Port Security, DHCP Snooping, and Dynamic ARP Inspection address different access-layer risks.
- End-device ports are usually locked down more tightly than uplinks, router ports, and access point ports.
- Trusted and untrusted boundaries must be identified before features are enabled.
- A bad rollout can cause an outage as quickly as an attack.
- In production, map ports first, write the config, use a maintenance window, and verify afterward.

## Key Points

- A written policy matters because it makes configuration repeatable and defensible.
- Port Security limits which MAC addresses can appear on end-device ports.
- DHCP Snooping blocks rogue DHCP servers and helps reduce DHCP starvation risk.
- DAI uses the DHCP Snooping binding table to catch ARP spoofing.
- Uplink, trunk, router, firewall, and wireless access point ports must not be treated like ordinary client ports.
- Verification after deployment is mandatory; without it, you do not know what is actually active.

## Notes

On paper, the request sounds simple: implement Port Security, DHCP Snooping, and Dynamic ARP Inspection.

In reality, that request is too broad. Someone has to decide:

- which ports are user access ports;
- which ports lead to infrastructure;
- which VLANs are protected;
- where DHCP replies travel;
- where ARP traffic should be trusted;
- what happens when a policy is violated;
- how to roll back if connectivity breaks.

That is not just entering commands. That is policy design.

## Why Policy Matters

If features are enabled from memory or mood, the network quickly becomes inconsistent.

One switch has Port Security, another does not. DHCP Snooping is enabled for only one VLAN. An uplink is missing trust. DAI is enabled without accounting for a static-IP server.

The result:

- sites behave differently;
- troubleshooting takes longer;
- new administrators do not understand the standard;
- changes are risky to delegate;
- after an incident, it is hard to prove what policy existed.

A written policy is not bureaucracy. It makes the network repeatable, verifiable, and maintainable.

## Port Security Policy

Baseline rule:

```text
End-device ports get Port Security.
Infrastructure ports are not treated as ordinary client ports.
```

For Castle Rysen, the logic is:

- one fixed endpoint port gets `maximum 1`;
- sensitive ports use `shutdown` on violation;
- stable devices can use sticky MAC;
- patron ports may be a bad fit for sticky MAC;
- an IP phone with a PC behind it may require `maximum 2`.

Example:

```text
interface range fa0/3-20
 switchport mode access
 switchport port-security
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation shutdown
```

This rule does not fit uplinks, router ports, or ports toward wireless access points. Those ports may legitimately see many MAC addresses, and a strict `maximum 1` would break normal operation.

## DHCP Snooping Policy

DHCP Snooping answers one important question:

```text
Which ports are allowed to bring in DHCP server replies?
```

Policy:

- enable DHCP Snooping globally;
- enable it for the cafe VLANs;
- trust only ports toward the legitimate DHCP server;
- leave client-facing access ports untrusted;
- apply a rate limit on untrusted ports.

Example:

```text
ip dhcp snooping
ip dhcp snooping vlan 10,20,30

interface gi0/1
 ip dhcp snooping trust

interface range fa0/3-20
 ip dhcp snooping limit rate 10
```

If you forget a trusted uplink, clients may stop receiving addresses. Trace the DHCP offer path across all switches first.

## DHCP Starvation Protection

DHCP starvation is an attack where a device sends many DHCP requests, often with different MAC addresses, to exhaust the DHCP pool.

The features work together:

- Port Security limits the number of MAC addresses on the port;
- DHCP Snooping blocks rogue DHCP replies;
- DHCP rate limiting limits DHCP packet volume.

This does not make the network invulnerable, but it significantly reduces the risk of simple Layer 2 attacks.

## Dynamic ARP Inspection Policy

DAI validates ARP messages and helps stop ARP spoofing.

It depends on the DHCP Snooping binding table.

Policy:

- enable and verify DHCP Snooping first;
- then enable DAI on the target VLANs;
- review infrastructure and uplink ports separately;
- account for static-IP devices before rollout;
- verify ARP rate limits.

Example:

```text
ip arp inspection vlan 10,20,30

interface gi0/1
 ip arp inspection trust
```

User-facing access ports usually stay untrusted. That is where ARP should be inspected. Router, firewall, server, and trunk ports may require trust or static bindings.

## Trusted And Untrusted

Trust boundaries are the central idea in this topic.

| Feature | Trusted usually means | Untrusted usually means |
| --- | --- | --- |
| DHCP Snooping | Uplink toward DHCP server/router | Client access ports |
| DAI | Uplinks, trunks, infrastructure | Client access ports |
| Port Security | Not trust-based; MAC-limit based | End-device access ports |

A trust boundary mistake often looks like a strange network issue:

- DHCP does not assign addresses;
- ARP stops working;
- clients see the gateway but cannot reach beyond it;
- one segment works and another does not;
- devices disappear after protection is enabled.

That is not random. The switch is blocking traffic according to the configured policy.

## Rollout Order

Practical rollout:

1. Build a port map.
2. Separate access, trunk, uplink, and infrastructure ports.
3. Find the DHCP server and DHCP offer path.
4. Identify static-IP devices.
5. Write the Port Security, DHCP Snooping, and DAI policy.
6. Prepare the config in a text file.
7. Deploy during a maintenance window.
8. Verify with show commands.
9. Save the configuration.
10. Document exceptions.

This is slower than typing commands live, but far more reliable.

## Verification

Commands:

```text
show port-security
show port-security interface fa0/3
show ip dhcp snooping
show ip dhcp snooping binding
show ip arp inspection
show ip arp inspection interfaces
show interfaces status err-disabled
show interfaces trunk
```

Confirm:

- Port Security is enabled only where intended;
- violation mode matches the policy;
- DHCP Snooping is enabled on the correct VLANs;
- trusted DHCP ports are correct;
- the binding table is populated;
- DAI is enabled on the correct VLANs;
- trusted ARP interfaces are intentional;
- there are no unexpected err-disabled ports.

## Castle Rysen Scenario

Castle Rysen asked for Layer 2 security. That sounds high-level, but the engineer must turn it into a standard.

Policy result:

- end-device ports are controlled with Port Security;
- rogue DHCP servers are limited with DHCP Snooping;
- DHCP starvation becomes harder;
- ARP spoofing is checked with DAI;
- uplinks and infrastructure ports are not broken by incorrect trust;
- the configuration can be repeated across other cafe locations.

This is no longer a set of commands. It is a baseline access-layer security model.

## Main Takeaway

Layer 2 security is not a magic button.

It is a set of features that must match the real topology. Port Security controls who connects. DHCP Snooping controls who can provide IP settings. DAI controls who can claim IP-to-MAC identity.

Together, they make a switch more than a frame-forwarding device; they make it the first line of local network defense. But only if they are deployed as a policy, not as a random command set.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Layer 2 security | Security at the Ethernet switching layer. |
| Port Security | Limits MAC addresses on an access port. |
| DHCP Snooping | Blocks DHCP server replies on untrusted ports. |
| Dynamic ARP Inspection | Validates ARP messages against a trusted table. |
| DAI | Abbreviation for Dynamic ARP Inspection. |
| DHCP starvation | Attempt to exhaust the DHCP pool with many requests. |
| ARP spoofing | Forging ARP information to intercept traffic. |
| trusted port | Port allowed to carry infrastructure traffic for a specific feature. |
| untrusted port | Port where traffic is inspected or restricted. |
| rollout | Planned deployment of changes. |

## Questions

### 1. Why should Layer 2 security be deployed through a policy?

Answer: A policy makes settings repeatable, verifiable, and understandable for other administrators.

### 2. Where is Port Security usually enabled?

Answer: On end-device access ports where a limited number of MAC addresses is expected.

### 3. Which ports are usually trusted for DHCP Snooping?

Answer: Ports toward the real DHCP server, router, or uplink carrying DHCP offers.

### 4. Why should DAI not be enabled blindly?

Answer: Static-IP devices and infrastructure ports may not match the DHCP Snooping binding table and can be blocked.

### 5. What ties Port Security, DHCP Snooping, and DAI together?

Answer: They protect different parts of the access layer and together create a baseline Layer 2 security policy.

## What To Review Later

- Access/uplink/trunk port mapping.
- Port Security configuration.
- Trusted ports for DHCP Snooping.
- Binding table behavior.
- Trusted interfaces for DAI.
- Verification show commands.
