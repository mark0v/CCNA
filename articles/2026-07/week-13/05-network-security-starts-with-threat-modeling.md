# Network Security Starts With Threat Modeling

Source: закрытая страница курса  
Date added: 2026-07-29  
Related plan item: Week 13 / Network security starts with threat modeling  
Tags: network security, threat modeling, risk, controls, segmentation, firewall, defense strategy, security foundations
Language: Russian
Translation pair: articles-en/2026-07/week-13/05-network-security-starts-with-threat-modeling.md

## Summary

- Network security is not one tool, one firewall rule or one magic setting.
- Before configuring controls, you need to understand what you are defending against.
- This part of security starts with concepts, methods and awareness before hands-on configuration.
- Threats, risks and defenses must be mapped before tools make sense.
- NetworkChuck Coffee has real assets to protect: customer Wi-Fi, payment systems, employee devices, cameras and inventory systems.
- Good security starts with the threat, then chooses the right control.

## Key Points

- Security is a full career area, not a small CCNA side topic.
- Tools make sense only when you understand the risk they reduce.
- Firewalls, segmentation and access controls are methods, not the whole mission.
- If you do not understand the attack, the defense can feel random.
- Conceptual security work prepares you for better hands-on configuration later.
- Business impact matters: compromised systems and downtime cost money.

## Notes

Network security can feel less exciting at the beginning because the first step is not always a command.

The first step is orientation.

Before configuring firewalls, ACLs, VPNs, segmentation or device hardening, you need a mental map:

- what needs protection;
- what can go wrong;
- who or what might cause harm;
- what controls reduce the risk;
- how those controls affect the business.

That map keeps security from becoming random tool-clicking.

## Security Is Not One Thing

A common mistake is treating security as one feature.

Examples of bad mental models:

- "Install a firewall and we are secure."
- "Block a few ports and we are done."
- "Turn on encryption and the problem is solved."
- "Use VLANs and everything is safe."

Real security is layered. Each control solves a specific problem, and no single control solves everything.

Better model:

```text
Threat -> risk -> control -> verification
```

You first understand the threat. Then you choose a control that actually reduces that risk. Then you verify that the control works and does not break the business.

## Why Start With Concepts

Hands-on configuration matters, but it should not come first every time.

If you configure a firewall without knowing the threat, you may block the wrong traffic.

If you segment a network without knowing what must communicate, you may break applications.

If you lock down device access without knowing the management path, you may cut off the admin team.

Conceptual work helps answer:

- what are we trying to prevent;
- what needs to keep working;
- what traffic is normal;
- what traffic is risky;
- where enforcement should happen;
- how to test safely.

That makes later configuration more deliberate.

## NetworkChuck Coffee Example

NetworkChuck Coffee has more than "a network."

It has business functions riding on the network:

- customer Wi-Fi;
- payment systems;
- employee devices;
- security cameras;
- inventory systems;
- back office services;
- network management access;
- maybe site-to-site connectivity between shops.

Those systems do not have the same risk level.

| Asset / traffic | Why it matters |
| --- | --- |
| Payment systems | Direct revenue and compliance exposure. |
| Customer Wi-Fi | Untrusted users and guest traffic. |
| Cameras | Physical security and privacy. |
| Inventory systems | Business operations. |
| Network gear | Control plane for the whole environment. |
| Employee devices | Common malware and credential risk. |

If the network is compromised during the morning rush, the problem is not only technical. Orders, payments, staff workflow and customer trust can all be affected.

## Threats Before Controls

The control should match the threat.

Examples:

| Threat / risk | Possible control |
| --- | --- |
| Guest Wi-Fi reaching internal systems | VLAN segmentation and ACLs/firewall rules. |
| Unauthorized router login | VTY access control, SSH-only, strong authentication. |
| Malware moving between devices | Segmentation, endpoint controls, monitoring. |
| Payment traffic exposed | Network isolation, encryption, strict access policy. |
| Public-facing service attacked | Firewall policy, patching, logging, rate limiting. |
| Lost uptime from misconfiguration | Change control, backups, testing and rollback plans. |

The important sequence:

```text
Start with the risk. Then choose the control.
```

Do not start with a tool and search for somewhere to use it.

## Defense Methods

This section is about recognizing categories, not memorizing every product.

Common defense methods include:

- segmentation;
- traffic filtering;
- device hardening;
- access control;
- authentication and authorization;
- encryption;
- monitoring and logging;
- backups and recovery;
- patching and vulnerability management;
- secure management access;
- physical security.

Each method answers a different question.

Examples:

| Method | Question it helps answer |
| --- | --- |
| Segmentation | What should be separated? |
| Filtering | What traffic should be allowed or denied? |
| Authentication | Who is allowed in? |
| Authorization | What are they allowed to do? |
| Encryption | What must be protected in transit? |
| Logging | How will we know what happened? |
| Backups | How do we recover? |

## From Knowing To Doing

The conceptual phase is not where the work ends.

It sets up the hands-on phase.

Good order:

1. Understand the threat.
2. Choose the defense method.
3. Configure the control.
4. Test allowed behavior.
5. Test denied behavior.
6. Document the result.
7. Monitor and revisit.

This is how you avoid becoming someone who can follow a configuration recipe but cannot explain why the recipe exists.

## Real-World Change Mindset

Security tools can cause outages when applied carelessly.

Before changing policy:

- know what traffic exists;
- know what traffic must continue;
- know where the control is applied;
- plan tests;
- have rollback steps;
- use maintenance windows when possible;
- document intent.

Fast results matter in business, but random controls can leave the real vulnerability untouched while breaking something users need.

## Main Takeaway

Network security starts with understanding the problem.

Before touching the firewall, ACL, VLAN, VPN or authentication setting, ask:

```text
What am I protecting?
What am I protecting it from?
What control actually reduces that risk?
How will I prove it works?
```

That lens makes every later security configuration more useful.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Threat | Something that can cause harm to a system or business. |
| Risk | Likelihood and impact of a threat affecting an asset. |
| Control | Defense used to reduce risk. |
| Segmentation | Separating networks or systems to limit access and blast radius. |
| Firewall | Device or feature that enforces traffic policy. |
| Authentication | Proving identity. |
| Authorization | Deciding what an authenticated user or system can do. |
| Logging | Recording events for monitoring and investigation. |
| Threat modeling | Thinking through threats, assets, risks and defenses before implementation. |

## Questions

### 1. Why not start network security with configuration immediately?

Answer: Because controls only make sense when you understand the threat and risk they are supposed to reduce.

### 2. Why is security not one tool?

Answer: Different threats require different controls, and no single feature solves every security problem.

### 3. What does NetworkChuck Coffee need to protect?

Answer: Customer Wi-Fi, payment systems, employee devices, cameras, inventory systems, management access and uptime.

### 4. What is the right order for choosing a security control?

Answer: Start with the threat and risk, then choose the control that reduces that risk.

### 5. Why does conceptual security knowledge matter?

Answer: It helps you configure tools with purpose instead of memorizing steps without understanding the mission.

## What To Review Later

- Common network security threats.
- Segmentation strategy.
- Firewall and ACL policy design.
- Secure management access.
- Logging and monitoring.
- Change control and rollback planning.
