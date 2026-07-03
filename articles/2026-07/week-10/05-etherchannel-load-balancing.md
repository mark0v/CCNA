# EtherChannel Load Balancing

Source: закрытая страница курса  
Date added: 2026-07-03  
Related plan item: Week 10 / EtherChannel load balancing  
Tags: EtherChannel, load balancing, port-channel, hashing, LACP, bandwidth
Language: Russian
Translation pair: articles-en/2026-07/week-10/05-etherchannel-load-balancing.md

## Summary

- EtherChannel выглядит как один логический link, но внутри него остаются отдельные physical member links.
- Один conversation обычно использует один physical link, а не всю суммарную bandwidth bundle.
- Польза EtherChannel проявляется на множестве одновременных flows.
- Распределение traffic зависит от hash-based load balancing algorithm.
- Метод балансировки нужно проверять и при необходимости настраивать под реальный traffic pattern.

## Key Points

- Два линка по 1 Gbps в EtherChannel не дают одному flow гарантированные 2 Gbps.
- Switch выбирает member link через алгоритм на основе MAC/IP/port fields.
- Один и тот же набор input values обычно дает один и тот же output link.
- Неровная загрузка member links не всегда означает поломку.
- Команды `show etherchannel load-balance` и `port-channel load-balance` нужны для проверки и настройки поведения.

## Notes

Про EtherChannel часто говорят так: "он объединяет несколько линков в один логический канал". Это верно, но легко сделать неправильный вывод. Логический канал не означает, что один single flow автоматически использует всю суммарную пропускную способность всех member links.

Если в EtherChannel два физических линка по 1 Gbps, это не значит, что один PC, копирующий файл на один server, получит 2 Gbps. Обычно такой conversation попадет на один physical link и останется там. Выигрыш появляется, когда есть много разных conversations: разные hosts, servers, applications и sessions могут быть распределены по разным member links.

Пример для NetworkChuck Coffee:

- inventory workstation общается с server;
- POS terminal отправляет данные в back-office system;
- camera server пишет архив;
- Wi-Fi clients используют внутренние ресурсы.

Каждый отдельный flow может попасть на один link, но весь bundle в сумме начинает использоваться лучше. Именно поэтому EtherChannel дает aggregate bandwidth, а не магическое ускорение одного разговора.

Switch не распределяет трафик "по настроению" и не пытается идеально выровнять графики в реальном времени. Он использует load-balancing algorithm. Обычно это hash-based decision: switch берет выбранные поля frame или packet, пропускает их через алгоритм и выбирает physical member link.

Возможные input fields зависят от модели switch и IOS version, но часто встречаются:

| Option | What it uses |
| --- | --- |
| `src-mac` | Source MAC address. |
| `dst-mac` | Destination MAC address. |
| `src-dst-mac` | Source и destination MAC addresses вместе. |
| `src-ip` | Source IP address. |
| `dst-ip` | Destination IP address. |
| `src-dst-ip` | Source и destination IP addresses вместе. |

Если алгоритм использует source MAC, то трафик от одного sender может стабильно попадать на один и тот же member link. Это предсказуемо: same input дает same hash result. Но из-за этого utilization может быть неровным. Один link занят, второй почти пустой - и это не обязательно ошибка EtherChannel.

Поэтому default load balancing method не стоит принимать на веру. На разных платформах и версиях IOS default может отличаться. Правильный подход: проверить текущий operational method командой:

```text
Switch# show etherchannel load-balance
```

Если распределение не подходит под traffic pattern, метод можно изменить в global configuration mode:

```text
Switch(config)# port-channel load-balance src-dst-mac
```

Выбор алгоритма должен зависеть от того, какие поля реально меняются в трафике:

- много clients к одному server - часто полезны source-based или source-destination варианты;
- много server-to-server traffic - может лучше работать source-destination IP;
- чистый Layer 2 segment - MAC-based варианты могут быть логичнее;
- routed uplinks - IP-based варианты часто дают больше полезной уникальности.

Идея простая: чем больше полезной уникальности попадает в hash, тем выше шанс, что flows распределятся по member links лучше. Но "лучше" нужно оценивать по реальному трафику, а не по названию опции.

После изменения load balancing method важно настроить и вторую сторону EtherChannel. Оба switches участвуют в передаче, поэтому operational discipline требует согласовать подход на обоих ends. Даже если mismatch не выглядит как мгновенная авария, он может усложнить troubleshooting и дать странную utilization picture.

Порядок работы:

1. Проверить текущий метод:

```text
Switch# show etherchannel load-balance
```

2. Выбрать новый method под traffic pattern:

```text
Switch(config)# port-channel load-balance src-dst-mac
```

3. Повторить на другой стороне channel.

4. Проверить снова:

```text
Switch# show etherchannel load-balance
Switch# show etherchannel summary
```

Главное запомнить: EtherChannel - это aggregate throughput across multiple conversations. Это не single-flow bandwidth multiplication. Если это понять, load balancing перестает казаться странным и становится нормальной частью дизайна.

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `show etherchannel load-balance` | Показывает текущий метод load balancing для EtherChannel. |
| `port-channel load-balance src-dst-mac` | Настраивает балансировку по source и destination MAC addresses. |
| Hashing | Математический выбор member link на основе выбранных input fields. |
| Flow | Логический conversation между endpoints, например host-to-server traffic. |
| Aggregate bandwidth | Суммарная полезная емкость bundle для множества flows. |
| Member link | Физический интерфейс внутри EtherChannel bundle. |

## Questions

### 1. Почему один flow обычно не использует всю bandwidth EtherChannel?

Answer: Потому что EtherChannel распределяет flows между member links через hash-based algorithm. Один conversation обычно получает один physical link, чтобы не нарушать порядок кадров.

### 2. Что означает aggregate bandwidth?

Answer: Это общая пропускная способность bundle для множества одновременных conversations, а не гарантированная скорость для одного traffic flow.

### 3. Почему member links могут быть загружены неравномерно?

Answer: Hash algorithm использует выбранные input fields. Если traffic pattern однообразный, много flows может попасть на один и тот же physical link.

### 4. Как проверить текущий load balancing method?

Answer: Командой `show etherchannel load-balance`.

### 5. Почему алгоритм нужно выбирать под traffic pattern?

Answer: Потому что лучший algorithm зависит от того, какие поля реально отличаются между conversations. Если выбранные поля почти не меняются, распределение будет слабым.

## What To Review Later

- Какие load balancing options поддерживает конкретная Cisco platform.
- Разницу между MAC-based и IP-based hashing.
- Почему EtherChannel сохраняет packet order внутри одного flow.
- Как читать utilization member links при troubleshooting.
