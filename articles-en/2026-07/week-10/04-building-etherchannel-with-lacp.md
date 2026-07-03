# Building EtherChannel With LACP

Source: closed course page  
Date added: 2026-07-03  
Related plan item: Week 10 / Building EtherChannel with LACP  
Tags: EtherChannel, LACP, PAgP, port-channel, channel-group, STP, trunk
Language: English
Translation pair: articles/2026-07/week-10/04-building-etherchannel-with-lacp.md

## Summary

- EtherChannel turns multiple physical links into one logical Port-Channel.
- A bundle can be built three ways: static, PAgP, or LACP.
- In real networks, LACP is usually preferred because it is a standards-based negotiated protocol.
- After the bundle is created, future Layer 2 settings should be applied to the Port-Channel interface.

## Key Points

- Static EtherChannel performs no negotiation and is riskier when configuration mistakes exist.
- PAgP works, but it is Cisco proprietary.
- LACP is the industry standard, so it fits Cisco, non-Cisco switches, servers, and access points.
- For LACP, `active` + `active` or `active` + `passive` forms a channel; `passive` + `passive` does not.
- Verify the result with `show etherchannel summary` and `show spanning-tree`.

## Notes

EtherChannel matters for more than "more links." It matters because without it, STP may block one of the parallel switch-to-switch links. Physically, we have two cables. Logically, only one is forwarding. That is safe for Layer 2, but inefficient for bandwidth utilization.

EtherChannel changes the picture: several physical interfaces become one logical link. STP no longer sees two competing paths between the same switches. It sees one Port-Channel interface and makes decisions based on that.

There are three ways to build EtherChannel:

| Method | What it does | Practical use |
| --- | --- | --- |
| Static | Forces ports into a bundle with no negotiation. | Avoid in production unless there is a strong reason. |
| PAgP | Cisco-proprietary negotiation protocol. | Useful to know for Cisco-only environments and the exam. |
| LACP | Standards-based negotiation protocol. | Usually the best choice in real networks. |

Static mode looks simple: both sides are manually configured as a bundle. That simplicity is the risk. If one side is different or the wrong ports are selected, negotiation will not stop the mistake. In the worst case, you can create a loop or unstable behavior.

PAgP was created by Cisco and works in Cisco environments. Its modes are:

| PAgP mode | Behavior |
| --- | --- |
| `auto` | Passively waits for the other side to start negotiation. |
| `desirable` | Actively tries to form an EtherChannel. |

`auto` + `auto` does not form a channel because both sides are waiting. `desirable` + `auto` and `desirable` + `desirable` work.

LACP is the more universal option. It is a standards-based protocol used between different vendors and device types. Its modes are:

| LACP mode | Behavior |
| --- | --- |
| `passive` | Waits for LACP negotiation from the other side. |
| `active` | Actively sends LACP packets and tries to form a channel. |

`passive` + `passive` does not form an EtherChannel. `active` + `passive` works. `active` + `active` works too. In practice, using `active` on both sides is simple and explicit.

The key command for creating EtherChannel is `channel-group`. It is usually applied to an interface range because member ports must be configured consistently:

```text
Switch(config)# interface range fa0/1 - 2
Switch(config-if-range)# channel-group 1 mode active
```

After that, the switch creates a logical interface:

```text
Switch(config)# interface port-channel 1
```

This is the important shift. After the bundle is created, think in terms of the Port-Channel, not the individual physical interfaces. If you need to configure trunking, allowed VLANs, or Layer 2 settings, do it on `interface port-channel 1`, not randomly on one physical member port.

Example:

```text
Switch(config)# interface port-channel 1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20,30,40
```

Member ports must match. Check at least:

- speed;
- duplex;
- access or trunk mode;
- allowed VLAN list;
- native VLAN;
- LACP/PAgP/static mode;
- Layer 2 settings that affect the bundle.

If one member port differs, it may be removed from the bundle or placed in a suspended state. Future changes should be made on the Port-Channel interface so the member links do not drift apart.

After configuration, do not trust the config blindly. Verify it:

```text
Switch# show etherchannel summary
Switch# show spanning-tree
```

`show etherchannel summary` shows the group number, Port-Channel, Layer 2/Layer 3 state, and the physical ports actually participating in the bundle. `show spanning-tree` confirms that STP sees the Port-Channel as one logical path instead of several separate links.

In production, configure EtherChannel during a maintenance window when possible. Ports may flap while the bundle forms. That is technically normal, but users will still notice if POS terminals or Wi-Fi drop during business hours.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `channel-group 1 mode active` | Adds interfaces to EtherChannel group 1 using LACP active mode. |
| `interface port-channel 1` | Enters the logical interface that represents the bundle. |
| `show etherchannel summary` | Quickly checks EtherChannel state and member ports. |
| `show spanning-tree` | Checks how STP sees the Port-Channel. |
| `active` | LACP mode that actively tries to form a channel. |
| `passive` | LACP mode that waits for negotiation from the other side. |
| `desirable` | PAgP mode that actively tries to form a channel. |
| `auto` | PAgP mode that passively waits for negotiation. |

## Questions

### 1. Why is LACP usually preferred over static EtherChannel?

Answer: LACP performs negotiation and helps prevent a bundle from forming when settings do not match. Static mode simply assumes both sides are configured correctly.

### 2. Which LACP mode combinations form a channel?

Answer: `active` + `active` and `active` + `passive` form a channel. `passive` + `passive` does not because both sides are waiting.

### 3. Where should trunk settings be configured after EtherChannel is created?

Answer: On the `interface port-channel`, because it represents the whole bundle. Changing only one physical member port can create a mismatch.

### 4. Why is `show etherchannel summary` useful?

Answer: It shows whether the Port-Channel is up, whether it is operating as a Layer 2 or Layer 3 interface, and which physical ports are actually part of the bundle.

## What To Review Later

- The difference between static, PAgP, and LACP.
- LACP modes `active` and `passive`.
- PAgP modes `desirable` and `auto`.
- How to read flags in `show etherchannel summary`.
- Why member port settings must match.
