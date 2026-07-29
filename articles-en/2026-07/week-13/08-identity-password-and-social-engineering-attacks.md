# Identity, Password, And Social Engineering Attacks

Source: closed course page  
Date added: 2026-07-29  
Related plan item: Week 13 / Identity, password, and social engineering attacks  
Tags: identity security, password attacks, MFA, social engineering, phishing, spear phishing, whaling, smishing, vishing, AAA
Language: English
Translation pair: articles/2026-07/week-13/08-identity-password-and-social-engineering-attacks.md

## Summary

- Many attacks do not start by breaking a firewall; they start with a stolen or guessed identity.
- Admin identities are high-value targets because one valid login can open many systems.
- Passwords are still important, but passwords alone are weak.
- MFA combines at least two factors: something you know, have, or are.
- Password attacks often use stolen hashes, reconnaissance, dictionary attacks, or brute force.
- Social engineering attacks target human trust through phishing, spear phishing, whaling, smishing, vishing, and tailgating.
- This leads directly into AAA: authentication, authorization, and accounting.

## Key Points

- Attackers often prefer logging in over breaking in.
- Long, unique passwords and password managers are practical necessities.
- MFA should be enabled on admin accounts, VPNs, cloud dashboards, and network management systems.
- Spear phishing is targeted and often uses personal or organizational research.
- Whaling targets executives, senior admins, or other high-value people.
- Physical security matters because tailgating can bypass technical controls.

## Notes

Identity is one of the most valuable targets in a network.

If an attacker can use a valid account, especially an admin account, they may not need an advanced exploit. They can authenticate normally and start using legitimate tools for illegitimate goals.

At NetworkChuck Coffee, identities protect:

- network gear;
- admin portals;
- cloud dashboards;
- Wi-Fi controllers;
- POS systems;
- SaaS tools;
- VPN access;
- financial and operational systems.

Those are the keys to the business.

## Passwords Still Matter

Passwords are annoying, but they are still common.

They are an example of:

```text
something you know
```

A strong password today should be:

- long;
- unique;
- not reused;
- difficult to guess;
- stored safely;
- protected by MFA where possible.

Length matters because modern cracking tools can test huge numbers of guesses quickly, especially when attackers crack stolen password hashes offline.

Practical standard: use a password manager so every important system can have a long unique password.

## Multifactor Authentication

MFA means using at least two different factor categories.

| Factor | Meaning | Example |
| --- | --- | --- |
| Something you know | Secret in your memory | Password, PIN |
| Something you have | Physical or digital item | Authenticator app, hardware token, USB security key |
| Something you are | Biometric trait | Fingerprint, face scan, retinal scan |

Password alone is one factor.

Password plus authenticator app is two factors.

Password plus hardware security key is two factors.

MFA does not make compromise impossible, but it makes the attack much harder.

## Password Attack Methods

Most attackers are not manually typing guesses one at a time.

Common approaches:

| Method | Meaning |
| --- | --- |
| Hash cracking | Attacker steals hashed passwords and tries to crack them offline. |
| Reconnaissance | Attacker gathers personal or company information to improve guesses. |
| Dictionary attack | Tool tries wordlists and common combinations. |
| Brute force | Tool tries possible combinations systematically. |
| Credential reuse | Attacker tries a password leaked from another site. |
| Password spraying | Attacker tries a small number of common passwords across many accounts. |

Offline cracking is especially dangerous because the attacker can test guesses without triggering normal login lockouts.

## Password Managers

Unique passwords are not realistic to memorize at scale.

A password manager helps store:

- long generated passwords;
- unique credentials per system;
- secure notes;
- shared team credentials where appropriate;
- audit and rotation workflows depending on the product.

Protect the password manager itself carefully:

- strong master password;
- MFA enabled;
- recovery options secured;
- no password reuse;
- careful device security.

The password manager becomes a high-value vault.

## Social Engineering

Social engineering manipulates people instead of directly attacking technology.

The attacker may use:

- urgency;
- fear;
- authority;
- familiarity;
- curiosity;
- trust;
- fatigue;
- routine business processes.

This works because humans are part of the security system.

Firewalls and ACLs do not help if someone voluntarily gives credentials to a convincing fake login page.

## Phishing, Spear Phishing, Whaling

Phishing is a broad attack where fake messages try to trick users into clicking links, opening files, sending money, or entering credentials.

Spear phishing is targeted. The attacker researches a person or organization and makes the message believable.

Whaling is spear phishing aimed at high-value targets:

- executives;
- senior admins;
- finance staff;
- owners;
- people with authority;
- people with privileged access.

At NetworkChuck Coffee, a targeted message to a person with cloud dashboard or payment-system access could cause serious damage.

## Smishing, Vishing, Tailgating

Related social engineering types:

| Attack | Channel |
| --- | --- |
| Smishing | SMS/text messages. |
| Vishing | Voice calls. |
| Tailgating | Physical entry by following an authorized person. |

Tailgating matters because physical access can defeat many technical assumptions.

If someone gets into a wiring closet, server room, or office, they may connect rogue devices, steal hardware, access consoles, or observe sensitive information.

## Defenses

There is no single magic product for identity attacks.

Use layers:

| Defense | Why it helps |
| --- | --- |
| Long unique passwords | Reduces guessing and credential reuse risk. |
| Password manager | Makes unique passwords practical. |
| MFA | Adds a second barrier after password compromise. |
| Admin account hardening | Protects the highest-value identities. |
| Least privilege | Limits damage from one compromised account. |
| User awareness training | Helps people spot social engineering. |
| Simulated phishing | Builds recognition through practice. |
| Physical controls | Reduces tailgating and unauthorized access. |
| Logging and alerts | Helps detect suspicious login behavior. |

Admin accounts need stronger controls than regular user accounts because the blast radius is larger.

## NetworkChuck Coffee Design View

For NetworkChuck Coffee, prioritize identity security on:

- router and switch admin access;
- Wi-Fi controller;
- firewall;
- VPN;
- cloud dashboards;
- POS admin portal;
- password manager;
- finance and payroll systems;
- shared SaaS admin accounts.

Practical policy:

- MFA on all admin-capable systems;
- no shared admin passwords where avoidable;
- named accounts for accountability;
- password manager for unique credentials;
- training for phishing and social engineering;
- physical controls for network rooms;
- logging for failed and suspicious logins.

## AAA Preview

This topic leads into AAA.

AAA stands for:

| A | Meaning | Question |
| --- | --- | --- |
| Authentication | Prove identity | Who are you? |
| Authorization | Decide permissions | What are you allowed to do? |
| Accounting | Track activity | What did you do? |

Identity attacks focus heavily on authentication, but strong security needs all three.

An attacker with a valid login is bad. An attacker with excessive authorization and no accounting is worse.

## Main Takeaway

Attackers do not always break in. Often, they log in.

That means identity protection is network security.

Use long unique passwords, password managers, MFA, admin hardening, awareness training, and physical controls. Then connect that thinking to AAA so network devices can verify who users are, limit what they can do, and record what happened.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| MFA | Multifactor authentication. |
| Something you know | Password, PIN, or other memorized secret. |
| Something you have | Authenticator app, hardware token, or security key. |
| Something you are | Biometric factor. |
| Hash | One-way representation of data, often used for password storage. |
| Dictionary attack | Password attack using wordlists and combinations. |
| Brute force | Trying possible combinations until one works. |
| Social engineering | Manipulating people to bypass security. |
| Spear phishing | Targeted phishing attack. |
| Whaling | Spear phishing aimed at high-value targets. |
| Smishing | SMS phishing. |
| Vishing | Voice phishing. |
| Tailgating | Following an authorized person into a secured area. |
| AAA | Authentication, authorization, and accounting. |

## Questions

### 1. Why are identity attacks so dangerous?

Answer: A valid login can let attackers use legitimate access instead of breaking through technical defenses.

### 2. What are the three MFA factor categories?

Answer: Something you know, something you have, and something you are.

### 3. Why are password managers important?

Answer: They make long unique passwords practical across many systems.

### 4. What is spear phishing?

Answer: A targeted phishing attack that uses research to make the message believable.

### 5. What does AAA stand for?

Answer: Authentication, authorization, and accounting.

## What To Review Later

- MFA methods.
- Password manager security.
- Password spraying vs brute force.
- Phishing and spear phishing indicators.
- Physical security controls.
- Cisco AAA concepts.
