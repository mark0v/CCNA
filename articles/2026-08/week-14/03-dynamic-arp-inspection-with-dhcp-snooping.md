# Dynamic ARP Inspection With DHCP Snooping

Source: закрытая страница курса  
Date added: 2026-08-02  
Related plan item: Week 14 / Dynamic ARP Inspection with DHCP Snooping  
Tags: Dynamic ARP Inspection, DAI, DHCP Snooping, ARP spoofing, man-in-the-middle, switch security, Layer 2 security
Language: Russian
Translation pair: articles-en/2026-08/week-14/03-dynamic-arp-inspection-with-dhcp-snooping.md

## Кратко

- `Dynamic ARP Inspection` защищает от поддельных ARP-ответов.
- ARP по умолчанию доверчив: устройство спрашивает, кто владеет IP-адресом, и верит ответу.
- Атакующий может использовать `ARP spoofing`, чтобы выдать свой MAC-адрес за адрес сервера или gateway.
- `DAI` проверяет ARP-сообщения на untrusted-портах.
- Для проверки `DAI` обычно использует binding table, созданную `DHCP Snooping`.
- Uplink, trunk и порты со static IP-устройствами требуют особого внимания.
- Неправильное внедрение `DAI` может сломать нормальный ARP-трафик.

## Главное

- `DAI` не работает в вакууме: ему нужна достоверная таблица соответствий IP-to-MAC.
- `DHCP Snooping` создает основу доверия, а `DAI` использует ее для проверки ARP.
- Access-порты пользователей обычно остаются untrusted.
- Порты к инфраструктуре и uplink часто должны быть trusted или заранее учтены.
- Static IP-устройства могут отсутствовать в DHCP Snooping binding table.
- На untrusted-портах может действовать ARP rate limit.
- Перед включением в production нужно найти trunk, uplink, static-IP устройства и нестандартные edge-порты.

## Заметки

ARP выглядит безобидно. Устройство спрашивает: "У кого этот IP-адрес?" Другое устройство отвечает своим MAC-адресом. После этого клиент отправляет кадры на полученный MAC.

Проблема в том, что ARP сам по себе почти не проверяет правду. Если злонамеренное устройство ответит быстрее настоящего сервера или gateway, клиент может поверить ему.

Так появляется `ARP spoofing`: атакующий говорит "этот IP принадлежит мне", хотя это ложь. Дальше трафик может пройти через устройство атакующего. Это классический `man-in-the-middle`.

`Dynamic ARP Inspection`, или `DAI`, добавляет проверку. Коммутатор начинает смотреть на ARP-сообщения и сравнивать заявления устройств с тем, что уже известно из доверенной таблицы.

## Какую проблему решает DAI

Представим NetworkChuck Coffee.

Кассовый терминал хочет поговорить с сервером в back office. Он отправляет ARP-запрос:

```text
Кто владеет этим IP-адресом?
```

Настоящий сервер должен ответить своим MAC-адресом. Но rogue laptop в той же сети может ответить раньше:

```text
Этот IP - мой. Отправляй трафик мне.
```

Если клиент поверит, чувствительный трафик может пойти не туда.

`DAI` останавливает такую подмену. Он проверяет ARP-ответы и отбрасывает те, где IP и MAC не совпадают с известной привязкой.

## Связь с DHCP Snooping

`DAI` опирается на `DHCP Snooping`.

Когда клиент получает адрес через DHCP, switch видит:

- MAC-адрес клиента;
- полученный IP-адрес;
- VLAN;
- интерфейс.

Эта информация попадает в binding table.

Упрощенно:

```text
MAC address + IP address + VLAN + interface
```

После этого `DAI` может проверять ARP:

```text
Если устройство говорит, что владеет этим IP, его MAC должен совпадать с binding table.
```

Если совпадения нет, ARP-сообщение отбрасывается.

## Базовая настройка

Сначала нужен `DHCP Snooping`:

```text
ip dhcp snooping
ip dhcp snooping vlan 10,20
```

Потом включается ARP inspection для нужных VLAN:

```text
ip arp inspection vlan 10,20
```

Затем на нужных интерфейсах задается доверие:

```text
interface gi0/1
 ip arp inspection trust
```

Разбор:

| Команда | Что означает |
| --- | --- |
| `ip arp inspection vlan 10,20` | Включает `DAI` для VLAN 10 и VLAN 20. |
| `ip arp inspection trust` | Помечает интерфейс как trusted для ARP inspection. |
| `ip dhcp snooping` | Создает базу для binding table. |

По умолчанию порты считаются untrusted, и ARP-сообщения на них проверяются.

## Что нужно доверять

Перед включением `DAI` нужно пройтись по топологии.

Особенно важны:

- uplink между switch;
- trunk-порты;
- порты к router;
- порты к firewall;
- серверы со static IP;
- wireless access point с множеством клиентов;
- контроллеры и другие инфраструктурные устройства.

Почему это важно: не все устройства получают адрес по DHCP. Если устройство использует static IP, его может не быть в DHCP Snooping binding table. Тогда `DAI` может увидеть нормальный ARP-ответ и решить, что это подделка.

Есть два типовых подхода:

- сделать инфраструктурный интерфейс trusted;
- добавить корректную статическую привязку, если платформа и дизайн это поддерживают.

Главное - не включать `DAI` вслепую.

## Валидация ARP

`DAI` может выполнять дополнительные проверки.

Часто встречаются проверки:

- source MAC;
- destination MAC;
- IP address.

Идея простая: switch сравнивает то, что указано в ARP-пакете, с тем, что должно быть правдой.

Source MAC и IP address особенно важны против классической подмены, когда атакующий говорит: "Я владею этим IP", но его MAC-адрес не совпадает с известной привязкой.

Destination MAC validation может дать дополнительную защиту, но с ней нужно быть аккуратным. Например, `gratuitous ARP` иногда используется легитимно, в том числе в first-hop redundancy сценариях. Чем строже проверка, тем важнее понимать реальные edge cases.

## Ограничение частоты ARP

На untrusted-портах `DAI` может ограничивать количество ARP-пакетов в секунду.

Для обычного пользовательского ПК это полезно. Массовый поток ARP может быть признаком атаки или ошибки.

Но один порт не всегда означает одно устройство. Через wireless access point или маленький downstream-сегмент может проходить ARP-трафик многих клиентов. Тогда стандартный rate limit нужно проверить до rollout.

Иначе защита начнет выглядеть как случайные проблемы связи.

## Проверка

Полезные команды:

```text
show ip arp inspection
show ip arp inspection vlan 10
show ip arp inspection interfaces
show ip dhcp snooping binding
show running-config | include arp inspection
```

Что смотреть:

- включен ли `DAI` на нужных VLAN;
- какие интерфейсы trusted;
- какие интерфейсы untrusted;
- есть ли binding table;
- подходят ли ARP rate limits;
- нет ли статических устройств, которые не попали в таблицу.

## Сценарий NetworkChuck Coffee

В NetworkChuck Coffee `DHCP Snooping` уже защищает сеть от rogue DHCP server и строит binding table.

Следующий шаг - включить `DAI`, чтобы:

- проверять ARP-ответы на access-портах;
- блокировать попытки выдать чужой IP за свой;
- уменьшить риск `man-in-the-middle`;
- использовать данные, которые уже собрал `DHCP Snooping`.

Но перед этим нужно отметить trusted uplink, trunk и инфраструктурные порты. Иначе можно защитить сеть так хорошо, что она перестанет нормально работать.

## Главный вывод

`DAI` заставляет ARP-ответы доказывать правду.

Если устройство заявляет, что владеет IP-адресом, switch проверяет это заявление по binding table от `DHCP Snooping`. Если IP и MAC не совпадают, ARP-сообщение отбрасывается.

Это мощная защита Layer 2, но она требует планирования. Сначала строится доверенная DHCP-база, затем включается inspection, потом аккуратно настраиваются trusted-интерфейсы и проверяется поведение сети.

## Команды и термины

| Термин | Значение |
| --- | --- |
| `Dynamic ARP Inspection` | Функция switch, проверяющая ARP-сообщения. |
| `DAI` | Сокращение от `Dynamic ARP Inspection`. |
| `ARP spoofing` | Подмена ARP-ответов для выдачи себя за другой IP. |
| `DHCP Snooping binding table` | Таблица соответствий MAC, IP, VLAN и interface. |
| `trusted interface` | Интерфейс, ARP-трафику с которого доверяют. |
| `untrusted interface` | Интерфейс, где ARP-трафик проверяется. |
| `gratuitous ARP` | ARP-сообщение без предварительного запроса. |
| `man-in-the-middle` | Сценарий, где атакующий оказывается между участниками обмена. |
| ARP rate limit | Ограничение количества ARP-пакетов на untrusted-порту. |

## Вопросы

### 1. От какой атаки защищает DAI?

Ответ: От `ARP spoofing`, который может привести к `man-in-the-middle`.

### 2. Почему DAI зависит от DHCP Snooping?

Ответ: `DHCP Snooping` строит binding table, по которой `DAI` проверяет IP-to-MAC соответствия.

### 3. Почему static IP-устройства требуют внимания?

Ответ: Их может не быть в DHCP Snooping binding table, поэтому DAI может заблокировать их ARP-трафик.

### 4. Какие порты чаще всего проверяют перед включением DAI?

Ответ: Uplink, trunk, router/firewall порты, серверы со static IP и wireless access point.

### 5. Что нужно проверить после включения DAI?

Ответ: VLAN с ARP inspection, trusted/untrusted интерфейсы, binding table и ARP rate limits.

## Что повторить позже

- Настройку `ip arp inspection vlan`.
- Роль `DHCP Snooping binding table`.
- Разницу между trusted и untrusted интерфейсами.
- Риски static IP-устройств.
- Проверочные команды `show ip arp inspection`.
- ARP rate limit на untrusted-портах.
