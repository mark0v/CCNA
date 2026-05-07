# What is a Router?

Source: закрытая страница курса  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 00 Lesson 02  
Tags: router, gateway, arp, dns, routing table, layer 3, packet

## Summary

Router - это устройство, которое соединяет разные IP networks и помогает traffic выйти за пределы local network. Switch отвечает за локальную доставку внутри одной сети, а router принимает Layer 3 решения на основе IP addresses и routing table.

Главная мысль статьи: когда destination находится не в твоей локальной сети, компьютер отправляет traffic на default gateway. Обычно это router interface, который знает, куда отправить packet дальше.

## Key Points

- Switch соединяет устройства внутри одной сети.
- Router соединяет разные сети между собой.
- Разные IP ranges означают разные networks.
- Router работает на Layer 3 и принимает решения по IP addresses.
- Default gateway - это выход из локальной сети, обычно router interface.
- Если destination local, устройство ищет MAC address получателя через ARP.
- Если destination remote, устройство ищет MAC address router через ARP и отправляет traffic ему.
- Layer 3 packet сохраняет destination IP end-to-end.
- Layer 2 frame меняется на каждом network segment.
- Routing table - это карта сетей, известных router.
- DNS переводит human-friendly names в IP addresses, но routers маршрутизируют по IP, а не по именам.

## Notes

### What Is a Router?

Router - это не просто домашняя коробка для Wi-Fi. Его основная задача - соединять разные networks.

Если Johnny хочет связаться с Mark в той же local network, switch справится с этим. Но если Johnny хочет открыть сайт NetworkChuck Coffee, который находится в другой сети, switch уже не подходит. Нужен router.

Коротко:

- Switch handles local communication.
- Router handles communication between networks.

### Networks Are Defined by IP Ranges

Важно понимать, что networks отличаются не только тем, к какому switch подключены устройства. Главный признак здесь - IP address range.

Например:

| Network | Example range |
| --- | --- |
| Local coffee network | `10.1.1.x` |
| Remote web server network | `23.227.38.x` |

Это разные IP networks. Простое соединение двух switches не решает проблему маршрутизации между такими сетями. Для этого нужен router, потому что он понимает Layer 3, где живут IP addresses.

### Switch vs Router

Switch и router не конкурируют друг с другом. Они решают разные задачи.

| Device | Main job | Layer | Uses |
| --- | --- | --- | --- |
| Switch | Local delivery inside one LAN | Layer 2 | MAC addresses, frames |
| Router | Delivery between networks | Layer 3 | IP addresses, packets |

Switch думает в терминах MAC addresses. Это похоже на локальные delivery labels внутри одного neighborhood.

Router думает в терминах IP addresses. Это уже полный адрес на карте, который помогает выбрать путь к другой сети.

### Default Gateway

Default gateway - это адрес устройства, которому компьютер отправляет traffic, если destination находится вне local network.

В статье примером default gateway был:

```text
10.1.1.1
```

Обычно default gateway - это router interface в локальной сети.

Если gateway не настроен, устройство может общаться с соседями в своей сети, но не сможет выйти наружу. Оно как будто находится в районе без выхода на главную дорогу.

### Local Destination vs Remote Destination

Компьютер постоянно решает простой вопрос:

```text
Destination local or remote?
```

Если destination local:

1. Компьютер использует ARP, чтобы узнать MAC address нужного устройства.
2. Создает Layer 2 frame для этого MAC address.
3. Передает frame через switch.

Если destination remote:

1. Компьютер понимает, что destination не в local network.
2. Использует ARP, чтобы узнать MAC address default gateway.
3. Создает frame с destination MAC address router.
4. Router получает traffic и отправляет packet дальше.

Это объясняет, почему default gateway так важен для internet access.

### ARP

ARP, или Address Resolution Protocol, нужен для нахождения MAC address по известному IP address внутри local segment.

В статье ARP появляется в двух ситуациях:

- компьютер ищет MAC address local destination;
- компьютер ищет MAC address router, если destination remote.

Router тоже может использовать ARP на следующем network segment, если ему нужно узнать MAC address следующего получателя.

### What Changes and What Stays the Same

Когда traffic идет от Johnny к remote server, Layer 3 packet содержит destination IP server. Этот IP остается тем же от начала до конца.

Но Layer 2 frame меняется на каждом участке сети.

Пример:

| Segment | Source MAC | Destination MAC |
| --- | --- | --- |
| Johnny -> Router | Johnny MAC | Router MAC |
| Router -> Server side | Router MAC | Server MAC |

Router получает frame, снимает старую Layer 2 обертку, смотрит на Layer 3 destination IP, проверяет routing table и создает новый frame для следующего segment.

Это и есть routing.

### DNS

DNS, или Domain Name System, переводит понятные человеку names в IP addresses.

Сети не работают с именами вроде `NetworkChuck Coffee`. Для маршрутизации нужен IP address.

Обычная последовательность выглядит так:

1. Client спрашивает DNS server, какой IP address соответствует имени.
2. DNS возвращает IP address.
3. Client начинает отправлять traffic к этому IP.
4. Router использует routing table, чтобы доставить packet к нужной network.

Важно: routers do not route based on names. They route based on IP addresses.

### Routing Table

Routing table - это карта внутри router. В ней перечислены networks, которые router знает, и next hop или interface, через который нужно отправлять traffic.

В простой lab-среде router может знать только directly connected networks:

| Known network | How router reaches it |
| --- | --- |
| Network A | Directly connected interface |
| Network B | Directly connected interface |

В реальном интернете routing tables могут быть огромными. Router не пересылает traffic вслепую: он принимает решения на основе своей карты reachable destinations.

### Troubleshooting Tip

Если устройство может пинговать local machines, но не может выйти в internet или другую network, одна из первых проверок - default gateway.

Типичные проблемы:

- gateway не настроен;
- указан неправильный gateway;
- router interface down;
- проблема с routing table;
- traffic блокируется дальше по пути.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Router | Устройство, которое соединяет разные networks и пересылает packets между ними. |
| Switch | Устройство для локальной доставки traffic внутри одной LAN. |
| IP address | Layer 3 address, используемый для определения network и host. |
| MAC address | Layer 2 hardware address, используемый для локальной доставки frame. |
| Default gateway | Router interface, через который устройство отправляет traffic за пределы local network. |
| ARP | Address Resolution Protocol; помогает найти MAC address по IP address в local segment. |
| DNS | Domain Name System; переводит names в IP addresses. |
| Routing table | Таблица маршрутов, по которой router выбирает, куда отправить packet. |
| Packet | Layer 3 unit of data, где важны IP addresses. |
| Frame | Layer 2 wrapper, где важны MAC addresses. |
| Next hop | Следующее устройство, которому router отправляет packet по пути к destination. |

## Questions

### 1. Что делает router?

Router соединяет разные networks и помогает traffic переходить из одной IP network в другую.

### 2. Чем router отличается от switch?

Switch работает внутри одной local network и использует MAC addresses. Router работает между networks и использует IP addresses.

### 3. Что такое default gateway?

Default gateway - это устройство, обычно router interface, которому компьютер отправляет traffic, если destination находится вне local network.

### 4. Почему нельзя просто соединить два switches и решить routing между разными IP networks?

Потому что проблема не только в физическом соединении. Если устройства находятся в разных IP networks, нужен Layer 3 device, который умеет маршрутизировать packets между этими networks.

### 5. Что делает ARP?

ARP помогает узнать MAC address по IP address внутри local network segment.

### 6. Если destination находится в другой сети, чей MAC address ищет компьютер через ARP?

Компьютер ищет MAC address своего default gateway, то есть router interface в local network.

### 7. Что меняется при прохождении traffic через router: packet или frame?

Layer 3 packet с destination IP сохраняется end-to-end, а Layer 2 frame меняется на каждом network segment.

### 8. Зачем нужен DNS перед открытием сайта?

DNS переводит имя сайта в IP address. После этого client может отправлять traffic к нужному IP.

### 9. Что такое routing table?

Routing table - это карта router, где указано, какие networks ему известны и куда отправлять traffic для их достижения.

### 10. Что стоит проверить, если устройство видит local machines, но не выходит в internet?

Одна из первых проверок - default gateway: настроен ли он, правильный ли address указан и работает ли router interface.

## What To Review Later

- Difference between switch and router.
- Почему IP range определяет network.
- Default gateway как выход из local network.
- ARP для local и remote destinations.
- Packet vs frame при прохождении через router.
- DNS lookup before routing.
- Routing table как карта router.
