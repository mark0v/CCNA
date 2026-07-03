# EtherChannel Load Balancing

Source: closed course page  
Date added: 2026-07-03  
Related plan item: Week 10 / EtherChannel load balancing  
Tags: EtherChannel, load balancing, port-channel, hashing, LACP, bandwidth
Language: English
Translation pair: articles/2026-07/week-10/05-etherchannel-load-balancing.md

## Summary

- EtherChannel looks like one logical link, but separate physical member links still exist inside it.
- One conversation usually uses one physical link, not the full combined bandwidth of the bundle.
- EtherChannel is most useful when many simultaneous flows exist.
- Traffic distribution depends on a hash-based load balancing algorithm.
- The load balancing method should be verified and tuned for the real traffic pattern.

## Key Points

- Two 1 Gbps links in an EtherChannel do not guarantee 2 Gbps for one flow.
- The switch chooses a member link through an algorithm based on MAC/IP/port fields.
- The same input values usually produce the same output link.
- Uneven member link utilization does not automatically mean the EtherChannel is broken.
- `show etherchannel load-balance` and `port-channel load-balance` are used to verify and tune behavior.

## Notes

EtherChannel is often described as "bundling multiple links into one logical channel." That is true, but it can lead to a bad assumption. A logical channel does not mean one single flow automatically uses the combined bandwidth of every member link.

If an EtherChannel has two 1 Gbps physical links, one PC copying a file to one server does not normally get 2 Gbps. That conversation usually lands on one physical link and stays there. The gain appears when many different conversations exist: different hosts, servers, applications, and sessions can be distributed across different member links.

Example at NetworkChuck Coffee:

- an inventory workstation talks to a server;
- a POS terminal sends data to a back-office system;
- a camera server writes archive traffic;
- Wi-Fi clients use internal resources.

Each individual flow may use one link, but the bundle as a whole can be used more effectively. That is why EtherChannel provides aggregate bandwidth, not magical acceleration for one conversation.

The switch does not distribute traffic based on human-style judgment, and it does not try to perfectly equalize graphs in real time. It uses a load balancing algorithm. Usually this is a hash-based decision: the switch takes selected frame or packet fields, runs them through an algorithm, and chooses a physical member link.

Available input fields depend on the switch model and IOS version, but common options include:

| Option | What it uses |
| --- | --- |
| `src-mac` | Source MAC address. |
| `dst-mac` | Destination MAC address. |
| `src-dst-mac` | Source and destination MAC addresses together. |
| `src-ip` | Source IP address. |
| `dst-ip` | Destination IP address. |
| `src-dst-ip` | Source and destination IP addresses together. |

If the algorithm uses source MAC, traffic from one sender may consistently land on the same member link. That is predictable: the same input gives the same hash result. But it can also make utilization uneven. One link may be busy while another is mostly idle, and that does not automatically mean EtherChannel is broken.

That is why the default load balancing method should not be trusted blindly. Different platforms and IOS versions can have different defaults. The right approach is to check the current operational method:

```text
Switch# show etherchannel load-balance
```

If the distribution does not fit the traffic pattern, the method can be changed in global configuration mode:

```text
Switch(config)# port-channel load-balance src-dst-mac
```

Choose the algorithm based on which fields actually vary in the traffic:

- many clients to one server may benefit from source-based or source-destination methods;
- heavy server-to-server traffic may work better with source-destination IP;
- pure Layer 2 segments may fit MAC-based options better;
- routed uplinks often benefit from IP-based uniqueness.

The idea is simple: the more useful uniqueness the hash receives, the better chance flows have to spread across member links. But "better" should be judged by real traffic, not by the option name.

After changing the load balancing method, configure the other side of the EtherChannel too. Both switches participate in forwarding, so operational discipline means aligning the approach on both ends. Even if a mismatch is not an immediate outage, it can complicate troubleshooting and produce confusing utilization.

Workflow:

1. Check the current method:

```text
Switch# show etherchannel load-balance
```

2. Choose a new method for the traffic pattern:

```text
Switch(config)# port-channel load-balance src-dst-mac
```

3. Repeat on the other side of the channel.

4. Verify again:

```text
Switch# show etherchannel load-balance
Switch# show etherchannel summary
```

Main point: EtherChannel provides aggregate throughput across multiple conversations. It is not single-flow bandwidth multiplication. Once that is clear, load balancing stops looking strange and becomes a normal design tool.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `show etherchannel load-balance` | Shows the current EtherChannel load balancing method. |
| `port-channel load-balance src-dst-mac` | Configures balancing based on source and destination MAC addresses. |
| Hashing | Mathematical selection of a member link based on chosen input fields. |
| Flow | A logical conversation between endpoints, such as host-to-server traffic. |
| Aggregate bandwidth | The total usable capacity of the bundle across many flows. |
| Member link | A physical interface inside the EtherChannel bundle. |

## Questions

### 1. Why does one flow usually not use the full EtherChannel bandwidth?

Answer: EtherChannel distributes flows across member links with a hash-based algorithm. One conversation usually receives one physical link to preserve frame ordering.

### 2. What does aggregate bandwidth mean?

Answer: It means the total bundle capacity across many simultaneous conversations, not guaranteed speed for one traffic flow.

### 3. Why can member links be unevenly utilized?

Answer: The hash algorithm uses selected input fields. If the traffic pattern is repetitive, many flows can land on the same physical link.

### 4. How do you check the current load balancing method?

Answer: Use `show etherchannel load-balance`.

### 5. Why should the algorithm be chosen for the traffic pattern?

Answer: The best algorithm depends on which fields actually differ between conversations. If the selected fields do not vary much, distribution will be weak.

## What To Review Later

- Which load balancing options a specific Cisco platform supports.
- The difference between MAC-based and IP-based hashing.
- Why EtherChannel preserves packet order within one flow.
- How to read member link utilization during troubleshooting.
