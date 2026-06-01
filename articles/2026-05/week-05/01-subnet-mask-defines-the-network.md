# Subnet Mask Defines the Network

Source: закрытая страница курса  
Date added: 2026-06-01  
Related plan item: Week 5 / Subnet mask and network boundaries  
Tags: subnet mask, ipv4, network portion, host portion, classful addressing, subnetting, default gateway
Language: Russian
Translation pair: articles-en/2026-05/week-05/01-subnet-mask-defines-the-network.md

## Summary

IP address сам по себе не говорит устройству, где заканчивается его local network и где начинается внешний мир. Эту границу задает subnet mask. Маска определяет, какая часть IPv4 address является network portion, а какая часть является host portion.

Главная мысль: subnet mask отвечает на вопрос "этот destination находится в моей сети или для него нужен router?"

## Key Points

- IP address без subnet mask неполон.
- Subnet mask определяет network portion и host portion.
- Network portion описывает саму сеть.
- Host portion описывает конкретное устройство внутри этой сети.
- Если destination local, host может отправлять traffic напрямую внутри LAN.
- Если destination remote, host отправляет traffic на default gateway.
- `255` в простой маске означает network part.
- `0` в простой маске означает host part.
- Default classful masks: Class A `/8`, Class B `/16`, Class C `/24`.
- Большие default networks неудобны и опасны для реальной эксплуатации.
- Subnetting делит большую сеть на меньшие, управляемые networks.
- `/24` часто дает 254 usable host addresses.

## Notes

### Why The Subnet Mask Matters

Когда мы задаем устройству IP address, кажется, что самое главное уже сделано.

Но это только половина истории.

Устройство должно понять:

```text
Кто находится в моей локальной сети?
Куда нужно идти через router?
```

Для этого и нужна subnet mask.

IP address говорит:

```text
Вот мой address.
```

Subnet mask говорит:

```text
Вот какая часть address описывает network.
Вот какая часть address описывает host.
```

Без этой границы device не может нормально принять routing decision.

### Network Portion And Host Portion

У IPv4 address есть две логические части:

- network portion;
- host portion.

Network portion отвечает за "район", то есть за network.

Host portion отвечает за "номер дома" внутри этого района, то есть за конкретное устройство.

Полезная аналогия:

```text
Network portion = neighborhood
Host portion = house number inside that neighborhood
```

Subnet mask как раз и показывает, где проходит граница между этими частями.

### Simple 255 And 0 Rule

Пока мы не ушли глубоко в binary, можно использовать простую модель:

```text
255 = эта часть IP address относится к network
0   = эта часть IP address относится к host
```

Это не вся теория subnetting, но для первого понимания работает отлично.

Пример:

```text
IP address:   10.5.90.110
Subnet mask:  255.0.0.0
```

Здесь:

```text
Network portion: 10
Host portion:    5.90.110
```

Устройство считает local все addresses, которые начинаются с `10`.

Другой пример:

```text
IP address:   172.21.160.5
Subnet mask:  255.255.0.0
```

Здесь:

```text
Network portion: 172.21
Host portion:    160.5
```

Устройство считает local все addresses, которые начинаются с `172.21`.

### Local Or Remote

Главная практическая задача subnet mask:

```text
Определить, destination local или remote.
```

Если destination local:

- host пытается доставить frame напрямую в local network;
- для IPv4 он может использовать ARP, чтобы найти destination MAC address;
- router не нужен.

Если destination remote:

- host понимает, что destination находится за пределами local network;
- host отправляет frame на MAC address default gateway;
- packet внутри frame все равно содержит final destination IP.

Subnet mask - это линия на песке:

```text
Эта сторона = моя сеть.
Другая сторона = нужен router.
```

### Default Gateway Can Be Missing, Mask Cannot

Host может жить без default gateway, если ему нужно общаться только внутри local network.

Например:

```text
IP address:   192.168.1.10
Subnet mask:  255.255.255.0
Gateway:      not configured
```

Такое устройство сможет говорить с другими hosts в `192.168.1.0/24`, если Layer 2 connectivity работает.

Но без subnet mask operating system не понимает, какая network local.

Поэтому IP address без mask - это incomplete configuration.

### A Quick Word About Octets

IPv4 address состоит из четырех octets.

Пример:

```text
192.168.10.25
```

Здесь:

- `192` = first octet;
- `168` = second octet;
- `10` = third octet;
- `25` = fourth octet.

Каждый octet находится в диапазоне от `0` до `255`.

Слово `octet` важно, потому что subnet masks тоже записываются четырьмя octets:

```text
255.255.255.0
```

### Classful Defaults

Исторически IPv4 addresses делили на классы:

| Class | First octet range | Default mask | Prefix |
| --- | --- | --- | --- |
| Class A | 1-126 | 255.0.0.0 | /8 |
| Class B | 128-191 | 255.255.0.0 | /16 |
| Class C | 192-223 | 255.255.255.0 | /24 |

Это называется classful addressing.

В современных сетях мы не должны думать только classful-логикой, потому что используется CIDR and subnetting. Но default masks помогают понять, откуда взялись привычные границы.

### Why Default Networks Are Too Big

Class A network вроде:

```text
10.0.0.0
255.0.0.0
```

имеет очень большое address space.

Количество usable host addresses:

```text
16,777,214
```

Это слишком много для одной normal local network.

Проблемы giant flat network:

- слишком много broadcast traffic;
- сложнее troubleshooting;
- хуже security boundaries;
- сложнее разделять departments/locations;
- сложнее контролировать growth;
- network становится менее предсказуемой.

В реальной жизни нам нужны smaller networks.

### What Subnetting Does

Subnetting - это процесс, где мы берем большую network и делим ее на меньшие networks.

Мы делаем это, меняя subnet mask.

Идея простая:

```text
Двигаем границу между network portion и host portion.
```

Чем больше bits отдано network portion, тем больше subnets можно получить.

Чем меньше bits осталось host portion, тем меньше hosts помещается в каждую subnet.

Это trade-off:

```text
more networks = fewer hosts per network
fewer networks = more hosts per network
```

### NetworkChuck Coffee Example

Представим NetworkChuck Coffee.

У нас есть большой private range:

```text
10.0.0.0
```

Если оставить default Class A mask:

```text
255.0.0.0
```

то получится одна огромная сеть.

Но бизнесу нужно несколько coffee shops, и каждой location удобнее дать отдельную subnet.

Например:

```text
10.0.1.0/24  = Coffee House 1
10.0.2.0/24  = Coffee House 2
10.0.3.0/24  = Coffee House 3
10.0.4.0/24  = Coffee House 4
```

`/24` означает:

```text
255.255.255.0
```

В такой subnet обычно:

```text
254 usable host addresses
```

Этого достаточно для:

- registers;
- laptops;
- printers;
- tablets;
- cameras;
- phones;
- access points;
- office devices.

Теперь каждая кофейня получает отдельную, понятную и управляемую network.

### Why Smaller Subnets Are Useful

Smaller subnets помогают:

- уменьшить broadcast domain;
- проще искать проблемы;
- разделять locations;
- применять security rules;
- планировать addressing;
- контролировать growth;
- делать routing более понятным.

Это не только exam topic.

Это реальная operational skill.

### Important Memory Hook

Запомни:

```text
IP address identifies the host.
Subnet mask defines the network boundary.
Default gateway connects you to other networks.
```

Еще короче:

```text
IP = who I am
Mask = who is local
Gateway = where I go for remote
```

### Why Binary Comes Next

Правило `255 = network` и `0 = host` хорошо для простых masks:

```text
255.0.0.0
255.255.0.0
255.255.255.0
```

Но subnetting становится интереснее, когда mask выглядит так:

```text
255.255.255.128
255.255.255.192
255.255.255.224
```

Чтобы это понять, нужен binary.

Именно binary объясняет, почему mask может "резать" network не только по целым octets, но и внутри octet.

## Examples

### Example 1

```text
IP address:   10.5.90.110
Subnet mask:  255.0.0.0
```

Result:

```text
Network: 10.0.0.0
Host:    5.90.110
```

Simple reading:

```text
Anything starting with 10 is local.
```

### Example 2

```text
IP address:   172.21.160.5
Subnet mask:  255.255.0.0
```

Result:

```text
Network: 172.21.0.0
Host:    160.5
```

Simple reading:

```text
Anything starting with 172.21 is local.
```

### Example 3

```text
IP address:   10.0.3.50
Subnet mask:  255.255.255.0
```

Result:

```text
Network: 10.0.3.0
Host:    50
```

Simple reading:

```text
Anything starting with 10.0.3 is local.
```

## Quick Self-Check

### Question 1

What does subnet mask define?

Answer:

```text
The boundary between network portion and host portion.
```

### Question 2

Can a host communicate locally without a default gateway?

Answer:

```text
Yes, if it has a valid IP address, subnet mask and Layer 2 connectivity.
```

### Question 3

What does `/24` mean in decimal subnet mask form?

Answer:

```text
255.255.255.0
```

### Question 4

Why are huge flat networks bad?

Answer:

```text
They create too much broadcast traffic and are harder to secure, troubleshoot and manage.
```

### Question 5

What does subnetting do?

Answer:

```text
It divides a larger network into smaller networks by changing the subnet mask.
```

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Subnet mask | Value that defines which part of IPv4 address is network and which part is host. |
| Network portion | Part of IP address that identifies the network. |
| Host portion | Part of IP address that identifies a device inside the network. |
| Octet | One of four decimal numbers in IPv4 address. |
| Classful addressing | Old IPv4 model with Class A/B/C default masks. |
| `/24` | Prefix length equivalent to `255.255.255.0`. |
| Subnetting | Dividing a larger network into smaller networks. |
| Default gateway | Router address used to reach remote networks. |
| Broadcast domain | Area where broadcast traffic is heard. |

## What To Review Later

- IPv4 address structure
- Private vs public IP addresses
- Binary subnet masks
- CIDR notation
- Default gateway
- ARP
- Broadcast domains
- Routing between subnets

