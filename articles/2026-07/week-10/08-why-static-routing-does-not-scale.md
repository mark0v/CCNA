# Why Static Routing Does Not Scale

Source: закрытая страница курса  
Date added: 2026-07-03  
Related plan item: Week 10 / Why static routing does not scale  
Tags: static routing, dynamic routing, OSPF, routing protocols, resiliency, scalability
Language: Russian
Translation pair: articles-en/2026-07/week-10/08-why-static-routing-does-not-scale.md

## Summary

- Static routing полезен в маленьких и предсказуемых сетях.
- Его слабое место - отсутствие автоматической реакции на изменения.
- Чем больше sites, links и backup paths, тем тяжелее поддерживать routes вручную.
- Dynamic routing protocols позволяют routers обмениваться routes и адаптироваться к failures.
- Следующий большой шаг после static routing - понимание routing protocols, особенно OSPF.

## Key Points

- Static route делает ровно то, что настроил engineer, даже если выбранный path уже не работает.
- В растущей сети ручное сопровождение routes быстро становится operational burden.
- Dynamic routing дает scalability и resiliency.
- Routers могут автоматически learn, advertise и withdraw routes.
- OSPF важен потому, что это один из самых распространенных dynamic routing protocols в enterprise networks.

## Notes

Static routing хорош тем, что он простой и предсказуемый. Engineer явно говорит router-у: "чтобы попасть в эту network, иди через этот next hop". В маленькой лаборатории или небольшой сети это удобно. Конфигурация прозрачная, поведение легко объяснить, лишней автоматики нет.

Проблема начинается, когда сеть перестает быть маленькой.

Static routes не думают и не адаптируются. Если link упал, route сам по себе не перестроится. Router продолжит пытаться отправлять traffic в сторону, которую ему указали вручную. С точки зрения router-а команда все еще существует, значит path все еще считается правильным, если только interface или next-hop condition явно не делает route недоступным.

Для NetworkChuck Coffee это быстро становится реальной проблемой. Пока есть один cafe и один router, static routing может быть нормальным. Но если появляются central office, Fallout Shelter, branch cafes, backup WAN links и новые IP ranges, количество ручных routes начинает расти. Каждая новая location означает новые entries. Каждое изменение topology означает ручную правку. Каждый failure может стать ночным troubleshooting call.

Static routing начинает ломаться не потому, что он "плохой". Он ломается потому, что не масштабируется вместе с ростом сети.

Типичные проблемы:

- routes нужно добавлять на каждом relevant router вручную;
- backup paths требуют дополнительной настройки и контроля;
- изменения IP plan создают риск забытых routes;
- при failure network не всегда выбирает alternative path автоматически;
- troubleshooting зависит от того, насколько точно была поддержана документация.

С dynamic routing подход меняется. Router-ы больше не ждут, пока engineer вручную нарисует каждую дорогу. Они обмениваются routing information, узнают доступные networks и пересчитывают paths, когда topology меняется.

Идея простая:

> Static routing - это карта, которую engineer рисует вручную. Dynamic routing - это карта, которую routers обновляют сами, когда дороги закрываются или появляются новые.

Dynamic routing protocols дают две главные вещи:

| Benefit | Meaning |
| --- | --- |
| Resiliency | Если один path fails, routers могут выбрать другой доступный path. |
| Scalability | Сеть может расти без ручного добавления каждой route на каждом router. |

Это не просто удобство. В production это часто вопрос выживания сети. Если у NetworkChuck Coffee десятки locations и один WAN link падает, бизнес не должен ждать, пока engineer вручную перепишет routes. Payment systems, inventory sync, voice, cameras и internal services должны продолжать работать через backup path, если он есть.

Dynamic routing protocols решают это через route learning, route advertisement и convergence. Они позволяют routers:

- узнавать networks от соседей;
- advertising свои connected networks;
- выбирать лучший path по metric;
- удалять или менять routes при failure;
- восстанавливать connectivity без ручного вмешательства в каждую route.

Это не значит, что static routing исчезает. Он все еще полезен:

- для маленьких networks;
- для default routes;
- для edge cases;
- для routes, где нужен strict manual control;
- для simple lab или isolated сегментов.

Но когда появляется redundancy, growth и uptime requirements, static-only design становится слабым местом. В этот момент нужно переходить к dynamic routing.

Дальше начинается мир routing protocols. В CCNA важно понимать, зачем они существуют, чем отличаются и почему OSPF занимает такое заметное место. OSPF, Open Shortest Path First, широко используется в enterprise networks и позволяет routers делать большую часть routing work автоматически.

Главный takeaway: static routing - хороший инструмент, но не универсальная стратегия. Он дает control, но плохо переживает scale and change. Dynamic routing нужен там, где сеть должна расти, реагировать и оставаться доступной без постоянной ручной правки route table.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| Static route | Route, которую engineer настраивает вручную. |
| Dynamic routing | Подход, при котором routers автоматически обмениваются routing information. |
| Routing protocol | Protocol, который routers используют для learning и advertising routes. |
| Convergence | Процесс, когда routers приходят к актуальному общему пониманию topology после изменения. |
| Resiliency | Способность сети продолжать работу при failure. |
| Scalability | Способность сети расти без непропорционального роста ручной работы. |
| OSPF | Open Shortest Path First, распространенный link-state dynamic routing protocol. |

## Questions

### 1. Почему static routing удобен в маленьких сетях?

Answer: Он простой, предсказуемый и дает engineer-у полный manual control над path selection.

### 2. В чем главный недостаток static routing?

Answer: Static routes не адаптируются сами к changes и failures. Если topology изменилась, engineer должен обновить configuration вручную.

### 3. Почему static routing плохо масштабируется?

Answer: Чем больше routers, sites и networks, тем больше routes нужно создавать, поддерживать и проверять вручную.

### 4. Что дает dynamic routing?

Answer: Routers могут learn routes друг от друга, пересчитывать paths при изменениях и использовать backup paths без ручной правки каждой route.

### 5. Почему OSPF важен для CCNA?

Answer: OSPF - один из самых распространенных enterprise dynamic routing protocols, и он показывает, как routers могут строить scalable and resilient routing design.

## What To Review Later

- Когда static routes все еще уместны.
- Разницу между static routing и dynamic routing.
- Что такое convergence.
- Какие routing protocols встречаются в CCNA.
- Почему OSPF называется link-state protocol.
