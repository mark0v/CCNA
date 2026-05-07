# What is TCP/IP and OSI?

Source: закрытая страница курса  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 00 Lesson 03  
Tags: tcp/ip, osi, network models, standards, troubleshooting, layers

## Summary

TCP/IP и OSI - это network models, которые помогают описывать, как устройства обмениваются данными. Их главная ценность в том, что они превращают огромную тему “networking” в понятные layers: physical connection, local delivery, routing, transport и application protocols.

TCP/IP - практическая модель, которую реально используют современные сети. OSI - концептуальная модель, которую инженеры постоянно используют как язык для объяснения и troubleshooting.

## Key Points

- Устройства разных производителей могут общаться благодаря общим standards.
- Ранние сети часто были proprietary, поэтому устройства разных vendors плохо взаимодействовали.
- Packet switching - идея разбивать data на маленькие packets и отправлять их по сети.
- TCP/IP - практический stack, на котором построены современные сети.
- OSI - концептуальная модель из 7 layers, очень полезная для troubleshooting.
- TCP/IP обычно описывают через 5 layers: Physical, Data Link, Network, Transport, Application.
- Switch в основном работает на Data Link layer.
- Router работает на Network layer.
- OSI language помогает быстро определить, где именно сломалась сеть.

## Notes

### Networking Is Built on Agreement

Современная сеть кажется естественной: Raspberry Pi может общаться с iPhone, Windows laptop может открыть сайт на Linux server, а телефоны и серверы понимают друг друга.

Но это не произошло само собой. Раньше vendors создавали свои собственные computers и собственные способы коммуникации. В результате устройства разных производителей могли “говорить на разных языках” и не понимать друг друга.

TCP/IP и OSI появились как ответ на эту проблему. Это models, которые описывают, как communication должна происходить: как data упаковывается, адресуется, передается, принимается и понимается.

### Early Networking and Standards

В 1960-х появилась важная идея: computers могут общаться друг с другом по network. Одним из первых крупных проектов был ARPANET, созданный U.S. Department of Defense.

ARPANET показал, что computers могут отправлять data через network, а не быть isolated islands.

Одна из важных идей ранней сети - packet switching. Вместо передачи данных одним большим куском data разбивается на smaller chunks, packets, и отправляется через network.

Проблема была в том, что разные компании строили свои proprietary networking systems. IBM могла использовать один подход, другие vendors - другой. Без standards сеть оставалась бы набором несовместимых островов.

### Why Standards Matter

Standards нужны, чтобы разные устройства могли вести себя совместимо, даже если они созданы разными производителями.

Без standards:

- vendors создают несовместимые решения;
- devices не могут нормально общаться;
- networks трудно масштабировать;
- troubleshooting становится хаотичным;
- internet в современном виде почти невозможен.

С общими standards network становится предсказуемой: engineers могут понимать, что происходит, независимо от конкретного vendor.

### TCP/IP Is the Model We Actually Use

TCP/IP, или TCP/IP stack, - это practical real-world set of standards, который используют современные devices.

Если phone, server, router или laptop работает в современной сети, почти наверняка он использует TCP/IP.

Для CCNA удобно думать о TCP/IP через 5 layers:

| TCP/IP layer | What it handles |
| --- | --- |
| Physical | Cables, signals, network cards, electrical or wireless transmission |
| Data Link | MAC addresses and local network communication |
| Network | IP addresses and routing between networks |
| Transport | TCP, UDP and port numbers |
| Application | Services and protocols used by applications, such as web traffic |

Эта модель помогает разделить “networking stuff” на понятные stages.

### Devices and TCP/IP Layers

Устройства, которые уже встречались в прошлых статьях, хорошо ложатся на layers:

| Device / concept | Main layer | Why |
| --- | --- | --- |
| Cable / signal | Physical | Передает raw bits через среду |
| Switch | Data Link | Работает с MAC addresses and frames |
| Router | Network | Работает с IP addresses and routing |
| TCP / UDP | Transport | Отвечают за transport behavior and ports |
| Web traffic | Application | Относится к protocols and services for apps |

Модель помогает организовать хаос: вместо одной огромной темы мы видим отдельные функции.

### Why We Still Discuss OSI

OSI stands for Open Systems Interconnection. Это layered model из 7 layers.

OSI не стал практическим стандартом так, как TCP/IP, но он стал главным языком для объяснения и troubleshooting сетей.

OSI layers:

| OSI layer | Name |
| --- | --- |
| Layer 7 | Application |
| Layer 6 | Presentation |
| Layer 5 | Session |
| Layer 4 | Transport |
| Layer 3 | Network |
| Layer 2 | Data Link |
| Layer 1 | Physical |

Network engineers часто говорят:

- “Layer 1 issue” - проблема с physical layer, например cable или signal.
- “Layer 2 issue” - проблема с frames, MAC addresses, switch или VLAN.
- “Layer 3 issue” - проблема с IP addressing или routing.
- “Layer 7 issue” - проблема на application level.

### TCP/IP vs OSI

TCP/IP и OSI описывают похожие идеи, но группируют их немного по-разному.

| TCP/IP | OSI |
| --- | --- |
| Application | Application, Presentation, Session |
| Transport | Transport |
| Network | Network |
| Data Link | Data Link |
| Physical | Physical |

Для Layers 1-4 соответствие довольно понятное. Главное отличие наверху: OSI разделяет Application, Presentation и Session, а TCP/IP чаще объединяет эти функции в Application layer.

### Troubleshooting by Layers

Главная практическая польза моделей - troubleshooting.

Вместо того чтобы говорить “the network is broken”, лучше спросить:

```text
What layer is failing?
```

Примеры:

| Symptom | Possible layer |
| --- | --- |
| Cable unplugged | Layer 1 / Physical |
| Switch cannot forward frames | Layer 2 / Data Link |
| Wrong IP address or no route | Layer 3 / Network |
| TCP/UDP port issue | Layer 4 / Transport |
| App fails while connectivity works | Layer 7 / Application |

Такой подход превращает random problem в structured investigation.

### Example: NetworkChuck Coffee Cannot Process Online Orders

Если NetworkChuck Coffee не может принимать online orders, не стоит сразу обвинять “the network”.

Возможные причины могут быть на разных layers:

- dead cable;
- misconfigured switch port;
- wrong IP address;
- missing default gateway;
- DNS problem;
- application failure.

Network models помогают сузить область поиска и проверять проблему по слоям.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| TCP/IP | Practical network model and protocol stack used by modern networks. |
| OSI | Conceptual 7-layer model used to describe and troubleshoot network communication. |
| Network model | Organized way to describe how communication happens across a network. |
| Standard | Shared rule or specification that allows different systems to work together. |
| Proprietary | Technology controlled by one vendor, often incompatible with other vendors. |
| ARPANET | Early major network project that helped prove networked computer communication. |
| Packet switching | Breaking data into smaller packets and sending them across a network. |
| Physical layer | Layer responsible for cables, signals and transmission media. |
| Data Link layer | Layer responsible for MAC addresses, frames and local delivery. |
| Network layer | Layer responsible for IP addresses and routing between networks. |
| Transport layer | Layer responsible for TCP, UDP and port numbers. |
| Application layer | Layer where application protocols and user-facing services live. |

## Questions

### 1. Почему standards важны для networking?

Standards позволяют устройствам разных vendors общаться друг с другом предсказуемо и совместимо.

### 2. Что такое TCP/IP?

TCP/IP - это practical protocol stack and model, который используют современные сети для communication.

### 3. Что такое OSI?

OSI - это conceptual 7-layer model, который помогает описывать и troubleshoot network communication.

### 4. Почему TCP/IP используют на практике, но OSI всё равно учат?

TCP/IP реально используется устройствами, а OSI дает удобный язык для объяснения, обучения и troubleshooting.

### 5. На каком layer в основном работает switch?

Switch в основном работает на Data Link layer, то есть Layer 2, используя MAC addresses and frames.

### 6. На каком layer работает router?

Router работает на Network layer, то есть Layer 3, используя IP addresses and routing.

### 7. Что такое packet switching?

Packet switching - это подход, при котором data разбивается на небольшие packets, которые затем передаются через network.

### 8. Что означает “Layer 1 issue”?

Это проблема physical layer: cable, signal, port, media или другое физическое соединение.

### 9. Какой главный вопрос полезно задавать при troubleshooting?

“What layer is failing?” Этот вопрос помогает сузить область поиска проблемы.

### 10. В чем главное отличие верхних layers TCP/IP и OSI?

OSI отдельно выделяет Session и Presentation layers, а TCP/IP обычно включает эти функции в Application layer.

## What To Review Later

- TCP/IP 5-layer model.
- OSI 7-layer model.
- Соответствие TCP/IP и OSI layers.
- Почему standards сделали modern networking возможным.
- Как switch, router, cable и application соотносятся с layers.
- Troubleshooting mindset: сначала определить failing layer.
