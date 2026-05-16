# Setting Up Console Connections

Source: закрытая страница курса  
Date added: 2026-05-16  
Related plan item: Week 3 / Cisco console access  
Tags: cisco, console connection, console port, cli, serial, putty, com port, router, switch, packet tracer
Language: Russian
Translation pair: articles-en/2026-05/week-03/09-setting-up-console-connections.md

## Summary

Console connection - это первый способ попасть на router или switch, когда устройство еще не настроено для remote management. В Packet Tracer достаточно открыть CLI tab, но в реальной жизни новое устройство часто не имеет IP address, SSH, Telnet или другой сетевой настройки. Поэтому сначала нужен direct physical connection: laptop, console cable, terminal program и console port на устройстве.

Главная мысль: before a device can be managed remotely, it has to be managed locally.

## Key Points

- A new router or switch often needs local console access before remote management exists.
- Packet Tracer hides the physical console process behind the CLI tab.
- Switches can forward local traffic out of the box, but still need configuration for production use.
- Routers usually need configuration before they can route traffic usefully.
- The console port is for direct management, not normal user traffic.
- An RJ45-shaped console connector is not the same as a normal Ethernet data port.
- Console cables may use DB9 serial, USB-A, USB-C or USB-to-serial adapters.
- Modern laptops often require USB console cables or adapters.
- On Windows, the console adapter usually appears as a COM port.
- A terminal program such as PuTTY opens the serial session.
- Common Cisco console speed is 9600 baud.
- A blank terminal window may simply need Enter before the prompt appears.
- Console access is the first step toward configuring remote access later.

## Notes

### Почему console connection нужен

Когда оборудование только установлено в rack, оно еще не обязательно готово к management over the network.

Устройство может не иметь:

- IP address;
- SSH configuration;
- username/password setup;
- management VLAN;
- default gateway;
- remote access policy.

Поэтому первый вход часто делается через console connection.

Простая формула:

```text
Laptop -> console cable -> device console port -> CLI
```

### Packet Tracer vs Real Life

В Packet Tracer процесс выглядит слишком удобно:

```text
Double-click device -> CLI tab -> start typing
```

В реальной жизни CLI tab нет.

Нужно:

- найти console port;
- подключить cable;
- убедиться, что computer видит adapter;
- открыть terminal program;
- выбрать serial settings;
- нажать Enter и получить prompt.

Packet Tracer CLI tab - это виртуальная имитация console session.

### Switches Behave, Routers Don't

Switch обычно может делать basic switching почти сразу.

Если подключить несколько devices в один switch, он может начать forwarding frames внутри LAN.

Но это не значит, что switch production-ready.

Ему все равно нужны:

- hostname;
- security;
- management access;
- VLAN settings;
- documentation-friendly baseline.

Router ведет себя иначе.

Router должен знать:

- какие networks connected;
- как routing should work;
- как подключаться к outside network;
- какие interfaces включены и настроены.

Без configuration router часто просто ждет инструкций.

### Console Port

Console port - это dedicated management port.

Он нужен для:

- initial setup;
- local troubleshooting;
- recovery;
- access when network management is broken.

Важно:

```text
Console port is not a normal data port.
```

На older Cisco gear console connector может выглядеть как RJ45 Ethernet, но purpose and signaling другие.

Не надо думать:

```text
RJ45 shape = normal Ethernet port
```

Console port существует для direct device management.

### Console Cable Types

За годы появилось несколько вариантов console cables:

- DB9 serial to RJ45 console cable;
- USB-to-serial adapter + console cable;
- USB-A to RJ45 console cable;
- USB-C to RJ45 console cable;
- vendor-specific console cables.

Old-school вариант:

```text
Laptop serial port -> DB9 -> RJ45 console
```

Современный вариант:

```text
Laptop USB/USB-C -> console cable -> device console port
```

Проблема в том, что exact steps зависят от:

- operating system;
- cable type;
- adapter chipset;
- driver;
- USB-A vs USB-C;
- Windows, macOS or Linux.

### Real-World Troubleshooting Mindset

Не стоит искать один perfect universal guide.

Лучше понимать process:

1. Подключить cable.
2. Найти, какой port появился в OS.
3. Открыть terminal program.
4. Выбрать serial connection.
5. Указать правильный port.
6. Использовать правильную speed.
7. Нажать Enter and look for prompt.

Если что-то не работает, troubleshooting идет по этим шагам.

### Windows COM Port

На Windows console adapter часто появляется как COM port.

Проверить это можно в Device Manager.

Пример:

```text
USB Serial Port (COM3)
```

COM port - это serial communication port в Windows.

Если adapter появился как COM3, значит computer видит cable/adapter, и можно использовать COM3 в terminal program.

### Terminal Program

Terminal program открывает text-based session к device.

На Windows часто используют:

- PuTTY;
- Tera Term;
- SecureCRT;
- Windows Terminal with serial tools in some setups.

В учебном примере используется PuTTY, потому что он простой и бесплатный.

### PuTTY Serial Settings

Базовые шаги:

1. Open PuTTY.
2. Choose Serial.
3. Enter COM port, for example `COM3`.
4. Set speed to `9600`.
5. Open session.

Common Cisco console setting:

```text
Speed: 9600 baud
```

Окно может быть blank at first. Часто достаточно нажать:

```text
Enter
```

и появится device prompt.

### What Happens After Console Access

Console connection - это не final destination.

Это первый вход, чтобы настроить:

- hostname;
- passwords or local users;
- management interface;
- IP settings;
- SSH or other remote management;
- baseline security;
- saving configuration.

Позже, когда device будет configured, engineer сможет manage it remotely.

Но first setup часто начинается locally.

### Console Access in Troubleshooting

Console cable полезен не только при first setup.

Он нужен, когда:

- SSH is broken;
- management IP unreachable;
- device is misconfigured;
- password recovery is needed;
- boot messages must be observed;
- network path to device is down.

Console access остается safety path into the device.

### Main Takeaway

Console connection - это мост между installed hardware и configured network.

Без него ты смотришь на blinking lights.

С ним ты можешь:

- попасть в CLI;
- начать baseline configuration;
- проверить status;
- подготовить remote management;
- превратить rack equipment в working network.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Console connection | Direct local management connection from a computer to a network device. |
| Console port | Dedicated management port used for setup and troubleshooting. |
| CLI | Command-Line Interface used to configure and verify network devices. |
| Remote management | Managing a device over the network, commonly with SSH. |
| Local management | Managing a device through direct physical access, such as console. |
| COM port | Windows name for a serial communication port. |
| Serial connection | Text-based communication method used by console sessions. |
| PuTTY | Common terminal program used for SSH, Telnet and serial sessions. |
| Baud | Serial communication speed unit; Cisco console often uses 9600 baud. |
| DB9 | Older serial connector type used with classic console cables. |
| USB-to-serial adapter | Adapter that lets a modern USB computer use serial console connections. |
| RJ45 console | Console connector shape used on many Cisco devices, not a normal Ethernet data port. |
| Packet Tracer CLI tab | Simulator shortcut that represents console access virtually. |

## Questions

### 1. Why do we need a console connection for a new device?

Because the device may not yet have IP addressing, SSH or any remote management configured.

### 2. How does Packet Tracer simplify console access?

It lets you open the CLI tab directly, which acts like a virtual console session.

### 3. Can a switch work before full configuration?

At a basic level, yes. It may forward local LAN traffic, but it still needs proper production configuration.

### 4. Why does a router usually need configuration before it is useful?

It needs interface, routing and outside network settings before it can route traffic correctly.

### 5. What is the console port used for?

Direct local management, initial setup, troubleshooting and recovery.

### 6. Is an RJ45 console port the same as an Ethernet data port?

No. It may look similar, but the purpose and signaling are different.

### 7. What does Windows usually call a serial console adapter?

A COM port, such as COM3.

### 8. What terminal program was used in the lesson?

PuTTY.

### 9. What console speed is commonly used for Cisco devices?

9600 baud.

### 10. What should you try if PuTTY opens a blank serial window?

Press Enter to wake up or reveal the device prompt.

### 11. Is console access only for initial setup?

No. It is also useful for troubleshooting, recovery and access when remote management fails.

### 12. What is the main purpose of console access?

To get into the device locally so you can begin configuring and managing it.

## What To Review Later

- Console port vs Ethernet data port.
- Packet Tracer CLI tab vs real console access.
- Console cable types.
- USB-to-serial adapters.
- Windows COM ports.
- PuTTY serial settings.
- 9600 baud.
- Local management before remote management.
- Console access for troubleshooting.
