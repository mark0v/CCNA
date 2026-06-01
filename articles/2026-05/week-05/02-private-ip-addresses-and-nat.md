# Private IP Addresses and NAT

Source: закрытая страница курса  
Date added: 2026-06-01  
Related plan item: Week 5 / Private IPv4 ranges and NAT  
Tags: private ip, public ip, rfc 1918, nat, pat, ipv4, subnetting, default gateway
Language: Russian
Translation pair: articles-en/2026-05/week-05/02-private-ip-addresses-and-nat.md

## Summary

Private IP addresses - это IPv4 addresses, которые предназначены для использования внутри private networks и не маршрутизируются через public internet. Благодаря этому одни и те же private ranges могут использоваться в миллионах homes, offices and businesses одновременно.

Главная мысль: private IPs работают внутри сети, а NAT позволяет private devices выходить в internet через public IP address.

## Key Points

- IPv4 address space ограничен примерно 4.3 billion addresses.
- Private IPv4 ranges помогают экономить public addresses.
- Private addresses не должны маршрутизироваться в public internet.
- Private ranges описаны в RFC 1918.
- Есть три private IPv4 ranges: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`.
- Один и тот же private address может существовать в разных isolated networks.
- NAT переводит private addresses во внешний public address.
- PAT/NAT overload позволяет многим internal devices делить один public IP через ports.
- При troubleshooting сначала нужно понять: address private или public.
- Если соединить две сети с одинаковым private addressing, можно получить routing conflict.

## Notes

### Why Private IP Addresses Exist

IPv4 дает около:

```text
4,294,967,296 addresses
```

На первый взгляд это много.

Но в реальном мире addresses быстро заканчиваются:

- phones;
- laptops;
- servers;
- cameras;
- printers;
- TVs;
- IoT devices;
- cars;
- cloud systems;
- business networks.

Если бы каждому устройству нужен был уникальный public IPv4 address, IPv4 exhausted бы намного быстрее.

Решение:

```text
Выделить специальные ranges для private networks.
```

Эти addresses можно использовать внутри локальных сетей, но routers в internet не должны маршрутизировать их как public destinations.

### The Three Private IPv4 Ranges

Private IPv4 ranges:

| Range | Prefix | Common Use |
| --- | --- | --- |
| `10.0.0.0` - `10.255.255.255` | `10.0.0.0/8` | Large organizations, multi-site networks, labs. |
| `172.16.0.0` - `172.31.255.255` | `172.16.0.0/12` | Medium/large networks, enterprise segments. |
| `192.168.0.0` - `192.168.255.255` | `192.168.0.0/16` | Home networks, small offices, simple LANs. |

Их нужно узнавать сразу.

Memory hook:

```text
10 anything = private
172.16 through 172.31 = private
192.168 anything = private
```

Самая частая ошибка - думать, что весь `172.x.x.x` private.

Это неверно.

Private только:

```text
172.16.0.0 - 172.31.255.255
```

Например:

```text
172.20.5.10 = private
172.40.5.10 = not private RFC 1918
```

### RFC 1918

Private address ranges определены в RFC 1918.

Идея RFC 1918:

```text
Используйте эти ranges внутри private networks.
Public internet не будет маршрутизировать их globally.
```

Поэтому:

- мой дом может использовать `192.168.1.10`;
- твой дом тоже может использовать `192.168.1.10`;
- офис может использовать `10.0.1.50`;
- лаборатория может использовать `10.0.1.50`.

Пока эти networks isolated, конфликта нет.

### Private IPs Are Reusable

Private IP addresses reusable потому, что они не уникальны globally.

Они уникальны только внутри конкретной private network.

Пример:

```text
Home A laptop: 192.168.1.20
Home B laptop: 192.168.1.20
```

Оба могут существовать одновременно, потому что они находятся за разными routers and NAT boundaries.

Для public internet эти internal private addresses не видны как destination addresses.

### Private IPs Do Not Work On The Public Internet

Если packet с private destination address попадет в public internet, routers должны его drop/ignore, потому что RFC 1918 ranges не предназначены для public routing.

То есть:

```text
192.168.1.20
```

не является reachable global internet destination.

Если ты troubleshooting и видишь private IP, не пытайся "trace it across the internet".

Следующий logical stop:

- local router;
- firewall;
- NAT device;
- VPN boundary;
- internal routing.

### Why Classes Still Help

Classful networking old school, но historical classes помогают понять размер private ranges.

| Private range | Classful feeling | Default historical size |
| --- | --- | --- |
| `10.0.0.0/8` | Class A | Huge |
| `172.16.0.0/12` | Part of Class B space | Medium/large |
| `192.168.0.0/16` | Class C world | Small/home-friendly |

В modern networks мы используем CIDR and subnetting, а не чистые classes.

Но pattern полезный:

- `192.168.x.x` часто виден дома и в small offices;
- `10.x.x.x` часто виден в enterprise and labs;
- `172.16-31.x.x` часто забывают, но это тоже private range.

### What NAT Does

NAT stands for:

```text
Network Address Translation
```

NAT переводит addresses между internal private network и external public network.

Домашний пример:

```text
Laptop: 192.168.1.20
Phone:  192.168.1.30
TV:     192.168.1.40
Router public IP: 203.0.113.50
```

Private devices не могут напрямую выйти в internet со своими private addresses.

Router делает translation:

```text
192.168.1.20 -> 203.0.113.50
192.168.1.30 -> 203.0.113.50
192.168.1.40 -> 203.0.113.50
```

Снаружи кажется, что traffic приходит от public IP router.

### How One Public IP Can Serve Many Devices

Вопрос:

```text
Как один public IP может представлять много devices одновременно?
```

Ответ: ports.

Точнее, обычно используется PAT:

```text
Port Address Translation
```

Его также часто называют:

```text
NAT overload
```

Router tracks conversations через source ports.

Пример:

```text
192.168.1.20:50001 -> 203.0.113.50:50001
192.168.1.30:50002 -> 203.0.113.50:50002
192.168.1.40:50003 -> 203.0.113.50:50003
```

Когда replies возвращаются, router смотрит на port и понимает, какому internal device отправить traffic.

Это позволяет множеству devices использовать один public IPv4 address.

### NAT Is Useful, But Not Magic

NAT помог IPv4 прожить дольше, но он не является идеальным решением.

Плюсы:

- экономит public IPv4 addresses;
- позволяет reuse private ranges;
- скрывает internal addressing от internet;
- удобен для homes and businesses.

Минусы:

- усложняет troubleshooting;
- ломает end-to-end transparency;
- требует state tracking;
- может усложнить inbound connections;
- иногда мешает protocols/apps, которым нужно прямое соединение.

NAT не заменяет firewall, хотя часто работает на том же edge device.

### Private Addressing At NetworkChuck Coffee

Для NetworkChuck Coffee нет смысла выдавать public IP каждому устройству:

- registers;
- tablets;
- cameras;
- printers;
- smart devices;
- employee laptops;
- guest Wi-Fi clients.

Практичнее использовать private addressing internally.

Small shop example:

```text
192.168.10.0/24
```

Another shop:

```text
192.168.20.0/24
```

Larger multi-location design:

```text
10.0.0.0/8
```

Например:

```text
10.0.1.0/24  = Coffee House 1
10.0.2.0/24  = Coffee House 2
10.0.3.0/24  = Coffee House 3
```

Edge router/firewall делает NAT наружу.

### Duplicate Private IPs Can Become A Problem

Duplicate private IPs безопасны, пока networks isolated.

Но если соединить две сети, где одинаковые ranges, могут начаться проблемы.

Пример:

```text
Site A: 192.168.1.0/24
Site B: 192.168.1.0/24
```

Если между ними сделать VPN, router может не понимать, куда отправлять traffic для `192.168.1.50`, потому что такой network exists on both sides.

Это называется overlapping address space.

Решения:

- заранее планировать addressing;
- использовать разные subnets per site;
- redesign addressing;
- использовать NAT between overlapping networks, если redesign невозможен.

### Troubleshooting Tip

Перед troubleshooting всегда спроси:

```text
This IP address is private or public?
```

Если private:

- не ищи его в public internet;
- проверь local subnet;
- проверь default gateway;
- проверь NAT/firewall;
- проверь internal routing;
- проверь VPN boundaries.

Если public:

- проверь internet routing;
- DNS;
- firewall rules;
- provider/ISP;
- public service availability.

Это экономит много времени.

## Examples

### Example 1 - Home NAT

```text
Laptop private IP: 192.168.1.20
Router public IP:  203.0.113.50
```

Laptop открывает website.

Router translates:

```text
192.168.1.20 -> 203.0.113.50
```

Website видит source:

```text
203.0.113.50
```

а не:

```text
192.168.1.20
```

### Example 2 - Private Range Recognition

```text
10.44.12.8       = private
172.16.5.100     = private
172.31.255.10    = private
172.32.1.1       = not RFC 1918 private
192.168.88.25    = private
8.8.8.8          = public
```

### Example 3 - Coffee Shops

```text
Coffee House 1: 10.0.1.0/24
Coffee House 2: 10.0.2.0/24
Coffee House 3: 10.0.3.0/24
```

Each shop has its own subnet.

All shops can use private IPs internally.

Each shop can use NAT at the edge to reach internet.

## Quick Self-Check

### Question 1

What are the three private IPv4 ranges?

Answer:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

### Question 2

Is `172.32.10.5` private?

Answer:

```text
No. The private 172 range is only 172.16.0.0 through 172.31.255.255.
```

### Question 3

Can private IP addresses be routed across the public internet?

Answer:

```text
No. RFC 1918 private addresses are not meant for public internet routing.
```

### Question 4

What does NAT do?

Answer:

```text
It translates private internal addresses to public external addresses.
```

### Question 5

How can many private devices share one public IP?

Answer:

```text
Through PAT/NAT overload, which tracks conversations using port numbers.
```

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Private IP address | IPv4 address used inside private networks and not routed publicly. |
| Public IP address | Globally routable IP address on the internet. |
| RFC 1918 | Standard that defines private IPv4 address ranges. |
| NAT | Network Address Translation. |
| PAT | Port Address Translation, many private hosts sharing one public IP using ports. |
| NAT overload | Cisco/common term for PAT. |
| Overlapping address space | Two connected networks using the same IP range. |
| Edge router | Router/firewall at the boundary between internal network and outside network. |
| ISP | Internet Service Provider. |

## What To Review Later

- Subnet masks
- CIDR notation
- Default gateway
- NAT/PAT configuration
- Public vs private routing
- VPN overlapping subnets
- IPv6 addressing
- Firewall basics

