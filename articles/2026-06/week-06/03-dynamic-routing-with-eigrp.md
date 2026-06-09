# Dynamic Routing With EIGRP

Source: закрытая страница курса  
Date added: 2026-06-09  
Related plan item: Week 6 / Dynamic routing introduction  
Tags: dynamic routing, EIGRP, adjacency, neighbor, routing table, Cisco IOS, network statement
Language: Russian
Translation pair: articles-en/2026-06/week-06/03-dynamic-routing-with-eigrp.md

## Summary

Dynamic routing позволяет routers автоматически обмениваться информацией о доступных networks. В отличие от static routing, administrator не вводит каждый remote route вручную: routers формируют neighbor relationships и добавляют изученные routes в routing table.

В уроке используется классический EIGRP. После удаления static routes сеть перестает достигать remote LANs. Затем EIGRP включается на нужных interfaces, routers становятся neighbors и автоматически обмениваются маршрутами.

## Key Points

- Dynamic routing автоматизирует обмен routes между routers.
- Static routes остаются полезными, но плохо масштабируются при росте сети.
- EIGRP означает Enhanced Interior Gateway Routing Protocol.
- `router eigrp 1` запускает classic EIGRP process с AS number `1`.
- Routers должны использовать совместимый EIGRP autonomous system number.
- `network` statement выбирает participating interfaces и объявляемые connected networks.
- Routers обнаруживают друг друга с помощью hello packets.
- После формирования adjacency они обмениваются routing information.
- EIGRP route обозначается кодом `D` в Cisco routing table.
- Dynamic routing следует включать только на intended links.
- Internet-facing interface не должен участвовать без явной design-причины.
- После изменения routing нужно проверять neighbors, routes и end-to-end connectivity.

## Notes

### Break The Network To Understand It

Хороший lab-подход:

1. Удалить существующие static routes.
2. Убедиться, что remote connectivity пропала.
3. Посмотреть routing table.
4. Настроить dynamic routing.
5. Наблюдать появление neighbors и learned routes.
6. Снова проверить connectivity.

Так становится ясно, какую проблему решает routing protocol.

Удаление static route:

```cisco
no ip route 192.168.3.0 255.255.255.0 192.168.2.2
```

На втором router:

```cisco
no ip route 192.168.1.0 255.255.255.0 192.168.2.1
```

После этого connected networks остаются, но remote LAN routes исчезают.

### What Dynamic Routing Means

Dynamic routing protocol позволяет routers сообщать друг другу:

```text
Какие networks мне известны.
Через какой path они доступны.
Когда route появился, изменился или исчез.
```

Router принимает routing updates, обрабатывает их по правилам протокола и устанавливает лучшие routes в routing table.

Это не магия, а автоматизированный обмен информацией.

### Static Versus Dynamic Routing

Static routing:

- настраивается вручную;
- предсказуем;
- прост в маленьких topologies;
- не создает routing protocol traffic;
- требует ручного обновления при изменениях.

Dynamic routing:

- автоматически обменивается routes;
- лучше масштабируется;
- адаптируется к topology changes;
- требует protocol configuration;
- использует CPU, memory и network traffic;
- требует контроля boundaries и соседств.

Оба подхода могут использоваться в одной network.

### Why EIGRP

EIGRP - dynamic interior gateway protocol, традиционно тесно связанный с Cisco environments.

Полное название:

```text
Enhanced Interior Gateway Routing Protocol
```

В этом вводном уроке важна не вся внутренняя mechanics EIGRP, а основной workflow:

```text
Enable process
Select interfaces/networks
Discover neighbors
Exchange routes
Install learned routes
```

### Autonomous System Number

Classic EIGRP запускается командой:

```cisco
router eigrp 1
```

Число `1` - autonomous system number EIGRP process.

Для формирования classic EIGRP adjacency соседние routers должны использовать один и тот же AS number и иметь совместимые параметры.

Пример на обоих routers:

```cisco
router eigrp 1
```

AS number здесь служит идентификатором routing domain, а не public BGP autonomous system assignment.

### The `network` Statement

В classic EIGRP команда `network` выполняет две важные задачи:

1. Выбирает local interfaces, на которых должен работать EIGRP.
2. Объявляет connected networks этих interfaces EIGRP neighbors.

Простой lab-вариант:

```cisco
router eigrp 1
 network 192.168.1.0
 network 192.168.2.0
```

Более точный вариант использует wildcard mask:

```cisco
router eigrp 1
 network 192.168.1.0 0.0.0.255
 network 192.168.2.0 0.0.0.255
```

Wildcard `0.0.0.255` соответствует `/24`.

Точное указание помогает избежать случайного включения протокола на лишних interfaces.

### Hello Packets And Neighbors

На participating interface EIGRP отправляет hello packets.

Они нужны для обнаружения и поддержания neighbors.

Если только один router настроен, он отправляет hello messages, но adjacency не формируется.

После настройки второго router на общей WAN network routers обнаруживают друг друга и становятся EIGRP neighbors.

Это событие часто сопровождается console message о новой adjacency.

### Neighbor Adjacency

Adjacency означает, что routers:

- обнаружили друг друга;
- согласовали необходимые protocol parameters;
- готовы обмениваться routing information;
- следят за доступностью соседа.

Проверка:

```cisco
show ip eigrp neighbors
```

Если neighbor отсутствует, routes через него изучаться не будут.

### Learned Routes

После формирования adjacency routers обмениваются известными networks.

Cafe router может изучить Shelter LAN:

```text
192.168.3.0/24
```

Shelter router может изучить Cafe LAN:

```text
192.168.1.0/24
```

Проверка:

```cisco
show ip route
```

EIGRP-learned route отмечается:

```text
D
```

Буква `E` уже используется для старого EGP, поэтому Cisco применяет `D`, исторически связанную с алгоритмом DUAL.

Пример:

```text
D 192.168.3.0/24 [90/...] via 192.168.2.2
```

### Do Not Enable It Everywhere

Dynamic routing должен работать только там, где это предусмотрено design.

Не следует бездумно включать EIGRP:

- на internet-facing interface;
- в user access LAN, где neighbors не ожидаются;
- на untrusted networks;
- на interfaces, чьи networks не должны рекламироваться.

Случайное включение может:

- раскрыть internal prefixes;
- создать нежелательное neighbor relationship;
- добавить ошибочные routes;
- усложнить troubleshooting;
- расширить attack surface.

### Internet-Facing Interface

В NetworkChuck Coffee cafe router имеет link к ISP.

Этот interface не включается в EIGRP process, потому что:

- ISP не является внутренним EIGRP neighbor;
- internal routes не нужно рекламировать туда;
- internet access уже может использовать default route;
- routing boundaries должны быть намеренными.

Важно различать:

```text
Internal dynamic routing domain
External ISP connection
```

### Passive Interfaces

Если connected LAN нужно рекламировать, но EIGRP neighbors на нем не ожидаются, можно использовать passive interface.

Пример:

```cisco
router eigrp 1
 passive-interface GigabitEthernet0/0
```

Network этого interface может оставаться advertised, но EIGRP hello packets через него не отправляются.

Практичный подход:

```cisco
router eigrp 1
 passive-interface default
 no passive-interface GigabitEthernet0/1
```

Так все interfaces passive по умолчанию, кроме явно разрешенного router-to-router link.

### Verification Commands

Основные команды:

```cisco
show ip protocols
show ip eigrp neighbors
show ip eigrp topology
show ip route
show ip route eigrp
show ip interface brief
```

Они отвечают на разные вопросы:

| Command | Что проверяет |
| --- | --- |
| `show ip protocols` | Protocol process, networks, passive interfaces |
| `show ip eigrp neighbors` | Сформированные EIGRP neighbors |
| `show ip eigrp topology` | EIGRP topology information |
| `show ip route eigrp` | Routes, установленные через EIGRP |
| `show ip interface brief` | Interface addresses and states |

### End-To-End Testing

После появления `D` routes проверь:

```cisco
ping 192.168.3.10
traceroute 192.168.3.10
```

Но тестировать нужно с конечных hosts, а не только с routers.

Полезная последовательность:

1. PC достигает default gateway.
2. Routers достигают друг друга по WAN.
3. EIGRP adjacency существует.
4. Remote routes присутствуют.
5. Remote gateway достижим.
6. Remote host достижим.
7. Return traffic работает.

### Why Dynamic Routing Scales Better

Для двух routers static routing выглядит проще.

Но сеть может вырасти:

- несколько coffee shops;
- guest Wi-Fi networks;
- point-of-sale VLANs;
- voice networks;
- security cameras;
- inventory systems;
- redundant WAN links;
- data centers.

При каждом новом prefix ручное обновление всех routers становится дорогим и ошибкоопасным.

Dynamic routing уменьшает объем ручной route configuration и может автоматически реагировать на topology changes.

### Save The Configuration

После проверки:

```cisco
copy running-config startup-config
```

## Configuration Example

### Cafe Router

```cisco
enable
configure terminal

router eigrp 1
 network 192.168.1.0 0.0.0.255
 network 192.168.2.0 0.0.0.255
 passive-interface GigabitEthernet0/0

end
```

### Shelter Router

```cisco
enable
configure terminal

router eigrp 1
 network 192.168.2.0 0.0.0.255
 network 192.168.3.0 0.0.0.255
 passive-interface GigabitEthernet0/0

end
```

Interface names нужно адаптировать под фактическую topology.

### Verification

```cisco
show ip protocols
show ip eigrp neighbors
show ip route eigrp
ping 192.168.3.10
```

## Troubleshooting Checklist

Если EIGRP routes не появляются:

1. Проверь interface state и IP addressing.
2. Проверь, что routers находятся в одной WAN subnet.
3. Проверь одинаковый EIGRP AS number.
4. Проверь `network` statements.
5. Проверь wildcard masks.
6. Убедись, что router-to-router interface не passive.
7. Проверь `show ip eigrp neighbors`.
8. Проверь ACL или filtering.
9. Проверь, что нужная connected network действительно существует.
10. Проверь routing table и return path.

## Quick Self-Check

### Question 1

Что такое dynamic routing?

Answer:

```text
Автоматический обмен routing information между routers с помощью routing protocol.
```

### Question 2

Что означает EIGRP?

Answer:

```text
Enhanced Interior Gateway Routing Protocol.
```

### Question 3

Для чего нужен EIGRP AS number?

Answer:

```text
Он идентифицирует classic EIGRP routing process; neighbors должны использовать совместимый, обычно одинаковый номер.
```

### Question 4

Что делает EIGRP `network` statement?

Answer:

```text
Выбирает participating interfaces и объявляет их connected networks.
```

### Question 5

Какой код обозначает EIGRP route в routing table?

Answer:

```text
D
```

### Question 6

Почему не следует включать EIGRP на ISP interface?

Answer:

```text
Он не относится к internal routing domain, и internal routes не должны случайно рекламироваться наружу.
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Dynamic routing | Автоматический обмен routes между routers. |
| EIGRP | Enhanced Interior Gateway Routing Protocol. |
| `router eigrp 1` | Запуск classic EIGRP process с AS number `1`. |
| `network` | Выбор interfaces/networks для EIGRP participation. |
| Hello packet | Сообщение для обнаружения и поддержания neighbors. |
| Adjacency | Рабочее neighbor relationship между routers. |
| `D` | Код EIGRP route в Cisco routing table. |
| Passive interface | Interface, где hellos не отправляются, но network может рекламироваться. |
| `show ip eigrp neighbors` | Показывает EIGRP neighbors. |
| `show ip protocols` | Показывает настройки active routing protocols. |

## What To Review Later

- EIGRP DUAL algorithm
- Feasible distance and reported distance
- EIGRP metrics
- Passive interfaces
- Route summarization
- OSPF
- Administrative distance
- Routing protocol authentication
