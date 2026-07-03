# Why Routing Protocols Exist

Source: закрытая страница курса  
Date added: 2026-07-03  
Related plan item: Week 10 / Why routing protocols exist  
Tags: dynamic routing, static routing, OSPF, BGP, EIGRP, RIP, convergence, scalability
Language: Russian
Translation pair: articles-en/2026-07/week-10/09-why-routing-protocols-exist.md

## Summary

- Routing protocols существуют не потому, что static routes "плохие", а потому что сети меняются.
- Static routing хорошо работает в простых сетях, но плохо адаптируется к отказам и росту.
- Dynamic routing дает две ключевые вещи: adaptability и scalability.
- Routers обмениваются routing information, формируют neighbor relationships и сходятся к актуальной topology.
- OSPF, EIGRP, BGP и RIP решают routing-задачи по-разному, но общая цель одна: убрать постоянное ручное сопровождение routes.

## Key Points

- Static route может выглядеть активной, даже если фактический path за next hop уже не работает.
- Dynamic routing protocols используют hello messages и neighbor relationships, чтобы отслеживать доступность paths.
- Convergence означает, что routers обновили свое понимание topology после изменения.
- Scalability означает, что сеть может расти без ручной настройки каждой route на каждом router.
- BGP важен как routing protocol интернета, но его поведение намеренно более осторожное и медленное.

## Notes

Routing protocols нужны не как "продвинутая версия" static routing. Они нужны потому, что реальные сети растут, ломаются и меняются. Static route хорош, когда topology простая и предсказуемая. Но как только появляются несколько locations, backup links, WAN circuits и remote networks, ручное управление routes становится слабым местом.

В NetworkChuck Coffee это выглядит так: один site должен достучаться до server в другом site. При static routing engineer вручную добавляет route на одном router, потом на другом, потом на следующем. В маленькой сети это терпимо. В сети с десятками coffee shops и backup paths это быстро превращается в operational burden.

Главная проблема static routes - rigid behavior. Router знает только то, что ему ввели. Если local interface физически упал, router обычно может убрать связанную route из routing table. Но если проблема дальше по пути - например в carrier network, VPN path или промежуточном сегменте - interface может оставаться up, а traffic уже не проходит.

Это важная разница:

> Route, которая выглядит alive, не всегда является working path.

Dynamic routing protocols помогают закрыть этот gap. Routers отправляют hello messages соседям, формируют neighbor relationships и отслеживают, кто доступен. Если protocol перестает получать expected communication, router понимает, что path больше нельзя считать рабочим, и начинает recalculation.

Первое большое преимущество dynamic routing - adaptability.

Когда link или path fails, routers могут:

- удалить bad route;
- выбрать alternative path;
- перестать отправлять traffic в dead direction;
- вернуть route после восстановления connectivity;
- сделать это без ручной правки на каждом router.

Второе большое преимущество - scalability.

Static routing плохо масштабируется, потому что каждый новый network segment часто требует новых manual entries. Чем больше routers и sites, тем больше мест, где можно ошибиться. Dynamic routing меняет модель: routers advertise connected networks, learn remote networks и выбирают best paths на основе protocol logic.

В этом смысле dynamic routing - это не просто удобство. Это способ не стать человеком, который вручную поддерживает routing table для всего бизнеса.

После включения routing protocol routers начинают обмениваться информацией. Например, в OSPF routers формируют соседства и делятся тем, какие networks они знают. Когда все routers получили актуальную информацию и рассчитали paths, network converged. Convergence - это момент, когда routing domain снова имеет согласованное понимание topology.

Короткая карта протоколов:

| Protocol | Role |
| --- | --- |
| OSPF | Распространенный link-state protocol для enterprise networks. |
| EIGRP | Cisco-oriented protocol, исторически часто встречался в Cisco-средах. |
| BGP | Routing protocol интернета и больших межсетевых routing designs. |
| RIP | Старый protocol, полезен для понимания истории и labs, но редко выбирается для modern production. |

BGP стоит упомянуть отдельно. Он управляет routing между огромными networks в интернете. Поэтому он не пытается реагировать мгновенно на каждое колебание route. В глобальном масштабе слишком быстрая реакция на каждый flap может создать нестабильность. BGP intentionally conservative: он использует timers и policy-driven behavior, чтобы routing был управляемым на масштабе интернета.

Для CCNA сейчас важнее зафиксировать базовую мысль: routing protocols дают adaptability и scalability. Они позволяют network реагировать на failures и расти без бесконечного ручного добавления routes.

Static routes все еще нужны:

- для маленьких predictable networks;
- для default route к ISP;
- для isolated или edge cases;
- когда нужен строгий manual control.

Но если есть redundancy, multiple sites, WAN complexity или growth plan, dynamic routing уже не выглядит "лишней сложностью". Это нормальный design tool.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Routing protocol | Protocol, который routers используют для exchange routing information. |
| Hello message | Control message, которым routers проверяют соседей и поддерживают adjacency. |
| Neighbor relationship | Состояние, когда routers распознали друг друга и могут обмениваться routing data. |
| Convergence | Процесс, когда routers обновляют routes после изменения topology. |
| Adaptability | Способность routing автоматически реагировать на failures и changes. |
| Scalability | Способность routing design расти без непропорционального ручного труда. |
| Routing table | Таблица известных routes, по которой router выбирает forwarding path. |
| Route flap | Ситуация, когда route быстро появляется и пропадает. |

## Questions

### 1. Почему routing protocols вообще нужны?

Answer: Они позволяют routers автоматически learn routes, exchange topology information и реагировать на network changes без ручной правки каждой route.

### 2. Почему static route может быть опасной при partial failure?

Answer: Local interface может оставаться up, хотя реальный path дальше по сети уже не работает. Static route продолжит выглядеть usable, пока router не получит другую причину убрать ее.

### 3. Что дают hello messages?

Answer: Они помогают routers проверять доступность соседей. Если expected hellos пропадают, routing protocol может считать path недоступным и пересчитать routes.

### 4. Что такое convergence?

Answer: Это процесс, в котором routers приходят к обновленному и согласованному пониманию network topology после изменения.

### 5. Почему BGP не обязан быть быстрым?

Answer: BGP работает на масштабе интернета. Слишком быстрая реакция на каждое колебание routes могла бы создать нестабильность, поэтому BGP действует более осторожно.

## What To Review Later

- Разницу между static и dynamic routing.
- Что такое OSPF neighbor relationship.
- Как routing protocols выбирают best path.
- Почему convergence time важен для uptime.
- Чем отличаются OSPF, EIGRP, BGP и RIP.
