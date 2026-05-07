# I Can HACK Your Switches (Protect Yourself with Port Security)

Source: закрытая страница курса  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 00 Lesson 14  
Tags: switch security, port security, sticky mac, black hole vlan, unused ports, dhcp, 802.1x

## Summary

Открытый Ethernet jack или active unused switch port может стать entry point в network. Если attacker device получает DHCP address, он может узнать subnet mask, default gateway, DNS и начать scanning. Базовая защита switches начинается с простых действий: shut down unused ports, помещать неиспользуемые ports в black hole VLAN и включать port security на active access ports.

Главная мысль статьи: switch port не должен быть “дверью по умолчанию”. Unused ports должны быть disabled или isolated, а active ports должны доверять только ожидаемым devices.

## Key Points

- Open Ethernet jacks are attack surface.
- Attacker device needs active port, DHCP/reachability and access to other hosts.
- Unused switch ports should be administratively shut down.
- `down` and `administratively down` are different states.
- Black hole VLAN isolates ports into a network with no DHCP, no gateway and no production access.
- Layered baseline: shut unused ports and place them in black hole VLAN.
- Port security limits which MAC addresses can use an access port.
- MAC address is Layer 2 hardware address.
- Violation actions can include shutdown, restrict or protect.
- Sticky MAC lets the switch learn and keep the first seen MAC address.
- Ports can enter error-disabled state after security violation.
- Recovery often involves fixing the issue, then `shutdown` and `no shutdown`.
- Port security is baseline security, not a replacement for 802.1X.
- 802.1X provides stronger authentication-based network access control.

## Notes

### Open Ethernet Ports Are Risk

An exposed Ethernet jack is not just a convenience. It is possible attack surface.

If someone can plug in a device and immediately join the network, they may be able to:

- receive IP settings from DHCP;
- learn subnet mask;
- learn default gateway;
- learn DNS server;
- scan local hosts;
- find open ports;
- map the network.

Practical idea:

```text
An open switch port is an invitation unless you deliberately make it useless to the wrong device.
```

### What an Attacker Device Needs

An attacker device does not need magic. It usually needs basic conditions:

| Need | Why it matters |
| --- | --- |
| Active switch port | Physical entry into network |
| DHCP or usable addressing | Gets IP configuration |
| Reachability | Can scan/access other devices |
| Production VLAN access | Lands in useful network |

If one of these assumptions breaks, the attack becomes harder.

### Shut Down Unused Ports

First baseline protection:

```text
Shut down unused ports.
```

On Cisco switch interface:

```text
shutdown
```

This makes the interface administratively down.

Difference:

| State | Meaning |
| --- | --- |
| Down | No active link right now, but port may come up if device is plugged in |
| Administratively down | Port is intentionally disabled by admin |

Unused ports should not be waiting for random devices.

### Black Hole VLAN

Sometimes real environments keep ports available because documentation, patch panels or office moves are messy.

If ports cannot all be shut down, another baseline protection is black hole VLAN.

Black hole VLAN idea:

```text
Put unused/open ports into an isolated VLAN that goes nowhere.
```

Characteristics:

- no DHCP;
- no default gateway;
- no production access;
- no useful reachability;
- isolated from real users/devices.

If someone plugs into such a port, they get nothing useful.

### Why Use Both Shutdown and Black Hole VLAN?

Layered control is better than one control.

Recommended baseline from the article:

```text
Shut unused ports down and assign them to black hole VLAN.
```

Why both?

- someone may accidentally remove shutdown;
- templates may drift;
- configs may be partially applied;
- one control may fail;
- second control still reduces risk.

### Bigger Problem: Stealing an Active Port

Securing unused ports is not enough.

An attacker could unplug a legitimate device and connect their own device to that active port.

This is where port security helps.

### Port Security

Port security lets a switch port allow only specific MAC addresses.

Example concept:

```text
Only this Raspberry Pi MAC address is allowed on this port.
```

If another MAC address appears, the switch treats it as a violation.

Port security is usually configured on access ports, which are host-facing switch ports.

### MAC Address

MAC address is Layer 2 hardware address.

Switches use MAC addresses for local delivery and can use them for port-based security decisions.

Port security says:

```text
This port should only see expected MAC address(es).
```

### Violation Actions

Port security can react to unauthorized MAC address in different ways.

Common violation modes:

| Mode | Behavior |
| --- | --- |
| protect | Drops unauthorized traffic silently |
| restrict | Drops unauthorized traffic and can log/count violation |
| shutdown | Puts port into error-disabled state |

The article prefers shutdown because it makes the attack obvious and stops the port.

### Sticky MAC

Sticky MAC lets the switch learn the first MAC address it sees and treat it as allowed.

Why it is useful:

- less manual MAC collection;
- easier deployment;
- practical for day-to-day admin;
- avoids hard-coding every MAC by hand.

Concept:

```text
The switch learns the legitimate device and sticks to it.
```

### Maximum MAC Addresses

Port security can define how many MAC addresses are allowed on one port.

Typical:

```text
maximum 1
```

But sometimes more than one MAC is legitimate.

Example:

```text
IP phone with PC connected through phone = may allow 2 MAC addresses.
```

Always match max MAC count to real device design.

### Example Cisco Port Security Flow

Typical access-port port security concept:

```text
interface FastEthernet0/1
 switchport mode access
 switchport port-security
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation shutdown
```

This means:

- interface is a host-facing access port;
- port security is enabled;
- only one MAC is allowed;
- switch learns the first MAC and sticks to it;
- unauthorized MAC triggers shutdown violation mode.

### Error-Disabled State

If port security violation occurs with shutdown mode, the port can enter error-disabled state.

Meaning:

```text
The switch disabled the port due to a security/error condition.
```

This is different from you manually shutting it down.

Common recovery flow:

1. Remove unauthorized device.
2. Reconnect legitimate device.
3. Enter interface config.
4. Use `shutdown`.
5. Use `no shutdown`.

Example:

```text
interface FastEthernet0/1
 shutdown
 no shutdown
```

### Useful Verification Commands

Useful Cisco verification commands for this topic:

```text
show port-security
show port-security interface FastEthernet0/1
show interfaces status
show interfaces FastEthernet0/1 status
show mac address-table
```

Depending on platform/version, exact output can vary.

### 802.1X

Port security is baseline switch security.

Larger environments often use 802.1X for stronger access control.

802.1X requires users or devices to authenticate before getting network access.

Comparison:

| Feature | Port Security | 802.1X |
| --- | --- | --- |
| Main control | MAC address allowed on port | Authentication before access |
| Complexity | Lower | Higher |
| Strength | Baseline | Stronger identity-based control |
| CCNA relevance | Important | Conceptually important |

Do not ignore basics just because advanced tools exist.

### Baseline Switch Security Strategy

Practical baseline:

1. Shut unused ports.
2. Put unused/open ports in black hole VLAN.
3. Avoid DHCP/gateway on black hole VLAN.
4. Configure active user ports as access ports.
5. Enable port security where appropriate.
6. Use sticky MAC for practical deployment.
7. Choose violation mode intentionally.
8. Monitor and document exceptions.
9. Consider 802.1X for stronger environments.

### Main Takeaway

An attacker needs assumptions:

- port is active;
- port lands in useful network;
- DHCP/reachability exists;
- any MAC address is accepted.

Defense removes those assumptions:

```text
Make unused ports dead.
Make available ports isolated.
Make active ports trust only expected hardware.
```

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Attack surface | Exposed area that can be abused by attacker. |
| DHCP | Service that automatically hands out IP configuration. |
| Subnet mask | Defines size/boundary of IP network. |
| Default gateway | Router address used to leave local network. |
| DNS server | Resolves names to IP addresses. |
| Administratively down | Interface disabled by admin using shutdown. |
| Black hole VLAN | Isolated VLAN with no useful connectivity. |
| VLAN | Virtual LAN, logical network separation. |
| Access port | Switch port assigned to one VLAN for endpoint devices. |
| MAC address | Layer 2 hardware address. |
| Port security | Cisco switch feature limiting MAC addresses allowed on a port. |
| Sticky MAC | Feature that learns allowed MAC address dynamically and keeps it. |
| Violation mode | Action taken when unauthorized MAC appears. |
| Protect | Drops unauthorized frames silently. |
| Restrict | Drops unauthorized frames and can log/count violations. |
| Shutdown | Error-disables port on violation. |
| Error-disabled | Switch-disabled state caused by an error/security condition. |
| 802.1X | Authentication-based network access control. |
| `shutdown` | Cisco command to administratively disable an interface. |
| `no shutdown` | Cisco command to enable an interface. |

## Questions

### 1. Why are open Ethernet jacks dangerous?

Because someone can plug in a device, receive network information, and start scanning or mapping the environment.

### 2. What basic conditions does an attacker device need?

An active port, useful network/VLAN access, IP addressing such as DHCP, and reachability to other devices.

### 3. What does `shutdown` do on a Cisco interface?

It administratively disables the interface so it will not come up even if a device is plugged in.

### 4. What is the difference between down and administratively down?

Down usually means no active link now. Administratively down means the admin intentionally disabled the port.

### 5. What is a black hole VLAN?

A black hole VLAN is an isolated VLAN with no DHCP, no gateway and no production access, used to make unused/open ports useless.

### 6. Why use both shutdown and black hole VLAN?

Because layered controls help if one control is accidentally removed or misapplied.

### 7. What problem does port security solve?

It limits which MAC addresses are allowed on an active switch port, helping prevent unauthorized devices from using that port.

### 8. What is sticky MAC?

Sticky MAC lets the switch learn the first seen MAC address and use it as an allowed secure MAC address.

### 9. Why might you allow two MAC addresses on one port?

If an IP phone is connected to the switch and a PC is connected through the phone, two legitimate MAC addresses may appear.

### 10. What violation mode does the article prefer?

Shutdown, because it stops the port and makes the security event obvious.

### 11. What is error-disabled state?

It is a state where the switch has disabled a port because of an error or security violation.

### 12. How can you commonly recover a port after a port-security shutdown violation?

Fix the cause, then enter the interface and use `shutdown` followed by `no shutdown`.

### 13. What is 802.1X?

802.1X is authentication-based network access control that requires users or devices to authenticate before network access.

### 14. Is port security the final answer for switch security?

No. It is a strong baseline, but larger environments may need stronger controls like 802.1X.

## What To Review Later

- Open ports as attack surface.
- DHCP information an attacker can learn.
- `shutdown` vs normal down state.
- Black hole VLAN.
- Port security basics.
- Sticky MAC.
- Violation modes: protect, restrict, shutdown.
- Error-disabled recovery.
- Port security vs 802.1X.
