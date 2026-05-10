# Do Not Design Your Network Like This

Source: private course page  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 00 Lesson 06  
Tags: network design, topology, flat network, segmentation, redundancy, reliability

## Summary

Bad network design often starts with convenience: plug everything into whatever is nearby and hope it works. That may be fine for a tiny lab, but it becomes risky in a real business. Good design requires structure, segmentation, planning and room for growth.

Main idea: a working network is not automatically a well-designed network.

## Key Points

- Randomly connecting devices creates fragile networks.
- Flat networks are easy at first but risky as they grow.
- Business networks need planning.
- Critical systems should not be mixed casually with guest or untrusted devices.
- Segmentation limits blast radius.
- Redundancy helps reduce single points of failure.
- Documentation matters.
- Design choices should follow business needs.

## Notes

### Working vs Designed

A network can pass traffic and still be poorly designed.

Warning signs:

- unlabeled cables;
- random unmanaged switches;
- no diagram;
- no segmentation;
- no security boundaries;
- no plan for growth;
- no redundancy for critical paths.

### Flat Network Problem

In a flat network, many different device types share the same space:

- guest laptops;
- POS systems;
- cameras;
- employee devices;
- servers;
- IoT devices.

If one weak device is compromised, the attacker may have too much reach.

### Better Mindset

Start with:

- what the business needs;
- what devices exist;
- what traffic matters;
- what must be protected;
- what must keep working during failure.

Then design the network.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Flat network | A network with little or no segmentation. |
| Segmentation | Separating devices or traffic into controlled groups. |
| Redundancy | Backup paths or systems for resilience. |
| Single point of failure | One component whose failure breaks service. |

## Questions

### Can a bad design still work?

Yes, but it may be hard to secure, scale and troubleshoot.

### Why is segmentation useful?

It limits what devices can reach and reduces the impact of compromise.

## What To Review Later

- VLANs.
- Network diagrams.
- Redundant uplinks.
- Guest network isolation.
