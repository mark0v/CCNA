# Castle Rysen Coffee RFP Overview

Source: закрытая страница курса  
Date added: 2026-05-08  
Related plan item: Week 1 / Skill 02 Lesson 01  
Tags: rfp, network architecture, business requirements, resilience, segmentation, monitoring

## Summary

Эта статья вводит сценарий Castle Rysen Coffee через RFP, Request for Proposal. Вместо изучения технологий как случайных отдельных тем, RFP задает business problem: нужно спроектировать сеть для central office, fallout shelters и district coffee shops, учитывая connectivity, resilience, internet redundancy, video streaming, surveillance cameras, security, performance and monitoring.

Главная мысль статьи: хороший network design начинается не с hardware list, а с понимания business requirements, traffic types, uptime expectations и security risks.

## Key Points

- RFP means Request for Proposal.
- RFP describes a business problem and asks for a proposed solution.
- Castle Rysen Coffee scenario makes network design memorable, but requirements are realistic.
- Network design should start with business needs, not devices.
- Business structure: central office, fallout shelters and district coffee shops.
- District shops are the network edge where customers interact with the business.
- The network must be adaptable and resilient.
- Sites need unbroken connectivity between central command, shelters and coffee shops.
- Resilient internet connectivity means one ISP outage should not kill the business if redundancy is possible.
- District shops need to support local Plex-based video streaming.
- Shops have 3-5 surveillance cameras, which implies constant bandwidth and security planning.
- Security must address external and internal threats.
- Segmentation, access control and monitoring matter.
- Production networks require performance optimization and vigilant monitoring.

## Notes

### Why Start With an RFP?

An RFP, Request for Proposal, is a business saying:

```text
Here is our problem. Design a solution.
```

The Castle Rysen Coffee story is dramatic, but the RFP approach is real-world.

The goal is to give a mission before introducing random technologies.

Instead of learning:

- switches in isolation;
- routing in isolation;
- security in isolation;
- monitoring in isolation;

we learn them as parts of a network that must support a business.

### Business First, Hardware Later

Good network design starts with the business problem.

Bad approach:

```text
Start with a hardware list.
```

Better approach:

```text
Understand the business, traffic, uptime, security and operations needs.
Then choose the design and hardware.
```

A technically impressive network can still fail if it does not match the company.

### Castle Rysen Coffee Structure

The business has three major location types:

| Location type | Role |
| --- | --- |
| Central office | Big-picture control and central command |
| Fallout shelters | Administration, accounting and back-office business functions |
| District coffee shops | Customer-facing locations where sales and service happen |

This structure matters because network architecture must follow business structure.

### District Shops as the Edge

District coffee shops are the edge of the network.

They are where:

- customers buy coffee;
- staff process orders;
- customer Wi-Fi may exist;
- POS systems operate;
- cameras record;
- local services may run;
- business reputation is visible.

If these sites go down, customers feel it immediately.

### Adaptable and Impervious Infrastructure

The RFP asks for adaptable and impervious network infrastructure.

Plain English:

- adaptable = can grow and change;
- impervious/resilient = keeps working when things go wrong.

Things that can go wrong:

- devices fail;
- links fail;
- ISP circuits drop;
- users click dangerous things;
- traffic grows;
- new services appear;
- security incidents happen.

Design should expect failure, not pretend it will not happen.

### Multi-Site Connectivity

The RFP requires unbroken connectivity between:

- central command;
- fallout shelters;
- district coffee shops.

This implies:

- WAN connectivity;
- routing between sites;
- redundancy where possible;
- reliable paths to central services;
- site-to-site communication planning.

It is not enough to make one building work. The sites must operate as one business.

### Resilient Internet Connectivity

Resilient internet connectivity means:

```text
One internet outage should not automatically kill the business.
```

Possible design implications:

- dual ISP links;
- failover;
- redundant WAN paths;
- backup cellular;
- dynamic routing or SD-WAN later;
- monitoring of circuit health.

The right solution depends on budget, location and business risk.

### Plex-Based Video Streaming

Each district shop must support local Plex-based video streaming.

Plex here means local media streaming platform.

Network implications:

- video consumes bandwidth;
- local streaming may affect LAN performance;
- traffic may need segmentation;
- server/storage placement matters;
- Wi-Fi and wired capacity matter;
- QoS might matter later.

Video streaming is very different from light email/web browsing traffic.

### Surveillance Cameras

Each coffee house has 3-5 surveillance cameras.

Even if network engineer does not manage the camera application, the network must support it.

Implications:

- constant bandwidth use;
- possible PoE requirements;
- storage/NVR traffic;
- security segmentation;
- restricted access;
- monitoring;
- uptime expectations.

RFP line “support surveillance cameras” actually hides several technical requirements.

### Read Between the Lines

When reading an RFP, do not look only for explicit hardware requirements.

Look for:

- traffic types;
- uptime expectations;
- security boundaries;
- user groups;
- business dependencies;
- growth needs;
- monitoring needs;
- performance expectations.

Example:

```text
Support video surveillance
```

really means:

```text
Plan for constant bandwidth, storage paths, camera isolation and access control.
```

### Security Beyond the Firewall

The RFP mentions external marauders and internal insurrections.

Real-world translation:

- threats can come from outside;
- threats can come from inside;
- users can make mistakes;
- insiders can abuse access;
- compromised devices can spread.

Security is not just:

```text
Put a firewall at the edge.
```

Security design includes:

- segmentation;
- access control;
- monitoring;
- limiting reachability;
- separating user/device classes;
- protecting business-critical systems.

### Segmentation

Segmentation means separating parts of the network so one problem does not become everyone's problem.

Possible segments:

| Segment | Example devices |
| --- | --- |
| POS | Payment terminals |
| Guest Wi-Fi | Customer devices |
| Staff | Employee laptops/desktops |
| Cameras | Surveillance devices |
| Admin | Back-office systems |
| Media | Plex/video devices |

Segmentation is one of the main ways to reduce blast radius.

### Performance and Monitoring

The RFP also points toward:

- performance optimization;
- vigilant monitoring.

Production network mindset:

```text
Do not just build it and walk away.
```

Monitoring helps detect:

- failing links;
- bandwidth saturation;
- device health issues;
- abnormal traffic;
- security events;
- service degradation.

Performance optimization ensures the network can actually support business workloads.

### Thinking Like a Network Architect

This lesson is about mindset.

Network architect thinking includes:

- understand the business;
- identify site roles;
- classify traffic types;
- plan security boundaries;
- plan redundancy;
- consider growth;
- monitor and maintain;
- choose technology based on requirements.

The technology comes after the problem is understood.

### Main Takeaway

We are not learning networking in a vacuum.

We are solving a business problem:

```text
Build a network that keeps Castle Rysen Coffee alive and operating.
```

The RFP gives context for future topics:

- LAN/WAN;
- routing;
- switching;
- wireless;
- security;
- redundancy;
- monitoring;
- performance.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| RFP | Request for Proposal; business request for a proposed solution. |
| Central office | Main control/command location in the scenario. |
| Fallout shelter | Administrative/back-office business location in the scenario. |
| District shop | Customer-facing coffee shop location. |
| Network edge | Place where users/customers/devices interact with the network. |
| Resilience | Ability to continue operating when something fails. |
| Redundancy | Extra paths/devices/services to survive failure. |
| WAN | Wide Area Network connecting separate locations. |
| Plex | Media streaming platform used in the scenario. |
| Surveillance camera | Camera device requiring network connectivity and often constant bandwidth. |
| Segmentation | Separating network areas to reduce risk and control access. |
| Access control | Rules controlling who/what can reach resources. |
| Monitoring | Watching systems/network health, performance and events. |
| Performance optimization | Tuning/designing network to meet workload needs. |
| Business dependency | Service or function the business relies on. |

## Questions

### 1. What does RFP mean?

RFP means Request for Proposal.

### 2. Why start with an RFP instead of a hardware list?

Because network design should start with business requirements, not devices.

### 3. What are the main Castle Rysen Coffee location types?

Central office, fallout shelters and district coffee shops.

### 4. Why are district shops important in the design?

They are customer-facing edge locations where downtime directly affects service and revenue.

### 5. What does adaptable network infrastructure mean?

It means the network can grow, change and support new needs over time.

### 6. What does resilient or impervious network infrastructure mean?

It means the network can keep working when links, devices or services fail.

### 7. What does unbroken connectivity between sites imply?

It implies WAN links, routing, redundancy and reliable communication between central office, shelters and shops.

### 8. Why does Plex video streaming matter for network design?

Video streaming uses significant bandwidth and may require planning for capacity, placement and segmentation.

### 9. Why do surveillance cameras affect network design?

Cameras generate traffic, may need PoE, require storage paths and should usually be segmented for security.

### 10. Why is security more than “put in a firewall”?

Because threats can be external or internal, and design also needs segmentation, access control and monitoring.

### 11. What should you look for when reading an RFP?

Traffic types, uptime expectations, business dependencies, security needs, performance requirements and hidden implications.

### 12. What separates a production network from a hobby network?

Production networks require resilience, monitoring, performance planning, security and alignment with business operations.

## What To Review Later

- RFP as business problem statement.
- Business-first network design.
- Castle Rysen Coffee site roles.
- Edge locations and customer impact.
- WAN and resilient internet implications.
- Plex/video and camera traffic requirements.
- Security: external and internal threats.
- Segmentation, access control and monitoring.
