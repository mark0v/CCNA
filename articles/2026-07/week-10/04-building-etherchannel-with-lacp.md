# Building EtherChannel With LACP

Source: закрытая страница курса  
Date added: 2026-07-03  
Related plan item: Week 10 / Building EtherChannel with LACP  
Tags: EtherChannel, LACP, PAgP, port-channel, channel-group, STP, trunk
Language: Russian
Translation pair: articles-en/2026-07/week-10/04-building-etherchannel-with-lacp.md

## Summary

- EtherChannel превращает несколько физических линков в один логический Port-Channel.
- Есть три способа собрать bundle: static, PAgP и LACP.
- В реальных сетях предпочтительнее LACP, потому что это стандартный negotiated protocol.
- После создания bundle дальнейшие Layer 2 настройки нужно делать на Port-Channel interface.

## Key Points

- Static EtherChannel не выполняет negotiation и опаснее при ошибках конфигурации.
- PAgP работает, но это Cisco-proprietary protocol.
- LACP - industry standard, поэтому подходит для Cisco, non-Cisco switches, servers и access points.
- Для LACP режимы `active` + `active` или `active` + `passive` формируют channel; `passive` + `passive` не формируют.
- Проверять результат нужно командами `show etherchannel summary` и `show spanning-tree`.

## Notes

EtherChannel важен не просто потому, что "линков больше". Он важен потому, что без него STP может заблокировать один из параллельных switch-to-switch links. Физически у нас два кабеля, но логически работает только один. Это безопасно для Layer 2, но плохо для bandwidth utilization.

EtherChannel меняет картину: несколько физических interfaces объединяются в один logical link. STP больше не видит два конкурирующих пути между одними и теми же switches. Он видит один Port-Channel interface и принимает решение уже по нему.

Есть три способа построить EtherChannel:

| Method | What it does | Practical use |
| --- | --- | --- |
| Static | Принудительно добавляет порты в bundle без negotiation. | Лучше избегать в production, если нет сильной причины. |
| PAgP | Cisco-proprietary negotiation protocol. | Полезно знать для Cisco-only сред и экзамена. |
| LACP | Standards-based negotiation protocol. | Обычно лучший выбор в реальных сетях. |

Static mode выглядит простым: обе стороны просто настроены как bundle. Но именно это и опасно. Если одна сторона настроена иначе или выбраны неправильные порты, negotiation не остановит ошибку. В худшем случае можно получить loop или нестабильное поведение.

PAgP был создан Cisco и работает в Cisco-средах. Его режимы:

| PAgP mode | Behavior |
| --- | --- |
| `auto` | Пассивно ждет, пока другая сторона начнет negotiation. |
| `desirable` | Активно пытается сформировать EtherChannel. |

`auto` + `auto` не поднимет channel, потому что обе стороны ждут. `desirable` + `auto` и `desirable` + `desirable` работают.

LACP - более универсальный вариант. Это стандартный protocol, который используется между разными vendors и типами устройств. Его режимы:

| LACP mode | Behavior |
| --- | --- |
| `passive` | Ждет LACP negotiation от другой стороны. |
| `active` | Активно отправляет LACP packets и пытается сформировать channel. |

`passive` + `passive` не формирует EtherChannel. `active` + `passive` работает. `active` + `active` тоже работает. Практически проще использовать `active` на обеих сторонах, чтобы обе стороны явно пытались поднять channel.

Базовая команда для создания EtherChannel - `channel-group`. Обычно она применяется к interface range, потому что member ports должны настраиваться одинаково:

```text
Switch(config)# interface range fa0/1 - 2
Switch(config-if-range)# channel-group 1 mode active
```

После этого switch создает логический interface:

```text
Switch(config)# interface port-channel 1
```

Это важный момент. После создания bundle нужно думать не о двух отдельных interfaces, а о Port-Channel. Если нужно сделать trunk, разрешить VLANs или поменять Layer 2 параметры, это делается на `interface port-channel 1`, а не случайно на одном физическом member port.

Пример:

```text
Switch(config)# interface port-channel 1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20,30,40
```

Member ports должны совпадать. Проверять нужно как минимум:

- speed;
- duplex;
- access или trunk mode;
- allowed VLAN list;
- native VLAN;
- LACP/PAgP/static mode;
- Layer 2 параметры, которые влияют на bundle.

Если один member port отличается, он может быть исключен из bundle или уйти в suspended state. Поэтому будущие изменения нужно делать на Port-Channel interface и не расходить настройки member links вручную.

После настройки не нужно верить конфигурации на слово. Проверяем:

```text
Switch# show etherchannel summary
Switch# show spanning-tree
```

`show etherchannel summary` показывает group number, Port-Channel, Layer 2/Layer 3 state и physical ports, которые реально участвуют в bundle. `show spanning-tree` показывает, что STP теперь видит Port-Channel как один logical path, а не несколько отдельных links.

В production EtherChannel лучше настраивать в maintenance window. При создании bundle порты могут flap: уходить down и возвращаться up, пока channel формируется. Это нормально технически, но пользователи не обязаны радоваться, если в этот момент падают POS terminals или Wi-Fi.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `channel-group 1 mode active` | Добавляет interfaces в EtherChannel group 1 с LACP active mode. |
| `interface port-channel 1` | Переход к логическому interface, который представляет bundle. |
| `show etherchannel summary` | Быстрая проверка состояния EtherChannel и member ports. |
| `show spanning-tree` | Проверка того, как STP видит Port-Channel. |
| `active` | LACP mode, который активно пытается сформировать channel. |
| `passive` | LACP mode, который ждет negotiation от другой стороны. |
| `desirable` | PAgP mode, который активно пытается сформировать channel. |
| `auto` | PAgP mode, который пассивно ждет negotiation. |

## Questions

### 1. Почему LACP обычно предпочтительнее static EtherChannel?

Answer: LACP выполняет negotiation и помогает не поднять bundle при несовпадающих настройках. Static mode просто предполагает, что обе стороны настроены правильно.

### 2. Какие LACP mode combinations формируют channel?

Answer: `active` + `active` и `active` + `passive` формируют channel. `passive` + `passive` не формирует, потому что обе стороны ждут.

### 3. Где нужно делать trunk-настройки после создания EtherChannel?

Answer: На `interface port-channel`, потому что он представляет весь bundle. Изменение только одного physical member port может создать mismatch.

### 4. Чем полезна команда `show etherchannel summary`?

Answer: Она показывает, поднялся ли Port-Channel, работает ли он как Layer 2 или Layer 3 interface, и какие physical ports реально входят в bundle.

## What To Review Later

- Разницу между static, PAgP и LACP.
- LACP modes `active` и `passive`.
- PAgP modes `desirable` и `auto`.
- Как читать flags в `show etherchannel summary`.
- Почему настройки member ports должны совпадать.
