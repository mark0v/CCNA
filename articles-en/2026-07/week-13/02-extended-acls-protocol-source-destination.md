# Extended ACLs: Protocol, Source, Destination

Source: closed course page  
Date added: 2026-07-29  
Related plan item: Week 13 / Extended ACLs protocol, source, and destination  
Tags: ACL, extended ACL, protocol, source, destination, TCP, UDP, ICMP, ports, wildcard mask
Language: English
Translation pair: articles/2026-07/week-13/02-extended-acls-protocol-source-destination.md

## Summary

- Extended ACLs look complex, but each line is built around three decisions: protocol, source, and destination.
- Extended ACLs can match not only source, but also destination, protocol, and port.
- TCP, UDP, ICMP, and IP are the core protocol choices to recognize.
- Port numbers usually belong on the destination side when clients access services.
- ACLs process top-down; first match wins.
- Extended ACLs are usually placed as close to the source as possible.

## Key Points

- Standard ACLs match source only; extended ACLs are more precise.
- `ip` in an ACL means all IP-based traffic, including TCP, UDP, and ICMP.
- `icmp` can match ping and other control/status messages.
- `tcp` and `udp` allow application-level matching by port.
- Common service ports matter for both exams and real troubleshooting.
- A typo or misplaced port can make an ACL look right while doing the wrong thing.

## Notes

Extended ACLs are powerful because they can describe traffic much more precisely than standard ACLs.

The trick is to stop reading the command as one giant wall of syntax.

Use this mental model:

```text
protocol + source + destination
```

Then, when needed, add service details such as TCP or UDP port numbers.

## The Three Decisions

Every extended ACL entry answers three core questions.

| Decision | Question |
| --- | --- |
| Protocol | What kind of traffic is this? |
| Source | Where is the traffic coming from? |
| Destination | Where is the traffic going? |

Example logic:

```text
deny icmp host 10.0.18.2 any
```

Read it as:

```text
Deny ICMP from host 10.0.18.2 to any destination.
```

That does not block web, DNS, SSH, or every protocol from that host. It blocks ICMP traffic from that host.

## Protocol Choices

Common protocol choices:

| Protocol | Meaning |
| --- | --- |
| `tcp` | Reliable transport used by many applications. |
| `udp` | Lightweight transport used by DNS, voice, video, and many real-time apps. |
| `icmp` | Control and status traffic, including ping. |
| `ip` | All IP-based traffic. |

The `ip` keyword is broad.

Example:

```text
permit ip any any
```

This permits all IP traffic that reaches that line. It is often used after a specific deny so the ACL does not accidentally block everything through implicit deny.

## Source And Destination

After protocol, define source and destination.

A source or destination can be:

- one host;
- a subnet with wildcard mask;
- `any`.

Examples:

```text
deny icmp host 10.0.18.2 any
permit icmp host 10.0.18.2 host 10.0.20.10
deny tcp 10.0.18.0 0.0.0.255 host 10.0.30.10 eq 80
```

Read each ACL line as a sentence. If the sentence sounds wrong, the ACL is probably wrong.

## Order Still Matters

ACLs process top-down, first match wins.

Example:

```text
permit icmp host 10.0.18.2 host 10.0.20.10
deny icmp host 10.0.18.2 any
permit ip any any
```

This allows one host to ping one specific destination, blocks that same host from pinging everything else, and permits other IP traffic.

If the deny line comes first, the specific permit below it never gets checked for that traffic.

That is why sequence numbers and named ACLs are useful. They help you edit the ACL without rebuilding the whole list.

## Ports And Applications

Extended ACLs can match TCP or UDP ports.

Common ports:

| Application | Protocol / port |
| --- | --- |
| HTTP | TCP 80 |
| HTTPS | TCP 443 |
| FTP | TCP 21 |
| Telnet | TCP 23 |
| SSH | TCP 22 |
| SMTP | TCP 25 |
| POP3 | TCP 110 |
| IMAP | TCP 143 |
| DNS | UDP 53 |
| Ping | ICMP echo |

This matters because exams and real configs may describe the application, while the router expects protocol and port logic.

## The Port Placement Gotcha

When a client accesses a web server, port `80` is usually the destination port.

The client uses a temporary source port. The server listens on TCP 80.

Correct concept:

```text
permit tcp host 10.0.18.2 host 10.0.30.10 eq 80
```

Read it as:

```text
Permit TCP from client 10.0.18.2 to server 10.0.30.10 on destination port 80.
```

Wrong mental model:

```text
The client source port is 80.
```

Usually it is not.

Misplacing a port number can create a rule that is syntactically valid but logically wrong.

## Extended ACL Placement

Extended ACLs are usually placed as close to the source as possible.

Reason: extended ACLs are specific. They can match source, destination, protocol, and port, so unwanted traffic can be stopped early without accidentally blocking unrelated destinations.

This differs from standard ACLs:

| ACL type | Placement rule |
| --- | --- |
| Standard ACL | Close to destination. |
| Extended ACL | Close to source. |

Standard ACLs are blunt because they know only source. Extended ACLs are precise, so placing them near the source avoids wasting bandwidth and processing deeper in the network.

## NetworkChuck Coffee Design View

For NetworkChuck Coffee, extended ACLs can express business rules more precisely.

Examples:

- one office PC cannot ping anything;
- one host can ping only a troubleshooting server;
- guest Wi-Fi cannot browse an internal web server;
- staff VLAN can reach HTTPS on a server but not SSH;
- POS terminals can reach payment services on specific ports.

This is why extended ACLs are more powerful than standard ACLs. They let the network policy describe not just who is sending traffic, but what they are trying to reach and how.

## Troubleshooting Habit

When checking an extended ACL:

1. Read the line out loud.
2. Confirm protocol.
3. Confirm source.
4. Confirm destination.
5. Confirm whether the port belongs to source or destination.
6. Check line order.
7. Remember implicit deny.

This catches many common mistakes quickly.

## Main Takeaway

Extended ACLs are not one big scary command. They are deliberate choices:

```text
What protocol?
From what source?
To what destination?
Which port or message type, if needed?
```

They are powerful because they are precise. They are dangerous because precision leaves less room for typos, wrong order, and wrong port placement.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Extended ACL | ACL that can match source, destination, protocol, and ports. |
| `tcp` | Matches TCP traffic. |
| `udp` | Matches UDP traffic. |
| `icmp` | Matches ICMP traffic, including ping. |
| `ip` | Matches all IP-based traffic. |
| `host` | Matches one specific IP address. |
| `any` | Matches any source or destination. |
| `eq 80` | Matches exact port 80. |
| First match wins | ACL processing stops at the first matching line. |

## Questions

### 1. What are the three core parts of an extended ACL entry?

Answer: Protocol, source, and destination.

### 2. What does `permit ip any any` mean?

Answer: Permit all IP-based traffic that reaches that ACL line.

### 3. Why does order matter in extended ACLs?

Answer: ACLs process top-down and stop at the first match.

### 4. When a client accesses HTTP on a server, where does port 80 usually belong?

Answer: On the destination side, because the server listens on TCP port 80.

### 5. Where should extended ACLs usually be placed?

Answer: As close to the source as possible.

## What To Review Later

- Extended ACL syntax.
- TCP vs UDP vs ICMP.
- Common port numbers.
- Source vs destination port placement.
- Named ACL sequence numbers.
- Standard vs extended ACL placement.
