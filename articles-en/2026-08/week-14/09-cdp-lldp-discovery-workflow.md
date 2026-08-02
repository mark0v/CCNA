# CDP LLDP Discovery Workflow

Source: closed course page  
Date added: 2026-08-02  
Related plan item: Week 14 / CDP LLDP discovery workflow  
Tags: CDP, LLDP, neighbor discovery, troubleshooting workflow, network documentation, topology mapping, switch operations
Language: English
Translation pair: articles/2026-08/week-14/09-cdp-lldp-discovery-workflow.md

## Summary

- CDP and LLDP matter not just as exam topics, but as a practical way to start understanding an unfamiliar network.
- If you can access one switch or router, you can gradually build a neighbor map.
- Discovery commands help turn an unknown network into an understandable topology map.
- The main value is reducing guesswork during troubleshooting.
- A large lab is not required here; the real skill is knowing how to begin from one device.
- Document as you discover, or the knowledge stays only in someone's head.

## Key Points

- Do not trust old labels, memory, or verbal assumptions without verification.
- Start with one known device.
- Run `show cdp neighbors` or `show lldp neighbors`.
- Record local interface, neighbor, remote port, and management address.
- Move to the next device and repeat the process.
- Even a rough map is better than no documentation.
- Discovery protocols do not replace documentation; they help build or verify it.

## Notes

After learning CDP and LLDP, it is easy to expect a large final lab. But these protocols are most useful in a real situation: you are facing an unfamiliar network and do not know what connects where.

That is where discovery becomes the starting point.

If you can access even one device, you can ask it:

```text
Who is next to you?
```

One neighbor leads to the next. The next shows another part of the network. Gradually, the network stops being blinking ports and becomes a map.

## Discovery As A Starting Point

When documentation is missing, the first task is not fixing everything immediately.

The first task is:

```text
Understand what I am looking at.
```

CDP and LLDP help with that. They show directly connected neighbors and give you points for the next move.

You usually need to learn:

- which switch connects to the current switch;
- where the router is;
- which port is an uplink;
- which port leads to an access point;
- which devices do not match documentation;
- which interfaces should be checked next.

This is especially important during an outage. The faster you understand topology, the faster you stop troubleshooting blindly.

## Why There Is No Giant Final Lab

Discovery protocols are technically simple.

The commands are simple too:

```text
show cdp neighbors
show cdp neighbors detail
show lldp neighbors
show lldp neighbors detail
```

The skill is not memorizing a long configuration. The skill is using these commands as a workflow.

In a real network, you often do not build a polished demo. You:

- connect to an available device;
- check neighbors;
- record links;
- move forward;
- verify the next section.

That chain is simple, but very effective.

## Workflow

Practical order:

1. Find one known device you can access.
2. Connect by console, SSH, or another approved method.
3. Run `show cdp neighbors` and/or `show lldp neighbors`.
4. Record neighbor device, local interface, and remote port.
5. If you need the neighbor address, run the detailed command.
6. Connect to the next device.
7. Repeat discovery.
8. Draw a rough topology map.
9. Compare it with existing documentation.
10. Update documentation and mark unknown areas.

The main idea: you do not need the whole network at once. You need the next reliable step.

## What To Record

Minimum table:

| Field | Why it matters |
| --- | --- |
| Device | Where the command was run. |
| Local interface | The local port where the neighbor appears. |
| Neighbor | The neighboring device name. |
| Remote port | The port on the neighboring device. |
| Protocol | CDP or LLDP. |
| Management address | How to connect to the neighbor. |
| Notes | Unusual details or mismatches. |

Even if this starts on paper, it is better than nothing. Later it can become a clean diagram.

## NetworkChuck Coffee Scenario

NetworkChuck Coffee opens a new site or inherits an old network.

In the closet:

- unlabeled switches;
- unclear uplinks;
- old cables;
- no current diagram;
- POS and back-office systems depend on the network.

The administrator starts from one known switch:

```text
show cdp neighbors detail
show lldp neighbors detail
```

Then they identify:

- which switch feeds POS systems;
- where the back office is;
- where the internet router sits;
- where access points connect;
- which link is an uplink;
- which devices need follow-up.

When card payments fail during the morning rush, that map is not theory. It is how you know where to look.

## Do Not Trust Blindly

Discovery protocols are useful, but read the output carefully.

Possible traps:

- a neighbor entry may be stale because of holdtime;
- CDP may not see a non-Cisco device;
- LLDP may be disabled;
- an access port may expose too much information;
- documentation may contradict reality;
- a device name may be old or wrong.

Good approach:

```text
check discovery -> compare with physical/config evidence -> document the result
```

## Verification

Commands:

```text
show cdp neighbors
show cdp neighbors detail
show cdp interface
show lldp neighbors
show lldp neighbors detail
show lldp interface
show interfaces status
show interfaces trunk
```

Confirm:

- expected neighbors are visible;
- active discovery protocols are known;
- local and remote ports match;
- unexpected devices are identified;
- discovery is enabled where operations need it;
- discovery is disabled where information should not be exposed.

## Main Takeaway

CDP and LLDP do not give you the final diagram. They give you the beginning.

They let you move from "I do not know what is connected here" to "I can see the next hop and keep going." During troubleshooting, that is a major difference.

Use discovery as a habit: find a known device, check neighbors, record links, move forward, and update documentation. That is how an unknown network becomes supportable.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| CDP | Cisco Discovery Protocol, Cisco's neighbor discovery protocol. |
| LLDP | Link Layer Discovery Protocol, standards-based discovery protocol. |
| known device | Device you can safely access to begin investigation. |
| neighbor | Directly connected device. |
| topology map | Diagram of the network's real connections. |
| local interface | Port on the current device. |
| remote port | Port on the neighboring device. |
| management address | Address used to connect to the neighboring device. |
| rough map | Draft diagram built during troubleshooting. |

## Questions

### 1. Why are CDP and LLDP useful without a large lab?

Answer: Their main value is a real workflow: start from one device and gradually reveal the topology.

### 2. Where should you start in an unfamiliar network?

Answer: With a known device you can access, then run neighbor discovery.

### 3. What should you record during discovery?

Answer: Device, local interface, neighbor, remote port, protocol, management address, and notes.

### 4. Why should old labels not be trusted blindly?

Answer: Cables and devices may have changed while documentation was not updated.

### 5. What is the main result of discovery?

Answer: Understanding the real topology and getting the next reliable troubleshooting step.

## What To Review Later

- `show cdp neighbors detail`.
- `show lldp neighbors detail`.
- Step-by-step discovery workflow.
- How to keep topology notes.
- Where discovery protocols should be disabled.
- Difference between documentation and the real network state.
