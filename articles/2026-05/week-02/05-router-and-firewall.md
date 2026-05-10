# Router & Firewall

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Router and firewall roles  
Tags: router, firewall, lan, wan, edge, all-in-one, security, routing, network design

## Summary

Router и firewall часто живут в одном физическом устройстве, особенно в маленьких сетях, но их основные роли разные. Router перемещает traffic между networks, особенно между LAN и WAN. Firewall проверяет traffic и решает, что разрешить, а что заблокировать.

Главная мысль: не оценивай устройство только по надписи на коробке. Смотри, какую функцию оно выполняет в конкретной сети.

## Key Points

- Router routes traffic between networks.
- Firewall enforces security rules.
- LAN - локальная сеть внутри здания.
- WAN - внешняя сеть, часто internet.
- Router обычно стоит на границе LAN и WAN.
- Switch и AP отвечают за локальную сторону сети.
- Router отвечает за traffic, который выходит из локальной сети или возвращается в нее.
- Router обычно имеет меньше портов, чем switch.
- Многие современные routers имеют встроенные switch ports.
- Wireless router может совмещать router, switch, firewall и access point.
- Router может иметь firewall features.
- Firewall может выполнять routing.
- Core function router - перемещение traffic.
- Core function firewall - inspection and control.
- В маленькой сети all-in-one устройство может быть нормальным выбором.
- В растущей сети роли часто лучше разделять.

## Notes

### Router

Router соединяет разные networks.

В NetworkChuck Coffee он отвечает за вопрос:

```text
Этот traffic остается внутри LAN или должен уйти наружу?
```

Одна сторона router смотрит в локальную сеть, другая - в сторону ISP/internet.

```text
LAN -> Router -> WAN/Internet
```

### Firewall

Firewall отвечает за security policy.

Он решает:

- какой traffic разрешен;
- какой traffic заблокирован;
- какие connections можно открыть наружу;
- что можно пустить внутрь;
- какие правила применяются к разным zones/users/devices.

### Почему возникает путаница

В маленьких сетях одно устройство часто делает сразу все:

- routing;
- firewalling;
- switching;
- wireless;
- NAT;
- VPN;
- filtering.

Это удобно, но для обучения важно мысленно разделять функции. Иначе устройство превращается в "коробку, которая делает интернет", а это плохая ментальная модель.

### All-in-one vs Dedicated Gear

Для первой маленькой кофейни all-in-one device может быть вполне разумным:

- дешевле;
- проще поставить;
- меньше железа;
- быстрее запустить.

Но с ростом появляются новые вопросы:

- guest WiFi надо отделить от POS;
- cameras нельзя смешивать с office devices;
- нужен VPN;
- нужен stronger security inspection;
- нужен monitoring;
- растет нагрузка.

Тогда отдельные роли становятся полезнее.

## Commands / Terms

```text
Router - устройство для передачи traffic между networks
Firewall - устройство/функция для контроля и фильтрации traffic
LAN - Local Area Network
WAN - Wide Area Network
Edge - граница сети
All-in-one - устройство, совмещающее несколько функций
```

## Questions

### В чем основная роль router?

Перемещать traffic между networks, особенно между LAN и WAN.

### В чем основная роль firewall?

Проверять traffic и применять security rules.

### Может ли одно устройство быть и router, и firewall?

Да. В маленьких сетях это очень часто встречается.

### Почему важно понимать функции, а не только названия устройств?

Потому что реальные устройства часто совмещают роли. Правильный вопрос: что это устройство делает в этой topology?

## What To Review Later

- NAT.
- Default gateway.
- Firewall zones.
- Stateful inspection.
- VPN on firewalls.
- Guest WiFi segmentation.
