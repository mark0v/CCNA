# Why Power over Ethernet (PoE) is Amazing!!

Source: закрытая страница курса  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 00 Lesson 12  
Tags: poe, power over ethernet, 802.3af, 802.3at, 802.3bt, pse, pd, power budget

## Summary

Power over Ethernet, или PoE, позволяет одному Ethernet cable передавать и data, и electrical power. Это упрощает deployment IP phones, wireless access points, security cameras и других devices, потому что не нужно отдельно тянуть power outlet к каждому месту установки.

Главная мысль статьи: PoE - это не просто удобство. Это infrastructure feature, которая влияет на planning, switch selection, power budget, reliability и troubleshooting.

## Key Points

- PoE carries data and power over one Ethernet cable.
- PoE стал особенно важным из-за IP phones, wireless access points и cameras.
- PSE means Power Sourcing Equipment, usually PoE switch.
- PD means Powered Device, such as phone, AP or camera.
- PoE упрощает installation and relocation devices.
- Важно проверять not only “does switch support PoE”, but total PoE budget.
- 802.3af = Type 1 PoE = up to 15.4 W per port.
- 802.3at = Type 2 PoE+ = up to 30 W per port.
- 802.3bt = Type 3 up to 60 W and Type 4 up to 90 W.
- Newer PoE standards are generally backward compatible.
- Active PoE negotiates power before sending it.
- Passive PoE sends power without negotiation and can damage wrong devices.
- CDP and LLDP can help devices negotiate/report power needs.
- `show power inline` helps inspect PoE usage on Cisco switches.
- Switches have per-port power limits and total shared PoE budget.

## Notes

### Why PoE Feels Like Magic

Before PoE, deploying some network devices often required two things:

- network cable;
- electrical power.

That meant more installation work, more coordination and often a need for both network cabling and electrical work.

PoE solves this by sending data and power over the same Ethernet cable.

Common PoE devices:

- IP phones;
- wireless access points;
- security cameras;
- small switches;
- lighting systems;
- thin clients;
- some building systems.

### Why PoE Is Useful

PoE is useful because it makes deployment:

- easier;
- cheaper;
- faster;
- cleaner;
- more flexible.

Example for NetworkChuck Coffee:

- phones at the front counter;
- cameras near registers;
- wireless access points across the shop;
- devices moved when coverage or layout changes.

If an access point needs to move, PoE can make the job much simpler. Move the cable/drop and device, without needing a new electrical outlet in the ceiling.

### PSE and PD

PoE has two important roles:

| Term | Meaning |
| --- | --- |
| PSE | Power Sourcing Equipment; provides power, usually a PoE switch. |
| PD | Powered Device; receives power, such as phone, camera or AP. |

In a typical deployment:

```text
PoE switch (PSE) -> Ethernet cable -> IP phone/AP/camera (PD)
```

The switch provides both network connectivity and power.

### PoE Budget

One of the most important real-world PoE planning points is power budget.

Do not ask only:

```text
Does this switch support PoE?
```

Also ask:

```text
How much total PoE budget does this switch have?
How much power can each port deliver?
```

A switch may support PoE on every port but still not have enough total wattage to power every connected device at full draw.

Example problem:

```text
Switch has enough ports, but not enough watts.
```

Result: some phones/APs/cameras may power up, while others do not.

### PoE Standards

PoE standards matter for exams and product specs.

| Standard | Common name | Type | Max power per port |
| --- | --- | --- | --- |
| 802.3af | PoE | Type 1 | 15.4 W |
| 802.3at | PoE+ | Type 2 | 30 W |
| 802.3bt | PoE++ / UPOE-like standardized high power | Type 3 | 60 W |
| 802.3bt | PoE++ | Type 4 | 90 W |

PoE started with lower-power devices like phones. Higher-power standards enabled larger access points, small switches, lighting, thin clients and other devices.

### Cisco Inline Power and UPOE

Before standardized PoE became common, Cisco had Cisco Inline Power for early IP telephony deployments.

Cisco also pushed higher-power PoE with UPOE before the industry standardized high-power PoE through 802.3bt.

For CCNA, focus on the standard names and wattages, but remember that vendor-specific history explains why some older terms still appear.

### Backward Compatibility

PoE standards are generally backward compatible.

That means a newer PoE switch can usually support older PoE devices.

Example:

```text
802.3bt-capable switch can usually power 802.3af/at devices.
```

This matters because real environments often contain mixed old and new devices.

### Active PoE

Active PoE is the safer/smarter version.

Before sending power, PSE and PD negotiate:

- is the device PoE-capable?
- how much power does it need?
- what class or budget should be assigned?

Protocols that can help:

- CDP, Cisco Discovery Protocol;
- LLDP, Link Layer Discovery Protocol.

Simple idea:

```text
Active PoE asks before sending power.
```

### Passive PoE

Passive PoE sends power without negotiation.

This can be dangerous because the port may deliver power even if the connected device does not expect it.

Risk:

```text
Wrong passive PoE connection can damage equipment.
```

Passive PoE exists and may be required by some legacy or specific devices, but it should be used intentionally and carefully.

### Active vs Passive PoE

| Feature | Active PoE | Passive PoE |
| --- | --- | --- |
| Negotiates power | Yes | No |
| Safer for mixed devices | Yes | No |
| Standards-based behavior | Usually | Not always |
| Risk if wrong device connected | Lower | Higher |
| Typical use | Enterprise switches/devices | Some legacy/special gear |

### Checking PoE on Cisco Switches

Useful Cisco command from the article:

```text
show power inline
```

This command helps check:

- total available PoE power;
- used power;
- remaining power;
- per-port device draw;
- whether devices are powered;
- PoE state per interface.

This is an operational command, not just exam trivia.

### Per-Port Limit vs Total Budget

There are two different power questions:

1. How much power can each port deliver?
2. How much total power does the switch have to share?

Example:

| Limit type | Meaning |
| --- | --- |
| Per-port limit | Maximum wattage one interface can provide |
| Total PoE budget | Total wattage available across switch ports |

Both matter.

If a device tries to draw more power than allowed, the switch may shut the port down or place it into an error-disabled state to protect hardware.

### Why PoE Matters Beyond the Exam

PoE turns network infrastructure into physical business infrastructure.

It supports:

- phones;
- cameras;
- access points;
- lights;
- small switches;
- endpoint devices.

At NetworkChuck Coffee, PoE can directly affect:

- payment areas;
- wireless coverage;
- security camera placement;
- phone deployment;
- clean cabling;
- uptime and troubleshooting.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| PoE | Power over Ethernet; data and power over one Ethernet cable. |
| PSE | Power Sourcing Equipment; device providing PoE power. |
| PD | Powered Device; device receiving PoE power. |
| 802.3af | Type 1 PoE, up to 15.4 W per port. |
| 802.3at | Type 2 PoE+, up to 30 W per port. |
| 802.3bt | High-power PoE standard, Type 3 up to 60 W and Type 4 up to 90 W. |
| PoE+ | Common name for 802.3at. |
| UPOE | Cisco higher-power PoE technology before/alongside standardized high-power PoE. |
| Active PoE | PoE that negotiates power before delivery. |
| Passive PoE | PoE that sends power without negotiation. |
| CDP | Cisco Discovery Protocol. |
| LLDP | Link Layer Discovery Protocol. |
| PoE budget | Total power available from a switch for PoE devices. |
| `show power inline` | Cisco command for viewing PoE power state and usage. |
| Error-disabled | Switch port state after a protection-triggering error condition. |

## Questions

### 1. What does PoE do?

PoE sends data and electrical power over the same Ethernet cable.

### 2. Why is PoE useful for devices like IP phones, APs and cameras?

Because those devices need both network connectivity and power. PoE removes the need for a separate local power outlet.

### 3. What is PSE?

PSE means Power Sourcing Equipment. It provides power, usually a PoE switch.

### 4. What is PD?

PD means Powered Device. It receives PoE power, such as IP phone, wireless AP or camera.

### 5. Why is PoE budget important?

A switch may support PoE on many ports but not have enough total wattage to power every connected device at full draw.

### 6. What standard is Type 1 PoE and how much power does it provide?

802.3af, up to 15.4 W per port.

### 7. What standard is PoE+ and how much power does it provide?

802.3at, Type 2, up to 30 W per port.

### 8. What standard provides Type 3 and Type 4 PoE?

802.3bt provides Type 3 up to 60 W and Type 4 up to 90 W.

### 9. What is the difference between active PoE and passive PoE?

Active PoE negotiates power before delivery. Passive PoE sends power without negotiation.

### 10. Why can passive PoE be dangerous?

Because it may send power to a device that does not expect it, potentially damaging the device.

### 11. Which protocols can help with PoE negotiation or device discovery?

CDP and LLDP.

### 12. What Cisco command helps inspect PoE power usage?

`show power inline`.

### 13. What two power questions should you ask when selecting a PoE switch?

How much power can each port deliver, and how much total PoE budget does the switch have?

### 14. What can happen if a device draws more power than the interface allows?

The switch can shut the port down or place it into an error-disabled state.

## What To Review Later

- PoE use cases: phones, APs, cameras.
- PSE vs PD.
- PoE standards and wattages: 802.3af, 802.3at, 802.3bt.
- Active PoE vs passive PoE.
- CDP and LLDP in power negotiation/discovery.
- Per-port power vs total PoE budget.
- `show power inline`.
