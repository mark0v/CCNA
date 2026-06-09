# Document the Network as You Build

Source: closed course page  
Date added: 2026-06-09  
Related plan item: Week 6 / Network documentation and IPAM foundations  
Tags: network documentation, IPAM, inventory, show version, show ip interface brief, lifecycle, troubleshooting
Language: English
Translation pair: articles/2026-06/week-06/05-document-the-network-as-you-build.md

## Summary

Network documentation should be maintained while the network is being built, not postponed until project closeout. Even a simple spreadsheet containing devices, interfaces and IP addresses can greatly accelerate troubleshooting, support and hardware replacement.

Main idea: useful documentation that is easy to update is better than a perfect system that never gets created. Start with one practical table and let it grow with the network.

## Key Points

- Document immediately after configuration changes.
- Do not rely on memory or a promise to return later.
- Excel or Google Sheets is enough to begin.
- Core fields include device name, model, serial, interface, MAC and IP address.
- Firmware, purchase date, in-service date and warranty are operationally useful.
- `show version` provides model, serial and software information.
- `show ip interface brief` quickly shows interfaces, IP addresses and status.
- `show interface` provides interface MAC and operational data.
- Collect values directly from devices instead of reconstructing them from memory.
- Consistent formatting improves searching and comparison.
- An inventory spreadsheet is an early step toward IPAM and lifecycle management.
- Documentation updates belong in the same change process as network updates.

## Notes

### Documentation Is Not Closeout Work

Documentation often appears near the end of a formal project plan.

By that point:

- the team is tired;
- deadlines have passed;
- details have been forgotten;
- engineers have moved to the next project;
- temporary solutions have become permanent;
- nobody wants to reconstruct the topology from memory.

The correct time to record a change is:

```text
Immediately after the change is configured and verified.
```

### Why It Matters During An Incident

During an outage, documentation should answer:

```text
What is the device name?
Where is it located?
What is its management IP?
Which interface is connected?
Which neighbor is on the other side?
Which software version is installed?
Is it under warranty?
When was it changed?
```

Without those answers, troubleshooting begins by rediscovering the network.

### Start With One Useful Sheet

An enterprise platform is not required on day one.

Create a sheet named:

```text
Devices and IP Addresses
```

Suggested columns:

| Column | Purpose |
| --- | --- |
| Device Name | Unique hostname |
| Role | Router, switch, firewall, AP or server |
| Site / Location | Physical location |
| Vendor / Model | Exact hardware platform |
| Serial Number | Support and asset tracking |
| Interface | Physical or logical port |
| Interface Description | Purpose of the link |
| MAC Address | Layer 2 identity |
| IP Address / Prefix | Layer 3 assignment |
| Default Gateway | Gateway for managed endpoints |
| Firmware / OS | Software version |
| Purchase Date | Start of lifecycle |
| In-Service Date | Deployment date |
| Warranty End | Replacement/support planning |
| Owner | Responsible person or team |
| Notes | Special details |

### Keep The Structure Practical

The table should be:

- understandable without separate instructions;
- easy to filter;
- consistently formatted;
- simple to update;
- available to the correct engineers;
- protected against accidental edits.

Useful improvements include:

- bold headers;
- frozen header row;
- filters;
- consistent date format;
- fixed IP/CIDR format;
- highlighting for expired warranties;
- dropdown values for role and status.

### Collect Data From Devices

Do not populate the inventory from memory.

Useful Cisco IOS commands:

```cisco
show version
show ip interface brief
show interfaces
show inventory
show cdp neighbors detail
show lldp neighbors detail
```

Each command provides a different part of the picture.

### `show version`

This command commonly provides:

- Cisco IOS version;
- uptime;
- hardware model;
- memory;
- system image;
- serial or processor board ID;
- configuration register.

Record the complete software release and build.

### `show inventory`

On supported devices:

```cisco
show inventory
```

It can display:

- chassis PID;
- serial number;
- installed modules;
- power supplies;
- transceivers.

It is often better than `show version` for detailed hardware inventory.

### `show ip interface brief`

```cisco
show ip interface brief
```

It quickly displays:

- interface name;
- assigned IP;
- assignment method;
- administrative status;
- line protocol status.

This is a good starting point for interface and IP mapping.

### `show interfaces`

For a specific interface:

```cisco
show interface GigabitEthernet0/1
```

It can provide:

- hardware/MAC address;
- description;
- status;
- speed and duplex;
- counters and errors;
- MTU;
- traffic rates.

An inventory normally stores stable identity data rather than temporary counters.

### Neighbor Discovery

For documenting links:

```cisco
show cdp neighbors detail
show lldp neighbors detail
```

These commands can correlate:

- local interface;
- remote device;
- remote port;
- management address;
- platform.

Discovery output should still be validated against actual cabling and design.

### Standardize The Data

Choose consistent formats:

```text
Hostname:       CAFE01-RTR01
Interface:      GigabitEthernet0/1
IPv4:           192.168.2.1/24
MAC:            00:1A:2B:3C:4D:5E
Date:           2026-06-09
Software:       Cisco IOS 15.2(4)M
```

Avoid mixing:

- `Gi0/1` and `GigabitEthernet0/1`;
- CIDR and separate masks;
- different MAC separators;
- local and ISO date formats;
- marketing and exact product names.

Consistency improves search, sorting and automation.

### Why Model And Serial Matter

Exact model and serial numbers support:

- vendor support cases;
- warranty verification;
- replacement/RMA;
- spare planning;
- security advisory checks;
- asset ownership;
- audits.

`Cisco switch` is not specific enough.

Record the exact platform, such as:

```text
Cisco Catalyst C9200L-24P-4G
```

### Why Firmware Matters

Different software versions can cause:

- different protocol behavior;
- known defects;
- security vulnerabilities;
- command incompatibilities;
- different defaults;
- loss of vendor support.

A firmware inventory identifies devices requiring patches or upgrades.

### Lifecycle And Warranty

Purchase and in-service dates indicate equipment age.

Warranty and end-of-support dates help plan:

- budgets;
- replacements;
- maintenance windows;
- spare inventory;
- migrations.

An outage is the wrong time to discover that a device is unsupported.

### This Is The Beginning Of IPAM

IPAM means:

```text
IP Address Management
```

IPAM organizes:

- address spaces;
- subnets;
- assigned and available IPs;
- DHCP scopes;
- DNS records;
- VLANs;
- sites;
- owners;
- reservations;
- conflicts.

A spreadsheet is not a full IPAM platform, but it establishes the required discipline.

### Grow Documentation Gradually

Future sheets can cover:

- Subnets and VLANs;
- Routing;
- WAN Circuits;
- Cabling;
- Rack Layout;
- Wireless;
- Firewall Rules;
- Support Contracts;
- Change Log;
- Backup and Recovery.

Add structure as real needs appear.

### Make Updates Part Of Change Management

For each network change:

1. Plan the configuration.
2. Prepare or update documentation.
3. Perform the change.
4. Verify the result.
5. Record actual values.
6. Add date and author.

A change is not fully complete until documentation matches the actual state.

### Protect Sensitive Information

Do not store plaintext passwords, private keys or reusable secrets in a normal spreadsheet.

Documentation can contain:

- authentication type;
- vault entry name;
- owner;
- rotation date;
- recovery procedure location.

The secrets themselves belong in an approved password manager or secrets vault.

## Example Inventory Row

| Device | Role | Site | Model | Serial | Interface | IP/Prefix | MAC | Software | Warranty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CAFE01-RTR01 | Edge Router | Cafe 01 | ISR 4331 | FDOXXXXXXX | Gi0/0/0 | 192.168.1.1/24 | 00:1A:2B:3C:4D:5E | IOS XE 17.x | 2028-06-30 |

## Practical Checklist

- Create a central inventory.
- Add understandable columns.
- Collect data directly from devices.
- Normalize names, dates, MAC and IP formats.
- Record site and role.
- Record model, serial and software.
- Add lifecycle and warranty details.
- Document interface descriptions and neighbors.
- Do not store secrets in plaintext.
- Update documentation with every change.
- Periodically compare documentation with the live network.

## Quick Self-Check

### Question 1

When should a network change be documented?

Answer:

```text
During the change, immediately after configuration and verification.
```

### Question 2

Which commands quickly provide device and IP information?

Answer:

```text
show version, show inventory and show ip interface brief.
```

### Question 3

Why does firmware version matter?

Answer:

```text
It affects behavior, defects, security, compatibility and support.
```

### Question 4

What is IPAM?

Answer:

```text
The practice of managing IP address spaces, subnets and assignments.
```

### Question 5

Should passwords be stored in an inventory spreadsheet?

Answer:

```text
No. Secrets belong in a protected password manager or vault.
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Network inventory | Register of devices, interfaces and operational details. |
| IPAM | IP Address Management. |
| `show version` | Device model, software and system information. |
| `show inventory` | Hardware modules, PIDs and serial numbers. |
| `show ip interface brief` | Short interface IP/status list. |
| `show interface` | Detailed information for an interface. |
| CDP / LLDP | Neighbor discovery protocols. |
| Lifecycle | Period from purchase to retirement. |
| RMA | Vendor replacement process for faulty hardware. |
| Source of truth | Authoritative location for current information. |

## What To Review Later

- IPAM platforms
- Network diagrams
- Configuration backups
- Change management
- Asset lifecycle
- NetBox
- Automated discovery
- Documentation audits
