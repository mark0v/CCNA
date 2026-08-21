# Network Automation Planes And SDN

Source: закрытая страница курса  
Date added: 2026-08-21  
Related plan item: Week 17 / Network automation planes and SDN  
Tags: network automation, SDN, management plane, control plane, data plane, Python, CAPWAP, OpenFlow, NETCONF, APIs  
Language: Russian  
Translation pair: articles-en/2026-08/week-17/08-network-automation-planes-and-sdn.md

## Кратко

- Network automation не убивает командную строку, но убирает повторяющуюся ручную работу.
- Если одинаковая задача повторяется на многих устройствах, ее стоит автоматизировать скриптом, шаблоном или централизованным управлением.
- Management plane - как администратор управляет устройством: SSH, web-интерфейс, SNMP, API.
- Control plane - где принимаются решения: маршрутизация, topology, forwarding logic.
- Data plane - где пакеты реально пересылаются, часто через ASICs.
- Basic automation чаще работает с management plane.
- `SDN` идет дальше и централизует control plane через controller.
- Wireless LAN Controller с lightweight AP - практичный пример централизованного контроля.

## Главное

- Automation - это лекарство от повторения, а не магия.
- Одну кофейню можно обслуживать вручную. Много точек уже требуют повторяемости.
- Скрипт на Python, который подключается к нескольким устройствам и меняет пароль, - это простой пример automation.
- Три planes помогают понять современную сетевую архитектуру: management, control, data.
- `SDN` не просто "автоматизирует вход". Он переносит сетевую логику в controller.
- Data plane все равно важен: устройства должны быстро пересылать пакеты.
- Полная мечта SDN требует стандартов и открытых протоколов, а не только vendor-specific controller.

## Заметки

Когда люди слышат network automation, иногда появляется неправильная мысль:

```text
Командная строка умерла.
Больше не нужно понимать switches.
```

Нет.

Automation не отменяет понимание сетей. Она убирает повторяющуюся работу, которую человек делает снова и снова.

Если задача одинаковая на 10, 100 или 500 devices, ее не обязательно печатать руками на каждом устройстве.

## Автоматизация как лекарство от повторения

Network automation - это практичная идея:

```text
Если действие повторяется, его можно стандартизировать и выполнить автоматически.
```

Подходы могут быть разными:

- скрипт;
- шаблон;
- playbook;
- controller;
- API;
- централизованная система управления.

Смысл один: не превращать инженера в человека, который вручную вводит одно и то же сотни раз.

## Сценарий NetworkChuck Coffee

Одна кофейня - это просто.

Можно вручную настроить:

- router;
- несколько switches;
- беспроводные точки доступа;
- VLANs;
- passwords;
- SSH settings;
- NTP;
- syslog.

Но потом NetworkChuck Coffee растет.

Появляются:

- несколько точек;
- одинаковые VLANs;
- одинаковые настройки безопасности;
- одинаковые wireless policies;
- одинаковые пароли или secrets;
- одинаковые настройки мониторинга.

Теперь ручная настройка становится рискованной.

Одно устройство обновили. Второе забыли. На третьем сделали опечатку. На четвертом пропустили команду.

Automation нужна, чтобы внедрение было повторяемым.

## Пример с Python

`Python` - популярный programming language для automation.

Простой пример network automation:

```text
Script подключается к нескольким устройствам.
Выполняет вход.
Отправляет одинаковые команды.
Проверяет результат.
Сохраняет вывод.
```

Например, можно обновить пароль на нескольких lab devices или собрать status интерфейсов.

Важно начинать безопасно.

Не нужно первой задачей менять production на сотнях switches. Лучше начать с задач только для чтения или лабораторной среды.

## Три плоскости сетевого устройства

Чтобы понять automation и `SDN`, полезно разделить устройство на три логические planes:

- management plane;
- control plane;
- data plane.

Это не три физические коробки. Это три роли внутри сетевого устройства.

## Плоскость управления

`Management plane` - это то, как администратор взаимодействует с устройством.

Примеры:

- SSH;
- web interface;
- SNMP;
- API calls;
- console;
- NETCONF;
- RESTCONF.

Если script подключается к router по SSH и отправляет команды, он работает через management plane.

Basic network automation обычно начинается именно здесь.

## Плоскость контроля

`Control plane` - это часть устройства, которая принимает решения.

Примеры:

- routing protocols;
- решения по topology;
- neighbor relationships;
- STP decisions;
- path selection;
- control traffic exchange.

Control plane отвечает не за физическую пересылку каждого пакета, а за понимание:

```text
Куда нужно отправлять трафик?
Какой путь правильный?
Какая topology актуальна?
```

## Плоскость данных

`Data plane` - это пересылка packets.

Упрощенно:

```text
Packet вошел.
Устройство проверило forwarding information.
Packet вышел через нужный interface.
```

Data plane должен быть быстрым.

Поэтому часто используются `ASICs` - специализированные chips для быстрой пересылки трафика.

Короткая схема:

```text
Management plane = administration.
Control plane = decisions.
Data plane = forwarding.
```

## Где здесь SDN

`SDN`, или `Software Defined Networking`, идет дальше обычной automation.

Basic automation:

```text
Я все еще управляю отдельными devices.
Просто делаю это быстрее через scripts или tools.
```

SDN:

```text
Network intelligence переносится в controller.
Devices становятся проще и больше сосредоточены на пересылке.
```

То есть `SDN` централизует не только management, но и часть control plane.

## Контроллер

`Controller` - это центральная система, которая принимает решения и управляет устройствами.

Он может:

- хранить policies;
- выдавать configuration;
- управлять topology;
- собирать telemetry;
- программировать forwarding behavior;
- координировать changes.

В идеале engineer работает с controller, а controller уже управляет устройствами.

## Пример с беспроводным контроллером

Wireless LAN Controller - понятный пример.

Lightweight AP часто не живет как полностью независимое устройство.

Он:

- подключается к сети;
- находит WLC;
- получает configuration;
- вещает нужные SSIDs;
- связывает traffic с VLANs;
- может туннелировать traffic через controller;
- отдает часть intelligence controller.

Это практический пример SDN-like thinking: централизованное управление и контроль вместо ручной настройки каждого AP.

В Cisco-среде для AP-to-controller communication часто используется `CAPWAP`.

## Почему универсальный SDN сложен

Полная мечта `SDN` выглядит так:

```text
Любое устройство.
Любой vendor.
Один controller.
Единое управление.
```

Но реальность сложнее.

Если Cisco controller управляет только Cisco, а другой vendor управляет только своими devices, это полезно, но не весь идеал.

Настоящее развитие требует:

- open standards;
- common protocols;
- predictable APIs;
- consistent data models;
- interoperability между vendors.

## Протоколы и инструменты

В разговорах об automation и SDN встречаются разные протоколы:

- `OpenFlow`;
- `NETCONF`;
- `RESTCONF`;
- `OpFlex`;
- SSH;
- SNMP;
- APIs.

Не нужно запоминать каждую деталь сразу.

Главная идея:

```text
Сети становятся programmable.
Devices можно запрашивать, настраивать и координировать через standard или vendor APIs.
```

## За пределами классической сети

Эта идея видна не только в routers и switches.

Похожий подход есть в:

- home automation;
- camera systems;
- cloud platforms;
- infrastructure tools;
- wireless controllers;
- firewall managers;
- monitoring platforms.

Ожидание становится нормальным:

```text
Подключить.
Принять под управление.
Управлять централизованно.
Автоматизировать.
```

## Практический совет

Если ты начинаешь automation, не пытайся сразу заменить весь workflow.

Начни с безопасного:

- резервные копии конфигураций;
- сбор status интерфейсов;
- сбор inventory;
- проверка NTP;
- проверка syslog;
- смена lab passwords;
- сравнение с baseline.

Сначала набери доверие к scripts. Потом можно расширяться.

## Главный вывод

Network automation помогает убрать повторяющиеся ручные задачи, особенно через management plane.

`SDN` идет дальше: он централизует control plane и переносит intelligence в controller. Но data plane остается критичным, потому что устройства все равно должны быстро пересылать packets.

Три идеи для запоминания:

1. Automation уменьшает повторение.
2. SDN централизует control.
3. Data plane продолжает двигать traffic.

## Команды и термины

| Термин | Значение |
| --- | --- |
| network automation | Автоматизация повторяющихся задач управления сетью. |
| `Python` | Язык программирования, часто используемый для automation. |
| management plane | Плоскость управления устройством: SSH, API, SNMP, web UI. |
| control plane | Плоскость принятия решений: routing, topology, path selection. |
| data plane | Плоскость пересылки packets. |
| `ASIC` | Специализированный chip для быстрой обработки traffic. |
| `SDN` | Software Defined Networking, подход с centralized control. |
| controller | Центральная система управления и контроля. |
| `WLC` | Wireless LAN Controller. |
| `CAPWAP` | Protocol для связи lightweight AP с controller. |
| `OpenFlow` | Protocol, связанный с programmable forwarding. |
| `NETCONF` | Protocol для программного управления network devices. |
| API | Programmable interface для взаимодействия systems. |
| orchestration | Coordinated automation across systems. |

## Вопросы

### 1. Что автоматизация не отменяет?

Ответ: Она не отменяет понимание сетей и command line. Она убирает повторяющуюся ручную работу.

### 2. Что такое management plane?

Ответ: Способ управления устройством: SSH, web UI, SNMP, API и похожие interfaces.

### 3. Чем control plane отличается от data plane?

Ответ: Control plane принимает решения о paths и topology, а data plane пересылает packets.

### 4. Чем SDN отличается от basic automation?

Ответ: Basic automation чаще управляет devices через management plane, а SDN централизует control plane через controller.

### 5. Почему data plane все равно важен?

Ответ: Даже при smart controller devices должны быстро пересылать traffic.

## Что повторить позже

- Три planes: management, control, data.
- Почему automation начинается с repetitive tasks.
- Чем SDN отличается от обычного scripting.
- Роль controller.
- Почему WLC похож на practical SDN example.
- Зачем нужны open protocols и APIs.
