# Using Straight-through, Crossover, and MDI-X

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Ethernet cabling  
Tags: ethernet, straight-through, crossover, mdi-x, auto-mdix, tx, rx, 802.3, cabling

## Summary

Straight-through and crossover cables exist because older Ethernet devices had fixed transmit and receive pin expectations. A straight-through cable connected unlike devices, such as a PC and a switch, because their TX/RX pin roles naturally matched. A crossover cable connected like devices, such as switch-to-switch or PC-to-PC, by swapping transmit and receive pairs inside the cable.

Main idea: modern Auto MDI-X usually handles this automatically, but understanding the original logic helps when troubleshooting older gear, odd embedded devices or links that refuse to come up.

## Key Points

- Ethernet cabling behavior is based on the IEEE 802.3 standards family.
- Standards allow devices from different vendors to interoperate.
- TX means transmit.
- RX means receive.
- Older 10 Mbps and 100 Mbps Ethernet used specific pin pairs for transmit and receive.
- A PC/end device typically transmitted on pins 1 and 2 and received on pins 3 and 6.
- A switch used the opposite behavior, receiving on pins 1 and 2 and transmitting on pins 3 and 6.
- Straight-through cables map pin 1 to pin 1, pin 2 to pin 2 and so on.
- Straight-through cables worked for unlike devices because TX on one side lined up with RX on the other.
- Crossover cables swap transmit and receive pairs.
- Crossover cables were used for like devices, such as switch-to-switch or PC-to-PC.
- Auto MDI-X lets modern devices automatically adjust transmit/receive behavior.
- With Auto MDI-X, standard patch cables usually work regardless of whether the connected devices are like or unlike.
- Older gear and unusual devices may still require you to understand cable type and pin behavior.

## Notes

### Why This Still Matters

Modern Ethernet often feels simple:

```text
Plug in a cable -> link comes up
```

But that simplicity hides older cabling logic. When a link does not come up, the mental model still matters.

Understanding straight-through, crossover and Auto MDI-X helps troubleshoot:

- old switches;
- old PCs;
- budget devices;
- embedded devices;
- lab equipment;
- strange link failures;
- dusty network closets with mixed hardware.

At NetworkChuck Coffee, this could matter if an older switch, register terminal, camera or small appliance refuses to link.

### Ethernet Standards

Ethernet is standards-based.

The relevant standards family:

```text
IEEE 802.3
```

This matters because standards create interoperability.

Examples:

- a Dell PC can connect to a Cisco switch;
- an Apple device can use Ethernet;
- different vendors can build devices that still communicate;
- Ethernet cabling behaves predictably across environments.

Without shared standards, every vendor could have created different cabling rules.

### TX and RX

Two important terms:

| Term | Meaning |
| --- | --- |
| TX | Transmit |
| RX | Receive |

For a link to work, transmit on one side must line up with receive on the other side.

Simple model:

```text
Device A TX -> Device B RX
Device B TX -> Device A RX
```

If both sides transmit on the same pair or listen on the same pair, the link will not work correctly.

### Older Ethernet Pin Behavior

On older 10 Mbps and 100 Mbps Ethernet, only some pins did the main communication work.

The article focuses on these pin pairs:

| Pins | Role on PC/end device | Role on switch |
| --- | --- | --- |
| 1 and 2 | TX | RX |
| 3 and 6 | RX | TX |

This difference is why a normal straight-through cable worked so well between a PC and a switch.

### Straight-through Cable

A straight-through cable maps pins directly from one end to the other.

Simple model:

```text
Pin 1 -> Pin 1
Pin 2 -> Pin 2
Pin 3 -> Pin 3
Pin 6 -> Pin 6
```

This cable was used for unlike devices.

Examples:

- PC to switch;
- server to switch;
- printer to switch;
- router Ethernet port to switch in many classic cases.

Why it works:

```text
PC TX pins -> switch RX pins
Switch TX pins -> PC RX pins
```

The devices have opposite expectations, so the straight-through cable lines everything up.

### Crossover Cable

A crossover cable swaps transmit and receive pairs.

Core idea:

```text
Pins 1 and 2 cross to pins 3 and 6.
Pins 3 and 6 cross to pins 1 and 2.
```

This cable was used for like devices.

Examples:

- switch to switch;
- PC to PC;
- router to router in some classic Ethernet cases.

Why it was needed:

```text
Same device type -> same TX/RX expectations -> mismatch
```

The cable fixed the mismatch by crossing the pairs.

### Like vs Unlike Devices

Old-school memory model:

| Connection | Classic cable type |
| --- | --- |
| PC to switch | Straight-through |
| PC to PC | Crossover |
| Switch to switch | Crossover |
| Server to switch | Straight-through |

This is the simplified rule that appeared in many networking lessons and older exams.

### Auto MDI-X

Auto MDI-X changed the day-to-day cabling experience.

Auto MDI-X lets a device automatically detect the connection and adjust which pins it uses for transmit and receive.

Important nuance:

```text
Auto MDI-X does not physically rewire the cable.
It changes the device's transmit/receive behavior.
```

With Auto MDI-X, most modern devices can use a normal Ethernet patch cable and sort out the TX/RX logic automatically.

### Why This Feels Like History Now

Today, most modern switches, PCs and network devices support Auto MDI-X.

That means you usually:

- grab a standard patch cable;
- plug in the devices;
- wait for link lights;
- move on.

But the history still matters because not every device is modern, and not every environment is clean.

### Troubleshooting Mindset

If a link does not come up, check basics first:

- cable type;
- cable quality;
- link lights;
- port status;
- port speed/duplex settings;
- device age;
- Auto MDI-X support;
- whether devices are like or unlike;
- whether the cable is damaged.

Do not assume Auto MDI-X will always save you, especially with older equipment.

### Main Takeaway

The essential logic:

```text
TX must reach RX.
RX must receive TX.
```

Straight-through cables worked when device pin roles already complemented each other.

Crossover cables worked when the cable needed to swap TX/RX pairs.

Auto MDI-X lets modern hardware handle the swap automatically.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| IEEE 802.3 | Ethernet standards family. |
| TX | Transmit. |
| RX | Receive. |
| Straight-through cable | Cable where pins map directly end-to-end. |
| Crossover cable | Cable that swaps transmit and receive pairs. |
| MDI | Medium Dependent Interface, often associated with end-device Ethernet port behavior. |
| MDI-X | Medium Dependent Interface Crossover, often associated with switch-side Ethernet port behavior. |
| Auto MDI-X | Feature that automatically adjusts transmit/receive behavior. |
| Link lights | Port LEDs that show physical link/activity. |
| Like devices | Devices with similar port behavior, such as switch-to-switch or PC-to-PC. |
| Unlike devices | Devices with complementary port behavior, such as PC-to-switch. |

## Questions

### 1. What standards family defines Ethernet behavior?

IEEE 802.3.

### 2. Why are Ethernet standards important?

They let devices from different vendors interoperate using the same agreed rules.

### 3. What does TX mean?

TX means transmit.

### 4. What does RX mean?

RX means receive.

### 5. On older 10/100 Ethernet, which pins did a PC typically use to transmit?

Pins 1 and 2.

### 6. On older 10/100 Ethernet, which pins did a PC typically use to receive?

Pins 3 and 6.

### 7. What is a straight-through cable?

A cable where each pin maps directly to the same pin on the other end.

### 8. Why did straight-through cables work for PC-to-switch connections?

Because the PC's transmit pins lined up with the switch's receive pins, and the switch's transmit pins lined up with the PC's receive pins.

### 9. What is a crossover cable?

A cable that swaps transmit and receive pairs so like devices can communicate.

### 10. When were crossover cables traditionally used?

For like-device connections, such as switch-to-switch or PC-to-PC.

### 11. What problem does Auto MDI-X solve?

It automatically adjusts transmit/receive behavior so the correct pairs line up without manually choosing straight-through or crossover.

### 12. Does Auto MDI-X physically rewire the cable?

No. It changes the device's transmit/receive behavior.

### 13. Why should you still know this topic if modern devices usually handle it automatically?

Because older gear, embedded devices and strange troubleshooting cases may still require understanding cable type and TX/RX behavior.

### 14. What should you check if a link will not come up?

Cable type, link lights, port status, port speed, device age and whether Auto MDI-X is supported.

## What To Review Later

- IEEE 802.3 as the Ethernet standards family.
- TX vs RX.
- Older 10/100 pin behavior.
- Straight-through for unlike devices.
- Crossover for like devices.
- Auto MDI-X and why it changed modern cabling.
- Troubleshooting physical links when Auto MDI-X may not be available.
