# NTP Synchronization And Stratum

Source: closed course page  
Date added: 2026-08-16  
Related plan item: Week 15 / NTP synchronization and stratum  
Tags: NTP, stratum, ntp master, ntp server, loopback, time synchronization, Cisco IOS
Language: English
Translation pair: articles/2026-08/week-15/03-ntp-synchronization-and-stratum.md

## Summary

- Manual clock setting is better than wrong time, but it does not scale.
- NTP synchronizes time between network devices automatically.
- In NTP, servers provide time and clients synchronize to them.
- Stratum shows how close a device is to the original time source.
- Lower stratum means a more authoritative source.
- A Cisco router can be made a local time source with `ntp master`.
- A client device uses `ntp server <ip-address>`.
- If synchronization fails, check IP connectivity and time zone first.

## Key Points

- The goal of NTP is not setting correct time once; it is keeping devices aligned.
- Accurate timestamps matter for logs, certificates, VPN, authentication, and troubleshooting.
- Stratum 1 is closest to the original precise time source.
- Stratum 16 means the source is not trusted.
- In a lab, a router can act as `ntp master` with the default stratum of 8.
- In production, it is usually better to use internal NTP servers that synchronize to upstream sources.
- A loopback interface is useful as a stable NTP identity.

## Notes

Manually setting time on a Cisco device is useful as a quick fix. It is better than leaving a router or switch with a default date from the past.

But as soon as there is more than one device, manual clock setting becomes a problem:

- clocks drift;
- different people set different times;
- some devices are missed;
- reboot behavior may differ;
- logs stop lining up again.

The main goal:

```text
All devices should automatically agree on what time it is.
```

That is what NTP is for.

## What NTP Does

NTP, or Network Time Protocol, gives devices a shared time source.

Simple model:

| Role | Function |
| --- | --- |
| NTP server | Provides time. |
| NTP client | Requests time and synchronizes. |

An NTP server can be:

- a Linux server;
- a Windows server;
- a public NTP server;
- a router;
- a firewall;
- a dedicated time source.

For a small lab, a router can be made the local master. For production, a better design is controlled: a few internal devices synchronize to reliable upstream sources, and the rest of the network points internally.

## Why This Matters

At NetworkChuck Coffee, wrong time quickly damages troubleshooting.

Imagine:

- a switch says an interface dropped at 09:01;
- a router reports a routing event at 08:54;
- a firewall shows a deny later but with another time zone;
- a POS system reports failure with yet another timestamp.

Now the event order is unclear. If the order is unclear, the investigation becomes slower and less reliable.

Consistent time makes the network behave like one coordinated system instead of separate boxes with separate clocks.

## Stratum

Stratum is the number that shows how close a device is to the original precise time source.

Simplified:

| Stratum | Meaning |
| --- | --- |
| `stratum 1` | Directly connected to a very accurate time source. |
| `stratum 2` | Gets time from stratum 1. |
| `stratum 3` | Gets time from stratum 2. |
| `stratum 16` | Not considered a trusted source. |

Lower stratum is more authoritative.

This prevents the network from building endless time chains. If devices synchronize from one another forever without control, clock drift eventually turns accurate time into nonsense.

## Router As NTP Master

In a lab, you can manually set the router clock first, then make it the local NTP source.

Example:

```text
show clock
clock set 11:22:30 12 Sep 2024

configure terminal
ntp master
end

show ntp status
```

The `ntp master` command tells the router to act as an NTP server for other devices.

On Cisco, this master often reports the default stratum of 8. That is normal for a lab: the router is saying it is a time source, but not pretending to be an atomic clock.

If the router is synchronized to itself as master, the wording may look odd at first, but the logic is simple: in that small network, it is the authority.

## Client Side

On the switch or another client device, configure the NTP server.

Example:

```text
configure terminal
ntp server 10.1.0.1
end

show ntp status
show clock detail
```

The command:

```text
ntp server <ip-address>
```

tells the device to get time from that server.

Important: NTP is not magic. If the switch cannot ping the router, synchronization will not work. Connectivity first, service second.

Check:

- IP address on the client;
- default gateway or route;
- VLAN/interface state;
- ACL;
- reachability to the NTP server;
- time zone.

## Synchronization Is Not Always Instant

After configuring NTP, wait a bit.

Sometimes `show ntp status` initially says unsynchronized. That is not always a failure. NTP may need a minute or more before the device selects the server and synchronizes.

Check order:

1. IP connectivity to the server exists.
2. `ntp server` is configured correctly.
3. `show ntp status` changes to synchronized.
4. `show clock detail` shows NTP as the source.
5. Displayed time looks correct after time zone is considered.

## Loopback As A Stable Address

If a router has multiple physical interfaces, which IP should clients use as the NTP server address?

A practical answer is a loopback interface.

A loopback is a virtual interface that does not depend on one physical port staying up. If routing to the loopback is correct, devices can use one stable address.

Example idea:

```text
interface loopback0
 ip address 10.1.0.1 255.255.255.255
```

Then clients use:

```text
ntp server 10.1.0.1
```

On real gear, you can also control the NTP source interface. Some simulators may limit that command, but the design idea still matters: stable identity beats a random physical interface.

## Time Zone

NTP usually synchronizes time around a UTC-style reference, while the local device displays time using its time zone.

If displayed time looks wrong, NTP is not always the problem.

Check in order:

1. Whether NTP is synchronized.
2. What source `show clock detail` shows.
3. Which time zone is configured.
4. Whether there is daylight saving mismatch.

Verify synchronization first, then troubleshoot display offset.

## Production Design

In production, hundreds of devices usually should not point directly to a public NTP server.

Cleaner design:

- one or more internal NTP servers synchronize to upstream sources;
- network devices use internal NTP servers;
- redundancy is used;
- authentication is enabled when needed;
- source interfaces and ACLs are intentional.

Benefits:

- less dependency on internet access;
- better control;
- one policy;
- less external traffic;
- clearer troubleshooting.

## NetworkChuck Coffee Scenario

NetworkChuck Coffee grows.

One router can act as internal NTP master in a lab or small environment. Switches and access points synchronize to it.

Result:

- logs line up by time;
- troubleshooting becomes cleaner;
- security events can be compared;
- POS and back-office systems feel more coordinated;
- during an outage, the timeline is easier to build.

It is not the flashiest setting, but without it the network quickly starts telling contradictory stories.

## Verification

Commands:

```text
show clock
show clock detail
show ntp status
show ntp associations
ntp master
ntp server 10.1.0.1
clock timezone AZ -7
```

Check:

- correct clock on the master;
- whether `ntp master` is enabled;
- which stratum the device reports;
- connectivity from client to server;
- whether the client synchronized;
- whether `show clock detail` shows NTP as the source;
- whether time zone is correct.

## Main Takeaway

Manual clock setting is a useful temporary measure, but it does not solve consistent time across a network.

NTP solves exactly that: it gives network devices a shared time source and keeps them synchronized. Stratum helps identify source authority, `ntp master` can create a local source, and `ntp server` points clients to it.

Get connectivity first, configure NTP, wait for synchronization, and only then trust timestamps.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| NTP | Network Time Protocol, time synchronization protocol. |
| `ntp master` | Makes a Cisco device a local NTP source. |
| `ntp server` | Points a client device to an NTP server. |
| `show ntp status` | Shows NTP synchronization state. |
| `show ntp associations` | Shows NTP associations. |
| stratum | Distance level from the original time source. |
| `stratum 16` | Untrusted or unsynchronized state. |
| loopback interface | Virtual interface with a stable IP address. |
| clock drift | Gradual time divergence. |
| UTC | Baseline global time standard. |

## Questions

### 1. Why is manual clock setting a trap?

Answer: It can fix one device, but it does not keep many devices synchronized over time.

### 2. What does NTP do?

Answer: It synchronizes device time to a shared source.

### 3. What does stratum mean?

Answer: How close an NTP source is to the original precise time source.

### 4. Which command makes a router a local NTP source?

Answer: `ntp master`.

### 5. What should you check if NTP does not synchronize?

Answer: IP connectivity, correct `ntp server`, routes, ACLs, interface state, and time zone.

## What To Review Later

- `ntp master`.
- `ntp server <ip-address>`.
- `show ntp status`.
- `show ntp associations`.
- Meaning of stratum.
- Using loopback as a stable NTP address.
- Difference between synchronization and local time display.
