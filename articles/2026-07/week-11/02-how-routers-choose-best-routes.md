# How Routers Choose Best Routes

Source: закрытая страница курса  
Date added: 2026-07-11  
Related plan item: Week 11 / How routers choose best routes  
Tags: routing table, administrative distance, metric, static routes, OSPF, RIP, floating static
Language: Russian
Translation pair: articles-en/2026-07/week-11/02-how-routers-choose-best-routes.md

## Summary

- Routing table показывает не все, что router знает, а только winning routes.
- Router выбирает route по трем главным шагам: specificity, administrative distance, metric.
- Default route используется только когда нет более specific route.
- Administrative distance показывает, насколько router доверяет source of route.
- Metric используется как tie-breaker внутри одного routing protocol.

## Key Points

- More specific route всегда выигрывает у менее specific route.
- Directly connected route имеет AD 0, static route - AD 1, OSPF - AD 110, RIP - AD 120.
- Floating static route - это static route с повышенной administrative distance для backup-сценариев.
- Если routes пришли из одного protocol, router выбирает по metric.
- RIP использует hop count, OSPF использует cost, EIGRP использует composite metric.

## Notes

Router не просто "знает лучший путь". Он получает routing information из разных sources, сравнивает варианты и устанавливает в routing table только победителей. Поэтому routing table - это не весь brain router-а, а текущий final answer.

Router может знать backup paths, alternate paths и routes из разных protocols, но активная routing table содержит только те routes, которые выиграли selection process. Если текущий winner исчезает, другой route может занять его место.

Главная мысль:

> Routing table - это не все, что router знает. Это список routes, которые выиграли спор.

## Step 1: Specificity

Первый decision point - specificity. Чем длиннее prefix, тем route specific. More specific route wins.

Пример:

| Route | Meaning |
| --- | --- |
| `10.10.10.0/24` | Менее specific route. |
| `10.10.10.128/25` | Более specific route. |
| `0.0.0.0/0` | Default route, least specific. |

Если packet идет к `10.10.10.140`, route `/25` выиграет у `/24`, потому что он точнее описывает destination. Default route используется только если нет ничего более specific.

Это объясняет, почему default route не забирает весь traffic. Она не "главная". Она последняя fallback option: "если ничего другого не подошло, отправь сюда".

## Step 2: Administrative Distance

Если specificity одинаковая, router смотрит на administrative distance. Это trust level источника route. Lower AD wins.

Важные значения:

| Source | Administrative Distance |
| --- | --- |
| Directly connected | 0 |
| Static route | 1 |
| OSPF | 110 |
| RIP | 120 |

Если router learns same prefix from OSPF and RIP, он выберет OSPF, потому что 110 лучше, чем 120. Если есть static route к тому же prefix, static route выиграет у OSPF, потому что 1 лучше, чем 110.

Это делает static routes мощными и опасными. Router почти полностью доверяет manual configuration. Если static route настроена неправильно, она может silently override хороший dynamic route и увести traffic не туда.

## Floating Static Routes

Floating static route - это static route с intentionally worse administrative distance. Она нужна как backup path.

Например, main route приходит через OSPF с AD 110. Мы хотим static backup через LTE/5G, но только если OSPF route исчезнет. Тогда static route получает AD выше 110:

```text
ip route 10.50.0.0 255.255.0.0 192.0.2.2 121
```

Теперь static route не конкурирует с OSPF, пока OSPF route available. Но если OSPF route исчезнет, floating static может войти в routing table.

Практический use case для NetworkChuck Coffee: основной WAN link несет traffic между sites, а cellular backup должен включаться только при failure. Floating static позволяет держать backup route в reserve без постоянного использования expensive link.

## Step 3: Metric

Если specificity и administrative distance tied, router смотрит на metric. Metric работает внутри одного protocol.

Например, две OSPF routes к одному prefix имеют одинаковую specificity и одинаковую AD 110. Тогда OSPF выбирает route с lower cost.

Разные protocols считают metric differently:

| Protocol | Metric |
| --- | --- |
| RIP | Hop count. |
| OSPF | Cost, usually based on bandwidth. |
| EIGRP | Composite metric, including bandwidth and other factors. |

RIP смотрит на количество routers до destination. Он не понимает качество links так гибко, как более современные protocols. OSPF использует cost: faster links обычно получают lower cost, а lower cost wins. EIGRP использует composite metric, где несколько факторов превращаются в одно значение.

Главное правило: внутри protocol lower metric usually wins.

## Full Selection Order

Router выбирает route так:

1. More specific prefix wins.
2. If equal, lower administrative distance wins.
3. If equal, lower metric wins.

Когда это понятно, `show ip route` перестает быть загадкой. Можно посмотреть на competing routes и объяснить, почему именно одна route оказалась installed.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Routing table | Active list of best routes installed by the router. |
| Specificity | Насколько точно route описывает destination network; longer prefix wins. |
| Default route | Least specific route, `0.0.0.0/0`, used only when no better match exists. |
| Administrative distance | Trust value for route source; lower is better. |
| Metric | Protocol-specific path quality value; lower usually wins. |
| Floating static | Static route with increased AD used as backup. |
| `show ip route` | Command that displays installed routes. |

## Questions

### 1. Почему routing table не показывает все possible routes?

Answer: Потому что routing table содержит installed winners. Router может знать alternate routes, но показывает только active best routes.

### 2. Почему default route не выигрывает у specific route?

Answer: Default route `0.0.0.0/0` является least specific. Любая более точная route к destination wins.

### 3. Что означает administrative distance?

Answer: Это trust value источника route. Lower value означает, что router больше доверяет этому source.

### 4. Зачем нужна floating static route?

Answer: Чтобы использовать static route как backup. Ей дают higher AD, чтобы она не выигрывала у primary dynamic route, пока primary route доступна.

### 5. Когда используется metric?

Answer: Когда competing routes имеют одинаковую specificity и administrative distance, обычно потому что они пришли из одного protocol.

## What To Review Later

- Значения administrative distance для common route sources.
- Как OSPF рассчитывает cost.
- Почему static routes могут override dynamic routes.
- Как читать competing routes в `show ip route`.
