# Castle Rysen Network Design

Source: закрытая страница курса  
Date added: 2026-05-16  
Related plan item: Week 3 / Applying network design models  
Tags: network design, soho, two-tier, three-tier, mdf, idf, fiber, redundancy, ethernet distance
Language: Russian
Translation pair: articles-en/2026-05/week-03/06-castle-rysen-network-design.md

## Summary

Network design models становятся полезными, когда их применяют к реальному зданию. Маленькое кафе и большое multi-zone здание используют похожие принципы, но масштаб приводит к разным решениям. Для маленькой SOHO-сети важно не допустить хаотичного роста switches и оставить spare capacity. Для крупного здания нужен более структурный подход: MDF как центральная точка, IDF в отдельных зонах, redundant uplinks и fiber там, где Ethernet distance limit становится проблемой.

Главная мысль: модель - это не теория ради экзамена, а decision tool для реального проекта.

## Key Points

- Small café networks can become messy quickly if switches are added organically.
- SOHO does not mean "ignore design."
- Around the third switch, it is time to become intentional.
- Keep switch capacity available instead of maxing out every port.
- Leaving 20-30% spare ports helps during failures and growth.
- Separating roles across switches makes failures easier to recover from.
- Larger buildings often need MDF and IDF planning.
- MDF is the main network distribution point.
- IDFs serve local building zones and connect back to the MDF.
- Redundant uplinks reduce single points of failure.
- Fiber is often used between MDF and IDFs.
- Ethernet copper runs are commonly limited to about 100 meters.
- Attenuation means signal weakens over distance.
- Three-tier thinking helps organize large, multi-area buildings.
- Design models help translate theory into real cable and equipment placement.

## Notes

### От модели к реальному зданию

Two-tier, three-tier и spine-leaf звучат абстрактно, пока ты не стоишь в настоящем здании и не решаешь:

- где поставить switches;
- куда вести cables;
- где будет network core;
- как пережить отказ switch или cable;
- какие distances допустимы.

Модель помогает превратить здание в понятный network plan.

### Scenario 1 - Small Café

Представим NetworkChuck Coffee или Castle Rysen Coffee как маленькое кафе примерно на 15 человек.

Это похоже на SOHO:

```text
Small Office, Home Office
```

Внутри могут быть:

- Plex server;
- wireless access points;
- POS terminals;
- staff computers;
- printers;
- phones;
- guest Wi-Fi.

На таком размере сеть часто растет organically:

```text
Need more ports -> add a switch
Need more ports again -> add another switch
Now nobody knows what connects where
```

Это ловушка.

### When Three Switches Appear

Практическое правило из реального мира:

```text
When you hit switch number three, start designing intentionally.
```

Это не строгий exam rule, но очень полезная привычка.

Не нужно просто добавлять switch and hope. Нужно остановиться и подумать:

- какие devices куда подключены;
- какие roles есть у switches;
- что сломается при отказе одного switch;
- есть ли spare ports;
- как быстро восстановить сервис.

### Cleaner Small Café Design

Допустим, есть три 24-port switches:

- Switch A;
- Switch B;
- Switch C.

Вместо хаоса можно распределить роли:

```text
Switch A: wireless access points
Switch B: most wired devices
Switch C: additional wired devices / spare capacity
```

Если Switch A dedicated to WAPs fails, ты теряешь Wi-Fi, но не всю сеть.

Временно можно перенести AP cables на Switch B или Switch C, если там есть spare ports.

### Leave Breathing Room

Не max out switch ports.

Хорошая практика:

```text
Keep 20-30% of ports free.
```

Почему это важно:

- легче пережить failed switch;
- проще добавить new devices;
- проще временно перенести cables;
- меньше emergency work;
- меньше риска при troubleshooting.

Если каждый port занят, любой отказ превращается в кризис.

### Two-Tier-ish Thinking

Для маленького кафе не обязательно строить полноценный campus design.

Но полезно мыслить в стиле two-tier:

```text
Access devices -> organized switching -> router/internet/services
```

Даже loose two-tier design лучше, чем random sprawl.

Цель:

- простота;
- понятная схема;
- recoverability;
- room for growth.

### Scenario 2 - Larger Building

Теперь представим Fallout Shelter или большое multi-area здание.

Внутри есть зоны:

- eatery;
- sleeping quarters;
- administration wing;
- network core;
- other building areas.

Здесь SOHO-подход уже не работает.

Нужен structure.

### MDF

MDF означает:

```text
Main Distribution Facility
```

Это главная network room или центральная точка распределения.

В MDF обычно находятся:

- distribution/core switches;
- router connections;
- internet handoff;
- firewall or edge devices;
- major uplinks;
- central patching.

В большом здании MDF - это heart of the network.

### IDF

IDF означает:

```text
Intermediate Distribution Facility
```

IDF размещаются ближе к отдельным зонам здания.

Примеры:

- IDF for eatery;
- IDF for sleeping quarters;
- IDF for administration;
- IDF for another floor or wing.

IDF acts like local access layer for that area.

От IDF cables идут к devices в этой зоне.

### MDF to IDF Connections

IDFs connect back to MDF.

Часто для этого используют:

- fiber optic cable;
- sometimes Ethernet copper, if distance allows.

Важно: обычно прокладывают не один uplink, а multiple links for redundancy.

Плохой вариант:

```text
IDF -> one cable -> MDF
```

Лучше:

```text
IDF -> redundant uplinks -> MDF
```

Один cable - single point of failure.

### Ethernet Distance Limit

Copper Ethernet обычно ограничен примерно:

```text
100 meters
```

Если run слишком длинный, signal quality ухудшается.

Это связано с attenuation:

```text
Attenuation = signal loss over distance
```

В большом здании не всегда можно вести каждый cable напрямую в MDF. Иногда distance просто слишком большой.

### Why IDFs Exist

IDFs помогают не бороться с физикой.

Вместо того чтобы тянуть каждый endpoint cable до central core:

```text
Device -> local IDF -> fiber/uplink -> MDF
```

Так large building становится управляемым:

- local cable runs shorter;
- uplinks planned;
- zones become clear;
- troubleshooting gets easier;
- redundancy can be designed.

### Three-Tier Thinking in Practice

Для большого здания:

```text
End devices -> IDF/access layer -> MDF/distribution or core -> outside networks/services
```

В campus environment можно расширить:

```text
Access in each area -> Distribution per building -> Core between buildings
```

Модель помогает понять, где у тебя access, где distribution, и когда нужен core.

### Café vs Fallout Shelter

| Environment | Design Thought |
| --- | --- |
| Small café | Keep it simple, organized and recoverable. |
| Three switches in café | Stop growing randomly; assign roles and leave spare ports. |
| Large multi-zone building | Use MDF and IDFs. |
| Long cable distances | Use fiber or strategically placed IDFs. |
| Critical links | Add redundancy. |

### Main Takeaway

Models are decision tools.

Они помогают, когда ты стоишь в реальном здании и решаешь:

- café can use simple two-tier-ish design;
- big multi-zone building needs MDF/IDF planning;
- copper distance limits matter;
- redundancy must be intentional;
- switch capacity must leave room for failure and growth.

Theory is the map. Real building is the territory.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| SOHO | Small Office, Home Office; simple small-network environment. |
| Organic growth | Network growth by adding devices as needed without a planned design. |
| Two-tier model | Design with access and distribution/collapsed core functions. |
| Three-tier model | Design with access, distribution and core layers. |
| MDF | Main Distribution Facility; main network distribution point or network room. |
| IDF | Intermediate Distribution Facility; local distribution point for a building area or floor. |
| WAP | Wireless Access Point. |
| Redundancy | Extra path, device or link that keeps service available during failure. |
| Single point of failure | One component whose failure can break a larger service or area. |
| Uplink | Connection from a lower-layer switch or IDF back toward distribution/core. |
| Fiber optic cable | Cable using light, often used for longer distances and uplinks. |
| Ethernet distance limit | Copper Ethernet runs are commonly limited to about 100 meters. |
| Attenuation | Signal weakening over distance. |
| Spare capacity | Unused ports or resources reserved for growth and recovery. |

## Questions

### 1. Why can a small café network become messy quickly?

Because switches are often added organically as ports run out, without documenting roles or paths.

### 2. What practical warning appears around the third switch?

It is time to stop adding switches randomly and start designing intentionally.

### 3. Why should you avoid maxing out switch ports?

Spare ports make growth and failure recovery much easier.

### 4. How much spare switch capacity is a good practical target?

About 20-30% free ports when possible.

### 5. Why might one switch be dedicated to wireless access points?

It creates a clean role boundary, so if that switch fails, the failure is easier to understand and recover from.

### 6. What is an MDF?

Main Distribution Facility; the main network distribution room or central point for core/distribution equipment.

### 7. What is an IDF?

Intermediate Distribution Facility; a local network distribution point serving a specific area, floor or wing.

### 8. Why use IDFs in a large building?

They shorten local cable runs, organize zones and connect back to the MDF through planned uplinks.

### 9. Why are redundant uplinks important?

They reduce the risk that one failed cable or link disconnects an entire area.

### 10. What is the common copper Ethernet distance limit?

About 100 meters.

### 11. What is attenuation?

Signal weakening over distance.

### 12. When does fiber make sense between MDF and IDF?

When distance, bandwidth or uplink reliability needs exceed what copper Ethernet can comfortably provide.

## What To Review Later

- SOHO growth trap.
- Switch role planning.
- Leaving 20-30% spare ports.
- Two-tier-ish café design.
- MDF and IDF roles.
- Redundant uplinks.
- Ethernet 100-meter distance limit.
- Attenuation.
- Fiber between distribution points.
