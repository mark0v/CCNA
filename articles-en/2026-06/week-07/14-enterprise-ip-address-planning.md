# Enterprise IP Address Planning: Castle Rysen Coffee

Source: closed course page  
Date added: 2026-06-13  
Related plan item: Week 7 / Enterprise IP address planning  
Tags: IPv4, VLSM, address planning, enterprise design, route summarization, RFC 1918, growth
Language: English
Translation pair: articles/2026-06/week-07/14-enterprise-ip-address-planning.md

## Summary

A real IP address plan is not sized only by current employee count. It accounts for:

- user and corporate devices;
- servers and virtual infrastructure;
- Wi-Fi, cameras and access control;
- management networks;
- growth;
- geography and organizational structure;
- route summarization;
- operational simplicity.

Castle Rysen Coffee uses private block `10.0.0.0/8` and this hierarchy:

```text
Central Office:       10.0.0.0/20
Regional Group 1:     10.0.16.0/20
Regional Group 2:     10.0.32.0/20
...
```

Every regional `/20` contains:

- one shelter `/23`;
- up to 50 district shops `/26`;
- reserve for infrastructure, links and growth.

## Key Points

- Headcount is not the same as IP-address count.
- Translate business requirements into device and service requirements.
- Site blocks are often larger than current individual VLANs.
- Hierarchical plans reflect geography and ownership.
- Contiguous allocations simplify route summarization.
- Reserved space is part of a design, not necessarily waste.
- Every summary block must be aligned.
- Detailed site subnets can change without changing the global plan.
- IPAM and documentation are essential.

## From Headcount To Device Count

One person can use:

- laptop;
- phone;
- tablet;
- wearable;
- virtual desktop;
- wired and wireless interfaces.

Addresses are also required for:

- access points;
- switches;
- routers;
- firewalls;
- printers;
- cameras;
- badge readers;
- door controllers;
- POS terminals;
- servers;
- hypervisors;
- management interfaces;
- load balancers;
- monitoring;
- temporary and guest devices.

Therefore:

```text
200 people != 200 IP addresses
```

## Discovery Before Calculation

Before selecting prefixes, gather:

1. Site types and site counts.
2. Current endpoints by category.
3. Growth forecast.
4. Infrastructure and redundancy.
5. VLAN and security-zone requirements.
6. WAN topology.
7. Cloud, VPN and partner ranges.
8. Existing overlaps.
9. Summarization boundaries.
10. Operational ownership.

Record unknown assumptions explicitly.

## Choosing Private Space

RFC 1918 defines:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

For a large growing organization, `10.0.0.0/8` provides convenient space for hierarchical planning.

This does not mean using the whole `/8` as one subnet. It is a parent allocation for many smaller prefixes.

Check for overlap with:

- mergers and acquisitions;
- VPN partners;
- cloud VNets or VPCs;
- remote workers;
- lab environments.

## Castle Rysen Coffee Requirements

Example assumptions:

| Site type | Count | Planning capacity |
| --- | ---: | ---: |
| Central Office | 1 | about 4,000 addresses |
| Fallout Shelter | 30 | about 500 addresses each |
| District Shop per Shelter | up to 50 | about 50 addresses each |

Planning capacity does not imply one broadcast domain. It is a site allocation later divided into VLANs with VLSM.

## Central Office

For approximately 4,000 addresses:

```text
2^11 = 2048   insufficient
2^12 = 4096   sufficient
```

Site block:

```text
10.0.0.0/20
```

Range:

```text
Network:   10.0.0.0
Last:      10.0.15.255
Addresses: 4096
```

This `/20` should not automatically become one VLAN. It can be divided into:

- employee VLANs;
- voice;
- wireless;
- servers;
- management;
- cameras;
- guest;
- infrastructure.

## Regional-Group Size

One regional group contains:

```text
1 shelter
50 district shops
```

### Shelter

For about 500 addresses:

```text
/23 = 512 total, 510 traditional usable
```

### District Shop

For about 50 addresses:

```text
/26 = 64 total, 62 traditional usable
```

### Raw Capacity

```text
Shelter:        1 * 512 = 512
District shops: 50 * 64 = 3200
Total used:               3712
```

The next power-of-two block is:

```text
4096 addresses = /20
```

Allocate one regional `/20` to every shelter and its shops.

## Why `/20` Beats Exact Packing

A regional `/20` provides:

```text
4096 addresses
```

Current plan usage:

```text
3712 addresses
```

Reserve:

```text
4096 - 3712 = 384 addresses
```

Possible uses:

- WAN or transit links;
- management;
- regional services;
- additional shops;
- growth;
- migration overlap;
- future VLANs.

The main benefit is:

```text
One regional group = one clean /20 summary
```

## Regional Group 1

Summary:

```text
10.0.16.0/20
```

Range:

```text
10.0.16.0 - 10.0.31.255
```

### Shelter 1

```text
10.0.16.0/23
```

Range:

```text
10.0.16.0 - 10.0.17.255
```

### Shops 1 Through 50

First shop:

```text
10.0.18.0/26
```

Every following `/26` advances by 64 addresses.

| Shop | Network |
| ---: | --- |
| 1 | `10.0.18.0/26` |
| 2 | `10.0.18.64/26` |
| 3 | `10.0.18.128/26` |
| 4 | `10.0.18.192/26` |
| 5 | `10.0.19.0/26` |
| ... | ... |
| 49 | `10.0.30.0/26` |
| 50 | `10.0.30.64/26` |

The final shop occupies:

```text
10.0.30.64 - 10.0.30.127
```

### Reserved Space

Free inside the regional `/20`:

```text
10.0.30.128 - 10.0.31.255
```

CIDR decomposition:

```text
10.0.30.128/25
10.0.31.0/24
```

This reserve lets the next regional group begin at a clean boundary:

```text
10.0.32.0/20
```

## Regional Pattern

The third-octet increment for `/20` is:

```text
16
```

First groups:

| Group | Summary |
| ---: | --- |
| Central Office | `10.0.0.0/20` |
| Regional 1 | `10.0.16.0/20` |
| Regional 2 | `10.0.32.0/20` |
| Regional 3 | `10.0.48.0/20` |
| Regional 4 | `10.0.64.0/20` |
| ... | ... |
| Regional 15 | `10.0.240.0/20` |
| Regional 16 | `10.1.0.0/20` |

After `10.0.240.0/20`, the third octet rolls over into the second.

With 30 regional groups, the final group is:

```text
Regional 30 = 10.1.224.0/20
```

## Overall Parent For Phase One

Central `/20` plus 30 regional `/20` blocks:

```text
31 * 4096 = 126,976 addresses
```

Aligned parent:

```text
10.0.0.0/15
```

Range:

```text
10.0.0.0 - 10.1.255.255
```

After allocation through `10.1.239.255`, this remains:

```text
10.1.240.0/20
```

inside the `/15`.

This does not mean the enterprise must advertise `/15` everywhere. Summary design depends on topology and failure domains.

## Hierarchical Addressing

A good scheme encodes structure:

```text
Enterprise
  -> Region
    -> Site
      -> VLAN / function
```

Benefits:

- routes are easier to read;
- ownership is easier to delegate;
- prefixes aggregate cleanly;
- incidents are easier to localize;
- expansion follows a repeatable pattern;
- site redesign does not break the global hierarchy.

## Dividing Site Blocks Internally

A site allocation is a container, not one subnet.

Example Central Office `/20`:

| Function | Example prefix |
| --- | --- |
| Employees | `/22` |
| Guest | `/22` |
| Servers | `/23` |
| Voice | `/23` |
| Cameras | `/24` |
| Management | `/24` |
| Infrastructure | `/25` |
| Reserve | remaining aligned blocks |

Actual sizes come from discovery, not this illustrative table.

## Route Summarization

Regional group 1 can contain many routes:

```text
10.0.16.0/23
10.0.18.0/26
10.0.18.64/26
...
10.0.30.64/26
```

At the regional boundary, they can be summarized as:

```text
10.0.16.0/20
```

only when:

- every covered route is behind that region;
- no more-specific route uses another path;
- the summary does not create an unmanaged black hole;
- failure behavior is understood.

## Re-addressing As A Project

Renumbering affects:

- DHCP scopes;
- static devices;
- router interfaces;
- firewall rules and objects;
- ACLs;
- NAT;
- DNS;
- monitoring;
- certificates and allowlists;
- VPN selectors;
- routing;
- documentation;
- application dependencies.

It is a migration program, not only a subnet calculation.

## Migration Phases

### 1. Discovery

- inventory addresses;
- identify owners;
- find static assignments;
- map VLANs and routes;
- detect overlaps;
- baseline traffic.

### 2. Design

- approve hierarchy;
- size site containers;
- assign VLAN prefixes;
- plan summaries;
- define naming and IPAM fields.

### 3. Validation

- model in a lab;
- validate routing;
- test DHCP, DNS, NAT and security policy;
- confirm rollback.

### 4. Pilot

- migrate a low-risk site;
- measure outages;
- update the runbook;
- resolve hidden dependencies.

### 5. Rollout

- migrate by region or site;
- use change windows;
- verify after every stage;
- retire old routes deliberately.

### 6. Closeout

- remove temporary configuration;
- reconcile IPAM;
- update diagrams;
- capture lessons learned.

## Cutover Checklist

- [ ] New VLANs and SVIs configured.
- [ ] DHCP scopes created and exclusions correct.
- [ ] Routing and summaries staged.
- [ ] Firewall, ACL and NAT updated.
- [ ] DNS changes prepared.
- [ ] Static devices mapped.
- [ ] Monitoring accepts new ranges.
- [ ] Remote access path preserved.
- [ ] Rollback commands tested.
- [ ] Old/new coexistence understood.
- [ ] Post-change tests assigned.

## Address-Plan Validation

For every allocation:

- correct network boundary;
- sufficient capacity;
- no overlap;
- contained in parent;
- gateway reserved;
- DHCP range documented;
- growth reserve;
- summary relationship;
- owner and purpose;
- lifecycle status.

## Automated Verification

Python can verify the regional pattern:

```python
from ipaddress import ip_network

enterprise = ip_network("10.0.0.0/15")
groups = list(enterprise.subnets(new_prefix=20))

central = groups[0]
regions = groups[1:31]

print(central)
print(regions[0])
print(regions[-1])
```

Expected:

```text
10.0.0.0/20
10.0.16.0/20
10.1.224.0/20
```

## Practice

A new region needs:

- one hub for 900 addresses;
- 20 branches with 100 addresses each;
- 40 kiosks with 25 addresses each;
- 20 WAN links with 2 addresses each;
- at least 20% address reserve.

Tasks:

1. Select prefixes.
2. Calculate the raw total.
3. Choose an aligned regional container.
4. Propose a largest-first allocation.
5. Determine the summary.

### Possible Answer

```text
Hub:      /22 = 1024 addresses
Branches: /25 = 128 each -> 2560
Kiosks:   /27 = 32 each  -> 1280
WAN:      /30 = 4 each   -> 80
Raw total: 4944
```

With 20% reserve:

```text
4944 * 1.2 = 5932.8
```

The next power-of-two container is:

```text
8192 addresses = /19
```

The specific allocation must start on a `/19` boundary and be checked for fragmentation.

## Common Mistakes

### Counting People Instead Of Devices

Headcount informs discovery but is not final capacity.

### Making A Site Allocation One VLAN

A container prefix is intended for further subnetting.

### Packing Without Reserve

This complicates growth and summarization.

### Reserving Without Justification

Headroom should match forecast and architecture.

### Ignoring Alignment

A convenient-looking number is not necessarily a valid boundary.

### Promising A Summary Without Topology

Aggregation must reflect real paths.

### Forgetting External Overlap

Private ranges can conflict through VPN, cloud or acquisition.

### Treating Renumbering Only As A Routing Change

Dependencies also exist in security, DNS, applications and operations.

## Quick Self-Check

### Question 1

Why do 200 employees not mean 200 addresses?

Answer:

```text
Users have multiple devices, while infrastructure and services
also consume addresses.
```

### Question 2

Which block provides about 4,000 addresses?

Answer:

```text
/20, containing 4,096 total addresses.
```

### Question 3

Why place one shelter and 50 shops in a `/20`?

Answer:

```text
Their raw blocks consume 3,712 addresses, while /20 provides 4,096,
leaving reserve and a clean summary boundary.
```

### Question 4

Where does shop 50 end when shops begin at `10.0.18.0/26`?

Answer:

```text
Shop 50 is 10.0.30.64/26 and ends at 10.0.30.127.
```

### Question 5

What allows the next group to begin at `10.0.32.0/20`?

Answer:

```text
Deliberately reserving 10.0.30.128 through 10.0.31.255
inside the first regional /20.
```

## Commands And Terms

| Term | Meaning |
| --- | --- |
| Site container | Parent prefix for a site's internal VLANs. |
| Regional block | Contiguous allocation for a region and its sites. |
| Headroom | Justified reserve for growth. |
| Hierarchical addressing | Scheme reflecting enterprise structure. |
| Summary route | Aggregate route covering contiguous child prefixes. |
| Re-addressing | Migrating existing systems to a new IP scheme. |
| IPAM | Source of truth for address allocations. |
| RFP | Document containing business and technical requirements. |

## What To Review Later

- VLSM
- Route summarization
- RFC 1918
- IPAM
- DHCP migration
- Routing design
- Renumbering runbooks
- IPv6 address planning

