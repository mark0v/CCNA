# Categories Of Routing Protocols

Source: закрытая страница курса  
Date added: 2026-07-11  
Related plan item: Week 11 / Categories of routing protocols  
Tags: routing protocols, IGP, EGP, distance vector, link state, path vector, OSPF, BGP
Language: Russian
Translation pair: articles-en/2026-07/week-11/01-categories-of-routing-protocols.md

## Summary

- Категории routing protocols важны не только для экзамена, а для понимания поведения сети при сбоях.
- Первый большой раздел: IGP для маршрутизации внутри организации и EGP для маршрутизации между организациями.
- Distance vector protocols учатся через соседей и не держат полную карту сети.
- Link state protocols строят более полную карту topology и обычно быстрее converge.
- Path vector - отдельная категория для BGP, где path information и policy важнее простой "кратчайшей дороги".

## Key Points

- IGP работает внутри одной administrative domain.
- EGP работает между administrative domains; главный пример - BGP.
- Distance vector проще и легче, но может медленнее и менее точно реагировать на изменения.
- Link state требует больше CPU/memory, но дает routers больше visibility.
- BGP нужен там, где важны scale, route control и policy.

## Notes

Категории routing protocols легко воспринимать как сухую экзаменационную классификацию. На практике это способ понять, как протокол будет вести себя под нагрузкой, при failure и во время troubleshooting.

Команды включения routing protocol полезны только до первого сбоя. Когда сеть перестает работать, важнее понимать архитектуру: как protocol learns routes, как он выбирает best path, как быстро он converge и насколько полную картину сети он видит.

В NetworkChuck Coffee это быстро становится практическим вопросом. Если появляются несколько locations, partner networks, ISP handoffs и cloud connections, routing перестает быть "просто таблицей маршрутов". От него зависят card payments, online orders, inventory systems и связь между stores.

## IGP vs EGP

Первый уровень классификации:

| Category | Meaning | Example |
| --- | --- | --- |
| IGP | Interior Gateway Protocol, работает внутри организации. | OSPF, EIGRP, RIP, IS-IS |
| EGP | Exterior Gateway Protocol, работает между организациями. | BGP |

IGP используется внутри вашей сети. Например, NetworkChuck Coffee routing между back office, POS systems, security cameras, warehouse networks и branch cafes - это internal routing. Здесь routers должны обмениваться маршрутами внутри одной controlled environment.

EGP используется между организациями или administrative domains. Главный EGP - BGP, Border Gateway Protocol. Это routing protocol интернета, но он полезен не только internet providers. Если NetworkChuck Coffee подключается к partner network и нужно обмениваться только approved routes, BGP дает нужный control.

Главная мысль: IGP отвечает за внутренние дороги компании, EGP - за контролируемый обмен routes за пределами компании.

## Distance Vector: Routing By Rumor

Distance vector protocols можно представить как routing by rumor. Router не строит полную карту всей network. Он слушает соседей и узнает: "чтобы попасть туда, отправляй traffic через меня".

Преимущество такого подхода - простота и меньшая resource cost. Router не обязан хранить всю topology и делать сложные расчеты. Это может быть полезно в маленьких или ограниченных environments.

Недостаток - limited visibility. Если router видит сеть только через updates от neighbors, изменения могут распространяться постепенно. При сбоях это может давать delayed convergence или странное routing behavior, пока все routers не получат актуальную информацию.

Классические examples:

- RIP;
- EIGRP.

Для troubleshooting важно спрашивать не только "route есть или нет", но и "как она была learned". Если route пришла через distance vector protocol, стоит смотреть neighbor relationships, update timing и возможность incomplete information.

## Link State: Routing By Map

Link state protocols работают иначе. Router получает больше информации о topology и строит более полную картину сети. Вместо "neighbor сказал идти туда" router понимает layout и сам рассчитывает best path.

Главный example для CCNA - OSPF, Open Shortest Path First. Также существует IS-IS, который часто встречается в больших provider или enterprise environments, но в CCNA focus обычно на OSPF.

Преимущества link state:

- routers видят больше network topology;
- changes обычно обрабатываются быстрее;
- convergence часто лучше;
- path calculation более осознанный.

Цена:

- больше CPU usage;
- больше memory usage;
- больше complexity.

Это не магия, а tradeoff. Link state дает better visibility and faster decisions, но требует больше ресурсов и аккуратного design.

## Path Vector: BGP And Policy

BGP выделяют в category path vector. Он не строит полную карту интернета как link state protocol, потому что internet слишком большой. Вместо этого BGP работает с path information и policy.

В BGP важен не только вопрос "куда короче". Часто важнее:

- какие routes принимать;
- какие routes advertising наружу;
- каким external paths доверять;
- какой provider предпочитать;
- какие networks не должны попасть внутрь.

Именно поэтому BGP хорошо подходит для internet routing, partner connections, multi-homing и controlled route exchange between organizations. Он масштабируется не за счет полной карты всего мира, а за счет path attributes and policy.

## Fast Recap

| Concept | Practical meaning |
| --- | --- |
| IGP | Internal routing внутри вашей organization. |
| EGP | External routing между organizations. |
| Distance vector | Легче и проще, learns by neighbor updates. |
| Link state | Видит больше topology, often faster convergence, costs more resources. |
| Path vector | BGP-style routing with path and policy control. |

Главный takeaway: category labels нужны не для заучивания. Они объясняют behavior. Если понять architecture, configuration перестает быть набором случайных команд, а troubleshooting становится логичным.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| IGP | Interior Gateway Protocol, routing внутри одной organization. |
| EGP | Exterior Gateway Protocol, routing между organizations. |
| Distance vector | Protocol type, где routers learn routes через neighbor updates. |
| Link state | Protocol type, где routers build topology knowledge and calculate best paths. |
| Path vector | Protocol type, где decisions основаны на path information and policy. |
| OSPF | Link-state IGP, widely used in enterprise networks. |
| BGP | Path-vector EGP, routing protocol of the internet. |
| Convergence | Процесс, когда routers приходят к актуальному пониманию topology после change. |

## Questions

### 1. В чем разница между IGP и EGP?

Answer: IGP используется для routing внутри одной организации, а EGP - для routing между организациями или administrative domains.

### 2. Почему distance vector называют routing by rumor?

Answer: Router узнает routes от соседей и не держит полную карту topology. Он доверяет neighbor updates и строит forwarding decisions на их основе.

### 3. Чем link state отличается от distance vector?

Answer: Link state protocols дают routers более полную карту topology, поэтому они могут сами рассчитывать best path и часто быстрее реагировать на changes.

### 4. Почему BGP относится к path vector?

Answer: BGP принимает decisions на основе path information и policy, а не просто полной topology map или соседских rumors.

### 5. Почему эта классификация важна для troubleshooting?

Answer: Category объясняет, как route была learned, как protocol реагирует на failure и где искать проблему: в neighbors, topology database, policy или external advertisements.

## What To Review Later

- Какие routing protocols относятся к IGP.
- Почему BGP является главным EGP.
- Разницу между distance vector и link state convergence.
- Основные use cases для OSPF и BGP.
