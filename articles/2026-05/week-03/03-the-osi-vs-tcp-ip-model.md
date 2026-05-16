# The OSI vs TCP/IP Model

Source: закрытая страница курса  
Date added: 2026-05-16  
Related plan item: Week 3 / OSI and TCP/IP models  
Tags: osi, tcp/ip, layers, troubleshooting, interoperability, network models
Language: Russian
Translation pair: articles-en/2026-05/week-03/03-the-osi-vs-tcp-ip-model.md

## Summary

OSI model и TCP/IP model описывают, как работает network communication. OSI делит процесс на семь layers, а TCP/IP - на четыре. При этом в реальной сети чаще работают TCP/IP protocols, но engineers обычно используют OSI vocabulary, чтобы обсуждать troubleshooting, design и поведение сети.

Главная идея: OSI - это не просто таблица для экзамена. Это язык, по которому engineers быстро говорят о проблемах: Layer 1 для physical issues, Layer 2 для switching/MAC/frame problems, Layer 3 для IP/routing/addressing, Layer 4 для transport behavior.

## Key Points

- OSI and TCP/IP both describe network communication.
- OSI has seven layers.
- TCP/IP is usually shown with four layers in the modern model.
- TCP/IP is what the internet actually uses.
- OSI is the model engineers commonly use to describe and troubleshoot TCP/IP networks.
- OSI vocabulary gives engineers a common language.
- Layered thinking helps isolate problems instead of guessing.
- Interoperability depends on vendors following shared layer standards.
- IEEE 802.11 is an example of a Layer 2 wireless standard.
- The top three OSI layers map mostly into the TCP/IP Application layer.
- The bottom four OSI layers are where network engineers spend most of their time.
- Modern TCP/IP aligns closely with OSI Layers 1-4.

## Notes

### Почему мы учим OSI

Многие новички думают, что OSI model нужна только для экзамена: выучить layers, сдать тест и забыть.

На практике OSI постоянно используется в network engineering.

Когда сеть ломается, engineer часто думает слоями:

```text
Is the cable connected?
Is switching working?
Is IP addressing correct?
Is routing working?
Is TCP/UDP behavior normal?
```

Это и есть layered troubleshooting.

### Две модели, одна задача

OSI model и TCP/IP model делают похожую работу: они описывают, как происходит network communication.

Важно:

- модель не является самой сетью;
- модель объясняет поведение сети;
- модель помогает говорить о процессе передачи данных.

Главное различие:

```text
OSI model: 7 layers
TCP/IP model: 4 layers
```

### Почему есть две модели

TCP/IP стал фактической основой интернета, потому что оказался готов и начал использоваться раньше.

OSI был более подробной и формальной моделью, но TCP/IP победил в практике.

В итоге получилась странная, но важная реальность:

```text
Real protocols: mostly TCP/IP
Engineering language: often OSI
```

Мы используем OSI model, чтобы описывать и troubleshooting TCP/IP networks.

### Зачем нужны layers

Layers важны по трем главным причинам:

1. Common language.
2. Troubleshooting and design.
3. Interoperability.

### Common Language

Если engineer говорит:

```text
This looks like a Layer 3 addressing issue.
```

другой engineer сразу понимает:

- IP addressing;
- default gateway;
- routing;
- subnetting;
- reachability between networks.

Без модели разговор превращается в слишком общее:

```text
The network is broken.
```

Это не помогает быстро найти причину.

### Troubleshooting and Design

Layered model позволяет изолировать проблему.

Примеры:

| Problem | Likely Layer |
| --- | --- |
| Cable unplugged | Layer 1 |
| Bad switch behavior or MAC issue | Layer 2 |
| Wrong IP address or gateway | Layer 3 |
| TCP connection problem | Layer 4 |

Такой подход помогает не разбирать всю сеть сразу. Ты проверяешь один layer, исключаешь его и двигаешься дальше.

### Interoperability

Interoperability означает, что оборудование разных vendors может работать вместе.

Это возможно, потому что vendors строят устройства под общие standards.

Пример:

```text
802.11 defines wireless behavior at Layer 2.
```

Если Cisco AP и Aruba AP следуют одному standard, они могут участвовать в совместимой wireless ecosystem.

Layered standards помогают разным устройствам "говорить" на понятных правилах.

### Верхние три OSI layers

Верхние layers OSI:

- Layer 7 - Application;
- Layer 6 - Presentation;
- Layer 5 - Session.

Они больше связаны с тем, как application создает, форматирует и управляет data до передачи по сети.

Network engineers часто меньше работают с этими слоями напрямую. Поэтому TCP/IP model объединяет их в один большой Application layer.

### Нижние четыре OSI layers

Нижние layers OSI:

- Layer 4 - Transport;
- Layer 3 - Network;
- Layer 2 - Data Link;
- Layer 1 - Physical.

Это область, где network engineers проводят большую часть времени.

Здесь находятся:

- TCP/UDP;
- IP addressing;
- routing;
- switching;
- MAC addresses;
- frames;
- cables;
- interfaces;
- signals.

### TCP/IP and OSI Alignment

Современная TCP/IP model хорошо совпадает с нижними четырьмя слоями OSI:

| OSI Layer | Modern TCP/IP Layer |
| --- | --- |
| Application, Presentation, Session | Application |
| Transport | Transport |
| Network | Internet |
| Data Link | Data Link |
| Physical | Physical |

В старой версии TCP/IP Data Link и Physical часто объединяли в один Link layer. Это было менее удобно для troubleshooting, поэтому современное объяснение обычно разделяет их.

### Как это звучит в реальной работе

В реальной команде ты чаще услышишь:

```text
Check Layer 1.
Looks like Layer 2.
This is probably Layer 3.
```

И почти никогда:

```text
This is an Internet layer problem.
```

То есть TCP/IP работает в основе, но OSI language живет в разговорах engineers.

### Что нужно знать сейчас

На этом этапе нужно уверенно знать:

- seven OSI layers;
- порядок layers;
- что делают bottom four layers;
- как OSI maps to TCP/IP;
- почему OSI vocabulary используется для TCP/IP networks.

Это база для следующих тем, где каждый layer будет разобран глубже.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| OSI model | Seven-layer model used to describe network communication and troubleshooting. |
| TCP/IP model | Practical protocol model used by the internet and modern networks. |
| Layer | Logical section of network communication with a specific role. |
| Application layer | Layer where user-facing applications and network services interact with data. |
| Presentation layer | OSI layer responsible for data format, encoding, compression or encryption concepts. |
| Session layer | OSI layer associated with managing sessions between systems. |
| Transport layer | Layer 4; handles TCP/UDP, ports, segmentation and transport behavior. |
| Network layer | Layer 3; handles IP addressing, routing and packet forwarding. |
| Data Link layer | Layer 2; handles frames, MAC addresses and local network delivery. |
| Physical layer | Layer 1; handles cables, signals, connectors and physical interfaces. |
| Interoperability | Ability of different vendors or systems to work together through shared standards. |
| IEEE 802.11 | Wireless LAN standard associated with Layer 2 behavior. |
| Common language | Shared vocabulary engineers use to describe problems quickly and clearly. |

## Questions

### 1. Что описывают OSI и TCP/IP models?

Они описывают, как network communication работает и как данные проходят через разные logical layers.

### 2. Сколько layers в OSI model?

Семь.

### 3. Сколько layers обычно показывает modern TCP/IP model?

Четыре основных layer: Application, Transport, Internet, Link/Network Access. В современных объяснениях Data Link и Physical часто показывают отдельно.

### 4. Почему engineers используют OSI language, если в реальности работает TCP/IP?

Потому что OSI vocabulary удобнее и точнее для troubleshooting, design и общения между engineers.

### 5. Что обычно означает Layer 1 problem?

Проблему physical layer: cable, connector, signal, interface или физическое подключение.

### 6. Что обычно означает Layer 2 problem?

Проблему switching, MAC addresses, frames, VLANs или local network delivery.

### 7. Что обычно означает Layer 3 problem?

Проблему IP addressing, routing, default gateway или connectivity between networks.

### 8. Почему layered troubleshooting полезен?

Он помогает изолировать проблему по слоям, а не проверять всю сеть хаотично.

### 9. Что такое interoperability?

Способность оборудования разных vendors работать вместе благодаря shared standards.

### 10. Почему 802.11 важен как пример?

Потому что это wireless standard, который помогает устройствам разных vendors работать по совместимым Layer 2 правилам.

### 11. Какие OSI layers TCP/IP объединяет в Application layer?

Application, Presentation и Session.

### 12. Какие четыре OSI layers особенно важны для network engineers?

Transport, Network, Data Link и Physical.

## What To Review Later

- Seven OSI layers in order.
- OSI vs TCP/IP layer mapping.
- Why OSI is used as troubleshooting language.
- Layer 1 physical examples.
- Layer 2 switching and wireless examples.
- Layer 3 IP and routing examples.
- Layer 4 TCP/UDP examples.
- Interoperability and shared standards.
