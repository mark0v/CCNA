# Cisco SDN Models And Platforms

Source: закрытая страница курса  
Date added: 2026-08-21  
Related plan item: Week 17 / Cisco SDN models and platforms  
Tags: SDN, Cisco, SD-Access, SD-WAN, ACI, Catalyst Center, DNAC, APIC, VXLAN, API  
Language: Russian  
Translation pair: articles-en/2026-08/week-17/09-cisco-sdn-models-and-platforms.md

## Кратко

- В Cisco SDN много названий, но их проще разделить на модели и платформы.
- `API` - это "дверь" в устройство или систему, через которую контроллер может управлять сетью.
- `SD-Access` относится к campus network: здания, филиалы, switches, access points.
- `SD-WAN` относится к WAN: связи между площадками, интернет, VPN, MPLS и private circuits.
- `ACI` относится к data center, где живут приложения и сервисы.
- `VXLAN` помогает строить виртуальные туннели поверх существующей сети.
- `DNA Center` теперь чаще называется `Catalyst Center`, но на экзамене может встретиться старое имя.
- `APIC` - controller для ACI.

## Главное

- SDN означает переход от ручного управления отдельными устройствами к централизованному управлению сетью как системой.
- Cisco делит SDN на разные области: campus, WAN и data center.
- Для экзамена важно запомнить названия. Для работы важнее понимать назначение.
- SD-Access управляет сетью внутри здания или филиала.
- SD-WAN соединяет площадки и ресурсы через разные типы каналов.
- ACI управляет data center.
- Catalyst Center/DNAC - центральная платформа для SD-Access.
- APIC - controller для ACI.

## Заметки

Эта тема сначала выглядит как игра в термины.

Cisco любит названия:

- SD-Access;
- SD-WAN;
- ACI;
- DNAC;
- Catalyst Center;
- VXLAN;
- APIC.

Если держать все это в голове как одну кучу, получается путаница.

Проще разделить:

```text
Модели = где применяется подход.
Платформы = чем этим управляют.
```

## Что такое SDN

`Software Defined Networking`, или `SDN`, - это подход, при котором сеть управляется через центральный controller.

Старая модель:

```text
Зайти на Switch 1.
Настроить Switch 1.
Зайти на Router 2.
Настроить Router 2.
Зайти на AP 3.
Настроить AP 3.
```

SDN-подход:

```text
Зайти в центральную платформу.
Описать нужную policy.
Позволить controller применить изменения к сети.
```

Это не значит, что инженер больше не должен понимать устройства. Наоборот, без понимания routing, switching, VLANs и security SDN превращается в красивую панель без смысла.

## Роль API

`API`, или Application Programming Interface, - это способ программного взаимодействия с устройством или системой.

Простая аналогия:

```text
Controller хочет управлять switch.
Ему нужна дверь внутрь.
API - это такая дверь.
```

Через API можно:

- читать состояние устройства;
- отправлять configuration;
- проверять health;
- получать telemetry;
- запускать provisioning;
- автоматизировать troubleshooting.

В мире SDN API важны потому, что controller должен не просто "знать" о devices. Он должен уметь с ними разговаривать.

## Три модели Cisco SDN

Cisco SDN проще всего запомнить через три области:

| Модель | Где применяется | Простая идея |
| --- | --- | --- |
| `SD-Access` | Campus network | Управляет сетью здания или филиала. |
| `SD-WAN` | Wide area network | Соединяет площадки и ресурсы. |
| `ACI` | Data center | Управляет data center infrastructure. |

Короткая схема:

```text
SD-Access = сеть внутри здания.
SD-WAN = сеть между зданиями.
ACI = сеть data center.
```

## SD-Access

`SD-Access` - это Cisco-модель для campus network.

Campus network - это сеть внутри здания, офиса, магазина, школы или филиала.

Туда входят:

- switches;
- access points;
- локальная маршрутизация;
- VLANs;
- policies;
- подключение пользователей и устройств.

Если NetworkChuck Coffee открывает новую кофейню и хочет централизованно управлять in-store network, сюда хорошо ложится SD-Access.

Идея простая: не настраивать каждый switch и access point вручную, а управлять campus network через центральную платформу.

## SD-WAN

`SD-WAN` - это Cisco-модель для wide area network.

WAN соединяет:

- филиалы;
- магазины;
- офисы;
- data centers;
- cloud resources.

SD-WAN может использовать разные типы связей:

- интернет;
- VPN;
- MPLS;
- private circuits;
- LTE/5G backup.

Для пользователя главное не то, по какому каналу прошел traffic. Ему важно, чтобы приложение работало.

SD-WAN помогает controller выбрать подходящий путь и сделать работу между площадками более предсказуемой.

## ACI

`ACI`, или Application Centric Infrastructure, - это Cisco-модель для data center.

Если SD-Access занимается зданием, а SD-WAN соединяет площадки, то ACI живет там, где работают приложения и сервисы.

Data center требует другого подхода:

- много servers;
- много applications;
- высокая плотность traffic;
- строгие policies;
- частые changes;
- зависимость от application requirements.

ACI дает централизованное управление data center network и привязывает network policy к потребностям приложений.

## VXLAN

`VXLAN` может выглядеть как еще один пугающий термин, но базовая идея понятная.

VXLAN создает виртуальные туннели поверх существующей сети.

Упрощенно:

```text
Devices физически находятся в разных местах.
VXLAN помогает им общаться так, будто между ними есть логическая связность.
```

Это похоже на VPN внутри собственной сети.

Почему это важно:

- физическая topology становится менее жестким ограничением;
- controller может строить виртуальную connectivity;
- изменения не всегда требуют новых кабелей и портов;
- campus и data center designs становятся гибче.

VXLAN особенно важен в software-defined environments, где controller формирует логическую структуру поверх физической сети.

## Платформы Cisco

Теперь отделим модели от платформ.

Модель отвечает на вопрос:

```text
Где мы применяем SDN?
```

Платформа отвечает на вопрос:

```text
Через что мы этим управляем?
```

Для SD-Access Cisco долго использовала название `DNA Center`, или `DNAC`.

В новых материалах Cisco это чаще называется `Catalyst Center`.

Для экзамена важно знать оба имени:

```text
DNA Center = DNAC = Catalyst Center в современном названии.
```

Смысл платформы:

- видеть health устройств;
- видеть topology;
- проверять CPU и memory;
- выполнять provisioning;
- смотреть licensing;
- получать troubleshooting data;
- управлять сетью как единой системой.

## APIC

Для data center и ACI используется `APIC` - Application Policy Infrastructure Controller.

Самая короткая связка:

```text
ACI использует APIC.
```

APIC является controller для ACI environment и помогает управлять policies, connectivity и data center fabric.

## Как это запомнить

Минимальная таблица для CCNA:

| Cisco-термин | Что запомнить |
| --- | --- |
| `SD-Access` | Campus network. |
| `SD-WAN` | WAN и связи между площадками. |
| `ACI` | Data center. |
| `DNA Center` / `DNAC` | Старое/экзаменационное название платформы для SD-Access. |
| `Catalyst Center` | Новое название платформы для SD-Access. |
| `APIC` | Controller для ACI. |
| `VXLAN` | Виртуальные туннели поверх существующей сети. |
| `API` | Программная дверь для управления системой или устройством. |

## Практический совет

Если готовишься к экзамену, выучи названия.

Если работаешь с реальной сетью, выучи назначение.

Никого не впечатлит механическое знание расшифровки `ACI`, если ты не понимаешь, что:

```text
ACI = data center.
SD-Access = campus.
SD-WAN = WAN.
Catalyst Center/DNAC = centralized campus management.
```

Именно назначение помогает не потеряться в Cisco branding.

## Главный вывод

Cisco SDN - это не случайный набор названий.

Это карта:

- APIs дают controller способ говорить с устройствами;
- VXLAN помогает строить виртуальную связность;
- SD-Access управляет campus network;
- SD-WAN управляет WAN;
- ACI управляет data center;
- Catalyst Center/DNAC управляет SD-Access;
- APIC управляет ACI.

Когда видишь эти линии, тема перестает быть набором acronyms и становится нормальной архитектурой.

## Команды и термины

| Термин | Значение |
| --- | --- |
| `SDN` | Software Defined Networking, централизованный подход к управлению сетью. |
| `API` | Application Programming Interface, способ программного взаимодействия с системой. |
| `SD-Access` | Cisco SDN model для campus network. |
| `SD-WAN` | Cisco SDN model для wide area network. |
| `ACI` | Application Centric Infrastructure, Cisco SDN model для data center. |
| `VXLAN` | Технология виртуальных туннелей поверх существующей сети. |
| `DNA Center` | Старое название Cisco-платформы для SD-Access. |
| `DNAC` | Сокращение от DNA Center. |
| `Catalyst Center` | Новое название Cisco-платформы для SD-Access. |
| `APIC` | Controller для Cisco ACI. |
| controller | Центральная система, которая управляет сетью или ее частью. |

## Вопросы

### 1. Зачем в SDN нужен API?

Ответ: API дает controller способ программно взаимодействовать с устройством или системой.

### 2. Для чего используется SD-Access?

Ответ: Для campus network: зданий, филиалов, switches, access points и локальных policies.

### 3. Для чего используется SD-WAN?

Ответ: Для соединения площадок и ресурсов через WAN, включая internet, VPN, MPLS и private circuits.

### 4. Где применяется ACI?

Ответ: В data center.

### 5. Чем Catalyst Center связан с DNA Center?

Ответ: Catalyst Center - новое название платформы, которую Cisco раньше называла DNA Center/DNAC.

### 6. Что делает VXLAN?

Ответ: Создает виртуальные туннели поверх существующей сети и дает более гибкую logical connectivity.

## Что повторить позже

- Разницу между model и platform.
- SD-Access = campus.
- SD-WAN = WAN.
- ACI = data center.
- DNA Center/DNAC и Catalyst Center.
- APIC как controller для ACI.
- Роль API и VXLAN в SDN.
