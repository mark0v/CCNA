# Configuring Router Interfaces

Source: закрытая страница курса  
Date added: 2026-06-01  
Related plan item: Week 5 / Configuring router interfaces  
Tags: router interface, cisco ios, no shutdown, administratively down, cdp, lldp, stp, base configuration
Language: Russian
Translation pair: articles-en/2026-05/week-05/07-configuring-router-interfaces.md

## Summary

Router interface configuration похожа на switch interface configuration, но у routers есть важные отличия. Главное: router interfaces часто shutdown by default, поэтому IP address сам по себе не включает interface. После настройки нужно выполнить `no shutdown`.

Главная мысль: router interface должен иметь правильный IP address, subnet mask и быть administratively enabled, иначе он не будет работать.

## Key Points

- Router CLI feels familiar after switch configuration.
- Router interfaces are often administratively down by default.
- `no shutdown` is required to enable a router interface.
- `show ip interface brief` is the fastest first verification command.
- Router interface names can be simple or modular, like `GigabitEthernet0/0/0`.
- Base configuration should come before interface activation.
- Configure first, enable second is a good operational habit.
- STP orange state on a switch link is often normal before forwarding.
- CDP helps discover Cisco neighbors.
- LLDP is the open industry-standard neighbor discovery protocol.
- Hardcoding speed/duplex on modern links should be done only with a reason.

## Notes

### Routers Feel Familiar

Если ты уже работал с Cisco switch CLI, router CLI не выглядит полностью новым.

Ты по-прежнему используешь:

```text
enable
configure terminal
interface ...
show ip interface brief
```

Но routers behave differently in important ways.

Самое важное отличие:

```text
Router interfaces are usually shut down by default.
```

### Administratively Down

На switch port часто можно увидеть `down/down`, если cable не подключен.

Это может означать:

```text
Port is enabled, but physical link is down.
```

На router interface часто встречается:

```text
administratively down
```

Это означает:

```text
Interface is disabled in software.
```

Иными словами, router interface выключен configuration command.

Чтобы включить:

```text
no shutdown
```

Если забыть `no shutdown`, можно долго troubleshooting "неисправный" link, хотя interface просто выключен.

### Interface Naming On Routers

Router interface names can vary.

Examples:

```text
GigabitEthernet0/0
GigabitEthernet0/1
GigabitEthernet0/0/0
Serial0/1/0
```

More slashes usually mean more modular hardware layout.

Typical meaning:

- slot/module;
- submodule;
- port.

Do not memorize one universal pattern for all routers.

Instead:

```text
Look at the device.
Use show commands.
Read the interface names carefully.
```

### Find Available Interfaces

Useful first command:

```text
show ip interface brief
```

It shows:

- interface names;
- IP addresses;
- status;
- protocol state.

Example output idea:

```text
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0/0   unassigned      YES unset  administratively down down
GigabitEthernet0/0/1   unassigned      YES unset  administratively down down
```

This tells you:

- which interfaces exist;
- whether they have IP addresses;
- whether they are enabled;
- whether link/protocol is up.

### Packet Tracer Hardware View

Packet Tracer can help visualize router modules.

You can often:

- inspect physical slots;
- add Ethernet cards;
- add serial modules;
- add switch modules;
- watch interface names change.

This makes modular naming easier to understand.

The interface name reflects where the port lives in the hardware.

### Base Configuration First

Before assigning interface IPs, get basic device identity and access in place.

Typical base config:

```text
hostname Cafe01-RT01
enable secret <password>
line console 0
password <password>
login
line vty 0 4
password <password>
login
service password-encryption
banner motd #Authorized access only#
```

Then save:

```text
copy running-config startup-config
```

Why:

- device has clear identity;
- access is controlled;
- config survives reload;
- environment is readable.

For NetworkChuck Coffee, names like `Cafe01-RT01` make the topology easier to understand.

### Configure Router Interface

Basic interface configuration:

```text
configure terminal
interface GigabitEthernet0/0/0
description Link to Cafe01-SW01
ip address 192.168.0.1 255.255.255.0
no shutdown
```

Important:

```text
IP address does not automatically enable the interface.
```

You need:

```text
no shutdown
```

### Configure First, Enable Second

Good habit:

```text
Configure the interface while it is shut down.
Then bring it up once.
```

Why:

- prevents repeated link flaps;
- avoids unnecessary alarms;
- reduces err-disable risks in some environments;
- makes change more controlled;
- helps during staging.

Example workflow:

```text
interface GigabitEthernet0/0/0
shutdown
description Link to Cafe01-SW01
ip address 192.168.0.1 255.255.255.0
no shutdown
```

This is especially useful when applying multiple settings.

### Link Bounce And Err-Disable

Some configuration changes can cause a port to bounce:

```text
down -> up -> down -> up
```

On switches, unstable behavior can sometimes trigger an err-disabled state depending on features/configuration.

Plain English:

```text
The switch sees a problem and disables the port to protect the network.
```

That is why controlled interface activation matters.

### STP Orange State

When router connects to switch in Packet Tracer, the switch link may show orange before turning green.

That is often STP:

```text
Spanning Tree Protocol
```

STP prevents Layer 2 loops.

It may briefly listen/learn before forwarding traffic.

Do not assume orange immediately means broken.

It may mean:

```text
The switch is checking the path before forwarding.
```

### Why Managed Switches Matter

Managed switches support protections like STP.

Cheap unmanaged switches often lack visibility and control.

Risks of unmanaged switches in business networks:

- loops;
- unknown devices;
- no port visibility;
- hard troubleshooting;
- unexpected broadcast storms;
- unstable phones/POS/Wi-Fi.

At NetworkChuck Coffee, a random unmanaged switch under a counter can create a lot of trouble.

Use managed infrastructure where operations matter.

### Verify Router Interface

After configuration:

```text
show ip interface brief
```

Look for:

```text
Status:   up
Protocol: up
IP:       correct
```

Example:

```text
GigabitEthernet0/0/0   192.168.0.1   YES manual up   up
```

If it is still administratively down:

```text
no shutdown
```

If status is down/down:

- check cable;
- check other side;
- check module;
- check switch port;
- check physical connection.

### Use CDP To Discover Neighbors

CDP stands for:

```text
Cisco Discovery Protocol
```

It helps discover directly connected Cisco devices.

Useful command:

```text
show cdp neighbors
```

More detail:

```text
show cdp neighbors detail
```

CDP can show:

- neighbor device ID;
- local interface;
- neighbor interface;
- platform;
- capabilities;
- IP address in detailed output.

This is useful when diagrams are missing or outdated.

### LLDP

LLDP stands for:

```text
Link Layer Discovery Protocol
```

LLDP is vendor-neutral and more open than CDP.

In mixed-vendor networks, LLDP is often the better discovery protocol.

Memory:

```text
CDP = Cisco
LLDP = open standard
```

### Speed And Duplex On Router Interfaces

Routers also have speed/duplex settings on Ethernet interfaces.

But on modern Gigabit Ethernet and faster links, auto-negotiation is usually preferred unless there is a specific reason.

Hardcoding can help when required, but it can also create mismatch if one side is wrong.

Rule:

```text
If you hardcode one side, make sure the other side matches.
```

When in doubt, verify with:

```text
show interface
```

## Example Configuration

### Base Config

```text
enable
configure terminal
hostname Cafe01-RT01
enable secret cisco123
line console 0
password cisco123
login
line vty 0 4
password cisco123
login
service password-encryption
end
copy running-config startup-config
```

### Router Interface

```text
configure terminal
interface GigabitEthernet0/0/0
description Link to Cafe01-SW01
ip address 192.168.0.1 255.255.255.0
no shutdown
end
```

### Verification

```text
show ip interface brief
show interface GigabitEthernet0/0/0
show cdp neighbors
show cdp neighbors detail
```

### Ping Test

If switch management IP is:

```text
192.168.0.2
```

Router can test:

```text
ping 192.168.0.2
```

If ping works:

- Layer 1 is working;
- Layer 2 local connectivity is working;
- IP addressing is likely correct for that segment.

## Troubleshooting Checklist

If router interface does not work:

- check `show ip interface brief`;
- check for `administratively down`;
- apply `no shutdown` if needed;
- verify IP address and subnet mask;
- check cable;
- check switch port status;
- check STP transition if connected to switch;
- check speed/duplex;
- inspect `show interface`;
- verify neighbor with CDP/LLDP;
- ping directly connected device.

## Quick Self-Check

### Question 1

What is the key default behavior of many router interfaces?

Answer:

```text
They are administratively down by default.
```

### Question 2

What command enables a shutdown interface?

Answer:

```text
no shutdown
```

### Question 3

What command quickly shows router interface names, IPs and status?

Answer:

```text
show ip interface brief
```

### Question 4

Why can router interface names have multiple slashes?

Answer:

```text
They can reflect modular hardware layout: slot/module/submodule/port.
```

### Question 5

What does CDP help with?

Answer:

```text
Discovering directly connected Cisco neighbor devices.
```

## Commands / Terms

| Command / Term | Meaning |
| --- | --- |
| `administratively down` | Interface is disabled by configuration. |
| `no shutdown` | Enables an interface. |
| `shutdown` | Disables an interface. |
| `show ip interface brief` | Quick view of interface IP addresses and status. |
| `show interface` | Detailed interface information and counters. |
| `show cdp neighbors` | Shows directly connected Cisco neighbors. |
| `show cdp neighbors detail` | Shows more details, often including neighbor IP. |
| CDP | Cisco Discovery Protocol. |
| LLDP | Link Layer Discovery Protocol, vendor-neutral discovery. |
| STP | Spanning Tree Protocol, Layer 2 loop prevention. |
| SVI | Switch Virtual Interface. |

## What To Review Later

- Router interface IP configuration
- Static routing
- Default gateway
- CDP and LLDP
- STP basics
- Speed/duplex troubleshooting
- Managed vs unmanaged switches
- Packet Tracer router modules

