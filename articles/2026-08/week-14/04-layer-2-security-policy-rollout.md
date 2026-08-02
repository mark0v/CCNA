# Layer 2 Security Policy Rollout

Source: закрытая страница курса  
Date added: 2026-08-02  
Related plan item: Week 14 / Layer 2 security policy rollout  
Tags: Layer 2 security, Port Security, DHCP Snooping, Dynamic ARP Inspection, switch security, trust boundary, rollout policy
Language: Russian
Translation pair: articles-en/2026-08/week-14/04-layer-2-security-policy-rollout.md

## Кратко

- Layer 2 security нужно внедрять как политику, а не как набор случайных команд.
- Требование "защитить сеть" нужно перевести в конкретные правила для портов, VLAN и доверенных направлений.
- `Port Security`, `DHCP Snooping` и `Dynamic ARP Inspection` закрывают разные риски access layer.
- End-device порты обычно блокируются сильнее, чем uplink, router и access point порты.
- Trusted/untrusted границы нужно определить до включения функций.
- Плохой rollout может вызвать outage так же быстро, как и атака.
- В production сначала маппинг портов, потом конфиг, потом окно работ, потом проверка.

## Главное

- Письменная политика важна: она делает конфигурацию повторяемой и защищает от хаоса.
- `Port Security` ограничивает, какие MAC-адреса могут появляться на end-device портах.
- `DHCP Snooping` блокирует rogue DHCP server и помогает против DHCP starvation.
- `DAI` использует DHCP Snooping binding table, чтобы ловить ARP spoofing.
- Uplink, trunk, router, firewall и wireless access point порты нельзя настраивать как обычные клиентские порты.
- Проверка после внедрения обязательна: без нее ты не знаешь, что реально включено.

## Заметки

На бумаге запрос выглядит просто: внедрить `Port Security`, `DHCP Snooping` и `Dynamic ARP Inspection`.

В реальности такой запрос слишком общий. Кто-то должен решить:

- какие порты являются access-портами пользователей;
- какие порты ведут к инфраструктуре;
- какие VLAN защищаются;
- где проходят DHCP-ответы;
- где можно доверять ARP-трафику;
- что делать при нарушении политики;
- как откатить изменение, если сеть ломается.

Это уже не "ввести команды". Это проектирование политики.

## Почему нужна политика

Если включать функции по памяти и настроению, сеть быстро станет непредсказуемой.

На одном switch `Port Security` включен, на другом нет. Где-то `DHCP Snooping` работает только для одной VLAN. Где-то uplink забыли сделать trusted. Где-то `DAI` включили, но static IP-сервер не учли.

Итог:

- разные площадки ведут себя по-разному;
- troubleshooting занимает больше времени;
- новые администраторы не понимают стандарт;
- изменения опасно делегировать;
- после инцидента сложно доказать, какая политика реально была.

Письменная политика нужна не для бюрократии. Она нужна, чтобы сеть можно было повторяемо строить, проверять и поддерживать.

## Политика Port Security

Базовое правило:

```text
End-device порты получают Port Security.
Инфраструктурные порты не настраиваются как обычные клиентские.
```

Для Castle Rysen логика такая:

- порт к одному фиксированному endpoint - `maximum 1`;
- нарушение на чувствительном порту - `shutdown`;
- для стабильных устройств можно использовать `sticky MAC`;
- для patron-портов sticky MAC может быть плохой идеей;
- IP phone + PC может требовать `maximum 2`.

Пример:

```text
interface range fa0/3-20
 switchport mode access
 switchport port-security
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation shutdown
```

Это правило не подходит для uplink, router-портов и портов к wireless access point. Там может быть много MAC-адресов, и жесткий `maximum 1` быстро сломает нормальную работу.

## Политика DHCP Snooping

`DHCP Snooping` отвечает на один важный вопрос:

```text
Какие порты имеют право приносить DHCP server replies?
```

Policy:

- включить `DHCP Snooping` глобально;
- включить его на нужных cafe VLAN;
- trusted - только порты в сторону настоящего DHCP server;
- клиентские access-порты оставить untrusted;
- на untrusted-портах применить rate limit.

Пример:

```text
ip dhcp snooping
ip dhcp snooping vlan 10,20,30

interface gi0/1
 ip dhcp snooping trust

interface range fa0/3-20
 ip dhcp snooping limit rate 10
```

Если забыть trusted uplink, клиенты могут перестать получать адреса. Поэтому сначала нужно проследить путь DHCP offer через все switch.

## Защита от DHCP Starvation

`DHCP starvation` - атака, при которой устройство генерирует много DHCP-запросов, часто с разными MAC-адресами, чтобы вычерпать пул адресов.

Здесь функции помогают вместе:

- `Port Security` ограничивает количество MAC-адресов на порту;
- `DHCP Snooping` блокирует rogue DHCP replies;
- DHCP rate limit ограничивает поток DHCP-пакетов.

Это не делает сеть неуязвимой, но резко снижает риск простых Layer 2 атак.

## Политика Dynamic ARP Inspection

`DAI` проверяет ARP-сообщения и помогает остановить `ARP spoofing`.

Но он зависит от `DHCP Snooping binding table`.

Policy:

- сначала включить и проверить `DHCP Snooping`;
- затем включить `DAI` на нужных VLAN;
- infrastructure/uplink порты продумать отдельно;
- static IP-устройства учесть до rollout;
- проверить ARP rate limits.

Пример:

```text
ip arp inspection vlan 10,20,30

interface gi0/1
 ip arp inspection trust
```

Access-порты пользователей обычно untrusted. Именно там мы хотим проверять ARP. Но router, firewall, server и trunk-порты могут требовать trust или статических привязок.

## Доверенные и недоверенные порты

Граница доверия - центральная идея всей этой темы.

| Функция | Trusted обычно где | Untrusted обычно где |
| --- | --- | --- |
| `DHCP Snooping` | uplink к DHCP server/router | access-порты клиентов |
| `DAI` | uplink, trunk, инфраструктура | access-порты клиентов |
| `Port Security` | не про trust, а про MAC-limit | end-device access-порты |

Ошибка в trust boundary почти всегда выглядит как странная проблема сети:

- DHCP не выдает адреса;
- ARP не работает;
- клиенты видят gateway, но не ходят дальше;
- один сегмент работает, другой нет;
- после включения защиты "случайно" пропадает часть устройств.

На самом деле это не случайность. Коммутатор блокирует трафик по настроенной политике.

## Рабочий порядок внедрения

Практичный rollout:

1. Собрать карту портов.
2. Разделить access, trunk, uplink и инфраструктурные порты.
3. Найти DHCP server и путь DHCP offer.
4. Найти static IP-устройства.
5. Написать политику для `Port Security`, `DHCP Snooping` и `DAI`.
6. Подготовить конфиг в текстовом файле.
7. Внедрять в maintenance window.
8. Проверить show-командами.
9. Сохранить конфигурацию.
10. Задокументировать исключения.

Такой порядок скучнее, чем быстро печатать команды, зато он намного надежнее.

## Проверка

Команды:

```text
show port-security
show port-security interface fa0/3
show ip dhcp snooping
show ip dhcp snooping binding
show ip arp inspection
show ip arp inspection interfaces
show interfaces status err-disabled
show interfaces trunk
```

Что подтвердить:

- `Port Security` включен только там, где должен быть;
- violation mode соответствует политике;
- `DHCP Snooping` включен на нужных VLAN;
- trusted DHCP-порты выбраны правильно;
- binding table заполняется;
- `DAI` включен на нужных VLAN;
- trusted ARP-интерфейсы выбраны осознанно;
- нет неожиданных `err-disabled` портов.

## Сценарий Castle Rysen

Castle Rysen попросил внедрить Layer 2 security. Это звучит высокоуровнево, но инженер должен превратить это в стандарт.

Результат политики:

- end-device порты контролируются через `Port Security`;
- rogue DHCP server ограничивается через `DHCP Snooping`;
- `DHCP starvation` становится сложнее;
- ARP spoofing проверяется через `DAI`;
- uplink и инфраструктурные порты не ломаются из-за неправильного trust;
- конфигурацию можно повторить на других cafe location.

Это уже не набор команд. Это базовая модель защиты access layer.

## Главный вывод

Layer 2 security - это не магическая кнопка.

Это набор функций, которые должны совпадать с реальной топологией. `Port Security` контролирует, кто подключается. `DHCP Snooping` контролирует, кто может выдавать IP-настройки. `DAI` контролирует, кто может правдоподобно заявлять IP-to-MAC соответствия.

Вместе они делают switch не просто устройством пересылки кадров, а первой линией защиты локальной сети. Но только если внедрены как политика, а не как случайный набор команд.

## Команды и термины

| Термин | Значение |
| --- | --- |
| Layer 2 security | Защита на уровне коммутации Ethernet. |
| `Port Security` | Ограничивает MAC-адреса на access-порту. |
| `DHCP Snooping` | Блокирует DHCP server replies на untrusted-портах. |
| `Dynamic ARP Inspection` | Проверяет ARP-сообщения по доверенной таблице. |
| `DAI` | Сокращение от `Dynamic ARP Inspection`. |
| `DHCP starvation` | Попытка исчерпать DHCP pool множеством запросов. |
| `ARP spoofing` | Подмена ARP-информации для перехвата трафика. |
| trusted port | Порт, которому разрешен инфраструктурный трафик для конкретной функции. |
| untrusted port | Порт, где трафик проверяется или ограничивается. |
| rollout | Плановое внедрение изменений. |

## Вопросы

### 1. Почему Layer 2 security лучше внедрять через политику?

Ответ: Политика делает настройки повторяемыми, проверяемыми и понятными для других администраторов.

### 2. Где обычно включают Port Security?

Ответ: На end-device access-портах, где ожидается ограниченное число MAC-адресов.

### 3. Какие порты обычно trusted для DHCP Snooping?

Ответ: Порты в сторону настоящего DHCP server, router или uplink, через который приходит DHCP offer.

### 4. Почему DAI нельзя включать вслепую?

Ответ: Static IP-устройства и инфраструктурные порты могут не соответствовать DHCP Snooping binding table и быть заблокированы.

### 5. Что объединяет Port Security, DHCP Snooping и DAI?

Ответ: Они защищают разные части access layer и вместе создают базовую Layer 2 security policy.

## Что повторить позже

- Маппинг access/uplink/trunk портов.
- Настройку `Port Security`.
- Trusted-порты для `DHCP Snooping`.
- Binding table.
- Trusted-интерфейсы для `DAI`.
- Проверочные show-команды.
