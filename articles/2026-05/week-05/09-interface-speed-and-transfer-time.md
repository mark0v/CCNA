# Interface Speed and Transfer Time

Source: закрытая страница курса  
Date added: 2026-06-01  
Related plan item: Week 5 / Interface speed and transfer-time math  
Tags: interface speed, bandwidth, bits, bytes, transfer time, mbps, gbps, overhead, network design
Language: Russian
Translation pair: articles-en/2026-05/week-05/09-interface-speed-and-transfer-time.md

## Summary

Interface speed важно понимать не как абстрактное "быстрее лучше", а как practical capacity: сколько data можно передать за определенное время. Для этого нужно не путать bytes and bits, уметь переводить file size в network speed units и учитывать real-world overhead.

Главная мысль: если ты можешь оценить, сколько времени займет transfer, ты можешь лучше проектировать links, uplinks and network capacity.

## Key Points

- Bytes обычно измеряют file size and storage.
- Bits обычно измеряют network transfer speed.
- `1 byte = 8 bits`.
- Uppercase `B` обычно означает bytes.
- Lowercase `b` обычно означает bits.
- `100 GB` file size is not the same as `100 Gb`.
- Network speeds are usually shown as `Mbps`, `Gbps`, `Tbps`.
- To calculate transfer time, convert file size into bits.
- Transfer time formula: `file size in bits / link speed in bits per second`.
- Real transfer time is longer because of overhead and real-world conditions.
- A rough planning estimate can add about 20% overhead.
- Understanding speed helps with link sizing, backup windows, uplinks and bottleneck analysis.

## Notes

### Speed Is A Design Question

Network speed is not just a number on a spec sheet.

It answers questions like:

```text
How long will this file take to copy?
Is this uplink enough?
Will backups finish overnight?
Will users wait too long?
Where is the bottleneck?
```

At NetworkChuck Coffee, this matters if users move large files:

- media files;
- backups;
- camera recordings;
- databases;
- application data;
- shared storage.

If the network is too slow, business feels it.

### Bytes Vs Bits

The first rule:

```text
Bytes measure storage/file size.
Bits measure network speed.
```

Examples:

```text
100 GB file
1 TB backup
500 MB video
```

Those are storage/file sizes.

Network speeds:

```text
100 Mbps
1 Gbps
10 Gbps
```

Those are transfer rates.

### 1 Byte Equals 8 Bits

The core conversion:

```text
1 byte = 8 bits
```

So:

```text
100 GB = 100 billion bytes
100 billion bytes * 8 = 800 billion bits
```

The network moves bits.

So before calculating transfer time, convert file size into bits.

### Uppercase B And Lowercase b

This detail matters:

| Symbol | Meaning |
| --- | --- |
| `B` | Byte |
| `b` | bit |
| `MB` | megabyte |
| `Mb` | megabit |
| `GB` | gigabyte |
| `Gb` | gigabit |

Huge mistake:

```text
10 GB/s is not the same as 10 Gb/s.
```

Because:

```text
10 GB/s = 80 Gb/s
```

That is an 8x difference.

### Size Ladder

For planning math, use simple decimal steps:

```text
1 KB = 1,000 bytes
1 MB = 1,000,000 bytes
1 GB = 1,000,000,000 bytes
1 TB = 1,000,000,000,000 bytes
```

There are binary distinctions like `1,024`, and they matter in some storage contexts.

But for quick network planning:

```text
Use 1,000-based math for clear estimates.
```

Same idea for bits:

```text
1 Kb = 1,000 bits
1 Mb = 1,000,000 bits
1 Gb = 1,000,000,000 bits
1 Tb = 1,000,000,000,000 bits
```

### Transfer Time Formula

Use this formula:

```text
Transfer time = file size in bits / link speed in bits per second
```

Steps:

1. Convert file size to bytes if needed.
2. Multiply bytes by 8 to get bits.
3. Convert link speed to bits per second.
4. Divide.
5. Convert seconds to minutes/hours.

### Example: 100 GB Over 100 Mbps

File:

```text
100 GB
```

Convert to bytes:

```text
100,000,000,000 bytes
```

Convert to bits:

```text
100,000,000,000 * 8 = 800,000,000,000 bits
```

Link speed:

```text
100 Mbps = 100,000,000 bits per second
```

Transfer time:

```text
800,000,000,000 / 100,000,000 = 8,000 seconds
```

Convert:

```text
8,000 seconds / 60 = 133.3 minutes
```

Result:

```text
About 2 hours 13 minutes
```

That is painful if the business moves files like this regularly.

### Example: 100 GB Over 1 Gbps

Same file:

```text
800,000,000,000 bits
```

Link speed:

```text
1 Gbps = 1,000,000,000 bits per second
```

Transfer time:

```text
800,000,000,000 / 1,000,000,000 = 800 seconds
```

Convert:

```text
800 / 60 = 13.3 minutes
```

Result:

```text
About 13 minutes 20 seconds
```

This is a huge improvement over 100 Mbps.

### Add Real-World Overhead

Perfect math assumes every bit of link capacity carries file data.

Real networks do not work that way.

Data is broken into packets/frames.

Each unit carries extra information:

- Ethernet headers;
- IP headers;
- TCP/UDP headers;
- checksums;
- inter-frame gaps;
- acknowledgments;
- retransmissions if needed;
- encryption/tunneling overhead;
- protocol overhead.

This is overhead.

Practical estimate:

```text
Add about 20% overhead for rough planning.
```

Example:

```text
13.3 minutes * 1.2 = 16 minutes
```

So a 100 GB transfer over 1 Gbps may be closer to 16 minutes in real life.

### Data Does Not Move As One Giant Blob

Your computer does not throw a 100 GB file across the wire as one huge object.

It breaks data into smaller pieces.

At different layers those are called:

- segments;
- packets;
- frames;
- bits on the wire.

Each piece needs addressing/control information.

That is why overhead exists.

### Why This Matters For Design

If you understand transfer math, you can reason about:

- access port speed;
- switch uplink speed;
- server/storage links;
- backup windows;
- WAN links;
- internet circuits;
- camera/video traffic;
- file server performance;
- link aggregation needs;
- bottlenecks.

Example:

If ten users each copy large files through a single 1 Gbps uplink, that uplink may become the bottleneck.

Interface speed is not only about one device.

It is about total traffic path.

### Bottleneck Thinking

A transfer path may include:

```text
PC -> access switch -> uplink -> core/distribution -> server
```

Effective speed is limited by the slowest constrained point.

Example:

```text
PC link:        1 Gbps
Switch uplink:  1 Gbps
Server link:    10 Gbps
```

If many PCs share one 1 Gbps uplink, the uplink can become congested.

That is why uplink planning matters.

### Practice Examples

Try calculating:

- `1 MB` over `100 Mbps`;
- `250 GB` backup over `1 Gbps`;
- `1 TB` archive over `10 Gbps`;
- `50 GB` video over `100 Mbps`;
- `500 MB` file over `1 Gbps`.

Do the math a few times until the conversion feels natural.

## Quick Reference

### Formula

```text
seconds = (file size in bytes * 8) / bits per second
```

### Common Speeds

| Speed | Bits per second |
| --- | --- |
| 10 Mbps | 10,000,000 bps |
| 100 Mbps | 100,000,000 bps |
| 1 Gbps | 1,000,000,000 bps |
| 10 Gbps | 10,000,000,000 bps |

### Common Conversions

| File size | Bits |
| --- | --- |
| 1 MB | 8,000,000 bits |
| 1 GB | 8,000,000,000 bits |
| 100 GB | 800,000,000,000 bits |
| 1 TB | 8,000,000,000,000 bits |

## Quick Self-Check

### Question 1

What is the difference between bytes and bits?

Answer:

```text
Bytes usually measure storage/file size; bits usually measure network transfer speed.
```

### Question 2

How many bits are in one byte?

Answer:

```text
8 bits.
```

### Question 3

What is the formula for transfer time?

Answer:

```text
file size in bits / link speed in bits per second
```

### Question 4

How long does a 100 GB file take over 1 Gbps in perfect math?

Answer:

```text
About 800 seconds, or 13.3 minutes.
```

### Question 5

Why should you add overhead to estimates?

Answer:

```text
Real traffic includes headers, acknowledgments, encapsulation, retransmissions and other overhead.
```

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Byte | 8 bits, commonly used for file/storage size. |
| Bit | Smallest binary unit, 0 or 1. |
| `B` | Byte. |
| `b` | bit. |
| Mbps | Megabits per second. |
| Gbps | Gigabits per second. |
| Bandwidth | Maximum theoretical capacity of a link. |
| Throughput | Actual achieved data rate. |
| Overhead | Extra protocol/control data beyond payload. |
| Bottleneck | Slowest constrained point in a path. |
| Link aggregation | Combining multiple physical links for more capacity/redundancy. |

## What To Review Later

- Ethernet speeds
- Duplex
- Throughput vs bandwidth
- TCP overhead
- WAN sizing
- Uplink planning
- Link aggregation
- QoS basics
- Backup window planning

