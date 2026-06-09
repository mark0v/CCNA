# Configuring Static NAT

Source: закрытая страница курса  
Date added: 2026-06-09  
Related plan item: Week 6 / Static NAT configuration  
Tags: static NAT, ip nat inside, ip nat outside, port forwarding, translation table, Cisco IOS
Language: Russian
Translation pair: articles-en/2026-06/week-06/11-configuring-static-nat.md

## Summary

Static NAT создает постоянное двустороннее one-to-one mapping между inside local и inside global addresses. Он подходит для internal server или другого host, который должен постоянно иметь predictable public identity.

Одной translation command недостаточно. Router также должен знать, какой interface является NAT inside, а какой NAT outside. Проверка выполняется через `show ip nat translations`, routing и end-to-end tests.

## Key Points

- Static NAT постоянно связывает один internal address с одним external address.
- Mapping работает для outbound и inbound traffic.
- Основная команда: `ip nat inside source static`.
- Inside interface получает `ip nat inside`.
- Internet-facing interface получает `ip nat outside`.
- Static mapping виден в NAT table даже без active traffic.
- Static NAT не предоставляет общий internet access всем hosts.
- Routing и return path должны работать независимо от NAT.
- Port-level static NAT публикует отдельный service вместо всего address.
- Published services требуют firewall policy и security hardening.

## Notes

### Static NAT Use Case

NetworkChuck Coffee размещает internal server:

```text
Inside local:  192.168.1.50
Inside global: 216.0.5.20
```

Customers обращаются к public address `216.0.5.20`, а edge router переводит traffic к `192.168.1.50`.

Обратный outbound traffic server также представляется address `216.0.5.20`.

### One-To-One And Bidirectional

Static NAT означает:

```text
One inside local address <-> one inside global address
```

Mapping:

```text
192.168.1.50 <-> 216.0.5.20
```

Оно:

- постоянное;
- predictable;
- существует до появления sessions;
- допускает inbound connections при наличии routing и security policy.

### Configure The Static Mapping

В global configuration mode:

```cisco
ip nat inside source static 192.168.1.50 216.0.5.20
```

Чтение команды:

```text
Представлять inside source 192.168.1.50
как global address 216.0.5.20.
```

Используй contextual help:

```cisco
ip nat ?
ip nat inside ?
ip nat inside source ?
```

`?` является нормальным рабочим инструментом Cisco IOS.

### Mark The Inside Interface

Interface, ведущий к internal server:

```cisco
interface GigabitEthernet0/0
 description Cafe LAN
 ip nat inside
```

### Mark The Outside Interface

Interface, ведущий к ISP:

```cisco
interface GigabitEthernet0/2
 description ISP uplink
 ip nat outside
```

Без interface roles router имеет mapping, но не знает, на каком crossing применять translation.

### Complete Example

```cisco
enable
configure terminal

interface GigabitEthernet0/0
 description Cafe LAN
 ip nat inside

interface GigabitEthernet0/2
 description ISP uplink
 ip nat outside

ip nat inside source static 192.168.1.50 216.0.5.20

end
```

Фактические interface names и addresses должны соответствовать topology.

### Public Address Routing

ISP side должен знать, что public address `216.0.5.20` доступен через cafe edge router.

Это может обеспечиваться:

- connected public subnet;
- provider static route;
- routed public block;
- proxy ARP в поддерживаемом design.

Если outside network не доставляет traffic к inside global address, NAT mapping сам по себе не поможет.

### Verify The Mapping

```cisco
show ip nat translations
```

Static entry может выглядеть:

```text
Pro  Inside global  Inside local    Outside local  Outside global
---  216.0.5.20     192.168.1.50    ---            ---
```

После generating traffic появляются protocol-specific entries.

Дополнительно:

```cisco
show ip nat statistics
show running-config | include ip nat
show ip interface brief
show ip route
```

### Troubleshooting Order

Если static NAT не работает:

1. Проверить static mapping.
2. Проверить `ip nat inside`.
3. Проверить `ip nat outside`.
4. Проверить internal host IP, mask и gateway.
5. Проверить route к outside destination.
6. Проверить reachability ISP next hop.
7. Проверить routing public inside-global address к edge router.
8. Проверить ACL/firewall policy.
9. Проверить service на internal host.
10. Проверить NAT translations и counters.

### Static NAT Is Host-Specific

Если mapping существует только для:

```text
192.168.1.50
```

то другой host, например `192.168.1.60`, не получает translation автоматически.

Static NAT не заменяет PAT для общего user internet access.

Обычно design использует:

- static NAT или static PAT для published services;
- PAT overload для outbound client traffic.

### Port-Level Static Translation

Можно публиковать только определенный TCP/UDP service.

Пример HTTPS:

```cisco
ip nat inside source static tcp 192.168.1.50 443 216.0.5.20 443
```

Это означает:

```text
TCP 216.0.5.20:443 -> 192.168.1.50:443
```

Можно перевести и port:

```cisco
ip nat inside source static tcp 192.168.1.50 443 216.0.5.20 8443
```

Тогда:

```text
TCP 216.0.5.20:8443 -> 192.168.1.50:443
```

### Publishing Multiple Services

Один public IP может направлять разные ports разным internal hosts:

```text
216.0.5.20:443 -> 192.168.1.50:443
216.0.5.20:25  -> 192.168.1.60:25
```

Каждая комбинация protocol/address/port должна быть уникальной.

### Security Considerations

Static NAT не является разрешением firewall.

Перед публикацией service:

- разрешить только required ports;
- использовать stateful firewall;
- patch internal server;
- отключить unnecessary services;
- включить logging и monitoring;
- защитить authentication;
- использовать TLS;
- рассмотреть DMZ вместо user LAN;
- проверить vulnerability exposure.

Возможность опубликовать service не означает, что это безопасно делать без controls.

### Clearing Translations

В lab может потребоваться:

```cisco
clear ip nat translation *
```

В production команда прерывает active translated sessions. Используй ее только после оценки impact.

## Configuration Checklist

- Определить inside local address.
- Выделить routable inside global address.
- Проверить provider routing.
- Настроить static mapping.
- Назначить NAT inside interface.
- Назначить NAT outside interface.
- Проверить routing.
- Проверить firewall/ACL.
- Проверить translation table.
- Тестировать inbound и outbound directions.
- Сохранить configuration.
- Обновить documentation.

## Quick Self-Check

### Question 1

Что создает static NAT?

Answer:

```text
Постоянное one-to-one mapping между inside local и inside global addresses.
```

### Question 2

Какие interface commands обязательны?

Answer:

```text
ip nat inside и ip nat outside.
```

### Question 3

Почему mapping может существовать, но traffic не проходить?

Answer:

```text
Могут отсутствовать interface roles, routing, firewall permission или работающий service.
```

### Question 4

Дает ли static NAT internet всем internal hosts?

Answer:

```text
Нет. Он переводит только явно настроенный host или service.
```

### Question 5

Что делает static PAT?

Answer:

```text
Переводит конкретный protocol/port public address к конкретному internal service.
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Static NAT | Permanent one-to-one address mapping. |
| Static PAT | Permanent protocol/port mapping. |
| `ip nat inside source static` | Создает static translation. |
| `ip nat inside` | Назначает internal interface role. |
| `ip nat outside` | Назначает external interface role. |
| Inside local | Internal host address before translation. |
| Inside global | Address representing the host outside. |
| `show ip nat translations` | Показывает translation table. |
| `show ip nat statistics` | Показывает NAT roles и counters. |
| Port forwarding | Публикация internal service через public port. |

## What To Review Later

- Dynamic NAT configuration
- PAT overload configuration
- NAT order of operations
- Public block routing
- Proxy ARP
- DMZ design
- NAT troubleshooting
