# Access Switch Security Baseline

Source: закрытая страница курса  
Date added: 2026-08-02  
Related plan item: Week 14 / Access switch security baseline  
Tags: switch security, security baseline, Port Security, DHCP Snooping, Dynamic ARP Inspection, access layer, template
Language: Russian
Translation pair: articles-en/2026-08/week-14/05-access-switch-security-baseline.md

## Кратко

- `Port Security`, `DHCP Snooping` и `Dynamic ARP Inspection` не должны оставаться только темами для экзамена.
- Следующий шаг - превратить их в стандартную процедуру для access switch.
- Политика может быть короткой: что включаем, где включаем, что проверяем, какие есть исключения.
- CLI template помогает применять защиту одинаково на каждом switch.
- Повторяемость важна для безопасности: случайные настройки создают случайные дыры.
- Хорошая baseline-политика начинается с лаборатории и потом переносится в production.

## Главное

- Security baseline - это стартовый набор защит, который применяется по умолчанию.
- Не нужно ждать инцидента, чтобы включить базовые функции access layer.
- Политика должна быть понятной, проверяемой и пригодной для передачи другому администратору.
- Template должен включать не только команды настройки, но и команды проверки.
- Исключения нужно записывать: uplink, trunk, wireless access point, static IP-устройства, IP phone + PC.
- Уверенность появляется не от просмотра уроков, а от повторяемой практики.

## Заметки

Многие изучают `Port Security`, `DHCP Snooping` и `Dynamic ARP Inspection`, сдают проверку и идут дальше. Это ловушка.

Эти функции важны не потому, что они есть в CCNA. Они важны потому, что это практичная защита для обычных сетей. Не только для большого enterprise, не только для отдельной security-команды, а для любого инженера, который подключает коммутаторы и отвечает за access layer.

Правильный вопрос после этой темы:

```text
Как я буду защищать access switch по умолчанию?
```

Ответом должна стать не память, а процедура.

## Политика вместо импровизации

Если бы мы строили NetworkChuck Coffee, эти настройки не должны были бы жить только в голове администратора.

Нужен короткий документ:

- какие функции включаются на новом switch;
- какие VLAN защищаются;
- какие порты считаются access;
- какие порты trusted;
- какой violation mode используется;
- какие show-команды запускаются после внедрения;
- какие исключения допустимы.

Политика не обязана быть огромным документом. Для начала достаточно одной страницы в knowledge base или чеклиста в репозитории.

Главное, чтобы она отвечала на вопрос:

```text
Что мы делаем каждый раз, когда вводим access switch в работу?
```

## Почему повторяемость важна

Consistency - часть безопасности.

Если один switch настроен аккуратно, второй частично, а третий вообще без защиты, сеть становится непредсказуемой.

Типовые последствия:

- rogue DHCP server проходит там, где забыли `DHCP Snooping`;
- лишнее устройство подключается там, где нет `Port Security`;
- ARP spoofing возможен в VLAN, где забыли `DAI`;
- troubleshooting занимает дольше, потому что нет единого стандарта;
- новый администратор не знает, на что опираться.

Без baseline каждая новая установка превращается в импровизацию. В production это плохая привычка.

## Минимальная политика access switch

Пример простой политики:

| Область | Правило |
| --- | --- |
| End-device access ports | Включить `Port Security`. |
| Fixed devices | Использовать `sticky MAC`, если устройство стабильно. |
| Patron/shared ports | Не использовать sticky без явной причины. |
| IP phone + PC | Проверить, нужен ли `maximum 2`. |
| DHCP | Включить `DHCP Snooping` на рабочих VLAN. |
| DHCP trusted | Доверять только uplink/router/server path. |
| ARP | Включить `DAI` после проверки `DHCP Snooping`. |
| Infrastructure ports | Рассматривать отдельно, не как обычные client ports. |
| Verification | Запускать show-команды после каждого rollout. |

Это не финальный стандарт для любой компании. Это стартовая точка, которую нужно адаптировать к своей сети.

## Пример CLI Template

Шаблон должен быть чистым и предсказуемым.

```text
! Global Layer 2 security baseline
ip dhcp snooping
ip dhcp snooping vlan 10,20,30
ip arp inspection vlan 10,20,30

! Trusted uplink toward router/DHCP infrastructure
interface gi0/1
 description Uplink to infrastructure
 ip dhcp snooping trust
 ip arp inspection trust

! End-device access ports
interface range fa0/3-20
 switchport mode access
 switchport port-security
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation shutdown
 ip dhcp snooping limit rate 10
```

Это не команды для слепого копирования. Это структура:

- сначала глобальные функции;
- затем trusted-интерфейсы;
- затем access-порты;
- затем проверка.

Перед применением нужно заменить VLAN, интерфейсы и исключения под реальную площадку.

## Проверочный блок

Template без проверки - половина работы.

После настройки нужны команды:

```text
show port-security
show ip dhcp snooping
show ip dhcp snooping binding
show ip arp inspection
show ip arp inspection interfaces
show interfaces status err-disabled
show interfaces trunk
```

Проверить нужно:

- включены ли функции на нужных VLAN;
- правильно ли отмечены trusted-порты;
- не попали ли клиентские порты в trusted без причины;
- есть ли binding table;
- нет ли неожиданных `err-disabled`;
- соответствует ли фактическая конфигурация политике.

## Исключения

Хороший стандарт должен явно описывать исключения.

Примеры:

- uplink между switch;
- trunk к другому switch;
- router или firewall;
- wireless access point с множеством клиентов;
- server со static IP;
- IP phone с PC за ним;
- временный lab-порт;
- порт для troubleshooting.

Исключение не означает "настроим как-нибудь". Оно означает: причина понятна, риск принят, конфигурация записана.

## Практический план

Дальше стоит сделать три вещи:

1. Написать одностраничную baseline-политику для access switch.
2. Собрать CLI template из этой политики.
3. Прогнать template в lab до состояния, когда настройка и проверка не вызывают сомнений.

Это лучше, чем просто смотреть еще материалы и ждать уверенности.

Уверенность появляется от цикла:

```text
настроил -> сломал -> проверил -> исправил -> повторил
```

Так команды превращаются в рабочий навык.

## Сценарий NetworkChuck Coffee

Для новой площадки NetworkChuck Coffee администратор не должен начинать с пустого листа.

У него уже есть baseline:

- access-порты получают `Port Security`;
- DHCP защищается через `DHCP Snooping`;
- ARP проверяется через `DAI`;
- infrastructure path помечается trusted;
- исключения документируются;
- после rollout запускаются show-команды.

Так сеть строится по стандарту, а не по настроению.

## Главный вывод

Базовая Layer 2 security должна стать привычкой.

`Port Security`, `DHCP Snooping` и `Dynamic ARP Inspection` - это не просто CCNA-темы. Это строительные блоки нормальной access-layer защиты.

Когда ты превращаешь их в policy и template, ты перестаешь просто знать команды. Ты начинаешь проектировать процесс, который можно повторить, проверить и передать другому инженеру.

## Команды и термины

| Термин | Значение |
| --- | --- |
| security baseline | Минимальный стандарт защит, применяемый по умолчанию. |
| CLI template | Повторяемый набор команд для типовой настройки. |
| `Port Security` | Ограничивает MAC-адреса на access-порту. |
| `DHCP Snooping` | Блокирует DHCP-ответы на untrusted-портах. |
| `Dynamic ARP Inspection` | Проверяет ARP по доверенной таблице. |
| trusted port | Порт, которому разрешен инфраструктурный трафик. |
| exception | Осознанное отклонение от baseline с документированной причиной. |
| rollout | Плановое внедрение конфигурации. |

## Вопросы

### 1. Почему эти функции нельзя оставлять только как материал для экзамена?

Ответ: Они решают реальные проблемы access layer и должны стать частью стандартной настройки.

### 2. Что должно быть в baseline-политике?

Ответ: Правила включения функций, trusted-порты, VLAN, исключения и команды проверки.

### 3. Почему template должен включать verification-команды?

Ответ: Без проверки нельзя доказать, что настройка реально работает и соответствует политике.

### 4. Почему исключения нужно документировать?

Ответ: Иначе они превращаются в скрытые риски и усложняют troubleshooting.

### 5. Как превратить команды в навык?

Ответ: Повторять настройку в lab, проверять результат, ломать сценарии и исправлять ошибки.

## Что повторить позже

- Одностраничную access switch baseline policy.
- CLI template для Layer 2 security.
- Исключения для uplink, trunk и static IP.
- Проверочные команды.
- Порядок lab-тестирования.
- Разницу между знанием команды и повторяемым процессом.
