# QoS Classification And Marking

Source: closed course page  
Date added: 2026-08-21  
Related plan item: Week 16 / QoS classification and marking  
Tags: QoS, classification, marking, CoS, DSCP, IP Precedence, NBAR, ACL, class map, EF
Language: English
Translation pair: articles/2026-08/week-16/08-qos-classification-and-marking.md

## Summary

- Before traffic can be prioritized, it must be identified.
- `Classification` answers: what kind of traffic is this?
- `Marking` answers: what label should this traffic receive?
- Traffic can be classified by IP address, port, protocol, interface, VLAN, or application.
- `ACL`, `NBAR`, and `class map` help group traffic for `QoS` policy.
- Layer 2 marking uses `CoS`.
- Layer 3 marking commonly uses `DSCP`.
- For voice traffic, remember `EF`, or `Expedited Forwarding`.

## Key Points

- `QoS` begins with understanding traffic, not queuing.
- Classification inspects traffic and places it into a category.
- Marking gives traffic a value that downstream devices can use.
- Marking saves resources because every device does not need to deeply inspect the packet again.
- Traffic should usually be classified as close to the network edge as possible.
- `CoS` uses 3 bits in the 802.1Q tag and provides values from 0 to 7.
- `DSCP` uses 6 bits and provides a more flexible marking system.

## Notes

Many people want to jump straight to the visible part of `QoS`:

```text
Make voice go first.
Prioritize video.
Limit bad traffic.
```

Before that, the network must answer a basic question:

```text
What kind of traffic is this?
```

You cannot correctly prioritize a flow if the network does not know what it is.

That is why classification and marking form the foundation of `QoS`.

## What Classification Is

Classification is the process of identifying traffic type.

A device looks at a packet and decides:

- this is voice;
- this is web;
- this is video;
- this is guest traffic;
- this is a payment system;
- this is backup traffic;
- this is management traffic.

After that, traffic can be treated differently.

Simple idea:

```text
Identify first. Manage second.
```

## What Traffic Can Be Classified By

Traffic can be identified using different match criteria:

- source IP;
- destination IP;
- protocol;
- TCP or UDP port;
- interface;
- VLAN;
- application;
- time;
- existing marking.

The more accurate the classification, the more precise the `QoS` policy.

But precision costs resources. Deep application inspection is heavier than matching by address or port.

## ACL As A Classification Tool

One familiar way to classify traffic is an `ACL`.

An `ACL` can match:

- source address;
- destination address;
- protocol;
- port number;
- sometimes a time range.

For example, you can identify payment traffic or separate the guest network from office traffic.

In `QoS`, an `ACL` is often not used to block traffic. It is used to say:

```text
This traffic belongs to this category.
```

That is an important difference from access lists used for filtering.

## NBAR

`NBAR`, or `Network Based Application Recognition`, lets a device recognize applications more deeply than a simple port number.

This matters because modern applications do not always behave predictably:

- they may use different ports;
- they may hide inside normal web traffic;
- they may change behavior;
- they may require more precise recognition.

`NBAR` gives smarter classification, but it uses more device resources.

Practical takeaway:

```text
Use deeper recognition where it is actually needed.
```

## Class Map

A `class map` is where match conditions are grouped.

Simplified:

```text
Everything that matches these rules belongs in this class.
```

Examples:

- voice traffic;
- video traffic;
- business-critical traffic;
- guest traffic;
- scavenger traffic.

A `class map` keeps traffic categories organized so policy can act on them later.

## What Marking Is

After classification, traffic can be marked.

Marking assigns a value that tells other devices:

```text
How should this traffic be treated?
```

If classification is detective work, marking is the label on the box.

The device identifies the traffic once, then applies a mark. Downstream devices can make faster decisions using that mark instead of repeating all the inspection.

## Why Marking Matters

Marking makes `QoS` scalable.

Without marking, every device along the path may need to reanalyze:

- what application this is;
- where it came from;
- where it is going;
- which port it uses;
- how important it is.

With marking, a device can simply read a `CoS` or `DSCP` value.

That matters in larger networks where the same flows cross many devices.

## CoS At Layer 2

`CoS`, or `Class of Service`, is Layer 2 marking.

It is stored in the 802.1Q VLAN tag.

Important facts:

- it uses 3 bits;
- it provides 8 values from 0 to 7;
- it matters especially on trunk links;
- it works where a VLAN tag exists.

General logic:

```text
Lower values mean less important traffic.
Higher values mean more important traffic.
```

The very top is not always for user traffic. Network control traffic is often more important than voice because if the control plane fails, the whole network can fail.

## IP Precedence And DSCP

The older Layer 3 marking method was `IP Precedence`.

It used 3 bits, giving a limited number of levels.

Later, `DSCP`, or `Differentiated Services Code Point`, was introduced.

`DSCP` uses 6 bits and provides up to 64 values.

That is much more flexible because modern networks support more application types and need more precise policies.

## How To Read AF

In `DSCP`, you often see `AF`, or `Assured Forwarding`, values.

Examples:

```text
AF11
AF12
AF13
AF23
```

In `AFxy`:

- the first digit is the traffic class;
- the second digit is the drop preference.

For traffic class:

```text
Higher is better.
```

For drop preference:

```text
Lower means less likely to be dropped.
```

Example:

```text
AF11 is better than AF12 within the same class.
AF12 is better than AF13 within the same class.
AF23 has a higher class than AF11.
```

Class matters first. Drop preference matters inside the class.

## EF For Voice

The most important mark to remember at this level is `EF`.

`EF` means `Expedited Forwarding`.

It is commonly used for voice traffic.

Voice is sensitive to delay, jitter, and loss, so it needs fast and predictable handling.

If you remember one `DSCP` mark for `CCNA`, start with `EF`.

## NetworkChuck Coffee Scenario

At NetworkChuck Coffee, the network carries:

- VoIP;
- payments;
- cameras;
- guest Wi-Fi;
- back-office traffic;
- web browsing;
- updates.

If all of that looks the same to the network, `QoS` cannot make a good decision.

The network needs to:

1. Classify voice.
2. Classify payments.
3. Separate guest traffic.
4. Mark important flows.
5. Let downstream devices trust those marks.

That is how the network starts to understand what matters.

## Practical Tip

Classify traffic as close to the edge as possible.

Reasons:

- it is easier to identify the source there;
- it is easier to separate user traffic from network traffic;
- deep inspection is not repeated on every device;
- the rest of the network can use markings.

Good model:

```text
Classify once.
Mark once.
Trust and enforce downstream.
```

## Main Takeaway

`QoS` begins with classification and marking.

Classification identifies traffic. Marking labels it so other devices can make fast decisions.

Layer 2 uses `CoS`. Layer 3 commonly uses `DSCP`. For voice, remember `EF`.

Without classification and marking, later `QoS` mechanisms - queuing, shaping, policing, and priority - do not have a solid foundation.

## Commands And Terms

| Term | Meaning |
| --- | --- |
| classification | Identifying traffic type. |
| marking | Assigning a value to traffic. |
| `ACL` | Access Control List, can be used to match traffic in `QoS`. |
| `NBAR` | Network Based Application Recognition, application recognition. |
| `class map` | Group of match conditions for a traffic class. |
| `CoS` | Class of Service, Layer 2 marking in the 802.1Q tag. |
| `IP Precedence` | Older 3-bit Layer 3 marking. |
| `DSCP` | Differentiated Services Code Point, 6-bit Layer 3 marking. |
| `AF` | Assured Forwarding, a group of `DSCP` values. |
| `EF` | Expedited Forwarding, `DSCP` value commonly used for voice traffic. |
| drop preference | Drop likelihood inside a class. |

## Questions

### 1. What is classification in QoS?

Answer: Identifying the type of traffic before applying policy.

### 2. What is marking?

Answer: Assigning a label to traffic so other devices can make faster decisions.

### 3. How is CoS different from DSCP?

Answer: `CoS` works at Layer 2 in the 802.1Q tag, while `DSCP` works at Layer 3 in the IP header.

### 4. Why is NBAR useful?

Answer: It provides more precise application recognition when ports and addresses are not enough.

### 5. Which DSCP mark matters for voice?

Answer: `EF`, or `Expedited Forwarding`.

## Review Later

- The difference between classification and marking.
- Where `CoS` is used.
- Why `DSCP` is more flexible than `IP Precedence`.
- How to read `AF` values.
- Why `EF` matters for voice traffic.
- Why traffic should be classified closer to the edge.
