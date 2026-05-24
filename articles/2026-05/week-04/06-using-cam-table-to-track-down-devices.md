# Using CAM Table to Track Down Devices

Source: закрытая страница курса  
Date added: 2026-05-24  
Related plan item: Week 4 / Device tracking with CAM table  
Tags: switching, cam table, mac address table, arp, cdp, device tracking, troubleshooting, access port, uplink
Language: Russian
Translation pair: articles-en/2026-05/week-04/06-using-cam-table-to-track-down-devices.md

## Summary

Одно из самых практичных умений network administrator - найти, где физически подключено устройство. Обычно процесс начинается с IP address: нужно сгенерировать traffic, получить MAC через ARP, найти этот MAC в CAM/MAC address table, понять port, проверить, не является ли он uplink, затем перейти на следующий switch и повторять, пока не найдешь final access port.

Главная мысль: если ты умеешь follow a MAC address across switches, ты можешь решать огромное количество реальных troubleshooting задач.

## Key Points

- Finding devices is a core real-world networking skill.
- A user complaint often starts with only an IP address or vague symptom.
- Switches forward based on MAC addresses, not IP addresses.
- ARP bridges IP address to MAC address on the local network.
- Generating traffic with `ping` refreshes ARP and MAC table information.
- `show arp` helps find the MAC address for an IP address.
- `show mac address-table` helps find the switch port where a MAC was learned.
- One MAC on a port may indicate a directly connected endpoint.
- Many MAC addresses on a port usually indicate an uplink or downstream switch.
- Device tracing is often hop-by-hop.
- CDP helps identify neighboring Cisco devices.
- `show cdp neighbors` shows what device is connected on a port.
- MAC address tables and ARP caches age out.
- Quiet devices are harder to find than active devices.
- Once the port is found, deeper troubleshooting can begin.

## Notes

### Finding Devices Is the Job

In real networking, a common task is:

```text
Find that device.
```

Examples:

- this device is slow;
- this machine is causing problems;
- security detected suspicious traffic;
- a POS terminal is lagging;
- a rogue device appeared;
- a user plugged something in.

The goal is to trace from a logical clue to a physical location:

```text
IP address -> MAC address -> switch -> port -> cable/wall jack/device
```

### Start with Switch Logic

Switches primarily operate with MAC addresses.

If someone gives you an IP address, the switch cannot directly use that for Layer 2 forwarding.

So first, translate:

```text
IP address -> MAC address
```

That is where ARP helps.

### Generate Traffic First

Tables can be stale or empty if the device has been quiet.

Before looking up the device, generate traffic:

```text
ping 192.168.1.18
```

The ping may cause:

- ARP resolution;
- fresh MAC learning;
- updated switch tables.

A talking device is easier to find than a silent one.

### show arp

Command:

```text
show arp
```

This shows IP-to-MAC mappings known by the device.

Use it to find:

```text
IP address -> MAC address
```

Example workflow:

```text
Target IP: 192.168.1.18
Ping target
show arp
Find MAC for 192.168.1.18
```

Now you have the identity that switches understand.

### show mac address-table

Command:

```text
show mac address-table
```

Use it to answer:

```text
Where did this switch learn that MAC address?
```

The output points to an interface.

That interface may be:

- direct endpoint port;
- uplink to another switch;
- port toward a downstream device;
- trunk carrying many devices.

Do not assume too quickly.

### One MAC on a Port

If one MAC address appears on a port, it may be a direct endpoint.

Example:

```text
Fa0/8 -> POS terminal MAC
```

That might mean:

```text
The device is connected on Fa0/8.
```

Still verify the physical documentation or cable path.

### Many MACs on a Port

If many MAC addresses appear on one interface, that port is likely not the final endpoint.

It may be:

- uplink to another switch;
- trunk port;
- downstream unmanaged switch;
- access point with multiple clients behind it;
- virtualization host.

Common interpretation:

```text
Many MACs on one port = something downstream
```

That means continue tracing.

### Hop-by-Hop Tracing

Device tracing often works like this:

```text
Find MAC on Switch A.
MAC appears on Gi0/1.
Gi0/1 is uplink to Switch B.
Log into Switch B.
Find same MAC.
Repeat until final access port.
```

This is normal.

You are not doing it wrong because it takes multiple steps.

### CDP

CDP means:

```text
Cisco Discovery Protocol
```

CDP lets Cisco devices identify directly connected Cisco neighbors.

Useful command:

```text
show cdp neighbors
```

This can show:

- neighboring device name;
- local interface;
- neighbor interface;
- platform;
- capabilities.

In plain English, it helps answer:

```text
What device is connected to that port?
```

### Using CDP During the Hunt

If the MAC appears on `Fa0/3`, check:

```text
show cdp neighbors
```

If CDP says `Fa0/3` connects to another switch, go there next.

Workflow:

```text
MAC found on Fa0/3
CDP says Fa0/3 -> Switch1
Log into Switch1
show mac address-table
Find same MAC again
Continue
```

This removes guesswork.

### Logical Diagram vs Wiring Closet

Logical diagrams are clean.

Real MDF/IDF closets are often messy:

- patch panels;
- cable bundles;
- unlabeled runs;
- blinking lights;
- access switches;
- uplinks;
- collapsed core/distribution designs.

Practice in diagrams and Packet Tracer still matters because it trains the mental process.

### Collapsed Core Context

Collapsed core means core and distribution roles are combined.

You may still have:

- access switches where endpoints connect;
- upper-layer switches where traffic aggregates;
- uplinks between layers.

When tracing devices, understand whether the port points toward:

- endpoint;
- access switch;
- distribution/collapsed core switch;
- another downstream segment.

### Aging Tables

ARP caches and MAC address tables age out.

That means entries disappear after inactivity.

If you cannot find the device:

- generate traffic;
- ping it;
- ask user to connect/use it;
- check tables again quickly.

Do not forget: quiet devices are harder to find.

### Two Scenarios, Same Method

The same method works for many cases.

Scenario 1:

```text
User says internet is slow.
You start with the user's IP.
Trace to switch port.
Then inspect interface health.
```

Scenario 2:

```text
Security alert gives suspicious IP.
You find MAC.
Trace through switches.
Locate device or wall jack.
```

Different problem, same workflow.

### Full Tracking Workflow

Practical flow:

1. Start with IP address.
2. Generate traffic:

```text
ping <ip-address>
```

3. Find MAC:

```text
show arp
```

4. Find port:

```text
show mac address-table
```

5. If port is uplink, identify neighbor:

```text
show cdp neighbors
```

6. Move to next switch.
7. Repeat until final access port.
8. Verify cable, wall jack and connected device.

### What Happens After You Find the Port

Finding the port is not always the final fix.

It unlocks deeper troubleshooting:

- interface errors;
- CRC errors;
- packet counts;
- speed/duplex mismatch;
- bad cabling;
- wrong VLAN;
- flapping link;
- unexpected device.

But first, you must locate the device.

### Main Takeaway

Tracing devices with CAM table is foundational.

This is not command memorization.

It is operational thinking:

```text
IP clue -> MAC identity -> switch path -> physical port -> real device
```

That is how network administrators turn vague reports into actionable troubleshooting.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| `ping` | Command used to generate traffic and test reachability. |
| `show arp` | Cisco command showing IP-to-MAC mappings. |
| ARP | Address Resolution Protocol; maps IP addresses to MAC addresses locally. |
| CAM table | Table mapping MAC addresses to switch ports. |
| `show mac address-table` | Cisco command showing learned MAC addresses and interfaces. |
| CDP | Cisco Discovery Protocol. |
| `show cdp neighbors` | Cisco command showing directly connected Cisco neighbors. |
| Uplink | Port that leads to another switch or upstream network device. |
| Access port | Port usually connected to an endpoint. |
| MDF | Main Distribution Frame/Facility; central network distribution area. |
| IDF | Intermediate Distribution Frame/Facility; local distribution area. |
| Collapsed core | Design where core and distribution functions are combined. |
| ARP cache | Table storing IP-to-MAC mappings. |
| MAC aging | Process where inactive MAC table entries expire. |

## Questions

### 1. What is the main skill in this lesson?

Tracking a device from IP address to MAC address to switch port.

### 2. Why do you need ARP when starting with an IP address?

Because switches use MAC addresses, so the IP must be mapped to a MAC address first.

### 3. Why generate traffic with ping?

To refresh ARP and MAC table information so the device becomes easier to find.

### 4. What command shows IP-to-MAC mappings?

`show arp`.

### 5. What command shows where a switch learned a MAC address?

`show mac address-table`.

### 6. What does one MAC on a port often suggest?

The port may connect directly to an endpoint.

### 7. What do many MACs on a port often suggest?

The port may be an uplink, trunk or connection to another downstream device.

### 8. Why is device tracing often hop-by-hop?

Because the target MAC may be learned through multiple switches before reaching the final access port.

### 9. What does CDP help identify?

Directly connected Cisco neighbor devices.

### 10. What command shows CDP neighbors?

`show cdp neighbors`.

### 11. Why can a quiet device be hard to find?

Because ARP cache and MAC table entries can age out after inactivity.

### 12. What can you troubleshoot after finding the port?

Interface errors, CRC errors, speed/duplex, cabling, VLANs, link flaps or unexpected devices.

## What To Review Later

- IP-to-MAC workflow.
- `ping` to generate traffic.
- `show arp`.
- `show mac address-table`.
- Uplink vs endpoint port.
- `show cdp neighbors`.
- Hop-by-hop tracing.
- MAC table aging.
- MDF/IDF reality vs logical diagrams.
- Interface troubleshooting after locating the device.
