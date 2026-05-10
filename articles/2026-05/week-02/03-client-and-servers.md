# Client & Servers

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Client-server basics  
Tags: client, server, endpoint, switch, access point, network communication, plex, cameras

## Summary

Network - не главный герой. Это инфраструктура, которая позволяет устройствам и сервисам общаться, чтобы бизнес реально работал. В NetworkChuck Coffee сеть нужна не ради switch closet, а ради phones, laptops, cameras, servers и services, которые поддерживают работу кофейни.

Главная мысль: огромное количество сетевых взаимодействий укладывается в client/server model. Client просит, server предоставляет, а network переносит этот разговор между endpoints.

## Key Points

- Network - это infrastructure, а не цель бизнеса.
- Цель networking - communication между devices и services.
- Client/server - базовая модель многих сетевых взаимодействий.
- Client - устройство или приложение, которое запрашивает что-то.
- Server - устройство или приложение, которое предоставляет что-то.
- Один участник делает request, другой отвечает.
- Phone, который смотрит видео с local media server, является client.
- Plex/media box, который отдает фильм, является server.
- Camera может быть client, если отправляет video на storage/video server.
- Clients - это не только laptops и phones.
- Servers - это не только огромные data center machines.
- Endpoint - широкий термин для устройств на краю сети, которые общаются через нее.
- Clients и servers оба являются endpoints.
- Switches, cabling и access points - infrastructure, которая поддерживает communication.
- Troubleshooting полезно начинать с вопроса: кто client, какой server он пытается достичь и какой path между ними.

## Notes

### Network is not the goal

Network engineers любят switches, cables, ports и blinking lights, но бизнес существует не ради них.

Network поддерживает business needs:

- streaming media;
- storing surveillance footage;
- serving customers;
- processing work;
- connecting devices;
- keeping services available.

В NetworkChuck Coffee switch closet важен потому, что он позволяет real devices делать real work.

### Network as infrastructure

Network похожа на дорогу.

Она не destination. Она path, по которому идет communication.

Модель:

```text
Device/service needs to talk -> network carries the conversation
```

Если смотреть только на infrastructure, можно пропустить смысл traffic.

### Inside the coffee shop

Внутри кофейни:

- switch живет в network closet;
- cables идут от switch к устройствам;
- wireless access point подключается к switch;
- phones, tablets и laptops подключаются через Wi-Fi;
- servers или storage systems могут подключаться кабелем;
- cameras могут отправлять video по сети.

Topology важна, но relationships между устройствами важны еще сильнее.

### Access point and switch path

Wireless device все равно использует wired network за кулисами.

Пример path:

```text
Phone -> Wi-Fi -> access point -> switch -> server
```

Phone кажется wireless, но после AP traffic обычно идет через wired infrastructure.

### Client/server pattern

Client/server relationship - один из самых важных patterns в networking.

Главная идея:

```text
Client asks.
Server provides.
```

Или:

```text
Client -> request -> server
Server -> response/data -> client
```

Когда видишь этот pattern, network traffic становится проще понимать.

### What is a client?

Client - это device или application, которое просит что-то или начинает communication.

Примеры:

- phone запрашивает video;
- laptop открывает web page;
- tablet подключается к internal app;
- camera отправляет footage на storage;
- POS terminal обращается к server;
- приложение просит print service.

Client запускает interaction.

### What is a server?

Server - это device или application, которое предоставляет service.

Примеры:

- media server отдает movie;
- file server отдает files;
- web server отдает website;
- database server отдает data;
- video server принимает/хранит footage;
- authentication server проверяет logins.

Server отвечает на requests или принимает данные для service.

### Media streaming example

В NetworkChuck Coffee phone хочет посмотреть movie с локального media server.

| Device | Role | Why |
| --- | --- | --- |
| Phone | Client | Запрашивает movie |
| Plex/media box | Server | Хранит и отправляет movie |
| AP/switch | Infrastructure | Переносит traffic |

Traffic path:

```text
Phone -> AP -> switch -> media server
Media server -> switch -> AP -> phone
```

Это уже не абстрактные packets, а request и response.

### Not every client looks like a laptop

Clients - не только user devices.

Client - это любое device/application, которое инициирует request или отправляет data другой системе.

Значит, security camera тоже может быть client.

Почему?

```text
Camera sends video to a video/storage server.
```

В этой relationship camera инициирует отправку data.

### Surveillance example

В NetworkChuck Coffee cameras могут отправлять footage на video server.

| Device | Role | Why |
| --- | --- | --- |
| Camera | Client | Захватывает и отправляет video |
| Video/storage server | Server | Принимает и хранит footage |
| Switch/cabling | Infrastructure | Переносит video traffic |

Другой use case, тот же client/server pattern.

### Troubleshooting mindset

Не начинай с:

```text
Is the network broken?
```

Начинай с:

```text
Who is the client?
What server is it trying to reach?
What path should traffic take?
```

Это быстро сужает проблему.

Полезные вопросы:

- какое устройство просит?
- какой service нужен?
- какой server должен ответить?
- client подключен к network?
- server подключен к network?
- path между ними работает?
- проблема в endpoint, infrastructure или service?

### Endpoint

Endpoint - широкий термин для устройств на краю сети, которые общаются через нее.

Endpoints:

- phones;
- laptops;
- tablets;
- printers;
- cameras;
- servers;
- POS terminals;
- smart TVs;
- storage systems.

Важно:

```text
Both clients and servers are endpoints.
```

Endpoint - это не только user device.

### Infrastructure vs endpoints

Network infrastructure:

- switches;
- cabling;
- access points;
- routers;
- firewalls;
- patch panels.

Endpoints используют эту infrastructure.

| Infrastructure | Endpoint |
| --- | --- |
| Switch | Phone |
| Access point | Laptop |
| Cabling | Camera |
| Router | Server |

Network engineers заботятся об infrastructure, чтобы endpoints работали.

### Communication platform

Network - это communication platform.

В кофейне есть не просто connected gadgets.

Есть:

- clients making requests;
- servers providing services;
- endpoints relying on infrastructure;
- traffic moving through switches and APs;
- business functions depending on reliable communication.

Это делает network diagram осмысленной.

### Main takeaway

Когда смотришь на traffic, спрашивай:

```text
Who is asking?
Who is providing?
What infrastructure carries the conversation?
```

Client/server объясняет relationship.

Network переносит conversation.

Endpoints участвуют в нем.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Client | Device или application, которое запрашивает что-то или начинает communication. |
| Server | Device или application, которое предоставляет service или отвечает на requests. |
| Endpoint | Device/system на краю сети, который общается через нее. |
| Infrastructure | Network components, которые переносят traffic: switches, cabling, APs. |
| Switch | Устройство, которое соединяет wired LAN devices. |
| Access point | Устройство, которое расширяет wired network в Wi-Fi. |
| Service | Функция, которую предоставляет server: files, media, web, storage, authentication. |
| Request | Сообщение от client с просьбой что-то получить/сделать. |
| Response | Data или answer, отправленные server обратно. |
| Plex/media server | Пример server, который хранит и streams media. |
| Video server | Система, которая принимает и хранит surveillance footage. |

## Questions

### 1. Почему network не главный герой?

Потому что network - это infrastructure. Ее цель - дать devices и services общаться, чтобы бизнес работал.

### 2. Что такое client/server model?

Это relationship, где один участник просит что-то, а другой предоставляет.

### 3. Что такое client?

Client - это device или application, которое делает request или инициирует communication.

### 4. Что такое server?

Server - это device или application, которое предоставляет service или отвечает на requests.

### 5. В media streaming example кто client?

Phone, потому что он запрашивает movie.

### 6. В media streaming example кто server?

Plex/media box, потому что он хранит и отправляет movie.

### 7. Может ли camera быть client?

Да. Если она отправляет video на video/storage server, она действует как client.

### 8. Кто server в camera example?

Video/storage server, который принимает и хранит footage.

### 9. Что такое endpoint?

Endpoint - это device или system на краю сети, который общается через сеть.

### 10. Servers являются endpoints?

Да. Clients и servers оба могут быть endpoints.

### 11. Какие devices могут быть endpoints?

Phones, laptops, printers, cameras, servers, POS terminals, tablets и другие network devices.

### 12. Какую роль играют switch и access point в client/server communication?

Они являются infrastructure, которая переносит traffic между endpoints.

### 13. С какого troubleshooting-вопроса стоит начать?

Кто client и какой server он пытается достичь?

### 14. Почему client/server помогает troubleshooting?

Он показывает, кто просит, кто должен ответить и какой path должен пройти traffic.

### 15. Что переносит network в этой модели?

Conversation между clients и servers.

## What To Review Later

- Network as infrastructure, not the business goal.
- Client asks, server provides.
- Request and response.
- Phone/media server example.
- Camera/video server example.
- Endpoint meaning.
- Clients and servers are both endpoints.
- Infrastructure vs endpoints.
- Troubleshooting by identifying client, server and path.
