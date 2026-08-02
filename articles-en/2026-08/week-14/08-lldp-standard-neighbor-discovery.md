# LLDP Standard Neighbor Discovery

Source: closed course page  
Date added: 2026-08-02  
Related plan item: Week 14 / LLDP standard neighbor discovery  
Tags: LLDP, CDP, Link Layer Discovery Protocol, neighbor discovery, mixed-vendor network, troubleshooting, switch operations
Language: English
Translation pair: articles/2026-08/week-14/08-lldp-standard-neighbor-discovery.md

## Summary

- LLDP is the standards-based Layer 2 neighbor discovery protocol.
- It solves almost the same problem as CDP, but it is not tied to Cisco.
- LLDP is especially useful in mixed-vendor networks.
- On many Cisco devices, LLDP is not enabled by default.
- Main commands are `lldp run`, `show lldp neighbors`, and `show lldp neighbors detail`.
- On an interface, LLDP transmit and receive can be controlled separately.
- That gives more control between visibility and security.

## Key Points

- CDP is convenient in Cisco environments, while LLDP matters where different vendors exist.
- A discovery protocol shows directly connected neighbors, not the whole network at once.
- If LLDP is disabled, it will not help during urgent troubleshooting.
- Enabling LLDP should be part of the standard for networks with mixed-vendor equipment.
- Directional control lets you enable receive and transmit separately.
- On user-facing ports, think carefully about what discovery information should be exposed.

## Notes

LLDP, or Link Layer Discovery Protocol, can be understood as the standards-based version of the same idea Cisco implements with CDP.

The task is the same:

```text
Show which device is directly connected to this port.
```

The difference is reach. CDP is Cisco-proprietary. LLDP is an industry standard. That makes it better for networks where Cisco, HPE, Aruba, Juniper, Linux systems, hypervisors, IP phones, wireless access points, and other devices sit next to each other.

## Why LLDP Matters

Real networks do not always use one vendor.

A large enterprise may standardize everything on Cisco. But in midsize companies, branches, and networks that grew organically, mixed equipment is common:

- Cisco switches;
- HPE or Aruba switches;
- Ubiquiti access points;
- Linux servers;
- IP phones from another vendor;
- firewalls from another platform.

If you rely only on CDP, some neighbors may be invisible. LLDP gives different devices a shared discovery language.

For NetworkChuck Coffee, that is practical. Today the main location might use Cisco. Tomorrow a new branch may use more budget-friendly hardware. Discovery still matters.

## The Main Catch

LLDP has one important catch: on many Cisco devices, it is not enabled by default.

That helps explain why CDP appears so often in real Cisco environments. When the network is poorly documented, discovery is needed immediately. But a disabled feature cannot help.

So in mixed-vendor environments, you need to know LLDP and make enabling it part of the standard.

Command:

```text
lldp run
```

Then view neighbors:

```text
show lldp neighbors
show lldp neighbors detail
```

## What LLDP Shows

The output is similar to CDP.

You can usually see:

- neighbor device;
- local interface;
- remote port;
- capabilities;
- platform or system description;
- management address;
- additional operational details.

Detailed output is especially useful when you need to move to the neighboring device or identify exactly what is connected to a port.

Example workflow:

```text
show lldp neighbors detail
record neighbor and port
compare with documentation
move to the next device
update topology notes
```

## Directional Control

One strength of LLDP is directional control on an interface.

You can separately allow:

- receiving LLDP information;
- transmitting LLDP information;
- both directions;
- neither direction.

Example:

```text
interface fa0/10
 no lldp transmit
 lldp receive
```

Or disable both on a port:

```text
interface fa0/10
 no lldp transmit
 no lldp receive
```

This is useful when you want to listen to information from a connected device without advertising switch details back out of the port.

## Visibility And Security

Discovery information is useful to administrators, but it can help attackers too.

LLDP can reveal:

- device name;
- system description;
- platform;
- capabilities;
- management address;
- port details;
- sometimes VLAN-related data.

So a good policy is not simply "enable everywhere" or "disable everywhere."

A practical policy:

- enable LLDP between network devices;
- use it where phones, access points, or mixed-vendor links need it;
- limit transmit on ports facing untrusted endpoints;
- document exceptions.

## CDP Comparison

| Property | CDP | LLDP |
| --- | --- | --- |
| Type | Cisco-proprietary | Open standard |
| Environment | Cisco-heavy | Mixed-vendor |
| Default on Cisco | Often enabled | Often disabled |
| Enable command | `cdp run` | `lldp run` |
| Neighbor view | `show cdp neighbors` | `show lldp neighbors` |
| Directional control | Less granular | Separate transmit/receive |

Both protocols are useful. The difference is not the basic idea; it is interoperability and control.

## Verification

Useful commands:

```text
show lldp
show lldp neighbors
show lldp neighbors detail
show lldp interface
show running-config | include lldp
```

Check:

- whether LLDP is enabled globally;
- which interfaces transmit;
- which interfaces receive;
- whether expected neighbors are visible;
- whether unexpected neighbors appear;
- whether information is exposed on unnecessary user-facing ports.

## NetworkChuck Coffee Scenario

NetworkChuck Coffee opens a new branch. Some equipment is Cisco, and some comes from another vendor.

If only CDP is enabled, the administrator may not see every neighbor. If LLDP is enabled, there is a shared discovery layer.

That makes it faster to identify:

- which switch connects to the router;
- where the access point is;
- which ports go to phones;
- which devices do not match documentation;
- where the topology map needs updates.

This does not make the network perfect, but it gives a fast way to see reality.

## Main Takeaway

LLDP is the standard discovery option for networks where Cisco is not the only participant.

It is similar to CDP in purpose, but broader in application. Its main risk is forgetting to enable it where it is needed. Its main strength is interoperability and precise transmit/receive control on interfaces.

If the network is mixed-vendor, LLDP should be part of the operational baseline.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| LLDP | Link Layer Discovery Protocol, standards-based neighbor discovery protocol. |
| CDP | Cisco Discovery Protocol, Cisco's discovery protocol. |
| `lldp run` | Enables LLDP globally. |
| `show lldp neighbors` | Shows a brief list of LLDP neighbors. |
| `show lldp neighbors detail` | Shows detailed neighbor information. |
| transmit | Sending LLDP information from a port. |
| receive | Receiving LLDP information on a port. |
| mixed-vendor network | Network with equipment from multiple manufacturers. |
| management address | Address used to manage a neighboring device. |

## Questions

### 1. Why use LLDP?

Answer: To discover directly connected neighbors in networks with different vendors.

### 2. How is LLDP different from CDP?

Answer: LLDP is a standards-based vendor-neutral protocol, while CDP is Cisco-proprietary.

### 3. Why might LLDP not help during urgent troubleshooting?

Answer: On many Cisco devices, it is not enabled by default.

### 4. What does directional control provide in LLDP?

Answer: The ability to separately allow LLDP transmit and receive on an interface.

### 5. Why should LLDP be configured intentionally?

Answer: It helps administrators, but it can expose topology and management information to untrusted devices.

## What To Review Later

- `lldp run`.
- `show lldp neighbors`.
- `show lldp neighbors detail`.
- `no lldp transmit`.
- `no lldp receive`.
- Difference between CDP and LLDP.
- Discovery policy on user-facing ports.
