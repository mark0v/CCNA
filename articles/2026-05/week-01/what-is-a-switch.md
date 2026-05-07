# What is a Switch?

Source: закрытая страница курса  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 00 Lesson 01  
Tags: switch, hub, cam table, mac address, layer 2, frame

## Summary

Switch - это устройство, которое соединяет устройства внутри одной локальной сети и пересылает трафик более умно, чем hub. Он не отправляет каждый кадр всем подряд, а учится, какие MAC addresses находятся за какими портами, сохраняет эту информацию в CAM table и отправляет traffic туда, куда он действительно должен попасть.

Главная мысль статьи: switch делает локальную сеть быстрее, тише и безопаснее, потому что принимает решения на Layer 2, используя MAC addresses и frames.

## Key Points

- Switch соединяет устройства внутри одной local network.
- Hub просто повторяет входящий traffic на все порты.
- Switch отправляет traffic только на нужный порт, если знает, где находится получатель.
- Switch учится по source MAC address входящего frame.
- Таблица, где switch хранит соответствие MAC address -> port, называется CAM table.
- Switch работает на Layer 2 OSI model.
- На Layer 2 правильный термин для передаваемой единицы данных - frame.
- Для проверки того, что switch выучил, используется команда `show mac-address-table`.
- Для критичных устройств Ethernet обычно предпочтительнее Wi-Fi из-за стабильности и предсказуемой скорости.

## Notes

### What Is a Switch?

Switch - это устройство, которое позволяет устройствам в локальной сети общаться друг с другом. Например, в NetworkChuck Coffee через switch могут быть подключены POS terminals, office PCs, printers и back office server.

Внешне switch выглядит просто: коробка с портами Ethernet. Но внутри он принимает электрические сигналы с кабелей и решает, куда отправить данные дальше.

Ключевое слово здесь - intelligently. Switch не просто повторяет всё подряд, а старается пересылать данные именно туда, где находится нужное устройство.

### Why Switch Is Better Than Hub

Hub - это старое и простое устройство, которое не принимает умных решений. Если один порт получает traffic, hub повторяет этот traffic на все остальные порты.

Это создает несколько проблем:

- лишний шум в сети;
- потраченная впустую bandwidth;
- худшая безопасность;
- больше ненужной работы для устройств.

Switch решает эту проблему. Если Johnny отправляет traffic Mark, switch старается отправить его именно Mark, а не всем устройствам в сети.

Простая формула:

- Hub blasts traffic everywhere.
- Switch sends traffic where it belongs.

### How a Switch Learns

Switch не знает расположение устройств заранее. Он учится во время работы сети.

Когда устройство отправляет frame, switch смотрит на source MAC address. Так он понимает: этот MAC address находится за конкретным портом. После этого switch сохраняет информацию в CAM table.

Позже, когда приходит frame с destination MAC address, switch проверяет CAM table и отправляет frame на нужный port.

Это и делает switch намного эффективнее hub: он учится, запоминает и использует эту информацию для forwarding decisions.

### CAM Table

CAM table, или Content Addressable Memory table, - это таблица, где switch хранит соответствие между MAC addresses и switch ports.

Пример логики:

| MAC address | Port |
| --- | --- |
| MAC Bob | Port 1 |
| MAC Mark | Port 2 |
| MAC Printer | Port 3 |

Если switch видит destination MAC address Mark, он проверяет CAM table и отправляет frame на Port 2.

В Cisco CLI для просмотра этой информации используется команда:

```text
show mac-address-table
```

Эта команда полезна для диагностики: она показывает, какие MAC addresses switch уже выучил.

### Layer 2, MAC Addresses, Frames

Switch работает на Layer 2 of the OSI model. Это значит, что он принимает решения на основе MAC addresses, а не IP addresses.

Важно различать уровни:

| Layer | Addressing | Data unit |
| --- | --- | --- |
| Layer 2 | MAC address | Frame |
| Layer 3 | IP address | Packet |

Когда мы говорим о switch, нужно держать в голове связку:

```text
Switch = Layer 2 = Frames = MAC addresses
```

В реальной речи инженеры иногда смешивают слова packet и frame, но для понимания CCNA это различие важно.

### Troubleshooting Tip

Если устройство не может связаться с другим устройством в той же LAN, одна из первых проверок - MAC address table на switch.

Если switch не выучил MAC address устройства, проблема может быть в физическом или data link уровне:

- cable;
- switch port;
- NIC;
- VLAN;
- неправильное подключение;
- проблема с самим устройством.

### Wireless Fits, Ethernet Wins

Wireless access point подключает беспроводные устройства к сети, часто через switch. Но Wi-Fi работает иначе, потому что wireless-среда больше похожа на shared medium: когда сигнал передается по воздуху, его потенциально слышат все устройства рядом.

Для guest devices и mobile endpoints Wi-Fi необходим. Но для критичных устройств, таких как cash register, back office desktop или server, Ethernet обычно лучше.

Причина простая: wired connection чаще дает лучшую стабильность, предсказуемую скорость и надежность.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Switch | Устройство, которое соединяет устройства внутри локальной сети и пересылает traffic на нужные ports. |
| Hub | Старое устройство, которое повторяет входящий traffic на все ports. |
| MAC address | Hardware address устройства, который используется на Layer 2. |
| CAM table | Таблица на switch, где хранится соответствие MAC address -> port. |
| Source MAC address | MAC address отправителя frame. По нему switch учится. |
| Destination MAC address | MAC address получателя frame. По нему switch выбирает порт для пересылки. |
| Frame | Единица данных на Layer 2. |
| Packet | Единица данных на Layer 3. |
| Layer 2 | Data Link layer модели OSI, где используются MAC addresses и frames. |
| `show mac-address-table` | Cisco command для просмотра MAC addresses, которые switch выучил. |

## Questions

### 1. Что делает switch?

Switch соединяет устройства внутри одной локальной сети и пересылает traffic на нужные порты, используя MAC addresses.

### 2. Почему switch лучше hub?

Hub отправляет traffic на все порты, а switch старается отправить traffic только туда, где находится нужный получатель. Это уменьшает шум, экономит bandwidth и улучшает работу сети.

### 3. Как switch узнает, где находится устройство?

Switch смотрит на source MAC address входящего frame и запоминает, с какого порта этот MAC address пришел.

### 4. Что такое CAM table?

CAM table - это таблица, где switch хранит соответствие между MAC addresses и ports.

### 5. На каком уровне OSI работает switch?

Switch работает на Layer 2, то есть на Data Link layer.

### 6. Чем frame отличается от packet в контексте этой статьи?

Frame - это единица данных на Layer 2, где используются MAC addresses. Packet - это единица данных на Layer 3, где используются IP addresses.

### 7. Какая команда помогает посмотреть, какие MAC addresses выучил switch?

Команда `show mac-address-table`.

### 8. Почему Ethernet предпочтительнее Wi-Fi для критичных устройств?

Ethernet обычно стабильнее, предсказуемее по скорости и надежнее, особенно для устройств вроде касс, рабочих станций и серверов.

## What To Review Later

- Разница между switch и hub.
- Как switch строит CAM table.
- Source MAC address vs destination MAC address.
- Связка `Switch = Layer 2 = Frames = MAC addresses`.
- Когда нужно проверять `show mac-address-table`.
- Почему wired connection важен для критичных бизнес-устройств.
