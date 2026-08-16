# Core Services Deployment Baseline

Source: closed course page  
Date added: 2026-08-16  
Related plan item: Week 15 / Core services deployment baseline  
Tags: core services, NTP, DHCP, DNS, SSH, baseline configuration, deployment template, operations
Language: English
Translation pair: articles/2026-08/week-15/08-core-services-deployment-baseline.md

## Summary

- NTP, DHCP, DNS, and SSH should be part of a basic deployment checklist.
- These services are not extras; they are the foundation of normal network device operations.
- NTP provides consistent time.
- DHCP automates IP settings where the design calls for it.
- DNS makes names usable for people and applications.
- SSH provides secure remote management.
- The goal is not memorizing four acronyms, but building them into the configuration standard.

## Key Points

- If a lesson does not change how you build devices, the knowledge remains trivia.
- Every new device should be treated as part of a system that depends on core services.
- A baseline template reduces the chance of forgetting important "boring" settings.
- Core services should be verified during deployment, not after the first outage.
- Environments differ, but the basic service list repeats constantly.
- A good standard makes the network manageable, predictable, and supportable.

## Notes

Many lessons end with the feeling of "I watched it, so I know it." For network operations, that is not enough.

The real result appears when knowledge becomes a standard:

```text
Every device receives a baseline set of core services.
```

A switch, router, or firewall is not just a hostname and IP address. It is a device that should live in a managed environment with correct time, names, addressing, and secure access.

## Core Four

For NetworkChuck Coffee, the baseline set is:

| Service | Why it matters |
| --- | --- |
| NTP | Synchronizes time for logs, troubleshooting, and security events. |
| DHCP | Provides IP settings where the design requires automatic addressing. |
| DNS | Turns names into IP addresses and makes the network easier to use. |
| SSH | Provides secure remote access for device management. |

SSH can feel like a separate security topic, but in practice it belongs in the baseline. Remote management without SSH looks outdated and risky in a modern network.

## Why These Are Not Small Details

A router can route without DNS. A switch can switch without NTP. A device can be reachable without SSH.

That does not make it a proper production network.

Without core services:

- logs cannot be reliably correlated by time;
- new clients do not receive settings;
- apps and internal resources fail by name;
- administrators use insecure protocols;
- troubleshooting slows down;
- deployment depends on one engineer's memory.

Common does not mean unimportant. Often, the common pieces are the foundation.

## Template Instead Of Memory

Do not rely on "I will remember later."

You need a base configuration template:

- for routers;
- for switches;
- for firewalls;
- for lab devices;
- for branch sites;
- for cafe locations.

The template should answer:

- where the device gets time;
- which DNS server it uses;
- whether DHCP server, client, or relay is needed;
- whether SSH is enabled;
- whether Telnet is disabled;
- which verification commands should be run;
- which exceptions are allowed.

That turns deployment from improvisation into a repeatable process.

## Minimal Checklist

Basic thought process:

1. Configure hostname and management identity.
2. Configure NTP or define NTP servers.
3. Configure DNS with `ip name-server` and local mappings if needed.
4. Configure DHCP if the device participates as server, client, or relay.
5. Configure SSH.
6. Restrict VTY lines with `transport input ssh`.
7. Verify services with show commands.
8. Save the configuration.
9. Update documentation.

This does not replace full design. It is a baseline that prevents forgotten basics.

## Example Baseline Snippets

NTP:

```text
ntp server 10.255.0.1
show ntp status
show clock detail
```

DNS:

```text
ip name-server 10.1.0.53
ip domain-name cafe.local
show hosts
```

DHCP:

```text
ip dhcp excluded-address 192.168.10.1 192.168.10.20
ip dhcp pool CAFE-VLAN10
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 10.1.0.53
show ip dhcp binding
```

SSH:

```text
username admin secret StrongPasswordHere
crypto key generate rsa modulus 2048
ip ssh version 2
line vty 0 4
 login local
 transport input ssh
show ip ssh
```

These snippets must be adapted to the specific network. Their value is that they remind you the baseline should be complete, not random.

## NetworkChuck Coffee Scenario

NetworkChuck Coffee opens a new location.

If the new switch receives only basic config, it may pass traffic. But future support will be weak:

- logs without correct time;
- no name resolution;
- unclear DHCP role;
- insecure or incomplete remote access;
- no single deployment standard.

If the baseline is applied:

- the device synchronizes time;
- uses the correct DNS;
- participates in DHCP design where needed;
- is reachable by SSH;
- is verified with show commands;
- is added to documentation.

That is the difference between "it turned on" and "it can be supported."

## Engineer Habit

An experienced engineer does not begin with fancy features.

They check the foundation first:

- clock;
- reachability;
- name resolution;
- address assignment;
- secure management;
- logging;
- documentation.

That creates traction in a new environment. Not because the engineer knows every command in the world, but because they know which things almost always matter.

## Verification

Commands:

```text
show clock detail
show ntp status
show ntp associations
show hosts
show running-config | include ip name-server
show ip dhcp pool
show ip dhcp binding
show ip ssh
show running-config | section line vty
```

Confirm:

- time source is correct;
- NTP is synchronized;
- DNS server is configured;
- name resolution works;
- DHCP role is understood;
- DHCP bindings appear if the device is a server;
- SSH is enabled;
- Telnet is closed;
- configuration is saved;
- documentation is updated.

## Main Takeaway

Core services are not optional decoration.

NTP, DHCP, DNS, and SSH make network devices operationally sane: time aligns, addresses are assigned, names work, and remote management is protected.

If these services are built into the deployment template, the network becomes predictable. If they depend on memory and mood, they will be forgotten at the worst possible time.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| core services | Basic services required for normal network operations. |
| NTP | Time synchronization. |
| DHCP | Automatic IP setting assignment. |
| DNS | Name resolution. |
| SSH | Secure remote management. |
| baseline template | Basic repeatable configuration template. |
| `transport input ssh` | Restricts VTY remote access to SSH only. |
| `ip name-server` | Defines a DNS server for a Cisco device. |
| `ntp server` | Defines an NTP server. |
| `ip helper-address` | DHCP relay command. |

## Questions

### 1. Which four core services should be remembered?

Answer: NTP, DHCP, DNS, and SSH.

### 2. Why does SSH belong in the baseline, not only the security section?

Answer: Almost every managed device should have secure remote access from the beginning.

### 3. Why is a template better than memory?

Answer: A template makes deployment repeatable and reduces the risk of forgetting basics.

### 4. What separates "the device turned on" from "the device can be supported"?

Answer: Time sync, DNS, clear DHCP role, secure remote access, verification, and documentation.

### 5. Why verify core services immediately?

Answer: If they are broken or forgotten, future troubleshooting becomes slower and more expensive.

## What To Review Later

- Baseline templates for routers and switches.
- NTP verification.
- DNS verification.
- DHCP roles: server, client, relay.
- SSH setup and `transport input ssh`.
- Documenting core services for each site.
