# Let's Hack Your Home Network

Source: private course page  
Date added: 2026-05-07  
Related plan item: Week 1 / Skill 00 Lesson 09  
Tags: soho, home network, security, router hardening, iot, vlan, vpn, ids, ips

## Summary

Home networks are often more vulnerable than they look because a single SOHO router usually combines router, switch, access point, firewall and internet gateway roles. Laptops, phones, TVs, IoT devices and work devices all connect to it.

Main idea: a home network, especially for remote work, is basically a tiny branch office and should be secured intentionally.

## Key Points

- SOHO means Small Office / Home Office.
- Home all-in-one routers combine many roles.
- Main risks include internet exposure, weak internal devices, wireless abuse and remote work access.
- A public IP makes the home router visible from the internet.
- Unnecessary port forwards increase attack surface.
- Remote management from the WAN should usually be disabled.
- Default admin credentials must be changed.
- Firmware updates close known vulnerabilities.
- WPA2 is a minimum; WPA3 is better when available.
- IoT devices should be isolated when possible.
- VLANs and guest networks help segmentation.
- VPN is cleaner than random port forwarding for remote access.

## Notes

### SOHO Risk

A home router often handles:

- routing;
- switching;
- WiFi;
- firewalling;
- internet gateway;
- sometimes VPN or parental controls.

That is a lot of trust in one small box.

### Four Risk Areas

Useful checklist:

```text
Internet exposure
Internal weak devices
Wireless security
Remote work access
```

### Hardening Steps

Start with basics:

- change default admin password;
- update firmware;
- disable unused port forwards;
- disable WAN remote management;
- use strong WiFi security;
- isolate guests and IoT;
- use VPN for remote access.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| SOHO | Small Office / Home Office. |
| Public IP | Internet-facing address. |
| Port forwarding | Exposing internal services through the router. |
| VLAN | Logical segmentation inside a network. |
| VPN | Encrypted tunnel for remote access. |

## Questions

### Why is a home network a security concern?

It contains many devices and often depends on one underprotected all-in-one router.

### Why avoid random port forwards?

They expose internal services to the internet and increase risk.

## What To Review Later

- Router hardening.
- WPA2/WPA3.
- VLANs.
- IDS/IPS.
- Home VPN access.
