# Cisco NAT Terminology

Source: закрытая страница курса  
Date added: 2026-06-09  
Related plan item: Week 6 / Cisco NAT address terminology  
Tags: NAT, inside local, inside global, outside local, outside global, Cisco IOS, address translation
Language: Russian
Translation pair: articles-en/2026-06/week-06/10-cisco-nat-terminology.md

## Summary

Cisco описывает addresses в NAT с помощью двух пар понятий: `inside/outside` и `local/global`. Inside или outside определяет, к какой стороне translation относится host. Local или global описывает, как address представлен с соответствующей точки зрения.

В обычном outbound PAT scenario inside local часто является private address, inside global - public translated address, а outside global - public address internet server. Но local не всегда означает private, а global не всегда буквально означает public: это названия ролей в translation.

## Key Points

- Inside относится к hosts на внутренней стороне NAT.
- Outside относится к hosts на внешней стороне NAT.
- Inside local - address inside host, видимый во внутренней network.
- Inside global - address, представляющий inside host во внешней network.
- Outside global - реальный address outside host во внешней network.
- Outside local - address outside host, представленный во внутренней network.
- В простом internet NAT inside local обычно private, inside global public.
- Outside local и outside global часто совпадают, если outside address не переводится.
- NAT terminology основана на perspective и representation.
- Понимание терминов упрощает чтение `show ip nat translations`.

## Notes

### Why The Terms Matter

NAT configuration и verification используют Cisco terminology.

Без нее строки вроде:

```text
Inside global
Inside local
Outside local
Outside global
```

выглядят как четыре случайных label.

На самом деле они отвечают на два вопроса:

1. Этот host относится к inside или outside?
2. Как его address представлен locally или globally?

### Inside And Outside

`Inside` обычно означает network, которой управляет организация и чьи addresses переводятся.

Примеры NetworkChuck Coffee:

- cafe laptop;
- POS terminal;
- internal server;
- guest client;
- inside interface edge router.

`Outside` означает external network и hosts за NAT boundary:

- internet server;
- cloud API;
- public DNS server;
- ISP side.

Inside/outside описывает сторону и ownership context, а не тип address.

### Local And Global

Точное понимание:

- `local` - address, используемый/видимый в local address domain;
- `global` - address, используемый/видимый в global/external address domain.

Практическое beginner shortcut:

```text
local often looks private
global often looks public
```

Но это не универсальное правило.

Например, организация может использовать public addresses внутри, а outside local может быть не private. Поэтому для точности думай о representation, а не только о RFC 1918/public.

## Inside Local

Inside local - IP address inside host в его внутренней network.

Пример:

```text
192.168.1.50
```

Это address, настроенный на POS terminal или laptop.

В typical IPv4 NAT он private, но определение не требует этого.

```text
Inside local = how the inside host is addressed on the inside.
```

## Inside Global

Inside global - address, который представляет inside host во внешней/global network.

Пример:

```text
216.0.5.2
```

При PAT много inside local addresses могут разделять один inside global address, различаясь port numbers.

```text
192.168.1.50:51000 -> 216.0.5.2:30001
192.168.1.60:52000 -> 216.0.5.2:30002
```

```text
Inside global = how the inside host appears outside.
```

## Outside Global

Outside global - реальный address outside host в global/external network.

Если cafe PC обращается к:

```text
8.8.8.8
```

то `8.8.8.8` обычно является outside global address.

```text
Outside global = how the outside host is addressed on the outside.
```

## Outside Local

Outside local - address, представляющий outside host во внутренней/local network.

В большинстве простых internet PAT scenarios outside address не переводится:

```text
Outside local  = 8.8.8.8
Outside global = 8.8.8.8
```

Они совпадают.

Outside local отличается, когда NAT также изменяет представление outside host для inside network.

Use cases:

- overlapping address spaces после merger;
- legacy device, ожидающий destination в определенном range;
- policy-driven bidirectional NAT;
- network integration during migration.

### Outside Local Example

Реальный outside server:

```text
Outside global: 203.0.113.50
```

Inside users обращаются к alias:

```text
Outside local: 10.200.0.50
```

NAT device переводит:

```text
10.200.0.50 <-> 203.0.113.50
```

Для inside host destination выглядит local-style, хотя реальный host находится outside.

## Typical PAT Conversation

Cafe PC:

```text
Inside local: 192.168.1.50
```

Cafe edge public address:

```text
Inside global: 216.0.5.2
```

Internet server:

```text
Outside local: 8.8.8.8
Outside global: 8.8.8.8
```

Translation:

```text
Inside local 192.168.1.50:51000
-> Inside global 216.0.5.2:30001
-> Outside global 8.8.8.8:53
```

### Table

| Term | Typical Meaning | Example |
| --- | --- | --- |
| Inside local | Inside host address before translation | `192.168.1.50` |
| Inside global | Address representing inside host outside | `216.0.5.2` |
| Outside global | Real external host address | `8.8.8.8` |
| Outside local | External host address as seen inside | `8.8.8.8` or translated alias |

## Reading Cisco NAT Output

Command:

```cisco
show ip nat translations
```

Example:

```text
Pro  Inside global       Inside local        Outside local       Outside global
icmp 216.0.5.2:1         192.168.1.50:1      1.1.1.1:1           1.1.1.1:1
```

Interpretation:

- private inside host is `192.168.1.50`;
- it appears outside as `216.0.5.2`;
- outside host is `1.1.1.1`;
- outside address is not translated, so local/global values match.

## A Better Memory Method

Не запоминай четыре определения независимо.

Для каждого address спроси:

```text
Whose host is it?
How is that host represented from this perspective?
```

Then:

```text
Inside local  = our host, inside representation
Inside global = our host, outside representation
Outside global = their host, outside representation
Outside local  = their host, inside representation
```

## Overlapping Networks

NAT может помочь, если две организации используют одинаковый prefix:

```text
Company A: 10.10.0.0/16
Company B: 10.10.0.0/16
```

При temporary integration одна сторона может быть представлена translated range:

```text
10.200.0.0/16
```

Это позволяет coexistence, пока выполняется long-term renumbering или redesign.

Но такой NAT усложняет:

- troubleshooting;
- logging;
- application dependencies;
- DNS;
- security policy;
- documentation.

Он полезен как migration tool, а не всегда как идеальная permanent architecture.

## Common Mistakes

### Mistake 1: Local Always Means Private

Часто так, но не обязательно.

Local описывает perspective/address domain.

### Mistake 2: Global Means The ISP Owns It

Inside global представляет inside host outside. Address может быть provider-assigned, organization-owned или получен другим способом.

### Mistake 3: Outside Local Is Always Different

В обычном PAT outside local и outside global часто одинаковы.

### Mistake 4: Inside Means The Router Interface

Inside в терминологии описывает hosts/addresses на inside side. Команда `ip nat inside` отдельно маркирует interface role.

## Practical Exercise

Нарисуй:

```text
PC -> NAT Router -> Internet Server
```

Назначь:

```text
PC: 192.168.1.50
Router public: 216.0.5.2
Server: 1.1.1.1
```

Подпиши:

- inside local;
- inside global;
- outside local;
- outside global.

Затем повтори с outside alias, чтобы outside local отличался от outside global.

## Quick Self-Check

### Question 1

Что такое inside local?

Answer:

```text
Address inside host, используемый во внутренней network до translation.
```

### Question 2

Что такое inside global?

Answer:

```text
Address, представляющий inside host во внешней/global network.
```

### Question 3

Почему outside local и outside global часто одинаковы?

Answer:

```text
Потому что обычный outbound NAT не переводит address outside destination.
```

### Question 4

Всегда ли local означает private?

Answer:

```text
Нет. Это удобный common-case shortcut, но термин описывает representation/perspective.
```

### Question 5

Когда outside local может отличаться?

Answer:

```text
Когда outside host представлен inside network через translated alias, например при overlapping networks.
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Inside local | Inside host address in the inside network. |
| Inside global | Address representing the inside host outside. |
| Outside global | Actual outside host address in the outside network. |
| Outside local | Address representing the outside host inside. |
| `ip nat inside` | Marks an interface as the NAT inside side. |
| `ip nat outside` | Marks an interface as the NAT outside side. |
| `show ip nat translations` | Displays translations using Cisco terminology. |
| Address domain | Context in which an address representation is used. |
| Overlapping network | Networks using conflicting address space. |

## What To Review Later

- Static NAT syntax
- Dynamic NAT syntax
- PAT syntax
- Inside/outside interface roles
- NAT order of operations
- Overlapping-network translation
- NAT troubleshooting
