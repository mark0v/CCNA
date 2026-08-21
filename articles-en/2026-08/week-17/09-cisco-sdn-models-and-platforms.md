# Cisco SDN Models And Platforms

Source: closed course page  
Date added: 2026-08-21  
Related plan item: Week 17 / Cisco SDN models and platforms  
Tags: SDN, Cisco, SD-Access, SD-WAN, ACI, Catalyst Center, DNAC, APIC, VXLAN, API  
Language: English  
Translation pair: articles/2026-08/week-17/09-cisco-sdn-models-and-platforms.md

## Summary

- Cisco SDN has many names, but it is easier to separate them into models and platforms.
- `API` is the doorway a controller uses to interact with a device or system.
- `SD-Access` applies to the campus network: buildings, branches, switches, and access points.
- `SD-WAN` applies to the WAN: site-to-site connectivity, internet, VPN, MPLS, and private circuits.
- `ACI` applies to the data center, where applications and services live.
- `VXLAN` helps create virtual tunnels across an existing network.
- `DNA Center` is now commonly called `Catalyst Center`, but the older name may still appear on exams.
- `APIC` is the controller for ACI.

## Key Points

- SDN moves management away from device-by-device administration and toward centralized control.
- Cisco splits SDN across campus, WAN, and data center use cases.
- For the exam, know the names. For the job, know the purpose.
- SD-Access manages the campus.
- SD-WAN connects sites and resources.
- ACI manages the data center.
- Catalyst Center/DNAC is the central platform for SD-Access.
- APIC is the controller for ACI.

## Notes

This topic looks like a terminology game at first.

Cisco has a lot of names:

- SD-Access;
- SD-WAN;
- ACI;
- DNAC;
- Catalyst Center;
- VXLAN;
- APIC.

If you hold all of that as one pile, it gets messy.

Separate it this way:

```text
Models = where the approach is used.
Platforms = what manages it.
```

## What SDN Means

`Software Defined Networking`, or `SDN`, is an approach where the network is managed through a central controller.

Old model:

```text
Log in to Switch 1.
Configure Switch 1.
Log in to Router 2.
Configure Router 2.
Log in to AP 3.
Configure AP 3.
```

SDN approach:

```text
Log in to a central platform.
Define the policy.
Let the controller apply changes across the network.
```

That does not mean engineers no longer need to understand devices. Without routing, switching, VLAN, and security knowledge, SDN is just a polished dashboard with no context.

## The Role of APIs

`API`, or Application Programming Interface, is a way for software to interact with a device or system.

Simple analogy:

```text
The controller wants to manage a switch.
It needs a doorway in.
The API is that doorway.
```

Through an API, a system can:

- read device state;
- send configuration;
- check health;
- receive telemetry;
- run provisioning;
- automate troubleshooting.

In SDN, APIs matter because a controller must be able to talk to devices, not merely know that they exist.

## Three Cisco SDN Models

Cisco SDN is easiest to remember through three areas:

| Model | Where It Applies | Simple Idea |
| --- | --- | --- |
| `SD-Access` | Campus network | Manages the building or branch network. |
| `SD-WAN` | Wide area network | Connects sites and resources. |
| `ACI` | Data center | Manages data center infrastructure. |

Short version:

```text
SD-Access = the network inside the building.
SD-WAN = the network between buildings.
ACI = the data center network.
```

## SD-Access

`SD-Access` is Cisco's model for the campus network.

A campus network is the network inside a building, office, store, school, or branch.

It includes:

- switches;
- access points;
- local routing;
- VLANs;
- policies;
- user and device access.

If NetworkChuck Coffee opens a new shop and wants centralized control over the in-store network, SD-Access fits that problem.

The idea is simple: manage the campus network through a central platform instead of manually configuring every switch and access point.

## SD-WAN

`SD-WAN` is Cisco's model for the wide area network.

The WAN connects:

- branches;
- stores;
- offices;
- data centers;
- cloud resources.

SD-WAN can use different link types:

- internet;
- VPN;
- MPLS;
- private circuits;
- LTE/5G backup.

Users do not care which link carried the traffic. They care that the application worked.

SD-WAN helps the controller choose the right path and make site-to-site connectivity more predictable.

## ACI

`ACI`, or Application Centric Infrastructure, is Cisco's model for the data center.

If SD-Access handles the building and SD-WAN connects sites, ACI lives where applications and services run.

Data centers need a different approach:

- many servers;
- many applications;
- high traffic density;
- strict policies;
- frequent changes;
- application-driven requirements.

ACI provides centralized management for the data center network and ties network policy to application needs.

## VXLAN

`VXLAN` can look like another intimidating term, but the basic idea is approachable.

VXLAN creates virtual tunnels across an existing network.

Simplified:

```text
Devices are physically in different places.
VXLAN helps them communicate as if logical connectivity exists between them.
```

It is like a VPN inside your own network.

Why it matters:

- physical topology becomes less limiting;
- the controller can build virtual connectivity;
- changes do not always require new cabling and switch ports;
- campus and data center designs become more flexible.

VXLAN is especially important in software-defined environments where a controller builds logical structure on top of the physical network.

## Cisco Platforms

Now separate models from platforms.

A model answers:

```text
Where are we applying SDN?
```

A platform answers:

```text
What are we using to manage it?
```

For SD-Access, Cisco long used the name `DNA Center`, or `DNAC`.

In newer Cisco material, this is more commonly called `Catalyst Center`.

For the exam, know both names:

```text
DNA Center = DNAC = Catalyst Center in the newer naming.
```

The platform can:

- show device health;
- show topology;
- check CPU and memory;
- perform provisioning;
- show licensing;
- provide troubleshooting data;
- manage the network as one system.

## APIC

For the data center and ACI, Cisco uses `APIC`: Application Policy Infrastructure Controller.

The shortest connection:

```text
ACI uses APIC.
```

APIC is the controller for an ACI environment and helps manage policies, connectivity, and the data center fabric.

## How to Remember It

Minimum CCNA table:

| Cisco Term | What to Remember |
| --- | --- |
| `SD-Access` | Campus network. |
| `SD-WAN` | WAN and site-to-site connectivity. |
| `ACI` | Data center. |
| `DNA Center` / `DNAC` | Older/exam name for the SD-Access platform. |
| `Catalyst Center` | Newer name for the SD-Access platform. |
| `APIC` | Controller for ACI. |
| `VXLAN` | Virtual tunnels across an existing network. |
| `API` | Programmable doorway into a system or device. |

## Real World Tip

If you are studying for an exam, memorize the names.

If you are working on the job, memorize the purpose.

Nobody is impressed by a mechanical expansion of `ACI` if you do not understand that:

```text
ACI = data center.
SD-Access = campus.
SD-WAN = WAN.
Catalyst Center/DNAC = centralized campus management.
```

Purpose is what keeps Cisco branding from becoming random noise.

## Takeaway

Cisco SDN is not a random list of names.

It is a map:

- APIs give the controller a way to talk to devices;
- VXLAN helps build virtual connectivity;
- SD-Access manages the campus network;
- SD-WAN manages the WAN;
- ACI manages the data center;
- Catalyst Center/DNAC manages SD-Access;
- APIC manages ACI.

Once those lanes are clear, the topic stops feeling like a pile of acronyms and starts looking like a normal architecture.

## Commands and Terms

| Term | Meaning |
| --- | --- |
| `SDN` | Software Defined Networking, a centralized approach to managing networks. |
| `API` | Application Programming Interface, a way for software to interact with a system. |
| `SD-Access` | Cisco SDN model for the campus network. |
| `SD-WAN` | Cisco SDN model for the wide area network. |
| `ACI` | Application Centric Infrastructure, Cisco SDN model for the data center. |
| `VXLAN` | A technology for virtual tunnels across an existing network. |
| `DNA Center` | Older name for Cisco's SD-Access platform. |
| `DNAC` | Short for DNA Center. |
| `Catalyst Center` | Newer name for Cisco's SD-Access platform. |
| `APIC` | Controller for Cisco ACI. |
| controller | A central system that manages a network or part of a network. |

## Questions

### 1. Why does SDN need APIs?

Answer: APIs give the controller a programmable way to interact with devices or systems.

### 2. What is SD-Access used for?

Answer: Campus networks: buildings, branches, switches, access points, and local policies.

### 3. What is SD-WAN used for?

Answer: Connecting sites and resources across the WAN, including internet, VPN, MPLS, and private circuits.

### 4. Where is ACI used?

Answer: In the data center.

### 5. How is Catalyst Center related to DNA Center?

Answer: Catalyst Center is the newer name for the platform Cisco previously called DNA Center/DNAC.

### 6. What does VXLAN do?

Answer: It creates virtual tunnels across an existing network and provides more flexible logical connectivity.

## Review Later

- The difference between a model and a platform.
- SD-Access = campus.
- SD-WAN = WAN.
- ACI = data center.
- DNA Center/DNAC and Catalyst Center.
- APIC as the controller for ACI.
- The roles of API and VXLAN in SDN.
