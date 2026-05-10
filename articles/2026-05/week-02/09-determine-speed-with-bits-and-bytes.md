# Determine Speed with Bits and Bytes

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Network speed basics  
Tags: bits, bytes, bandwidth, speed, gbps, mbps, transfer rate, file size, conversion

## Summary

Network speed обычно измеряется в bits per second, а file size и storage - в bytes. Разница между lowercase `b` и uppercase `B` огромная: `b` means bits, `B` means bytes. Так как 1 byte = 8 bits, для примерной оценки transfer speed в bytes нужно разделить network speed на 8.

Главная мысль: storage обычно в bytes, network speed обычно в bits, а мост между ними - число 8.

## Key Points

- Bit - минимальная единица данных: `0` или `1`.
- Byte - группа из 8 bits.
- Bytes часто используют для file size and storage.
- Network speeds обычно измеряются в bits per second.
- Lowercase `b` means bits.
- Uppercase `B` means bytes.
- `Mbps` = megabits per second.
- `MBps` = megabytes per second.
- `Gbps` = gigabits per second.
- `GBps` = gigabytes per second.
- Чтобы перевести bits per second в bytes per second, делим на 8.
- 1 Gbps = 1,000 Mbps.
- 1,000 Mbps / 8 = примерно 125 MBps.
- 100 MB file over ideal 125 MBps link takes about 0.8 seconds.
- Реальная скорость ниже из-за overhead, latency, protocol behavior, wireless interference and congestion.

## Notes

### Bit and Byte

Bit - это один binary value:

```text
0 or 1
```

Byte - это 8 bits.

Файлы и storage обычно удобнее считать в bytes:

- KB;
- MB;
- GB;
- TB.

Network links обычно описываются в bits per second:

- Mbps;
- Gbps;
- Tbps.

### The Letter Problem

Разница в одной букве меняет смысл:

```text
Mb = megabit
MB = megabyte
Gb = gigabit
GB = gigabyte
```

Если пользователь говорит "100 megabyte internet", почти всегда он имеет в виду `100 megabit`.

### Simple Conversion

Пример для 1 Gbps link:

```text
1 Gbps = 1,000 Mbps
1,000 Mbps / 8 = 125 MBps
```

Пример transfer time:

```text
100 MB file / 125 MBps = 0.8 seconds
```

Это ideal baseline, а не гарантия.

### Why It Matters

Для маленькой кофейни 1 Gbps может быть более чем достаточно. Но для backups, video editing, server replication or cloud transfers нужно уметь оценивать link capacity.

Без понимания bits vs bytes легко купить не тот тариф, неправильно оценить transfer time или неверно объяснить пользователю ожидания.

## Commands / Terms

```text
bit - 0 or 1
byte - 8 bits
Mbps - megabits per second
MBps - megabytes per second
Gbps - gigabits per second
GBps - gigabytes per second
Formula: bits / 8 = bytes
```

## Questions

### Почему 1 Gbps не означает 1 GB per second?

Потому что `Gbps` - это gigabits per second, а `GBps` - gigabytes per second. В одном byte 8 bits.

### Сколько примерно MBps дает 1 Gbps link?

Около 125 MBps в идеальных условиях.

### Почему реальная скорость может быть ниже?

Из-за overhead, latency, protocol behavior, wireless interference, congestion and device limits.

## What To Review Later

- Decimal vs binary units.
- Bandwidth vs throughput.
- Latency.
- Protocol overhead.
- ISP speed plans.
