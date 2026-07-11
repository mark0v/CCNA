# OSPF Troubleshooting: Neighbors And States

Source: закрытая страница курса  
Date added: 2026-07-11  
Related plan item: Week 11 / OSPF troubleshooting neighbors and states  
Tags: OSPF, troubleshooting, neighbor states, DR, BDR, LSDB, LSA, router ID
Language: Russian
Translation pair: articles-en/2026-07/week-11/05-ospf-troubleshooting-neighbors-and-states.md

## Summary

- OSPF troubleshooting начинается с neighbors, а не с routes.
- Если routers не стали neighbors, они не будут exchange routing information.
- Neighbor states показывают, на каком этапе остановился OSPF process.
- `Two-Way` не всегда проблема: на broadcast networks это может быть нормальным для non-DR/BDR peers.
- Хороший troubleshooting - это чтение behavior protocol, а не случайная правка config.

## Key Points

- First command: `show ip ospf neighbor`.
- OSPF compatibility требует same subnet, same area, same timers, matching authentication и matching network type.
- States `Down`, `Init`, `Two-Way`, `Exstart`, `Exchange`, `Loading`, `Full` помогают narrow down failure.
- DR/BDR election нужна на broadcast networks, чтобы не создавать update chaos.
- Router ID должен быть unique; duplicate router IDs ломают OSPF.

## Notes

Memorizing commands помогает только до первого real troubleshooting. В OSPF важно понимать не только команды, а поведение protocol. Если route не появилась, первым вопросом должен быть не "почему route нет?", а "есть ли OSPF neighbor?"

OSPF lives and dies by neighbors. Без neighbor relationship routers не обменяются link-state information, не построят consistent LSDB и не установят learned routes в routing table.

Главная последовательность:

1. Проверить neighbors.
2. Посмотреть neighbor state.
3. Понять, на каком этапе process остановился.
4. Проверить условия, нужные для этого этапа.
5. Исправить конкретный mismatch.

## Neighbor Requirements

Чтобы OSPF routers стали neighbors, они должны совпадать по ключевым параметрам:

| Requirement | Why it matters |
| --- | --- |
| Same subnet | Routers должны быть Layer 3 neighbors на общем segment. |
| Same area | Interface должен быть в same OSPF area. |
| Same hello/dead timers | Routers должны ожидать hellos с одинаковой логикой. |
| Matching authentication | Если auth включена, параметры должны совпадать. |
| Matching network type | Point-to-point, broadcast и другие types влияют на adjacency behavior. |
| Unique router ID | Router ID - identity router-а в OSPF domain. |

Если один из этих параметров не совпадает, adjacency может не сформироваться или stuck in state.

## Neighbor States

OSPF neighbor relationship проходит через states:

| State | Meaning | Troubleshooting focus |
| --- | --- | --- |
| Down | Hellos не получены. | Interface, IP, OSPF enabled, physical/link status. |
| Init | Hello получен, но router еще не видит себя в neighbor hello. | One-way communication, timers, ACLs, multicast reachability. |
| Two-Way | Routers видят друг друга. | Normal on broadcast for non-DR/BDR; иначе проверить next states. |
| Exstart | Routers выбирают master/slave для database exchange. | MTU mismatch часто проявляется здесь. |
| Exchange | Routers обмениваются DBD summaries. | Database exchange problems. |
| Loading | Routers запрашивают missing LSAs. | LSR/LSU exchange, LSDB completion. |
| Full | LSDB synchronized. | Healthy full adjacency. |

Эти states - не trivia. Это troubleshooting roadmap. Если neighbor stuck в `Init`, проблема обычно раньше database exchange. Если stuck в `Exstart`, стоит думать о MTU или negotiation problems. Если `Two-Way` на broadcast network с non-DR/BDR peer - это может быть нормальным.

## Two-Way Is Not Always Bad

На point-to-point links обычно хочется видеть `Full`. Но на broadcast networks OSPF elects DR and BDR:

- DR - designated router;
- BDR - backup designated router.

Идея DR/BDR - не заставлять всех routers формировать full adjacency со всеми. Иначе на shared segment было бы слишком много update relationships.

Поэтому router может быть `Two-Way` с non-DR/BDR peers и `Full` с DR/BDR. Это healthy behavior.

Если помнить только "Full is good", можно ошибочно считать нормальный `Two-Way` problem.

## OSPF Packet Flow

Когда routers стали совместимыми, они обмениваются packets:

| Packet | Role |
| --- | --- |
| Hello | Discover and maintain neighbors. |
| DBD | Database Description, summary of LSDB contents. |
| LSR | Link-State Request, request for missing details. |
| LSU | Link-State Update, carries LSAs and changes. |
| LSAck | Acknowledges received LSAs. |

DBD packet - это summary, не весь LSDB. Router смотрит, чего ему не хватает, запрашивает details через LSR, получает их через LSU и подтверждает через LSAck.

Когда это понятно, debug output перестает быть хаотичным noise. Видно, на каком этапе protocol сейчас находится: hello exchange, summary exchange, loading missing LSAs или full synchronization.

## Commands To Use First

Начинай с neighbor table:

```text
show ip ospf neighbor
```

Потом проверяй process и interfaces:

```text
show ip protocols
show ip ospf interface brief
show ip ospf database
show running-config | section router ospf
show ip route ospf
```

`show ip protocols` показывает active routing protocols, advertised networks и useful process details.

`show ip ospf interface brief` показывает, какие interfaces участвуют в OSPF, в какой area они находятся, и какую роль играют.

`show ip ospf database` показывает LSDB. Это полезно, но обычно не первый command, потому что output может быть большим.

## Clear OSPF Process

Команда:

```text
clear ip ospf process
```

restart OSPF process. Она полезна в lab, например после изменения router ID. Но в production это disruptive: neighbors drop, routes relearn, traffic может кратко пострадать. Использовать только с пониманием impact.

## Router ID And DR/BDR

Router ID - это OSPF identity router-а. Если не настроить manually, Cisco router выбирает:

1. Highest IP на loopback interface.
2. Если loopback нет - highest IP на active physical/logical interface.

Router IDs должны быть unique. Duplicate router ID может привести к strange adjacency и LSDB behavior.

На broadcast networks router ID участвует в DR/BDR election вместе с OSPF priority. На point-to-point links DR/BDR не нужны, потому что на segment только two routers.

## Troubleshooting Method

Правильный pattern:

1. Не менять config сразу.
2. Проверить `show ip ospf neighbor`.
3. Определить state.
4. Проверить requirements для этого state.
5. Подтвердить interface participation.
6. Проверить router ID, area, timers, authentication, network type.
7. Только потом менять config.

Troubleshooting is where book knowledge becomes real skill. Не надо panic-editing. Нужно спокойно читать output и делать минимальные точные изменения.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `show ip ospf neighbor` | Shows OSPF neighbors and their states. |
| `show ip protocols` | Shows running routing protocols and advertised networks. |
| `show ip ospf interface brief` | Shows OSPF-enabled interfaces, areas, and roles. |
| `show ip ospf database` | Shows LSDB contents. |
| `clear ip ospf process` | Restarts OSPF process; disruptive in production. |
| DR | Designated router on broadcast segment. |
| BDR | Backup designated router. |
| Router ID | Unique OSPF identity for a router. |

## Questions

### 1. Почему OSPF troubleshooting начинается с neighbors?

Answer: Без neighbor relationship routers не обменяются OSPF information и не смогут learn routes друг от друга.

### 2. Какие параметры должны совпасть для OSPF adjacency?

Answer: Same subnet, same area, hello/dead timers, authentication, network type и unique router IDs.

### 3. Почему `Two-Way` не всегда bad state?

Answer: На broadcast networks non-DR/BDR routers могут оставаться Two-Way друг с другом, формируя Full adjacency только с DR/BDR.

### 4. Что может означать stuck в `Exstart`?

Answer: Часто это указывает на MTU mismatch или проблему negotiation database exchange.

### 5. Почему `clear ip ospf process` опасна в production?

Answer: Она сбрасывает OSPF process, neighbors drop, routes переизучаются, и это может вызвать temporary outage.

## What To Review Later

- OSPF neighbor state machine.
- DR/BDR election rules.
- OSPF packet types: Hello, DBD, LSR, LSU, LSAck.
- Router ID selection.
- Safe OSPF troubleshooting workflow.
