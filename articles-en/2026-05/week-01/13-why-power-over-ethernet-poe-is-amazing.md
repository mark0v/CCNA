# Why Power over Ethernet (PoE) is Amazing!!

Source: private course page  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 01 Lesson 01  
Tags: poe, power over ethernet, pse, pd, cdp, lldp, poe budget, 802.3af, 802.3at, 802.3bt

## Summary

Power over Ethernet lets one Ethernet cable carry both data and electrical power. That makes phones, access points, cameras and other devices easier to deploy because they do not need a separate power outlet nearby.

Main idea: PoE turns network cabling into infrastructure for both connectivity and power.

## Key Points

- PoE means Power over Ethernet.
- PSE means Power Sourcing Equipment.
- PD means Powered Device.
- Switches often act as the PSE.
- Phones, APs and cameras are common PDs.
- PoE reduces the need for separate electrical work.
- PoE budget matters as much as port count.
- 802.3af provides up to 15.4 W.
- 802.3at / PoE+ provides up to 30 W.
- 802.3bt Type 3 provides up to 60 W.
- 802.3bt Type 4 provides up to 90 W.
- Active PoE negotiates power.
- Passive PoE sends power without negotiation and must be used carefully.
- Commands like `show power inline` help inspect PoE usage on Cisco switches.

## Notes

### Why PoE Matters

PoE simplifies deployment for:

- IP phones;
- wireless access points;
- security cameras;
- small switches;
- lighting systems;
- thin clients in some environments.

### Power Budget

Two questions always matter:

```text
How much power can each port deliver?
How much total power can the switch provide?
```

A switch may have PoE on many ports but not enough total wattage for every port at full draw.

### Active vs Passive PoE

Active PoE negotiates power with the connected device.

Passive PoE simply sends power. That can damage the wrong device.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| PoE | Power over Ethernet. |
| PSE | Device providing power. |
| PD | Device receiving power. |
| 802.3af | Type 1 PoE, up to 15.4 W. |
| 802.3at | PoE+, up to 30 W. |
| 802.3bt | Higher-power PoE standard. |

## Questions

### Why is PoE useful?

It provides data and power over one cable.

### Why check PoE budget?

The switch may not have enough total wattage for all connected devices.

## What To Review Later

- `show power inline`.
- LLDP/CDP power negotiation.
- PoE classes.
- Switch power budgets.
