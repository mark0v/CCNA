# Why Spanning Tree Protocol Exists

Source: закрытая страница курса  
Date added: 2026-06-28  
Related plan item: Week 9 / Spanning Tree Protocol foundations  
Tags: STP, Spanning Tree Protocol, switching, redundancy, Layer 2, broadcast storm, CCNA
Language: Russian
Translation pair: articles-en/2026-06/week-09/02-why-spanning-tree-protocol-exists.md

## Кратко

Spanning Tree Protocol, STP, существует из-за простой проблемы: в Layer 2 network redundant links могут создать loop.

А loop на switch network - это не "один пакет пошел не туда". Это потенциальный broadcast storm, когда broadcast frames начинают ходить по кругу, размножаться и забивать сеть до отказа.

Поэтому STP делает две вещи:

- находит dangerous redundant paths;
- блокирует часть paths, чтобы topology оставалась loop-free.

При этом blocked link не пропадает навсегда. Он остается standby path. Если primary link упадет, STP может перестроить topology и вернуть connectivity через запасной путь.

Главная идея:

```text
Redundancy is good.
Layer 2 loops are dangerous.
STP keeps redundancy from destroying the network.
```

## Почему STP Пугает Студентов

STP часто стоит рядом с subnetting в списке тем, которые ломают уверенность у CCNA students.

Причина не в том, что идея невозможная.

Причина в том, что STP быстро уходит в детали:

- bridge ID;
- root bridge election;
- root ports;
- designated ports;
- blocked ports;
- timers;
- port states;
- convergence;
- per-VLAN behavior.

Если начать сразу с этих деталей, тема выглядит как набор странных правил.

Правильнее начинать с why.

STP появился не для экзамена. Он появился потому, что реальные switch networks нуждаются в redundancy, но Layer 2 Ethernet сам по себе не умеет безопасно переживать loops.

## Что Происходит Без STP

Представь два switches, между которыми есть два physical links.

На diagram это выглядит хорошо:

```text
SW1 ===== SW2
```

Один link может быть primary, второй может быть backup.

Но Ethernet frames не имеют TTL, как IP packets. Если Layer 2 frame попал в loop, он не исчезнет сам просто потому, что "прошло слишком много hops".

Особенно опасны broadcast frames.

Broadcast должен быть отправлен всем ports в VLAN, кроме того port, откуда он пришел. Если между switches есть loop, каждый switch может снова и снова пересылать этот broadcast дальше.

Результат:

- broadcast frames circulate endlessly;
- copies multiply;
- switch CPU и bandwidth перегружаются;
- MAC address tables начинают flapping;
- normal traffic перестает проходить;
- users видят "network down", хотя links физически горят.

Это и есть broadcast storm.

## Broadcast Storm На Практике

Broadcast storm редко выглядит красиво.

Обычно симптомы такие:

- сеть внезапно становится очень медленной;
- pings начинают теряться;
- DHCP перестает стабильно отвечать;
- телефоны, кассы, камеры или workstations отваливаются;
- switches показывают высокую загрузку;
- logs заполняются MAC flapping или topology changes;
- отключение одного cable неожиданно "лечит" проблему.

В маленькой lab это может быть просто раздражающим.

В business network это outage.

Если это кафе, перестают работать заказы. Если это склад, могут остановиться scanners. Если это офис, пользователи теряют доступ к services.

STP нужен именно для того, чтобы redundant link не превратился в такой incident.

## Что Делает STP

STP смотрит на switch topology и строит loop-free tree.

Слово "tree" здесь важно.

Дерево в networking sense - это topology без loops. Между двумя точками есть путь, но нет бесконечного круга.

STP выбирает, какие ports будут forwarding, а какие должны быть blocked.

Упрощенно:

```text
Forwarding ports carry traffic.
Blocked ports protect the network from loops.
```

Если active path ломается, STP может пересчитать topology и открыть previously blocked path.

Поэтому STP не уничтожает redundancy. Он переводит часть redundancy в standby.

## Почему Это Не Просто "Выключить Лишний Link"

Можно спросить: если redundant link опасен, почему просто не отключить его?

Потому что redundancy нужна.

Без backup links один failed cable, failed port или failed switch path может отрезать часть сети.

STP позволяет держать физическую redundancy подключенной, но контролируемой.

Разница:

```text
No redundancy:
one failure can break connectivity.

Uncontrolled redundancy:
one loop can break the whole Layer 2 network.

STP-controlled redundancy:
backup path exists, but loops are prevented.
```

Это и делает STP базовой технологией enterprise switching.

## Что STP Отслеживает

На базовом уровне STP обменивается служебными messages между switches. Эти messages называются BPDU, Bridge Protocol Data Units.

Через BPDU switches понимают:

- какие switches есть в topology;
- какой switch должен быть root bridge;
- какие ports дают лучший path к root bridge;
- какие ports должны forward traffic;
- какие ports нужно block, чтобы не было loop.

Пока не нужно запоминать все election rules.

Сейчас важно другое:

```text
STP is not guessing.
Switches exchange information and calculate a safe forwarding topology.
```

Следующие уроки уже разберут, как именно STP принимает эти decisions.

## Где Это Связано С Нашей Сетью

В NetworkChuck Coffee и Fallout Shelter scenarios мы постепенно строим более реалистичную switch infrastructure.

Пока сеть маленькая и links одиночные, STP может казаться второстепенным.

Но как только появляется второй uplink, redundant switch path или более серьезная collapsed core topology, STP становится обязательной темой.

Без STP:

- один extra cable может создать loop;
- один misconfigured port может положить VLAN;
- один "backup link" может стать причиной outage;
- troubleshooting превращается в угадывание.

С STP:

- topology остается loop-free;
- redundant path может ждать как backup;
- blocked port не обязательно означает failure;
- engineer может объяснить, почему traffic идет именно так.

## Не Отключай STP Просто Так

В lab иногда хочется выключить STP, чтобы "link стал зеленым" или "traffic пошел быстрее".

Это опасная привычка.

Если STP заблокировал port, сначала надо понять почему.

Проверь:

- есть ли redundant path;
- какой switch root bridge;
- какой port root/designated/blocked;
- есть ли неожиданный cable;
- нет ли access port, который случайно стал частью loop;
- совпадает ли topology с diagram.

STP block - это не всегда проблема.

Иногда это как раз доказательство, что network protection работает.

## Первые Команды Для Наблюдения

На CCNA level начинай с наблюдения, а не с tuning.

Полезные команды:

```text
show spanning-tree
show spanning-tree vlan 10
show spanning-tree summary
show interfaces status
show mac address-table
```

Что искать:

- root bridge;
- local bridge ID;
- port roles;
- port states;
- forwarding ports;
- blocking ports;
- topology changes;
- MAC address movement.

Пока цель простая: увидеть, что STP реально работает, а не просто выучить определение.

## Главный Вывод

STP нужен не потому, что Cisco хочет усложнить CCNA.

STP нужен потому, что Layer 2 redundancy без контроля может уничтожить сеть.

Он предотвращает switching loops и broadcast storms, блокируя redundant paths там, где это необходимо.

Но blocked path - это не wasted link. Это standby protection, которое может спасти connectivity при failure.

Если коротко:

```text
STP is the safety system that lets switched networks have redundancy without loops.
```

Понимание STP - это разница между человеком, который просто видит blinking lights, и engineer, который понимает, почему сеть работает именно так.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| STP | Spanning Tree Protocol. Protocol that prevents Layer 2 loops in switched networks. |
| Broadcast storm | Network failure where broadcast frames loop and multiply until the network is overloaded. |
| Redundant link | Extra physical path used for backup or resiliency. |
| Loop-free topology | Layer 2 topology where frames cannot circulate endlessly. |
| BPDU | Bridge Protocol Data Unit. STP message exchanged between switches. |
| Root bridge | Central reference switch used by STP to calculate paths. |
| Blocking port | Port that STP prevents from forwarding traffic to avoid a loop. |
| Forwarding port | Port that actively forwards traffic. |

## Questions

### 1. Why does STP exist?

Answer:

STP exists to prevent Layer 2 loops when switched networks have redundant links.

### 2. Why are Layer 2 loops dangerous?

Answer:

Ethernet frames do not have a TTL like IP packets. A broadcast frame can loop repeatedly, multiply, overload the network and cause a broadcast storm.

### 3. Does a blocked STP port always mean something is broken?

Answer:

No. A blocked port may mean STP is correctly preventing a loop while keeping the link available as a standby path.

## What To Review Later

- Root bridge election.
- Root ports and designated ports.
- STP port states.
- STP timers and convergence.
- Rapid Spanning Tree Protocol.
- EtherChannel as an alternative to letting STP block parallel links.
