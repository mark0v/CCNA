# Disabling DTP And VTP Risk

Source: закрытая страница курса  
Date added: 2026-06-20  
Related plan item: Week 8 / VLAN-related Cisco protocols and hardening  
Tags: DTP, VTP, VLAN, trunking, Cisco, switch hardening, VLAN hopping
Language: Russian
Translation pair: articles-en/2026-06/week-08/08-disabling-dtp-and-vtp-risk.md

## Кратко

Некоторые Cisco features были созданы для удобства, но в современных production networks их часто предпочитают отключать.

Два важных примера:

- DTP - Dynamic Trunking Protocol;
- VTP - VLAN Trunking Protocol.

Оба протокола Cisco proprietary. Оба были задуманы как automation. Оба могут создать unnecessary risk, если оставить их без контроля.

Практический вывод:

```text
Access ports should be access ports.
Trunk ports should be trunk ports.
VLAN databases should not magically change across the network.
```

Чем меньше guessing и hidden automation, тем легче troubleshooting и тем меньше attack surface.

## DTP: Переговоры О Trunk Mode

DTP означает Dynamic Trunking Protocol.

Он позволяет switch ports договариваться, должны ли они стать trunk link.

Trunk link переносит traffic нескольких VLANs. Access port принадлежит одной VLAN.

Идея DTP звучит удобно:

```text
Switch ports negotiate automatically.
If trunk is needed, trunk forms.
```

Но в real network это часто не то поведение, которое хочется видеть.

Если engineer хочет trunk, он может явно настроить trunk:

```text
switchport mode trunk
```

Если engineer хочет access port, он может явно настроить access:

```text
switchport mode access
```

Network становится понятнее, когда port behavior задан явно.

## DTP Modes

DTP использует negotiation modes.

Главные идеи:

```text
dynamic auto       -> I can become trunk if the other side asks
dynamic desirable  -> I want to become trunk
trunk              -> I am trunk
access             -> I am access
```

Примеры поведения:

```text
desirable + auto       -> trunk forms
desirable + desirable  -> trunk forms
auto + auto            -> trunk does not form
```

Для экзамена эти combinations нужно понимать.

Для real work чаще проще убрать negotiation и настроить port mode вручную.

## Почему DTP Может Быть Опасен

Если DTP включен на user-facing port, rogue device может попытаться negotiated trunk.

Это опасно, потому что trunk может переносить traffic нескольких VLANs.

Сценарий:

1. Attacker подключает устройство в открытый wall jack.
2. Port оставлен в dynamic mode.
3. Устройство пытается договориться о trunk.
4. Если trunk formed, attacker может попытаться получить доступ к VLANs, которые ему не предназначены.

Это связано с риском VLAN hopping.

VLAN hopping - это ситуация, где device пытается попасть в VLANs, к которым у него не должно быть доступа.

## switchport nonegotiate

Команда, которая отключает DTP negotiation на interface:

```text
switchport nonegotiate
```

После этого port не пытается договариваться о trunk mode.

Обычно подход такой:

Для access port:

```text
interface FastEthernet0/10
 switchport mode access
 switchport access vlan 20
 switchport nonegotiate
```

Для trunk port:

```text
interface GigabitEthernet0/1
 switchport mode trunk
 switchport nonegotiate
```

Важно: если отключаешь negotiation, обе стороны trunk должны быть настроены явно.

## Практическое Правило Для DTP

На production switches лучше hard-code port behavior:

```text
User-facing ports -> access
Infrastructure links -> trunk
Unused ports -> shutdown
```

Идея простая: port должен делать то, что ты ему сказал, а не обсуждать это с неизвестным устройством.

Это помогает:

- уменьшить ambiguity;
- сделать troubleshooting быстрее;
- снизить риск accidental trunk;
- уменьшить attack surface;
- сделать configuration более читаемой.

## VTP: Название Сбивает С Толку

VTP означает VLAN Trunking Protocol.

Название может запутать: VTP не является trunking method.

Trunking method для VLAN traffic - это 802.1Q tagging.

VTP делает другое: распространяет VLAN database между switches.

Например:

```text
Create VLAN 10 on one switch
VTP advertises VLAN 10
Other switches learn/create VLAN 10
```

Идея была удобной: create once, replicate everywhere.

Но проблема в том, что VTP может распространять не только creation, но и deletion.

## Почему VTP Может Быть Рискованным

В большой сети автоматическое распространение VLAN database может быть опасным.

Один неправильный switch или одна неправильная VLAN deletion может повлиять на many switches.

Типичные неприятные сценарии:

- кто-то удаляет VLAN на switch, который участвует в VTP как server;
- deletion распространяется по VTP domain;
- VLAN исчезает на других switches;
- ports теряют logical networks;
- users, phones, servers или management connectivity ломаются.

Другой сценарий:

- старый lab switch подключают в production;
- на нем осталась другая VLAN database;
- он участвует в VTP;
- network получает неожиданные VLAN updates.

Автоматизация удобна, пока она не автоматизирует ошибку.

## VTP Modes

Традиционно VTP имеет три основных режима.

### Server

Switch может:

- создавать VLANs;
- удалять VLANs;
- изменять VLAN database;
- advertising эти changes другим switches.

На многих старых switches server был default mode, что делало VTP особенно опасным.

### Client

Switch:

- принимает VTP updates;
- применяет VLAN database от server;
- не создает и не удаляет VLANs locally.

Звучит безопаснее, но switch все равно зависит от updates.

### Transparent

Switch:

- управляет своей VLAN database самостоятельно;
- не принимает чужие VTP updates для своей VLAN database;
- не распространяет свои VLAN changes как server.

Именно transparent mode часто предпочитают в modern networks.

Команда:

```text
vtp mode transparent
```

## VTP Domain

VTP domain - это имя, которое определяет, какие switches должны обмениваться VTP information.

Важно: domain name case-sensitive.

Например:

```text
COOKIE
cookie
```

Это разные domains.

Но даже domain boundary не отменяет главный operational risk: если ты не хочешь автоматического распространения VLAN database, лучше не полагаться на VTP.

## Что Обычно Делать В Production

Практический подход:

```text
DTP:
  Manually set access/trunk mode
  Disable negotiation where appropriate

VTP:
  Use transparent mode unless there is a deliberate reason not to
```

Примеры:

```text
switchport mode access
switchport nonegotiate
```

```text
switchport mode trunk
switchport nonegotiate
```

```text
vtp mode transparent
```

Цель не в том, чтобы выключить все подряд. Цель - убрать automation, которую ты не контролируешь и которая не нужна для design.

## Exam Vs Real World

Для экзамена нужно знать:

- что такое DTP;
- что такое VTP;
- DTP modes и когда trunk formed;
- VTP modes;
- что делает `switchport nonegotiate`;
- что делает `vtp mode transparent`;
- что 802.1Q отвечает за tagging, а не VTP.

Для real world нужно еще и judgment:

```text
Just because a feature exists does not mean it should be enabled.
```

Иногда профессиональный design - это boring design:

- explicit port modes;
- no unnecessary negotiation;
- predictable VLAN database;
- documented trunks;
- checked allowed VLANs;
- fewer surprises.

## Главный Вывод

DTP и VTP были созданы для удобства, но удобство может стать risk.

DTP может случайно или нежелательно превратить port в trunk.

VTP может распространить VLAN changes туда, где ты этого не хотел.

Поэтому practical baseline:

```text
Hard-code access ports.
Hard-code trunk ports.
Disable DTP negotiation where appropriate.
Use VTP transparent unless VTP is intentionally designed and controlled.
```

Хорошая сеть часто скучная в лучшем смысле: она делает именно то, что написано в config, и не пытается быть умнее engineer.

