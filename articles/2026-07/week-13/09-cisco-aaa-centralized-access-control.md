# Cisco AAA: Centralized Access Control

Source: закрытая страница курса  
Date added: 2026-07-29  
Related plan item: Week 13 / Cisco AAA centralized access control  
Tags: AAA, Cisco, authentication, authorization, accounting, RADIUS, TACACS+, 802.1X, EAP, WPA2-Enterprise
Language: Russian
Translation pair: articles-en/2026-07/week-13/09-cisco-aaa-centralized-access-control.md

## Summary

- AAA is not just about passwords; it is about identity and access control at scale.
- AAA means Authentication, Authorization and Accounting.
- Local usernames on every network device work only in tiny environments.
- Centralized AAA lets routers, switches and access points check a shared identity source.
- RADIUS and TACACS+ are the major protocols used with AAA systems.
- AAA also supports user network access through technologies like 802.1X and EAP.

## Key Points

- Authentication asks: who are you?
- Authorization asks: what are you allowed to do?
- Accounting asks: what did you do?
- Central identity improves speed and control during employee changes or emergency lockouts.
- RADIUS is broad and common across many environments.
- TACACS+ is strongly associated with Cisco device administration.
- WPA2-Enterprise uses AAA-style user authentication instead of one shared Wi-Fi password.

## Notes

AAA matters because real networks have scale.

One router with one local admin account is simple.

Dozens of routers, switches, firewalls, wireless controllers and access points with separate local accounts is operational debt. Password changes become painful. Former employee access becomes risky. Audit trails become inconsistent.

AAA gives network devices a central way to validate users, enforce permissions and track activity.

## What AAA Means

AAA stands for:

| A | Meaning | Question |
| --- | --- | --- |
| Authentication | Proving identity | Who are you? |
| Authorization | Deciding permissions | What can you do? |
| Accounting | Recording activity | What did you do? |

These three jobs work together.

Authentication alone is not enough. Knowing who someone is does not mean they should be allowed to do everything.

Authorization limits what authenticated users can do.

Accounting creates records so activity can be reviewed later.

## Why Local Logins Do Not Scale

Local accounts can work in a tiny lab:

```text
username admin secret ...
```

But in a real environment, local-only accounts create problems:

- every device must be updated separately;
- password rotation is slow;
- offboarding is error-prone;
- shared accounts destroy accountability;
- permissions are hard to standardize;
- logs are fragmented;
- emergency lockout takes too long.

At NetworkChuck Coffee, if one admin leaves the company, access should be removed quickly everywhere.

With local-only accounts, someone has to touch every device.

With centralized AAA, disable the central account and every integrated device stops trusting that login.

## Centralized Authentication

With centralized AAA, a network device does not need to make every identity decision alone.

Login flow concept:

1. Admin connects to router or switch.
2. Device asks for credentials.
3. Device sends authentication request to AAA server.
4. AAA server checks identity source.
5. AAA server replies accept or reject.
6. Device allows or denies access.

The identity source could be:

- Active Directory;
- LDAP directory;
- Linux identity system;
- cloud identity platform;
- dedicated AAA server;
- integrated enterprise identity service.

AAA is an architecture, not only one specific Cisco box.

## Authorization

Authorization decides what an authenticated user can do.

Examples:

- read-only access;
- full administrator access;
- limited command set;
- network operator role;
- wireless user access;
- guest access;
- admin access only from trusted groups.

This matters because not every valid user should have equal power.

If a help desk account only needs read-only troubleshooting access, it should not have full configuration authority.

## Accounting

Accounting records activity.

Examples:

- who logged in;
- when they logged in;
- whether login succeeded or failed;
- what commands were run;
- when the session ended;
- which device was accessed.

Accounting gives accountability.

Without accounting, an organization may know that a device changed, but not who changed it or when.

For incident response and change review, that evidence matters.

## RADIUS And TACACS+

Two major protocols appear in AAA conversations.

| Protocol | Practical role |
| --- | --- |
| RADIUS | Broad industry standard, common for network access and many authentication scenarios. |
| TACACS+ | Cisco-associated protocol often used for device administration and command authorization. |

Both help network devices talk to a central access system.

For now, understand the role:

```text
The device asks the AAA system about identity, permissions and records.
RADIUS or TACACS+ carries that conversation.
```

The deeper protocol details can come later.

## AAA Beyond Admin Logins

AAA is not only for administrators logging into routers.

The same identity model applies to user network access, especially wireless and switchport authentication.

Important terms:

| Term | Meaning |
| --- | --- |
| 802.1X | Port-based network access control. |
| EAP | Extensible Authentication Protocol, framework used in authentication methods. |
| WPA2-Enterprise | Wi-Fi security mode using per-user or per-device authentication. |
| Pre-shared key | One shared Wi-Fi password for many users. |

Pre-shared keys are simple, but they do not scale well.

If one employee leaves and still knows the shared Wi-Fi password, changing it means updating many devices.

With enterprise authentication, each user has their own identity. Disable that user, and access is removed without changing the password for everyone else.

## NetworkChuck Coffee Design View

As NetworkChuck Coffee grows, AAA becomes more important.

Systems that should tie into centralized identity:

- routers;
- switches;
- firewalls;
- wireless controllers;
- access points;
- VPN;
- cloud admin portals;
- monitoring tools;
- Wi-Fi access;
- management systems.

Business benefits:

- faster offboarding;
- easier password policy enforcement;
- better audit trails;
- role-based access;
- fewer shared secrets;
- less manual cleanup;
- stronger accountability.

AAA turns identity into infrastructure policy instead of scattered device-by-device configuration.

## Local Fallback

Centralized AAA is powerful, but the design still needs a fallback plan.

If the AAA server is unreachable, engineers may still need emergency access.

Common design idea:

- prefer centralized AAA;
- keep limited local break-glass account;
- secure local fallback strongly;
- monitor its use;
- document when it may be used.

Fallback access should be controlled, not forgotten.

## Main Takeaway

Cisco AAA is the framework for centralized identity, permissions and activity tracking.

It answers:

```text
Who are you?
What are you allowed to do?
What did you do?
```

That matters for router and switch administration, employee offboarding, wireless access, VPNs and audit trails.

AAA is how network access stops being a pile of local passwords and becomes a managed security system.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| AAA | Authentication, authorization and accounting. |
| Authentication | Proving identity. |
| Authorization | Deciding what an identity can do. |
| Accounting | Recording what happened. |
| RADIUS | Common AAA protocol used widely across network access systems. |
| TACACS+ | Cisco-associated AAA protocol often used for device administration. |
| 802.1X | Port-based network access control. |
| EAP | Extensible Authentication Protocol. |
| WPA2-Enterprise | Wi-Fi mode using per-user/per-device authentication. |
| Pre-shared key | One shared password used by multiple clients. |
| Active Directory | Microsoft directory service commonly used as an identity source. |

## Questions

### 1. What does AAA stand for?

Answer: Authentication, authorization and accounting.

### 2. Why do local logins fail at scale?

Answer: They require device-by-device management, making password changes, offboarding and auditing slow and error-prone.

### 3. What does authentication answer?

Answer: Who are you?

### 4. What does authorization answer?

Answer: What are you allowed to do?

### 5. Why is WPA2-Enterprise better than one shared Wi-Fi password in a growing business?

Answer: Each user can authenticate with their own identity, so access can be removed per user without changing a shared password everywhere.

## What To Review Later

- Cisco AAA configuration flow.
- RADIUS vs TACACS+ differences.
- 802.1X roles and terminology.
- EAP methods.
- AAA fallback design.
- Accounting logs and command authorization.
