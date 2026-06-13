# Decimal To Binary Conversion For IPv4 Subnetting

Source: closed course page  
Date added: 2026-06-13  
Related plan item: Week 7 / Decimal to binary conversion  
Tags: subnetting, binary, decimal, IPv4, octet, bit, powers of two
Language: English
Translation pair: articles/2026-06/week-07/06-decimal-to-binary-conversion.md

## Summary

IPv4 subnetting requires confidently converting decimal values from `0` through `255` into eight-bit binary.

Each position in an IPv4 octet has a fixed weight:

```text
128  64  32  16   8   4   2   1
```

Write `1` when a position's value is used and `0` when it is not.

For example:

```text
153 = 128 + 16 + 8 + 1
153 = 10011001
```

This is not an isolated math trick. Binary reveals which bits belong to the network portion, which belong to the host portion and where subnet boundaries occur.

## Key Points

- A bit has one of two values: `0` or `1`.
- A byte contains 8 bits.
- An IPv4 address contains 4 octets, or 32 bits.
- One octet represents a value from `0` through `255`.
- The eight positional weights are `128`, `64`, `32`, `16`, `8`, `4`, `2` and `1`.
- A `1` includes that position's weight in the total.
- A `0` excludes it.
- Write a binary octet with all eight bits, including leading zeros.
- Decimal-to-binary conversion supports subnet masks, prefixes, network addresses and broadcast calculations.

## Why Network Engineers Need Binary

An IPv4 address is normally written in human-friendly dotted-decimal notation:

```text
192.168.1.10
```

Each decimal octet represents 8 bits:

```text
192      168      1        10
11000000 10101000 00000001 00001010
```

A subnet mask is also a 32-bit value:

```text
255.255.255.0
11111111.11111111.11111111.00000000
```

Binary makes the boundary between the network and host portions visible. Understanding the bits makes subnetting predictable instead of dependent on memorizing disconnected tables.

## Bits, Bytes And Octets

### Bit

A bit is the smallest unit of binary data:

```text
0
```

or:

```text
1
```

### Byte

A byte contains 8 bits:

```text
00000000
```

### Octet

In IPv4, an 8-bit group is commonly called an octet:

```text
1 octet = 8 bits
4 octets = 32 bits
```

For example:

```text
IPv4: 172.16.5.25

Octet 1: 172
Octet 2: 16
Octet 3: 5
Octet 4: 25
```

Convert each octet independently.

## Binary Positional Weights

The positions in one octet have these values:

| Bit position | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Weight | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

Moving from right to left, every weight doubles:

```text
1, 2, 4, 8, 16, 32, 64, 128
```

These are powers of two:

| Power | Value |
| --- | ---: |
| `2^0` | 1 |
| `2^1` | 2 |
| `2^2` | 4 |
| `2^3` | 8 |
| `2^4` | 16 |
| `2^5` | 32 |
| `2^6` | 64 |
| `2^7` | 128 |

Written left to right, an octet uses the reverse order:

```text
128 64 32 16 8 4 2 1
```

## The Fixed-Container Model

Think of binary as eight containers with fixed capacities:

```text
[128] [64] [32] [16] [8] [4] [2] [1]
```

Select the containers needed to make the decimal value:

- `1` means use this container;
- `0` means skip it.

For decimal `20`:

```text
20 = 16 + 4
```

Flags:

```text
Weights: 128 64 32 16  8  4  2  1
Bits:      0  0  0  1  0  1  0  0
```

Result:

```text
20 = 00010100
```

## Decimal-To-Binary Algorithm

For a value from `0` through `255`:

1. Write the weights `128 64 32 16 8 4 2 1`.
2. Start with `128`.
3. Ask whether the current weight fits into the remaining value.
4. If it does, write `1` and subtract the weight.
5. If it does not, write `0`.
6. Move to the next weight.
7. Continue through the `1` position.
8. Verify the result by adding the selected weights.

Template:

```text
Decimal value: N

Weight: 128 64 32 16 8 4 2 1
Bit:      ?  ?  ?  ? ? ? ? ?
```

## Example 1: Decimal 153

Starting value:

```text
153
```

Check each weight:

| Weight | Fits? | Bit | Remainder |
| ---: | --- | ---: | ---: |
| 128 | Yes | 1 | `153 - 128 = 25` |
| 64 | No | 0 | 25 |
| 32 | No | 0 | 25 |
| 16 | Yes | 1 | `25 - 16 = 9` |
| 8 | Yes | 1 | `9 - 8 = 1` |
| 4 | No | 0 | 1 |
| 2 | No | 0 | 1 |
| 1 | Yes | 1 | `1 - 1 = 0` |

Therefore:

```text
Weights: 128 64 32 16 8 4 2 1
Bits:      1  0  0  1 1 0 0 1

153 = 10011001
```

Check:

```text
128 + 16 + 8 + 1 = 153
```

## Example 2: Decimal 210

Decomposition:

```text
210 = 128 + 64 + 16 + 2
```

```text
Weights: 128 64 32 16 8 4 2 1
Bits:      1  1  0  1 0 0 1 0
```

Result:

```text
210 = 11010010
```

Check:

```text
128 + 64 + 16 + 2 = 210
```

## Example 3: Decimal 20

Decomposition:

```text
20 = 16 + 4
```

```text
Weights: 128 64 32 16 8 4 2 1
Bits:      0  0  0  1 0 1 0 0
```

Result:

```text
20 = 00010100
```

Leading zeros matter. `10100` is mathematically the same value, but `00010100` clearly displays a complete IPv4 octet.

## Example 4: Decimal 192

```text
192 = 128 + 64
```

```text
Weights: 128 64 32 16 8 4 2 1
Bits:      1  1  0  0 0 0 0 0
```

```text
192 = 11000000
```

This value frequently appears in the private IPv4 range `192.168.0.0/16`.

## Example 5: Decimal 168

```text
168 = 128 + 32 + 8
```

```text
Weights: 128 64 32 16 8 4 2 1
Bits:      1  0  1  0 1 0 0 0
```

```text
168 = 10101000
```

The first two octets of `192.168.1.10` are therefore:

```text
192 = 11000000
168 = 10101000
```

## Why The Maximum Is 255

When all eight bits are `1`, every weight is selected:

```text
11111111
```

```text
128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = 255
```

One IPv4 octet therefore ranges from:

```text
00000000 = 0
11111111 = 255
```

Eight bits represent:

```text
2^8 = 256 different values
```

Those values run from `0` through `255`, not from `1` through `256`.

## Important Boundary Values

| Decimal | Binary | Explanation |
| ---: | --- | --- |
| 0 | `00000000` | No weights are selected |
| 1 | `00000001` | Only weight 1 is selected |
| 2 | `00000010` | Only weight 2 is selected |
| 127 | `01111111` | Every weight except 128 |
| 128 | `10000000` | Only weight 128 |
| 254 | `11111110` | Every weight except 1 |
| 255 | `11111111` | Every weight is selected |

Learn to recognize this sequence:

```text
128 = 10000000
192 = 11000000
224 = 11100000
240 = 11110000
248 = 11111000
252 = 11111100
254 = 11111110
255 = 11111111
```

It appears again in subnet masks.

## Reverse Check: Binary To Decimal

To verify a conversion, add the weights containing `1`.

Example:

```text
10110110
```

```text
Weights: 128 64 32 16 8 4 2 1
Bits:      1  0  1  1 0 1 1 0
```

Selected weights:

```text
128 + 32 + 16 + 4 + 2 = 182
```

Therefore:

```text
10110110 = 182
```

This reverse check catches a missing bit or a subtraction error.

## Faster Addition Method

You do not have to perform every subtraction after gaining experience. You can directly select powers of two that form the value.

For example:

```text
100 = 64 + 32 + 4
```

```text
100 = 01100100
```

Or:

```text
200 = 128 + 64 + 8
```

```text
200 = 11001000
```

The subtraction method is safer initially. Direct addition becomes faster once the weights are familiar.

## Converting A Complete IPv4 Address

Take:

```text
192.168.1.10
```

Convert every octet:

| Decimal octet | Binary octet |
| ---: | --- |
| 192 | `11000000` |
| 168 | `10101000` |
| 1 | `00000001` |
| 10 | `00001010` |

Full representation:

```text
11000000.10101000.00000001.00001010
```

The dots separate octets and are not bits.

## Connection To Subnet Masks

Consider:

```text
255.255.255.0
```

In binary:

```text
11111111.11111111.11111111.00000000
```

This corresponds to:

```text
/24
```

The first 24 bits are `1` and identify the network portion. The final 8 bits are `0` and identify the host portion.

Another example:

```text
255.255.255.192
```

Last octet:

```text
192 = 11000000
```

Complete mask:

```text
11111111.11111111.11111111.11000000
```

This is:

```text
/26
```

Binary shows why decimal mask value `192` adds two network bits.

## Why Subnet-Mask Ones Are Contiguous

A normal IPv4 subnet mask contains a continuous sequence of `1` bits followed only by `0` bits:

```text
11111111.11111111.11110000.00000000
```

This pattern represents `/20`.

An octet containing the transition from network bits to host bits can only be one of these:

| Binary | Decimal |
| --- | ---: |
| `00000000` | 0 |
| `10000000` | 128 |
| `11000000` | 192 |
| `11100000` | 224 |
| `11110000` | 240 |
| `11111000` | 248 |
| `11111100` | 252 |
| `11111110` | 254 |
| `11111111` | 255 |

A value such as `10101000` is a valid binary octet, but it is not a valid transition octet in a normal contiguous subnet mask because its ones are separated by zeros.

## Practice

Convert these values into 8-bit binary:

1. `5`
2. `10`
3. `25`
4. `64`
5. `85`
6. `100`
7. `172`
8. `200`
9. `224`
10. `250`

### Answers

| Decimal | Binary |
| ---: | --- |
| 5 | `00000101` |
| 10 | `00001010` |
| 25 | `00011001` |
| 64 | `01000000` |
| 85 | `01010101` |
| 100 | `01100100` |
| 172 | `10101100` |
| 200 | `11001000` |
| 224 | `11100000` |
| 250 | `11111010` |

## Complete-Address Practice

Convert:

```text
10.20.30.40
```

Answer:

```text
00001010.00010100.00011110.00101000
```

Convert:

```text
172.16.100.254
```

Answer:

```text
10101100.00010000.01100100.11111110
```

## Practical Learning Approach

When learning:

1. Complete 10 to 15 conversions manually.
2. Write the positional weights every time.
3. Keep all 8 bits.
4. Verify each answer by adding selected weights.
5. Use a calculator only after making a manual attempt.
6. Repeat subnet-mask values until recognition is immediate.

Using a calculator, spreadsheet or IPAM in production is not a mistake. Engineering tools reduce accidental arithmetic errors. Manual skill is still necessary to interpret results, identify impossible values quickly and work during exams or troubleshooting without depending on one tool.

## Common Mistakes

### Writing Fewer Than Eight Bits

```text
20 = 10100
```

This is mathematically valid, but IPv4 notation is clearer as:

```text
20 = 00010100
```

### Reversing The Weights

The correct left-to-right order is:

```text
128 64 32 16 8 4 2 1
```

### Forgetting To Subtract A Selected Weight

After writing `1`, subtract that weight from the remainder.

### Treating 256 As A Valid Octet

An octet has 256 possible states, but its highest value is `255` because counting starts at `0`.

### Confusing Position With Weight

The leftmost position has weight `128`, not `8`.

### Checking Only By Appearance

A binary pattern can look plausible and still be wrong. Add the selected weights.

### Treating Every Binary Value As A Valid Subnet Mask

Every octet from `00000000` through `11111111` is a valid number, but a normal subnet mask requires contiguous ones.

## Quick Self-Check

### Question 1

What are the positional weights in an IPv4 octet?

Answer:

```text
128, 64, 32, 16, 8, 4, 2, 1
```

### Question 2

Why can an octet not exceed `255`?

Answer:

```text
An octet has only 8 bits. With all bits enabled:
128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = 255.
```

### Question 3

How is `153` written in binary?

Answer:

```text
153 = 128 + 16 + 8 + 1 = 10011001
```

### Question 4

Why write `20` as `00010100` instead of only `10100`?

Answer:

```text
The full eight-bit form clearly shows the IPv4 octet boundary.
```

### Question 5

How do you verify `11010010`?

Answer:

```text
128 + 64 + 16 + 2 = 210
```

### Question 6

What is decimal `192` in binary, and why is it important?

Answer:

```text
192 = 11000000. In a subnet mask it represents two network bits
in that octet.
```

## Commands And Terms

| Term | Meaning |
| --- | --- |
| Bit | One binary digit: `0` or `1`. |
| Byte | A group of 8 bits. |
| Octet | An 8-bit group in IPv4 notation. |
| Decimal | Base-10 number system. |
| Binary | Base-2 number system. |
| Bit weight | Decimal value assigned to a bit position. |
| Leading zero | A zero on the left preserving full octet width. |
| Dotted decimal | Normal IPv4 notation using four decimal octets. |
| Network portion | Bits identifying the network. |
| Host portion | Bits identifying an interface inside the network. |

## What To Review Later

- Binary-to-decimal conversion
- Powers of two
- IPv4 address structure
- Subnet-mask binary patterns
- CIDR prefix length
- Network and host portions
- Block size
- Network and broadcast calculation

