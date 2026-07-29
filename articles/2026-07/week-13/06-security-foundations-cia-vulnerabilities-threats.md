# Security Foundations: CIA, Vulnerabilities, Threats

Source: закрытая страница курса  
Date added: 2026-07-29  
Related plan item: Week 13 / Security foundations: CIA, vulnerabilities, and threats  
Tags: network security, CIA triad, confidentiality, integrity, availability, vulnerability, threat, exploit, mitigation, DHCP snooping
Language: Russian
Translation pair: articles-en/2026-07/week-13/06-security-foundations-cia-vulnerabilities-threats.md

## Summary

- Security is not about building a perfect system; it is about protecting a usable system reasonably well.
- The CIA triad gives the core security mission: confidentiality, integrity and availability.
- A vulnerability is a weakness, a threat is something that can abuse it, and an exploit is the method used.
- Every useful system has tradeoffs between convenience and risk.
- Mitigation means applying controls that reduce or manage risk.
- DHCP snooping is a practical example of reducing risk without removing DHCP.

## Key Points

- Confidentiality means data stays private.
- Integrity means data stays accurate and trustworthy.
- Availability means systems are reachable when needed.
- Security decisions depend on likelihood, impact and mitigation cost.
- Not every vulnerability deserves the same urgency.
- Real security is prioritization, not panic.

## Notes

Security does not mean locking everything so tightly that nobody can use it.

A coffee shop network that is perfectly locked down but cannot support customers, payment systems or staff is not successful. The goal is a usable system that is protected well enough for the business risk.

That balance is the foundation for every later security control.

## The CIA Triad

The CIA triad is the core framework:

| Principle | Meaning | NetworkChuck Coffee example |
| --- | --- | --- |
| Confidentiality | Data is seen only by authorized people or systems. | Customer records are not exposed. |
| Integrity | Data stays accurate and trustworthy. | Inventory, financial records and configs are not altered improperly. |
| Availability | Systems are up and reachable when needed. | POS systems work during the morning rush. |

Most security conversations connect back to one or more of these goals.

If customer data leaks, confidentiality is broken.

If someone changes device configs without authorization, integrity is broken.

If payment systems go offline, availability is broken.

## Vulnerability, Threat, Exploit

These terms are easier when separated clearly.

| Term | Meaning |
| --- | --- |
| Vulnerability | A weakness. |
| Threat | Something or someone that could take advantage of the weakness. |
| Exploit | The method used to take advantage of the weakness. |
| Threat actor | Person, group or system causing malicious or harmful activity. |
| Mitigation | Control used to reduce the risk. |

Simple analogy:

| House example | Security term |
| --- | --- |
| Window | Vulnerability |
| Burglar | Threat actor |
| Rock through the window | Exploit |
| Lock, alarm, stronger glass | Mitigation |

The same pattern applies to networks.

## Useful Systems Have Weaknesses

Every useful network service creates some opening.

Examples:

- DHCP makes addressing easy, but rogue DHCP can cause outages.
- Wi-Fi gives mobility, but adds wireless attack surface.
- Remote access helps admins, but creates login exposure.
- Web services support users, but can be attacked.
- File sharing helps teams, but can expose data if misconfigured.

Convenience and security are always in tension.

The goal is not to remove all usefulness. The goal is to understand the risk and apply the right controls.

## Internal Threats

Security problems do not always come from outside attackers.

They can come from:

- employees;
- contractors;
- unmanaged devices;
- careless configuration;
- someone plugging in the wrong device;
- malicious insiders;
- users who do not understand the impact of their actions.

Sometimes intent is malicious. Sometimes it is ignorance. The network still suffers either way.

That is why security design must consider both external and internal risk.

## Security Is A Balance

Security is not one-size-fits-all.

Different organizations can make different decisions about the same risk.

Decision factors:

- likelihood of the event;
- business impact if it happens;
- cost of mitigation;
- usability impact;
- compliance requirements;
- company culture;
- operational complexity.

Good security work asks:

```text
How likely is this?
What happens if it succeeds?
What does the mitigation cost in money, time or usability?
```

That is how real teams prioritize.

## DHCP Example

DHCP is useful because it automatically gives IP addresses to clients.

At NetworkChuck Coffee, manually configuring every laptop, tablet, printer and POS terminal would be painful.

But DHCP has a risk: a rogue DHCP server could appear on the network.

Attack pattern:

| Element | DHCP example |
| --- | --- |
| Asset | Network clients need correct IP configuration. |
| Vulnerability | Clients trust DHCP responses. |
| Threat | A malicious or careless user introduces a rogue DHCP server. |
| Exploit | Fake DHCP offers are sent to clients. |
| Impact | Clients get bad gateway/DNS/IP information and lose connectivity or get redirected. |
| Mitigation | DHCP snooping. |

DHCP snooping lets the switch define which ports are trusted to send DHCP server responses.

If an unauthorized port tries to act like a DHCP server, the switch can block those responses.

That is good security: keep the useful service, but control the dangerous behavior.

## Mitigation Mindset

Mitigation does not always mean eliminating risk completely.

It can mean:

- reducing likelihood;
- reducing impact;
- detecting abuse faster;
- limiting blast radius;
- making recovery easier;
- documenting accepted risk.

Examples:

| Risk | Mitigation |
| --- | --- |
| Rogue DHCP server | DHCP snooping. |
| Guest Wi-Fi reaching internal systems | VLAN segmentation and ACLs. |
| Unauthorized device management | SSH-only, strong passwords, VTY ACLs. |
| Config tampering | AAA, backups, logging and change control. |
| Malware spread | Segmentation and endpoint protection. |

The control should match the actual risk.

## NetworkChuck Coffee Design View

For NetworkChuck Coffee, the mission is not abstract.

Protect:

- customer data;
- payment systems;
- inventory records;
- staff systems;
- cameras;
- network devices;
- uptime during busy hours.

The right security design keeps the business working while reducing risk.

That means:

- customers can still connect to Wi-Fi;
- payment systems still process sales;
- staff tools stay available;
- sensitive systems are not exposed to guest devices;
- admins can manage gear from trusted networks;
- failures and attacks have limited blast radius.

## Main Takeaway

Security is attack and counterattack.

Attackers look for weaknesses. Defenders look for those weaknesses first and apply controls before they are abused.

The right questions:

```text
What are we protecting?
What could go wrong?
How might someone abuse it?
What can we do about it without breaking the business?
```

Everything else builds on that foundation.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| CIA triad | Confidentiality, integrity and availability. |
| Confidentiality | Keeping data private. |
| Integrity | Keeping data accurate and trustworthy. |
| Availability | Keeping systems accessible when needed. |
| Vulnerability | Weakness that can be abused. |
| Threat | Something that could take advantage of a weakness. |
| Exploit | Method used to abuse a vulnerability. |
| Threat actor | Person, group or system carrying out harmful activity. |
| Mitigation | Control that reduces or manages risk. |
| DHCP snooping | Switch feature that blocks unauthorized DHCP server responses. |

## Questions

### 1. What are the three parts of the CIA triad?

Answer: Confidentiality, integrity and availability.

### 2. What is a vulnerability?

Answer: A weakness that could be abused.

### 3. What is the difference between a threat and an exploit?

Answer: A threat is something that could cause harm; an exploit is the method used to take advantage of a vulnerability.

### 4. Why is security a balance?

Answer: Controls reduce risk, but they can also cost money, time, complexity or usability.

### 5. What does DHCP snooping mitigate?

Answer: Rogue DHCP servers sending unauthorized DHCP responses to clients.

## What To Review Later

- CIA triad examples.
- Vulnerability vs threat vs exploit.
- Risk prioritization.
- DHCP snooping.
- Insider threats.
- Mitigation planning.
