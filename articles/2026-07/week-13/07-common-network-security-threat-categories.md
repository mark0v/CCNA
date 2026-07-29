# Common Network Security Threat Categories

Source: закрытая страница курса  
Date added: 2026-07-29  
Related plan item: Week 13 / Common network security threat categories  
Tags: network security, DoS, DDoS, spoofing, MITM, reconnaissance, malware, ransomware, DHCP, port scanning
Language: Russian
Translation pair: articles-en/2026-07/week-13/07-common-network-security-threat-categories.md

## Summary

- Security threats are easier to understand as behavior categories, not isolated attack names.
- DoS attacks try to make systems unavailable.
- Spoofing means pretending to be a device, address or identity.
- Man-in-the-middle attacks intercept traffic between systems.
- Reflection, amplification and DDoS attacks multiply impact.
- Reconnaissance gathers information before the main attack.
- Malware is an umbrella for malicious software such as ransomware, worms, viruses and backdoors.

## Key Points

- Threat categories often overlap in real attacks.
- Spoofing can support DoS or man-in-the-middle attacks.
- Reconnaissance can happen quietly before obvious compromise.
- Open ports and exposed services are possible entry points.
- Ransomware creates immediate business impact by encrypting or locking data.
- Backdoors allow attackers to return after initial compromise.

## Notes

Security gets more practical when you recognize patterns.

You do not need to memorize a thousand attack names first. Start with the behavior:

- overwhelm;
- impersonate;
- intercept;
- amplify;
- scout;
- infect;
- persist.

Once you recognize the behavior, you can think about the weakness being targeted and the defense that might reduce the risk.

## Denial Of Service

Denial of Service, or DoS, is about making a service unavailable.

The attacker may not care about stealing data. The goal can be simple:

```text
Make the target too busy, too full or too broken to serve real users.
```

Classic example: TCP SYN flood.

Normal TCP handshake:

1. Client sends SYN.
2. Server replies SYN-ACK.
3. Client replies ACK.

In a SYN flood, the attacker starts many connections but does not finish them. The target keeps track of half-open connections and can run out of resources.

Impact:

- server becomes slow or unavailable;
- router, switch or access point resources are exhausted;
- legitimate users cannot connect;
- business services go offline.

At NetworkChuck Coffee, if online ordering or payment systems become unavailable during a rush, availability is broken and revenue is affected.

## Distributed Denial Of Service

DDoS is DoS with many sources.

Instead of one attacker, many compromised systems send traffic at the same target.

Possible sources:

- infected PCs;
- compromised servers;
- IoT devices;
- cameras;
- home routers;
- rented botnet infrastructure.

DDoS is harder to handle because blocking one source is not enough. Traffic can arrive from many networks at once.

## Spoofing

Spoofing means pretending to be something else.

Examples:

- MAC address spoofing;
- IP address spoofing;
- pretending to be another device;
- using fake identities in protocol messages.

Spoofing can create direct problems or support another attack.

DHCP example:

1. Attacker sends many fake DHCP requests.
2. Each request uses a different made-up MAC address.
3. DHCP server leases addresses to fake clients.
4. Real clients may not get valid IP addresses.

One device pretends to be many devices, creating a denial-of-service condition.

## Man In The Middle

Man-in-the-middle, or MITM, means the attacker positions themselves between two communicating systems.

The dangerous part is that traffic may still work.

The attacker may:

- read traffic;
- capture credentials;
- modify data;
- redirect users;
- silently observe communication.

NetworkChuck Coffee example:

An attacker introduces a rogue DHCP server. Clients receive a fake default gateway and DNS settings. Traffic starts flowing through the attacker's system.

Users may still reach websites, so the attack can stay quiet while data is captured or modified.

## Reflection And Amplification

Reflection and amplification attacks multiply effect.

Reflection means traffic is bounced through other systems, often to hide the real source or make responses go to the victim.

Amplification means a small request causes a much larger response, increasing attack volume.

These techniques can make DoS or DDoS attacks stronger.

General idea:

```text
Small attacker effort -> larger victim impact
```

The defense often requires upstream filtering, provider help and reducing exposed services that can be abused.

## Reconnaissance

Reconnaissance is information gathering before or during an attack.

Examples:

- WHOIS lookups;
- DNS enumeration;
- port scanning;
- banner grabbing;
- checking public services;
- identifying exposed software versions;
- mapping reachable networks.

Port scanning checks which TCP or UDP ports are open.

Open ports are not automatically bad. Services need ports to work. But every exposed service is something to inventory, patch, monitor and justify.

Recon matters because the visible attack often starts after the attacker already knows what to target.

## Malware

Malware means malicious software.

It is an umbrella term.

Examples:

| Malware type | Behavior |
| --- | --- |
| Virus | Attaches to files or programs and spreads when they run. |
| Worm | Spreads across systems, often without user action. |
| Trojan | Pretends to be legitimate or useful software. |
| Ransomware | Encrypts or locks data and demands payment. |
| Backdoor | Hidden access path for later return. |
| Spyware | Collects information silently. |

Malware can do more than infect one device. It can create persistence, steal data, move laterally, disable services and prepare the environment for later attacks.

## Ransomware And Backdoors

Ransomware is especially painful because the business impact is immediate.

Possible effects:

- files encrypted;
- servers unavailable;
- payment systems disrupted;
- backups targeted;
- operations stopped;
- customer trust damaged.

Backdoors make recovery harder. If attackers leave a hidden way back in, restoring a system may not be enough.

Defenders may close one hole and then discover another path the attacker prepared earlier.

This is why incident response must include containment, eradication and validation, not only restoring files.

## NetworkChuck Coffee Design View

For NetworkChuck Coffee, these threats map directly to business harm.

| Threat category | Business impact |
| --- | --- |
| DoS / DDoS | Online ordering or payments unavailable. |
| Spoofing | DHCP exhaustion or fake device identity. |
| MITM | Customer or staff traffic intercepted. |
| Reconnaissance | Attacker learns exposed services and weaknesses. |
| Malware | POS, inventory, payroll or customer data affected. |
| Backdoors | Attacker returns after cleanup. |

Security is not abstract when downtime, customer data and trust are involved.

## Basic Hygiene First

Before obsessing over advanced defenses, start with visibility and hygiene.

Practical actions:

- know what services are exposed;
- close unnecessary ports;
- inventory reachable systems;
- patch public-facing services;
- limit public information where possible;
- monitor logs;
- segment guest and internal networks;
- protect DHCP and management-plane access.

Advanced tools help, but obvious open doors still matter.

## Main Takeaway

Threats are easier to understand as families of behavior.

Remember:

- DoS overwhelms.
- Spoofing impersonates.
- MITM intercepts.
- Reflection and amplification multiply impact.
- Reconnaissance scouts.
- Malware infects, persists, steals or extorts.

The next step is matching these threat categories to the weaknesses they exploit and the defenses that reduce the risk.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| DoS | Denial of Service, attack that makes a service unavailable. |
| DDoS | Distributed Denial of Service from many sources. |
| SYN flood | DoS attack abusing half-open TCP handshakes. |
| Spoofing | Pretending to be another address, device or identity. |
| MITM | Man-in-the-middle, attacker intercepts traffic between systems. |
| Reflection | Bouncing attack traffic through other systems. |
| Amplification | Making small requests create larger responses toward a victim. |
| Reconnaissance | Gathering information before attack. |
| Port scan | Checking which TCP/UDP ports are open. |
| Malware | Malicious software umbrella term. |
| Ransomware | Malware that locks or encrypts data for payment. |
| Backdoor | Hidden method for attacker return. |

## Questions

### 1. What is the goal of a DoS attack?

Answer: To make a service unavailable to legitimate users.

### 2. How can spoofing support a DHCP-related DoS?

Answer: An attacker can send many fake DHCP requests with spoofed MAC addresses until the DHCP pool is exhausted.

### 3. Why is MITM dangerous even when traffic still works?

Answer: The attacker may silently read, capture or modify traffic while users think everything is normal.

### 4. What is reconnaissance?

Answer: Gathering information about a target before or during an attack.

### 5. Why are backdoors a major incident response concern?

Answer: They can let attackers return even after the obvious infection or compromise is cleaned up.

## What To Review Later

- TCP three-way handshake.
- DHCP starvation and rogue DHCP.
- Port scanning and service exposure.
- DDoS mitigation basics.
- Malware families.
- Incident response phases.
