# From Routing Resiliency To Gateway Resiliency

Source: закрытая страница курса  
Date added: 2026-07-11  
Related plan item: Week 11 / From routing resiliency to gateway resiliency  
Tags: dynamic routing, OSPF, first hop redundancy, default gateway, FHRP, resiliency, routing protocols
Language: Russian
Translation pair: articles-en/2026-07/week-11/07-from-routing-resiliency-to-gateway-resiliency.md

## Summary

- Dynamic routing protocols дают routers способность learn, share и recover routes automatically.
- OSPF deployment в NetworkChuck Coffee уже показывает real routing resiliency.
- Но hosts не участвуют в OSPF и обычно знают только один default gateway.
- Если default gateway у host падает, routed core может быть resilient, но endpoint все равно теряет connectivity.
- Следующий шаг - first hop redundancy protocols, которые делают default gateway highly available.

## Key Points

- Dynamic routing полезен не названиями protocols, а тем, что помогает network grow and recover.
- OSPF позволяет routers адаптироваться к changes без manual static route updates.
- Routing resiliency между routers не решает проблему gateway failure для clients.
- Hosts обычно не строят routing table для всей network; они отправляют off-subnet traffic на default gateway.
- FHRP нужен, чтобы у hosts был resilient first hop.

## Notes

После блока dynamic routing легко подумать, что теперь network fully resilient. Routers learned routes, OSPF работает, areas настроены, default route может распространяться dynamically. Но это только часть story.

Routing protocols решают проблему router-to-router reachability. Они помогают routers:

- discover networks;
- share route information;
- recalculate paths after failure;
- use alternate routes;
- reduce manual static route maintenance.

Это уже big step. Static routes работают в маленьких environments, но когда NetworkChuck Coffee grows into multiple cafes, offices, warehouse networks and shared services, manual route management быстро становится operational burden.

OSPF deployment в этой неделе был sample deployment, not final form. Он показал pattern, который можно расширять:

- cafe и fallout shelter routes exchange dynamically;
- WAN link участвует в OSPF;
- routes appear through protocol instead of static config;
- multi-area design and summarization prepare network for growth;
- default route can be injected centrally.

Это делает routers smarter and more resilient.

## What Routers Can Do Now

После dynamic routing routers могут:

- learn where remote networks are;
- choose paths based on protocol metrics;
- react when topology changes;
- remove failed paths;
- install alternate routes;
- recover when links return.

В real network это matters. Links fail, devices reboot, interfaces flap, configs change. Dynamic routing protocols keep the routing domain from depending on one engineer manually editing routes during every failure.

Главная practical question для design:

> Does this work today, and what happens when a link fails, a site is added, or traffic pattern changes?

Dynamic routing earns its keep именно во второй части вопроса.

## The Host Problem

Но hosts - другая история.

Laptops, phones, printers, POS terminals, cameras и workstations usually do not run OSPF. Они не формируют neighbor relationships, не build LSDB, не recalculate best path и не learn alternate routes from routers.

Обычно host знает:

- свой IP address;
- subnet mask;
- default gateway;
- DNS servers.

Default gateway - это first router или Layer 3 interface, куда host отправляет traffic для destinations outside local subnet.

Если этот gateway disappears, host не становится routing expert. Он просто теряет путь наружу.

Это subtle design gap:

- routed infrastructure между routers может быть redundant;
- OSPF может иметь alternate paths;
- WAN design может быть resilient;
- но host все равно зависит от one configured default gateway.

Если gateway fails, user experience breaks.

## Why Routing Resiliency Is Not Enough

Представим NetworkChuck Coffee:

- POS terminals use default gateway `10.10.10.1`;
- Wi-Fi clients use gateway `10.10.20.1`;
- office laptops use gateway `10.10.30.1`.

OSPF может отлично работать behind those gateways. Но если router или SVI serving `10.10.10.1` fails, POS terminals don't care that OSPF elsewhere is healthy. Their first hop is gone.

Это означает:

> Routers can be resilient while hosts are still stranded.

Чтобы сделать full design resilient, нужно закрыть gap между host и first router.

## First Hop Redundancy

Следующая тема - first hop redundancy protocols, FHRP.

Цель FHRP:

- дать hosts stable default gateway;
- allow multiple routers/L3 devices to share gateway responsibility;
- move gateway function to backup device if primary fails;
- keep clients using same configured gateway address;
- reduce outage impact when first-hop device fails.

В plain English: мы даем endpoints backup plan.

Routing protocols сделали routers smart. FHRP делает endpoint experience resilient.

Common FHRP protocols:

| Protocol | Notes |
| --- | --- |
| HSRP | Cisco first hop redundancy protocol. |
| VRRP | Standards-based first hop redundancy protocol. |
| GLBP | Cisco protocol with gateway redundancy and load balancing behavior. |

Мы не abandon OSPF. Мы строим следующий layer resiliency поверх него. Сначала routers learned how to handle network changes. Теперь hosts need reliable first hop.

## Section Recap

Что уже было covered:

- why dynamic routing protocols matter;
- protocol families: OSPF, RIP, EIGRP, BGP;
- path selection with metrics, costs and administrative distance;
- OSPF `network` command and passive interfaces;
- basic OSPF adjacency;
- OSPF troubleshooting;
- multi-area OSPF, ABR, ASBR, summarization and default route injection.

Что осталось unresolved:

- client devices still depend on one default gateway;
- hosts do not participate in routing protocols;
- gateway failure can break users even if routing core remains healthy.

Именно поэтому следующий logical step - first hop redundancy.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Dynamic routing | Routers automatically learn and share route information. |
| OSPF | Link-state IGP used for scalable internal routing. |
| Default gateway | First-hop router address used by hosts for off-subnet traffic. |
| First hop | First Layer 3 device a host uses to reach remote networks. |
| FHRP | First Hop Redundancy Protocol, makes default gateway highly available. |
| HSRP | Cisco FHRP. |
| VRRP | Standards-based FHRP. |
| GLBP | Cisco FHRP with load sharing behavior. |

## Questions

### 1. Что dynamic routing уже решил?

Answer: Он позволил routers automatically learn routes, share information and recover from topology changes without manual static route edits.

### 2. Почему этого недостаточно для hosts?

Answer: Hosts usually do not run routing protocols. Они знают default gateway, и если он fails, host теряет path outside local subnet.

### 3. Что такое default gateway?

Answer: Это first-hop Layer 3 address, куда host отправляет traffic для destinations outside its local subnet.

### 4. Зачем нужен FHRP?

Answer: Чтобы сделать default gateway resilient, позволяя backup router/L3 device принять gateway role при failure primary device.

### 5. Как FHRP связан с OSPF?

Answer: OSPF handles routing between routers. FHRP handles gateway availability for hosts. Они решают разные parts of resiliency design.

## What To Review Later

- Difference between routing resiliency and first-hop resiliency.
- How hosts use default gateways.
- HSRP, VRRP and GLBP roles.
- Why OSPF health does not guarantee client connectivity.
