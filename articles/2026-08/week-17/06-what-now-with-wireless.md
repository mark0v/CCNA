# What Now With Wireless

Source: закрытая страница курса  
Date added: 2026-08-21  
Related plan item: Week 17 / What now with wireless  
Tags: wireless, Wi-Fi, RF, access points, design, troubleshooting, coverage, interference, capacity
Language: Russian
Translation pair: articles-en/2026-08/week-17/06-what-now-with-wireless.md

## Кратко

- `CCNA` не уходит глубоко в wireless configuration, потому что тема быстро становится огромной.
- Главный вывод: wireless - это не Ethernet с антеннами.
- Wi-Fi работает в менее контролируемой среде: стены, стекло, люди, деревья, погода, соседние AP, Bluetooth и interference.
- Coverage не равен performance.
- Хороший Wi-Fi требует design, channel planning, понимания RF и проверки на месте.
- Лучший следующий шаг - строить, тестировать, наблюдать и корректировать.
- Wireless стоит уважать как отдельную специализацию, даже если ты не становишься wireless engineer сразу.

## Главное

- В wired networking путь сигнала намного более контролируемый.
- В wireless данные передаются через общую и шумную радиосреду.
- Packet loss, retries и interference - часть реальности Wi-Fi.
- Просто повесить WAP через каждые несколько метров - не design.
- Signal strength сам по себе не гарантирует хорошую работу.
- Для бизнеса плохой Wi-Fi может означать медленные платежи, недовольных клиентов и потерю денег.
- Практика на доме, офисе, церкви или маленьком бизнесе даст больше понимания, чем только теория.

## Заметки

После блока wireless fundamentals естественный вопрос:

```text
Что теперь?
```

Честный ответ: на уровне `CCNA` Cisco не пытается превратить тебя в wireless specialist. Это правильно, потому что wireless быстро становится очень глубокой темой.

Но цель уже достигнута, если ты понял главное:

```text
Wi-Fi нельзя проектировать как Ethernet с антеннами.
```

## Беспроводная сеть - не Ethernet с антеннами

В wired network среда контролируемая:

- cable;
- switch port;
- known path;
- меньше внешних факторов;
- проще изоляция проблем.

В wireless среда другая.

Трафик уходит в воздух, где на него влияют:

- стены;
- окна;
- стекло;
- бетон;
- люди;
- деревья;
- погода;
- соседние access points;
- Bluetooth devices;
- микроволновки;
- другие источники interference.

Поэтому wireless не "сломанный Ethernet". Это другая среда со своими правилами.

## Не только coverage

Плохой wireless design часто начинается с неправильного вопроса:

```text
Есть ли сигнал?
```

Сигнал важен, но этого мало.

Правильные вопросы:

- хватает ли capacity;
- есть ли channel overlap;
- не слишком ли много clients в одной cell;
- как работает roaming;
- нет ли interference;
- не слишком ли большая мощность AP;
- поддерживают ли clients нужные standards;
- не держатся ли clients за слабый AP.

Coverage без performance - это ложное чувство успеха.

## Надежда - не стратегия

Плохой подход:

```text
Повесим WAP на потолок через каждые несколько метров.
Будет нормально.
```

Это не design.

Это надежда.

Хороший design учитывает:

- план помещения;
- материалы стен;
- density пользователей;
- приложения;
- guest и staff networks;
- channel plan;
- power levels;
- placement;
- roaming;
- wired uplinks;
- PoE;
- security.

## Что важно унести

Самый ценный результат этой недели - смена мышления.

Теперь wireless должен восприниматься не как checkbox:

```text
Wi-Fi есть? Да.
```

А как design problem:

```text
Как сделать Wi-Fi надежным, безопасным и полезным для реальных пользователей?
```

Если ты понял, что signal strength не равен user experience, это уже большой шаг.

## Практика важнее еще одной таблицы

Следующий шаг - не просто читать больше терминов.

Лучший шаг:

```text
Build.
Test.
Observe.
Adjust.
```

Можно взять любое место, которое тебе важно:

- дом;
- квартира;
- church;
- small office;
- lab;
- coffee shop;
- склад;
- учебный класс.

Настрой Wi-Fi, пройди по помещению, посмотри, где сигнал меняется, где падает скорость, где client не хочет roaming, где появляются retries.

Так wireless становится не теорией, а навыком.

## Что можно попробовать

Практические упражнения:

1. Перемести access point на несколько метров и сравни результат.
2. Измени channel и посмотри на interference.
3. Проверь 2.4 GHz против 5 GHz в разных комнатах.
4. Замерь performance рядом с AP и далеко от него.
5. Посмотри, как client roaming работает между двумя AP.
6. Раздели guest и private SSID.
7. Проверь, что guest Wi-Fi не видит internal devices.
8. Посмотри, как стены, двери и люди меняют signal quality.

Главное - наблюдать связь между изменением и результатом.

## Оборудование для практики

Не нужен enterprise budget, чтобы учиться.

Для home lab или small office можно использовать affordable gear. Например, многие используют Ubiquiti, потому что это доступный способ получить centralized management и реальный hands-on experience.

Это не единственный правильный вариант.

Идея другая:

```text
Выбери систему, на которой можно учиться placement, channels, power, SSID, guest network и monitoring.
```

## Сценарий NetworkChuck Coffee

Если NetworkChuck Coffee строит Wi-Fi, нельзя думать только:

```text
Клиентам нужен internet.
Поставим AP в back office.
```

В реальности есть:

- customers;
- POS systems;
- staff devices;
- inventory scanners;
- cameras;
- guest Wi-Fi;
- staff Wi-Fi;
- morning rush;
- разные зоны помещения.

Плохой wireless design может привести к:

- медленным checkouts;
- broken payments;
- жалобам customers;
- disconnected tablets;
- проблемам с scanners;
- потерянным sales.

Это уже не учебная проблема. Это бизнес.

## Как продолжать учиться

Дальше полезно развивать привычку:

- ходить по помещению;
- смотреть на signal quality;
- проверять interference;
- думать о walls, glass, bodies и density;
- смотреть, как clients переходят между AP;
- проверять реальный throughput;
- менять одну вещь за раз;
- документировать результаты.

Wireless хорошо учится через feedback loop:

```text
Изменил.
Проверил.
Сравнил.
Сделал вывод.
```

## Практический совет

Не начинай с попытки выучить каждый RF term.

Начни с места, которое реально важно, и спроектируй покрытие для него. Потом проверь, что получилось.

Теория нужна. Но без проверки на месте wireless легко превращается в набор красивых слов.

## Главный вывод

Wireless - это отдельная среда со своими правилами.

Это не Ethernet с антеннами и не простая checkbox-функция. Хороший Wi-Fi требует планирования, проверки, понимания interference, coverage, capacity, roaming и security.

После этой недели важнее всего не знать каждую настройку, а уважать сложность wireless и уметь задавать правильные вопросы перед deployment и troubleshooting.

## Команды и термины

| Термин | Значение |
| --- | --- |
| wireless | Беспроводная передача данных через радиосреду. |
| Wi-Fi | Практическая технология беспроводного доступа. |
| `WAP` | Wireless Access Point, точка беспроводного доступа. |
| `RF` | Radio frequency, радиочастотная среда. |
| coverage | Зона наличия сигнала. |
| performance | Реальное качество работы для пользователя. |
| capacity | Способность обслужить нужное количество clients и traffic. |
| interference | Помехи в радиосреде. |
| roaming | Переход client между access points. |
| channel planning | Планирование каналов для уменьшения overlap и interference. |
| power level | Мощность передачи access point. |
| site survey | Проверка и измерение wireless среды на месте. |

## Вопросы

### 1. Почему wireless нельзя считать Ethernet с антеннами?

Ответ: Потому что wireless работает в общей радиосреде с interference, отражениями, потерями и перемещающимися clients.

### 2. Почему coverage недостаточно?

Ответ: Сигнал может быть, но performance может быть плохим из-за перегрузки, interference, слабых clients или плохого roaming.

### 3. Почему просто добавить больше WAP не всегда правильно?

Ответ: Без channel planning и power design новые AP могут создать больше overlap и interference.

### 4. Как лучше продолжать учиться wireless?

Ответ: Строить маленький реальный проект, тестировать, наблюдать и корректировать настройки.

### 5. Почему плохой Wi-Fi важен для бизнеса?

Ответ: Он может замедлить платежи, нарушить работу staff devices, вызвать жалобы клиентов и привести к потерям.

## Что повторить позже

- Почему wireless - отдельная среда.
- Разницу между coverage и performance.
- Роль interference, density и roaming.
- Почему channel planning важнее случайного добавления AP.
- Как строить feedback loop при настройке Wi-Fi.
