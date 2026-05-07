# Let's Hack Your Home Network

Source: закрытая страница курса  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 00 Lesson 09  
Tags: soho, home network, security, router hardening, iot, vlan, vpn, ids, ips

## Summary

Home network часто уязвимее, чем кажется, потому что один SOHO router обычно выполняет сразу несколько ролей: router, switch, wireless access point, firewall и internet gateway. При этом к нему подключены laptops, phones, TVs, IoT devices и иногда work devices. Статья объясняет основные зоны риска и показывает, как уменьшить attack surface: закрыть ненужные services, обновить firmware, усилить Wi-Fi, изолировать IoT и использовать VPN.

Главная мысль статьи: домашняя сеть, особенно при remote work, становится маленьким branch office. Ее нужно проектировать и защищать осознанно.

## Key Points

- SOHO means Small Office / Home Office.
- Home all-in-one router часто совмещает router, switch, WAP, firewall и gateway.
- Основные risk areas: internet exposure, internal weak devices, wireless security, remote work access.
- Public IP address делает home router видимым для internet.
- Open ports снаружи могут быть dangerous, особенно Remote Desktop и старые services.
- Router hardening начинается с firewall, disabling unnecessary port forwarding, disabling remote management и смены default admin credentials.
- Firmware updates важны, потому что часто закрывают vulnerabilities.
- Wi-Fi должен использовать WPA2 минимум, WPA3 лучше.
- Default SSID может раскрывать router vendor/model.
- Router лучше настроить так, чтобы он не отвечал на WAN pings, если это возможно.
- IoT devices опасны, потому что могут делать outbound connections и стать internal weak link.
- Segmentation разделяет trusted devices, IoT и guests.
- VLANs и client isolation помогают ограничить lateral movement.
- IDS/IPS помогают detect/prevent known threats.
- Для remote work и external access лучше использовать VPN, а не random port forwards.

## Notes

### Your Home Network Is a SOHO Network

SOHO network - это Small Office / Home Office network.

В такой сети один device часто делает почти всё:

- router;
- wireless access point;
- switch;
- firewall;
- internet gateway.

Проблема в том, что к этому device подключается много разных endpoints:

- laptops;
- phones;
- tablets;
- TVs;
- smart speakers;
- cameras;
- light bulbs;
- work devices;
- IoT devices.

Чем больше разных devices, тем больше risk.

### Home Network as a Tiny Branch Office

Если человек работает удаленно, home network становится частью business security story.

Для NetworkChuck Coffee похожая проблема была бы в small office location:

- guest Wi-Fi;
- POS tablets;
- cameras;
- office systems;
- employee laptops.

Если всё это висит на одном flat underprotected network, компрометация одного device может стать проблемой для остальных.

Практическая идея:

```text
Same concept, smaller scale, still dangerous.
```

### Four Risk Areas

Статья делит home network risks на четыре области:

| Area | Question |
| --- | --- |
| Internet exposure | Can someone attack from the internet? |
| Internal weak devices | Can an internal device become the weak link? |
| Wireless security | Is Wi-Fi easy to abuse? |
| Remote work access | How do you connect back to company resources? |

Такой подход помогает не думать о security хаотично, а смотреть по категориям.

### Public IP and Open Ports

ISP дает router public IP address. Это address, который visible from internet.

Если кто-то знает этот public IP, он может probe/scanning services and ports. Цель такого сканирования - найти exposed services или old vulnerabilities.

Open ports могут быть legitimate, но dangerous, если они не нужны или плохо защищены.

Особенно опасные примеры:

- Remote Desktop open to internet;
- outdated services;
- unknown port forwards;
- remote management interface;
- exposed admin panels.

### Scanning From Outside

Чтобы понять, что internet видит снаружи, проверку нужно делать не изнутри собственной LAN.

Правильнее использовать:

- another network;
- cloud server;
- external scanning service.

Цель:

```text
See what the internet sees.
```

Если найден unknown open port, лучше сначала закрыть его, а потом разбираться, что могло зависеть от него.

### Router Hardening Checklist

Во многих случаях existing router можно сделать safer без покупки нового hardware.

Basic hardening:

- enable firewall;
- disable unnecessary port forwarding;
- disable remote management from internet;
- change default admin username/password;
- install firmware updates;
- use strong Wi-Fi encryption;
- change default SSID;
- use long strong Wi-Fi password;
- disable WAN ping response if possible.

Это не делает network perfect, но сильно уменьшает obvious risk.

### Firmware Updates

Firmware - это operating system router.

Vendor updates могут содержать:

- bug fixes;
- feature updates;
- security patches;
- vulnerability fixes.

Если vulnerability patched by vendor, но router не обновлен, network остается exposed.

### Wi-Fi Security

Wireless needs attention.

Minimum recommendation:

```text
WPA2 minimum, WPA3 if supported.
```

Default SSID лучше заменить, потому что он может reveal router brand/model. Это помогает attacker искать known vulnerabilities для конкретного device.

Wi-Fi password должен быть long and strong.

### WAN Ping Response

Ping - это простой “are you there?” message.

Если router отвечает на pings from internet, scanners легче обнаруживают active target.

Если router поддерживает настройку:

```text
Disable response to WAN pings.
```

Идея: быть boring and quiet from the outside.

### IoT as Internal Risk

IoT means Internet of Things.

Examples:

- smart bulbs;
- cameras;
- smart TVs;
- doorbells;
- voice assistants;
- smart plugs;
- appliances.

IoT devices часто делают outbound connections. Firewall usually allows outbound traffic, потому что device сам начал conversation.

Risk:

```text
Threat may not break in from outside.
Threat may already be inside and call out.
```

Если compromised IoT device находится в одной flat network с laptop или NAS, он может стать foothold для lateral movement.

### Segmentation

Segmentation - это разделение devices на separate networks.

Пример:

| Segment | Devices |
| --- | --- |
| Trusted | Laptops, phones, tablets |
| IoT | Cameras, bulbs, smart speakers, TVs |
| Guest | Visitor devices |
| Work | Company laptop or work resources |

Главная цель:

```text
One compromised smart device should not reach everything else.
```

### VLANs and Client Isolation

VLANs provide virtual network separation on shared physical infrastructure.

Если home/prosumer gear поддерживает VLANs, можно разделить trusted devices, IoT и guest network.

Client isolation - настройка, которая запрещает devices на same wireless network говорить друг с другом напрямую.

Client isolation особенно полезен для:

- guest Wi-Fi;
- IoT Wi-Fi;
- untrusted devices.

### When Basic Gear Is Not Enough

Если current router не поддерживает нужные security features, может понадобиться upgrade.

Варианты:

- custom firmware like DD-WRT, if supported;
- prosumer gear;
- enterprise-style gear;
- platforms like Cisco, UniFi, pfSense.

Better gear can provide:

- better firewall policies;
- VLAN support;
- traffic visibility;
- VPN options;
- IDS/IPS;
- better logs and monitoring.

### IDS and IPS

IDS stands for Intrusion Detection System.

IPS stands for Intrusion Prevention System.

| System | Role |
| --- | --- |
| IDS | Detect suspicious/known threat traffic |
| IPS | Detect and block/prevent threat traffic |

IDS/IPS helps move from “I hope I am safe” to “I am actively watching my network.”

### Working From Home and VPNs

Remote work changes home network risk.

VPN, Virtual Private Network, creates encrypted tunnel between user and another network, usually company network.

Common VPN types:

| Type | Meaning |
| --- | --- |
| Remote access VPN | Software on laptop connects user to company network |
| Site-to-site VPN | Firewall/router creates persistent tunnel between home/site and office |

VPN protects company traffic and provides safer access to company resources.

### External Access to Home Resources

Если нужен access to home resources from outside, случайные port forwards - плохой подход.

Better approach:

```text
Use your own VPN back into the home network.
```

Это safer than exposing services directly to internet.

### Main Takeaway

Home network security plan:

1. Scan/check what is exposed externally.
2. Harden the router.
3. Secure wireless.
4. Update firmware.
5. Isolate untrusted/IoT devices.
6. Upgrade gear if needed.
7. Use VPN for remote work or external access.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| SOHO | Small Office / Home Office network. |
| Public IP address | Internet-visible address assigned by ISP. |
| Open port | Network port accepting traffic from outside or inside. |
| Port forwarding | Router rule forwarding external traffic to internal device/service. |
| Remote management | Ability to administer router from outside network; risky if exposed. |
| Firmware | Router/device operating system. |
| SSID | Wi-Fi network name. |
| WPA2 | Common Wi-Fi security standard; minimum recommended here. |
| WPA3 | Newer Wi-Fi security standard. |
| WAN ping | Ping request from internet/WAN side. |
| IoT | Internet of Things; smart connected devices. |
| Segmentation | Splitting devices into separate networks/security zones. |
| VLAN | Virtual LAN; logical network separation. |
| Client isolation | Preventing wireless clients from talking directly to each other. |
| DD-WRT | Custom router firmware for supported devices. |
| IDS | Intrusion Detection System. |
| IPS | Intrusion Prevention System. |
| VPN | Virtual Private Network; encrypted tunnel between networks/devices. |
| Remote access VPN | User device connects into company/home network via VPN client. |
| Site-to-site VPN | Persistent VPN tunnel between two networks. |
| Nmap | Tool used to scan networks/hosts for open ports and services. |

## Questions

### 1. Что означает SOHO?

SOHO means Small Office / Home Office.

### 2. Почему home router является важной security точкой?

Потому что он часто выполняет роли router, switch, wireless access point, firewall и internet gateway одновременно.

### 3. Какие четыре risk areas выделяет статья?

Internet exposure, internal weak devices, wireless security и remote work access.

### 4. Почему public IP address важен для security?

Это address, по которому internet видит router. Через него external scanners могут искать open ports и exposed services.

### 5. Что нужно сделать с unknown open ports?

Их лучше закрыть сразу, а затем выяснять, какой service мог от них зависеть.

### 6. Какие basic router hardening steps стоит выполнить?

Enable firewall, disable unnecessary port forwarding, disable remote management, change default admin credentials, update firmware, secure Wi-Fi.

### 7. Почему важно обновлять firmware?

Firmware updates часто закрывают vulnerabilities. Без update router может оставаться exposed.

### 8. Почему default SSID лучше изменить?

Default SSID может reveal router brand/model, что помогает attacker искать known vulnerabilities.

### 9. Почему IoT devices опасны?

Они могут быть poorly secured, делать outbound connections и стать internal weak link inside the network.

### 10. Что такое segmentation?

Segmentation - это разделение devices на separate networks, чтобы compromised device не имел direct access ко всему остальному.

### 11. Чем VLAN помогает дома?

VLAN позволяет логически разделить trusted devices, IoT и guests на shared infrastructure.

### 12. Что делает client isolation?

Client isolation prevents devices on same wireless network from talking directly to each other.

### 13. Чем IDS отличается от IPS?

IDS detects suspicious traffic, IPS can detect and block/prevent threats.

### 14. Почему для доступа домой извне лучше VPN, а не random port forwards?

VPN создает encrypted controlled access, а port forwards напрямую expose internal services to internet.

### 15. Почему remote work делает home network частью company security story?

Потому что company resources accessed from home depend on the security of that home connection and device environment.

## What To Review Later

- SOHO network risks.
- Public IP, open ports and port forwarding.
- Router hardening checklist.
- WPA2/WPA3 and SSID hygiene.
- WAN ping response.
- IoT threat model.
- Segmentation, VLANs and client isolation.
- IDS vs IPS.
- Remote access VPN vs site-to-site VPN.
