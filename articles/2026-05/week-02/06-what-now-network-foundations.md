# What Now?

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Network foundations recap  
Tags: network design, rfp, requirements, switch, router, firewall, access point, planning

## Summary

После знакомства с router, switch, access point и firewall появляется важная база: теперь требования из RFP перестают быть туманными фразами и превращаются в практические design decisions. Если бизнес просит reliable WiFi, secure connectivity или room for growth, network engineer должен перевести это в topology, device roles, ports, coverage и security boundaries.

Главная мысль: RFP говорит, куда нужно прийти. Твои network skills помогают построить дорогу.

## Key Points

- Это уже "настоящая" networking база, а не просто набор определений.
- RFP обычно описывает outcomes, а не конкретные технологии.
- Network engineer переводит business requirements в technical design.
- Требование "understand network needs" превращается в вопросы о users, devices, ports, APs and coverage.
- "Configure network devices" означает работу с routers, switches, APs and firewalls.
- VLANs, trunks, EtherChannel и другие темы могут не быть явно названы в RFP.
- Даже если advanced terms не указаны, они могут понадобиться в implementation.
- Сначала важно понять structure, purpose and language.
- Потом можно глубже изучать mechanisms.
- Confidence приходит не от знания всего, а от понимания, как думать о задаче.

## Notes

### Filling in the Cracks

RFP может сказать:

```text
Understand the organization's network needs.
```

Но за этой короткой фразой прячутся практические вопросы:

- сколько пользователей;
- сколько devices;
- сколько switch ports;
- сколько wireless access points;
- какие зоны покрытия;
- нужен ли guest WiFi;
- где стоят cameras;
- какие systems критичны;
- какая internet handoff от ISP.

Так requirements превращаются в design.

### Vocabulary Starts to Click

Когда документ говорит `network devices`, теперь понятно, что речь может идти про:

- routers;
- switches;
- wireless access points;
- firewalls;
- servers;
- endpoints.

Это важно, потому что real-world документы часто написаны общими словами. Твоя задача - переводить эти слова в конкретные technical decisions.

### What Is Still Ahead

Мы еще не разобрали глубоко:

- VLANs;
- trunk ports;
- EtherChannel;
- routing protocols;
- ACLs;
- DHCP;
- NAT;
- DNS;
- wireless design.

Это нормально. Сейчас строится foundation. Сложные темы лучше ложатся, когда уже понятно, зачем они нужны.

## Commands / Terms

```text
RFP - Request for Proposal
Requirement - требование бизнеса или проекта
Design decision - техническое решение на основе требования
Topology - схема связей между устройствами
```

## Questions

### Что делает network engineer с требованиями RFP?

Переводит бизнес-результаты в конкретный technical design.

### Почему в RFP не всегда пишут VLAN, trunks или EtherChannel?

Потому что заказчик часто описывает outcome, а не implementation details.

### Почему эта база важна перед кабелями и настройками?

Потому что нужно понимать, какие устройства соединять, зачем они нужны и какую роль играют.

## What To Review Later

- Reading technical requirements.
- Mapping business needs to network design.
- VLANs and segmentation.
- Redundancy and uplinks.
- Wireless coverage planning.
