# Switch Port Numbering and CAM Table

Source: closed course page  
Date added: 2026-05-24  
Related plan item: Week 4 / Switch interfaces and CAM table  
Tags: switching, switch ports, cam table, mac address table, interface status, fastethernet, gigabitethernet, uplink
Language: English
Translation pair: articles/2026-05/week-04/03-switch-port-numbering-and-cam-table.md

## Summary

Switch port numbering and the CAM table are practical tools for understanding what is physically happening in a LAN. Interface names show port type and speed, numbering helps locate modules, stacks and ports, and the CAM/MAC address table shows which MAC addresses the switch learned on which interfaces.

Main idea: switch output is a map of the physical network. If you can read port names, status and the MAC address table, you can find devices faster, identify uplinks and understand where a problem begins.

## Key Points

- Switch port names are not random.
- Interface names often show speed/type, such as FastEthernet, GigabitEthernet or TenGigabitEthernet.
- FastEthernet usually means 10/100 Mbps.
- GigabitEthernet means 1000 Mbps.
- TenGigabitEthernet means 10 Gbps.
- Cisco abbreviations must be unique enough for IOS to understand.
- `Fa` commonly abbreviates FastEthernet.
- `Gi` or `G` commonly abbreviates GigabitEthernet.
- Numbering like `0/1` or `1/12` reflects module/slot/stack and port structure.
- Modular switches and stacked switches explain why numbering is more complex than "port 1."
- CAM table stores learned MAC addresses and associated ports.
- Cisco command `show mac address-table` displays the MAC address table.
- One MAC on a port often suggests one end device.
- Many MAC addresses on one port often suggests an uplink to another switch.
- Do not stop tracing when the MAC is found on an uplink.
- `show ip interface brief`, `show interface status` and `show mac address-table` are core switch investigation commands.

## Notes

### Seeing a Switch as a Map

A switch should not be seen only as a box with blinking lights.

It is a map of the local network.

Each interface can tell you:

- interface name;
- port type;
- speed;
- status;
- connected device or path;
- learned MAC addresses.

At NetworkChuck Coffee, this matters when:

- POS system drops offline;
- access point behaves strangely;
- back-office device cannot connect;
- unknown device appears;
- network performance feels wrong.

The practical question is:

```text
What port is it on?
```

### Useful Interface Commands

Common commands:

```text
show ip interface brief
show interface status
show mac address-table
```

Use them to answer:

- what interfaces exist;
- which interfaces are up;
- what speed/duplex is negotiated;
- which MAC addresses were learned;
- which port may lead to the device.

### Interface Names

Cisco interface names describe the interface type.

Examples:

| Interface Type | Common Meaning |
| --- | --- |
| FastEthernet | Usually 10/100 Mbps |
| GigabitEthernet | 1000 Mbps |
| TenGigabitEthernet | 10 Gbps |

In CLI output, names may appear in full or abbreviated.

Examples:

```text
FastEthernet0/1
Fa0/1
GigabitEthernet0/1
Gi0/1
TenGigabitEthernet1/1
Te1/1
```

### Cisco Abbreviations

Cisco IOS lets you abbreviate commands and interface names as long as the abbreviation is unique enough.

FastEthernet often becomes:

```text
Fa
```

GigabitEthernet often becomes:

```text
Gi
```

or sometimes:

```text
G
```

It may feel strange at first, but it becomes natural with practice.

### What Does 0/1 Mean?

The `0/1` format is not random.

It comes from switch platforms that can have modules, slots or stacks.

Basic idea:

```text
module-or-switch / port
```

Examples:

```text
FastEthernet0/1
GigabitEthernet1/12
FastEthernet4/8
```

`FastEthernet1/12` can mean module or switch 1, port 12.

`FastEthernet4/8` can mean module or switch 4, port 8.

Exact meaning depends on platform.

### Modular Switches

Large chassis switches can use line cards.

A line card is a module with many ports.

In that world, numbering like this makes sense:

```text
slot/module 1, port 12
slot/module 4, port 8
```

That is why Cisco interface numbers often have more than one number.

### Switch Stacking

Even smaller switches may use similar numbering because of stacking.

Stacking means multiple physical switches are connected and managed as one logical switch.

In a stack, the first number may represent the physical switch in the stack.

Example:

```text
GigabitEthernet2/0/5
```

Depending on platform, this could mean:

```text
switch 2 / module 0 / port 5
```

Do not memorize one universal format only. Learn the concept: the numbers help locate hardware inside a scalable switch system.

### CAM Table

CAM means:

```text
Content Addressable Memory
```

In switching, people often say CAM table to mean the table where the switch stores learned MAC addresses.

Modern Cisco output usually uses:

```text
MAC address table
```

The core idea:

```text
MAC address -> switch port
```

The switch uses this table to forward frames intelligently.

### show mac address-table

Command:

```text
show mac address-table
```

This displays MAC addresses the switch has learned and the interfaces associated with them.

Useful for:

- finding a device;
- identifying where traffic enters;
- tracing an endpoint;
- spotting uplinks;
- understanding local Layer 2 paths.

### One MAC vs Many MACs

If a port shows one MAC address, it may be connected to a single end device.

Example:

```text
Fa0/3 -> one printer MAC
```

If a port shows many MAC addresses, it often connects to another switch.

Example:

```text
Gi0/1 -> 20 MAC addresses
```

That usually means Gi0/1 is an uplink toward another switch or downstream network segment.

### Do Not Stop at the First Match

When tracing a MAC address, do not stop too early.

If the MAC appears on an uplink, the device is probably not physically plugged into that local switch port.

It may live beyond another switch.

Better workflow:

```text
Find MAC on current switch.
Check whether interface is endpoint or uplink.
If uplink, move to downstream switch.
Repeat until the MAC is on an access port.
```

This is how device tracing becomes accurate.

### Why Diagrams Matter

Network diagrams help explain what switch output means.

Without a diagram, you may not know whether:

- Gi0/1 goes to another switch;
- Fa0/12 goes to a wall jack;
- Te1/1 is an uplink;
- a port connects to an AP;
- a port connects to a downstream unmanaged switch.

Even a rough diagram can save time.

### show interface status

Command:

```text
show interface status
```

This is useful for seeing:

- interface name;
- status;
- VLAN;
- duplex;
- speed;
- type.

This can reveal real issues.

Example:

```text
Half-duplex 100 Mbps
```

That may indicate an old device, negotiation problem or performance bottleneck.

### Building Your Troubleshooting Eyes

The goal is not only to memorize commands.

The goal is to look at output and ask:

- what kind of port is this;
- is it up or down;
- what speed is it using;
- is it full-duplex or half-duplex;
- is it an access port or uplink;
- how many MAC addresses are learned there;
- does this match the diagram;
- where should I go next?

This is how switch troubleshooting becomes practical.

### Main Takeaway

Switch port numbering and CAM table output help connect logical network behavior to physical reality.

If you can read:

```text
interface names
port status
MAC address table
speed/duplex
uplink vs endpoint clues
```

then you can start tracing devices like a real network admin.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Interface | Network port or logical connection on a device. |
| FastEthernet | Interface type commonly associated with 10/100 Mbps. |
| GigabitEthernet | Interface type for 1000 Mbps. |
| TenGigabitEthernet | Interface type for 10 Gbps. |
| `Fa` | Common abbreviation for FastEthernet. |
| `Gi` | Common abbreviation for GigabitEthernet. |
| `Te` | Common abbreviation for TenGigabitEthernet. |
| Module | Hardware unit or slot in a modular switch. |
| Line card | Module containing ports in a chassis switch. |
| Switch stack | Multiple physical switches managed as one logical switch. |
| CAM table | Content Addressable Memory table used to map MAC addresses to ports. |
| MAC address table | Cisco term/output for learned MAC addresses and interfaces. |
| Uplink | Port leading to another switch or upstream network device. |
| Access port | Port usually connected to an end device. |
| `show ip interface brief` | Command showing interface and IP/status summary. |
| `show interface status` | Command showing interface status, VLAN, duplex and speed. |
| `show mac address-table` | Command showing learned MAC addresses and associated ports. |

## Questions

### 1. Why do switch port names matter?

They help identify interface type, speed and physical location in the switch.

### 2. What does FastEthernet usually mean?

10/100 Mbps Ethernet.

### 3. What does GigabitEthernet mean?

1000 Mbps Ethernet.

### 4. What does TenGigabitEthernet mean?

10 Gbps Ethernet.

### 5. Why does Cisco use abbreviations like `Fa` and `Gi`?

Because IOS accepts short abbreviations when they are unique enough.

### 6. What does numbering like `0/1` usually represent?

A module/switch/slot and port structure, depending on platform.

### 7. Why do larger switches need numbering beyond simple port numbers?

Because they may have modules, line cards or stacked switch members.

### 8. What does the CAM table store?

Learned MAC addresses and the switch ports associated with them.

### 9. What command shows learned MAC addresses?

`show mac address-table`.

### 10. What does one MAC address on a port often suggest?

That the port may connect to a single end device.

### 11. What do many MAC addresses on one port often suggest?

That the port is likely an uplink to another switch or downstream network.

### 12. Why should you not stop at the first port where you find a MAC?

Because that port may be an uplink, and the actual device may be farther downstream.

### 13. What command helps reveal speed and duplex?

`show interface status`.

### 14. Why are network diagrams useful here?

They help interpret whether a port is an endpoint connection, uplink, AP, wall jack or downstream switch.

## What To Review Later

- Interface naming.
- FastEthernet, GigabitEthernet and TenGigabitEthernet.
- Cisco interface abbreviations.
- Module/slot/port numbering.
- Switch stacking.
- CAM table / MAC address table.
- One MAC vs many MACs on a port.
- Uplink vs access port.
- `show ip interface brief`.
- `show interface status`.
- `show mac address-table`.
