# Reading Show Interface Output

Source: закрытая страница курса  
Date added: 2026-06-01  
Related plan item: Week 5 / Reading interface counters and errors  
Tags: show interface, interface counters, crc, fcs, collisions, late collisions, duplex mismatch, troubleshooting
Language: Russian
Translation pair: articles-en/2026-05/week-05/08-reading-show-interface-output.md

## Summary

`show interface` может выглядеть пугающе, потому что вывод большой. Но для первого troubleshooting не нужно читать каждую строку. Нужно быстро найти главное: interface state, MAC address, IP settings, speed/duplex, load, traffic rates and error counters.

Главная мысль: `show interface` рассказывает историю link. Твоя задача - читать правильные строки.

## Key Points

- Start with `show ip interface brief` for a quick alive/down view.
- Use `show interface <interface>` when you need deeper link details.
- MAC address helps verify physical/L2 connectivity through switch MAC table.
- Speed and duplex are major troubleshooting clues.
- Load may be shown on a 1-255 scale, not as a percentage.
- Five minute input/output rate shows recent traffic trend.
- Packet and byte counters show cumulative traffic since interface counters started.
- Input errors and CRC errors often point toward physical/data-link problems.
- CRC checks whether frame data arrived intact.
- FCS is the Frame Check Sequence field used for error detection.
- Output errors, collisions and late collisions can point toward duplex or physical issues.
- In modern switched Ethernet, collisions are suspicious.

## Notes

### Do Not Memorize Every Line

`show interface` can feel like a wall of text.

Do not try to memorize every field on day one.

Instead, learn to scan for:

- interface state;
- hardware/MAC address;
- IP address if shown;
- MTU/bandwidth if relevant;
- speed;
- duplex;
- load;
- input/output rates;
- input errors;
- CRC errors;
- output errors;
- collisions;
- late collisions;
- interface resets.

That is enough to start useful troubleshooting.

### Start With Show IP Interface Brief

Before going deep, run:

```text
show ip interface brief
```

This answers:

```text
What interfaces exist?
Which IPs are assigned?
Which interfaces are up?
Which interfaces are down?
Which are administratively down?
```

Then, if one interface needs deeper inspection:

```text
show interface gigabitEthernet 0/0/0
```

or whatever interface name your device uses.

### MAC Address In The Output

`show interface` usually shows the hardware address / burned-in address.

That MAC address is useful because you can compare it with the switch MAC address table.

Example workflow:

1. Find router interface MAC address.
2. Go to switch.
3. Check MAC address table.
4. Confirm the MAC is learned on the expected switch port.

This helps verify that physical Layer 2 connectivity matches your diagram.

Useful switch command:

```text
show mac address-table
```

### Interface State

Look at interface status.

Common examples:

```text
GigabitEthernet0/0/0 is up, line protocol is up
GigabitEthernet0/0/0 is administratively down, line protocol is down
GigabitEthernet0/0/0 is down, line protocol is down
```

Quick meaning:

| State | Meaning |
| --- | --- |
| up/up | Interface enabled and working at Layer 1/2. |
| administratively down/down | Interface disabled with `shutdown`. |
| down/down | Interface enabled but no physical/protocol link. |

If it says administratively down:

```text
no shutdown
```

If it says down/down:

- check cable;
- check other side;
- check switch port;
- check module;
- check speed/duplex;
- check physical layer.

### Speed And Duplex

Speed tells how fast the link operates:

```text
100 Mbps
1 Gbps
10 Gbps
```

Duplex tells whether communication is:

- half-duplex;
- full-duplex.

Modern switched networks should usually be full-duplex.

If duplex is wrong, performance can become strange:

- slow sometimes;
- intermittent;
- high errors;
- collisions;
- late collisions;
- retransmissions.

Speed/duplex lines are small, but they can explain a lot.

### Load

Cisco may show load as a fraction over `255`.

Example idea:

```text
txload 1/255, rxload 1/255
```

Meaning:

```text
255/255 = fully saturated
```

So if load climbs high, the interface may genuinely be busy or close to maxed out.

It is not always shown as a clean percentage.

You need to understand the scale.

### Five Minute Rates

Useful lines:

```text
5 minute input rate
5 minute output rate
```

They show recent traffic trend.

This helps answer:

```text
Is this interface busy right now?
```

Compare that with cumulative packets/bytes:

```text
How much traffic has passed over time?
```

Recent rate and total counters are different clues.

### Input Errors

Input errors mean the interface received frames with problems.

Possible causes:

- bad cable;
- electrical interference;
- bad connector;
- failing NIC;
- duplex mismatch;
- physical layer issue;
- damaged frame.

Do not panic over one old counter.

Watch whether it is increasing.

Rising input errors are more important than stale historical numbers.

### CRC Errors

CRC stands for:

```text
Cyclic Redundancy Check
```

Plain English:

```text
The receiver checks whether the frame arrived intact.
```

Sender calculates a value from the frame data.

Receiver calculates again.

If values do not match:

```text
CRC error
```

Rising CRC errors often point to physical/data-link problems:

- bad cable;
- bad termination;
- cable too long;
- interference;
- bad transceiver;
- failing NIC;
- dirty fiber connector.

### Frames, FCS And OSI Layer 2

At Layer 2, data is carried in a frame.

A frame includes:

- destination MAC;
- source MAC;
- payload;
- FCS.

FCS stands for:

```text
Frame Check Sequence
```

FCS is used for error detection and is closely related to CRC.

If frame integrity check fails, counters like CRC/input errors can increase.

People often say "packet" casually for everything, but technically:

```text
Layer 2 = frame
Layer 3 = packet
```

### Cable Problems Can Be Sneaky

Bad cabling does not always cause a clean outage.

It can cause:

- random slowness;
- occasional disconnects;
- intermittent application issues;
- weird one-off failures;
- "it seems fine now" symptoms.

That is why interface counters matter.

If CRC/input errors keep increasing, do not immediately rewrite configs or blame applications.

Check physical layer.

In real deployments, cable certification matters.

Link light is not enough proof that cabling is healthy.

### Output Errors

Output-side errors reflect problems while sending frames out of the interface.

Useful counters include:

- output errors;
- collisions;
- late collisions;
- interface resets.

Output errors can point to:

- congestion;
- physical link issue;
- duplex mismatch;
- bad hardware;
- queue/drop problems depending on platform.

### Collisions

Collisions were normal in old hub-based Ethernet.

In modern switched full-duplex Ethernet:

```text
Collisions should basically not be happening.
```

If collisions increase on a switched link, investigate:

- duplex mismatch;
- half-duplex configuration;
- old device;
- physical issue;
- unusual topology.

### Late Collisions

Late collisions are especially suspicious.

They happen later in the frame than a normal collision should.

Common causes:

- duplex mismatch;
- cable length problem;
- cabling fault;
- physical layer problem.

If you see late collisions, do not ignore them.

They are strong clues.

### Interface Resets

Interface resets can indicate instability.

If reset counter keeps increasing, users may experience:

- random disconnects;
- link drops;
- intermittent failures;
- "internet is weird today."

Possible causes:

- bad cable;
- failing NIC;
- bad port;
- power issue;
- speed/duplex negotiation problem;
- physical layer flapping.

### Read The Right Things

When opening `show interface`, do not read it as a novel.

Read it like a troubleshooter:

```text
Is it up?
Is the speed correct?
Is duplex correct?
Is the link loaded?
Are input errors rising?
Are CRC errors rising?
Are output errors rising?
Are collisions or late collisions present?
Are resets increasing?
```

That short scan gives direction.

## Practical Troubleshooting Flow

1. Run `show ip interface brief`.
2. Identify the interface to inspect.
3. Run `show interface <interface>`.
4. Check status and protocol.
5. Check speed and duplex.
6. Check load and five minute rates.
7. Check input errors and CRC.
8. Check output errors.
9. Check collisions and late collisions.
10. Check resets.
11. If counters rise, investigate physical layer or duplex.
12. Compare MAC address with switch MAC table if needed.

## Example Interpretation

### Case 1

```text
Interface is up/up
Speed 1000 Mbps
Full-duplex
No CRC errors increasing
No collisions
```

Likely:

```text
The link itself looks healthy.
```

### Case 2

```text
Interface is up/up
Full-duplex on one side
Collisions increasing
Late collisions increasing
```

Possible issue:

```text
Duplex mismatch or physical layer problem.
```

### Case 3

```text
CRC errors increasing
Input errors increasing
Users report random slowness
```

Possible issue:

```text
Bad cable, interference, bad termination, failing NIC or transceiver.
```

## Quick Self-Check

### Question 1

What command should you often start with before detailed interface inspection?

Answer:

```text
show ip interface brief
```

### Question 2

What does CRC help detect?

Answer:

```text
Whether a frame arrived corrupted.
```

### Question 3

What does FCS stand for?

Answer:

```text
Frame Check Sequence.
```

### Question 4

Are collisions normal on modern full-duplex switched Ethernet?

Answer:

```text
No. Increasing collisions are suspicious.
```

### Question 5

What do rising CRC/input errors often suggest?

Answer:

```text
A physical layer or data-link issue such as bad cable, interference, bad NIC or transceiver.
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `show ip interface brief` | Quick interface/IP/status summary. |
| `show interface <interface>` | Detailed interface status and counters. |
| MAC address | Layer 2 hardware address of interface. |
| Speed | Link rate. |
| Duplex | Whether link sends/receives simultaneously. |
| Load | Interface utilization, sometimes shown over 255. |
| Input errors | Received frames with problems. |
| CRC | Cyclic Redundancy Check. |
| FCS | Frame Check Sequence. |
| Output errors | Errors while sending frames. |
| Collision | Ethernet transmit conflict, suspicious on modern switched links. |
| Late collision | Abnormal collision later in frame transmission. |
| Interface reset | Interface recovered/restarted, often a clue for instability. |

## What To Review Later

- Ethernet frame structure
- FCS and CRC
- Duplex mismatch
- Speed negotiation
- Layer 1 troubleshooting
- Cable certification
- Switch MAC address table
- Interface counters
- Bits per second and link speeds

