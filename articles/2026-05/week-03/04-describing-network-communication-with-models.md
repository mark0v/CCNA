# Describing Network Communication with Models

Source: закрытая страница курса  
Date added: 2026-05-16  
Related plan item: Week 3 / Describing communication with OSI  
Tags: osi, encapsulation, tcp, udp, ports, ip address, mac address, physical layer, troubleshooting
Language: Russian
Translation pair: articles-en/2026-05/week-03/04-describing-network-communication-with-models.md

## Summary

Один клик в браузере запускает целую цепочку network communication. Запрос проходит через OSI layers сверху вниз: application создает request, данные форматируются, session отделяет один разговор от другого, transport добавляет TCP/UDP и ports, network добавляет IP addresses, data link добавляет MAC addresses, а physical layer превращает все это в электрические сигналы, свет или radio waves.

На примере mocha request для NetworkChuck Coffee хорошо видно, что OSI model - это не просто список layers. Это способ описать реальный путь данных через сеть.

## Key Points

- A browser click can be described through all seven OSI layers.
- Layer 7 is where network-aware applications operate.
- Encapsulation means each layer wraps data with its own header or information.
- Presentation layer formats data using standards such as HTTP or HTTPS.
- Session layer helps separate different conversations on the same machine.
- Transport layer chooses TCP or UDP.
- TCP is reliable and uses acknowledgments.
- UDP is faster and does not wait for every lost packet to be recovered.
- Port numbers identify the application or service conversation.
- HTTPS commonly uses destination port 443.
- Network layer adds source and destination IP addresses.
- Data Link layer uses MAC addresses for hop-to-hop delivery.
- IP addresses usually stay end-to-end, while MAC addresses change at each router hop.
- Physical layer converts bits into electrical signals, light pulses or radio waves.
- The receiving side decapsulates the data in reverse order.

## Notes

### Один клик, семь layers

Представим NetworkChuck Coffee.

Сотрудник открывает browser на back-office computer и нажимает кнопку Mocha, чтобы получить рецепт из central repository.

Для пользователя это один click.

Для сети это путь через OSI model:

```text
Application -> Presentation -> Session -> Transport -> Network -> Data Link -> Physical
```

На другом конце server принимает данные и распаковывает их в обратном порядке.

### Layer 7 - Application

Application layer - это место, где network-aware application начинает communication.

Примеры:

- Chrome;
- Firefox;
- Edge;
- email client;
- API client;
- file transfer application.

Важно: не каждое приложение автоматически является network application. Если программа ни с кем не общается по сети, она не участвует в network communication.

В нашем примере browser создает request:

```text
Give me the mocha recipe.
```

### Layer 6 - Presentation

Presentation layer отвечает за format, representation и иногда encoding/encryption concepts.

В practical web example browser использует понятные server standards:

- HTTP;
- HTTPS.

Идея простая: request должен быть оформлен так, чтобы server понял, что именно просит client.

### Encapsulation

Encapsulation - это процесс, при котором каждый layer добавляет к данным свою служебную информацию.

Можно представить это так:

```text
Original data
Data + Transport header
Data + Transport header + IP header
Data + Transport header + IP header + MAC header
Bits on the wire
```

На каждом layer data получает новый "wrapper", который нужен для доставки.

### Layer 5 - Session

Session layer помогает управлять отдельными conversations.

На одном компьютере одновременно могут работать:

- browser;
- Spotify;
- email client;
- chat application;
- background updates.

Сеть должна понимать, какой ответ к какому разговору относится.

В реальных TCP/IP networks значительную часть этой практической сортировки помогают делать transport layer и port numbers, но OSI model выделяет идею session management отдельно.

### Layer 4 - Transport

Transport layer выбирает transport behavior:

- TCP;
- UDP.

TCP - reliable. Он ожидает acknowledgments и старается доставить данные полностью и по порядку.

UDP - unreliable в техническом смысле: он не требует подтверждения каждого packet и не делает такую же recovery-логику, как TCP.

Unreliable не значит "плохой". Это значит "не гарантирует доставку на уровне transport protocol".

### TCP vs UDP

TCP хорошо подходит для:

- web browsing;
- login forms;
- file downloads;
- transactions;
- situations where missing data is unacceptable.

UDP хорошо подходит для:

- live video;
- voice traffic;
- gaming;
- time-sensitive traffic.

Если live stream потерял packet, часто лучше продолжить поток, чем останавливать видео и ждать повторную доставку старого фрагмента.

### Port Numbers

Port numbers помогают понять, какому application conversation принадлежит traffic.

Всего есть 65,536 port numbers:

```text
0 through 65535
```

Well-known ports находятся ниже 1024.

Пример:

```text
HTTPS: TCP port 443
SMTP: TCP port 25
```

Когда browser отправляет mocha request:

```text
Source port: 55192
Destination port: 443
```

Когда server отвечает:

```text
Source port: 443
Destination port: 55192
```

Так computer понимает, что response belongs to browser, not Spotify or another application.

### Why Ports Matter in Troubleshooting

Когда service "не отвечает", хороший вопрос:

```text
Is the right port open?
```

Firewalls часто allow или block traffic based on port numbers.

Если HTTPS service должен отвечать на port 443, но firewall блокирует 443, проблема может быть не в application, а в path/policy.

### Layer 3 - Network

Network layer добавляет source and destination IP addresses.

IP address - это end-to-end address.

Аналогия: финальный город назначения в маршруте.

Например:

```text
Source IP: back-office computer
Destination IP: central coffee server
```

IP помогает понять, откуда packet идет и куда в итоге должен попасть.

### Layer 2 - Data Link

Data Link layer использует MAC addresses.

MAC address работает hop-to-hop.

Это значит:

- MAC address нужен, чтобы добраться до next device;
- на каждом router старый Layer 2 header снимается;
- для следующего segment добавляется новый Layer 2 header;
- IP source/destination при этом обычно остаются теми же end-to-end.

Простая мысль:

```text
IP gets you to the final destination.
MAC gets you to the next hop.
```

### IP vs MAC

Разница:

| Address Type | Scope | Changes at Router? | Used By |
| --- | --- | --- | --- |
| IP address | End-to-end | Usually no | Layer 3 |
| MAC address | Hop-to-hop | Yes | Layer 2 |

Traceroute помогает увидеть route as multiple hops. Он показывает, что путь через internet - это не один прыжок, а последовательность routers.

### Layer 1 - Physical

Physical layer превращает данные в физический сигнал.

В зависимости от medium это может быть:

- electrical signals on copper;
- pulses of light on fiber;
- radio waves over Wi-Fi.

В самом низу это просто bits:

```text
1s and 0s moving across a medium
```

### Decapsulation

Когда request доходит до central coffee server, процесс идет обратно.

Server распаковывает данные снизу вверх:

```text
Physical -> Data Link -> Network -> Transport -> Session -> Presentation -> Application
```

Каждый layer читает свою информацию, снимает свой wrapper и передает payload выше.

Потом server отправляет response с mocha recipe обратно тем же принципом.

### Why This Matters

Эта модель помогает понять, что network communication - это не magic.

Один click включает:

- application request;
- formatting;
- session/conversation tracking;
- TCP or UDP behavior;
- port numbers;
- IP addressing;
- MAC addressing;
- physical signaling.

Чем лучше ты видишь этот процесс, тем проще потом понимать IP addressing, routing, switching and troubleshooting.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Encapsulation | Process where each layer wraps data with its own header or control information. |
| Decapsulation | Reverse process where the receiver removes layer information and passes data upward. |
| HTTP | Web protocol used for browser/server communication without built-in encryption. |
| HTTPS | Secure web protocol commonly using TCP port 443. |
| TCP | Reliable transport protocol that uses acknowledgments and ordered delivery. |
| UDP | Transport protocol that sends data without TCP-style delivery guarantees. |
| Port number | Transport-layer identifier for a service or application conversation. |
| Well-known port | Port number below 1024 commonly assigned to standard services. |
| Source port | Port used by the sending side for a specific conversation. |
| Destination port | Port the sender targets on the receiving side. |
| IP address | Layer 3 address used for end-to-end delivery between networks. |
| MAC address | Layer 2 address used for hop-to-hop delivery on a local segment. |
| Traceroute | Tool that shows the router hops along a path to a destination. |
| Physical medium | Copper, fiber or wireless space used to carry bits. |

## Questions

### 1. Что происходит, когда user нажимает кнопку Mocha в browser?

Browser создает network request, который проходит вниз по OSI layers, encapsulates на каждом layer и отправляется к server.

### 2. Что такое encapsulation?

Это процесс, при котором каждый layer добавляет к данным свою служебную информацию, например transport header, IP header или MAC header.

### 3. На каком layer работают TCP и UDP?

На Transport layer, Layer 4.

### 4. Чем TCP отличается от UDP?

TCP reliable и использует acknowledgments. UDP не гарантирует доставку таким же способом, зато лучше подходит для time-sensitive traffic.

### 5. Почему video streaming часто использует UDP?

Потому что для live traffic иногда важнее продолжить поток, чем ждать повторную доставку уже устаревшего packet.

### 6. Для чего нужны port numbers?

Они помогают определить service или application conversation, например HTTPS на port 443.

### 7. Что делает destination port 443?

Он указывает, что client обращается к HTTPS service на server.

### 8. Почему response от server идет на random high-numbered client port?

Потому что этот source port client использовал для конкретной browser conversation, и так OS понимает, какому приложению вернуть response.

### 9. Что добавляет Network layer?

Source and destination IP addresses.

### 10. Чем IP address отличается от MAC address?

IP address используется end-to-end, а MAC address используется hop-to-hop и меняется на каждом router segment.

### 11. Что делает Physical layer?

Он превращает bits в electrical signals, light pulses или radio waves.

### 12. Что такое decapsulation?

Это обратный процесс на receiving side, когда каждый layer снимает свой header/wrapper и передает данные выше.

## What To Review Later

- Encapsulation and decapsulation.
- Seven OSI layers in order.
- TCP vs UDP.
- Port numbers and well-known ports.
- HTTPS port 443.
- IP address vs MAC address.
- Hop-to-hop vs end-to-end delivery.
- Physical media: copper, fiber and Wi-Fi.
