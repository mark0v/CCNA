# QoS Congestion Delay Jitter And Loss

Source: closed course page  
Date added: 2026-08-21  
Related plan item: Week 16 / QoS congestion delay jitter and loss  
Tags: QoS, congestion, delay, jitter, packet loss, queuing, shaping, policing, voice, video
Language: English
Translation pair: articles/2026-08/week-16/07-qos-congestion-delay-jitter-and-loss.md

## Summary

- `QoS` is needed only where congestion exists.
- Congestion appears when more traffic wants through than a link can transmit.
- By default, networks often forward packets with `FIFO` behavior.
- Treating every packet equally can be bad for voice and video.
- The main congestion symptoms are delay, jitter, and loss.
- `QoS` does not increase link capacity. It manages who receives better treatment.
- Core mechanisms include classification, marking, queuing, shaping, and policing.

## Key Points

- If there is no congestion, `QoS` has little visible effect.
- Bottlenecks can appear on uplinks, WAN links, internet edges, or Wi-Fi.
- A voice packet and a large file download should not always receive the same treatment.
- Delay breaks the natural rhythm of conversation.
- Jitter makes audio and video delivery uneven.
- Packet loss causes audio dropouts, blocky video, and retransmissions.
- `QoS` helps make intentional decisions when bandwidth is not enough for everyone.

## Notes

The most important idea:

```text
If there is no congestion, QoS is not needed.
```

In a world with unlimited bandwidth, every packet could be sent immediately. There would be no need for queues, priorities, markings, or special policies.

Real networks do not work that way.

Links fill up. Devices send too much data at the same time. Several fast ports may converge on one shared uplink. At the internet edge, an entire network may fight for one WAN link.

That is where `QoS` becomes useful.

## What Congestion Is

`Congestion` means overload.

It happens when more data wants to cross a link than the link can transmit at that moment.

Example:

```text
Many devices send traffic into one uplink.
The uplink cannot send everything at once.
Packets begin to wait, delay, or drop.
```

A classic case is many clients connected to a switch at 1 Gbps while the shared uplink is also 1 Gbps. One client is not a problem. Several active clients at once can create a queue.

## Where Bottlenecks Appear

Congestion often appears where many flows converge into one path:

- uplinks between switches;
- WAN links;
- internet edge;
- VPN tunnels;
- Wi-Fi;
- links to cloud services;
- overloaded routers or firewalls.

Wi-Fi is especially sneaky because the radio medium is shared. Clients effectively take turns speaking. The more devices compete for airtime, the more delay and instability appear.

## Why FIFO Is Not Enough

Without special rules, a network may behave like `FIFO`, or `First In, First Out`.

That means:

```text
Whoever arrived first gets sent first.
```

That is simple, but not always smart.

A voice packet for a live conversation may sit behind a large update, backup, or guest download. Technically, that is fair. Practically, it can damage the call.

`QoS` is needed so the network can say:

```text
This traffic is time-sensitive.
Handle it sooner.
```

## Three Congestion Symptoms

When a network is congested, three problems show up most often:

- delay;
- jitter;
- packet loss.

They are especially visible in voice, video, and other real-time applications.

## Delay

`Delay` is latency.

A packet cannot be sent right now, so it waits.

For a web page, that may simply be annoying. For a conversation, delay quickly becomes noticeable.

Real-world example:

```text
Both people start talking at once.
Then both stop.
Then both apologize.
```

That is often delay breaking the natural rhythm of conversation.

## Jitter

`Jitter` is variation in delay between packets.

Example:

```text
The first packet arrives in 80 ms.
The second arrives in 90 ms.
The third arrives in 70 ms.
The fourth arrives in 140 ms.
```

Small variation is acceptable. Too much variation makes it hard for the receiving device to rebuild a smooth audio or video stream.

The problem is not only late packets. The problem is packets arriving with uneven timing.

## Packet Loss

`Packet loss` means packets are lost.

A packet may be dropped because a queue is full. Or it may arrive too late to be useful.

Results:

- voice cuts out;
- audio sounds robotic;
- video becomes blocky;
- streams freeze;
- TCP traffic retransmits.

Loss is especially painful for applications where timing matters more than perfect delivery of every byte.

## Jitter Buffer

A `jitter buffer` is a small buffer on the receiving side.

It briefly holds packets to smooth small timing differences.

Idea:

```text
Do not play audio immediately.
Collect a tiny amount of packets first.
Then play the stream more smoothly.
```

This helps with small amounts of jitter. But if delay variation becomes too large, the buffer cannot hide it. Late packets effectively become loss.

## What QoS Does During Congestion

`QoS` helps the network behave more intelligently when there is not enough room for everyone.

At a high level, it does five things.

### Classification

The network identifies the traffic type.

Examples:

- voice;
- video;
- web;
- backups;
- guest Wi-Fi;
- network management.

### Marking

After classification, traffic receives a mark.

The mark helps downstream devices quickly understand how to treat the packet.

### Queuing

When a link is busy, packets wait in queues.

`QoS` can place important traffic closer to the front or into a separate priority queue.

### Shaping

`Shaping` smooths traffic.

Instead of sending a large burst all at once, a device may temporarily buffer packets and release them more evenly.

This is a gentler way to make traffic fit a target rate.

### Policing

`Policing` is stricter.

It limits traffic and may drop excess packets if a flow exceeds the configured threshold.

It is not "please slow down." It is "you exceeded the limit, so some traffic will be dropped."

## NetworkChuck Coffee Scenario

At NetworkChuck Coffee, one link is shared by:

- a VoIP call to a supplier;
- security camera uploads;
- a large guest Wi-Fi download;
- POS traffic;
- management traffic.

Without `QoS`, everything fights for the same path. The voice call may sound terrible even though the phone and provider are fine. The problem is that important real-time traffic is stuck in a shared queue.

With `QoS`, you can:

- classify voice;
- mark it;
- give it queue priority;
- limit less important traffic;
- smooth bursts where needed.

Same bandwidth. Smarter behavior.

## QoS Does Not Add Capacity

The trap is thinking `QoS` is a way to "speed up the internet."

It is not.

```text
QoS does not create new bandwidth.
```

It helps decide how to use existing capacity when there is not enough for everyone.

If a link is constantly congested, `QoS` can protect important traffic, but it does not remove the root problem. You may still need more bandwidth, a different backup schedule, traffic limits, or a new design.

## Practical Tip

Users rarely speak in technical terms.

They usually do not say:

```text
We have jitter on the WAN link.
```

They say:

```text
Calls sound strange.
Video freezes.
The internet is fine except during meetings.
```

The engineer's job is to translate human complaints into network symptoms:

- delay;
- jitter;
- loss;
- congestion;
- wrong prioritization.

That is where `QoS` stops being theory.

## Main Takeaway

`QoS` matters because real networks become congested.

When there is no congestion, special rules matter much less. When congestion exists, the network must decide who goes first, who waits, and who gets limited.

`QoS` does not increase the link. It helps distribute existing capacity intentionally and protect the traffic that truly matters.

## Commands And Terms

| Term | Meaning |
| --- | --- |
| `QoS` | Quality of Service, traffic management mechanisms used during congestion. |
| congestion | Overload, when traffic exceeds what a link can transmit. |
| `FIFO` | First In, First Out, handling traffic in arrival order. |
| delay | Packet delivery latency. |
| jitter | Variation in delay between packets. |
| packet loss | Packets lost or delivered too late to be useful. |
| jitter buffer | Buffer used to smooth uneven packet delivery. |
| classification | Identifying the traffic type. |
| marking | Tagging traffic for later treatment. |
| queuing | Packet queues during congestion. |
| shaping | Smoothing traffic to a target rate. |
| policing | Strictly limiting traffic, possibly by dropping excess packets. |

## Questions

### 1. When is QoS actually needed?

Answer: When congestion exists and the network must decide which traffic receives better service.

### 2. What is congestion?

Answer: A situation where more traffic exists than a link or device can transmit at that moment.

### 3. How is delay different from jitter?

Answer: `Delay` is latency itself, while `jitter` is variation in delay between packets.

### 4. What does shaping do?

Answer: It smooths traffic bursts by temporarily buffering packets and releasing them more evenly.

### 5. What does policing do?

Answer: It limits traffic and may drop packets when a flow exceeds its configured limit.

## Review Later

- Why `QoS` is needed only during congestion.
- Where bottlenecks appear.
- The difference between delay, jitter, and packet loss.
- How a jitter buffer works.
- The five basic `QoS` mechanisms.
- Why `QoS` does not increase bandwidth.
