# What Now? Cabling

Source: closed course page  
Date added: 2026-05-16  
Related plan item: Week 3 / Cabling next steps  
Tags: cabling, structured cabling, copper, fiber, network design, troubleshooting, infrastructure
Language: English
Translation pair: articles/2026-05/week-03/01-what-now-cabling.md

## Summary

Cabling knowledge matters for every networking professional, but that does not always mean the network engineer is the person physically pulling cable through ceilings, walls and patch panels. At the CCNA level, you need to understand cable types, copper categories, fiber, connectors, speed limits and distance limits because those details shape real design and troubleshooting decisions.

Main idea: your job is often not to install every cable yourself. Your job is to know which cable should be used, why it makes sense and where the wrong choice can break the project.

## Key Points

- Cabling knowledge is required for network design and troubleshooting.
- Physical cable installation is often a separate job.
- Network engineers must understand cable types, speed limits, distance limits and connector types.
- Structured cabling is a real specialized skill, not a "lower" version of networking.
- In larger environments, installers often work from a plan created by engineers or designers.
- Engineers must know when copper is enough and when fiber is required.
- Good cabling knowledge helps communicate with installers and validate project scope.
- NetworkChuck Coffee examples show why media choices affect cost, uptime and deployment quality.
- Cabling can become its own career path.
- Starting in cabling can lead naturally into switching, routing, wireless and network engineering.
- You do not need to be the person terminating every run to be a legitimate network professional.

## Notes

### Knowing Cabling vs. Doing Cabling

After learning about cables, the natural question is: what do I do with this knowledge?

The answer is slightly counterintuitive: you need to understand cabling well, but in real networking jobs the network engineer is not always the person physically installing every cable.

There are two related but different layers:

- knowing which cable type should be used;
- physically installing that cable cleanly and correctly in a building.

They are connected skills, but they are not always the same role.

### What a Network Engineer Should Understand

When you design or assess a network, you need to understand:

- whether the project uses Cat5e, Cat6, Cat6a or fiber;
- what speed the selected medium supports;
- which distance limits matter;
- which connectors and transceivers are involved;
- where copper is enough and where fiber makes more sense;
- how the cable infrastructure affects the topology.

This is not exam trivia. It is the foundation for decisions that affect money, timelines and uptime.

### NetworkChuck Coffee Example

Imagine a NetworkChuck Coffee project where the scope says to:

- assess the existing network infrastructure;
- identify weak points;
- design a new topology;
- connect and configure network devices.

For that kind of project, cabling knowledge is required.

If the register area connects back to the switch closet, you need to know whether a copper run is enough. If different parts of the building or separate wiring closets need to be connected, copper may no longer fit the distance requirement and fiber may be the better answer.

Choosing the wrong medium can cause:

- extra cost;
- rework;
- project delays;
- downtime during business hours.

### Why the Installer and Engineer Are Often Different People

In larger projects, the person pulling cable may not be responsible for the network design. They often work from a plan:

```text
Install Cat6 here.
Terminate it there.
Label it this way.
Patch it into this panel.
```

The installer owns the physical work: clean runs, labeling, termination, pathways, safety and building requirements.

The engineer owns making sure the plan itself is technically correct.

### Structured Cabling Is Its Own Specialty

Proper cable installation is not just "pulling a wire."

It involves:

- ceiling tiles;
- conduits;
- cable trays;
- j-hooks;
- patch panels;
- labeling;
- bend radius;
- safety issues;
- building codes;
- testing and certifying links.

It is physical, detailed and important work. People who do it well deserve real respect.

### How to Be Useful in a Project

A network engineer often needs to be able to say:

```text
No, we cannot use that cable here.
Yes, this medium supports the required speed.
We need fiber between these closets because copper will not handle that distance.
This port, panel and cable label do not match the plan.
```

So the value is not only in doing the physical work. The value is also in making correct decisions.

Sometimes your job is not to install the thing. Your job is to know whether the installed thing makes sense.

### Can Cabling Be a Career?

Yes. Structured cabling can be a full career.

It is not a fallback path and it is not a lesser version of networking. It is a practical specialty where skilled people can build a strong career.

Cabling can also be an excellent entry point into networking:

```text
Structured cabling -> switching -> routing -> wireless -> network engineering
```

That path gives you a strong bottom-up understanding of the network: from floor tiles and patch panels to the CLI.

### Practical Takeaway

At this stage, you should know cabling well enough to:

- design with confidence;
- choose the right transmission medium;
- understand copper and fiber limits;
- speak intelligently with installers;
- verify whether the installation matches the plan;
- start troubleshooting at the physical layer, not only in the config.

You do not need to feel like a fake network engineer just because you are not terminating every cable run by hand.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Cabling | The physical cable infrastructure of a network: copper, fiber, connectors, patch panels and pathways. |
| Structured cabling | An organized building cabling system with rules for pathways, labeling and termination. |
| Copper | A metallic transmission medium, usually twisted-pair Ethernet cable in this context. |
| Fiber | Optical transmission medium, useful for longer distances, high speeds and some uplink scenarios. |
| Cat5e | A copper cable category often seen in older or smaller networks. |
| Cat6 | A common copper cable category used for many modern Ethernet runs. |
| Distance limit | The maximum useful cable length before speed, signal or standard limitations matter. |
| Connector | The physical end used to attach a cable to a device, jack or panel. |
| Patch panel | A panel where permanent cable runs terminate and connect to equipment through patch cables. |
| Termination | Correctly attaching cable conductors to a connector, jack or patch panel. |
| Installer | Specialist who physically runs, labels and terminates cable links. |
| Network engineer | Specialist who designs, configures, validates and troubleshoots network infrastructure. |
| Physical layer | OSI Layer 1: cables, signals, connectors and physical interfaces. |

## Questions

### 1. Does a network engineer need to know cabling?

Yes. Even if they do not install every cable, cabling knowledge is needed for design, troubleshooting and working with installers.

### 2. Does knowing cabling mean the engineer always pulls the cable?

No. Physical installation is often handled by structured cabling specialists.

### 3. Which cabling details are especially important at the CCNA level?

Cable categories, speed limits, distance limits, connector types, copper vs. fiber and the role of the physical layer.

### 4. Why is structured cabling its own specialty?

Because it has its own tools, standards, safety concerns, building constraints, labeling, pathways, patch panels and termination quality requirements.

### 5. What should an engineer be able to decide when choosing media?

Whether the selected cable type supports the required speed, distance and topology, or whether a different medium such as fiber is needed.

### 6. When can fiber be better than copper?

When the project needs longer distance, high-speed uplinks, links between closets or any scenario where copper does not meet the requirement.

### 7. Why is the wrong cable medium risky for the business?

It can cause rework, delays, extra cost and downtime.

### 8. Can cabling be its own career?

Yes. Structured cabling is a valuable and complete specialty.

### 9. Why can cabling experience help a future network engineer?

It builds physical infrastructure knowledge that helps later with switching, routing, wireless and troubleshooting.

### 10. What is the main takeaway from this lesson?

Know cabling well enough to make correct decisions, even when another specialist performs the physical installation.

## What To Review Later

- Copper vs. fiber.
- Cat5e, Cat6 and Cat6a basics.
- Speed and distance limits.
- Connector types.
- Patch panels and termination.
- Physical layer troubleshooting.
- Difference between installer and network engineer roles.
- Cabling as a possible career path.
