# WAN....it's Not the Internet!! (sometimes)

Source: закрытая страница курса  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 00 Lesson 08  
Tags: wan, lan, mpls, metro ethernet, vpn, sd-wan, qos, leased line

## Summary

WAN, Wide Area Network, - это connectivity между отдельными locations на расстоянии: offices, branches, stores, data centers и cloud environments. WAN иногда использует internet, но не равен internet автоматически. Исторически businesses часто использовали private carrier services: leased lines, MPLS и Metro Ethernet. Сейчас также распространены internet VPNs и SD-WAN.

Главная мысль статьи: WAN design выбирают по business need: cost, performance, reliability, geography, latency, security и тому, где живут важные services.

## Key Points

- LAN соединяет devices внутри одного building или contained location.
- WAN соединяет отдельные locations across distance.
- WAN нужен, когда branches должны обращаться к centralized services: phone system, payroll, POS databases, apps, email, websites.
- WAN может быть private carrier service или public internet with VPN.
- Leased line - dedicated provider circuit, historically reliable but expensive and limited.
- Frame Relay и ATM - older WAN technologies.
- MPLS - provider-managed private WAN service.
- MPLS is not the public internet.
- CE router means Customer Edge.
- PE router means Provider Edge.
- Metro Ethernet часто используется для fast connectivity между major sites в одном metro area.
- Metro Ethernet flavors: E-Line, E-LAN, E-Tree.
- Site-to-site VPN encrypts traffic over public internet.
- Plain internet paths can have jitter, congestion and unpredictable performance.
- QoS prioritizes important traffic, such as voice.
- SD-WAN helps use internet connections more intelligently for path selection, resilience, cloud access and performance.

## Notes

### WAN Does Not Automatically Mean Internet

Когда люди слышат WAN, они часто думают “internet”. Иногда это правда, но не всегда.

WAN - это network connectivity между separate locations across distance.

Для NetworkChuck Coffee это может быть:

- corporate office to data center;
- coffee shops to corporate;
- coffee shops to data center;
- branches to cloud services.

LAN обычно находится внутри одного contained location:

```text
One building / one local site = LAN
Multiple sites across distance = WAN
```

### Why Businesses Need WAN

Businesses используют WAN не “ради сети”, а потому что services часто centralized.

Примеры centralized services:

- phone system;
- payroll system;
- POS databases;
- email;
- websites;
- internal applications;
- inventory systems;
- payment systems.

Если branch local network работает идеально, но WAN path до business apps умер, branch всё равно выглядит “сломленным” для users.

Практическая мысль:

```text
WAN connects business functions that live in different places.
```

### Legacy WAN: Leased Lines

Leased line - это dedicated circuit, который company арендует у provider.

Плюсы:

- dedicated path;
- predictable service;
- traffic belongs to customer;
- historically trusted for business connectivity.

Минусы:

- expensive;
- limited speeds by modern standards;
- hard to scale many sites;
- lots of point-to-point complexity.

Пример old speed: T1, который сегодня выглядит very small.

### Older WAN Technologies

Статья кратко упоминает older WAN options:

- Frame Relay;
- ATM.

Их не нужно глубоко разбирать в этом уроке, но важно знать, что они использовались businesses до newer WAN approaches.

Старые technologies могут встречаться в real world, потому что infrastructure часто живет долго, если она still works и expensive to replace.

### MPLS

MPLS stands for Multiprotocol Label Switching.

Практическая идея:

```text
Each site connects to provider MPLS cloud.
Provider privately carries traffic between sites.
```

Вместо того чтобы строить point-to-point lines между every office, company подключает sites к provider network, а provider handles traffic delivery.

Пример:

```text
Phoenix branch -> MPLS provider cloud -> Data center
Phoenix branch -> MPLS provider cloud -> Seattle branch
```

### MPLS Is Not Public Internet

MPLS - это provider-managed private WAN service, not the public internet.

Provider может обслуживать many customers в одной infrastructure, но логически разделяет их traffic using labels and virtual circuits.

Важно:

```text
Private/logically separated does not automatically mean encrypted like VPN.
```

MPLS часто называют Layer 2.5 technology, потому что он находится между traditional Layer 2 behavior и Layer 3 routing concepts.

### CE and PE Routers

В MPLS часто встречаются термины:

| Term | Meaning |
| --- | --- |
| CE | Customer Edge router |
| PE | Provider Edge router |

CE router находится на стороне customer. PE router находится на стороне provider и подключает customer к provider network.

### Metro Ethernet

Metro Ethernet - это provider service для fast Ethernet-style connectivity, часто между sites в одном metropolitan area.

Частые use cases:

- corporate office to data center;
- data center to data center;
- major site to major site;
- high throughput low latency links.

Metro Ethernet часто Layer 2, поэтому может ощущаться как Ethernet extension between sites.

### Metro Ethernet Types

| Type | Meaning |
| --- | --- |
| E-Line | Point-to-point Ethernet service |
| E-LAN | Multipoint Ethernet service, похож на provider switch fabric |
| E-Tree | Hub-and-spoke Ethernet service |

Для NetworkChuck Coffee Metro Ethernet может быть слишком expensive для каждой маленькой branch, но отлично подходит между corporate и data center.

### MPLS vs Metro Ethernet

Выбор зависит от business need.

| Need | Often good fit |
| --- | --- |
| Connect many branches privately through carrier | MPLS |
| High-speed link between major nearby sites | Metro Ethernet |
| Corporate to data center in same metro area | Metro Ethernet |
| Branch network with provider-managed private WAN | MPLS |

Начинать нужно не с technology name, а с question:

```text
What does the business need this WAN to do?
```

### Internet WAN and VPNs

Иногда WAN строится поверх public internet.

Branch может купить regular business internet connection и построить site-to-site VPN до corporate/data center.

Site-to-site VPN:

- encrypts traffic;
- crosses public internet;
- cheaper than many private WAN options;
- common for branches and small sites.

Проблема: public internet path может быть unpredictable.

Возможные issues:

- jitter;
- congestion;
- packet loss;
- variable latency;
- poor voice quality.

### QoS

QoS stands for Quality of Service.

QoS отвечает на вопрос:

```text
Which traffic matters more?
```

Примеры priorities:

| Traffic | Priority idea |
| --- | --- |
| Voice | High priority |
| Payment/POS | High priority |
| Payroll/business apps | Important |
| Random downloads | Lower priority |
| Streaming entertainment | Usually lower in business network |

MPLS historically handled QoS well, which is one reason businesses liked it.

### SD-WAN

SD-WAN changes how businesses use WAN connectivity.

SD-WAN can help with:

- smarter path selection;
- better use of multiple internet links;
- resiliency;
- performance;
- cloud access;
- centralized policy;
- application-aware routing.

This matters because many apps no longer live only in company data center. They may live in:

- AWS;
- Azure;
- SaaS platforms;
- public cloud services.

SD-WAN helps make regular internet links more useful and manageable for business WAN needs.

### Main Takeaway

WAN means connectivity between separate locations.

WAN can be:

- leased line;
- Frame Relay/ATM legacy service;
- MPLS;
- Metro Ethernet;
- public internet with site-to-site VPN;
- SD-WAN over multiple transports.

The right WAN design depends on:

- cost;
- performance;
- geography;
- latency;
- reliability;
- security;
- cloud usage;
- business requirements.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| LAN | Local Area Network; network inside one local site/building. |
| WAN | Wide Area Network; connectivity between separate locations across distance. |
| Leased line | Dedicated circuit rented from a provider. |
| T1 | Older leased-line circuit speed/type. |
| Frame Relay | Older WAN technology used before newer WAN services. |
| ATM | Older WAN technology. |
| MPLS | Multiprotocol Label Switching; provider-managed private WAN service. |
| MPLS cloud | Provider MPLS network that carries customer traffic between sites. |
| CE router | Customer Edge router. |
| PE router | Provider Edge router. |
| Metro Ethernet | Ethernet-style provider service, often high-speed between metro-area sites. |
| E-Line | Point-to-point Metro Ethernet service. |
| E-LAN | Multipoint Metro Ethernet service. |
| E-Tree | Hub-and-spoke Metro Ethernet service. |
| Site-to-site VPN | Encrypted tunnel between sites over public internet. |
| QoS | Quality of Service; traffic prioritization. |
| SD-WAN | Software-defined WAN; smarter WAN path selection, policy and resilience. |
| Jitter | Variation in packet delay, harmful for voice/video. |

## Questions

### 1. Что такое WAN?

WAN - это connectivity между separate locations across distance: offices, branches, stores, data centers и cloud environments.

### 2. WAN всегда означает internet?

Нет. WAN может использовать public internet, но также может быть private carrier service like leased lines, MPLS или Metro Ethernet.

### 3. Чем LAN отличается от WAN?

LAN работает внутри одного local site/building, а WAN соединяет multiple sites across distance.

### 4. Почему businesses нуждаются в WAN?

Потому что important services часто centralized, а branches должны reliable access phone systems, POS databases, apps, email, payroll and other services.

### 5. Что такое leased line?

Leased line - dedicated circuit rented from provider. Он predictable, но expensive и difficult to scale.

### 6. Что такое MPLS?

MPLS - provider-managed private WAN service, где customer sites connect into provider MPLS cloud and provider routes traffic between them.

### 7. MPLS - это public internet?

Нет. MPLS - это private provider-managed WAN, хотя provider может carrying traffic for many customers logically separated.

### 8. Что означают CE и PE?

CE - Customer Edge router. PE - Provider Edge router.

### 9. Где Metro Ethernet особенно полезен?

Для high-speed connectivity between major sites, such as corporate office and data center, especially within same metro area.

### 10. Назови три Metro Ethernet service types.

E-Line, E-LAN и E-Tree.

### 11. Что делает site-to-site VPN?

Site-to-site VPN encrypts traffic between locations as it crosses public internet.

### 12. Почему plain internet WAN может быть проблемой для voice traffic?

Потому что internet paths can be unpredictable, jittery, congested and variable in latency.

### 13. Что такое QoS?

QoS, Quality of Service, prioritizes important traffic, such as voice or business-critical applications.

### 14. Зачем нужен SD-WAN?

SD-WAN helps businesses use internet and other WAN links more intelligently with better path selection, performance, resiliency and cloud access.

## What To Review Later

- WAN vs LAN.
- WAN does not automatically mean internet.
- Leased lines, Frame Relay and ATM as legacy WAN.
- MPLS as provider-managed private WAN.
- CE router vs PE router.
- Metro Ethernet: E-Line, E-LAN, E-Tree.
- Public internet VPN tradeoffs.
- QoS for voice and business-critical traffic.
- SD-WAN and modern cloud-oriented WAN.
