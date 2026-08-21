# Wireless Security Fundamentals

Source: closed course page  
Date added: 2026-08-21  
Related plan item: Week 17 / Wireless security fundamentals  
Tags: wireless security, Wi-Fi, WEP, WPA, WPA2, WPA3, PSK, 802.1X, EAP, RADIUS, encryption, authentication
Language: English
Translation pair: articles/2026-08/week-17/05-wireless-security-fundamentals.md

## Summary

- Wireless security matters because signal extends beyond walls.
- In a wired network, an attacker often needs physical access. With Wi-Fi, attacks can happen from a nearby parking lot.
- Wireless security protects one layer: communication between the client and access point.
- Two things matter: encryption and authentication.
- `WEP` is obsolete and insecure.
- `WPA` was a transitional improvement after `WEP`.
- `WPA2` became the mature standard and is still widely used.
- `WPA3` improves protection and addresses weaknesses in `WPA2`.
- `PSK` fits homes and small networks.
- `802.1X/EAP` fits business environments, staff turnover, and multiple locations.

## Key Points

- Wi-Fi is not safe just because it is "inside the building."
- Radio signal does not respect walls, doors, or office boundaries.
- Encryption protects data from being read if intercepted.
- Authentication decides who is allowed to connect.
- A shared password is convenient, but scales poorly.
- Identity-based access lets you disable one user instead of changing the password for the whole network.
- Wireless security does not replace segmentation, firewalls, MFA, permissions, or proper network policy.

## Notes

Wireless security is often underestimated.

In a wired network, an attacker usually needs access to something physical:

- cable;
- wall jack;
- switch port;
- building;
- equipment room.

With Wi-Fi, we transmit access into the air.

Even when access points are placed carefully, signal may leak:

- into a hallway;
- into a parking lot;
- into a neighboring office;
- outside;
- into an adjacent space.

That is why wireless security is not optional.

## Why Wireless Is More Exposed

Signal does not stop perfectly at the wall.

You can tune power levels, place APs correctly, and design coverage well, but fully hiding radio signal inside a building is usually unrealistic.

Practical picture:

```text
Employee sits inside.
Access point transmits inside.
Signal leaks outside.
Someone in a nearby car may also hear it.
```

That does not mean Wi-Fi is automatically insecure. It means it must be protected intentionally.

## Wireless Security Is One Layer

Wireless security does not solve all network security.

It protects one specific segment:

```text
Client <-> Access Point
```

Other layers still matter:

- accounts;
- permissions;
- MFA;
- network segmentation;
- firewall policies;
- device posture;
- logging;
- monitoring;
- guest isolation;
- VLAN design.

Do not think of wireless security as the only defense. It is one layer in the overall model.

## Two Main Ideas

Wireless security keeps coming back to two words:

- encryption;
- authentication.

## Encryption

`Encryption` means data is scrambled.

If someone intercepts traffic in the air, they should not be able to read the contents.

Simplified:

```text
Even if you hear the signal, you should not understand the data.
```

Without proper encryption, Wi-Fi becomes a convenient observation point for anyone nearby.

## Authentication

`Authentication` answers a different question:

```text
Are you allowed to connect?
```

That may involve:

- shared Wi-Fi password;
- username/password;
- certificate;
- account in an identity system;
- RADIUS verification;
- another EAP method.

Encryption protects content. Authentication controls entry.

You need both.

## Open Networks

If a Wi-Fi network does not show a lock icon and does not require a password at the wireless layer, it is usually an open network.

Sometimes a captive portal appears after connection:

- hotel login page;
- airport portal;
- coffee shop terms page.

But remember:

```text
A captive portal is not the same as full wireless encryption.
```

It may control internet access, but the wireless layer may still be open.

## Security Evolution

Wireless security evolved through these steps:

```text
WEP -> WPA -> WPA2 -> WPA3
```

Each step addressed problems in the previous one.

## Obsolete WEP

`WEP`, or `Wired Equivalent Privacy`, was an early attempt to protect Wi-Fi.

The name sounded confident, as if wireless could be about as secure as plugging in with a cable.

In practice, `WEP` was weak.

It could be broken, and that became a serious problem as Wi-Fi adoption grew. Today, `WEP` should not be used in normal networks.

Practical rule:

```text
If you see WEP, it is a security finding.
```

## Transitional WPA

`WPA`, or `Wi-Fi Protected Access`, appeared as a quick response to `WEP` weaknesses.

It was a step forward.

It improved protection and allowed many devices to become safer without replacing all hardware immediately.

But `WPA` was more of a transitional solution than the final destination.

## Mature WPA2

`WPA2` was a major improvement.

It introduced stronger protection, especially through `AES`.

`AES` is a strong encryption algorithm used far beyond Wi-Fi.

`WPA2` was the main standard for years and is still seen almost everywhere.

Important:

```text
WPA2 did not become garbage just because WPA3 exists.
```

In real networks, `WPA2` is still often acceptable and strong when configured correctly.

## Modern WPA3

`WPA3` appeared to improve protection and address weaknesses in `WPA2`.

Improvements around handshake behavior and protection against some weak-password attacks are especially important.

`WPA3` is the right direction for new hardware and new deployments.

But compatibility matters:

- do clients support WPA3;
- do APs support WPA3;
- are old devices still present;
- is mixed mode needed;
- how does onboarding change.

## Pre-Shared Key

`PSK`, or `pre-shared key`, is the familiar Wi-Fi password.

Idea:

```text
There is one shared secret.
Whoever knows it can connect.
```

For homes or small offices, this is often fine.

Benefits:

- easy to configure;
- users understand it;
- no RADIUS required;
- no complex identity infrastructure.

The downsides appear at scale.

## The Shared Password Problem

A shared password scales poorly.

Imagine:

- 50 employees;
- tablets;
- printers;
- cameras;
- IoT devices;
- multiple locations;
- staff turnover.

If one employee leaves and the password must change, pain begins:

- devices drop from Wi-Fi;
- printers stop working;
- tablets need reconfiguration;
- IoT devices break;
- helpdesk gets flooded;
- every location needs updates.

One shared password is convenient while the environment is small and stable.

## 802.1X And EAP

Larger environments often use `802.1X` with `EAP`.

`EAP`, or `Extensible Authentication Protocol`, is a framework for different authentication methods.

Idea:

```text
Not one password for everyone.
Each user or device authenticates individually.
```

Authentication may use:

- RADIUS server;
- Active Directory;
- Microsoft 365;
- certificate authority;
- identity provider;
- another backend identity system.

If an employee leaves, their account is disabled. The whole wireless network password does not need to change.

## EAP Methods

`EAP` is not one single method.

It is a framework with different methods:

- username/password;
- certificates;
- tunneled authentication;
- combinations of credentials and certificates.

You do not need to memorize every option at this stage.

The principle matters:

```text
802.1X/EAP provides individual verification instead of one shared password.
```

## NetworkChuck Coffee Scenario

If NetworkChuck Coffee is one small shop with a few trusted devices, strong `WPA2-PSK` or `WPA3-PSK` may be fine.

But if the business grows:

- multiple shops;
- guest Wi-Fi;
- staff Wi-Fi;
- POS devices;
- printers;
- tablets;
- cameras;
- employees come and go;
- internal resources are reachable from staff network.

Then a shared password becomes a problem.

It is better to consider identity-based access:

```text
Disable one user.
Do not break the whole wireless network.
```

That matters when staff turnover is normal and device count grows.

## Guest Wi-Fi

Guest Wi-Fi should be separated from the internal network.

Even if guests receive internet access, they should not see:

- cameras;
- printers;
- POS systems;
- staff laptops;
- management interfaces;
- internal servers.

Wireless security is not only a password. It is also segmentation.

Practical idea:

```text
Guest traffic belongs in a separate network.
```

## Practical Tip

For home or tiny office:

- use `WPA2` or `WPA3`;
- configure a strong PSK;
- do not use `WEP`;
- separate guest and private networks.

For business:

- evaluate `802.1X/EAP`;
- use RADIUS or an identity system;
- separate guest traffic;
- plan for staff turnover;
- document recovery;
- verify client compatibility with `WPA3`.

## Main Takeaway

Wireless security matters because Wi-Fi sends access through the air, not through a controlled cable.

You need to protect both entry into the network and data in the radio medium. Authentication decides who can connect. Encryption protects traffic from being read.

`WEP` is obsolete. `WPA` was a transition. `WPA2` became the mature and widely used standard. `WPA3` improves protection for modern networks.

For small environments, a strong PSK can be enough. For a growing business, `802.1X/EAP` is usually a better direction because it manages access by user or device instead of one shared password.

## Commands And Terms

| Term | Meaning |
| --- | --- |
| wireless security | Protection for wireless access and data transmission. |
| encryption | Scrambling data so it cannot be read if intercepted. |
| authentication | Checking whether a client is allowed to connect. |
| open network | Wi-Fi network without a wireless password at connection. |
| captive portal | Web authorization page after joining a network. |
| `WEP` | Wired Equivalent Privacy, obsolete and weak protection. |
| `WPA` | Wi-Fi Protected Access, transitional method after `WEP`. |
| `WPA2` | Mature wireless security standard with strong encryption. |
| `WPA3` | More modern standard with improved protection. |
| `AES` | Encryption algorithm used in strong security designs. |
| `PSK` | Pre-shared key, shared Wi-Fi password. |
| `802.1X` | Standard for port-based/network access authentication. |
| `EAP` | Extensible Authentication Protocol, framework for authentication methods. |
| `RADIUS` | Server protocol for centralized authentication. |

## Questions

### 1. Why does wireless security matter so much?

Answer: Because Wi-Fi signal extends beyond the physical boundary of the building and may be reachable from outside.

### 2. How is encryption different from authentication?

Answer: Encryption protects data from being read, while authentication checks who is allowed to connect.

### 3. Why should WEP not be used?

Answer: `WEP` is weak and has long been considered insecure.

### 4. When is PSK acceptable?

Answer: In a home network or small office with few trusted users and devices.

### 5. Why is 802.1X/EAP better for business?

Answer: It can authenticate each user or device individually and disable access without changing one shared Wi-Fi password.

## Review Later

- Why wireless is more exposed than wired.
- The difference between encryption and authentication.
- The evolution from `WEP -> WPA -> WPA2 -> WPA3`.
- Where `PSK` fits.
- Why `802.1X`, `EAP`, and `RADIUS` matter.
- Why guest Wi-Fi should be separated from the internal network.
