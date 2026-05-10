# Physically Connecting the Coffee House

Source: закрытая страница курса  
Date added: 2026-05-09  
Related plan item: Week 2 / Physical build from diagram  
Tags: physical layer, cabling, rack, ports, interfaces, access point, router, switch, deployment, labels

## Summary

Logical diagram должен превратиться в реальные cables, ports and link lights. В этой части NetworkChuck Coffee topology собирается физически: two switches, two wireless access points, router and Plex server. Каждая линия на diagram становится конкретным кабелем между конкретными interfaces.

Главная мысль: diagram - это инструкция. Physical build должен совпадать с planned port-to-port mapping.

## Key Points

- Logical design is not enough; it must become physical connections.
- Every diagram line should map to a real cable.
- Exact interface names and port numbers matter.
- If diagram says Router Gi0/0 to Switch Gi0/24, build should match that.
- Consistency between diagram and rack helps troubleshooting.
- Interface naming like Gi0/0 may reflect module/slot/port structure.
- Slimline Ethernet cables are useful in labs and short tidy runs.
- Slimline cables are not always ideal for long permanent infrastructure.
- Wireless APs are usually ceiling/wall mounted in real deployments.
- AP cabling is often hidden for clean installation.
- Router internet-facing port connects toward ISP handoff in production.
- Label both ends of cables.
- As engineers grow, their work often shifts from cabling to design/config/troubleshooting.
- Physical layer still matters even if installers handle cabling later.

## Notes

### Diagram Becomes Real

Process:

```text
Logical device -> Physical device
Diagram line -> Real cable
Interface label -> Actual port
```

Если physical network не совпадает с diagram, documentation теряет ценность.

### Port Numbers Matter

Пример:

```text
Router GigabitEthernet0/0 -> Switch GigabitEthernet0/24
```

Это не просто красивая подпись. Это planned connection.

При installation нужно найти именно эти ports и подключить exactly as planned.

### Cabling Quality

В lab можно использовать slimline Ethernet cables:

- аккуратнее;
- удобнее для short runs;
- меньше cable clutter.

Но для permanent infrastructure нужно выбирать cable type по стандарту и условиям run. Не все lab-friendly cables подходят для walls, ceilings или long runs.

### Access Points

APs в реальной кофейне часто:

- mounted on ceilings;
- mounted on walls;
- powered over Ethernet;
- connected back to switch;
- cabled through hidden paths.

Network should work well and look professional.

### Internet Cable

Router interface toward internet в lab может быть условным. В production он подключается к ISP handoff:

- fiber handoff;
- cable modem;
- DSL;
- wireless provider gear;
- enterprise circuit.

## Commands / Terms

```text
Physical layer - actual cables, ports and signals
Interface - port on device
ISP handoff - point where provider gives connectivity
MDF - Main Distribution Facility
Rack - место установки network gear
Cable label - подпись на кабеле
```

## Questions

### Что значит "diagram becomes real"?

Каждое устройство и соединение на схеме должно соответствовать реальному устройству и кабелю.

### Почему exact port mapping важен?

Потому что configuration, troubleshooting and documentation зависят от того, что подключено куда.

### Почему надо label both ends?

Чтобы быстро понимать, куда идет кабель, особенно через недели или месяцы после установки.

### Почему network engineer должен понимать physical layer?

Даже если cabling делает другая команда, engineer проектирует, проверяет и troubleshooting строит на этой физической базе.

## What To Review Later

- Interface naming conventions.
- Cable labeling standards.
- Rack cable management.
- MDF/IDF design.
- ISP handoff types.
