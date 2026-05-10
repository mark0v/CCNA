# LAN vs. WAN

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Network fundamentals  
Tags: lan, wan, network, switch, access point, wifi, network closet, local network

## Summary

Network - это способ, с помощью которого устройства могут общаться друг с другом. LAN и WAN описывают масштаб этой связи: LAN работает внутри ограниченного места, например дома, офиса или кофейни, а WAN нужен, когда трафик выходит за пределы локальной сети, чаще всего в интернет или к удаленной площадке.

Главная мысль: LAN - это "внутри", WAN - это "наружу". LAN держится на локальной инфраструктуре: switches, cabling, access points и network closet. WAN дает путь во внешний мир.

## Key Points

- Network позволяет устройствам обмениваться данными.
- Local data - это данные, которые хранятся и доступны на конкретном устройстве.
- Даже два соединенных компьютера уже образуют network.
- В IT слово network означает систему связанных устройств, которые могут общаться.
- В кофейне сеть - это не только видимый Wi-Fi.
- Wireless-клиенты почти всегда опираются на проводную инфраструктуру.
- Network closet - скрытая комната, где живет ключевое сетевое оборудование.
- Switch соединяет проводные устройства внутри LAN.
- Wireless access point дает Wi-Fi, но обычно сам подключается к switch.
- LAN означает Local Area Network.
- LAN ограничена локальным пространством: дом, офис, магазин, здание.
- LAN traffic остается внутри локальной среды.
- WAN означает Wide Area Network.
- WAN соединяет сети на больших расстояниях.
- В обычной речи WAN часто означает интернет-подключение.
- WAN также может соединять одну бизнес-площадку с другой.
- При troubleshooting сначала полезно понять: проблема внутри здания или при выходе наружу.

## Notes

### Что такое network?

Network - это способ связи между устройствами.

Связь может идти через:

- copper cable;
- fiber;
- Wi-Fi;
- другой метод подключения.

Самая простая модель:

```text
Device A может поговорить с Device B.
Это уже network.
```

Сеть может быть маленькой, некрасивой и плохо масштабируемой, но если устройства могут обмениваться данными, базовая идея уже работает.

### Local data

Local означает, что данные находятся на конкретном устройстве и доступны с него.

Примеры:

- локальные файлы;
- локальные папки;
- локальные приложения;
- данные на самом устройстве.

Пока устройства не соединены, каждое живет как отдельный остров. После подключения они могут обмениваться данными.

### Network как общее понятие

Network - не только IT-слово.

Можно говорить о:

- сети дорог;
- сети людей;
- сети кофеен;
- компьютерной сети.

Общая идея:

```text
Связанные элементы, которые могут взаимодействовать.
```

В IT этими элементами обычно являются devices и services.

### Пример NetworkChuck Coffee

Клиент видит приятную сторону кофейни:

- Wi-Fi;
- кассу;
- tablets;
- гостевую зону;
- медиа-устройства.

Но за этим стоит физическая инфраструктура:

- network closet;
- switches;
- patch panels;
- cabling;
- wireless access points;
- router/firewall;
- WAN connection;
- power/UPS.

Видимый wireless-опыт зависит от очень физической сети за стеной.

### Wireless тоже нуждается в проводах

Wireless не означает, что во всей сети нет проводов.

Обычно это значит:

```text
Клиентскому устройству не нужен кабель.
Но access point все равно подключен к wired network.
```

Wi-Fi чаще всего является расширением проводной LAN, а не полной заменой LAN.

### Network closet

Network closet - это место, где находится основная сетевая инфраструктура.

Туда могут сходиться:

- register/POS devices;
- office computers;
- cameras;
- access points;
- printers;
- local servers;
- smart TVs or media devices;
- internet/WAN equipment.

Для посетителя это невидимо, но для бизнеса это сердце connectivity.

### Зачем нужен switch

Подключать каждое устройство напрямую к каждому другому устройству невозможно и неудобно.

Плохая модель:

```text
Computer A -> Computer B -> Computer C -> Computer D
```

Если что-то ломается посередине, часть сети может отвалиться.

Нормальная модель:

```text
Devices -> Switch
```

Switch становится центральной точкой для проводных устройств LAN и помогает им общаться.

### Wireless access point

Wireless access point часто сокращают до:

```text
AP
```

AP создает Wi-Fi для:

- phones;
- laptops;
- tablets;
- handheld devices.

Но сам AP обычно подключается к switch.

Простая модель:

```text
Phone -> Wi-Fi -> Access Point -> Switch -> LAN/WAN
```

### LAN

LAN означает Local Area Network.

Это сеть внутри ограниченной локальной области:

- одна кофейня;
- дом;
- офис;
- офисный suite;
- здание;
- локальная бизнес-площадка.

В NetworkChuck Coffee к LAN могут относиться:

- register/POS system;
- back office PC;
- smart TV;
- printer;
- Wi-Fi clients;
- cameras;
- local server;
- access points;
- switches.

### LAN traffic

LAN traffic остается внутри локальной среды.

Примеры:

- POS terminal говорит с локальным устройством в магазине;
- laptop печатает на printer в офисе;
- клиент смотрит видео с local media server;
- office PC открывает локальную shared folder;
- phone обращается к internal server.

LAN не обязана быть маленькой. В ней могут быть many switches, APs, printers, cameras и clients. Главное - это локальность.

### WAN

WAN означает Wide Area Network.

WAN выходит за пределы локальной среды и соединяет большие расстояния.

В обычной речи WAN часто означает:

```text
Internet connection
```

Но технически WAN может соединять:

- branch с branch;
- coffee shop с headquarters;
- office с data center;
- площадки в разных городах;
- площадки в разных странах.

### WAN traffic

WAN traffic покидает локальную сеть.

Примеры:

- register обращается к cloud payment processor;
- laptop открывает Netflix;
- manager проверяет inventory из другого города;
- branch office подключается к headquarters;
- локальная сеть обращается к cloud apps.

Модель:

```text
LAN -> WAN -> internet/remote site
```

### Troubleshooting LAN vs WAN

Хороший troubleshooting начинается с вопроса о масштабе:

```text
Проблема внутри здания
или только когда трафик выходит наружу?
```

Если проблема локальная, думай про LAN:

- switch;
- cabling;
- Wi-Fi;
- access point;
- local addressing;
- local device issue.

Если проблема возникает при выходе наружу, думай про WAN:

- internet circuit;
- ISP issue;
- router/firewall;
- WAN connection;
- remote service;
- routing outside the site.

### Mental model

| Type | Scope | Example |
| --- | --- | --- |
| LAN | Внутри локального места | Устройства кофейни общаются между собой |
| WAN | За пределы локального места | Кофейня выходит в интернет или к remote site |

Короткая версия:

```text
LAN is inside.
WAN is outside.
```

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Network | Связанные устройства, которые могут обмениваться данными. |
| Local | Находится на текущем устройстве или внутри локальной среды. |
| LAN | Local Area Network; сеть внутри ограниченной локальной области. |
| WAN | Wide Area Network; сеть для связи за пределами локальной площадки. |
| Switch | Устройство, которое соединяет проводные LAN devices. |
| AP | Access Point; устройство, которое дает Wi-Fi и обычно подключается к wired LAN. |
| Wi-Fi | Беспроводной способ доступа клиентских устройств к сети. |
| Network closet | Комната/место, где установлена сетевая инфраструктура. |
| LAN traffic | Трафик, который остается внутри local network. |
| WAN traffic | Трафик, который выходит к internet или remote locations. |
| ISP | Internet Service Provider. |

## Questions

### 1. Что такое network?

Network - это способ, с помощью которого устройства могут общаться друг с другом.

### 2. Что означает local в этом уроке?

Local означает, что данные или ресурсы находятся на текущем устройстве или внутри локальной среды.

### 3. Что происходит, когда два отдельных компьютера соединяют между собой?

Они образуют network, потому что теперь могут обмениваться данными.

### 4. Зачем кофейне network closet?

Там находится инфраструктура для Wi-Fi, касс, камер, office devices и WAN connectivity.

### 5. Почему wireless не означает полностью "без проводов"?

Потому что wireless clients обычно подключаются через AP, который сам подключен к wired network.

### 6. Что делает switch?

Switch соединяет проводные устройства внутри local network.

### 7. Что означает AP?

AP означает Access Point.

### 8. Что делает access point?

Он дает Wi-Fi, чтобы wireless devices могли подключаться к сети.

### 9. Что означает LAN?

LAN означает Local Area Network.

### 10. Что такое LAN?

LAN - это сеть внутри ограниченной области: дома, офиса, магазина или здания.

### 11. Что означает WAN?

WAN означает Wide Area Network.

### 12. Что такое WAN?

WAN соединяет сети на больших расстояниях или за пределами локальной среды.

### 13. Что WAN часто означает в обычной речи?

Обычно internet connection.

### 14. Может ли WAN быть не интернетом?

Да. WAN может соединять одну бизнес-площадку с другой удаленной площадкой.

### 15. Какой простой mental model для LAN vs WAN?

LAN - inside, WAN - outside.

### 16. Какой вопрос стоит задать первым при troubleshooting?

Проблема остается внутри здания или появляется только при выходе наружу?

### 17. Если printer внутри магазина недоступен, это скорее LAN или WAN?

LAN, потому что связь локальная.

### 18. Если register не может достучаться до cloud payment processor, это скорее LAN или WAN?

WAN или internet-path issue, потому что трафик выходит наружу.

## What To Review Later

- Network = connected devices that can communicate.
- Wireless usually rides on wired infrastructure.
- Switch role in the LAN.
- AP role for Wi-Fi.
- LAN = local/inside.
- WAN = wide/outside.
- Internet as common WAN example.
- WAN can also connect business sites.
- Troubleshooting starts by scoping LAN vs WAN.
