# What Now? IP Addressing Foundations

Source: закрытая страница курса  
Date added: 2026-06-01  
Related plan item: Week 5 / IP addressing checkpoint before routers  
Tags: ip addressing, cidr, subnet mask, block size, switch management, router, troubleshooting
Language: Russian
Translation pair: articles-en/2026-05/week-05/04-what-now-ip-addressing-foundations.md

## Summary

Этот урок - checkpoint после первых тем по IP addressing. Мы уже понимаем, зачем нужны IP addresses, как subnet mask определяет network boundary, чем private IPs отличаются от public, и как начальный addressing plan строится из требований бизнеса.

Главная мысль: IP addressing перестает быть набором чисел и начинает выглядеть как система, с которой можно работать.

## Key Points

- IP addressing fundamentals are practical, not just theory.
- CIDR notation помогает описывать network size.
- Block size patterns подготавливают к subnetting.
- Subnet mask помогает понять, что local, а что remote.
- Private IPs and NAT объясняют, как internal devices выходят в internet.
- Addressing plan должен отражать business requirements.
- Switch может не нуждаться в IP для Layer 2 forwarding, но ему нужен IP for management.
- Routers используют IP addressing для соединения разных networks.
- Troubleshooting часто начинается с проверки IP address, subnet mask and gateway.
- Следующий большой шаг - router configuration.

## Notes

### This Is Real Networking

Когда ты изучаешь basics, легко подумать:

```text
When do we get to real networking?
```

Ответ:

```text
This is real networking.
```

IP addressing, masks, CIDR, private ranges and gateways - это не "разогрев".

Это foundation, на котором стоят:

- router configuration;
- subnetting;
- VLAN design;
- inter-VLAN routing;
- routing tables;
- firewall rules;
- troubleshooting;
- network documentation.

Если IP foundation слабый, все следующие темы будут ощущаться chaotic.

Если foundation нормальный, router topics начинают складываться логично.

### You Know More Than You Think

К этому моменту ты уже умеешь:

- понимать структуру IPv4 address;
- видеть network and host portions;
- читать простые subnet masks;
- понимать `/24`;
- узнавать private IPv4 ranges;
- объяснять зачем нужен NAT;
- понимать почему large flat networks плохи;
- видеть зачем нужны separate network segments;
- создавать простой addressing pattern for sites.

Это уже рабочий набор навыков.

Не весь subnetting еще изучен глубоко, но pattern уже начал появляться.

### CIDR Is Shorthand For Network Size

CIDR notation выглядит так:

```text
192.168.10.0/24
```

`/24` говорит, сколько bits относится к network portion.

В familiar decimal mask:

```text
/24 = 255.255.255.0
```

CIDR помогает быстро описывать size and boundary сети.

Позже CIDR станет еще важнее, когда мы начнем считать:

- block sizes;
- number of subnets;
- usable host addresses;
- summary routes.

### Block Size Pattern

В initial addressing design мы уже использовали pattern:

```text
Shop 1 = 192.168.0.0/24 - 192.168.3.0/24
Shop 2 = 192.168.4.0/24 - 192.168.7.0/24
Shop 3 = 192.168.8.0/24 - 192.168.11.0/24
```

То есть:

```text
Four /24 networks per shop.
```

Это не random.

Pattern помогает:

- видеть structure;
- оставлять growth room;
- упростить documentation;
- готовиться к summarization;
- думать subnetting blocks.

Subnetting становится легче, когда ты сначала видишь rhythm of address blocks.

### What This Lets You Do Right Now

С этими знаниями ты уже можешь начать basic device addressing.

Например:

- назначить IP address PC;
- проверить subnet mask;
- понять local vs remote destination;
- настроить default gateway;
- дать management IP switch;
- построить простой addressing plan для small site;
- заметить obvious addressing mistakes.

Это практическая skill.

Не просто exam definition.

### Switches And Management IPs

Switch работает на Layer 2 и пересылает frames по MAC addresses.

Для basic switching ему не нужен IP address.

Но в реальной сети switch often gets management IP.

Зачем:

- remote login;
- SSH management;
- monitoring;
- SNMP;
- configuration;
- troubleshooting;
- firmware/software tasks.

Memory hook:

```text
Switching traffic does not require switch IP.
Managing the switch over the network does.
```

Пример:

```text
Switch management IP: 192.168.10.2/24
Default gateway:      192.168.10.1
```

Теперь admin может reach switch remotely, если routing and access rules позволяют.

### Routers Are The Next Step

До этого мы говорили о devices inside networks.

Routers connect networks.

Router uses IP addressing more actively:

- decides where traffic should go;
- has interfaces in different networks;
- acts as default gateway;
- forwards packets between subnets;
- uses routing table;
- separates broadcast domains.

Если host хочет говорить outside local network, он отправляет traffic to default gateway.

That gateway is usually router interface IP.

Example:

```text
PC IP:        192.168.10.50
Mask:         255.255.255.0
Gateway:      192.168.10.1
Router int:   192.168.10.1
```

Router becomes the doorway to other networks.

### Troubleshooting Fuel

На работе confidence часто начинается с простых вопросов:

```text
Is the IP address correct?
Is the subnet mask correct?
Is the default gateway correct?
Is this destination local or remote?
Is this IP private or public?
Is there an overlap?
```

Bad addressing breaks everything quickly.

Если device не может connect, IP settings - одно из первых мест для проверки.

Typical issues:

- wrong subnet mask;
- missing default gateway;
- wrong gateway;
- duplicate IP address;
- address from wrong subnet;
- private/public misunderstanding;
- overlapping subnets across VPN/sites.

### This Is A Launchpad

Мы еще не закончили subnetting.

Мы только начали видеть:

- masks;
- CIDR;
- blocks;
- private ranges;
- network boundaries.

Позже мы вернемся и углубимся в mechanics.

Но сейчас важно понять: ты уже пересек важную линию.

Ты не просто слышишь terms.

Ты начинаешь ими пользоваться.

### What Comes Next

Next step:

```text
Router configuration.
```

Почему routers next:

- they connect networks;
- they need IP addresses on interfaces;
- they use masks to understand connected networks;
- they become default gateways;
- they move packets between subnets.

Everything we learned about IP addressing becomes immediately useful on routers.

## Practical Checklist

Before moving into router configuration, make sure you can explain:

- what an IP address identifies;
- what a subnet mask defines;
- what `/24` means;
- what a default gateway does;
- what private IP ranges are;
- what NAT does;
- why switches may need management IPs;
- why routers stop broadcasts;
- why network segments exist;
- why clean addressing plans matter.

## Quick Self-Check

### Question 1

Does a Layer 2 switch need an IP address to forward frames?

Answer:

```text
No. It forwards frames using MAC addresses.
```

### Question 2

Why give a switch an IP address?

Answer:

```text
For management, monitoring, remote access and troubleshooting.
```

### Question 3

What is the next major device type after basic IP addressing?

Answer:

```text
Routers, because they connect different networks.
```

### Question 4

Why is CIDR notation useful?

Answer:

```text
It gives a compact way to describe network size and boundary.
```

### Question 5

Why does bad addressing cause outages quickly?

Answer:

```text
Because devices may think destinations are local/remote incorrectly or may not know where to send traffic.
```

## Commands / Terms

| Term | Meaning |
| --- | --- |
| CIDR | Classless Inter-Domain Routing, prefix notation like `/24`. |
| Block size | Addressing pattern/increment used when dividing networks. |
| Management IP | IP address used to manage a network device remotely. |
| Default gateway | Router address a host uses to reach remote networks. |
| Router | Device that forwards packets between networks. |
| Local destination | Destination inside the same subnet. |
| Remote destination | Destination outside the local subnet. |
| Troubleshooting | Structured process of finding and fixing problems. |

## What To Review Later

- Router interface configuration
- Default gateway
- Static routes
- Connected routes
- VLAN management interfaces
- Subnetting block sizes
- CIDR notation
- IP troubleshooting commands

