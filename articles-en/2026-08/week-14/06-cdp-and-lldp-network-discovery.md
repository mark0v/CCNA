# CDP And LLDP Network Discovery

Source: closed course page  
Date added: 2026-08-02  
Related plan item: Week 14 / CDP and LLDP network discovery  
Tags: CDP, LLDP, network discovery, neighbor discovery, troubleshooting, switch operations, documentation
Language: English
Translation pair: articles/2026-08/week-14/06-cdp-and-lldp-network-discovery.md

## Summary

- CDP and LLDP help you see neighboring devices on a link.
- They are not glamorous protocols, but they are very useful during troubleshooting.
- CDP is Cisco's neighbor discovery protocol.
- LLDP is a standards-based protocol that works across vendors.
- These protocols show what is connected to a port, what device it is, and which interface is on the far end.
- They help when documentation is stale or a network diagram is missing.
- Discovery protocols show the network as it is, not as it was drawn.

## Key Points

- Network diagrams often become outdated as physical connections change.
- Before fixing a problem, you need to understand the real topology.
- CDP and LLDP reduce guesswork when identifying neighboring devices.
- They are useful when first connecting to an unfamiliar switch.
- Discovery information can include device ID, local interface, remote interface, platform, and capabilities.
- In production, these protocols should be used intentionally: they give administrators visibility, but they can expose information to the wrong devices.

## Notes

CDP and LLDP do not look like major topics. They do not encrypt traffic, build routes, or directly block attacks. But when the network is confusing, documentation is outdated, and cables have been moved without notes, they become valuable.

The idea is simple:

```text
A device tells its neighbor who it is and which port it is using.
```

Then an administrator runs a show command and sees what is on the other end of the cable.

That is especially useful when the paper diagram no longer matches reality.

## Why This Matters

The network in the diagram and the network in the rack often differ.

Common causes:

- someone moved a cable;
- a switch was replaced;
- a wireless access point was added;
- an IP phone was installed;
- a temporary connection became permanent;
- documentation was not updated;
- the old administrator left.

In that situation, troubleshooting should not start from assumptions alone. You need to understand the device's neighbors quickly.

CDP and LLDP answer practical questions:

- what is connected to this switch;
- through which local interface;
- which remote interface is on the neighbor;
- what the neighbor calls itself;
- what type of device it is;
- what capabilities it advertises.

## CDP

CDP, or Cisco Discovery Protocol, is Cisco's proprietary protocol.

It lets Cisco devices exchange neighbor information. A switch can advertise its name, port, platform, capabilities, and other operational details.

Typical command:

```text
show cdp neighbors
```

More detailed command:

```text
show cdp neighbors detail
```

You may see:

- device ID;
- local interface;
- holdtime;
- capabilities;
- platform;
- neighbor port ID;
- sometimes a management IP address.

CDP is especially convenient in Cisco-heavy environments.

## LLDP

LLDP, or Link Layer Discovery Protocol, is a standards-based neighbor discovery protocol.

The main difference is that it is vendor-neutral. It can work between Cisco, Juniper, HPE, Aruba, Linux systems, hypervisors, IP phones, wireless access points, and other equipment if they support the standard.

Typical command:

```text
show lldp neighbors
```

More detailed command:

```text
show lldp neighbors detail
```

In a mixed network, LLDP is often more important than CDP because it works more broadly.

## Shared Mission

CDP and LLDP have different origins and formats, but almost the same goal:

```text
Show neighboring devices and help identify the real topology.
```

Comparison:

| Protocol | Characteristic |
| --- | --- |
| CDP | Cisco-proprietary, convenient in Cisco environments. |
| LLDP | Standards-based, useful in mixed-vendor networks. |

Both operate at Layer 2 and send information directly to neighboring devices on the local link.

## NetworkChuck Coffee Scenario

Imagine NetworkChuck Coffee during the morning rush.

A card terminal starts timing out. Customers are waiting, payments are unstable, and there is no time to physically trace cables.

The administrator connects to a switch and runs:

```text
show cdp neighbors
show lldp neighbors
```

They can quickly see:

- which access point is connected to which port;
- where the IP phone is;
- which uplink leads to the neighboring switch;
- which port goes toward the back office;
- whether reality matches the documentation.

This does not automatically solve the problem, but it removes confusion. Troubleshooting without confusion is almost always faster.

## More Than Discovery

Discovery protocols can advertise more than a neighbor's name.

Depending on the device and configuration, you may see:

- capabilities;
- platform;
- native VLAN;
- voice VLAN;
- management address;
- duplex information;
- power information for PoE scenarios.

That helps not only with topology, but also with checking whether the connected device fits the environment correctly.

For example, an IP phone or access point may learn useful information from a neighboring switch. That turns the protocol from simple discovery into operational assistance.

## Limits And Security

Useful visibility has a downside.

CDP and LLDP can reveal:

- device names;
- models;
- software versions;
- management IP addresses;
- topology hints;
- VLAN details.

On internal switch-to-switch links, this is usually helpful. On ports exposed to untrusted users, that information may be unnecessary.

The policy should be intentional:

- enable discovery where it helps administrators;
- disable or limit it where the port is accessible to untrusted devices;
- follow the organization's security requirements.

Example commands:

```text
no cdp run
cdp run

interface fa0/10
 no cdp enable
```

For LLDP, the logic is similar, but commands depend on the platform:

```text
lldp run

interface fa0/10
 no lldp transmit
 no lldp receive
```

## Verification

Useful commands:

```text
show cdp neighbors
show cdp neighbors detail
show cdp interface
show lldp neighbors
show lldp neighbors detail
show lldp interface
```

Check:

- whether the expected neighbor is visible;
- whether the remote port matches documentation;
- whether an unexpected device appears;
- whether discovery is enabled on unnecessary user-facing ports;
- whether the protocol is disabled where operations need it.

## Practical Habit

When connecting to an unfamiliar switch, a useful start is:

1. Check neighbors.
2. Compare output with documentation.
3. Find unexpected connections.
4. Verify uplinks and trunks.
5. Update diagrams or notes.

That turns CDP and LLDP from "small protocol topics" into real network support tools.

## Main Takeaway

CDP and LLDP help you see the network as it exists right now.

If the diagram is stale, documentation is missing, or troubleshooting starts in an unfamiliar environment, discovery protocols provide a fast way to understand device neighbors.

They do not replace documentation. They help verify and update it. That is their strength: fewer assumptions, faster diagnosis, and clearer topology.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| CDP | Cisco Discovery Protocol, Cisco's proprietary neighbor discovery protocol. |
| LLDP | Link Layer Discovery Protocol, standards-based neighbor discovery protocol. |
| neighbor | Directly connected Layer 2 device. |
| local interface | Local port where the neighbor is seen. |
| port ID | Port on the neighboring device. |
| capabilities | Advertised device roles, such as switch, router, or phone. |
| management address | Address used to manage the device. |
| discovery protocol | Protocol that lets devices advertise information to neighbors. |

## Questions

### 1. What are CDP and LLDP used for?

Answer: They show neighboring devices and help identify the real connection topology.

### 2. How is CDP different from LLDP?

Answer: CDP is Cisco-proprietary, while LLDP is standards-based and vendor-neutral.

### 3. Why are these protocols useful during troubleshooting?

Answer: They show what is connected to a port without physically tracing cables.

### 4. Why can discovery protocols be a security concern?

Answer: They can reveal device names, models, management IP addresses, and topology hints.

### 5. What should you do when connecting to an unfamiliar switch?

Answer: Check neighbors with CDP or LLDP and compare the output with documentation.

## What To Review Later

- `show cdp neighbors`.
- `show cdp neighbors detail`.
- `show lldp neighbors`.
- `show lldp neighbors detail`.
- Difference between Cisco-proprietary and vendor-neutral protocols.
- Where discovery protocols should be disabled.
