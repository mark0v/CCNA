# Initial IP Addressing Design

Source: закрытая страница курса  
Date added: 2026-06-01  
Related plan item: Week 5 / Initial addressing design for Castle Rysen  
Tags: ip addressing, network design, subnetting, cidr, broadcast domain, vlan, summarization, rfp
Language: Russian
Translation pair: articles-en/2026-05/week-05/03-initial-ip-addressing-design.md

## Summary

Initial IP addressing design начинается не с random IP ranges, а с business requirements. Нужно понять, сколько sites есть у организации, какие traffic types нужно разделить, где нужен growth room и как addressing plan будет масштабироваться.

Главная мысль: хороший addressing plan переводит бизнес-требования в предсказуемую техническую структуру.

## Key Points

- Network design starts with requirements, not with random IPs.
- RFP помогает понять scale, sites and segmentation needs.
- Network segment - логическая часть сети, обычно отдельный broadcast domain.
- Router останавливает broadcasts между network segments.
- District shop может требовать несколько segments: internal, voice, guest.
- VLANs часто используются для logical separation внутри одного switching environment.
- `/24` означает subnet mask `255.255.255.0`.
- Для shop удобно выделять blocks по четыре `/24` networks: три active + one spare.
- Spare network оставляет room for growth.
- Clean grouped addressing помогает future route summarization.
- Predictable addressing упрощает troubleshooting, routing and expansion.

## Notes

### Start With The Business

Когда появляется задача "address the network", нельзя просто открыть таблицу и начать писать IP ranges.

Сначала нужно понять бизнес:

- сколько locations;
- какие типы sites;
- как sites связаны друг с другом;
- сколько users/devices;
- какие traffic types нужно разделить;
- где нужен growth;
- какие future services могут появиться.

Для Castle Rysen эти ответы приходят из RFP.

RFP tells us:

- есть central office;
- central office supports fallout shelters;
- fallout shelters support district shops;
- each district shop needs separate network segments.

Это уже не flat network.

Это structured design problem.

### Translate Business Language Into Network Design

Business requirement:

```text
Separate internal communication, voice traffic and guest access.
```

Network designer hears:

```text
We need multiple network segments.
```

Это важный translation step.

Бизнес обычно не говорит:

```text
Create VLAN 10, VLAN 20 and VLAN 30 with separate subnets.
```

Бизнес говорит:

```text
Employees, phones and guests should be separated.
```

Твоя задача как network person - превратить это в:

- segments;
- subnets;
- VLANs later;
- routing boundaries;
- security policy;
- addressing plan.

### What Is A Network Segment

Network segment - это отдельная логическая часть сети, где devices находятся в одном local network space.

Близкий термин:

```text
broadcast domain
```

Broadcast domain отвечает на вопрос:

```text
Как далеко пройдет broadcast?
```

Например, ARP request является broadcast.

Если broadcast остается внутри одного segment, это хорошо.

Если broadcast начинает лететь везде, сеть быстро становится шумной.

### Routers Stop Broadcasts

Router не пропускает обычные Layer 2 broadcasts между networks.

Это одна из ключевых функций router:

```text
Stop broadcasts at the network boundary.
```

Когда мы создаем routed boundary, мы фактически создаем отдельный network segment.

Поэтому если district shop требует три segments, мы думаем:

```text
Internal users = one segment
Voice devices  = one segment
Guest access   = one segment
```

Каждый segment должен иметь свой IP network.

### VLAN Sidebar

В реальной сети внутри одного shop часто не ставят три физически отдельные сети.

Обычно используют VLANs.

VLAN means:

```text
Virtual LAN
```

VLAN позволяет разделить один physical switching environment на несколько logical networks.

Например:

```text
VLAN 10 = Internal
VLAN 20 = Voice
VLAN 30 = Guest
```

Мы еще не углубляемся в VLANs, но важно увидеть, что RFP уже намекает на будущую design direction.

### Why Use /24 For The First Design

На этом этапе удобно использовать `/24` networks.

`/24` means:

```text
255.255.255.0
```

Обычно это дает:

```text
254 usable host addresses
```

Для small district shop этого достаточно для:

- registers;
- laptops;
- phones;
- printers;
- guest Wi-Fi clients;
- cameras;
- tablets;
- access points.

`/24` also easy to read and easy to teach.

Позже можно делать more efficient subnetting, но initial high-level design лучше держать понятным.

### Shop Addressing Pattern

Для first shop можно выделить четыре `/24` networks:

```text
192.168.0.0/24  = Shop 1 Internal
192.168.1.0/24  = Shop 1 Voice
192.168.2.0/24  = Shop 1 Guest
192.168.3.0/24  = Shop 1 Spare
```

Почему четыре?

Потому что сейчас нужны три active segments, но spare оставляет room for growth.

Future use cases:

- cameras;
- IoT devices;
- dedicated management network;
- security systems;
- separate payment devices;
- new business service.

Spare space помогает не переделывать addressing plan при первом же изменении.

### Blocks Of Four

Следующий shop получает next block of four:

```text
192.168.4.0/24  = Shop 2 Internal
192.168.5.0/24  = Shop 2 Voice
192.168.6.0/24  = Shop 2 Guest
192.168.7.0/24  = Shop 2 Spare
```

Third shop:

```text
192.168.8.0/24   = Shop 3 Internal
192.168.9.0/24   = Shop 3 Voice
192.168.10.0/24  = Shop 3 Guest
192.168.11.0/24  = Shop 3 Spare
```

Pattern:

```text
Shop 1 = 0-3
Shop 2 = 4-7
Shop 3 = 8-11
```

Это clean, predictable and expandable.

### Why Grouping Matters

Grouping networks in clean blocks helps later with:

- troubleshooting;
- documentation;
- site identification;
- route summarization;
- avoiding overlap;
- faster mental parsing.

Route summarization means we can represent multiple related networks with one larger route.

Пока не нужно знать все mechanics, но idea important:

```text
Clean blocks today can mean cleaner routing tomorrow.
```

Если addressing random, future routing tables and troubleshooting become painful.

### Thinking Beyond One Shop

Если проектировать enterprise from day one, может быть логично использовать larger private range:

```text
10.0.0.0/8
```

Почему?

Castle Rysen может иметь:

- central office;
- many fallout shelters;
- many district shops;
- regions;
- guest networks;
- voice networks;
- internal networks;
- future services.

Large range gives room.

Но для обучения полезно сначала focus on one district shop.

Если мы решим весь global design до того, как хорошо понимаем one shop, будет слишком много moving parts.

### Fallout Shelters And Address Space Planning

Для fallout shelters можно начать с другого конца range или выделить separate blocks, чтобы не overlap with shop allocations.

Это не random.

Хороший design:

- оставляет space for shops;
- оставляет space for shelters;
- оставляет space for central office;
- avoids overlap;
- uses predictable patterns.

Predictable addressing looks boring.

That is good.

В больших сетях boring and predictable - это сила.

### CIDR Term

CIDR stands for:

```text
Classless Inter-Domain Routing
```

CIDR notation uses prefix length:

```text
192.168.0.0/24
```

`/24` tells us how many bits belong to network portion.

Equivalent decimal mask:

```text
255.255.255.0
```

CIDR lets us move beyond old classful boundaries and design networks flexibly.

### Design Process

Useful process:

1. Read requirements.
2. Identify sites.
3. Identify traffic groups.
4. Decide required segments.
5. Pick private address space.
6. Assign predictable blocks.
7. Leave spare networks.
8. Document everything.
9. Check for overlap.
10. Think about future routing and summarization.

Do not start with IPs.

Start with the structure.

### Real World Tip

When building an addressing plan:

```text
Do not solve only today's problem.
```

Leave room for:

- growth;
- new sites;
- new services;
- security separation;
- route summarization;
- future troubleshooting.

Future-you will be very happy when expansion does not require renumbering every device.

## Example Addressing Plan

### Shop 1

| Segment | Network | Purpose |
| --- | --- | --- |
| Internal | `192.168.0.0/24` | Employee devices and internal systems. |
| Voice | `192.168.1.0/24` | IP phones and voice devices. |
| Guest | `192.168.2.0/24` | Guest Wi-Fi clients. |
| Spare | `192.168.3.0/24` | Future growth. |

### Shop 2

| Segment | Network | Purpose |
| --- | --- | --- |
| Internal | `192.168.4.0/24` | Employee devices and internal systems. |
| Voice | `192.168.5.0/24` | IP phones and voice devices. |
| Guest | `192.168.6.0/24` | Guest Wi-Fi clients. |
| Spare | `192.168.7.0/24` | Future growth. |

### Shop 3

| Segment | Network | Purpose |
| --- | --- | --- |
| Internal | `192.168.8.0/24` | Employee devices and internal systems. |
| Voice | `192.168.9.0/24` | IP phones and voice devices. |
| Guest | `192.168.10.0/24` | Guest Wi-Fi clients. |
| Spare | `192.168.11.0/24` | Future growth. |

## Practice Exercise

Use `172.16.0.0` private range.

Address three cafes.

Each cafe needs:

- internal segment;
- voice segment;
- guest segment;
- one spare network.

Use `/24` networks.

One possible answer:

```text
Cafe 1 Internal = 172.16.0.0/24
Cafe 1 Voice    = 172.16.1.0/24
Cafe 1 Guest    = 172.16.2.0/24
Cafe 1 Spare    = 172.16.3.0/24

Cafe 2 Internal = 172.16.4.0/24
Cafe 2 Voice    = 172.16.5.0/24
Cafe 2 Guest    = 172.16.6.0/24
Cafe 2 Spare    = 172.16.7.0/24

Cafe 3 Internal = 172.16.8.0/24
Cafe 3 Voice    = 172.16.9.0/24
Cafe 3 Guest    = 172.16.10.0/24
Cafe 3 Spare    = 172.16.11.0/24
```

The pattern is the point.

## Quick Self-Check

### Question 1

What should network design start with?

Answer:

```text
Business requirements.
```

### Question 2

What is a broadcast domain?

Answer:

```text
The area where a broadcast message can travel before a router or boundary stops it.
```

### Question 3

Why use one spare `/24` per shop?

Answer:

```text
To leave room for future growth without redesigning the addressing plan.
```

### Question 4

What does `/24` mean?

Answer:

```text
A 24-bit network prefix, equivalent to subnet mask 255.255.255.0.
```

### Question 5

Why group networks in clean blocks?

Answer:

```text
It helps documentation, troubleshooting, growth and future route summarization.
```

## Commands / Terms

| Term | Meaning |
| --- | --- |
| RFP | Request for proposal, document with business/project requirements. |
| Network segment | Separate logical part of a network. |
| Broadcast domain | Area where broadcast traffic is heard. |
| VLAN | Virtual LAN, logical Layer 2 separation inside switching infrastructure. |
| CIDR | Classless Inter-Domain Routing. |
| `/24` | Prefix length equivalent to `255.255.255.0`. |
| Route summarization | Representing multiple related networks with one larger route. |
| Spare network | Reserved network for future use. |
| Addressing plan | Structured assignment of IP ranges to sites and segments. |

## What To Review Later

- Subnet masks
- Private IP addresses
- VLANs
- Broadcast domains
- CIDR notation
- Route summarization
- Inter-VLAN routing
- Network documentation

