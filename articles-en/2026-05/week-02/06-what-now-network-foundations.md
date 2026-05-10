# What Now?

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Network foundations wrap-up  
Tags: rfp, network design, requirements, router, switch, access point, business needs, implementation

## Summary

This lesson wraps up the foundational device and design vocabulary. Knowing what routers, switches, firewalls and wireless access points do is not just beginner trivia. It is the practical language needed to read project requirements, understand business needs and start turning them into a real network design.

Main idea: an RFP tells you the destination, but networking knowledge lets you build the road. The next step is moving from device roles and design thinking into the physical side of how everything connects.

## Key Points

- The foundational device concepts are real networking, not just warm-up material.
- Routers, switches, firewalls and access points are the glue of basic network design.
- RFP means Request for Proposal.
- An RFP usually describes outcomes and requirements, not every technical implementation detail.
- Networking knowledge helps fill in the gaps that project documents leave open.
- Business requirements translate into practical design decisions.
- A vague requirement can imply device counts, switch port needs, AP coverage and router/firewall choices.
- Network vocabulary helps decode phrases like device configuration, infrastructure requirements and coverage zones.
- Advanced topics like VLANs, trunk ports and EtherChannels matter, but they come after the basic structure is clear.
- Real clients usually ask for outcomes like reliable WiFi, secure connectivity and room for growth.
- The network engineer translates those outcomes into technical design.
- Confidence comes from knowing how to think about the problem, not from knowing everything immediately.
- The next learning step is physical connectivity: cable types, connection standards and how devices actually plug together.

## Notes

### This Is the Real Stuff

It can feel like routers, switches, firewalls and access points are only introductory definitions.

But these concepts are the foundation of real network design.

They help answer practical questions:

- What devices do we need?
- Where should they live?
- How many ports are required?
- How much wireless coverage is needed?
- What traffic stays local?
- What traffic leaves the site?
- Where should security controls live?

This is not separate from real networking. This is where real networking starts.

### From Definitions to Design

At this point, the concepts are no longer isolated definitions.

They form a design picture:

| Device/function | Role |
| --- | --- |
| Switch | Connect local wired devices |
| Access point | Extend LAN access over WiFi |
| Router | Connect the LAN to other networks/WAN |
| Firewall | Inspect and control traffic |
| Server | Provide services |
| Client | Request/consume services |
| Endpoint | Device/system using the network |

Once those roles are clear, network diagrams and project requirements become easier to understand.

### RFP

RFP means Request for Proposal.

An RFP is a document where an organization describes what it needs and asks vendors/engineers to propose a solution.

An RFP often explains:

- business goals;
- required outcomes;
- site requirements;
- reliability expectations;
- security needs;
- growth plans;
- constraints.

But it usually does not spell out every technical detail.

### Filling in the Cracks

Project documents often leave gaps.

Example RFP phrase:

```text
Understand the organization's network needs.
```

A network engineer translates that into practical questions:

- How many users?
- How many devices?
- How many wired ports?
- How many switches?
- 24-port or 48-port switches?
- How many wireless access points?
- Where should APs be placed?
- Are cameras included?
- Is guest WiFi required?
- Does the site need redundancy?
- What internet/WAN connection is needed?

That translation is the real skill.

### Business Requirements Become Design Decisions

Networking is not only memorizing device names.

Business needs affect:

- hardware choices;
- port counts;
- cabling layout;
- wireless coverage;
- internet/WAN design;
- firewall placement;
- segmentation;
- growth planning;
- physical installation.

The business says what it needs. The engineer figures out how to build it.

### Vocabulary Starts to Click

Common project phrases become clearer once you know the devices and roles.

Examples:

| Project language | Practical meaning |
| --- | --- |
| Configure network devices | Configure routers, switches, firewalls, APs |
| Infrastructure requirements | Hardware, cabling, ports, power, closets, uplinks |
| Coverage zones | Where WiFi needs to work |
| Connectivity standards | How devices connect and communicate |
| Secure connectivity | Firewall rules, segmentation, VPNs, access control |
| Room for growth | Spare ports, scalable design, expansion planning |

You do not need to know every detail yet, but you should start knowing which questions to ask.

### What Has Not Been Covered Yet

Important topics still ahead:

- VLANs;
- trunk ports;
- EtherChannels;
- deeper routing;
- wireless design;
- security policies;
- redundancy;
- addressing;
- cabling standards.

These concepts matter, especially for CCNA, but they make more sense after the basic structure is clear.

### Layering the Learning

The article emphasizes learning in layers.

First:

```text
Understand the structure, purpose and language.
```

Then:

```text
Learn the mechanisms that make it work.
```

Dumping every advanced term too early leads to memorization without understanding.

### Real-World Translation

Clients often describe outcomes, not technologies.

They may say:

- we need reliable WiFi;
- we need secure connectivity;
- we need room for growth;
- our payment systems must be protected;
- cameras must record reliably;
- staff need coverage in the back office.

They usually do not say:

- deploy VLANs;
- configure trunk ports;
- build redundant uplinks;
- use EtherChannel.

The network engineer maps business outcomes to technical implementation.

### NetworkChuck Coffee Example

Planning a new coffee shop means asking practical design questions:

- How many POS systems?
- Where will cameras go?
- Does guest WiFi need isolation?
- How many employees need back office coverage?
- What internet handoff does the provider deliver?
- How many switches are needed?
- How many APs are needed?
- What should be wired vs wireless?
- Where does the router/firewall sit?

The same thinking applies to any environment:

- coffee shop;
- castle project;
- corporate office;
- campus;
- branch location.

### Confidence in Networking

Confidence does not come from knowing everything immediately.

It comes from knowing how to think:

```text
Understand the requirement.
Identify the devices and roles.
Ask the right questions.
Translate business needs into design.
Build and test.
```

This mindset is more valuable than memorizing disconnected terms.

### Next Step: Physical Connectivity

The next logical question:

```text
How do all these devices actually connect together?
```

That leads into:

- cable types;
- copper vs fiber;
- connection standards;
- patching;
- ports;
- physical installation;
- signal limits;
- structured cabling.

Now that the major pieces are recognizable, the next step is connecting them for real.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| RFP | Request for Proposal; document describing business/project needs. |
| Requirement | Outcome or need the network must support. |
| Network design | Translating requirements into devices, topology, cabling and configuration. |
| Switch | Device that connects local wired devices. |
| Router | Device that moves traffic between networks. |
| Firewall | Device/function that enforces security rules. |
| Access point | Device that provides WiFi access to the LAN. |
| VLAN | Virtual LAN; logical network separation, covered later. |
| Trunk port | Switch port carrying multiple VLANs, covered later. |
| EtherChannel | Bundling multiple links together, covered later. |
| Coverage zone | Area where wireless service is expected. |
| Infrastructure | Physical/logical foundation that supports devices and services. |

## Questions

### 1. Why are routers, switches and access points not just beginner trivia?

Because they are the basic building blocks used to translate business requirements into a real network design.

### 2. What does RFP stand for?

Request for Proposal.

### 3. What does an RFP usually describe?

It usually describes business needs, goals and outcomes, not every implementation detail.

### 4. What does networking knowledge help you do when reading an RFP?

It helps fill in the technical gaps and turn broad requirements into practical design decisions.

### 5. What can a broad requirement like "understand network needs" imply?

User counts, device counts, switch sizes, port counts, AP coverage, cabling needs and WAN/security decisions.

### 6. Why does vocabulary matter?

Because phrases like device configuration, coverage zones and infrastructure requirements become understandable and actionable.

### 7. Are VLANs, trunk ports and EtherChannels important?

Yes, but they make more sense after the basic device roles and network structure are clear.

### 8. What do clients usually describe in real projects?

Outcomes, such as reliable WiFi, secure connectivity and room for growth.

### 9. What is the network engineer's job with those outcomes?

To translate them into a technical design and implementation.

### 10. What questions might you ask for a new coffee shop location?

How many POS systems, where cameras go, whether guest WiFi needs isolation, how many APs are needed and what internet handoff exists.

### 11. Where does confidence in networking come from?

From knowing how to think about the problem and ask the right questions, not from knowing everything immediately.

### 12. What is the next learning step after understanding device roles?

Understanding how the devices physically connect: cable types, connection standards and physical network building.

## What To Review Later

- RFP meaning.
- Business outcomes vs technical implementation.
- Translating requirements into design decisions.
- Device roles: switch, AP, router, firewall.
- Why vocabulary matters.
- Advanced topics are layered in later.
- Real clients ask for outcomes, not always specific technologies.
- Confidence comes from problem-solving approach.
- Next step: physical connectivity and cabling.
