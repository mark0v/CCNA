# Updating Addressing, NAT, And DHCP

Source: закрытая страница курса  
Date added: 2026-06-20  
Related plan item: Week 8 / Applying the new subnet plan  
Tags: IPv4, subnetting, NAT, wildcard mask, DHCP, router configuration, Packet Tracer
Language: Russian
Translation pair: articles-en/2026-06/week-08/01-updating-addressing-nat-and-dhcp.md

## Кратко

Когда subnet plan готов на бумаге, его нужно перенести в живую конфигурацию. В этой части мы берем новый subnet `10.0.18.0/26` для district shop и приводим под него router interface, NAT и DHCP.

Главная мысль простая: IP addressing не живет отдельно от остальных сервисов. Если меняется subnet, вместе с ним нужно проверить:

- gateway address;
- subnet mask;
- старые interfaces и loopbacks;
- NAT access list;
- wildcard mask;
- DHCP excluded addresses;
- DHCP pool;
- DNS server;
- default router для клиентов;
- фактические DHCP bindings.

Иначе сеть может выглядеть почти правильно, но ломаться из-за старой конфигурации, которая осталась где-то сбоку.

## Новый Gateway Для LAN

На LAN-facing router interface был назначен адрес:

```text
10.0.18.1 255.255.255.192
```

`255.255.255.192` - это dotted decimal запись для `/26`.

Это нужно уметь переводить в обе стороны:

```text
/26 = 255.255.255.192
255.255.255.192 = /26
```

В разных командах и интерфейсах тебе могут встретиться разные форматы. Где-то удобнее slash notation, где-то требуется dotted decimal mask. Для инженера это один и тот же смысл, просто две формы записи.

Для subnet `10.0.18.0/26` диапазон выглядит так:

```text
Network address:    10.0.18.0
Usable range:       10.0.18.1 - 10.0.18.62
Broadcast address:  10.0.18.63
Subnet mask:        255.255.255.192
```

Логично отдать первый usable address router interface, потому что он будет default gateway для устройств в этой LAN.

## Старую Конфигурацию Нужно Убирать

При изменении адресного плана недостаточно добавить новый IP address. Нужно удалить то, что больше не соответствует design.

В уроке были убраны:

- старые loopback interfaces;
- старый WAN link;
- stale config, который относился к прошлой схеме.

Это важная привычка. Очень часто проблема появляется не потому, что новая настройка неправильная, а потому что рядом осталась старая. Router продолжает иметь лишние routes, NAT rules, interfaces или ACL entries, и troubleshooting становится мутным.

Хороший подход:

1. Понять, что должно остаться по новой схеме.
2. Удалить то, что больше не используется.
3. Настроить новые параметры.
4. Проверить, что running config больше не содержит старого design.

## NAT Тоже Нужно Обновить

NAT означает Network Address Translation. Это механизм, который позволяет internal private IP addresses выходить во внешние сети, например в internet.

Если subnet изменился, NAT rule тоже должна измениться. Старая NAT access list все еще может ссылаться на предыдущий subnet. Тогда новые clients либо не будут переводиться, либо NAT будет работать не для того диапазона.

Новый subnet:

```text
10.0.18.0/26
```

Subnet mask:

```text
255.255.255.192
```

Wildcard mask для ACL:

```text
0.0.0.63
```

Wildcard mask - это обратная форма subnet mask.

```text
255.255.255.192
0.0.0.63
```

Последний octet можно проверить так:

```text
255 - 192 = 63
```

Поэтому для `10.0.18.0/26` NAT ACL должна матчить диапазон `10.0.18.0 - 10.0.18.63` через wildcard `0.0.0.63`.

На практике это выглядит странно только в начале. Потом мозг привыкает: subnet mask говорит, какая часть fixed, а wildcard mask говорит, какая часть может изменяться.

## DHCP: Пусть Router Раздает Адреса Сам

DHCP означает Dynamic Host Configuration Protocol. Он автоматически выдает клиентам IP configuration:

- IP address;
- subnet mask;
- default gateway;
- DNS server;
- иногда дополнительные параметры.

Без DHCP каждый PC пришлось бы настраивать вручную. Это медленно, неудобно и почти гарантированно приводит к ошибкам, особенно когда устройств становится больше.

В этом уроке router был настроен как DHCP server для district shop subnet.

## Excluded Addresses

Сначала нужно исключить addresses, которые DHCP не должен выдавать клиентам.

Обычно исключают:

- gateway address;
- addresses для network devices;
- static infrastructure addresses;
- addresses, которые могут понадобиться позже для servers, printers или other fixed devices.

Например, если router interface использует `10.0.18.1`, DHCP не должен выдать этот адрес PC. Иначе получится IP conflict.

## DHCP Pool

После exclusions создается DHCP pool. В нем задается:

- network;
- subnet mask;
- default router;
- DNS server.

Для нашей схемы важные параметры такие:

```text
Network:         10.0.18.0
Mask:            255.255.255.192
Default router:  10.0.18.1
```

Default router - это gateway, через который client выходит за пределы своей local network.

## Проверка На Клиентах

После настройки DHCP PCs были переключены со static addressing на DHCP.

Они получили addresses:

```text
10.0.18.11
10.0.18.12
```

Это хороший знак: clients получили addresses из правильного subnet, а router начал видеть DHCP bindings, связанные с MAC addresses клиентов.

DHCP binding показывает примерно такую связь:

```text
Client MAC address -> Assigned IP address
```

Именно такие моменты полезны в lab practice: ты видишь путь от design к configuration, а потом к proof.

## Что Доказал Этот Урок

Это был не просто урок про замену IP addresses в Packet Tracer. Он показал, что subnetting plan должен быть operational.

То есть ты должен уметь:

- читать `/26` и понимать диапазон;
- переводить `/26` в `255.255.255.192`;
- выбрать gateway address;
- убрать старую конфигурацию;
- обновить NAT под новый subnet;
- посчитать wildcard mask;
- настроить DHCP pool;
- проверить, что clients реально получили правильные addresses.

Subnet plan полезен только тогда, когда его можно применить на router, switches, wireless gear и end devices.

## Практический Вывод

Когда меняется subnet, всегда думай не только про interface IP.

Проверь весь набор зависимостей:

```text
Interface IP
Subnet mask
Routing
NAT ACL
DHCP pool
Excluded addresses
Client configuration
Verification commands
```

Сеть работает устойчиво не потому, что одна команда введена правильно. Она работает устойчиво, когда все связанные части design согласованы между собой.

