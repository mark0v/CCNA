# Configuring VLAN Trunks

Source: закрытая страница курса  
Date added: 2026-06-20  
Related plan item: Week 8 / Configuring VLAN trunks  
Tags: VLAN, trunk port, 802.1Q, subnetting, allowed VLANs, show interfaces trunk
Language: Russian
Translation pair: articles-en/2026-06/week-08/06-configuring-vlan-trunks.md

## Кратко

Создать VLAN на одном switch недостаточно. Если VLAN должна существовать на нескольких switches, ее traffic нужно перенести между ними. Для этого используются trunk ports.

Trunk port - это switch port, который может переносить traffic нескольких VLANs одновременно.

Ключевые идеи:

- access port принадлежит одной VLAN;
- trunk port переносит несколько VLANs;
- trunk links обычно соединяют switches между собой;
- 802.1Q tagging показывает, к какой VLAN относится frame;
- VLAN обычно соответствует отдельной IP subnet;
- devices в одной VLAN и одной subnet должны общаться через trunk;
- devices в разных VLANs не должны общаться без routing.

Trunk превращает VLAN из локального объекта на одном switch в logical network, которая может span multiple switches.

## VLAN Нужна Не Только Как Имя

VLAN - это не просто label на ports.

VLAN означает отдельный broadcast domain. В большинстве практических designs этот broadcast domain соответствует отдельной IP subnet.

Например:

```text
VLAN 10 Admin:   10.0.18.0/27
VLAN 20 Patron:  10.0.18.32/27
```

Если раньше store использовал один `/26`, а теперь нужны две VLANs, можно split этот `/26` на два `/27`.

Это сохраняет larger addressing plan, но дает две отдельные сети внутри одного site allocation.

Пример:

```text
Original store subnet: 10.0.18.0/26

Split into:
10.0.18.0/27   -> Admin VLAN
10.0.18.32/27  -> Patron VLAN
```

Так один store остается внутри своего original block, но получает logical separation.

## Почему Subnetting Возвращается

VLANs и subnetting почти всегда идут вместе.

Если ты создаешь две VLANs, тебе обычно нужны две IP subnets.

Иначе получится странная ситуация: на Layer 2 ты вроде разделил devices, но на Layer 3 не дал им отдельные address spaces.

Хорошее правило:

```text
One VLAN = one broadcast domain = one IP subnet
```

Это не просто memorized phrase. Это practical design habit.

VLAN без правильной subnet за ней похожа на новую комнату без стен. Название есть, но настоящего разделения нет.

## Что Делает Trunk

Access port используется для endpoint device и принадлежит одной VLAN.

Например:

```text
PC port -> VLAN 10 only
Camera port -> VLAN 30 only
Printer port -> VLAN 20 only
```

Trunk port используется для infrastructure links.

Например:

```text
Switch 1 <-> Switch 2
Switch <-> Router
Switch <-> Firewall
Switch <-> Layer 3 switch
```

Trunk переносит traffic нескольких VLANs:

```text
Trunk link carries VLAN 10, VLAN 20, VLAN 30, VLAN 99
```

Это позволяет devices в одной VLAN оставаться в одной logical network, даже если они подключены к разным switches.

## Настройка Trunk Port

Базовая команда:

```text
Switch(config-if)# switchport mode trunk
```

Эта команда переводит port в trunk mode.

Если trunk настраивается между двумя switches, обе стороны link должны быть правильно настроены.

Пока настройки на сторонах не совпадают, link может briefly flap. В lab это нормально. В production это может вызвать outage, поэтому такие изменения нужно планировать.

## 802.1Q Tagging

Когда traffic идет через trunk, switch должен знать, к какой VLAN относится каждый frame.

Для этого используется 802.1Q tag.

Простая схема:

```text
Frame from VLAN 10 enters trunk
Switch adds 802.1Q VLAN tag
Frame crosses trunk
Next switch reads tag
Frame is placed back into VLAN 10
```

802.1Q - industry standard для VLAN tagging.

Старый Cisco proprietary вариант назывался ISL. Сейчас в нормальных современных сетях основной стандарт - 802.1Q.

## Как Доказать, Что Trunk Работает

Важно не просто настроить trunk, а проверить behavior.

Практическая проверка:

1. На Switch 1 назначить PC в VLAN 10.
2. На Switch 2 назначить другой PC в VLAN 10.
3. Дать обоим IP addresses из одной subnet.
4. Выполнить ping между ними.

Если ping проходит, значит VLAN 10 traffic корректно переносится через trunk.

Пример:

```text
PC-A on Switch 1 -> VLAN 10 -> 10.0.18.10/27
PC-B on Switch 2 -> VLAN 10 -> 10.0.18.11/27

Ping should work.
```

Это доказывает, что VLAN 10 не trapped на одном switch. Она stretched across switches через trunk.

## Проверка Separation

После этого полезно проверить обратное.

Перемести один PC в другую VLAN, например VLAN 20, и дай ему address из другой subnet.

```text
PC-A on Switch 1 -> VLAN 10 -> 10.0.18.10/27
PC-B on Switch 2 -> VLAN 20 -> 10.0.18.40/27

Ping should fail without routing.
```

Если ping перестал проходить, это хорошо.

Это значит:

- VLAN separation работает;
- devices находятся в разных broadcast domains;
- traffic между VLANs не проходит без Layer 3 routing.

Это не ошибка. Это design.

## show interfaces trunk

После настройки trunk нужно проверять trunk state.

Команда:

```text
Switch# show interfaces trunk
```

Она помогает увидеть:

- какие ports работают как trunks;
- какой encapsulation используется;
- какие VLANs allowed on trunk;
- какие VLANs active;
- какие VLANs forwarding.

Это одна из главных команд для VLAN/trunk troubleshooting.

## Allowed VLAN List: Команда, Которая Может Сломать День

Trunk может переносить много VLANs, но sometimes нужно ограничить список VLANs, allowed на trunk.

Это полезно:

- чтобы не переносить лишний traffic;
- чтобы уменьшить broadcast noise;
- чтобы не отправлять VLANs туда, где они не нужны;
- чтобы улучшить security posture.

Но здесь есть опасный момент.

Команда вида:

```text
switchport trunk allowed vlan 10
```

не добавляет VLAN 10 к списку.

Она заменяет allowed list и оставляет только VLAN 10.

Если на trunk до этого шли VLAN 20, 30, 99, management VLAN или voice VLAN, ты можешь случайно отрезать их одним command.

Для добавления нужно использовать `add`:

```text
switchport trunk allowed vlan add 10
```

Для удаления:

```text
switchport trunk allowed vlan remove 10
```

После изменения всегда проверяй:

```text
show interfaces trunk
```

Это одна из тех команд, где маленькая разница в syntax может превратиться в большой outage.

## Почему VLAN Pruning Полезен

В больших networks не каждый switch должен видеть every VLAN.

Например, traffic dorm VLAN или guest VLAN не должен без причины ездить по links, где нет devices этой VLAN.

Ограничение allowed VLANs на trunks помогает:

- уменьшить unnecessary broadcast traffic;
- ограничить reach VLANs;
- сделать topology понятнее;
- снизить impact возможной проблемы;
- улучшить security boundaries.

Но pruning нужно делать deliberate, с документацией и проверкой.

## Что Было Доказано В Уроке

К концу этой части были доказаны две вещи.

Первое: trunk links переносят VLAN traffic между switches.

Второе: devices в одной VLAN и одной subnet могут общаться через разные switches, если trunk настроен правильно.

Также было доказано обратное: devices в разных VLANs не общаются без inter-VLAN routing.

Это именно то поведение, которое нужно:

```text
Same VLAN + same subnet + trunk works -> communication works
Different VLANs + no routing -> communication fails
```

## Что Дальше

Trunks позволяют VLANs span multiple switches.

Но trunks не дают devices из разных VLANs общаться между собой.

Для communication между VLAN 10 и VLAN 20 нужен Layer 3:

- router;
- Layer 3 switch;
- firewall.

Это называется inter-VLAN routing.

Мы построили walls. Дальше нужно carefully add doors.

