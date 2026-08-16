# Secure Cisco Remote Access With SSH

Source: closed course page  
Date added: 2026-08-16  
Related plan item: Week 15 / Secure Cisco remote access with SSH  
Tags: SSH, Telnet, remote access, VTY, RSA keys, login local, transport input ssh, Cisco IOS, management security
Language: English
Translation pair: articles/2026-08/week-15/06-secure-cisco-remote-access-with-ssh.md

## Summary

- Telnet is dangerous because it sends logins, passwords, and commands in clear text.
- The risk becomes serious when an attacker can capture traffic or perform a man-in-the-middle attack.
- SSH encrypts the management session and should be standard on Cisco devices.
- SSH requires a hostname, domain name, local user, and RSA keys.
- `login local` makes VTY lines use the local user database.
- `transport input ssh` closes Telnet and allows SSH only.
- The configuration must be tested: Telnet should fail and SSH should work.

## Key Points

- "Telnet is insecure" is true, but the reason matters.
- Telnet does not become safe just because it is hard to capture in one specific network.
- Security audits usually expect SSH-only management access.
- SSH requires cryptographic identity, so setup takes several steps.
- RSA keys depend on hostname and domain name.
- If the hostname changes after key generation, keys may need to be regenerated.
- A shared line password is weaker than username/password in the local database.

## Notes

Telnet is often described with one sentence: "it is insecure." That is true, but incomplete.

The problem is not that the whole internet automatically sees your password. The problem is that Telnet sends data in clear text. If someone can capture traffic between the admin workstation and the Cisco device, they can see login information and commands.

Main idea:

```text
Telnet is dangerous because it does not encrypt management traffic.
```

In a modern network, that is not acceptable as a standard practice.

## Why Telnet Is Bad

Telnet sends the following in readable form:

- username;
- password;
- commands;
- command output;
- device prompts.

An attacker needs a way to see the traffic:

- packet capture on your device;
- access to the same segment;
- compromised switch or SPAN;
- man-in-the-middle;
- control over part of the network path.

If that access exists, the Telnet session is readable.

Even if the network has DHCP Snooping, Dynamic ARP Inspection, and other Layer 2 protections, that does not make Telnet acceptable. Those protections reduce specific risks, but Telnet itself still does not encrypt the session.

## Why SSH Wins

SSH, or Secure Shell, encrypts the remote management session.

When an administrator enters a password or command, the traffic is not readable text on the wire. To a packet sniffer, it looks like encrypted data.

But SSH is not a one-command "make secure" switch.

It needs:

- device identity;
- hostname;
- domain name;
- cryptographic keys;
- user credentials;
- VTY line configuration;
- allowed transport protocol.

That is why SSH setup is more involved than Telnet.

## Setup Order

Typical order:

1. Create a local username and secret.
2. Make sure hostname is configured.
3. Configure an IP domain name.
4. Generate RSA keys.
5. Enable SSH version 2.
6. Configure VTY lines for `login local`.
7. Restrict remote access with `transport input ssh`.
8. Verify that Telnet is closed and SSH works.

Order matters. RSA keys are built around device identity. If hostname and domain name are wrong, keys may need to be regenerated.

## Basic Configuration

Example:

```text
configure terminal

hostname R1
ip domain-name cafe.local

username admin secret StrongPasswordHere

crypto key generate rsa modulus 2048
ip ssh version 2

line vty 0 4
 login local
 transport input ssh
end
```

Breakdown:

| Command | Function |
| --- | --- |
| `hostname R1` | Sets the device name. |
| `ip domain-name cafe.local` | Sets the domain name for key generation. |
| `username admin secret ...` | Creates a local user with a protected secret. |
| `crypto key generate rsa modulus 2048` | Creates RSA keys for SSH. |
| `ip ssh version 2` | Enables SSHv2. |
| `login local` | Uses the local user database on VTY lines. |
| `transport input ssh` | Allows only SSH for inbound VTY access. |

## RSA Keys And Device Identity

SSH uses a public/private key pair.

On a Cisco device, RSA keys are created with:

```text
crypto key generate rsa modulus 2048
```

These keys are tied to device identity, where hostname and domain name matter.

Bad order:

```text
crypto key generate rsa
hostname RealName
ip domain-name cafe.local
```

After that change, keys may need to be regenerated.

Better order:

```text
hostname R1
ip domain-name cafe.local
```

Then generate keys.

## VTY Lines And Login Local

VTY lines are virtual terminal lines used for remote access.

Older or simple lab Telnet configurations often use a line password:

```text
line vty 0 4
 password cisco
 login
```

That is a shared password on the line. Everyone uses the same password and no username is required.

For SSH, use:

```text
username admin secret StrongPasswordHere

line vty 0 4
 login local
```

`login local` means the device checks the local user database. The connection prompts for username and password.

That is already a better security model than one shared line password.

For large networks, local users are still not ideal. AAA, centralized authentication, and accounting usually come next. For CCNA and small labs, local users are the right starting point.

## The Command That Closes Telnet

Key command:

```text
transport input ssh
```

It is configured under VTY lines:

```text
line vty 0 4
 transport input ssh
```

If you configure SSH but leave Telnet allowed, the job is not finished. You added the secure option, but did not remove the insecure one.

`transport input ssh` means:

```text
Accept only SSH for remote access.
```

After that, Telnet should close or be refused, while SSH should succeed.

## Verification

Useful commands:

```text
show ip ssh
show running-config | section line vty
show running-config | include username|ip domain-name|hostname
show crypto key mypubkey rsa
```

Client-side checks:

```text
telnet 192.168.10.1
ssh -l admin 192.168.10.1
```

Confirm:

- SSH version 2 is enabled;
- RSA keys exist;
- local username exists;
- VTY lines use `login local`;
- VTY lines allow only `transport input ssh`;
- Telnet no longer works;
- SSH accepts username/password.

## NetworkChuck Coffee Scenario

At NetworkChuck Coffee, routers and switches keep the cafe network alive.

Admin traffic should not cross the network in clear text. If someone can capture a management session, they should not get the password and commands in readable form.

Minimum policy:

- Telnet disabled;
- SSH version 2 enabled;
- local admin user with secret;
- RSA keys generated with adequate modulus;
- VTY restricted to SSH;
- management access documented;
- later, centralized AAA.

That moves remote management from merely convenient to basically protected.

## Practical Notes

SSH is the standard, but not the only control.

Also consider:

- management VLAN;
- access-class on VTY;
- strong secrets;
- AAA;
- logging;
- role-based access;
- disabling unused services;
- secure out-of-band access;
- documentation.

But the first step is simple: do not leave Telnet open.

## Main Takeaway

Telnet provides remote management, but it does so in clear text. That is unacceptable for a modern network.

SSH encrypts the management session, but it needs the right foundation: hostname, domain name, RSA keys, local user, `login local`, and `transport input ssh`.

The goal is not merely to "enable SSH." The goal is to close Telnet and verify the result. Only then does remote management move from "access exists" to "access is protected."

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Telnet | Old remote access protocol without encryption. |
| SSH | Secure Shell, encrypted remote access. |
| clear text | Data readable without decryption. |
| VTY lines | Virtual terminal lines for remote connections. |
| `username ... secret` | Creates a local user with protected secret. |
| `ip domain-name` | Domain name required for SSH key generation. |
| `crypto key generate rsa` | Creates RSA keys. |
| `ip ssh version 2` | Enables SSH version 2. |
| `login local` | Uses local user database for login. |
| `transport input ssh` | Allows only SSH on VTY lines. |
| AAA | Authentication, Authorization, Accounting. |

## Questions

### 1. Why is Telnet insecure?

Answer: It sends login information and commands in clear text.

### 2. What makes SSH better than Telnet?

Answer: SSH encrypts the remote management session.

### 3. Why are hostname and domain name needed before RSA keys?

Answer: They are part of the device identity used for SSH key generation.

### 4. What does `login local` do?

Answer: It makes VTY lines check username/password against the local user database.

### 5. Which command closes Telnet on VTY lines?

Answer: `transport input ssh`.

## What To Review Later

- Full SSH configuration order.
- Difference between line password and `login local`.
- `crypto key generate rsa modulus 2048`.
- `ip ssh version 2`.
- `transport input ssh`.
- Testing Telnet failure and SSH success.
