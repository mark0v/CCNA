# IPv6, The Someday Protocol

Source: closed course page  
Date added: 2026-07-18  
Related plan item: Week 12 / IPv6, the someday protocol  
Tags: IPv6, IPv4 exhaustion, address space, carriers, NAT, CGNAT, subnetting, /64
Language: English
Translation pair: articles/2026-07/week-12/04-ipv6-the-someday-protocol.md

## Summary

- IPv6 was called the "someday protocol" for years because enterprise adoption moved slower than many people expected.
- Someday has arrived, but mostly through carriers, ISPs, mobile networks, and large internet services.
- The main reason IPv6 exists is public IPv4 address exhaustion.
- IPv6 uses a 128-bit address space, so address scarcity stops being the main design pressure.
- In IPv6, a common subnet size is /64: the first 64 bits for the network, the last 64 bits for the host.
- For many businesses, a full internal migration still may not have a strong business case, but engineers must be able to read and troubleshoot IPv6.

## Key Points

- IPv4 has about 4.2 billion theoretical addresses, and many are reserved or already allocated.
- Private IPv4 plus NAT delayed the pressure for ordinary businesses.
- Carriers feel IPv4 exhaustion much harder because they serve millions of customers.
- IPv6 addresses are written in hexadecimal chunks separated by colons.
- IPv6 subnetting usually prioritizes simplicity over aggressive conservation.
- Adoption can be high on the public internet even when many enterprises still feel IPv4-heavy.

## Notes

IPv6 did not fail. It arrived differently than many people expected.

The expectation was that businesses would one day rebuild internal networks, replace IPv4, and the internet would sharply become IPv6-first. Reality is different. The big push came from providers, where public IPv4 address scarcity directly blocks growth.

That is why IPv6 can feel rare inside an enterprise and normal on the public internet at the same time.

## Why IPv4 Hit The Wall

IPv4 uses a 32-bit address space. In theory, that is about 4.2 billion addresses.

The problem is that not all of those addresses are usable as public internet addresses:

- some ranges are reserved;
- some are multicast;
- some are experimental;
- many were allocated long ago;
- many sit inside organizations and providers.

So the problem is not just mathematical. We cannot freely hand out fresh public IPv4 space the way the early internet could.

For an ordinary company, this is not always immediate pain because private addressing and NAT still work. NetworkChuck Coffee can use private IPv4 internally and hide many devices behind a smaller public address footprint.

For carriers, the situation is different. If a provider serves millions of customers and devices, public IPv4 scarcity becomes a direct operational problem.

## Why Carriers Moved First

Carriers, ISPs, and mobile providers feel address pressure most strongly.

They need to connect:

- phones;
- home routers;
- tablets;
- IoT devices;
- business circuits;
- cloud-connected services;
- millions of customer sessions.

NAT helps, but NAT is also complexity. Carrier-grade NAT can stretch IPv4 further, but it adds operational overhead, troubleshooting pain, and translation state at huge scale.

IPv6 gives providers more room to grow. That is why "someday" became "right now" for them earlier than it did for many internal enterprise networks.

## The Address Space Change

IPv6 uses 128 bits instead of IPv4's 32 bits.

This is not a small increase. It is a shift from "we must conserve addresses carefully" to "we can design with breathing room."

IPv4 address:

```text
192.0.2.10
```

IPv6 address:

```text
2001:db8:1234:5678:abcd:ef01:2345:6789
```

IPv4 uses decimal octets separated by dots. IPv6 uses hexadecimal groups separated by colons.

Hexadecimal means digits `0-9` and letters `a-f`. Each IPv6 group represents 16 bits. Some people call these groups hextets, though terminology varies.

## Subnetting Feels Different

IPv4 subnetting often feels like conservation math.

You ask:

- How many hosts do I need?
- How many subnets do I need?
- Can I avoid wasting addresses?
- Where should I move the subnet boundary?

IPv6 changes the mindset. A very common LAN prefix is `/64`:

| Prefix part | Meaning |
| --- | --- |
| First 64 bits | Network prefix |
| Last 64 bits | Interface identifier / host portion |

That host space is enormous, but that is normal in IPv6.

The goal is not to squeeze every possible address into use. The goal is clean design, predictable subnetting, and enough space that address exhaustion stops driving every decision.

## Why Adoption Numbers Can Look Surprising

It can feel strange to hear that major services see a large amount of IPv6 traffic while many engineers have barely configured IPv6 inside business networks.

The reason is that adoption is not evenly distributed.

Large providers may:

- assign IPv6 to customers;
- prefer IPv6 toward major services;
- use translation at scale;
- operate dual-stack networks;
- push IPv6 in mobile and broadband environments.

From the viewpoint of a large service like a search engine, video platform, or cloud provider, traffic may arrive over IPv6 even if the user's local world still feels partly IPv4.

That is why IPv6 can be very real on the internet while still feeling optional in many smaller organizations.

## NetworkChuck Coffee Design View

Would NetworkChuck Coffee immediately re-address every internal network with IPv6? Probably not.

Good engineering still needs business justification. If the internal IPv4 design is stable, NAT works, and there is no immediate operational need, a full IPv6 internal migration may be difficult to justify.

More realistic approach:

- keep internal IPv4 working;
- support IPv6 where the ISP, cloud, or applications require it;
- understand dual stack;
- monitor IPv6 traffic if it exists;
- apply security policy to IPv6 too;
- prepare engineers to troubleshoot it.

That is a practical posture: do not panic, but do not ignore it.

## Main Takeaway

IPv6 became the "someday protocol" because enterprise urgency lagged behind the predictions.

But carriers and public internet services had a different reality. They felt IPv4 exhaustion first, and they moved. That is why IPv6 is already a real part of modern internet traffic, even if many internal business networks still look mostly IPv4.

Learn IPv6 now so it is not unfamiliar when it appears in routing, DNS, firewall rules, packet captures, or cloud deployments.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| IPv4 exhaustion | Shortage of broadly available public IPv4 address space. |
| IPv6 | 128-bit successor to IPv4 with much larger address space. |
| NAT | Network Address Translation, commonly used to share public IPv4 addresses. |
| CGNAT | Carrier-grade NAT, large-scale NAT used by providers. |
| Hexadecimal | Base-16 notation using `0-9` and `a-f`. |
| Hextet | Informal term for a 16-bit IPv6 address group. |
| `/64` | Common IPv6 LAN prefix size. |
| Dual stack | IPv4 and IPv6 running side by side. |

## Questions

### 1. Why did IPv6 get called the "someday protocol"?

Answer: Because people expected fast adoption for years, but many enterprises kept running mostly IPv4 much longer than predicted.

### 2. Who felt IPv4 exhaustion first?

Answer: Carriers, ISPs, and mobile providers, because they need addresses for massive numbers of customers and devices.

### 3. Why did NAT delay IPv6 adoption for many businesses?

Answer: NAT lets many internal private IPv4 devices share a smaller number of public IPv4 addresses.

### 4. What is the common IPv6 LAN prefix size?

Answer: `/64`, with 64 bits for the network prefix and 64 bits for the host/interface portion.

### 5. Should every business immediately replace internal IPv4 with IPv6?

Answer: Not necessarily. The practical approach is to support IPv6 where it makes sense, understand it, secure it, and be ready to troubleshoot it.

## What To Review Later

- IPv6 address format and hexadecimal notation.
- IPv6 address compression rules.
- `/64` prefix design.
- NAT vs CGNAT.
- Dual-stack deployment.
- IPv6 security visibility.
