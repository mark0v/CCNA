# The Importance of Network Standards

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Ethernet and standards  
Tags: ethernet, standards, ieee, mac address, csma-cd, switch, hub, interoperability, binary

## Summary

Ethernet - это не сам кабель. Кабель является medium, а Ethernet - это standard, то есть набор правил, по которым устройства понимают друг друга. Благодаря standards устройства разных vendors могут работать вместе.

Главная мысль: cable - это дорога, Ethernet - правила движения. Без общего стандарта подключенные устройства не смогут нормально общаться.

## Key Points

- RJ45 cable часто называют "Ethernet cable", но технически Ethernet - это standard.
- Standards дают устройствам общий язык.
- Ethernet стал доминирующим networking standard.
- IEEE стандартизировал Ethernet в семействе 802.3.
- Standards позволяют устройствам разных vendors взаимодействовать.
- MAC address - уникальный hardware identifier сетевого интерфейса.
- MAC addresses используются на local network level.
- Switch learns MAC addresses and forwards traffic intelligently.
- Everything becomes binary: zeros and ones.
- Copper carries data as electrical signals.
- Fiber carries data as light pulses.
- Hubs повторяли traffic out every port.
- Switches делают forwarding decisions.
- CSMA/CD использовался в старых shared Ethernet environments для collision detection.
- Modern switched Ethernet обычно не сталкивается с collisions так же, как старые hub networks.

## Notes

### Ethernet Is the Standard

Люди часто говорят:

```text
Ethernet cable
```

В разговоре это нормально. Но точнее:

```text
Cable = physical medium
Ethernet = communication standard
```

Для NetworkChuck Coffee важно не только подключить устройства, но и убедиться, что они говорят по совместимым правилам.

### Why Standards Exist

Без standards каждый vendor мог бы придумать свой способ communication. Тогда компьютер одного производителя мог бы не понимать switch другого производителя.

Standards решают это:

- общий формат communication;
- совместимость разных vendors;
- predictable behavior;
- easier troubleshooting.

### MAC Address

MAC address - уникальный identifier network interface.

Обычно он выглядит как 12 hexadecimal characters.

Switch использует MAC addresses, чтобы понять, где находится устройство.

```text
MAC address -> switch port mapping
```

Так switch не рассылает traffic всем подряд, а отправляет его туда, где находится destination.

### Hubs and Collisions

Hub повторял signal out every port. Если два devices говорили одновременно, возникала collision.

CSMA/CD means:

```text
Carrier Sense Multiple Access with Collision Detection
```

Устройства слушали среду, пытались отправить данные, обнаруживали collisions и повторяли передачу позже.

Современные switches сделали Ethernet намного эффективнее, потому что они учатся и принимают forwarding decisions.

## Commands / Terms

```text
Ethernet - networking standard
IEEE - Institute of Electrical and Electronics Engineers
802.3 - Ethernet standards family
MAC address - hardware identifier
Hexadecimal - 0-9 and A-F
CSMA/CD - collision detection method in old shared Ethernet
Hub - старое устройство, повторяющее traffic
Switch - устройство, forwarding на основе MAC addresses
```

## Questions

### Ethernet - это кабель?

Нет. Ethernet - это standard. Кабель - medium, по которому передается signal.

### Зачем нужны standards?

Чтобы устройства разных vendors могли работать вместе по общим правилам.

### Что делает switch с MAC addresses?

Он учит, на каком порту находится какой MAC address, и forwarding traffic точнее.

### Почему hubs были менее эффективны?

Они рассылали traffic всем и создавали shared environment с collisions.

## What To Review Later

- IEEE 802.3 standards.
- MAC address table.
- Ethernet frames.
- Hub vs switch.
- Full duplex vs half duplex.
