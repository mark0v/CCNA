# Choosing Between HSRP, VRRP, And GLBP

Source: закрытая страница курса  
Date added: 2026-07-11  
Related plan item: Week 11 / Choosing between HSRP, VRRP, and GLBP  
Tags: HSRP, VRRP, GLBP, FHRP, default gateway, preemption, virtual MAC, gateway redundancy
Language: Russian
Translation pair: articles-en/2026-07/week-11/10-choosing-between-hsrp-vrrp-and-glbp.md

## Summary

- HSRP, VRRP и GLBP решают одну family problem: resilient default gateway for hosts.
- HSRP и VRRP очень похожи: один router forwards, другой ждет failover.
- VRRP - standards-based, HSRP - Cisco proprietary.
- GLBP добавляет gateway load balancing, а не только active/standby redundancy.
- В real world часто выбирают VRRP, в Cisco/CCNA context нужно хорошо знать HSRP.

## Key Points

- HSRP uses active/standby terminology.
- VRRP uses master/backup terminology.
- HSRP preemption is not enabled by default; VRRP preemption is enabled by default.
- GLBP can hand different virtual MAC addresses to different clients for load sharing.
- Each VLAN with its own default gateway usually needs its own FHRP configuration.

## Notes

FHRP protocols не нужно воспринимать как три completely unrelated technologies. Они решают одну базовую problem: hosts need a default gateway, and that gateway should not depend on one physical router.

Вместо того чтобы pointing clients to one router IP, FHRP позволяет routers share a virtual gateway identity. Hosts keep one default gateway IP. Behind the scenes routers coordinate who owns that gateway right now.

The practical question is not "which acronym sounds best?" The question is:

- vendor environment;
- desired failover behavior;
- need for standards-based support;
- need for load balancing;
- operational simplicity;
- exam requirements.

## HSRP And VRRP

HSRP and VRRP are similar in core behavior:

| Feature | HSRP | VRRP |
| --- | --- | --- |
| Ownership | Cisco proprietary | Standards-based |
| Main roles | Active / Standby | Master / Backup |
| Basic model | One forwards, one waits | One forwards, one waits |
| Preemption default | Off by default | On by default |
| Typical context | Cisco-focused environments, CCNA | Mixed-vendor and broad industry use |

Both provide a virtual IP for hosts. Both use a virtual MAC. Both allow failover if primary gateway device fails.

Terminology differs, but the mental model is the same:

- one router is currently responsible for forwarding;
- another router is ready to take over;
- hosts keep using the virtual gateway.

## Preemption

Preemption means the preferred router can take back active/master role when it comes back online.

This matters operationally.

If a router failed because of unstable hardware or buggy software, automatic failback can be dangerous. It might return, take traffic back, fail again, and create repeated micro-outages.

Real-world rule: automatic failback should match operational policy. Sometimes it is better to fail over and stay on the stable router until engineers decide what to do.

In HSRP, preemption must be enabled explicitly if you want it:

```text
standby 1 preempt
```

In VRRP, preemption is enabled by default in many implementations.

## VRRP Address Efficiency

One useful VRRP detail: virtual gateway IP can be the real IP of one router. This can avoid using an extra address only for the virtual gateway.

In networks with tight address space, this matters. It is not usually the main design driver, but it can be useful in old networks, packed server segments or constrained subnets.

## Exam And Troubleshooting Details

For exam and troubleshooting, recognize:

- virtual MAC address patterns;
- multicast addresses;
- protocol version differences;
- preemption behavior;
- roles and states.

You do not need to become a hex robot, but if you see an FHRP virtual MAC in ARP or switch MAC table, recognition helps fast.

HSRP version differences also matter. HSRP version 2 supports IPv6 and more groups than version 1. In larger environments, group scale and IPv6 support can matter.

## GLBP

GLBP, Gateway Load Balancing Protocol, is Cisco proprietary and adds load balancing.

HSRP and VRRP are mainly active/standby. One router forwards for a virtual gateway, another waits.

GLBP is different:

- one device acts as Active Virtual Gateway;
- multiple devices can act as Active Virtual Forwarders;
- clients can receive different virtual MAC addresses for same gateway IP;
- traffic can be spread across routers.

Roles:

| Role | Meaning |
| --- | --- |
| AVG | Active Virtual Gateway, answers ARP and manages assignment. |
| AVF | Active Virtual Forwarder, forwards traffic for assigned virtual MAC. |

The AVG answers ARP requests. Instead of always giving every client the same virtual MAC, it can hand out different virtual MACs. One client may use Router A, another may use Router B.

This is not perfect load balancing because clients generate different traffic volumes. But it can distribute gateway usage more evenly than simple active/standby.

## Manual Load Sharing With HSRP/VRRP

HSRP and VRRP can still be used for manual load sharing across VLANs.

Example:

- Router A active for VLAN 10;
- Router B active for VLAN 20;
- Router A standby for VLAN 20;
- Router B standby for VLAN 10.

This spreads gateway responsibility by VLAN. It is not the same as GLBP client-by-client balancing, but it is common and predictable.

## NetworkChuck Coffee Design View

NetworkChuck Coffee may have:

- POS VLAN;
- staff VLAN;
- camera VLAN;
- guest Wi-Fi VLAN;
- back office VLAN.

Each VLAN has its own default gateway. That means each VLAN needs its own FHRP plan.

You do not configure one global FHRP and finish. You decide gateway redundancy per subnet/VLAN.

In a small or medium network, prefer the simplest resilient design that operations can troubleshoot. Complexity has a cost.

Practical guideline:

| Scenario | Likely choice |
| --- | --- |
| Cisco-only and CCNA/lab focus | HSRP |
| Mixed-vendor or standards-based design | VRRP |
| Need gateway load balancing and Cisco support | GLBP |
| Simple active/standby with broad vendor support | VRRP |

## Main Takeaway

Do not get lost in acronym soup.

Remember:

- HSRP and VRRP provide gateway failover.
- VRRP is standards-based and common in broader real world.
- HSRP is Cisco-centric and important for CCNA.
- GLBP provides redundancy plus gateway load balancing.
- Preemption behavior matters.
- Virtual MAC and multicast details matter for verification and troubleshooting.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| HSRP | Cisco Hot Standby Router Protocol. |
| VRRP | Standards-based Virtual Router Redundancy Protocol. |
| GLBP | Cisco Gateway Load Balancing Protocol. |
| Preemption | Preferred router takes back active/master role after recovery. |
| Active | HSRP router currently forwarding for virtual gateway. |
| Standby | HSRP backup router. |
| Master | VRRP router currently forwarding. |
| Backup | VRRP backup router. |
| AVG | GLBP Active Virtual Gateway. |
| AVF | GLBP Active Virtual Forwarder. |

## Questions

### 1. Чем HSRP и VRRP похожи?

Answer: Оба provide virtual default gateway and active/standby-style failover for hosts.

### 2. Главное отличие HSRP от VRRP?

Answer: HSRP is Cisco proprietary, while VRRP is standards-based.

### 3. Что такое preemption?

Answer: Это behavior, когда preferred router забирает active/master role обратно после recovery.

### 4. Чем GLBP отличается от HSRP/VRRP?

Answer: GLBP can load balance by giving different clients different virtual MAC addresses for the same gateway IP.

### 5. Почему FHRP нужно планировать per VLAN?

Answer: Each VLAN/subnet has its own default gateway, so each needs its own gateway redundancy design.

## What To Review Later

- HSRP versions and virtual MAC formats.
- VRRP multicast and virtual MAC behavior.
- GLBP AVG and AVF roles.
- VLAN-by-VLAN gateway redundancy design.
- Preemption and failback policy.
