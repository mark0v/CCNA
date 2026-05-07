# REAL LIFE Example!! (TCP/IP and OSI Layers)

Source: закрытая страница курса  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 00 Lesson 04  
Tags: tcp/ip, osi, encapsulation, de-encapsulation, frame, packet, segment, https

## Summary

Эта статья показывает TCP/IP и OSI layers в движении: Johnny открывает сайт NetworkChuck Coffee, а данные проходят через application, transport, network, data link и physical layers. Каждый layer добавляет свою информацию, этот процесс называется encapsulation. На стороне получателя данные распаковываются обратно, это de-encapsulation.

Главная мысль статьи: устройства в середине пути не обязаны понимать весь запрос целиком. Switch смотрит на MAC address, router смотрит на IP address, а server как конечная точка распаковывает всё до application layer.

## Key Points

- Network models становятся понятнее, когда мы смотрим на движение traffic по layers.
- Application layer начинает user-facing network services, например HTTPS request из browser.
- Transport layer выбирает способ доставки: TCP или UDP.
- HTTPS обычно использует TCP port `443`.
- Encapsulation - процесс оборачивания данных headers/trailers при движении вниз по stack.
- На transport layer данные становятся segment.
- На network layer добавляются IP addresses, и это packet.
- На data link layer добавляются MAC addresses, и это frame.
- Switch принимает решения по Layer 2 и destination MAC address.
- Router снимает старую Layer 2 обертку, смотрит на Layer 3 IP packet и создает новый frame для следующего hop.
- IP addresses остаются end-to-end, а MAC addresses меняются hop-by-hop.
- Destination server de-encapsulates data до application layer и затем строит response.

## Notes

### Why Layers Start Making Sense Here

OSI и TCP/IP models легко заучить как список названий, но настоящая польза появляется, когда видно движение данных.

Johnny открывает сайт NetworkChuck Coffee. Для пользователя это один click в browser, но внутри network происходит цепочка процессов:

1. Browser создает request.
2. Transport layer выбирает delivery behavior.
3. Network layer добавляет IP addressing.
4. Data Link layer добавляет local MAC addressing.
5. Physical layer передает bits через cable или wireless medium.

Каждый layer делает свою работу и передает данные дальше.

### Application Layer

Application layer - это место, где начинается user-facing network service.

В примере Johnny вводит website в browser. Browser формирует request к web server. Protocol здесь - HTTPS, secure version of HTTP.

Важно: application layer не означает само приложение как программу целиком. В контексте модели это network service/protocol, через который приложение общается по сети.

Пример:

| User action | Application protocol |
| --- | --- |
| Open secure website | HTTPS |
| Open regular website | HTTP |

### Transport Layer

Transport layer решает, как данные будут доставляться. Обычно здесь выбирается TCP или UDP.

| Protocol | Main idea |
| --- | --- |
| TCP | Reliable delivery, checks that data arrives correctly |
| UDP | Faster, less overhead, no same reliability guarantees |

Для HTTPS используется TCP. Также появляется port number:

```text
HTTPS = TCP port 443
```

Port number помогает destination понять, какому service предназначен traffic.

Когда transport layer добавляет свой header, данные называются segment.

### Encapsulation

Encapsulation - это процесс, при котором каждый layer добавляет свою служебную информацию перед передачей данных следующему layer.

Удобная аналогия: message кладется в envelope, затем этот envelope кладется в следующий envelope, и так дальше.

Общая последовательность:

| Step | Layer | Adds | Result |
| --- | --- | --- | --- |
| 1 | Application | Application data | Data |
| 2 | Transport | TCP/UDP header, ports | Segment |
| 3 | Network | IP header, source/destination IP | Packet |
| 4 | Data Link | MAC header and trailer | Frame |
| 5 | Physical | Signals/bits | Transmission |

Это один из самых важных процессов в networking.

### Network Layer

Network layer - это Layer 3. Здесь находятся IP addresses и routing.

На этом layer данные получают:

- source IP address;
- destination IP address.

После добавления Layer 3 header данные называются packet.

IP address отвечает за end-to-end delivery: от исходного устройства до конечного destination.

### Data Link Layer

Data Link layer - это Layer 2. Здесь находятся MAC addresses и local delivery.

На этом layer packet оборачивается в frame. Frame содержит:

- source MAC address;
- destination MAC address;
- trailer для Layer 2 checks.

MAC address нужен не для всего пути целиком, а для доставки на текущем local network segment.

Практическое правило:

```text
End-to-end delivery = IP / Layer 3
Hop-by-hop local delivery = MAC / Layer 2
```

### Switch Visibility

Когда frame приходит на switch, switch не изучает весь web request.

Switch не интересуют:

- HTTPS;
- TCP;
- destination website;
- application data.

Switch смотрит на Layer 2:

1. Проверяет destination MAC address.
2. Смотрит MAC address table.
3. Отправляет frame out the correct port.

Switch делает только свою работу: local delivery на Layer 2.

### Router Visibility

Router работает иначе. Когда frame приходит на router, router видит, что Layer 2 destination MAC address указывает на него.

Дальше router:

1. Снимает старую Layer 2 обертку.
2. Смотрит внутрь на Layer 3 packet.
3. Проверяет destination IP address.
4. Смотрит routing table.
5. Выбирает next hop или outgoing interface.
6. Создает новый Layer 2 frame для следующего segment.

Router не пересылает старый frame как есть, потому что старые MAC addresses были valid только для предыдущего hop.

### What Stays the Same and What Changes

Самый важный момент:

```text
IP addresses stay the same end-to-end.
MAC addresses change hop-by-hop.
```

Пример:

| Path segment | Source MAC | Destination MAC | Source IP | Destination IP |
| --- | --- | --- | --- | --- |
| Johnny -> Router | Johnny MAC | Router MAC | Johnny IP | Server IP |
| Router -> Next network | Router MAC | Next-hop/server MAC | Johnny IP | Server IP |

Layer 3 packet продолжает указывать на конечный server. Layer 2 frame каждый раз создается заново для local delivery на текущем участке пути.

### De-Encapsulation on the Server

Когда frame доходит до NetworkChuck Coffee server, server начинает de-encapsulation.

Он проверяет данные layer by layer:

1. Layer 2: destination MAC address мой?
2. Layer 3: destination IP address мой?
3. Layer 4: TCP port `443`, значит это secure web service.
4. Application layer: request к website.

После этого server понимает, что Johnny хочет загрузить homepage, строит response, и процесс повторяется в обратном направлении.

### Why Middle Devices Do Not Need the Whole Story

Каждое устройство обрабатывает только ту часть traffic, которая относится к его layer:

| Device | What it cares about |
| --- | --- |
| Switch | Destination MAC address |
| Router | Destination IP address |
| Server | Full stack up to application request |

Это делает network scalable. Устройство не должно понимать всё, чтобы выполнить свою роль.

### Quiz Mindset

В статье упоминается, что quiz questions были не только на memorization. Их цель - заставить думать, какой layer или protocol отвечает за конкретную функцию.

Хороший exam/troubleshooting вопрос:

```text
Which layer is responsible for this job?
```

Так проще исключать неправильные варианты и находить источник проблемы.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Encapsulation | Оборачивание data headers/trailers при движении вниз по network stack. |
| De-encapsulation | Распаковка data при движении вверх по stack на destination. |
| HTTPS | Secure web protocol, usually uses TCP port 443. |
| TCP | Reliable transport protocol. |
| UDP | Faster transport protocol without TCP-style reliability. |
| Port number | Number that identifies destination service at transport layer. |
| Segment | Data unit at transport layer. |
| Packet | Data unit at network layer with IP addressing. |
| Frame | Data unit at data link layer with MAC addressing. |
| MAC address | Local Layer 2 address used hop-by-hop. |
| IP address | Layer 3 address used for end-to-end delivery. |
| Routing table | Router's map for choosing where to send packets next. |

## Questions

### 1. Что такое encapsulation?

Encapsulation - это процесс, при котором каждый layer добавляет свою служебную информацию к данным перед передачей вниз по stack.

### 2. Как называется единица данных на transport layer?

На transport layer данные называются segment.

### 3. Как называется единица данных на network layer?

На network layer данные называются packet.

### 4. Как называется единица данных на data link layer?

На data link layer данные называются frame.

### 5. Какой protocol и port обычно используются для HTTPS?

HTTPS обычно использует TCP port `443`.

### 6. На что смотрит switch при пересылке traffic?

Switch смотрит на Layer 2 destination MAC address и использует MAC address table.

### 7. На что смотрит router при пересылке traffic между networks?

Router смотрит на Layer 3 destination IP address и использует routing table.

### 8. Что происходит с Layer 2 frame на router?

Router снимает старый Layer 2 frame, анализирует IP packet и создает новый frame для следующего network segment.

### 9. Что остается одинаковым end-to-end: IP addresses или MAC addresses?

IP addresses остаются одинаковыми end-to-end.

### 10. Что меняется hop-by-hop?

MAC addresses и Layer 2 frame меняются hop-by-hop.

### 11. Почему server распаковывает данные глубже, чем switch или router?

Потому что server является final destination и должен передать request до application layer, чтобы web service понял запрос.

### 12. Какой вопрос полезно задавать на экзамене и при troubleshooting?

“Which layer is responsible for this job?” Это помогает понять, какой protocol или device должен выполнять нужную функцию.

## What To Review Later

- Encapsulation and de-encapsulation.
- Порядок PDU names: data, segment, packet, frame, bits/signals.
- HTTPS = TCP port `443`.
- Switch visibility vs router visibility.
- IP stays end-to-end, MAC changes hop-by-hop.
- Difference between end-to-end delivery and local hop-by-hop delivery.
