# Exploring MAC Address Tables on a Cisco Switch

Source: закрытая страница курса  
Date added: 2026-05-24  
Related plan item: Week 4 / Cisco MAC address table lab  
Tags: switching, mac address table, cam table, arp, packet tracer, stp, spanning tree, broadcast, troubleshooting
Language: Russian
Translation pair: articles-en/2026-05/week-04/05-exploring-mac-address-tables-on-a-cisco-switch.md

## Summary

MAC address table становится понятнее, когда ты видишь, как switch learns addresses in real time. В Packet Tracer можно построить простую topology, настроить PC1 и PC2 в одной subnet, очистить ARP cache, выполнить ping и наблюдать, как ARP request вызывает broadcast, switch learns source MAC, а затем `show mac address-table` показывает learned MAC addresses and ports.

Главная мысль: switch learns first, forwards second. MAC address table - это живая карта сети, которая меняется по мере появления traffic.

## Key Points

- Building the lab yourself matters more than only watching a demo.
- Clear topology labels make switching behavior easier to understand.
- PC1 and PC2 can be placed in the same subnet, for example `192.168.1.50/24` and `192.168.1.51/24`.
- `arp -a` shows the ARP cache on a host.
- Before first communication, ARP cache may be empty.
- Ping may trigger ARP before ICMP traffic can be sent.
- ARP request is broadcast to `FFFF.FFFF.FFFF`.
- The switch learns the source MAC from incoming frames.
- Broadcasts are flooded out active ports except the incoming port.
- ARP reply is usually unicast back to the requester.
- First ping can take longer because ARP happens first.
- `show mac address-table` shows learned MAC addresses and interfaces.
- `clear mac address-table dynamic` clears dynamically learned MAC entries.
- MAC table entries are dynamic: learned, aged out and relearned.
- STP can block a redundant link to prevent loops.
- A blocked STP port is not automatically a failure.

## Notes

### Build It, Don't Just Watch It

Watching a switching demo can create false confidence.

Real learning happens when you:

- build the topology;
- connect devices;
- assign IP addresses;
- generate traffic;
- inspect ARP cache;
- inspect switch MAC address table;
- repeat until the behavior makes sense.

In Packet Tracer, this makes abstract switching visible.

### Lab Topology

Simple lab:

```text
PC1 -> Switch -> PC2
```

Or with multiple switches:

```text
PC1 -> Switch 1 -> Switch 2 -> PC2
```

Example IP addresses:

```text
PC1: 192.168.1.50/24
PC2: 192.168.1.51/24
```

Both are in the same subnet:

```text
192.168.1.0/24
```

### Clean Diagrams Matter

Messy labels create messy thinking.

Before testing, clean up:

- device names;
- interface labels;
- cable placement;
- IP labels;
- port notes.

The easier the topology is to read, the easier it is to understand what the switch is doing.

### ARP Cache

On a PC, the ARP cache stores known IP-to-MAC mappings.

Command:

```text
arp -a
```

Before traffic, the ARP cache may be empty.

That is useful for learning because you can watch the ARP process happen from scratch.

### First Ping

When PC1 pings PC2:

```text
ping 192.168.1.51
```

PC1 knows the destination IP.

But it may not know PC2's MAC address yet.

Before ICMP ping can be sent in an Ethernet frame, PC1 needs a destination MAC.

That triggers ARP.

### ARP Request

ARP request asks:

```text
Who has 192.168.1.51? Tell 192.168.1.50.
```

It uses broadcast destination MAC:

```text
FFFF.FFFF.FFFF
```

Everyone in the local broadcast domain receives it.

### What the Switch Learns First

When the ARP request enters the switch, the switch reads the source MAC.

It learns:

```text
PC1 MAC -> incoming switch port
```

This happens before the final ping succeeds.

The switch learns from incoming frames, not from magic or manual entry.

### Flooding the Broadcast

Because ARP request is broadcast, the switch floods it.

Rule:

```text
Flood out active ports except the incoming port.
```

PC2 receives the request and recognizes its own IP address.

Other devices ignore the request.

### ARP Reply

PC2 sends ARP reply back to PC1.

This is usually unicast:

```text
Source MAC: PC2 MAC
Destination MAC: PC1 MAC
```

When the reply enters the switch, the switch learns:

```text
PC2 MAC -> incoming switch port
```

Now the MAC address table has entries for both PCs.

### ICMP Ping After ARP

After ARP completes, PC1 knows PC2's MAC address.

Then PC1 can build the real frame for ICMP ping.

Flow:

```text
Check ARP cache
Send ARP request if needed
Receive ARP reply
Send ICMP echo request
Receive ICMP echo reply
```

First ping may be slower because discovery happens first.

Later pings are faster because the ARP mapping is cached.

### show mac address-table

Cisco command:

```text
show mac address-table
```

This shows:

- learned MAC addresses;
- VLAN association;
- type of entry;
- interface/port where MAC was learned.

In plain English, it helps answer:

```text
Where is this device connected?
```

### Dynamic MAC Entries

Most learned entries are dynamic.

Dynamic means:

- switch learned them from traffic;
- they can age out;
- they can be relearned;
- they are not manually fixed forever.

The MAC address table is alive.

It changes as devices communicate.

### clear mac address-table dynamic

Command:

```text
clear mac address-table dynamic
```

This clears dynamically learned MAC entries.

After clearing:

- table loses learned dynamic entries;
- new traffic causes relearning;
- you can watch the learning process again.

This is a powerful lab exercise.

### STP and Blocked Links

In a topology with redundant links, Packet Tracer may show one link blocked.

This is often STP.

STP means:

```text
Spanning Tree Protocol
```

STP prevents Layer 2 loops by blocking redundant paths when needed.

### Why STP Blocks Links

Without STP, a broadcast could loop forever between switches.

That can cause:

- broadcast storm;
- high CPU;
- frozen devices;
- network meltdown;
- business outage.

So a blocked redundant link may be protection, not a failure.

Do not disable STP casually.

### Real Troubleshooting Value

In real network administration, `show mac address-table` is useful when:

- locating a device;
- finding a rogue host;
- checking where traffic enters;
- tracing an AP, camera or POS terminal;
- confirming whether a device is connected;
- determining whether a port is endpoint or uplink.

At NetworkChuck Coffee, this helps move from:

```text
Something is broken
```

to:

```text
This MAC was learned on this port
```

That is actionable evidence.

### Main Takeaway

This lab shows switching as a live process:

1. Host checks ARP cache.
2. ARP request is broadcast.
3. Switch learns source MAC.
4. Switch floods broadcast.
5. Target sends ARP reply.
6. Switch learns target MAC.
7. Ping traffic can flow.
8. MAC table shows what the switch learned.

Once you see it happen, switching becomes logic instead of mystery.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| `arp -a` | Host command that displays ARP cache. |
| ARP cache | Local table of IP-to-MAC mappings on a host. |
| ARP request | Broadcast request asking who owns an IP address. |
| ARP reply | Usually unicast response containing the requested MAC address. |
| ICMP | Protocol used by ping. |
| `ping` | Command used to test reachability. |
| MAC address table | Switch table showing learned MAC addresses and interfaces. |
| `show mac address-table` | Cisco command that displays the MAC address table. |
| Dynamic MAC entry | MAC table entry learned from traffic and subject to aging. |
| `clear mac address-table dynamic` | Cisco command that clears dynamically learned MAC entries. |
| STP | Spanning Tree Protocol; prevents Layer 2 loops. |
| Broadcast storm | Looping broadcast traffic that can overwhelm a network. |
| Flooding | Sending a frame out multiple ports except the incoming port. |
| Unicast | One-to-one communication. |

## Questions

### 1. Why should you build the Packet Tracer lab yourself?

Because watching can create false confidence; building forces you to understand the steps.

### 2. What does `arp -a` show?

The host's ARP cache.

### 3. Why might the ARP cache be empty before the first ping?

Because the host has not yet learned IP-to-MAC mappings for local devices.

### 4. Why does ping often trigger ARP first?

Because the host needs the destination MAC address before sending the Ethernet frame.

### 5. What destination MAC does an ARP request use?

`FFFF.FFFF.FFFF`.

### 6. What does the switch learn from an ARP request?

The source MAC address and the incoming port.

### 7. How does a switch handle the ARP broadcast?

It floods it out active ports except the incoming port.

### 8. What command shows the switch MAC address table?

`show mac address-table`.

### 9. What does `clear mac address-table dynamic` do?

It clears dynamically learned MAC address entries so the switch can relearn them from traffic.

### 10. Why is the MAC table called "alive"?

Because entries are learned, aged out and relearned based on traffic.

### 11. What does STP prevent?

Layer 2 loops and broadcast storms.

### 12. Should you assume a blocked redundant link is broken?

No. It may be STP protecting the network from a loop.

## What To Review Later

- Packet Tracer simulation mode.
- ARP cache with `arp -a`.
- First ping and ARP.
- Broadcast destination MAC.
- Switch source MAC learning.
- `show mac address-table`.
- Dynamic MAC entries.
- `clear mac address-table dynamic`.
- STP and blocked links.
- Broadcast storm risk.
