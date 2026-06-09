# Why NAT Matters

Source: закрытая страница курса  
Date added: 2026-06-09  
Related plan item: Week 6 / NAT introduction  
Tags: NAT, private IPv4, public IPv4, internet access, edge router, PAT, network deployment
Language: Russian
Translation pair: articles-en/2026-06/week-06/07-why-nat-matters.md

## Summary

NAT, или Network Address Translation, преобразует IP address при прохождении traffic через network boundary. Чаще всего edge router заменяет private source address внутреннего host на public address, пригодный для связи через internet.

NAT изучается сразу после routing, потому что это одна из первых практических задач при развертывании сети. IP addressing и default route создают путь, но private hosts обычно не смогут полноценно использовать public internet без translation.

## Key Points

- NAT означает Network Address Translation.
- Private IPv4 ranges предназначены для внутренних networks.
- Private addresses не маршрутизируются в public internet.
- NAT связывает internal addressing с public connectivity.
- Edge router или firewall часто выполняет translation.
- Internet access обычно требует routing и NAT одновременно.
- Многие private hosts могут разделять один public IP через PAT.
- NAT нужно учитывать в design с начала deployment.
- NAT не заменяет routing, firewall policy или DNS.
- Проверка internet access должна входить в ранний rollout checklist.

## Notes

### Why NAT Appears Early

В учебных программах NAT иногда откладывают до более поздних тем, потому что configuration может использовать ACL и дополнительную terminology.

В реальном deployment потребность появляется почти сразу:

- users открывают websites;
- POS terminals обращаются к cloud services;
- systems скачивают updates;
- guest Wi-Fi требует internet;
- monitoring отправляет telemetry;
- branch applications используют SaaS.

Поэтому NAT находится рядом с базовым IP addressing и default routing.

### What NAT Actually Does

Базовая идея:

```text
NAT translates one IP address representation into another.
```

В типичном outbound scenario:

```text
Inside host: 192.168.1.10
Public identity: 216.0.5.2
```

Router изменяет source information перед отправкой packet в internet и запоминает translation, чтобы вернуть reply правильному host.

### Private IPv4 Ranges

RFC 1918 определяет private IPv4 ranges:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

Они могут повторно использоваться в разных организациях, потому что public internet не маршрутизирует их как globally unique destinations.

Преимущества:

- экономия public IPv4 space;
- независимое internal addressing;
- удобное разделение LANs;
- возможность менять provider без полной renumbering внутренних hosts.

### Why Private Hosts Cannot Simply Go Out

Предположим, PC отправляет packet:

```text
Source:      192.168.1.10
Destination: 8.8.8.8
```

Default route может доставить packet к ISP.

Но private source `192.168.1.10` не является globally routable. Public networks не имеют уникального return path к этому host.

NAT заменяет private source на public address edge device.

### Routing And NAT Are Different

Routing решает:

```text
Where should this packet go next?
```

NAT решает:

```text
Which address should represent this endpoint across the boundary?
```

Для internet access нужны оба:

1. Client имеет correct IP, mask и default gateway.
2. Edge router имеет route к ISP.
3. NAT переводит private address.
4. Firewall/ACL разрешает traffic.
5. DNS разрешает names при необходимости.

### NetworkChuck Coffee Example

Внутренние devices:

- POS terminals;
- employee laptops;
- guest clients;
- security cameras;
- back-office server.

Они используют private addresses.

Для cloud access traffic проходит:

```text
Internal device
-> access switch
-> cafe router/default gateway
-> NAT
-> ISP
-> Internet service
```

Reply возвращается public address, затем translation table направляет его внутреннему device.

### PAT: The Common Form

PAT означает Port Address Translation и также называется NAT overload.

Много hosts используют один public IPv4 address, различаясь translated transport ports.

Пример:

```text
192.168.1.10:51000 -> 216.0.5.2:30001
192.168.1.20:51000 -> 216.0.5.2:30002
```

Один public address обслуживает множество simultaneous sessions.

### NAT Is Common, Not Universal

NAT широко используется в IPv4 networks, но утверждение "internet всегда требует NAT" не абсолютно.

Host с globally routable public IPv4 address может работать без NAT, если routing и security policy позволяют.

IPv6 design также стремится восстановить end-to-end addressing и обычно не использует NAT как обязательный механизм.

В нашем small-business IPv4 scenario private addressing делает NAT/PAT практической необходимостью.

### NAT Does Not Equal Security

NAT скрывает внутреннюю addressing structure и не создает unsolicited translation автоматически в обычном PAT scenario.

Но NAT не заменяет firewall.

Security требует:

- stateful policy;
- ACLs;
- segmentation;
- secure services;
- patching;
- logging;
- monitoring.

Не следует считать translation полноценным security control.

### Plan NAT During Deployment

Ранний checklist:

- inside subnets;
- outside/public addressing;
- ISP next hop;
- default route;
- NAT type;
- translated address или pool;
- traffic selection;
- exclusions;
- firewall policy;
- verification plan;
- documentation.

Если NAT оставить "на потом", users могут иметь working LAN и routing между sites, но без business-critical internet services.

### Common NAT Types

| Type | Purpose |
| --- | --- |
| Static NAT | Постоянное one-to-one соответствие addresses |
| Dynamic NAT | Временный перевод через pool public addresses |
| PAT / overload | Many-to-one translation с использованием ports |

Следующие уроки подробно разберут configuration и terminology.

### What NAT Does Not Fix

NAT не исправит:

- down interface;
- неверный default gateway;
- отсутствующий default route;
- DNS failure;
- blocked firewall rule;
- broken ISP circuit;
- incorrect subnet mask;
- application outage.

Troubleshooting должен начинаться с layer-by-layer verification.

## Simplified Packet Flow

Outbound:

```text
192.168.1.10:51000
-> cafe router
-> translated to 216.0.5.2:30001
-> internet server
```

Inbound reply:

```text
internet server
-> 216.0.5.2:30001
-> cafe router translation lookup
-> 192.168.1.10:51000
```

## Deployment Checklist

- Проверить client addressing.
- Проверить default gateway.
- Проверить ISP-facing interface.
- Проверить default route.
- Определить inside и outside boundaries.
- Выбрать NAT/PAT design.
- Проверить traffic selection.
- Проверить firewall policy.
- Тестировать IP reachability отдельно от DNS.
- Проверить translations и counters.
- Документировать configuration.

## Quick Self-Check

### Question 1

Что делает NAT?

Answer:

```text
Преобразует IP address information при прохождении traffic через network boundary.
```

### Question 2

Почему private IPv4 host обычно нуждается в NAT для internet?

Answer:

```text
Private address не маршрутизируется как globally unique address в public internet.
```

### Question 3

Чем routing отличается от NAT?

Answer:

```text
Routing выбирает путь, а NAT изменяет address representation.
```

### Question 4

Что такое PAT?

Answer:

```text
Many-to-one translation, где sessions различаются transport ports.
```

### Question 5

Является ли NAT заменой firewall?

Answer:

```text
Нет. Для security нужна явная firewall/ACL policy и другие controls.
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| NAT | Network Address Translation. |
| PAT | Port Address Translation, или NAT overload. |
| Private IPv4 | RFC 1918 address для internal use. |
| Public IPv4 | Globally routable IPv4 address. |
| Inside network | Internal side of the translation boundary. |
| Outside network | External/public side of the boundary. |
| Translation table | Active mappings между internal и external flows. |
| Static NAT | Permanent one-to-one mapping. |
| Dynamic NAT | Temporary mapping from an address pool. |
| Edge router | Router at the internal/external network boundary. |

## What To Review Later

- Inside local and inside global
- Outside local and outside global
- Static NAT
- Dynamic NAT
- PAT configuration
- NAT ACLs
- `show ip nat translations`
- NAT troubleshooting
