# I Can HACK Your Switches (Protect Yourself with Port Security)

Source: private course page  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 01 Lesson 03  
Tags: switch security, port security, mac address, sticky mac, vlan, black hole vlan, shutdown, 802.1x

## Summary

An open Ethernet jack is an attack surface. If someone can plug in a device, get an IP address and scan the network, the switch port has become a doorway into the environment. Port security, disabled unused ports and isolated unused VLANs reduce that risk.

Main idea: do not leave switch ports useful to the wrong device.

## Key Points

- Open Ethernet ports can be abused.
- An attacker device can use DHCP to learn network details.
- Unused ports should be administratively shut down.
- `Down` and `administratively down` are different states.
- A black hole VLAN isolates unused ports from production.
- Black hole VLANs should have no DHCP, gateway or production access.
- Port security limits which MAC addresses may use a port.
- Sticky MAC lets the switch learn and remember allowed MAC addresses.
- Violation actions include protect, restrict and shutdown.
- Shutdown violation mode can place the port into err-disabled state.
- Recovery often requires `shutdown` and `no shutdown` after fixing the issue.
- 802.1X provides stronger identity-based access control.

## Notes

### Attacker Requirements

An attacker needs:

```text
Active port
Network access
DHCP or usable addressing
Reachability to internal devices
```

Break any of those assumptions and the attack becomes harder.

### Baseline Protection

Good baseline:

- shut unused ports;
- place unused ports in a black hole VLAN;
- disable DHCP/gateway for that VLAN;
- use port security on active access ports;
- document active ports.

### Port Security

Port security lets a switch port accept only expected MAC addresses.

Sticky MAC is practical because the switch learns the first valid device instead of requiring manual MAC entry everywhere.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Port security | Switch feature limiting allowed MAC addresses. |
| Sticky MAC | Learned MAC address saved for port security. |
| Black hole VLAN | Isolated VLAN with no useful access. |
| Err-disabled | Switch port disabled because of a violation or error. |
| 802.1X | Authentication-based network access control. |

## Questions

### Why shut down unused ports?

So someone cannot plug in and immediately join the network.

### Why use a black hole VLAN too?

It adds another layer if a port is accidentally enabled later.

### What does sticky MAC do?

It lets the switch learn the allowed MAC address automatically.

## What To Review Later

- Cisco port security commands.
- Violation modes.
- Err-disable recovery.
- 802.1X.
- NAC design.
