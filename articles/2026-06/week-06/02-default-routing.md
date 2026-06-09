# Default Routing

Source: закрытая страница курса  
Date added: 2026-06-09  
Related plan item: Week 6 / Default routing  
Tags: default route, gateway of last resort, ISP, static route, routing table, longest prefix match, Cisco IOS
Language: Russian
Translation pair: articles-en/2026-06/week-06/02-default-routing.md

## Summary

Router не обязан знать маршрут к каждой network в internet. Вместо этого на edge router настраивают default route - fallback path, который используется, когда в routing table нет более конкретного маршрута.

Главная мысль: default route не делает router всезнающим. Она лишь указывает, кому передать packet дальше, если router сам не знает destination network.

## Key Points

- Default route используется только при отсутствии более specific route.
- В IPv4 она записывается как `0.0.0.0 0.0.0.0`.
- Default route часто указывает на next-hop router ISP.
- Gateway of last resort - следующий hop для неизвестных destinations.
- Более specific routes имеют приоритет над default route.
- Перед настройкой default route ISP-facing interface должен быть настроен и `up/up`.
- ISP предоставляет public IP, subnet mask и next-hop information.
- `/30` часто используется на point-to-point links между routers.
- В `show ip route` default static route обычно отмечается `S*`.
- Default route решает вопрос outbound routing, но не заменяет NAT или return routing.

## Notes

### Do We Need Every Internet Route?

Internet состоит из огромного количества networks.

Для небольшого business router бессмысленно вручную добавлять маршрут к каждой из них.

Вместо полного internet routing table router должен знать:

```text
Если у меня нет более точного маршрута, отправить traffic upstream provider.
```

Эту инструкцию дает default route.

### Gateway Of Last Resort

Gateway of last resort - это router, которому отправляется traffic, если более подходящего маршрута нет.

Пример:

```text
Cafe router знает local LAN.
Cafe router знает WAN к shelter.
Cafe router не знает destination website.
Cafe router использует gateway of last resort.
```

Default route является последним вариантом, а не первым.

### Routing Knowledge Builds In Layers

Router получает маршруты постепенно:

1. Connected routes появляются от active interfaces.
2. Static routes добавляют конкретные remote networks.
3. Default route покрывает все остальные неизвестные destinations.
4. Dynamic routing protocols могут автоматически обмениваться routes.

Каждый слой дополняет предыдущий.

### What The ISP Provides

При подключении к ISP обычно предоставляются:

- public IP address для customer router;
- subnet mask или prefix length;
- ISP next-hop IP;
- DNS information;
- иногда VLAN, encapsulation или authentication settings.

Эти значения нельзя угадывать. Их нужно получить у provider и задокументировать.

Пример:

```text
Cafe router public IP: 216.0.5.2/30
ISP router IP:         216.0.5.1/30
```

### Why `/30` Is Common

Prefix `/30` соответствует mask:

```text
255.255.255.252
```

Традиционная `/30` subnet содержит четыре addresses:

- network address;
- два usable host addresses;
- broadcast address.

Это удобно для point-to-point IPv4 link, где нужны адреса только двум router interfaces.

В современных сетях также может использоваться `/31`, но `/30` остается распространенным учебным и legacy-вариантом.

### Configure The ISP Interface First

До добавления default route необходимо поднять link к ISP.

Пример:

```cisco
enable
configure terminal
interface GigabitEthernet0/2
 description Link to ISP
 ip address 216.0.5.2 255.255.255.252
 no shutdown
end
```

Проверка:

```cisco
show ip interface brief
ping 216.0.5.1
```

Если ISP next hop недостижим, default route не обеспечит internet connectivity.

### Default Route Command

Базовый Cisco IOS command:

```cisco
ip route 0.0.0.0 0.0.0.0 216.0.5.1
```

Элементы:

| Часть | Значение |
| --- | --- |
| `0.0.0.0` | Любая destination network |
| `0.0.0.0` | Mask, совпадающая с любым IPv4 address |
| `216.0.5.1` | Next-hop ISP router |

Перевод на обычный язык:

```text
Если не найден более specific route, отправить packet к 216.0.5.1.
```

### Why `0.0.0.0/0` Matches Everything

CIDR-запись default route:

```text
0.0.0.0/0
```

Prefix length `/0` означает, что для совпадения не требуется ни одного фиксированного network bit.

Поэтому любой IPv4 destination подходит под этот route.

Но routing table может содержать и более specific matches.

### Longest Prefix Match

Router выбирает наиболее specific matching route, то есть route с самым длинным prefix.

Пример:

```text
192.168.3.0/24 via 192.168.2.2
0.0.0.0/0 via 216.0.5.1
```

Packet к `192.168.3.10` совпадает с обоими routes, но `/24` более specific, чем `/0`.

Поэтому он пойдет к shelter router, а не к ISP.

Packet к неизвестному internet address, например `8.8.8.8`, не совпадет с конкретными local/remote routes и использует `/0`.

### Verify The Default Route

Используй:

```cisco
show ip route
```

Ожидаемая запись может выглядеть так:

```text
S* 0.0.0.0/0 [1/0] via 216.0.5.1
```

Где:

- `S` - static route;
- `*` - candidate default route;
- `0.0.0.0/0` - default destination;
- `216.0.5.1` - next hop.

В верхней части output также может появиться:

```text
Gateway of last resort is 216.0.5.1 to network 0.0.0.0
```

### NetworkChuck Coffee Packet Flow

Пользователь в cafe открывает website:

1. PC определяет, что destination не в local subnet.
2. PC отправляет frame своему default gateway.
3. Cafe router получает packet.
4. Router ищет destination в routing table.
5. Более specific route отсутствует.
6. Router выбирает default route.
7. Packet отправляется ISP router.
8. ISP и internet routing infrastructure продолжают forwarding.

Схема:

```text
Cafe PC
  -> Cafe switch
  -> Cafe router
  -> default route
  -> ISP router
  -> Internet
```

### What Happens Without A Default Route

Без default route internal networks могут продолжать работать:

- hosts общаются внутри LAN;
- cafe достигает shelter по static route;
- routers пингуют connected interfaces.

Но unknown internet destinations не имеют matching route.

Router отбрасывает packets:

```text
No matching route -> packet dropped
```

### Default Route Does Not Solve Everything

Default route задает outbound direction, но internet access может требовать и других компонентов:

- valid public addressing;
- NAT/PAT для private hosts;
- ISP return route;
- DNS;
- firewall or ACL policy;
- working physical link;
- correct default gateway on clients.

Если private host отправляет packet в internet, default route может направить его к ISP, но без NAT private source address обычно не будет корректно маршрутизироваться в public internet.

### BGP And Internet-Scale Routing

Крупные providers и networks обмениваются internet routes с помощью BGP.

BGP расшифровывается как Border Gateway Protocol.

Он позволяет autonomous systems сообщать друг другу, какие prefixes они могут достигать.

Небольшой cafe router не обязан хранить полный internet table. Он просто отправляет неизвестный traffic своему provider, который располагает более широким routing knowledge.

### Troubleshooting Order

Если default routing не работает:

1. Проверь ISP interface status.
2. Проверь public IP и mask.
3. Пингуй ISP next hop.
4. Проверь `show ip route`.
5. Проверь правильность `0.0.0.0/0`.
6. Проверь next-hop typo.
7. Проверь NAT для private clients.
8. Проверь ACL/firewall rules.
9. Проверь DNS отдельно от IP reachability.
10. Убедись, что ISP имеет return path.

### Save The Configuration

После проверки:

```cisco
copy running-config startup-config
```

Иначе default route исчезнет после reload.

## Configuration Example

```cisco
enable
configure terminal

interface GigabitEthernet0/2
 description Internet uplink
 ip address 216.0.5.2 255.255.255.252
 no shutdown

ip route 0.0.0.0 0.0.0.0 216.0.5.1

end
show ip interface brief
show ip route
ping 216.0.5.1
```

## Practical Checklist

- Получить addressing information от ISP.
- Настроить ISP-facing interface.
- Проверить состояние `up/up`.
- Проверить reachability ISP next hop.
- Настроить `0.0.0.0/0`.
- Проверить `S*` в routing table.
- Убедиться, что specific static routes по-прежнему выбираются.
- Проверить NAT для private networks.
- Проверить DNS после IP connectivity.
- Сохранить configuration.

## Quick Self-Check

### Question 1

Когда используется default route?

Answer:

```text
Когда routing table не содержит более specific route к destination.
```

### Question 2

Как выглядит IPv4 default route?

Answer:

```text
0.0.0.0/0
```

### Question 3

Что означает gateway of last resort?

Answer:

```text
Next hop, которому router передает traffic для неизвестных destinations.
```

### Question 4

Какой route победит: `192.168.3.0/24` или `0.0.0.0/0` для address `192.168.3.10`?

Answer:

```text
192.168.3.0/24, потому что это более specific prefix.
```

### Question 5

Как default static route обозначается в Cisco routing table?

Answer:

```text
S*
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Default route | Fallback route для неизвестных destinations. |
| `0.0.0.0/0` | IPv4 prefix, совпадающий с любым destination. |
| Gateway of last resort | Next hop для traffic без более specific route. |
| `ip route 0.0.0.0 0.0.0.0 <next-hop>` | Cisco default static route command. |
| `S*` | Static candidate default route в Cisco routing table. |
| ISP | Internet service provider. |
| Public IP | Address, маршрутизируемый в public internet. |
| Longest prefix match | Выбор самого specific matching route. |
| `/30` | Небольшая IPv4 subnet с двумя традиционно usable addresses. |
| BGP | Internet-scale routing protocol между autonomous systems. |

## What To Review Later

- NAT and PAT
- Longest prefix match
- Floating default routes
- BGP basics
- IPv4 subnetting
- ISP edge design
- Default route troubleshooting
