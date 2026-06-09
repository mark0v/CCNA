# What Now? Routing Foundations

Source: закрытая страница курса  
Date added: 2026-06-09  
Related plan item: Week 6 / Routing foundations checkpoint  
Tags: routing, static route, default route, EIGRP, routing table, NAT, documentation, WAN
Language: Russian
Translation pair: articles-en/2026-06/week-06/06-what-now-routing-foundations.md

## Summary

Этот checkpoint объединяет базовые routing skills: connected, static, default и dynamic routes, чтение routing table, построение WAN и ведение documentation. Теперь routing воспринимается не как набор отдельных commands, а как процесс выбора пути для каждого packet.

Следующий важный шаг - NAT. Default route показывает traffic направление к ISP, но private IPv4 addresses не становятся public-routable автоматически.

## Key Points

- Базовая routed network уже может соединять несколько LANs.
- Connected routes возникают автоматически от active interfaces.
- Static routes вручную описывают пути к remote networks.
- Default route обрабатывает destinations без более specific match.
- EIGRP показал принцип автоматического обмена routes.
- `show ip route` показывает текущих winners, установленных для forwarding.
- Router может знать альтернативные paths, не показывая их как active route.
- Private addressing удобно для внутренних networks, но требует NAT для internet access.
- Текущая простая addressing scheme будет улучшена после изучения subnetting.
- Documentation является частью engineering workflow.
- Следующий блок связывает routing с NAT и полноценным internet access.

## Notes

### What You Can Do Now

После этого блока ты можешь:

- назначить IP addresses router interfaces;
- поднять interfaces командой `no shutdown`;
- проверить состояние через `show ip interface brief`;
- распознать connected и local routes;
- связать две locations через WAN;
- добавить static route к remote LAN;
- настроить return path;
- добавить default route к ISP;
- запустить базовый EIGRP;
- проверить neighbor adjacency;
- читать route entry;
- объяснить AD, metric и longest prefix match;
- документировать devices и IP assignments.

Это уже рабочая основа routed networking.

### From A Diagram To A Real Flow

Topology больше не является абстрактным рисунком.

Можно проследить packet:

```text
Source host
-> local switch
-> default gateway
-> routing table lookup
-> next hop
-> remote router
-> destination network
```

Для reply выполняется отдельный routing decision в обратную сторону.

### Temporary Addressing Is Fine For Learning

В lab используется знакомая схема:

```text
192.168.1.0/24
192.168.2.0/24
192.168.3.0/24
```

Она легко читается и помогает сосредоточиться на routing.

Но real network design должен учитывать:

- количество hosts;
- growth;
- route summarization;
- VLAN structure;
- address waste;
- security boundaries;
- site hierarchy;
- DHCP scopes.

После subnetting addressing plan станет эффективнее.

### Static Routing Recap

Static route явно сообщает router:

```text
To reach this network, use this next hop.
```

Пример:

```cisco
ip route 192.168.3.0 255.255.255.0 192.168.2.2
```

Static routing:

- прост;
- предсказуем;
- подходит для small/stub networks;
- требует ручного сопровождения;
- нуждается в return routes.

### Default Routing Recap

Default route:

```cisco
ip route 0.0.0.0 0.0.0.0 216.0.5.1
```

Она означает:

```text
Если более specific route отсутствует, передать packet ISP next hop.
```

Default route не заменяет:

- specific routes;
- NAT;
- DNS;
- firewall policy;
- ISP return routing.

### Dynamic Routing Recap

EIGRP продемонстрировал dynamic routing:

```text
Routers discover neighbors.
Routers advertise connected networks.
Routers exchange route information.
Routers install preferred paths.
```

Базовая конфигурация:

```cisco
router eigrp 1
 network 192.168.1.0 0.0.0.255
 network 192.168.2.0 0.0.0.255
```

Dynamic routing полезен при росте topology и количестве prefixes.

### Reading `show ip route`

`show ip route` показывает текущую forwarding decision.

Важные route codes:

| Code | Meaning |
| --- | --- |
| `C` | Connected |
| `L` | Local interface address |
| `S` | Static |
| `S*` | Static candidate default |
| `D` | EIGRP |

Route selection:

1. Longest prefix match.
2. Lower administrative distance для одинакового prefix.
3. Lower protocol metric для paths одного source.

### The Routing Table Shows Winners

Router может получить несколько routes к одному destination.

Но `show ip route` обычно показывает best route или equal-cost winners, установленные для forwarding.

Альтернативные routes могут находиться:

- в EIGRP topology table;
- в OSPF LSDB;
- в BGP table;
- в configuration как floating static route.

Поэтому отсутствие route в main table не всегда означает, что protocol никогда о нем не слышал.

### Why Internet Still Does Not Work Fully

Default route направляет packet к ISP.

Но внутренние hosts используют private addresses:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

Эти ranges не маршрутизируются в public internet.

Если cafe PC с address `192.168.1.10` отправляет traffic наружу:

1. PC отправляет packet default gateway.
2. Router выбирает default route.
3. Packet может уйти к ISP.
4. Private source address остается непригодным для normal public return routing.

Нужна address translation.

### NAT Is The Next Step

NAT означает:

```text
Network Address Translation
```

NAT изменяет address information на network edge.

Для small business internet access чаще используется PAT:

```text
Port Address Translation
```

Много private hosts могут использовать один public IP с разными transport-layer ports.

Упрощенная схема:

```text
192.168.1.10:50000
-> translated to
216.0.5.2:30001
```

Router отслеживает translation и возвращает reply правильному internal host.

### Routing And NAT Solve Different Problems

Routing отвечает:

```text
Where should the packet go?
```

NAT отвечает:

```text
Which address representation should cross this boundary?
```

Для internet access нужны оба механизма:

- route к ISP;
- address translation для private hosts.

### Documentation Is A Core Skill

Документация - не побочная задача после успешного ping.

Нужно фиксировать:

- hostname;
- site;
- interface purpose;
- IP/prefix;
- next hop;
- route purpose;
- WAN circuit;
- software version;
- configuration rationale;
- date and author.

Особенно полезно записывать не только что настроено, но и почему.

Через несколько месяцев это экономит время на reverse engineering собственных решений.

### A Suggested Routing Record

| Device | Destination | Prefix | Route Type | Next Hop | Exit Interface | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| CAFE01-RTR01 | Shelter LAN | 192.168.3.0/24 | EIGRP | 192.168.2.2 | Gi0/1 | Site connectivity |
| CAFE01-RTR01 | Default | 0.0.0.0/0 | Static | 216.0.5.1 | Gi0/2 | Internet upstream |

### Troubleshooting Mindset

Теперь vague issue:

```text
The remote server is unreachable.
```

можно разложить:

1. Local host addressing.
2. Default gateway.
3. Local interface state.
4. Connected route.
5. Remote route.
6. Next-hop reachability.
7. Routing protocol neighbor.
8. Return route.
9. NAT, если crossing public boundary.
10. ACL/firewall policy.

Это переход от command memorization к systematic troubleshooting.

## Routing Foundations Checklist

- [ ] Могу объяснить connected route.
- [ ] Могу настроить static route.
- [ ] Всегда проверяю return path.
- [ ] Могу настроить default route.
- [ ] Понимаю gateway of last resort.
- [ ] Понимаю basic dynamic routing.
- [ ] Могу проверить EIGRP neighbor.
- [ ] Читаю `[AD/metric]`.
- [ ] Применяю longest prefix match.
- [ ] Понимаю, почему нужен NAT.
- [ ] Документирую network while building.

## Quick Self-Check

### Question 1

Что показывает `show ip route`?

Answer:

```text
Лучшие routes, установленные router для forwarding.
```

### Question 2

Почему default route недостаточно для private host internet access?

Answer:

```text
Private source addresses требуют NAT/PAT для нормального обмена с public internet.
```

### Question 3

Что выбирается первым при route lookup?

Answer:

```text
Самый длинный matching prefix.
```

### Question 4

Какую проблему решает dynamic routing?

Answer:

```text
Автоматизирует обмен routes и уменьшает ручное сопровождение растущей network.
```

### Question 5

Когда обновлять documentation?

Answer:

```text
Во время каждого change, пока configuration и rationale свежи.
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `show ip route` | Показывает installed routes. |
| Static route | Вручную заданный путь. |
| Default route | Fallback path для unknown destinations. |
| Dynamic routing | Автоматический обмен routes. |
| EIGRP | Dynamic routing protocol из урока. |
| NAT | Network Address Translation. |
| PAT | Translation многих private sessions через public IP. |
| Private IPv4 | Addresses, не маршрутизируемые в public internet. |
| Return path | Маршрут reply к source. |
| Documentation | Актуальная запись topology и design decisions. |

## What To Review Later

- NAT terminology
- Static NAT
- Dynamic NAT
- PAT / overload
- Inside local and inside global
- Subnetting
- ACLs and firewall policy
- Route troubleshooting
