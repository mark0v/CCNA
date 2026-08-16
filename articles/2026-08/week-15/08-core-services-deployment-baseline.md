# Core Services Deployment Baseline

Source: закрытая страница курса  
Date added: 2026-08-16  
Related plan item: Week 15 / Core services deployment baseline  
Tags: core services, NTP, DHCP, DNS, SSH, baseline configuration, deployment template, operations
Language: Russian
Translation pair: articles-en/2026-08/week-15/08-core-services-deployment-baseline.md

## Кратко

- `NTP`, `DHCP`, `DNS` и `SSH` должны стать частью базового deployment checklist.
- Эти сервисы не extras, а основа нормальной эксплуатации network devices.
- `NTP` дает согласованное время.
- `DHCP` автоматизирует выдачу IP-настроек там, где это нужно.
- `DNS` делает имена удобными для людей и приложений.
- `SSH` обеспечивает защищенный remote management.
- Цель - не запомнить четыре acronym, а встроить их в стандарт настройки.

## Главное

- Если после темы не меняется способ настройки устройств, знания остаются trivia.
- Каждый новый device должен рассматриваться как часть системы, зависящей от core services.
- Baseline template снижает шанс забыть важные "скучные" настройки.
- Core services нужно проверять при deployment, а не ждать первого outage.
- Разные environments отличаются, но базовый список сервисов повторяется постоянно.
- Хороший стандарт делает сеть manageable, predictable и supportable.

## Заметки

Многие уроки заканчиваются ощущением "я посмотрел, значит знаю". Но для network operations этого мало.

Настоящий результат появляется, когда знания превращаются в стандарт:

```text
Каждое устройство получает базовый набор core services.
```

Switch, router или firewall - это не просто hostname и IP address. Это device, который должен жить в управляемой среде: с правильным временем, именами, адресацией и безопасным доступом.

## Четыре базовых сервиса

Для NetworkChuck Coffee базовый набор выглядит так:

| Сервис | Зачем нужен |
| --- | --- |
| `NTP` | Синхронизирует время для logs, troubleshooting и security events. |
| `DHCP` | Выдает IP settings там, где design требует автоматической адресации. |
| `DNS` | Превращает names в IP addresses и делает сеть удобной. |
| `SSH` | Дает secure remote access для управления devices. |

`SSH` легко воспринимать как отдельную security-тему, но на практике он должен быть в baseline. Remote management без SSH в современной сети выглядит устаревшим и опасным.

## Почему это не мелочи

Router может route без DNS. Switch может switch без NTP. Device может быть reachable без SSH.

Но production network от этого не становится нормальной.

Без core services появляются проблемы:

- logs нельзя надежно сопоставить по времени;
- новые clients не получают настройки;
- apps и internal resources не открываются по names;
- admins заходят через insecure протоколы;
- troubleshooting становится медленным;
- deployment зависит от памяти конкретного инженера.

Common не значит unimportant. Часто самые обычные вещи и являются фундаментом.

## Шаблон вместо памяти

Нельзя полагаться на "я потом вспомню".

Нужен base configuration template:

- для routers;
- для switches;
- для firewalls;
- для lab devices;
- для branch sites;
- для cafe locations.

Template должен отвечать:

- откуда device получает time;
- какой DNS server он использует;
- нужен ли DHCP server, client или relay;
- включен ли SSH;
- отключен ли Telnet;
- какие verification commands нужно выполнить;
- какие exceptions допустимы.

Так deployment перестает быть импровизацией.

## Минимальный checklist

Базовый порядок мыслей:

1. Настроить hostname и management identity.
2. Настроить `NTP` или указать NTP servers.
3. Настроить `DNS` через `ip name-server` и local mappings, если нужны.
4. Настроить `DHCP`, если device участвует как server, client или relay.
5. Настроить `SSH`.
6. Ограничить VTY lines через `transport input ssh`.
7. Проверить services show-командами.
8. Сохранить configuration.
9. Обновить documentation.

Это не заменяет полный design. Это baseline, который предотвращает забытые базовые вещи.

## Пример baseline-фрагментов

NTP:

```text
ntp server 10.255.0.1
show ntp status
show clock detail
```

DNS:

```text
ip name-server 10.1.0.53
ip domain-name cafe.local
show hosts
```

DHCP:

```text
ip dhcp excluded-address 192.168.10.1 192.168.10.20
ip dhcp pool CAFE-VLAN10
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 10.1.0.53
show ip dhcp binding
```

SSH:

```text
username admin secret StrongPasswordHere
crypto key generate rsa modulus 2048
ip ssh version 2
line vty 0 4
 login local
 transport input ssh
show ip ssh
```

Эти snippets нужно адаптировать под конкретную сеть. Их ценность в том, что они напоминают: baseline должен быть полным, а не случайным.

## Сценарий NetworkChuck Coffee

NetworkChuck Coffee открывает новую точку.

Если новый switch получает только basic config, он может пропускать traffic. Но будущая поддержка будет слабой:

- logs без правильного time;
- no name resolution;
- непонятная DHCP role;
- insecure или недонастроенный remote access;
- нет единого deployment standard.

Если применяется baseline:

- устройство сразу синхронизирует time;
- использует правильный DNS;
- участвует в DHCP design там, где нужно;
- доступно по SSH;
- проверено show-командами;
- внесено в documentation.

Это разница между "оно включилось" и "его можно поддерживать".

## Привычка инженера

Опытный engineer не начинает с fancy features.

Он сначала проверяет фундамент:

- clock;
- reachability;
- name resolution;
- address assignment;
- secure management;
- logging;
- documentation.

Так появляется traction в новой среде. Не потому что engineer знает все команды мира, а потому что знает, какие вещи почти всегда важны.

## Проверка

Команды:

```text
show clock detail
show ntp status
show ntp associations
show hosts
show running-config | include ip name-server
show ip dhcp pool
show ip dhcp binding
show ip ssh
show running-config | section line vty
```

Что подтвердить:

- time source корректный;
- NTP synchronized;
- DNS server задан;
- name resolution работает;
- DHCP role понятна;
- DHCP bindings появляются, если device server;
- SSH enabled;
- Telnet закрыт;
- configuration сохранена;
- documentation обновлена.

## Главный вывод

Core services - не дополнительные украшения.

`NTP`, `DHCP`, `DNS` и `SSH` делают network devices удобными для эксплуатации: время совпадает, адреса выдаются, имена работают, remote management защищен.

Если эти сервисы встроены в deployment template, сеть становится predictable. Если они зависят от памяти и настроения, они обязательно будут забыты в самый неудобный момент.

## Команды и термины

| Термин | Значение |
| --- | --- |
| core services | Базовые сервисы, нужные для нормальной эксплуатации сети. |
| `NTP` | Синхронизация времени. |
| `DHCP` | Автоматическая выдача IP-настроек. |
| `DNS` | Name resolution. |
| `SSH` | Защищенный remote management. |
| baseline template | Базовый повторяемый шаблон настройки. |
| `transport input ssh` | Ограничивает VTY remote access только SSH. |
| `ip name-server` | Указывает DNS server для Cisco device. |
| `ntp server` | Указывает NTP server. |
| `ip helper-address` | DHCP relay command. |

## Вопросы

### 1. Какие четыре core services нужно держать в голове?

Ответ: `NTP`, `DHCP`, `DNS` и `SSH`.

### 2. Почему SSH относится к baseline, а не только к security section?

Ответ: Почти каждое управляемое device должно иметь secure remote access с самого начала.

### 3. Почему template лучше памяти?

Ответ: Template делает deployment повторяемым и снижает риск забыть базовые настройки.

### 4. Что отличает "устройство включилось" от "устройство можно поддерживать"?

Ответ: Наличие time sync, DNS, понятной DHCP role, secure remote access, проверки и документации.

### 5. Почему core services нужно проверять сразу?

Ответ: Если они сломаны или забыты, будущий troubleshooting станет медленнее и дороже.

## Что повторить позже

- Baseline template для routers и switches.
- Проверку `NTP`.
- Проверку `DNS`.
- DHCP roles: server, client, relay.
- SSH setup и `transport input ssh`.
- Документирование core services для каждого site.
