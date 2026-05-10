# Data Center Networks: What Do They Look Like?

Source: private course page  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 00 Lesson 07  
Tags: data center, servers, switches, redundancy, uplinks, architecture

## Summary

A data center network is built to connect large numbers of servers, storage systems and services with high speed and high reliability. It looks different from a small office network because scale, redundancy, cooling, power and traffic volume all become much more serious.

Main idea: data centers are not just rooms full of servers. They are carefully designed network environments built for performance and availability.

## Key Points

- Data centers host servers, applications, storage and network services.
- Reliability is a major design goal.
- Redundant power, links and devices are common.
- Switches connect servers and aggregate traffic.
- Uplinks carry traffic between layers of the design.
- Data center traffic can be east-west and north-south.
- High-speed fiber is common for uplinks and server connections.
- Good design reduces single points of failure.

## Notes

### Why Data Centers Matter

Many services users rely on live in data centers:

- websites;
- applications;
- databases;
- media platforms;
- cloud services;
- enterprise systems.

When the data center network fails, many services fail with it.

### Traffic Patterns

Two useful directions:

```text
North-south = traffic entering or leaving the data center
East-west   = traffic between systems inside the data center
```

Modern applications often generate a lot of east-west traffic because services talk to other services.

### Redundancy

Data center designs avoid relying on one cable, one switch or one power source where possible. Redundancy is not just extra hardware; it must be designed and configured correctly.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Data center | Facility that hosts computing and network infrastructure. |
| Uplink | Higher-speed connection carrying aggregated traffic. |
| North-south traffic | Traffic entering or leaving the data center. |
| East-west traffic | Traffic inside the data center. |

## Questions

### Why are data center networks different from small office networks?

They handle more traffic, more systems and higher availability requirements.

### Why is redundancy important?

It helps services continue when a device, link or power source fails.

## What To Review Later

- Spine-leaf architecture.
- Server uplinks.
- Storage networking.
- High availability.
