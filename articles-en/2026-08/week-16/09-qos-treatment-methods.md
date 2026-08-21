# QoS Treatment Methods

Source: closed course page  
Date added: 2026-08-21  
Related plan item: Week 16 / QoS treatment methods  
Tags: QoS, trust boundary, queuing, WRED, shaping, policing, LLQ, tail drop, traffic starvation
Language: English
Translation pair: articles/2026-08/week-16/09-qos-treatment-methods.md

## Summary

- Classification and marking tell the network what traffic is.
- `QoS` treatment methods decide what happens during congestion.
- A `trust boundary` defines which markings the network trusts.
- `FIFO` handles packets in arrival order.
- `Tail drop` drops packets when the queue is full.
- `WRED` begins dropping some lower-priority traffic early to avoid harsh congestion behavior.
- `Shaping` smooths traffic by buffering.
- `Policing` enforces a hard limit and may drop excess traffic.
- `LLQ` prioritizes delay-sensitive traffic while policing that priority queue.

## Key Points

- If there is no congestion, queuing, shaping, policing, and `WRED` have little visible effect.
- Do not blindly trust markings from any device.
- At the edge, define where trust begins.
- `Tail drop` does not care whether traffic is important.
- `WRED` is useful for TCP flows because it helps avoid synchronized slowdowns.
- `Shaping` is better when traffic matters and delay is acceptable.
- `Policing` is better when a hard ceiling is required.
- `LLQ` is commonly used for voice and other real-time traffic.

## Notes

Earlier, we handled the first two `QoS` tasks:

```text
Classify traffic.
Mark traffic.
```

Now the network knows what the traffic is: voice, video, web, backup, guest traffic, or something else.

The next question is:

```text
What should happen when there is not enough room for everyone?
```

That is where treatment methods begin: queuing, `WRED`, shaping, policing, and `LLQ`.

## Trust Boundary

Before treatment, you must decide which markings can be trusted.

A `trust boundary` is the place in the network where you decide:

```text
From here, I trust the marking.
Before this point, I verify, reset, or remark traffic myself.
```

This matters because any device can try to mark itself as high priority.

Examples:

- user laptop;
- game console;
- misconfigured application;
- malware;
- cheap device on the network.

If the network blindly trusts every mark, `QoS` becomes chaos.

Practical idea:

```text
Trust markings only from controlled devices.
At the edge, inspect, reset, or remark traffic.
```

## When Treatment Methods Matter

Queuing, shaping, policing, and `WRED` matter during congestion.

If the link is free, packets pass without a fight.

But when the link is full, the network must decide:

- who goes first;
- who waits;
- who receives less bandwidth;
- who gets dropped;
- whose priority is limited.

`QoS` does not make a slow link magically fast. It decides who suffers first when the link is full.

## FIFO

`FIFO`, or `First In, First Out`, is the simplest approach.

Logic:

```text
First packet in, first packet out.
```

It is simple, but not intelligent.

A voice packet can sit behind a large backup. Payment traffic can wait behind a guest download. For a business network, that is a bad outcome.

`FIFO` understands arrival order, not importance.

## Tail Drop

When a queue fills, a device may begin dropping new packets at the end of the queue.

That is called `tail drop`.

Problem:

```text
Tail drop does not ask whether the packet is important.
Queue full means packet dropped.
```

Voice, database traffic, web, and guest traffic can all be dropped the same way.

## Global Synchronization

`Tail drop` can create another problem: `global synchronization`.

When many TCP flows see drops at the same time, they reduce their sending rate at the same time. Then they increase again together. Then they hit the ceiling again.

The result is a sawtooth pattern:

```text
Traffic rises.
The queue fills.
Many flows lose packets.
All reduce speed.
Then all grow again.
```

Bandwidth is used unevenly and inefficiently.

## WRED

`WRED`, or `Weighted Random Early Detection`, handles this more gently.

Instead of waiting for a full queue, `WRED` begins dropping some packets early.

Key point:

```text
Lower-priority traffic starts suffering earlier.
```

If markings include different drop preferences, `WRED` can use them when deciding what to drop first.

This is especially useful for TCP because individual flows back down earlier and not all at once.

Results:

- fewer sharp collapses;
- less global synchronization;
- smoother congestion behavior;
- more protection for important traffic.

## Shaping

`Shaping` is a gentler traffic limiter.

It says:

```text
You are sending too fast.
I will temporarily buffer packets and release them more smoothly.
```

Shaping delays traffic, but does not necessarily drop it.

It fits when:

- traffic is important;
- small delay is acceptable;
- packet loss is undesirable;
- bursts need smoothing;
- a provider expects a specific rate.

Example: sending traffic more smoothly toward a WAN link.

## Policing

`Policing` is stricter.

It says:

```text
You exceeded the limit.
Excess traffic will be dropped or remarked.
```

Policing does not try to preserve every packet.

It fits when:

- a hard ceiling is required;
- traffic must not consume the link;
- loss is acceptable;
- guest traffic needs limiting;
- aggressive applications must be contained.

Practical difference:

| Method | Behavior |
| --- | --- |
| `Shaping` | Buffers and smooths. |
| `Policing` | Enforces strictly and may drop. |

## Queuing Methods

Queues decide who goes first when traffic types compete for one link.

### FIFO

The simplest option. No priority.

### WFQ

`WFQ`, or `Weighted Fair Queuing`, gives some preference to lower-bandwidth flows.

This can help interactive traffic such as remote sessions. But it may not be enough for constant real-time streams like voice.

### Custom Queuing

`Custom Queuing` assigns portions of bandwidth to different classes and services queues in rotation.

Problem: if voice waits its turn, the delay may already be noticeable.

### Priority Queuing

`Priority Queuing` lets the priority queue go first.

That sounds great, but it has a risk:

```text
If too much traffic enters the priority queue, other queues starve.
```

That is called `traffic starvation`.

## LLQ

`LLQ`, or `Low Latency Queuing`, combines several good ideas.

It provides:

- a real priority queue for delay-sensitive traffic;
- policing for that priority queue;
- class-based queues for other important traffic;
- fair queueing for everything else.

The important part: the priority queue exists, but it is limited.

Otherwise, voice or other high-priority traffic could consume the whole link and harm other applications.

`LLQ` is especially useful for voice because voice needs low delay and predictable delivery.

## NetworkChuck Coffee Scenario

At NetworkChuck Coffee, one link is shared by:

- a VoIP call to a supplier;
- POS systems;
- back-office file uploads;
- cameras;
- guest Wi-Fi;
- network management.

Without `QoS`, everything competes equally. If a large upload starts in the back office, a voice call can become choppy.

With `QoS`, you can:

- trust markings only from managed devices;
- remark user traffic at the edge;
- prioritize voice traffic with `LLQ`;
- limit guest traffic with policing;
- smooth business traffic with shaping;
- use `WRED` for less important TCP traffic.

This is not theory. This protects what keeps the business running.

## Practical Tip

Use shaping when delivery can be delayed a little but packet loss would hurt.

Use policing when a hard limit is required and excess traffic should not consume the link.

Do not trust markings from random devices.

And remember:

```text
The priority queue must be limited.
```

Otherwise, the solution for one traffic type becomes a problem for everything else.

## Main Takeaway

Classification and marking tell the network what traffic is.

Treatment methods decide what happens when the link is full.

`WRED` reduces harsh loss behavior. `Shaping` smooths traffic. `Policing` enforces hard limits. Queues decide who goes first. `LLQ` provides low latency for important real-time traffic while preventing the priority queue from taking all bandwidth.

## Commands And Terms

| Term | Meaning |
| --- | --- |
| `trust boundary` | Boundary where the network begins trusting traffic markings. |
| `FIFO` | First In, First Out, handling traffic in arrival order. |
| `tail drop` | Dropping packets when the queue is full. |
| `global synchronization` | Many TCP flows slowing down at the same time after packet drops. |
| `WRED` | Weighted Random Early Detection, early dropping based on priority. |
| `shaping` | Smoothing traffic by buffering. |
| `policing` | Strictly limiting traffic, possibly by dropping excess traffic. |
| `WFQ` | Weighted Fair Queuing. |
| `Custom Queuing` | Queuing with assigned bandwidth portions. |
| `Priority Queuing` | Queue with absolute priority. |
| `LLQ` | Low Latency Queuing, priority queue with a limit. |
| `traffic starvation` | Situation where one class consumes resources and others receive little service. |

## Questions

### 1. What is a trust boundary?

Answer: The point where the network begins trusting traffic markings.

### 2. How is shaping different from policing?

Answer: `Shaping` buffers and smooths traffic, while `policing` strictly limits traffic and may drop packets.

### 3. What is tail drop?

Answer: Dropping new packets when a queue is already full.

### 4. Why is WRED useful?

Answer: It starts dropping lower-priority traffic in a controlled way before the queue becomes completely full.

### 5. Why is LLQ better than simple priority queuing?

Answer: `LLQ` prioritizes delay-sensitive traffic but limits that queue so other classes do not starve.

## Review Later

- The role of a `trust boundary`.
- The difference between `FIFO`, `tail drop`, and `WRED`.
- The difference between shaping and policing.
- The danger of `traffic starvation`.
- Why `LLQ` matters for voice.
- Why treatment methods matter during congestion.
