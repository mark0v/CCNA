# LLDP Standard Neighbor Discovery

Source: закрытая страница курса  
Date added: 2026-08-02  
Related plan item: Week 14 / LLDP standard neighbor discovery  
Tags: LLDP, CDP, Link Layer Discovery Protocol, neighbor discovery, mixed-vendor network, troubleshooting, switch operations
Language: Russian
Translation pair: articles-en/2026-08/week-14/08-lldp-standard-neighbor-discovery.md

## Кратко

- `LLDP` - стандартный протокол обнаружения соседей на Layer 2.
- Он решает почти ту же задачу, что и `CDP`, но не привязан к Cisco.
- `LLDP` особенно полезен в mixed-vendor сетях.
- На многих Cisco-устройствах `LLDP` не включен по умолчанию.
- Основные команды: `lldp run`, `show lldp neighbors`, `show lldp neighbors detail`.
- На интерфейсе можно отдельно управлять передачей и приемом LLDP.
- Это дает больше контроля между видимостью и безопасностью.

## Главное

- `CDP` удобен в Cisco-среде, а `LLDP` нужен там, где есть разные vendor.
- Discovery-протокол показывает directly connected neighbors, а не всю сеть сразу.
- Если `LLDP` выключен, он не поможет в момент срочного troubleshooting.
- Включение `LLDP` стоит добавить в стандартную политику для сетей, где есть mixed-vendor оборудование.
- Directional control позволяет включать receive и transmit отдельно.
- На user-facing портах нужно думать, какую discovery-информацию можно раскрывать.

## Заметки

`LLDP`, или `Link Layer Discovery Protocol`, можно воспринимать как стандартную версию идеи, которую Cisco реализует через `CDP`.

Задача та же:

```text
Показать, какое устройство подключено напрямую к этому порту.
```

Разница в охвате. `CDP` - Cisco-proprietary. `LLDP` - industry standard. Поэтому он лучше подходит для сетей, где рядом работают Cisco, HPE, Aruba, Juniper, Linux-системы, hypervisor, IP phone, wireless access point и другое оборудование.

## Почему LLDP важен

В реальных сетях не всегда есть один vendor.

Большой enterprise может стандартизировать все на Cisco. Но в средних компаниях, филиалах и сетях, которые росли постепенно, часто встречается смесь:

- Cisco switch;
- HPE или Aruba switch;
- Ubiquiti access point;
- Linux server;
- IP phone другого vendor;
- firewall другой платформы.

Если полагаться только на `CDP`, часть соседей может быть невидима. `LLDP` дает общий язык discovery между разными устройствами.

Для NetworkChuck Coffee это практично. Сегодня основная площадка может быть на Cisco, завтра новый филиал получит более бюджетное оборудование. Discovery все равно нужен.

## Главная неприятность

У `LLDP` есть важный нюанс: на многих Cisco-устройствах он не включен по умолчанию.

Это объясняет, почему `CDP` часто встречается в реальной Cisco-среде чаще. Когда сеть плохо задокументирована, discovery нужен сразу. Но выключенная функция не помогает.

Поэтому в mixed-vendor среде нужно не просто знать `LLDP`, а включать его как часть стандарта.

Команда:

```text
lldp run
```

После этого можно смотреть соседей:

```text
show lldp neighbors
show lldp neighbors detail
```

## Что показывает LLDP

Вывод похож на `CDP`.

Обычно можно увидеть:

- neighbor device;
- local interface;
- remote port;
- capabilities;
- platform или system description;
- management address;
- дополнительные operational details.

Подробный вывод особенно полезен, когда нужно перейти на соседнее устройство или уточнить, что именно подключено к порту.

Пример рабочего цикла:

```text
show lldp neighbors detail
записать neighbor и port
сравнить с документацией
перейти к следующему устройству
обновить topology notes
```

## Управление направлением

Сильная сторона `LLDP` - возможность управлять направлением на интерфейсе.

Можно отдельно разрешить:

- принимать LLDP-информацию;
- отправлять LLDP-информацию;
- делать и то и другое;
- отключить оба направления.

Пример:

```text
interface fa0/10
 no lldp transmit
 lldp receive
```

Или полностью отключить на порту:

```text
interface fa0/10
 no lldp transmit
 no lldp receive
```

Это полезно, когда нужно слушать информацию от подключенного устройства, но не раскрывать сведения о switch обратно.

## Баланс пользы и безопасности

Discovery-информация полезна администратору, но может помочь атакующему.

Через `LLDP` можно раскрыть:

- имя устройства;
- описание системы;
- platform;
- capabilities;
- management address;
- сведения о портах;
- иногда VLAN-related данные.

Поэтому хорошая политика не звучит как "включить везде" или "выключить везде".

Практичнее:

- включить `LLDP` между сетевыми устройствами;
- использовать его там, где есть phones, access points или mixed-vendor links;
- ограничить transmit на портах для недоверенных endpoint;
- документировать исключения.

## Сравнение с CDP

| Свойство | `CDP` | `LLDP` |
| --- | --- | --- |
| Тип | Cisco-proprietary | Open standard |
| Среда | Cisco-heavy | Mixed-vendor |
| Default на Cisco | Часто включен | Часто выключен |
| Команда включения | `cdp run` | `lldp run` |
| Просмотр соседей | `show cdp neighbors` | `show lldp neighbors` |
| Directional control | Менее гибко | transmit/receive отдельно |

Оба протокола полезны. Разница не в базовой идее, а в совместимости и управлении.

## Проверка

Полезные команды:

```text
show lldp
show lldp neighbors
show lldp neighbors detail
show lldp interface
show running-config | include lldp
```

Что проверить:

- включен ли `LLDP` глобально;
- какие интерфейсы transmit;
- какие интерфейсы receive;
- видны ли expected neighbors;
- нет ли unexpected neighbors;
- не раскрывается ли информация на лишних user-facing портах.

## Сценарий NetworkChuck Coffee

NetworkChuck Coffee открывает новый филиал. Часть оборудования Cisco, часть - другого vendor.

Если включен только `CDP`, администратор видит не всех соседей. Если включен `LLDP`, появляется общий discovery-слой.

Тогда можно быстрее понять:

- какой switch подключен к router;
- где access point;
- какие порты идут к phones;
- какие устройства не совпадают с документацией;
- где нужно обновить topology map.

Это не делает сеть идеальной, но дает быстрый способ увидеть реальность.

## Главный вывод

`LLDP` - это стандартный способ discovery для сетей, где Cisco не единственный участник.

Он похож на `CDP` по задаче, но шире по применению. Главный риск - забыть включить его там, где он нужен. Главная сила - interoperability и точный контроль transmit/receive на интерфейсах.

Если сеть mixed-vendor, `LLDP` должен быть частью operational baseline.

## Команды и термины

| Термин | Значение |
| --- | --- |
| `LLDP` | Link Layer Discovery Protocol, стандартный протокол обнаружения соседей. |
| `CDP` | Cisco Discovery Protocol, Cisco-протокол discovery. |
| `lldp run` | Включает LLDP глобально. |
| `show lldp neighbors` | Показывает краткий список LLDP-соседей. |
| `show lldp neighbors detail` | Показывает подробную информацию о соседях. |
| transmit | Отправка LLDP-информации с порта. |
| receive | Прием LLDP-информации на порту. |
| mixed-vendor network | Сеть с оборудованием разных производителей. |
| management address | Адрес для управления соседним устройством. |

## Вопросы

### 1. Зачем нужен LLDP?

Ответ: Чтобы обнаруживать напрямую подключенных соседей в сетях с разными vendor.

### 2. Чем LLDP отличается от CDP?

Ответ: `LLDP` является стандартным vendor-neutral протоколом, а `CDP` является Cisco-proprietary.

### 3. Почему LLDP может не помочь в срочном troubleshooting?

Ответ: На многих Cisco-устройствах он не включен по умолчанию.

### 4. Что дает directional control в LLDP?

Ответ: Возможность отдельно разрешать передачу и прием LLDP-информации на интерфейсе.

### 5. Почему LLDP нужно настраивать осознанно?

Ответ: Он помогает администраторам, но может раскрывать сведения о topology и management недоверенным устройствам.

## Что повторить позже

- `lldp run`.
- `show lldp neighbors`.
- `show lldp neighbors detail`.
- `no lldp transmit`.
- `no lldp receive`.
- Разницу между `CDP` и `LLDP`.
- Политику discovery на user-facing портах.
