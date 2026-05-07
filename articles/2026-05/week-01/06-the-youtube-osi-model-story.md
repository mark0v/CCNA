# The YouTube OSI Model Story

Source: закрытая страница курса  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 00 Lesson 05  
Tags: osi, application layer, presentation layer, session layer, transport layer, tcp, udp, ports, youtube

## Summary

Эта статья показывает, что происходит на верхних уровнях OSI model, когда пользователь открывает YouTube. Browser начинает запрос на Application layer, Presentation layer отвечает за форматирование и encryption, Session layer поддерживает conversation, а Transport layer выбирает способ доставки через TCP или UDP и использует port numbers.

Главная мысль статьи: верхние layers не “теория ради теории”. Они объясняют, как приложения превращают действия пользователя в network traffic и почему разные типы данных требуют разных transport protocols.

## Key Points

- Application layer - точка входа приложения в network communication.
- Presentation layer отвечает за data format и encryption.
- Session layer поддерживает communication session как одну conversation.
- Transport layer выбирает delivery behavior: TCP или UDP.
- TCP надежный: использует three-way handshake, acknowledgments и retransmission.
- UDP быстрее и проще: меньше контроля, меньше задержек.
- YouTube может использовать TCP для website elements и UDP для video stream.
- Port number показывает, какому service/application предназначен traffic.
- HTTPS обычно использует port `443`.
- SSH обычно использует port `22`.
- FTP обычно использует port `21`.
- RDP обычно использует port `3389`.
- Ephemeral port - временный source port, который client использует для конкретной conversation.

## Notes

### What Happens When You Watch YouTube?

На поверхности YouTube выглядит просто: открыть browser, перейти на сайт, нажать video. Но за этим действием скрывается работа нескольких OSI layers.

В прошлой статье фокус был на lower layers:

- Network;
- Data Link;
- Physical;
- routers;
- switches;
- packets;
- frames.

Здесь фокус выше: что делает browser и upper layers до того, как traffic дойдет до routing, switching и physical transmission.

### Upper Layers Are Not Just Theory

Когда Johnny вводит `youtube.com` в browser, Application layer начинает процесс. Это layer, где приложение “просит” network о communication.

Примеры приложений:

- web browser;
- online game;
- Spotify;
- email client;
- chat application.

Если app нужен network access, взаимодействие начинается через верхние layers.

### Application Layer

Application layer - это interface между program и network.

В случае YouTube browser говорит примерно:

```text
I need to reach youtube.com.
```

Application layer связан с network protocols and services, которые приложения используют для общения. Для web traffic это может быть HTTP или HTTPS.

### Presentation Layer

Presentation layer отвечает за то, чтобы data была в понятном и usable format.

Его задачи:

- data formatting;
- encoding/decoding;
- encryption/decryption;
- making data understandable for both sides.

Примеры formats:

| Format | Use |
| --- | --- |
| HTML | Web pages |
| XML | Structured data |
| JPG | Images |

В статье также упоминается SSL как пример protection/encryption. Главная идея: стороны должны договориться о формате и способе защиты data.

### Session Layer

Session layer отвечает за conversation между systems.

Он:

- opens communication;
- keeps communication going;
- closes communication when finished.

На lower layers traffic может проходить через many devices and paths. Но с точки зрения session это одна логическая conversation между browser и server.

Практический mental model:

```text
Lower layers move pieces.
Session layer maintains the conversation.
```

### TCP/IP Note About Upper Layers

В TCP/IP model Presentation и Session layers обычно не выделяются отдельно. Их functions чаще включены в Application layer.

Важно: если модель группирует layers иначе, сами функции не исчезают. Formatting, encryption и session management всё равно где-то выполняются.

### Transport Layer

Transport layer решает, как data должна быть доставлена.

Он не решает, куда идти по network. Это задача Network layer и IP addressing.

Transport layer отвечает за delivery behavior:

- reliable or fast;
- controlled or lightweight;
- TCP or UDP;
- source and destination ports.

### TCP

TCP, Transmission Control Protocol, ориентирован на reliability.

Перед передачей real data TCP использует three-way handshake:

```text
Client: Hey.
Server: Hey, I hear you.
Client: Cool, let's talk.
```

После этого TCP использует acknowledgments. Если data потерялась, TCP может запросить retransmission.

TCP подходит, когда важно получить data правильно:

- website elements;
- logins;
- file transfers;
- email;
- forms and transactions.

### UDP

UDP быстрее и проще, потому что не делает TCP-style reliability checks.

Он подходит, когда speed and low delay важнее идеальной доставки каждого кусочка data.

Типичные use cases:

- voice;
- video streaming;
- gaming;
- live traffic.

UDP не “плохой”. Он просто решает другую задачу.

### Why YouTube Uses Both TCP and UDP

YouTube может использовать разные transport protocols для разных частей experience.

| Traffic type | Better fit | Why |
| --- | --- | --- |
| Website page, menus, buttons, login | TCP | Нужно доставить корректно |
| Video stream | UDP | Важнее скорость и непрерывность |

Если потерян небольшой chunk video, часто лучше продолжить playback, чем остановить всё ради resend.

Для streaming, live video и gaming задержка может быть хуже, чем потеря небольшого количества data.

### TCP vs UDP: Business Need First

Правильный выбор protocol зависит от задачи.

| Need | Better fit |
| --- | --- |
| Reliability | TCP |
| Speed / low latency | UDP |
| File transfer | TCP |
| Voice/video | UDP |
| Login/payment/web forms | TCP |
| Real-time gaming | UDP |

Нельзя думать “TCP good, UDP bad”. Нужно смотреть на business need and application behavior.

### Ports

Port - это number, который показывает, какому service или application предназначен traffic.

Один server может поддерживать разные services:

- website;
- SSH;
- FTP;
- remote desktop;
- APIs;
- streaming.

Port помогает сказать, в какую “door” на server нужно попасть.

Common ports from the article:

| Service | Port |
| --- | --- |
| HTTPS | `443` |
| SSH | `22` |
| FTP | `21` |
| RDP | `3389` |

### Ephemeral Ports

На client side часто используется ephemeral port. Это temporary source port, который computer выбирает для конкретной conversation.

Пример:

```text
Client ephemeral port -> Server port 443
```

Ephemeral ports помогают client понять, какому local application/process вернуть response. Поэтому один computer может одновременно:

- смотреть YouTube;
- слушать Spotify;
- открывать много browser tabs;
- держать несколько network sessions.

### Putting It All Together

Когда Johnny смотрит YouTube:

1. Browser начинает request на Application layer.
2. Presentation layer заботится о format and encryption.
3. Session layer поддерживает conversation.
4. Transport layer выбирает TCP или UDP и использует ports.
5. Lower layers берут prepared traffic и доставляют его через network.

OSI model полезна не потому, что real world всегда идеально следует textbook diagram. Она полезна потому, что помогает понять role каждого layer.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Application layer | OSI Layer 7; where network services used by applications begin. |
| Presentation layer | OSI Layer 6; handles data format, encoding and encryption/decryption. |
| Session layer | OSI Layer 5; opens, maintains and closes communication sessions. |
| Transport layer | OSI Layer 4; handles TCP/UDP behavior and ports. |
| TCP | Reliable transport protocol with handshake, acknowledgments and retransmission. |
| UDP | Lightweight transport protocol focused on speed and low delay. |
| Three-way handshake | TCP setup process before real data transfer begins. |
| Acknowledgment | TCP confirmation that data was received. |
| Retransmission | TCP sending lost data again. |
| Port | Number that identifies a service or application endpoint. |
| Ephemeral port | Temporary client-side source port for a specific conversation. |
| HTTPS | Secure web traffic, commonly using TCP port 443. |
| SSH | Secure remote shell, commonly using port 22. |
| FTP | File Transfer Protocol, commonly using port 21. |
| RDP | Remote Desktop Protocol, commonly using port 3389. |

## Questions

### 1. Что делает Application layer?

Application layer является точкой, где приложение начинает network communication и использует network services/protocols.

### 2. За что отвечает Presentation layer?

Presentation layer отвечает за data formatting, encoding и encryption/decryption, чтобы обе стороны могли понять data.

### 3. За что отвечает Session layer?

Session layer открывает, поддерживает и закрывает communication session между systems.

### 4. Что решает Transport layer?

Transport layer решает, как доставлять data: надежно через TCP или быстрее и легче через UDP, а также использует port numbers.

### 5. Почему TCP считается reliable?

TCP использует three-way handshake, acknowledgments и retransmission потерянных данных.

### 6. Почему UDP полезен для video streaming и gaming?

UDP дает меньшую задержку и меньше overhead. Для real-time traffic часто лучше продолжить передачу, чем ждать повторной доставки потерянного chunk.

### 7. Почему YouTube может использовать и TCP, и UDP?

Website elements лучше доставлять надежно через TCP, а video stream часто выигрывает от скорости и меньшей задержки UDP.

### 8. Что такое port?

Port - это number, который указывает, какому service или application endpoint предназначен traffic.

### 9. Какой port обычно использует HTTPS?

HTTPS обычно использует port `443`.

### 10. Что такое ephemeral port?

Ephemeral port - это temporary source port на client side, выбранный для конкретной conversation.

### 11. Почему нельзя считать TCP хорошим, а UDP плохим?

Потому что они решают разные задачи. TCP лучше для reliability, UDP лучше для speed/low latency в real-time traffic.

### 12. Где в TCP/IP model обычно оказываются функции Presentation и Session layers?

В TCP/IP model эти функции обычно входят в Application layer.

## What To Review Later

- Upper OSI layers: Application, Presentation, Session, Transport.
- TCP reliability: handshake, acknowledgments, retransmission.
- UDP tradeoff: speed over perfect delivery.
- Common ports: `443`, `22`, `21`, `3389`.
- Ephemeral source ports.
- Why applications may use TCP and UDP for different parts of the same experience.
