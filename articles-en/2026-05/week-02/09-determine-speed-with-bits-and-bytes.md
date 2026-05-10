# Determine Speed with Bits and Bytes

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Network speed basics  
Tags: bits, bytes, bandwidth, speed, gbps, mbps, transfer rate, file size, conversion

## Summary

Network speed is usually measured in bits per second, while file sizes and storage are usually measured in bytes. This small letter difference matters a lot: lowercase `b` means bits, uppercase `B` means bytes. Since 1 byte equals 8 bits, you divide by 8 to estimate how many bytes per second a network link can transfer.

Main idea: storage is usually bytes, network speed is usually bits, and the bridge between them is 8. Understanding that lets you estimate transfer times, compare ISP plans and size network links more realistically.

## Key Points

- A bit is the smallest unit of data: either `0` or `1`.
- A byte is 8 bits grouped together.
- Bytes are often used for file sizes and storage.
- Network speeds are usually measured in bits per second.
- Lowercase `b` means bits.
- Uppercase `B` means bytes.
- `Mbps` means megabits per second.
- `MBps` means megabytes per second.
- `Gbps` means gigabits per second.
- `GBps` means gigabytes per second.
- To convert bits per second to bytes per second, divide by 8.
- A 1 Gbps link is 1,000 Mbps.
- 1,000 Mbps divided by 8 equals about 125 MBps.
- A 100 MB file over an ideal 125 MBps link takes about 0.8 seconds.
- Real transfers are affected by overhead, latency, protocol behavior and wireless interference.
- The math still gives a useful baseline for planning.

## Notes

### Why This Matters

People often mix up bits and bytes.

That creates bad expectations.

Example misunderstanding:

```text
"I have 1 gig internet, so a 1 GB file should download in 1 second."
```

Not quite.

Most network speeds are in bits, while the file size is in bytes.

You need to convert before estimating transfer time.

### Bit

A bit is the smallest unit of data.

It can be:

```text
0 or 1
```

Computers use bits because underneath everything, data is represented as binary states.

Examples of binary-style meaning:

- off/on;
- no/yes;
- 0/1;
- low/high electrical state.

### Byte

A byte is:

```text
8 bits
```

Bytes are more human-friendly than individual bits.

A byte is often thought of as enough to represent a simple character, such as:

- `A`;
- `5`;
- another basic symbol/character depending on encoding.

This is why file sizes and storage are usually shown in bytes.

### Bits vs Bytes

The core distinction:

| Unit | Meaning | Common use |
| --- | --- | --- |
| bit | Single `0` or `1` | Network speed |
| byte | 8 bits | File size and storage |

Short version:

```text
A bit is what the computer sends.
A byte is what we tend to recognize.
```

### Size Ladder

For practical networking math, think in rough jumps of 1,000.

Storage/file-size ladder:

```text
Byte
Kilobyte
Megabyte
Gigabyte
Terabyte
```

The exact 1,024 vs 1,000 distinction exists, but for quick network speed estimates, using 1,000 is usually enough.

### Uppercase B Problem

Tiny letter difference, huge meaning:

| Symbol | Meaning |
| --- | --- |
| `b` | bit |
| `B` | byte |

Examples:

| Notation | Meaning |
| --- | --- |
| `Mbps` | megabits per second |
| `MBps` | megabytes per second |
| `Gbps` | gigabits per second |
| `GBps` | gigabytes per second |

This is where many speed misunderstandings happen.

### Network Speed Uses Bits

When an ISP or switch says:

```text
1 Gbps
```

That usually means:

```text
1 gigabit per second
```

Not:

```text
1 gigabyte per second
```

Those are different by a factor of 8.

### Conversion Rule

The key formula:

```text
bytes = bits / 8
```

For speeds:

```text
MBps = Mbps / 8
```

And:

```text
GBps = Gbps / 8
```

### 1 Gbps Example

A 1 Gbps link is:

```text
1,000 Mbps
```

Convert to megabytes per second:

```text
1,000 Mbps / 8 = 125 MBps
```

So an ideal 1 Gbps link can move about:

```text
125 megabytes per second
```

### File Transfer Time

To estimate transfer time:

```text
file size / transfer rate = time
```

Example:

```text
100 MB file / 125 MBps = 0.8 seconds
```

So a 100 MB file over an ideal 1 Gbps link takes about:

```text
0.8 seconds
```

### Real Life Is Not Perfect

Real transfers are not always ideal.

Things that affect performance:

- protocol overhead;
- latency;
- congestion;
- disk speed;
- server performance;
- wireless interference;
- packet loss;
- encryption overhead;
- shared bandwidth;
- client device limitations.

The math still gives a baseline.

It helps answer:

```text
Is this performance roughly reasonable?
```

### ISP Plan Expectations

When comparing ISP plans, ask:

```text
Is the number in bits or bytes?
```

Most ISP speeds are in bits per second.

Example:

```text
100 Mbps internet
```

means 100 megabits per second, which is roughly:

```text
12.5 MBps
```

### Network Design Use

This math matters more as networks grow.

Use cases:

- file transfers;
- backups;
- video editing networks;
- server replication;
- cloud uploads;
- switch uplinks;
- storage networks;
- camera/video systems.

Choosing between 1 Gbps, 2.5 Gbps, 10 Gbps or faster links requires understanding what those numbers actually mean.

### NetworkChuck Coffee Example

For a coffee shop, 1 Gbps may be plenty for:

- guest browsing;
- social media;
- light streaming;
- POS cloud traffic;
- employee devices;
- normal back office work.

But if the business adds heavy workloads, the math becomes more important:

- large backups;
- many cameras;
- video production;
- local servers;
- high-volume cloud transfers.

### Main Takeaway

Remember:

```text
Storage/file size = usually bytes.
Network speed = usually bits.
1 byte = 8 bits.
```

To estimate transfer speed:

```text
network speed in bits / 8 = approximate bytes per second
```

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Bit | Smallest unit of data, `0` or `1`. |
| Byte | 8 bits. |
| Binary | Data represented with `0`s and `1`s. |
| Kilobyte | Roughly 1,000 bytes for practical estimates. |
| Megabyte | Roughly 1,000 kilobytes. |
| Gigabyte | Roughly 1,000 megabytes. |
| Terabyte | Roughly 1,000 gigabytes. |
| `b` | Lowercase symbol for bit. |
| `B` | Uppercase symbol for byte. |
| Mbps | Megabits per second. |
| MBps | Megabytes per second. |
| Gbps | Gigabits per second. |
| GBps | Gigabytes per second. |
| Bandwidth | Amount of data a connection can carry over time. |
| Overhead | Extra protocol/control data that reduces usable transfer rate. |
| Latency | Delay before data begins or continues moving. |

## Questions

### 1. What is a bit?

A bit is the smallest unit of data, either `0` or `1`.

### 2. What is a byte?

A byte is 8 bits.

### 3. Which unit is usually used for network speed?

Bits per second.

### 4. Which unit is usually used for file size and storage?

Bytes.

### 5. What does lowercase `b` mean?

Bit.

### 6. What does uppercase `B` mean?

Byte.

### 7. What does `Mbps` mean?

Megabits per second.

### 8. What does `MBps` mean?

Megabytes per second.

### 9. How do you convert bits to bytes?

Divide by 8.

### 10. How many megabits per second are in 1 Gbps?

1,000 Mbps.

### 11. About how many megabytes per second can a 1 Gbps link transfer in ideal conditions?

About 125 MBps.

### 12. How long would a 100 MB file take over an ideal 125 MBps transfer rate?

About 0.8 seconds.

### 13. Why are real transfers slower than ideal math?

Because of overhead, latency, protocol behavior, wireless interference, congestion and device limitations.

### 14. What question should you ask when comparing ISP plans?

Is this number in bits or bytes?

### 15. Why does this math matter for network design?

It helps estimate transfer times, set expectations and choose appropriately sized links.

### 16. What is the bridge between storage sizes and network speeds?

The number 8, because 1 byte equals 8 bits.

## What To Review Later

- Bit = `0` or `1`.
- Byte = 8 bits.
- Storage/file sizes are usually bytes.
- Network speeds are usually bits.
- Lowercase `b` vs uppercase `B`.
- Mbps vs MBps.
- Gbps to MBps conversion.
- Transfer time formula.
- Why real-world performance differs from ideal math.
- Using speed math for link sizing and expectations.
