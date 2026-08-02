# CDP One-Hop Cisco Discovery

Source: closed course page  
Date added: 2026-08-02  
Related plan item: Week 14 / CDP one-hop Cisco discovery  
Tags: CDP, Cisco Discovery Protocol, neighbor discovery, troubleshooting, PoE, voice VLAN, network documentation
Language: English
Translation pair: articles/2026-08/week-14/07-cdp-one-hop-cisco-discovery.md

## Summary

- CDP shows directly connected Cisco neighbors.
- It does not map the entire network at once; it gives you the next hop.
- Main commands are `show cdp neighbors` and `show cdp neighbors detail`.
- Detailed output can often show the neighbor's IP address.
- CDP sends updates every 60 seconds.
- Holdtime is usually 180 seconds, so entries may remain briefly after a device disconnects.
- CDP is useful for discovery, but on user-facing ports it can expose too much information.

## Key Points

- CDP is especially useful in poorly documented Cisco networks.
- It helps quickly identify what is connected to a router or switch.
- Discovery is one hop at a time: the device shows only direct neighbors.
- With `show cdp neighbors detail`, you can collect IP addresses and move from neighbor to neighbor.
- CDP can carry not only identity, but also operational data such as PoE and voice VLAN information.
- In production, it is often reasonable to keep CDP between network devices and disable it on user-facing access ports.

## Notes

In an ideal world, every network has a current diagram. In reality, you often get a rack, a bundle of cables, an outdated diagram, and a message that the previous administrator left months ago.

In that situation, CDP, or Cisco Discovery Protocol, gives you a starting point. It lets you ask a device:

```text
Who is directly connected next to you?
```

The answer will not show the whole network. It will show the next step. During troubleshooting, that is often enough.

## How CDP Works

CDP is Cisco's discovery protocol for directly connected neighbors.

Cisco devices periodically send control messages to neighbors. These messages are not routed through the whole network. They stay on the local link.

So CDP answers one question:

```text
What is directly connected to this device?
```

That limitation is useful. You log in to one switch, check neighbors, move to the next device, check again, and gradually build the real map.

## Main Command

Quick view:

```text
show cdp neighbors
```

It usually shows:

- neighbor device ID;
- local interface;
- holdtime;
- capabilities;
- platform;
- neighbor port ID.

Output logic:

```text
Local Interface -> Neighbor Device -> Neighbor Port
```

That helps identify which cable goes where without pulling it from the rack.

## Detailed Output

When you need the next step, use:

```text
show cdp neighbors detail
```

This output often provides more:

- neighbor IP address;
- software version;
- platform;
- capabilities;
- interface details;
- management address.

The IP address is especially important. If the neighbor is reachable, you can connect to it with SSH or Telnet and continue mapping from that side.

Discovery becomes action:

```text
find neighbor -> see IP -> connect -> repeat
```

## Timers

CDP sends updates every 60 seconds.

This is the hello interval: the device regularly tells neighbors that it is still present.

CDP also has a holdtime, usually 180 seconds. That is how long a neighbor entry can remain in the table if new CDP messages stop arriving.

Why this matters:

- a disconnected device may still appear in the table;
- after a physical disconnect, the entry does not vanish instantly;
- during troubleshooting, a stale entry should not be mistaken for a live link.

If a cable was unplugged but the neighbor still appears, check the timer. The entry may simply not have expired yet.

## More Than Neighbor Mapping

CDP's primary job is discovery, but over time it became a carrier for more operational information.

It can help in scenarios such as:

- PoE;
- IP phones;
- voice VLAN;
- platform identification;
- duplex mismatch hints;
- management reachability.

PoE, or Power over Ethernet, lets a switch power a device over the Ethernet cable. An IP phone or wireless access point can communicate its power needs, and the switch can manage its power budget more intelligently.

Voice VLAN is another example. An IP phone can learn which VLAN to use for voice traffic and fit into the network correctly.

So CDP does not only answer "who are you?" It can also help answer "what do you need to operate?"

## CDP And LLDP

CDP is Cisco-proprietary. It fits Cisco environments well.

LLDP is the standards-based discovery option for mixed-vendor networks.

Comparison:

| Protocol | Where it is especially useful |
| --- | --- |
| CDP | Cisco-heavy network. |
| LLDP | Mixed-vendor network. |

Do not assume CDP is old news. On many Cisco devices, it is enabled by default, which often makes it the fastest available source of information.

## Security

CDP's convenience has a cost.

If CDP is enabled on a port where an untrusted device can connect, that device may learn useful details:

- switch name;
- platform;
- software version;
- interface information;
- management IP;
- topology hints.

For an administrator, that is helpful. For an attacker, it is reconnaissance.

So the real network decision should be intentional:

- keep CDP on network-to-network links where operations need it;
- disable it on user-facing access ports where unnecessary;
- follow the organization's security policy.

Commands:

```text
no cdp run
cdp run

interface fa0/10
 no cdp enable
```

`no cdp run` disables CDP globally. `no cdp enable` disables it on one interface.

## NetworkChuck Coffee Scenario

NetworkChuck Coffee has lost its current diagram.

The administrator logs in to the first router or switch and runs:

```text
show cdp neighbors detail
```

They write down:

- neighbor name;
- local interface;
- remote port;
- neighbor IP address;
- platform;
- device role.

Then they connect to the neighbor and repeat the process.

After a few passes, a real map appears: which switches connect, where the router is, where access points connect, and which ports are uplinks.

That is faster than waiting for perfect documentation that may not exist.

## Verification

Useful commands:

```text
show cdp
show cdp neighbors
show cdp neighbors detail
show cdp interface
show running-config | include cdp
```

Check:

- whether CDP is enabled globally;
- which interfaces have it active;
- whether expected neighbors are visible;
- whether local and remote ports match documentation;
- whether unexpected devices appear;
- whether CDP is exposed on unnecessary access ports.

## Practical Habit

When entering an unfamiliar Cisco network:

1. Start from a trusted router or switch.
2. Run `show cdp neighbors detail`.
3. Record neighbors, interfaces, and IP addresses.
4. Move to the next device.
5. Build the topology map.
6. Update documentation.
7. Decide where CDP should be disabled.

This simple workflow quickly turns chaos into a usable map.

## Main Takeaway

CDP does not show the entire network at once. It shows the next directly connected neighbor.

That is enough to move forward. In a poorly documented Cisco environment, CDP gives you a fast way to build a map, find uplinks, see remote ports, and obtain neighboring device addresses.

Use it like a flashlight: one hop at a time. But remember security, and do not leave discovery information exposed where anyone can read it.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| CDP | Cisco Discovery Protocol, Cisco's neighbor discovery protocol. |
| `show cdp neighbors` | Short command to view CDP neighbors. |
| `show cdp neighbors detail` | Detailed CDP output with additional neighbor information. |
| device ID | Neighbor device name in the CDP table. |
| local interface | Local interface where the neighbor is visible. |
| port ID | Interface on the neighboring device. |
| holdtime | Time a record remains without new CDP updates. |
| PoE | Power over Ethernet, powering a device over Ethernet. |
| voice VLAN | VLAN for voice traffic, often used by IP phones. |
| reconnaissance | Information gathering before an attack. |

## Questions

### 1. What does CDP show?

Answer: Directly connected Cisco neighbors and details about ports, platform, and capabilities.

### 2. Why does CDP not show the whole network at once?

Answer: It works only with directly connected neighbors on the local link.

### 3. Why use `show cdp neighbors detail`?

Answer: It provides expanded details, often including the neighbor's IP address.

### 4. Why does holdtime matter during troubleshooting?

Answer: A record can remain in the table until the timer expires, even after the device is disconnected.

### 5. Why can CDP be risky on access ports?

Answer: It can expose device names, software version, platform, and management IP to an untrusted device.

## What To Review Later

- `show cdp neighbors`.
- `show cdp neighbors detail`.
- CDP hello interval of 60 seconds.
- CDP holdtime of 180 seconds.
- Difference between global and per-interface disabling.
- When to use CDP and when to use LLDP.
