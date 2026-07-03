# What EtherChannel Actually Does

Source: закрытая страница курса  
Date added: 2026-07-03  
Related plan item: Week 10 / What EtherChannel actually does  
Tags: EtherChannel, LACP, PAgP, LAG, STP, link aggregation, load balancing
Language: Russian
Translation pair: articles-en/2026-07/week-10/03-what-etherchannel-actually-does.md

## Summary

- EtherChannel объединяет несколько физических линков между одними и теми же устройствами в один логический канал.
- Для STP такой bundle выглядит как один путь, поэтому отдельные member links не блокируются как независимые redundant links.
- EtherChannel увеличивает aggregate throughput, но обычно не ускоряет один отдельный flow сверх скорости одного member link.
- Канал можно собрать статически, через PAgP или через LACP; в реальных сетях чаще выбирают LACP.

## Key Points

- EtherChannel - это Cisco-название для link aggregation.
- В industry context часто используется термин LAG, Link Aggregation Group.
- В bundle можно объединять только линки между одной и той же парой устройств.
- Один разговор обычно остается на одном physical link, а разные conversations распределяются между member links.
- Speed, duplex, VLAN settings и trunk/access mode должны совпадать на всех member interfaces.

## Notes

Spanning Tree решает проблему Layer 2 loops, но делает это грубо: видит несколько независимых путей между коммутаторами и блокирует лишние. Безопасно - да. Эффективно - не всегда. Если между двумя switch-ами есть два рабочих uplink-а, хочется использовать оба, а не смотреть на один blocked port.

EtherChannel решает именно эту задачу. Он берет несколько физических interfaces между одной и той же парой устройств и объединяет их в один logical link. Для коммутаторов это уже не набор отдельных loop candidates, а один канал. Для STP это тоже один logical path.

Термины здесь важно развести:

- EtherChannel - Cisco-термин;
- LAG, Link Aggregation Group - более общий industry term;
- port-channel - логический интерфейс, который появляется после объединения физических портов.

Главное правило: member links должны соединять одну и ту же пару устройств. Нельзя взять один порт до Switch B, другой до Switch C и сделать из них один нормальный EtherChannel. Bundle работает потому, что оба конца понимают одну и ту же логическую связь.

Если два порта по 1 Gbps объединены в EtherChannel, общий канал может дать 2 Gbps aggregate bandwidth. Если восемь портов по 10 Gbps объединены в bundle, общая емкость становится 80 Gbps. Но здесь есть важная оговорка: это не значит, что один single flow автоматически станет быстрее одного member link.

EtherChannel обычно распределяет трафик по member links через load balancing algorithm. Алгоритм может смотреть на source/destination MAC, source/destination IP, TCP/UDP ports или их комбинации - зависит от платформы и настроек. Поэтому разговор между Host A и Host B может идти по одному физическому линку, а разговор между Host C и Host D - по другому.

Практический вывод:

- один большой file transfer может остаться ограниченным 1 Gbps на bundle из двух 1 Gbps links;
- много одновременных flows смогут распределиться по нескольким линкам;
- aggregate throughput сети вырастет, даже если каждый отдельный flow не "склеивается" из нескольких кабелей.

Это не packet-level bonding. EtherChannel не режет один поток пакетов на куски и не собирает его обратно на другой стороне. Он распределяет conversations между линками так, чтобы bundle в целом нес больше трафика.

Где это используется:

- switch-to-switch uplinks;
- серверные подключения;
- uplink-и wireless access points;
- storage или video systems, где один интерфейс может стать bottleneck;
- distribution/access design, где нужны и bandwidth, и resilience.

В NetworkChuck Coffee это может быть канал между access switch и distribution switch. Access switch обслуживает POS, Wi-Fi, cameras и back office systems. Один uplink может стать узким местом, а несколько независимых uplink-ов STP заблокирует. EtherChannel позволяет использовать несколько кабелей как один logical uplink.

Есть три способа построить EtherChannel:

| Method | Meaning |
| --- | --- |
| Static | Порты вручную принудительно добавляются в bundle без negotiation. |
| PAgP | Cisco-proprietary negotiation protocol для EtherChannel. |
| LACP | Industry-standard negotiation protocol, который работает между разными vendors. |

Static mode может выглядеть простым, но он опаснее: если одна сторона настроена неправильно, negotiation не остановит ошибку. Поэтому в production обычно предпочтительнее LACP. Он позволяет сторонам договориться о bundle и не поднимать канал корректно, если параметры не совпадают.

Для EtherChannel особенно важна consistency. На member interfaces должны совпадать:

- speed;
- duplex;
- trunk или access mode;
- allowed VLAN list;
- native VLAN;
- negotiation mode;
- общие параметры Layer 2.

Если один порт отличается, bundle может не подняться, уйти в suspended state или вести себя непредсказуемо.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| EtherChannel | Cisco feature для объединения нескольких физических линков в один логический канал. |
| LAG | Link Aggregation Group; общий термин для link aggregation. |
| Port-channel | Логический интерфейс, который представляет EtherChannel bundle. |
| Member link | Физический интерфейс, входящий в EtherChannel. |
| LACP | Стандартный протокол negotiation для link aggregation. |
| PAgP | Cisco-proprietary протокол negotiation для EtherChannel. |
| Aggregate throughput | Общая пропускная способность bundle для множества flows. |

## Questions

### 1. Почему EtherChannel помогает STP?

Answer: Он превращает несколько физических линков в один logical link. STP видит один путь, а не несколько отдельных redundant paths, которые нужно блокировать.

### 2. Можно ли объединить в EtherChannel порты, которые идут к разным коммутаторам?

Answer: Нет, в обычном EtherChannel member links должны соединять одну и ту же пару устройств. Иначе это не один логический канал между двумя endpoints.

### 3. Даст ли EtherChannel из двух 1 Gbps линков скорость 2 Gbps для одного file transfer?

Answer: Обычно нет. Один flow чаще всего остается на одном member link. EtherChannel увеличивает aggregate throughput для множества одновременных flows.

### 4. Почему LACP обычно лучше static EtherChannel?

Answer: LACP выполняет negotiation и помогает не поднять bundle при несовпадающих настройках. Static mode не проверяет договоренность сторон так надежно.

## What To Review Later

- Какие load balancing algorithms доступны на конкретной Cisco platform.
- Разницу между `channel-group` и `interface port-channel`.
- Режимы LACP: active и passive.
- Режимы PAgP: desirable и auto.
