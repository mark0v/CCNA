# Static Routing Basics

Source: закрытая страница курса  
Date added: 2026-06-09  
Related plan item: Week 6 / Static routing  
Tags: static route, routing table, next hop, return path, WAN, Cisco IOS, ip route
Language: Russian
Translation pair: articles-en/2026-06/week-06/01-static-routing-basics.md

## Summary

Static route - это вручную заданный путь к remote network, о которой router еще не знает. Router автоматически добавляет connected networks, но сети за другим router не появляются в routing table сами по себе.

Главная мысль: router может пересылать packets только туда, куда у него есть маршрут. Для полноценной связи нужен не только forward path, но и return path.

## Key Points

- Routers автоматически знают только directly connected networks.
- Remote network должна присутствовать в routing table.
- Static route настраивается вручную командой `ip route`.
- В маршруте указываются destination network, subnet mask и next-hop address.
- Next hop должен быть достижим через уже известную сеть.
- Маршрут только на одном router создает неполную или одностороннюю связность.
- Ответный router должен знать путь назад к source network.
- Успешный ping с самого router не всегда доказывает связность между конечными hosts.
- `show ip route` помогает понять, что router знает в данный момент.
- После настройки маршрутов нужно проверять оба направления.

## Notes

### What Static Routing Solves

В схеме NetworkChuck Coffee используются три сети:

```text
Cafe LAN:       192.168.1.0/24
Private WAN:    192.168.2.0/24
Shelter LAN:    192.168.3.0/24
```

Cafe router напрямую подключен к:

- `192.168.1.0/24`;
- `192.168.2.0/24`.

Shelter router напрямую подключен к:

- `192.168.2.0/24`;
- `192.168.3.0/24`.

Эти connected routes появляются автоматически, если interfaces настроены и находятся в состоянии `up/up`.

Но Cafe router не знает о `192.168.3.0/24`, а Shelter router не знает о `192.168.1.0/24`.

Именно этот пробел заполняют static routes.

### Routers Do Not Guess

Человек смотрит на topology diagram и видит очевидный путь:

```text
Cafe LAN -> Cafe router -> WAN -> Shelter router -> Shelter LAN
```

Router не анализирует схему так, как человек.

Для каждого packet он проверяет destination IP по своей routing table. Если подходящего маршрута нет, router не угадывает направление и отбрасывает packet.

Правило:

```text
No route, no trip.
```

### Prove What Already Works

Перед добавлением static route полезно проверить базовую связность:

1. Hosts достигают своих default gateways.
2. Router interfaces находятся в состоянии `up/up`.
3. Routers достигают друг друга через WAN.
4. Connected routes присутствуют в `show ip route`.

Это отделяет routing problem от проблем Layer 1, Layer 2 или неправильной IP configuration.

Если PC не может достичь даже собственного default gateway, добавление remote static route не решит проблему.

### Static Route Syntax

Базовый синтаксис Cisco IOS:

```text
ip route <destination-network> <subnet-mask> <next-hop-ip>
```

Команду можно прочитать так:

```text
Чтобы достичь этой destination network с такой subnet mask,
отправь packet следующему router по этому next-hop IP.
```

Для маршрута от Cafe router к Shelter LAN:

```cisco
ip route 192.168.3.0 255.255.255.0 192.168.2.2
```

Где:

| Часть | Значение |
| --- | --- |
| `192.168.3.0` | Destination network |
| `255.255.255.0` | Subnet mask destination network |
| `192.168.2.2` | Next-hop address Shelter router |

Router использует известную WAN network, чтобы передать packet следующему router.

### Why Next Hop Is Common

Static route также может ссылаться на exit interface.

Пример:

```cisco
ip route 192.168.3.0 255.255.255.0 GigabitEthernet0/1
```

Но во многих Ethernet-сценариях понятнее указывать next-hop IP:

```cisco
ip route 192.168.3.0 255.255.255.0 192.168.2.2
```

Так маршрут прямо показывает, какой соседний router должен получить traffic следующим.

Выбор синтаксиса зависит от типа link и design, но для начального понимания next hop обычно читается яснее.

### First Route: Forward Path

После добавления маршрута на Cafe router он знает:

```text
To reach 192.168.3.0/24, send traffic to 192.168.2.2.
```

Теперь forward path до Shelter LAN существует.

Можно проверить:

```cisco
show ip route
ping 192.168.3.10
```

Static route обычно отмечается в routing table буквой:

```text
S
```

Однако один успешный тест с router не всегда означает, что любой cafe host сможет полноценно общаться с remote server.

### One-Way Communication Is Not Success

Для нормального обмена traffic должен пройти в обе стороны:

```text
Request: Cafe LAN -> Shelter LAN
Reply:   Shelter LAN -> Cafe LAN
```

Если Cafe router знает путь к `192.168.3.0/24`, но Shelter router не знает путь к `192.168.1.0/24`, request может дойти до server, а reply потеряется.

Это классическая missing return route.

При troubleshooting всегда задавай два вопроса:

```text
Can traffic get there?
Can the reply get back?
```

### Second Route: Return Path

На Shelter router нужен обратный маршрут:

```cisco
ip route 192.168.1.0 255.255.255.0 192.168.2.1
```

Где:

| Часть | Значение |
| --- | --- |
| `192.168.1.0` | Cafe destination network |
| `255.255.255.0` | Cafe subnet mask |
| `192.168.2.1` | Next-hop address Cafe router |

После этого оба router знают remote LAN:

```text
Cafe router:
192.168.3.0/24 via 192.168.2.2

Shelter router:
192.168.1.0/24 via 192.168.2.1
```

Теперь есть forward и return paths.

### Why Router Ping Can Be Misleading

Источник ping влияет на routing behavior.

Если Cafe router pingует remote server, source IP может быть адресом WAN interface. Shelter router уже знает WAN network как connected route, поэтому reply может вернуться.

Но если ping отправляет PC из Cafe LAN, source IP принадлежит `192.168.1.0/24`. Без обратного маршрута Shelter router не знает, куда отправить reply.

Поэтому нужно тестировать:

- router-to-router;
- router-to-host;
- host-to-host;
- оба направления.

### Verify The Routing Table

После настройки используй:

```cisco
show ip route
```

Проверь:

- появилась ли строка с `S`;
- правильно ли указана destination network;
- правильная ли mask;
- правильный ли next hop;
- достижим ли next hop;
- есть ли маршрут на обратном router.

Можно также проверить running configuration:

```cisco
show running-config | include ip route
```

### Save The Configuration

После успешной проверки сохрани configuration:

```cisco
copy running-config startup-config
```

Или:

```cisco
write memory
```

Иначе маршруты могут исчезнуть после reload.

### When Static Routes Are Useful

Static routes хорошо подходят для:

- небольших networks;
- простых branch connections;
- стабильных путей;
- лабораторий;
- stub networks;
- default routes;
- backup routes;
- строго контролируемого forwarding.

Но при большом количестве routers и networks ручное управление становится сложным. Тогда используют dynamic routing protocols.

## Configuration Example

### Cafe Router

```cisco
enable
configure terminal
ip route 192.168.3.0 255.255.255.0 192.168.2.2
end
show ip route
```

### Shelter Router

```cisco
enable
configure terminal
ip route 192.168.1.0 255.255.255.0 192.168.2.1
end
show ip route
```

### Verification

```cisco
ping 192.168.2.2
ping 192.168.3.10
traceroute 192.168.3.10
show ip route
show ip interface brief
```

## Troubleshooting Checklist

Если static routing не работает:

1. Проверь IP address и subnet mask source host.
2. Проверь default gateway source host.
3. Проверь interface states командой `show ip interface brief`.
4. Проверь connected routes.
5. Проверь destination network и mask в static route.
6. Проверь next-hop IP.
7. Убедись, что next hop достижим.
8. Проверь static route на remote router.
9. Проверь return path.
10. Проверь host firewall и ACL только после проверки routing.
11. Протестируй каждый hop отдельно.

## Quick Self-Check

### Question 1

Что такое static route?

Answer:

```text
Вручную настроенный маршрут к network, которую router не знает автоматически.
```

### Question 2

Какие три основные части содержит команда `ip route`?

Answer:

```text
Destination network, subnet mask и next-hop IP либо exit interface.
```

### Question 3

Почему маршрута только на одном router недостаточно?

Answer:

```text
Reply traffic также должен иметь маршрут обратно к source network.
```

### Question 4

Какой командой посмотреть routing table?

Answer:

```text
show ip route
```

### Question 5

Какой код обозначает static route в Cisco routing table?

Answer:

```text
S
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Static route | Маршрут, настроенный administrator вручную. |
| `ip route` | Cisco IOS command для добавления IPv4 static route. |
| Destination network | Remote network, которую нужно достичь. |
| Next hop | Следующий router на пути к destination. |
| Forward path | Путь request к destination. |
| Return path | Путь reply обратно к source. |
| `show ip route` | Показывает routing table. |
| `S` | Код static route в Cisco routing table. |
| Connected route | Автоматический маршрут к directly attached network. |
| Remote network | Network, не подключенная напрямую к текущему router. |

## What To Review Later

- Default routes
- Floating static routes
- Administrative distance
- Recursive route lookup
- Longest prefix match
- Dynamic routing protocols
- Route troubleshooting
