# Castle Rysen Coffee RFP Overview

Source: private course page  
Date added: 2026-05-08  
Related plan item: Week 1 / Skill 02 Lesson 01  
Tags: rfp, network architecture, business requirements, resilience, segmentation, monitoring

## Summary

This article introduces the Castle Rysen Coffee scenario through an RFP, Request for Proposal. Instead of learning technologies as disconnected topics, the RFP gives a business problem: design a network for a central office, fallout shelters and district coffee shops with connectivity, resilience, internet redundancy, video streaming, cameras, security, performance and monitoring.

Main idea: good network design starts with business requirements, traffic types, uptime expectations and security risks, not with a hardware list.

## Key Points

- RFP means Request for Proposal.
- An RFP describes a business problem and asks for a proposed solution.
- The scenario is fictional, but the network requirements are realistic.
- Network design should start with business needs.
- Location types include central office, fallout shelters and district coffee shops.
- District shops are the customer-facing edge of the business.
- The network must be adaptable and resilient.
- Locations need reliable connectivity to each other.
- Internet redundancy helps prevent one ISP outage from killing the business.
- Shops need local Plex-based video streaming.
- Each shop has 3-5 surveillance cameras.
- Cameras imply constant bandwidth and security planning.
- Threats can be external and internal.
- Segmentation, access control and monitoring are important.
- Production networks need performance optimization and ongoing monitoring.

## Notes

### Why Start With an RFP?

An RFP says:

```text
Here is the problem. Propose a solution.
```

It gives the mission before the technology.

### Business Structure

| Location type | Role |
| --- | --- |
| Central office | Central control and command |
| Fallout shelters | Administration, accounting and back-office functions |
| District coffee shops | Customer-facing locations |

### Requirements Hidden in the Story

The project implies:

- WAN connectivity;
- resilient internet;
- local LAN design;
- video streaming bandwidth;
- surveillance camera traffic;
- segmentation;
- monitoring;
- security policy;
- performance planning.

### Security Scope

Security is not only "block outsiders." Internal mistakes, compromised devices and malicious insiders can also create risk.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| RFP | Request for Proposal. |
| Resilience | Ability to keep working through failure. |
| Segmentation | Separating traffic/devices into controlled groups. |
| Monitoring | Watching the network for health and issues. |

## Questions

### Why start with business requirements?

Because the network exists to support the business, not to show off hardware.

### What does video surveillance imply for design?

Constant bandwidth, storage considerations and segmentation/security needs.

### Why is monitoring part of the requirement?

Because production networks must be watched after deployment.

## What To Review Later

- Reading RFPs.
- Translating requirements into design.
- WAN resilience.
- Security segmentation.
- Network monitoring.
