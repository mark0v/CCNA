# How WiFi Really Works

Source: closed course page  
Date added: 2026-08-21  
Related plan item: Week 17 / How WiFi really works  
Tags: Wi-Fi, wireless, RF, access points, airtime, frequency, interference, signal loss, 2.4 GHz, 5 GHz, 6 GHz
Language: English
Translation pair: articles/2026-08/week-17/02-how-wifi-really-works.md

## Summary

- Wi-Fi is not magic. It is bits sent over radio waves.
- Copper uses electricity, fiber uses light, and Wi-Fi uses radio frequencies.
- Wireless is harder than wired networking because the medium is less controlled.
- All wireless clients share airtime.
- More active clients means less available transmit time per client.
- Higher frequencies usually allow more speed, but less range and weaker obstacle penetration.
- Distance, walls, reflections, and interference directly affect Wi-Fi quality.

## Key Points

- Wireless can feel unpredictable, but problems have physical causes.
- Switched Ethernet isolates traffic better than a wireless medium can.
- In Wi-Fi, devices cannot all talk at the same time.
- One weak faraway client can hurt the whole wireless cell.
- 2.4 GHz usually travels farther, but is slower and often noisier.
- 5 GHz and 6 GHz provide more speed and capacity, but require better planning.
- Good wireless design is planning, not turning power to maximum and hoping.

## Notes

Many engineers dislike wireless because it feels less predictable.

Wired networking feels tidy:

```text
Cable connected.
Port up.
Configuration matches.
Traffic flows.
```

Wireless is different. A problem can come from a wall, a microwave, a neighboring network, an airport nearby, or a strange event that happens at the same time every day.

But the core idea is:

```text
Wireless is not magic.
It is bits riding radio waves.
```

## Bits Across Different Media

Networks always transmit zeros and ones.

Only the medium changes:

| Medium | How Data Moves |
| --- | --- |
| Copper | Electrical signal. |
| Fiber | Light. |
| Wi-Fi | Radio waves. |

This removes some of the mystery.

Wi-Fi is not random. It is just affected by more surrounding factors than a cable inside a wall.

## Why Wireless Is Less Controlled

In a wired network, the signal moves through a physical cable.

Problems can still happen:

- bad cable;
- damaged connector;
- wrong speed;
- duplex mismatch;
- interference in a poor environment.

But the signal path is contained by the cable.

In wireless, the signal goes into the air.

In that air, there are:

- walls;
- furniture;
- people;
- other access points;
- neighboring networks;
- Bluetooth;
- microwaves;
- reflections;
- radio interference sources;
- power limits.

Wireless is not impossible. It is just less controlled.

## Shared Airtime

In modern switched Ethernet, each connection is much better isolated.

Wireless cannot work exactly the same way because devices share the same radio medium.

If everyone talks at once, communication fails.

Simplified:

```text
Wireless devices must take turns talking.
```

The access point helps manage the medium. But the medium is still shared.

## Why Device Count Matters

Marketing may say:

```text
Supports 200 devices.
Supports 500 devices.
```

The better question is:

```text
How many devices will actively transmit during the busiest moment?
```

A device can be associated but barely transmit traffic. That is one thing.

It is very different when dozens of clients simultaneously:

- stream video;
- upload files;
- use cloud apps;
- make voice or video calls;
- update applications;
- sync data.

Each one needs airtime. The more active clients there are, the less airtime each one gets.

## Weak Clients Slow Everyone

A distant or weak client often transmits more slowly and needs more airtime.

This detail matters.

If a client is far from the access point, signal is weaker. To transmit reliably, it may need more time. One weak client can degrade the experience for other clients in the same wireless cell.

That is why this is a bad idea:

```text
Install one powerful access point and cover the whole building.
```

A large coverage area with weak clients at the edge may look convenient, but perform poorly.

## Frequency And Hertz

`Hertz` means how many times a wave repeats in one second.

When we say `2.4 GHz`, that means:

```text
2.4 billion cycles per second.
```

`5 GHz` is about 5 billion cycles per second. `6 GHz` is even higher.

Simplified:

```text
Higher frequency gives more opportunity to carry data.
```

That is why newer bands can deliver better speeds.

## Frequency Tradeoff

Higher frequency has a cost.

As frequency goes up:

- useful range becomes shorter;
- walls and obstacles are harder to penetrate;
- placement matters more;
- the correct number of access points matters more.

Lower frequency usually travels farther. Higher frequency usually gives more speed and cleaner planning, but needs denser coverage.

That is not always bad.

Smaller coverage areas can help: easier channel reuse, fewer weak distant clients, and better capacity control.

## 2.4, 5, And 6 GHz

Practically:

| Band | General Idea |
| --- | --- |
| 2.4 GHz | Longer range, fewer channels, more interference. |
| 5 GHz | Better speed and capacity, shorter range. |
| 6 GHz | More capacity, modern clients required, careful design needed. |

Do not choose a band only because newer sounds better.

Look at the requirement:

- where clients are;
- how many clients exist;
- what walls are present;
- which applications run;
- which devices are supported;
- how dense the access point deployment is.

## Signal Weakening

`Free space path loss` means the signal weakens as distance increases.

In plain language:

```text
The farther the client is from the access point, the weaker the signal gets.
```

That is normal for sound, light, and radio.

In Wi-Fi, the consequences matter: weak signal often means lower speed, more retries, more airtime, and worse user experience.

## Materials And Obstacles

`Absorption` means materials weaken the signal.

Signal can be weakened by:

- drywall;
- brick;
- concrete;
- glass;
- metal;
- water;
- people;
- furniture.

Different materials weaken signal differently.

That is why the floor plan matters. What works in one cafe may perform badly in another with different walls and layout.

## Reflection And Refraction

Radio signals can:

- reflect;
- bend;
- arrive by different paths;
- interfere with themselves.

That makes the wireless environment more complex.

Sometimes a client is physically close, but quality is poor because of reflections, materials, or interference.

## Interference

Wi-Fi operates in unlicensed spectrum.

That means your devices are not the only ones using it.

Problem sources:

- neighboring Wi-Fi networks;
- Bluetooth devices;
- microwaves;
- wireless cameras;
- old equipment;
- industrial devices;
- external radio signals.

Sometimes the cause is unexpected, such as an outside system near the office that creates interference on a schedule.

## NetworkChuck Coffee Scenario

At NetworkChuck Coffee, mornings are busy.

At the same time, the network supports:

- guest Wi-Fi;
- POS terminals;
- employee tablets;
- cameras;
- streaming music;
- back-office devices.

If guest Wi-Fi starts slowing down, do not simply say:

```text
Wireless is flaky.
```

Check:

- how many clients are actively transmitting;
- which band is in use;
- how far clients are from the access point;
- whether weak clients exist;
- which walls and materials sit between client and access point;
- whether interference exists;
- whether the wireless cell is too large.

There is a cause. Find it like an engineer instead of blaming Wi-Fi randomness.

## Practical Tip

When planning Wi-Fi, do not only ask:

```text
How many devices can connect?
```

Ask:

```text
How many devices will actively transmit during the busiest moment?
```

Those are different questions.

The first is about association. The second is about real performance.

## Main Takeaway

Wi-Fi is bits transmitted over radio waves through a complex environment.

Wireless is not random or magical. It follows physics: airtime is shared, frequencies have tradeoffs, distance weakens signal, materials interfere, reflections complicate things, and interference adds noise.

Good Wi-Fi is built through planning, not by turning power to maximum.

## Commands And Terms

| Term | Meaning |
| --- | --- |
| Wi-Fi | Wireless network based on radio signals. |
| wireless | Data transmission without a cable to the client. |
| `RF` | Radio frequency, the radio environment. |
| access point | Device that provides Wi-Fi access. |
| airtime | Time spent using the shared radio medium. |
| wireless cell | Service area of one access point. |
| hertz | Number of wave cycles per second. |
| GHz | Billions of cycles per second. |
| 2.4 GHz | Band with longer range and more interference. |
| 5 GHz | Band with better capacity and shorter range. |
| 6 GHz | Newer band with high capacity and shorter range. |
| free space path loss | Signal weakening with distance. |
| absorption | Signal weakening through materials. |
| reflection | Signal bouncing. |
| refraction | Signal bending. |
| interference | Noise or disruption in the radio medium. |

## Questions

### 1. How is Wi-Fi different from copper and fiber?

Answer: Copper uses electricity, fiber uses light, and Wi-Fi uses radio waves.

### 2. Why is wireless less controlled?

Answer: The signal travels through shared radio space with walls, clients, neighboring networks, reflections, and interference.

### 3. Why are active clients more important than connected clients?

Answer: Airtime is consumed by clients that are actually transmitting data.

### 4. Why can one weak client hurt everyone else?

Answer: It may need more airtime to transmit reliably, taking time away from other clients.

### 5. What is the tradeoff with higher frequencies?

Answer: They can provide more speed and capacity, but usually have shorter range and weaker obstacle penetration.

## Review Later

- How Wi-Fi transmits bits.
- Why airtime is shared.
- Differences between 2.4, 5, and 6 GHz.
- What free space path loss is.
- How materials and interference affect signal.
- Why good wireless design requires planning.
