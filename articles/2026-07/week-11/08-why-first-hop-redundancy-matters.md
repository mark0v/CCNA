# Why First Hop Redundancy Matters

Source: закрытая страница курса  
Date added: 2026-07-11  
Related plan item: Week 11 / Why first hop redundancy matters  
Tags: HSRP, first hop redundancy, default gateway, resiliency, gateway redundancy, FHRP
Language: Russian
Translation pair: articles-en/2026-07/week-11/08-why-first-hop-redundancy-matters.md

## Summary

- Redundancy - это не "добавить второй router", а design system вокруг failure points.
- Два router-а не помогут, если оба зависят от одного upstream connection.
- Hosts зависят от default gateway и обычно не умеют сами выбирать alternate router.
- First hop redundancy protocols дают clients stable gateway, за которым стоят два или more routers.
- HSRP - Cisco protocol, где один router active, а другой standby.

## Key Points

- Hardware redundancy без internet/WAN redundancy может оставить single point of failure.
- Default gateway failure ломает user connectivity, даже если switches and hosts healthy.
- FHRP делает gateway role highly available.
- HSRP позволяет двум routers appear as one shared gateway IP.
- Redundancy must be tested; untested failover is only hope.

## Notes

Redundancy часто продают как простую идею: купили second router, plugged it in, теперь protected. В реальной сети это не так. Redundancy - это system design вокруг failure points.

Если у NetworkChuck Coffee есть два routers, но один ISP circuit, то upstream connection остается single point of failure. Если оба routers зависят от одного modem, одного provider или одного cable path, hardware redundancy не спасет от internet outage.

Правильный вопрос:

> What happens when this thing breaks?

Этот вопрос нужно задавать для каждого component:

- router;
- switch;
- ISP circuit;
- power;
- cabling;
- default gateway;
- routing path;
- firewall/NAT device.

## The First Hop Problem

Client devices обычно простые. POS terminals, laptops, phones, printers, cameras and tablets не участвуют в OSPF. Они не пересчитывают paths. Они не знают topology. У них есть configured default gateway.

Default gateway - это first hop, куда host отправляет traffic outside local subnet.

Если default gateway disappears:

- host продолжает пытаться отправлять traffic туда же;
- switches могут быть healthy;
- internet circuit может быть alive;
- routing core может иметь alternate paths;
- но endpoint все равно stranded.

Это gap между infrastructure resiliency and user experience.

## What FHRP Solves

First Hop Redundancy Protocol, FHRP, решает именно gateway problem.

Идея:

- два или больше routers/L3 devices share one virtual gateway identity;
- hosts use one virtual IP as default gateway;
- one router actively forwards traffic;
- another router waits in standby;
- если active router fails, standby takes over;
- clients keep using same gateway IP.

В plain English: для users два routers act like one gateway.

Это важно для NetworkChuck Coffee. Если gateway для POS VLAN падает, card readers stop processing payments. Если gateway для guest Wi-Fi падает, customers lose internet. Если gateway для back office падает, inventory sync and cloud services break.

FHRP делает failover mostly invisible для hosts. Они не должны знать, какой physical router сейчас active.

## HSRP

HSRP, Hot Standby Router Protocol, - Cisco first hop redundancy protocol.

Basic roles:

| Role | Meaning |
| --- | --- |
| Active | Router currently forwarding traffic for virtual gateway. |
| Standby | Backup router ready to take over if active fails. |
| Virtual IP | Gateway IP configured on hosts. |
| Virtual MAC | MAC address associated with virtual gateway. |

Hosts configure default gateway as virtual IP. ARP resolves that virtual IP to virtual MAC. Active router owns that virtual MAC at the moment and forwards traffic.

If active router fails, standby router becomes active and starts answering for same virtual gateway identity. Hosts keep using the same configured default gateway.

## Routing Redundancy vs Gateway Redundancy

OSPF and HSRP solve different problems:

| Problem | Protocol type |
| --- | --- |
| Routers need to learn paths through the network. | Dynamic routing, like OSPF. |
| Hosts need a resilient default gateway. | FHRP, like HSRP. |

OSPF can make router-to-router paths resilient. HSRP makes host-to-first-hop access resilient.

They complement each other. OSPF can keep the routed infrastructure adaptive, while HSRP keeps clients attached to a working gateway.

## Redundancy Has Cost

Every backup device needs:

- configuration;
- monitoring;
- updates;
- security;
- testing;
- documentation;
- operational ownership.

Every backup ISP circuit needs cost, contracts, monitoring and failover design. Redundancy is not free. It is business continuity engineering.

The business case should be framed around impact:

- lost payments;
- stopped orders;
- failed cloud sync;
- customer Wi-Fi outage;
- staff downtime;
- emergency troubleshooting time.

If outage cost is higher than redundancy cost, redundancy becomes protection for revenue, not extra equipment.

## Test The Failover

A redundant design that was never tested is not a reliable design.

Test questions:

- What happens when active router loses power?
- What happens when upstream interface fails?
- Does standby become active?
- Do clients keep the same default gateway?
- Does routing behind the gateway still work?
- Does monitoring alert correctly?
- Does failback happen as expected?

Do not wait for the first real outage to discover standby was misconfigured.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| FHRP | First Hop Redundancy Protocol, makes default gateway highly available. |
| HSRP | Cisco FHRP using active and standby routers. |
| Default gateway | First router/L3 address hosts use for off-subnet traffic. |
| Virtual IP | Shared gateway IP used by hosts. |
| Virtual MAC | Shared MAC used by active HSRP router. |
| Active router | HSRP router currently forwarding traffic. |
| Standby router | HSRP router ready to take over. |
| Single point of failure | One component whose failure can take service down. |

## Questions

### 1. Почему two routers не всегда означают redundancy?

Answer: Если оба routers зависят от same upstream path, ISP circuit, power or gateway design, остается single point of failure.

### 2. Что ломается при default gateway failure?

Answer: Hosts теряют first hop для traffic outside local subnet, even if rest of network is still healthy.

### 3. Что делает HSRP?

Answer: HSRP позволяет two routers present one virtual gateway IP to clients, with one active router and one standby router.

### 4. Чем HSRP отличается от OSPF?

Answer: OSPF handles route learning between routers. HSRP handles default gateway availability for hosts.

### 5. Почему failover нужно тестировать?

Answer: Untested redundancy may not work when real failure happens. Testing confirms active/standby behavior, client continuity and alerts.

## What To Review Later

- HSRP active and standby roles.
- Virtual IP and virtual MAC behavior.
- Difference between routing resiliency and first-hop resiliency.
- Common failure points beyond routers.
- How to test failover safely.
