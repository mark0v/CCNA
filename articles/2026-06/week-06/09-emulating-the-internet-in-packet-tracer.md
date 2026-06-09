# Emulating the Internet in Packet Tracer

Source: закрытая страница курса  
Date added: 2026-06-09  
Related plan item: Week 6 / Packet Tracer internet simulation  
Tags: Packet Tracer, ISP router, loopback, default route, NAT, return path, 1.1.1.1, 8.8.8.8
Language: Russian
Translation pair: articles-en/2026-06/week-06/09-emulating-the-internet-in-packet-tracer.md

## Summary

Для изучения internet edge в Packet Tracer не нужно подключать simulation к реальному network adapter. Надежнее использовать отдельный router как ISP и создать loopback interfaces, имитирующие public internet hosts.

Edge router может достигать этих loopbacks через default route, но private LAN host без NAT получает failure из-за отсутствующего return path. Эта controlled failure наглядно показывает проблему, которую решает NAT.

## Key Points

- Для учебного internet достаточно отдельного ISP router.
- Packet Tracer cloud object не обязателен.
- Не следует усложнять lab bridging к реальной машине без необходимости.
- Между cafe edge и ISP создается point-to-point/WAN network.
- Сначала проверяется direct Layer 3 reachability между routers.
- Loopback interfaces создают стабильные simulated public endpoints.
- `1.1.1.1` и `8.8.8.8` удобны как узнаваемые test addresses в lab.
- Default route позволяет cafe router отправлять unknown traffic ISP.
- Ping с edge router может работать до настройки NAT.
- Ping с private PC может fail из-за отсутствия return route к RFC 1918 network.
- NAT заменит private source на address, известный ISP side.

## Notes

### Keep The Lab Focused

Попытка связать Packet Tracer с physical host network может добавить проблемы:

- adapter bridging;
- host firewall;
- hypervisor settings;
- permissions;
- unsupported Packet Tracer behavior;
- accidental interaction с real network.

Для изучения routing и NAT это лишняя сложность.

Цель lab:

```text
Simulate the behavior, not the entire real internet.
```

### Use A Router As The ISP

Provider network также построена на routers.

Для lab:

1. Добавить Cisco router.
2. Назвать его `ISP-RTR01`.
3. Соединить с `CAFE01-RTR01`.
4. Назначить addresses на общей WAN subnet.
5. Создать public-style loopbacks.
6. Проверить routing.

Topology:

```text
Cafe LAN
   |
CAFE01-RTR01
   |
Public WAN handoff
   |
ISP-RTR01
   |
Loopback test destinations
```

### Basic ISP Router Setup

Пример housekeeping:

```cisco
enable
configure terminal
hostname ISP-RTR01
enable secret <secret>

line console 0
 password <console-password>
 login

line vty 0 4
 password <vty-password>
 login
 transport input telnet
end
```

В production plaintext line passwords и Telnet не рекомендуются. Для реального environment используй local users, SSH, AAA и protected secrets.

В lab эти commands могут демонстрировать basic access configuration.

### Configure The WAN Handoff

Пример `/30`:

```text
ISP router:  216.0.5.1/30
Cafe router: 216.0.5.2/30
```

На ISP:

```cisco
configure terminal
interface GigabitEthernet0/0
 description Link to CAFE01-RTR01
 ip address 216.0.5.1 255.255.255.252
 no shutdown
end
```

На cafe edge:

```cisco
configure terminal
interface GigabitEthernet0/2
 description Link to ISP-RTR01
 ip address 216.0.5.2 255.255.255.252
 no shutdown
end
```

Interface names зависят от выбранных router models и modules.

### Verify The Handoff First

Проверить:

```cisco
show ip interface brief
ping 216.0.5.1
```

На ISP:

```cisco
ping 216.0.5.2
```

До NAT должны работать:

- physical link;
- interface status;
- same-subnet addressing;
- ARP/Layer 2 delivery;
- direct IP reachability.

### Why Loopbacks Are Useful

Loopback interface:

- virtual;
- не зависит от cable state;
- остается up, пока не shut administratively;
- удобен как stable router ID или test endpoint;
- не требует отдельного simulated server.

Создание:

```cisco
configure terminal

interface Loopback0
 ip address 1.1.1.1 255.255.255.255

interface Loopback1
 ip address 8.8.8.8 255.255.255.255

end
```

Mask `/32` обозначает один host address.

### About The Public Test Addresses

В реальности:

- `1.1.1.1` принадлежит public DNS service Cloudflare;
- `8.8.8.8` принадлежит Google Public DNS.

В isolated Packet Tracer lab эти addresses используются только как узнаваемые simulated endpoints.

Нельзя назначать чужие public addresses в реальной connected network.

### Default Route On The Cafe Router

Cafe router должен отправлять unknown destinations к ISP:

```cisco
ip route 0.0.0.0 0.0.0.0 216.0.5.1
```

Проверка:

```cisco
show ip route
ping 1.1.1.1
ping 8.8.8.8
```

Почему ping с router работает:

- destination следует default route;
- source обычно становится public WAN address `216.0.5.2`;
- ISP знает connected `/30`;
- reply имеет valid return path.

### Why The Inside PC Fails

Inside PC:

```text
IP:      192.168.1.50/24
Gateway: 192.168.1.1
```

Он отправляет ping к `1.1.1.1`:

1. PC передает packet cafe router.
2. Cafe router использует default route.
3. ISP получает packet с source `192.168.1.50`.
4. ISP routing table не содержит `192.168.1.0/24`.
5. Reply не имеет пути обратно.

Outbound path существует, return path отсутствует.

### Why The ISP Should Not Know Private LANs

Можно было бы добавить на simulated ISP:

```cisco
ip route 192.168.1.0 255.255.255.0 216.0.5.2
```

Тогда lab ping мог бы заработать без NAT.

Но это не моделирует normal public internet behavior.

Real ISP не хранит route к каждой customer's private RFC 1918 network, потому что эти ranges:

- повторяются у многих customers;
- не globally unique;
- фильтруются на public edge.

Поэтому правильное решение для scenario - NAT на cafe router.

### This Failure Is Valuable

Последовательность доказывает:

```text
Router-to-internet simulation works.
Default route works.
WAN handoff works.
Private-host return path does not work.
```

Это сужает проблему до source addressing/translation, а не vague "internet is broken".

### Test IP Before Applications

Начинай с direct IP tests:

```text
ping 1.1.1.1
ping 8.8.8.8
```

Browser test добавляет variables:

- DNS;
- HTTP/HTTPS;
- certificates;
- server application;
- proxy;
- filtering;
- browser behavior.

Сначала докажи Layer 3 connectivity, затем переходи к DNS и applications.

### Suggested Verification Order

1. `show ip interface brief`
2. Ping directly connected ISP address.
3. `show ip route`
4. Ping ISP loopback from cafe router.
5. Ping ISP loopback from inside PC.
6. Observe the expected failure.
7. Configure NAT/PAT.
8. Repeat PC ping.
9. Inspect NAT translations.

## Configuration Example

### ISP Router

```cisco
enable
configure terminal
hostname ISP-RTR01

interface GigabitEthernet0/0
 description Link to CAFE01-RTR01
 ip address 216.0.5.1 255.255.255.252
 no shutdown

interface Loopback0
 ip address 1.1.1.1 255.255.255.255

interface Loopback1
 ip address 8.8.8.8 255.255.255.255

end
```

### Cafe Router

```cisco
enable
configure terminal

interface GigabitEthernet0/2
 description Link to ISP-RTR01
 ip address 216.0.5.2 255.255.255.252
 no shutdown

ip route 0.0.0.0 0.0.0.0 216.0.5.1

end
```

## Troubleshooting Checklist

- Проверить cable и interface modules.
- Проверить `up/up`.
- Проверить `/30` addressing.
- Проверить ping между WAN addresses.
- Проверить loopback state.
- Проверить default route.
- Проверить source IP ping с router.
- Проверить inside PC gateway.
- Объяснить return path failure до NAT.
- Не маскировать проблему static route к RFC 1918 на ISP.

## Quick Self-Check

### Question 1

Зачем использовать router вместо Packet Tracer cloud?

Answer:

```text
Router создает понятную и контролируемую эмуляцию ISP routing behavior.
```

### Question 2

Зачем нужны loopback interfaces?

Answer:

```text
Они дают стабильные virtual endpoints для проверки reachability.
```

### Question 3

Почему cafe router может ping `1.1.1.1` до NAT?

Answer:

```text
Он использует public WAN source address, к которому ISP имеет connected return route.
```

### Question 4

Почему private PC не получает reply?

Answer:

```text
ISP не знает route к private source network, поэтому отсутствует return path.
```

### Question 5

Почему не нужно добавлять private route на ISP?

Answer:

```text
Public internet не маршрутизирует customer RFC 1918 networks; scenario должен решаться NAT.
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| ISP router | Simulated provider router. |
| WAN handoff | Connection между customer edge и provider. |
| Loopback | Stable virtual router interface. |
| `/32` | Prefix, представляющий один IPv4 host. |
| Default route | Fallback route toward ISP. |
| Return path | Route для reply traffic. |
| RFC 1918 | Private IPv4 address specification. |
| `show ip interface brief` | Проверяет interface addressing/status. |
| `show ip route` | Проверяет routing decisions. |
| Emulated internet | Controlled lab representation of provider/public networks. |

## What To Review Later

- PAT configuration
- NAT inside and outside interfaces
- NAT ACLs
- `show ip nat translations`
- Packet Tracer simulation mode
- ICMP packet flow
- Return path troubleshooting
