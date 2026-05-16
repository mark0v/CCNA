# Navigating the Cisco IOS Software

Source: закрытая страница курса  
Date added: 2026-05-16  
Related plan item: Week 3 / Cisco IOS navigation  
Tags: cisco ios, cli, user mode, privileged mode, global configuration, interface configuration, show commands, packet tracer
Language: Russian
Translation pair: articles-en/2026-05/week-03/10-navigating-the-cisco-ios-software.md

## Summary

Cisco IOS - это command-line operating system, через который network engineer настраивает и проверяет Cisco routers and switches. Чтобы уверенно работать с устройством, нужно понимать modes, prompts и context: где можно только смотреть, где можно выполнять privileged commands, а где уже меняется configuration.

Главная мысль: Cisco CLI - это не просто набор команд. Это structured environment, где команда должна быть введена в правильном mode.

## Key Points

- Cisco IOS means Internetwork Operating System.
- IOS is the CLI environment used to configure and verify Cisco devices.
- In real life, initial access often happens through console cable and terminal software.
- In Packet Tracer, the CLI tab simulates that console experience.
- If the CLI looks blank, pressing Enter often reveals the prompt.
- Cisco devices use different modes for different access levels and contexts.
- User EXEC mode uses the `>` prompt.
- Privileged EXEC mode uses the `#` prompt.
- `enable` moves from user mode to privileged mode.
- `configure terminal` enters global configuration mode.
- Global configuration affects the whole device.
- Interface configuration mode affects one interface or port.
- `?` helps discover available commands and syntax.
- Tab auto-completes commands when enough characters are typed.
- `exit` moves back one level.
- `end` or `Ctrl+Z` returns to privileged EXEC mode.
- `show running-config` shows the active configuration.
- `show ip interface brief` gives a quick interface status summary.

## Notes

### Why IOS Navigation Matters

At this point, networking becomes hands-on.

Instead of only looking at diagrams, you begin to:

- connect to a device;
- type commands;
- change settings;
- verify behavior;
- troubleshoot from the CLI.

For NetworkChuck Coffee, this is how switches, routers and access points become manageable parts of the business network.

### Cisco IOS

IOS means:

```text
Internetwork Operating System
```

It is the Cisco operating system and CLI environment used on many Cisco devices.

Through IOS, you can:

- inspect device status;
- configure settings;
- verify interfaces;
- save configuration;
- troubleshoot problems.

### Packet Tracer vs Real Access

In real life, you often access a new switch or router through:

```text
Laptop -> console cable -> console port -> terminal program
```

In Packet Tracer:

```text
Device -> CLI tab
```

The CLI tab is a simulation of the console experience.

If the screen appears blank, press:

```text
Enter
```

Often the device is simply waiting to show the prompt.

### Modes Matter

Cisco IOS uses different modes.

Each mode has:

- its own prompt;
- its own command set;
- its own purpose;
- its own level of power.

This prevents every command from being available everywhere.

CLI navigation is about knowing:

```text
Where am I?
What can I do here?
Where does this command belong?
```

### User EXEC Mode

User EXEC mode is the first limited mode.

Prompt:

```text
Switch>
```

This mode allows basic checks, but not serious configuration changes.

It is useful when someone needs limited visibility without full control.

### Privileged EXEC Mode

To enter privileged EXEC mode:

```text
enable
```

Prompt changes to:

```text
Switch#
```

Privileged mode allows more powerful show commands and gives access to configuration modes.

The `#` prompt is a strong clue that you are in a more powerful place.

### Global Configuration Mode

From privileged EXEC mode:

```text
configure terminal
```

Prompt:

```text
Switch(config)#
```

Global configuration mode changes settings for the whole device.

Example global settings:

- hostname;
- management/security baseline;
- global services;
- device-wide behavior.

Example:

```text
hostname NCC-SW1
```

A meaningful hostname matters when managing multiple devices.

### Interface Configuration Mode

From global configuration mode, you can enter an interface context.

Example:

```text
interface FastEthernet0/1
```

Prompt:

```text
Switch(config-if)#
```

Commands entered here affect that specific interface.

Examples:

- add a description;
- shut down the port;
- bring it back up;
- change port-specific settings.

The key idea:

```text
Interface mode affects one interface.
Global mode affects the device.
```

### CLI Context

Cisco CLI is context-based.

A command can be valid in one mode and invalid in another.

Example:

```text
description Guest WiFi AP
```

This belongs under an interface, not random privileged mode.

If a command fails, ask:

```text
Am I in the right mode?
```

### Question Mark Help

`?` is one of the most useful IOS tools.

Use it to discover commands:

```text
Switch# ?
```

Use it inside a command to see what comes next:

```text
Switch# show ?
```

This means you do not need to memorize every possible command at once.

Cisco can guide you through syntax.

### Tab Completion

Tab helps auto-complete commands.

Example:

```text
conf<Tab>
```

can complete to:

```text
configure
```

If enough characters make the command unique, IOS fills in the rest.

This improves speed and reduces typing mistakes.

### Moving Between Modes

`exit` moves back one level:

```text
Switch(config-if)# exit
Switch(config)#
```

`end` returns directly to privileged EXEC:

```text
Switch(config-if)# end
Switch#
```

`Ctrl+Z` does the same kind of jump back to privileged EXEC.

In real work, this becomes muscle memory:

```text
configure -> change -> end -> verify
```

### Interface Descriptions

Add descriptions when configuring interfaces.

Example:

```text
description Guest WiFi AP - Cafe Floor
```

Six months later, this helps troubleshooting immediately.

Good descriptions tell future you:

- what is connected;
- where it is;
- why the port matters.

### show running-config

Command:

```text
show running-config
```

Short form:

```text
show run
```

This shows the active configuration currently loaded on the device.

It is useful to:

- verify changes;
- review device behavior;
- copy configuration for backup;
- understand what has been configured.

### show ip interface brief

Command:

```text
show ip interface brief
```

This gives a quick summary of:

- interfaces;
- IP addresses;
- status;
- protocol state.

It is one of the first commands to run when you log into an unfamiliar Cisco device.

It cuts through confusion quickly.

### Main Takeaway

IOS navigation is the foundation for everything else.

You need to know:

- how to enter the CLI;
- how to read prompts;
- how to move between modes;
- how to find commands with `?`;
- how to use Tab completion;
- how to exit modes;
- how to verify with `show run` and `show ip interface brief`.

Once you can move around comfortably, configuration becomes much less mysterious.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Cisco IOS | Cisco Internetwork Operating System used to configure and manage many Cisco devices. |
| CLI | Command-Line Interface. |
| User EXEC mode | Limited mode shown with `>` prompt. |
| Privileged EXEC mode | More powerful mode shown with `#` prompt. |
| `enable` | Command used to enter privileged EXEC mode. |
| `configure terminal` | Command used to enter global configuration mode. |
| Global configuration mode | Mode for device-wide configuration. |
| Interface configuration mode | Mode for configuring a specific interface. |
| Prompt | CLI text showing current device name and mode. |
| `?` | IOS help tool for discovering commands and syntax. |
| Tab completion | Auto-completion of commands when enough characters are typed. |
| `exit` | Moves back one CLI level. |
| `end` | Returns to privileged EXEC mode. |
| `Ctrl+Z` | Keyboard shortcut that returns to privileged EXEC mode. |
| `show running-config` | Displays the active running configuration. |
| `show run` | Short form of `show running-config`. |
| `show ip interface brief` | Displays a concise interface and IP status summary. |

## Questions

### 1. What does Cisco IOS stand for?

Internetwork Operating System.

### 2. What does the Packet Tracer CLI tab represent?

A simulated console/CLI session to the device.

### 3. What should you try if the CLI screen is blank?

Press Enter to reveal or wake up the prompt.

### 4. What prompt symbol shows user EXEC mode?

`>`.

### 5. What command enters privileged EXEC mode?

`enable`.

### 6. What prompt symbol shows privileged EXEC mode?

`#`.

### 7. What command enters global configuration mode?

`configure terminal`.

### 8. What does interface configuration mode affect?

One specific interface or port.

### 9. Why can a valid command fail?

Because it may be entered in the wrong mode or context.

### 10. What does `?` help with?

Discovering available commands and command syntax.

### 11. What does Tab do in IOS?

It auto-completes a command when the typed characters are unique enough.

### 12. What is the difference between `exit` and `end`?

`exit` moves back one level; `end` returns directly to privileged EXEC mode.

### 13. What does `show running-config` display?

The active configuration currently running on the device.

### 14. Why is `show ip interface brief` useful?

It gives a quick view of interfaces, IP addresses and up/down status.

## What To Review Later

- Cisco IOS modes and prompts.
- User EXEC vs privileged EXEC.
- Global configuration mode.
- Interface configuration mode.
- `?` command help.
- Tab completion.
- `exit`, `end` and `Ctrl+Z`.
- `show running-config`.
- `show ip interface brief`.
