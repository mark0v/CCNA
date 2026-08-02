# Access Switch Security Baseline

Source: closed course page  
Date added: 2026-08-02  
Related plan item: Week 14 / Access switch security baseline  
Tags: switch security, security baseline, Port Security, DHCP Snooping, Dynamic ARP Inspection, access layer, template
Language: English
Translation pair: articles/2026-08/week-14/05-access-switch-security-baseline.md

## Summary

- Port Security, DHCP Snooping, and Dynamic ARP Inspection should not remain only exam topics.
- The next step is turning them into a standard procedure for access switches.
- A policy can be short: what to enable, where to enable it, what to verify, and what exceptions exist.
- A CLI template helps apply protection consistently on every switch.
- Repeatability matters for security because random configuration creates random gaps.
- A good baseline policy starts in the lab and then moves into production.

## Key Points

- A security baseline is the starting set of protections applied by default.
- Do not wait for an incident to enable basic access-layer protections.
- A policy should be understandable, verifiable, and easy to hand to another administrator.
- A template should include verification commands, not only configuration commands.
- Exceptions must be documented: uplinks, trunks, wireless access points, static-IP devices, and IP phone plus PC ports.
- Confidence comes from repeatable practice, not from watching more lessons alone.

## Notes

Many people learn Port Security, DHCP Snooping, and Dynamic ARP Inspection, pass the check, and move on. That is the trap.

These features matter not because they appear in CCNA, but because they are practical protections for ordinary networks. Not only for large enterprises and not only for dedicated security teams. Anyone who touches access switches should think about how to lock them down.

The right question after this section is:

```text
How will I protect access switches by default?
```

The answer should be a procedure, not memory.

## Policy Instead Of Improvisation

If we were building NetworkChuck Coffee, these settings should not live only in an administrator's head.

We need a short document:

- which features are enabled on a new switch;
- which VLANs are protected;
- which ports are access ports;
- which ports are trusted;
- which violation mode is used;
- which show commands are run after deployment;
- which exceptions are allowed.

A policy does not need to be a huge document. It can start as one page in a knowledge base or a checklist in the repository.

The key is that it answers:

```text
What do we do every time we bring an access switch into service?
```

## Why Repeatability Matters

Consistency is part of security.

If one switch is configured carefully, the second partially, and the third has no protection, the network becomes unpredictable.

Common results:

- rogue DHCP passes where DHCP Snooping was missed;
- an extra device connects where Port Security is absent;
- ARP spoofing is possible in a VLAN where DAI was skipped;
- troubleshooting takes longer because there is no single standard;
- a new administrator does not know what to rely on.

Without a baseline, every new deployment becomes improvisation. In production, that is a bad habit.

## Minimal Access Switch Policy

Example policy:

| Area | Rule |
| --- | --- |
| End-device access ports | Enable Port Security. |
| Fixed devices | Use sticky MAC if the endpoint is stable. |
| Patron/shared ports | Do not use sticky without a clear reason. |
| IP phone + PC | Check whether `maximum 2` is required. |
| DHCP | Enable DHCP Snooping on production VLANs. |
| DHCP trusted | Trust only the uplink/router/server path. |
| ARP | Enable DAI after DHCP Snooping is verified. |
| Infrastructure ports | Treat separately, not like ordinary client ports. |
| Verification | Run show commands after every rollout. |

This is not the final standard for every company. It is a starting point to adapt to your network.

## Example CLI Template

A template should be clean and predictable.

```text
! Global Layer 2 security baseline
ip dhcp snooping
ip dhcp snooping vlan 10,20,30
ip arp inspection vlan 10,20,30

! Trusted uplink toward router/DHCP infrastructure
interface gi0/1
 description Uplink to infrastructure
 ip dhcp snooping trust
 ip arp inspection trust

! End-device access ports
interface range fa0/3-20
 switchport mode access
 switchport port-security
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation shutdown
 ip dhcp snooping limit rate 10
```

These commands are not for blind copying. They show the structure:

- global features first;
- trusted interfaces next;
- access ports next;
- verification afterward.

Replace VLANs, interfaces, and exceptions before applying the template.

## Verification Block

A template without verification is only half the work.

After configuration, use:

```text
show port-security
show ip dhcp snooping
show ip dhcp snooping binding
show ip arp inspection
show ip arp inspection interfaces
show interfaces status err-disabled
show interfaces trunk
```

Verify:

- features are enabled on the intended VLANs;
- trusted ports are correct;
- client ports are not trusted without a reason;
- the binding table is populated;
- there are no unexpected err-disabled ports;
- the real configuration matches the policy.

## Exceptions

A good standard explicitly describes exceptions.

Examples:

- switch uplinks;
- trunks to other switches;
- routers or firewalls;
- wireless access points with many clients;
- servers with static IP addresses;
- IP phones with PCs behind them;
- temporary lab ports;
- troubleshooting ports.

An exception does not mean "configure it however." It means the reason is known, the risk is accepted, and the configuration is documented.

## Practical Plan

Do three things next:

1. Write a one-page baseline policy for access switches.
2. Build a CLI template from that policy.
3. Run the template in a lab until deployment and verification feel routine.

That is better than watching more material and waiting for confidence to appear.

Confidence comes from the loop:

```text
configure -> break -> verify -> fix -> repeat
```

That is how commands become skill.

## NetworkChuck Coffee Scenario

For a new NetworkChuck Coffee location, the administrator should not start from a blank page.

There is already a baseline:

- access ports get Port Security;
- DHCP is protected with DHCP Snooping;
- ARP is inspected with DAI;
- the infrastructure path is trusted;
- exceptions are documented;
- show commands are run after rollout.

That means the network is built to a standard, not by mood.

## Main Takeaway

Basic Layer 2 security should become a habit.

Port Security, DHCP Snooping, and Dynamic ARP Inspection are not just CCNA topics. They are building blocks for normal access-layer protection.

When you turn them into a policy and template, you stop merely knowing commands. You start designing a process that can be repeated, verified, and handed to another engineer.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| security baseline | Minimum protection standard applied by default. |
| CLI template | Repeatable set of commands for standard configuration. |
| Port Security | Limits MAC addresses on an access port. |
| DHCP Snooping | Blocks DHCP replies on untrusted ports. |
| Dynamic ARP Inspection | Validates ARP against a trusted table. |
| trusted port | Port allowed to carry infrastructure traffic. |
| exception | Intentional deviation from the baseline with a documented reason. |
| rollout | Planned deployment of configuration changes. |

## Questions

### 1. Why should these features not remain only exam material?

Answer: They solve real access-layer problems and should become part of standard configuration.

### 2. What should a baseline policy include?

Answer: Feature rules, trusted ports, VLANs, exceptions, and verification commands.

### 3. Why should a template include verification commands?

Answer: Without verification, you cannot prove the configuration works or matches the policy.

### 4. Why document exceptions?

Answer: Undocumented exceptions become hidden risks and make troubleshooting harder.

### 5. How do commands become skill?

Answer: By repeating deployment in the lab, verifying results, breaking scenarios, and fixing mistakes.

## What To Review Later

- One-page access switch baseline policy.
- CLI template for Layer 2 security.
- Exceptions for uplinks, trunks, and static IP devices.
- Verification commands.
- Lab testing order.
- Difference between knowing a command and having a repeatable process.
